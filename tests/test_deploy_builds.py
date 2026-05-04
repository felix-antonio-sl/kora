import tempfile
import unittest
from pathlib import Path

from common import ROOT, run_cli


class DeployBuildsTests(unittest.TestCase):
    def test_deploy_skill_to_codex_home(self):
        transmute = run_cli(
            "transmute",
            "--target",
            "codex",
            "--agent",
            "kora/jointjs-open-source",
            check=False,
        )
        self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

        with tempfile.TemporaryDirectory() as tmp_home:
            result = run_cli(
                "deploy-builds",
                "--skill",
                "kora/jointjs-open-source",
                "--target",
                "codex",
                "--home",
                tmp_home,
                "--apply",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            deployed = Path(tmp_home) / ".codex" / "skills" / "jointjs-open-source" / "SKILL.md"
            self.assertTrue(deployed.exists(), deployed)
            self.assertIn("name: jointjs-open-source", deployed.read_text(encoding="utf-8"))

    def test_deploy_agent_to_opencode_home(self):
        transmute = run_cli(
            "transmute",
            "--target",
            "opencode",
            "--agent",
            "dev/steipete",
            check=False,
        )
        self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

        with tempfile.TemporaryDirectory() as tmp_home:
            result = run_cli(
                "deploy-builds",
                "--agent",
                "dev/steipete",
                "--target",
                "opencode",
                "--home",
                tmp_home,
                "--apply",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            deployed = Path(tmp_home) / ".config" / "opencode" / "agents" / "steipete.md"
            self.assertTrue(deployed.exists(), deployed)
            body = deployed.read_text(encoding="utf-8")
            self.assertIn("mode:", body)
            self.assertIn("## Instructions", body)

    def test_deploy_openclaw_agent_preserves_runtime_state(self):
        transmute = run_cli(
            "transmute",
            "--target",
            "openclaw",
            "--agent",
            "dev/steipete",
            check=False,
        )
        self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

        with tempfile.TemporaryDirectory() as tmp_home:
            runtime_memory = (
                Path(tmp_home)
                / "openclaw-fleet"
                / "workspaces"
                / "steipete"
                / "memory"
                / "runtime.md"
            )
            runtime_memory.parent.mkdir(parents=True, exist_ok=True)
            runtime_memory.write_text("runtime state\n", encoding="utf-8")

            result = run_cli(
                "deploy-builds",
                "--agent",
                "dev/steipete",
                "--target",
                "openclaw",
                "--home",
                tmp_home,
                "--apply",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            workspace = Path(tmp_home) / "openclaw-fleet" / "workspaces" / "steipete"
            self.assertTrue((workspace / "AGENTS.md").exists())
            self.assertEqual(runtime_memory.read_text(encoding="utf-8"), "runtime state\n")

    def test_deploy_openclaw_skill_uses_workspace_destination(self):
        transmute = run_cli(
            "transmute",
            "--target",
            "openclaw",
            "--agent",
            "kora/jointjs-open-source",
            check=False,
        )
        self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

        with tempfile.TemporaryDirectory() as tmp_home:
            result = run_cli(
                "deploy-builds",
                "--skill",
                "kora/jointjs-open-source",
                "--target",
                "openclaw",
                "--openclaw-workspace",
                "steipete",
                "--home",
                tmp_home,
                "--apply",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            deployed = (
                Path(tmp_home)
                / "openclaw-fleet"
                / "workspaces"
                / "steipete"
                / "skills"
                / "jointjs-open-source"
                / "SKILL.md"
            )
            self.assertTrue(deployed.exists(), deployed)
            self.assertIn("name: jointjs-open-source", deployed.read_text(encoding="utf-8"))

    def test_dry_run_does_not_write_files(self):
        transmute = run_cli(
            "transmute",
            "--target",
            "claude-code",
            "--agent",
            "kora/jointjs-open-source",
            check=False,
        )
        self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

        with tempfile.TemporaryDirectory() as tmp_home:
            result = run_cli(
                "deploy-builds",
                "--skill",
                "kora/jointjs-open-source",
                "--target",
                "claude-code",
                "--home",
                tmp_home,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            self.assertIn("Dry-run complete", result.stdout)
            self.assertFalse((Path(tmp_home) / ".claude").exists())

    def test_deploy_requires_explicit_target(self):
        result = run_cli(
            "deploy-builds",
            "--skill",
            "kora/jointjs-open-source",
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--target", result.stderr)

    def test_apply_blocks_overwrite_without_flag(self):
        transmute = run_cli(
            "transmute",
            "--target",
            "codex",
            "--agent",
            "kora/jointjs-open-source",
            check=False,
        )
        self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

        with tempfile.TemporaryDirectory() as tmp_home:
            deployed = Path(tmp_home) / ".codex" / "skills" / "jointjs-open-source" / "SKILL.md"
            deployed.parent.mkdir(parents=True, exist_ok=True)
            deployed.write_text("local runtime edit\n", encoding="utf-8")

            blocked = run_cli(
                "deploy-builds",
                "--skill",
                "kora/jointjs-open-source",
                "--target",
                "codex",
                "--home",
                tmp_home,
                "--apply",
                check=False,
            )
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("Refusing to overwrite", blocked.stderr)
            self.assertEqual(deployed.read_text(encoding="utf-8"), "local runtime edit\n")

            overwritten = run_cli(
                "deploy-builds",
                "--skill",
                "kora/jointjs-open-source",
                "--target",
                "codex",
                "--home",
                tmp_home,
                "--apply",
                "--overwrite",
                check=False,
            )
            self.assertEqual(overwritten.returncode, 0, overwritten.stderr or overwritten.stdout)
            self.assertIn("name: jointjs-open-source", deployed.read_text(encoding="utf-8"))

    def test_transmute_staged_review_skill_by_urn_ref(self):
        result = run_cli(
            "transmute",
            "--target",
            "agentskills",
            "--agent",
            "kora/kora-skills",
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

        built = (
            ROOT
            / "artifacts"
            / "skills"
            / "_TALLER"
            / "REVIEW"
            / "kora-skills"
            / "_BUILD"
            / "agentskills"
            / "SKILL.md"
        )
        self.assertTrue(built.exists(), built)
        self.assertIn("name: kora-skills", built.read_text(encoding="utf-8"))

    def test_deploy_staged_review_skill_to_temp_home(self):
        transmute = run_cli(
            "transmute",
            "--target",
            "codex",
            "--agent",
            "kora/kora-agents",
            check=False,
        )
        self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

        with tempfile.TemporaryDirectory() as tmp_home:
            result = run_cli(
                "deploy-builds",
                "--skill",
                "kora/kora-agents",
                "--target",
                "codex",
                "--home",
                tmp_home,
                "--apply",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            deployed = Path(tmp_home) / ".codex" / "skills" / "kora-agents" / "SKILL.md"
            self.assertTrue(deployed.exists(), deployed)
            self.assertIn("name: kora-agents", deployed.read_text(encoding="utf-8"))

    def test_rebuild_required_skill_path_is_not_transmutable_source(self):
        legacy = (
            ROOT
            / "artifacts"
            / "skills"
            / "_TALLER"
            / "INBOX"
            / "_rebuild_required"
            / "2026-05-03"
            / "kora"
            / "kora-skills"
        )
        result = run_cli(
            "transmute",
            "--target",
            "agentskills",
            "--agent",
            str(legacy),
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not an active source", result.stderr)


if __name__ == "__main__":
    unittest.main()
