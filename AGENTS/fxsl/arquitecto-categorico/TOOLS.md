---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-categorico-tools:3.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Parametros:** `urn` conceptual del artefacto KB a resolver.
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo antes de acceder al artefacto.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en el turno actual.
- **Descripcion funcional:** Resuelve una URN valida del catalogo a la ruta local del artefacto de conocimiento.
- **Notas:** El catalogo es una vista materializada para resolucion; la autoridad primaria sigue siendo el filesystem con manifests validos.

## kb_route

- **Firma:** query_topic: string -> urns: string[]
- **Parametros:** `query_topic` con la familia de modelado o integracion a priorizar.
- **Cuando usar:** Clasificar tema y priorizar una o mas URNs KB antes de resolverlas via `catalog_resolve`.
- **Cuando NO usar:** Cuando el tema ya fue mapeado en el turno actual.
- **Descripcion funcional:** Devuelve URNs canonicas KORA primero y, cuando agrega contexto util, URNs FXSL auxiliares como apoyo secundario.
- **Routing Map:**

| Enrutador Macro | Alcance | URNs canonicas KORA | URNs FXSL de apoyo |
| --- | --- | --- | --- |
| **Estructuras Estaticas y Datos Puros** | Modelado DDL, JSON Schema, GraphQL, primary keys, constraints | `urn:kora:kb:cat-foundations`, `urn:kora:kb:cat-skill-algebra`, `urn:kora:kb:cat-audit-invariants` | `urn:fxsl:kb:seven-sketches`, `urn:fxsl:kb:categorical-data-structures`, `urn:fxsl:kb:constraint-logic`, `urn:fxsl:kb:action-primary-key`, `urn:fxsl:kb:data-access-layers` |
| **Integracion y Data Lakes** | Multi-modelos, data lakes, CQL, Grothendieck, transformaciones, pushouts | `urn:kora:kb:cat-discovery-presheaf`, `urn:kora:kb:cat-audit-invariants`, `urn:kora:kb:cat-fxsl-bridge` | `urn:fxsl:kb:cql-data-integration`, `urn:fxsl:kb:data-lakes-ct`, `urn:fxsl:kb:formal-framework-data-lakes-ct`, `urn:fxsl:kb:unified-multimodel`, `urn:fxsl:kb:multicategory-multimodel-query-processing`, `urn:fxsl:kb:unified-representation-transformation-multimodel`, `urn:fxsl:kb:algebraic-model-management` |
| **Comportamiento y Transiciones** | Coalgebras, lenses, monadas, dinamica stateful, teoria de sistemas | `urn:kora:kb:cat-behavioral-preservation`, `urn:kora:kb:cat-foundations`, `urn:kora:kb:cat-fxsl-bridge` | `urn:fxsl:kb:coalgebras`, `urn:fxsl:kb:categorical-systems-theory`, `urn:fxsl:kb:cognitive-toolkit`, `urn:fxsl:kb:action-primary-key` |
| **Evolucion y Auditoria** | Migraciones de esquemas, evolucion en el tiempo, patrones de auditoria, consistency MBSE | `urn:kora:kb:cat-audit-invariants`, `urn:kora:kb:cat-behavioral-preservation`, `urn:kora:kb:cat-fxsl-bridge` | `urn:fxsl:kb:schema-evolution`, `urn:fxsl:kb:audit-patterns`, `urn:fxsl:kb:mbse-consistency`, `urn:fxsl:kb:formal-framework-multimodel-data-transformations` |
| **Meta-Arquitectura y Epistemologia** | Profuntores, bimodules, tension DIK, KBs formales, representaciones algebraicas | `urn:kora:kb:cat-foundations`, `urn:kora:kb:cat-skill-algebra`, `urn:kora:kb:cat-ecosystem-2cat`, `urn:kora:kb:cat-fxsl-bridge` | `urn:fxsl:kb:algebraic-databases`, `urn:fxsl:kb:kb-category`, `urn:fxsl:kb:mathematical-modelling`, `urn:fxsl:kb:exploring-category-theoretic-approaches-to-databases`, `urn:fxsl:kb:algebraic-model-management` |
