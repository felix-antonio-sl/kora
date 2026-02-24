---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-sistemas-informacion-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB → LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual. Politica LLM_NATIVE: conocimiento internalizado, KB consultable pero no obligatorio.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Algebraic databases, profunctors, bimodules | urn:fxsl:kb:algebraic-databases |
| Multi-model, Grothendieck, schema cat | urn:fxsl:kb:unified-multimodel |
| Data lakes, zones, categorical framework | urn:fxsl:kb:data-lakes-ct |
| CQL, provenance, data integration | urn:fxsl:kb:cql-data-integration |
| Categorical Systems Theory, lenses, wiring | urn:fxsl:kb:categorical-systems-theory |
| Schema evolution, versions, migration | urn:fxsl:kb:schema-evolution |
| DAL, SQL/NoSQL, APIs, repos, ORMs | urn:fxsl:kb:data-access-layers |
| CT approaches databases (survey) | urn:fxsl:kb:exploring-category-theoretic-approaches-to-databases |
| Formal framework DL CT | urn:fxsl:kb:formal-framework-data-lakes-ct |
| Formal framework multimodel transformations | urn:fxsl:kb:formal-framework-multimodel-data-transformations |
| Multicategory multimodel query processing | urn:fxsl:kb:multicategory-multimodel-query-processing |
| Unified representation transformation multimodel | urn:fxsl:kb:unified-representation-transformation-multimodel |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, sintaxis especifica versiones DBMS, configuraciones performance, frameworks recientes.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.

## artifact_generate

- **Firma:** model: DataModel, format: TargetFormat → artifact: string
- **Cuando usar:** S-ARTIFACT-GENERATION. Traducir modelo de datos a formato target.
- **Cuando NO usar:** Modelo no formalizado aun (requiere S-DATA-MODELING primero).
- **Formatos:** PostgreSQL DDL, MySQL DDL, GraphQL SDL, JSON Schema, OpenAPI 3.x, Prisma, Mermaid ERD, Data Flow Diagram, Work System Snapshot, Migration Scripts
