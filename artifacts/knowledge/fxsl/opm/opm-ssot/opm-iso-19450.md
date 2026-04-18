---
_manifest:
  urn: urn:fxsl:kb:opm-iso-19450
  provenance:
    created_by: kora/curator
    created_at: '2026-03-22'
    source: OPERATIONS/source/fxsl/opm-methodology/opm-iso.md
version: 1.2.0
status: published
tags:
- opm
- iso-19450
- systems-engineering
- conceptual-modeling
- bimodal-representation
- mbse
- opcloud
lang: en
extensions:
  kora:
    family: specification
    shard_index: 1
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opm-iso-19450
---

# OPM ISO/PAS 19450 — Object-Process Methodology


Compact conceptual language and methodology for modelling automation systems and knowledge representation. Specifies formal syntax and semantics for system architects, designers and OPM-compliant tool vendors. Application ranges from simple assemblies to complex multidisciplinary dynamic systems.

OPM provides two semantically equivalent modalities: graphical (OPD set) and textual (OPL sentences in English subset). Domain experts understand OPL without technical training. OPM unifies function, structure and behaviour in a single model.

**Tool support:** OPCloud (cloud-based, primary implementation) generates OPL automatically from OPDs, supports simulation, MQTT/ROS integration, CSV import, AI requirements generation, templates, sub-models, and collaborative editing. Predecessor: OPCAT (desktop, freely available). **Applications:** next-generation appliance design, commercial aircraft modelling, business process knowledge management, automotive vehicle control, ISS robotic arms, insurance product design, and molecular biology research.

---

## Scope and Conformance

OPM is specified with sufficient detail for practitioners to produce conceptual models at various extents of detail and for tool vendors to create supporting software.

Three conformance levels:

| Level | Requirements |
|-------|-------------|
| Partial (symbolic) | Use only OPM symbols (§4) and elements (§7-12) with assigned semantics |
| Full | Partial + modelling approach per §6 and §14 |
| Toolmaker | Partial + provision for full + OPL support per EBNF (Annex A) |

No normative references.

---

## Glossary

76 formal definitions from ISO/PAS 19450 §3. Cross-references use definition numbers.

