import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from tools.check import ROOT, canonical, findings, fresh, index_findings, inputs


class GuardTests(unittest.TestCase):
    def test_safe_and_forbidden_inputs(self):
        self.assertEqual(findings('docs/note.md', b'Public metadata only.'), [])
        self.assertTrue(findings('outputs/inventaire-prive.json', b'{}'))
        self.assertTrue(findings('.local/queue.sqlite', b'content'))
        self.assertTrue(findings('new.pdf', b'%PDF-1.7'))
        self.assertEqual(findings('public.pdf', b'%PDF-1.7', True), [])
        self.assertTrue(findings('config.txt', ('ghp_' + 'x' * 30).encode()))
        self.assertTrue(findings('.env', b'anything'))
        self.assertTrue(findings('file.txt', ('C:' + '\\Users\\someone\\private').encode()))

    def test_proof_detects_content_index_and_head_changes(self):
        temp_root = ROOT / '.local/test-temp'
        temp_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_root) as temp:
            root = Path(temp)
            def git(*args):
                subprocess.run(['git', '-C', temp, *args], check=True, capture_output=True)
            git('init', '-q')
            (root / 'a.txt').write_text('original', encoding='utf-8')
            git('add', 'a.txt')
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture')
            initial = inputs(root)
            proof = {'passed': True, 'inputs': initial}
            self.assertTrue(fresh(proof, inputs(root)))
            self.assertFalse(fresh({'passed': False, 'inputs': initial}, initial))
            (root / 'a.txt').write_text('changed', encoding='utf-8')
            self.assertFalse(fresh(proof, inputs(root)))
            changed = inputs(root)
            git('add', 'a.txt')
            self.assertNotEqual(changed, inputs(root))
            git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'changed')
            self.assertNotEqual(initial['head'], inputs(root)['head'])
            (root / 'new.txt').write_text('untracked', encoding='utf-8')
            self.assertIn('new.txt', inputs(root)['files'])
            (root / 'secret.txt').write_text('ghp_' + 'x' * 30, encoding='utf-8')
            git('add', 'secret.txt')
            (root / 'secret.txt').write_text('safe working copy', encoding='utf-8')
            self.assertTrue(index_findings(root, {'base_commit': 'HEAD', 'protected_prefixes': []}))

    def test_only_line_endings_normalized_for_baseline(self):
        self.assertEqual(canonical(b'public\r\n'), canonical(b'public\n'))
        self.assertNotEqual(canonical(b'public\r\n'), canonical(b'changed\n'))
        self.assertEqual(canonical(b'\xff\r\n'), b'\xff\r\n')


if __name__ == '__main__':
    unittest.main()
