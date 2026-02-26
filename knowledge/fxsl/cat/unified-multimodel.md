---
_manifest:
  urn: urn:fxsl:kb:unified-multimodel
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 1.0.0
status: published
tags:
- category-theory
- multi-model
- data-integration
- schema-unification
- fxsl
lang: en
---

# Unified Multi-Model Representation

## Overview

Ctx: Global schema category and unification of SQL/NoSQL/Graph models.
Src: Multi-model Data via Category Theory.
XRef: `urn:fxsl:kb:algebraic-databases#UBER-QUERY`, `urn:fxsl:kb:data-lakes-ct#DL-GROTHENDIECK-DEF`

Notes: uber-queries from algebraic_databases enable cross-schema query composition; Grothendieck construction unifies indexed schema families. Together form theoretical basis for CM-INTEGRATION-ENGINE.

## Schema Category Global

**UM-SCHEMA-CATEGORY-GLOBAL** — Schema Category global: category with objects = logical types and morphisms = relations/paths between them.

- Objects: tables, collections, nodes, documents, keyspaces
- Morphisms: Foreign Keys, refs, edges, paths, patterns
- Attributes per object: root, pkey, refs, access_path by kind

Construction procedure:
1. Inventory all data sources (PostgreSQL, MongoDB, Neo4j, Redis, etc.).
2. For each source, extract logical types as objects.
3. Extract relations (FKs, refs, edges) as morphisms.
4. Unify into single category using coproducts for disjoint objects.
5. Identify semantically equivalent objects; create equivalence morphisms.
6. Result = global Schema Category.

## Model Kinds

| Kind | Objects | Morphisms | Instance |
|---|---|---|---|
| Relational | Tables | Foreign Keys | Tuple sets |
| Document | Collections | Nested refs / embedding | JSON trees |
| Graph | Node types | Edge types | Labeled graphs |
| Key-Value | Keyspaces | Key prefixes/patterns | Maps K→V |

All = realizations of global Schema Category.

## Instance Category

**UM-INSTANCE-FUNCTOR** — Multi-model instance = functor I: SchemaCategory → **Set** assigning concrete data to each global type. Represents combined content of multiple databases as single categorical instance.

**UM-WRAPPER-FUNCTOR** — Wrapper W_db: DB_specific → SchemaCategory translates each physical schema to global schema. Examples: W_postgres, W_mongo, W_neo4j each map tables/collections/graphs to global Schema Category objects. Normalizes different technologies to common categorical language.

## Query Processing

**UM-QUERY-AS-FUNCTOR** — Multi-model query = functor Q: SchemaCategory → OutputKind. Each query chooses output type (relational/document/graph/flat) as target category.

Procedure:
1. Define query in terms of global Schema Category.
2. Choose OutputKind (relational, document, graph, flat).
3. Construct functor Q mapping global types to output types.
4. Execute Q over global instance I to get Q(I).
5. Materialize result in OutputKind format.

Example: "users with their orders" over PostgreSQL + MongoDB. SchemaCategory: {User, Order, user_orders: Order→User}. OutputKind: document (JSON). Result: [{user: {...}, orders: [{...}, {...}]}].

**UM-OUTPUT-KIND** — OutputKind = target category representing output format.

| OutputKind | Use When |
|---|---|
| relational | Consumer is SQL-based or needs JOINs |
| document | Consumer is REST API, GraphQL, or frontend |
| graph | Need traversals or path queries |
| flat | CSV exports, simple ETL, ML pipelines |
