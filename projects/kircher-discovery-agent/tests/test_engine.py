import unittest
from kda.engine import Claim, KircherDiscoveryAgent

class EngineTests(unittest.TestCase):
    def setUp(self):
        self.agent = KircherDiscoveryAgent([
            Claim("a", "graph motif", "represents", "edges", "graph theory", "synthetic source", ("finite graph",)),
            Claim("b", "graph motif", "represents", "interactions", "biology", "synthetic source", ("network model",)),
            Claim("c", "error correction", "can reduce", "channel errors", "information theory", "synthetic source", ("channel",)),
            Claim("d", "error correction", "can reduce", "reasoning errors", "AI", "synthetic hypothesis", ("task",)),
        ])
    def test_graph_has_nodes_and_edges(self):
        graph = self.agent.graph()
        self.assertGreaterEqual(len(graph["nodes"]), 4)
        self.assertEqual(len(graph["edges"]), 4)
    def test_cross_domain_candidates_require_shared_structure(self):
        candidates = self.agent.cross_domain_candidates()
        self.assertGreaterEqual(len(candidates), 2)
        self.assertTrue(all("not proof" in c.rationale for c in candidates))
    def test_duplicate_claim_rejected(self):
        with self.assertRaises(ValueError):
            self.agent.add_claim(self.agent.claims["a"])
    def test_conflict_conditions_are_not_overstated(self):
        agent = KircherDiscoveryAgent([
            Claim("x", "model", "score", "0.8", "eval", "synthetic", ("dataset v1",)),
            Claim("y", "model", "score", "0.6", "eval", "synthetic", ("dataset v2",)),
        ])
        self.assertFalse(agent.contradiction_candidates()[0]["possible_conflict"])
    def test_invalid_limit_rejected(self):
        with self.assertRaises(ValueError):
            self.agent.cross_domain_candidates(0)

if __name__ == "__main__":
    unittest.main()
