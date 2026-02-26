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
  specs/                        # 7 foundational specs (gobernanza, md-spec, spec-md, agent-spec-md, skill-spec-md, runtime-spec-md, swarm-spec-md)
  knowledge/                    # KBs organized by namespace (gn, fxsl, kora, tde, legal, gov, orko, mgmt)
    kora/categorical-foundations/  # Formal Layer: 6 documents (00-05) with categorical math backing the specs
  agents/                       # Agent workspaces organized by namespace
  catalog/                      # Master URN registry (source of truth)
  skills/                       # Skills federation (shared across agents)
  inbox/ → source/ → drafts/ → knowledge/   # Intake pipeline for new artifacts
  scripts/                      # CLI tools
  docs/                         # Plans and documentation
```

### Governance Hierarchy (precedence, highest to lowest)

1. **gobernanza.md** v2.1.0 — Meta-rules governing the ecosystem
2. **md-spec.md** v3.0.0 (descriptive) / **spec-md.md** v3.0.0 (prescriptive) — Format specifications
3. **agent-spec-md.md** v7.2.0 — Agent architecture specification
   - 3a. **skill-spec-md.md** v2.0.0 — Skill format and lifecycle
   - 3b. **runtime-spec-md.md** v2.0.1 — Cross-platform deployment + Model Routing
   - 3c. **swarm-spec-md.md** v1.1.0 — Multi-agent orchestration (swarms, golden paths, circuit breakers, security inter-agente, sentinel)
4. Namespace extensions

### Two-Layer Knowledge System

**Operational Layer** (specs/): prescriptive rules in natural language + Python pseudocode, consumed by LLMs as system prompts.

**Formal Layer** (knowledge/kora/categorical-foundations/00-05): categorical math backing the operational rules. Descriptive knowledge governed by KORA/MD — justifies but does NOT govern.

Rules are connected via the `Traces to:` convention (defined in spec-md §1.3):
```markdown
Every tool the agent can use MUST be declared in TOOLS.md.
Traces to: formal/01 §7 (Segregation is Necessary theorem)
```
Rules with a trace have formal backing; rules without (token budgets, naming) are pragmatic.

### Two Artifact Formats

| Format | Spec | Purpose |
|--------|------|---------|
| **KORA/MD** | md-spec.md v3.0.0 | Describe knowledge (KBs) — telegraphic, RAG-optimized. Process: Koraficación (§6) |
| **KORA/Spec-MD** | spec-md.md v3.0.0 | Prescribe rules/specs — RFC 2119 keywords (DEBE, NO DEBE, DEBERÍA, PUEDE). Process: Crystallization (§1.2) |

### Agent Model (agent-spec-md.md v7.2.0)

An agent is a reactive state machine with 5 essential components:

| # | Component | Materializes as | Invariant |
|---|-----------|----------------|-----------|
| 1 | Behavior (FSM) | AGENTS.md | Deterministic transitions |
| 2 | Interface | TOOLS.md | Closed algebra (all tools declared) |
| 3 | State | SOUL.md (personality) + USER.md (operator) | Completeness |
| 4 | Security | config.json | Immutable from LLM |
| 5 | Wiring | Declared in AGENTS.md | Compositionality preserved |

Cognitive processes live in `skills/CM-*.md` as lazy-loaded skills — never injected into bootstrap.

```
agents/{namespace}/{name}/
  AGENTS.md        Behavior: FSM states + transitions + co-induction
  SOUL.md          State/Personality: identity, tone, archetype (dissipates in sub-agents)
  USER.md          State/Operator: profile, routines, output preferences (main session only)
  TOOLS.md         Interface: tool signatures, KB routing, usage guidance
  config.json      Security: allowed_kb, sandbox, tools allow/deny, sub_agents, limits (OPTIONAL), model_routing (OPTIONAL, incl. diversity)
  skills/
    CM-*.md        Cognitive skills (lazy-loaded, one per FSM state that needs one)
