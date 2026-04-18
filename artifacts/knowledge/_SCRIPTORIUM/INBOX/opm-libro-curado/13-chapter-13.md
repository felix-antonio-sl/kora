# Chapter 13 The Dynamic System Aspect
Every day we are confronted with systems that have an inherent tendency to change.
The weather, the stock market, or the economic situation, are examples.
Meinhardt (1995)
Systems change over time. An important motivation in the development of OPM has been to strike a
needed balance in a system’s conceptual model between the structural, static and procedural, dynamic
aspects of the system. The dynamic aspect of a system specifies how the system operates to attain its
function, complementing its static aspect. OPM is at least process-oriented as it is object-oriented. Indeed,
OPM models unify structure and behavior in one coherent frame of reference, with time being the
fundamental underlying concept. This chapter addresses modeling the dynamics aspect of a system.
## 13.1 Change and Effect
Processes and system dynamics are closely associated with the notion of change. Change is such a
familiar and basic concept that defining it seems both difficult and unnecessary. However, when we talk
about a change in OPM, we need to be specific about what a change means.
A change of an object is an alteration in the state of that object.
More specifically, a change of an object is replacing its current state by another state. The only thing
that can cause this change is a process. The process causes the change by taking as input an object at
some state—the input state, and outputting it in another state—the output state. Hence, a change of an
object means a change in the state the object is at.
Stateful objects can be affected, i.e., their states can change. This change mechanism underlines the
intimate, inseparable link between objects and processes. We call this change in state the effect of the
process on the object.
Effect is a change in the state of an object that a process causes by its occurrence.
While the terms “change” and “effect” seem almost synonymous, there is a subtle difference in their
usage. We use effect to refer to what the process does to the object, and change—to what happens to the
object as a result of the process occurrence. Later in this section we refine the above definition of effect
with the notions of input and output links.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 13

The Dynamic System Aspect
## 13.2 Existence and Transformation
In Sect. 10.3.2, we have defined transformation of an object by a process as the generalization of
construction, effect, and consumption. Construction is synonymous with creation, generation, or yielding.
Effect is synonymous with change or switch, and consumption is synonymous with elimination,
termination, annihilation, or destruction. The effect of a process on an object is to change that object from
one of its states to another, but the object still exists, and it keeps maintaining the identity it had before
the process occurred. Construction and consumption change the very existence of the object and are
therefore more profound transformations than effect. When we say that a process constructs (yields,
generates, creates, or results in) an object, we mean that the object, which had not previously existed, has
undergone a radical transformation and is now a new, separate entity. When we say that a process
consumes (eliminates or destroys) an object, we mean that the object, which had previously existed, has
undergone a radical transformation so it no longer exists in the system.
## 13.2.1 Construction and Consumption: Extreme Object Changes
When we consider existent and non-existent as states of an object, construction and consumption become
extreme cases of object state changes, as
### Figure 13.1
presents using nine OPDs. The rows in this 3×3 matrix are three stages of transformation
evolution of three objects, Constructed Object, Existing Object, and Consumed Object. The horizontal
axis (the three columns) represents the kind of object transformations, from constructive on the left to
destructive on the right. Accordingly, there are three corresponding processes: Constructing on the left
column, Changing in the middle, and Consuming on the right.
The vertical axis (the three rows) represents the level of detail, from the most detailed at the top row to
the most abstract at the bottom row. In the top row, all the states of all three objects are expressed, and
input-output link pairs originate from and arrive at these states. In the middle row, since the state non-
existent of Constructed Object and the state non-existent of Consumed Object do not exist, they are
removed along with the links connecting them. Also, edges of the remaining transforming links in all
three columns have migrated from the states to the contour of the object box. This is an interim stage
aimed at showing the evolution of links. Finally, in the bottom row, all the remaining states are
suppressed, showing the final three transforming links: result, effect, and consumption links. The effect
link (bottom center) is an abstraction of the input-output link pair (top center), in which the states are
suppressed such that the semantics of the effect link is a change in the states of the object from some
unspecified input state to another unspecified output state.
The use of the states non-existent and existent of an object is useful when we wish to explicitly model
that the object is present in or missing from the system. For example, we have used it to model molecular
biology concepts such as removal of a factor or gene knockdown (Somekh et al. 2014).
## 13.2.2 Change of State or Change of Identity?
During their life, objects can undergo a host of transformations. Transformation of an object can, by our
definition, take place only when a process acts upon the object. This transformation generates, affects, or
eliminates the object. The extent of the change can vary from very small to very large. If the change is

