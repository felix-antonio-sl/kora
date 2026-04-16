---
name: opmodel-knowledge
description: Recupera y organiza conocimiento operativo sobre OPModel para steipete, usando primero el repo vivo y luego el legado preservado del steipe antiguo.
---

# OPModel Knowledge

Usar cuando el usuario pregunte por OPModel, HODOM, fixtures `.opmodel`, roadmap, gaps, cobertura ISO, visual core o trabajo legado del steipe antiguo.

## Fuentes en orden

1. Repo vivo: `/home/felix/projects/opmodel`
2. Legado preservado: `reference/opmodel/legacy-steipete/`
3. Memoria local: `memory/2026-03-28-opmodel-legacy.md`
4. Corpus OPM/ISO: `/home/felix/kora/KNOWLEDGE/fxsl/opm/`

## Reglas

- Tratar `/home/felix/projects/opmodel` como fuente primaria del estado actual.
- Tratar `reference/opmodel/legacy-steipete/` como memoria operacional y contexto histórico.
- No asumir que métricas, tests o commits del legado siguen vigentes sin verificar en el repo vivo.
- Traducir rutas legacy dentro de contenedor (`/home/node/projects/opmodel`) a la ruta host actual (`/home/felix/projects/opmodel`).
- Cuando el usuario pida roadmap o deuda, revisar `informe-gaps-plan-implementacion.md` y contrastar con el repo vivo.
- Cuando el usuario pida teoría OPM/ISO, responder desde el corpus `fxsl/opm`, no desde artefactos de producto.

## Salida esperada

- Estado actual del repo vivo
- Contexto histórico relevante del legado
- Diferencia entre pasado preservado y presente real
- Siguiente acción sugerida si aplica
