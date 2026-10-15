"""Offline, fail-closed checks with proof bound to actual Git/worktree inputs."""
import argparse
import ast
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
DENIED = ('**/.env', '.env', '.env.*', '**/.env.*', '*.sqlite*', '*.db', '*.log',
          '.local/*', 'outputs/*', '*inventaire-prive*', '*review-text*', '*revue-ocr-prive*',
          '*controle-visuel-prive*', '*zotero-*-verification*', '*text-audit*', '*visual-audit*')
SECRETS = (
    re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}'),
    re.compile(r'\bgithub_pat_[A-Za-z0-9_]{30,}'),
    re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}'),
    re.compile(r'\bAKIA[A-Z0-9]{16}'),
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'(?i)(?:api[_-]?key|password|secret|token)\s*[:=]\s*[\"\x27][A-Za-z0-9_/-]{20,}[\"\x27]'),
    re.compile(r'(?i)[A-Z]:[\\/]+Users[\\/]+[^\s\"<>]+'),
)


def resolve_node(path=None, home=None, platform=sys.platform):
    """Use PATH first, then the existing Windows Codex runtime; never install anything."""
    executable = shutil.which('node', path=path)
    if executable:
        return executable
    if platform == 'win32':
        bundled = (Path(home) if home is not None else Path.home()) / '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
        if bundled.is_file():
            return str(bundled)
    return None


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.PIPE)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(data):
    """Git autocrlf may change checkout bytes; never normalize binary artifacts."""
    try:
        return data.decode('utf-8-sig').replace('\r\n', '\n').encode('utf-8')
    except UnicodeDecodeError:
        return data


def inputs(root):
    names = sorted(set(git(root, 'ls-files', '-z', '--cached', '--others', '--exclude-standard').decode().split('\0')) - {''})
    files = {}
    for name in names:
        file = root / name
        if file.is_symlink():
            raise ValueError(f'Symlink not accepted: {name}')
        if file.exists():
            if not file.is_file() or not file.resolve().is_relative_to(root.resolve()):
                raise ValueError(f'Non-regular input: {name}')
            files[name] = digest(file.read_bytes())
        else:
            files[name] = None
    result = {
        'head': git(root, 'rev-parse', 'HEAD').decode().strip(),
        'branch': git(root, 'branch', '--show-current').decode().strip(),
        'status': git(root, 'status', '--porcelain=v1', '--untracked-files=all').decode(),
        'staged_diff_sha256': digest(git(root, 'diff', '--cached', '--binary')),
        'unstaged_diff_sha256': digest(git(root, 'diff', '--binary')),
        'files': files,
    }
    result['fingerprint'] = digest(json.dumps(result, sort_keys=True).encode())
    return result


def findings(name, data, allowed_binary=False):
    out = []
    if any(fnmatch.fnmatch(name.lower(), pattern) for pattern in DENIED):
        out.append('forbidden path')
    if Path(name).suffix.lower() in {'.pdf', '.zip', '.7z', '.docx', '.xlsx', '.png', '.jpg', '.ttf'} and not allowed_binary:
        out.append('new or modified binary requires explicit review policy')
    try:
        text = data.decode('utf-8-sig')
    except UnicodeDecodeError:
        if not allowed_binary:
            out.append('unreviewed binary')
        return out
    if any(pattern.search(text) for pattern in SECRETS):
        out.append('possible secret or private machine path (value withheld)')
    if re.search(r'(?m)^(?:<<<<<<< |=======\s*$|>>>>>>> )', text):
        out.append('merge conflict marker')
    return out


def static_checks(root, snapshot, config):
    errors = []
    base = config['base_commit']
    baseline = set(git(root, 'ls-tree', '-r', '--name-only', base).decode().splitlines())
    for name, sha in snapshot['files'].items():
        protected = any(name.startswith(p) for p in config['protected_prefixes'])
        old = git(root, 'show', f'{base}:{name}') if name in baseline else None
        current = (root / name).read_bytes() if sha is not None else None
        if protected and (old is None or current is None or canonical(old) != canonical(current)):
            errors.append(f'{name}: protected APDS artifact differs from baseline')
        if sha is None:
            continue
        data = (root / name).read_bytes()
        errors.extend(f'{name}: {issue}' for issue in findings(name, data, old == data))
        if name.endswith('.py'):
            try:
                ast.parse(data.decode('utf-8-sig'), filename=name)
            except (SyntaxError, UnicodeError) as exc:
                errors.append(f'{name}: Python syntax invalid ({type(exc).__name__})')
        if name.endswith('.json'):
            try:
                json.loads(data.decode('utf-8-sig'))
            except (ValueError, UnicodeError):
                errors.append(f'{name}: invalid JSON')
    # Include staged deletions, which no longer appear in ls-files.
    for name in baseline:
        if any(name.startswith(p) for p in config['protected_prefixes']) and name not in snapshot['files']:
            errors.append(f'{name}: protected artifact removed')
    folder = root / 'catalogue/apds-2026-10-08/plans-publics'
    for item in json.loads((folder / 'manifest.json').read_text(encoding='utf-8-sig')):
        file = (folder / item['filename']).resolve()
        if file.parent != folder.resolve() or not file.is_file():
            errors.append('Invalid public PDF path')
        elif digest(file.read_bytes()) != item['sha256'] or file.stat().st_size != item['bytes']:
            errors.append(f'{file.name}: public PDF fingerprint mismatch')
    return errors


