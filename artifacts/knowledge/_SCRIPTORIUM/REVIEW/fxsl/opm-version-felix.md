---
_manifest:
  urn: urn:fxsl:kb:opm-version-felix
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/fxsl/opm-methodology/OPM version
      felix.md — version personal de OPM con anotaciones de Felix
version: 1.0.0
status: borrador
tags:
- opm
- version-felix
- anotaciones
- fxsl
lang: es
extensions:
  kora:
    family: guide
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:opm-version-felix
---

# Object Process Methodology (OPM)


## Overview

Object process methodology (OPM) is a conceptual modeling language and methodology for capturing knowledge and designing systems. Based on a minimal universal ontology of stateful objects and processes that transform them, OPM can be used to formally specify the function, structure, and behavior of artificial and natural systems in a large variety of domains. Catering to human cognitive abilities, an OPM model represents the system under design or study bimodally in both graphics and text for improved representation, understanding, communication, and learning.

In OPM, an object is anything that does or does not exist. Objects are stateful—they may have states, such that at each point in time, the object is at one of its states or in transition between states. A process is a thing that transforms an object by creating or consuming it, or by changing its state.

OPM is bimodal; it is expressed both visually/graphically in object-process diagrams (OPD) and verbally/textually in Object-Process Language (OPL), a set of automatically generated sentences in a subset of English. A patented software package called OPCAT, for generating OPD and OPL, is freely available.[5]

## Terms

1. Abstraction: Reduction of detail and system model completeness to improve comprehension.
2. Affectee: A transformee affected by a process resulting in a state change. Only stateful objects can be affectees.
3. Agent: An enabler that is a human or a group of humans.
4. Attribute: An object that characterizes something other than itself.
5. Behaviour: Transformation of objects via execution of an Object-Process Methodology model.
6. Beneficiary: A system stakeholder who gains functional value from system operation
7. Class: A collection of things sharing the same perseverance essence, affiliation values, features and states
8. Completeness: Extent to which all system details are specified in a model.
9. Condition Link: A procedural link from an object or object state to a process imposing a procedural constraint.
10. Consumee: A transformee consumed or eliminated by a process
11. Context: The portion of an Object-Process Methodology model represented by an Object-Process Diagram and Object-Process Language text.
12. Control Link: A procedural link with added control semantics.
13. Control Modifier: A symbol on a link adding control semantics, e.g., ‘e’ for event or ‘c’ for condition.
14. Discriminating Attribute: An attribute whose values distinguish corresponding specialization relations.
15. Effect: A state change in an object or attribute. Only applies to stateful objects 
16. Element: A thing or a link 
17. Enabler: An entity (human or non-human) that enables a process.
18. Event: Point in time when an object is created, appears, or transitions into a particular state 
19. Event Link: A control link representing an event originating from an object or object state enabling a process 
20. Exhibitor: A thing characterized by a feature 
21. Feature: An attribute or operation 
22. Folding: An abstraction by hiding refineables of an unfolded refinee. Opposite of unfolding 
23. Function: A process providing functional value to a beneficiary 
24. General: An Object-Process Methodology (OPM) refineable with specializations.
25. Informatical: Pertaining to data, information, or knowledge.
26. Inheritance: Assignment of OPM elements from a general to its specializations.
27. Input Link: A link from an object’s source state to the transforming process 
28. Instance: An object or process in a model or operational context.
29. Instance (Operational): A uniquely identifiable object or process during runtime.
30. Instrument: A non-human enabler 
31. Invocation: The initiation of a process by another process.
32. Involved Object Set: The union of preprocess and postprocess object sets.
33. In-Zoom Context: Things and links within the boundary of an in-zoomed object.
34. In-Zooming (Object): Unfolding to reveal constituent objects and spatial order.
35. In-Zooming (Process): Unfolding to reveal constituent processes and temporal order.
36. Link: Graphical expression of a structural or procedural relation.
37. Metamodel: Model of a modelling language.
38. Model Fact: A relation between two OPM elements.
39. Object: A model element representing a thing with potential physical or informatical existence.
40. Object Class: A pattern for objects with the same structure and transformation pattern 
41. Object-Process Diagram (OPD): Graphic representation of an OPM model.
42. Object-Process Language (OPL): Textual representation of an OPM model.
43. Object-Process Methodology (OPM): A bimodal language for modeling complex systems.
44. OPD Object Tree: Graph elaborating an object through refinement 
45. OPD Process Tree: Graph elaborating processes through in-zooming.
46. Operation: A process characterizing a thing 
47. Output Link: A link from a transforming process to the output state of an object.
48. Out-Zooming (Object): Inverse of object in-zooming 
49. Out-Zooming (Process): Inverse of process in-zooming 
50. Perseverance: A property defining static or dynamic characteristics of things 
51. Postcondition: A condition resulting from successful process completion.
52. Postprocess Object Set: Objects resulting from a process completion.
53. Precondition: A condition required to start a process 
54. Preprocess Object Set: Objects evaluated before starting a process 
55. Primary Essence: The predominant essence (physical or informatical) of a system.
56. Procedural Link: Graphical notation of procedural relations 
57. Procedural Relation: A time-dependent or conditional connection between objects and processes.
58. Process: A transformation of objects in the system.
59. Process Class: A pattern for processes sharing the same transformation pattern.
60. Property: Annotations distinguishing elements 
61. Refineable: An OPM element amenable to refinement.
62. Refinee: An element elaborated by refinement.
63. Refinement: Elaboration increasing model detail and completeness.
64. Resultee: A transformee created by a process.
65. Stakeholder: Individuals or groups with interest in the system.
66. Stateful Object: An object with specified states.
67. Stateless Object: An object lacking specified states.
68. State (Object): Possible situation or position of an object.
69. State (System): Snapshot of a system model at a specific time.
70. State Expression: Refinement revealing subsets of an object’s states.
71. State Suppression: Abstraction hiding subsets of an object’s states.
72. Structural Link: Graphical notation of structural relations.
73. Structural Relation: Invariant connections among system elements.
74. Structure: Non-transient relations among objects in an OPM model.
75. System Diagram (SD): The root OPD depicting the system’s top-level context.
76. Thing: An object or process.
77. Transformation: Creation, consumption, or state change of an object.
78. Transformee: An object affected by a process.
79. Transforming Link: A consumption, effect, or result link.
80. Unfolding: Refinement adding detail to refinees.
81. Value (Attribute): State of an attribute.
82. Value (Functional): Benefit derived from a system’s function.
83. Whole: An aggregate.

