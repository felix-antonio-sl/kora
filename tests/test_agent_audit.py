import json
import textwrap
import unittest

from common import GENERATED_DOCS, run_cli
from kora_lib.agent_audit import (
    audit_agents_file,
    audit_config_file,
    audit_skill_file,
    audit_tools_file,
    build_agent_audit_payload,
)


class AgentAuditTests(unittest.TestCase):
    def test_agents_audit_flags_pseudostate_destination(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "AGENTS.md"
            path.write_text(
                "1. STATE: S-DISPATCHER -> ACT: clasificar -> Trans: IF shift -> CONTEXT_SHIFT.\n",
                encoding="utf-8",
            )
            findings = audit_agents_file("test/sample", path)
            self.assertEqual(findings[0]["rule_id"], "agent.fsm_pseudostate_destination")

    def test_agents_audit_flags_missing_transition_precedence(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "AGENTS.md"
            path.write_text(
                "1. STATE: S-DISPATCHER -> ACT: clasificar -> Trans: IF a -> S-A. IF b -> S-B.\n",
                encoding="utf-8",
            )
            findings = audit_agents_file("test/sample", path)
            self.assertTrue(any(item["rule_id"] == "agent.missing_transition_precedence" for item in findings))

    def test_tools_audit_flags_policy_leakage(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "TOOLS.md"
            path.write_text("## file_write\n- **Notas:** SIEMPRE requiere confirmacion del usuario.\n", encoding="utf-8")
            findings = audit_tools_file("test/sample", path)
            self.assertEqual(findings[0]["rule_id"], "tools.policy_leakage")

    def test_config_audit_flags_semantic_runtime_capability(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "config.json"
            path.write_text(
                json.dumps({"runtime_capabilities": {"allow": ["analysis"], "deny": []}}),
                encoding="utf-8",
            )
            findings = audit_config_file("test/sample", path)
            self.assertEqual(findings[0]["rule_id"], "config.semantic_runtime_capability")

    def test_skill_audit_flags_state_leak_and_rule_relaxation(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "CM-TEST.md"
            path.write_text(
                textwrap.dedent(
                    """\
                    ## Input/Output
                    - **Input:** estado_actual: FSMState
                    ## Procedimiento
                    1. Si CR < 1.5, aceptar por densidad.
                    2. La FSM debe volver a despachar.
                    """
                ),
                encoding="utf-8",
            )
            findings = audit_skill_file("test/sample", path, "CR>1.5")
            rule_ids = {item["rule_id"] for item in findings}
            self.assertIn("skill.state_variable_leak", rule_ids)
            self.assertIn("skill.transition_classifier_leak", rule_ids)
            self.assertIn("skill.relaxes_hard_rule", rule_ids)

    def test_build_agent_audit_payload_has_expected_shape(self):
        payload = build_agent_audit_payload()
        self.assertIn("cohorts", payload)
        self.assertEqual(set(payload["cohorts"].keys()), {"meta-kora", "dev", "ops", "domains"})
        self.assertIn("global_summary", payload)
        self.assertIn("top_systemic_debts", payload["global_summary"])
        self.assertIn("top_false_greens", payload["global_summary"])

    def test_sync_docs_generates_agent_audit_docs(self):
        run_cli("sync-docs")
        payload = json.loads((GENERATED_DOCS / "agent-audit.json").read_text(encoding="utf-8"))
        markdown = (GENERATED_DOCS / "agent-audit.md").read_text(encoding="utf-8")
        self.assertIn("cohorts", payload)
        self.assertIn("meta-kora", payload["cohorts"])
        self.assertIn("## Cohorte meta-kora", markdown)


if __name__ == "__main__":
    unittest.main()
