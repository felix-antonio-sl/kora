# Chapter 21 Complexity Management:
Refinement and Abstraction
The human mind, after all, can only juggle so many pieces of data at once before
being overwhelmed.
C. Downton (1998)
The very need for systems analysis and design strategies stems from complexity. If systems or problems
were simple enough for humans to be grasped by merely glancing at them, no methodology would have
been required. Due to the need for tackling sizeable, complex problems, a system development
methodology must be equipped with a comprehensive approach, backed by set of reliable and useful
tools, for controlling and managing complexity. OPM provides four refinement-abstraction mechanisms
to manage systems’ inherent complexity: (1) unfolding–folding, (2) in-zooming–out-zooming, (3) state-
expressing–state-suppressing, and (4) view creating. These mechanisms, defined and discussed in this
chapter, make possible the specification of contextualized model segments as separate, yet interconnected
OPDs. Taken together, they provide a complete model of the functional, value providing system. These
mechanisms enable presenting and viewing the modelled system, and the elements it contains, in various
contexts that are interrelated by the common objects, processes and relations. The set of clearly specified
and compatible interconnected Object-Process Diagrams completely specify the entire system to an
appropriate extent of detail and provide a comprehensive representation of that system with a
corresponding textual statement of the model in OPL. This chapter elaborates on complexity management
issues and specifies the various abstracting-refining mechanisms.
## 21.1 The Need for Complexity Management
Analyzing is the process of gradually increasing the human analyzer’s knowledge about and
understanding of the system’s architecture—the system’s structure and behavior combination, which
enables it to attain its function. This is typical of a scientist’s work, who, in a sense, is engaged in reverse-
engineering nature and systems in it. Analogously, designing—a major engineering task—is the process
of gradually increasing the amount of details about the system being architected. Complexity is inherent
in real-life systems: Soon enough during this architecting process, the sheer amount of details contained
in any real-world system of reasonable size overwhelms the system analyzer or architect, who must be
equipped with a concept and tools to tackle this detail explosion problem. We cannot do much about the
inherent complexity of the system, but by using a simple modeling framework, we can significantly
reduce the system’s complicatedness—how complicated it is perceived by a person looking at the model
that specifies the system. OPM strives to minimize complicatedness through simplicity of the language.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_

Complexity Management: Refinement and Abstraction
Requirements analysis and conceptual design are first steps in the lifecycle of a new system, product
or project. Creating (sometimes unconscious) resistance on the side of the prospective audience—the
various stakeholders—to accept the analysis and design results, because they look too complex and thus
intimidating, may have the adverse effect of jeopardizing the likelihood of success of subsequent phases
of the product development.
The severity and frequency of the detail explosion problem calls for an adequate solution to meet the
needs of the systems modeling and analysis community. A major test of any analysis methodology is
therefore complexity management—the extent to which it provides reasonable tools for managing the
ever-growing complexity of the modeling outcomes in a coherent, clear, and useful manner. Such
complexity management tools are extremely important for organizing the knowledge that the system
architects and designers accumulate and generate during the system architecting and design process.
Equally important is the role of complexity management tools in facilitating the communication of the
analysis and design results to other humans, including customers, beneficiaries, peers, superiors and
system developers down the development cycle road—implementers, testers, operators, etc.
Trying to incorporate the details into one big diagram, the amount of drawn symbols gets very large,
and their interconnections quickly become an entangled web. Because the diagram has become so
cluttered, it is increasingly unwieldy and difficult to comprehend. System architects experience this detail
explosion phenomenon on a daily basis, and anyone who has tried to model a non-toy system of even
modest complexity will sympathize with and endorse this description. This information overload happens
even if the language (such as UML and SysML) advocates using multiple diagram kinds for the various
system aspects. While some of the diagram kinds might be simpler than one kind (as in OPM), combining
them all to obtain a holistic system view is cognitively much more difficult. A system modeling language
must include integral mechanisms for controlling and managing this complexity. This entails being able
to present and view the system at various levels of detail that are consistent with each other.
## 21.2 The Model Complexity Assertion
The basic principle of OPM complexity management is the following detail hierarchy OPM principle.
The Detail Hierarchy OPM Principle
Whenever an OPD becomes hard to comprehend due to an excessive amount of details, a new,
descendant OPD shall be created.
The creation of the new OPD is done by one of the first two complexity management mechanisms—
in-zooming or unfolding—taking advantage of the model fact representation OPM principle. This
principle states that an OPM model fact needs to appear in at least one OPD in order for it to be
represented in the model. Based on this principle, we can omit from the descendant, newly created OPD,
in which a specific thing was refined, any model fact that already appeared in the ancestor OPD and is not
needed to make some point in the new OPD, without losing that fact from the model. This way, new
OPDs can be kept simple as they need not carry all the “baggage” of their ancestors. This provides for
maintaining any OPD sufficiently simple so it does not overwhelm the limited human cognitive capacity.

The determination of when an OPD becomes too complex due to excessive amount of details is left to
the discretion of the modeler, because it cannot be defined by merely fixing a maximal number of model
elements in the OPD. There are other factors, such as regularity, layout, and link crossings that affect
comprehension Nonetheless, a modeling tool such as OPCAT should limit the size of the canvas on which
a single OPD is drawn. This indirectly limits the number of entities and enforces periodic use of in-
zooming and unfolding.
Since this refinement and detail removal can be done recursively and at any required number of times,
we can tackle highly complex systems and still keep the model humanly accessible and comprehensible.
Hence we can make the following OPM model complexity assertion:
The OPM Model Complexity Assertion
Applying refinement mechanisms of in-zooming and unfolding to stateful objects or processes,
OPM can conceptually model systems at any level of complexity.
## 21.3 Aspect-Based Versus Detail-Level-Based Decomposition
UML and SysML address the problem of managing systems complexity primarily by aspect
decomposition—dividing the system model into 14 (UML) and 9 (SysML) different diagram types for
modeling various aspects of the system – structure, dynamics, state transitions, timing, etc.
difficult transition
UML: aspect-based decomposition
structure behavior states
abstract
detailed
### Figure 21.1
The two orthogonal divide-and-conquer strategies