| # | Term | Definition |
|---|------|-----------|
| 3.1 | Abstraction | Decreasing detail and completeness to improve comprehension |
| 3.2 | Affectee | Transformee whose state changes via process; must be stateful object |
| 3.3 | Agent | Enabler that is a human or group of humans |
| 3.4 | Attribute | Object that characterizes a thing other than itself |
| 3.5 | Behaviour | Transformation of objects from model execution |
| 3.6 | Beneficiary | Stakeholder gaining functional value from system operation |
| 3.7 | Class | Collection of things with same perseverance, essence, affiliation, features and states |
| 3.8 | Completeness | Extent to which all system details are specified |
| 3.9 | Condition link | Procedural link from object/state to process denoting procedural constraint |
| 3.10 | Consumee | Transformee that a process consumes or eliminates |
| 3.11 | Context | Portion of OPM model represented by one OPD and corresponding OPL |
| 3.12 | Control link | Procedural link with additional control semantics |
| 3.13 | Control modifier | Symbol on link adding control semantics: "e" (event) or "c" (condition) |
| 3.14 | Discriminating attribute | Attribute whose values identify corresponding specializations |
| 3.15 | Effect | State change of object or attribute value; applies only to stateful objects |
| 3.16 | Element | Thing or link |
| 3.17 | Enabler | Object enabling a process without being transformed |
| 3.18 | Event | Point in time of object creation/appearance or entrance to state; may initiate precondition evaluation |
| 3.19 | Event link | Control link denoting event from object/state to process |
| 3.20 | Exhibitor | Thing characterized by a feature via exhibition-characterization |
| 3.21 | Feature | Attribute or operation |
| 3.22 | Folding | Abstraction by hiding refineables of unfolded refinee (4 kinds: part, feature, specialization, instance) |
| 3.23 | Function | Process providing functional value to a beneficiary |
| 3.24 | General | Refineable with specializations |
| 3.25 | Informatical | Of or pertaining to data, information, knowledge |
| 3.26 | Inheritance | Assignment of OPM elements from general to specializations |
| 3.27 | Input link | Link from object source state to transforming process |
| 3.28 | Instance (model) | Object/process that is refinee in classification-instantiation |
| 3.29 | Instance (operational) | Uniquely identifiable thing during runtime/simulation |
| 3.30 | Instrument | Non-human enabler |
| 3.31 | Invocation | Initiation of a process by a process |
| 3.32 | Involved object set | Union of preprocess and postprocess object sets |
| 3.33 | In-zoom context | Things and links within boundary of in-zoomed thing |
| 3.34 | In-zooming (object) | Part unfolding indicating spatial ordering of constituent objects |
| 3.35 | In-zooming (process) | Part unfolding indicating temporal partial ordering of constituent processes |
| 3.36 | Link | Graphical expression of structural or procedural relation |
| 3.37 | Metamodel | Model of a modelling language |
| 3.38 | Model fact | Relation between two OPM things or states |
| 3.39 | Object | Model element representing a thing with potential physical or informatical existence |
| 3.40 | Object class | Pattern for objects with same structure and transformation pattern |
| 3.41 | OPD | OPM graphic representation of model or part of model |
| 3.42 | OPL | English subset textual representation of OPM model |
| 3.43 | OPM | Formal bimodal graphic-text language for specifying complex multidisciplinary systems |
| 3.44 | OPD object tree | Tree graph depicting object elaboration through refinement |
| 3.45 | OPD process tree | Tree graph from SD through process in-zooming; primary navigation mechanism |
| 3.46 | Operation | Process characterizing a thing (what the thing does) |
| 3.47 | Output link | Link from transforming process to output state of object |
| 3.48 | Out-zooming (object) | Inverse of object in-zooming |
| 3.49 | Out-zooming (process) | Inverse of process in-zooming |
| 3.50 | Perseverance | Property: static (object) or dynamic (process) |
| 3.51 | Postcondition | Condition resulting from successful process completion |
| 3.52 | Postprocess object set | Objects remaining or resulting from process completion |
| 3.53 | Precondition | Condition for starting a process |
| 3.54 | Preprocess object set | Objects evaluated prior to starting a process |
| 3.55 | Primary essence | Majority essence (informatical or physical) of system things |
| 3.56 | Procedural link | Graphical notation of procedural relation |
| 3.57 | Procedural relation | Time-dependent or conditional connection between object/state and process |
| 3.58 | Process | Transformation of one or more objects |
| 3.59 | Process class | Pattern for processes with same transformation pattern |
| 3.60 | Property | Modelling annotation distinguishing elements (cardinalities, tags, labels) |
| 3.61 | Refineable | Thing amenable to refinement: whole, exhibitor, general, or class |
| 3.62 | Refinee | Thing refining a refineable: part, feature, specialization, or instance |
| 3.63 | Refinement | Elaboration increasing detail and completeness |
| 3.64 | Resultee | Transformee that a process creates |
| 3.65 | Stakeholder | Individual/organization with interest in the system |
| 3.66 | Stateful object | Object with specified states |
| 3.67 | Stateless object | Object lacking specified states |
| 3.68 | State (object) | Possible situation or position of an object |
| 3.69 | State (system) | Snapshot of system model at a point in time |
| 3.70 | State expression | Refinement revealing subset of object's states |
| 3.71 | State suppression | Abstraction hiding subset of object's states |
| 3.72 | Structural link | Graphical notation of structural relation |
| 3.73 | Structural relation | Operationally invariant connection between things |
| 3.74 | Structure | Objects and non-transient relations in model |
| 3.75 | System Diagram (SD) | Root OPD depicting system function and top-level context |
| 3.76 | Thing | Object or process |
| 3.77 | Transformation | Creation, consumption, or state change of an object |
| 3.78 | Transformee | Object affected by a process |
| 3.79 | Transforming link | A consumption, effect, or result link |
| 3.80 | Unfolding | Refinement adding detail to refinees |
| 3.81 | Value (attribute) | State of an attribute |
| 3.82 | Value (functional) | Benefit derived from a system's function |
| 3.83 | Whole | An aggregate |
| 3.84 | OPPL | Sentence classification layer over OPL used for model informativeness grading. Categories: Definition, Structural, Procedural, Meta, Unknown |

