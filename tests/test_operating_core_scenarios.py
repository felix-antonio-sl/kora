import unittest

from common import FIXTURES, GENERATED_DOCS, ROOT, load_json, run_cli
from kora_lib.catalog import build_catalog_lookup, load_catalog
from kora_lib.contracts import build_operating_core_payload, load_workspace_contract


SCENARIOS = load_json(FIXTURES / "operating-core-scenarios.json")


def load_contract_text(contract):
    parts = []
    for path in contract.sources.values():
        abs_path = FIXTURES.parents[1] / path
        if abs_path.exists():
            parts.append(abs_path.read_text(encoding="utf-8"))
    return "\n".join(parts)


def assert_terms_present(test_case, haystack, terms, label):
    lower_haystack = haystack.lower()
    for term in terms:
        test_case.assertIn(term.lower(), lower_haystack, msg=f"missing {label}: {term}")


def assert_workspace_refs_resolve(test_case, refs, label):
    for ref in refs:
        namespace, name = ref.split("/", 1)
        test_case.assertTrue(
            (ROOT / "agents" / namespace / name).is_dir(),
            msg=f"invalid {label}: {ref}",
        )


def assert_contract_supports_scenario(test_case, contract, scenario):
    full_text = load_contract_text(contract)

    for state_name in scenario.get("requires_states", []):
        test_case.assertIn(state_name, contract.states, msg=f"{contract.workspace} missing state {state_name}")

    for skill_name in scenario.get("requires_skills", []):
        test_case.assertIn(skill_name, contract.skill_refs, msg=f"{contract.workspace} missing skill ref {skill_name}")

    for tool_name in scenario.get("requires_tools", []):
        test_case.assertIn(tool_name, contract.tools, msg=f"{contract.workspace} missing tool {tool_name}")
        test_case.assertIn(tool_name, contract.tools_allow, msg=f"{contract.workspace} missing tools.allow {tool_name}")

    for route in scenario.get("requires_routes", []):
        test_case.assertIn(route, contract.handoff_targets, msg=f"{contract.workspace} missing handoff {route}")

    if "requires_allowed_terms" in scenario:
        assert_terms_present(test_case, contract.allowed_line, scenario["requires_allowed_terms"], "allowed term")

    if "requires_evidence_terms" in scenario:
        assert_terms_present(test_case, full_text, scenario["requires_evidence_terms"], "scenario term")

    if "requires_tool_output_terms" in scenario:
        outputs = "\n".join(tool.output_signature for tool in contract.tools.values())
        assert_terms_present(test_case, outputs, scenario["requires_tool_output_terms"], "tool output term")

    if "requires_allowed_kb_min" in scenario:
        test_case.assertGreaterEqual(
            len(contract.allowed_kb),
            scenario["requires_allowed_kb_min"],
            msg=f"{contract.workspace} missing allowed_kb depth",
        )

    if scenario.get("requires_no_skills"):
        test_case.assertEqual(contract.skill_refs, [], msg=f"{contract.workspace} unexpectedly declares skills")

    if scenario.get("requires_no_handoffs"):
        test_case.assertEqual(contract.handoff_targets, [], msg=f"{contract.workspace} unexpectedly declares handoffs")


