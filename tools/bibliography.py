"""Local bibliography proposal queue. Network commands perform public GET requests only."""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.biblio.model import stable_hash
from tools.biblio.sources import discover, fetch_catalogue, zotero_records
from tools.biblio.store import Store

ROOT = Path(__file__).resolve().parents[1]


def local_path(value):
    """All writable artifacts confined to ignored .local, never the public catalogue."""
    root = ROOT / '.local'
    if root.is_symlink():
        raise ValueError('.local must not be a symlink')
    target = (root / value).resolve()
    if not target.is_relative_to(root.resolve()) or target == root.resolve():
        raise ValueError('Output must remain under .local')
    return target


def read_public(path):
    file = Path(path)
    if file.is_symlink() or file.suffix.lower() != '.json' or file.stat().st_size > 8_000_000:
        raise ValueError('Input must be a small public-metadata JSON file, not a symlink')
    return json.loads(file.read_text(encoding='utf-8-sig'))


def save_export(path, value):
    if path.exists():
        raise ValueError('Output exists; use a new filename to preserve the earlier review export')
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents overwriting a database or a previous decision export.
    with path.open('x', encoding='utf-8') as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write('\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', default='bibliography.sqlite', help='Path relative to .local')
    sub = parser.add_subparsers(dest='command', required=True)
    ingest = sub.add_parser('ingest', help='Ingest declared public metadata or synthetic fixtures')
    ingest.add_argument('file')
    search = sub.add_parser('discover', help='GET Crossref public metadata; query must be public')
    search.add_argument('--query', required=True)
    search.add_argument('--search-field', choices=['title', 'bibliographic'], default='title')
    search.add_argument('--pages', type=int, default=1)
    search.add_argument('--rows', type=int, default=20)
    search.add_argument('--restart', action='store_true')
    catalogue = sub.add_parser('catalogue', help='GET public Zotero snapshot; never writes Zotero')
    catalogue.add_argument('--pages', type=int, default=10)
    catalogue.add_argument('--restart', action='store_true')
    snapshot = sub.add_parser('catalogue-file', help='Use explicit public or synthetic Zotero snapshot')
    snapshot.add_argument('file')
    snapshot.add_argument('--as-of', required=True, help='Known snapshot date, never silently treated as current')
    snapshot.add_argument('--label', required=True)
    export = sub.add_parser('export', help='Export proposals and decision history; not an import file')
    export.add_argument('--out', required=True, help='New filename relative to .local')
    export.add_argument('--provider', choices=['deterministic', 'simulated'], default='deterministic')
    decide = sub.add_parser('decide', help='Record an explicit local human review decision')
    decide.add_argument('id')
    decide.add_argument('--decision', required=True, choices=['retain', 'reject', 'defer'])
    decide.add_argument('--reviewer', required=True)
    decide.add_argument('--reason', required=True)
    decide.add_argument('--scope', choices=['indeterminate', 'DSPA-Core', 'DSPA-Relevant'], default='indeterminate')
    decide.add_argument('--evidence-id')
    decide.add_argument('--scope-basis')
    decide.add_argument('--scope-quote', help='Exact source evidence excerpt; title alone is insufficient')
    sub.add_parser('status')
    backup = sub.add_parser('backup')
    backup.add_argument('--out', required=True)
    args = parser.parse_args(argv)
    store = Store(local_path(args.db))
    try:
        if args.command == 'ingest':
            ids = store.ingest_batch(read_public(args.file))
            result = {'input_records': len(ids), 'candidate_ids': sorted(set(ids))}
        elif args.command == 'discover':
            result = discover(store, args.query, pages=args.pages, rows=args.rows, restart=args.restart, search_field=args.search_field)
        elif args.command == 'catalogue':
            result = fetch_catalogue(store, pages=args.pages, restart=args.restart)
        elif args.command == 'catalogue-file':
            records = zotero_records(read_public(args.file))
            store.set_catalogue(records, {'source': args.label, 'as_of': args.as_of, 'sha256': stable_hash(records), 'count': len(records), 'complete': 'caller-supplied snapshot; completeness not certified'})
            result = {'snapshot_records': len(records), 'as_of': args.as_of}
        elif args.command == 'decide':
            result = store.decide(args.id, args.decision, args.reviewer, args.reason, args.scope, args.evidence_id, args.scope_basis, args.scope_quote)
        elif args.command == 'export':
            value = store.queue(args.provider)
            save_export(local_path(args.out), value)
            result = {'export': args.out, 'candidates': len(value['candidates']), 'purpose': value['purpose']}
        elif args.command == 'backup':
            store.backup(local_path(args.out))
            result = {'backup': args.out, 'integrity': 'ok'}
        else:
            value = store.queue()
            result = {'candidates': len(value['candidates']), 'decisions': sum(bool(c['human_decision']) for c in value['candidates']),
                      'needs_recheck': sum(c['review_status'] == 'needs_recheck' for c in value['candidates']),
                      'catalogue_snapshot': value['catalogue_snapshot'], 'runs': [json.loads(r[0]) for r in store.db.execute('SELECT payload FROM runs ORDER BY id')]}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    finally:
        store.close()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, sqlite3.Error) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