Complexity Management: Refinement and Abstraction
Advocating the integration of the various system aspects into a single model, the approach OPM takes
is orthogonal, detail-based decomposition: Rather than applying a separate model for each system aspect,
OPM handles the inherent system complexity by decomposition of the system into a hierarchy of self-
similar diagrams of the same single kind—OPDs—via its abstracting-refining mechanisms. These enable
presenting and viewing the system, and the things that comprise it, at various detail levels. The entire
system is completely specified through its OPD set—a set of compatible OPDs, each providing a partial
view of the system being investigated or developed, which together provide a full picture of the system.
Each OPD is accompanied by its automatically generated OPL paragraph.
Figure 21.1 shows the two orthogonal complexity management strategies. In the aspect-based
decomposition, two thick, solid, vertical lines separate the structure, behavior and state transition aspects
from each other. The thin bidirectional horizontal arrows across these lines symbolize difficult transition
among the various models. The detail-based decomposition is represented by the two thin, dashed,
horizontal lines that separate the various levels of detail—abstract, detailed and concrete, from each other.
The thick bidirectional vertical arrows symbolize easy transition among the detail levels. The diagram is
schematic; it by no means implies that horizontally there are only three levels of abstraction in OPM. In
fact, this number is not bounded. The diagram should also not be interpreted as if vertically there are only
three diagram types in a multi-diagram-type approach.
## 21.4 The Completeness-Clarity Trade-off
Like most classical engineering problems, complexity management entails a tradeoff that must be
balanced between two conflicting requirements: completeness and clarity. Completeness means that the
system must be specified to the last relevant, necessary detail. Clarity means that to communicate the
analysis and design outcomes, the documentation, be it textual or diagrammatic, must be legible and
comprehensible. The complexity challenge entails balancing these two forces that pull in opposite
directions and need to be reconciled: On one hand, completeness requires that the system details be
stipulated to the fullest extent possible. On the other hand, the need for clarity imposes an upper limit on
the level of complexity of each individual diagram and does not allow for a diagram that is too cluttered
or loaded.
Figure 21.2 is an OPM model of the parts of Complexity Managing and its effect on the System Model’s
Completeness and Clarity attributes. Complexity management must address and solve this problem of
completeness-clarity tradeoff by striking the right balance between these two contradicting demands.
OPM achieves clarity through abstracting and completeness through refining. Abstracting, the inverse of
refining, saves space and reduces complexity, but it comes at the price of completeness. Conversely,
refining, which contributes to completeness, comes at the price of loss of clarity. There are “no free
meals”; as is typically the case with engineering problems, there is a clear tradeoff between completeness
of details and clarity of their presentation. The solution OPM proposes is to keep each OPD simple
enough, and to distribute the system specification over a set of consistently inter-related and mutually-
aware OPDs that contain things at various detail levels. Abstracting and refining are the analytical tools
that provide for striking the right balance between clarity and completeness.

## 21.5 State Expression and State Suppression
Explicitly depicting the states of an object in an OPD may result in a diagram that is too crowded or busy,
making it hard to read or comprehend. OPM enables state suppression—hiding the appearance of some or
all the states of an object as represented in a particular OPD when those states are not necessary in that
OPD’s context. In Fig. 21.4, the two states of each one of the two attributes form the OPD in Fig. 21.2
were suppressed, so the input-output link pair changes to an effect link (Fig. 21.3).
### Figure 21.2
The parts of Complexity Managing and its effect on the System Model’s Completeness and Clarity
attributes
### Figure 21.3
A stateful object with all states expressed (left) and a suppressed version (right)
The inverse operation of state suppression—state expression—exposes one or more hidden object
states. The modeler may suppress any subset of states. The complete set of states of an object is the union

Complexity Management: Refinement and Abstraction
of the set of states of that same object appearing in all of the OPDs in the OPD set—the set of OPDs of
the entire OPM model.
Graphically, the annotation indicating that an object presents a proper subset (i.e., at least one but not
all) of its states, shall be a small state suppression symbol in the object’s right bottom corner. This symbol
appears as a small state with an ellipsis label, which signifies the existence of one or more states that the
view is suppressing, The textual equivalence of the state suppression symbol shall be the OPL reserved
phrase “or at least one other state”.
## 21.6 Unfolding and Folding
Unfolding is a mechanism for refinement, elaboration, or decomposition. Unfolding reveals a set of things
that relate to the unfolded thing—the refineable. The result of unfolding is a hierarchy tree, the root of
which is the refineable. Linked to the root are the refinees—one or more things—parts, specializations,
features, or instances—that adds details about the refineable through one or more of the four fundamental
structural relations. Any refinee can, in turn, be the refineable for the next level of unfolding.
### Figure 21.4
The OPD from Fig. 21.2 after state suppression of the two attributes and folding of Complexity Management
Folding is the inverse operation of unfolding. It is a collapsing and abstracting mechanism, which can
be applied to a hierarchy of an unfolded refineable. Folding is applied from the bottom of the hierarchy
upward. Each folding operation hides some or all of the refineables. Folding all the refineables leaves just
the refineable—the root of the tree hierarchy.
Since each of the four fundamental structural relation links may undergo unfolding and folding, the
four kinds of unfolding-folding pairs are the following.
aggregation unfolding—exposing the parts of a whole, and participation folding—hiding the parts of
the whole,

exhibition unfolding—exposing the exhibitor’s features, and characterization folding—hiding the
features of the exhibitor,
generalization unfolding—exposing the specializations of the general, and specialization folding—
hiding specializations of the general, and
classification unfolding—exposing the class instances, and instantiation folding—hiding the
instances of the class.
## 21.7 In-Diagram and New-Diagram Unfolding
Unfolding can be done either in the current OPD or in a new OPD.
In-diagram unfolding is unfolding in which the refineable and its refinees appear
unfolded in the same OPD in which the refinee was originally.
Since unfolding uses one of the four the fundamental structural links, in-diagram unfolding is
graphically, syntactically, and semantically equivalent to using the corresponding fundamental structural
links. While in-diagram unfolding increases the load of the diagram, it saves the need to create a new
diagram, but if there are many refinees, or the current OPD is already busy, we will prefer new-diagram
unfolding.
New-diagram unfolding is unfolding in which the refineable and its refinees appear
unfolded in a new OPD.
Both in- and new-diagram unfolding can be applied to both objects and processes. Graphically, in
new-diagram unfolding, the unfolded refineable is denoted by a thick contour in both the more abstract
OPD in which the refineable appears folded, without refinees, and in the new, more detailed OPD, in
which the refineable appears unfolded and connected to its refinees with one or more fundamental
structural link.
The modeler should make a decision as to whether to use in-diagram or new-diagram unfolding based
on clarity considerations: If the current OPD is already crowded and tends to be cluttered, a new OPD
should be created to prevent the current OPD from becoming unwieldy. If in-diagram unfolding had been
applied and later the OPD became too crowded, the modeler can then switch from in-diagram to new-
diagram unfolding, thereby alleviating the complicatedness of the current OPD (at the price of an
additional OPD in the OPD set). Thus, the modeler decision whether to use in-diagram or new-diagram
unfolding should account for the trade-off between the clutter added to the current OPD and the need to
create a new OPD for displaying the refinees and associated links amongst them.
Partial unfolding may be depicted using the non-comprehensiveness symbol for aggregation,
exhibition, and classification. To satisfy a particular contextual relevance for an OPD, a modeler may
choose which refinees appear unfolded.
While unfolding and folding can be applied to both objects and processes, it is more prevalent for
objects, while processes can be refined via in-zooming, discussed next, or via unfolding. Process
unfolding is useful for functional decomposition which is very important in complex systems. Such
systems have many more auxiliary functions, in addition to the core function, that are concurrent or

