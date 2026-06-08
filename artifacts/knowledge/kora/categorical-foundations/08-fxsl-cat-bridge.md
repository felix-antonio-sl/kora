---
_manifest:
  urn: urn:kora:kb:cat-fxsl-bridge
  provenance:
    created_by: FS
    created_at: '2026-03-08'
    source: Bridge from legacy FXSL categorical knowledge into the official KORA formal
      layer
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
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:cat-fxsl-bridge
relations:
  depends:
    - "urn:kora:kb:cat-foundations"
    - "urn:kora:kb:cat-skill-algebra"
    - "urn:kora:kb:cat-ecosystem-2cat"
    - "urn:kora:kb:cat-discovery-presheaf"
    - "urn:kora:kb:cat-audit-invariants"
    - "urn:kora:kb:cat-behavioral-preservation"
---

# Bridge from FXSL/Cat to the KORA Formal Layer

## Purpose

This document records how the retired FXSL categorical root-note corpus was absorbed into the official KORA formal layer. It is the canonical bridge that explains which concepts were promoted, where they now live, and how they should be cited from KORA documents.

## 1. Bridge Rule

**Rule.** When a concept from the retired FXSL/Cat root notes exists in the KORA formal layer, KORA documents should cite the KORA formal-layer document for canonical formal traceability.

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

The retired FXSL/Cat root-note corpus remains:
- absorbed as source provenance for documents 00-08
- non-canonical for KORA traceability
- absent from the productive catalog after retirement

## 5. Migration Guidance

When bridging a legacy concept:
1. preserve the concept name if it already has stable external meaning
2. normalize anchors so URN fragments resolve
3. rewrite stale file-system and catalog references to the current KORA layout
4. prefer KORA URNs over path-based assumptions

## 6. Result

The practical consequence of this bridge is simple: the retired FXSL/Cat root notes no longer participate in the productive catalog, and the official mathematical backbone for KORA now extends through documents 00-09, with 06 and 07 carrying the promoted audit and behavioral machinery, and 09 carrying the order-theoretic foundation of the PMI×LFS harness space (see §7).

## 7. Partial Absorption of the Living ICAS Corpus

The retired root notes (§§2-6) are distinct from the **living auxiliary** ICAS corpus `artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/` (`urn:fxsl:kb:icas-agencia`, `urn:fxsl:kb:icas-efectos`, `urn:fxsl:kb:icas-interaccion`, `urn:fxsl:kb:icas-escala`). That corpus was **not** retired; it remains present as auxiliary, non-canonical material. It is the conceptual source on which `harness-spec` founds the PMI×LFS ontological space.

Until 2026-06-08 that foundation had **no** preimage in the official formal layer: `harness-spec` cited the ICAS corpus directly (via `relations.cites`), so the constitution-level ontology rested formally on non-normative auxiliary material (audit 2026-06-07, eje 7). Document 09 closes the order-theoretic part of that gap:

| ICAS source | Canonical KORA target | Promoted content | Not promoted |
|---|---|---|---|
| icas-agencia, icas-efectos, icas-interaccion, icas-escala (living auxiliary, founds PMI×LFS) | [09-harness-lattice](urn:kora:kb:cat-harness-lattice) | PMI×LFS as a bounded product lattice; the 5 inter-axis laws as a bounded sublattice `W` (the `vector-laws` contract) | the bridge from the harness lattice to the agent F-coalgebra — recorded in 09 §5 as an **open problem**, not a demonstrated morphism |

The absorption is therefore **partial and honest**: the lattice structure is now a formal-layer theorem; the coalgebraic bridge is explicitly deferred. Per the citation strategy of §3, KORA documents needing the order-theoretic foundation of PMI×LFS should cite 09; the ICAS notes remain valid only as background `Rationale`, never as formal `Traces to`.
