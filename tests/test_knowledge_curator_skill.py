import unittest

from common import ROOT
from kora_lib.artifacts import load_yaml_safe


class KnowledgeCuratorSkillTests(unittest.TestCase):
    def test_knowledge_curator_is_marked_for_rebuild(self):
        skill_path = ROOT / "artifacts" / "skills" / "_TALLER" / "INBOX" / "knowledge-curator" / "SKILL.md"
        doc, err = load_yaml_safe(skill_path)
        self.assertIsNone(err)
        self.assertEqual(doc["status"], "retirado")
        self.assertFalse(doc["extensions"]["kora"]["rebuild"]["current_is_source"])
        self.assertEqual(
            doc["extensions"]["kora"]["rebuild"]["directive"],
            "urn:kora:kb:meta-kora-rebuild-directive",
        )

    def test_productive_curation_conductor_is_absent(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "SKILL.md"
        self.assertFalse(skill_path.exists(), skill_path)


if __name__ == "__main__":
    unittest.main()
