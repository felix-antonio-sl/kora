---
_manifest:
  urn: urn:kora:skill:forgemaster-lifecycle-orchestrator:2.0.0
  type: lazy_load_endofunctor
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Consolida checkpoints y entregables del modo guiado del ciclo DESIGN -> CREATE -> IMPLEMENT -> VALIDATE sin gobernar transiciones FSM.

## Input/Output
- **Input:** checkpoint_label: string, entregables: object, observaciones: string[] | null
- **Output:** LifecycleReport (ver Signature Output)

## Procedimiento
1. Recibir la etiqueta del checkpoint actual y los entregables ya producidos.
2. Normalizar el checkpoint: objetivos cubiertos, artefactos producidos, pendientes y riesgos.
3. Consolidar los checkpoints previos compatibles en un resumen acumulado del ciclo guiado.
4. Emitir un reporte estructurado de continuidad sin gobernar transiciones ni introducir control secuencial.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| checkpoint_consolidado | string | Etiqueta del checkpoint reportado |
| checkpoints_previos | string[] | Checkpoints con resumen disponible |
| pendientes | string[] | Pendientes visibles para continuar el ciclo |
| observaciones | string[] | Notas relevantes del ciclo guiado |