small, such as a change in the location of the object or in its color, we tend to say that the object was
altered from one of its states to another while keeping its identity. As the extent of the effect grows, so
does the difference between the object before the process started and after it ended. At some point, the
two become so conceptually different that the modeler is inclined to think of the object resulting from the
process as a newly created object. The object that had existed before the process took place may have
been eliminated or at least changed radically. As we show below, the issue of whether an object changed
only its state or its entire identity is similar in natural and artificial systems.
Construction
Effect Consumption
Stage
change
presentation
via input-
output link
pair
Constructed Object
Existing Object Consumed Object
existent
source
destination
non-existent non-existent
existent
state
state
Constructing Affecting Consuming
Non-existent
states
removed;
links
migrated
Constructed Object Existing Object Consumed Object
existent
source
state
destination
state
existent
Constructing Affecting Consuming
All states
removed,
input-output
link pair
joined,
resulting in
result,
effect, and
consumption
links
Constructed Object Existing Object Consumed Object
Constructing Affecting Consuming
### Figure 13.1
Construction and consumption as extreme cases of effect
## 13.2.3 Transformations in Living Organisms
In nature, living organisms undergo a striking variety of transformations. Some of the transformations are
deemed as just a change in state, while others are considered to be a change in the organism’s identity.
The transformation from a cub to a grown-up lion is considered a change in the state of a lion from young
to adult. Similarly, growing of a baby into an adult is considered a change in the person’s state. The

The Dynamic System Aspect
silkworm, on the other hand, has four distinct forms of existence. It transforms from egg to larva (worm,
or caterpillar) to pupa, the larva undergoes complete transformation within a protective cocoon or
hardened case, to butterfly, which, in turn, lays the eggs of the next silkworm generation. Each
transformation yields an object that is very distinct from its predecessor in shape and function. The
difference is so profound that each such transformation is called metamorphosis. We are inclined to view
each reincarnation as a separate object rather than a mere change of the same object’s state. A frog, like
other amphibians, transforms from spawn to egg to tadpole to legged tadpole to froglet to adult, providing
an example similar to the silkworm.
### Figure 13.2
Two concurrently simulated models of Frog lifecycle. Left: Change of object state. Right: Change of object
identity
Figure 13.2 shows an OPCAT screenshot of two OPM models that are simulated concurrently. The
model on the left shows Frog as a single object with six states: spawn, egg, tadpole, legged tadpole,
froglet, and adult. Thanks to the invocation links, once invoked by externally activating Splitting, this
model completes a whole cycle from spawn to adult.
The model on the right shows six different stateless objects of the various incarnations of frog: Spawn
Frog, Egg Frog, Tadpole Frog, Legged Tadpole Frog, Froglet Frog, and Adult Frog (here each process

needs to be invoked separately; this can be avoided if we replace each consumption link, e.g., the one
from Egg Frog to Hatching, with an event consumption link). At this point of the simulation the process
Legs Growing is active (as the dark color and points along the arrows show). The pertinent OPL sentence
for the model on the left is:
Legs Growing changes Frog from tadpole to legged tadpole.
The pertinent OPL sentences for the model on the right is:
Legs Growing consumes Tadpole Frog.
Legs Growing yields Legged Tadpole Frog.
The frog and silkworm examples are conveniently thought of as changes of object although
genetically they are the same organism, because the various incarnations of these creatures are profoundly
different from each other in both appearance and behavior. The human and lion examples, on the other
hand, are more naturally modeled as a change of the object’s state.
## 13.2.4 Transformations of Artificial Objects
The situation with transformations of artificial objects is similar to natural ones: If the change is profound,
objects change identity, otherwise, the same object just alters its state. What transformation is “profound”
is subjective and context-sensitive. Consider, for example, two processes from a manufacturing realm:
Molding and Testing. Molding acts on the object Raw Material (e.g., plastic), converting it to another
object, that we call Product. The identity of Raw Material changed as a result of the Molding process to
the extent that we need to refer to the process outcome by a different name. Hence, the object Raw
Material has been eliminated or consumed, while a new object, called Product, has been created (or
constructed, or generated). We can model the relation between the two objects, for example by adding a
tagged structural relation from Product to Raw Material with the tag “is made of”, which will result in the
OPL sentence Product is made of Raw Material.
Suppose Product now undergoes the process of Testing, in which its shear strength is measured. If the
test succeeds, Product is approved, otherwise it is rejected. Unlike the Molding process, which altered the
identity of the processed object from Raw Material to Product, Testing does not change Product to the
extent that we would be inclined to say that it lost its identity. Instead, the only effect of the Testing
process is to alter the state of Product (from untested to tested). While there is a difference between
Product before and after the Testing, (since after the test we have information about the product’s
strength, which we did not have before), this difference is not profound enough to justify change of
identity. However, it does cause a change in state. Hence, transformation can be thought of as a general
term that encompasses creation, effect (change of state) and elimination of an object. We will elaborate
on this when discussing system dynamics.
The criterion for whether the process changes the object’s state or the object’s identity is whether it is
possible and makes sense to create an attribute which the object in question exhibits with the same values
as the states of the object. In our case the attribute of Product would be Testing Status object with the
same values, pre-tested and tested. If this is possible, as is the case here, then the change is only in the
state of the object but not in its identity. If not, as is the case in the Raw Material to Product example—the
change is in the object identity.

