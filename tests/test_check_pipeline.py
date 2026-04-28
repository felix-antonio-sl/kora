"""Tests for the unified check pipeline and check algebra properties."""

import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from common import run_cli, ROOT
from kora_lib.graph import GraphEdge


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
        self.assertIn("traces-requirements-semantics", result.stdout)
        self.assertIn("formal-trace-discipline", result.stdout)
        self.assertIn("autoria-conformance", result.stdout)
        self.assertIn("construction-source-primary", result.stdout)
        self.assertIn("construction-vector-fit", result.stdout)
        self.assertIn("construction-knowledge-explicit", result.stdout)
        self.assertIn("construction-authoring-shape", result.stdout)

    def test_check_strict_exit_status_matches_diagnostics(self):
        result = run_cli("check", "--strict", check=False)
        self.assertIn("Summary", result.stdout)
        match = re.search(r"Total diagnostics:\s+(\d+)", result.stdout)
        diagnostics = int(match.group(1)) if match else 0
        expected = 0 if diagnostics == 0 else 1
        self.assertEqual(result.returncode, expected, f"check --strict status mismatch:\n{result.stdout}\n{result.stderr}")

    def test_check_scope_filter(self):
        result = run_cli("check", "--scope", "repo")
        self.assertIn("Checks run:", result.stdout)

    def test_check_severity_filter(self):
        result = run_cli("check", "--severity", "critical")
        self.assertIn("Checks run:", result.stdout)

    def test_check_phase_filter(self):
        result = run_cli("check", "--phase", "verify")
        self.assertIn("Checks run:", result.stdout)

    def test_catalog_exists_fix_hint_uses_toolchain_entrypoint(self):
        from unittest.mock import patch
        from kora_lib.checks import _check_catalog_exists

        with patch("kora_lib.catalog.load_catalog", return_value=None):
            diags = _check_catalog_exists()

        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].path, "docs/generated/catalog.yml")
        self.assertEqual(diags[0].fix_hint, "python3 toolchain/kora index")

    def test_lint_md_fix_hint_uses_toolchain_entrypoint(self):
        from unittest.mock import patch
        from kora_lib.checks import _check_lint_md

        fake_issues = {"issues": [("artifacts/knowledge/kora/example.md", "mock lint failure")]}
        with patch("kora_lib.validation.lint_markdown_paths", return_value=fake_issues):
            diags = _check_lint_md()

        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].fix_hint, "python3 toolchain/kora lint-md --fix")

    def test_traces_requirements_semantics_rejects_non_requirement_targets(self):
        from kora_lib.checks import _check_traces_requirements_semantics

        nodes = [
            {
                "urn": "urn:kora:kb:trace-model",
                "file": "artifacts/knowledge/kora/sys/trace-model.md",
                "relations": {"traces_requirements": ["urn:kora:kb:not-a-requirement"]},
                "is_requirement": False,
            },
            {
                "urn": "urn:kora:kb:not-a-requirement",
                "file": "artifacts/knowledge/kora/sys/not-a-requirement.md",
                "relations": {},
                "is_requirement": False,
            },
        ]

        with patch("kora_lib.kb_graph.collect_knowledge_nodes", return_value=nodes):
            diags = _check_traces_requirements_semantics()

        self.assertEqual(len(diags), 1)
        self.assertIn("non-requirement node", diags[0].message)

    def test_construction_checks_reject_non_current_shape(self):
        from kora_lib.checks import _check_construction_authoring_shape, _check_construction_vector_fit

        artifact = (
            ROOT / "artifacts" / "agents" / "demo" / "draft" / "AGENT.md",
            "artifacts/agents/demo/draft/AGENT.md",
            {
                "_manifest": {"urn": "urn:kora:artefacto:draft"},
                "status": "activo",
                "agent": {},
                "extensions": {
                    "kora": {
                        "atlas": {"forma_material": "agente-propiamente-tal"},
                        "harness_vector": {"pi": 1, "mu": 1, "xi": 1, "lambda": 0, "phi": 1, "sigma": [1]},
                        "vector_ontologico": {"pi": 1, "mu": 1, "xi": 1, "lambda": 0, "phi": 1, "sigma": [1]},
                    }
                },
            },
        )

        with patch("kora_lib.checks._iter_construction_artifacts", return_value=[artifact]):
            shape_diags = _check_construction_authoring_shape()
            vector_diags = _check_construction_vector_fit()

        self.assertTrue(any("artefacto" in d.message for d in shape_diags))
        self.assertTrue(any("harness_vector" in d.message for d in vector_diags))

    def test_construction_knowledge_requires_urns(self):
        from kora_lib.checks import _check_construction_knowledge_explicit

        artifact = (
            ROOT / "artifacts" / "skills" / "demo" / "bad-kb" / "SKILL.md",
            "artifacts/skills/demo/bad-kb/SKILL.md",
            {
                "_manifest": {"urn": "urn:kora:artefacto:bad-kb"},
                "status": "activo",
                "extensions": {
                    "kora": {
                        "atlas": {"forma_material": "habilidad"},
                        "conocimiento_permitido": ["serialization/autoria-spec.md"],
                    }
                },
            },
        )

        with patch("kora_lib.checks._iter_construction_artifacts", return_value=[artifact]):
            diags = _check_construction_knowledge_explicit()

        self.assertEqual(len(diags), 1)
        self.assertIn("no-URN", diags[0].message)


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

    def test_urn_integrity_accepts_bootstrap_alias_and_retired_targets(self):
        from kora_lib.checks import _check_urn_integrity

        fake_doc = {"_manifest": {"urn": "urn:kora:catalog:master:2.0.0"}, "Catalog": {}}
        fake_known = {
            "urn:kora:catalog:master:2.0.0",
            "urn:kora:kb:autoria-spec",
            "urn:kora:kb:cat-governance-lattice",
        }
        fake_edges = [
            GraphEdge("XRef", ROOT / "artifacts" / "agents" / "kora" / "guardian" / "AGENT.md", "urn:kora:agent-bootstrap:guardian-user:1.0.0"),
            GraphEdge("XRef", ROOT / "artifacts" / "agents" / "kora" / "guardian" / "AGENT.md", "urn:kora:kb:agent-spec-md"),
            GraphEdge("XRef", ROOT / "serialization" / "autoria-spec.md", "urn:kora:kb:agentfile-spec"),
            GraphEdge("XRef", ROOT / "serialization" / "md-spec.md", "urn:kora:kb:05-governance-lattice"),
            GraphEdge("XRef", ROOT / "serialization" / "md-spec.md", "urn:kora:kb:definitely-missing"),
        ]

        with patch("kora_lib.catalog.load_catalog", return_value=fake_doc), patch(
            "kora_lib.catalog.build_catalog_lookup",
            return_value=(fake_known, {}),
        ), patch("kora_lib.graph.build_reference_graph", return_value=(1, fake_edges)):
            diags = _check_urn_integrity()

        self.assertEqual(len(diags), 1)
        self.assertEqual(diags[0].message, "Broken URN reference: urn:kora:kb:definitely-missing")


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
        with tempfile.TemporaryDirectory() as tmp:
            nonexistent = Path(tmp) / "nonexistent.md"
            result = run_cli("promote", str(nonexistent), check=False)
            self.assertNotEqual(result.returncode, 0)

    def test_promote_rejects_file_outside_drafts(self):
        result = run_cli("promote", "KNOWLEDGE/kora/sys/pipeline-ingesta.md", check=False)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
