# AGENTS.md

This file is the Codex entrypoint for this repository.

For all operational guidance, read and follow `CLAUDE.md` at the repository
root. `CLAUDE.md` is the single operational source for agents working in KORA:
repo purpose, current topology, source-of-truth rules, precedence, host roles,
toolchain commands, validation gates, and workflow.

If this file and `CLAUDE.md` ever differ, `CLAUDE.md` wins.

Recommended session bootstrap:

1. Read `CLAUDE.md`.
2. Read `governance/gobernanza.md` when precedence or policy matters.
3. Read the latest relevant handoff in `docs/handoffs/` when continuity matters.
4. Verify local host role before making repository-level claims:

   ```bash
   python3 toolchain/kora host
   ```

5. Before structural changes, use the standard gate described in `CLAUDE.md`.