Complexity Management: Refinement and Abstraction
independent of the core function’s flow. There is usually at least one more function—system setup and
management, a set of many services. Service-oriented systems offer several parallel or concurrent
services that cannot be thought of as working serially. Real-time systems perform several functions in
parallel rather than serially, while each component continuously samples its input from the other
components and acts upon it.
## 21.8 Port Folding
A procedural link from an operation of an object exhibitor to another object is lost during the operation
unfolding, because two objects cannot be directly connected by a procedural link. Similarly, a procedural
link from an attribute of a process exhibitor to another process is lost during the operation unfolding,
because two objects cannot be directly connected by a procedural link. However, it is often desirable to
maintain these links (Fig. 21.5).
### Figure 21.5
Port folding. Left: the unfolded model. Right: The port-folded version
Based on Mordecai and Dori (2013), a possible solution is port folding, shown in Fig. 21.6. Port
folding is a specialization of folding, an intermediate state between complete folding and complete
unfolding, in which we shift the process refinee—the operation—to the contour of the object refineable—
the exhibitor. Graphically, this looks similar to a SysML activity diagram port on the folded exhibitor.
Port folding is a useful representation if the modeler wants to use the object rectangles to give an idea
about the physical layout and relative sizes of the various system components. The reserved phrase “as
ports” (or “as a port” for singular) at the end of the exhibition sentence indicates port folding. Port folding
can also be applied to attributes of processes.
## 21.9 In-Zooming and Out-Zooming
In-zooming is a refinement operation, usually applied to processes, which specifies the subprocesses of
the process being in-zoomed, as well as their (possibly partial) performance or execution order. As an

example, in Fig. 21.6, the process Check-Based Paying from Fig. 19.13 is in-zoomed in the descendant
OPD on the right, showing its four subprocesses, as expressed in the OPL sentence:
Check-Based Paying zooms into Writing & Signing, Delivering & Accepting, Endorsing & Submitting, and
Cashing & Cancelling, in that sequence.
The execution order of these four processes follows the timeline OPM principle, repeated here:
The Timeline OPM Principle
The timeline within an in-zoomed process is directed by default from the top of the in-zoomed
process ellipse to its bottom.
The execution order is expressed in OPL by the reserved phrase in that sequence at the end of the in-
zooming sentence. The exposition of the four subprocesses in the context of the Check-Based Paying
process provides for explicitly specifying how the states of both Check and Keeper change throughout the
lifecycle of check, as also expressed in the OPL sentence to the left of the OPD.
Within the context of the in-zoomed process there may be partial order: overall there is an order
dictated by the timeline, but two or more processes can be performed in parallel. As an example, suppose
a process P zooms into seven subprocesses, SP1, SP2 … SP7, such that SP1 executes first, then SP2 and
SP3 in parallel, then SP4, and finally SP5, SP6, and SP7 in parallel. Then the OPL sentence will be:
P zooms into SP1, parallel SP2 and SP3, SP4, and parallel SP5, SP6, and SP7, in that sequence.
### Figure 21.6
The process Check-Based Paying from Fig. 19.13 is in-zoomed, showing the details of the state changes that
Check and Keeper undergo, as well as the agents involved in each subprocess

Complexity Management: Refinement and Abstraction
OPM can be considered process-oriented from the aspect of giving priority to modeling processes first
(initially the system’s function, the process that delivers the external value) and recursively zooming into
this function while modeling the objects that are relevant to each process at the corresponding detail level.
## 21.9.1 In-Diagram and New-Diagram In-Zooming
Like unfolding, in-zooming can be done either in the current OPD or in a new OPD.
In-diagram in-zooming is in-zooming in which no new OPD is created, and the
refineable appear in-zoomed along with its refinees in the same OPD.
New-diagram in-zooming is in-zooming in which the refineable and its refinees
appear in-zoomed in a new OPD.
All the examples so far were of new-diagram in-zooming. Indeed this is the more prevalent way of in-
zooming, since in-zooming requires a lot of “real estate” to specify the internal subprocesses and the
process being in-zoomed, as well as for depicting the additional relevant objects with links to these new
subprocesses, making the current OPD often too crowded. However, as Fig. 21.12 shows, in-diagram in-
zooming is also useful.
## 21.9.2 In-Zooming and Out-Zooming of Objects
Just like process in-zooming has the aggregation-participation semantics between the in-zoomed process
and its temporally-ordered subprocesses, so does object in-zooming has the aggregation-participation
semantics between the in-zoomed object and its spatially-ordered parts. In other words, the spatial order
according to the top-down or left-to-right layout of the parts determines their order. This is demonstrated
in the metamodel in Fig. 21.7: Whole from SD zooms in SD1 into Part A and Part B, in that vertical sequence.
### Figure 21.7
A metamodel of in-zooming and out-zooming of objects
If Part A and Part B in Fig. 21.7 would be arranged horizontally, the OPL sentence would be: Whole
from SD zooms in SD1 into Part A and Part B, in that horizontal sequence. The ability to define order within
objects opens the way to modeling tables and matrices of any dimension. For example, we can rename
Whole in Fig. 21.7 to be Table, and Part A and Part B can be called Row 1 and Row 2, respectively. In the
next in-zoom level, each row can be in-zoomed to expose its elements, arranged horizontally, e.g., Row 1

zooms into Element (1,1), Element (1,2), and Element 1,3), in that horizontal sequence. Thus, Element (1,2) will be
the second element in the first row of the matrix. A third dimension can be achieved by zooming into
each element, this time vertically, and this can proceed recursively. Each in-zooming operation, applied to
all the elements at the current level, adds one more dimension. Since each element can have a value, we
can use OPM to do matrix operations, such as addition or multiplication, and OPM tables can be used for
relational databases.
Time is one-dimensional and flows only forward, so to determine process execution order—the
timing—we only needed the vertical axis to specify the order of the subprocesses in an in-zoomed
process. Physical objects, however, are three-dimensional, so for object in-zooming we can at least
schematically model the relative layout of object parts in two dimensions, taking advantage of the fact
that the paper or computer screen used for conceptual modeling are two-dimensional. The limitation here
is that objects are rectangular rather than arbitrarily shaped, but we can still get a schematic, albeit rough,
2D layout. Moreover, if the in-zoomed object is an informatical object, such as a table or a matrix,
zooming into it can expose the actual cells of the table or matrix as individual objects.
## 21.10 Synchronous Versus Asynchronous Process Refinement
Unlike unfolding, which can be applied to each of the four the fundamental structural links, in-
zooming has the semantics of aggregation-participation only: The refineables are parts of the in-zoomed
refinee; they cannot be features, specializations, or instances. However, in addition to the whole part
semantics, the layout of the subprocesses within the in-zoomed process determines their execution order.
Conversely, when processes are unfolded, as are the four subprocesses of Complexity Managing in Fig.
21.2, there is no implied order to them (unless they have positive orderability, which must be denoted by
the ordered symbol next to the aggregation black triangle). The of aggregation unfolding of Complexity
Managing in Fig. 21.2, rather than in-zooming of Complexity Managing, is correct, because there is no
predetermined order of applying the four refinement operations while modeling a system. Rather, the
modeler applies them in an arbitrary order as needed. This is an example of an asynchronous process. On
the other hand, Check-Based Paying, shown in Fig. 21.6, is an example of a synchronous process.
A synchronous process is a process whose subprocesses have a predefined, fixed
order.
An asynchronous process is a process whose subprocesses do not have a predefined,
fixed order.
Due to the difference between aggregation and in-zooming as far as processes are concerned, in-
zooming is suitable for modeling synchronous processes, while aggregation unfolding—for modeling
asynchronous processes. A system can have a blend of both synchronous and asynchronous processes.
Moreover, if a process has several synchronous subprocesses and others that are not, the same process can
be both in-zoomed, showing its synchronous subprocesses ordered in the in-zoomed process ellipse and
its asynchronous ones—aggregation unfolded, either in the same or in a separate OPD.

