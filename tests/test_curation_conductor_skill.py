import unittest
from pathlib import Path

from common import ROOT


class CurationConductorSkillTests(unittest.TestCase):
    def test_curation_conductor_skill_exists(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "SKILL.md"
        self.assertTrue(skill_path.exists(), skill_path)

    def test_curation_conductor_references_exist(self):
        base = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "referencias"
        self.assertTrue((base / "process-map.md").exists())
        self.assertTrue((base / "family-decision-table.md").exists())

    def test_curation_conductor_declares_atomic_as_specialized_route(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        self.assertIn("No usar `atomic` como curación universal.", text)
        self.assertIn("`atomic` -> usar `atomize`", text)

    def test_curation_conductor_reroutes_spec_like_inputs(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "SKILL.md"
        process_path = (
            ROOT
            / "artifacts"
            / "skills"
            / "kora"
            / "curation-conductor"
            / "referencias"
            / "process-map.md"
        )
        self.assertIn("reroute", skill_path.read_text(encoding="utf-8"))
        self.assertIn("rerouted_to_spec", process_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