## Basics

OPM entities: object, object state and process

OPM has two main parts: the language and the methodology. The language is bimodal—it is expressed in two complementary ways (modalities): the visual, graphical part—a set of one or more object-process diagrams (OPDs), and a corresponding textual part—a set of sentences in object-process language (OPL), which is a subset of English.

The top-level OPD is the system diagram (SD), which provides the context for the system's function. For man-made systems this function is expected to benefit a person or a group of people—the beneficiary. The function is the main process in SD, which also contains the objects involved in this process: the beneficiary, the operand (the object upon which the process operates), and possibly the attribute whose value the process changes.

OPM graphical elements are divided into entities, expressed as closed shapes, and relations, expressed as links that connect entities.

### Entities

Entities are the building blocks of OPM. They include objects and processes, collectively called things, and object states.

- Object: Associations among objects constitute the object structure of the system being modeled. In OPL text, the object name shall appear in bold face with capitalization of each word.
- Object state: An object state is a particular situation classification of an object at some point during its lifetime. At every point in time, the object is in one of its states or in transition between two of its states—from its input state to its output state.
- Process: A process is an expression of the pattern of transformation of objects in the system. A process does not exist in isolation; it is always associated with and occurs or happens to one or more objects. A process transforms objects by creating them, consuming them, or changing their state. Thus, processes complement objects by providing the dynamic, behavioral aspect of the system. In OPL text, the process name shall appear in bold face with capitalization of each word.

### Links

#### OPM structural links

A structural links defines a structural relation. A structural relation shall specify an association that persists in the system for at least some interval of time.

#### Procedural link

A procedural link defines procedural relation. A procedural relation shall specify how the system operates to attain its function, designating time dependent or conditional triggering of processes, which transform objects.

