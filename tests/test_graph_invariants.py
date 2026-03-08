import unittest

from common import ROOT, run_cli
from kora_lib.catalog import build_catalog_lookup, load_catalog
from kora_lib.graph import build_reference_graph
from kora_lib.workspaces import fragment_exists, workspace_exists_from_urn


class GraphInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run_cli("index")
        cls.catalog = load_catalog()
        cls.known_urns, cls.urn_to_entry = build_catalog_lookup(cls.catalog)
        cls.scanned_files, cls.edges = build_reference_graph()

    def test_repository_graph_is_nontrivial(self):
        self.assertGreater(self.scanned_files, 700)
        self.assertTrue(any(edge.kind == "TracesTo" for edge in self.edges))
        self.assertTrue(any(edge.kind == "RoutesToAgent" for edge in self.edges))
        self.assertTrue(any(edge.kind == "InvokesSkill" for edge in self.edges))

    def test_every_traces_to_targets_official_formal_layer(self):
        for edge in self.edges:
            if edge.kind != "TracesTo":
                continue
            self.assertIn(edge.target, self.known_urns, msg=f"Unresolved trace target: {edge.target}")
            target_path = self.urn_to_entry[edge.target]["file"]
            self.assertTrue(
                str(target_path.relative_to(ROOT)).startswith("knowledge/kora/categorical-foundations/"),
                msg=f"Trace leaves official formal layer: {edge.target} -> {target_path}",
            )

    def test_every_fragment_reference_resolves(self):
        for edge in self.edges:
            if not edge.fragment:
                continue
            if edge.target in self.known_urns:
                target_path = self.urn_to_entry[edge.target]["file"]
                self.assertTrue(
                    fragment_exists(target_path, edge.fragment),
                    msg=f"Broken fragment {edge.target}#{edge.fragment}",
                )
            elif workspace_exists_from_urn(edge.target):
                parts = edge.target.split(":")
                target_path = ROOT / "agents" / parts[1] / parts[3] / "AGENTS.md"
                self.assertTrue(
                    fragment_exists(target_path, edge.fragment),
                    msg=f"Broken workspace fragment {edge.target}#{edge.fragment}",
                )
            else:
                self.fail(f"Fragment target does not resolve: {edge.target}#{edge.fragment}")

    def test_every_route_targets_existing_workspace(self):
        for edge in self.edges:
            if edge.kind != "RoutesToAgent":
                continue
            namespace, name = edge.target.split("/", 1)
            target_dir = ROOT / "agents" / namespace / name
            self.assertTrue(target_dir.is_dir(), msg=f"Broken route {edge.target}")

    def test_every_invoked_skill_exists_in_workspace(self):
        for edge in self.edges:
            if edge.kind != "InvokesSkill":
                continue
            skill_path = edge.source.parent / "skills" / f"{edge.target}.md"
            self.assertTrue(skill_path.exists(), msg=f"Missing skill {edge.target} for {edge.source}")

    def test_every_declared_tool_matches_config_allowlist(self):
        declared = {}
        allowed = {}
        for edge in self.edges:
            if edge.kind == "DeclaresTool":
                workspace = edge.source.parent
                declared.setdefault(workspace, set()).add(edge.target)
            elif edge.kind == "AllowsTool":
                workspace = edge.source.parent
                allowed.setdefault(workspace, set()).add(edge.target)

        for workspace, tool_names in declared.items():
            self.assertEqual(
                tool_names,
                allowed.get(workspace, set()),
                msg=f"Tool mismatch in {workspace}",
            )

    def test_all_allowed_kb_urns_resolve(self):
        for edge in self.edges:
            if edge.kind != "AllowsKB":
                continue
            self.assertIn(edge.target, self.known_urns, msg=f"Unknown allowed_kb URN: {edge.target}")


if __name__ == "__main__":
    unittest.main()
