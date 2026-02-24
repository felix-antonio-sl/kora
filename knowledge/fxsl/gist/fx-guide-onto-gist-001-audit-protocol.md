---
urn: urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol
version: 1.0.0
status: published
tags: [ontology, audit, gist, sparql, owl, shacl, governance]
lang: es
---

# Protocolo de Auditoría Ontológica 360° (Gist)

## Overview

End-to-end ontology audit framework with 4 quadrants (pragmatic, structural, semantic, syntactic). Calibrates severity by maturity level (L1-L4). Produces checklist, evidence (SPARQL/OWL/SHACL), and actionable reports.

## Maturity Matrix

| Level | Name | Description |
|-------|------|-------------|
| **L1** | Prototype | Initial exploration, high tolerance for inconsistencies |
| **L2** | Development | Model under construction, requires basic consistency |
| **L3** | Production | Operational model, requires strict conformance |
| **L4** | Federated | Published for external integration, maximum rigor |

## Quadrant 1: Pragmatic

**Focus**: Purpose, scope, governance, audience.

### Competency Questions (CQs) and Functional Requirements

| ID | Criterion | Weight | L1 | L2 | L3 | L4 |
|----|-----------|--------|----|----|----|----|
| P1.1 | CQs documented | High | ○ | ● | ● | ● |
| P1.2 | CQs translatable to SPARQL | High | ○ | ○ | ● | ● |
| P1.3 | CQ coverage vs. classes/properties | Medium | ○ | ○ | ● | ● |
| P1.4 | Traceability CQ ↔ Stakeholder | Low | ○ | ○ | ○ | ● |

**Key Questions**:
- Do documented competency questions exist?
- Can each CQ be written as SPARQL query?
- Is every class/property justified by at least one CQ?
- Are there gaps (CQs the model cannot answer)?

**Anti-Patterns**:

| Pattern | Symptom | Impact |
|---------|---------|--------|
| CQ-less Ontology | No documented CQs | Impossible to validate utility |
| Orphan Concepts | Classes not in any CQ | Unnecessary complexity |
| Scope Creep | CQs exceeding domain | Unmanageable model |

**Technique**: Detect unused classes/properties

```sparql
SELECT ?class (COUNT(?s) AS ?instances) (COUNT(?usage) AS ?usages)
WHERE {
  ?class a owl:Class .
  OPTIONAL { ?s a ?class }
  OPTIONAL { ?usage ?p ?class }
}
GROUP BY ?class
HAVING (COUNT(?s) = 0 && COUNT(?usage) = 0)
# Classes without instances/usage = candidates for elimination
```

### Scope and Minimalism Alignment

| ID | Criterion | Description |
|----|-----------|-------------|
| P2.1 | Class/CQ Ratio | Ideally ≤ 3 classes per covered CQ |
| P2.2 | Reuse Index | % of reused properties vs. ad-hoc |
| P2.3 | Axiom Density | Axioms per class (ideal L3: 2-5) |

**Key Questions**:
- Can any class be eliminated without losing CQ coverage?
- Is detail level appropriate? (neither excessive nor insufficient)
- Are domain boundaries clear? What explicitly NOT modeled?

**Checklist**:
- Scope Statement documented (max 3 paragraphs)
- Explicit Out-of-Scope list
- Version and effective date
- Change Request process defined
- Governance owner identified

### Audience and Human Usability

| ID | Criterion | Verification |
|----|-----------|--------------|
| P3.1 | Label Readability | rdfs:label in natural language, no camelCase |
| P3.2 | Definition Completeness | 100% of classes have skos:definition or rdfs:comment |
| P3.3 | Examples | Complex classes have skos:example |
| P3.4 | Multilingualism | Labels in required languages with @lang tags |

**Anti-Patterns**:

| Pattern | Example | Correction |
|---------|---------|------------|
| CamelCase Labels | "hasEmploymentRelation" | "tiene relación de empleo"@es |
| Definition-less | Class without rdfs:comment | Add 1-2 sentence definition |
| Jargon Overload | "RDF reification pattern" | "Representa relación con múltiples participantes" |

