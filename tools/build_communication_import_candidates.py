"""Build conservative Zotero candidates from delegated Communication evidence.

The output is an import proposal, not a catalogue mutation.  It excludes
indexes and generic context pages, retains reported limitations, and leaves a
date blank where the delegated evidence does not safely support one.
"""
import csv
import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "reviews" / "communication-supplement-2026-10-25"
FINAL = REVIEW / "perplexity-final-2026-11-03" / "delegated-final-review.tsv"
PRIORITY = REVIEW / "delegated-priority-review.tsv"

NOT_INDIVIDUAL_WORK = {
    "SUP-16": "Evolving author index, not an individual communication work.",
    "SUP-32": "Two evolving institutional context pages, not an individual work.",
    "SUP-35": "Undated regional project profile, not an individual communication work.",
}

DATES = {
    "SUP-03": "2016-07-20", "SUP-06": "2015-08-19", "SUP-11": "2010",
    "SUP-13": "2018", "SUP-14": "2016-01-20", "SUP-18": "2013-06-12",
    "SUP-19": "2013-05-10", "SUP-20": "2016-08-30", "SUP-21": "2014-11-03",
    "SUP-22": "2018", "SUP-23": "2015-05-04", "SUP-25": "2018-11-14",
    "SUP-28": "2025-11-19", "SUP-34": "2020-05-05", "SUP-50": "2021-02-25",
    "SUP-52": "2000-02-25", "SUP-53": "2000-02-25", "SUP-54": "2002-01-20",
    "SUP-55": "2002-06-04", "SUP-59": "2021", "SUP-60": "2020-12",
    "SUP-61": "2026-04-19", "SUP-62": "2026-04-06", "SUP-63": "2026-07-31",
    "SUP-68": "2018-01-16", "SUP-51": "1994-10-23",
}

# Only actors explicitly described as an author, reporter, director or issuing
# organization are promoted to Zotero creators. Other roles remain in extra.
CREATORS = {
    "SUP-03": [("Emiko", "Jozuka")], "SUP-06": [("Andrea K.", "Turkalo")],
    "SUP-11": [("Stefanie", "Zeyn"), ("Thomas", "Behrend")],
    "SUP-13": [("Thomas", "Behrend")], "SUP-14": [("Susan", "Schulman")],
    "SUP-18": [("", "Wildlife Conservation Society")], "SUP-19": [("", "Wildlife Conservation Society")],
    "SUP-20": [("", "Wildlife Conservation Society")], "SUP-21": [("Andrea K.", "Turkalo")],
    "SUP-22": [("Todd", "McGrain")], "SUP-23": [("Peter", "Canby")],
    "SUP-24": [("", "The New Yorker")], "SUP-25": [("Peter", "Canby")],
    "SUP-28": [("Antoinette", "Hovor")], "SUP-29": [("", "World Wildlife Fund")],
    "SUP-30": [("", "Helmholtz Institute for One Health")],
    "SUP-31": [("", "Helmholtz Institute for One Health")],
    "SUP-33": [("Jörn", "auf dem Kampe")], "SUP-34": [("Andy", "Isaacson")],
    "SUP-37": [("", "Helmholtz Institute for One Health")], "SUP-48": [("", "World Rainforest Movement")],
    "SUP-50": [("", "ScienceDaily")], "SUP-52": [("Ann M.", "Simmons")],
    "SUP-53": [("Ann M.", "Simmons")], "SUP-54": [("Patrick J.", "Kiger")],
    "SUP-55": [("Lucy", "Jones")], "SUP-59": [("", "WWF Deutschland")],
    "SUP-60": [("", "Dzanga-Sangha Protected Areas")],
    "SUP-61": [("Rhett Ayers", "Butler"), ("David", "Akana")],
    "SUP-62": [("David", "Akana")], "SUP-63": [("Rhett Ayers", "Butler")],
    "SUP-68": [("Jürgen", "Schneider")], "SUP-51": [("Donald J.", "Frederick")],
}


