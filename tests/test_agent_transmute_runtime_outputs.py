import unittest

from common import ROOT, run_cli


class AgentRuntimeOutputTransmuteTests(unittest.TestCase):
    def test_transmute_codex_emits_agent_markdown(self):
        result = run_cli("transmute", "--target", "codex", "--agent", "kora/custodio", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Bundle:", result.stdout)

        target_dir = ROOT / "artifacts" / "agents" / "kora" / "custodio" / "_BUILD" / "codex"
        self.assertTrue((target_dir / "_transmutation.yml").exists())
        bundle_path = target_dir / "custodio.md"
        self.assertTrue(bundle_path.exists(), bundle_path)
        bundle = bundle_path.read_text(encoding="utf-8")
        self.assertIn("runtime: codex", bundle)
        self.assertIn("## Instructions", bundle)

    def test_transmute_opencode_emits_agent_markdown(self):
        result = run_cli("transmute", "--target", "opencode", "--agent", "kora/custodio", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Agent:", result.stdout)

        target_dir = ROOT / "artifacts" / "agents" / "kora" / "custodio" / "_BUILD" / "opencode"
        self.assertTrue((target_dir / "_transmutation.yml").exists())
        bundle_path = target_dir / "agents" / "custodio.md"
        self.assertTrue(bundle_path.exists(), bundle_path)
        bundle = bundle_path.read_text(encoding="utf-8")
        self.assertIn("mode:", bundle)
        self.assertIn("## Instructions", bundle)

    def test_transmute_openclaw_emits_workspace_markdown(self):
        result = run_cli("transmute", "--target", "openclaw", "--agent", "kora/custodio", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Workspace:", result.stdout)

        target_dir = ROOT / "artifacts" / "agents" / "kora" / "custodio" / "_BUILD" / "openclaw"
        self.assertTrue((target_dir / "_transmutation.yml").exists())
        for rel in (
            "workspace/AGENTS.md",
            "workspace/SOUL.md",
            "workspace/IDENTITY.md",
            "workspace/USER.md",
            "workspace/TOOLS.md",
            "workspace/BOOT.md",
            "workspace/MEMORY.md",
            "config/openclaw.json5",
            "DEPLOY.md",
        ):
            self.assertTrue((target_dir / rel).exists(), rel)
        agents_md = (target_dir / "workspace" / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("## Instructions", agents_md)


if __name__ == "__main__":
    unittest.main()
