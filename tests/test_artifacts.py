import unittest

import jsonschema

from common import FIXTURES, ROOT, load_json
from kora_lib.artifacts import load_yaml_safe
from kora_lib.config import AGENT_REQUIRED_FILES
from kora_lib.reports import compute_stats_payload, render_stats_markdown
from kora_lib.validation import validate_agents_canonical_structure
from kora_lib.workspaces import get_workspace_missing_files, iter_agent_workspaces, validate_skill_file


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

    def test_extended_skill_fixture_loads(self):
        doc, err = load_yaml_safe(FIXTURES / "extended-skill" / "SKILL.md")
        self.assertIsNone(err)
        self.assertEqual(doc["_manifest"]["urn"], "urn:test:skill:sample-extended:1.0.0")

    def test_agent_spec_restores_fsm_contract(self):
        content = (ROOT / "specs" / "agent-spec-md.md").read_text(encoding="utf-8")
        required_terms = (
            "## 1. FSM",
            "## 2. Reglas Duras",
            "## 3. Co-induccion",
            "## 4. Contexto Multi-turno",
            "## 5. Wiring",
            "S-DISPATCHER",
            "S-END",
            "formal/01 §3.2",
            "formal/01 §3.3",
            "formal/01 §6.3",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_md_spec_restores_koraficacion_contract(self):
        content = (ROOT / "specs" / "md-spec.md").read_text(encoding="utf-8")
        required_terms = (
            "## 6. Koraficacion",
            "skeleton",
            "meat",
            "fat",
            "FS=100%",
            "CR>1.5",
            "### 6.10 Verificacion mecanica",
            "### 6.11 Verificacion de fidelidad",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_spec_md_restores_crystallization_contract(self):
        content = (ROOT / "specs" / "spec-md.md").read_text(encoding="utf-8")
        required_terms = (
            "### 1.2 Proceso de cristalizacion",
            "## 6. Patron obligatorio: regla + ejemplo + traza",
            "Correcto:",
            "Incorrecto:",
            "## 10. Template (esqueleto minimo)",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_skill_spec_descopes_extended_support_and_keeps_degenerate_baseline(self):
        content = (ROOT / "specs" / "skill-spec-md.md").read_text(encoding="utf-8")
        required_terms = (
            "la unica forma soportada, auditada y gobernada automaticamente",
            "Skill degenerado: archivo `CM-*.md`",
            "## 5. Descope explicito de Skills extendidos",
            "fuera del soporte efectivo del repo",
            "El validator base **DEBE** juzgar conformidad solo sobre Skill degenerado.",
        )
        for term in required_terms:
            self.assertIn(term, content)

        rejected_terms = (
            "## 5. Progressive Disclosure Lifecycle",
            "## 6. Topologia y coexistencia",
            "### 3.3 Script Protocol",
            "| Discover |",
            "| Activate |",
            "| Execute |",
        )
        for term in rejected_terms:
            self.assertNotIn(term, content)

    def test_forgemaster_no_longer_claims_extended_skill_support(self):
        files = (
            ROOT / "agents" / "kora" / "forgemaster" / "TOOLS.md",
            ROOT / "agents" / "kora" / "forgemaster" / "skills" / "CM-AGENT-VALIDATOR.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("baseline auditado soporta solo Skills degenerados", content)
        self.assertNotIn("Skills siguen formato degenerate (CM-only) o extended (directorio)", content)

    def test_forgemaster_generation_skills_keep_soul_minimal(self):
        files = (
            ROOT / "agents" / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER.md",
            ROOT / "agents" / "kora" / "forgemaster" / "skills" / "CM-COMPONENT-BUILDER.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("Identidad Dialectica, Paradigma Cognitivo, Tono", content)
        self.assertNotIn("Saludo", content)
        self.assertNotIn("Estilo", content)
        self.assertNotIn("Ejemplos", content)

    def test_meta_core_agents_keep_control_layer_compact(self):
        files = (
            ROOT / "agents" / "kora" / "curator" / "AGENTS.md",
            ROOT / "agents" / "kora" / "custodio" / "AGENTS.md",
            ROOT / "agents" / "kora" / "forgemaster" / "AGENTS.md",
            ROOT / "agents" / "kora" / "guardian" / "AGENTS.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("REFINE_DRAFT", content)
        self.assertNotIn("-> CONTEXT_SHIFT", content)
        self.assertNotIn("→ ACT:", content)
        self.assertNotIn("Pre-analisis(", content)
        self.assertNotIn("Elicitar dominio y fuente", content)
        self.assertNotIn("Ejecutar kora health", content)
        self.assertNotIn("Ejecutar ciclo completo secuencial", content)

    def test_meta_context_managers_do_not_encode_fsm_destinations(self):
        files = (
            ROOT / "agents" / "kora" / "curator" / "skills" / "CM-CONTEXT-MANAGER.md",
            ROOT / "agents" / "kora" / "custodio" / "skills" / "CM-CONTEXT-MANAGER.md",
            ROOT / "agents" / "kora" / "forgemaster" / "skills" / "CM-CONTEXT-MANAGER.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("estado_destino", content)
        self.assertNotIn("estado_fsm", content)
        self.assertNotIn("estado_actual: FSMState", content)
        self.assertNotIn("S-DISPATCHER", content)
        self.assertNotIn("S-END", content)
        self.assertIn("requiere_reclasificacion", content)

    def test_forgemaster_scaffolder_uses_requested_namespace_in_bootstrap_urns(self):
        content = (
            ROOT / "agents" / "kora" / "forgemaster" / "skills" / "CM-WORKSPACE-SCAFFOLDER.md"
        ).read_text(encoding="utf-8")
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-agents:1.0.0", content)
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-soul:1.0.0", content)
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-user:1.0.0", content)
        self.assertIn("urn:{namespace}:agent-bootstrap:{nombre}-tools:1.0.0", content)
        self.assertNotIn("urn:kora:agent-bootstrap:{nombre}-agents:1.0.0", content)

    def test_custodio_scope_excludes_agent_and_kb_mutation(self):
        agents = (ROOT / "agents" / "kora" / "custodio" / "AGENTS.md").read_text(encoding="utf-8")
        surgeon = (
            ROOT / "agents" / "kora" / "custodio" / "skills" / "CM-SURGEON.md"
        ).read_text(encoding="utf-8")
        evolution = (
            ROOT / "agents" / "kora" / "custodio" / "skills" / "CM-EVOLUCION-PLANNER.md"
        ).read_text(encoding="utf-8")
        self.assertIn("fuera de `agents/`, specs fundacionales y contenido KB", agents)
        self.assertIn("sin intervenir `agents/`, specs fundacionales ni contenido KB", surgeon)
        self.assertIn("fuera de `agents/`, specs fundacionales y contenido KB", evolution)

    def test_curator_and_custodio_soul_avoid_operational_policy_leakage(self):
        curator = (ROOT / "agents" / "kora" / "curator" / "SOUL.md").read_text(encoding="utf-8")
        custodio = (ROOT / "agents" / "kora" / "custodio" / "SOUL.md").read_text(encoding="utf-8")
        self.assertNotIn("FS=100%", curator)
        self.assertNotIn("CR>1.5", curator)
        self.assertNotIn("Pipeline de ingesta", curator)
        self.assertNotIn("catalog_master_kora.yml", custodio)
        self.assertNotIn("Pipeline como flujo", custodio)

    def test_meta_core_tools_stay_semantic(self):
        custodio_tools = (ROOT / "agents" / "kora" / "custodio" / "TOOLS.md").read_text(encoding="utf-8")
        forgemaster_tools = (
            ROOT / "agents" / "kora" / "forgemaster" / "TOOLS.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn("Implementacion:", custodio_tools)
        self.assertNotIn("Invoca internamente", forgemaster_tools)
        self.assertNotIn("Leer todos los archivos del workspace", forgemaster_tools)

    def test_runtime_spec_restores_adapter_and_equivalence_contract(self):
        content = (ROOT / "specs" / "runtime-spec-md.md").read_text(encoding="utf-8")
        required_terms = (
            "## 4. Adapters por plataforma",
            "## 5. Wrapper generation",
            "## 6. Platform equivalence",
            "## 7. Model routing",
            "## 8. Fallback chains y budget",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_swarm_spec_restores_operational_orchestration_contract(self):
        content = (ROOT / "specs" / "swarm-spec-md.md").read_text(encoding="utf-8")
        required_terms = (
            "## 4. Golden Paths",
            "## 5. Circuit Breakers",
            "## 6. Backpressure",
            "## 7. Event Routing",
            "## 9. Security inter-agente",
            "## 10. Sentinel pattern",
        )
        for term in required_terms:
            self.assertIn(term, content)

    def test_curator_tracks_restored_md_and_spec_contracts(self):
        files = (
            ROOT / "agents" / "kora" / "curator" / "AGENTS.md",
            ROOT / "agents" / "kora" / "curator" / "SOUL.md",
            ROOT / "agents" / "kora" / "curator" / "TOOLS.md",
            ROOT / "agents" / "kora" / "curator" / "skills" / "CM-KORAFICATOR.md",
            ROOT / "agents" / "kora" / "curator" / "skills" / "CM-CRYSTALLIZER.md",
            ROOT / "agents" / "kora" / "curator" / "skills" / "CM-ARTIFACT-AUDITOR.md",
            ROOT / "agents" / "kora" / "curator" / "skills" / "CM-ARTIFACT-DESIGNER.md",
            ROOT / "agents" / "kora" / "curator" / "skills" / "CM-LIFECYCLE-ORCHESTRATOR.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("Funtor K", content)
        self.assertIn("Funtor C", content)
        self.assertIn("md-spec §9", content)
        self.assertNotIn("Funtor F", content)
        self.assertNotIn("Funtor G", content)
        self.assertNotIn("md-spec §8", content)
        self.assertNotIn("verificacion adversarial", content)

    def test_ops_core_agents_follow_canonical_agent_sections(self):
        files = (
            ROOT / "agents" / "ops" / "orquestador-swarm" / "AGENTS.md",
            ROOT / "agents" / "ops" / "security" / "AGENTS.md",
            ROOT / "agents" / "ops" / "verificador" / "AGENTS.md",
        )
        required_terms = (
            "## 3. Co-induccion",
            "## 4. Contexto Multi-turno",
            "## 5. Wiring",
        )
        for path in files:
            content = path.read_text(encoding="utf-8")
            for term in required_terms:
                self.assertIn(term, content)

    def test_all_agents_follow_canonical_section_order(self):
        for path in ROOT.glob("agents/*/*/AGENTS.md"):
            content = path.read_text(encoding="utf-8")
            self.assertEqual(validate_agents_canonical_structure(content), [], path.as_posix())

    def test_orquestador_swarm_drops_dead_swarm_section_refs(self):
        files = (
            ROOT / "agents" / "ops" / "orquestador-swarm" / "AGENTS.md",
            ROOT / "agents" / "ops" / "orquestador-swarm" / "TOOLS.md",
            ROOT / "agents" / "ops" / "orquestador-swarm" / "skills" / "CM-CIRCUIT-BREAKER-MANAGER.md",
        )
        content = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertNotIn("Swarm::Ops §10", content)
        self.assertNotIn("§10.1", content)
        self.assertNotIn("§10.2", content)
        self.assertNotIn("§10.3", content)
        self.assertNotIn("§10.4", content)

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
