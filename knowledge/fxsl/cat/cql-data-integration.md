---
_manifest:
  urn: urn:fxsl:kb:cql-data-integration
  provenance:
    created_by: FS
    created_at: '2025-12-05'
    source: Categorical Data Integration for Computational Science (Brown, Spivak,
      Wisnesky, 2019)
version: 2.0.0
status: published
tags:
- category-theory
- data-integration
- cql
- scientific-data
- functorial-migration
- fxsl
lang: en
---

# CQL: Categorical Query Language

## Overview

- Open-source query and data integration scripting language for scientific data sharing.
- Addresses data misinterpretation via structure-preserving migrations and automatic provenance.


- **Key Benefit**: Static guarantee that migrated data respects constraints; functorial migrations are structure-preserving for both source and target.

## Definition

- **CQL**: Based on algebraic database formalism motivated by category theory.

- **Features**:

- Static guarantees of data integrity via rich constraint language.
- Complete provenance for all transformations.
- Seamless programming language integration into schema.

## Data Sharing Problem

- Traditional approach: researchers share data in tables/figures (unstructured).
- Challenge: data misinterpretation, lack of standards, heterogeneous formats.


- **CQL Solution**: Define schema (Olog) explicitly capturing conceptual knowledge; constraints prevent misuse; migrations are mathematically sound.

## Ologs (Ontology Logs)

- **Definition**: Like concept maps with formal interpretation.

- **Boxes**: Database tables (or sets with functions).
- **Arrows**: Foreign keys (or functions).
- **Path Equations**: When two paths yield same result (integrity constraint).

- **Conceptual Value**: Schema not mere container; conveys important semantic knowledge.

## Functorial Migration

- **Definition**: Application of Δ/Σ/Π induced by schema funtor F: S_source→S_target.

- **Guarantee**: Correctness by construction; if funtor exists, migration respects integrity.

- **Provenance**: Funtoriality preserves information about data origin; trazable through transformations.

- **Procedure**:

1. Define source schema S_source (ologs).
2. Define target schema S_target.
3. Construct funtor F: S_source → S_target.
4. CQL automatically generates Δ_F, Σ_F, Π_F.
5. Apply appropriate operator.
6. CQL guarantees correctness + automatic provenance.

## Heterogeneity Handling

- **Factors**:

- Different names for same concepts.
- Implicit constants not documented.
- Denormalization and information duplication.
- Hidden structure in string fields.
- Different granularity levels.
- Labelled nulls for distinct (but unknown) values.

- **CQL Solutions**:

- **Names**: Direct specification in mapping.
- **Constants**: Declare during migration.
- **Denormalization**: Map attributes to paths; unpack JSON via functions.
- **Hidden Structure**: Use functions to access nested fields.
- **Granularity**: Migrate low→high via NULL; high→low via ignoring excess.
- **Labelled Nulls**: Distinct (unknown) values behave like variables in functions/constraints.

## Case Study: OQMD

- Integration of Open Quantum Materials Database with Catalysis database.
- Demonstrates:

- Table correspondence via overlap analysis.
- Unit conversion and format translation functions.
- Subset filtering and record deduplication.
- Cross-database joins and enrichment.

## Conclusion

- CQL provides intuitive language for precisely specifying translation between structured data representations.
- Facilitates sharing by allowing researchers to work at their natural level of abstraction while guaranteeing structural integrity across migrations.

