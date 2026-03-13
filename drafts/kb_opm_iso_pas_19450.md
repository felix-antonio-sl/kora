---
_manifest:
  urn: "urn:kora:kb:opm-iso-pas-19450"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-12"
    source: "ISO/PAS 19450:2015 - Object-Process Methodology"
  version: "1.0.0"
  status: draft
  tags: [opm, methodology, iso, systems-engineering, conceptual-modeling]
  lang: en
  extensions: {}
---

# Object-Process Methodology (ISO/PAS 19450)

## 1 Scope

OPM specifies a conceptual approach, language, and methodology for modelling and knowledge representation of automation systems. Range: simple assemblies to complex multidisciplinary dynamic systems. Suitable for implementation by information and computer technology tools.

OPM provides two semantically equivalent representation modalities:

- **Graphical**: Object-Process Diagrams (OPD)
- **Textual**: Object-Process Language (OPL), subset of English

OPM notation supports conceptual modelling with formal syntax and semantics. Domain-independent nature opens system modelling to scientific, commercial, and industrial communities.

Application domains:

- Systems architecting, engineering, development, life cycle support
- Multidisciplinary environment coordination
- Technical standards drafting and authoring

## 2 Normative References

None.

## 3 Terms and Definitions

### 3.1 Abstraction

Decreasing extent of detail and system model completeness to achieve better comprehension.

### 3.2 Affectee

Transformee that is affected by a process occurrence; its state changes.

- Note: Affectee can only be a stateful object. Stateless object can only be created or consumed.

### 3.3 Agent

Human or group of humans; enabler.

### 3.4 Attribute

Object that characterizes a thing other than itself.

### 3.5 Behaviour

Transformation of objects resulting from execution of an OPM model comprising things and links.

### 3.6 Beneficiary

System stakeholder who gains functional value from system operation.

### 3.7 Class

Collection of things with same perseverance, essence, affiliation values, and same feature and state set.

### 3.8 Completeness

Extent to which all details of a system are specified in a model.

### 3.9 Condition Link

Procedural link from object or object state to process, denoting procedural constraint.

### 3.10 Consumee

Transformee that a process occurrence consumes or eliminates.

### 3.11 Context

Portion of OPM model represented by OPD and corresponding OPL text.

### 3.12 Control Link

Procedural link with additional control semantics.

### 3.13 Control Modifier

Symbol embellishing a link to add control semantics.

- Symbols: 'e' for event, 'c' for condition.

### 3.14 Discriminating Attribute

Attribute whose different values identify corresponding specialization relations.

### 3.15 Effect

Change in state of an object or attribute value.

- Note: Effect only applies to stateful object.

### 3.16 Element

Thing or link.

### 3.17 Enabler

Object that enables a process but which the process does not transform.

### 3.18 Event

Point in time of creation of an object, or entrance of an object to a particular state; may initiate evaluation of process precondition.

### 3.19 Event Link

Control link denoting event originating from object or object state to process.

### 3.20 Exhibitor

Thing that exhibits a feature by means of exhibition-characterization relation.

### 3.21 Feature

Attribute or operation.

### 3.22 Folding

Mechanism of abstraction achieved by hiding refineables of an unfolded refinee.

- Four kinds: parts, features, specializations, instances.
- Primarily applied to objects. When applied to process, subprocesses are unordered (asynchronous systems).

### 3.23 Function

Process that provides functional value to a beneficiary.

### 3.24 General

Refineable with specializations.

### 3.25 Informatical

Of or pertaining to informatics (data, information, knowledge).

### 3.26 Inheritance

Assignment of OPM elements of a general to its specializations.

### 3.27 Input Link

Link from object source state to transforming process.

### 3.28 Instance

Model instance: object instance or process instance that is a refinee in classification-instantiation relation.

### 3.29 Instance

Operational instance: object or process instance that is an actual uniquely identifiable thing during model operation.

### 3.30 Instrument

Non-human enabler.

### 3.31 Invocation

Initiating of a process by a process.

### 3.32 Involved Object Set

Union of preprocess object set and postprocess object set.

### 3.33 In-Zoom Context

Things and links within boundary of thing being in-zoomed.

### 3.34 In-Zooming

Object part unfolding indicating spatial ordering of constituent objects.

