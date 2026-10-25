"""Offline evidence inventory for user-authorized Perplexity research handoffs."""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / ".local" / "perplexity-handoffs"
REGISTRY = PRIVATE / "jobs.json"

def read_registry():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    ids = [j["id"] for j in data["jobs"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate mission identifiers")
    for identifier in ids:
        if not re.fullmatch(r"[A-Z][A-Z0-9-]{1,63}", identifier):
            raise ValueError("Invalid mission identifier")
    return data

def record(data, args):
    job = next((j for j in data["jobs"] if j["id"] == args.job), None)
    if job is None:
        raise ValueError("Mission not declared")
    url = urlsplit(args.source_url)
    if url.scheme != "https" or url.hostname not in ("www.perplexity.ai", "perplexity.ai") or url.username or url.password or url.query or url.fragment or not url.path.startswith("/search/"):
        raise ValueError("Expected canonical Perplexity discussion URL without credentials or query")
    if job.get("session_url") and args.source_url != job["session_url"]:
        raise ValueError("Discussion differs from declared mission")
    source = Path(args.file).resolve(strict=True)
    if not source.is_file() or source.suffix.lower() not in (".md", ".txt", ".csv", ".tsv", ".json"):
        raise ValueError("Expected a textual report file")
    if source.stat().st_size > 10_000_000:
        raise ValueError("Report exceeds 10 MB")
    raw = source.read_bytes()
    raw.decode("utf-8-sig")
    digest = hashlib.sha256(raw).hexdigest()
    target_dir = PRIVATE / job["id"]
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / (digest + source.suffix.lower())
    if target.exists():
        if target.read_bytes() != raw:
            raise ValueError("Existing evidence differs")
    else:
        with target.open("xb") as f:
            f.write(raw)
    evidence = {"sha256": digest, "bytes": len(raw), "kind": args.kind,
                "path": target.relative_to(ROOT).as_posix(),
                "source_url": args.source_url, "collected_at": datetime.now(timezone.utc).isoformat(),
                "documentary_status": "unreviewed"}
    exports = job.setdefault("exports", [])
    if not any(e["sha256"] == digest and e["source_url"] == args.source_url and e["kind"] == args.kind for e in exports):
        exports.append(evidence)
        temporary = REGISTRY.with_suffix(".tmp")
        temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(REGISTRY)
    print(json.dumps({"job": job["id"], "evidence": evidence}, ensure_ascii=False))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("status")
    add = commands.add_parser("record")
    add.add_argument("--job", required=True)
    add.add_argument("--file", required=True)
    add.add_argument("--source-url", required=True)
    add.add_argument("--kind", choices=("response", "export", "user_handoff"), required=True)
    args = parser.parse_args()
    try:
        data = read_registry()
        if args.command == "status":
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            record(data, args)
    except (OSError, ValueError, AssertionError, StopIteration) as error:
        print("Handoff unavailable: " + str(error), file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
