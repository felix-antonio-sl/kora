---
_manifest:
  urn: "urn:kora:kb:runtime-deployment-inventory-2026-05-03"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-05-03"
    source: "Inventario posterior al retiro runtime del stack meta-KORA historico en /home/felix."
version: "1.0.0"
status: publicado
tags: [runtime, deployment, inventory, claude-code, codex, opencode, meta-kora]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:meta-kora-rebuild-directive"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
---

# Inventario runtime `/home/felix` — 2026-05-03

## 1. Rutas activas

| Runtime | Agentes | Skills |
|---|---|---|
| Claude Code | `/home/felix/.claude/agents/` | `/home/felix/.claude/skills/` |
| Codex | `/home/felix/.codex/agents/` | `/home/felix/.codex/skills/` |
| OpenCode | `/home/felix/.config/opencode/agents/` | `/home/felix/.config/opencode/skills/` |

Regla: todo artefacto KORA desplegado en esas rutas debe provenir de IR
canonico validado y de una transmutacion fresca.

## 2. Activos canonicos disponibles

### Agentes

| Runtime | Canonicamente desplegados |
|---|---|
| Claude Code | `allan-kelly`, `salubrista`, `steipete`, `urgenciologo` |
| Codex | `allan-kelly`, `steipete` |
| OpenCode | `allan-kelly`, `steipete` |

### Skills

| Runtime | Canonicamente desplegadas |
|---|---|
| Claude Code | `cat-thinking`, `cell-design`, `jointjs-open-source`, `mente-omega`, `modelamiento-opm`, `ship-discipline` |
| Codex | `cat-thinking`, `cell-design`, `jointjs-open-source`, `mente-omega`, `modelamiento-opm`, `ship-discipline` |
| OpenCode | `cat-thinking`, `cell-design`, `jointjs-open-source`, `mente-omega`, `ship-discipline` |

## 3. Extras no canonicos detectados

Claude Code conserva artefactos externos/no canonicos en sus rutas activas:

- agentes: `agent-architect`, `forjador-openclaw`, `ifml-architect`,
  `jobs-healthcare-ux`, `opm-specialist`, `polymath`,
  `steve-jobs-agentic-designer`, `ux-research-design-ai`
- skills: `database-designer`

No se movieron en esta pasada porque no pertenecen al stack meta-KORA retirado.

## 4. Retiro ejecutado

Los siguientes artefactos dejaron de estar activos en Claude Code, Codex y
OpenCode:

- agente: `custodio`
- skills: `artifact-curator`, `kora-agents`, `kora-skills`

Ubicacion de cuarentena reversible:

- `/home/felix/.kora/quarantine/rebuild-required/2026-05-03/claude/`
- `/home/felix/.kora/quarantine/rebuild-required/2026-05-03/codex/`
- `/home/felix/.kora/quarantine/rebuild-required/2026-05-03/opencode/`

Estos bundles quedan disponibles solo para inventario negativo. No son fuente
de diseno ni runtime valido para la nueva generacion meta-KORA.
