---
_manifest:
  urn: "urn:fxsl:kb:sysml-foundations-diagrams"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "OPERATIONS/source/fxsl/opm-methodology/opm-libro-sysml.md"
version: "1.0.0"
status: published
tags: [sysml, uml, diagrams, systems-modeling, block-definition, activity, sequence, requirements, parametric]
lang: en
extensions:
  kora:
    family: textbook
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
    book_source: "Dori, D. (2015). Model-Based Systems Engineering with OPM and SysML. Springer."
    chapters: [4, 12]
---

# SysML Foundations and Diagrams — Systems Modeling Language Overview

## Resumen

SysML (Systems Modeling Language) is a UML 2 profile customized for systems engineering. It replaces UML's software-centric ontology with general-purpose constructs applicable to hardware, software, data, personnel, and facilities. SysML organizes system models across 9 diagram types grouped into 4 pillars: structure, behavior, requirements, and parametrics. This artifact covers UML origins, SysML development path, all 9 diagram types with key semantics, and systematic OPM-SysML comparison. For OPM formal content, see [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## UML Origins and SysML Development

### UML Foundation

- **UML** (Unified Modeling Language): standardized visual specification language for software system modeling
- Defined and maintained by OMG (Object Management Group), first adopted November 1997
- Specifies graphical notation + corresponding semantics for abstract system models
- 13 diagram types total: 6 structural, 7 behavioral
- Evolved through minor versions (1.x) and one major revision (UML 2)
- Dominant modeling language in the software industry

### UML Limitations for Systems Engineering

- Software-centric ontology limited to software artifacts
- Physical characteristics and system components poorly expressed
- Inadequate support for hierarchical decomposition within system models

### SysML Genesis

- OMG Systems Engineering Domain Special Interest Group (SE DSIG) established to adapt UML
- Supported by INCOSE and ISO AP 233 workgroup
- **UML for SE RFP** issued by OMG, March 2003
- SysML: sole response to the RFP
- Team composition: industry users, tool vendors, government agencies, professional organizations, academia
- **SysML v1.0**: formally released by OMG, September 2007 (4.5 years after RFP)
- SysML reuses a UML 2 subset + provides systems engineering extensions

## The Four Pillars of SysML

| Pillar | Diagram Types | Purpose |
|---|---|---|
| **Structure** | Block Definition Diagram (bdd), Internal Block Diagram (ibd), Package Diagram, Use Case Diagram | System composition, hierarchy, interconnections, classification |
| **Behavior** | Activity Diagram, Sequence Diagram, State Machine Diagram, Use Case Diagram | Workflow, message flow, state transitions, system usage |
| **Requirements** | Requirements Diagram | Textual requirements representation, traceability, verification |
| **Parametrics** | Parametric Diagram | Mathematical constraints between properties, engineering analysis integration |

## SysML Diagram Taxonomy

### Relationship to UML

| Category | Diagram | UML Relationship |
|---|---|---|
| Unchanged from UML | Use Case, Package, Sequence, State Machine | Adopted without modification |
| Modified from UML | Block Definition, Internal Block, Activity | Extended/adapted for SE |
| New in SysML | Requirements, Parametric | No UML counterpart |

## Use Case Diagram (uc)

**Definition**: describes system usage by actors (environment) to achieve goals realized through services.

### Key Elements

| Element | Symbol | Semantics |
|---|---|---|
| Use Case | Oval with name | Service the system provides |
| Actor | Stick figure or `<<actor>>` stereotype box | External entity interacting with the system |
| Subject | Rectangle with name at top center | System providing the service |
| Communication Path | Line between actor and use case | Interaction link |
| Diagram Frame | Outer rectangle with name tag | Required container for any SysML diagram |

### Use Case Formality Levels

- **Brief**: one-paragraph summary of main success scenario
- **Casual**: informal multi-paragraph covering various scenarios
- **Fully dressed**: all steps, variations, preconditions, success guarantees

### Diagram Frame Heading Syntax

`<diagramKind> [modelElementType] <modelElementName> [diagramName]`

- `diagramKind` (bold) and `modelElementName`: mandatory
- `modelElementType` and `diagramName`: optional, enclosed in brackets
- Each `diagramKind` has a 2-3 letter lowercase abbreviation (e.g., `uc`, `bdd`, `stm`)

### Stereotypes

A **stereotype** is an extensibility mechanism for creating new model elements. Notation: name within guillemets (`<<name>>`), recorded at top middle of rectangular box.

## Block Definition Diagram (bdd)

**Definition**: defines block features (properties, operations) and inter-block relationships (associations, generalizations, dependencies).

### Block

A **block** is SysML's basic structural element — modular component defining a feature collection describing a system part or element of interest. Analogous to UML class but general-purpose (not software-specific). Applicable at any system hierarchy level, from single components to top-level system. Can include structural and behavioral features.

