---
_manifest:
  urn: "urn:kora:doc:audit-clawforge-r2-2026-03-24"
  provenance:
    created_by: "kora/forgemaster"
    created_at: "2026-03-24"
    source: "CM-AGENT-VALIDATOR contra agent-spec v8.9.0, skill-spec v4.3.0, gobernanza v3.5.0"
version: "1.0.0"
status: published
tags: [audit, clawforge, agent-spec, skill-spec]
lang: es
extensions: {}
---

# Auditoría kora/clawforge — Ronda 2 (2026-03-24)

## Contexto

Segunda ronda de auditoría sobre kora/clawforge tras la corrección de la ronda 1 (orphan skills, cross-skill composition, FSM destinations en outputs). Esta ronda verifica conformidad completa post-fix.

**Auditor:** kora/forgemaster (S-VALIDATE → CM-AGENT-VALIDATOR)
**Target:** `AGENTS/kora/clawforge/`
**Baseline:** agent-spec-md v8.9.0, skill-spec-md v4.3.0, gobernanza v3.5.0

## Resultado

**Inicial: FAIL** (1 HIGH, 2 MEDIUM, 1 LOW)
**Post-fix: PASS** (31/31 checks, 0 issues en toolchain)

## Hallazgos

| ID | Sev | Componente | Hallazgo | Fix |
|----|-----|-----------|----------|-----|
| H-01 | HIGH | skills/ (3 SKILL.md) | 3 URN references rotas: skills bumped a v1.1.0 sin re-indexar catálogo (CM-OPENCLAW-CONTRACT-VALIDATOR, CM-OPENCLAW-HANDOFF, CM-OPENCLAW-PATCH-APPLIER) | `kora index` |
| M-01 | MEDIUM | CM-CONTEXT-MANAGER.md | Procedimiento paso 2 codifica destino FSM: "reenviar a S-DISPATCHER" | Cambiado a "marcar shift detectado" |
| M-02 | MEDIUM | CM-OPENCLAW-SURGEON.md | Procedimiento paso 3 codifica destino FSM: "reenviar a S-VALIDATE" | Cambiado a "Recomendar revalidacion del componente tocado" |
| L-01 | LOW | AGENTS.md | ACTs de S-HANDOFF y S-PROMOTE verbosos (descriptivos, no procedurales) | Informativo, no corregido |

## Checks ejecutados (31)

| # | Check | Spec | Veredicto |
|---|---|---|---|
| 1 | Topología obligatoria | agent-spec §3 | PASS |
| 2 | Frontmatter bootstrap | agent-spec §3 | PASS |
| 3 | Version workspace | agent-spec §3 | PASS |
| 4 | Gramática de behavior | agent-spec §4.1 | PASS |
| 5 | FSM canónica | agent-spec §4.2-§4.3 | PASS |
| 6 | ACT breve | agent-spec §4.2.8 | PASS |
| 7 | CM obligatorio | agent-spec §4.2.9 | PASS |
| 8 | Segregación componentes | agent-spec §4.4 | PASS |
| 9 | SOUL.md canónico | agent-spec §4.4 | PASS |
| 10 | Behavior puro | agent-spec §4.3 | PASS |
| 11 | Interfaz cerrada | agent-spec §5 | PASS |
| 12 | kb_route con URNs | agent-spec §5 | PASS |
| 13 | allowed_kb resoluble | agent-spec §6 | PASS |
| 14 | Runtime segregado | agent-spec §5-§6 | PASS |
| 15 | Config válido | agent-spec §6 | PASS |
| 16 | Co-inducción mínima | agent-spec §4.1 | PASS |
| 17 | Contexto multi-turno | agent-spec §4.1 | PASS |
| 18 | Skills resolubles | agent-spec §7 | PASS |
| 19 | Skills sin huérfanos | agent-spec §7 | PASS |
| 20 | Unicidad materialización | skill-spec §3 | PASS |
| 21 | CM Core canónico | skill-spec §3 | PASS |
| 22 | Identidad skill | skill-spec §3.1 | PASS |
| 23 | Naming convention | skill-spec §3.1.5 | PASS |
| 24 | Bundle gobernado | skill-spec §3.2 | PASS |
| 25 | Metadata acotada | skill-spec §3.2 / gob §6 | PASS |
| 26 | allowed_tools ⊆ TOOLS.md | skill-spec §5 | PASS |
| 27 | No-relajación | skill-spec §6 | PASS |
| 28 | Purity | skill-spec §3.3 | PASS (post-fix) |
| 29 | Routing resoluble | agent-spec §8 | PASS |
| 30 | Toolchain health | gobernanza §10.3 | PASS (post-fix) |
| 31 | Toolchain validate | gobernanza §10.3 | PASS |

## Estadísticas workspace

- 14 estados FSM, 24 skills (13 degenerados, 11 extendidos)
- 12 tools, 11 allowed_kb URNs (todas resolubles)
- 11 reglas duras, 14 checks co-inducción
- 3 archivos tocados en fix + catálogo re-indexado
- `kora health --strict`: 0 issues
- `kora validate --profile strict`: 27/27 válidos

## Patrón corregido

Residual de purity leak: 2 skills nombraban estados FSM directamente en texto de Procedimiento (`S-DISPATCHER`, `S-VALIDATE`). El routing ya estaba correctamente declarado en AGENTS.md; los skills duplicaban la instrucción de forma acoplada. Post-fix: los skills describen la acción semántica y la FSM controla el routing.
