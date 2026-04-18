# Chapter 4 SysML: Use Case, Block, and State
Machine Diagrams
SysML supports the specification, analysis, design, verification, and validation of a
broad range of complex systems. These systems may include hardware, software,
information, processes, personnel, and facilities.
OMG SysML, v1.3 p.1 ( )
Accessed June 20, 2014
We leave OPM for a while and turn to start our parallel SysML model. SysML is a multi-view language,
where each view uses a different type of diagram. There are nine SysML diagram types in total. In this
chapter we are exposed to three diagram types: the use case diagram, the block definition diagram, and
the state machine diagram. The use case diagram shows the context of the system and how the system is
used to bring value to at least one of its actors. The block definition diagram presents the blocks of the
system—major entities of interest. The state machine diagram shows how states of blocks in the system
are changed. Comparing OPM and SysML, we already see that the approaches they take are different and
complementary. OPM uses a single model that combines the various system aspects, while SysML uses a
number of diagram types, each focusing on some particular aspect of the system.
A use case is a way the system is used, a service it provides to at least one of its users.
## 4.1 The SysML Use Case Diagram
We start our model with the use case diagram, since this is the view that is used to elicit requirements
and to provide initial understanding of the system and its surroundings.
According to the OMG SysML 1.3 (2012) standard, a use case diagram “describes the usage of a
system (subject) by its actors (environment) to achieve a goal that is realized by the subject providing a
set of services to selected actors” (OMG SysML 1.3, 2012, p.145).
Before drawing use case diagrams, use cases need to be written in text. This text takes on different
formats. Depending on need, use cases are written in varying degrees of formality. They can be
brief—short one-paragraph summary, usually of the main success scenario;
casual—informal paragraph format, where multiple paragraphs describe various scenarios; and
fully dressed—the most elaborate level, where all the steps and variations are written in detail,
and there are supporting sections, such as preconditions and success guarantees.
Figure 4.1 is a preliminary use case diagram of the Automatic Crash Response (ACR) system.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_

SysML: Use Case, Block, and State Machine Diagrams
The name of the use case in our use case model is “Automatically respond to crash.” As Fig. 4.1
shows, the use case is depicted as an oval with the name inside it. The system users are called actors.
An actor is an external entity that interacts with the system and can get services from
it.
An actor is depicted either as a human stick figure, or as the stereotype «actor»; see Table 4.1. Two
actors appear in the use case diagram in Fig. 4.1: Vehicle Occupants and Advisor. An actor is by
definition an external entity. Unlike OPM, SysML does not require that the actor be a person; it can be
anything with which the system interacts.
### Figure 4.1
A preliminary SysML use case diagram of the Automatic Crash Response (ACR) system
Vehicle Occupants are undoubtedly an external entity, since they are not part of the system, but
rather its users and beneficiaries. The case for the Advisor is not that clear-cut, since the Advisor can be
considered as part of the system, and rather than getting a service from the system, she is the one that
provides the service. However, the requirement that an actor gets a service is not mandatory, and as a
human, the Advisor interacts with the system. In this model, we exclude humans from being considered
part of the system; hence Advisor is also an actor. Each one of the two actors is linked to the use case via
a communication path—a line between the actor and the use case.
The system which provides the required function in a use case diagram is called subject.
A subject in a use case diagram is the system that provides the service.

A use case subject is depicted as a rectangle with the subject name at the rectangle's top center. As
### Figure 4.1
shows, the subject in our use case diagram is called ACR-System.
The entire use case diagram is depicted within a diagram frame—a rectangle that is required for any
SysML diagram. In its upper leftmost corner, a diagram frame has name tag—a rectangle with a tapered
bottom right corner—which contains the heading name. The heading name has the following syntax:
<diagramKind> [modelElementType] <modelElementName> [diagramName]
The fields diagramKind, which is bolded, and modelElementName are mandatory. Each diagramKind
has a two or three lower case letter abbreviation. As shown in Fig. 4.1, the diagramKind of our use case is
uc, while the diagramName is ACR-System. The two other tokens, modelElementType and
diagramName are optional, and if they appear, they are enclosed within brackets, enabling the diagram
reader to tell them apart.
Table 4.1 lists the main elements of a use case diagram, their semantics and symbols.
Table 4.1 The main elements of a use case diagram, their semantics and symbols
Guillemets, also known as the symbols for rewind («) and fast forward (»), are angle quotes, as the
ones surrounding the following word: «guillemets». In SysML, a word within a pair of guillemets denotes
a stereotype—an extensibility mechanism that enables creating new model elements.
A stereotype is depicted as a rectangular box with the stereotype name, such as “block” within a pair
of guillemets, «block», recorded in the top middle of the box, as is the case with «actor» in Table 4.1. The
name of the actor, ActorName, is recorded beneath the «actor» stereotype notation.

