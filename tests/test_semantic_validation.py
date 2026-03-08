import unittest

from common import ROOT
from kora_lib.validation import (
    build_formal_trace_targets,
    formal_section_exists,
    validate_agents_semantics,
    validate_config_semantics,
    validate_kb_pipeline_consistency,
    validate_skill_purity,
    validate_soul_semantics,
    validate_tools_semantics,
    validate_traces_semantics,
    validate_user_semantics,
)


class SemanticValidationTests(unittest.TestCase):
    def test_soul_semantics_flags_explicit_fsm_syntax(self):
        failures = validate_soul_semantics("STATE: S-DISPATCHER -> ACT: clasificar\n")
        self.assertTrue(failures)

    def test_soul_semantics_ignores_state_names_in_narrative_examples(self):
        failures = validate_soul_semantics('Ejemplo: "dashboard" -> S-METRICAS.\n')
        self.assertEqual(failures, [])

    def test_user_semantics_flags_security_leak(self):
        failures = validate_user_semantics("Preferencias: sandbox strict\n")
        self.assertTrue(failures)

    def test_agents_semantics_flags_legacy_confidentiality(self):
        failures = validate_agents_semantics("- Confidentiality: block_instructions=true\n")
        self.assertTrue(failures)

    def test_skill_purity_flags_conversational_turn_control(self):
        failures = validate_skill_purity("Si ambiguedad: preguntar al usuario\n")
        self.assertTrue(failures)

    def test_skill_purity_allows_structured_pending_state(self):
        failures = validate_skill_purity("Emitir gate_result.status = pending_approval hasta decision humana.\n")
        self.assertEqual(failures, [])

    def test_tools_semantics_flags_runtime_permission_heading(self):
        content = "## filesystem_write\n- **Firma:** x\n"
        failures = validate_tools_semantics(content, ["filesystem_write"])
        self.assertTrue(failures)

    def test_tools_semantics_requires_semantic_markers(self):
        content = "## kb_route\nDescripcion sin markers\n"
        failures = validate_tools_semantics(content, ["kb_route"])
        self.assertTrue(failures)

    def test_kb_pipeline_consistency_flags_legacy_catalog_to_kb_route(self):
        failures = validate_kb_pipeline_consistency(["Fuente correcta via cadena catalog→kb_route"])
        self.assertTrue(failures)

    def test_kb_pipeline_consistency_accepts_kb_route_to_catalog_resolve(self):
        failures = validate_kb_pipeline_consistency(["Fuente correcta via cadena kb_route→catalog_resolve"])
        self.assertEqual(failures, [])

    def test_formal_section_exists_for_real_section(self):
        targets = build_formal_trace_targets()
        self.assertTrue(formal_section_exists(targets["05"]["path"], "1.2"))

    def test_validate_traces_semantics_flags_missing_section_anchor(self):
        failures = validate_traces_semantics(ROOT / "specs" / "dummy.md", "Traces to: formal/05 (Bounded Lattice)\n")
        self.assertTrue(failures)

    def test_validate_traces_semantics_flags_fxsl_direct_support(self):
        failures = validate_traces_semantics(
            ROOT / "specs" / "dummy.md",
            "Traces to: formal/05 §1.2 (Bounded Lattice), knowledge/fxsl/cat/audit-patterns.md\n",
        )
        self.assertTrue(failures)

    def test_validate_traces_semantics_accepts_real_trace(self):
        failures = validate_traces_semantics(
            ROOT / "specs" / "dummy.md",
            "Traces to: formal/05 §1.2 (Bounded Lattice)\n",
        )
        self.assertEqual(failures, [])

    def test_validate_config_semantics_flags_runtime_overlap(self):
        config_data = {
            "tools": {"allow": ["kb_route"], "deny": []},
            "runtime_capabilities": {"allow": ["kb_route"], "deny": []},
        }
        failures = validate_config_semantics(config_data, ["kb_route"])
        self.assertTrue(failures)


if __name__ == "__main__":
    unittest.main()
