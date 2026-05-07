import unittest

from common import agent_workspace_path, run_cli


class AgentRuntimeOutputTransmuteTests(unittest.TestCase):
    def test_transmute_codex_emits_skill_bundle(self):
        # Codex CLI does not load ~/.codex/agents/. Personas project as skills.
        result = run_cli("transmute", "--target", "codex", "--agent", "dev/steipete", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Bundle:", result.stdout)

        target_dir = agent_workspace_path("dev/steipete") / "_BUILD" / "codex"
        self.assertTrue((target_dir / "_transmutation.yml").exists())
        bundle_path = target_dir / "steipete" / "SKILL.md"
        self.assertTrue(bundle_path.exists(), bundle_path)
        bundle = bundle_path.read_text(encoding="utf-8")
        self.assertIn("runtime: codex", bundle)
        self.assertIn("## Instructions", bundle)
        self.assertTrue((target_dir / "steipete" / "agents" / "openai.yaml").exists())

    def test_transmute_opencode_aborts_as_paused_target(self):
        result = run_cli("transmute", "--target", "opencode", "--agent", "dev/steipete", check=False)
        self.assertNotEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("esta en pausa", result.stderr)

    def test_transmute_opencode_with_force_paused_proceeds(self):
        result = run_cli("transmute", "--target", "opencode", "--agent", "dev/steipete", "--force-paused", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Agent:", result.stdout)

        target_dir = agent_workspace_path("dev/steipete") / "_BUILD" / "opencode"
        self.assertTrue((target_dir / "_transmutation.yml").exists())
        bundle_path = target_dir / "agents" / "steipete.md"
        self.assertTrue(bundle_path.exists(), bundle_path)
        bundle = bundle_path.read_text(encoding="utf-8")
        self.assertIn("mode:", bundle)
        self.assertIn("## Instructions", bundle)

    def test_transmute_openclaw_emits_workspace_markdown(self):
        result = run_cli("transmute", "--target", "openclaw", "--agent", "dev/steipete", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("Manifest:", result.stdout)
        self.assertIn("Workspace:", result.stdout)

        target_dir = agent_workspace_path("dev/steipete") / "_BUILD" / "openclaw"
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