### Governance and Lifecycle

| ID | Criterion | Question |
|----|-----------|----------|
| P4.1 | Versioning | owl:versionInfo and deprecation policy? |
| P4.2 | Provenance | Creator, date, license documented? |
| P4.3 | Change Management | Process for proposing changes? |
| P4.4 | Deprecation | How obsolete terms marked? (owl:deprecated) |

**Metadata Template (L3+)**:

```turtle
<https://example.org/ontology/domain> a owl:Ontology ;
  owl:versionInfo "1.2.0" ;
  owl:versionIRI <https://example.org/ontology/domain/1.2.0> ;
  owl:priorVersion <https://example.org/ontology/domain/1.1.0> ;
  dc:title "Domain Ontology"@en ;
  dc:creator "Knowledge Team" ;
  dc:created "2025-01-15"^^xsd:date ;
  dc:modified "2026-01-23"^^xsd:date ;
  dc:license <https://creativecommons.org/licenses/by/4.0/> ;
  rdfs:comment "Ontología para modelar..."@es .
```

**Trade-off**: Perfect logic can degrade pragmatic utility if too complex. Prioritize operable clarity; if Gist pattern simple solves problem, avoid complex OWL.

## Quadrant 2: Structural

**Focus**: Taxonomy, architecture, properties, namespaces, patterns, reuse.

### Taxonomic Hygiene

#### Class Hierarchy Analysis

| ID | Verification | Method |
|----|--------------|--------|
| S1.1 | Cycles in subClassOf | SPARQL query or reasoner |
| S1.2 | Maximum depth | Count levels (recommended: ≤ 7) |
| S1.3 | Average breadth | Direct subclasses per class (recommended: 3-7) |
| S1.4 | Orphan classes | Classes without superclass (except owl:Thing) |
| S1.5 | Multiple inheritance | Detect and validate if intentional |

**Multiple Inheritance Detection**:

```sparql
SELECT ?class (COUNT(?parent) AS ?parentCount)
WHERE {
  ?class rdfs:subClassOf ?parent .
  FILTER(?parent != owl:Thing)
}
GROUP BY ?class
HAVING (COUNT(?parent) > 1)
```

#### Class vs. Instance vs. Category

| Pattern | Use When | Example | Anti-pattern |
|---------|----------|---------|--------------|
| owl:Class | Types with formal axioms, stable | ex:Employee rdfs:subClassOf gist:Person | Class per variant |
| Instance | Specific individuals | ex:_Person_JuanPerez a gist:Person | ex:JuanPerez a owl:Class |
| gist:Category | Flexible taxonomies, no axioms | ex:_EmployeeType_Permanent a gist:Category | Class for admin types |

**Key Questions**:
- Classes that should be instances? (e.g., `ChileCountry` as class)
- Instances that should be classes? (master data modeling error)
- Using `gist:Category` for user-managed taxonomies?

### Property Hygiene

#### Object Properties

| ID | Verification | Criterion |
|----|--------------|-----------|
| S2.1 | Inverse declared | All navigable properties have inverse? |
| S2.2 | Domain/Range | Declared but not overly restrictive? |
| S2.3 | Characteristics | Functional, transitive, symmetric correctly applied? |
| S2.4 | Naming consistency | Verbs for object properties (hasX, isXOf)? |

**Properties Without Inverse**:

```sparql
SELECT ?prop WHERE {
  ?prop a owl:ObjectProperty .
  FILTER NOT EXISTS { ?prop owl:inverseOf ?inv }
  FILTER NOT EXISTS { ?inv owl:inverseOf ?prop }
}
```

#### Datatype Properties

| ID | Verification | Criterion |
|----|--------------|-----------|
| S2.5 | Explicit datatype | rdfs:range with xsd: datatype? |
| S2.6 | Measured values | Measurables use gist:Magnitude pattern? |
| S2.7 | Dates | Using xsd:date, xsd:dateTime consistently? |

**Anti-Patterns**:

