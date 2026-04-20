import unittest
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

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

    def test_append_invocation_record_can_emit_retrieval_jsonl(self):
        with TemporaryDirectory() as tmpdir:
            generated_dir = Path(tmpdir)
            invocations_path = generated_dir / "invocations.jsonl"
            retrieval_path = generated_dir / "retrieval.jsonl"
            transmute_module.append_invocation_record(
                {
                    "agent_urn": "urn:salud:artefacto:urgenciologo",
                    "input_hash": "sha256:in",
                    "output_hash": "sha256:out",
                    "eval_result": "baseline",
                    "retrieval_urns": ["urn:salud:kb:me-dolor-toracico"],
                },
                path=invocations_path,
                retrieval_path=retrieval_path,
            )
            self.assertTrue(retrieval_path.exists(), retrieval_path)
            retrieval_content = retrieval_path.read_text(encoding="utf-8")
            self.assertIn('"urn:salud:kb:me-dolor-toracico"', retrieval_content)

    def test_build_deploy_status_report_detects_stale_claude_bundle(self):
        with TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            repo_root = tmp / "repo"
            agents_root = repo_root / "artifacts" / "agents" / "salud" / "urgenciologo"
            agents_root.mkdir(parents=True)
            agent_path = agents_root / "AGENT.md"
            agent_path.write_text(
                "---\n_manifest:\n  urn: urn:salud:artefacto:urgenciologo\n  type: artefacto\n  provenance:\n    created_by: test\n    created_at: '2026-04-20'\n    source: fixture\nversion: 1.0.0\nstatus: activo\nnombre: Urgenciologo\ndescripcion: fixture\nlang: es\nextensions:\n  kora:\n    vector_ontologico:\n      pi: 2\n      mu: 1\n      xi: 2\n      lambda: 0\n      phi: 1\n      sigma: [2,1,2,1,1]\n    presentacion: estado-primario\n    atlas:\n      arnes_categorico: persona\n      forma_material: agente-propiamente-tal\n    entornos_objetivo: [claude-code]\nartefacto:\n  plan:\n    estado_inicial: S-DISPATCHER\n    estado_terminal: S-END\n    estados:\n      - id: S-DISPATCHER\n        accion: x\n      - id: S-END\n        accion: y\n  perfil:\n    descripcion: fixture\n    dominio: [x]\n    disparadores: [x]\n    salidas: [x]\n  interfaz:\n    tools: []\n    permissions:\n      allow: []\n      deny: []\n  contexto:\n    memory:\n      mode: session\n  invariantes:\n    reglas_duras: [x]\n    compromisos_eticos:\n      safety_norm: Alta\n      fairness: Media\n      transparency: Alta\n      accountability: Alta\n      sustainability: Media\n---\n# Urgenciologo\n",
                encoding="utf-8",
            )
            claude_dir = tmp / "claude"
            claude_dir.mkdir()
            deployed = claude_dir / "urgenciologo.md"
            deployed.write_text(
                "---\nname: urgenciologo\ndescription: fixture\ntools: [Read]\nmodel: opus\ncolor: red\nmax_turns: 12\n---\n\n## Provenance\n\n- Source URN: `urn:salud:artefacto:urgenciologo`\n- Source Hash: `sha256:stale`\n- Transmuted At: `2026-04-20T00:00:00+00:00`\n",
                encoding="utf-8",
            )
            with patch.object(transmute_module, "KORA_ROOT", repo_root), patch.object(
                transmute_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ):
                report = transmute_module.build_deploy_status_report(claude_agents_dir=claude_dir)
            statuses = {item["agent"]: item for item in report["agents"]}
            self.assertEqual(statuses["salud/urgenciologo"]["claude-code"]["status"], "stale")

    def test_record_invocation_updates_verified_at_and_lead_time(self):
        with TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            kb_path = tmp / "dolor-toracico.md"
            kb_path.write_text(
                "---\n_manifest:\n  urn: urn:salud:kb:me-dolor-toracico\n  provenance:\n    created_by: test\n    created_at: '2026-04-20'\n    source: fixture\nversion: 1.0.0\nstatus: published\nlang: es\nextensions:\n  kora:\n    shard_index: 1\n    shard_count: 1\n    shard_root_urn: urn:salud:kb:me-dolor-toracico\n---\n\n# Dolor toracico\n",
                encoding="utf-8",
            )
            invocations = tmp / "invocations.jsonl"
            retrieval = tmp / "retrieval.jsonl"
            lead_time = tmp / "lead-time.jsonl"
            fixed_commit_ts = datetime(2026, 4, 20, 12, 0, tzinfo=timezone.utc)
            with patch.object(transmute_module, "_git_last_commit_ts", return_value=fixed_commit_ts):
                transmute_module.record_invocation(
                    agent_urn="urn:salud:artefacto:urgenciologo",
                    input_text="pregunta",
                    output_text="respuesta",
                    eval_result="baseline",
                    retrieval_urns=["urn:salud:kb:me-dolor-toracico"],
                    verified_paths=[kb_path],
                    source_paths=[kb_path],
                    invocations_path=invocations,
                    retrieval_path=retrieval,
                    lead_time_path=lead_time,
                )
            updated_frontmatter, _ = load_markdown_parts(kb_path)
            verified_at = ((updated_frontmatter.get("extensions") or {}).get("kora") or {}).get("verified_at")
            self.assertTrue(verified_at, updated_frontmatter)
            self.assertTrue(lead_time.exists(), lead_time)
            self.assertIn('"eval_result": "baseline"', lead_time.read_text(encoding="utf-8"))

    def test_stamp_verified_at_preserves_existing_shard_siblings(self):
        with TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            shard1 = tmp / "dolor-toracico.md"
            shard2 = tmp / "dolor-toracico--p02.md"
            content = (
                "---\n"
                "_manifest:\n"
                "  urn: urn:salud:kb:me-dolor-toracico\n"
                "  provenance:\n"
                "    created_by: test\n"
                "    created_at: '2026-04-20'\n"
                "    source: fixture\n"
                "version: 1.0.0\n"
                "status: published\n"
                "lang: es\n"
                "extensions:\n"
                "  kora:\n"
                "    shard_index: 1\n"
                "    shard_count: 2\n"
                "    shard_root_urn: urn:salud:kb:me-dolor-toracico\n"
                "---\n\n# Titulo\n"
            )
            shard1.write_text(content, encoding="utf-8")
            shard2.write_text(content.replace("shard_index: 1", "shard_index: 2"), encoding="utf-8")
            transmute_module.stamp_verified_at(shard1, timestamp=datetime(2026, 4, 20, 15, 0, tzinfo=timezone.utc))
            self.assertTrue(shard2.exists(), shard2)


if __name__ == "__main__":
    unittest.main()