The Dynamic System Aspect
Generalizing the natural and artificial examples, when the change is not profound or drastic, we are
inclined to think that the object only alters its state while retaining its identity. When the transformation is
extreme, a change in object identity takes place. As is the case in similar situations, the borderline
between “drastic” and “non-drastic” is not well-defined. Analyzing the same system, different modelers
may provide different viewpoints on whether a particular object should lose its identity and become a new
object. Indeed, we will see instances where it makes sense to model changes in objects either as a change
in their state (or attribute value), or as a change in their identity, and both versions would be acceptable.
## 13.3 Procedural Links
Procedural links are the indispensable “mortar” between processes and objects or their states. They
provide for integration of the system’s structure and behavior within a single model. Procedural links are
of utmost importance.
A procedural link is a link between a process and an object or its state, or between
two processes.
The majority of procedural links are between a process and an object or its state. The only three
procedural link kinds between two processes are the invocation link and the overtime and undertime
exception links discussed in Chap. 22. As discussed in Sect. 10.10.3 an invocation link may replace a
transient, short-lived physical or informatical object that a source process creates to initiate the destination
process, which immediately consumes the transient object. This is also true for the exception links (where
the object may be a message). Therefore we often omit the last part of the procedural link definition and
say that a procedural link is a link between a process and an object or its state.
The structure-behavior integration that procedural links provide is one of the most important features
of OPM. This integration within a single model eliminates in the first place the inherent diagram kind
multiplicity problem (Peleg and Dori 2000) that are characteristic of object-oriented methods such as
UML and SysML, whose ontology is far from being minimal.
## 13.3.1 Transforming Versus Enabling Procedural Links
The definition of OPM process requires that the process transforms at least one object. In addition to the
object(s) being transformed, the process can also require one or more objects that enable that process, but
are not transformed by it. Hence, from the viewpoint of a given process, OPM distinguishes between two
types of objects: a transformee—an object that the process transforms (generates, affects, or consumes),
and an enabler—an object that enables the process but is not transformed by that process. Accordingly,
there are two types of procedural links: transforming links and enabling links.
## 13.3.2 Transformees
We have defined transformee of process P is an object B that P transforms as a result of its occurrence.
The transformation can be construction, effect (change of state) or consumption. Transformee is a role
that the object B assumes with respect to the particular process P. so B can be a transformee with respect

to some process P1 and an enabler with respect to another process P2. A transformee can be one of three
types defined below.
A consumee of a process P is a transformee of P that P consumes as a result of the
occurrence of P.
A resultee of a process P is a transformee of P that P creates as a result of the
occurrence of P.
An affectee of a process P is a transformee of P that that P affects as a result of the
occurrence of P.
In the bottom line of Fig. 13.1, Consumed Object, Constructed Object, and Existing Object are the
consumee, resultee, and affectee, respectively. A consumee can be thought of as an input to the process,
as the process consumes it, and a resultee—an output of the process, as the process creates it. An affectee
is both input and output: the process takes it in its input state and outputs it in its output state.
These analogies are definitely true for physical objects. However, an informatical object can serve as
input to a process without being consumed in whole or in part. For example, suppose in Fig. 13.3 a File in
a database is erased by an Erasing process, then File is a consumee of as well as an input to Erasing. If
File is created by a Creating process, then File is a resultee as well as an output of Creating. If the File is
edited (such that data is added to, changed, or removed from the file) by an Editing process, then File is an
affectee of Editing, as well as both input and output.
If the File is read from via a Reading process, then File is an input to this process, but it is not
consumed or changed in any other way—it serves as an instrument for Reading, as we discuss below. A
physical object, such as a resource, which is an input to a process, is consumed by the process, at least in
part. There are many physical objects, such as a Hammer—a tool for the process of Nail Driving, that are
instruments and are essentially unchanged by the process which they enable.
## 13.4 Transforming Links
Transforming links are unidirectional or bidirectional arrows connecting the transformee to the process
which transforms it.
A transforming link is a procedural link that connects a process with a transformee of
that process.
Figure 13.3 shows the links between File on one hand and File Creating, File Editing, and File Deleting
on the other hand as examples of result, effect, and consumption links, respectively. These are
specializations of a transforming link, as defined below.
In Fig. 13.4, Processing is linked to three Transformee specializations: Consumee, Affectee, and
Resultee via their corresponding transforming links—consumption, effect, and result links.

The Dynamic System Aspect
### Figure 13.3
Result, effect, and consumption link between File and File Creating, File Editing, and File Deleting,
respectively
A result link is a unidirectional transformation link from a process to the resultee that
this process creates.
An effect link is a bidirectional transformation link that connects a process with an
affectee of that process.
A consumption link is a unidirectional transformation link from a consumee to the
process that consumes it.
### Figure 13.4
Processing linked the three transformee types by their corresponding transforming links Enablers
## 13.4.1 Consumption and Result Timing
Existence of a consumee is a precondition, or part of the precondition, for process activation. If the
required amount of consumee instances (usually 1) does not exist at the time of process initiation, then
process activation shall wait for that amount of consumee instances to become existent. The consumption
of the consumee instance(s) is immediate upon process activation, unless the model expresses
consumption of the object over time, in which case consumption rate, a specialization of transformation
rate, is used, as explained below.

