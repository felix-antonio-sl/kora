---
_manifest:
  urn: urn:fxsl:kb:opm-version-felix-p02
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
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:opm-version-felix
---

# Object Process Methodology (OPM) - Parte 02

## Condition links

A condition link is a procedural link between a source object or object state and a destination process that provides a bypass mechanism.

Condition consumption link: A condition consumption link is a condition link from an object to a process, meaning that if in run-time an object instance exists, then the process precondition is satisfied, the process executes and consumes the object instance. Graphically, an arrow with a closed arrowhead pointing from the object to the process with the small letter c (for condition) near the arrowhead shall denote a condition consumption link.

1. Condition effect link: However, if that object instance does not exist, then the process precondition evaluation fails and the control skips the process. Graphically, a bidirectional arrow with two closed arrowheads, one pointing in each direction between the affected object and the affecting process, with the small letter c (for condition) near the process end of the arrow.

1. Condition agent link: Graphically, a line with a filled circle ('black lollipop") at the terminal end extending from an agent object to the process it enables, with the small letter c (for condition) near the process end. The syntax of the condition agent link OPL sentence is: Agent handles Process if Agent exists, else Process is skipped.

1. Condition instrument link: Graphically, a line with an empty circle ("white lollipop") at the terminal end, extending from an instrument object to the process it enables, with the small letter c (for condition) near the process end, shall denote a condition instrument link. The syntax of the condition instrument link OPL sentence shall be: Process occurs if Instrument exists, else Process is skipped.

1. Condition state-specified consumption link: A condition state-specified consumption link is a condition consumption link that originates from a specified state of an object and terminates at a process, meaning that if an object instance exists in the specified state and the rest of the process precondition is satisfied, then the process executes and consumes the object instance. Graphically, an arrow with a closed arrowhead pointing from the object qualifying state to the process with the small letter c (for condition) near the arrowhead.

1. Condition input-output-specified effect link: A condition input-output-specified effect link is an input-output specified effect link with the additional meaning that if at run-time an object instance exists and it is in the process input state (and assuming that the rest of the process precondition is satisfied), then the process executes and affects the object instance. Graphically, the condition input-output-specified effect link with the small letter c (for condition) near the arrowhead of the input. The syntax of the condition input-output-specified effect link OPL sentence is: Process occurs if Object is input-state, in which case Process changes Object from input-state to output-state, otherwise Process is skipped.

1. Condition input-specified effect link: A condition input specified effect link is an input-specified effect link with the additional meaning that if at run-time an object instance exists in the specified input state and the rest of the process precondition is satisfied, then the process executes and affects the object instance by changing its state from its input state to an unspecified state. However, if that object instance does not exist at the input state, then the process precondition evaluation fails and the control skips the process. Graphically, the condition input-specified effect link with the small letter c (for condition) near the arrowhead of the input link. The syntax of a condition input-specified effect link OPL sentence is: Process occurs if Object is input state, in which case Process changes Object from input-state, otherwise Process is skipped.

1. Condition output-specified effect link: A condition output-specified effect link is an output-specified effect link with the additional meaning that if at run-time an object instance exists and the rest of the process precondition is satisfied, then the process executes and affects the object instance by changing its state to the specified output-state. However, if that object instance does not exist, then the process precondition evaluation fails and the control skips the process. Graphically, the condition output-specified effect link with the small letter c (for condition) near the arrowhead of the input link. The syntax of the condition output-specified effect OPL sentence is: Process occurs if Object exists, in which case Process changes Object to output-state, otherwise Process is skipped.

1. Condition state-specified agent link: The syntax of the condition state-specified agent link OPL sentence is: Agent handles Process if Agent is qualifying-state, else Process is skipped.

1. Condition state-specified instrument link

## Structural links

Structural links specify static, time-independent, long-lasting relations in the system. A structural link connects two or more objects or two or more processes, but not an object and a process, except in the case of an exhibition-characterization link.

##### Unidirectional tagged structural link

Has a user-defined semantics regarding the nature of the relation from one thing to the other. Graphically, an arrow with an open arrowhead. Along the tagged structural link, the modeler should record a meaningful tag in the form of a textual phrase that expresses the nature of the structural relation between the connected objects (or processes) and makes sense when placed in the OPL sentence whose syntax follows.

##### Unidirectional null-tagged structural link

A unidirectional tagged structural link with no tag. In this case, the default unidirectional tag is used. The modeler has the option of setting the default unidirectional tag for a specific system or a set of systems. If no default is defined, the default tag is "relates to".

##### Bidirectional tagged structural link

When the tags in both directions are meaningful and not just the inverse of each other, they may be recorded by two tags on either side of a single bidirectional tagged structural link. The syntax of the resulting tagged structural link is two separate tagged structural link OPL sentences, one for each direction. Graphically, a line with harpoon shaped arrowheads on opposite sides at both ends of the link's line shall.

##### Reciprocal tagged structural link

A bidirectional tagged structural link with one tag. In either case, reciprocity indicate that the tag of a bidirectional structural link has the same semantics for its forward and backward directions. When no tag appears, the default tag shall be "are related". The syntax of the reciprocal tagged structural link with only one tag shall be: Source-thing and destination thing are reciprocity-tag. The syntax of the reciprocal tagged structural link with no tag is: Source thing and Destination-thing are related.

##### Fundamental structural relations

The most prevalent structural relations among OPM things and are of particular significance for specifying and understanding systems. Each of the fundamental relations is elaborate or refine one OPM thing, the source thing, or refinee, into a collection of one or more OPM things, the destination thing or things, or refineables.

##### Aggregation-participation link

A refinee—the whole—aggregates one or more other refineables—the parts. Graphically, a black solid (filled in) triangle with its apex connecting by a line to the whole and the parts connecting by lines to the opposite horizontal base shall denote the aggregation-participation relation link.

##### Exhibition-characterization link

A thing exhibits, or is characterized by, another thing. The exhibition-characterization relation binds a refinee—the exhibitor—with one or more refineables, which shall identify features that characterize the exhibitor Graphically, a smaller black triangle inside a larger empty triangle with that larger triangle's apex connecting by a line to the exhibitor and the features connecting to the opposite (horizontal) base defines the exhibition-characterization relation link.

##### Generalization-specialization and inheritance

These are structural relations which provide for abstracting any number of objects or process classes into superclasses, and assigning attributes of superclasses to subordinate classes.

1. Generalization-specialization link

1. Inheritance through specialization

1. Specialization restriction through discriminating attribute: A subset of the possible values of an inherited attribute may restrict the specialization.

##### Classification-instantiation and system execution

Classification-instantiation link: A source thing, which is an object class or a process class connect to one or more destination things, which are valued instances of the source thing's pattern, i.e. the features specified by the pattern acquire explicit values. This relation provides the modeler with an explicit mechanism for expressing the relationship between a class and its instances created by the provision of feature values. Graphically, a small black circle inside an otherwise empty larger triangle with apex connecting by a line to the class thing and the instance things connecting by lines to the opposite base defines the classification-instantiation relation link. The syntax is: Instance-thing is an instance of Class-thing.

Instances of object class and process class

##### State-specified structural relations and links

State-specified characterization relation and link: An exhibition-characterization relation from a specialized object that exhibits a value for a discriminating attribute of that object, meaning that the specialized object shall have only that value. Graphically, the exhibition-characterization link triangular symbol, with its apex connecting to the specialized object and its opposite base connecting to the value, defines the state-specified characterization relation. The syntax is: Specialized-object exhibits value-name Attribute-Name.

State-specified tagged structural relations and links: A structural relation between a state of an object or value of an attribute and another object or its state or value, meaning that these two entities are associated with the tag expressing the semantics of the association. In case of a null tag (i.e., the tag is not specified), the corresponding default null tag is used. Three groups of state-specified tagged structural relations exist: (1) source state-specified tagged structural relation, (2) destination state-specified tagged structural relation, (3) source-and-destination state-specified tagged structural relation. Each of these groups includes the appropriate unidirectional, bidirectional, and reciprocal tagged structural relation, giving rise to seven kinds of state-specified tagged structural relation link and corresponding OPL sentences.

## Relationship cardinalities

### Object multiplicity in structural and procedural links

Object multiplicity shall refer to a requirement or constraint specification on the quantity or count of object instances associated with a link. Unless a multiplicity specification is present, each end of a link shall specify only one thing instance. The syntax of an OPL sentence that includes an object with multiplicity shall include the object multiplicity preceding the object name, with the object name appearing in its plural form. Multiplicity specifications may appear in the following cases:

to specify multiple source or destination object instances for a tagged structural link of any kind;

to specify a participant object with multiple instances in an aggregation-participation link, where a different participation specification may be attached to each one of the parts of the whole;

to specify an object with multiple instances in a procedural relation.

### Object multiplicity expressions and constraints

Object multiplicity may include arithmetic expressions, which shall use the operator symbols "+", "–", "*", "/", "(", and ")" with their usual semantics and shall use the usual textual correspondence in the corresponding OPL sentences.

An integer or an arithmetic expression may constrain object multiplicity. Graphically, expression constraints shall appear after a semicolon separating them from the expression that they constrain and shall use the equality/inequality symbols "=", "&lt;", "&gt;", "&lt;=", and "&gt;=", the curly braces "{" and "}" for enclosing set members, and the membership operator "in" (element of, ∈), all with their usual semantics. The corresponding OPL sentence shall place the constraint phrase in bold letters after the object to which the constraint applies in the form ", where constraint".

### Attribute value and multiplicity constraints

The expression of object multiplicity for structural and procedural links specifies integer values or parameter symbols that resolve to integer values. In contrast, the values associated with attributes of objects or processes may be integer or real values, or parameter symbols that resolve to integer or real values, as well as character strings and enumerated values. Graphically, a labelled, rounded-corner rectangle placed inside the attribute to which it belongs shall denote an attribute value with the value or value range (integers, real numbers, or string characters) corresponding to the label name. In OPL text, the attribute value shall appear in bold face without capitalization.

The syntax for an object with an attribute value OPL sentence shall be: Attribute of Object is value.

The syntax for an object with an attribute value range OPL sentence shall be: Attribute of Object range is value-range. A structural or a procedural link connecting with an attribute that has a real number value may specify a relationship constraint, which is distinct from an object multiplicity.

Graphically, an attribute value constraint is an annotation by a number, integer or real, or a symbol parameter, near the attribute end of the link and aligning with the link.

## Logical operators: AND, XOR, and OR

### Logical AND procedural links

The logical operators AND, XOR, and OR among procedural relations enable specification of elaborate process precondition and postcondition. Separate, non-touching links shall have the semantics of logical AND. Here, unlocking the safe requires all three keys.

### Logical XOR and OR procedural links

A link fan shall follow the semantics of either a XOR or an OR operator. The link fan end that is common to the links shall be the convergent link end. The link end that is not common to the links shall be the divergent link end.

The XOR operator shall mean that exactly one of the things in the span of the link fan exists, if the divergent link end has objects, or happens, if the divergent link end has processes. Graphically, a dashed arc across the links in the link fan with the arc focal point at the convergent end point of contact shall denote the XOR operator.

The OR operator shall mean that at least one of the two or more things in the span of the link fan exists, if the divergent link end has objects, or happens, if the divergent end has processes. Graphically, two concentric dashed arcs across the links with their focal point at the convergent end point of contact shall denote the OR operator.

##### State-specified XOR and OR link fans

##### Control-modified link fans

##### Link probabilities and probabilistic link fans

### Execution path and path labels

A path label shall be a label along a procedural link, which, in the case that there is more than one option to follow upon process termination, prescribes that the link to follow will be the one having the same label as the one which we entered the process.

## Modeling principles and model comprehension

The definition of system purpose, scope, and function in terms of boundary, stakeholders and preconditions is the basis for determining whether other elements should appear in the model. This determines the scope of the system model. OPM provides abstracting and refining mechanisms to manage the expression of model clarity and completeness.[1][4]

Stakeholder and system's beneficiary identification

For man-made systems this function is expected to benefit a person or a group of people—the beneficiary. After the function of the system aligns with the functional value expectation of its main beneficiary, the modeler identifies and adds other principal stakeholders to the OPM model.

### Procedure to start an OPM model

- System’s Main Functionality
 - Objective: Define the primary benefit expected from the system.
 - Write the name of the main process that provides this benefit.
 - The name must end with a verb in the gerund form (e.g., ending in “-ing”).
 - Question: What is the main process of the system?

- Beneficiary Group
 - Definition: A beneficiary is a stakeholder who gains value and benefits from the system.
 - Question: Who is the beneficiary of the system?
 - Note:
 - OPM objects must be singular.
 - To express plurals:
 - For inanimate objects, add the suffix Set.
 - For human groups, use the suffix Group.
 - The beneficiary group will have an attribute defined in the next stage.

- Beneficiary Attribute
 - Definition: The beneficiary attribute describes how the beneficiary group benefits from the system.
 - Question: What is the beneficiary attribute of the system?
 - The main process changes this attribute from:
 - Input state: The current, short-term state.
 - Output state: The desired, long-term state.
 - Questions:
 - What is the input state?
 - What is the output state?

- Agent
 - Definition: The agent is a human or group of humans who enable the transforming process.
 - The agent may or may not be the same as the beneficiary group.
 - Questions:
 - Is the beneficiary also the system agent? (Yes/No)
 - If there are additional enablers, list them here (maximum of 3, separated by “Enter”).

- System Name
 - Definition: The system is the instrument that enables the transforming process.
 - The default system name is:
 - The name of the main process followed by the word “system”.
 - Alternatively, you may define your own name.
 - Question: What is the name of the system?

- Instrument
 - Definition: An instrument is a tool or resource required for the transforming process.
 - Instruments are essential throughout the process but remain unchanged at its completion.
 - Question: What instruments are required for the transforming process?
 - Note:
 - OPM things must be singular. Use Set for inanimate objects or Group for human groups.
 - Limit to 3 tools, separated by “Enter”.
 - If some tools are physical, you can select them.

- Input
 - Definition: Inputs are objects consumed by the process.
 - Question: What are the inputs of the process?
 - Note:
 - Limit to 3 inputs, separated by “Enter”.
 - If an input is affected by the main process, it should later be defined as an output.

- Output
 - Definition: Outputs are the results created, affected, or changed by the transforming process.
 - Questions:
 - Is the output also an input?
 - What is the output of the system?
 - Select the output of the system.

- Environmental Objects
 - Definition: Environmental objects are external to the system but interact with it during the process.
 - Example: Electric energy in a “Pizza Making” process.
 - Question: What environmental objects are associated with the process?
 - You can select these objects from those previously defined.

### System diagram

The resulting top-level OPD is the system diagram (SD), which includes the stakeholder group, in particular the beneficiary group, and additional top-level environmental things, which provide the context for the system's operation. The SD should contain only the central and important things—those things indispensable for understanding the function and context of the system. The function is the main process in SD, which also contains the objects involved in this process: the beneficiary, the operand (the object upon which the process operates), and possibly the attribute of the operand whose value the process changes. SD should also contain an object representing the system that enables the function. The default name of this system is created by adding the word "System" to the name of the function. For example, if the function is Car Painting, the name of the system would be Car Painting System.

### OPD tree

Clarity and completeness trade-off

Establishing an appropriate balance requires careful management of context during model development. However, the modeler may take advantage of the union of information provided by the entire OPD set of an OPM system model and have one OPD which is clear and unambiguous but not complete, and another that focuses on completeness for some smaller part of the system by adding more details.

#### Refinement-abstraction mechanisms

OPM shall provide abstracting and refining mechanisms to manage the expression of model clarity and completeness. These mechanisms shall enable presenting and viewing the system, and the things that comprise it, in various contexts that are interrelated by the objects, processes and relations that are common amongst them.

#### State expression and state suppression

The inverse of state suppression shall be state expression, i.e., refining the OPD by adding the information concerning possible object states. The OPL corresponding to the OPD shall express only the states of the objects that are depicted.

#### Unfolding and folding

It reveals a set of things that are hierarchically below the unfolded thing. The result is a hierarchy tree, the root of which is the unfolded thing. Linked to the root are the things that constitute the context of the unfolded thing. Conversely, folding is a mechanism for abstraction or composition, which applies to an unfolded hierarchical tree.

#### In-zooming and out-zooming

In-zooming is a kind of unfolding, which is applicable to aggregation-participation only and has additional semantics. For processes, in-zooming enables modeling the sub-processes, their temporal order, their interactions with objects, and passing of control to and from this context. For objects, in-zooming creates a distinct context that enables modeling the constituent objects spatial or logical order. Graphically, the timeline within the context of an in-zoomed process flows from the top of its process ellipse symbol to the ellipse bottom.
