# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

KORA is a formally-specified monorepo for building and governing AI agents using categorical theory foundations. It fuses 6 repos (koda, fxsl, gorenuble, tde, orko, korvo) into a single namespace-organized structure. Primary language is **Spanish (es-CL)**.

## Commands

```bash
scripts/kora index      # Rebuild catalog from all artifacts (run after any structural change)
scripts/kora resolve "urn:kora:kb:agent-spec-md"  # Resolve URN to file path
scripts/kora health     # Check for broken URN references
scripts/kora validate   # Validate agent workspaces (requires: pip install jsonschema)
scripts/kora stats      # Show monorepo statistics
scripts/kora intake     # Show intake pipeline status (inbox → source → drafts → knowledge)
```

No build system — this is a documentation/specification monorepo. Python3 + PyYAML required for CLI.

## Architecture

### Directory Structure

```
kora/
  specs/                        # 4 foundational specs (gobernanza, md-spec, spec-md, agent-spec-md)
  knowledge/                    # KBs organized by namespace (gn, fxsl, kora, tde, legal, gov, orko, mgmt)
  agents/                       # Agent workspaces organized by namespace
  catalog/                      # Master URN registry (source of truth)
  skills/                       # Skills federation
  inbox/ → source/ → drafts/ → knowledge/   # Intake pipeline for new artifacts
  scripts/                      # CLI tools
  docs/                         # Plans and documentation
```

### Governance Hierarchy (precedence, highest to lowest)

1. **gobernanza.md** — Meta-rules governing the ecosystem
2. **md-spec.md** (descriptive) / **spec-md.md** (prescriptive) — Format specifications
3. **agent-spec-md.md** — Agent architecture specification
4. Namespace extensions

### Two Artifact Formats

| Format | Spec | Purpose | Functor |
|--------|------|---------|---------|
| **KORA/MD** | md-spec.md v2.0.0 | Describe knowledge (KBs) — telegraphic, RAG-optimized | F: DocHumano → KORA/MD (§6) |
| **KORA/Spec-MD** | spec-md.md v2.1.0 | Prescribe rules/specs — RFC 2119 keywords (DEBE, NO DEBE, DEBERÍA, PUEDE) | G: Decisions → KORA/Spec-MD (§1.2) |

### Agent Model (agent-spec-md.md v5.0.0)

An agent is an F-coalgebra `c: U → F(U)` with 5 essential components:

| # | Component | Symbol | Materializes as |
|---|-----------|--------|----------------|
| 1 | Transition morphism | c | AGENTS.md (FSM) |
| 2 | Interface functor | F | TOOLS.md |
| 3 | State space (fibres) | U | SOUL.md + USER.md |
| 4 | Effect monad | M | config.json |
| 5 | Wiring diagram | W | AGENTS.md adjunctions |

Cognitive processes live in `skills/CM-*.md` as lazy-loaded endofunctors — never injected into bootstrap.

```
agents/{namespace}/{name}/
  AGENTS.md        c: FSM states + transitions + invariants + co-induction
  SOUL.md          U: identity, paradigm, tone, behavioral contract
  USER.md          U: operator profile, routines, output preferences
  TOOLS.md         F: tool signatures, KB routing map, usage guidance
  config.json      M: allowed_kb, sandbox, tools allow/deny, sub_agents
  skills/
    CM-*.md        Lazy-loaded endofunctors (one per FSM state that needs one)
```

### Segregation Principle

FSM logic (c) must **never** mix with personality (SOUL.md), operator context (USER.md), or security policies (config.json). Each component is independently evaluable.

### URN System

Format: `urn:{namespace}:{type}:{id}` — e.g., `urn:kora:kb:agent-spec-md`

- Agent components: `urn:{ns}:agent-bootstrap:{name}-{component}:{version}`
- Skills: `urn:{ns}:skill:{name}-{skill-name}:{version}`
- Knowledge: `urn:{ns}:kb:{id}`

Active namespaces: **kora**, **fxsl**, **gn**, **tde**, **orko**, **korvo**, **gov**, **legal**, **mgmt**, **ops**

Catalog (`catalog/catalog_master_kora.yml`) is the source of truth. Run `scripts/kora index` after changes.

### Key Namespace Agents

| Namespace | Domain | Notable agents |
|-----------|--------|----------------|
| **kora** | Framework governance | guardian, forgemaster (agent lifecycle), curator (artifact lifecycle), clawmaster (OpenClaw specialist) |
| **fxsl** | Personal/technical | arquitecto-categorico, ontologista-gist, ingeniero-software-composicional |
| **gn** | GORE Ñuble regional gov | goreologo, ingeniero-goreos, erp-gore |
| **korvo** | Personal assistant | korax (PCA v3.0 cognitive exoskeleton) |

## Working with Agents

### Creating a new agent

1. Create directory `agents/{namespace}/{name}/` with 5 mandatory files + `skills/`
2. All files need YAML frontmatter with `_manifest.urn` and `_manifest.type`
3. config.json must have keys: `allowed_kb`, `sandbox`, `tools`, `sub_agents`
4. Run `scripts/kora index` to register in catalog

### Validation checklist (agent-spec-md conformance)

- **Topology**: all 5 files present + skills/ directory
- **Frontmatter**: valid URNs on all components and skills
- **Segregation**: no cross-component contamination (FSM logic only in AGENTS.md, personality only in SOUL.md, etc.)
- **FSM**: deterministic transitions, all states reachable, hub state present
- **CM coverage**: every stateful FSM state has a corresponding CM-*.md skill
- **Co-induction**: pre-output checklist or invariants for verification

### Deprecating an agent

Add `status: deprecated` and `deprecated_by: "urn:..."` to frontmatter of all components.

## Migration Status

Completed: Phase 0 (Genesis) → Phase 1 (Source Mapping) → Phase 2 (Koraficación) → Phase 4 (Agentificación) → Phase Audit (Coherencia) → Phase I (Ingesta pipeline + Xanpan corpus)

Pending: **Phase F** (Governance): KODA formal deprecation, catalog regeneration, source repo archival

## Key Conventions

- **Koraficación** (md-spec §6): Transform human documents into KORA/MD — telegraphic, RAG-optimized
- **Agentificación** (agent-spec §12): Functor G transforms monoliths into KORA workspace directories
- **Segregation**: the defining architectural constraint — always verify before committing agent changes
- **Lazy evaluation**: skills are loaded on-demand per FSM state, never in bootstrap. Bootstrap files pay per-turn token cost.
