---
_manifest:
  urn: "urn:kora:agent-bootstrap:korax-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo.
- **Cuando NO usar:** Datos ya en contexto.

## buffer_manage

- **Firma:** action: (capture|triage|list|purge), item: string → result: BufferState
- **Cuando usar:** S_CAPTURE, S_TRIAGE. Gestion del buffer de captura PCA.
- **Cuando NO usar:** Fuera de estados de captura/triaje.

## plan_generate

- **Firma:** date: string, context: GTDContext → plan: DailyPlan
- **Cuando usar:** S_PLAN. Planificacion matutina con bloques DEEP/SHALLOW.
- **Cuando NO usar:** Fuera de rutina matutina.

## sync_review

- **Firma:** period: string → review: StrategicReview
- **Cuando usar:** S_SYNC. Sincronizacion estrategica quincenal.
- **Cuando NO usar:** Fuera de rutina de sincronizacion.

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, contexto externo.
- **Cuando NO usar:** Temas cubiertos por KB o contexto del operador.
