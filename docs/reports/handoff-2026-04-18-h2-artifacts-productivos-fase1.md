---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-18-h2-artifacts-productivos-fase1"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-18"
    source: "Handoff operativo parcial del frente H2-artifacts sobre agentes productivos."
version: "1.0.0"
status: publicado
tags: [handoff, h2-artifacts, agents, skills, productivos]
lang: es
extensions:
  kora:
    family: note
---

# Handoff explicito — H2-artifacts sobre productivos

## Alcance ejecutado

Se trabajo solo en territorio propio:

- `artifacts/agents/*`
- `artifacts/skills/*`
- `docs/reports/`

No se modificaron artefactos de knowledge, toolchain, tests ni `docs/generated/`.

## Resultado

### Productivos GN

Se promovieron dos habilidades productivas nuevas:

- `urn:gn:artefacto:intake`
- `urn:gn:artefacto:synthesizer`

Se actualizaron:

- `artifacts/agents/gn/digitrans/AGENT.md`
- `artifacts/agents/gn/goreologo/AGENT.md`

Criterio aplicado:

- `PROMOVER`: intake y synthesizer por reuso entre ambos agentes.
- `ABSORBER`: guidance y analisis de dominio propios del agente al cuerpo del `AGENT.md`.
- Compatibilidad transitoria: los `CM-*` locales se mantuvieron como capa contractual porque la suite vigente todavia los exige en `skill_refs`.

### Productivos KORA

Se promovieron tres habilidades productivas nuevas:

- `urn:kora:artefacto:context-manager`
- `urn:kora:artefacto:intent-classifier`
- `urn:kora:artefacto:lifecycle-orchestrator`

Se actualizaron:

- `artifacts/agents/kora/clawforge/AGENT.md`
- `artifacts/agents/kora/curator/AGENT.md`
- `artifacts/agents/kora/custodio/AGENT.md`
- `artifacts/agents/kora/forgemaster/AGENT.md`
- `artifacts/agents/kora/guardian/AGENT.md`

Criterio aplicado:

- `PROMOVER`: contexto, intent y lifecycle por reuso claro entre multiples agentes productivos.
- `ABSORBER`: modulos especificos de OpenClaw, curaduria, stewardship, forja y guardia normativa al lenguaje operativo del `AGENT.md`.
- Compatibilidad transitoria: se mantuvo `artefacto.skills` local por contrato vigente del operating core y tests dinamicos.

## Verificacion observada

Corridas exitosas durante esta fase:

- `python3 toolchain/kora check --strict` → `17/17` verde
- `python3 -m unittest discover -s tests` → `302 OK (skipped=2)`

Nota:

- El baseline inicial era `299 OK`, pero el worktree contiene drift paralelo en `tests/`, `toolchain/`, `serialization/` y knowledge del territorio del agente A. No se toco ese frente.

## Commits realizados

1. `5670a1e` — `agents(gn): promueve intake y synthesizer`
2. `b1e498e` — `agents(kora/clawforge): promueve core de contexto e intent`
3. `e15b553` — `agents(kora): absorbe modulos operativos en body`

## Observaciones sobre territorio ajeno

Se detecto drift activo fuera del frente propio:

- `serialization/knowledge-spec.md`
- `tests/test_artifacts.py`
- `tests/test_cli_smoke.py`
- `tests/test_graph_invariants.py`
- `toolchain/kora_lib/{graph,kb_graph,promote,reports}.py`
- knowledge nueva bajo `artifacts/knowledge/kora/sys/*`
- `docs/generated/*`

No se intervinieron. Si se requiere merge final, regenerar `docs/generated/*` despues de integrar ambos frentes.

## Reentrada exacta

Si la siguiente sesion retoma este frente, el punto de partida correcto es:

1. `git status --short` para confirmar que el drift pendiente sigue siendo ajeno al frente propio.
2. `git log --oneline --decorate -6` para verificar que los commits de esta fase sigan en `master`.
3. `python3 toolchain/kora check --strict`
4. `python3 -m unittest discover -s tests`
5. Inventario de `_FRAGUA/INBOX/` y `_TALLER/INBOX/` antes de promover nada.

## Pendiente

No se abordo aun:

- `FRENTE 2` de staging en `artifacts/agents/_FRAGUA/INBOX/`
- `FRENTE 2` de staging en `artifacts/skills/_TALLER/INBOX/`

Siguiente paso recomendado:

1. Inventariar `_FRAGUA/INBOX/` y `_TALLER/INBOX/` con triage `promover / deduplicar / descartar`.
2. Mantener el mismo patron: skill productivo nuevo si hay objeto reusable real; compatibilidad minima solo si el contrato vigente la exige.
