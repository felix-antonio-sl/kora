import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import jsonschema

from common import (
    AGENTS_ROOT,
    FIXTURES,
    ROOT,
    agent_workspace_path,
    has_productive_workspaces,
    load_json,
    skill_artifact_dir,
)
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
            "KORA/MD v12",
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
            "Contrato vigente v11",
            "Contrato vigente v12",
        )
        for term in required_terms:
            self.assertIn(term, content)
        self.assertNotIn("test de bolsillo", content)

    def test_md_spec_v11_delegates_prescriptive_to_spec_md(self):
        """KORA v9 (2026-05-20): md-spec v11 delega regimen prescriptivo a spec-md v1.0."""
        md_content = (ROOT / "serialization" / "md-spec.md").read_text(encoding="utf-8")
        # md-spec ya no contiene el contenido prescriptivo extendido.
        self.assertNotIn("#### 5.6.1.1 Proceso de cristalizacion", md_content)
        self.assertNotIn("#### 5.6.1.2 Lenguaje de obligacion", md_content)
        # md-spec apunta a spec-md.
        self.assertIn("urn:kora:kb:spec-md", md_content)
        # spec-md v1.0 existe con el perfil prescriptivo.
        spec_md = ROOT / "serialization" / "spec-md.md"
        self.assertTrue(spec_md.exists())
        sm_content = spec_md.read_text(encoding="utf-8")
        self.assertIn("KORA/Spec-MD v1.0.0", sm_content)
        self.assertIn("RFC 2119", sm_content)
        self.assertIn("Cristalizacion", sm_content)
        self.assertIn("Traces to", sm_content)

    def test_autoria_spec_v2_declares_arnes_as_ontological_discriminant(self):
        """KORA v9 (2026-05-20): autoria-spec v2.0 declara arnes como discriminante ontologico."""
        content = (ROOT / "serialization" / "autoria-spec.md").read_text(encoding="utf-8")
        self.assertIn("Especificacion de Autoria de Artefactos Agenticos v2.0.0", content)
        self.assertIn("Arnes como discriminante ontologico", content)
        self.assertIn("forma material es derivada operacional", content.lower())

    def test_md_spec_v10_retired_atomic_family(self):
        """KORA v8 (2026-05-20): familia atomic eliminada de md-spec v10."""
        content = (ROOT / "serialization" / "md-spec.md").read_text(encoding="utf-8")
        # Familia atomic NO debe aparecer como entrada de tabla canonica.
        self.assertNotIn("| `atomic` |", content)
        # Subseccion §5.6.1 Familia atomic ya no existe; §5.6.1 ahora es el
        # perfil `spec`.
        self.assertNotIn("### 5.6.1 Familia `atomic`", content)
        # El termino sigue admitido en lexico (Meat = hechos atomicos, etc.)
        # pero no como invariante de familia.

    def test_knowledge_spec_v3_retired_canonical_producer(self):
        """KORA v8 (2026-05-20): productor canonico atomic retirado."""
        content = (ROOT / "serialization" / "knowledge-spec.md").read_text(encoding="utf-8")
        # §9 ya no registra atomize como productor activo.
        self.assertIn("registro de productores canonicos esta vacio", content)
        self.assertIn("adr-retiro-atomize-y-lecciones-koda", content)
        # El URN del skill archivado se nombra para trazabilidad.
        self.assertIn("urn:kora:artefacto:atomize", content)

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

    def test_atomize_skill_archived_with_retired_status(self):
        """KORA v8 (2026-05-20): skill atomize archivado, URN preservado."""
        archived_skill = ROOT / "governance" / "decisiones-archivadas" / "skills-retiradas" / "atomize" / "SKILL.md"
        self.assertTrue(archived_skill.exists(), str(archived_skill))
        content = archived_skill.read_text(encoding="utf-8")
        self.assertIn("status: retirado", content)
        self.assertIn("urn:kora:artefacto:atomize", content)
        # El skill NO debe estar en productivo.
        productive_skill = ROOT / "artifacts" / "skills" / "kora" / "atomize"
        self.assertFalse(productive_skill.exists(), f"Skill atomize debe estar archivado, no en {productive_skill}")

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
        """Cada runtime-extension activa declara dominio y matriz de preservacion por eje."""
        for spec_name in (
            "claude-code-runtime-extension.md",
            "codex-runtime-extension.md",
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
        path = ROOT / "governance" / "decisiones-archivadas" / "specs-en-pausa" / "mastra-runtime-extension.md"
        self.assertTrue(path.exists(), f"Archived spec missing: {path}")
        content = path.read_text(encoding="utf-8")
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

    def test_meta_kora_rebuild_directive_is_materialized(self):
        path = ROOT / "artifacts" / "knowledge" / "kora" / "sys" / "meta-kora-rebuild-directive.md"
        doc, err = load_yaml_safe(path)
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:kora:kb:meta-kora-rebuild-directive")
        self.assertIn("No deben usarse como fuente", doc["_md_body"])

    def test_retired_meta_agents_do_not_resolve_as_staged_workspaces(self):
        from kora_lib.workspaces import find_agent_workspace

        for workspace_ref in ("kora/custodio", "kora/guardian", "kora/clawforge"):
            self.assertIsNone(find_agent_workspace(workspace_ref, include_staging=True), workspace_ref)

    def test_meta_kora_legacy_skills_purged(self):
        """Poda radical 2026-05-21: _rebuild_required/2026-05-03/kora/ eliminado."""
        rebuild_root = (
            ROOT / "artifacts" / "skills" / "_TALLER" / "INBOX" / "_rebuild_required"
        )
        self.assertFalse(rebuild_root.exists(), f"_rebuild_required eliminado en poda radical, no debe existir: {rebuild_root}")
        for name in ("artifact-curator", "curation-conductor"):
            self.assertFalse((ROOT / "artifacts" / "skills" / "kora" / name / "SKILL.md").exists(),
                             f"{name} retirado: sin productivo, sin legacy")
        for name in ("kora-agents", "kora-skills"):
            productive = ROOT / "artifacts" / "skills" / "kora" / name / "SKILL.md"
            self.assertTrue(productive.exists(), f"{name} productivo preservado")
            doc, err = load_yaml_safe(productive)
            self.assertIsNone(err)
            self.assertEqual(doc["status"], "activo")

    def test_digitrans_uses_tde_as_primary_corpus(self):
        agent = (agent_workspace_path("gn/digitrans") / "AGENT.md").read_text(encoding="utf-8")
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
        digitrans = agent_workspace_path("gn/digitrans")
        agents = (digitrans / "AGENT.md").read_text(encoding="utf-8")
        intake = (digitrans / "skills" / "CM-INTAKE.md").read_text(encoding="utf-8")
        self.assertIn("[prioridad 1]", agents)
        self.assertIn("dominio=normativo", agents)
        self.assertIn("S-REJECT", agents)
        self.assertIn("S-CLARIFY", agents)
        self.assertNotIn("REFINE_DRAFT_INTERNALLY", agents)
        self.assertNotIn("-> CONTEXT_SHIFT", agents)
        self.assertFalse((digitrans / "SOUL.md").exists())
        self.assertFalse((digitrans / "USER.md").exists())
        self.assertFalse((digitrans / "TOOLS.md").exists())
        self.assertIn("artefacto:", agents)
        self.assertIn("interfaz:", agents)
        self.assertNotIn("lista para enrutar a S-", intake)
        self.assertIn("cierre_solicitado", intake)

    def test_digitrans_dispatcher_exits_scope_and_ambiguity_without_self_loop(self):
        agents = (agent_workspace_path("gn/digitrans") / "AGENT.md").read_text(encoding="utf-8")
        self.assertNotIn("IF fuera_scope [prioridad 1] -> S-DISPATCHER", agents)
        self.assertNotIn("IF ambiguo [prioridad 7] -> S-DISPATCHER", agents)
        self.assertIn("IF fuera_scope [prioridad 1] -> S-REJECT", agents)
        self.assertIn("IF ambiguo [prioridad 7] -> S-CLARIFY", agents)
        self.assertIn("IF tema != dominio TDE -> rechazar con motivo", agents)

    def test_digitrans_tools_route_docdigital_and_pisee_explicitly(self):
        agent = (agent_workspace_path("gn/digitrans") / "AGENT.md").read_text(encoding="utf-8")
        self.assertIn("urn:tde:kb:manual-coordinadora-transformacion-digital", agent)
        self.assertIn("urn:tde:kb:decreto-12-interoperabilidad", agent)

    def test_pensador_generador_stays_staged_in_autoria_shape(self):
        staged = AGENTS_ROOT / "_FRAGUA" / "_archivo" / "2026-05-poda-version-a" / "personas" / "pensador-generador"
        productive = AGENTS_ROOT / "fxsl" / "pensador-generador"

        self.assertFalse((productive / "AGENT.md").exists())
        self.assertTrue((staged / "AGENT.md").exists(), f"Archived agent missing: {staged / 'AGENT.md'}")
        doc, err = load_yaml_safe(staged / "AGENT.md")
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:fxsl:artefacto:pensador-generador")
        self.assertEqual(doc["status"], "borrador")
        self.assertIn("artefacto", doc)
        self.assertFalse((staged / "AGENTS.md").exists())
        self.assertFalse((staged / "SOUL.md").exists())
        self.assertFalse((staged / "TOOLS.md").exists())
        self.assertFalse((staged / "config.json").exists())

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
