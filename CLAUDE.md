# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

KORA is a formally-specified monorepo for building and governing AI agents using categorical theory foundations. It contains agent definitions (YAML monoliths being migrated to workspace directories), knowledge bases (YAML being migrated to Markdown), and four foundational specifications that govern the entire ecosystem. Primary language is **Spanish (es-CL)**.

## Commands

```bash
# Rebuild catalog from all artifacts (scans YAML files for _manifest.urn)
scripts/kora index

# Resolve a URN to its physical file path
scripts/kora resolve "urn:kora:agent:guardian:1.0.0"

# Check for broken URN references across all files
scripts/kora health

# Validate agent YAMLs against JSON schema (requires: pip install jsonschema)
scripts/kora validate
```

No build system — this is a documentation/specification monorepo. Python3 + PyYAML required for CLI.

## Architecture

### Governance Hierarchy (precedence, highest to lowest)

1. **gobernanza.md** — Meta-rules governing the ecosystem
2. **md-spec.md** (descriptive) / **spec-md.md** (prescriptive) — Format specifications
3. **agent-spec-md.md** — Agent architecture specification
4. Namespace extensions

### The Four Foundational Specs (`knowledge/foundations/core/kora/`)

| File | Version | Governs |
|------|---------|---------|
| `gobernanza.md` | v1.2.0 | Precedence, LLM injection patterns, namespace extensions |
| `md-spec.md` | v2.0.0 | Knowledge artifacts (KORA/MD) — RAG-optimized, telegraphic Markdown |
| `spec-md.md` | v2.1.0 | Prescriptive documents — RFC 2119 keywords, normative structure |
| `agent-spec-md.md` | v5.0.0 | Agent architecture — F-coalgebra model, 12 sections |

### Agent Model (agent-spec-md.md v5.0.0)

An agent is an F-coalgebra `c: U → F(U)` with 5 essential components:

| # | Component | Symbol | Materializes as |
|---|-----------|--------|----------------|
| 1 | Transition morphism | c | AGENTS.md (FSM) |
| 2 | Interface functor | F | TOOLS.md |
| 3 | State space (fibres) | U | SOUL.md (phenomenology) + USER.md (operator context) |
| 4 | Effect monad | M | config.json (immutable from LLM) |
| 5 | Wiring diagram | W | Declared in AGENTS.md adjunctions |

IDENTITY.md is **optional**. Endofunctors (cognitive models) live in `skills/CM-*.md` with lazy evaluation.

### URN System

Format: `urn:{namespace}:{type}:{id}:{version}` — e.g., `urn:kora:kb:gobernanza:1.2.0`

- Catalog (`catalog/catalog_master_kora.yml`) is the source of truth for URN resolution
- Run `scripts/kora index` after adding/removing artifacts to rebuild the catalog
- Legacy URNs `urn:knowledge:koda:*` are being migrated to `urn:{namespace}:kb:*`

### Active Migration (KODA → KORA)

The repo is mid-migration from KODA (June 2025) to KORA (Feb 2026):

- **Agents**: 40 YAML monoliths in `agents/` → workspace directories (Phase 4, pending)
- **Knowledge**: 139 YAML KBs in `knowledge/applied/` → KORA/MD Markdown (Phase 3, pending)
- **Specs**: Phases 0-2 complete (tools/ cleaned, agent-spec-md.md v5.0.0 with funtor G)
- Plan: `docs/plans/2026-02-23-koda-kora-remediation-plan.md`

## Key Conventions

- **RFC 2119 keywords** (DEBE, NO DEBE, DEBERÍA, PUEDE) are normative in prescriptive documents
- **Frontmatter**: All KORA artifacts use `_manifest.urn` in YAML frontmatter; Markdown specs use `version`, `status`, `tags`, `lang`
- **Segregation principle**: FSM logic (c) must never mix with personality (SOUL.md), operator context (USER.md), or security policies (config.json)
- **Token Economy**: Minimize context window consumption via topological segregation and lazy evaluation of cognitive models
- **Koraficación** (md-spec §6): The process of transforming human documents into KORA/MD format — telegraphic, RAG-optimized, fidelity-preserving
- **Agentificación** (agent-spec §12): Functor G that transforms KODA YAML monoliths into KORA workspace directories