class OperatingCoreScenarioTests(unittest.TestCase):
    def test_operating_core_payload_is_materialized_by_sync_docs(self):
        run_cli("sync-docs")
        payload = load_json(GENERATED_DOCS / "operating-core-contracts.json")
        self.assertIn("cohorts", payload)
        self.assertIn("kora", payload["cohorts"])
        self.assertIn("gn/goreologo", {item["workspace"] for item in payload["cohorts"]["domain_canary"]})
        self.assertIn("gn/digitrans", {item["workspace"] for item in payload["cohorts"]["domain_canary"]})

    def test_operating_core_payload_matches_declared_core(self):
        payload = build_operating_core_payload()
        self.assertEqual(payload["totals"]["workspaces"], 13)
        self.assertEqual(set(payload["cohorts"].keys()), {"kora", "dev", "ops", "domain_canary"})

    def test_meta_kora_audit_is_materialized_with_explicit_status(self):
        payload = build_operating_core_payload()
        self.assertIn("meta_kora", payload)
        self.assertEqual(payload["meta_kora"]["summary"], SCENARIOS["meta_kora"]["summary"])

        statuses = {item["workspace"]: item["status"] for item in payload["meta_kora"]["workspaces"]}
        self.assertEqual(statuses, SCENARIOS["meta_kora"]["statuses"])

    def test_meta_kora_operating_core_and_auxiliary_boundary_is_explicit(self):
        payload = build_operating_core_payload()
        core_workspaces = set()
        for cohort_items in payload["cohorts"].values():
            core_workspaces.update(item["workspace"] for item in cohort_items)

        for item in payload["meta_kora"]["workspaces"]:
            if item["status"] == "operating_core":
                self.assertTrue(item["in_operating_core"], msg=f"{item['workspace']} should be in operating core")
                self.assertIn(item["workspace"], core_workspaces)
            else:
                self.assertFalse(item["in_operating_core"], msg=f"{item['workspace']} should stay auxiliary")
                self.assertNotIn(item["workspace"], core_workspaces)

    def test_operating_core_routes_and_handoffs_are_real_workspaces(self):
        payload = build_operating_core_payload()
        for cohort_items in payload["cohorts"].values():
            for item in cohort_items:
                assert_workspace_refs_resolve(self, item["route_targets"], "route")
                assert_workspace_refs_resolve(self, item["handoff_targets"], "handoff")
                assert_workspace_refs_resolve(self, item["sub_agents"], "sub-agent")

        for item in payload["meta_kora"]["workspaces"]:
            assert_workspace_refs_resolve(self, item["route_targets"], "meta route")
            assert_workspace_refs_resolve(self, item["handoff_targets"], "meta handoff")
            assert_workspace_refs_resolve(self, item["sub_agents"], "meta sub-agent")

    def test_operating_core_contracts_do_not_include_noise_tokens_as_handoffs(self):
        noise_tokens = {"agentes/LLM", "modelo/provider", "formal/01", "formal/02", "pass/fail", "meat/fat"}
        for workspace in ("kora/forgemaster", "kora/curator", "dev/reviewer", "ops/verificador", "ops/security"):
            contract = load_workspace_contract(workspace)
            self.assertTrue(noise_tokens.isdisjoint(contract.handoff_targets), msg=f"noise leaked into {workspace}")

    def test_domain_canary_sample_kb_urns_resolve(self):
        catalog = load_catalog()
        self.assertIsNotNone(catalog)
        _known, lookup = build_catalog_lookup(catalog)
        for urn in SCENARIOS["domain_canary"]["sample_allowed_kb"]:
            self.assertIn(urn, lookup, msg=f"missing canary KB URN {urn}")
        for urn in SCENARIOS["secondary_domain_canary"]["sample_allowed_kb"]:
            self.assertIn(urn, lookup, msg=f"missing secondary canary KB URN {urn}")

    def test_domain_canary_all_allowed_kb_urns_resolve(self):
        catalog = load_catalog()
        self.assertIsNotNone(catalog)
        _known, lookup = build_catalog_lookup(catalog)
        for workspace in ("gn/goreologo", "gn/digitrans"):
            contract = load_workspace_contract(workspace)
            for urn in contract.allowed_kb:
                self.assertIn(urn, lookup, msg=f"missing canary allowed_kb URN {urn}")

    def test_domain_canary_agent_urns_resolve_via_cli(self):
        expected = {
            "urn:gn:agent-bootstrap:goreologo-agents:2.4.0": "agents/gn/goreologo/AGENTS.md",
            "urn:gn:agent-bootstrap:goreologo-tools:2.4.0": "agents/gn/goreologo/TOOLS.md",
            "urn:gn:agent-bootstrap:goreologo-config:1.0.0": "agents/gn/goreologo/config.json",
            "urn:gn:agent-bootstrap:digitrans-agents:2.0.0": "agents/gn/digitrans/AGENTS.md",
            "urn:gn:agent-bootstrap:digitrans-tools:2.0.0": "agents/gn/digitrans/TOOLS.md",
            "urn:gn:agent-bootstrap:digitrans-config:2.0.0": "agents/gn/digitrans/config.json",
        }
        for urn, rel_path in expected.items():
            result = run_cli("resolve", urn)
            self.assertIn(rel_path, result.stdout)


