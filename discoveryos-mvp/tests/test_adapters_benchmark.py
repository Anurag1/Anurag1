import tempfile
import unittest
from pathlib import Path

from discoveryos.adapters import build_component_manifest, component_export_to_claims
from discoveryos.benchmark import run_benchmark


class AdapterTests(unittest.TestCase):
    def test_manifest_marks_integration_status_honestly(self):
        manifest = build_component_manifest()
        self.assertIn("HONet", manifest["components"])
        self.assertIn("not_all_runtime_connected", manifest["status"])

    def test_component_export_is_normalized_with_provenance(self):
        claims = component_export_to_claims("HONet", {
            "records": [{"id": "task-1", "text": "Model retained task knowledge", "source": "run-001", "confidence": 0.7}]
        })
        self.assertEqual(claims[0]["id"], "HONet:task-1")
        self.assertEqual(claims[0]["source"], "run-001")
        self.assertIn("honet", claims[0]["tags"])

    def test_rejects_unknown_component(self):
        with self.assertRaisesRegex(ValueError, "Unknown component"):
            component_export_to_claims("MadeUp", {"records": []})

    def test_benchmark_produces_machine_readable_comparison(self):
        result = run_benchmark([{
            "case_id": "contradiction",
            "claims": [
                {"id": "a", "text": "Battery storage improves grid reliability", "source": "s1"},
                {"id": "b", "text": "Battery storage does not improve grid reliability", "source": "s2"},
            ],
        }])
        self.assertEqual(result["case_count"], 1)
        self.assertEqual(result["aggregate"]["discoveryos_candidate_contradictions"], 1)
        self.assertEqual(result["aggregate"]["baseline_candidate_contradictions"], 0)
        self.assertIn("not an LLM head-to-head", result["interpretation"])


if __name__ == "__main__":
    unittest.main()
