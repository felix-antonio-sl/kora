import unittest

import jsonschema

from common import FIXTURES, ROOT, load_json
from kora_lib.artifacts import load_yaml_safe
from kora_lib.config import AGENT_REQUIRED_FILES
from kora_lib.reports import compute_stats_payload, render_stats_markdown
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

    def test_skill_spec_restores_lifecycle_and_protocol(self):
        content = (ROOT / "specs" / "skill-spec-md.md").read_text(encoding="utf-8")
        required_terms = (
            "## 5. Progressive Disclosure Lifecycle",
            "Discover",
            "Activate",
            "Execute",
            "### 3.3 Script Protocol",
            "Wrap",
            "Extract",
        )
        for term in required_terms:
            self.assertIn(term, content)

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