### 3.35 In-Zooming

Process part unfolding indicating temporal partial ordering of constituent processes.

### 3.36 Link

Graphical expression of structural relation or procedural relation between OPM things.

### 3.37 Metamodel

Model of a modelling language or part of a modelling language.

### 3.38 Model Fact

Relation between two OPM things or states in OPM model.

### 3.39 Object

OPM model element representing a thing that does or might exist physically or informatically.

### 3.40 Object Class

Pattern for objects that have same structure and pattern of transformation.

### 3.41 Object-Process Diagram (OPD)

OPM graphic representation of OPM model, in which objects and processes appear with structural and procedural links.

### 3.42 Object-Process Language (OPL)

Subset of English natural language representing textually the OPM model that OPD represents graphically.

### 3.43 Object-Process Methodology (OPM)

Formal language and method for specifying complex multidisciplinary systems in single function-structure-behaviour unifying model; uses bimodal graphic-text representation of objects and their transformation or use by processes.

### 3.44 OPD Object Tree

Tree graph whose root is an object, depicting elaboration of object through refinement.

### 3.45 OPD Process Tree

Tree graph whose root is System Diagram and each node is an OPD obtained by in-zooming of a process.

### 3.46 Operation

Process that a thing performs, which characterizes the thing other than itself.

### 3.47 Output Link

Link from transforming process to output destination state of object.

### 3.48 Out-Zooming

Inverse of object in-zooming.

### 3.49 Out-Zooming

Inverse of process in-zooming.

### 3.50 Perseverance

Property of thing which can be static (defining object) or dynamic (defining process).

### 3.51 Postcondition

Condition that is outcome of successful process completion.

### 3.52 Postprocess Object Set

Collection of objects remaining or resulting from process completion.

### 3.53 Precondition

Condition for starting a process.

### 3.54 Preprocess Object Set

Collection of objects to evaluate prior to starting a process.

### 3.55 Primary Essence

Essence of majority of things in system, which can be informatical or physical.

### 3.56 Procedural Link

Graphic notation of procedural relation in OPM.

### 3.57 Procedural Relation

Connection or association between object or object state and process.

- Specifies how system operates to attain function.
- Designates time-dependent or conditional initiating of processes that transform objects.

### 3.58 Process

Transformation of one or more objects in the system.

### 3.59 Process Class

Pattern for processes that perform same object transformation pattern.

### 3.60 Property

Modelling annotation common to all elements of specific kind to distinguish that element.

- Cardinality constraints, path labels, structural link tags are frequent property annotations.
- Unlike attribute, property value may not change during model simulation.

### 3.61 Refineable

Thing amenable to refinement; can be whole, exhibitor, general, or class.

### 3.62 Refinee

Thing that refines a refineable; can be part, feature, specialization, or instance.

- Four kinds correspond to refineables (part-whole, feature-exhibitor, specialization-generalization, instance-class).

### 3.63 Refinement

Elaboration that increases extent of detail and consequent model completeness.

### 3.64 Resultee

Transformee that a process occurrence creates.

### 3.65 Stakeholder

Individual, organization, or group that has interest in or might be affected by system.

### 3.66 Stateful Object

Object with specified states.

### 3.67 Stateless Object

Object lacking specified states.

### 3.68 State

Possible situation or position of object.

- Note: OPM has no concept of process state ("started", "in process", "finished"). Instead models subprocesses.

### 3.69 State

Snapshot of system model at certain point in time; shows all existing object instances, current states of each stateful object instance, and process instances with elapsed times.

### 3.70 State Expression

Refinement involving revealing of any proper subset of object set of states.

### 3.71 State Suppression

Abstraction involving hiding of any proper subset of object set of states.

### 3.72 Structural Link

Graphic notation of structural relation in OPM.

### 3.73 Structural Relation

Operationally invariant connection or association between things.

- Persist in system for at least some interval of time.
- Provide structural aspect, not contingent upon time-dependent conditions.

### 3.74 Structure

Collection of objects in OPM model and non-transient relations among them.

### 3.75 System Diagram (SD)

OPD with one systemic process indicating system function and objects connecting with that function to depict overall context and top-level view.

### 3.76 Thing

Object or process.

### 3.77 Transformation

Change in object properties, state, or existence.

### 3.78 Transformee

