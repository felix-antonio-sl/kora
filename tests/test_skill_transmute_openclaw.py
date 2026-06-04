import unittest

from common import ROOT, run_cli


class OpenClawSkillTransmuteTests(unittest.TestCase):
    def test_transmute_skill_bundles_include_source_provenance(self):
        target_specs = (
            ("claude-code", ("claude-code", "jointjs-open-source", "SKILL.md")),
            ("codex", ("codex", "jointjs-open-source", "SKILL.md")),
            ("opencode", ("opencode", "jointjs-open-source", "SKILL.md")),
            ("openclaw", ("openclaw", "skills", "jointjs-open-source", "SKILL.md")),
        )
        skill_root = ROOT / "artifacts" / "skills" / "kora" / "jointjs-open-source"

        for target, rel_parts in target_specs:
            with self.subTest(target=target):
                result = run_cli("transmute", "--target", target, "--agent", "kora/jointjs-open-source", check=False)
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

                bundle = (skill_root / "_BUILD").joinpath(*rel_parts).read_text(encoding="utf-8")
                self.assertIn("## Provenance", bundle)
                self.assertIn("- Source URN: `urn:kora:artefacto:jointjs-open-source`", bundle)
                self.assertIn("- Source Hash: `sha256:", bundle)

    def test_transmute_openclaw_accepts_productive_skill(self):
        result = run_cli("transmute", "--target", "openclaw", "--agent", "kora/jointjs-open-source", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Bundle:", result.stdout)

        target_dir = ROOT / "artifacts" / "skills" / "kora" / "jointjs-open-source" / "_BUILD" / "openclaw"
        manifest_path = target_dir / "_transmutation.yml"
        bundle_path = target_dir / "skills" / "jointjs-open-source" / "SKILL.md"

        self.assertTrue(manifest_path.exists(), manifest_path)
        self.assertTrue(bundle_path.exists(), bundle_path)

        manifest = manifest_path.read_text(encoding="utf-8")
        self.assertIn("source_urn: urn:kora:artefacto:jointjs-open-source", manifest)
        self.assertIn("target: openclaw", manifest)

        bundle = bundle_path.read_text(encoding="utf-8")
        self.assertIn("name: jointjs-open-source", bundle)
        self.assertIn("description:", bundle)
        self.assertIn("https://docs.jointjs.com/", bundle)


if __name__ == "__main__":
    unittest.main()
