---
_manifest:
  urn: urn:kora:skill:curator-lifecycle-orchestrator:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Consolida checkpoints y entregables del modo guiado de curaduria sin gobernar transiciones FSM ni secuenciar el agente desde el skill.

## Input/Output
- **Input:** fase_activa: string, entregables: object, fuentes: Document[] | null
- **Output:** LifecycleSummary (ver Signature Output)

## Procedimiento
1. Recibir la fase guiada activa y los entregables ya producidos por la FSM o por skills previos.
2. Normalizar el checkpoint de la fase activa: plan, artefacto, metricas, observaciones y pendientes.
3. Consolidar checkpoints compatibles de design, forge y audit en un resumen acumulado del ciclo guiado.
4. Emitir un resumen estructurado que permita continuar el trabajo sin recodificar control del agente dentro del skill.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| fase_activa | string | Fase guiada actualmente consolidada |
| fases_registradas | string[] | Fases con checkpoint disponible |
| tipo | enum(descriptivo\|prescriptivo)\|null | Tipo de artefacto si ya fue clasificado |
| urn | URN \| null | URN del artefacto si ya existe |
| metricas_visibles | {FS: number, CR: number} \| null | Metricas acumuladas visibles |
| pendientes | string[] | Pendientes para continuar el ciclo |