Complexity Management: Refinement and Abstraction
Since the aggregation-participation fundamental structural relation does not prescribe any partial order
of process performance, the modeling of synchronous process refinement must use in-zooming, in which
order can be defined. The system in Fig. 10.5 is synchronous: there is a fixed, well-defined order of each
subprocess within the in-zoom context of Dish Washing.
To model asynchronous process refinement we use the aggregation-participation fundamental
structural link, either through in-diagram aggregation unfolding or as a new-diagram aggregation
unfolding of the process. Figure 21.8 depicts a portion of a Home Safety System that carries out the
function Home Safety Maintaining, which includes the subprocesses Burglary Handling, Fire Protecting,
and Earthquake Alarming. Since the order of these three subprocesses is unknown, the OPD uses in-
diagram aggregation unfolding with an aggregation-participation link from this function rather than an in-
zoomed version of Home Safety Maintaining. Home Safety Maintaining in-zooms to a recurring systemic
process, Monitoring & Detecting, for which Detection Module is an instrument and Threat Appearing is an
environmental process.
### Figure 21.8
Home Safety Maintaining is an asynchronous system
## 21.11 The Equivalence between In-Zooming and Unfolding
One can express the details of a synchronous process via both in-zooming and unfolding. Figure 21.9
presents a process P in-zoomed, in the OPM model on the left, and its equivalent OPM model on the
right, in which P is unfolded. However, as we can see in Fig. 21.9, in-zooming is preferable as it requires
less symbols and yield a shorter OPL paragraph. Using in-zooming rather than unfolding, we can use
instrument and result links instead of instrument event link and result event link, because the events
within an in-zoomed context are implicit.

Importantly, when a process is in-zoomed, its subprocesses are its parts, while the objects exposed as
a result of this in-zooming are the process’ attributes. Symmetrically, when an object is in-zoomed, its
internal objects are its parts, while its internal processes are its operations. The latter fact provides for
depicting processes as operations of an object by putting them inside the in-zoomed view of that object.
### Figure 21.9
The eqivalence between in-zooming (left) and unfolding (right)1
## 21.12 The System Map and the Ultimate OPD
There is exactly one System Diagram, SD—the top-level OPD, the level 0 OPD. It often contains one
main, core systemic process, which is the value-delivering function of the system. Recursive new-
diagram process in-zooming iterations result in a set of OPDs that are organized in a (hierarchical) tree
structure, with SD being the root (detail level 0) of the OPD tree, SD1, SD2, etc. being at detail level 1 of
the OPD hierarchy, SD1.1, SD1.2, … SD 2.1, SD2.2… being at detail level 2 of the OPD hierarchy, and
so on.
An OPD tree is a directed tree graph whose nodes are OPDs obtained by recursive
refinement (in-zooming and/or unfolding) of processes in the system, starting with the
function—the process in SD.
The OPD set is the set of all the nodes in the OPD tree.
1The red contour is assigned by OPCAT automatically to a thing that is both in-zoomed and unfolded.

Complexity Management: Refinement and Abstraction
Detail level of an OPD is the number of nodes in the OPD tree that need to be
traversed from that OPD to the root, SD, including SD itself.
The OPD tree is a tree of processes—a graph whose nodes are OPDs. The root is SD, the System
Diagram, and the other nodes are the descendant OPDs, marked with their OPD labels, such as SD1,
which is at detail level 1, SD2.3, which is at detail level 2, etc. The directed edges of an OPD tree have
labels with each edge pointing from the parent OPD, which contains the refineable element, to a child
OPD containing refinees, which elaborates a process in the parent OPD via new-diagram in-zooming for
synchronous subprocesses or new-diagram aggregation unfolding for asynchronous subprocesses.
Since in-zooming has the semantics of aggregation-participation, each in-zooming in the hierarchy is
also interpreted as aggregation-participation in order to preserve the tree structure. Figure 21.10 shows at
the top the OPD tree—the hierarchy of the Product Lifecycle Engineering system OPM model (Dori and
Shpitalni 2005). The OPD set of the model in Fig. 21.10 has 11 OPDs spanning 4 levels of detail.
While the OPD tree is presented like a file hierarchy (see Fig. 21.10 top), the system map, shown at
the bottom of Fig. 21.10, is a more elaborate presentation of the OPD tree.
The system map is an elaborate OPD tree, in which each node in the tree is a
miniaturized icon of the OPD, with thick grey arrows pointing from each process in
one OPD to its refined (in-zoomed or unfolded) version in the child OPD.
The system map explicitly depicts the elements (things and links) in each OPD (node). Because the
system map may become very large and unwieldy, mechanisms shall allow access to model content and
the associations among elements. The system map helps navigate in a complex system that may comprise
hundreds of OPDs at many levels of detail. As an example, the executable OPM model of the mRNA
decay model in Somekh et al. (2014) contains hundreds of objects and processes in over 40 OPDs at 9
levels of detail, with hyperlinks from a thing in the model to the paper from which the model fact was
extracted.
Figure 21.11 is a screenshot of a simulated execution of the mRNA Decay OPM model (Somekh et al.
2014), showing it being at an OPD SD2.4.2.2.1.2.4.2 – elF4F Dissociates Cap and Decaysome in-zoomed,
as indicated also by the frame around this process in the OPD tree on the left. This OPD demonstrates the
self-similarity of OPDs: regardless of what detail level an OPD is at, it used only stateful objects,
processes, and relations among them.
Currently, the system in Fig. 21.11 is executing in parallel four subprocesses (in dark blue), after
having completed the subprocess elF4F Dissociates Cap above them. The dissociation is manifested in
each of these four subprocesses by consuming a link, modeled as an object in its own right, between two
objects, e.g., the factor Xrn1 and the protein elF4E at the bottom are dissociated by the process elF4E and
Xrn1 Dissociation. Below the OPD is the lifespan diagram, enabling inspection of each object and process
at each point in time. The browser on the left is open on the relevant paper, one of the 43 papers from
which the model facts in this OPD were taken, obtained by clicking on the in-zoomed process.
This example demonstrates the indispensability of the refinement mechanisms, and in particular in-
zooming. Without it, it would be impossible to comprehensibly show the hundreds of things in the model
and the thousands of links among them in a single OPD or in any other kind of diagram.

