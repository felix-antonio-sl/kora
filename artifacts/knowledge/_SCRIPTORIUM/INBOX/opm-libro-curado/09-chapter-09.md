# Chapter 9 Conceptual Modeling: Purpose and
Context
A conceptual model is a formal model, in which every entity being modeled in the real
world has a transparent and one-to-one correspondence to an object in the model.
Simmons (1994)
Before going into formal presentations of OPM and SysML as conceptual system modeling languages and
OPM as a systems engineering methodology, we discuss the theoretical aspects underlying the framework of
systems, systems architecture, and systems engineering, within which conceptual modeling is a valuable
intellectual activity.
## 9.1 Systems, Modeling, and Systems Engineering
Systems are all around us. Natural systems have been around for eons, and biological organisms have
evolved into extremely complex systems. Artificial, human-made systems, products, and services are also
becoming increasingly complex. Systems of infrastructural nature, such as air traffic control, the Internet,
and electronic economy, are orders of magnitude more complex than products individuals normally use. The
combination of miniaturization and computational power has been so pervasive that even common
household products exhibit intelligent features embedded within increasingly minuscule, commodity-like
hardware, giving rise to the emerging Internet of Things—a conglomerate of weakly interconnected devices
of all kinds, creating a loosely coupled mega system-of-systems.
## 9.1.1 Science and Engineering: Commonalities and Differences
The main difference between science and engineering is that scientists aim to explore and understand
observable physical, informatical (cybernetic) and human phenomena, while engineers, who are informed
by scientific discoveries, architect, design, develop, maintain and evolve artificial systems for the benefit of
humans. Sometimes, engineers are required to perform reverse engineering—the exploration of an existing
system whose function, structure, behavior, or working principles are not available and unknown.
Considering this exploratory character of reverse engineering, science can be thought of as reverse
engineering of nature. When a system is being designed (by engineers) or investigated (by scientists),
details about it accumulate quickly. The collected facts, be they real, assumed, contemplated or
conjectured, become so voluminous that they are hard to master without an orderly way of making sense
of what is being revealed. Managing these facts is mandatory in order for them to make sense as a whole.
In view of the rapid development of systems’ complexities, the need for an intuitive yet formal way of
documenting designs of new systems or collected information about existing ones becomes ever more

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 9

Conceptual Modeling: Purpose and Context
apparent. This, in turn, requires a solid infrastructure for recording, storing, organizing, querying, and
presenting the knowledge being accumulated and the creative ideas that build on this knowledge.
## 9.1.2 Conceptual Modeling and Model-Based Systems Engineering
The process of representing system-related knowledge in both science and engineering is conventionally
referred to as conceptual modeling, and the outcome of this activity is a conceptual model. Subsequent,
higher order cognitive activities, including understanding, analyzing, designing, presenting, and
communicating the analysis findings and design ideas, can be based on the evolving conceptual model.
The vision of the Massachusetts Institute of Technology Engineering Systems Division (MIT ESD,
2015) is that “the fundamental principles and properties of engineering systems are well-understood, so
that these systems can be modeled, designed, and managed effectively.”
Conceptual modeling, which often precedes or done alongside mathematical and physical modeling, is
the primary activity required for engineering systems to be understood, designed, and managed. Modeling
is the process underlying model-based systems engineering (MBSE), the focus of this book. MBSE is
not just about modeling, as some people mistakenly perceive; it is systems engineering (SE) that is based
on formal modeling of various kinds—conceptual, mathematical, and physical). The conceptual model is
the comprehensive underlying blueprint—the reference artifact that constitutes the source of authority of
the various system aspects—requirements, performance, functionality, structure, dynamics, and many
other physical and informatical (cybernetic) aspects. Thus, MBSE requires a rigorous conceptual
modeling methodology that encompasses a universal ontology, a language, a set of principles and
guideline, and a supportive modeling software environment.
Understanding physical, biological, artificial, and social systems requires a well-founded, formal, yet
intuitive methodology and language that is capable of modeling the complexities inherent in these
systems in a coherent, straightforward manner. The same modeling paradigm, the heart of the
methodology, should serve for both designing new systems (engineering) and for studying (science) and
improving existing ones. It should apply to artificial as well as natural systems and represent both equally
faithfully. A common, unified conceptual modeling framework for both artificial and natural systems is
most important, because complex engineered systems and physical phenomena often mutually affect each
other. For example, in order to model a system such as an aircraft, a satellite, a ballistic missile defense
system, or a medical device, one must understand the relevant mechanical, electrical, chemical,
biological, and physical principles that govern both the system and the environment in which it operates
and with which it interacts.
## 9.2 A Foundational Systems Engineering OPM Ontology
Ontology is a set of concepts and their relations in some domain of discourse.
The size of the ontology is the number of concepts and relation in the ontology. Systems science and
engineering are in need of a well-defined foundational, universal, general, necessary and sufficient ontology
that would underpin concepts and terms it uses in order for them to be precise and unambiguous. The
following minimal ontology principle provides a good starting point for our discussion.

