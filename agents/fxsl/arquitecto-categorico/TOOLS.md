---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-categorico-tools:3.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** `urn: string -> path: string`
- **Parametros:** `urn` conceptual del artefacto KB a resolver.
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo antes de acceder al artefacto.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en el turno actual.
- **Descripcion funcional:** Resuelve una URN valida del catalogo a la ruta local del artefacto de conocimiento.
- **Notas:** `catalog_master_*.yml` es la fuente de verdad del catalogo.

## kb_route

- **Firma:** `query_topic: string -> urns: string[]`
- **Parametros:** `query_topic` con la familia de modelado o integracion a priorizar.
- **Cuando usar:** Clasificar tema y priorizar una o mas URNs KB antes de resolverlas via `catalog_resolve`.
- **Cuando NO usar:** Cuando el tema ya fue mapeado en el turno actual.
- **Descripcion funcional:** Devuelve el conjunto de URNs KB primarias asociadas a una macro-familia conceptual del agente.
- **Routing Map:**

| Enrutador Macro | Alcance | URNs Asociadas |
| --- | --- | --- |
| **Estructuras Estaticas y Datos Puros** | Modelado DDL, JSON Schema, GraphQL, primary keys, constraints | `urn:fxsl:kb:seven-sketches`, `urn:fxsl:kb:categorical-data-structures`, `urn:fxsl:kb:constraint-logic`, `urn:fxsl:kb:action-primary-key`, `urn:fxsl:kb:data-access-layers` |
| **Integracion y Data Lakes** | Multi-modelos, data lakes, CQL, Grothendieck, transformaciones, pushouts | `urn:fxsl:kb:cql-data-integration`, `urn:fxsl:kb:data-lakes-ct`, `urn:fxsl:kb:formal-framework-data-lakes-ct`, `urn:fxsl:kb:unified-multimodel`, `urn:fxsl:kb:multicategory-multimodel-query-processing`, `urn:fxsl:kb:unified-representation-transformation-multimodel`, `urn:fxsl:kb:algebraic-model-management` |
| **Comportamiento y Transiciones** | Coalgebras, lenses, monadas, dinamica stateful, teoria de sistemas | `urn:fxsl:kb:coalgebras`, `urn:fxsl:kb:categorical-systems-theory`, `urn:fxsl:kb:cognitive-toolkit` |
| **Evolucion y Auditoria** | Migraciones de esquemas, evolucion en el tiempo, patrones de auditoria, consistency MBSE | `urn:fxsl:kb:schema-evolution`, `urn:fxsl:kb:audit-patterns`, `urn:fxsl:kb:mbse-consistency`, `urn:fxsl:kb:formal-framework-multimodel-data-transformations` |
| **Meta-Arquitectura y Epistemologia** | Profuntores, bimodules, tension DIK, KBs formales, representaciones algebraicas | `urn:fxsl:kb:algebraic-databases`, `urn:fxsl:kb:kb-category`, `urn:fxsl:kb:mathematical-modelling`, `urn:fxsl:kb:exploring-category-theoretic-approaches-to-databases` |
