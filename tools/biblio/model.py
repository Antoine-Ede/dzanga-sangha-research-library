"""Conservative metadata normalization; identity never inferred from title alone."""
import hashlib
import html
import json
import re
import unicodedata
from datetime import datetime, timezone
from difflib import SequenceMatcher
from urllib.parse import unquote, urlsplit

FIELDS = ('title', 'authors', 'date', 'doi')


def stable_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def text(value, name, limit=20000, empty=True):
    if not isinstance(value, str) or len(value) > limit or '\x00' in value or (not empty and not value.strip()):
        raise ValueError(f'Invalid {name}')
    return value.strip()


def public_url(value):
    value = text(value, 'URL', 4096, False)
    parsed = urlsplit(value)
    if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('Public http(s) URL required')
    return value


def normalize_doi(value):
    value = text(value or '', 'DOI', 512).strip()
    if re.match(r'^https?://(?:dx\.)?doi\.org/', value, re.I):
        value = unquote(re.sub(r'^https?://(?:dx\.)?doi\.org/', '', value, flags=re.I))
    value = re.sub(r'^doi:\s*', '', value, flags=re.I).lower()
    return value if re.fullmatch(r'10\.\d{4,9}/\S+', value) else None


def normalize_title(value):
    plain = html.unescape(re.sub(r'<[^>]*>', ' ', value or ''))
    decomposed = unicodedata.normalize('NFKD', plain).casefold()
    plain = ''.join(char for char in decomposed if not unicodedata.combining(char))
    return ' '.join(re.sub(r'[^\w\s]', ' ', plain).split())


def observation(value):
    if not isinstance(value, dict) or value.get('visibility') not in ('public_metadata', 'synthetic'):
        raise ValueError('Only explicitly public metadata or synthetic fixtures are accepted')
    result = {key: text(value.get(key), key, 2000, False) for key in ('source', 'record_id', 'query', 'retrieved_at')}
    if not re.fullmatch(r'[A-Za-z0-9._-]{1,80}', result['source']):
        raise ValueError('source must be an unambiguous provider identifier')
    stamp = datetime.fromisoformat(result['retrieved_at'].replace('Z', '+00:00'))
    if stamp.tzinfo is None:
        raise ValueError('retrieved_at requires timezone')
    result['retrieved_at'] = stamp.astimezone(timezone.utc).isoformat()
    result['visibility'] = value['visibility']
    result['url'] = public_url(value.get('url'))
    metadata = value.get('metadata')
    if not isinstance(metadata, dict):
        raise ValueError('metadata object required')
    authors = metadata.get('authors', [])
    if not isinstance(authors, list) or len(authors) > 500:
        raise ValueError('authors must be a list')
    result['metadata'] = {
        'title': text(metadata.get('title') or '', 'title') or None,
        'authors': [text(author, 'author', 1000, False) for author in authors],
        'date': text(metadata.get('date') or '', 'date', 200) or None,
        'doi': normalize_doi(metadata.get('doi')),
    }
    issues = value.get('source_issues', [])
    if not isinstance(issues, list):
        raise ValueError('Invalid source issues')
    result['source_issues'] = [text(issue, 'source issue', 4000, False) for issue in issues]
    result['warnings'] = list(result['source_issues'])
    if metadata.get('doi') and not result['metadata']['doi']:
        result['warnings'].append('Malformed DOI supplied; retained only in source evidence, not assigned.')
    # Preserve supplied public fields, even if the normalized value is rejected.
    result['supplied_metadata'] = {key: metadata.get(key) for key in FIELDS}
    evidence = value.get('evidence', [])
    if not isinstance(evidence, list) or len(evidence) > 100:
        raise ValueError('Invalid evidence list')
    result['evidence'] = []
    for entry in evidence:
        if not isinstance(entry, dict):
            raise ValueError('Invalid evidence entry')
        result['evidence'].append({'field': text(entry.get('field'), 'evidence field', 100, False),
                                   'text': text(entry.get('text'), 'evidence text', 20000, False),
                                   'locator': text(entry.get('locator'), 'evidence locator', 2000, False)})
    return result


def consolidate(observations):
    proposals, conflicts, missing = {}, {}, []
    for field in FIELDS:
        choices = []
        for entry in observations:
            value = entry['metadata'][field]
            if value in (None, '', []):
                continue
            existing = next((x for x in choices if x['value'] == value), None)
            ref = {'observation_id': entry['id'], 'locator': f'metadata.{field}'}
            if existing:
                existing['evidence_refs'].append(ref)
            else:
                choices.append({'value': value, 'evidence_refs': [ref], 'status': 'proposal'})
        proposals[field] = choices
        if not choices:
            missing.append(field)
        if len(choices) > 1:
            conflicts[field] = choices
    return proposals, conflicts, missing


