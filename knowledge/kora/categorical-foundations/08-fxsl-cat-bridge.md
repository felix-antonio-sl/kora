---
_manifest:
  urn: urn:kora:kb:cat-fxsl-bridge
  provenance:
    created_by: FS
    created_at: '2026-03-08'
    source: "Bridge from legacy FXSL categorical knowledge into the official KORA formal layer"
version: 1.0.0
status: published
tags:
- category-theory
- bridge
- migration
- fxsl
- formal-layer
- kora
lang: en
---

# Bridge from FXSL/Cat to the KORA Formal Layer

## Purpose

This document records how the legacy FXSL categorical corpus is absorbed into the official KORA formal layer. It is not a replacement for the source notes in `knowledge/fxsl/cat`; it is the canonical bridge that explains which concepts were promoted, where they now live, and how they should be cited from KORA documents.

## 1. Bridge Rule

**Rule.** When a concept exists both in `knowledge/fxsl/cat` and in the KORA formal layer, KORA documents should cite the KORA formal-layer document for canonical formal traceability and the FXSL note as supporting source material.

## 2. Promoted Themes

| FXSL source cluster | Canonical KORA target | Promoted content |
|---------------------|-----------------------|------------------|
| audit-patterns, constraint-logic, kb-category, schema-evolution | [06-audit-invariants](urn:kora:kb:cat-audit-invariants) | structural, referential, completeness, migration, provenance invariants |
| coalgebras, categorical-systems-theory, action-primary-key, schema-evolution | [07-behavioral-preservation](urn:kora:kb:cat-behavioral-preservation) | coalgebraic preservation, bisimulation, wiring, action-indexed behavior |
| algebraic-databases, seven-sketches | [00-foundations](urn:kora:kb:cat-foundations), [02-skill-algebra](urn:kora:kb:cat-skill-algebra) | functoriality, adjunctions, Kan-based migration intuition |
| mbse-consistency, mathematical-modelling | [03-ecosystem-2cat](urn:kora:kb:cat-ecosystem-2cat), [06-audit-invariants](urn:kora:kb:cat-audit-invariants) | partial orders, injections, consistency witnesses |
| data-lakes-ct, unified-multimodel, unified-representation-transformation-multimodel, formal-framework-multimodel-data-transformations | [04-discovery-presheaf](urn:kora:kb:cat-discovery-presheaf), [06-audit-invariants](urn:kora:kb:cat-audit-invariants) | indexed integration, Grothendieck aggregation, migration/provenance viewpoints |

## 3. Citation Strategy

Use the following order:
1. cite the KORA formal-layer document for the theorem, invariant, or formal claim
2. cite the FXSL note only when additional background, examples, or domain-specific terminology is useful

## 4. Legacy Status

The FXSL corpus remains:
- valid as descriptive mathematical knowledge
- useful as a source of examples and legacy terminology
- non-canonical for KORA traceability once a concept has been promoted into documents 00-08

## 5. Migration Guidance

When bridging a legacy concept:
1. preserve the concept name if it already has stable external meaning
2. normalize anchors so URN fragments resolve
3. rewrite stale file-system and catalog references to the current KORA layout
4. prefer KORA URNs over path-based assumptions

## 6. Result

The practical consequence of this bridge is simple: the FXSL corpus remains searchable and reusable, but the official mathematical backbone for KORA now extends through documents 00-08, with 06 and 07 carrying the promoted audit and behavioral machinery.
