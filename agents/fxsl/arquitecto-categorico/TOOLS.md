---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-categorico-tools:2.0.0"
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
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| FDM, DIK, Lenses, Monads | urn:fxsl:kb:cognitive-toolkit |
| DB functors, adj, lim/colim, migration | urn:fxsl:kb:seven-sketches |
| Profunctors, bimodules, uber-queries | urn:fxsl:kb:algebraic-databases |
| Lenses, wiring, monadic, behavior | urn:fxsl:kb:categorical-systems-theory |
| Coalg, bisim, coinduction, OOP | urn:fxsl:kb:coalgebras |
| Schema cat, multi-model, Grothendieck | urn:fxsl:kb:unified-multimodel |
| Data lakes, zones | urn:fxsl:kb:data-lakes-ct |
| CQL, provenance, ologs | urn:fxsl:kb:cql-data-integration |
| Model complexity, convertibility | urn:fxsl:kb:mathematical-modelling |
| MBSE, S2ML, consistency | urn:fxsl:kb:mbse-consistency |
| Audit dims, severity, patterns | urn:fxsl:kb:audit-patterns |
| KB as cat, invariants | urn:fxsl:kb:kb-category |
| Constraints, preservation | urn:fxsl:kb:constraint-logic |
| Schema evolution, versions | urn:fxsl:kb:schema-evolution |
| DAL, SQL/NoSQL, APIs, repos, ORMs, lakes | urn:fxsl:kb:data-access-layers |
| Tensiones, polos, adjunciones diseno, A1-A4, MBT | urn:fxsl:kb:fx-tensiones |
| Action as PK, event sourcing | urn:fxsl:kb:action-primary-key |
| Categorical data structures | urn:fxsl:kb:categorical-data-structures |
| Algebraic model management | urn:fxsl:kb:algebraic-model-management |
| CT approaches to databases (survey) | urn:fxsl:kb:exploring-category-theoretic-approaches-to-databases |
| Formal framework DL CT | urn:fxsl:kb:formal-framework-data-lakes-ct |
| Formal framework multimodel transformations | urn:fxsl:kb:formal-framework-multimodel-data-transformations |
| Multicategory multimodel query processing | urn:fxsl:kb:multicategory-multimodel-query-processing |
| Unified representation transformation multimodel | urn:fxsl:kb:unified-representation-transformation-multimodel |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, frameworks especificos, sintaxis de versiones recientes.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.

## artifact_generate

- **Firma:** model: CategoricalModel, format: TargetFormat → artifact: string
- **Cuando usar:** S-ARTIFACT-GENERATION. Traducir modelo categorico a formato target.
- **Cuando NO usar:** Modelo no formalizado aun (requiere S-CATEGORICAL-MODELING primero).
- **Formatos:** PostgreSQL DDL, GraphQL SDL, JSON Schema, OpenAPI 3.x, Prisma, Mermaid, PlantUML, SPARQL
