"""SQLite transactions preserve observations and decisions on retries or failures."""
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from .model import FIELDS, consolidate, deterministic_proposal, matches, observation, stable_hash, text


def now():
    return datetime.now(timezone.utc).isoformat()


def dumps(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


class Store:
    def __init__(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, timeout=10)
        self.db.row_factory = sqlite3.Row
        self.db.execute('PRAGMA foreign_keys=ON')
        version = self.db.execute('PRAGMA user_version').fetchone()[0]
        app_id = self.db.execute('PRAGMA application_id').fetchone()[0]
        existing_tables = self.db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        if existing_tables and app_id != 1146310721:
            self.db.close()
            raise ValueError('Existing database belongs to another application; left untouched')
        if version not in (0, 1):
            self.db.close()
            raise ValueError('Unsupported database schema; preserve the database')
        self.db.executescript('''
        CREATE TABLE IF NOT EXISTS candidates(id TEXT PRIMARY KEY, created_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS aliases(alias TEXT PRIMARY KEY, candidate_id TEXT NOT NULL REFERENCES candidates(id));
        CREATE TABLE IF NOT EXISTS observations(id TEXT PRIMARY KEY, candidate_id TEXT NOT NULL REFERENCES candidates(id), payload TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS sightings(observation_id TEXT REFERENCES observations(id), query TEXT, first_seen TEXT, last_seen TEXT, PRIMARY KEY(observation_id, query));
        CREATE TABLE IF NOT EXISTS decisions(seq INTEGER PRIMARY KEY, candidate_id TEXT REFERENCES candidates(id), payload TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY, payload TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS pages(run_id TEXT REFERENCES runs(id), page_key TEXT, payload TEXT NOT NULL, PRIMARY KEY(run_id, page_key));
        CREATE TABLE IF NOT EXISTS catalogue(key TEXT PRIMARY KEY, payload TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY, payload TEXT NOT NULL);
        PRAGMA user_version=1;
        PRAGMA application_id=1146310721;
        ''')

    def close(self):
        self.db.close()

    @contextmanager
    def transaction(self):
        with self.db:
            yield

    def ingest(self, value):
        entry = observation(value)
        alias = f"source:{entry['source']}:{entry['record_id']}"
        doi = entry['metadata']['doi']
        doi_alias = f'doi:{doi}' if doi else None
        old = self.db.execute('SELECT candidate_id FROM aliases WHERE alias=?', (alias,)).fetchone()
        doi_old = self.db.execute('SELECT candidate_id FROM aliases WHERE alias=?', (doi_alias,)).fetchone() if doi else None
        candidate = old[0] if old else doi_old[0] if doi_old else 'cand-' + stable_hash(doi_alias or alias)[:24]
        self.db.execute('INSERT OR IGNORE INTO candidates VALUES(?,?)', (candidate, now()))
        for key in filter(None, (alias, doi_alias)):
            self.db.execute('INSERT OR IGNORE INTO aliases VALUES(?,?)', (key, candidate))
        # Never silently move an existing identity or its human decisions.
        if old and doi_old and old[0] != doi_old[0]:
            entry['warnings'].append(f'Identity conflict with {doi_old[0]}; manual reconciliation required.')
        query, stamp = entry.pop('query'), entry.pop('retrieved_at')
        obs_id = 'obs-' + stable_hash(entry)[:24]
        self.db.execute('INSERT OR IGNORE INTO observations VALUES(?,?,?)', (obs_id, candidate, dumps(entry)))
        self.db.execute('''INSERT INTO sightings VALUES(?,?,?,?)
                        ON CONFLICT(observation_id,query) DO UPDATE SET
                        first_seen=MIN(first_seen,excluded.first_seen), last_seen=MAX(last_seen,excluded.last_seen)''', (obs_id, query, stamp, stamp))
        return candidate

    def ingest_batch(self, values):
        if not isinstance(values, list):
            raise ValueError('Public input must be a list')
        with self.transaction():
            return [self.ingest(value) for value in values]

    def run_state(self, run_id, default):
        row = self.db.execute('SELECT payload FROM runs WHERE id=?', (run_id,)).fetchone()
        return json.loads(row[0]) if row else default

    def save_run(self, run_id, state):
        self.db.execute('INSERT INTO runs VALUES(?,?) ON CONFLICT(id) DO UPDATE SET payload=excluded.payload', (run_id, dumps(state)))

    def observations(self, candidate):
        entries = []
        for row in self.db.execute('SELECT id,payload FROM observations WHERE candidate_id=? ORDER BY rowid', (candidate,)):
            value = json.loads(row['payload'])
            value['id'] = row['id']
            value['discoveries'] = [dict(x) for x in self.db.execute('SELECT query,first_seen,last_seen FROM sightings WHERE observation_id=? ORDER BY query', (row['id'],))]
            entries.append(value)
        return entries

    def decide(self, candidate, decision, reviewer, reason, scope='indeterminate', evidence_id=None, scope_basis=None, scope_quote=None):
        if decision not in ('retain', 'reject', 'defer') or scope not in ('indeterminate', 'DSPA-Core', 'DSPA-Relevant'):
            raise ValueError('Invalid decision or scope')
        reviewer, reason = text(reviewer, 'reviewer', 200, False), text(reason, 'reason', 4000, False)
        observations = self.observations(candidate)
        if not observations:
            raise ValueError('Unknown candidate')
        if scope != 'indeterminate':
            if evidence_id not in {entry['id'] for entry in observations} or not scope_basis or len(scope_basis.strip()) < 15:
                raise ValueError('Scope decision requires an observation ID and an explicit evidence basis')
            cited = next(entry for entry in observations if entry['id'] == evidence_id)
            if not scope_quote or len(scope_quote.strip()) < 15 or not any(scope_quote in evidence['text'] and evidence['field'] not in ('title', 'metadata.title') for evidence in cited['evidence']):
                raise ValueError('Scope needs a verifiable source excerpt beyond a title mention')
        if scope == 'DSPA-Core' and not any(word in scope_basis.casefold() for word in ('data', 'données', 'observ', 'échant', 'sample', 'terrain', 'field')):
            raise ValueError('Core basis must explicitly address APDS data/observations/samples/fieldwork')
        if scope == 'DSPA-Core' and not any(word in scope_basis.casefold() for word in ('apds', 'dzanga')):
            raise ValueError('Core basis must explicitly identify APDS origin')
        value = {'decision': decision, 'reviewer': reviewer, 'reason': reason, 'scope': scope,
                 'scope_evidence_id': evidence_id, 'scope_basis': scope_basis, 'scope_quote': scope_quote, 'decided_at': now(),
                 'actor_claim': 'human-entered; identity not authenticated by this local CLI',
                 'reviewed_observation_ids': [entry['id'] for entry in observations],
                 'reviewed_catalogue_sha256': self.catalogue_info().get('sha256'),
                 'catalogue_validated': False, 'content_dissemination': 'not_assessed'}
        with self.transaction():
            self.db.execute('INSERT INTO decisions(candidate_id,payload) VALUES(?,?)', (candidate, dumps(value)))
        return value

    def set_catalogue(self, records, info):
        keys = [item['key'] for item in records]
        if len(keys) != len(set(keys)):
            raise ValueError('Duplicate keys in catalogue snapshot')
        with self.transaction():
            self.db.execute('DELETE FROM catalogue')
            self.db.executemany('INSERT INTO catalogue VALUES(?,?)', [(item['key'], dumps(item)) for item in records])
            self.db.execute("INSERT INTO settings VALUES('catalogue',?) ON CONFLICT(key) DO UPDATE SET payload=excluded.payload", (dumps({**info, 'sha256': stable_hash(records)}),))

    def catalogue_info(self):
        row = self.db.execute("SELECT payload FROM settings WHERE key='catalogue'").fetchone()
        return json.loads(row[0]) if row else {}

    def queue(self, provider='deterministic'):
        if provider not in ('deterministic', 'simulated'):
            raise ValueError('Only deterministic and offline simulated providers exist')
        catalogue = [json.loads(row[0]) for row in self.db.execute('SELECT payload FROM catalogue ORDER BY key')]
        info = self.db.execute("SELECT payload FROM settings WHERE key='catalogue'").fetchone()
        entries = []
        for row in self.db.execute('SELECT id,created_at FROM candidates ORDER BY id'):
            observations = self.observations(row['id'])
            fields, conflicts, missing = consolidate(observations)
            metadata = {field: choices[0]['value'] if choices else [] if field == 'authors' else None for field, choices in fields.items()}
            history = [json.loads(d[0]) for d in self.db.execute('SELECT payload FROM decisions WHERE candidate_id=? ORDER BY seq', (row['id'],))]
            decision = history[-1] if history else None
            changed = bool(decision) and (set(decision['reviewed_observation_ids']) != {x['id'] for x in observations}
                                          or decision.get('reviewed_catalogue_sha256') != self.catalogue_info().get('sha256'))
            review_status = 'pending' if not decision else 'needs_recheck' if changed else 'reviewed'
            proposal = deterministic_proposal(observations)
            if provider == 'simulated':
                from .model import simulated_proposal
                proposal = simulated_proposal(observations)
            all_matches = {}
            for obs in observations:
                for match in matches(obs['metadata'], catalogue):
                    all_matches.setdefault(match['key'], []).append({**match, 'observation_id': obs['id']})
            entries.append({'id': row['id'], 'created_at': row['created_at'], 'metadata': metadata,
                            'field_proposals': fields, 'conflicts': conflicts, 'missing_metadata': missing,
                            'doi_absence_is_error': False, 'observations': observations,
                            'relevance_proposal': proposal, 'possible_catalogue_duplicates': all_matches,
                            'review_status': review_status, 'human_decision': decision, 'decision_history': history,
                            'metadata_accuracy': 'not_certified', 'catalogue_validated': False,
                            'content_dissemination': 'not_assessed'})
        # Duplicate candidates can remain distinct after late DOI corrections; surface them.
        for entry in entries:
            others = [{'key': other['id'], **obs['metadata']} for other in entries if other['id'] != entry['id'] for obs in other['observations']]
            entry['possible_queue_duplicates'] = [match for obs in entry['observations'] for match in matches(obs['metadata'], others)]
        return {'schema_version': 1, 'exported_at': now(), 'purpose': 'local human review, not a Zotero import',
                'catalogue_snapshot': json.loads(info[0]) if info else None,
                'catalogue_warning': 'Snapshot only; recheck current Zotero before any later curation.' if info else 'No catalogue snapshot: duplicate checks are incomplete.',
                'candidates': entries}

    def backup(self, destination):
        destination = Path(destination)
        if destination.exists():
            raise ValueError('Backup destination already exists')
        destination.parent.mkdir(parents=True, exist_ok=True)
        backup = sqlite3.connect(destination)
        try:
            self.db.backup(backup)
            if backup.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                raise ValueError('Backup integrity check failed')
        finally:
            backup.close()
