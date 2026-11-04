import importlib.util
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "build_communication_import_candidates", Path(__file__).resolve().parents[1] / "tools" / "build_communication_import_candidates.py"
)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class CommunicationCandidateTests(unittest.TestCase):
    def test_builds_conservative_candidate_set(self):
        data = module.build()
        ids = {item["id"] for item in data["candidates"]}
        self.assertEqual(data["candidate_count"], 33)
        self.assertNotIn("SUP-47", ids)
        self.assertNotIn("SUP-16", ids)
        self.assertIn("SUP-51", ids)
        self.assertTrue(all(item["itemType"] == "webpage" for item in data["candidates"]))