The minimal ontology principle
If a system can be specified at the same level of accuracy and detail by two languages of different
ontology sizes, then the language with the smaller size is preferable to the one with the larger
size, provided that the specification comprehensibility of the former is at least comparable with
that of the latter.
Not only does this principle make perfect sense; it is also in line with the long accepted Ockham’s
Razor (Ockham, 1495)—a principle attributed to 14th Century logician and Franciscan friar William of
Ockham, England, which states that “Entities should not be multiplied unnecessarily” (in Latin:
“Pluralitas non est ponenda sine necessitate”). Often called the principle of parsimony, three more useful
variation on Ockham’s Razor follow.
“When you have two competing theories that make exactly the same predictions, the simpler one is
the better.”
“One should not increase, beyond what is necessary, the number of entities required to explain
anything” (Helighen 1997).
“One should always choose the simplest explanation of a phenomenon, the one that requires the
fewest leaps of logic.”
The reason for adding to the minimal ontology principle the condition “… provided that the
specification comprehensibility of the former is at least comparable with that of the latter” is that taken to
extreme, one can argue that the binary code of 0 and 1 is the shortest, so it is the best. This is true for
computers, for which real human comprehension is (still?) meaningless anyway. For humans, from a
semantic viewpoint, a binary specification of any non-trivial system (e.g., a computer program in machine
code, to make the case clearer) is completely undecipherable without disproportionate effort. Therefore
we require that both ontologies enable specification (or modeling) of systems with about the same level of
comprehensibility, or better yet, that the specification that uses the smaller ontology is more
comprehensible. If the ontology is defined carefully and is grounded on deep philosophical foundations,
there is not necessarily a tradeoff between the size of the ontology and the specification length or
comprehensibility of the system modeled based on that ontology.
Ockham’s Razor inspired also the minimum description length (MDL) principle (Rissanen 1978), a
method for inductive inference that provides a generic solution to the model selection problem, i.e., how
does one decide among competing explanations of data given limited observations. MDL is based on the
insight that any regularity in a given set of data can be used to compress the data by describing it with
fewer symbols than the number of symbols needed to describe the original data. In a similar vein, we
formulate the following minimal conceptual modeling language OPM principle.
The Minimal Conceptual Modeling Language OPM Principle
A symbol system—a language—that can conceptually model a given system using ontology with
fewer diagram kinds and fewer symbols and relations among them is preferable to a larger
language with more diagram kinds and more symbols and relations among them.
Using the smaller ontology puts less cognitive load on the human modeler, making the conceptual
model more comprehensible and communicable to all the stakeholders without compromising the fidelity

Conceptual Modeling: Purpose and Context
and detail level of the model. We can rephrase the above principle almost inversely: A language with
fewer symbols and fewer diagram kinds that is based on a universal ontology can describe any system
with better comprehensibility than a language with more symbols and more diagram kinds.
Alleviating the human cognitive load is highly desirable, because the modeler must cope with the
inherent, irreducible complexities of man-made systems to be built (systems engineering) or natural
systems to be investigated (science), so reducing the unnecessary complexity (often called
complicatedness) by providing a simpler language is of tremendous value.
## 9.2.1 Objects Exist, Processes Happen? Some Thought-Provoking Q&As
If we accept the minimal ontology principle, then we need to find the minimal universal ontology—the
ontology that is necessary and sufficient to model the universe and systems in it. We start by first asserting
that anything in the universe either exists or happens. We proceed with a series of questions and answers
designed to lead us to insights about a possible minimal universal ontology.
Q1: Assuming that everything in the universe is a thing, what can things in the universe “do”?
A1: Things can exist or happen. Any thing can either exist or happen. Nothing can be said to neither
exist nor happen, in fact or potentially, and physically or informatically.
Q2: What would be a general name for all the things in the universe that exist or might exist physically or
conceptually?
A2: Objects exist or might exist.
Q3: What are the things in the universe that happen or might exist physically or conceptually?
A3: Processes happen or might happen.
Processes cannot just happen in vacuum, without “doing” something, which leads to the next question.
Q4: What are the things to which processes happen?
A4: Processes happen or might happen to objects.
Q5: What do processes do to objects?
A5: Processes transform objects.
Q6: What does it mean for a process to transform an object?
A6: Transforming an object by a process means one of the following three options:
1. creating (generating) an object,
2. destroying (consuming) an object, or
3. affecting (changing) an object.
Q7: What does it mean for a process to affect an object?
A7: A process affects an object by changing its state.
Hence, objects must be stateful, i.e., they must have states.
Q8: In what way are things semantically associated? Is this the only way?
A8: Things are semantically associated through relations. Relations are the only way we can think
about the way things relate or refer to or are associated with each other.
Q9: Is there a difference between how objects and processes are related?
A9: Objects are associated to objects (and processes to processes) via structural (static) relations,
while objects and processes are associated via time-dependent procedural (dynamic) relations.

Q10: what are the two universal aspects, i.e., the two aspects from which things in the universe can be
viewed, considered, and described?
A10: The two universal aspects are (1) structure—the way objects relate to each other and processes
relate to each other—and (2) behavior—the way processes transform objects over time.
## 9.2.2 The Object-Process Theorem
The answers to the questions above can be thought of as universal axioms, because while they make
sense, they are difficult to prove. If we accept these axioms, the conclusion is that things—stateful objects
and processes—and relations among them are the only three elements needed to describe the universe!
We can use the universal axioms to prove the following Object-Process Theorem.
The Object-Process Theorem
Stateful objects, processes, and relations among them constitute a minimal universal ontology.
Proof:
The proof is based on (1) necessity and (2) sufficiency of stateful objects, processes, and relations
among them as the only three kinds of elements needed to constitute a minimal universal ontology.
Accordingly, the proof is divided in two parts: necessity and sufficiency.
Part 1—necessity: Stateful objects and processes are necessary to specify the two universal aspects,
structure and behavior: Specifying the structural, static system aspect requires stateful objects and
relations among them. Specifying the procedural, dynamic system aspect requires processes and
relations between them and the objects they transform.
Part 2—sufficiency: Things can either exist (we call these things stateful objects) or happen (we call
them processes) and nothing else. Things can be associated with each other only through relations.
Therefore, things (objects and processes) and relations among them are the only elements needed to
specify facts or ideas. Q.E.D.
## 9.2.3 The Object-Process Corollary
The Object-Process Theorem gives rise to the following Object-Process Corollary.
The Object-Process Corollary
Using stateful objects, processes, and relations among them, one can conceptually model any
system in any domain.
Since according to the Object-Process Theorem stateful objects, processes, and relations among them
constitute a minimal universal ontology, and the universe is the union of all the domains it comprises, this
assertion makes sense. One possible exception to this is the subatomic particle quantum domain, where
our macro-world distinction between objects and processes becomes blurry. For example, electrons and
photons are described as both particles (objects) and waves (processes). As soon as we step into the
atomic and molecular level, e.g., molecular biology (Somekh et al. 2014), the Object-Process Corollary
becomes valid, and OPM becomes a viable and attractive modeling paradigm.

