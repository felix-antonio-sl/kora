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
Orquesta el ciclo de vida completo de un artefacto en modo guiado: DESIGN → FORGE (KORAFICATE|CRYSTALLIZE) → AUDIT, consolidando entregables y contexto inter-fase.

## Input/Output
- **Input:** intencion: IntentClassification (modo=GUIADO), fuentes: Document[] | null
- **Output:** LifecycleSummary (ver Signature Output)

## Procedimiento
### Fase 1: DESIGN
1. Invocar CM-ARTIFACT-DESIGNER.
2. Registrar ArtifactPlan, tipo, namespace, URN y fuentes relevantes.
3. Emitir checkpoint estructurado de fase con los pendientes del plan.

### Fase 2: FORGE
1. Segun tipo:
   - Descriptivo → invocar CM-KORAFICATOR (Funtor K).
   - Prescriptivo → invocar CM-CRYSTALLIZER (Funtor C).
2. Registrar artefacto preliminar, metricas y observaciones de fidelidad.
3. Emitir checkpoint estructurado de fase con artefacto y pendientes.

### Fase 3: AUDIT
1. Invocar CM-ARTIFACT-AUDITOR.
2. Consolidar veredicto PASS|FAIL, checks y metricas finales.
3. Si FAIL, registrar issues accionables para una futura fase de reparacion o re-iteracion.

### Cierre
1. Consolidar resumen final: tipo, URN, metricas, status_sugerido y issues resueltos.
2. Registrar acciones operativas sugeridas posteriores al ciclo.

### Gestion de Contexto Inter-Fase
- Mantener estado acumulado entre fases: {fase_actual, plan, artefacto, reporte}.
- Preservar solo datos necesarios para reanudar la fase activa sin recalcular entregables previos.
- Separar checkpoint de fase de cualquier decision conversacional o transicion FSM.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| fases_completadas | string[] | Fases ejecutadas en el ciclo |
| tipo | enum(descriptivo\|prescriptivo) | Tipo de artefacto generado |
| urn | URN | URN del artefacto resultante |
| metricas_finales | {FS: number, CR: number} | Metricas del artefacto validado |
| status_sugerido | enum(draft\|published) | Status sugerido post-ciclo |
