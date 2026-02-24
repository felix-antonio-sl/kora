---
_manifest:
  urn: "urn:fxsl:kb:data-access-layers"
  provenance:
    created_by: "FS"
    created_at: "2025-12-08"
version: "2.0.0"
status: published
tags: [category-theory, data-access, architecture, dal, storage-models]
lang: en
---

# Data Access Layers via Category Theory

## Storage Patterns

| Pattern | Definition | Use |
|---------|-----------|-----|
| SQL Limits | Relational = limits (product, pullback, equalizer) | Integrity, JOINs, ACID |
| NoSQL Colimits | NoSQL = colimits (coproduct, pushout) | Flexible schema, polyglot |
| Mixed Lens | SQL(write) ↔ Doc(read) asymmetric lens | Hybrid architectures |

## APIs as Functors

| API Type | Functor | Check |
|----------|---------|-------|
| REST | Domain → ResourceCat | F(id)=id, F(g∘f)=F(g)∘F(f) |
| GraphQL | Domain → TypeCat | Pullback dynamic |
| gRPC | Domain → ProtoCat | Streaming, microservices |
| Streams | Coalgebra | Action = pk |

## Repository Structure

**Coalgebra**: c: X → F(X)

**Bisimulation**: R₁~R₂ ⟺ ∀ops. observe(R₁(ops)) = observe(R₂(ops))

## ORM as Adjunction

**Structure**: Adjunction ORM ⊣ Reflect: DomainCat ⇆ SchemaCat

- **Unit**: η: E → Reflect(ORM(E)) ≈ id
- **Counit**: ε: ORM(Reflect(T)) → T ≈ id
- **Drift**: Violation of η/ε = drift

## DataLake Construction

**Construction**: colim(Dataset_i, Pipeline_ij)

**Grothendieck**: ∫F, I=zones, F(z)=schema_z

**Audit**: Pipelines = morfismos; diagram conmuta

## Synthesis

**2-Category**: Objects = components, 1-morphisms = transformations, 2-morphisms = migrations

**Audit Dimensions**: Storage-Model Align, API-Functor Preserve, Repo-Bisim, ORM-Adj Valid, Pipeline-Commute
