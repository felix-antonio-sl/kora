import tempfile
import unittest
from pathlib import Path

import common  # noqa: F401 - adds toolchain/ to sys.path for kora_lib imports
from kora_lib.recovery import collect_recovery_inventory


def write_md(path, frontmatter, body="# Titulo\n"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{frontmatter}---\n\n{body}", encoding="utf-8")


class RecoveryInventoryTests(unittest.TestCase):
    def test_collects_canonical_external_mapping_and_source_gaps(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            agents = root / "kora" / "artifacts" / "agents"
            skills = root / "kora" / "artifacts" / "skills"
            knowledge = root / "kora" / "artifacts" / "knowledge"
            home = root / "home"
            openclaw = root / "openclaw-fleet" / "workspaces"

            write_md(
                agents / "dev" / "bar" / "AGENT.md",
                '_manifest:\n  urn: "urn:dev:artefacto:bar"\nversion: "1.0.0"\nstatus: activo\n',
            )
            skill_text = '_manifest:\n  urn: "urn:dev:artefacto:foo"\nversion: "1.0.0"\nstatus: activo\n'
            write_md(skills / "dev" / "foo" / "SKILL.md", skill_text)
            write_md(
                knowledge / "dev" / "with-source.md",
                '_manifest:\n  urn: "urn:dev:kb:with-source"\n  provenance:\n    source: "source.pdf"\nversion: "1.0.0"\nstatus: publicado\nextensions:\n  kora:\n    family: note\n',
            )
            write_md(
                knowledge / "dev" / "without-source.md",
                '_manifest:\n  urn: "urn:dev:kb:without-source"\nversion: "1.0.0"\nstatus: publicado\nextensions:\n  kora:\n    family: note\n',
            )
            write_md(
                knowledge / "_SCRIPTORIUM" / "INBOX" / "draft.md",
                '_manifest:\n  urn: "urn:dev:kb:draft"\nversion: "0.1.0"\nstatus: borrador\n',
            )
            write_md(
                skills / "_TALLER" / "INBOX" / "baz" / "SKILL.md",
                '_manifest:\n  urn: "urn:dev:artefacto:baz"\nversion: "0.1.0"\nstatus: borrador\n',
            )

            write_md(home / ".codex" / "skills" / "foo" / "SKILL.md", skill_text)
            write_md(home / ".claude" / "skills" / "baz" / "SKILL.md", skill_text.replace("foo", "baz"))
            write_md(home / ".claude" / "agents" / "bar.md", "name: bar\n")
            write_md(openclaw / "bar" / "SOUL.md", "name: bar\n")
            (openclaw / "bar" / "config.json").write_text('{"ok": true}\n', encoding="utf-8")

            payload = collect_recovery_inventory(
                agents_root=agents,
                skills_root=skills,
                knowledge_root=knowledge,
                home=home,
                openclaw_workspaces=openclaw,
            )

        self.assertEqual(payload["canonical"]["counts"]["agents"], 1)
        self.assertEqual(payload["canonical"]["counts"]["skills"], 1)
        self.assertEqual(payload["canonical"]["counts"]["knowledge"], 2)
        self.assertEqual(payload["canonical"]["knowledge"]["source_gaps"], 1)
        self.assertEqual(payload["canonical"]["staging"]["knowledge_inbox"], 1)

        codex_item = payload["external"]["codex_skills"]["items"][0]
        self.assertEqual(codex_item["name"], "foo")
        self.assertEqual(codex_item["mapping"]["status"], "mapped_skill")
        self.assertTrue(codex_item["same_hash_as_canonical"])

        claude_skill = payload["external"]["claude_skills"]["items"][0]
        self.assertEqual(claude_skill["name"], "baz")
        self.assertEqual(claude_skill["mapping"]["status"], "staged_skill")

        claude_agent = payload["external"]["claude_agents"]["items"][0]
        self.assertEqual(claude_agent["mapping"]["status"], "mapped_agent")

        openclaw_workspace = payload["external"]["openclaw_workspaces"]["items"][0]
        self.assertEqual(openclaw_workspace["name"], "bar")
        self.assertEqual(openclaw_workspace["mapping"]["status"], "mapped_agent")
        self.assertEqual(openclaw_workspace["runtime_files"], ["SOUL.md", "config.json"])


if __name__ == "__main__":
    unittest.main()
