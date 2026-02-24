---
_manifest:
  urn: urn:fxsl:kb:audit-patterns
  provenance:
    created_by: FS
    created_at: '2025-12-05'
    source: Category Theory / DIK Auditing & Diagnostics
version: 2.0.0
status: published
tags:
- category-theory
- audit
- dik-framework
- pattern-detection
- consistency
- fxsl
lang: en
---

# Categorical Audit Patterns

## DIK Classification of Artifacts

### Data Level

- **Definition**: Instance I: S → Set over schema S.

- Concrete values, rows, records, observations.
- Funtor mapping sets to objects and functions to morfismos.

- **Audit Focus**: Referential integrity, completeness, consistency with schema.

- **Example**: SQL table with data, JSON document, CSV file.

### Information Level

- **Definition**: Schema S (finitely presented category).

- Objects = entities/types, Morfismos = relations/attributes.
- Path equations = business constraints.

- **Audit Focus**: Structural coherence, commutativity, completeness of relations.

- **Example**: DDL SQL, JSON Schema, GraphQL Schema, .koda.yml.

### Knowledge Level

- **Definition**: Transformations, migrations, abstract models (funtores between categories, adjunctions, Kan extensions).

- **Characteristics**: Behaviors (coálgebras), inference rules, processes.

- **Audit Focus**: Functoriality, structure preservation, validity of adjunctions, complete processes.

- **Example**: Migration funtor F: S → T, agent specification, .koda.yml with processes.

## Audit Dimensions

### Structural

- Verify artifact forms valid categorical structure.


- **Checks**:

- **Identity**: Each object has identity morfismo.
- **Composition**: Morfismos compose correctly.
- **Associativity**: (h∘g)∘f = h∘(g∘f).
- **Path Equality**: Parallel declared paths commute.

- **Severity if Fail**: CRITICAL.

### Referential

- Verify integrity of internal and external references.


- **Checks**:

- **Internal Refs**: Ref: point to existing IDs in same document.
- **External Refs**: XRef: point to resolvable URNs.
- **Foreign Keys**: Instance foreign keys point to existing records.

- **Severity if Fail**: HIGH.

### Completeness

- Verify artifact is complete per its DIK level.


- **Checks**:

- **Data**: Instance I defined for all objects in schema.
- **Information**: Schema has objects, morfismos, equations explicit.
- **Knowledge**: Key concepts have operative processes.

- **Severity if Fail**: MEDIUM.

### Quality

- Evaluate advanced categorical quality.


- **Checks**:

- **Universal Constructions**: Use limits/colimits where applicable.
- **Functoriality**: Transformations preserve structure.
- **Behavioral Equivalence**: Equivalent states identified (bisimulation).

- **Severity if Fail**: LOW.

### Migration

- Verify migrations as functorial squares.


- **Checks**:

- **Funtor Validity**: F: S→T preserves identities and composition.
- **Square Commutativity**: Migration square commutes naturally.
- **Constraint Preservation**: Migration preserves required constraints.

- **Severity if Fail**: HIGH.

### Behavioral

- Audit dynamic behavior via coálgebras.


- **Checks**:

- **Interface Conformance**: System implements declared interface funtor.
- **Bisimulation**: Declared equivalent components are bisimilar.
- **Action Index**: Episodes have action as primary key.

- **Severity if Fail**: MEDIUM/LOW.

## Improvement Patterns

- **Broken Diagram**: Parallel paths don't commute → Add path equation or correct morfismos.
- **Orphan Object**: Object without morfismos (except identity) → Connect or eliminate.
- **Dangling Reference**: Ref/XRef points to inexistent → Correct or create target.
- **Missing Process**: Concept without operative procedure → Add process with executable steps.
- **Version Mismatch**: Version ≠ URN version → Align versions.
- **Ad-hoc Construction**: Ad-hoc where universal exists → Use corresponding limit/colimit.
- **Non-functorial Migration**: Migration doesn't preserve composition → Redefine as valid funtor or use Σ/Δ/Π.
- **Redundant Bisimilar**: Bisimilar components treated as distinct → Identify via morphism to final coalgebra.

## Full Audit Procedure

1. **DIK Classification**: Determine level (DATA | INFORMATION | KNOWLEDGE); identify type.
2. **Structural Audit**: Execute checks for identity, composition, associativity, path equality. Register CRITICAL issues.
3. **Referential Audit**: Execute ref validity, XRef resolution, foreign-key checks. Register HIGH issues.
4. **Completeness Audit**: Per DIK level, verify completeness. Register MEDIUM issues.
5. **Quality Audit**: Check universal constructions, functoriality, behavioral equivalence. Register LOW issues.
6. **Migrations**: Verify funtor validity, square commutativity, constraint preservation.
7. **Behavioral**: Verify interface conformance, bisimulation, action indexing.
8. **Report Generation**: Consolidate by severity, associate improvement patterns, propose solutions with categorical justification.
