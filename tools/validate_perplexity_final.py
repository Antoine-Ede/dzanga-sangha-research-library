"""Fail-closed validation for a delegated SUP verification delivery."""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "reviews" / "communication-supplement-2026-10-25"
EXPECTED_HEADER = [
    "id", "status", "title_confirmed", "creator_confirmed", "date_confirmed",
    "type_confirmed", "source_url", "evidence_summary", "dzanga_relevance",
    "relationship_or_duplicate", "limitations", "checked_at",
]
EXCLUDED = {"SUP-04", "SUP-27", "SUP-51", "SUP-57", "SUP-64", "SUP-65"}
ALLOWED = {"verified_delegated", "partial", "blocked", "duplicate_candidate"}


def read_tsv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != EXPECTED_HEADER:
            raise ValueError("Unexpected TSV header or column order")
        rows = list(reader)
    return rows


def expected_ids(path=REVIEW / "reported-sources.tsv"):
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        return {row["id"] for row in csv.DictReader(handle, delimiter="\t")} - EXCLUDED


def validate(path, source_register=REVIEW / "reported-sources.tsv"):
    rows = read_tsv(path)
    ids = [row["id"] for row in rows]
    wanted = expected_ids(source_register)
    errors = []
    if len(rows) != 64:
        errors.append(f"Expected 64 rows, found {len(rows)}")
    if len(ids) != len(set(ids)):
        errors.append("Duplicate SUP identifier")
    if set(ids) != wanted:
        errors.append("SUP identifier set differs from source register")
    if set(ids) & EXCLUDED:
        errors.append("Excluded SUP identifier present")
    for row in rows:
        if row["status"] not in ALLOWED:
            errors.append(f"{row['id']}: invalid status")
        if not row["source_url"].startswith(("https://", "http://")):
            errors.append(f"{row['id']}: source URL missing or unsupported")
        if not row["checked_at"]:
            errors.append(f"{row['id']}: missing checked_at")
        else:
            try:
                date.fromisoformat(row["checked_at"])
            except ValueError:
                errors.append(f"{row['id']}: checked_at is not ISO date")
    return {
        "rows": len(rows), "unique_ids": len(set(ids)),
        "statuses": dict(sorted(Counter(row["status"] for row in rows).items())),
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--source-register", type=Path, default=REVIEW / "reported-sources.tsv")
    args = parser.parse_args()
    result = validate(args.path, args.source_register)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
