import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import jsonschema

from common import AGENTS_ROOT, FIXTURES, ROOT, has_productive_workspaces, load_json
from kora_lib.artifacts import load_yaml_safe
from kora_lib.config import AGENT_REQUIRED_FILES
from kora_lib.reports import compute_stats_payload, render_stats_markdown
from kora_lib.validation import validate_agents_canonical_structure, validate_workspace_semantics
from kora_lib.workspaces import get_workspace_missing_files, iter_agent_workspaces, validate_skill_file


_SKIP_IF_NO_WORKSPACES = unittest.skipUnless(
    has_productive_workspaces(),
    "Sin workspaces productivos (AGENTS/{ns}/{name}/). El fleet vive en staging (_FRAGUA/INBOX/) durante el reprocesamiento v8.",
)


def _requires_productive_workspaces(cls):
    """Decorador de clase que aplica skip a todos los metodos test_* que
    dependen de workspaces productivos en AGENTS/{ns}/{name}/.

    Heuristica: escanea el source del metodo; si contiene referencia a
    AGENTS_ROOT o iter_agent_workspaces, aplica skip condicional.
    """
    import inspect
    if has_productive_workspaces():
        return cls
    for name in dir(cls):
        if not name.startswith("test_"):
            continue
        method = getattr(cls, name)
        if not callable(method):
            continue
        try:
            src = inspect.getsource(method)
        except (OSError, TypeError):
            continue
        if "AGENTS_ROOT" in src or "iter_agent_workspaces" in src:
            setattr(cls, name, _SKIP_IF_NO_WORKSPACES(method))
    return cls


