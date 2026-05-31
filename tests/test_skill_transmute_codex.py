import unittest
from pathlib import Path

from common import ROOT, run_cli
from toolchain.kora_lib.transmute import _strip_inline_knowledge_contract


class CodexSkillTransmuteTests(unittest.TestCase):
    def test_transmute_codex_accepts_productive_skill(self):
        result = run_cli("transmute", "--target", "codex", "--agent", "kora/jointjs-open-source", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Bundle:", result.stdout)

        target_dir = ROOT / "artifacts" / "skills" / "kora" / "jointjs-open-source" / "_BUILD" / "codex"
        manifest_path = target_dir / "_transmutation.yml"
        bundle_path = target_dir / "jointjs-open-source" / "SKILL.md"

        self.assertTrue(manifest_path.exists(), manifest_path)
        self.assertTrue(bundle_path.exists(), bundle_path)

        manifest = manifest_path.read_text(encoding="utf-8")
        self.assertIn("source_urn: urn:kora:artefacto:jointjs-open-source", manifest)
        self.assertIn("target: codex", manifest)

        bundle = bundle_path.read_text(encoding="utf-8")
        self.assertIn("name: jointjs-open-source", bundle)
        self.assertIn("description:", bundle)
        self.assertIn("https://docs.jointjs.com/", bundle)
        self.assertIn("## Knowledge Contract", bundle)
        self.assertIn("urn:kora:kb:catalogo-patrones-skills", bundle)

    def test_strip_inline_knowledge_contract(self):
        body = "## Operacion\n\nContenido.\n\n## Knowledge Contract\n\nContrato legado.\n"

        projected = _strip_inline_knowledge_contract(body)

        self.assertIn("## Operacion", projected)
        self.assertNotIn("## Knowledge Contract", projected)


if __name__ == "__main__":
    unittest.main()