| Pattern | Example | Correction |
|---------|---------|------------|
| Stringly-typed | ex:employeeId "12345" | Use xsd:integer or IRI |
| Direct Measurement | ex:weight "75.5" | gist:Magnitude with UoM |
| Embedded Semantics | billingAddress, shippingAddress separate | gist:Address + gist:AddressUsageType |

### Namespace and IRI Hygiene

| ID | Criterion | Verification |
|----|-----------|--------------|
| S3.1 | No squatting | Don't define in gist:, foaf:, schema:? |
| S3.2 | Consistent prefixes | One prefix per namespace throughout? |
| S3.3 | Dereferenceable | IRIs resolve to documentation or opaque? |
| S3.4 | IRI pattern | Consistent for classes, properties, instances? |

**Recommended IRI Patterns**:

```
https://org.example/ontology/domain/              # TBox
https://org.example/data/domain/                  # ABox
https://org.example/data/domain/_Person_abc123   # Instance (_prefix)
https://org.example/refdata/Country_CL            # Reference data
```

### Modeling Patterns and Reuse

#### Gist Pattern Evaluation

| Pattern | When | Verify |
|---------|------|--------|
| TemporalRelation | Relations with temporal context | Employment, membership, ownership as relations? |
| Magnitude + UoM | Measurable values | Weight, price, distance using pattern? |
| Category | Flexible taxonomies | Admin types as categories? |
| Address | Physical/electronic addresses | Using containedText + refersTo? |
| Agreement/Commitment | Contracts, obligations | Structure for parties and terms? |

#### Reuse Metrics

```sparql
SELECT
  (COUNT(DISTINCT ?imported) AS ?importedProps)
  (COUNT(DISTINCT ?custom) AS ?customProps)
  (COUNT(DISTINCT ?imported) * 100.0 /
   (COUNT(DISTINCT ?imported) + COUNT(DISTINCT ?custom)) AS ?reusePercent)
WHERE {
  { ?imported a owl:ObjectProperty . FILTER(STRSTARTS(STR(?imported), "https://w3id.org/semanticarts/")) }
  UNION
  { ?custom a owl:ObjectProperty . FILTER(!STRSTARTS(STR(?custom), "https://w3id.org/semanticarts/")) }
}
# Goal L3+: reusePercent >= 40%
```

## Quadrant 3: Semantic

**Focus**: Logic, inference, constraints, identity, OWL profiles.

### Logical Consistency

| Tool | Profile | Use |
|------|---------|-----|
| HermiT | OWL 2 DL | Consistency, classification |
| Pellet | OWL 2 DL | Consistency, explanations |
| ELK | OWL 2 EL | High performance, large ontologies |
| RDFox | OWL 2 RL | Materialization, queries |

**Checklist**:
- Loads without errors in Protégé
- Reasoner runs < 60s (L3)
- No unsatisfiable classes
- No inconsistencies detected
- Spot-check inferences as expected

**Unsatisfiable Classes** (equivalent to owl:Nothing):

```sparql
SELECT ?class WHERE {
  ?class owl:equivalentClass owl:Nothing .
}
```

**Common Causes**:
- Contradictory restrictions (min 1 AND max 0)
- Disjointness with superclass
- Incompatible ranges in property chain

### Constraint Rigor

#### Domain/Range Guidance

| Scenario | Recommendation |
|----------|-----------------|
| General property | Don't declare domain/range (inherit from superclass) |
| Specific property | Domain/Range on most general applicable class |
| Multiple domains | Use owl:unionOf or don't declare |

**Anti-Pattern (Over-constrained)**:

```turtle
# ❌ Too restrictive
ex:hasPet rdfs:domain ex:Person ;
          rdfs:range ex:Dog .
# Problem: Can't have cats

# ✅ Flexible
ex:hasPet rdfs:domain ex:Person ;
          rdfs:range ex:Animal .
```

#### Disjointness

| ID | Verification | Impact |
|----|--------------|--------|
| L1.1 | Explicit disjointness | Sister classes disjoint? |
| L1.2 | Covering axioms | Union of subclasses = superclass? |
| L1.3 | Completeness | Model uses CWA or OWA appropriately? |

