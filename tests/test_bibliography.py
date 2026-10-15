import copy
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit

from tools.biblio.model import matches, normalize_doi, normalize_title, observation, simulated_proposal
from tools.biblio.sources import MAX_BYTES, NoRedirect, SourceError, crossref_record, discover, fetch_catalogue, get_json, zotero_records
from tools.biblio.store import Store
from tools.bibliography import ROOT, local_path, save_export

FIXTURES = ROOT / 'tests/fixtures'


def fixtures():
    return json.loads((FIXTURES / 'candidates.json').read_text(encoding='utf-8'))


def work(number):
    return {'DOI': f'10.5555/synthetic.{number}', 'URL': f'https://example.invalid/{number}', 'title': [f'Synthetic study {number}'], 'author': [{'given': 'Example', 'family': 'Author'}], 'published': {'date-parts': [[2000]]}}


def page(items, cursor='next'):
    return {'status': 'ok', 'message': {'items': items, 'next-cursor': cursor}}, {}


def zotero_item(number):
    return {'key': f'FIXTURE{number}', 'data': {'itemType': 'report', 'title': f'Synthetic report {number}', 'date': '', 'creators': []}}


class QueueTests(unittest.TestCase):
    def setUp(self):
        parent = ROOT / '.local/test-temp'
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=parent)
        self.path = Path(self.temp.name)
        self.store = Store(self.path / 'queue.sqlite')

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def test_relaunch_and_human_decision_survive(self):
        values = fixtures()
        first = self.store.ingest_batch(values)
        self.store.decide(first[0], 'retain', 'Synthetic reviewer', 'Relevant incomplete report retained for review')
        self.store.close()
        self.store = Store(self.path / 'queue.sqlite')
        second = self.store.ingest_batch(values)
        self.assertEqual(first, second)
        queue = self.store.queue()['candidates']
        self.assertEqual(len(queue), 3)
        self.assertEqual(sum(len(c['observations']) for c in queue), 4)
        report = next(c for c in queue if c['id'] == first[0])
        self.assertEqual(report['human_decision']['decision'], 'retain')
        self.assertEqual(report['review_status'], 'reviewed')
        self.assertFalse(report['catalogue_validated'])

    def test_incomplete_no_doi_is_valid(self):
        self.store.ingest_batch(fixtures()[:1])
        candidate = self.store.queue()['candidates'][0]
        self.assertEqual(set(candidate['missing_metadata']), {'date', 'authors', 'doi'})
        self.assertFalse(candidate['doi_absence_is_error'])
        self.assertIsNone(candidate['metadata']['date'])
        self.assertEqual(candidate['relevance_proposal']['scope'], 'indeterminate')

    def test_conflicts_and_false_title_match_not_merged(self):
        self.store.ingest_batch(fixtures())
        catalogue = zotero_records(json.loads((FIXTURES / 'catalogue.json').read_text()))
        self.store.set_catalogue(catalogue, {'source': 'synthetic', 'as_of': '2026-10-15'})
        candidates = self.store.queue()['candidates']
        conflicting = next(c for c in candidates if c['metadata']['doi'] == '10.5555/apds.fixture.a')
        self.assertEqual({p['value'] for p in conflicting['conflicts']['date']}, {'2001', '2002'})
        other = next(c for c in candidates if c['metadata']['doi'] == '10.5555/apds.fixture.b')
        match = other['possible_catalogue_duplicates']['SYNTHETIC-EXISTING'][0]
        self.assertIn('doi', match['contradictory_fields'])
        self.assertFalse(match['automatic_merge'])
        self.assertTrue(other['possible_queue_duplicates'])

    def test_new_evidence_reopens_without_overwriting_decision(self):
        record = fixtures()[0]
        key = self.store.ingest_batch([record])[0]
        self.store.decide(key, 'defer', 'Synthetic reviewer', 'Need date evidence')
        record['metadata']['date'] = '2000'
        self.store.ingest_batch([record])
        candidate = self.store.queue()['candidates'][0]
        self.assertEqual(candidate['review_status'], 'needs_recheck')
        self.assertEqual(candidate['human_decision']['decision'], 'defer')
        self.assertEqual(len(candidate['decision_history']), 1)

    def test_catalogue_change_requires_recheck_preserves_decision(self):
        key = self.store.ingest_batch(fixtures()[:1])[0]
        self.store.decide(key, 'retain', 'Synthetic reviewer', 'Retain incomplete report')
        self.store.set_catalogue([{'key': 'NEW', 'title': 'New catalogue entry'}], {'source': 'synthetic'})
        candidate = self.store.queue()['candidates'][0]
        self.assertEqual(candidate['review_status'], 'needs_recheck')
        self.assertEqual(candidate['human_decision']['decision'], 'retain')

    def test_missing_doi_later_added_keeps_local_id(self):
        record = fixtures()[0]
        key = self.store.ingest_batch([record])[0]
        record['metadata']['doi'] = '10.5555/added-later'
        self.assertEqual(self.store.ingest_batch([record])[0], key)

    def test_late_identity_conflict_preserves_both_decisions(self):
        records = [fixtures()[0], fixtures()[1]]
        ids = self.store.ingest_batch(records)
        for key in ids:
            self.store.decide(key, 'defer', 'Synthetic reviewer', 'Keep separate pending review')
        records[0]['metadata']['doi'] = records[1]['metadata']['doi']
        self.store.ingest_batch([records[0]])
        candidates = self.store.queue()['candidates']
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(c['human_decision'] for c in candidates))
        self.assertTrue(any('Identity conflict' in w for c in candidates for o in c['observations'] for w in o['warnings']))

    def test_atomic_invalid_batch(self):
        values = fixtures()
        values[1]['metadata']['authors'] = 'not a list'
        with self.assertRaises(ValueError):
            self.store.ingest_batch(values)
        self.assertEqual(self.store.queue()['candidates'], [])

    def test_core_requires_source_excerpt_and_basis(self):
        key = self.store.ingest_batch(fixtures()[1:2])[0]
        obs = self.store.observations(key)[0]
        with self.assertRaises(ValueError):
            self.store.decide(key, 'retain', 'Synthetic reviewer', 'Relevant', 'DSPA-Core', obs['id'], 'Dzanga-Sangha mentioned in title')
        with self.assertRaises(ValueError):
            self.store.decide(key, 'retain', 'Synthetic reviewer', 'Relevant', 'DSPA-Core', obs['id'], 'APDS field observations', 'Invented source quote')
        decision = self.store.decide(key, 'retain', 'Synthetic reviewer', 'Fixture review', 'DSPA-Core', obs['id'], 'APDS field observations in the synthetic abstract', 'observations were collected in the APDS')
        self.assertFalse(decision['catalogue_validated'])
        self.assertEqual(decision['content_dissemination'], 'not_assessed')

    def test_network_resume_keeps_page_one_and_decisions(self):
        fetch = Mock(side_effect=[page([work(1)], 'cursor-two'), SourceError('simulated outage')])
        with self.assertRaises(SourceError):
            discover(self.store, 'public fixture', rows=1, pages=2, fetch=fetch)
        key = self.store.queue()['candidates'][0]['id']
        self.store.decide(key, 'defer', 'Synthetic reviewer', 'Await full review')
        resumed = Mock(return_value=page([], None))
        state = discover(self.store, 'public fixture', rows=1, pages=2, fetch=resumed)
        self.assertTrue(state['complete'])
        self.assertIn('cursor=cursor-two', resumed.call_args[0][0])
        self.assertEqual(len(self.store.queue()['candidates']), 1)
        self.assertEqual(self.store.queue()['candidates'][0]['human_decision']['decision'], 'defer')
        never = Mock(side_effect=AssertionError('Completed run should not refetch'))
        discover(self.store, 'public fixture', rows=1, fetch=never)

    def test_restart_retains_records_and_decisions(self):
        discover(self.store, 'query', rows=2, fetch=Mock(return_value=page([work(1)], None)))
        key = self.store.queue()['candidates'][0]['id']
        self.store.decide(key, 'reject', 'Synthetic reviewer', 'Not relevant')
        discover(self.store, 'query', rows=2, restart=True, fetch=Mock(return_value=page([work(1)], None)))
        self.assertEqual(len(self.store.queue()['candidates']), 1)
        self.assertEqual(self.store.queue()['candidates'][0]['human_decision']['decision'], 'reject')

    def test_invalid_external_page_and_pagination_fail_closed(self):
        for payload in ({}, {'status': 'ok', 'message': {'items': {}}}, {'status': 'ok', 'message': {'items': [work(1), {'DOI': 3}]}}):
            with self.assertRaises(ValueError):
                discover(self.store, 'invalid fixture', rows=2, restart=True, fetch=Mock(return_value=(payload, {})))
            self.assertEqual(self.store.queue()['candidates'], [])
        with self.assertRaises(SourceError):
            discover(self.store, 'missing cursor', rows=1, fetch=Mock(return_value=page([work(1)], None)))
        self.assertEqual(self.store.queue()['candidates'], [])

    def test_search_field_has_separate_resume_identity(self):
        first = Mock(return_value=page([work(1)], None))
        a = discover(self.store, 'query', rows=2, fetch=first)
        self.assertIn('query.title=', first.call_args[0][0])
        second = Mock(return_value=page([work(2)], None))
        b = discover(self.store, 'query', rows=2, search_field='bibliographic', fetch=second)
        self.assertIn('query.bibliographic=', second.call_args[0][0])
        self.assertNotEqual(a['run_id'], b['run_id'])

    def test_discovery_dates_do_not_move_backwards(self):
        item = fixtures()[0]
        self.store.ingest_batch([item])
        item['retrieved_at'] = '2020-01-01T00:00:00+00:00'
        self.store.ingest_batch([item])
        discovery = self.store.queue()['candidates'][0]['observations'][0]['discoveries'][0]
        self.assertTrue(discovery['first_seen'].startswith('2020'))
        self.assertTrue(discovery['last_seen'].startswith('2026'))

    def test_repeated_page_is_bounded(self):
        with self.assertRaises(SourceError):
            discover(self.store, 'query', rows=1, pages=2, fetch=Mock(return_value=page([work(1)], 'same')))
        self.assertEqual(len(self.store.queue()['candidates']), 1)

    def test_catalogue_version_change_preserves_previous_snapshot(self):
        self.store.set_catalogue([{'key': 'OLD', 'title': 'Previous snapshot'}], {'source': 'synthetic previous'})
        responses = Mock(side_effect=[([zotero_item(i) for i in range(100)], {'last-modified-version': '10'}), ([zotero_item(100)], {'last-modified-version': '11'})])
        with self.assertRaises(SourceError):
            fetch_catalogue(self.store, fetch=responses)
        self.assertEqual(self.store.queue()['catalogue_snapshot']['source'], 'synthetic previous')
        state = fetch_catalogue(self.store, restart=True, fetch=Mock(return_value=([zotero_item(200)], {'last-modified-version': '12'})))
        self.assertTrue(state['complete'])
        self.assertEqual(self.store.queue()['catalogue_snapshot']['count'], 1)

    def test_catalogue_resume_stable_version(self):
        first = Mock(return_value=([zotero_item(i) for i in range(100)], {'last-modified-version': '10'}))
        state = fetch_catalogue(self.store, pages=1, fetch=first)
        self.assertFalse(state['complete'])
        self.assertIsNone(self.store.queue()['catalogue_snapshot'])
        second = Mock(return_value=([zotero_item(100)], {'last-modified-version': '10'}))
        fetch_catalogue(self.store, fetch=second)
        self.assertIn('start=100', second.call_args[0][0])
        self.assertEqual(self.store.queue()['catalogue_snapshot']['count'], 101)

    def test_server_backoff_persists_across_invocations(self):
        first = Mock(return_value=([zotero_item(i) for i in range(100)], {'last-modified-version': '10', 'backoff': '60'}))
        with self.assertRaises(SourceError):
            fetch_catalogue(self.store, pages=2, fetch=first)
        self.assertEqual(first.call_count, 1)
        never = Mock(side_effect=AssertionError('Must not contact server during backoff'))
        with self.assertRaises(SourceError):
            fetch_catalogue(self.store, fetch=never)
        with self.assertRaises(SourceError):
            fetch_catalogue(self.store, restart=True, fetch=never)
        first_search = Mock(return_value=({'status': 'ok', 'message': {'items': [work(1)], 'next-cursor': 'next'}}, {'backoff': '60'}))
        discover(self.store, 'synthetic query', rows=1, fetch=first_search)
        with self.assertRaises(SourceError):
            discover(self.store, 'synthetic query', rows=1, restart=True, fetch=never)
        never.assert_not_called()

    def test_duplicate_catalogue_keys_not_accepted(self):
        with self.assertRaises(SourceError):
            fetch_catalogue(self.store, fetch=Mock(return_value=([zotero_item(1), zotero_item(1)], {'last-modified-version': '1'})))
        self.assertIsNone(self.store.queue()['catalogue_snapshot'])

    def test_no_ai_and_simulated_contract(self):
        self.store.ingest_batch(fixtures())
        default = self.store.queue()
        self.assertTrue(all(c['relevance_proposal']['provider'] == 'deterministic' for c in default['candidates']))
        simulated = self.store.queue('simulated')
        candidate = simulated['candidates'][0]
        self.assertEqual(candidate['relevance_proposal']['provider'], 'simulated')
        proposal = candidate['relevance_proposal']
        bad = {**proposal, 'catalogue_validated': True}
        with self.assertRaises(ValueError):
            simulated_proposal(candidate['observations'], bad)
        bad = {**proposal, 'status': 'validated'}
        with self.assertRaises(ValueError):
            simulated_proposal(candidate['observations'], bad)
        bad = {**proposal, 'scope': 'DSPA-Core', 'abstained': False}
        with self.assertRaises(ValueError):
            simulated_proposal(candidate['observations'], bad)
        bad = {**proposal, 'scope': 'DSPA-Core', 'abstained': False, 'evidence_refs': [{'observation_id': 'invented', 'locator': 'abstract', 'quote': 'imagined'}]}
        with self.assertRaises(ValueError):
            simulated_proposal(candidate['observations'], bad)
        with self.assertRaises(ValueError):
            self.store.queue('paid-provider')

    def test_quoted_title_supported_without_rendering_html(self):
        record = fixtures()[0]
        record['metadata']['title'] = 'Dzanga-Sangha: "forêt" & <i>observations</i>'
        self.store.ingest_batch([record])
        candidate = self.store.queue('simulated')['candidates'][0]
        self.assertEqual(candidate['metadata']['title'], record['metadata']['title'])
        self.assertEqual(normalize_title(record['metadata']['title']), 'dzanga sangha foret observations')

    def test_backup_and_own_database_only(self):
        self.store.ingest_batch(fixtures())
        backup = self.path / 'backup.sqlite'
        self.store.backup(backup)
        restored = Store(backup)
        try:
            self.assertEqual(len(restored.queue()['candidates']), 3)
        finally:
            restored.close()
        with self.assertRaises(ValueError):
            self.store.backup(backup)
        other = self.path / 'other.sqlite'
        with sqlite3.connect(other) as db:
            db.execute('CREATE TABLE unrelated(value TEXT)')
        db.close()
        with self.assertRaises(ValueError):
            Store(other)

    def test_cli_roundtrip_no_remote_write(self):
        db = (self.path / 'cli.sqlite').relative_to(ROOT / '.local').as_posix()
        out = (self.path / 'review.json').relative_to(ROOT / '.local').as_posix()
        def cli(*args):
            result = subprocess.run([sys.executable, 'tools/bibliography.py', '--db', db, *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        cli('ingest', str(FIXTURES / 'candidates.json'))
        cli('ingest', str(FIXTURES / 'candidates.json'))
        cli('catalogue-file', str(FIXTURES / 'catalogue.json'), '--as-of', '2026-10-15', '--label', 'synthetic fixture')
        self.assertEqual(cli('status')['candidates'], 3)
        cli('export', '--out', out)
        review = json.loads((self.path / 'review.json').read_text(encoding='utf-8'))
        key = review['candidates'][0]['id']
        cli('decide', key, '--decision', 'defer', '--reviewer', 'Synthetic reviewer', '--reason', 'Synthetic CLI roundtrip')
        self.assertEqual(cli('status')['decisions'], 1)
        self.assertIn('not a Zotero import', review['purpose'])


class InputAndNetworkTests(unittest.TestCase):
    def test_normalized_doi_and_untrusted_input(self):
        self.assertEqual(normalize_doi('https://doi.org/10.5555/ABC'), '10.5555/abc')
        self.assertIsNone(normalize_doi('not a DOI'))
        item = fixtures()[0]
        for visibility in ('private', None):
            with self.assertRaises(ValueError):
                observation({**item, 'visibility': visibility})
        with self.assertRaises(ValueError):
            observation({**item, 'url': 'file:///private.pdf'})
        invalid = copy.deepcopy(item)
        invalid['metadata']['doi'] = 'invalid'
        self.assertTrue(observation(invalid)['warnings'])
        with self.assertRaises(ValueError):
            observation({**item, 'source': 'ambiguous:source'})

    def test_crossref_date_variants_remain_visible(self):
        item = work(1)
        item['published-online'] = {'date-parts': [[1999]]}
        result = crossref_record(item, 'synthetic query', '2026-10-15T10:00:00+00:00')
        self.assertTrue(result['source_issues'])
        self.assertEqual(result['metadata']['date'], '2000')
        self.assertEqual(len(result['evidence']), 2)
        self.assertTrue(observation(result)['warnings'])

    def test_output_path_and_overwrite_refused(self):
        with self.assertRaises(ValueError):
            local_path('../catalogue/overwrite.json')
        with self.assertRaises(ValueError):
            save_export(FIXTURES / 'catalogue.json', {})

    def test_get_only_fixed_hosts_no_redirect(self):
        for url in ('http://api.crossref.org/works', 'https://example.invalid/', 'https://api.crossref.org:1234/works', 'https://user:pass@api.crossref.org/works'):
            with self.assertRaises(SourceError):
                get_json(url)
        with self.assertRaises(SourceError):
            NoRedirect().redirect_request(None, None, 302, None, None, 'https://example.invalid')

    def test_retry_timeout_invalid_json_and_response_size(self):
        response = Mock()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        response.headers = {'Content-Type': 'application/json'}
        response.read.return_value = b'{"status":"ok"}'
        pause = Mock()
        opener = Mock()
        opener.open.side_effect = [HTTPError('https://api.crossref.org/works', 429, 'limited', {'Retry-After': '1'}, None), URLError('offline'), response]
        with patch('tools.biblio.sources.build_opener', return_value=opener):
            result, headers = get_json('https://api.crossref.org/works', sleep=pause)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(pause.call_count, 2)
        self.assertTrue(all(call.args[0].method == 'GET' for call in opener.open.call_args_list))
        for body in (b'invalid json', b'x' * (MAX_BYTES + 1)):
            response.read.return_value = body
            with patch('tools.biblio.sources.build_opener') as factory:
                factory.return_value.open.return_value = response
                with self.assertRaises(SourceError):
                    get_json('https://api.crossref.org/works', sleep=pause)
        with patch('tools.biblio.sources.build_opener') as factory:
            factory.return_value.open.side_effect = TimeoutError('timeout')
            with self.assertRaises(SourceError):
                get_json('https://api.crossref.org/works', sleep=pause)
            self.assertEqual(factory.return_value.open.call_count, 3)

    def test_long_retry_after_is_not_ignored(self):
        pause = Mock()
        for retry in ('60', 'Thu, 15 Oct 2037 10:00:00 GMT'):
            with patch('tools.biblio.sources.build_opener') as factory:
                factory.return_value.open.side_effect = HTTPError('https://api.crossref.org/works', 429, 'limited', {'Retry-After': retry}, None)
                with self.assertRaises(SourceError) as caught:
                    get_json('https://api.crossref.org/works', attempts=1, sleep=pause)
                self.assertIsNotNone(caught.exception.not_before)
        pause.assert_not_called()


if __name__ == '__main__':
    unittest.main()