Conceptual Modeling: Purpose and Context
This first version of the Object-Process Corollary says nothing about the level of complexity of the
systems that are amenable to being modeled with stateful objects, processes, and relations among them.
## 9.2.4 The Object-Process Assertion: The Basis for OPM
Combining the Object-Process Corollary with the Model Complexity Assertion, we get the following
Object-Process Assertion.
The Object-Process Assertion
Using stateful objects, processes, and relations among them, along with refinement mechanisms
of in-zooming and unfolding, one can conceptually model systems in any domain and at any level
of complexity.
Combining the Object-Process Theorem, according to which stateful objects, processes, and relations
among them constitute a minimal universal ontology, with the minimal ontology principle, the optimal
conceptual modeling language must have just two types of concepts—stateful objects and processes,
collectively called things—along with relations among them. Collectively, things and relations are the
only two OPM’s elements.
Things in the same system must be related, either directly or indirectly. Graphically, these relation are
expressed by links. Things and links are collectively called elements, and so element is the top-level OPM
concept.
An OPM element is a thing or a link.
## 9.2.5 Why Not Just One Kind of Thing? A Graph with Nodes and Links?
One may argue that an even more minimalistic representation than three kinds of elements—objects,
processes, and relations among them—could be just two: things and relations among them. Indeed, quite a
number of knowledge representation frameworks have come up with this idea of representing knowledge via
a graph with nodes of just one kind and links connecting them. Some of these frameworks, which vary in
their level of formality, are surveyed in Dori (2004). These include the concept maps (Arnheim 1969),
entity-relationship diagram (Chen 1976), semantic networks (Lehman 1999), conceptual graphs (Chein and
Mugnier 1992), and systemigrams (Blair et al. 2007). Looking at examples of graphs expressed in these
approaches, one quickly reveals that since there is only one kind of node, there is no distinction between an
object and a process, so the ability to distinguish between structure and behavior—the two distinct facets
that must be represented in any model—is severely crippled, or even nonexistent. At the small price of
increasing the number of elements in the ontology from two to three, we gain a tremendous capability of
concurrently modeling both the structure and the behavior of a system.
Indeed, objects are the things that exist. Relations among them constitute the structure of the system.
This is the static, structural aspect of the system. To understand the system’s dynamic, procedural aspect,
to know what happens to objects in the system and how it operates to provide value, a second,
complementary type of thing is needed—a process. We know of the existence of an object if we can name
it and refer to its unconditional, relatively stable existence, but without processes we can neither tell how
this object is created or destroyed, nor how its states change over its lifetime.

A stateless object is an object that has no states. A stateful object is an object that has one or more
states. These states are stable in the sense that it takes a process to switch an object from one of its states
to another, and as long as no process acts on the object, the object remains in the same state.
Figure 9.1 presents the main symbols of OPM. The symbols for object, state, and process are
respectively shown as the first (left-most) group of symbols. The rest of the symbols are links: structural
links are shown in the middle group and procedural links—in the right-most group. Their names and
semantics have been mentioned in Part I, and will be further elaborated as we proceed.
Objects and processes, collectively referred to as OPM things, are the two types of OPM’s universal
building blocks. OPM views objects and processes as being on equal footing, so processes are not
necessarily subordinate to or owned by objects. Symmetrically, objects are not necessarily inferior to
processes, nor are processes necessarily owned by objects.
### Figure 9.1
The three groups of OPM element symbols
State is depicted in Fig. 9.1 between object and process. Discussed in more detail later on, state is a
situation in which an object can be at some point during its lifetime.
## 9.2.6 The Thing Importance OPM Principle
In OO, objects “own” processes, which in the OO jargon are called operations, or services, or methods.
OPM takes a different stand: Major system-level processes can be as important as, or even more important
than objects in the system model. In particular, we already noted that the top-level process of a system (or
subsystem) is its function, the top-level value-providing and purpose-serving process, for the performance of
which the system is built and used. Hence, a process must be amenable to being modeled independently of
any particular set of objects involved in its occurrence. Therefore, OPM views both objects and processes as
first-class citizens. They stand on equal footing; neither has supremacy over the other. Rather, their
importance is related the model hierarchy as expressed in the following thing importance OPM Principle.
The Thing Importance OPM Principle
The importance of a thing T in an OPM model is directly related to the highest OPD in the OPD
hierarchy where T appears.
For example, the object ACR System and the process Automatic Crash Responding in Fig. 1.2 are of the
same relative importance, as they show up for the first time in SD, the System Diagram, which is the top-
level OPD. Indeed, the object ACR System is required for the process Automatic Crash Responding to take
place, so one cannot argue for the supremacy of the object ACR System over the process Automatic Crash
Responding or vice versa.