In addition, an OPM tool set should provide a mechanism for creating views, as OPDs with associated
OPL sentences, of objects and processes that meet specific criteria. These views may include the critical
path for minimal system execution duration, or a list of system agents and instruments, or an OPD of
objects and processes involved in a specific kind of link or set of links. For example, an OPD can be
created by (1) refining (unfolding or in-zooming) an object or (2) collecting and presenting in a new OPD
things that appear in various OPDs for expressing assignment of system sub-functions to system-module
objects.
### Figure 21.10
The tree hierarchy (top) and system map (bottom) of the Product Lifecycle Engineering system OPM
model

Complexity Management: Refinement and Abstraction
The ultimate OPD is single flat representation of the OPM system model.
The ultimate OPD is obtained by recursively flattening the OPD tree from the bottom up all the way to
the OPD tree toot, such that the entire model is represented in this single OPD. Except for very small
system models, the ultimate OPD is definitely unfit for use by humans due to our limited cognitive
capacity. However, for computer processing—knowledge management, navigation, querying, etc., the
ultimate OPD is very useful.
### Figure 21.11
A screenshot of simulated execution of the mRNA Decay OPM model (Somekh et al. 2014), showing detail
level 8—SD2.4.2.2.1.2.4.2—elF4F Dissociates Cap and Decaysome in-zoomed
## 21.13 The OPD Object Tree and Forest
Unlike the OPD (process) tree, which results from process refinement and has a single root, there can be
many OPD object trees, at least one from each refineable object, which together constitute a forest.
An OPD object tree is a tree whose root is an object B and whose nodes are things
that result from recursively refining B via unfolding and in-zooming, where each in-
zooming is converted to aggregation-participation.
Each tree stems from a distinct refineable object that unfolds or in-zooms to reveal its details—not
necessarily just parts as in the process in-zooming, but possibly also features, specializations, or
instances. Rather than identifying the possible flow of execution control as in the OPD (process) tree,

each OPD object tree encapsulates the information about an object as a hierarchical structure. Since in-
zooming has the semantics of aggregation-participation, like the OPD tree, each in-zooming in the
hierarchy of the OPD process is also interpreted as aggregation-participation in order to preserve the tree
structure. Complete or partial OPD object trees can be presented as views (see Sect. 21.18). The root of
each OPD object tree can be attached as a child of the node in the OPD (process) tree, creating the system
map (see Sect. 21.12).
## 21.14 Out-Zooming
Out-zooming is the inverse operation of in-zooming. A scenario in which the need for out-zooming arises
is when the modeler observes that the current OPD is already over-crowded, making it necessary to hide
the content of an in-zoomed process in the current OPD. In-diagram out-zooming does not create a new
OPD, which implies removing and losing the subprocesses and objects inside the process being out-
zoomed. Therefore, unless the modeler decides that these subprocesses are too detailed for the purpose at
hand and is ready to delete them, in-diagram out-zooming does not make a lot of sense.
New-diagram in-zooming elaborates a refineable in an existing OPD, say SDn, where n is the current
level of detail, by creating a new OPD, SDn+1, which elaborates the refineable at the next detail level by
adding subprocesses, associated objects, and relevant links. Figure 21.12 is a metamodel of the New-
Diagram In-Zooming and New-Diagram Out-Zooming processes. The OPM model on the right uses in-
diagram in-zooming of the model on the left to elaborate the two processes: New-Diagram In-Zooming, for
creating a new-diagram in-zoomed context, filled in with subprocesses and objects, and New-Diagram
Out-Zooming, for creating a new-diagram out-zoomed (empty) context. New-Diagram In-Zooming begins
with Content Showing, followed by Link Refining. New-Diagram Out-Zooming begins with Link
Abstracting, the inverse process of Link Refining, followed by Content Hiding, the inverse process of
Content Showing.
Semi-Zoomed OPD is an interim object, which is created and subsequently consumed during both New
Diagram In-Zooming and New-Diagram Out-Zooming. This interim object appears only within the contexts
of both New-Diagram In-Zooming and New-Diagram Out-Zooming.
In Fig. 21.13, the metamodel on the left hand side of Fig. 21.12 is elaborated by embedding an actual
OPDs inside its objects SDn, SDn+1, and Semi-Zoomed OPD. In this particular OPM model example,
SDn, presented in Fig. 21.13 at the top middle, includes the process P, which is a refineable about to be
in-zoomed, as well as four objects: the consumee C, the agent A, the instrument D, and the resultee B,
connected to P with the corresponding different procedural links. This OPD inside the meta-object SDn is
instrument for the New-Diagram In-Zooming on the left.
Content Showing is the first of the two New-Diagram In-Zooming subprocesses. During Content
Showing, the boundary of P expands to make room for showing its content—the model subprocesses P1,
P2, and P3, as well as the interim model object BP. The result of Content Showing is presented as the
content of the interim object Semi-Zoomed OPD. This interim object is recognizable only in the context of
New-Diagram In-Zooming. The second subprocess, Link Refining, done by the modeler, consumes it while
creating SDn+1 presented in Fig. 21.13 at the bottom in the middle.
During Link Refining, the procedural links attached to the contour of P migrate to the appropriate
subprocesses as determined by the modeler. Thus, since P1 consumes C, the consumption link arrowhead

Complexity Management: Refinement and Abstraction
migrates from P to P1. The agent A handles both P1 and P2, so in SDn+1 two agent links, one to P1 and
the other to P2, replace the single one in SDn from A to P. P3 requires D, so the instrument link migrates
from P to P3. Finally, since BP results from P1, and P3 consumes it, the corresponding result and
consumption links are added, making BP an interim, internal object of P, recognizable only within the
context of P. Likewise, P1, P2, and P3 are internal processes of P, and as such they are recognizable only
within the context of P. The OPD inside the meta-object SDn+1 is instrument for the New-Diagram Out-
Zooming on the right. What happens next is the exact inverse of what we have seen, both in the order of
the subprocesses and what each of them does.
### Figure 21.12
A metamodel of new-diagram in-zooming and new-diagram out-zooming
Link Abstracting is the first of the two New-Diagram Out-Zooming subprocesses. During Link
Abstracting, the links connected to subprocesses and interim objects of P migrate to (the boundary, the
ellipse circumference of) P itself, resulting in exactly the same Semi-Zoomed OPD that is depicted inside
New-Diagram In-Zooming. This Semi-Zoomed OPD interim object is consumed by Content Hiding,
creating SDn presented in Fig. 21.13 at the top in the middle. The boundary of P can now shrink, as it is
empty and there is no need for making room to show its content (the model subprocesses P1, P2, and P3,

as well as the interim model object BP), which is now hidden. The result of Content Showing is presented
as the content of the interim object Semi-Zoomed OPD.
## 21.15 Simplifying an OPD
In-diagram out-zooming—the elimination of an in-zoomed process content—followed by new-diagram
in-zooming can simplify an already-modeled OPD that the modeler deems overly complicated or
overloaded with details. In-diagram out-zooming reduces the cognitive load necessary to understand the
complicated OPD at the expense of adding a new OPD to the OPD set, which is the result of the
subsequent new-diagram in-zooming, which creates a new OPD at an interim level of detail, as explained
next.
Figure 21.14 demonstrates simplifying an OPD by in-diagram out-zooming followed by new-diagram
out-zooming. On the left is the original OPD set with three OPDs: SD, SD1 and SD1.1. Realizing that SD1
is overly complicated, in order to simplify the model, the modeler decides that a set TO (Things to be
Out-zoomed), comprising four things in SD1—P1, P2, and P3, along with BP—shall be replaced by a
single new process P123 via new-diagram out-zooming.
### Figure 21.13
The metamodel on the left in Fig. 21.12 elaborated with an example of an actual OPM model inside it
In the middle of Fig. 21.14, P123 undergoes new-diagram out-zooming, resulting in SD1.1[new] (in a
real implementation, the new OPDs shall not be marked with [new]; this label only helps the explanation
here).

