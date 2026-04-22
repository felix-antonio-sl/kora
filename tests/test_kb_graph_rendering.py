import sys
import unittest

from common import ROOT

if str(ROOT / "toolchain") not in sys.path:
    sys.path.insert(0, str(ROOT / "toolchain"))

from kora_lib.kb_graph import render_kb_graph_markdown, render_orphans_markdown


GRAPH_FIXTURE = {
    "edges": [
        {"from": "urn:kora:kb:a", "to": "urn:kora:kb:b", "type": "depends"},
    ],
    "broken_edges": [],
    "orphans_root": ["urn:kora:kb:root"],
    "orphans_intencional": ["urn:kora:kb:intencional"],
    "orphans_real": [
        {
            "urn": "urn:kora:kb:real",
            "namespace": "kora",
            "file": "specs/example.md",
        }
    ],
    "stats": {
        "total_nodes": 3,
        "total_edges": 1,
        "orphan_nodes": 3,
        "orphans_root": 1,
        "orphans_intencional": 1,
        "orphans_real": 1,
        "broken_edges": 0,
        "cycles_in_depends": 0,
        "by_namespace": {"kora": 3},
        "by_relation_type": {"depends": 1},
    },
}


class KbGraphRenderingTests(unittest.TestCase):
    def test_render_kb_graph_markdown_is_stable(self):
        first = render_kb_graph_markdown(GRAPH_FIXTURE)
        second = render_kb_graph_markdown(GRAPH_FIXTURE)
        self.assertEqual(first, second)
        self.assertNotIn("Generated:", first)
        self.assertNotIn("datetime", first)

    def test_render_orphans_markdown_is_stable(self):
        first = render_orphans_markdown(GRAPH_FIXTURE)
        second = render_orphans_markdown(GRAPH_FIXTURE)
        self.assertEqual(first, second)
        self.assertNotIn("Generated:", first)
        self.assertNotIn("datetime", first)


if __name__ == "__main__":
    unittest.main()
