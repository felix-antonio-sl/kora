---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-18-h2-artifacts-productivos-fase1"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-18"
    source: "Memoria operativa compacta del frente H2-artifacts sobre agentes productivos."
version: "1.0.0"
status: publicado
tags: [operational-memory, snapshot, h2-artifacts, agents, skills]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-h2-artifacts-productivos-fase1"
---

# Memoria operativa — H2-artifacts productivos fase 1

Snapshot operativo al cierre del barrido sobre los 7 agentes productivos.

## Snapshot numerico

| Metrica | Valor | Nota |
|---------|-------|------|
| Agentes productivos tocados | 7 | `gn/{digitrans,goreologo}` + `kora/{clawforge,curator,custodio,forgemaster,guardian}` |
| Skills productivos nuevos | 5 | `gn/intake`, `gn/synthesizer`, `kora/context-manager`, `kora/intent-classifier`, `kora/lifecycle-orchestrator` |
| Commits de la fase | 3 | `5670a1e`, `b1e498e`, `e15b553` |
| Branch local | `master` | trabajo directo por instruccion del usuario |
| Upstream al cerrar esta memoria | `origin/master` | local estaba `ahead` antes del push |
| Check pipeline | `17/17` | `python3 toolchain/kora check --strict` |
| Suite unittest | `302 OK (skipped=2)` | worktree ya traia drift paralelo fuera del frente |

## Decisiones duras

1. `PROMOVER` solo cuando habia reuso real o un morfismo reusable claro.
2. `ABSORBER` cuando la capacidad era propia del agente y no justificaba objeto productivo separado.
3. Mantener compatibilidad minima cuando el contrato vigente o la suite todavia exigian `CM-*` locales o `artefacto.skills`.
4. No tocar `toolchain`, `tests`, `serialization`, `knowledge` ni `docs/generated` del frente ajeno.

## Habilidades promovidas

### Namespace `gn`

- `urn:gn:artefacto:intake`
- `urn:gn:artefacto:synthesizer`

### Namespace `kora`

- `urn:kora:artefacto:context-manager`
- `urn:kora:artefacto:intent-classifier`
- `urn:kora:artefacto:lifecycle-orchestrator`

## Patron aplicado

- `digitrans` y `goreologo`: promotion de intake/synthesizer; el resto se absorbio al `AGENT.md`.
- `clawforge`: promotion de primitives reutilizables; OpenClaw/stack absorbed al behavior.
- `curator`, `custodio`, `forgemaster`, `guardian`: se reescribio el `AGENT.md` para que el body deje de depender semanticamente de `CM-*` y use primitives productivos o descripcion absorbida.

## Riesgos abiertos

1. El worktree mantiene drift paralelo no propio en `tests/`, `toolchain/`, `serialization/`, knowledge y `docs/generated/`.
2. El contrato operativo vigente todavia fuerza compatibilidades locales en algunos agentes; no se intento quebrar ese contrato desde este frente.
3. `_FRAGUA/INBOX/` y `_TALLER/INBOX/` aun no fueron triageados en esta fase.

## Siguiente movimiento recomendado

1. Mantener congelado el frente productivo salvo que aparezca una falla nueva por cambios del agente A.
2. Pasar a staging: inventario, deduplicacion y promocion controlada en `_FRAGUA/INBOX/` y `_TALLER/INBOX/`.
3. Regenerar `docs/generated/*` solo despues de integrar ambos frentes y justo antes del cierre final.