def read_tsv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def website_title(url):
    host = urlparse(url).hostname or ""
    labels = {
        "vice.com": "VICE", "blog.wcs.org": "Wildlife Conservation Society",
        "br.de": "Bayerischer Rundfunk", "iwonder.com": "iWonder",
        "slow-journalism.com": "Delayed Gratification", "newsroom.wcs.org": "Wildlife Conservation Society",
        "docnyc.net": "DOC NYC", "newyorker.com": "The New Yorker",
        "worldwildlife.org": "World Wildlife Fund", "helmholtz-hioh.de": "Helmholtz Institute for One Health",
        "wrm.org.uy": "World Rainforest Movement", "sciencedaily.com": "ScienceDaily",
        "latimes.com": "Los Angeles Times", "newsimg.bbc.co.uk": "BBC News",
        "wwf.de": "WWF Deutschland", "dzanga-sangha.org": "Dzanga-Sangha Protected Areas",
        "news.mongabay.com": "Mongabay", "dw.com": "Deutsche Welle",
    }
    for suffix, title in labels.items():
        if host == suffix or host.endswith("." + suffix):
            return title
    return host


def creator(first, last):
    return {"creatorType": "author", "name": last} if not first else {
        "creatorType": "author", "firstName": first, "lastName": last
    }


def candidate(row):
    identifier = row["id"]
    return {
        "id": identifier,
        "itemType": "webpage",
        "title": row["title_confirmed"],
        "creators": [creator(first, last) for first, last in CREATORS.get(identifier, [])],
        "date": DATES.get(identifier, ""),
        "url": row["source_url"],
        "websiteTitle": website_title(row["source_url"]),
        "tags": ["TYPE:Communication", "STATUS:Verified", "ACCESS:Open", "EVIDENCE:Perplexity-Delegated", "SITE:Dzanga-Sangha"],
        "extra": "\n".join([
            f"Communication evidence ID: {identifier}",
            f"Delegated source check: {row['checked_at']}",
            "Evidence provenance: Perplexity delivery received by Codex; no independent primary-source recheck by Codex.",
            f"Reported roles: {row['creator_confirmed']}",
            f"Reported type: {row['type_confirmed']}",
            f"DSPA relevance: {row['dzanga_relevance']}",
            f"Limits: {row['limitations']}",
        ]),
    }


def build():
    rows = [row for row in read_tsv(FINAL) if row["status"] == "verified_delegated" and row["id"] not in NOT_INDIVIDUAL_WORK]
    priority = [row for row in read_tsv(PRIORITY) if row["id"] == "SUP-51" and row["reported_status"] == "verified_delegated"]
    if len(rows) != 32 or len(priority) != 1:
        raise ValueError("Unexpected delegated candidate coverage")
    priority_row = {
        "id": "SUP-51", "title_confirmed": priority[0]["title"], "creator_confirmed": priority[0]["creators_roles"],
        "checked_at": priority[0]["collection_date"][:10], "type_confirmed": "Reportage journalistique",
        "source_url": priority[0]["source_urls"], "dzanga_relevance": priority[0]["local_relevance"],
        "limitations": priority[0]["uncertainties"],
    }
    candidates = [candidate(row) for row in rows] + [candidate(priority_row)]
    identifiers = [item["id"] for item in candidates]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("Duplicate candidate identifier")
    return {
        "schema_version": 1,
        "source": "delegated Perplexity delivery; import requires live Zotero duplicate check",
        "candidate_count": len(candidates),
        "excluded_non_individual_pages": NOT_INDIVIDUAL_WORK,
        "candidates": candidates,
    }


def main():
    parser = __import__("argparse").ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=REVIEW / "communication-import-candidates.json")
    args = parser.parse_args()
    data = build()
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "candidate_count": data["candidate_count"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
