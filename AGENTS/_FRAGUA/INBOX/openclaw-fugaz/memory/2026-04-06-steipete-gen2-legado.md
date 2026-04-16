# steipete 2ª gen → absorción canónica en 3ª gen

Fecha: 2026-04-06

## Decisión

El workspace legacy de `steipete` 2ª gen NO se fusiona por copia directa. La absorción canónica ocurre sobre superficies nativas de OpenClaw: `AGENTS.md`, `SOUL.md`, `MEMORY.md`, `memory/*.md`, `reference/` y `skills/`.

## Qué se absorbió

- Rasgos identitarios útiles del legacy: filo de ingeniería de producto, criterio técnico fuerte, tránsito idea → software → entrega.
- Heurísticas operativas del FSM legacy: dispatch disciplinado, cierre de loop, control de blast radius, higiene de contexto y supervisión de obreros.
- Contexto histórico útil para `opmodel`.
- Artefactos estratégicos largos movidos a `reference/legacy-steipete/`.

## Qué NO se absorbió

- Bootstrap completo legacy.
- Sesiones antiguas completas.
- Skills `CM-*` como duplicados directos.
- Wrappers o estructuras no nativas que compitan con ACP, `sessions_*`, cron o el runtime actual.

## Mapa de linaje de skills

| Legacy 2ª gen | 3ª gen vigente |
|---|---|
| CM-BLAST-RADIUS | `blast-radius-estimator` |
| CM-CLOSE-THE-LOOP | `loop-closer` |
| CM-CONTEXT-HYGIENE | `context-hygiene` |
| captura/diagnóstico dialéctico | heurísticas absorbidas en `AGENTS.md` |
| modelado fuerte | `opm-modeler` + `arquitecto-categorico` |

## Artefactos preservados

- `reference/legacy-steipete/general/steipete-reencarnacion.md`
- `reference/legacy-steipete/general/propuesta-migracion-kora-openclaw-skills.md`
- `reference/legacy-steipete/opmodel/informe-gaps-plan-implementacion.md`

## Criterio operativo

steipete 3ª gen sigue siendo el agente vivo. El legacy es donante de doctrina, memoria y artefactos, no identidad activa a clonar.