**Pattern**:

```turtle
ex:Employee rdfs:subClassOf ex:Person .
ex:Customer rdfs:subClassOf ex:Person .
ex:Employee owl:disjointWith ex:Customer .

# Or using DisjointUnion (OWL 2)
ex:Person owl:disjointUnionOf (ex:Employee ex:Customer ex:Prospect) .
```

### Identity Management

| Feature | Use | Verify |
|---------|-----|--------|
| owl:FunctionalProperty | Unique value per subject | hasBirthDate functional? |
| owl:InverseFunctionalProperty | Uniquely identifies | hasSSN is IFP? |
| owl:hasKey | Composite key | Classes have keys defined? |

**Anti-Pattern (String Linking)**:

```turtle
# ❌ String link
ex:_Order_123 ex:customerName "Acme Corp" .
ex:_Invoice_456 ex:customerName "Acme Corp" .
# No semantic link, typos break integrity

# ✅ IRI link
ex:_Order_123 ex:hasCustomer ex:_Organization_AcmeCorp .
ex:_Invoice_456 ex:hasCustomer ex:_Organization_AcmeCorp .
```

### OWL Profiles and Computational Complexity

| Profile | Complexity | Use | Verify |
|---------|-----------|-----|--------|
| OWL 2 Full | Undecidable | Avoid | N/A |
| OWL 2 DL | 2-NEXPTIME | Medium ontologies | Default |
| OWL 2 EL | PTIME | Large (SNOMED) | No negation, unions |
| OWL 2 QL | AC0 | Query answering | No complex existentials |
| OWL 2 RL | PTIME | Inference rules | No existentials in head |

**Verification**: Check Protégé → Ontology > Metrics > OWL Profile.

## Quadrant 4: Syntactic

**Focus**: Artifact quality: parsing, style, annotations, modularity, tests, CI.

### Syntactic Validation

#### Parse and Serialization

| Verification | Tool | Command |
|--------------|------|---------|
| Turtle valid | rapper | rapper -i turtle -c ontology.ttl |
| RDF/XML valid | xmllint + rapper | Validate XML + RDF |
| Prefixes declared | Parser | No unknown prefix warnings |
| Valid IRIs | Parser | No illegal characters |

#### Style Checklist