def matches(metadata, catalogue):
    """Indicators for human examination, never probabilities or merge instructions."""
    out = []
    for item in catalogue:
        reasons = []
        if metadata.get('doi') and metadata['doi'] == item.get('doi'):
            reasons.append('same_normalized_doi')
        first, second = normalize_title(metadata.get('title')), normalize_title(item.get('title'))
        ratio = SequenceMatcher(None, first, second).ratio() if first and second else 0
        if first and first == second:
            reasons.append('same_normalized_title_review_required')
        elif min(len(first), len(second)) >= 20 and ratio >= .82:
            reasons.append('similar_title_review_required')
        if reasons:
            contradictions = [field for field in ('doi', 'date', 'authors') if metadata.get(field) and item.get(field) and metadata[field] != item[field]]
            out.append({'key': item['key'], 'reasons': reasons, 'contradictory_fields': contradictions,
                        'title_similarity_indicator': round(ratio, 3), 'automatic_merge': False})
    return out


def deterministic_proposal(observations):
    references = []
    for obs in observations:
        title = obs['metadata'].get('title') or ''
        if re.search(r'dzanga[\s-]*sangha', title, re.I):
            references.append({'observation_id': obs['id'], 'locator': 'metadata.title', 'quote': title})
    return {'provider': 'deterministic', 'status': 'proposal', 'scope': 'indeterminate', 'abstained': True,
            'reason': 'Mention in title; APDS field provenance still to verify.' if references else 'No sufficient APDS field provenance in supplied metadata.',
            'evidence_refs': references, 'uncertainties': ['Relevance and field provenance require human examination.'],
            'enrichments': [], 'content_dissemination': 'not_assessed'}


def simulated_proposal(observations, supplied=None):
    """Offline contract exerciser. Even valid citations do not certify truth."""
    value = supplied if supplied is not None else {**deterministic_proposal(observations), 'provider': 'simulated'}
    if not isinstance(value, dict) or value.get('provider') != 'simulated' or value.get('status') != 'proposal':
        raise ValueError('Simulated output must remain a proposal')
    if set(value) != {'provider', 'status', 'scope', 'abstained', 'reason', 'evidence_refs', 'uncertainties', 'enrichments', 'content_dissemination'}:
        raise ValueError('Unexpected model fields; decisions and validation are not model outputs')
    text(value['reason'], 'proposal reason', 4000, False)
    if value.get('scope') not in ('indeterminate', 'DSPA-Core', 'DSPA-Relevant') or not isinstance(value.get('abstained'), bool):
        raise ValueError('Invalid proposal scope/abstention')
    if not isinstance(value.get('uncertainties'), list) or not value['uncertainties']:
        raise ValueError('Proposal must state uncertainty')
    for uncertainty in value['uncertainties']:
        text(uncertainty, 'uncertainty', 4000, False)
    if not isinstance(value.get('enrichments'), list):
        raise ValueError('Enrichments must be a list')
    known = {obs['id']: obs for obs in observations}
    def validate_refs(refs):
        if not isinstance(refs, list):
            raise ValueError('Evidence references must be a list')
        for ref in refs:
            if not isinstance(ref, dict) or ref.get('observation_id') not in known:
                raise ValueError('Unknown evidence reference')
            obs = known[ref['observation_id']]
            locator, quote = ref.get('locator'), ref.get('quote')
            sources = {f'metadata.{field}': obs['metadata'][field] if isinstance(obs['metadata'][field], str) else json.dumps(obs['metadata'][field], ensure_ascii=False) for field in FIELDS}
            sources.update({entry['locator']: entry['text'] for entry in obs['evidence']})
            if not isinstance(quote, str) or not quote.strip() or locator not in sources or quote not in sources[locator]:
                raise ValueError('Evidence quote does not occur at the source locator')
    validate_refs(value.get('evidence_refs'))
    if not value['abstained'] and not value['evidence_refs']:
        raise ValueError('An assertion requires evidence')
    if value['scope'] != 'indeterminate' and not value['evidence_refs']:
        raise ValueError('Scope proposal requires evidence; never a human decision')
    if value['scope'] == 'DSPA-Core' and not any(
            entry['locator'] == ref['locator'] and entry['field'] not in ('title', 'metadata.title')
            for ref in value['evidence_refs'] for entry in known[ref['observation_id']]['evidence']):
        raise ValueError('Core proposal requires source evidence beyond title or metadata')
    if value['abstained'] and (value['scope'] != 'indeterminate' or value['enrichments']):
        raise ValueError('An abstention cannot assert scope or enrichments')
    for entry in value.get('enrichments', []):
        if not isinstance(entry, dict) or entry.get('field') not in (*FIELDS, 'themes', 'sites', 'taxa', 'methods', 'summary') or 'value' not in entry:
            raise ValueError('Invalid proposed enrichment')
        if not entry.get('evidence_refs'):
            raise ValueError('Enrichment requires evidence')
        validate_refs(entry['evidence_refs'])
    if value.get('content_dissemination') != 'not_assessed':
        raise ValueError('A model cannot clear dissemination rights')
    return value