Object that undergoes transformation in process.

### 3.79 Unidirectional Tagged Structural Link

Structural link with single direction and tag.

### 3.80 Unfolding

Refinement operation that exposes refineables of a refineable.

### 3.81 Value

Specific state of attribute.

### 3.82 Functional Value

Value provided by system function to beneficiary.

## 4 Symbols

### Graphical Symbols

| Symbol                          | Meaning                                         |
| ------------------------------- | ----------------------------------------------- |
| Rectangle                       | Object                                          |
| Ellipse                         | Process                                         |
| Border style/shading variations | Physical, informatic, environmental distinction |

### Structural Links

- Unidirectional tagged structural link
- Bidirectional tagged structural link

### Procedural Links

- Agent link
- Instrument link
- Effect link
- Consumption link
- Result link
- Input-output link pair
- Instrument event link
- Consumption event link
- Instrumental condition link
- Consumption condition link
- Invocation link

### Special Links

- Self-invocation link
- Over-time exception link
- Under-time exception link

## 5 Conformance

### 5.1 Partial (Symbolic) Conformance

Using only OPM symbols defined in Clause 4 with assigned meaning; using only OPM elements defined in Clauses 7-12 with assigned meaning.

### 5.2 Full Conformance

Partial conformance plus conformance with approach and scheme of modelling systems with OPM (Clauses 6 and 14).

### 5.3 Toolmaker Conformance

Partial conformance; provision for full conformance support; OPL support according to EBNF (Annex A).

## 6 OPM Principles and Concepts

### 6.1 Modelling Principles

#### 6.1.1 Modelling as Purpose-Serving Activity

System function and modelling purpose guide scope and extent of detail. Complex systems involve many stakeholders with different relevant aspects.

#### 6.1.2 Unification of Function, Structure, and Behaviour

- **Structure model**: assembly of physical and informatical objects connected by structural relations.
- **Behaviour model**: mechanisms that act on system over time to transform objects.
- Combination enables system to perform function delivering functional value.

#### 6.1.3 Identifying Functional Value

Process expressing functional value shall express function as perceived by main beneficiary. Identifying and labelling this primary process is critical first step.

#### 6.1.4 Function versus Behaviour

Value of function often expressed in process terms emphasizing behaviour. Distinguish between function and behaviour to create clear system model.

- Example: River crossing achieved by bridge or ferry. Same function, different structure and behaviour.

#### 6.1.5 System Boundary Setting

System environment: collection of things outside system that may interact with it.

#### 6.1.6 Clarity and Completeness Trade-off

Real systems contain overwhelming detail. Understanding requires balancing clarity and completeness. Excessive detail reduces comprehension.

### 6.2 Fundamental Concepts

#### 6.2.1 Bimodal Representation

OPM model shall be bimodal with expression in semantically equivalent graphics and text.

- Each graphical OPD shall have equivalent textual paragraph using OPL.

#### 6.2.2 OPM Modelling Elements

- **Things**: objects, processes
- **Links**: procedural, structural

#### 6.2.3 OPM Things: Objects and Processes

- **Object**: thing that exists or can exist physically or informatically.
- **Process**: thing that transforms objects.
  - Transforms by: creating, consuming, changing state.

#### 6.2.4 OPM Links: Procedural and Structural

- **Procedural**: specify how system operates to attain function.
- **Structural**: persist for time interval.

#### 6.2.5 OPM Context Management

Mechanisms for managing contextual scope of model detail. Fundamental unit: OPD.

#### 6.2.6 OPM Model Implementation

- **Conceptual models**: describe structure and behaviour patterns.
- **Runtime models**: represent operational instance occurrences.
- Simulation: creating object and process operational instances.

## 7 OPM Thing Syntax and Semantics

### 7.1 Objects

#### 7.1.1 Description

Object: thing that exists or has potential of physical or informatical existence.

- Temporal viewpoint: existence persistent unless process acts on it.
- Category identifier identifies pattern of structure, properties, features.

#### 7.1.2 Representation

Rectangular box containing object name.

### 7.2 Processes

#### 7.2.1 Description

Process: thing that transforms one or more objects.

- Transformation types: generation, effect, consumption.
- Process has positive performance time duration.

#### 7.2.2 Representation

Ellipse containing process name.