### Key Elements

| Element | Symbol | Semantics |
|---|---|---|
| Block | `<<block>>` stereotype box | Modular structural component |
| Actor | Stick figure or `<<actor>>` box | External interacting entity |
| ReferenceAssociation | Line with labels + multiplicity | Association link between blocks |
| PartAssociation | Line with filled diamond (whole side) | Whole-part composition |
| Generalization | Line with hollow triangle (general side) | Inheritance/classification hierarchy |

### Structural Diagram Pair

- **BDD**: block definitions, relationships, system hierarchy, classification trees
- **IBD** (Internal Block Diagram): internal structure of a single block via properties and connectors

## State Machine Diagram (stm)

**Definition**: models discrete behavior through state transitions. Based on Harel statechart formalism (1987, 1988).

### Key Elements

| Element | Semantics |
|---|---|
| State (rountangle) | Condition of a block; can be composite (containing inner processes) |
| Transition (arrow) | State change; labeled with `trigger [guard] / activity` |
| Initial pseudo-state (filled circle) | Entry point indicator |
| Final pseudo-state (filled circle + white rim) | Exit point indicator |
| Trigger | Event causing transition |
| Guard | Boolean condition (in brackets) enabling transition |

### OPM Comparison

OPM denotes initial state via bold rountangle frame and final state via double rountangle frame, eliminating pseudo-state symbols. See [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## Activity Diagram (act)

**Definition**: represents input/output flow and control flow between actions. The only SysML behavioral diagram extended from UML 2 (others unchanged or eliminated).

### Fundamental Constructs

| Element | Symbol | Semantics |
|---|---|---|
| Action | Rountangle | Basic (usually atomic) process unit |
| Block/Object | Rectangle | Data/material flowing between actions |
| Control Flow | Arrow between actions | Sequencing without explicit object |
| Object Flow | Arrow through block node or pins | Data/material transfer between actions |
| Fork Node | Thick bar (one input, multiple outputs) | Concurrent action initiation |
| Join Node | Thick bar (multiple inputs, one output) | Synchronization barrier |
| Decision Node | Diamond | Conditional branching |
| Initial Node | Filled circle | Activity start |
| Final Node | Filled circle + white rim | Activity end |

### Special Action Nodes

| Node | Symbol | Semantics |
|---|---|---|
| Accept Event | Concave pentagon | Waits for signal occurrence |
| Send Signal | Convex pentagon | Creates and sends signal |
| Time Event | Hourglass | Waits for time moment or periodic duration |

### Action Refinement

An action with a **rake (trident) symbol** at bottom-right denotes a call action elaborated into its own activity diagram. Analogous to OPM process in-zooming.

### Swimlanes

Activity partition grouping actions by responsible actor or execution thread. Actors indicated in vertical lanes; timeline runs top-to-bottom.

### SysML Extensions over UML

- Continuous flow modeling with rate restrictions
- Probability support
- Control-as-data extensions
- `<<effbd>>` stereotype for EFFBD (Enhanced Functional Flow Block Diagram) conformance

## Sequence Diagram (sd)

**Definition**: represents message-based flow of control between interacting entities (actors, systems, system parts) over time.

### Key Elements

| Element | Semantics |
|---|---|
| Lifeline | Dashed vertical line descending from a block; represents entity existence over time |
| Execution Occurrence | Wide line/elongated rectangle on lifeline; represents active operation |
| Message (synchronous) | Solid arrow with filled arrowhead |
| Message (asynchronous) | Solid arrow with open arrowhead |
| Return Message | Dashed arrow |
| Found Message | Arrow from unknown source (black circle origin) |
| Lost Message | Arrow to unknown destination (black circle target) |
| Creation Message | Arrow to block header (creates instance) |
| Destroy Message | Arrow to X symbol (destroys instance) |
| Gate | Interaction endpoint connecting to external blocks/systems |

### Time Representation

Vertical axis = time (top to bottom). Tilted message arrows denote non-zero transmission latency.

## Requirements Diagram (req)

**Definition**: graphical representation of text-based requirements and their relationships to other model elements. New in SysML — no UML counterpart. Bridges requirements management tools and system model.

### Requirement Properties

- Unique identifier (ID)
- Text specification
- Optional extensions: verification status, priority, type, source, risk

### Display Formats

Graphical, tabular, or tree structure.

### Requirement Relationships

| Stereotype | Semantics |
|---|---|
| Containment (crossed circle) | Hierarchical parent-child decomposition |
| `<<deriveReqt>>` | Derived requirement traces to source requirement |
| `<<satisfy>>` | Model element satisfies a requirement |
| `<<verify>>` | Test case verifies a requirement |
| `<<refine>>` | Model element refines a textual requirement |
| `<<trace>>` | Traceability link from requirement to fulfilling component |
| `<<copy>>` | Requirement is copy of another |

### Cross-Diagram Symbol Mixing

SysML v1.3 Annex A permits "careful mixing" of diagram element types across diagram kinds, provided element constraints are "well-specified." The specification leaves interpretation to the modeler.

## Parametric Diagram (par)

**Definition**: expresses constraints between properties via mathematical equations. New in SysML — no UML counterpart. Enables integration of engineering analysis (performance, reliability) with design models.

### Constraint Property Blocks

- **ConstraintBlock**: contains constraint equation + parameter list
- Notation: rectangle with `<<constraint>>` keyword, or rountangle (eliminates keyword need)
- Parameters bound to actual value properties of other blocks
- Reusable: defined in BDD, applied in parametric diagrams, packageable into model libraries

### Binding Mechanism

Constraint parameters (e.g., `m` in `F=m*a`) bind to specific value properties of blocks (e.g., vehicle mass). Tracks performance parameters throughout system lifecycle.

### OPM Equivalent

Any mathematical constraint maps to a calculating (informatical) process that uses input parameters (instruments) to produce output. See [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## SysML vs OPM Systematic Comparison

### Attribute Comparison

| Feature | SysML | OPM |
|---|---|---|
| Theoretical foundation | UML; Object-Oriented paradigm | Minimal universal ontology; Object-Process Theorem |
| Standard documentation | ~1670 pp (UML Infra 700 + UML Super 700 + SysML 270) | ~180 pp (ISO 19450 main 100 + appendices 80) |
| Standardization body | OMG | ISO |
| Diagram kinds | 9 | 1 (OPD) |
| Top-level concept | Block (UML object class) | Thing (object or process) |
| Complexity management | Aspect-based decomposition | Detail-level-based decomposition |
| Hierarchical decomposition | In some diagram kinds | Yes |
| Symbol count | ~120 | ~20 |
| Graphic modality | Yes | Yes |
| Textual modality | No (tool-dependent, non-standard) | Yes (OPL — formal, standard) |
| Physical-informatical distinction | No | Yes (built-in) |
| Systemic-environmental distinction | Partial (boundaries) | Yes |
| Logical relations (OR, XOR, AND) | No | Yes |
| Probability modeling | No | Yes |
| Execution/simulation/validation | Partial (tool-dependent, some diagram kinds) | Yes |

### Processes as First-Class Citizens

OPM treats processes as first-class citizens — stand-alone "things" alongside objects. UML/SysML encapsulates behavior within objects (OO approach), resulting in multiple process-like terms without explicit shared definition: use case, activity, action, method, sequence.

OPM process taxonomy: transforms objects via (1) state change, (2) object generation, (3) object consumption.

### Physical and Informatical Things

OPM distinguishes physical vs. informatical for both objects and processes. Additionally distinguishes systemic (part of system) vs. environmental (part of environment). SysML lacks both built-in distinctions.

### Model Multiplicity vs. Singularity

- **SysML**: 9 diagram types, each presenting one system aspect (model multiplicity, inherited from UML)
- **OPM**: single diagram type (OPD) combining structure, behavior, and function in one integrated model; hierarchy via OPD refinement levels

### Bimodal Representation

OPM combines mathematically-grounded graphical language with natural language sentences (OPL). Two semantically equivalent modalities engage distinct cognitive channels (visual and lingual). SysML is graphics-only at the standard level.

### Activity Diagrams vs. OPDs

| Aspect | SysML Activity Diagram | OPM OPD |
|---|---|---|
| Arrow semantics | Flow (implicit location change) | Transformation (creation, consumption, state change) |
| Instrument vs. consumee distinction | Not expressible | Native (instrument link vs. consumption link) |
| Physical/informatical distinction | Not expressible | Native (bold vs. regular frames) |
| Decision modeling | Diamond node + `<<decisionInput>>` note | Boolean object with states |
| Refinement mechanism | Rake symbol to sub-activity | In-zooming |

### Requirements in OPM

OPM models requirements without specialized symbols: informatical object class `Requirement` with instances, `satisfies` tagged structural link, and exhibition-characterization for decomposition (Client Free Text, Vitality, Urgency, Satisfying Status, Deriving Requirement).

### Parametrics in OPM

Mathematical constraints expressed as calculating processes with input instruments yielding output objects. OPL textual representation directly translatable to executable code.

## SysML-OPM Synergies

Empirical evaluation (Grobshtein and Dori 2011):

- **OPM advantage**: presenting system hierarchy levels, combining structure with behavior in single view
- **SysML advantage**: modeling detailed views of specific aspects; certain auto-generated SysML views from OPM models answer focused questions faster
- **Synergy potential**: combining OPM's holistic integration with SysML's specialized aspect views
