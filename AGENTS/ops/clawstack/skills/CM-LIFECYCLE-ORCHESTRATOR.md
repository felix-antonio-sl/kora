---
_manifest:
  urn: urn:ops:skill:clawstack-lifecycle-orchestrator:1.0.0
  type: lazy_load_endofunctor
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Consolida checkpoints y entregables del modo guiado (PROVISION -> CONFIGURE -> AUDIT o DEPLOY -> AUDIT) sin gobernar transiciones FSM.

## Input/Output
- **Input:** fase_actual: string (PROVISION|CONFIGURE|AUDIT|DEPLOY), entregables: PhaseDeliverable[]
- **Output:** LifecycleSummary (ver Signature Output)

## Procedimiento
1. Recibir fase guiada activa y entregables producidos por el skill de la fase.
2. Normalizar checkpoint: plataforma, estado visible del stack (3 capas), issues, pendientes.
3. Consolidar checkpoints de las fases completadas en resumen acumulado.
4. Emitir resumen estructurado para que la FSM determine siguiente fase.
5. Al completar AUDIT (ultima fase del ciclo provision o deploy): emitir resumen final del ciclo completo.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| plataforma | string | Plataforma target |
| fases_completadas | string[] | Fases ya terminadas |
| estado_stack | {host, docker, openclaw} | Estado visible por capa |
| issues_abiertos | string[] | Issues pendientes |
| proximos_pasos | string[] | Acciones recomendadas |
