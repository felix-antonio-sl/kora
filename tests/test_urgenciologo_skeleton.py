import unittest
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from textwrap import dedent
from unittest.mock import patch

from common import ROOT, run_cli
from kora_lib.artifacts import load_markdown_parts
from kora_lib import transmute as transmute_module
from kora_lib import workspaces as workspaces_module


class UrgenciologoSkeletonTests(unittest.TestCase):
    def _write_agent_fixture(self, agent_path: Path, targets: list[str]) -> None:
        targets_yaml = ", ".join(targets)
        agent_path.write_text(
            dedent(
                f"""\
                ---
                _manifest:
                  urn: urn:salud:artefacto:urgenciologo
                  type: artefacto
                  provenance:
                    created_by: test
                    created_at: '2026-04-20'
                    source: fixture
                version: 1.0.0
                status: activo
                nombre: Urgenciologo
                descripcion: fixture
                lang: es
                extensions:
                  kora:
                    vector_ontologico:
                      pi: 2
                      mu: 1
                      xi: 2
                      lambda: 0
                      phi: 1
                      sigma: [2,1,2,1,1]
                    presentacion: estado-primario
                    atlas:
                      arnes_categorico: persona
                      forma_material: agente-propiamente-tal
                    entornos_objetivo: [{targets_yaml}]
                artefacto:
                  plan:
                    estado_inicial: S-DISPATCHER
                    estado_terminal: S-END
                    estados:
                      - id: S-DISPATCHER
                        accion: x
                      - id: S-END
                        accion: y
                  perfil:
                    descripcion: fixture
                    dominio: [x]
                    disparadores: [x]
                    salidas: [x]
                  interfaz:
                    tools: []
                    permissions:
                      allow: []
                      deny: []
                  contexto:
                    memory:
                      mode: session
                  invariantes:
                    reglas_duras: [x]
                    compromisos_eticos:
                      safety_norm: Alta
                      fairness: Media
                      transparency: Alta
                      accountability: Alta
                      sustainability: Media
                ---
                # Urgenciologo
                """
            ),
            encoding="utf-8",
        )

    def _write_skill_fixture(self, skill_path: Path, targets: list[str]) -> None:
        targets_yaml = ", ".join(targets)
        skill_path.write_text(
            dedent(
                f"""\
                ---
                _manifest:
                  urn: urn:kora:artefacto:test-skill
                  type: artefacto
                  provenance:
                    created_by: test
                    created_at: '2026-04-20'
                    source: fixture
                version: 1.0.0
                status: activo
                nombre: test-skill
                descripcion: fixture
                lang: es
                extensions:
                  kora:
                    vector_ontologico:
                      pi: 2
                      mu: 0
                      xi: 2
                      lambda: 0
                      phi: 1
                      sigma: [2,1,2,1,1]
                    presentacion: accion-primaria
                    atlas:
                      arnes_categorico: disciplina
                      forma_material: habilidad
                    entornos_objetivo: [{targets_yaml}]
                artefacto:
                  perfil:
                    dominio: [test]
                    disparadores: [test]
                    salidas: [test]
                  plan:
                    estado_inicial: S-START
                    estado_terminal: S-END
                    estados:
                      - id: S-START
                        accion: test
                      - id: S-END
                        accion: done
                  interfaz:
                    herramientas: []
                    permisos: test
                  invariantes:
                    reglas_duras: [test]
                    compromisos_eticos:
                      transparencia: test
                ---
                # test-skill
                """
            ),
            encoding="utf-8",
        )

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
        self.assertIn("## Knowledge Contract", content)
        self.assertIn("urn:salud:kb:me-dolor-toracico", content)
        self.assertIn("artifacts/knowledge/salud/med-emergencia/dolor-toracico.md", content)

    def test_transmute_yml_contains_resolved_knowledge_contract(self):
        result = run_cli("transmute", "--target", "claude-code", "--agent", "salud/urgenciologo", check=False)
        target_dir = ROOT / "artifacts" / "agents" / "salud" / "urgenciologo" / "_BUILD" / "claude-code"
        manifest_path = target_dir / "_transmutation.yml"
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertTrue(manifest_path.exists(), manifest_path)
        manifest = manifest_path.read_text(encoding="utf-8")
        self.assertIn("knowledge_contract:", manifest)
        self.assertIn("allowed_urns:", manifest)
        self.assertIn("routes:", manifest)
        self.assertIn("urn:salud:kb:me-dolor-toracico", manifest)
        self.assertIn("artifacts/knowledge/salud/med-emergencia/dolor-toracico.md", manifest)

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
            self._write_agent_fixture(agent_path, ["claude-code"])
            claude_dir = tmp / "claude"
            claude_dir.mkdir()
            deployed = claude_dir / "urgenciologo.md"
            deployed.write_text(
                "---\nname: urgenciologo\ndescription: fixture\ntools: [Read]\nmodel: opus\ncolor: red\nmax_turns: 12\n---\n\n## Provenance\n\n- Source URN: `urn:salud:artefacto:urgenciologo`\n- Source Hash: `sha256:stale`\n- Transmuted At: `2026-04-20T00:00:00+00:00`\n",
                encoding="utf-8",
            )
            with patch.object(transmute_module, "KORA_ROOT", repo_root), patch.object(
                transmute_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ), patch.object(
                transmute_module, "SKILLS_ROOT", repo_root / "artifacts" / "skills"
            ), patch.object(
                workspaces_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ):
                report = transmute_module.build_deploy_status_report(claude_agents_dir=claude_dir)
            statuses = {item["agent"]: item for item in report["agents"]}
            self.assertEqual(statuses["salud/urgenciologo"]["claude-code"]["status"], "stale")

    def test_build_deploy_status_report_audits_openclaw_workspace_agents_md(self):
        with TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            repo_root = tmp / "repo"
            agents_root = repo_root / "artifacts" / "agents" / "salud" / "urgenciologo"
            agents_root.mkdir(parents=True)
            agent_path = agents_root / "AGENT.md"
            self._write_agent_fixture(agent_path, ["openclaw"])

            openclaw_dir = tmp / "openclaw"
            workspace = openclaw_dir / "urgenciologo"
            workspace.mkdir(parents=True)
            deployed = workspace / "AGENTS.md"
            current_hash = transmute_module._sha256(agent_path)
            deployed.write_text(
                "## Provenance\n\n"
                "- Source URN: `urn:salud:artefacto:urgenciologo`\n"
                f"- Source Hash: `{current_hash}`\n"
                "- Transmuted At: `2026-04-20T00:00:00+00:00`\n",
                encoding="utf-8",
            )

            with patch.object(transmute_module, "KORA_ROOT", repo_root), patch.object(
                transmute_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ), patch.object(
                transmute_module, "SKILLS_ROOT", repo_root / "artifacts" / "skills"
            ), patch.object(
                workspaces_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ):
                report = transmute_module.build_deploy_status_report(
                    openclaw_workspaces_dir=openclaw_dir,
                )

            statuses = {item["agent"]: item for item in report["agents"]}
            status = statuses["salud/urgenciologo"]["openclaw"]
            self.assertEqual(status["status"], "ok")
            self.assertEqual(status["path"], str(deployed))
            self.assertEqual(status["workspace_path"], str(workspace))

    def test_build_deploy_status_report_uses_openclaw_workspace_path_alias(self):
        with TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            repo_root = tmp / "repo"
            agents_root = repo_root / "artifacts" / "agents" / "salud" / "urgenciologo"
            agents_root.mkdir(parents=True)
            agent_path = agents_root / "AGENT.md"
            self._write_agent_fixture(agent_path, ["openclaw"])

            frontmatter, body = load_markdown_parts(agent_path)
            frontmatter.setdefault("extensions", {})["openclaw"] = {
                "agent_id": "hospitalista",
                "workspace_path": "workspaces/hospitalista/",
            }
            agent_path.write_text(
                "---\n"
                + transmute_module.yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
                + "---\n"
                + body,
                encoding="utf-8",
            )

            openclaw_dir = tmp / "openclaw"
            alias_workspace = openclaw_dir / "hospitalista"
            alias_workspace.mkdir(parents=True)
            deployed = alias_workspace / "AGENTS.md"
            current_hash = transmute_module._sha256(agent_path)
            deployed.write_text(
                "## Provenance\n\n"
                "- Source URN: `urn:salud:artefacto:urgenciologo`\n"
                f"- Source Hash: `{current_hash}`\n"
                "- Transmuted At: `2026-04-20T00:00:00+00:00`\n",
                encoding="utf-8",
            )

            with patch.object(transmute_module, "KORA_ROOT", repo_root), patch.object(
                transmute_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ), patch.object(
                transmute_module, "SKILLS_ROOT", repo_root / "artifacts" / "skills"
            ), patch.object(
                workspaces_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ):
                report = transmute_module.build_deploy_status_report(
                    openclaw_workspaces_dir=openclaw_dir,
                )

            statuses = {item["agent"]: item for item in report["agents"]}
            status = statuses["salud/urgenciologo"]["openclaw"]
            self.assertEqual(status["status"], "ok")
            self.assertEqual(status["workspace_path"], str(alias_workspace))

    def test_build_deploy_status_report_audits_skill_deployments(self):
        with TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            repo_root = tmp / "repo"
            skill_root = repo_root / "artifacts" / "skills" / "kora" / "test-skill"
            skill_root.mkdir(parents=True)
            skill_path = skill_root / "SKILL.md"
            self._write_skill_fixture(skill_path, ["codex"])

            codex_dir = tmp / "codex"
            deployed = codex_dir / "test-skill" / "SKILL.md"
            deployed.parent.mkdir(parents=True)
            current_hash = transmute_module._sha256(skill_path)
            deployed.write_text(
                "## Provenance\n\n"
                "- Source URN: `urn:kora:artefacto:test-skill`\n"
                f"- Source Hash: `{current_hash}`\n"
                "- Transmuted At: `2026-04-20T00:00:00+00:00`\n",
                encoding="utf-8",
            )

            with patch.object(transmute_module, "KORA_ROOT", repo_root), patch.object(
                transmute_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ), patch.object(
                transmute_module, "SKILLS_ROOT", repo_root / "artifacts" / "skills"
            ), patch.object(
                workspaces_module, "AGENTS_ROOT", repo_root / "artifacts" / "agents"
            ):
                report = transmute_module.build_deploy_status_report(codex_skills_dir=codex_dir)

            statuses = {item["skill"]: item for item in report["skills"]}
            self.assertEqual(statuses["kora/test-skill"]["codex"]["status"], "ok")

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