### 7.3 OPM Things

#### 7.3.1 OPM Thing Defined

OPM thing: either object or process. Symmetric in many respects, depend on each other.

#### 7.3.2 Object-Process Test

Process must satisfy three criteria:

1. Time association
2. Verb association
3. Object transformation

Example: Flight is process because it transforms location of airplane.

#### 7.3.3 OPM Thing Generic Properties

| Property     | Object (static)           | Process (dynamic)         |
| ------------ | ------------------------- | ------------------------- |
| Perseverance | static                    | dynamic                   |
| Essence      | physical or informatical  | physical or informatical  |
| Affiliation  | systemic or environmental | systemic or environmental |

#### 7.3.4 Default Values

- Default affiliation: systemic.
- System primary essence: majority essence of contained things.

### 7.4 Object States

#### 7.4.1 Stateful and Stateless Objects

- **Stateful object**: has set of permissible states.
- **Stateless object**: no specified states.

#### 7.4.2 Object State Representation

Rounded rectangle inside object represents state.

#### 7.4.3 Initial, Default, and Final States

- **Initial state**: state at object creation.
- **Final state**: state when object is consumed.
- **Default state**: most likely state during random inspection.

#### 7.4.4 Representation

- Initial states: thick border
- Final states: double border
- Default states: diagonal arrow indicator

#### 7.4.5 Attribute Values

Attributes are objects whose states represent attribute values.

- Example: Temperature = 75°C.
- May specify measurement units.

## 8 OPM Link Syntax and Semantics Overview

### 8.1 Procedural Link Overview

#### 8.1.1 Kinds of Procedural Links

- **Transforming link**: connects process with transformee object.
- **Enabling link**: connects enabler object with process.
- **Control link**: execution control mechanism.

#### 8.1.2 Procedural Link Uniqueness OPM Principle

Object or state shall have exactly one role with respect to process it links to.

#### 8.1.3 State-Specified Procedural Links

Procedural link may connect process to specified state of object.

### 8.2 Operational Semantics and Execution Control

#### 8.2.1 Event-Condition-Action Control Mechanism

Execution control based on ECA paradigm.

- Process performance begins when:
  1. Initiating event occurs
  2. Precondition is satisfied
- Events and conditions jointly specify flow of execution.

#### 8.2.2 Preprocess and Postprocess Object Sets

- **Preprocess object set**: defines preconditions for process activation.
  - Typical elements: consumed objects, affected objects, enablers.
- **Postprocess object set**: defines postconditions.
  - Typical elements: resultees, affected objects.

## 9 Procedural Links

### 9.1 Transforming Links

#### 9.1.1 Kinds of Transforming Links

Three types:

- **Consumption link**: destroys or eliminates object.
- **Result link**: creates object.
- **Effect link**: changes state of object.

#### 9.1.2 Consumption Link

Process destroys or eliminates linked object.

- Syntax: **Processing consumes Consumee.**

#### 9.1.3 Result Link

Process creates linked object.

- Syntax: **Processing yields Resultee.**

#### 9.1.4 Effect Link

Process changes state of object.

- Syntax: **Processing affects Affectee.**

#### 9.1.5 Basic Transforming Links Summary

| Name             | Semantics                    | Syntax                       |
| ---------------- | ---------------------------- | ---------------------------- |
| Consumption link | Process consumes object      | Processing consumes Consumee |
| Result link      | Process generates object     | Processing yields Resultee   |
| Effect link      | Process affects object state | Processing affects Affectee  |

### 9.2 Enabling Links

#### 9.2.1 Kinds of Enabling Links

Two kinds:

- **Agent link**: human enabler.
- **Instrument link**: inanimate enabler.

#### 9.2.2 Agent and Agent Link

Agent: human or group capable of intelligent decision-making.

- Syntax: **Agent handles Processing.**

#### 9.2.3 Instrument and Instrument Link

Instrument: inanimate enabler necessary for process.

- Syntax: **Processing requires Instrument.**

#### 9.2.4 Basic Enabling Links Summary

| Name            | Semantics                        | Syntax                         |
| --------------- | -------------------------------- | ------------------------------ |
| Agent Link      | Human enables process            | Agent handles Processing       |
| Instrument Link | Inanimate object enables process | Processing requires Instrument |

