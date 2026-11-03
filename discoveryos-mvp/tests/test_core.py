import unittest

from discoveryos.core import analyze_case


class AnalyzeCaseTests(unittest.TestCase):
    def test_detects_candidate_contradiction_and_emits_question(self):
        report = analyze_case({
            "case_id": "test",
            "claims": [
                {"id": "a", "text": "Battery storage improves grid reliability", "source": "s1", "confidence": 0.8},
                {"id": "b", "text": "Battery storage does not improve grid reliability", "source": "s2", "confidence": 0.4},
            ],
        })
        self.assertEqual(report["summary"]["claim_count"], 2)
        self.assertEqual(report["summary"]["candidate_contradiction_count"], 1)
        self.assertTrue(report["hypotheses_to_test"])
        self.assertTrue(any("distinguish claim a from claim b" in q for q in report["follow_up_questions"]))

    def test_empty_case_requests_research_question(self):
        report = analyze_case({"claims": []})
        self.assertEqual(report["summary"]["claim_count"], 0)
        self.assertTrue(report["follow_up_questions"])

    def test_rejects_duplicate_ids(self):
        with self.assertRaisesRegex(ValueError, "unique"):
            analyze_case({"claims": [
                {"id": "x", "text": "One claim", "source": "s1"},
                {"id": "x", "text": "Another claim", "source": "s2"},
            ]})

    def test_rejects_invalid_confidence(self):
        with self.assertRaisesRegex(ValueError, "between 0 and 1"):
            analyze_case({"claims": [
                {"id": "x", "text": "One claim", "source": "s1", "confidence": 2}
            ]})


if __name__ == "__main__":
    unittest.main()