### Figure 13.5
Consumption and result timing: Steel Rod is consumed and disappears as soon as Machining starts. Shaft is
created only when Machining ends
In Fig. 13.5, Steel Rod is a consumee for the process Machining, which generates the resultee Shaft.
Once Machining has started, it consumes Steel Rod. However, Shaft is considered to be created only upon
termination of Machining. During the process, Steel Rod does not exist anymore, but neither does Shaft.
## 13.4.2 The Evolution of Effect Link
Explicitly expressing the states of an object in the diagram often yields an OPD that is too detailed,
crowded or busy, making it hard to read. This is a manifestation of the comprehensiveness-clarity
tradeoff: these two desired qualities of complex system models are in constant conflict.
### Figure 13.6
The evolution of the effect link
Figure 13.6 shows state suppression and the evolution of the effect link, similar to the middle column
in Fig. 13.1. In the middle OPD, the input and output links, which on the right OPD are attached to the
state rountangles, migrate to the boundary of the Lamp object box. They now link the process and the
object directly, going from and to the object itself rather than from and to its states. This interim
representation is not valid in OPM. To reduce the graphic clutter, the input and output links, denoted by
two opposite unidirectional arrows, have been superimposed by joining them into one bidirectional arrow,
yielding the symbol of the effect link. Finally, on the left, the states of Lamp have been suppressed,
because they are no longer vital since the links are not attached to them.
## 13.5 Enablers
Suppose you wish to move from your place to an apartment in another city. To do this, you need a
moving truck, which you rent from a moving truck rental company. You return the truck to the same
place where you took it and with the same amount of gasoline as you took it. Hence, ignoring the
amortization of the truck, nothing in it has changed. However, you would not be able to carry out the

The Dynamic System Aspect
moving without it. We say that the Truck is an enabler of the Moving process. Moreover, since some of
your furniture are very heavy, you need a Friend as a second enabler of the Moving process.
An enabler of a process is an object that enables the process execution. Its presence is needed
throughout the duration of the process, but when the process is over, the enabler exists at the same state as
it was when the process started. In other words, an enabler of a process is an object that must be present
throughout the process duration in order for that process to occur and terminate successfully, but is not
transformed as a result of the occurrence of the process.
An enabler E of a process P is an object that must exist and be available in order for
P to start, and remain present throughout the occurrence of P in order for P to
terminate normally, with E ultimately unaffected.
The enabler might undergo state change during the process, but, as the enabler definition states, when
the enabled process is over, the enabler is at the same state at which it started. For example, the enabler
Oven in Fig. 13.7 will change state from off to on at the beginning of the enabled Baking process, and
from on back to off just prior to the end of Baking.
As the Moving example has shown, some enables are human, while others are inanimate. Hence, an
enabler has two specializations: an agent or an instrument, as defined below.
## 13.5.1 Agent: A Human Enabler
The term agent is reserved for a human enabler.
An agent is an enabler who is a human or a group of humans.
An agent is an intelligent enabler, who can control the process it enables by exercising common sense
or goal-oriented considerations, implying that it must consist of one or more humans. Usually, it is a
single person—the system’s user or beneficiary. An agent can also be an organization, or a unit within a
man-made organization, such as department, city council, government, group, team, etc.
The notion of agent is important because it provides for modeling the “human in the loop”, i.e., how
people interact with the system. This is a clear indication to the system designer of points of interaction
with the system where human interface needs to be developed. Moreover, the hierarchy of processes that
the agent is involved in provides an excellent guideline for the arrangement of a friendly graphic user
interface, and creation of such interface can even be automated to some extent based on this model.
In the world of software and embedded systems, robots are often referred to as agents, and software
agents are common in the Internet, capitalizing on evolving agent technologies. In OPM, which is geared
to model all kinds of systems, including complex socio-technical systems and systems where humans are
users and beneficiaries, humans (as individuals or groups) are privileged and distinguished from all the
other inanimate enablers, so the term agent is reserved for humans only.1 This enables focusing the
attention of system architects and designers to care for humans’ safety and special needs and desires
1A robot can still be called an embedded-software agent, and programs acting in the Internet on behalf of humans can
still be called software agents. Agent without any qualification is reserved for individuals or groups of humans.