SysML: Use Case, Block, and State Machine Diagrams
## 4.2 SysML Blocks and the Block Definition Diagram
A SysML block is a modular component which defines a collection of features that describe a part of the
system or another element of interest. A SysML block, which roughly corresponds to a UML class, may
include both structural and behavioral features, such as properties and operations. A block can include
properties to specify its values, parts, and references to other blocks.
The block definition diagram captures the definition of blocks in terms of properties and operations,
and relationships, such as a system hierarchy or a system classification tree. A related SysML diagram is
the internal block diagram (ibd), which captures the internal structure of a block in terms of properties
and connectors between properties.
A SysML block definition diagram (bdd) defines features of blocks and relationships
between blocks, such as associations, generalizations, and dependencies.
### Figure 4.2
A preliminary block definition diagram of the Automatic Crash Response (ACR) system
Figure 4.2 is a preliminary block definition diagram (bdd) of the Automatic Crash Response (ACR)
system. The diagramKind, bdd, denotes this. This bdd expresses the two major blocks of the system and
the relation between them, as well as the major actors and their relations the blocks.
This two blocks in the bdd are ACR-System and Automatic-Crash-Response. They are linked by the
ReferenceAssociation labeled “provides”. Advisor is shown as an actor which is part of the ACR-System.
This whole-part relation is expressed by the black diamond, the SysML symbol for whole-part relation.

Vehicle Occupants is another actor. It is linked by the ReferenceAssociation labeled “benefit from” to the
Automatic-Crash-Response block (Fig. 4.2).
Table 4.2 The main elements of a block definition diagram, their semantics and symbols
Element:
Symbol
Semantics
Block
A modular component which defines a col-
lection of features to describe a part of the
system or another element of interest.
«block»
BlockName
Actor:
An external entity that interacts with the
system and can get services from it
«actor»
ActorName
ActorName
ReferenceAssociation:
A link between blocks indicating the nature
of their association
association1 property1
0..1
{ordered} 1..*
PartAssociation:
A link between blocks indicating that the
block linked to the diamond is the whole
association1 property1
0..1
{ordered} 1..*
Generalization:
A link between two block indicating that the
block linked to the triangle is the general one
## 4.3 SysML State Machine Diagram
SysML has a diagram type that is dedicated to modeling states of a block and possible transitions among
them—the state machine diagram, or stm in short. Following the idea presented initially by Harel (1987,
1988), the SysML State Machine package defines a set of concepts that can model discrete behavior
through state transitions. The state machine can represent behavior, expressed as the state history of an
object in terms of its transitions and states.
Figure 4.3 is a SysML state machine diagram (stm) of the Vehicle Occupants Group. It is similar to
the OPD in Fig. 2 .3 in that both contain the same two states for the Vehicle Occupants Group. The stm
symbol used to denote a state is a rountangle—the same as in OPM. The main difference between the two
is that stm is not of the entire ACR system. Rather, it is only of the Vehicle Occupants Group block. The
OPM process Automatic Crash Responding is expressed in the stm as a trigger by the same name, which
causes the transition from the possibly injured state to the being helped state.
The black circle in Fig. 4.3 is the initial state. This state is referred to as a pseudo state since it is not a
real state, just an indication to the diagram reader where to start. It is linked to the initial state, possibly
injured, of the block whose state machine is modeled, which in our case is Vehicle Occupants Group. The
black circle with the white rim in Fig. 4.3 is the final (pseudo) state—it is pointed to by the (real) final
state—being helped. These two symbols enable identification of the initial and final states in a state
machine diagram, respectively. As we shall see later, OPM denotes an initial state using a bold line of the

SysML: Use Case, Block, and State Machine Diagrams
state rountangle frame, and a final state—by a double rountangle frame. This eliminates the need for the
two kinds of pseudo states that SysML uses.
### Figure 4.3
A SysML State Machine diagram (stm) of the ACR system
Table 4.3 The main elements of a state machine diagram, their semantics and symbols

Table 4.3 shows the main elements of a state machine diagram, their semantics and symbols. As the
table shows, a state can be composite and contain inner, lower-level processes. A transition can be
labeled, in addition to a trigger, also by an optional guard in brackets and one or more optional activities
that syntactically follow the backslash symbol (\), which are actions done during the transition.
## 4.4 Summary
SysML has nine types of diagrams that model various aspects of the system
The use case diagram is often the first to be prepared since it provides the context of the system
and how actors interact with it.
Block is a basic unit, akin to class in UML, used in the block definition diagram and internal
block diagram. It serves to define the structure of the system.
State machine diagram is a SysML diagram that specifies the possible states of relevant blocks
in the system and transitions between these states.
## 4.5 Problems
1. Draw a SysML use case diagram of the system described below.
A passenger arriving at an airport deposits her baggage with the airline she is flying with. A
baggage handling system manages the transfer of the baggage to the passenger’s destination.
2. 3. 4. 5. 6. Draw a block definition diagram of the system in the system described above.
Baggage Location has states passenger, origin airport, aircraft, destination airport, other
location. Model this using a SysML state machine diagram and indicate what causes transitions
between states.
Compare the three types of diagrams created in the three problems above in terms of their
information content.
What can be said about the system by looking at each diagram alone?
How can the information be integrated to obtain a complete view of the system?