def make_agent_scenario_test(scenario):
    def test_method(self):
        contract = load_workspace_contract(scenario["workspace"])
        assert_contract_supports_scenario(self, contract, scenario)

    return test_method


def make_handoff_test(scenario):
    def test_method(self):
        source_contract = load_workspace_contract(scenario["from"])
        target_contract = load_workspace_contract(scenario["to"])
        assert_workspace_refs_resolve(self, source_contract.route_targets, "source route")
        assert_workspace_refs_resolve(self, target_contract.handoff_targets, "target handoff")

        for tool_name in scenario.get("source_requires_tools", []):
            self.assertIn(tool_name, source_contract.tools, msg=f"{scenario['from']} missing source tool {tool_name}")
        for tool_name in scenario.get("target_requires_tools", []):
            self.assertIn(tool_name, target_contract.tools, msg=f"{scenario['to']} missing target tool {tool_name}")

        if scenario.get("requires_explicit_route"):
            self.assertIn(scenario["to"], source_contract.route_targets, msg=f"{scenario['from']} lacks explicit route to {scenario['to']}")

        if "source_requires_evidence_terms" in scenario:
            assert_terms_present(
                self,
                load_contract_text(source_contract),
                scenario["source_requires_evidence_terms"],
                "source handoff term",
            )
        if "target_requires_evidence_terms" in scenario:
            assert_terms_present(
                self,
                load_contract_text(target_contract),
                scenario["target_requires_evidence_terms"],
                "target handoff term",
            )

    return test_method


def make_loop_test(loop):
    def test_method(self):
        for workspace in loop["steps"]:
            contract = load_workspace_contract(workspace)
            for state_name in loop["required_states_by_step"].get(workspace, []):
                self.assertIn(state_name, contract.states, msg=f"{workspace} missing loop state {state_name}")
            for tool_name in loop["required_tools_by_step"].get(workspace, []):
                self.assertIn(tool_name, contract.tools, msg=f"{workspace} missing loop tool {tool_name}")
        for source, target in loop.get("required_routes", []):
            contract = load_workspace_contract(source)
            self.assertIn(target, contract.handoff_targets, msg=f"{source} missing loop handoff {target}")

    return test_method


def make_canary_support_test(step):
    def test_method(self):
        contract = load_workspace_contract(step["workspace"])
        assert_contract_supports_scenario(self, contract, step)

    return test_method


for scenario in SCENARIOS["agent_scenarios"]:
    setattr(
        OperatingCoreScenarioTests,
        f"test_agent_scenario__{scenario['id'].replace('-', '_')}",
        make_agent_scenario_test(scenario),
    )

for scenario in SCENARIOS["handoff_scenarios"]:
    setattr(
        OperatingCoreScenarioTests,
        f"test_handoff__{scenario['id'].replace('-', '_')}",
        make_handoff_test(scenario),
    )

for loop in SCENARIOS["institutional_loops"]:
    setattr(
        OperatingCoreScenarioTests,
        f"test_institutional_loop__{loop['id'].replace('-', '_')}",
        make_loop_test(loop),
    )

setattr(
    OperatingCoreScenarioTests,
    "test_domain_canary__goreologo_contract_support",
    make_canary_support_test(SCENARIOS["domain_canary"]),
)

setattr(
    OperatingCoreScenarioTests,
    "test_domain_canary__digitrans_contract_support",
    make_canary_support_test(SCENARIOS["secondary_domain_canary"]),
)

for index, step in enumerate(SCENARIOS["domain_canary"]["core_support"], start=1):
    setattr(
        OperatingCoreScenarioTests,
        f"test_domain_canary__core_support_{index}_{step['workspace'].replace('/', '_')}",
        make_canary_support_test(step),
    )

for scenario in SCENARIOS["meta_auxiliary_scenarios"]:
    setattr(
        OperatingCoreScenarioTests,
        f"test_meta_auxiliary__{scenario['workspace'].replace('/', '_')}",
        make_canary_support_test(scenario),
    )


if __name__ == "__main__":
    unittest.main()
