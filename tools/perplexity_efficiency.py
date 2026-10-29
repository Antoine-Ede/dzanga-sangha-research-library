"""Summarise observable Perplexity handoff volume without claiming token savings.

The provider does not expose billing or model-token usage in the browser handoff.
This tool therefore reports only reproducible local proxies (mission, case, byte,
character, word and visible-duration counts).  It deliberately returns ``null``
for actual tokens, a direct-search baseline and any savings calculation.
"""
import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".local" / "perplexity-handoffs" / "jobs.json"


def words(text):
    return len(re.findall(r"\S+", text, flags=re.UNICODE))


def visible_seconds(observation):
    """Return only an explicitly displayed duration, never an inferred one."""
    if not observation:
        return None
    minute = re.search(r"\b(\d+)\s*min(?:\s*(\d+)\s*s)?\b", observation, re.I)
    if minute:
        return int(minute.group(1)) * 60 + int(minute.group(2) or 0)
    second = re.search(r"(\d+)\s*s\b", observation, re.I)
    return int(second.group(1)) if second else None


def measure(registry_path=REGISTRY):
    data = json.loads(Path(registry_path).read_text(encoding="utf-8"))
    browser_jobs = [job for job in data["jobs"] if job.get("transport") == "browser"]
    responses = []
    all_exports = []
    for job in browser_jobs:
        for artifact in job.get("exports", []):
            path = ROOT / artifact["path"]
            if not path.is_file():
                raise ValueError(f"Missing handoff evidence: {artifact['path']}")
            all_exports.append(artifact)
            if artifact.get("kind") == "response":
                text = path.read_text(encoding="utf-8-sig")
                responses.append({"job": job["id"], "bytes": len(path.read_bytes()),
                                  "characters": len(text), "words": words(text)})
    durations = [visible_seconds(job.get("observation")) for job in browser_jobs]
    durations = [duration for duration in durations if duration is not None]
    case_slots = [case for job in browser_jobs for case in job.get("case_ids", [])]
    return {
        "schema_version": 1,
        "scope": "observable local handoff evidence only",
        "browser_jobs": len(browser_jobs),
        "completed_or_observed_browser_jobs": sum("completed" in job.get("status", "") for job in browser_jobs),
        "case_slots": len(case_slots),
        "unique_case_ids": len(set(case_slots)),
        "evidence_artifacts": len(all_exports),
        "response_artifacts": len(responses),
        "response_bytes": sum(item["bytes"] for item in responses),
        "response_characters": sum(item["characters"] for item in responses),
        "response_words_whitespace_split": sum(item["words"] for item in responses),
        "visible_durations_seconds": durations,
        "visible_duration_seconds_total": sum(durations),
        "visible_duration_count": len(durations),
        "actual_provider_tokens": None,
        "direct_research_baseline_tokens": None,
        "measured_token_savings": None,
        "limitation": "The browser handoff exposes neither provider usage nor a matched direct-search baseline; text volume and visible duration are not token accounting."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit compact JSON")
    args = parser.parse_args()
    result = measure()
    print(json.dumps(result, ensure_ascii=False, indent=None if args.json else 2))


if __name__ == "__main__":
    main()