- Consistent indentation (2 spaces)
- Subject-ordered, then predicate-ordered
- Blank lines between entities
- Turtle comments for sections (#=== CLASSES ===)
- Prefixes alphabetically sorted
- One file per module (large ontologies)

### Annotations and Documentation

| Annotation | L1 | L2 | L3 | L4 |
|-----------|----|----|----|----|
| rdfs:label | ● | ● | ● | ● |
| rdfs:comment | ○ | ● | ● | ● |
| skos:definition | ○ | ○ | ● | ● |
| skos:example | ○ | ○ | ○ | ● |
| skos:scopeNote | ○ | ○ | ○ | ● |
| dc:source | ○ | ○ | ○ | ● |

**Completeness Query**:

```sparql
SELECT ?entity
  (BOUND(?label) AS ?hasLabel)
  (BOUND(?comment) AS ?hasComment)
  (BOUND(?definition) AS ?hasDefinition)
WHERE {
  { ?entity a owl:Class } UNION { ?entity a owl:ObjectProperty } UNION { ?entity a owl:DatatypeProperty }
  OPTIONAL { ?entity rdfs:label ?label }
  OPTIONAL { ?entity rdfs:comment ?comment }
  OPTIONAL { ?entity skos:definition ?definition }
}
HAVING (!BOUND(?label) || !BOUND(?comment))
```

### Modularity and Dependencies

| ID | Criterion | Verification |
|----|-----------|--------------|
| M1 | TBox/ABox separation | Ontology separate from instances? |
| M2 | Modules by domain | Subdomains in separate files? |
| M3 | Explicit imports | owl:imports for dependencies? |
| M4 | Versioned imports | Versioned IRIs for critical imports? |

**Pattern**:

```
ontology/
├── core.ttl                    # Core classes/properties
├── extensions/
│   ├── temporal.ttl            # Temporal extensions
│   └── spatial.ttl             # Spatial extensions
├── reference-data/
│   ├── countries.ttl           # Reference data
│   └── currencies.ttl
└── bundle.ttl                  # Imports all modules
```

### Testing and Automated Validation

#### SHACL Shapes Example

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix ex: <https://example.org/ns/> .

ex:PersonShape a sh:NodeShape ;
  sh:targetClass ex:Person ;
  sh:property [
    sh:path ex:hasName ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:string ;
    sh:message "Persona debe tener exactamente un nombre"@es
  ] ;
  sh:property [
    sh:path ex:hasBirthDate ;
    sh:maxCount 1 ;
    sh:datatype xsd:date ;
    sh:lessThan ex:hasDeathDate ;
    sh:message "Nacimiento anterior a muerte"@es
  ] .
```

#### CI/CD Pipeline Example

```yaml
ontology-validation:
  steps:
    - name: Syntax Check
      run: rapper -i turtle -c *.ttl

    - name: Consistency Check
      run: java -jar HermiT.jar -c ontology.ttl

    - name: SHACL Validation
      run: shacl validate -s shapes.ttl -d data.ttl

    - name: Metrics Report
      run: python ontology_metrics.py > report.md
```

## Consolidated Audit Checklist

### Phase 1: Preparation

- [ ] Identify maturity objective (L1-L4)
- [ ] Obtain CQ and scope documentation
- [ ] Identify stakeholders and audience
- [ ] Set up environment (Protégé, reasoner, SHACL processor)

### Phase 2: Pragmatic Audit (Q1)

- [ ] Verify CQ existence and quality
- [ ] Validate CQ ↔ Model coverage
- [ ] Evaluate minimalism and scope
- [ ] Review label/definition readability
- [ ] Verify governance metadata

### Phase 3: Structural Audit (Q2)

- [ ] Analyze class hierarchy (cycles, depth, breadth)
- [ ] Validate Class/Instance/Category distinction
- [ ] Review properties (inverses, characteristics)
- [ ] Verify namespace hygiene
- [ ] Evaluate standard pattern reuse

### Phase 4: Semantic Audit (Q3)

- [ ] Run reasoner (consistency)
- [ ] Check for unsatisfiable classes
- [ ] Analyze domain/range constraints
- [ ] Validate disjointness
- [ ] Review identity handling
- [ ] Confirm OWL profile

### Phase 5: Syntactic Audit (Q4)

- [ ] Validate parsing (no errors)
- [ ] Verify style and format
- [ ] Evaluate annotation completeness
- [ ] Review modularity
- [ ] Verify imports/dependencies
- [ ] Check test coverage (SHACL)

### Phase 6: Report and Recommendations

- [ ] Classify findings by severity (Critical/Major/Minor/Info)
- [ ] Provide correction examples
- [ ] Prioritize corrective actions
- [ ] Document design trade-offs
- [ ] Generate comparative metrics

## Audit Report Template

```markdown
# Ontology Audit Report

**Ontology**: [Name]
**Version**: [X.Y.Z]
**Date**: [YYYY-MM-DD]
**Auditor**: [Name/Agent]
**Target Level**: [L1-L4]

## Executive Summary

| Quadrant | Score | Status |
|----------|-------|--------|
| Pragmatic | X/10 | RED/YELLOW/GREEN |
| Structural | X/10 | RED/YELLOW/GREEN |
| Semantic | X/10 | RED/YELLOW/GREEN |
| Syntactic | X/10 | RED/YELLOW/GREEN |
| **Total** | **X/40** | |

## Critical Findings

1. [Finding with impact and correction]

## Major Findings

1. [Finding with impact and correction]

## Minor Findings

1. [Finding with impact and correction]

## Metrics

- Total Classes: X
- Total Properties: X (Object: Y, Datatype: Z)
- Total Instances: X
- Reuse Index: X%
- Axiom Density: X axioms/class
- Annotation Coverage: X%

## Prioritized Recommendations

1. [Action] - Urgency: High/Medium/Low
```