Complexity Management: Refinement and Abstraction
Here is how this is done. The modeler indicates the things in the set TO (things to be out-zoomed) and
the name of the new interim process to be created (P123 in our case). The grey background denotes these
candidate elements. The process-to-be P123 now undergoes new-diagram out-zooming, following the two
subprocesses described earlier: link abstracting and content hiding. As a result of link abstracting, the
links that were connected to subprocesses of the future P123 process migrated to the contour of the now-
created P123, and as a result of content hiding, P123 becomes empty, as shown in SD1[new].
### Figure 21.14
Simplifying SD1 of the OPM model on the left by in-diagram out-zooming followed by new-diagram in-
zooming yields a new OPM model on the left, in which SD1[new] and SD1.1[new] replace SD1
In order to preserve the model facts that were eliminated (such as the model facts that A is agent to P1
and P2), a new OPD, SD1.1[new], was created with these facts. Hence, on the right of Fig. 21.14 is the
new OPD set, which now has four OPDs: SD[new], SD1[new], SD1.1[new], and SD1.1.1[new], renumbered
to reflect the new OPD hierarchy, In this augmented hierarchy, the complicated OPD SD1 has been
replaced by two simpler OPDs – SD1[new] and SD1.1[new].

Examining SD1[new], we see that it is indeed less complicated and less crowded than the original SD1,
since it has a net of five fewer elements: three removed processes, P1, P2, and P3, one removed object,
BP, two removed links, and one added process, P123. This new OPD is inserted into the process
hierarchy, pushing the old SD1.1, which remains unchanged, one detail level down, from detail level 2 to
detail level 3. Due to the addition of SD1.1[new], SD1.1is renumbered to be SD1.1.1[new].
## 21.16 Abstraction Accounts for Procedural Link Precedence
Recall that the procedural link uniqueness OPM principle asserts that at any level of detail, an object and
a process can be connected with at most one procedural link, which uniquely determines the role of the
object with respect to the process at that detail level.
When the modeler performs abstraction via state suppression, folding, or out-zooming, the procedural
links between refinees and other things in the OPD that are not refinees, migrate to the context
(graphically the contour, or circumference) of the refineable. For example, suppressing the states in Fig.
10.4, the pair of input-output links migrates from the two states to Person to become an effect link.
Another example is P123 in Fig. 21.14.
This migration may cause a conflict, in which two or more procedural links of different kinds link an
object and a process. According to the procedural link uniqueness OPM principle an object or an object
state can link to a process only by a single, unique procedural link. Figure 21.15 demonstrates the
problem of procedural link abstraction. In SD1, the result link from P1 to B is more significant, or is
semantically stronger, than the effect link from P2 to B, so when the process P in SD1 is out-zoomed in
SD, the result link prevails.
### Figure 21.15
Abstracting different procedural links invokes the link precedence
To sustain this principle, OPM resolves the conflict between candidate links by determining, based on
the links’ semantic strength, which link remains or which new link replaces the candidates in the abstract
OPD. The loss of detail information is consistent with the notion of abstraction. Semantic strength and
link precedence are two concepts to guide the determination of which links to retain and which to hide
when an OPD is out-zoomed or folded.
Semantic strength of a procedural link is the significance of the information that the
link carries.
Information concerning a change in existence, either creation or elimination, is more significant than
information about change to an existing thing. The relative semantic strength of the two conflicting
procedural links determines the link precedence. When two or more procedural links compete to remain

Complexity Management: Refinement and Abstraction
represented in an OPD that is being abstracted (out-zoomed, folded, or state-suppressed), the link that
prevails is the one with the highest semantic strength.
## 21.16.1 Precedence Among Transforming Links
Transforming links include result, effect, and consumption links, and their variants having the event or
condition control modifiers.
Link precedence is an ordered list of procedural links with diminishing sematic
strength.
Table 21.1 Link precedence among the transforming links
Table 21.1 shows link precedence among the transforming links: P in the upper left corner is out-
zoomed. The column headings show the three possible transforming links between P1 and B, while the
row headings show the three possible links between P2 and B. The table cells show the prevailing link
between B and P after P is out-zoomed. Cells marked as “Invalid” indicate the impossibility of the
combination. For example, inspecting the center cell, if P1 consumes B, then B no longer exists when P2
later tries to consume it again. Since object creation and consumption are semantically stronger (i.e., they
have higher semantic strength) than affecting the object by changing its state, result and consumption
links have precedence over effect links, as demonstrated in Table 21.1. However, since result and
consumption links are semantically equivalent, when they compete, the prevailing link shall be the effect
link because the effect link allows both creation and elimination as effects.
## 21.16.2 Precedence Among Transforming and Enabling Links
Transforming links are semantically stronger than enabling links, because the transforming linksdenote creation, consumption, or change of the linked object, while the enabling links only denote
enablement. A transforming link therefore has precedence over an enabling link as shown in Fig. 21.16.

Within the enabling links, an agent link has precedence over an instrument link, because in artificial
systems the humans are central to the process, they handle the system and must ensure its proper
operation. In addition, wherever there is human interaction, an interface should exist and this information
should be available to the modeler of a refineable so that they can design the human-system interface
according to the conceptual model specification.
### Figure 21.16
Link precedence among transforming and enabling links
Summarizing the semantic strength of the procedural non-control links, the primary link precedence is
as follows:
Consumption = Result > Effect > Agent > Instrument
Here, the = and > symbols refer to the semantic strength of the links. State-specified links have higher
precedence than basic links that do not specify states.
## 21.16.3 Precedence Among Same-Kind Non-control Links and Control Links
Each non-control link kind has a corresponding event and condition link that are useful for determining
finer, secondary precedence distinction within each kind of procedural link. A secondary link precedence
exists within each procedural link in the primary link precedence. The event link has higher semantic
strength than its corresponding non-control link, while the condition link has a weaker semantic strength
than its corresponding non-control link. The semantic strength of an event link is stronger than the
semantic strength of its corresponding non-control link, because any event link has semantics of both its
corresponding non-control link plus the event capable of initiating a process. The semantic strength of a
conditional link is weaker than the semantic strength of its corresponding non-control link, because the
condition modifier weakens the precondition satisfaction criteria for the connecting process.
## 21.16.4 Summary of the Procedural Link Precedence
Summarizing the semantic strength of the procedural links based on the distinction between primary and
secondary precedence, the complete order of precedence is as follows:
1. consumption event > consumption
2. consumption = result
3. result > consumption condition
4. consumption condition > effect event
5. effect event > effect
6. effect > effect condition
7. effect condition > agent event
8. agent event > agent
9. agent > agent condition

