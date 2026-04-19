import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from common import AGENTS_ROOT, ROOT, has_productive_workspaces, run_cli
from kora_lib.catalog import build_catalog_lookup, load_catalog, urn_is_known
from kora_lib.config import DEPRECATED_URN_ALIASES, OPERATING_CORE_COHORTS
from kora_lib.graph import build_reference_graph
from kora_lib.kb_graph import build_graph
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
        # Threshold escalado al fleet actual; ajustar al alza al promover
        # mas workspaces desde _FRAGUA/INBOX/.
        self.assertGreater(self.scanned_files, 500)
        self.assertTrue(any(edge.kind == "XRef" for edge in self.edges))
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
                target_file = "AGENT.md" if len(parts) > 2 and parts[2] == "artefacto" else "AGENTS.md"
                target_path = AGENTS_ROOT / parts[1] / parts[3] / target_file
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
            self.assertTrue(
                edge.target in self.known_urns or edge.target in DEPRECATED_URN_ALIASES,
                msg=f"Unknown allowed_kb URN: {edge.target}",
            )

    def test_build_reference_graph_raises_on_invalid_workspace_config(self):
        with TemporaryDirectory(dir=ROOT) as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text("{\n", encoding="utf-8")
            with patch("kora_lib.graph.iter_repository_files", return_value=[config_path]):
                with self.assertRaises(RuntimeError):
                    build_reference_graph()

    def test_urn_resolution_accepts_historical_aliases_and_bootstrap_urns(self):
        known_urns = {
            "urn:kora:kb:autoria-spec",
            "urn:kora:kb:cat-governance-lattice",
        }
        self.assertTrue(urn_is_known("urn:kora:kb:agent-spec-md", known_urns))
        self.assertTrue(urn_is_known("urn:kora:kb:agentfile-spec", known_urns))
        self.assertTrue(urn_is_known("urn:kora:kb:05-governance-lattice", known_urns))
        self.assertTrue(urn_is_known("urn:kora:agent-bootstrap:guardian-user:1.0.0", known_urns))
        self.assertFalse(urn_is_known("urn:kora:kb:definitely-missing", known_urns))

    def test_kb_graph_ignores_retired_relations_and_canonicalizes_renames(self):
        nodes = [
            {
                "urn": "urn:kora:kb:autoria-spec",
                "namespace": "kora",
                "status": "published",
                "version": "1.0.0",
                "tags": [],
                "file": "specs/autoria-spec.md",
                "relations": {"supersedes": ["urn:kora:kb:agentfile-spec", "urn:kora:kb:skill-overlay-spec"]},
            },
            {
                "urn": "urn:kora:kb:md-spec",
                "namespace": "kora",
                "status": "published",
                "version": "8.0.0",
                "tags": [],
                "file": "specs/md-spec.md",
                "relations": {"cites": ["urn:kora:kb:05-governance-lattice"]},
            },
            {
                "urn": "urn:kora:kb:cat-governance-lattice",
                "namespace": "kora",
                "status": "published",
                "version": "1.0.0",
                "tags": [],
                "file": "KNOWLEDGE/kora/categorical-foundations/05-governance-lattice.md",
                "relations": {},
            },
        ]

        graph = build_graph(nodes)
        self.assertEqual(graph["broken_edges"], [])

    def test_kb_graph_emits_traces_requirement_edges(self):
        nodes = [
            {
                "urn": "urn:kora:kb:requirement-traceability-model",
                "namespace": "kora",
                "status": "published",
                "version": "1.0.0",
                "tags": ["note"],
                "file": "artifacts/knowledge/kora/sys/requirement-traceability-model.md",
                "relations": {"traces_requirements": ["urn:kora:kb:req-demo"]},
            },
            {
                "urn": "urn:kora:kb:req-demo",
                "namespace": "kora",
                "status": "published",
                "version": "1.0.0",
                "tags": ["requirement"],
                "file": "artifacts/knowledge/kora/sys/req-demo.md",
                "relations": {},
            },
        ]

        graph = build_graph(nodes)
        self.assertIn(
            {
                "from": "urn:kora:kb:requirement-traceability-model",
                "to": "urn:kora:kb:req-demo",
                "type": "traces_requirements",
            },
            graph["edges"],
        )


if __name__ == "__main__":
    unittest.main()
