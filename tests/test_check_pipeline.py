"""Tests for the unified check pipeline and check algebra properties."""

import unittest
from common import run_cli, ROOT


class CheckPipelineSmokeTests(unittest.TestCase):
    """Smoke tests for kora check CLI command."""

    def test_check_runs_without_error(self):
        result = run_cli("check")
        self.assertIn("Checks run:", result.stdout)
        self.assertIn("Summary", result.stdout)

    def test_check_list_shows_all_checks(self):
        result = run_cli("check", "--list")
        self.assertIn("Check Registry", result.stdout)
        self.assertIn("catalog-exists", result.stdout)
        self.assertIn("urn-integrity", result.stdout)
        self.assertIn("knowledge-zone", result.stdout)
        self.assertIn("lint-md", result.stdout)

    def test_check_strict_exits_zero_when_clean(self):
        result = run_cli("check", "--strict", check=False)
        self.assertEqual(result.returncode, 0, f"check --strict failed:\n{result.stdout}\n{result.stderr}")

    def test_check_scope_filter(self):
        result = run_cli("check", "--scope", "repo")
        self.assertIn("Checks run:", result.stdout)

    def test_check_severity_filter(self):
        result = run_cli("check", "--severity", "critical")
        self.assertIn("Checks run:", result.stdout)

    def test_check_phase_filter(self):
        result = run_cli("check", "--phase", "verify")
        self.assertIn("Checks run:", result.stdout)


class CheckAlgebraTests(unittest.TestCase):
    """Tests for categorical properties of the check algebra."""

    def test_no_duplicate_check_ids(self):
        from kora_lib.checks import all_checks
        checks = all_checks()
        ids = [c.id for c in checks]
        self.assertEqual(len(ids), len(set(ids)), f"Duplicate check IDs: {[x for x in ids if ids.count(x) > 1]}")

    def test_dependency_dag_is_acyclic(self):
        from kora_lib.checks import all_checks
        checks = all_checks()
        check_ids = {c.id for c in checks}
        # All dependencies reference existing checks
        for c in checks:
            for dep in c.depends:
                self.assertIn(dep, check_ids, f"Check {c.id} depends on nonexistent check {dep}")
        # No cycles via DFS
        adj = {c.id: list(c.depends) for c in checks}
        visited = set()
        in_stack = set()
        def has_cycle(node):
            if node in in_stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            in_stack.add(node)
            for dep in adj.get(node, []):
                if has_cycle(dep):
                    return True
            in_stack.discard(node)
            return False
        for c in checks:
            self.assertFalse(has_cycle(c.id), f"Cycle detected involving check {c.id}")

    def test_topo_sort_produces_valid_ordering(self):
        from kora_lib.checks import all_checks, _topo_sort
        checks = all_checks()
        ordered = _topo_sort(checks)
        ordered_ids = [c.id for c in ordered]
        # Every check appears exactly once
        self.assertEqual(sorted(ordered_ids), sorted(c.id for c in checks))
        # Every dependency comes before the check that depends on it
        for c in ordered:
            pos = ordered_ids.index(c.id)
            for dep in c.depends:
                dep_pos = ordered_ids.index(dep)
                self.assertLess(dep_pos, pos, f"Dependency {dep} appears after {c.id}")

    def test_every_check_has_implementation(self):
        from kora_lib.checks import all_checks, _IMPLEMENTATIONS
        for c in all_checks():
            self.assertIn(c.id, _IMPLEMENTATIONS, f"Check {c.id} has no implementation")

    def test_checks_with_fix_have_fix_registered(self):
        from kora_lib.checks import all_checks, _FIXES
        # At least catalog-exists and lint-md have fixes
        self.assertIn("catalog-exists", _FIXES)
        self.assertIn("lint-md", _FIXES)

    def test_minimum_check_count(self):
        from kora_lib.checks import all_checks
        self.assertGreaterEqual(len(all_checks()), 10)

    def test_all_severities_valid(self):
        from kora_lib.checks import all_checks
        valid = {"critical", "high", "medium", "low"}
        for c in all_checks():
            self.assertIn(c.severity, valid, f"Check {c.id} has invalid severity {c.severity}")

    def test_all_scopes_valid(self):
        from kora_lib.checks import all_checks
        valid = {"artifact", "workspace", "repo"}
        for c in all_checks():
            self.assertIn(c.scope, valid, f"Check {c.id} has invalid scope {c.scope}")


class KbGraphSmokeTests(unittest.TestCase):
    """Smoke tests for kb-graph command."""

    def test_kb_graph_runs(self):
        result = run_cli("kb-graph")
        self.assertIn("Knowledge Graph", result.stdout)

    def test_kb_graph_json_produces_file(self):
        result = run_cli("kb-graph", "--json")
        import json
        graph_path = ROOT / "docs" / "generated" / "kb-graph.json"
        self.assertTrue(graph_path.exists())
        data = json.loads(graph_path.read_text())
        self.assertIn("nodes", data)
        self.assertIn("edges", data)
        self.assertIn("stats", data)

    def test_kb_graph_check_cycles_passes(self):
        result = run_cli("kb-graph", "--check-cycles", check=False)
        self.assertEqual(result.returncode, 0)


class PromoteSmokeTests(unittest.TestCase):
    """Smoke tests for promote command."""

    def test_promote_rejects_nonexistent_file(self):
        result = run_cli("promote", "/tmp/nonexistent.md", check=False)
        self.assertNotEqual(result.returncode, 0)

    def test_promote_rejects_file_outside_drafts(self):
        result = run_cli("promote", "KNOWLEDGE/kora/sys/pipeline-ingesta.md", check=False)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