def index_findings(root, config):
    """The index may differ from both HEAD and the working copy."""
    errors = []
    names = git(root, 'diff', '--cached', '--name-only', '-z', config['base_commit']).decode().split('\0')
    for name in filter(None, names):
        try:
            data = git(root, 'show', f':{name}')
        except subprocess.CalledProcessError:
            data = None  # Staged deletion.
        try:
            old = git(root, 'show', f"{config['base_commit']}:{name}")
        except subprocess.CalledProcessError:
            old = None
        if any(name.startswith(p) for p in config['protected_prefixes']) and (data is None or old is None or canonical(data) != canonical(old)):
            errors.append(f'{name}: protected APDS artifact changed in index')
        if data is not None:
            errors.extend(f'{name} (index): {issue}' for issue in findings(name, data, data == old))
    return errors


def fresh(proof, snapshot):
    return proof.get('passed') is True and proof.get('inputs') == snapshot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-proof', action='store_true')
    args = parser.parse_args()
    proof_path = ROOT / '.local/verification.json'
    before = inputs(ROOT)
    if args.verify_proof:
        if not proof_path.exists() or not fresh(json.loads(proof_path.read_text(encoding='utf-8')), before):
            print('FAIL: proof missing, failed or stale. Run python tools/check.py.')
            return 1
        print('PASS: proof current for HEAD and worktree inputs', before['head'])
        return 0
    config = json.loads((ROOT / '.checks.json').read_text(encoding='utf-8'))
    errors = static_checks(ROOT, before, config) + index_findings(ROOT, config)
    node = resolve_node()
    if node is None:
        errors.append('Node.js unavailable in PATH and local Windows Codex runtime. Node.js 18+ is required; no JavaScript checks can be certified.')
        node = 'node'
    steps = []

    def run(command):
        try:
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=180,
                                    env={**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONDONTWRITEBYTECODE': '1'})
            step = {'command': command, 'returncode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
        except (OSError, subprocess.TimeoutExpired) as exc:
            step = {'command': command, 'returncode': 1, 'error': type(exc).__name__}
        steps.append(step)
        print(('PASS' if step['returncode'] == 0 else 'FAIL'), ' '.join(command))

    run(['git', 'diff', '--check', config['base_commit']])
    run(['git', 'diff', '--cached', '--check', config['base_commit']])
    run(['git', '--version'])
    run([node, '--version'])
    for name in before['files']:
        if name.endswith(('.js', '.cjs')) and before['files'][name] is not None:
            run([node, '--check', name])
    run([node, 'tests/site.cjs'])
    run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v'])
    changed = set(git(ROOT, 'diff', '--name-only', config['base_commit']).decode().splitlines())
    changed.update(git(ROOT, 'diff', '--cached', '--name-only', config['base_commit']).decode().splitlines())
    changed.update(git(ROOT, 'ls-files', '--others', '--exclude-standard').decode().splitlines())
    ui_changed = any(name in config['ui_files'] or name.startswith('assets/') for name in changed)
    if ui_changed:
        if not config.get('browser_command'):
            errors.append('UI changed: configure and execute browser_command plus user review before accepting.')
        else:
            run(config['browser_command'])
    after = inputs(ROOT)
    if after != before:
        errors.append('Inputs changed during verification')
    passed = not errors and all(step['returncode'] == 0 for step in steps)
    proof = {'schema_version': 1, 'created_at': datetime.now(timezone.utc).isoformat(), 'passed': passed,
             'base': config['base_commit'], 'inputs': before, 'python': sys.version,
             'steps': steps, 'errors': errors, 'browser': 'required' if ui_changed else 'not run: site unchanged from baseline',
             'limits': ['offline synthetic tests', 'no scientific or dissemination validation', 'no deployment', 'ignored runtime data not covered', 'pattern scanner is not a complete security barrier']}
    proof_path.parent.mkdir(exist_ok=True)
    temp = proof_path.with_suffix('.tmp')
    temp.write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(proof_path)
    for error in errors:
        print('FAIL:', error)
    print(('PASS' if passed else 'FAIL') + ': .local/verification.json; HEAD=' + before['head'])
    return 0 if passed else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print('FAIL:', type(error).__name__, 'verification could not complete')
        sys.exit(1)
