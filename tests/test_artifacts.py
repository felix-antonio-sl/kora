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
        cls.bootstrap_schema = load_json(ROOT / "schemas" / "kora-agent-schema.json")
        cls.config_schema = load_json(ROOT / "schemas" / "kora-agent-config-schema.json")

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
        content = (ROOT / "specs" / "autoria-spec.md").read_text(encoding="utf-8")
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
        content = (ROOT / "specs" / "md-spec.md").read_text(encoding="utf-8")
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
        content = (ROOT / "specs" / "md-spec.md").read_text(encoding="utf-8")
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
        content = (ROOT / "specs" / "knowledge-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "## 12. Productores canonicos de familia",
            "urn:kora:artefacto:atomize",
            "KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-",
            "hand_edited",
            "unica ruta soportada",
            "scaffold semantico degradado",
            "FS=100%",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_atomize_skill_is_runtime_agnostic_and_llm_first(self):
        content = (ROOT / "SKILLS" / "kora" / "atomize" / "SKILL.md").read_text(encoding="utf-8")
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
            ROOT / "SKILLS" / "kora" / "atomize" / "scripts" / "atomize.py",
            ROOT / "SKILLS" / "kora" / "atomize" / "scripts" / "validate_atomic.py",
            ROOT / "SKILLS" / "kora" / "atomize" / "scripts" / "check_atomic_bundle.py",
            ROOT / "SKILLS" / "kora" / "atomize" / "scripts" / "review_atomic_quality.py",
            ROOT / "SKILLS" / "kora" / "atomize" / "scripts" / "prepare_atomic_fidelity_review.py",
            ROOT / "SKILLS" / "kora" / "atomize" / "scripts" / "review_atomic_acceptance.py",
            ROOT / "SKILLS" / "kora" / "atomize" / "scripts" / "publish_atomic.py",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "llm-first-workflow.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "atomic-output-contract.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "plaintext-book-recovery.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "golden-case-opm-libro.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "golden-case-ocr-procedure.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "golden-case-multifile-dedup.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "golden-case-multifile-tension.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "quality-gates.md",
            ROOT / "SKILLS" / "kora" / "atomize" / "referencias" / "semantic-fidelity-review.md",
        )
        for path in required_paths:
            self.assertTrue(path.exists(), str(path))

    def test_skill_spec_restores_extended_support_with_governed_contract(self):
        content = (ROOT / "specs" / "autoria-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "serializacion",
            "forma_material: habilidad",
            "scripts/",
            "referencias/",
            "recursos/",
            "fidelidad-agentskills",
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

    def test_harness_spec_canonizes_ontology(self):
        content = (ROOT / "specs" / "harness-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "v1.0.0",
            "PMI × LFS",
            "constitucion ontologica",
            "harness_vector",
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

    def test_transmutation_spec_defines_functor_laws(self):
        content = (ROOT / "specs" / "transmutation-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "v1.0.0",
            "functor",
            "preservacion",
            "bisimulacion",
            "_transmutation.yml",
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
            "openclaw-runtime-extension.md",
        ):
            content = (ROOT / "specs" / spec_name).read_text(encoding="utf-8")
            # Todos declaran matriz por eje
            for eje in ("pi:", "mu:", "xi:", "lambda:", "phi:", "sigma:"):
                self.assertIn(eje, content, msg=f"{spec_name} missing eje {eje}")
            # Todos citan transmutation-spec
            self.assertIn("transmutation-spec", content, msg=f"{spec_name} missing transmutation-spec ref")
            # Todos tienen contrato vigente declarado
            self.assertIn("Contrato vigente", content, msg=f"{spec_name} missing Contrato vigente")

    def test_openclaw_extension_declares_acp_meta_runtime(self):
        content = (ROOT / "specs" / "openclaw-runtime-extension.md").read_text(encoding="utf-8")
        required_terms = (
            "v1.1.0",
            "meta-runtime",
            "ACP",
            "acp_backend",
            "Unico",  # unico target con soporte a Servicio (Μ=3)
            "Servicio",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_specs_declare_manifest_kind_taxonomy(self):
        governance = (ROOT / "specs" / "gobernanza.md").read_text(encoding="utf-8")
        autoria_spec = (ROOT / "specs" / "autoria-spec.md").read_text(encoding="utf-8")
        self.assertIn("Manifest kind", governance)
        self.assertIn("artefacto agentico", governance)
        self.assertIn("runtime_extension", governance)
        self.assertIn("transmutation_record", governance)
        self.assertIn("vector ontologico", autoria_spec)
        self.assertIn("serializacion de autoria", autoria_spec)
        self.assertIn("atlas.forma_material", autoria_spec)
        self.assertIn("urn:{ns}:artefacto:{id}", governance)

    def test_forgemaster_tracks_governed_extended_skill_support(self):
        files = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-VALIDATOR" / "SKILL.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER" / "SKILL.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("BUNDLE GOBERNADO", content)
        self.assertIn("skills/CM-*/SKILL.md", content)
        self.assertIn("scripts/", content)
        self.assertIn("references/", content)
        self.assertIn("assets/", content)

    def test_forgemaster_generation_skills_keep_soul_minimal(self):
        files = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER" / "SKILL.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-COMPONENT-BUILDER.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("Identidad Dialectica, Paradigma Cognitivo, Tono", content)
        self.assertNotIn("Saludo", content)
        self.assertNotIn("Estilo", content)
        self.assertNotIn("Ejemplos", content)

    def test_meta_core_agents_keep_control_layer_compact(self):
        workspace_dirs = (
            AGENTS_ROOT / "kora" / "curator",
            AGENTS_ROOT / "kora" / "custodio",
            AGENTS_ROOT / "kora" / "forgemaster",
            AGENTS_ROOT / "kora" / "guardian",
        )
        for workspace_dir in workspace_dirs:
            self.assertTrue((workspace_dir / "AGENT.md").exists(), workspace_dir.as_posix())
            self.assertFalse((workspace_dir / "AGENTS.md").exists(), workspace_dir.as_posix())
            self.assertFalse((workspace_dir / "SOUL.md").exists(), workspace_dir.as_posix())
            self.assertFalse((workspace_dir / "TOOLS.md").exists(), workspace_dir.as_posix())

    def test_meta_context_managers_do_not_encode_fsm_destinations(self):
        files = (
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-CONTEXT-MANAGER.md",
            AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-CONTEXT-MANAGER.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-CONTEXT-MANAGER.md",
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
                AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-INTENT-CLASSIFIER.md",
                AGENTS_ROOT / "kora" / "custodio" / "skills" / "CM-INTENT-CLASSIFIER.md",
                AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-INTENT-CLASSIFIER.md",
            )
            if path.exists()
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("FSMState", content)
        self.assertNotIn("|END)", content)
        self.assertIn("cierre_solicitado", content)

    def test_meta_lifecycle_orchestrators_do_not_control_agent_phases(self):
        files = tuple(
            path
            for path in (
                AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-LIFECYCLE-ORCHESTRATOR.md",
                AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-LIFECYCLE-ORCHESTRATOR.md",
            )
            if path.exists()
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("### Fase 1:", content)
        self.assertNotIn("### Fase 2:", content)
        self.assertNotIn("### Fase 3:", content)
        self.assertNotIn("transicionar a S-{fase_actual}", content)
        self.assertIn("checkpoint", content)

    def test_forgemaster_scaffolder_uses_requested_namespace_in_bootstrap_urns(self):
        content = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-agents:1.0.0", content)
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-soul:1.0.0", content)
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-user:1.0.0", content)
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-tools:1.0.0", content)
        self.assertNotIn("urn:kora:agent-bootstrap:{nombre}-agents:1.0.0", content)

    def test_forgemaster_scaffolder_declares_bootstrap_manifest_types(self):
        content = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER" / "SKILL.md"
        ).read_text(encoding="utf-8")
        for manifest_type in (
            "bootstrap_agents",
            "bootstrap_soul",
            "bootstrap_user",
            "bootstrap_tools",
            "bootstrap_config",
        ):
            self.assertIn(manifest_type, content)

    def test_forgemaster_scaffolder_supports_extended_skill_layout(self):
        content = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("AGENTS/{namespace}/{nombre}/skills/CM-{id}/", content)
        self.assertIn("skills/CM-{id}/", content)
        self.assertIn("SKILL.md", content)
        self.assertIn("scripts/", content)
        self.assertIn("references/", content)
        self.assertIn("assets/", content)

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

    def test_curator_and_custodio_soul_avoid_operational_policy_leakage(self):
        self.assertFalse((AGENTS_ROOT / "kora" / "curator" / "SOUL.md").exists())
        self.assertFalse((AGENTS_ROOT / "kora" / "custodio" / "SOUL.md").exists())

    def test_meta_core_tools_stay_semantic(self):
        custodio_tools = (AGENTS_ROOT / "kora" / "custodio" / "AGENT.md").read_text(encoding="utf-8")
        forgemaster_tools = (AGENTS_ROOT / "kora" / "forgemaster" / "AGENT.md").read_text(encoding="utf-8")
        self.assertNotIn("Implementacion:", custodio_tools)
        self.assertNotIn("Invoca internamente", forgemaster_tools)
        self.assertNotIn("Leer todos los archivos del workspace", forgemaster_tools)

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

    def test_curator_spec_md_skills_do_not_require_bold_keywords(self):
        files = (
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-AUDITOR" / "SKILL.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-CRYSTALLIZER.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-EDITOR.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("keywords RFC 2119 en negrita", content)
        self.assertNotIn("Keywords en **negrita**", content)
        self.assertIn("mayusculas", content)

    def test_curator_tracks_governed_extended_skill_support(self):
        files = (
            AGENTS_ROOT / "kora" / "curator" / "AGENT.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-AUDITOR" / "SKILL.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-DESIGNER" / "SKILL.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("artifact_validate", content)
        self.assertIn("form: extended", content)
        self.assertIn("references/", content)
        self.assertIn("assets/", content)

    def test_forgemaster_validator_drops_private_17_check_baseline(self):
        files = (AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-VALIDATOR" / "SKILL.md",)
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("17 checks", content)
        self.assertNotIn("CMs huerfanos", content)
        self.assertNotIn("EVALUACIONES", content)
        self.assertIn("baseline publicado", content)

    def test_forgemaster_tracks_current_spec_versions_and_fsm_precedence(self):
        agents = (AGENTS_ROOT / "kora" / "forgemaster" / "AGENT.md").read_text(encoding="utf-8")
        skills = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (
                AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-VALIDATOR" / "SKILL.md",
                AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-DESIGNER.md",
                AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-COMPONENT-BUILDER.md",
            )
        )
        self.assertIn("[prioridad 1]", agents)
        self.assertIn("agent-spec-md v8.7.0", skills)
        self.assertIn("skill-spec-md v4.2.0", skills)
        self.assertNotIn("agent-spec-md v8.3.0", skills)
        self.assertNotIn("skill-spec-md v3.4.0", skills)

    def test_forgemaster_validator_aligns_section_refs_and_formal_layer_access(self):
        validator = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-VALIDATOR" / "SKILL.md"
        ).read_text(encoding="utf-8")
        agent = (AGENTS_ROOT / "kora" / "forgemaster" / "AGENT.md").read_text(encoding="utf-8")
        self.assertIn("agent-spec-md §4.1", validator)
        self.assertIn("agent-spec-md §4.2-§4.3", validator)
        self.assertIn("gobernanza.md §5 y §8", validator)
        self.assertNotIn("GRAMATICA DE BEHAVIOR (§3.1)", validator)
        self.assertNotIn("FSM CANONICA (§3.2)", validator)
        self.assertIn("urn:kora:kb:cat-foundations", agent)
        self.assertIn("urn:kora:kb:cat-behavioral-preservation", agent)

    def test_forgemaster_extended_skill_docs_cover_design_build_and_validation(self):
        files = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-DESIGNER.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER" / "SKILL.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-COMPONENT-BUILDER.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-VALIDATOR" / "SKILL.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("skills/CM-{id}/SKILL.md", content)
        self.assertIn("extensions.{namespace}.skill", content)
        self.assertIn("no coexiste como archivo degenerado y como directorio extendido", content)
        self.assertIn("scripts/", content)
        self.assertIn("references/", content)
        self.assertIn("assets/", content)

    def test_forgemaster_transmutation_contract_centralizes_manifest_emission(self):
        emitter = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-ARTIFACT-EMITTER.md"
        ).read_text(encoding="utf-8")
        anthropic = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-ANTHROPIC-ADAPTER" / "SKILL.md"
        ).read_text(encoding="utf-8")
        openclaw = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-OPENCLAW-ADAPTER" / "SKILL.md"
        ).read_text(encoding="utf-8")
        claude_code = (
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-CLAUDE-CODE-ADAPTER" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("manifest_overrides", emitter)
        self.assertIn("unico responsable de generar", emitter)
        for content in (anthropic, openclaw, claude_code):
            self.assertIn("CM-ARTIFACT-EMITTER", content)
            self.assertIn("manifest_overrides", content)
            self.assertNotIn("artifact_write", content)
            self.assertNotIn("Generar _transmutation.yml", content)

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

    def test_opm_specialist_uses_neutral_intent_classification_and_clarify_state(self):
        ws = AGENTS_ROOT / "fxsl" / "opm-specialist"
        if not ws.is_dir():
            self.skipTest("fxsl/opm-specialist no productivo — en staging")
        agents = (ws / "AGENTS.md").read_text(encoding="utf-8")
        soul = (AGENTS_ROOT / "fxsl" / "opm-specialist" / "SOUL.md").read_text(encoding="utf-8")
        tools = (AGENTS_ROOT / "fxsl" / "opm-specialist" / "TOOLS.md").read_text(encoding="utf-8")
        classifier = (AGENTS_ROOT / "fxsl" / "opm-specialist" / "skills" / "CM-INTENT-CLASSIFIER.md").read_text(encoding="utf-8")
        self.assertIn("S-CLARIFY", agents)
        self.assertNotIn("IF ambiguo -> ACT: clarificar. -> S-DISPATCHER", agents)
        self.assertNotIn("REFINE_DRAFT", agents)
        self.assertIn("IF other fails -> S-DISPATCHER", agents)
        self.assertIn("scope_status=fuera_scope", agents)
        self.assertIn("cierre_solicitado", agents)
        self.assertIn("claridad=ambigua", agents)
        self.assertIn("modo_consulta=concepto", agents)
        self.assertIn("IF resuelto [prioridad 3] -> S-END", agents)
        self.assertNotIn("## Saludo", soul)
        self.assertNotIn("## Estilo", soul)
        self.assertNotIn("## Ejemplos", soul)
        self.assertIn("**Parametros:**", tools)
        self.assertIn("**Descripcion funcional:**", tools)
        self.assertNotIn("FSM de opm-specialist", classifier)
        self.assertIn("modo_consulta", classifier)
        self.assertIn("scope_status", classifier)
        self.assertIn("claridad", classifier)
        self.assertIn("cierre_solicitado", classifier)
        self.assertNotIn("terminar|fuera_scope|ambiguo", classifier)

    def test_runtime_spec_restores_adapter_and_equivalence_contract(self):
        content = (ROOT / "specs" / "runtime-spec-md.md").read_text(encoding="utf-8")
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
        content = (ROOT / "specs" / "autoria-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "orquestador",
            "operad dinamica",
            "artefacto.composicion",
            "agente-plataforma",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_curator_tracks_restored_md_and_spec_contracts(self):
        files = (
            AGENTS_ROOT / "kora" / "curator" / "AGENT.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-KORAFICATOR.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-CRYSTALLIZER.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-AUDITOR" / "SKILL.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-DESIGNER" / "SKILL.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-LIFECYCLE-ORCHESTRATOR.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("Funtor K", content)
        self.assertIn("Funtor C", content)
        self.assertIn("md-spec §9", content)
        self.assertNotIn("Funtor F", content)
        self.assertNotIn("Funtor G", content)
        self.assertNotIn("md-spec §8", content)
        self.assertNotIn("verificacion adversarial", content)

    def test_curator_declares_fsm_precedence_and_type_safe_fidelity_routing(self):
        agents = (AGENTS_ROOT / "kora" / "curator" / "AGENT.md").read_text(encoding="utf-8")
        self.assertIn("prioridad: 1", agents)
        self.assertIn(
            "validacion_falla AND causa=fidelidad AND tipo=descriptivo",
            agents,
        )
        self.assertIn(
            "validacion_falla AND causa=fidelidad AND tipo=prescriptivo",
            agents,
        )
        self.assertNotIn("IF FIDELITY_CHECK fails -> S-KORAFICATE", agents)

    def test_curator_guided_mode_uses_declared_transform_phases_only(self):
        files = (
            AGENTS_ROOT / "kora" / "curator" / "AGENT.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-LIFECYCLE-ORCHESTRATOR.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("FORGE", content)
        self.assertIn("KORAFICATE", content)
        self.assertIn("CRYSTALLIZE", content)

    def test_meta_skills_do_not_operationally_compose_other_meta_skills(self):
        files = (
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-EDITOR.md",
            AGENTS_ROOT / "kora" / "curator" / "skills" / "CM-ARTIFACT-SURGEON.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-EVOLVER.md",
            AGENTS_ROOT / "kora" / "forgemaster" / "skills" / "CM-AGENT-SURGEON.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("CM-ARTIFACT-AUDITOR mentalmente", content)
        self.assertNotIn("Ejecutar checklist correspondiente (CM-ARTIFACT-AUDITOR)", content)
        self.assertNotIn("CM-AGENT-VALIDATOR post-mejora", content)
        self.assertNotIn("Re-ejecutar CM-AGENT-VALIDATOR", content)
        self.assertIn("md-spec` §9 o `spec-md` §8", content)
        self.assertIn("agent-spec-md` v8.7.0 y `skill-spec-md` v4.2.0", content)

    def test_all_agents_follow_canonical_section_order(self):
        for path in ROOT.glob("AGENTS/*/*/AGENTS.md"):
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
