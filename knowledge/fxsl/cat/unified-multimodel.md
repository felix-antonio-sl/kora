---
urn: urn:fxsl:kb:unified-multimodel
version: 1.0.0
status: published
tags: [category-theory, multi-model, data-integration, schema-unification]
lang: es
---

# Unified Multi-Model Representation

## Overview

Framework for representing multi-model data (relational, document, graph, key-value) via unified schema category. Enables cross-model querying and integration.

## Global Schema Category

**Definition**: Schema Category global: category whose objects are logical types and morphisms are relations/paths between them.

| Component | Structure |
|-----------|-----------|
| **Objects** | Tables, collections, nodes, documents, keyspaces |
| **Morphisms** | Foreign Keys, refs, edges, paths, patterns |
| **Attributes** | root, pkey, refs, access_path per kind |

**Purpose**: Unified view of all data models before integration.

### Construction Process

1. Inventory all data sources (PostgreSQL, MongoDB, Neo4j, Redis, etc.)
2. Per source, extract logical types as objects
3. Extract relations (FKs, refs, edges) as morphisms
4. Unify in single category using coproducts for disjoint objects
5. Identify semantically equivalent objects, create equivalence morphisms
6. Result: Global Schema Category

## Model Kinds

**Definition**: Data model classes as realizations of global Schema Category.

| Kind | Objects | Morphisms | Instance |
|------|---------|-----------|----------|
| **Relational** | Tables | Foreign Keys | Sets of tuples |
| **Document** | Collections | Nested refs/embedding | JSON trees |
| **Graph** | Nodes (types) | Edges (types) | Labeled graphs |
| **Key-Value** | Keyspaces | Key prefixes/patterns | K→V maps |

## Instance Category

**Instance Functor**: Instance = funtor I: SchemaCategory → Set assigning concrete data to each global type.

**Purpose**: Represent combined content of multiple databases as single categorical instance.

**Wrapper Functor**: W_db: DB_specific → SchemaCategory translates each physical schema to global schema.

**Examples**:
- W_postgres, W_mongo, W_neo4j: each maps tables/collections/graphs to Schema Category objects

**Use**: Normalize different technologies to common categorical language.

## Query Processing

**Query as Functor**: Multi-model query = funtor Q: SchemaCategory → OutputKind.

**Interpretation**: Each query selects output type (relational/document/graph/flat) as target category.

### Query Execution

1. Define query in terms of global Schema Category
2. Choose OutputKind (relational, document, graph, flat)
3. Build funtor Q mapping global types to output types
4. Execute Q on global instance I: get Q(I)
5. Materialize result in OutputKind format

**Example**: Users with orders across PostgreSQL + MongoDB

```
SchemaCategory: {User, Order, user_orders: Order→User}
OutputKind: document (JSON)
Result: [{user: {...}, orders: [{...}, {...}]}]
```

## Output Models

**Definition**: OutputKind = target category representing output format.

| OutputKind | Use Case |
|-----------|----------|
| **relational** | SQL-based consumers, JOIN-heavy workloads |
| **document** | REST/GraphQL APIs, frontends |
| **graph** | Traversals, path queries |
| **flat** | CSV exports, ETL, ML pipelines |

### Decision Guide

- **relational**: When consumer is SQL-based or needs complex JOINs
- **document**: When consumer is REST/GraphQL API or frontend
- **graph**: When traversals or path queries required
- **flat**: For exports, simple ETL, or ML pipelines
