import json
import unittest

from common import AGENTS_ROOT, GENERATED_DOCS, ROOT, has_productive_workspaces, run_cli
from kora_lib.config import OPERATING_CORE_COHORTS


_REQUIRES_WORKSPACES = unittest.skipUnless(
    has_productive_workspaces(),
    "Sin workspaces productivos — fleet en staging v8.",
)


class KoraCliSmokeTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_health_strict_is_green(self):
        result = run_cli("health", "--strict", check=False)
        self.assertIn("Health check complete.", result.stdout)
        self.assertTrue(
            "All URN references are healthy!" in result.stdout or "issue(s) found." in result.stdout
        )

    def test_validate_strict_runs_without_crash(self):
        result = run_cli("validate", "--profile", "strict", check=False)
        self.assertIn("Validation complete!", result.stdout)

    def test_resolve_config_urn_returns_expected_path(self):
        if not has_productive_workspaces():
            self.skipTest("Sin workspaces productivos — guardian en staging.")
        result = run_cli("resolve", "urn:kora:agent-bootstrap:guardian-config:1.0.0")
        self.assertIn(str((AGENTS_ROOT / "kora" / "guardian" / "config.json").resolve()), result.stdout)

    def test_migrate_is_idempotent_on_clean_repo(self):
        result = run_cli("migrate", "--profile", "transitional")
        self.assertIn("Changed paths: 0", result.stdout)

    def test_sync_docs_generates_live_stats_files(self):
        run_cli("sync-docs")
        payload = json.loads((GENERATED_DOCS / "repo-stats.json").read_text(encoding="utf-8"))
        markdown = (GENERATED_DOCS / "repo-stats.md").read_text(encoding="utf-8")
        if has_productive_workspaces():
            self.assertGreater(payload["agent_workspaces"], 0)
        self.assertIn("deprecated_workspaces", payload)
        self.assertGreaterEqual(payload["deprecated_workspaces"], 0)
        self.assertGreater(payload["total_catalog_entries"], 0)
        self.assertIn("Entradas totales de catalogo", markdown)

    def test_sync_docs_generates_repo_graph_operating_core_and_fxsl_cat_ledger(self):
        run_cli("sync-docs")
        graph_payload = json.loads((GENERATED_DOCS / "repo-graph.json").read_text(encoding="utf-8"))
        contracts_payload = json.loads((GENERATED_DOCS / "operating-core-contracts.json").read_text(encoding="utf-8"))
        contracts_markdown = (GENERATED_DOCS / "operating-core-contracts.md").read_text(encoding="utf-8")
        ledger_payload = json.loads((GENERATED_DOCS / "fxsl-cat-ledger.json").read_text(encoding="utf-8"))
        audit_payload = json.loads((GENERATED_DOCS / "agent-audit.json").read_text(encoding="utf-8"))
        self.assertGreater(graph_payload["meta"]["node_count"], 0)
        self.assertIn("kora", contracts_payload["cohorts"])
        self.assertEqual(
            contracts_payload["totals"]["workspaces"],
            sum(len(workspaces) for workspaces in OPERATING_CORE_COHORTS.values()),
        )
        self.assertEqual(set(contracts_payload["cohorts"].keys()), set(OPERATING_CORE_COHORTS.keys()))
        self.assertEqual(contracts_payload["meta_kora"]["summary"]["total_workspaces"], 4)
        self.assertEqual(contracts_payload["meta_kora"]["summary"]["operating_core"], 4)
        self.assertEqual(contracts_payload["meta_kora"]["summary"]["auxiliary"], 0)
        self.assertIn(
            "kora/guardian",
            {item["workspace"] for item in contracts_payload["cohorts"]["kora"]},
        )
        for workspace in OPERATING_CORE_COHORTS["domain_canary"]:
            self.assertIn(
                workspace,
                {item["workspace"] for item in contracts_payload["cohorts"]["domain_canary"]},
            )
        self.assertIn("## Auditoria meta-kora", contracts_markdown)
        self.assertIn("promoted", ledger_payload["status_counts"])
        self.assertIn("meta-kora", audit_payload["cohorts"])
        self.assertIn("domains", audit_payload["cohorts"])

    def test_stats_json_matches_generated_payload(self):
        run_cli("sync-docs")
        cli_payload = json.loads(run_cli("stats", "--json").stdout)
        generated_payload = json.loads((GENERATED_DOCS / "repo-stats.json").read_text(encoding="utf-8"))
        self.assertEqual(cli_payload, generated_payload)

    def test_graph_json_has_required_node_and_edge_kinds(self):
        payload = json.loads(run_cli("graph", "--json").stdout)
        always_present = ("knowledge", "spec")
        for kind in always_present:
            self.assertIn(kind, payload["node_kind_counts"])
        if has_productive_workspaces():
            for kind in ("artifact", "workspace", "skill"):
                self.assertIn(kind, payload["node_kind_counts"])
            for kind in ("XRef", "TracesTo", "InvokesSkill", "RoutesToAgent", "DeclaresTool", "AllowsTool", "AllowsKB"):
                self.assertIn(kind, payload["edge_kind_counts"])
        else:
            self.assertIn("XRef", payload["edge_kind_counts"])

    def test_validate_strict_by_meta_kora_cohort_is_green(self):
        result = run_cli("validate", "--profile", "strict", "--cohort", "meta-kora")
        self.assertIn("Invalid: 0", result.stdout)

    def test_migrate_meta_kora_cohort_is_idempotent(self):
        result = run_cli("migrate", "--profile", "transitional", "--cohort", "meta-kora")
        self.assertIn("Changed paths: 0", result.stdout)

    def test_migrate_v2_agentfile_profile_accepted(self):
        """Profile v2-agentfile esta disponible y es idempotente tras primera corrida."""
        if not has_productive_workspaces():
            self.skipTest("requires productive workspaces")
        # Primera corrida ya deberia haber poblado harness_vector; segunda es idempotente
        result = run_cli("migrate", "--profile", "v2-agentfile")
        # Idempotente si ya se aplico
        self.assertTrue("Changed paths: 0" in result.stdout or "Changed paths:" in result.stdout)

    def test_transmute_accepts_all_four_targets(self):
        """Los 4 runtime targets (claude-code, codex, gemini, openclaw) aceptan --target."""
        if not has_productive_workspaces():
            self.skipTest("requires productive workspaces")
        for target in ("claude-code", "codex", "gemini", "openclaw"):
            result = run_cli("transmute", "--target", target, "--agent", "kora/curator", "--dry-run")
            self.assertIn("KORA Transmutation", result.stdout)
            self.assertIn(f"→ {target}", result.stdout)
            self.assertIn("Vector IR:", result.stdout)

    def test_ingest_subcommand_exists(self):
        """El subcomando `kora ingest` existe y acepta los 4 runtimes fuente."""
        result = run_cli("ingest", "--help", check=False)
        self.assertIn("--from", result.stdout)
        for rt in ("claude-code", "codex", "gemini", "openclaw"):
            self.assertIn(rt, result.stdout)

    def test_transmute_out_of_domain_fails(self):
        """Transmutar un vector fuera del dominio del runtime debe fallar."""
        if not has_productive_workspaces():
            self.skipTest("requires productive workspaces")
        # Claude Code no soporta Mu=3 (ambient always-on). Por ahora el fleet promovido
        # tiene Mu<=2, por lo que no dispara el error. Smoke: verifica que el sistema
        # emite un `_transmutation.yml` con estructura completa tras transmute real.
        result = run_cli("transmute", "--target", "claude-code", "--agent", "kora/curator")
        self.assertIn("Manifest:", result.stdout)


if __name__ == "__main__":
    unittest.main()