### 9.3 State-Specified Transforming Links

#### 9.3.1 State-Specified Consumption Link

Consumption link from specified state of consumee to process.

- Existence of consumee in specified state is precondition.
- Syntax: **Process consumes specified-state Object.**
- If consumee not in specified state, process waits.

#### 9.3.2 State-Specified Result Link

Result link from process to specified state of resultee.

- Existence of resultee at specified state is postcondition.
- Syntax: **Process yields specified-state Object.**

#### 9.3.3 State-Specified Effect Links

**Input-output-specified effect link**: pair of effect links from input source state to affecting process and from process to output destination state.

- Syntax: **Process changes Object from input-state to output-state.**

**Input-specified effect link**: input source specified, output unspecified (default state or probability distribution).

- Syntax: **Process changes Object from input-state.**

**Output-specified effect link**: input unspecified, output destination specified.

- Syntax: **Process changes Object to output-state.**

#### 9.3.4 State-Specified Transforming Links Summary

| Name                               | Semantics                                               |
| ---------------------------------- | ------------------------------------------------------- |
| State-specified consumption link   | Process consumes object in specified state              |
| State-specified result link        | Process yields object in specified state                |
| Input-output-specified effect link | Process changes object from input-state to output-state |
| Input-specified effect link        | Process changes object from input-state                 |
| Output-specified effect link       | Process changes object to output-state                  |

### 9.4 Control Links

#### 9.4.1 Kinds of Control Links

- **Event link**: control link with event modifier ('e').
- **Condition link**: control link with condition modifier ('c').
- **Exception link**: handles abnormal flow.

#### 9.4.2 Event Links

Event link denotes event originating from object or object state to process.

- Controls process initiation based on object creation or state change.

#### 9.4.3 Condition Links

Condition link denotes procedural constraint from object or object state to process.

- Process executes only when condition satisfied.

#### 9.4.4 Exception Links

Handle abnormal conditions during process execution.

- Over-time exception: process takes too long.
- Under-time exception: process completes too quickly.

### 9.5 Logical Operators: AND, XOR, OR

#### 9.5.1 Logical AND Procedural Links

Multiple objects must be involved in process.

- AND link fan: diverging/branching from multiple objects to process.

#### 9.5.2 Logical XOR and OR Procedural Links

- **XOR**: exactly one of multiple conditions triggers process.
- **OR**: one or more conditions trigger process.

#### 9.5.3 Diverging and Converging XOR and OR Links

- **Diverging**: one source triggers multiple possible process paths.
- **Converging**: multiple sources converge to single process.

#### 9.5.4 State-Specified XOR and OR Link Fans

XOR/OR links combined with state-specified links.

#### 9.5.5 Control-Modified Link Fans

Control modifiers (event, condition) combined with logical operators.

#### 9.5.6 Link Probabilities and Probabilistic Link Fans

Links may have probability weights for nondeterministic modelling.

## 10 Structural Links

### 10.1 Kinds of Structural Links

- **Tagged structural link**: unidirectional or bidirectional with tag.
- **Fundamental structural relations**: aggregation-participation, exhibition-characterization, generalization-specialization, classification-instantiation.

### 10.2 Tagged Structural Link

#### 10.2.1 Unidirectional Tagged Structural Link

Single direction with tag.

#### 10.2.2 Unidirectional Null-Tagged Structural Link

Unidirectional without tag.

#### 10.2.3 Bidirectional Tagged Structural Link

Both directions with tags.

#### 10.2.4 Reciprocal Tagged Structural Link

Both directions share same tag.

### 10.3 Fundamental Structural Relations

#### 10.3.1 Kinds

1. Aggregation-participation
2. Exhibition-characterization
3. Generalization-specialization
4. Classification-instantiation

#### 10.3.2 Aggregation-Participation Relation Link

- **Aggregation**: whole-part relationship.
- **Participation**: part contributes to whole.
- Syntax: **Part participates in Whole.**

#### 10.3.3 Exhibition-Characterization Link

- **Exhibitor**: thing that exhibits feature.
- **Characterization**: feature characterizes exhibitor.
- Syntax: **Exhibitor exhibits Characteristic.**

#### 10.3.4 Generalization-Specialization and Inheritance