while interacting with the rest if the system—the system’s usability and the users’ experience and delight
from using a well-designed and human-friendly and accommodating system.
The agent link is somewhat analogous to the actor—the “stick figure” in UML’s or SysML’s use-case
diagram. In OPM, however, no separate kind of diagram is needed, as modeling the user is incorporated
into the single OPM model. Use cases in SysML notation can automatically be extracted from the OPM
model, as can other SysML models (Grobshtein and Dori 2011).
Not any human or organization is necessarily only an agent. For example, if a Student is engaged in
the process of Studying, his or her Knowledge Level attribute change, say from shallow to deep. In this
case, Student is not only an agent, but also a transformee. Likewise, if a department in an enterprise is
undergoing business process reorganization, its structure and/or behavior changes as a result of this
process, so in addition to being an agent, it is also a transformee.
The procedural link uniqueness OPM principle states that at any level of detail, an object and a
process can be connected with at most one procedural link. Semantic strength and link precedence are
defined and discussed in detail in Chap. 21. Here we note only that transforming links are semantically
stronger than enabling links, because the transforming links denote creation, consumption, or change of
the linked object, while the enabling links only denote enablement. A transforming link has precedence
over an enabling link as shown in Fig. 21.15, therefore if we need to choose between an agent link and an
effect link, as in the examples above, effect link shall be chosen.
## 13.5.2 Instrument: A Non-Human Enabler
An instrument of a process is any non-human, physical or informatical object, which does not change as a
result of the execution of the process.
An instrument is a non-human enabler.
Examples of instruments include machines, tools, computers, robots, controllers, hardware, software,
documents, orders, recipes, algorithms, prescriptions, files, commands, information, and data. Algorithms
and recipes are prime examples of informatical instruments that can be used repeatedly, ideally without
wearing out (in practice we may witness “software amortization” as well…).
Physical instruments usually change to some extent as they enable a process. In particular, they can
wear out or degrade as they are being used as process enablers. Yet, from the viewpoint of the system
under development, such objects would still be considered instruments, as these changes are either not
significant enough to be accounted for, or they are out of the system’s scope.
In other cases, wear and tear are factors to be considered. For example, in developing a Manufacturing
System, a system architect may be required to account for Maintaining a Machine that wears out due to
the Metal Cutting process it enables. In this case, the Machine should not be assigned the role of an
instrument. Rather, it will be modeled as an affectee. The attribute of the Machine that changes as a result
of its operation can be, for example, its Amortization Level, or hours of operation since the last overhaul.
We will have to take this Machine Wearing process in account if our system encompasses the
maintenance aspect of the Machine. The distinction in an OPD among the two types of enablers—agents
and instruments—is made possible by their connection to the process they enable through the different
enabling links, defined next.

The Dynamic System Aspect
## 13.5.3 Enabling Links: Agent and Instrument Links
Enables are linked to processes through enabling links.
An enabling link is a procedural link that connects a process with an enabler of that
process.
An agent link is an enabling link that connects a process with an agent of that process.
An instrument link is a procedural link that connects a process with an enabler of that
process.
### Figure 13.7
Enabling links example: The agent link from Baker and the instrument link from Oven
Graphically, as Fig. 13.7 shows, an enabling link is a “lollipop”, a line leading from the enabler
(Baker) to the process (Cake Making) it enables, which ends with a circle touching the process side. If the
enabler is a human or a group of humans, the enabling link is an agent link, denoted as a “black lollipop”,
i.e., its ending circle is filled in (black).
The distinction between a human and a non-human enabler is important, since for humans to interact
with the system, a dedicated interface needs to be designed. Hence, an optional stick figure can be added
at the top-left corner of the agent’s object symbol, as shown in Fig. 13.7. This optional stick figure is
especially useful when the human in the model is an affectee, i.e., she or he is affected by the process to
which it is linked, in which case we must use the effect link rather than the agent link. In this case, the
stick figure retains the information that a human is involved.
If the enabler is an instrument, the enabling link is a “white lollipop”, i.e., its ending circle is blank
(white). The two OPL sentences associated with these links are:
Agent handles Processing.
Processing requires Instrument.
The OPL syntax of the first (agent) sentence is designed such that the agent appears first, followed by
the reserved OPL phrase handles, followed by the process name. For the instrument sentence, the OPL
syntax is such that the process name appears first, followed by the reserved OPL phrase requires, followed
by the instrument name. This difference in both the OPL phrases and the order of the enablers in the
sentences underlines that being humans, agents are more important than instruments.

All the process enablers must be present throughout the execution of the process which they enables.
For example, in Fig. 13.7 both the agent Baker and the instrument Oven must be present throughout a
Cake Baking process.
### Figure 13.8
The same object playing the roles instrument and affectee: Moving Truck is an instrument of Moving and an
affectee of Servicing
## 13.5.4 Enabler Versus Affectee
Enabler and affectee are possible roles that an object plays with respect to some processes. The same
object can be an enabler for one process but not for another, or it can be an enabler for one process and an
affectee for another. For example, the (environmental) process Servicing in Fig. 13.8, which the moving
company applies periodically to its Moving Truck, changes the state of Moving Truck from in need of
service to serviced, hence Moving Truck is an affectee of Servicing. However, with respect to the
(systemic) process Moving, Moving Truck is an enabler—an instrument for Moving, while Location of
Furniture is an affectee, as Moving changes the value (attribute state) of the Location attribute of Furniture
from old apartment to new apartment.
## 13.6 The Preprocess and Postprocess Object Sets
Recall that the involved object set is the union of the preprocess object set and postprocess object set.
As Fig. 13.9 shows, if the involved object-set contains enablers (agents and/or instruments), they are
common to the preprocess and postprocess object sets, because their presence is required throughout the
duration of the process they enable. Each process has its own involved object set, preprocess object set,
and postprocess object set, and each can contain any number of objects.
Affectees are also common to the pre-process and post-process object sets, because they had existed
before the affecting process started and remain existent after this process ended. Consumees disappear, so

