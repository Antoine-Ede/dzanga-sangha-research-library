"""Bounded GET-only public metadata adapters. No credentials, PDFs or redirects."""
import json
import time
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
from .model import normalize_doi, observation, public_url, stable_hash, text
from .store import now

GROUP = '6701789'
MAX_BYTES = 8_000_000


class SourceError(ValueError):
    def __init__(self, message, not_before=None):
        super().__init__(message)
        self.not_before = not_before


def backoff_until(headers):
    value = headers.get('backoff', '0')
    if not str(value).isdigit():
        raise SourceError('Invalid server Backoff header')
    seconds = int(value)
    if seconds > 86400:
        raise SourceError('Unexpected server backoff; retry manually after investigation')
    return (datetime.now(timezone.utc) + timedelta(seconds=seconds)).isoformat() if seconds else None


def ready(state):
    deadline = state.get('not_before')
    if deadline and datetime.now(timezone.utc) < datetime.fromisoformat(deadline):
        raise SourceError(f'Server pause active until {deadline}; checkpoint retained', deadline)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise SourceError('Redirect refused; public API host must remain fixed')


def get_json(url, *, attempts=3, timeout=20, sleep=time.sleep):
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or parsed.hostname not in ('api.crossref.org', 'api.zotero.org') or parsed.port not in (None, 443) or parsed.username or parsed.password:
        raise SourceError('Only fixed HTTPS public metadata APIs are allowed')
    for attempt in range(attempts):
        try:
            req = Request(url, method='GET', headers={'Accept': 'application/json', 'Zotero-API-Version': '3', 'User-Agent': 'DSPA-Library-Local-Review/0.1 (public metadata; no writes)'})
            with build_opener(NoRedirect()).open(req, timeout=timeout) as response:
                raw = response.read(MAX_BYTES + 1)
                if len(raw) > MAX_BYTES:
                    raise SourceError('Response exceeds size limit')
                content_type = response.headers.get('Content-Type', '')
                if 'json' not in content_type:
                    raise SourceError('Expected JSON content type')
                try:
                    body = json.loads(raw)
                except (UnicodeError, ValueError) as error:
                    raise SourceError('Invalid JSON response') from error
                return body, {k.lower(): v for k, v in response.headers.items()}
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504):
                raise SourceError(f'Public API HTTP {error.code}; checkpoint retained') from error
            retry = error.headers.get('Retry-After', '')
            # Do not retry before a long server-requested delay; let the operator resume later.
            if retry and (not retry.isdigit() or int(retry) > 5):
                if retry.isdigit():
                    deadline = (datetime.now(timezone.utc) + timedelta(seconds=min(int(retry), 31536000))).isoformat()
                else:
                    try:
                        deadline = parsedate_to_datetime(retry).astimezone(timezone.utc).isoformat()
                    except (ValueError, TypeError, OverflowError):
                        deadline = None
                raise SourceError('Server requested a longer pause; resume later from checkpoint', deadline) from error
            if attempt + 1 == attempts:
                deadline = backoff_until({'backoff': retry or '0'})
                raise SourceError(f'Public API HTTP {error.code}; checkpoint retained', deadline) from error
            sleep(max(float(retry or 0), 2 ** attempt))
        except (URLError, TimeoutError, OSError) as error:
            if attempt + 1 == attempts:
                raise SourceError('Public API unavailable; checkpoint retained') from error
            sleep(2 ** attempt)
    raise SourceError('No response')


def date_parts(value):
    if not isinstance(value, dict) or 'date-parts' not in value:
        return None
    parts = value['date-parts']
    if not isinstance(parts, list) or not parts or not isinstance(parts[0], list):
        raise SourceError('Invalid Crossref date')
    values = parts[0]
    if not 1 <= len(values) <= 3 or any(type(x) is not int for x in values):
        raise SourceError('Invalid Crossref date-parts')
    if not 1000 <= values[0] <= 2999 or len(values) > 1 and not 1 <= values[1] <= 12 or len(values) > 2 and not 1 <= values[2] <= 31:
        raise SourceError('Crossref date out of range')
    return '-'.join([str(values[0]), *[f'{x:02d}' for x in values[1:]]])