Key normative notes on glossary terms:

- **Property vs attribute (3.60)**: unlike an attribute, a property value **cannot change** during simulation or operational implementation. Cardinalities, tags and path labels are properties.
- **No process states (3.68)**: OPM has no concept of process state ("started", "in process", "finished"). Instead, model subprocesses such as Starting, Processing, Finishing.
- **Every thing implies instances (3.28/3.29)**: by creating a thing in the conceptual model, the modeller implies that at least one operational instance of that thing (or a specialization) can exist during system operation.

---

## Modelling Principles

Six principles govern OPM modelling:

1. **Purpose-serving activity** — System function and modelling purpose guide scope and detail. Different stakeholders require different views of the same system.
2. **Unification of function, structure and behaviour** — Structure (physical + informatical objects with structural relations) + behaviour (processes transforming objects over time) = function delivering value to stakeholders.
3. **Identifying functional value** — The value-providing process expresses the function as perceived by the main beneficiary. Identifying and labelling this primary process is the critical first step.
4. **Function vs behaviour** — Function is the value to the beneficiary; behaviour is how the system operates. Same function may have different structural/behavioural implementations (bridge vs ferry for river crossing).
5. **System boundary setting** — Environment is the collection of things outside the system that may interact with it. Systemic things have solid contour; environmental things have dashed contour.
6. **Clarity and completeness trade-off** — Real systems contain overwhelming detail. Understanding requires balancing clarity and completeness via OPD hierarchy.

---

## Fundamental Concepts

### Bimodal Representation

Every OPM model is expressed in semantically equivalent graphics (OPD) and text (OPL). Each OPD has a corresponding OPL paragraph. OPL uses colour coding: processes in blue, objects in green, states in golden brown. This redundancy leverages dual cognitive channels (visual + verbal).

### Modelling Elements

Two element kinds: **things** (objects and processes) and **links** (procedural and structural).

### Context Management

OPD is the fundamental unit depicting elements of a context. Mechanisms for managing contextual scope: state expression/suppression, unfolding/folding, in-zooming/out-zooming.

### Conceptual vs Runtime Models

Conceptual models describe structure and behaviour patterns. Runtime models represent operational instance occurrences during simulation. **A model expressing consistent detail is implementable as a simulation** capable of realizing resources and producing functional value — this is the formal criterion for model completeness.

---

## Visual Notation Specification

OPM's graphical layer uses a minimal set of shapes, contours, shadings and symbols. Every diagram element has a fixed visual specification that determines how to read and compose OPDs.

### Entity Symbols

Entities are closed shapes. Things (objects and processes) and their states are the building blocks.

| Entity | Shape | Contour variants | Shading variants | Label |
|--------|-------|-----------------|------------------|-------|
| Object | Rectangle | solid (systemic), dashed (environmental) | shaded (physical), flat/non-shaded (informatical) | object name, capitalized words |
| Process | Ellipse | solid (systemic), dashed (environmental) | shaded (physical), flat/non-shaded (informatical) | process name, capitalized gerund |
| State | Rounded-corner rectangle (rountangle) inside owning object | normal, thick (initial), double (final), with diagonal open arrow (default) | none | state name, non-capitalized |

The 8 thing symbol combinations result from the Cartesian product of Shape (rectangle/ellipse) × Depth (shaded/flat) × Contour (solid/dashed):