Complexity Management: Refinement and Abstraction
10. agent condition > instrument event
11. instrument event > instrument
12. instrument > instrument condition
## 21.17 Link Migration upon In-Zooming
The context (graphically, the outer circumference) of a process P acts as parentheses in algebra that are
used to express the distributive law: Any procedural link attached to P is thus viewed as is it is attached to
each one of P’s subprocesses. An example appears in Fig. 8.2, where crashed Vehicle is instrument to all
the four subprocesses inside Automatic Crash Responding.
As the modeler adds subprocesses, she or he often fails to manually migrate procedural links to the
specific subprocesses, causing them to be implicitly attached to superfluous procedural links that
invalidate the model. To help avoid these situations, as soon as a modeler draws the first subprocess P1
inside and in-zoomed process P, a modeling tool should automatically move to P1 all the procedural and
control links that were attached to P in the parent OPD. An example is Fig. 5.1, which shows the
Automatic Crash Responding process after it was in-zoomed and after its first subprocess, Crash Severity
Measuring, was drawn inside it near the top of the enclosing ellipse of the Automatic Crash Responding
process. The links that were attached to Automatic Crash Responding have migrated to be attached to
Crash Severity Measuring.
It is the modeler’s role to see to it that the various transforming links that are now attached to P1 will
be put back to P or moved to subsequent subprocesses. Similarly, enabling links may need to be migrated
to one or more specific subprocesses, where the linked enabler is really needed. As an alternative to the
automatic link migration, the tool can check the validity of the links after the insertion of each new
subprocess and alert the modeler as needed.
## 21.18 View Creating: The Fourth Refinement Mechanism
View creating—the fourth refinement mechanism after state expression, in-zooming and unfolding, is
achieved by collecting model facts from various OPDs in the OPD set and putting them together in a new
OPD called View for the purpose of demonstrating a specific aspect. Examples include (1) a process
tree—a complete or partial tree of the process hierarchy of the system, which is a purely procedural view
of the system, (2) an object tree—a complete or partial tree of the object hierarchy of the system, which is
a purely structural view of the system, (3) an allocation view, showing what objects are allocated to
perform what functions (processes) in the system model, and (4) an animated simulation motivated view,
aimed at easing the concurrent inspection of how certain objects and processes from disparate OPDs
interact. In a modeling tool, views shall not be edited to add, remove, or change any model fact. Rather,
this should be done in the non-view OPDs and reflected automatically in the pertinent views. The inverse
of view creating is view deleting.

## 21.19 Middle-Out as the De-facto Architecting Practice
Ideally, analysis and design start at the top and make their way gradually to the bottom—from the general
to the detailed. In real life, however, analysis typically starts at some arbitrary detail level and is rarely
linear. The design is not linear either. Usually, these are iterative processes, during which knowledge,
followed by understanding, is gradually accumulated and refined. The system architect cannot know in
advance the precise structure and behavior of the very top of the system—this requires analysis and
becomes apparent at some point along the analysis process. Step by step, the analyst builds the system
specification by accumulating and recording facts and observations about things in the system and
relations among them.
Due to the non-linear nature of the analysis and design processes, linear, unidirectional “bottom-up”
or “top-down” approaches, while seeming highly methodical, are rarely applicable to real-world systems.
Rather, it is frequently the case that the system under construction or investigation is so complex and
unexplored, that neither its top nor its bottom is known with certainty from the outset. More commonly,
analysis and design of real-life systems start in an unknown place along the system’s detail level
hierarchy. The analysis proceeds “middle-out” by combining top-down and bottom-up techniques to
obtain a complete comprehension and specification of the system at all the detail levels.
It thus turns out that even though architects usually strive to work in an orderly top-down fashion,
more often than not, the de-facto practice is the middle-out mode of analysis and design. Rather than
trying to fight it, system modeling approaches and tools must provide facilities to handle this middle-out
architecting mode along with support for top-down and bottom up approaches.
## 21.19.1 OPM Caters to the Mixed Approach
Using OPM, the accumulated knowledge is documented and represented as interconnected model facts
through a set of OPDs and their corresponding OPL paragraphs. If the OPD that is being augmented
becomes too crowded, busy, or unintelligible, a new OPD is created. This descendant OPD repeats one or
more of the things in its ancestor OPD in a refined form. These repeated things establish the link between
the ancestor and descendant OPDs. The descendant OPD does not usually replicate all the details of is
ancestor, as some of them are abstracted, while others are simply not included. This new OPD is therefore
amenable to refinement of new things to be laid out in the space that was saved by not including things
from the ancestor OPD. In other words, there is room in it to insert a certain amount of additional details
before it gets too cluttered. When this happens, a new cycle of refinement takes place, and this goes on
until the entire system has been completely specified. As we have seen in this chapter, OPM caters not
only to this top-down approach, but also to bottom-up and middle-out via abstracting and OPD
simplifying along with the addition of an interim detail level.
## 21.19.2 When Should a New OPD Be Created?
An OPD set has to be readable and easy to follow and comprehend. The following rules of thumb are
helpful in deciding when a new OPD should be created so OPDs are as easy to read and grasp as possible.
The OPD should not stretch over more than one page or one average-size monitor screen.
The OPD should not contain more than 20–25 entities (objects, processes or states).

Complexity Management: Refinement and Abstraction
Things (objects or processes) must not occlude each other. They are either completely contained
within higher-level things, in case of zooming, or have no overlapping area. An exception to
this guideline is when port folding (See Sect. 21.8) is applied.
The diagram should not contain too many links.
A link should not cross the area occupied by a thing.
The number of links crossing each other should be minimized.
## 21.20 Navigating Within an OPM System Model
Since, as we have seen, an OPM model can be very large navigation inside the model and orientation
becomes an issue.
## 21.20.1 OPM Diagram Labels and Tree Edge Labels
The OPM system name is the name of the OPM model that specifies the system. An OPD name is the
name that identifies each OPD in the OPD process tree. SD shall contain one and only one systemic
process, which represents the overarching system function that delivers functional value to stakeholders.
It may, in addition, to contain one or more environmental processes. SD is the label of the root OPD in
the OPD tree. The OPD tree root, SD, occupies level (tier) 0 in the OPD tree and it is the single node at
this level. Higher numbered tiers, i.e., those corresponding to successive refinements, may have more
than one OPD.
Not only the nodes in the OPD tree are labeled; the edges are too. Each edge (an arc connecting two
nodes—two OPDs) in the OPD tree has a unique label. The label expresses a refinement relation that
corresponds to the implicit invocation link or unfolding relation. Considering each OPD to be an object
and the entire OPD process tree to be a single OPD, each edge is a unidirectional tagged structural link
with a tag that reads: “is refined by in-zooming <Refineable Name> in ”, or “is refined by unfolding
<Refineable Name> in ”. An OPD refinement OPL sentence is an OPL sentence describing the refinement
relation between a refineable present in a tierN OPD and its refining OPD in tierN+1. The syntax of an in-
zoomed OPD refinement OPL sentence is:
<TierN OPD label> is refined by in-zooming <Refineable Process Name> in <TierN+1 OPD Label>.
Similarly, the syntax of an unfolded OPD refinement OPL sentence is:
<TierN OPD label> is refined by unfolding <Refineable Process Name> in <TierN+1 OPD Label>.
## 21.20.2 Whole System OPL Specification
An OPL paragraph is the collection of OPL sentences that together specify in text what the corresponding
OPD specifies graphically. An OPL paragraph name, using the OPD name, may precede the first OPL
sentence of each OPL paragraph.
An OPD model specification is the collection of successive OPDs in the system’s OPD
tree.