def crossref_record(item, query, stamp):
    if not isinstance(item, dict) or not isinstance(item.get('DOI'), str) or not normalize_doi(item['DOI']):
        raise SourceError('Crossref work needs a valid DOI identity')
    titles = item.get('title', [])
    authors = item.get('author', [])
    if not isinstance(titles, list) or any(not isinstance(x, str) for x in titles) or not isinstance(authors, list):
        raise SourceError('Invalid Crossref metadata shape')
    names = []
    for author in authors:
        if not isinstance(author, dict):
            raise SourceError('Invalid Crossref author')
        for field in ('name', 'given', 'family'):
            if field in author and not isinstance(author[field], str):
                raise SourceError('Invalid Crossref author name')
        name = author.get('name') or ' '.join(filter(None, [author.get('given'), author.get('family')]))
        if name:
            names.append(name)
    date = date_parts(item.get('published'))
    evidence = []
    date_variants = []
    for field in ('published', 'published-print', 'published-online', 'issued'):
        if item.get(field):
            evidence.append({'field': 'publication_date', 'text': json.dumps(item[field], ensure_ascii=False), 'locator': field})
            parsed = date_parts(item[field])
            if parsed:
                date_variants.append(parsed)
    if item.get('abstract'):
        evidence.append({'field': 'abstract', 'text': text(item['abstract'], 'abstract'), 'locator': 'abstract'})
    doi = normalize_doi(item['DOI'])
    return observation({'visibility': 'public_metadata', 'source': 'crossref', 'record_id': doi,
                        'url': item.get('URL') or f'https://doi.org/{doi}', 'query': query, 'retrieved_at': stamp,
                        'source_issues': ['Publication date variants differ; inspect named date fields in source evidence.'] if len(set(date_variants)) > 1 else [],
                        'metadata': {'title': titles[0] if titles else None, 'authors': names, 'date': date, 'doi': doi}, 'evidence': evidence})


def discover(store, query, *, pages=1, rows=20, restart=False, search_field='title', fetch=get_json):
    query = text(query, 'public query', 500, False)
    if not 1 <= pages <= 20 or not 1 <= rows <= 100:
        raise ValueError('pages must be 1..20, rows 1..100')
    if search_field not in ('title', 'bibliographic'):
        raise ValueError('Unsupported Crossref search field')
    run_id = 'crossref-' + stable_hash([query, rows, search_field])[:24]
    default = {'source': 'crossref', 'query': query, 'search_field': search_field, 'rows': rows, 'cursor': '*', 'complete': False, 'pages_saved': 0}
    state = store.run_state(run_id, default)
    if restart:
        ready(state)  # Restarting pagination must not bypass a server pause.
        state = default  # Existing observations and decisions deliberately retained.
    with store.transaction():
        store.save_run(run_id, state)
    try:
        for _ in range(pages):
            if state['complete']:
                break
            ready(state)
            url = 'https://api.crossref.org/works?' + urlencode({f'query.{search_field}': query, 'rows': rows, 'cursor': state['cursor']})
            payload, headers = fetch(url)
            if not isinstance(payload, dict) or payload.get('status') != 'ok' or not isinstance(payload.get('message'), dict):
                raise SourceError('Invalid Crossref envelope')
            message = payload['message']
            items = message.get('items')
            if not isinstance(items, list) or len(items) > rows:
                raise SourceError('Invalid Crossref items page')
            stamp = now()
            records = [crossref_record(item, f'{search_field}: {query}', stamp) for item in items]
            next_cursor = message.get('next-cursor')
            if len(items) == rows and (not isinstance(next_cursor, str) or not next_cursor):
                raise SourceError('Full Crossref page without next cursor')
            signature = stable_hash(items)
            if records and state.get('last_page_hash') == signature:
                raise SourceError('Repeated page; restart query later, existing results retained')
            next_state = {**state, 'cursor': next_cursor or state['cursor'], 'complete': len(items) < rows,
                          'pages_saved': state['pages_saved'] + 1, 'last_page_hash': signature, 'updated_at': stamp, 'error': None,
                          'not_before': backoff_until(headers)}
            with store.transaction():
                for record in records:
                    store.ingest(record)
                store.db.execute('INSERT OR REPLACE INTO pages VALUES(?,?,?)', (run_id, str(state['pages_saved']), json.dumps({'url': url, 'retrieved_at': stamp, 'response_sha256': signature, 'records': records}, ensure_ascii=False)))
                store.save_run(run_id, next_state)
            state = next_state
    except (ValueError, OSError) as error:
        with store.transaction():
            store.save_run(run_id, {**state, 'error': str(error), 'failed_at': now(), 'not_before': getattr(error, 'not_before', None) or state.get('not_before')})
        raise
    return {'run_id': run_id, **state}