The Dynamic System Aspect
they belong only to the pre-process object set, while resultees are created, so they belong only to the post-
process object set.
### Figure 13.9
The Involved Object Set partitioned into Preprocess Object Set and Postprocess Object Set
The Preprocess Object Set and the Postprocess Object Set are not necessarily disjoint—they may be
overlapping. Indeed, in Fig. 13.9, the overlapping members are the two enablers—Agent and Instrument,
and one transformee—the Affectee. Agent and Instrument might belong to both object sets, because, by
their definition, being enablers, they are required throughout the process (and are not supposed to change
as a result of the occurrence of the process they enable). Affectee belongs to both the preprocess object set
and postprocess object set, because it continues to exist after the process occurred, albeit in a different
state. Consumee is the only involved object which is not in the Postprocess Object Set, because the
Processing process consumed it, so it does not exist after Processing terminated. In an anti-symmetric
manner, Resultee is the only involved object which is not in the Preprocess Object Set, because
Processing generated it, so it did not exist prior to the beginning of Processing. The procedural links are
summarized in Table 13.1.
## 13.7 State-Specified Procedural Links
It is often the case that we wish to specify in our model not just that an object is transformed or that it
enables a process, but also at what state an enabler has to be in order for it to enable the process. We may
also wish to be able to specify not just the object that a process generates, but also the particular state at
which that object is generated as a result of the occurrence of a process. Likewise, one may wish to

specify not just what object a process consumes, but also the particular state that the object needs to be at
in order for the process to be able to consume it. State-specified procedural links provide for this.
A state-specified procedural link is a procedural link that connects a process to a
state of an object.
For each procedural link there is a state-specified version. State-specified procedural links differ from
their non-state-specified version in that rather than connecting the (transforming or enabled) process to
the involved object (transformee or enabler), they connect the process to one of the involved object’s
states. Thus, state-specified procedural links are elaborate versions of their regular procedural
counterparts.
Table 13.1 Procedural links, their semantics, symbols, source, and destination
## 13.8 State-Specified Enabling Links
State-specified enabling links—agent link and instrument link—are defined as follows.
A state-specified agent link is an agent link that originates from a specific state s of an
agent G to process P, denoting that in order for G to handle P, G must be at state s
throughout the duration of P.

The Dynamic System Aspect
Like its state-specified consumption link and result link counterparts, the state-specified instrument
link originates from a specific state and terminates at a process. The semantics of this link is that the
process is enabled if and only if the object exists and is at the state from which the link originates. This is
contrasted with the “regular” instrument link, which originates from the enabling instrument but not from
any particular state of that instrument. For example, a pilot must be sober in order to qualify as an agent
for the flying process of an Airplane. In OPL: Sober Pilot handles Flying.
A state-specified instrument link is an instrument link that originates from a specific
state s of the instrument I to process P, denoting that in order for P to execute, I must
be at state s throughout the duration of P.
The difference between the two instrument link types is demonstrated in Fig. 13.10, where on the left
hand side, the object Moving Truck is the instrument for Moving, implying that the state at which this
Moving Truck is does not matter. On the right hand side, the instrument link originates from the state
serviced of Moving Truck, implying that only if Moving Truck is serviced, Moving can take place.
### Figure 13.10
Instrument link vs. state-specified instrument link: Left: Instrument link—Moving Truck is an instrument of
Moving. Right: State-specified instrument link—serviced Moving Truck is an instrument of Moving
Table 13.2 summarizes the semantics, symbols, source, and destination of the two state-specified
enabling links.

## 13.9 State-Specified Transforming Links
State-specified transforming links differ from their corresponding regular, non-state-specified versions in
that rather than connecting the transformee (consumee, affectee, or resultee) to or from the transforming
process, they connect one of the transformee states to or from that process.
Table 13.2 State-specified enabling links: semantics, symbols, source, and destination
Each one of the three transforming links—consumption, effect, and result—has a state-specified
version, as defined below. The three transformees—consumee, transformee and resultee—are also roles
with respect to the corresponding processes associated with them, as are agent and instrument. Similarly,
the terms “input state” and “output state” refer to roles of two states of an affectee with respect to the
affecting process. The input state is the state just before the affecting process starts, while the output state
is the state the object is at just as that process ends.
An input state of object B is a state si of B at which B is when process P starts.
An input link is a link from the state si to process P.
An output state of object B is a state so of B at which B is when process P ends.
An output link is a link from process P to the state so.
A state-specified consumption link is a consumption link that originates from an input
state si of the consumee C and ends at process P, denoting that in order for C to be
consumed by P, it must be in state si.
The state-specified consumption link expresses the fact that the consumee is consumed by the process
if and only if the consumee is in the specified state—the one to which the consumption link is connected.