```

### Segregation Principle

FSM logic (behavior) must **never** mix with personality (SOUL.md), operator context (USER.md), or security policies (config.json). Each component is independently evaluable. Sub-agents inherit behavior + interface but **dissipate** personality + operator context.

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
| **kora** | Framework governance | forgemaster (agent lifecycle), curator (artifact lifecycle), clawmaster (OpenClaw specialist) |
| **fxsl** | Personal/technical | arquitecto-categorico, ontologista-gist, ingeniero-software-composicional |
| **gn** | GORE Ñuble regional gov | goreologo, ingeniero-goreos, erp-gore |
| **korvo** | Personal assistant | korax (PCA v3.0 cognitive exoskeleton) |
| **ops** | DevOps swarm | integrador, verificador, security, orquestador-swarm, deployer, observer |

## Working with Agents

### Creating a new agent

1. Create directory `agents/{namespace}/{name}/` with 5 mandatory files + `skills/`
2. All files need YAML frontmatter with `_manifest.urn` and `_manifest.type`
3. Valid `_manifest.type` values: `bootstrap_agents`, `bootstrap_soul`, `bootstrap_tools`, `bootstrap_user`, `bootstrap_config`, `lazy_load_endofunctor`
4. config.json must have keys: `allowed_kb`, `sandbox`, `tools`, `sub_agents`. Optional: `_manifest`, `limits` (policy_flags, quotas), `model_routing` (tier selection, fallback chains, budget, diversity — see runtime-spec-md §11-13)
5. Run `scripts/kora index` to register in catalog

### Validation checklist (agent-spec-md v7.2.0 conformance)

- **Topology**: all 5 files present + skills/ directory
- **Frontmatter**: valid URNs on all components and skills
- **Segregation**: no cross-component contamination (FSM logic only in AGENTS.md, personality only in SOUL.md, etc.)
- **FSM**: deterministic transitions, all states reachable, co-induction at terminal states
- **CM coverage**: every stateful FSM state has a corresponding CM-*.md skill
- **Interface closed**: every tool used must be declared in TOOLS.md
- **Security immutable**: config.json constraints applied server-side, never by the LLM

### Deprecating an agent

Add `status: deprecated` and `deprecated_by: "urn:..."` to frontmatter of all components.

### Skills (skill-spec-md v2.0.0)

Skills come in two forms:
- **Degenerate** (CM-only): a single `CM-*.md` file with 4 sections (Purpose, I/O, Procedure, Signature Output)
- **Extended** (directory): `{skill-name}/SKILL.md` + optional `scripts/`, `references/`, `assets/`

Wrap converts CM → extended Skill. Extract converts Skill → CM Core. Extract(Wrap(CM)) = CM (backward compatible).

Script Protocol: all executable scripts in Skills must be Python 3 with JSON I/O via stdin/stdout.

## Migration Status

Completed: Phase 0 (Genesis) → Phase 1 (Source Mapping) → Phase 2 (Koraficación) → Phase 4 (Agentificación) → Phase Audit (Coherencia) → Phase I (Ingesta pipeline + Xanpan corpus) → **Phase S (Spec Rewrite v7.0.0)**

Pending: **Phase F** (Governance): KODA formal deprecation, catalog regeneration, source repo archival

## Key Conventions

- **Koraficación** (md-spec §6): Transform human documents into KORA/MD — telegraphic, RAG-optimized
- **Agentificación** (agent-spec §12): Process that transforms monoliths into KORA workspace directories
- **Crystallization** (spec-md §1.2): Transform implicit decisions into explicit KORA/Spec-MD rules
- **Segregation**: the defining architectural constraint — always verify before committing agent changes
- **Lazy evaluation**: skills are loaded on-demand per FSM state, never in bootstrap. Bootstrap files pay per-turn token cost.
- **Traces to**: convention linking operational rules to categorical formal justifications in knowledge/kora/categorical-foundations/
- **Terminological equivalence** (agent-spec §15): v6.0.0 categorical terms (F-coalgebra, morphism, functor, monad, etc.) map to v7.0.0 operational terms (Agent, behavior, interface, security, etc.)
