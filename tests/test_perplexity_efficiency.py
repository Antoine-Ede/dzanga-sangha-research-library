import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "perplexity_efficiency", Path(__file__).resolve().parents[1] / "tools" / "perplexity_efficiency.py"
)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class EfficiencyTests(unittest.TestCase):
    def test_visible_duration_only_accepts_explicit_values(self):
        self.assertEqual(module.visible_seconds("Terminé 1min 12s visible"), 72)
        self.assertEqual(module.visible_seconds("Terminé29s"), 29)
        self.assertIsNone(module.visible_seconds("Response finished"))

    def test_measure_keeps_token_and_savings_unknown(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            evidence = root / ".local" / "perplexity-handoffs" / "JOB-1"
            evidence.mkdir(parents=True)
            report = evidence / "response.md"
            report.write_text("one two three", encoding="utf-8")
            registry = root / ".local" / "perplexity-handoffs" / "jobs.json"
            registry.write_text(json.dumps({"jobs": [{
                "id": "JOB-1", "transport": "browser", "status": "completed_observed",
                "observation": "Terminé 8s", "case_ids": ["SUP-01"],
                "exports": [{"kind": "response", "path": ".local/perplexity-handoffs/JOB-1/response.md"}]
            }]}), encoding="utf-8")
            old_root = module.ROOT
            try:
                module.ROOT = root
                result = module.measure(registry)
            finally:
                module.ROOT = old_root
            self.assertEqual(result["response_words_whitespace_split"], 3)
            self.assertEqual(result["visible_duration_seconds_total"], 8)
            self.assertIsNone(result["actual_provider_tokens"])
            self.assertIsNone(result["measured_token_savings"])
