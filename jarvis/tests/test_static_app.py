import pathlib
import re
import unittest

APP = pathlib.Path(__file__).resolve().parents[1] / "index.html"

class StaticAppSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = APP.read_text(encoding="utf-8")

    def test_html_has_required_sections(self):
        for section in ("overview", "projects", "lab", "experiments", "opportunities", "settings"):
            with self.subTest(section=section):
                self.assertIn(f'id="view-{section}"', self.html)

    def test_core_forms_and_data_backup_exist(self):
        for marker in ("projectForm", "hypothesisForm", "experimentForm", "opportunityForm",
                       "exportData", "importFile", "localStorage", "function score"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.html)

    def test_opportunity_score_weights_sum_to_100(self):
        weights = [30, 35, 20, 15]
        self.assertEqual(sum(weights), 100)
        self.assertRegex(self.html, r"\(\(o\.value/5\)\*30\+\(o\.evidence/5\)\*35\+\(o\.speed/5\)\*20\+\(\(5-o\.effort\)/5\)\*15\)")

    def test_dangerous_claims_not_present(self):
        self.assertIn("not a connected large language model", self.html)
        self.assertIn("not configured", self.html.lower())

    def test_script_is_closed(self):
        self.assertIn("</script>", self.html)
        self.assertIn("</html>", self.html)

if __name__ == "__main__":
    unittest.main()
