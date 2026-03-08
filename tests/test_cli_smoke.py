import json
import unittest

from common import GENERATED_DOCS, ROOT, run_cli


class KoraCliSmokeTests(unittest.TestCase):
    def test_health_strict_is_green(self):
        result = run_cli("health", "--strict")
        self.assertIn("All URN references are healthy!", result.stdout)

    def test_validate_strict_is_green(self):
        result = run_cli("validate", "--profile", "strict")
        self.assertIn("Invalid: 0", result.stdout)

    def test_resolve_config_urn_returns_expected_path(self):
        result = run_cli("resolve", "urn:kora:agent-bootstrap:guardian-config:1.0.0")
        self.assertIn("/Users/felixsanhueza/Developer/kora/agents/kora/guardian/config.json", result.stdout)

    def test_migrate_is_idempotent_on_clean_repo(self):
        result = run_cli("migrate", "--profile", "transitional")
        self.assertIn("Changed paths: 0", result.stdout)

    def test_sync_docs_generates_live_stats_files(self):
        run_cli("sync-docs")
        payload = json.loads((GENERATED_DOCS / "repo-stats.json").read_text(encoding="utf-8"))
        markdown = (GENERATED_DOCS / "repo-stats.md").read_text(encoding="utf-8")
        self.assertGreater(payload["agent_workspaces"], 0)
        self.assertGreater(payload["total_catalog_entries"], 0)
        self.assertIn("Entradas totales de catalogo", markdown)

    def test_sync_docs_generates_repo_graph_operating_core_and_fxsl_cat_ledger(self):
        run_cli("sync-docs")
        graph_payload = json.loads((GENERATED_DOCS / "repo-graph.json").read_text(encoding="utf-8"))
        contracts_payload = json.loads((GENERATED_DOCS / "operating-core-contracts.json").read_text(encoding="utf-8"))
        ledger_payload = json.loads((GENERATED_DOCS / "fxsl-cat-ledger.json").read_text(encoding="utf-8"))
        self.assertGreater(graph_payload["meta"]["node_count"], 0)
        self.assertIn("kora", contracts_payload["cohorts"])
        self.assertEqual(contracts_payload["totals"]["workspaces"], 12)
        self.assertIn(
            "gn/digitrans",
            {item["workspace"] for item in contracts_payload["cohorts"]["domain_canary"]},
        )
        self.assertIn("promoted", ledger_payload["status_counts"])

    def test_stats_json_matches_generated_payload(self):
        run_cli("sync-docs")
        cli_payload = json.loads(run_cli("stats", "--json").stdout)
        generated_payload = json.loads((GENERATED_DOCS / "repo-stats.json").read_text(encoding="utf-8"))
        self.assertEqual(cli_payload, generated_payload)

    def test_graph_json_has_required_node_and_edge_kinds(self):
        payload = json.loads(run_cli("graph", "--json").stdout)
        for kind in ("artifact", "workspace", "skill", "knowledge", "spec"):
            self.assertIn(kind, payload["node_kind_counts"])
        for kind in ("XRef", "TracesTo", "InvokesSkill", "RoutesToAgent", "DeclaresTool", "AllowsTool", "AllowsKB"):
            self.assertIn(kind, payload["edge_kind_counts"])

    def test_validate_strict_by_meta_kora_cohort_is_green(self):
        result = run_cli("validate", "--profile", "strict", "--cohort", "meta-kora")
        self.assertIn("Invalid: 0", result.stdout)

    def test_migrate_meta_kora_cohort_is_idempotent(self):
        result = run_cli("migrate", "--profile", "transitional", "--cohort", "meta-kora")
        self.assertIn("Changed paths: 0", result.stdout)


if __name__ == "__main__":
    unittest.main()
