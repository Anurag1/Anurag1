import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rmc_benchmark import make_payload, benchmark, deployment_footprint

class RMCTests(unittest.TestCase):
    def test_generation_is_deterministic(self):
        for kind in ("procedural", "repetitive", "random"):
            self.assertEqual(make_payload(kind, 8192), make_payload(kind, 8192))

    def test_requested_size(self):
        for kind in ("procedural", "repetitive", "random"):
            self.assertEqual(len(make_payload(kind, 12345)), 12345)

    def test_recipe_reconstruction_is_exact(self):
        footprint = deployment_footprint()
        for kind in ("procedural", "repetitive", "random"):
            result = benchmark(kind, 4096, 1, footprint, [1, 10])
            self.assertTrue(result["recipe_reconstruction_exact"])

    def test_full_cost_is_not_recipe_only_cost(self):
        footprint = deployment_footprint()
        result = benchmark("repetitive", 4096, 1, footprint, [1, 10])
        self.assertGreaterEqual(result["recipe_plus_full_deployment_bytes_for_one_artifact"], result["recipe_only_bytes_misleading_without_runtime"])
        self.assertEqual(len(result["storage_break_even_scenarios"]), 2)

    def test_deployment_footprint_has_expected_fields(self):
        footprint = deployment_footprint()
        self.assertGreater(footprint["generator_source_bytes"], 0)
        self.assertIn("python_executable_bytes", footprint)
        self.assertIn("standard_library_tree_bytes", footprint)
        self.assertGreaterEqual(footprint["deployment_one_time_bytes"], footprint["generator_source_bytes"])

    def test_unknown_kind_fails(self):
        with self.assertRaises(ValueError):
            make_payload("not-a-workload", 10)

if __name__ == "__main__":
    unittest.main()