| Symbol | Description | Meaning |
|--------|-------------|---------|
| Shaded solid rectangle | Physical systemic object | Tangible object inside system boundary |
| Shaded dashed rectangle | Physical environmental object | Tangible object outside system boundary |
| Flat solid rectangle | Informatical systemic object | Data/information object inside system |
| Flat dashed rectangle | Informatical environmental object | Data/information object outside system |
| Shaded solid ellipse | Physical systemic process | Physical process inside system |
| Shaded dashed ellipse | Physical environmental process | Physical process outside system |
| Flat solid ellipse | Informatical systemic process | Information process inside system |
| Flat dashed ellipse | Informatical environmental process | Information process outside system |

### Procedural Link Symbols

Procedural links connect objects/states to processes. Each link type has a distinct arrowhead, terminal symbol, or annotation.

| Link | Source | Destination | Graphic specification |
|------|--------|-------------|----------------------|
| Consumption link | object | process | Arrow with **closed arrowhead** pointing from consumee to consuming process |
| Result link | process | object | Arrow with **closed arrowhead** pointing from creating process to resultee |
| Effect link | object ↔ process | bidirectional | **Bidirectional arrow with two closed arrowheads**, one in each direction between affectee and process |
| Input-output effect pair | state → process → state | directional pair | Arrow with closed arrowhead from **input state** to process + arrow from process to **output state** of same object |
| Agent link | agent | process | Line with **filled circle** ("black lollipop") at terminal end extending from agent to process |
| Instrument link | instrument | process | Line with **empty circle** ("white lollipop") at terminal end extending from instrument to process |
| Consumption event link | object | process | Consumption link with small letter **"e"** annotation near arrowhead |
| Effect event link | object ↔ process | bidirectional | Effect link with small letter **"e"** near process end of arrow |
| Agent event link | agent | process | Agent link with small letter **"e"** near process end |
| Instrument event link | instrument | process | Instrument link with small letter **"e"** near process end |
| Condition consumption link | object | process | Consumption link with small letter **"c"** near arrowhead |
| Condition effect link | object ↔ process | bidirectional | Effect link with small letter **"c"** near process end |
| Condition agent link | agent | process | Agent link with small letter **"c"** near process end |
| Condition instrument link | instrument | process | Instrument link with small letter **"c"** near process end |
| Invocation link | process | process | **Lightning-symbol jagged line** from invoking source to invoked destination, ending with closed arrowhead |
| Self-invocation link | process | same process | **Pair of invocation links** originating at process and joining head-to-tail before ending back at origin |
| Overtime exception link | process | handling process | **Single short oblique bar** crossing the line near destination process |
| Undertime exception link | process | handling process | **Two parallel short oblique bars** crossing the line near destination process |

State-specified variants of all procedural links originate from a **specific state** inside the object rather than from the object itself. The annotation ("e" or "c") placement remains near the arrowhead or process end.

### Structural Link Symbols

| Link | Graphic specification |
|------|----------------------|
| Aggregation-participation | **Filled black triangle** with apex connecting by line to whole; parts connect by lines to opposite horizontal base |
| Exhibition-characterization | **Small black triangle inside larger empty triangle**; larger triangle apex connects to exhibitor; features connect to opposite base |
| Generalization-specialization | **Empty triangle**; apex connects to general; specializations connect to opposite base |
| Classification-instantiation | **Small black circle inside empty triangle**; apex connects to class; instances connect to base |
| Incomplete collection indicator | **Short horizontal bar** crossing the vertical line below the triangle symbol |
| Unidirectional tagged | Arrow with **open arrowhead** and tag annotation near shaft |
| Bidirectional tagged | Line with **harpoon-shaped arrowheads** on opposite sides at both ends; each tag aligns on side of arrow with harpoon edge sticking out |
| Reciprocal tagged | Same as bidirectional but with single tag or no tag |

### Logical Operator Symbols

