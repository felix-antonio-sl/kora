---
_manifest:
  urn: urn:kora:skill:forgemaster-lifecycle-orchestrator:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Consolida checkpoints y entregables del modo guiado del ciclo DESIGN -> CREATE -> IMPLEMENT -> VALIDATE sin gobernar transiciones FSM.

## Input/Output
- **Input:** fase_activa: string, entregables: object, observaciones: string[] | null
- **Output:** LifecycleReport (ver Signature Output)

## Procedimiento
1. Recibir la fase activa y los entregables ya producidos por la FSM o por skills previos.
2. Normalizar el checkpoint de la fase activa: objetivos cubiertos, artefactos producidos, pendientes y riesgos.
3. Consolidar los checkpoints previos compatibles en un resumen acumulado del ciclo guiado.
4. Emitir un reporte estructurado de continuidad que permita retomar el trabajo sin reintroducir control secuencial dentro del skill.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| fase_activa | string | Fase guiada actualmente consolidada |
| fases_registradas | string[] | Fases con checkpoint disponible |
| pendientes | string[] | Pendientes visibles para continuar el ciclo |
| observaciones | string[] | Notas relevantes del ciclo guiado |
