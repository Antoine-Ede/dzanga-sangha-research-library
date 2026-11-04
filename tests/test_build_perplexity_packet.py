import importlib.util
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "build_perplexity_packet", Path(__file__).resolve().parents[1] / "tools" / "build_perplexity_packet.py"
)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class PacketTests(unittest.TestCase):
    def test_exclusion_set_is_exact_and_unique(self):
        self.assertEqual(module.EXCLUDED, {"SUP-04", "SUP-27", "SUP-51", "SUP-57", "SUP-64", "SUP-65"})

    def test_rows_reads_tabular_utf8_data(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "source.tsv"
            source.write_text("id\ttitle\nSUP-01\tÉpreuve\n", encoding="utf-8")
            self.assertEqual(module.rows(source), [{"id": "SUP-01", "title": "Épreuve"}])
