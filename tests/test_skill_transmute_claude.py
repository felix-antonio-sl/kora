import unittest
from pathlib import Path

from common import ROOT, run_cli


class ClaudeSkillTransmuteTests(unittest.TestCase):
    def test_transmute_claude_code_accepts_productive_skill(self):
        result = run_cli("transmute", "--target", "claude-code", "--agent", "kora/jointjs-open-source", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Bundle:", result.stdout)

        target_dir = ROOT / "artifacts" / "skills" / "kora" / "jointjs-open-source" / "_BUILD" / "claude-code"
        manifest_path = target_dir / "_transmutation.yml"
        bundle_path = target_dir / "jointjs-open-source" / "SKILL.md"

        self.assertTrue(manifest_path.exists(), manifest_path)
        self.assertTrue(bundle_path.exists(), bundle_path)

        manifest = manifest_path.read_text(encoding="utf-8")
        self.assertIn("source_urn: urn:kora:artefacto:jointjs-open-source", manifest)
        self.assertIn("target: claude-code", manifest)

        bundle = bundle_path.read_text(encoding="utf-8")
        self.assertIn("name: jointjs-open-source", bundle)
        self.assertIn("description:", bundle)
        self.assertIn("https://docs.jointjs.com/", bundle)


if __name__ == "__main__":
    unittest.main()