An OPL model specification is the collection of successive OPL paragraphs
corresponding to the OPDs in the system’s OPD tree, from which duplicate OPL
sentences were removed.
An OPM model specification is a side-by-side presentation of the OPD model
specification and the corresponding OPL paragraph is presented to the right of each
OPD.
An example of an OPM model specification is presented in Table 21.2, which contains the entire
OPM model of the Dish Washing system in Fig. 10.5.An OPM model specification of a system begins
with a starting title, as in Dish Washing System OPM model specification.
The left column contains the OPDs in the OPM system’s OPD set in a breadth-first order, but the
modeler may override this default order. The corresponding OPL paragraphs are listed on the right
column, such that each OPL paragraph is to the right of its OPD.
## 21.21 Summary
Complexity management is essential for taming the complexity of real-world systems, both
man-made and natural.
The OPM Model Complexity Assertion is that applying refinement mechanisms of in-zooming
and unfolding to stateful objects or processes, OPM can conceptually model systems at any level
of complexity.
OPM’s complexity management approach is detail-level-based decomposition, which is in
contrast with UML and SysML approach of aspect-based decomposition.
The completeness-clarity trade-off is the tension between the need to specify the system such
that all the model facts are represented, while maintaining a clear, comprehensible representation
of the system.
The three refinement-abstraction mechanisms are unfolding–folding, in-zooming–out-zooming,
and state-expressing–state-suppressing. A fourth is view-creating–view-deleting.
State-expressing is showing one or more of an object’s states; state-suppression is hiding one or
more of the object’s states.
Each of the four fundamental structural relation links may undergo unfolding and folding, so
there are four kinds of unfolding-folding pairs.
In-diagram unfolding is unfolding in which the refineable and its refinees appear unfolded in
the same OPD in which the refinee was originally.
New-diagram unfolding is unfolding in which the refineable and its refinees appear unfolded in
a new OPD.

Complexity Management: Refinement and Abstraction
Unfolding is a mechanism for refinement, elaboration, or decomposition, which reveals a set of
refineables—things that relate to the unfolded thing—the refineable.A synchronous process is a process whose subprocesses have a predefined, fixed order.
An asynchronous process is a process whose subprocesses do not have a predefined, fixed
order.
New-diagram in-zooming is in-zooming in which the refineable and its refinees appear in-
zoomed in a new OPD.
In-diagram in-zooming is in-zooming in which no new OPD is created, and the refineable
appear in-zoomed along with its refinees in the same OPD.
In-zooming has the semantics of aggregation-participation plus positive orderability.
Process in-zooming determines the (possibly partial) temporal order of its subprocess execution.
Object in-zooming determines the (possibly 2-dimansional) spatial order of its parts.
An OPD tree is a directed nod- and edge-labeled tree graph whose nodes are OPDs obtained by
recursive in-zooming or unfolding of processes in the system, starting with the function—the
process in SD.
An OPD set is the set of all the nodes in the OPD tree.
Detail level of an OPD is the number of nodes in the OPD tree that need to be traversed from
that OPD to the root, SD, including SD itself.
The system map is an elaborate OPD tree, in which each node in the tree is a miniaturized icon
of the OPD, with thick grey arrows pointing from each process in one OPD to its refined (in-
zoomed or unfolded) version in the child OPD.
The ultimate OPD is single flat representation of the OPM system model.
Dori – Model-Based Systems Engineering with OPM and SysML
Table 21.2 OPM model specification of Dish Washing System

Complexity Management: Refinement and Abstraction
Out-zooming provides for incorporating the middle-out approach to conceptual modeling by
simplifying a complicated OPD while adding an interim level of detail.
Semantic strength of a procedural link is the significance of the information that the link carries.
Link precedence is an ordered list of procedural links with diminishing sematic strength.
The primary link precedence is Consumption = Result > Effect > Agent > Instrument.
View creating is collecting model facts from various OPDs in the OPD set and putting them
together in a new OPD called View for the purpose of demonstrating a specific aspect.
An OPD model specification is the collection of successive OPDs in the system’s OPD tree.
An OPL model specification is the collection of successive OPL paragraphs corresponding to
the OPDs in the system’s OPD tree, from which duplicate OPL sentences were removed.
An OPM model specification is a side-by-side presentation of the OPD model specification and
the OPL model specification, where to the right of each OPD the corresponding OPL paragraph
is presented.
## 21.22 Problems
1. Based on Fig. 21.1, create an OPM model that explains the two specializations of
decomposition, what they mean, and which kind is used by what language.
2. 3. Present on object with four states and a process that affects it.
Suppress the states that are not relevant to the model in the previous question and add the
incomplete state symbol.
4. Model a complex object with three levels of unfolding, including aggregation unfolding and
exhibition unfolding.
5. Select two subprocesses from Fig. 21.6. For each, apply new-diagram in-zooming and add model
elements as you see fit.
6. Perform out-zooming from the in-zoomed processes in the two OPDs created in the previous
problem.
7. 8. 9. What is the ultimate OPD of the system in Fig. 21.6?
Is the process in Fig. 21.6 synchronous or asynchronous? Explain.
Is the process in Fig. 21.17 synchronous or asynchronous? Explain.

10. 11. 12. 13. 13.13. 13. Fig. 21.17 Home Safety Maintaining system—a partial model
Draw an in-zoomed map of part of the Mid-West of the USA with at least six states, where each
state is an object, while maintaining approximate spatial relations among the states.
In Fig. 21.13, change the OPDs inside SDn and SDn+1 such that a need to invoke the procedural
link precedence shall arise.
For the model in the previous problem, create the Semi Zoomed OPD analogous to that in Fig.
21.13.
In Fig. 21.14, define TO as {P3, P4, P5, BK}, perform the out-zooming, and show the resulting
SD[new], SD1[new], SD1.1[new], and SD1.1.1[new].