Conceptual Modeling: Purpose and Context
Being able to tell objects and processes apart and use them properly in a model is key to modeling in
OPM. To define these fundamental concepts and to communicate their semantics, we next discuss the
concepts of existence and transformation.
## 9.3 Object, State, Transformation, and Process Defined
Since objects OPM can be physical or informatical (cybernetic), we define object as something that captures
these two facets without committing to either one, while including the element of “existence throughout
time.”
An object is a thing that exists or can exist physically or informatically.
The object’s existence can be physical or informatical. It can be as simple as a block of ice, a word in
a book or a record in a file, or as complex as an organization, the Internet, a human brain, or a galaxy.
A state is a possible situation or position at which an object can be for some positive
amount of time.
This definition implies that a state has a meaning only within and in the context of an object. A state
has no meaning out of the contexts of its owning object. For example, states of the object Organization
can be private or public, and states of the object Record can be locked or unlocked. The states private and
locked have no meaning outside the context of their respective owning objects.
Transformation is (1) creation (generation, construction), (2) consumption
(elimination, destruction), or (3) effect—change in the state of an object.
Transformation takes a positive amount of time.
A process is a thing that transforms an object.
By this definition, a process must be associated with at least one object: the one which that process
transforms. For example, Freezing is a process that changes the state of Water form liquid to ice. This is
the basis for the object transformation by process OPM principle.
The Object Transformation by Process OPM principle
In a complete OPM model, each process must be connected to at least one object that the
process transforms or one state of the object that the process transforms.
A non-trivial synchronous process (i.e., a process whose subprocesses have a defined order of
execution) comprises a hierarchical network of subprocesses. At every level of the process hierarchy there
is a time-induced partial order on the processes, i.e., some processes must end before others start, while
others can occur in parallel to other processes or as their alternatives.

## 9.4 System and Related Concepts
Deferring the formal definition of system for just a little, this is a good place to add a couple of questions to
our line of questions from Sect. 9.2.1:
Q11: What are the two main aspects all systems share?
A11: Being part of the universe, all systems can be viewed from the two major aspects: structure and
behavior.
Structure is the static aspect; it relates to the question what is the system made of? From the
structural aspect, a System is a finite set of components and their time-invariant interconnections.
Behavior is the dynamic aspect; it relates to the question how does the system change over time?
Q12: What is the additional major aspect that pertains primarily to premeditated man-made systems?
A12: Function—the utilitarian, subjective aspect: Why is the system built? For whom? Who are the
beneficiaries who gain from operating it? What value do these beneficiaries get from the system’s
operation?
To some extent, biological organisms can be argued to be systems which provide functions that
benefit themselves or other systems, but such (often mutual, e.g., symbiotic) benefits are a result of
evolutionary processes rather than a premeditated intention, which is characteristics of humans as “tool
building” organisms. Indeed, as the Smithsonian Institute (2015) experts indicated:
Spanning the past 2.6 million years … stone tools provide evidence about the technologies, dexterity,
particular kinds of mental skills, and innovations that were within the grasp of early human toolmakers…
Function is a key concept in man-made systems; it is a process which provides (functional) value to a
beneficiary. The beneficiary is a person or a group of people, and the value is their benefit at cost—the
difference between the system’s perceived benefit and the system’s cost. Based on this definition of
function, we define system as follows.
A system is a function-providing object.
This succinct definition is quite unorthodox. It is worth comparing this definition to the definition of
system in ISO/IEC 15288 standard. According to ISO/IEC 15288, system is a combination of interacting
elements organized to achieve one or more stated purposes. The standard definition is compatible with
ours, since it contains the element of purpose, which is akin to function—providing value to some
beneficiary. Our definition of a system is more general in that it does not require that the system be
combined of interacting elements. While that description is generally true, it does not convey the essence
of a system. In complex systems, and even more so in systems-of-systems, such as the international air-
traffic control system, whose emergent function is to regulate the air transportation worldwide, there are
numerous interacting physical and informatical parts, including airplanes, airports, communication
networks, and air carriers.

Conceptual Modeling: Purpose and Context
### Figure 9.2
Two concepts for a nail-driving system: Top-left: hammer; Top-right: DEWALT 18-Volt 18-Gauge 2 in.
Cordless Brad Nailer; Botto-left: OPD of the Nail-Driving System; Bottom-right: The corresponding OPL1
In a simple system, such as a nail-driving system—the hammer shown at the top-left of Fig. 9.2, being
a combination of two interacting elements—head and handle—the number of interacting parts is not the
predominant feature. What is important is that the hammer is a system that provides the function of nail
driving. Looking closely at this hammer, one can distinguish lower-level functional elements, such as
claw to extract nails, but they are not really separate parts, further emphasizing the functional aspects of
this system. The same function of nail driving can be accomplished by a much sophisticated system, such
as the one presented on the top-right of Fig. 9.2. Although this is a much more complex system, it
provides basically the same nail-driving function (and is indeed called “nailer”).
The OPM model (the OPD and the corresponding OPL) at the bottom of Fig. 9.2 emphasize the
common function of these two systems. The difference between the two systems is in several
performance metrics that can be deduced from the following description, provided in the Web site of this
product: “The DEWALT DC608K—18 Gauge 2 in. Cordless Brad Nailer delivers consistent nail
1From this point on, the OPDs are not shaded, as they are accompanied by their corresponding OPL paragraphs. The
colors of the various OPL phrases in the OPL here are as they appear in OPCAT. In subsequent OPLs, reserved OPL
phrases are in non-bold Arial font, and non-reserved phrases—in Bold Arial.