The Dynamic System Aspect
A state-specified result link is a result link that originates from process P and ends at
a state s of the resultee R, denoting that when P terminates, it creates R in state s.
The state-specified result link expresses the fact that the resultee is generated by the process only at
the specified state—the one to which the result link is connected.
A state-specified effect link is an in-out (input-output) link pair, whose input link
originates from an input state si of the affectee A and ends at process P, and whose
output link originates from P and ends at an output state so of A, denoting that in order
for A to be affected by P, A must be in si, in which case when P terminates A will be at
so.
Figure 13.11 shows two examples of state-specified consumption and result links. Machining can only
consume Raw Metal Bar in state cut and generate Part in state pre-tested. The corresponding OPL sentences
follow. The OPL syntax for a state-specified object is “state name” followed by “Object Name”. This
syntax is demonstrated in the two OPL sentences in Fig. 15.13 by cut Raw Metal Bar and by pre-tested
Part. When naming a state, one should therefore test its expressiveness by evaluating whether the phrase
that results from this concatenation makes sense and reads well in OPL sentences where it appears.
Since the function of this system is Machining, Cutting and Testing are environmental processes.2
Cutting must precede Machining in order to change Raw Metal Bar from its pre-cut to its cut state, while
Testing changes Part from pre-tested to tested. Additional examples of state-specified transforming links
appear in Table 13.3.
Machine
Operator
Raw Metal Bar
pre-cut cut
Machining
Part
pre-tested
tested
Cutting
Coolant
Testing
Machining consumes Coolant and cut Raw Metal Bar.
Machining yields pre-tested Part.
### Figure 13.11
State-specified consumption and result links: Machining can only consume Raw Metal Bar in state cut and
generate Part in state pre-tested
2In a system with a larger scope of Manufacturing, the three processes Cutting, Machining, and Testing, in that
sequence, would all be systemic subprocesses of Manufacturing.

## 13.9.1 State Change Versus Object Consumption and Generation
We have noted that object consumption and generation can be thought of as extreme cases of state
change, when the states are implicitly non-existent and implicitly existent. For example, in Fig. 13.11, the
Machining process consumes an object—Raw Material Bar—and generates a different object—Part.
However, the Cutting and Testing processes change only the states of Raw Material Bar and Part,
respectively, but not their identity. This is so because the Machining process is more drastic—it changes
the input object profoundly such that its identity as Raw Material Bar is lost, and a new object, Part, is
born.
As a result of the occurrence of the Machining process, Raw Material Bar has changed its state from
existent to non-existent. In other words, it was consumed. Part has changed its state from non-existent to
existent. In other words, it was generated. Conversely, Testing does not consume Part. It merely adds
information about the part, indicating whether it can pass to the next production stage. Cutting is not such
a clear-cut case, as one can justifiably argue that this process takes as input a long Raw Material Bar object
and outputs several shorter Raw Material Bar Segment objects, each of which is separately input to
Machining.
## 13.10 State-Specified Effect Links
Each of the five procedural links presented in Table 13.1 has a state-specified counterpart, which is
shown in Table 13.3. The single stateless effect link from Table 13.1 gives rise to three kinds of state-
specified effect link pairs, shown in Table 13.4.
Table 13.3 Consumption and result state-specified procedural links: semantics, symbols, source, and destination
Instead of the single effect link in Table 13.1, when states were not present, in Table 13.4 there are
three types of state-specified effect link pairs. Each link pair consists of an input link and an output link.

The Dynamic System Aspect
The difference between them stems from the origin of the input link and the destination of the output link.
We use the word in-out as a shorthand notation for input-output.
An in-out-specified effect link pair of process P is a pair of links consisting of an
input link from the input state sin of object B to P and an output link from P to the
output state so
Table 13.4 Input output state-specified procedural links: semantics, symbols, source, and destination
In the example for the in-out-specified effect link in Table 13.4, the OPL sentence is:

Purifying changes Copper from raw to pure.
Here, raw and purified are the input (source) and output (destination) states of Copper, respectively.
An input-specified effect link pair of process P is a pair of links consisting of an input link from the
input state sin of object B to P and an output link from P to B.
In the example for the output-specified effect link in Table 13.4, the OPL sentence is:
Testing changes Sample from awaiting test.
Here, awaiting test is the input state of Sample. The output state of Sample is not specified, implying that
(depending on the outcome of Testing) it can be any one of the three of Sample states.
An output-specified effect link pair of process P is a pair of links consisting of an
input link from object B to P and an output link from P to the output state sout of B.
In the example for the output-specified effect link in Table 13.3, the OPL sentence is:
Cleaning & Painting changes Engine Hood to painted.
Here, painted is the output state of Engine Hood. The input state of Engine Hood is not specified,
implying that it can be any one of the three Engine Hood states.
## 13.10.1 Value-Specified Procedural Links
A value-specified procedural link is a link between a process and one or two values of
an attribute that the process changes.
Each state-specified procedural link in Table 13.4 has a value-specified procedural link counterpart.
The three value-specified procedural links are depicted in Table 13.5. Values are states of attributes, so
the semantic and syntax of value-specified procedural links are somewhat different than their state-
specified counterparts, as specified in Table 13.5 and defined below.
A value setting link is a unidirectional value-specified procedural link from a process
to an attribute value, which sets that value, regardless of what it was earlier.
The value setting link is the counterpart of the state-specified result link of an object that is not an
attribute. The difference is that while the state-specified result link creates an object in the specified state,
the attribute is not created since it exists along with its exhibitor. What it does is to specify the value of
that attribute.
A value effect link is a bidirectional value-specified procedural link from a process to
an attribute value and back, which changes that value from some unspecified value to
another.
A value can be easily distinguished from a state by inspecting the object that “owns” the state in
question: If that owning object is an attribute, then the state is a value, and if not—the state is just a state.

