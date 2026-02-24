---
_manifest:
  urn: urn:fxsl:kb:algebraic-databases
  provenance:
    created_by: FS
    created_at: '2025-12-05'
    source: Algebraic Databases (Schultz, Spivak, Vasilakopoulou, Wisnesky)
version: 2.0.0
status: published
tags:
- category-theory
- databases
- profunctors
- proarrow-equipment
- algebraic-theories
- fxsl
lang: en
---

# Algebraic Databases

## Core Concepts

### Profunctors

- **Definition**:
- Profunctor M:
- C ⇸ D = funtor M:
- C^op × D → Set.


- Generalizes funtores; models relations between categories (queries, correspondences).
- Used to describe consultas and correspondences between database schemas.


### Bimodules

- **Definition**:
- Bimodule = profunctor estructurado in the double category Data (schemas, mappings, modules).


- **Objects**: Schemas (categories).
- **Vertical Morphisms**: Funtores (schema mappings).
- **Horizontal Morphisms**: Profunctors/modules (queries).

- Use:
- Encapsulate consultas as composable entities.


### Proarrow Equipment

- **Definition**:
- Proarrow equipment = double category organizing schemas, mappings, and profunctors.


- **Objects**: Schemas.
- **Vertical Morphisms**: Schema mappings (funtores).
- **Horizontal Morphisms**: Profunctors/Bimodules (queries).

- Use:
- Basis for query rewriting and composition of complex migraciones.


## Uber-Queries

- **Definition**:
- Uber-query = consulta expressed as composable profunctor within the equipment.


- **Properties**:

- Compositional: composes vía profunctor composition (M;N).
- Semantically precise: evaluation via Γ_M.
- Verifiable: allows algebraic proofs over the query.

- Use:
- Design pipelines of consultas over multiple schemas with formal guarantees.


## Query Evaluation

- **Gamma Evaluation**: Γ_M(I) = ∫^c M(c,−) × I(c) evaluates profunctor M over instance I.
- Applies uber-query M to concrete data I.


- **Query Composition**:
- (M;N)(a,c) = ∫^b M(a,b) × N(b,c).
- Constructs complex consultas from simple blocks algebraically.


## Theoretical Foundations

### Kan Extensions

- **Left Kan Extension (Lan_F)**: generalizes Σ_F. **Right Kan Extension (Ran_F)**: generalizes Π_F.
- Model complex schema+data transformations with universal properties.


### Kan Lift

- **Definition**:
- Inverse problem of extension; lift structures along a funtor.
- Requires fully faithful funtor to preserve semantics.
- Transformations multi-model with guarantees.


### Yoneda Embedding

- **Definition**:
- Embedding y:
- C → [C^op, Set] where y(A) = Hom(−, A).
- Property: y is fully faithful;
- C embeds in its presheaf category.
- Every object represented faithfully by its relations with other objects.


- **Procedure**:

1. Given object A in C, construct presheaf y(A) = Hom(−, A).
2. For morfismo f: A→B, y(f) is natural transformation Hom(−,A)→Hom(−,B).
3. y preserves and reflects isomorfismos: A≅B in C iff y(A)≅y(B).
4. Use to: represent schemas as presheaves, design APIs by behavior.

## Algebraic Database Schemas

- **Definition**:
- Database schema S over algebraic theory Type is a pair (S_e, S_o) where S_e is a category (entity category) and S_o:
- S_e ⇸ Type is an algebraic profunctor (observables profunctor).


## Algebraic Database Instances

- **Definition**:
- If S=(S_e,S_o) is a schema, an instance on S is a funtor I:
- S → Set whose restriction to Type is a Type-algebra.


- **Properties**:

- S-Inst is equivalent to a category of algebras for some algebraic theory.
- S-Inst has all small colimits.

## Fundamental Data Migration Functors

- Given schema mapping F:
- S → T, there are three funtores S-Inst ⇆ T-Inst:


- **Δ_F (Pullback)**: For I in T-Inst, Δ_F(I) = I ∘ F.
- **Σ_F (Left Pushforward)**: For I in S-Inst, Σ_F(I) = ∫^{s in S_e} I(s) · y(Fs).
- **Π_F (Right Pushforward)**: Δ_F has right adjoint Π_F, obtained as right Kan extension.

## Double Category Data

- **Definition**:
- Data is the double category whose objects are schemas, vertical morphisms are schema mappings, horizontal morphisms are bimodules, and 2-cells are transformations respecting the type side.


- **Composition**:
- M ⊗ N of bimodules M:
- R ⇸ S and N:
- S ⇸ T is given by M ⊗ N = Λ_N ∘ M.


- **Property**:
- Data is an equipment.

