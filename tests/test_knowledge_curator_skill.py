import unittest
from pathlib import Path

from common import ROOT


class KnowledgeCuratorSkillTests(unittest.TestCase):
    def test_knowledge_curator_skill_exists(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "knowledge-curator" / "SKILL.md"
        self.assertTrue(skill_path.exists(), skill_path)

    def test_knowledge_curator_references_exist(self):
        base = ROOT / "artifacts" / "skills" / "kora" / "knowledge-curator" / "referencias"
        self.assertTrue((base / "workflow-map.md").exists())
        self.assertTrue((base / "handoff-contract.md").exists())

    def test_knowledge_curator_is_kb_normal_only_and_reroutes_other_paths(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "knowledge-curator" / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        self.assertIn("Opera solo la ruta descriptiva `KB normal`.", text)
        self.assertIn("Si el diagnostico indica `atomic`, devolver handoff a `atomize`.", text)
        self.assertIn(
            "Si el material es prescriptivo, fundacional o de gobierno, devolver `rerouted_to_spec`.",
            text,
        )

    def test_knowledge_curator_implements_curator_subflows(self):
        workflow_path = (
            ROOT
            / "artifacts"
            / "skills"
            / "kora"
            / "knowledge-curator"
            / "referencias"
            / "workflow-map.md"
        )
        text = workflow_path.read_text(encoding="utf-8")
        self.assertIn("CM-ARTIFACT-DESIGNER", text)
        self.assertIn("CM-KORAFICATOR", text)
        self.assertIn("CM-ARTIFACT-AUDITOR", text)
        self.assertIn("CM-LIFECYCLE-ORCHESTRATOR", text)

    def test_curation_conductor_routes_kb_normal_to_knowledge_curator(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "SKILL.md"
        table_path = (
            ROOT
            / "artifacts"
            / "skills"
            / "kora"
            / "curation-conductor"
            / "referencias"
            / "family-decision-table.md"
        )
        self.assertIn("`KB normal` -> usar `knowledge-curator`", skill_path.read_text(encoding="utf-8"))
        self.assertIn("knowledge-curator", table_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
