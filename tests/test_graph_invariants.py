import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from common import AGENTS_ROOT, ROOT, has_productive_workspaces, run_cli
from kora_lib.catalog import build_catalog_lookup, load_catalog
from kora_lib.config import OPERATING_CORE_COHORTS
from kora_lib.graph import build_reference_graph
from kora_lib.workspaces import (
    fragment_exists,
    iter_agent_workspaces,
    workspace_exists_from_urn,
)


_SKIP_IF_NO_WORKSPACES = unittest.skipUnless(
    has_productive_workspaces(),
    "Workspaces productivos en staging; grafo no representa fleet activo.",
)


class GraphInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run_cli("index")
        cls.catalog = load_catalog()
        cls.known_urns, cls.urn_to_entry = build_catalog_lookup(cls.catalog)
        cls.scanned_files, cls.edges = build_reference_graph()

    @_SKIP_IF_NO_WORKSPACES
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
                str(target_path.relative_to(ROOT)).startswith("KNOWLEDGE/kora/categorical-foundations/"),
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
                target_path = AGENTS_ROOT / parts[1] / parts[3] / "AGENTS.md"
                self.assertTrue(
                    fragment_exists(target_path, edge.fragment),
                    msg=f"Broken workspace fragment {edge.target}#{edge.fragment}",
                )
            else:
                continue

    def test_every_route_targets_existing_workspace(self):
        for edge in self.edges:
            if edge.kind != "RoutesToAgent":
                continue
            namespace, name = edge.target.split("/", 1)
            target_dir = AGENTS_ROOT / namespace / name
            self.assertTrue(target_dir.is_dir(), msg=f"Broken route {edge.target}")

    def test_every_invoked_skill_exists_in_workspace(self):
        for edge in self.edges:
            if edge.kind != "InvokesSkill":
                continue
            skill_paths = (
                edge.source.parent / "skills" / f"{edge.target}.md",
                edge.source.parent / "skills" / edge.target / "SKILL.md",
            )
            self.assertTrue(any(path.exists() for path in skill_paths), msg=f"Missing skill {edge.target} for {edge.source}")

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

        for workspace_dir in iter_agent_workspaces():
            workspace = workspace_dir
            tool_names = declared.get(workspace, set())
            self.assertEqual(
                tool_names,
                allowed.get(workspace, set()),
                msg=f"Tool mismatch in {workspace}",
            )

    def test_operating_core_allowed_kb_urns_resolve(self):
        enforced_workspaces = set()
        for cohort_workspaces in OPERATING_CORE_COHORTS.values():
            enforced_workspaces.update(cohort_workspaces)
        for edge in self.edges:
            if edge.kind != "AllowsKB":
                continue
            try:
                rel = edge.source.relative_to(AGENTS_ROOT)
            except ValueError:
                continue
            workspace = f"{rel.parts[0]}/{rel.parts[1]}"
            if workspace not in enforced_workspaces:
                continue
            self.assertIn(edge.target, self.known_urns, msg=f"Unknown allowed_kb URN: {edge.target}")

    def test_build_reference_graph_raises_on_invalid_workspace_config(self):
        with TemporaryDirectory(dir=ROOT) as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text("{\n", encoding="utf-8")
            with patch("kora_lib.graph.iter_repository_files", return_value=[config_path]):
                with self.assertRaises(RuntimeError):
                    build_reference_graph()


if __name__ == "__main__":
    unittest.main()
