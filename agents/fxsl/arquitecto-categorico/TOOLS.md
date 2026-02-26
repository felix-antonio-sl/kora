---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-categorico-tools:3.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Enrutador Macro                           | Alcance                                                                                            | URNs Asociadas (Buscar en catalogo)                                                                                                                                                                                                                                                                                |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Estructuras Estáticas & Datos Puros**   | Modelado DDL, JSON Schema, GraphQL, Primary Keys, Constraints.                                     | `urn:fxsl:kb:seven-sketches`, `urn:fxsl:kb:categorical-data-structures`, `urn:fxsl:kb:constraint-logic`, `urn:fxsl:kb:action-primary-key`, `urn:fxsl:kb:data-access-layers`                                                                                                                                        |
| **Integración & Data Lakes**              | Multi-modelos, Data Lakes, CQL, Grothendieck, Transformaciones, Pushouts.                          | `urn:fxsl:kb:cql-data-integration`, `urn:fxsl:kb:data-lakes-ct`, `urn:fxsl:kb:formal-framework-data-lakes-ct`, `urn:fxsl:kb:unified-multimodel`, `urn:fxsl:kb:multicategory-multimodel-query-processing`, `urn:fxsl:kb:unified-representation-transformation-multimodel`, `urn:fxsl:kb:algebraic-model-management` |
| **Comportamiento & Transiciones (Topos)** | Coalgebras, Lenses, Monads, Dinámica stateful, Teoría de Sistemas.                                 | `urn:fxsl:kb:coalgebras`, `urn:fxsl:kb:categorical-systems-theory`, `urn:fxsl:kb:cognitive-toolkit`                                                                                                                                                                                                                |
| **Evolución & Auditoría**                 | Migraciones de esquemas (Δ/Σ/Π), Evolución en el tiempo, Patrones de Auditoría, Consistency MBSE.  | `urn:fxsl:kb:schema-evolution`, `urn:fxsl:kb:audit-patterns`, `urn:fxsl:kb:mbse-consistency`, `urn:fxsl:kb:formal-framework-multimodel-data-transformations`                                                                                                                                                       |
| **Meta-Arquitectura & Epistemología**     | Profuntores, Bimodules, Tensión DIK, Bases de Conocimiento formales, Representaciones Algebraicas. | `urn:fxsl:kb:algebraic-databases`, `urn:fxsl:kb:kb-category`, `urn:fxsl:kb:mathematical-modelling`, `urn:fxsl:kb:exploring-category-theoretic-approaches-to-databases`                                                                                                                                             |