The Dynamic System Aspect
The value effect link is the counterpart of the state-specified effect link of an object that is not an
attribute. The difference is that while the state-specified effect link changes an object from one
unspecified state to another, the value effect link changes the value from some unspecified value to
another.
An in-out-specified value effect link pair is a pair of a value-specified input link and
a value-specified output link which change that attribute value from the input vale to
the output value.
Table 13.5 Value-specified procedural links: semantics, symbols, source, and destination
The in-out-specified value effect link pair is the counterpart of the in-out-specified effect link pair of
an object that is not an attribute. The difference is that while the in-out-specified effect link pair changes

an object from one specified state to another specified state, the value effect link changes the value from
some specified value to another specified value.
The names of the values are parameter names. For example, t_new is the new value of Temperature of
Engine set by Heating. We can also assign actual numbers to the parameters, as demonstrated in Fig.
13.12.
### Figure 13.12
Value-specified procedural links with parameters and actual numeric values
## 13.11 Summary
A change of an object is an alteration in the state of that object.
Effect is a change in the state of an object that a process causes.
Construction is an extreme case of object effect, where the object’s input state is nonexistent
and the output state is existent.
Consumption is an extreme case of object effect, where the object’s input state is existent and
the output state is nonexistent.
When the transformation is extreme, a change in object identity takes place.
When the change is not profound or drastic, the object only alters its state while retaining its
identity.
A transformee of process P is an object B that P transforms as a result of the occurrence of P.
o A consumee of a process P is a transformee of P that P consumes as a result of the occurrence of P.
o A resultee of a process P is a transformee of P that P creates as a result of the occurrence of P.
o An affectee of a process P is a transformee of P that that P affects as a result of the occurrence of P.

The Dynamic System Aspect
A transforming link is a procedural link that connects a process with a transformee of that
process.
creates.
o A result link is a unidirectional transformation link from a process to the resultee that this process
o An effect link is a bidirectional transformation link that connects a process with an affectee of
that process.
o A consumption link is a unidirectional transformation link from a consumee to the process that
consumes it.
An enabler E of a process P is an object that must exist and be available in order for P to start,
and remain present throughout the occurrence of P in order for P to terminate normally, with E
ultimately unaffected.
o An agent is an enabler who is a human or a group of humans.
o An instrument is a non-human enabler.
An enabling link is a procedural link that connects a process with an enabler of that process.
o An agent link is an enabling link that connects a process with an agent of that process.
o An instrument link is a procedural link that connects a process with an enabler of that process.
An input state of object B is a state si of B at which B is when process P starts.
An input link is a link from the state si to process P.
An output state of object B is a state so of B at which B is when process P ends.
An output link is a link from process P to the state so.
A state-specified consumption link is a consumption link that originates from an input state si of
the consumee C and ends at process P, denoting that in order for C to be consumed by P, it must
be in state si.
A state-specified result link is a result link that originates from process P and ends at a state s of
the resultee R, denoting that when P terminates, it creates R in state s.
A state-specified effect link is an in-out (input-output) link pair, whose input link originates
from an input state si of the affectee A and ends at process P, and whose output link originates
from P and ends at an output state so of A, denoting that in order for A to be affected by P, A
must be in si, in which case when P terminates A will be at so.
o An in-out-specified effect link pair of process P is a pair of links consisting of an input link from
the input state sin of object B to P and an output link from P to the output state sout of B.
o An input-specified effect link pair of process P is a pair of links consisting of an input link from
the input state sin of object B to P and an output link from P to B.
o An output-specified effect link pair of process P is a pair of links consisting of an input link from
object B to P and an output link from P to the output state sout of B.
A value changing link is a link between a process and an unspecified value of an attribute which
the process changes.

## 13.12 Problems
1. Give two examples of each of the following, provide their OPM models, and verify that the
resulting OPL describes your original intent.
2. Change of an objects.
3. Consumption of an objects.
4. Creation of an objects.
The following questions relate to Figs. 13.13 and 13.14, which describe a system being simulated by
animation.
5. What is the system described in this OPD?
6. What are the affectee, agent and instrument?
7. What is the OPL sentence that describes effect?
8. What is the relation between Driver and Car? What link is used to express this?
9. What is the relation between Gasoline Tank and Car? What link is used to express this?
10. What is the process within Car Fueling taking place at this time?
11. What object does it transform and how? What is the OPL sentence describing this?
12. What link is missing between this process and Pump? What is the OPL sentence that would be
created if you added this link?
13. 14. 15. 16. What are the five affectees in this OPD? Which one is different than the other four and why?
What agent link is missing?
Describe the state changes of Pump.
What can you tell from the colors of the states of the various objects? Please refer specifically to
Gasoline Tank.
17. 18. What effect link is missing? Hint: Look at the one present.
Suppose Car is the only vehicle in the Gas Station throughout the Car Fueling process. Where
would you place the states called car present and car absent?
19. 20. How would the corresponding link change as a result?
What process reverts Gas Station to its original state?

The Dynamic System Aspect
Car
drives
Gasoline Tank
empty full
Driver
Car Fueling
Gas Station
### Figure 13.13
OPD for Chapter problems
### Figure 13.14
OPD of Car Fueling from Fig. 13.13 in-zoomed
21. Based on your responses to the previous two questions, explain why is it OK that in Fig. 13.13
Gas Station is an instrument, while in Fig. 13.14 it is an affectee?