@_requires_productive_workspaces
class ArtifactFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bootstrap_schema = load_json(ROOT / "serialization" / "schemas" / "kora-agent-schema.json")
        cls.config_schema = load_json(ROOT / "serialization" / "schemas" / "kora-agent-config-schema.json")

    def test_valid_kora_md_fixture_loads(self):
        doc, err = load_yaml_safe(FIXTURES / "valid-kora-md.md")
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:test:kb:sample-kb")
        self.assertEqual(doc["version"], "1.0.0")
        self.assertEqual(doc["extensions"]["test"]["dialect"], "fixture")

    def test_valid_kora_spec_fixture_loads(self):
        doc, err = load_yaml_safe(FIXTURES / "valid-kora-spec.md")
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:test:kb:sample-spec")
        self.assertIn("Traces to:", doc["_md_body"])

    def test_valid_agent_bootstrap_matches_schema(self):
        doc, err = load_yaml_safe(FIXTURES / "valid-agent-bootstrap.md")
        self.assertIsNone(err)
        jsonschema.validate(instance=doc, schema=self.bootstrap_schema)

    def test_invalid_agent_bootstrap_fails_schema(self):
        doc, err = load_yaml_safe(FIXTURES / "invalid-agent-bootstrap.md")
        self.assertIsNone(err)
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(instance=doc, schema=self.bootstrap_schema)

    def test_valid_config_matches_schema(self):
        doc, err = load_yaml_safe(FIXTURES / "valid-config.json")
        self.assertIsNone(err)
        jsonschema.validate(instance=doc, schema=self.config_schema)

    def test_invalid_config_zero_max_concurrent_fails(self):
        doc, err = load_yaml_safe(FIXTURES / "invalid-config-max-concurrent-zero.json")
        self.assertIsNone(err)
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(instance=doc, schema=self.config_schema)

    def test_valid_skill_fixture_passes_semantics(self):
        failures = validate_skill_file(FIXTURES / "valid-skill.md")
        self.assertEqual(failures, [])

    def test_invalid_skill_fixture_reports_missing_heading(self):
        failures = validate_skill_file(FIXTURES / "invalid-skill.md")
        self.assertTrue(any("missing required heading '## Input/Output'" in item for item in failures))

    def test_validate_workspace_semantics_enforces_skill_quota(self):
        with TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)
            skills = workspace / "skills"
            skills.mkdir()
            for index in range(2):
                (skills / f"CM-TEST-{index}.md").write_text(
                    "---\n_manifest:\n  urn: urn:test:skill:sample:1.0.0\n  type: lazy_load_endofunctor\n---\n",
                    encoding="utf-8",
                )

            failures = validate_workspace_semantics(
                workspace,
                {"limits": {"quotas": {"max_skills_per_agent": 1}}},
                [],
            )
            self.assertTrue(any("max_skills_per_agent=1" in item for item in failures))

    def test_extended_skill_fixture_loads(self):
        doc, err = load_yaml_safe(FIXTURES / "extended-skill" / "SKILL.md")
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:test:skill:sample-extended:1.0.0")

    def test_agent_spec_restores_fsm_contract(self):
        content = (ROOT / "serialization" / "autoria-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "serializacion",
            "AGENT.md",
            "artefacto.plan",
            "artefacto.interfaz",
            "artefacto.contexto",
            "artefacto.composicion",
            "artefacto.invariantes",
            "agente-propiamente-tal",
            "atlas.forma_material",
            "harness-spec",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_md_spec_restores_koraficacion_contract(self):
        content = (ROOT / "serialization" / "md-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "KORA/MD v8",
            "## 6. Koraficacion",
            "skeleton",
            "meat",
            "fat",
            "FS=100%",
            "### 5.4.2 Realizacion superficial",
            "### 5.6 Familias documentales",
            "Heading truncado",
            "Calidad de superficie",
            "### 6.10 Verificacion mecanica",
            "### 6.11 Verificacion de fidelidad",
            "`atomic`",
            "### 5.6.1 Familia `atomic`",
            "productor canonico",
            "Contrato vigente v8",
        )
        for term in required_terms:
            self.assertIn(term, content)
        self.assertNotIn("test de bolsillo", content)

    def test_md_spec_declares_atomic_family_and_canonical_producer(self):
        content = (ROOT / "serialization" / "md-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "familia `atomic`",
            "productor canonico",
            "enum cerrado",
            "15.000 caracteres",
            "200 proposiciones",
            "dedup multi-source",
            "particion semantica relevante",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_knowledge_spec_registers_atomize_as_canonical_producer(self):
        content = (ROOT / "serialization" / "knowledge-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "## 12. Productores canonicos de familia",
            "urn:kora:artefacto:atomize",
            "artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-",
            "hand_edited",
            "unica ruta soportada",
            "scaffold semantico degradado",
            "FS=100%",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_knowledge_spec_declares_requirement_trace_relation(self):
        content = (ROOT / "serialization" / "knowledge-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "traces_requirements",
            "Requirement",
            "TracesRequirement",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_h_minor_artifacts_exist(self):
        required_paths = (
            ROOT / "artifacts" / "knowledge" / "kora" / "sys" / "requirement-traceability-model.md",
            ROOT / "artifacts" / "knowledge" / "kora" / "sys" / "catalogo-patrones-skills.md",
            ROOT / "artifacts" / "knowledge" / "kora" / "sys" / "modelo-organizacional-kora.md",
        )
        for path in required_paths:
            self.assertTrue(path.exists(), str(path))

    def test_atomize_skill_is_runtime_agnostic_and_llm_first(self):
        content = (ROOT / "artifacts" / "skills" / "kora" / "atomize" / "SKILL.md").read_text(encoding="utf-8")
        required_terms = (
            "Claude Code",
            "Codex",
            "LLM",
            "Modo unico de operacion",
            "unico productor soportado",
            "Modo de recuperacion obligatoria",
            "Criterios de rechazo",
            "## Recursos",
            "### Scripts",
            "### Referencias",
            "scripts/atomize.py",
            "scripts/validate_atomic.py",
            "scripts/check_atomic_bundle.py",
            "scripts/review_atomic_quality.py",
            "scripts/prepare_atomic_fidelity_review.py",
            "scripts/review_atomic_acceptance.py",
            "scripts/publish_atomic.py",
            "referencias/llm-first-workflow.md",
            "referencias/atomic-output-contract.md",
            "referencias/plaintext-book-recovery.md",
            "referencias/golden-case-opm-libro.md",
            "referencias/golden-case-ocr-procedure.md",
            "referencias/golden-case-multifile-dedup.md",
            "referencias/golden-case-multifile-tension.md",
            "referencias/quality-gates.md",
            "referencias/semantic-fidelity-review.md",
            "Criterio de cierre semantico",
            "particion semantica relevante",
            "colapsa hechos distinguibles",
            "review aceptada y fresca",
        )
        for term in required_terms:
            self.assertIn(term, content)

        required_paths = (
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "scripts" / "atomize.py",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "scripts" / "validate_atomic.py",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "scripts" / "check_atomic_bundle.py",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "scripts" / "review_atomic_quality.py",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "scripts" / "prepare_atomic_fidelity_review.py",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "scripts" / "review_atomic_acceptance.py",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "scripts" / "publish_atomic.py",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "llm-first-workflow.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "atomic-output-contract.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "plaintext-book-recovery.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "golden-case-opm-libro.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "golden-case-ocr-procedure.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "golden-case-multifile-dedup.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "golden-case-multifile-tension.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "quality-gates.md",
            ROOT / "artifacts" / "skills" / "kora" / "atomize" / "referencias" / "semantic-fidelity-review.md",
        )
        for path in required_paths:
            self.assertTrue(path.exists(), str(path))

    def test_skill_spec_restores_extended_support_with_governed_contract(self):
        content = (ROOT / "serialization" / "autoria-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "serializacion",
            "forma_material: habilidad",
            "scripts/",
            "referencias/",
            "recursos/",
            "fidelidad-agentskills",
            "fidelidad-mastra",
            "risk_register",
            "progressive-disclosure",
            "componible_con",
        )
        for term in required_terms:
            self.assertIn(term, content)

        rejected_terms = (
            "fuera del soporte efectivo del repo",
        )
        for term in rejected_terms:
            self.assertNotIn(term, content)

    def test_cat_thinking_uses_icas_corpus_and_no_fxsl_traces(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "cat-thinking" / "SKILL.md"
        doc, err = load_yaml_safe(skill_path)
        self.assertIsNone(err)
        allowed = set(doc["extensions"]["kora"]["conocimiento_permitido"])
        expected_icas = {
            "urn:fxsl:kb:icas-sintesis",
            "urn:fxsl:kb:icas-composicion",
            "urn:fxsl:kb:icas-preservacion",
            "urn:fxsl:kb:icas-comparacion",
            "urn:fxsl:kb:icas-identidad-relacion",
            "urn:fxsl:kb:icas-universales",
            "urn:fxsl:kb:icas-adjunciones",
            "urn:fxsl:kb:icas-composicion-estructura",
            "urn:fxsl:kb:icas-enriquecimiento",
            "urn:fxsl:kb:icas-higher-categories",
            "urn:fxsl:kb:icas-efectos",
            "urn:fxsl:kb:icas-extension",
            "urn:fxsl:kb:icas-interaccion",
            "urn:fxsl:kb:icas-topoi",
            "urn:fxsl:kb:icas-safety-alignment",
            "urn:fxsl:kb:icas-escala",
            "urn:fxsl:kb:icas-agencia",
            "urn:fxsl:kb:icas-protocolos",
            "urn:fxsl:kb:icas-tiempo",
            "urn:fxsl:kb:icas-lifecycle",
            "urn:fxsl:kb:icas-procesos",
            "urn:fxsl:kb:icas-calidad-riesgo",
            "urn:fxsl:kb:icas-patrones",
            "urn:fxsl:kb:icas-infraestructura",
        }
        self.assertTrue(expected_icas.issubset(allowed))
        self.assertNotIn("Traces to: urn:fxsl", doc["_md_body"])

    def test_harness_spec_canonizes_ontology(self):
        content = (ROOT / "ontology" / "harness-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "v1.1.0",
            "PMI × LFS",
            "constitucion ontologica",
            "vector_ontologico",
            "free monad",
            "cofree comonad",
            # 6 ejes
            "Π — Plan",
            "Μ — Materia",
            "Ξ — Interaccion",
            "Λ — Nivel sociotecnico",
            "Φ — Acoplamiento humano-AI",
            "Σ — Vector etico",
            # 3 atlas
            "Atlas A",
            "Atlas B",
            "Atlas C",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_qa_spec_defines_enriched_quality_contract(self):
        content = (ROOT / "ontology" / "qa-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "KORA/QA-Spec v1.0.0",
            "([0,1]^5, <=, 1̄, ⊗)",
            "quality attributes",
            "qa_budget",
            "sigma_min",
            "latency",
            "availability",
            "mttr",
            "cost",
            "Bool",
            "Cost",
            "harness-spec",
            "runtime-spec-md",
            "autoria-spec",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_core_specs_reference_qa_spec(self):
        files = (
            ROOT / "governance" / "gobernanza.md",
            ROOT / "ontology" / "harness-spec.md",
            ROOT / "serialization" / "autoria-spec.md",
            ROOT / "runtime" / "runtime-spec-md.md",
        )
        for path in files:
            content = path.read_text(encoding="utf-8")
            self.assertIn("qa-spec", content, msg=str(path))

    def test_transmutation_spec_defines_functor_laws(self):
        content = (ROOT / "runtime" / "transmutation-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "v1.2.0",
            "functor",
            "preservacion",
            "bisimulacion",
            "_transmutation.yml",
            "trace_fidelity",
            "matriz de preservacion",
            "fidelidad",
            "source_vector",
            "structural_preservation",
            "projections",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_runtime_extensions_declare_preservation_matrix(self):
        """Cada runtime-extension declara dominio y matriz de preservacion por eje."""
        for spec_name in (
            "claude-code-runtime-extension.md",
            "codex-runtime-extension.md",
            "gemini-runtime-extension.md",
            "mastra-runtime-extension.md",
            "openclaw-runtime-extension.md",
        ):
            content = (ROOT / "runtime" / spec_name).read_text(encoding="utf-8")
            # Todos declaran matriz por eje
            for eje in ("pi:", "mu:", "xi:", "lambda:", "phi:", "sigma:"):
                self.assertIn(eje, content, msg=f"{spec_name} missing eje {eje}")
            # Todos citan transmutation-spec
            self.assertIn("transmutation-spec", content, msg=f"{spec_name} missing transmutation-spec ref")
            # Todos tienen contrato vigente declarado
            self.assertIn("Contrato vigente", content, msg=f"{spec_name} missing Contrato vigente")

    def test_openclaw_extension_declares_acp_meta_runtime(self):
        content = (ROOT / "runtime" / "openclaw-runtime-extension.md").read_text(encoding="utf-8")
        required_terms = (
            "v1.2.1",
            "meta-runtime",
            "ACP",
            "acp_backend",
            "Unico",  # unico target con soporte a Servicio (Μ=3)
            "Servicio",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_mastra_extension_declares_workflow_and_mcp_surfaces(self):
        content = (ROOT / "runtime" / "mastra-runtime-extension.md").read_text(encoding="utf-8")
        required_terms = (
            "v1.0.0",
            "Mastra",
            "Workflow",
            "runtimeContext",
            "MCP",
            "fidelidad-mastra",
            "mastra/",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_structural_backlog_specs_are_materialized(self):
        files = (
            ROOT / "runtime" / "multiagente-spec.md",
            ROOT / "ontology" / "procesos-spec.md",
            ROOT / "ontology" / "risk-register-spec.md",
        )
        required_terms = {
            "multiagente-spec.md": ("sheaf", "coreografia", "handoff", "ACP"),
            "procesos-spec.md": ("migrate", "validate", "transmute", "index"),
            "risk-register-spec.md": ("Kleisli", "risk_register", "qa-spec", "residual_sigma_floor"),
        }
        for path in files:
            self.assertTrue(path.exists(), str(path))
            content = path.read_text(encoding="utf-8")
            for term in required_terms[path.name]:
                self.assertIn(term, content, msg=f"{path.name} missing {term}")

    def test_specs_declare_manifest_kind_taxonomy(self):
        governance = (ROOT / "governance" / "gobernanza.md").read_text(encoding="utf-8")
        autoria_spec = (ROOT / "serialization" / "autoria-spec.md").read_text(encoding="utf-8")
        self.assertIn("Manifest kind", governance)
        self.assertIn("artefacto agentico", governance)
        self.assertIn("runtime_extension", governance)
        self.assertIn("transmutation_record", governance)
        self.assertIn("vector ontologico", autoria_spec)
        self.assertIn("serializacion de autoria", autoria_spec)
        self.assertIn("atlas.forma_material", autoria_spec)
        self.assertIn("urn:{ns}:artefacto:{id}", governance)

    def test_meta_core_agents_keep_control_layer_compact(self):
        workspace_dirs = (
            AGENTS_ROOT / "kora" / "custodio",
            AGENTS_ROOT / "kora" / "guardian",
        )
        for workspace_dir in workspace_dirs:
            self.assertTrue((workspace_dir / "AGENT.md").exists(), workspace_dir.as_posix())
            self.assertFalse((workspace_dir / "AGENTS.md").exists(), workspace_dir.as_posix())
            self.assertFalse((workspace_dir / "SOUL.md").exists(), workspace_dir.as_posix())
            self.assertFalse((workspace_dir / "TOOLS.md").exists(), workspace_dir.as_posix())

    def test_meta_context_managers_do_not_encode_fsm_destinations(self):
        files = tuple(
            path
            for path in (
                AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-CONTEXT-MANAGER.md",
            )
            if path.exists()
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("estado_destino", content)
        self.assertNotIn("estado_fsm", content)
        self.assertNotIn("estado_actual: FSMState", content)
        self.assertNotIn("S-DISPATCHER", content)
        self.assertNotIn("S-END", content)
        self.assertNotIn("la FSM debe volver a despachar", content)
        self.assertIn("requiere_revision_de_foco", content)

    def test_meta_intent_classifiers_do_not_receive_fsm_state(self):
        files = tuple(
            path
            for path in (
                AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-INTENT-CLASSIFIER.md",
            )
            if path.exists()
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("FSMState", content)
        self.assertNotIn("|END)", content)
        self.assertIn("cierre_solicitado", content)

    def test_custodio_scope_excludes_agent_and_kb_mutation(self):
        agents = (AGENTS_ROOT / "kora" / "custodio" / "AGENT.md").read_text(encoding="utf-8")
        surgeon = (
            AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-SURGEON.md"
        ).read_text(encoding="utf-8")
        evolution = (
            AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-EVOLUCION-PLANNER.md"
        ).read_text(encoding="utf-8")
        self.assertIn("excluyendo `AGENTS/`, specs fundacionales y contenido KB", agents)
        self.assertIn("sin intervenir `AGENTS/`, specs fundacionales ni contenido KB", surgeon)
        self.assertIn("fuera de `AGENTS/`, specs fundacionales y contenido KB", evolution)

    def test_custodio_soul_avoids_operational_policy_leakage(self):
        self.assertFalse((AGENTS_ROOT / "kora" / "custodio" / "SOUL.md").exists())

    def test_meta_core_tools_stay_semantic(self):
        custodio_tools = (AGENTS_ROOT / "kora" / "custodio" / "AGENT.md").read_text(encoding="utf-8")
        self.assertNotIn("Implementacion:", custodio_tools)

    def test_custodio_operational_skills_use_semantic_tools(self):
        files = (
            AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-HEALTH-INSPECTOR.md",
            AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-CATALOG-STEWARD.md",
            AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-INGESTA-STEWARD.md",
            AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-EVOLUCION-PLANNER.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("repo_health", content)
        self.assertIn("catalog_sync", content)
        self.assertIn("urn_resolve", content)
        self.assertIn("intake_pipeline", content)
        self.assertNotIn("`scripts/kora health`", content)
        self.assertNotIn("`scripts/kora index`", content)
        self.assertNotIn("`scripts/kora intake`", content)
        self.assertNotIn("`git status`", content)

    def test_guardian_runtime_capabilities_drop_analysis(self):
        content = (AGENTS_ROOT / "kora" / "guardian" / "AGENT.md").read_text(encoding="utf-8")
        self.assertNotIn('"analysis"', content)
        self.assertNotIn("runtime_capabilities", content)

    def test_digitrans_uses_tde_as_primary_corpus(self):
        agent = (AGENTS_ROOT / "gn" / "digitrans" / "AGENT.md").read_text(encoding="utf-8")
        self.assertNotIn("urn:gov:kb:intro-tde", agent)
        self.assertNotIn("urn:gov:kb:lexicon-wikiguias", agent)
        self.assertNotIn("urn:gov:kb:datosgob", agent)
        self.assertNotIn("urn:legal:kb:ley-21658-segdig", agent)
        self.assertNotIn("urn:legal:kb:ley-21719-datos-personales", agent)
        self.assertNotIn("urn:legal:kb:legislacion-ia-chile", agent)
        self.assertIn("urn:tde:kb:guia-metodologica-sistema-transformacion-digital-2025", agent)
        self.assertIn("urn:tde:kb:recomendaciones-tecnicas-cloud-publica", agent)
        self.assertNotIn("urn:orko:kb:orko-metodologia", agent)

    def test_digitrans_bootstrap_matches_current_agent_spec(self):
        agents = (AGENTS_ROOT / "gn" / "digitrans" / "AGENT.md").read_text(encoding="utf-8")
        intake = (AGENTS_ROOT / "gn" / "digitrans" / "skills" / "CM-INTAKE.md").read_text(encoding="utf-8")
        self.assertIn("[prioridad 1]", agents)
        self.assertIn("dominio=normativo", agents)
        self.assertIn("S-REJECT", agents)
        self.assertIn("S-CLARIFY", agents)
        self.assertNotIn("REFINE_DRAFT_INTERNALLY", agents)
        self.assertNotIn("-> CONTEXT_SHIFT", agents)
        self.assertFalse((AGENTS_ROOT / "gn" / "digitrans" / "SOUL.md").exists())
        self.assertFalse((AGENTS_ROOT / "gn" / "digitrans" / "USER.md").exists())
        self.assertFalse((AGENTS_ROOT / "gn" / "digitrans" / "TOOLS.md").exists())
        self.assertIn("artefacto:", agents)
        self.assertIn("interfaz:", agents)
        self.assertNotIn("lista para enrutar a S-", intake)
        self.assertIn("cierre_solicitado", intake)

    def test_digitrans_dispatcher_exits_scope_and_ambiguity_without_self_loop(self):
        agents = (AGENTS_ROOT / "gn" / "digitrans" / "AGENT.md").read_text(encoding="utf-8")
        self.assertNotIn("IF fuera_scope [prioridad 1] -> S-DISPATCHER", agents)
        self.assertNotIn("IF ambiguo [prioridad 7] -> S-DISPATCHER", agents)
        self.assertIn("IF fuera_scope [prioridad 1] -> S-REJECT", agents)
        self.assertIn("IF ambiguo [prioridad 7] -> S-CLARIFY", agents)
        self.assertIn("IF tema != dominio TDE -> rechazar con motivo", agents)

    def test_digitrans_tools_route_docdigital_and_pisee_explicitly(self):
        agent = (AGENTS_ROOT / "gn" / "digitrans" / "AGENT.md").read_text(encoding="utf-8")
        self.assertIn("urn:tde:kb:manual-coordinadora-transformacion-digital", agent)
        self.assertIn("urn:tde:kb:decreto-12-interoperabilidad", agent)

    def test_pensador_generador_normalizes_control_targets_and_soul(self):
        ws = AGENTS_ROOT / "fxsl" / "pensador-generador"
        if not ws.is_dir():
            self.skipTest("fxsl/pensador-generador no productivo — en staging")
        agents = (ws / "AGENTS.md").read_text(encoding="utf-8")
        soul = (AGENTS_ROOT / "fxsl" / "pensador-generador" / "SOUL.md").read_text(encoding="utf-8")
        tools = (AGENTS_ROOT / "fxsl" / "pensador-generador" / "TOOLS.md").read_text(encoding="utf-8")
        config = (AGENTS_ROOT / "fxsl" / "pensador-generador" / "config.json").read_text(encoding="utf-8")
        self.assertNotIn("REFINE_DRAFT", agents)
        self.assertNotIn("CONTEXT_SHIFT ->", agents)
        self.assertIn("IF other fails -> S-PRODUCCION", agents)
        self.assertIn("IF tema != dominio actual -> S-DISPATCHER para reclasificar", agents)
        self.assertNotIn("## Saludo", soul)
        self.assertNotIn("## Estilo", soul)
        self.assertNotIn("## Ejemplos", soul)
        self.assertIn("## catalog_resolve", tools)
        self.assertNotIn("## resolve_urn", tools)
        self.assertIn('"catalog_resolve"', config)
        self.assertNotIn('"resolve_urn"', config)
        self.assertNotIn("CONTEXTO (C1-C4)", agents)
        self.assertNotIn("PRAXIS (B1-B4)", agents)
        self.assertNotIn("VINDICATE", agents)

    def test_modelamiento_opm_declares_canonical_ssot(self):
        skill_path = ROOT / "artifacts" / "skills" / "kora" / "modelamiento-opm" / "SKILL.md"
        doc, err = load_yaml_safe(skill_path)
        self.assertIsNone(err)
        allowed = set(doc["extensions"]["kora"]["conocimiento_permitido"])
        expected = {
            "urn:fxsl:kb:opm-es",
            "urn:fxsl:kb:opd-es",
            "urn:fxsl:kb:opl-es",
            "urn:fxsl:kb:manual-metodologico-opm-es",
        }
        self.assertTrue(expected.issubset(allowed))
        self.assertIn("Bimodalidad", doc["_md_body"])

    def test_runtime_spec_restores_adapter_and_equivalence_contract(self):
        content = (ROOT / "runtime" / "runtime-spec-md.md").read_text(encoding="utf-8")
        required_terms = (
            "## 4. Adapters por plataforma",
            "## 5. Wrapper generation",
            "## 6. Platform equivalence",
            "## 7. Model routing",
            "## 8. Fallback chains y budget",
            "## 10. Transmutacion",
            "_transmutation.yml",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_swarm_spec_restores_operational_orchestration_contract(self):
        content = (ROOT / "serialization" / "autoria-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "orquestador",
            "operad dinamica",
            "artefacto.composicion",
            "agente-plataforma",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_all_agents_follow_canonical_section_order(self):
        for path in ROOT.glob("artifacts/agents/*/*/AGENTS.md"):
            content = path.read_text(encoding="utf-8")
            self.assertEqual(validate_agents_canonical_structure(content), [], path.as_posix())

    def test_render_stats_markdown_contains_current_categories(self):
        payload = compute_stats_payload()
        markdown = render_stats_markdown(payload)
        self.assertIn("# KORA Generated Stats", markdown)
        self.assertIn("| Agents |", markdown)
        self.assertIn("| Skills |", markdown)

    def test_compute_stats_payload_uses_required_workspace_files(self):
        payload = compute_stats_payload()
        expected_complete = [
            workspace
            for workspace in iter_agent_workspaces()
            if not get_workspace_missing_files(workspace, AGENT_REQUIRED_FILES)
        ]
        self.assertEqual(payload["agent_workspaces"], len(expected_complete))


if __name__ == "__main__":
    unittest.main()
