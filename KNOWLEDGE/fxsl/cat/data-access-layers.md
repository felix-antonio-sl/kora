---
_manifest:
  urn: urn:fxsl:kb:data-access-layers
  provenance:
    created_by: FS
    created_at: '2025-12-08'
    source: legacy-import
version: 2.0.0
status: published
tags:
- category-theory
- data-access
- architecture
- dal
- storage-models
- fxsl
lang: en
---

# Data Access Layers via Category Theory

Categorical patterns for DAL: storage, APIs, repositories, ORMs, data lakes.

## Storage and API

Storage: SQL = limits (product, pullback, equalizer) → integrity, JOINs, ACID. NoSQL = colimits (coproduct, pushout) → flexible schema, polyglot. Mixed: SQL(write) ↔ Doc(read) via asymmetric lens.

APIs as functors — Domain→ResourceCat (REST), Domain→TypeCat (GraphQL, dynamic pullback), Domain→ProtoCat (gRPC, streaming). Streams: coalgebra, action = primary key. Functor check: F(id)=id; F(g∘f)=F(g)∘F(f).

## Repository, ORM, Data Lake

**Repository** = coalgebra c: X → F(X). Bisimulation: R₁ ~ R₂ iff ∀ops. observe(R₁(ops)) = observe(R₂(ops)).

**ORM** = adjunction ORM ⊣ Reflect: DomainCat ⇆ SchemaCat. Unit η: E → Reflect(ORM(E)) ≈ id; counit ε: ORM(Reflect(T)) → T ≈ id. ORM drift = violation of η or ε.

**Data Lake** = colim(Dataset_i, Pipeline_ij). Grothendieck: ∫F where I = zones, F(z) = schema_z. Objects of ∫F: pairs (zone, entity). Audit: pipelines = morphisms; diagram must commute.

## Synthesis

2-categorical model: objects = DAL components, 1-morphisms = transformations, 2-morphisms = migrations.

Audit dimensions: STORAGE-MODEL-ALIGN (SQL/NoSQL matches limit/colimit structure), API-FUNCTOR-PRESERVE (functoriality), REPO-BISIM (bisimilar under interface), ORM-ADJ-VALID (η,ε hold), PIPELINE-COMMUTE (pipeline diagram commutes).
