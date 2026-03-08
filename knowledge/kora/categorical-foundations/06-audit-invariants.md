---
_manifest:
  urn: urn:kora:kb:cat-audit-invariants
  provenance:
    created_by: FS
    created_at: '2026-03-08'
    source: "FXSL categorical audit corpus (audit-patterns, constraint-logic, kb-category, schema-evolution) consolidated into the KORA formal layer"
version: 1.0.0
status: published
tags:
- category-theory
- audit
- invariants
- constraints
- provenance
- formal-layer
- kora
lang: en
---

# Audit Invariants for the KORA Knowledge Layer

## Purpose

This document formalizes the invariants that make a KORA knowledge corpus auditable. It absorbs the most reusable audit machinery from the FXSL categorical corpus and makes it part of the official KORA formal layer.

## Prerequisites

All notation from [00-foundations](urn:kora:kb:cat-foundations). The agent and skill structures from [01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra) and [02-skill-algebra](urn:kora:kb:cat-skill-algebra). The governance lattice from [05-governance-lattice](urn:kora:kb:cat-governance-lattice).

## 1. Audit Space

### 1.1 Artifact Stratification

**Definition.** Every auditable KORA artifact belongs to one of three categorical strata:

| Stratum | Formal shape | Typical KORA examples |
|---------|--------------|-----------------------|
| Data | Instance functor I: S → Set | tabular data, materialized registries, concrete logs |
| Information | Finitely presented category S | schemas, frontmatter grammars, workspace topology |
| Knowledge | Functor, adjunction, coalgebra, or proof object | specs, migrations, behavioral claims, audit procedures |

### 1.2 Audit Object

**Definition.** An audit is a predicate-valued functor:

```
Audit: Artifact → Pos
```

that sends an artifact to the partially ordered set of findings ordered by severity:

```
OK < LOW < MEDIUM < HIGH < CRITICAL
```

## 2. Core Invariants

### 2.1 Structural Invariants

**Invariant S1 (Identity).** Every declared object has an identity morphism.

**Invariant S2 (Composition).** If f: A → B and g: B → C are declared, then g ∘ f is well-typed and inherits the declared semantics.

**Invariant S3 (Path Equality).** Every declared parallel path equality is satisfied by every admitted instance.

### 2.2 Referential Invariants

**Invariant R1 (Internal Resolution).** Every internal reference resolves to an object, heading, or component present in the target artifact.

**Invariant R2 (External Resolution).** Every URN or routed external reference resolves to an indexed artifact in the knowledge graph.

**Invariant R3 (Fragment Resolution).** If a reference includes a fragment, that fragment resolves to a stable anchor in the target artifact.

### 2.3 Completeness Invariants

**Invariant C1 (Schema Completeness).** A schema-level artifact declares all required objects, morphisms, and constraints for its domain.

**Invariant C2 (Procedure Completeness).** A knowledge-level artifact that promises an executable or auditable process exposes the full procedure needed to run that process.

**Invariant C3 (Topology Completeness).** A composite artifact exposes all mandatory components of its governing topology.

### 2.4 Preservation Invariants

**Invariant P1 (Constraint Preservation).** A migration F: S → T is acceptable only if preserved constraints and intentionally lost constraints are both explicit.

**Invariant P2 (Behavior Preservation).** A transformation between two behavioral artifacts is acceptable only if the shared interface is preserved and the induced behavior remains bisimilar or the divergence is explicitly classified.

**Invariant P3 (Provenance Preservation).** Every derived datum or claim has a recoverable provenance path to its source artifacts.

## 3. The Audit Cube

**Definition.** The canonical KORA audit factors through four orthogonal dimensions:

```
Audit = Structural × Referential × Completeness × Preservation
```

Each artifact projects into a subset of the cube:

| Artifact kind | Structural | Referential | Completeness | Preservation |
|---------------|-----------|-------------|--------------|--------------|
| Knowledge note | required | required | required | optional |
| Schema | required | required | required | required |
| Migration note | required | required | required | required |
| Behavioral model | required | required | required | required |

## 4. Constraint Logic of Audit

### 4.1 Audit Theory

**Definition.** An audit theory is a pair:

```
T_audit = (S, Σ_audit)
```

where S is the artifact schema and Σ_audit is a finite set of invariants from §2 encoded as path equalities, existence constraints, inclusion constraints, or provenance obligations.

### 4.2 Satisfaction

**Definition.** An artifact instance I satisfies the audit theory, written I ⊨ T_audit, iff all invariants in Σ_audit hold.

**Corollary.** Failed audit = witness that I ⊭ T_audit.

## 5. Canonical Procedures

### 5.1 Static Audit

For static artifacts:
1. Extract object graph, references, and constraints.
2. Verify S1-S3.
3. Verify R1-R3.
4. Verify C1-C3.
5. Emit minimal counterexamples for every failing invariant.

### 5.2 Migration Audit

For versioned artifacts:
1. Build the version category Ver.
2. Interpret each migration as a functor.
3. Verify P1 and P3 for each step and for the composite chain.
4. Classify losses as documented, admissible, or debt.

### 5.3 Behavioral Audit

For coalgebraic artifacts:
1. Extract shared interface functor F.
2. Compare observed transitions under F.
3. Verify P2 by bisimulation or explicit divergence classification.

## 6. Minimal Report Object

**Definition.** A valid KORA audit report contains:
- audited artifact identity
- governing theory or topology
- violated invariants
- concrete witnesses
- repair direction

## 7. Consequence for the Knowledge Layer

**Theorem.** A knowledge corpus is audit-stable iff all indexed artifacts satisfy R1-R3 globally and every formal bridge between descriptive and operational layers satisfies P1-P3.

*Meaning:* broken fragments, stale legacy paths, and untracked semantic migrations are not superficial editorial defects; they are violations of the categorical invariants that make the corpus computably auditable.
