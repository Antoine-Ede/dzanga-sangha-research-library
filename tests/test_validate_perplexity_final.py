import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "validate_perplexity_final", Path(__file__).resolve().parents[1] / "tools" / "validate_perplexity_final.py"
)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class FinalDeliveryTests(unittest.TestCase):
    def write_tsv(self, path, rows):
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=module.EXPECTED_HEADER, delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)

    def test_rejects_wrong_header(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "bad.tsv"
            path.write_text("id\tstatus\nSUP-01\tpartial\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "header"):
                module.read_tsv(path)

    def test_rejects_non_iso_check_date(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source.tsv"
            source.write_text("id\nSUP-01\nSUP-04\n", encoding="utf-8")
            path = root / "review.tsv"
            row = {key: "" for key in module.EXPECTED_HEADER}
            row.update({"id": "SUP-01", "status": "partial", "source_url": "https://example.org", "checked_at": "yesterday"})
            self.write_tsv(path, [row])
            result = module.validate(path, source)
            self.assertIn("SUP-01: checked_at is not ISO date", result["errors"])

    def test_packaged_delegated_delivery_covers_the_expected_64_entries(self):
        path = module.REVIEW / "perplexity-final-2026-11-03" / "delegated-final-review.tsv"
        result = module.validate(path)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["rows"], 64)
        self.assertEqual(result["statuses"], {"blocked": 4, "partial": 25, "verified_delegated": 35})