penetration into both soft and hard joints. The sequential operating mode allows for precision placement
and the bump operating mode provides the user with production speed. The straight magazine, accepts 18
gauge nails ranging in lengths from 5/8 in. to 2 in. Its 12-position dial allows the user to move between
applications without having to re-acquire exact depth setting.” As we see, the function of this system is
described as delivering “nail penetration”, same as a hammer, albeit possibly with better speed, power,
and accuracy. Thus, according to our definition of system, both hammer and the Cordless Brad Nailer are
nail driving systems.
A subsystem, also known as a component, or a module, is a part of the system, which,
in itself, does not provide the function that system provides.
The system is comprised of subsystems or modules or components—all being objects—which only
when put together deliver the (emergent) function, making it a system. This is a good place to define a
system-of-systems (SoS), which in the sense explained below, can be thought of as the “opposite” of a
subsystem.
A system-of-systems, (SoS) is a system whose set of subsystems contains at least two
systems.
This definition of SoS implies that a SoS is comprised of at least two components, each of which is a
system in its own right, and therefore, by definition, has its own function. In other words, if we take a SoS
apart, we will end up with at least two functioning entities. Since a SoS is also a system, it has an
emergent function of its own in addition to the functions of its constituent systems. For example, the
global air traffic control system is a SoS whose function is air traffic controlling. It is comprised of many
systems, such as airports, national aviation authorities, national and international airspaces, the
International Air Transport Association (IATA, the trade association for the world’s airlines, representing
some 250 airlines or 84% of total air traffic; IATA 2015), international air traffic communication
protocol, emergency regulations, aircraft carriers, aircrafts, pilots, crews, passengers, and much more.
Many of the comprising systems, such as airport and air carrier, are SoSs in their own right. Conversely,
while a highly complex system, aircraft, for example, is not a SoS, because operating on its own, none of
its components, such as wing or fuel tank or fuselage, can provide any substantial function. In the rest of
the book, most of the claims about a system are applicable also to subsystems and SoSs.
## 9.4.1 Default System Naming
In spoken language, simple systems, such as a hammer, are often called tools, more complex systems, such
as an electric current meter, are instruments, and yet more complex ones are “systems,” but they all provide
some function—their stated goal—and the difference between them is their level of complexity. A default
system name is the name of the function this system provides followed by the word “system.” For example,
the system called printer, whose function is printing, can be called “printing system.” A hospital is a health
level improving system, a chair is a sitting system, a home is a residing system, a bathtub is a bathing
system, and an airplane is a flying system. Indeed, searching the Web for images of a “bathing system” and
a “sitting system”, one gets an incredible variety, some of which are presented in Fig. 9.3, of what people
refer to as bathing (top) and sitting (bottom) systems. The common function of the former is their ability to
cleanse or sooth people, and the latter—to seat people with some level of comfort.

Conceptual Modeling: Purpose and Context
### Figure 9.3
Search results of images of “bathing system” (top) and “sitting system” (bottom)
Figure 9.4 is an OPM model of the Nail-Driving function and the Nail-Driving System—the instrument
for achieving this function. The method used with each kind of Nail-Driving System can be captured in the
diagram as a specialization of Nail-Driving. Hammer and Cordless Brad Nailer are two such
specializations; they are incarnations of two different concepts for achieving the system’s function: The
Hammer, which is basic, and the Cordless Brad Nailer, which is more complex (and consequently more
expensive).
### Figure 9.4
OPM model of the Nail-Driving function and Nail-Driving System with its Hammer and Cordless Brad Nailer
specializations
## 9.4.2 Involved Humans: Stakeholder, Beneficiary, Customer, User, Supplier
System stakeholders are entities that are concerned with the system.

A stakeholder is an individual, an organization, or a group of people that has an
interest in, or might be affected by, a system.
Below we define the main stakeholder types. One or more of the system stakeholders is the
beneficiary—the stakeholder that extracts value and benefits from the system.
A beneficiary is a stakeholder who extracts value and benefits from the system.
Customers (either real or potential) are key stakeholders.
A customer is the stakeholder who orders the system and sponsors its development,
implementation, deployment, and support, or purchases a product that is part of the
system.
A user is a stakeholder who operates the system or directly interacts with it.
A supplier is a stakeholder who oversees the development, support, and maintenance
of the system or product.
The first kind of customer in the definition above is usually an organization who needs a specially-
designed system and orders it from the supplier (defined below). The second kind is usually an individual
who purchases a consumer good that was designed and manufactured by a supplier based on the
anticipation that people will be willing to pay for it because the customer foresees the value that this
system (in this case product, defined below) would deliver. Either way, without customers it is hard to
imagine why a system would be developed in the first place.
For relatively simple systems, such as household products, the customer and the user are the same. For
example, a car owner who drives it is the customer, user, and beneficiary, while other passengers are only
beneficiaries. Beneficiaries of a national missile defense system are the country’s citizens, although they
are neither the users nor the customers. The supplier is another key stakeholder.
Other stakeholders might include regulators, the judicial system, the public, and entities that might be
affected by the system.
## 9.4.3 System Source: Natural or Artificial
Systems originate from a source, which can be natural or artificial (human-made). The source determines
the mechanism through which the system has become functional. In natural systems, this is a result of the
actions governed by the laws of physics. In biological systems, a subset of natural systems, principles of
evolution play an additional critical role.
As this book focuses on engineering of artificial systems, from this point on, unless otherwise
specified, the term system will refer to an artificial system. The mechanism through which a system is
created and becomes functional involves some level of intellectual and physical human endeavor, be it as
primitive and as rudimentary as it might be. When this endeavor becomes considerable and passes some
threshold of complexity while showing signs of planning and coordination, we call it engineering, and

