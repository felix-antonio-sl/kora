# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

KORA is a formally-specified monorepo for building and governing AI agents using categorical theory foundations. It fuses 6 repos (koda, fxsl, gorenuble, tde, orko, korvo) into a single namespace-organized structure. Primary language is **Spanish (es-CL)**.

## Commands

```bash
# Rebuild catalog from all artifacts
scripts/kora index

# Resolve a URN to its physical file path
scripts/kora resolve "urn:kora:kb:agent-spec-md"

# Check for broken URN references
scripts/kora health

# Validate agent workspaces (requires: pip install jsonschema)
scripts/kora validate

# Show monorepo statistics (artifact counts, namespace breakdown)
scripts/kora stats
```

No build system — this is a documentation/specification monorepo. Python3 + PyYAML required for CLI.

## Architecture

### Directory Structure

```
kora/
  specs/                        # 4 foundational specs
    gobernanza.md               #   ecosystem meta-rules (v1.2.0)
    md-spec.md                  #   KORA/MD knowledge format (v2.0.0)
    spec-md.md                  #   KORA/Spec-MD prescriptive format (v2.1.0)
    agent-spec-md.md            #   agent architecture spec (v5.0.0)

  knowledge/                    # KBs organized by namespace
    gn/                         #   gobernanza regional (77 files)
      bpmn/ gestion/ gobernanza/ guias/ manuales/ normativa/ ris/
    fxsl/                       #   cat, gist, mbt (30 files)
      cat/ gist/ mbt/
    kora/                       #   manual-openclaw, sys (30 files)
      manual-openclaw/ sys/
    tde/                        #   transformacion digital (29 files)
      estrategia/ guias/ leyes/ normas_tecnicas/ plataformas/
    legal/                      #   normativa legal (21 files)
    gov/                        #   gobierno central (9 files)
    orko/                       #   8 KBs condensados
    mgmt/                       #   management (4 files)

  agents/                       # 41 agents as KORA workspaces (AGENTS.md + SOUL.md + USER.md + TOOLS.md + config.json + skills/)
    kora/                       #   7 framework agents
    fxsl/                       #   15 personal agents
    gn/                         #   12 GORE agents
    ops/                        #   3 transversal agents
    tde/                        #   1 agent
    orko/                       #   1 agent
    korvo/                      #   2 agents

  catalog/                      # Master URN registry
  skills/                       # Skills federation
  scripts/                      # CLI tools (kora index/resolve/health/validate/stats)
  docs/                         # Plans and documentation
```

### Governance Hierarchy (precedence, highest to lowest)

1. **gobernanza.md** — Meta-rules governing the ecosystem
2. **md-spec.md** (descriptive) / **spec-md.md** (prescriptive) — Format specifications
3. **agent-spec-md.md** — Agent architecture specification
4. Namespace extensions

### Agent Model (agent-spec-md.md v5.0.0)

An agent is an F-coalgebra `c: U → F(U)` with 5 essential components:

| # | Component | Symbol | Materializes as |
|---|-----------|--------|----------------|
| 1 | Transition morphism | c | AGENTS.md (FSM) |
| 2 | Interface functor | F | TOOLS.md |
| 3 | State space (fibres) | U | SOUL.md + USER.md |
| 4 | Effect monad | M | config.json |
| 5 | Wiring diagram | W | AGENTS.md adjunctions |

### URN System

Format: `urn:{namespace}:{type}:{id}` — e.g., `urn:kora:kb:agent-spec-md`

Active namespaces: **kora**, **fxsl**, **gn**, **tde**, **orko**, **korvo**, **gov**, **legal**, **mgmt**

Catalog (`catalog/catalog_master_kora.yml`) is the source of truth. Run `scripts/kora index` after changes.

### Migration Status

Completed:
- **Phase 0** (Genesis): Namespace-based directory restructuring
- **Phase 1** (Source Mapping): 208 artifacts mapped (79 FROM_SOURCE, 129 FROM_YAML)
- **Phase 2** (Koraficacion): 175+ YAML KBs → KORA/MD Markdown across all namespaces
- **Spec consolidation**: wf-koraficacion absorbed into md-spec v2.0.0 §6
- **CLI adaptation**: `scripts/kora` index/health/stats adapted to KORA/MD format
- **Phase 4** (Agentificacion): 40 YAML monoliths → 41 KORA workspaces via functor G₂ (agent-spec §12). 139 skills (CM-*.md files), 0 broken URN references (run `scripts/kora health` to verify).
- **Phase Audit** (Coherencia): Auditoría de coherencia lógica/semántica/editorial completa del corpus. Fix de 77 URNs rotas, skills materializados para 17 agentes, colon-newline fxsl/cat, gobernanza.md actualizada, KODA→KORA renaming.

Pending:
- **Phase F** (Governance): KODA formal deprecation, catalog regeneration, source repo archival

## Key Conventions

- **RFC 2119 keywords** (DEBE, NO DEBE, DEBERIA, PUEDE) are normative in prescriptive documents
- **Koraficacion** (md-spec §6): Transform human documents into KORA/MD — telegraphic, RAG-optimized
- **Agentificacion** (agent-spec §12): Functor G transforms KODA YAML monoliths into KORA workspace directories
- **Segregation principle**: FSM logic (c) must never mix with personality (SOUL.md), operator context (USER.md), or security policies (config.json)
