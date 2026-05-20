import shutil
import tempfile
import unittest
from pathlib import Path
from uuid import uuid4

from common import ROOT, run_cli


def write_staged_skill_fixture(name):
    review_dir = ROOT / "artifacts" / "skills" / "_TALLER" / "REVIEW" / name
    review_dir.mkdir(parents=True)
    (review_dir / "SKILL.md").write_text(
        f"""---
_manifest:
  urn: "urn:test:artefacto:{name}"
  type: artefacto
  provenance:
    created_by: "test"
    created_at: "2026-05-04"
    source: "test fixture"
version: "0.1.0"
status: activo
nombre: {name}
descripcion: "Skill fixture para probar transmutacion desde _TALLER/REVIEW."
tags: [test, transmute]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 1
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1, 1, 1, 1, 0]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [agentskills, codex]
    nivel_prescripcion: bajo
    conocimiento_permitido: []
artefacto:
  perfil:
    dominio: [test]
    disparadores:
      - "probar transmute"
    salidas:
      - "fixture transmutado"
  plan:
    estado_inicial: inicio
    estado_terminal: cierre
    estados: [inicio, cierre]
  interfaz:
    herramientas: [Read]
    permisos: "fixture"
    protocolos:
      entrada: "fixture"
      salida: "fixture"
  invariantes:
    reglas_duras:
      - "No usar fuera de tests."
---

# {name}

## Proposito

Fixture minima para verificar transmutacion y deploy desde REVIEW.
""",
        encoding="utf-8",
    )
    return review_dir


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
            "--force-paused",
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
        name = f"test-staged-skill-{uuid4().hex[:10]}"
        review_dir = write_staged_skill_fixture(name)
        try:
            result = run_cli(
                "transmute",
                "--target",
                "agentskills",
                "--agent",
                f"test/{name}",
                "--force-paused",
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            built = review_dir / "_BUILD" / "agentskills" / "SKILL.md"
            self.assertTrue(built.exists(), built)
            self.assertIn(f"name: {name}", built.read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(review_dir, ignore_errors=True)

    def test_deploy_staged_review_skill_to_temp_home(self):
        name = f"test-staged-skill-{uuid4().hex[:10]}"
        review_dir = write_staged_skill_fixture(name)
        try:
            transmute = run_cli(
                "transmute",
                "--target",
                "codex",
                "--agent",
                f"test/{name}",
                check=False,
            )
            self.assertEqual(transmute.returncode, 0, transmute.stderr or transmute.stdout)

            with tempfile.TemporaryDirectory() as tmp_home:
                result = run_cli(
                    "deploy-builds",
                    "--skill",
                    f"test/{name}",
                    "--target",
                    "codex",
                    "--home",
                    tmp_home,
                    "--apply",
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
                deployed = Path(tmp_home) / ".codex" / "skills" / name / "SKILL.md"
                self.assertTrue(deployed.exists(), deployed)
                self.assertIn(f"name: {name}", deployed.read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(review_dir, ignore_errors=True)

if __name__ == "__main__":
    unittest.main()