#### Event and condition

The Event-Condition-Action paradigm provides the OPM operational semantics and flow of control. An event is a point in time at which an object is created (or appears to be created from the system's perspective) or an object enters a specified state. At runtime, this process triggering initiates evaluation of the process precondition. Thus, starting a process execution has two prerequisites: (1) a triggering event, and (2) satisfaction of a precondition.

Once the event triggers a process, the event ceases to exist.

## Things

Objects and processes are symmetric in many regards and have much in common in terms of relations, such as aggregation, generalization, and characterization.

To apply OPM in a useful manner, the modeler has to make the essential distinction between objects and processes, as a prerequisite for successful system analysis and design. By default, a noun shall identify an object.

### Thing generic attributes

OPM things have three generic attributes:

- Perseverance
- Essence
- Affiliation

OPM thing generic attributes have the following default values:

The default value of the Affiliation generic attribute of a thing is systemic.

System essence shall be the primary essence of the system. Like thing essence, its values are informatical and physical. Information systems, in which the majority of things are informatical, shall be primarily informatical, while systems in which the majority of things are physical shall be primarily physical.

The default value of the Essence generic attribute of a thing in a primarily informatical [physical] system shall be informatical [physical].

## Object states

### Stateful and stateless objects

Dov Dori explains in Model-Based Systems Engineering with OPM and SysML that "An object state is a possible situation in which an object may exist. An object state has meaning only in the context of the object to which it belongs." A stateless object shall be an object that has no specification of states. A stateful object shall be an object for which a set of permissible states are specified. In a runtime model, at any point in time, any stateful object instance is at a particular permissible state or in transition between two states.

### Attribute values

An attribute is an object that characterizes a thing. An attribute value is a specialization of state in the sense that a value is a state of an attribute: an object has an attribute, which is a different object, to which that value is assigned for some period of time during the existence of the object exhibiting that attribute.

### Object state representation

A state is graphically defined by a labelled, rounded-corner rectangle placed inside the owning object. It can not live without an object. In OPL text, the state name shall appear in bold face without capitalization.

### Initial, default, and final states

A state that is initial is graphically defined by a state representation with thick contour. A state that is final is graphically defined by a state representation with double contour. A state that is default is graphically defined by a state representation with an open arrow pointing diagonally from the left. The corresponding OPL sentences shall include explicit indicators for an initial, final or default state.

## Procedural links

A procedural link is one of three kinds:

Transforming link, which connects a transformer (an object that the process transforms) or its state with a process to model object transformation, namely generation, consumption, or state change of that object as a result of the process execution.

Enabling link, which connects an enabler (an object that enables the process occurrence but is not transformed by that process) or its state, to a process, which enables the occurrence of that process.

Control link, which is a procedural (transforming or enabling) link with a control modifier—the letter e (for event) or c (for condition), which adds semantics of a control element. The letter e signifies an event for triggering the linked process, while the letter c signifies a condition for execution of the linked process, or connection of two processes denoting invocation, or exception.

##### Procedural link uniqueness OPM principle

A process needs to transform at least one object. Hence, a process shall be connected via a transforming link to at least one object or object state. At any particular extent of abstraction, an object or any one of its states shall have exactly one role as a model element with respect to a process to which it links: the object may be a transformee or an enabler. Additionally, it can be a trigger for an event (if it has the control modifier e), or a conditioning object (if it has the control modifier c), or both.

###### State-specified procedural links

A state-specified procedural link is a detailed version of its procedural link counterpart in that rather than connecting a process to an object, it connects a process to a specific state of that object.

##### Transforming links

The three kinds of transforming links are:

Consumption link: Graphically, an arrow with a closed arrowhead pointing from the consumee to the consuming process defines the consumption link. By assumption, the consumed object disappears as soon as the process begins execution. The syntax of a consumption link OPL sentence is: Processing consumes Consumee.

Effect link: A transforming link specifying that the linked process affects the linked object, which is the affectee, i.e., the process causes some unspecified change in the state of the affectee. Graphically, a bidirectional arrow with two closed arrowheads, one pointing in each direction between the affecting process and the affected object, shall define the effect link. The syntax of an effect link OPL sentence is: Processing affects Affectee.

Result link: Graphically, an arrow with a closed arrowhead pointing from the creating process to the resultee shall define a result link. The syntax of a result link OPL sentence is: Processing yields Resultee.

##### Enabling links

An enabling link is a procedural link specifying an enabler for a process—an object that must be present for that process to occur, but the existence and state of that object after the process is complete are the same as just before the process began. The two kinds of enabling links are:

Agent and agent link: A human or a group of humans capable of intelligent decision-making, who enable a process by interacting with the system to enable or control the process throughout execution. Graphically, a line with a filled circle ("black lollipop") at the terminal end extending from the agent object to the process it enables defines an agent link. The syntax of an agent link OPL sentence is: Agent handles Processing.

Instrument and instrument link: An inanimate or otherwise non-decision-making enabler of a process that cannot start or take place without the existence and availability of the instrument.

###### State-specified transforming links

State-specified consumption link: A consumption link that originates from a particular state of the consumee, meaning that the consumee must be in that state for it to be consumed by the process to which it is linked. Graphically, an arrow with a closed arrowhead pointing from the particular object state to the process, which consumes the object, defines the state-specified consumption link.

State-specified result link: A result link that terminates at a specific state of the resultee, meaning that the resultee shall be in that resultant state upon its construction. Graphically, an arrow with a closed arrowhead pointing from the process to the particular object state defines the state-specified result link. The syntax OPL sentence is: Process yields qualified-state Object.

State-specified effect links:

Input and output effect links- An input link is the link from the object's input state to the transforming process, while the output link is the link from the transforming process to the object's output state.

Input-output-specified effect link: A pair of effect links, where the input link originates from a particular state of the affectee and the output link originates from that process and terminates at the output state of the same affectee. Graphically, a pair of arrows with a closed arrowhead from the input state of the affectee to the affecting process and a similar arrow from that process to the state of the affectee at process terminates defines the input-output-specified effect link. The syntax OPL sentence is: Process changes Object from input-state to output-state.

Input-specified effect link: A pair of effect links, where the input link originates from a particular state of the affectee and the output link originates from that process and terminates at the affectee without specifying a particular state. Graphically, a pair of arrows consisting of an arrow with a closed arrowhead from a particular state—the input state—of the affectee to the process, and a similar arrow from that process to the affectee but not to any one of its states defines the input-specified effect link. The syntax OPL sentence is: Process changes Object from input-state.

Output-specified effect link: A pair of effect links, where the input (source) link originates from an affectee, and the output link originates from the process and terminates at the output (destination, resultant) state of the same affectee. Graphically, a pair of arrows consisting of an arrow with a closed arrowhead from the affectee, but not from any one of its states, to the affecting process, and a similar arrow from that process to a particular state of that affectee— the output state— defines the output-specified effect link.

###### State-specified enabling links

Originate from a specific qualifying state and terminate at a process, meaning that the process may occur if and only if the object exists at the state from which the link originates.

State-specified agent link: Graphically, a line with a filled circle ("black lollipop") at the terminal end extending from the qualifying state of the agent object to the process it enables defines a state-specified agent link. The syntax OPL sentence is: Qualifying-state Agent handles Processing.

State-specified instrument link: An instrument link that originates from a specific qualifying state of the instrument. Graphically, a line with an empty circle ("white lollipop") at the terminal end extending from the qualifying state of the instrument object to the process it enables defines a state-specified instrument link. The syntax OPL sentence is: Processing requires qualifying-state instrument.

## Event-Condition-Action control

##### Preprocess object set and process precondition

In order for an OPM process to start executing once it has been triggered, it needs a set of objects comprising one or more consumes, some possibly at specific states, and/or affects, collectively called the preprocess object set. At instance-level execution, each consume B in the pre-process object set of process P shall be consumed and stop to exist at the beginning of the lowest level sub-process of P which consumes B. Each affected (an object whose state changes) B in the preprocess object set of process P shall exit from its input state at the beginning of the lowest level sub-process of P.

##### Post-process object set and process post-condition

A set of objects, comprising one or more results, some possibly at given states, and/or affects, collectively called the post-process object set, shall result from executing a process and carrying out the transformations associated with its execution. Each resulted B in the post process object set of process P shall be created and start to exist at the end of the lowest level sub process of P which yields B. Each affected B in the post-process object set of process P shall enter its output state at the end of the lowest level sub-process of P.

## Control links

An event link and a condition link express an event and a condition, respectively. Control links occur either between an object and a process or between two processes.

## Event links

Triggering a process initiates an attempt to execute the process, but it does not guarantee success of this attempt. The triggering event forces an evaluation of the process' precondition for satisfaction, which, if and only if satisfied, allows process execution to proceed and the process becomes active. Regardless of whether the precondition is satisfied or not, the event will be lost. If the precondition is not satisfied, process execution will not occur until another event activates the process and a successful precondition evaluation allows the process to execute.

Basic transforming event links: A consumption event link is a link between an object and a process, which an instance of the object activates.

Consumption event link: Graphically, an arrow with a closed arrowhead pointing from the object to the process with the small letter e (for event). The syntax of a consumption event link OPL sentence is: Object triggers Process, which consumes Object.

Effect event link: Graphically, a bidirectional arrow with closed arrowheads at each end between the object and the process with a small letter e (for event). The syntax of an effect event link OPL sentence is: Object triggers Process, which affects Object.

##### Basic enabling event links:

Agent event link: An agent event link is an enabling link from an agent object to the process that it activates and enables. Graphically, a line with a filled circle ("black lollipop") at the terminal end extending from an agent object to the process it activates and enables with a small letter e (for event). The syntax of an agent event link OPL sentence is: Agent triggers and handles Process.

Instrument event link: Graphically, a line with an empty circle ("white lollipop') at the terminal end extending from the instrument object to the process it activates and enables with a small letter e (for event). The syntax of an instrument event link OPL sentence is: Instrument triggers Process, which requires Instrument.

##### State-specified transforming event links:

State-specified consumption event link: A state-specified consumption event link is a consumption link that originates from a specific state of an object and terminates at a process, which an instance of the object activates. Graphically, an arrow with a closed arrowhead pointing from the object state to the process with the small letter e (for event). The syntax of a state-specified consumption event link OPL sentence is: Specified-state Object triggers Process, which consumes Object.

Input-output-specified effect event link: An input-output-specified effect event link is an input-output-specified effect link with the additional meaning of activating the affecting process when the object enters the specified input state. Graphically, the input-output-specified effect link with a small letter e (for event). The syntax of an input-output specified effect event link OPL sentence is: Input-state Object triggers Process, which changes Object from input-state to output-state.

Input-specified effect event link: An input-specified effect event link is an input-specified effect link with the additional meaning of activating the affecting process when the object enters the specified input state. Graphically, the input-specified effect link with a small letter e (for event. The syntax of an input-specified effect event link OPL sentence is: Input-state Object triggers Process, which changes Object from input-state.

Output-specified effect event link: An output-specified effect event link is an output-specified effect link with the additional meaning of activating the affecting process when the object comes into existence. Graphically, the output-specified effect link with a small letter e (for event). The syntax of an output-specified effect event link OPL sentence is: Object in any state triggers Process, which changes Object to destination-state

##### State-specified agent event link:

State-specified agent event link: A state-specified agent event link is a state-specified agent link with the additional meaning of activating the process when the agent enters the specified state. Graphically, the state-specified agent link with a small letter e (for event). The syntax of a state-specified agent event link OPL sentence is: Qualifying-state Agent triggers and handles Processing".

State-specified instrument event link: A state-specified instrument event link is a state-specified instrument link with the additional meaning of activating the process when the instrument enters the specified state. Graphically, the state-specified instrument link with a small letter e (for event). The syntax of a state-specified instrument event link OPL sentence is: Qualifying-state Instrument triggers Processing, which requires qualifying-state Instrument."

## Invocation links

1. Process invocation

2. Self-invocation link

Implicit invocation link: Implicit invocation occurs upon sub-process termination within the context of an in-zoomed process, at which time the sub-process invokes the one(s) immediately below it. Graphically, there is no link between the invoking and the invoked sub-processes; their relative heights within the in-zoom context of their ancestor process implies this semantics.
