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
| Algebraic databases, profunctors, bimodules | urn:kora:kb:cat-foundations |
| Multi-model, Grothendieck, schema cat | urn:kora:kb:cat-discovery-presheaf |
| Data lakes, zones, categorical framework | urn:kora:kb:cat-discovery-presheaf |
| CQL, provenance, data integration | urn:kora:kb:cat-audit-invariants |
| Categorical Systems Theory, lenses, wiring | urn:kora:kb:cat-behavioral-preservation |
| Schema evolution, versions, migration | urn:kora:kb:cat-audit-invariants |
| DAL, SQL/NoSQL, APIs, repos, ORMs | urn:kora:kb:cat-audit-invariants |
| CT approaches databases (survey) | urn:kora:kb:cat-foundations |
| Formal framework DL CT | urn:kora:kb:cat-discovery-presheaf |
| Formal framework multimodel transformations | urn:kora:kb:cat-discovery-presheaf |
| Multicategory multimodel query processing | urn:kora:kb:cat-discovery-presheaf |
| Unified representation transformation multimodel | urn:kora:kb:cat-discovery-presheaf |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, sintaxis especifica versiones DBMS, configuraciones performance, frameworks recientes.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.

## artifact_generate

- **Firma:** model: DataModel, format: TargetFormat → artifact: string
- **Cuando usar:** S-ARTIFACT-GENERATION. Traducir modelo de datos a formato target.
- **Cuando NO usar:** Modelo no formalizado aun (requiere S-DATA-MODELING primero).
- **Formatos:** PostgreSQL DDL, MySQL DDL, GraphQL SDL, JSON Schema, OpenAPI 3.x, Prisma, Mermaid ERD, Data Flow Diagram, Work System Snapshot, Migration Scripts