| Operator | Graphic specification |
|----------|----------------------|
| AND | Separate **non-touching** links of same kind on process contour |
| XOR | **Dashed arc** across links of the link fan, arc focal point at convergent endpoint |
| OR | **Two concentric dashed arcs** across links of the link fan, focal point at convergent endpoint |
| Probabilistic | **`Pr=p`** annotation along each fan link; probabilities sum to 1 |

### Context Management Symbols

| Mechanism | Graphic specification |
|-----------|----------------------|
| State suppression indicator | **Small rountangle with "..." label** in object's right bottom corner; signifies hidden states |
| In-diagram unfolding | Refineable and refinees in same OPD, connected by fundamental structural links |
| New-diagram unfolding/in-zooming | Refineable has **thick contour** in both parent OPD (folded) and child OPD (unfolded/in-zoomed) |
| Process in-zooming | Ellipse of refineable **enlarges** to accommodate subprocess symbols; execution timeline flows **top → bottom** within enlarged ellipse |
| Object in-zooming | Rectangle of refineable **enlarges** to accommodate constituent object symbols; arrangement indicates spatial/logical order |
| Implicit invocation | **No explicit symbol**; top-to-bottom vertical arrangement of subprocess ellipse top points within in-zoom context implies invocation sequence |
| Parallel implicit invocation | Subprocess ellipses with top points at **same height** (within tolerance) start simultaneously |
| Duplicate thing | **Small offset shape behind** the repeated thing symbol; indicates same logical element appearing multiple times in OPD |
| Path label | **Text annotation** along procedural link; matching labels on entry/exit links determine execution path |

### In-Zooming Visual Composition

Process in-zooming creates a visual hierarchy. In SD, a process P appears as a simple ellipse connected to objects via procedural links. In SD1, P's ellipse enlarges and contains its subprocesses (P1, P2, P3) as smaller ellipses arranged vertically. Objects from SD connect to the specific subprocesses they relate to. Links attached to the **outer contour** of an in-zoomed process distribute to all subprocesses (enabling links only — consumption and result links **must not** attach to outer contour, as this would violate temporal logic). The modeller migrates consumption/result links to specific subprocesses during in-zooming.

Object in-zooming analogously enlarges a rectangle to show constituent objects in spatial or logical order. Unlike process in-zooming, no transfer of execution control occurs.

---

## Things: Objects and Processes

### Objects

An object is a thing that exists or has potential physical or informatical existence. Persistence is default unless a process acts on it. Represented as a **rectangular box** with the object name.

### Processes

A process transforms one or more objects by generating, affecting (changing state), or consuming them. Has positive performance time duration. Represented as an **ellipse** with the process name.

### Object-Process Test

Three criteria distinguish process from object: time association (happens over time), verb association (ends in gerund "-ing"), and object transformation (must transform at least one object).

### Generic Properties

All things have three generic properties:

| Property | Values | Default |
|----------|--------|---------|
| Perseverance | static (object) / dynamic (process) | determined by type (Persistent default, Transient non-default) |
| Essence | physical / informatical | Informatical is default; Physical is non-default. System primary essence = majority of things |
| Affiliation | systemic / environmental | Systemic is default; Environmental is non-default |

**Affiliation inheritance**: attributes of environmental objects are automatically environmental. Processes performed by environmental entities are environmental processes.

---

## Object States

### Stateful and Stateless Objects

A stateful object has a set of permissible states. At any point in time, a stateful instance is at one state or in transition. A stateless object has no specified states and can only be created or consumed, not affected.

### Representation

A rounded-corner rectangle inside the owning object, labelled with the state name. In OPL: state names in bold without capitalization.

### Initial, Default and Final States

| Designation | Graphic | Meaning |
|-------------|---------|---------|
| Initial | thick border | state at object creation |
| Final | double border | state when consumed |
| Default | diagonal arrow indicator | most likely state on random inspection |

### Attribute Values

An attribute is an object characterizing a thing. Attribute values are states of attributes. May specify measurement units. OPL syntax: `Attribute of Object is value.` or `Attribute of Object ranges from X to Y.`

---
