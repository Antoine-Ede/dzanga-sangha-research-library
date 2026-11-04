import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("perplexity_handoff", Path(__file__).resolve().parents[1] / "tools" / "perplexity_handoff.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

class PerplexityHandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.original = module.ROOT, module.PRIVATE, module.REGISTRY
        module.ROOT = Path(self.temp.name)
        module.PRIVATE = module.ROOT / ".local" / "perplexity-handoffs"
        module.REGISTRY = module.PRIVATE / "jobs.json"
        module.PRIVATE.mkdir(parents=True)
        self.url = "https://www.perplexity.ai/search/example"
        module.REGISTRY.write_text(json.dumps({"schema_version": 1, "jobs": [{"id": "HIST-TEST", "session_url": self.url, "exports": []}]}))
        self.source = module.ROOT / "response.md"
        self.source.write_text("# Unreviewed response\n", encoding="utf-8")
    def tearDown(self):
        module.ROOT, module.PRIVATE, module.REGISTRY = self.original
        self.temp.cleanup()
    def args(self, **changes):
        values = dict(job="HIST-TEST", file=str(self.source), source_url=self.url, kind="response")
        values.update(changes)
        return argparse.Namespace(**values)
    def test_preserves_original_and_deduplicates_capture(self):
        module.record(module.read_registry(), self.args())
        module.record(module.read_registry(), self.args())
        exports = module.read_registry()["jobs"][0]["exports"]
        self.assertEqual(len(exports), 1)
        self.assertEqual(exports[0]["documentary_status"], "unreviewed")
        self.assertEqual((module.ROOT / exports[0]["path"]).read_bytes(), self.source.read_bytes())
    def test_rejects_wrong_session_and_unknown_job(self):
        for args in (self.args(source_url=self.url+"-other"), self.args(job="UNKNOWN")):
            with self.assertRaises(ValueError):
                module.record(module.read_registry(), args)
        self.assertFalse((module.PRIVATE / "HIST-TEST").exists())
    def test_rejects_credentials_or_query_in_source_url(self):
        for url in ("https://user:pass@www.perplexity.ai/search/example", self.url+"?token=x"):
            with self.assertRaises(ValueError):
                module.record(module.read_registry(), self.args(source_url=url))
    def test_rejects_unsafe_job_identifier(self):
        module.REGISTRY.write_text(json.dumps({"schema_version":1,"jobs":[{"id":"../escape"}]}))
        with self.assertRaises(ValueError):
            module.read_registry()

if __name__ == "__main__":
    unittest.main()