Conceptual Modeling: Purpose and Context
more recently, systems engineering. Non-trivial systems, which are the focus of interest of systems
engineering, comprise a significant amount of processes acting to transform a large number of
interconnected objects (the system’s components) in a way that enables the attainment of the system’s
function.
A socio-technical system, also known as engineering system, is a system that
integrates technology, people, and services, combining perspectives from engineering,
A product is a commercially-viable system.
A service is a commercially-viable process.
A function of an artificial system is its top-level value-providing process, as perceived
management, and social sciences.
Products are designed and manufactured by a commercial entity and sold to another entity for profit.
Since a system is an object, a product is a commercially-viable object. Analogously, a service is a
process that is sold by a commercial entity for profit.
Here we refer to a business service. In the world of software, a service is similar to a method, or an
operation. More specifically, in Service-Oriented Architecture, the concept of service includes any
interface provided by a component in the system to other components, and by a system to other systems.
## 9.4.4 Function, Structure, and Behavior Definitions Refined
Having defined beneficiary, we can now refine our definition of function.
For example, the function of a hammer is nail driving, the function of a printer is printing, the function
of chair is sitting, key and lock—locking and unlocking, window—ventilating and lighting, refrigerator—
food shelf life prolonging, fire alarm—fire break alerting. More complex systems have higher-level, more
abstract functions. Thus, the function of the system called hospital is patients’ health level improving.
Each patient is a beneficiary of this system, the customer may be a government or a private entity, and the
medical staff constitutes the group of users. As another example, the function of a missile defense system
is defending a country from a missile attack. The customer of the system is that country’s government, the
user is its military, and the beneficiary is the people living in that country.
At lower levels of subsystem or component, a subsystem’s function can also benefit the system’s
higher-level function or other systems or subsystems. For example, Dictionary.com provides the
following nouns for rudder:
1. 2. Nautical: a vertical blade at the stern of a vessel that can be turned horizontally to change the
vessel’s direction when in motion.
Aeronautics: a movable control surface attached to a vertical stabilizer, located at the rear of an
airplane and used, along with the ailerons, to turn the airplane.
by the beneficiary.

In both the nautical and the aeronautics cases, rudder is a subsystem of a vehicle—a vessel and an
airplane, respectively, with the function of changing course or turning or navigating the vehicle. This
function of the rudder is part of the function of the vehicle, which is people and goods moving, and which
requires also propulsion, supplied by the vehicle’s propulsion subsystem.
Structure is the static, time-independent aspect of the system:
Structure of a system is its form—the assembly of its physical and informatical
components along with the long-lasting relations among them.
Behavior is the varying, time-dependent aspect of the system:
Behavior of a system is it dynamics—the way the system changes over time by
transforming systemic (internal) and/or environmental (external) objects.
## 9.4.5 The Need for Concurrent Structure-Behavior Modeling
During analysis and design, facts and ideas about objects in the system and its environment, and processes
that transform them are gathered and recorded. For almost each process that is discovered or contemplated,
the first questions asked refer to the objects involved in this process. Similarly, for each object identified in
the system, a key question is what processes this object participates in. As soon as a new object is introduced
into the system, the process that transforms it or is enabled by it begs to be modeled as well.
There is thus intimate cohesion of the two key system facets: structure (objects and relations among
them) and behavior (processes and their relations to objects). Due to this structure-behavior
complementarity, system analysts and architects intuitively and justifiably tend to model the structure and
the behavior of the system concurrently.
With its single, unifying object-process model, OPM caters to this structure-behavior concurrent
modeling requirement. It enables modeling these two major system aspects at the same time within the
same model without the need to constantly switch between different diagram types.
For an investigated (as opposed to an architected) system, the researcher tries to make sense of gathered
observations and to understand their cause and effect relations. In a sense, an attempt is made to reverse-
engineer the system under study, which is the task of scientists. In both the architected and the
investigated system cases, the system’s structure and behavior go hand in hand, and it is very difficult to
understand one without the other, so presenting both in the same single diagram makes sense.
## 9.4.6 System Architecture
With the understanding of what structure and behavior are, we can define a system’s architecture.
Architecture of a system is the combination of the system’s structure and behavior
which enables it to perform its function.

Conceptual Modeling: Purpose and Context
It might be interesting to compare our definition of architecture to the one used by the U.S. DoD
Architecture Framework (DoDAF 2007), which is based on IEEE STD 610.12:
Architecture: the structure of components, their relationships, and the principles and guidelines
governing their design and evolution over time.
TOGAF (2011) provides a similar definition in response to the question “What is an Architecture?”
An Architecture is the fundamental organization of something, embodied in its components, their
relationships to each other and the environment, and the principles governing its design and
evolution.
The common element in both definitions and our definition of architecture is the system’s structure.
However, the DoDAF and TOGAF definitions lack the integration of the structure with the behavior to
provide the function. On the other hand, the DoDAF definition includes “the principles and guidelines
governing the design and evolution of the system’s component over time”. However, these do not seem to
be part of the system’s architecture. Rather, principles and guidelines govern the architecting process,
which culminates in the system’s architecture. Interestingly, DoDAF Architecture Framework Version
2.02, Change 1 (DoDAF 2015), the version of January 2015 does not contain any clear definition of
architecture (and neither does the 2009 edition)!
## 9.4.7 System Environment and Thing’s Affiliation
In recent years, the term environment has increasingly taken on the meaning of the ecosystem of planet earth
in which we all live and which is continuously compromised as a result of cumulative effects of large-scale
man-made systems (such as power plants) and a large number of smaller scale man-made system (such as
automobiles and aircrafts). Our definition of the system’s environment is indeed compatible with this
realization, as it provides for the possibility that the environment can change as a result of the system’s
function.
The system’s environment is a collection of things that are outside the system but
interact with it.
The interaction of the system with its environment causes the system, and possibly its environment, to
change. To ensure sustainability, systems engineers must make sure to prevent or undo this adverse
change, especially as it pertains to possibly irreversible detrimental effects of current and contemplated
systems on global warming and natural resource depletion. This is not just a moral or ethical obligation—
it is a matter of securing sustainable life on earth of all organisms, including people, beyond the next
couple of decades…
A thing which is part of the system is systemic, while a thing which is part of the system’s
environment is environmental. The OPM thing’s attribute whose values are systemic and environmental
is affiliation. Making the distinction between systemic and environmental things is very important in
modeling, as it indicates what are the things that the architect can have control of and what should be
considered as given. For example, in designing a gas station, is the car systemic or environmental?
Obviously, cars and their drivers are going to interact with the gas station, but the gas station architect
does not have a control over the sizes of the cars and the locations of their gas tank openings—these are
given and must be accounted for. Therefore, car is environmental to gas station.