def zotero_records(items):
    if not isinstance(items, list):
        raise SourceError('Zotero snapshot must be a list')
    records = []
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get('data'), dict):
            raise SourceError('Invalid Zotero item')
        data = item['data']
        if data.get('itemType') in ('attachment', 'note', 'annotation'):
            continue
        key = text(item.get('key'), 'Zotero key', 50, False)
        creators = data.get('creators', [])
        if not isinstance(creators, list) or any(not isinstance(c, dict) for c in creators):
            raise SourceError('Invalid Zotero creators')
        authors = []
        for creator in creators:
            if creator.get('creatorType') != 'author':
                continue
            parts = [creator.get('name')] if creator.get('name') else [creator.get('firstName'), creator.get('lastName')]
            authors.append(' '.join(text(part, 'creator', 1000) for part in parts if part))
        doi = data.get('DOI')
        if not doi:
            import re
            match = re.search(r'^DOI:\s*(\S+)', data.get('extra') or '', re.M | re.I)
            doi = match[1] if match else None
        records.append({'key': key, 'title': text(data.get('title') or '', 'title') or None,
                        'authors': authors, 'date': text(data.get('date') or '', 'date', 200) or None,
                        'doi': normalize_doi(doi)})
    return records


def fetch_catalogue(store, *, pages=10, restart=False, fetch=get_json):
    if not 1 <= pages <= 50:
        raise ValueError('pages must be 1..50')
    run_id = 'zotero-public-' + GROUP
    default = {'source': 'zotero-public', 'group': GROUP, 'start': 0, 'version': None, 'complete': False}
    state = store.run_state(run_id, default)
    if restart:
        ready(state)
    with store.transaction():
        if restart:
            store.db.execute('DELETE FROM pages WHERE run_id=?', (run_id,))
            state = default
        store.save_run(run_id, state)
    try:
        for _ in range(pages):
            if state['complete']:
                break
            ready(state)
            url = f'https://api.zotero.org/groups/{GROUP}/items/top?' + urlencode({'format': 'json', 'limit': 100, 'start': state['start']})
            payload, headers = fetch(url)
            records = zotero_records(payload)
            if len(payload) > 100:
                raise SourceError('Oversized Zotero page')
            version = headers.get('last-modified-version')
            if not version or not str(version).isdigit():
                raise SourceError('Zotero library version missing')
            if state['version'] is not None and state['version'] != version:
                raise SourceError('Catalogue changed during pagination; use --restart to rebuild snapshot')
            next_state = {**state, 'version': version, 'start': state['start'] + len(payload),
                          'complete': len(payload) < 100, 'retrieved_at': now(), 'error': None,
                          'not_before': backoff_until(headers)}
            with store.transaction():
                store.db.execute('INSERT OR REPLACE INTO pages VALUES(?,?,?)', (run_id, str(state['start']), json.dumps({'url': url, 'retrieved_at': next_state['retrieved_at'], 'response_sha256': stable_hash(payload), 'records': records}, ensure_ascii=False)))
                if next_state['complete']:
                    all_records = [record for row in store.db.execute('SELECT payload FROM pages WHERE run_id=? ORDER BY CAST(page_key AS INTEGER)', (run_id,)) for record in json.loads(row[0])['records']]
                    # Same transaction: an invalid final page cannot replace the previous catalogue.
                    keys = [record['key'] for record in all_records]
                    if len(keys) != len(set(keys)):
                        raise SourceError('Duplicate Zotero keys across pages; restart snapshot')
                    store.db.execute('DELETE FROM catalogue')
                    store.db.executemany('INSERT INTO catalogue VALUES(?,?)', [(r['key'], json.dumps(r, ensure_ascii=False)) for r in all_records])
                    info = {'source': f'https://api.zotero.org/groups/{GROUP}/items/top', 'retrieved_at': next_state['retrieved_at'], 'library_version': version, 'count': len(all_records), 'sha256': stable_hash(all_records), 'complete': True}
                    store.db.execute("INSERT INTO settings VALUES('catalogue',?) ON CONFLICT(key) DO UPDATE SET payload=excluded.payload", (json.dumps(info),))
                store.save_run(run_id, next_state)
            state = next_state
    except (ValueError, OSError) as error:
        with store.transaction():
            store.save_run(run_id, {**state, 'error': str(error), 'failed_at': now(), 'not_before': getattr(error, 'not_before', None) or state.get('not_before')})
        raise
    return {'run_id': run_id, **state}
