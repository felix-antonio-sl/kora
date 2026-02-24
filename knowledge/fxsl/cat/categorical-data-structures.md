---
_manifest:
  urn: "urn:fxsl:kb:categorical-data-structures"
  provenance:
    created_by: "FS"
    created_at: "2025-12-14"
    source: "Categorical Data Structures for Technical Computing (Patterson et al., 2022)"
version: "2.0.0"
status: published
tags: [category-theory, data-structures, gat, c-sets, catlab, technical-computing]
lang: en
---

# Categorical Data Structures

## Overview

Addresses disconnection between rigorous mathematical models and ad-hoc software implementations. Central proposal: use Applied Category Theory to generate data structures automatically from formal specifications.

**Enabling technology**: GATs (Generalized Algebraic Theories), C-Sets (category-indexed sets), ACSets (Attributed C-Sets), Catlab.jl.

## Core Concepts

### C-Set

**Definition**: Given small schema category C, database is funtor X: C → Set.

- For each object c in C, X(c) is set of instances (rows in table).
- For each morfismo f: c → d, X(f): X(c) → X(d) is function (foreign-key column).

### ACSet

**Extension of C-Set** to handle concrete data (numbers, strings). ACSet is funtor X: S → Set where attribute objects map to fixed data types (R, String, etc.).

**Formalism**: Via comma categories or indexing over base type category.

### GAT

**Generalized Algebraic Theory**: system of dependent types allowing definition of categories, funtores, complex structures.

### Schema Presentation

Schema C presented finitely via generators (objects and morfismos) and equations (axioms).

### Syntax/Semantics Separation

- **Syntax**: GAT defines syntax (C).
- **Semantics**: Models of theory (funtores to Set) are data.

### Migration Operators

- **Δ_F (Pullback)**: Brings data from D to C; simple precomposition with F.
- **Σ_F (Left Pushforward)**: Migrates data from C to D summing/unioning structures (UNION or generalization).
- **Π_F (Right Pushforward)**: Migrates data from C to D via products (JOIN or MATCH).

### Gluing

Combination of partial models via colimits (pushouts) in C-Sets category, guaranteeing correct reference fusion.

## DIK Framework

### Data

Not passive static values, but funtores.

**Definition**: Database instance conforming to schema.

**Categorical Modeling**: Instance of database via C-Set objects and morfismos.

### Information

Defines valid shape of data; schema is first-class mathematical object.

**Definition**: Formal specification of data structure and algebraic constraints.

**Categorical Modeling**: Via GAT, schema presentation; syntax/semantics separation. Allows multiple implementations (in-memory, SQL, graphs) by changing target category or funtor implementation.

### Knowledge

Capacity to transform and reason about data preserving structure.

**Definition**: Functorial operations translating data between different schemas and combining datasets.

**Categorical Modeling**: Given funtor F: C → D induces three adjoined operations on C-Sets (Δ_F, Σ_F, Π_F). Gluing constructions.

### Modeling

Explicit and executable workflow (Catlab.jl): define domain (presentation/GAT) → generate code → manipulate generically via categorical API.

**Procedure**:
1. Define domain via GAT or category presentation (objects, morfismos).
2. Julia macros convert specification to optimized data types (structs) and indexed accessors.
3. Categorical API (limit, colimit, functor) decouples algorithm from data structure.

## Example: Catlab.jl

```
@present TheoryGraph(FreeSchema) begin
  V::Ob
  E::Ob
  src::Hom(E,V)
  tgt::Hom(E,V)
end
```

## Conclusions

Patterson et al. demonstrate categorical data structures are not theoretical curiosity but practical foundation for Technical Computing.

**Benefits**:
- **Interoperability**: C-Sets allow different domains (graphs, Petri nets, meshes) to share common language.
- **Correctness**: Data migrations mathematically guarantee structure preservation, eliminating entire classes of ETL errors.
- **Efficiency**: Code generation allows high-level abstractions to compete in performance with manual implementations.

**Significance**: Fundamental for building systems where Action (Fukada) and Structure (Patterson) coexist rigorously.
