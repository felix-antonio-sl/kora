---
_manifest:
  urn: urn:kora:skill:clawmaster-lifecycle-orchestrator:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Consolida checkpoints y entregables del modo guiado INSTALL -> CONFIGURE -> AUDIT para instancias OpenClaw, sin gobernar transiciones FSM desde el skill.

## Input/Output
- **Input:** fase_activa: string, plataforma: string, entregables: object
- **Output:** LifecycleSummary (ver Signature Output)

## Procedimiento
1. Recibir la fase guiada activa y los entregables ya producidos por el agente o por otros skills.
2. Normalizar el checkpoint de la fase activa: plataforma, estado visible, issues, pendientes y observaciones.
3. Consolidar checkpoints compatibles de install, configure y audit en un resumen acumulado del ciclo guiado.
4. Emitir un resumen estructurado que permita continuar el trabajo sin incrustar control secuencial del agente dentro del skill.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| plataforma | string | Plataforma de la instancia |
| fases_registradas | string[] | Fases con checkpoint disponible |
| estado_visible | string | Estado consolidado visible de la instancia |
| issues_abiertos | string[] | Issues aun abiertos en el ciclo guiado |
| proximos_pasos | string[] | Acciones recomendadas para continuar |