- **General**: refineable with specializations.
- **Specialization**: refinee of general.
- **Inheritance**: assignment of OPM elements from general to specializations.
- Syntax: **Specialization is General.**

#### 10.3.5 Classification-Instantiation Link

- **Class**: pattern for objects/processes.
- **Instance**: specific occurrence of class.
- Syntax: **Instance is instance of Class.**

#### 10.3.6 Fundamental Structural Relation Link Summary

| Relation                      | Semantics               | Syntax                            |
| ----------------------------- | ----------------------- | --------------------------------- |
| Aggregation-participation     | Whole-part relationship | Part participates in Whole        |
| Exhibition-characterization   | Feature-characteristic  | Exhibitor exhibits Characteristic |
| Generalization-specialization | Parent-child hierarchy  | Specialization is General         |
| Classification-instantiation  | Class-instance          | Instance is instance of Class     |

### 10.4 State-Specified Structural Relations

#### 10.4.1 State-Specified Characterization Relation Link

Characterization relation applies only when object in specific state.

#### 10.4.2 State-Specified Tagged Structural Relations

Tagged structural relation applies only when object in specific state.

## 11 Relationship Cardinalities

### 11.1 Object Multiplicity in Structural and Procedural Links

Cardinality constraints specify:

- **One (1)**: exactly one.
- **Zero or one (0..1)**: optional single.
- **Many (*)**: zero or more.
- **Range (n..m)**: between n and m.

### 11.2 Object Multiplicity Expressions and Constraints

Multiplicity expressions constrain number of object instances in relations.

### 11.3 Attribute Value and Multiplicity Constraints

Attribute values may have cardinality constraints.

## 12 Logical Operators: AND, XOR, and OR

### 12.1 Logical AND Procedural Links

Multiple objects must all be present for process.

- Syntax: **Object1 AND Object2 are required for Process.**

### 12.2 Logical XOR and OR Procedural Links

- **XOR**: exclusive choice.
- **OR**: inclusive choice (one or more).

### 12.3 Diverging and Converging XOR and OR Links

- Diverging: one input branches to multiple outputs.
- Converging: multiple inputs merge to one output.

### 12.4 State-Specified XOR and OR Link Fans

XOR/OR with state-specific conditions.

### 12.5 Control-Modified Link Fans

Control modifiers (event/condition) applied to logical link fans.

### 12.6 State-Specified Control-Modified Link Fans

State specifications combined with control-modified link fans.

### 12.7 Link Probabilities and Probabilistic Link Fans

Probabilistic modelling with weighted links.

## 13 Execution Path and Path Labels

Execution paths through OPM model:

- Sequential: processes execute in order.
- Parallel: processes execute simultaneously.
- Conditional: process execution depends on conditions.
- Looping: process repeats.

Path labels annotate execution flow for clarity.

## 14 Context Management with OPM

### 14.1 Completing the System Diagram

System Diagram (SD) provides top-level view of system.

### 14.2 Achieving Model Comprehension

#### 14.2.1 OPM Refinement-Abstraction Mechanisms

- **In-zooming**: drilling down into process or object detail.
- **Out-zooming**: moving up to higher abstraction level.
- **Folding**: hiding detail through abstraction.
- **Unfolding**: revealing detail through refinement.

#### 14.2.2 Control (Operational) Semantics within In-Zoomed Process Context

In-zoomed process context maintains independent execution semantics.

#### 14.2.3 OPM Fact Consistency Principle

Model facts must remain consistent across zoom levels.

#### 14.2.4 Abstraction Ambiguity Resolution for Procedural Links

Procedural links must maintain clear semantics at all abstraction levels.

## Annex A (Normative): OPL Formal Syntax in EBNF

OPL syntax defined in Extended Backus-Naur Form.

- Reserved words in regular font.
- Commas and periods in bold.
- Object and process names in bold italic.

## Annex B (Informative): Guidance for OPM

Common conventions and patterns in OPM applications.

## Annex C (Informative): Modelling OPM using OPM

OPM concepts applied to model OPM itself.

## Annex D (Informative): OPM Dynamics and Simulation

Dynamic behaviour and simulation capabilities of OPM models.

- Runtime instance creation.
- Process execution tracing.
- State change monitoring.

## Bibliography

- ISO 19450:2015
- OPM literature and tool documentation
