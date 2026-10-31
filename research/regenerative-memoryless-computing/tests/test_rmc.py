import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rmc_benchmark import make_payload, benchmark

class RMCTests(unittest.TestCase):
    def test_generation_is_deterministic(self):
        for kind in ("procedural", "repetitive", "random"):
            self.assertEqual(make_payload(kind, 8192), make_payload(kind, 8192))

    def test_requested_size(self):
        for kind in ("procedural", "repetitive", "random"):
            self.assertEqual(len(make_payload(kind, 12345)), 12345)

    def test_recipe_reconstruction_is_exact(self):
        for kind in ("procedural", "repetitive", "random"):
            result = benchmark(kind, 4096, 1)
            self.assertTrue(result["recipe_reconstruction_exact"])

    def test_unknown_kind_fails(self):
        with self.assertRaises(ValueError):
            make_payload("not-a-workload", 10)

if __name__ == "__main__":
    unittest.main()
