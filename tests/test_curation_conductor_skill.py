import unittest

from common import ROOT
from kora_lib.artifacts import load_yaml_safe


class CurationConductorSkillTests(unittest.TestCase):
    def test_curation_conductor_is_removed_from_productive_skills(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "SKILL.md"
        self.assertFalse(skill_path.exists(), skill_path)

    def test_curation_conductor_is_quarantined_for_rebuild(self):
        skill_path = (
            ROOT
            / "artifacts"
            / "skills"
            / "_TALLER"
            / "INBOX"
            / "_rebuild_required"
            / "2026-05-03"
            / "kora"
            / "curation-conductor"
            / "SKILL.md"
        )
        doc, err = load_yaml_safe(skill_path)
        self.assertIsNone(err)
        self.assertEqual(doc["status"], "retirado")
        self.assertEqual(
            doc["extensions"]["kora"]["rebuild"]["directive"],
            "urn:kora:kb:meta-kora-rebuild-directive",
        )
        self.assertFalse(doc["extensions"]["kora"]["rebuild"]["current_is_source"])


if __name__ == "__main__":
    unittest.main()
