---
_manifest:
  urn: urn:fxsl:kb:mathematical-modelling
  provenance:
    created_by: FS
    created_at: '2025-12-05'
    source: Mathematical Modelling by Help of Category Theory
version: 2.0.0
status: published
tags:
- category-theory
- mathematical-models
- complexity
- convertibility
- coupled-models
- fxsl
lang: en
---

# Mathematical Modelling via Category Theory

## Overview

- Develops category-theoretic framework for organizing families of mathematical models by complexity.
- Models objects; refinement relations morfismos.


## Core Concepts

### Category of Models

- Objects = finite non-empty sets of assumptions (natural language).


- Morfismos = relations between assumption sets.


- Each set mapped to model formulation
- all objects related to same physical dimension.


### Complexity Order

- Model A higher complexity than B iff Set_A ⊂ Set_B but Set_B ⊄ Set_A.


- Equal complexity iff Set_A = Set_B.


### Partial Order

- Models ordered by assumption inclusion
- defines poset structure.


### Convertible Models

- Two formulations B_1, B_2 for same assumptions Set_A are convertible if natural transformation links functors F, G: Set_A → B_1, B_2.

- **Property**: Convertible models have same complexity.

## Coupled Models

- Models (i,j) formed from assumptions Set_i and Set_j plus coupling conditions.


- **Category ModCoup_{i,j}**: Objects = finite assumption sets; morphisms = relations; coupling conditions non-empty.

- **Use**: Model hierarchical phenomena (thermal-elasticity, fluid-structure interaction).

### Complexity Variants

- **Base Complexity**: Compare assumption sets.
- **Coupling Complexity**: Compare coupling condition sets.
- **Total Complexity**: Compare both.

### Refinement

- Left/right base complexity refines base comparison by component.


## Universal Arrows & Completeness

- **Completeness**: Set_A complete w.r.t. phenomenon Set'_A iff Set_A ⊂ Set'_A; write Set_A | Set'_A.

- **Reducible**: Simpler object exists still complete.

- **Extendable**: More complex object still complete.

- **Minimal/Maximal**: Irreducible/not-extendable complete models.

## Automatically Generated Models

- **Algorithm**: From set X of all possible assumptions, select subsets S via type-checked derivation.

- **Type System**: Signals (time/space → typed value); differential operators (∂/∂xi); equations composed via higher-level notation with type-checking.

- **Outcome**: Automatically consistent model equations if type-check succeeds.

## Lattice of Models

- Partial orders capture expansions (add assumptions) or analogies (reformulate)
- different interpretations give different lattices.


## Conclusions

- Mathematical model M = triple (assumptions Set, formulation, mapping Set → formulation).
- Rigor distinguishes models; complexity orders enable efficient search through solution space.
- Category theory provides formal foundation for automatic model generation and comparison.

