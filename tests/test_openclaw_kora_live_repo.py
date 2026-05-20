import unittest

import yaml

from common import ROOT, run_cli
from kora_lib.artifacts import load_yaml_safe


CONTAINER_KORA_MOUNT = "/" + "home/node/repos/kora"


class OpenClawKoraLiveRepoTests(unittest.TestCase):
    def test_salud_agents_declare_live_kora_repo_access(self):
        for agent_name in ("salubrista", "urgenciologo"):
            doc, err = load_yaml_safe(
                ROOT / "artifacts" / "agents" / "salud" / agent_name / "AGENT.md"
            )
            self.assertIsNone(err)
            openclaw = doc["extensions"]["openclaw"]
            self.assertTrue(openclaw["kora_repo_required"])
            self.assertEqual(openclaw["kora_repo_env"], "KORA_REPO")
            self.assertEqual(openclaw["kora_repo_mount"], CONTAINER_KORA_MOUNT)
            self.assertEqual(openclaw["knowledge_mount_strategy"], "bind_mount_live_kora_clone")
            self.assertEqual(openclaw["knowledge_mount_mode"], "ro")

    def test_salubrista_declares_codex_target(self):
        doc, err = load_yaml_safe(ROOT / "artifacts" / "agents" / "salud" / "salubrista" / "AGENT.md")
        self.assertIsNone(err)
        self.assertIn("codex", doc["extensions"]["kora"]["entornos_objetivo"])
        self.assertIn("codex", doc["extensions"])

    def test_openclaw_runtime_and_ops_docs_capture_live_repo_contract(self):
        runtime = (ROOT / "runtime" / "openclaw-runtime-extension.md").read_text(encoding="utf-8")
        principles = (
            ROOT / "artifacts" / "knowledge" / "ops" / "principios-transmutacion-kora-openclaw.md"
        ).read_text(encoding="utf-8")
        memory = (
            ROOT / "governance" / "decisiones-archivadas" / "handoffs-historicos"
            / "operational-memory-2026-04-27-openclaw-kora-live-kb.md"
        ).read_text(encoding="utf-8")

        for content in (runtime, principles, memory):
            self.assertIn("bind_mount_live_kora_clone", content)
            self.assertIn("KORA_REPO", content)
            self.assertIn(CONTAINER_KORA_MOUNT, content)
            self.assertIn("artifacts/knowledge", content)

    def test_openclaw_transmutation_manifest_includes_kora_repo_access(self):
        result = run_cli("transmute", "--target", "openclaw", "--agent", "salud/salubrista", check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

        manifest_path = (
            ROOT
            / "artifacts"
            / "agents"
            / "salud"
            / "salubrista"
            / "_BUILD"
            / "openclaw"
            / "_transmutation.yml"
        )
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        access = manifest["transmutation"]["kora_repo_access"]
        self.assertTrue(access["required"])
        self.assertEqual(access["host_env"], "KORA_REPO")
        self.assertEqual(access["container_mount"], CONTAINER_KORA_MOUNT)
        self.assertEqual(access["sync_strategy"], "bind_mount_live_kora_clone")
        self.assertEqual(access["knowledge_root"], "artifacts/knowledge")


if __name__ == "__main__":
    unittest.main()