## 9.4.8 Function Versus Behavior
The above definitions lead to the conclusion that the function of a system is its top-level process. Moreover,
the architecture of the system, namely its structure-behavior combination, is what enables the system to
execute its top-level process, thereby to perform its function and deliver value to its beneficiary.
The value of the function to the beneficiary is often implicit; it is expressed in process terms, which
emphasize what happens, rather than the purpose for which the top-level process happens. This implicit
function statement can explain why the function of a system is often confused with the behavior or
dynamics of the system. However, it is critical to clearly and unambiguously distinguish between the two,
namely between function and behavior. Behavior is how the system changes along the time dimension.
Function is what value the system delivers to its beneficiary through its operation. Hence, behavior is
objective—it is the way the system changes, regardless of who describes the change, while function is
subjective—it is the value gained from the beneficiary’s perspective. This distinction between function
and behavior is of utmost importance since in many cases a system’s function can be achieved by
different architectures, i.e., different combinations of processes (system behavior) and objects (system
structure).
Consider, for example, a system for enabling humans to cross a river with their vehicles. Two obvious
architectures are ferry and bridge. While the two systems’ function and top-level process—river
crossing—are identical, they differ dramatically in their structure and behavior. Failure to recognize this
difference between function and behavior may lead to a premature choice of a sub-optimal architecture.
In the example above, this may amount to making a decision to build a bridge without considering the
ferry option altogether.
## 9.5 Language and Modeling
We now turn to definitions that concern language and modeling.
A language is a means of communication among humans, and possibly also machines,
to express concepts, ideas, processes, and methods.
A language comprises two components: syntax and semantics.
Syntax is the language’s set of symbols and rules that specify how the symbols can be
combined to yield syntactically-legal constructs.
Not any syntactically-legal construct in the language is meaningful.
Semantics is the meaning that a subset of the language’s syntactically-legal constructs
conveys.
## 9.5.1 Model and Modeling
Languages not only enable humans and machines to communicate; they are also means to building models.

Conceptual Modeling: Purpose and Context
A model is an abstraction of some portion of conceived reality (the system “as-is”) or
of a contemplated system (the system “to-be”) expressed in some language.
For example, a sufficiently detailed textual description of a machine part in free English text can be
considered a model of that part. However, this model is not formal as it is expressed in English, a natural,
non-formal language. Hence, at least with current technology, it cannot be automatically constructed or
analyzed, requiring a human in the loop.
A modeling language is a language for constructing models in some domain.
A formal modeling language is a modeling language that has a mathematically-
grounded syntax definition, enabling its automated analysis, checking, and synthesis.
For example, machine drawings of mechanical parts utilize a formal modeling language, drafting, in
which symbols convey formal syntax with agreed-upon semantics that mechanical engineers understand
and share. Thus, a dash-dotted line expressed an axis of symmetry, a dimension set with arrows, guides
and a text box expresses a part’s dimension, etc.
A formal modeling language is expressed using one or two modalities, i.e., modes of expression. Two
prominent modalities for expressing models are graphics and text. OPM is unique in that it is the only
known modeling language which uses these two modalities interchangeably and in tandem.
Modeling is the process of creating a model in some domain using a modeling
language that is appropriate for that domain.
Modeling is a foundational engineering activity. The resulting model is a centerpiece infrastructural
entity that supports the evolution of the system throughout its lifecycle in a “model-based” or “model-
driven” context.
## 9.5.2 Informal Versus Formal Models
People are used to freely drawing informal models of systems. The ad-hoc symbols in such models are
inconsistent and cannot scale up, allowing for expressing only simple system ideas. An example of such an
informal model is provided in Fig. 9.5. As the legend tells us, hatching of the boxes differentiates between
lifecycle processes and the “product hierarchy”. This ad-hoc model leaves many questions unanswered. For
example, what is the semantics of the implied hierarchy? Is it aggregation? Specialization? Why does a
system contain lifecycle processes alongside products? Why does one product consist of five subsystems
and the other of none? Interestingly, this model appears in an international standard (ISO/IEC 26702 IEEE
Std. 1220-2005), which, of all documents, should maintain the highest level of formality possible. Clearly,
this model lacks formality and presenting it as part of an international standard can be more misleading than
leaving it out.
A formal model is a model expressed in a formal modeling language.
Continuing our machine drawing example, a part drawing is a formal three-dimensional model of that
part. A CAD/CAM system which is designed to “understand” this language can automatically generate an

