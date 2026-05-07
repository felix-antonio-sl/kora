"""Tests for the claude-code budget functor and the budget-piso check.

Verifica la politica funtorial declarada en
`runtime/claude-code-runtime-extension.md §4.1`:

- T_{claude-code}: vector_ontologico -> (modo, max_turns_floor, effort_default)
- Bonus aditivo por Pi=3 y Xi>=3
- Promocion de effort a "max" cuando Pi=3, Xi>=3 o Phi>=3
- Override max_turns gana solo si respeta el piso

Y el check `claude-code-budget-piso` que enforce el piso.
"""

import unittest

from common import ROOT  # noqa: F401  (registers toolchain/ in sys.path)

from kora_lib.transmute import _derive_claude_code_budget
from kora_lib.checks import _derive_claude_code_floor


class DeriveClaudeCodeBudgetTests(unittest.TestCase):
    """Pure-function tests for the budget derivation."""

    def test_skill_vector_yields_skill_mode_no_budget(self):
        d = _derive_claude_code_budget({"pi": 1, "mu": 0, "xi": 1, "phi": 1})
        self.assertEqual(d["modo"], "skill")
        self.assertIsNone(d["max_turns_floor"])
        self.assertIsNone(d["effort_default"])

    def test_subagent_default(self):
        d = _derive_claude_code_budget({"pi": 2, "mu": 1, "xi": 2, "phi": 1})
        self.assertEqual(d["modo"], "subagent")
        self.assertEqual(d["max_turns_floor"], 10)
        self.assertEqual(d["effort_default"], "high")

    def test_persona_default(self):
        d = _derive_claude_code_budget({"pi": 2, "mu": 2, "xi": 2, "phi": 2})
        self.assertEqual(d["modo"], "persona")
        self.assertEqual(d["max_turns_floor"], 12)
        self.assertEqual(d["effort_default"], "high")

    def test_persona_with_complex_xi_promotes_effort_and_adds_bonus(self):
        d = _derive_claude_code_budget({"pi": 2, "mu": 2, "xi": 3, "phi": 2})
        self.assertEqual(d["modo"], "persona")
        self.assertEqual(d["max_turns_floor"], 15)
        self.assertEqual(d["effort_default"], "max")

    def test_persona_with_pi3_adds_bonus_and_promotes_effort(self):
        d = _derive_claude_code_budget({"pi": 3, "mu": 2, "xi": 2, "phi": 2})
        self.assertEqual(d["modo"], "persona")
        self.assertEqual(d["max_turns_floor"], 15)
        self.assertEqual(d["effort_default"], "max")

    def test_persona_with_pi3_and_xi3_adds_both_bonuses(self):
        d = _derive_claude_code_budget({"pi": 3, "mu": 2, "xi": 3, "phi": 3})
        self.assertEqual(d["modo"], "persona")
        self.assertEqual(d["max_turns_floor"], 18)
        self.assertEqual(d["effort_default"], "max")

    def test_high_phi_alone_promotes_effort_no_floor_bonus(self):
        d = _derive_claude_code_budget({"pi": 2, "mu": 2, "xi": 2, "phi": 3})
        self.assertEqual(d["modo"], "persona")
        self.assertEqual(d["max_turns_floor"], 12)
        self.assertEqual(d["effort_default"], "max")

    def test_mu3_is_out_of_domain(self):
        d = _derive_claude_code_budget({"pi": 2, "mu": 3, "xi": 2, "phi": 2})
        self.assertEqual(d["modo"], "out-of-domain")
        self.assertIsNone(d["max_turns_floor"])

    def test_invalid_vector_falls_back_to_persona(self):
        d = _derive_claude_code_budget(None)
        self.assertEqual(d["modo"], "persona")
        self.assertEqual(d["max_turns_floor"], 12)


class CheckFloorMirrorTests(unittest.TestCase):
    """The reduced floor function used by the check must agree with the functor."""

    def _floor_via_functor(self, vector):
        d = _derive_claude_code_budget(vector)
        return d["modo"], d["max_turns_floor"]

    def test_mirror_subagent(self):
        v = {"pi": 2, "mu": 1, "xi": 2}
        self.assertEqual(_derive_claude_code_floor(v), self._floor_via_functor(v))

    def test_mirror_persona_with_bonuses(self):
        v = {"pi": 3, "mu": 2, "xi": 3}
        self.assertEqual(_derive_claude_code_floor(v), self._floor_via_functor(v))

    def test_mirror_skill(self):
        v = {"pi": 1, "mu": 0, "xi": 1}
        self.assertEqual(_derive_claude_code_floor(v), self._floor_via_functor(v))


class BudgetPisoCheckRegistrationTests(unittest.TestCase):
    """The check is registered and listed in the registry."""

    def test_check_registered(self):
        from kora_lib.checks import get_check
        check = get_check("claude-code-budget-piso")
        self.assertIsNotNone(check)
        self.assertEqual(check.scope, "workspace")
        self.assertEqual(check.severity, "medium")
        self.assertIn("vector-laws", check.depends)


if __name__ == "__main__":
    unittest.main()
