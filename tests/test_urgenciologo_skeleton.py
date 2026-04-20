import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from common import ROOT, run_cli
from kora_lib.artifacts import load_markdown_parts
from kora_lib import transmute as transmute_module


class UrgenciologoSkeletonTests(unittest.TestCase):
    def test_urgenciologo_productive_agent_exists(self):
        agent_path = ROOT / "artifacts" / "agents" / "salud" / "urgenciologo" / "AGENT.md"
        self.assertTrue(agent_path.exists(), agent_path)

    def test_med_emergencia_toc_cites_dolor_toracico(self):
        frontmatter, _ = load_markdown_parts(
            ROOT / "artifacts" / "knowledge" / "salud" / "med-emergencia" / "toc-body-of-knowledge.md"
        )
        relations = frontmatter.get("relations") or {}
        cites = relations.get("cites") or []
        self.assertIn("urn:salud:kb:me-dolor-toracico", cites)

    def test_transmute_claude_code_emits_deployable_bundle(self):
        result = run_cli("transmute", "--target", "claude-code", "--agent", "salud/urgenciologo", check=False)
        target_dir = ROOT / "artifacts" / "agents" / "salud" / "urgenciologo" / "_BUILD" / "claude-code"
        bundle_path = target_dir / "urgenciologo.md"
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertTrue(bundle_path.exists(), bundle_path)
        content = bundle_path.read_text(encoding="utf-8")
        self.assertIn("name:", content)
        self.assertIn("description:", content)
        self.assertIn("tools:", content)
        self.assertIn("- Read", content)
        self.assertIn("- Grep", content)
        self.assertIn("- Glob", content)

    def test_append_invocation_record_writes_jsonl(self):
        self.assertTrue(
            hasattr(transmute_module, "append_invocation_record"),
            "append_invocation_record missing from kora_lib.transmute",
        )
        with TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "invocations.jsonl"
            transmute_module.append_invocation_record(
                {
                    "agent_urn": "urn:salud:artefacto:urgenciologo",
                    "input_hash": "sha256:in",
                    "output_hash": "sha256:out",
                    "eval_result": "baseline",
                },
                path=log_path,
            )
            content = log_path.read_text(encoding="utf-8")
            self.assertIn('"agent_urn": "urn:salud:artefacto:urgenciologo"', content)


if __name__ == "__main__":
    unittest.main()