actual part from this model. As another example, Newton’s second law, F= m×a, is a formal model of the
relation between a rigid body’s force, mass, and acceleration, expressed as a mathematical equation.
Interestingly, however, the rigid body, with which this model is concerned, with mass and acceleration
being its attributes, is nowhere to be found in this model. Rather, it is implicit that this is the subject of
this model. This still conforms to our definition of a model as an abstraction of some portion of conceived
reality.
System
Product Product
Development
and test
processes
Manufac
-turing
process
Distribution
and support
processes
Operations
and training
processes
Disposal
process
Subsystem Subsystem Subsystem Subsystem Subsystem
Elements of the product hierarchy
Life cycle processes
### Figure 9.5
An example of an informal model—Basic building blocks of a system (ISO/IEC 26702 IEEE Std. 1220-2005)
A conceptual model is a formal model of a system which expresses its architecture by
depicting its structure and behavior to a level of detail that is sufficient for its
subsequent detailed design and eventual materialization.
The part of OPM that specifies how to construct Object-Process Diagrams (OPDs) along with their
textual representations in OPL is an example of a conceptual modeling language. SysML is another
example.
A conceptual modeling language is a formal modeling language for constructing
conceptual models of systems.
## 9.5.3 Complexity Management
In later chapters, we discuss in detail how OPM handles complexity management. Briefly, each thing (object
or process) can undergo two refinement mechanisms: in-zooming and unfolding. In-zooming of processes
specifies the subprocesses of a process and their temporal ordering. In-zooming of objects specifies the parts
of an object and (roughly, to the extent relevant and possible) also their spatial ordering (currently only

Conceptual Modeling: Purpose and Context
schematically and in two dimensions). Unfolding of things (objects or processes) exposes their parts,
features (attributes or operations), specializations, or instances. Both refining processes—in-zooming and
unfolding—can be done in the same OPD or in a new OPD. New OPD refining (in-zooming or unfolding)
creates a new OPD in which the refined thing is elaborated to express more details.
## 9.6 Summary
Science can be thought of as reverse engineering of nature.
The Minimal Ontology principle states that if a system can be specified at the same level of
accuracy and detail by two languages of different ontology sizes, then the language with the
smaller size is preferred over the one with the larger size.
Objects exist, processes happen.
Ontology is a set of concepts and their relations in some domain of discourse.
A minimal universal ontology is the ontology that is necessary and sufficient to model the universe
and systems in it.
The Object-Process Theorem: Stateful objects, processes, and relations among them constitute a
minimal universal ontology.
The Object-Process Assertion: Using stateful objects, processes, and relations among them, along
with refinement mechanisms of in-zooming and unfolding, one can conceptually model systems in
any domain and at any level of complexity.
The thing importance OPM principle: The importance of a thing T in an OPM model is directly
related to the highest OPD in the OPD hierarchy where T appears.
An object is a thing that exists or can exist physically or informatically.
A state is a possible situation or position at which an object can be for some positive amount of
time.
Transformation of an object is (1) creation (generation, construction), (2) consumption
(elimination, destruction), or (3) effect—change in the state of that object.
A process is a thing that transforms an object.
The object transformation by process OPM principle: In a complete OPM model, each process
must be connected to at least one object that the process transforms or one state of the object that
the process transforms.
A system is a function-providing object.
A stakeholder is an individual, an organization, or a group of people that has an interest in, or
might be affected by, a system being contemplated, developed, or deployed.
A beneficiary is a stakeholder who extracts value and benefits from the system.
A customer is the stakeholder who orders the system and sponsors its development,
implementation, deployment, and support.

A user is a stakeholder who operates the system or directly interacts with it.
A supplier is a stakeholder who oversees the development, support, and maintenance of the system
or product.
A function of an artificial system is its top-level value-providing process, as perceived by the
beneficiary.
Structure of a system is its form—the assembly of its physical and informatical components along
with the long-lasting relations among them.
Behavior of a system is it dynamics—the way the system changes over time by transforming
systemic (internal) and/or environmental (external) objects.
Architecture of a system is the combination of the system’s structure and behavior which enables it
to perform its function.
The system’s environment is a collection of objects that are outside the system but interact with it,
causing the system and possibly its environment to change.
The function-behavior distinction: Behavior is how the system changes along the time dimension,
while function is what value the system delivers to its beneficiary through its operation.
A language is a means of communication among humans, and possibly also machines, to express
concepts, ideas, processes, and methods.
Syntax is the language’s set of symbols and rules that specify how the symbols can be combined to
yield syntactically-legal constructs.
Semantics is the meaning that a subset of the language’s syntactically-legal constructs conveys.
A model is an abstraction of some portion of conceived reality or of a contemplated system
expressed in some language.
A modeling language is a language for constructing models in some domain.
A formal modeling language is a modeling language that has a mathematically-grounded syntax
definition, enabling its automated analysis, checking, and synthesis.
A formal model is a model expressed in a formal modeling language.
A conceptual model is a formal model of a system which expresses its architecture by depicting its
structure and behavior to a level of detail that is sufficient for its subsequent detailed design and
eventual materialization.
A conceptual modeling language is a formal modeling language for constructing conceptual
models of systems.
## 9.7 Problems
1. Referring to the OPD in Fig. 7.4, find:
A process which is more important than an object,

2. 3. 4. 5. Conceptual Modeling: Purpose and Context
an object which is more important than a process,
an object and a process of equal importance,
two objects of equal importance, and
two objects of equal importance.
Explain why removing stateful objects, processes, or relations among them from the minimal
universal ontology makes it unusable.
Model a small OPD which is syntactically correct but semantically not.
Explain the connection between the object transformation by process OPM principle and the
definition of process.
Define two architectures for each one of the systems that deliver the following
a
. River crossing
b
. Time-of-day showing
c
. Food shelf-life prolonging
d
. Humans transporting
e. Movie viewing
