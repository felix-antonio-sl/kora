# Chapter 10 Things: Objects and Processes
Each convex mirror shall have … marked at the lower edge of the mirror’s reflective
surface… the words “Objects in Mirror Are Closer than They Appear.”
U.S, PART 571 Federal Motor Vehicle Safety Standards, Sec. 571.111 S5.4.2 (2004)
Immanuel Kant said that “Objects are our way of knowing.” While this is obviously true, it is not the
whole truth, but only about half of it. Objects are our way of knowing what exists, or in other words, the
structure of systems. To know what happens, to understand systems’ behavior, a second, complementary
type of things is needed—processes. We know of the existence of an object if we can name it and refer to
its unconditional, relatively stable existence, but without processes we cannot tell how this object is
transformed—how it is created, how its states change over time, and how it disappears. These two
fundamental concepts—objects and processes, generalized as things—are the focus of this chapter.
## 10.1 The Object-Oriented Versus The Object-Process Approach
As we saw in Sect. 9.2.5, objects and processes are the two types of OPM’s universal building blocks, and
processes are modeled as “first class citizens” that are not subordinate to objects. This object-process
orientation is a principal departure from the object-oriented (OO) software paradigm, which places
objects as the only major players. Objects “own” processes, which in the OO nomenclature are often
called “operations” or “services” or “methods”.
Major system-level processes can be as important as, or even more important than objects in the
system model. Hence, processes must be amenable to being modeled independently of a particular object
class. This is in line with the thing importance OPM principle, introduced in the previous chapter, which
states that the importance of a thing T in an OPM model is directly related to the highest OPD in the OPD
hierarchy where T appears. This object-process status equality paradigm enables OPM to conceptually
model real-world systems in graphics and text.
Being able to tell objects and processes apart and use them properly in a model is a key to mastering
OPM. To define these fundamental concepts and to communicate their semantics, we shall first discuss
“existence” and “change,” laying the foundation for defining objects and processes and distinguishing
between them. We will then introduce the “essence of things” and examine the difference between
“physical” and “informatical” things. The word informatical, or cybernetic, refers to a generalization of
being related to data, information, knowledge, expertise, or ingenuity without any reference to their
physical manifestation.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_

Things: Objects and Processes
## 10.2 Existence, Things, and Transformations
Webster’s New Dictionary (1997) defines existence as the noun derived from exist, which is be, have
being, continue to be. To exist means to stand out, to show itself, and have an identifiable, distinct
uniqueness within the physical or mental realm. A thing that exists in physical reality has “tangible being”
at a particular place and time. Because it stands out and shows itself, we can point to it and say: “Now,
there it is.”
To stand out means to present a stable form against a background of something else that exists. The
notion of “background” is essential, for if there were nothing else that existed, there could not be the
contrast of one thing standing out and distinguishing itself from a background of things that exist along
with it. The stable form that the existing thing must exhibit is “substantially unchanging” long enough
(relative to the typical rate of change of the background) for it to be recognized as “standing out.” That
which we cannot identify, nor have its identity be inferred in some way, can have no existence for us. In
other words, “to stand out” requires a continuous identifiability over an appropriate duration of time,
either physically or informatically.
Considering existence along the time dimension, there are two modes of “standing out,” or existence
of things. In the first mode, the “standing out” takes place during a positive, relatively substantial time
period. This “standing out” needs to be observable in a form that is basically unchanging, stable, or
persistent. We call that which stands out in this mode object. Webster’s Dictionary (1997) defines an
object as a material thing; that to which feeling or action is directed; end or aim; word dependent on a
verb or preposition. The verb on which the object “depends” is the syntactic manifestation of process.
Indeed Dictionary.com defines verb as “The key word in most sentences, the word that reveals what is
happening.” The pattern in our minds of “what is happening” is the process.
## 10.2.1 Object Refined
An earlier version of Webster’s Dictionary (1984) provides a different set of two relevant definitions for
object:
Anything that is visible or tangible and is stable in form.
Anything that may be apprehended intellectually.
These two definitions respectively correspond to our notions of physical and informatical (or cybernetic)
objects. The first definition is the one we normally think of when using the term object in daily usage.
The second definition pertains to the informatical, conceptual, cybernetic, logical, intangible facet of
objects. Informatical objects are different from their physical counterparts in that they have no physical
existence, so they are not subject to the laws of physics. However, the carrier of an informatical object is
a physical object; the existence of informatical objects depend on their being symbolically recorded,
inscribed, impressed, or engraved on some physical medium: a stone, papyrus, paper, an electromagnetic
medium, or a group of neurons in a brain. This is where the physical and informatical aspects of an
informatical object are tangential, giving rise to concepts such as noise and the correspondence between
statistical mechanics and information theory through entropy (Shannon and Weaver 1949).
Since OPM objects are physical or informatical, we define object as something that captures these two
facets without committing to either one, while including the element of “existence throughout time.”

An object is a thing that exists or has the potential of physical or informatical
existence.
This definition is quite remote from the classical definitions of object in the OO literature, which can
be phrased as “An object is an abstraction of attributes and operations that is meaningful to the system.”
For example, in the eBook Object-Oriented Programming Basics with Java, an object is defined as “an
encapsulated completely-specified data aggregate containing attributes and behavior.”
## 10.2.2 Objects and Human Memories
Qualifying the human brain as a tangible medium that can store intangible things may perhaps seem to
some readers cynical or inappropriate. It therefore deserves special discussion and justification. The
central nervous system, of which the brain is the major part, is the information system in humans and
other organisms. It controls and regulates the entire organism. The human recollection or the mental
record of a thing is still a mostly mysterious way that a thing is inscribed in one’s mind, but progress in
understanding brain structure and function is being constantly made (e.g., Kostovic and Rakic 1990).
Among many other, more elated capabilities of intelligence and emotions, the magnificent capability
of the human brain to remember things qualifies it as a superb recording medium. A human brain stores
vast amounts of data, information, and knowledge of various forms that are the essential basis for
intelligence, including inference, prediction, decision-making and behavior. Human memories are not just
a series of objects representing facts, images, faces, names, shapes, figures, forms, and symbols. They
also include structural and behavioral relationships that exist among these objects, and the rules that
govern them. Anything that is recorded in the human brain is an informatical object. This informatical
object may be the record of some (tangible and/or intangible) set of objects and the processes that the
objects in the set undergo.
## 10.3 Object Identity
The identity of objects is important, yet elusive. Physical objects must be treated differently than
informatical objects. Since a physical object is made of matter (or energy, which, following Einstein’s
teachings can be converted to matter and vice versa), two instances of a physical object are identical if
and only if they occupy the same space at the same time. This is possible if and only if the two are
actually the same object, implying that no two distinctly identifiable instances of a physical object are the
same. Thus, two new identical cars of Model X that just emerged from the assembly line are different
instances of the same object class.
## 10.3.1 The Identity of Informatical Objects
The situation with object identity is different when informatical objects are concerned, since here the
essential object feature is the idea, concept, pattern, or symbol it represents, rather than physical matter
documenting it. From the physical medium point of view, each informatical object instance, such as a
copy of the same book, is distinct, just like the two cars emerging from an assembly line. However, from

Things: Objects and Processes
the informatical point of view, all the physical copies of some informatical object are the same. Two
copies of the same book are identical insofar as their informatical content (semantics) is considered. They
are printed on separate pages and bound as two distinct physical object instances. Even if one copy is a
paper copy and the other is electronic, from the informatical viewpoint they are still the same.
From the informatical viewpoint, two identical (paper or computer) files containing blueprints and
manufacturing instructions for a Model X car are, the same object, because the informatical content they
convey is identical. Physically, the pieces of media, on which this physical object is recorded, are
different, since they are physical matter that obeys the laws of nature. Likewise, two copies of the same
file are physically different, as they occupy different address spaces in the computer’s primary or
secondary memory. However, when viewed as informatical objects, they are identical.
## 10.3.2 Process as a Transformation Metaphor
We noted that there are two modes of standing out. The first is in space, the second—in time. In the time
mode of “standing out”, the standing out is still of an object, but this time it occurs “in a changing way”
against a background, which is substantially stable. Because the object that stands out is undergoing
transformation, it may have different names before and after the transformation. It is convenient to think
of the thing that has brought about a transformation as some carrier that is “responsible” for this
transformation.
When we are inclined to think in this way, what we really are thinking about is the patterned
changing, the series of transformations that one object or more undergo. For the convenience of language
or thinking, we associate this patterned changing with the “carrier,” to which we mentally assign the
“responsibility.” We define transformation as a generalization of change, generation and destruction of an
object.
Transformation is generation (construction, creation) or consumption (destruction,
elimination) or change (effect, state transition), of an object.
## 10.3.3 Process Definition Refined
According to Webster’s dictionary (1997), a process is “a state of going on, series of actions and changes,
method of operation, action of law, outgrowth.” The American Heritage Dictionary (1996) defines
process as “a series of actions, changes, or functions, bringing about a result.” In Dictionary.com, verb,
which is roughly the syntactic analogue of process, is defined as “The key word in most sentences, the
word that reveals what is happening.”
We call the carrier that causes transformation process, and we say that the process is “that which
brought about the transformation” of an object. However, that carrier is just a metaphor, as we cannot
“hold” or touch a process, although that process may be entirely physical, as it involves transformation of
one or more physical objects. The only thing(s) we may be able to touch, see, or sense in any other way,
is the object being transformed. We can measure one or more of the object’s attribute values at certain
points in time, or as the process is transforming that object. For example, we can measure the values (in
degrees Celsius) of the temperature attribute of an iron bar object as it undergoes the process of heating,
or we can touch it and feel it getting hotter relative to some past time point, but we cannot touch the
heating process.

At any given point in time before, during, or after the occurrence of the process, the observed object
can potentially be different from what it was in a previous point in time. Using our human memory, we
get the sense of a process by comparing the present form of the object being transformed to its past form.
Hence, a process exists only as a concept, a mental construct in humans’ minds. We give names to
processes to refer to changing patterns of objects. Focusing on transformation, we adopt the following
definition.
Earlier we said that objects exist and processes happen. Here we just said that a process exists, but
only as a mental construct. In this regard, we could think of processes as (mental) objects too, and devise
a modeling paradigm that is based only on objects as “first class citizens”, arguably having an even more
compact universal ontology than OPM. Indeed, this is the object-oriented approach. However, as we
show throughout the book, the value of adding process as a concept in the universal ontology that is
separate from object far exceeds the price of adding another concept to this ontology.
A process is a mental construct representing a pattern of object transformation.
This definition of process acting on an object immediately implies that no process has meaning unless
it is associated with at least one object—that which the process transforms. The transformation of the
object(s) is the necessary and inevitable result of the process execution. This is the first instance in which
the symmetry between objects and processes breaks. While we defined and could refer to an object
without necessarily using the term “process,” the ability to define and think of a process, including its
transformation, depends on the existence of at least one object being transformed by that process.
Referring to the syntactic meaning of object, Dictionary.com provides the following definition:
Grammar. (in many languages, as English) a noun, noun phrase, or noun substitute representing by
its syntactical position either the goal of the action of a verb or the goal of a preposition in a
prepositional phrase, as ball in John hit the ball…
Here, like in our definition, a linkage is made between the object and the verb, which is the process. In
John hit the ball, hitting is the process and ball is the object. This example shows that it is often the case
that the syntactic term object—that to which action is directed—coincides with the semantic term object.
However, semantically, John is also an object (an instance of the object person), while syntactically it is a
subject. The syntactic term verb is often analogous to the semantic term process. We elaborate on this in
Sect. 10.6 when we discuss the process test.
## 10.3.4 Transformee Defined
When we say that the process brought about the generation of an object, we mean that the object, which
had not existed prior to the occurrence of the process, now exists—it is identifiable against its
background. Analogously, when we say that the process brought about the elimination of an object, we
mean that the object, which once stood out, cannot be identified so it no longer exists. These radical
changes of generation and elimination are extreme versions of transformation. A less radical
transformation is change of the objects’ states. The object which a process transforms is called
transformee.
Transformee of process P is an object that P transforms.

Things: Objects and Processes
We use the suffix “ee”, as in employee, here and in several other cases defined soon, to create a new
word that denotes an object which a process (verb) X acts on. Here, X = Transform. We will soon
encounter also Consumee, Resultee, and Affectee.
In a theoretic, frozen, static universe at absolute zero, no processes exist and no transformation occurs.
Without processes, all we can describe are static, persistent structural relations among objects. In realistic
earthly settings, processes and objects are of comparable importance as building blocks in the description
and understanding of natural systems and the universe as a whole (which is the mission of science), and
of designing artificial systems (which is the mission of engineering).
## 10.3.5 Cause and Effect
One insight from investigating the time relationship is cause and effect. Certain objects, when brought
into the right spatial and temporal relationship (e.g., being at the “same” place at the “same” time), enable
a process to take place, causing at least one object to be transformed: When the process is over, at least
one of the objects involved (as input, output, or both) is transformed (consumed, generated, or changed).
The “cause” in the “cause and effect” idiom is a triggering event that takes place in the concurrent or
otherwise time-orchestrated presence of the collection of objects, some of which might need to be in a
certain state. The “effect” in this “cause and effect” idiom is the transformation that one or more of these
objects undergo.
For example, running of an internal combustion engine is contingent upon the presence of the objects
air and gasoline vapor mixture inside the object cylinder at the right pressure and temperature (attributes
of mixture). The triggering event is the point in time when a spark (created by a previous timed process)
ignites the mixture. As a result of this process, the gasoline mixture is consumed and the piston’s kinetic
energy value increases. In feedback, cause and effect are circular: The effect at a given time is the cause
for a change later.
## 10.4 Syntax Versus Semantics
To make it possible to refer to things (objects and processes) and distinguish among them, natural
languages developed by humans to enable communication, assign names to the things. The name of a
thing constitutes a primary identifying symbol of that thing, making it amenable to reference and human
communication. These thing names are known as nouns. However, being part of speech, noun is a
syntactic term, while objects and processes are semantic terms. We elaborate on this issue next.
## 10.4.1 Are Objects and Processes the Semantic Analogues of Nouns and Verbs?
In natural languages, almost invariably, objects are syntactically represented as nouns. Processes are
syntactically often represented as verbs, but they can be nouns too. For example, brick is syntactically a
noun and semantically an object, while constructing is a verb and a process. However, construction in the
context of “the construction process” is also a noun, although semantically it is the same as “the
constructing process.” To make the point, we note that the phrase the construction process is plausible,
while the brick process is not. Likewise, the phrase the brick object is plausible, while the construction
object (where object is not referred to as a synonym for goal) is much less plausible. Even more

confusing is the object building (noun), which is the outcome of the building (constructing) process. It is
spelled and uttered the same as the process of building (verb). It is only from their context inside a
sentence that these two semantically different words are distinguishable.
A common software design strategy is the noun/adjective/verb object oriented design strategy
(MacIntyre 2010). In his blog, MacIntyre wrote:
… Then I learned C++, object oriented programming, and was introduced to the holy grail of object
oriented design advice, which went something like this: Take your requirements and circle all the nouns,
those are your classes. Then underline all the adjectives, those are your properties. Then highlight all your
verbs, those are your methods.
This Noun/Adjective/Verb design strategy seemed like the most ingenious piece of programming wisdom
ever spoken … but it’s led us down a misguided path. It’s the verb that’s misunderstood. The verb
should be another class, not a method. It should be a process class. As a programming concept, a
process is just as much a ‘thing’ as any real world object. The verb should be a class, which accepts the
noun as an input to be processed.
Interestingly, MacIntyre intuitively arrived at the conclusion that the verb is “another class”
(emphasis in source). He realized that a process is not less important than an object, and therefore should
not be a method owned by an object but a “process class” in its own right.
The examples discussed above demonstrate that the tempting assertion that object and process are the
semantic analogues of the syntactic concepts noun and verb is at best crude and inaccurate. Hence, rather
than relying on the syntactic notions of parts of speech, we need to establish a semantic, content-based
way to analyze words in a sentence that would enable us to tell objects from processes. This will enable
us to overcome the pitfalls and idiosyncrasies of natural languages.
## 10.4.2 Syntactic Versus Semantic Sentence Analysis
The difficulty we often experience in making the necessary and sufficient distinction between objects and
processes is rooted in our education: As students in high school, we have been trained to think and
analyze sentences in syntactic, parts of speech terms—nouns, verbs, adjectives and adverbs—rather than
in semantic, deeper sense-making terms—objects, processes, attributes, and operations. This is probably
true for any natural language we study and use, be it our mother tongue or a foreign language.
The same idea can very often be expressed by more than one sentence, giving rise to different
assignments of parts of speech. Semantic sentence analysis is the dissection of a sentence by its semantics
rather than its syntax. Only through semantic sentence analysis can we overcome superficial differences
in expression and get down to the intent of the writer or speaker of some text. Nevertheless, the idea of
semantic sentence analysis, in which we seek the deep meaning of a sentence beneath its appearance, is
probably a relatively less accepted idea.
To apply OPM in a useful manner, one should be able to analyze sentences semantically. This
primarily entails telling the difference between an object and a process. How to do this systematically is
the topic of the next sections. First we define three sets of objects with respect to their participation and
role in a process.

Things: Objects and Processes
## 10.4.3 The Preprocess Object Set
For a process to start, it needs to be triggered. This triggering can be external, by an object becoming
existent or available or by an object entering a certain state, or internal, by an event marking the end of a
preceding process in the context of a higher-level, in-zoomed process. Once triggered, the process “tries”
to operate (occur, happen, or execute). To this end, it needs to check for the existence of a set of objects—
the preprocess object set—which would allow it to be performed.
The preprocess object set of a process P, Pre(P), is the set of objects required to exist,
possibly in certain states, in order for P to start executing once it was triggered.
The triggering object itself is not part of the preprocess object set. Existence of the preprocess object
set, is the process precondition—the condition for the occurrence of the process. Being a process, the
noun representing it does not exist, but rather occurs, happens, operates, executes, transforms, changes, or
alters at least one other noun, which would be an object.
Let us consider two process examples: Flight and Manufacturing, shown in Fig. 10.1. In the Flight
example (the OPD on the left), Airplane, Pilot, and Runway are objects in the preprocess object set, since
Flight cannot occur without them. In set notation: Pre (Flight) = {Airplane, Pilot, Runway}.
For Manufacturing (the OPD on the right), the preprocess object set consists of Raw Material,
Operator, Machine and Model: Pre (Manufacturing) = {Raw Material, Operator, Machine, Model}. Product
is not in this set since it does not exist yet and is not needed for the process to start happening.
### Figure 10.1
Preprocess and postprocess object set examples
There may be requirements on the states of some of the objects in the preprocess object set. For
example, as the OPD on the left in Fig. 10.2 shows, in order for Flight to take off, it is required that
Runway be (at the state) open. In set notation: Pre (Flight) = {Airplane, Pilot, open Runway}. In other
words, this is expressed in the corresponding OPL sentence:
Flight requires open Runway.

### Figure 10.2
Example of a state-specified object, open Runway, in the preprocess object set of Flight
Similarly, as the OPD on the right in Fig. 10.2 shows, in order for Manufacturing to take place, it is
required that Machine be operational and Model be updated. In this case, the result will be pre-tested
Product. In set notation: Pre (Manufacturing) = {Operator, Raw Material, operational Machine, updated
Model}. This is expressed in the three corresponding OPL sentences:
Operator handles Manufacturing.
Manufacturing requires operational Machine and updated Model.
Manufacturing consumes Raw Material.
## 10.4.4 The Postprocess Object Set
The postprocess object set is defined analogously to the preprocess object set as follows.
The postprocess object set of process P, Post(P), is the set of one or more objects that
exist, possibly in certain states, after P finished executing.
Existence of all the objects in the postprocess object set, some possibly in specified states, is the
postcondition of that process.
The preprocess object set and the postprocess object set are not necessarily disjoint; they may be at
least partially overlapping. In the Flight example in Fig. 10.1, all three objects in the preprocess object set,
Airplane, Pilot, and Runway, are also in the postprocess object set: Post (Flight) = {Airplane, Pilot,
Runway}. We should note, however, that only Airplane and Pilot are transformed: their Location attribute
change from origin to destination. In Fig. 10.2 this is not modeled explicitly, only implicitly, specifying
that Airplane and Pilot each undergoes some state change.
In the Manufacturing example in Fig. 10.1, Raw Material, Operator, Machine and Model are in the
preprocess object set, while Operator, Machine, Model, and Product are in the postprocess object set: Post

Things: Objects and Processes
(Manufacturing) = {Operator, Machine, Model, Product}. Raw Material is transformed by being
consumed, while Product is transformed by being created.
If a process affects and object then the input state—the state of the affected object prior to the process
occurrence—is different than the output state—the state of the affected object following the process
occurrence. In this case, while the same object is in both the preprocess object set and in the postprocess
object set, it is in different states. This is demonstrated in Fig. 10.3, where pre-tested Product is in the
preprocess object set, while tested Product is in the postprocess object set.
### Figure 10.3
pre-tested Product is in the preprocess object set, while tested Product is in the postprocess object set
## 10.4.5 The Involved Object Set
The involved object set is defined as follows.
The involved object set of process P, Inv(P), is the union of P’s preprocess object set
and postprocess object set.
In set notation: Inv (P) = Pre (P) ∪ Post (P).
In the examples in Fig. 10.1, Inv (Flight) = {Runway, Pilot, Airplane}, and Inv (Manufacturing) =
{Operator, Machine, Model, Raw Material, Product}.
## 10.5 The Procedural Link Uniqueness OPM Principle
By the definition of process, a process transforms at least one object, so in a complete OPM model a
process must be linked to at least one object, or any one of its states, via a transforming link, either
directly or indirectly. A process and an object can be connected only via a procedural link, with the
exception of exhibition-characterization, which is a structural link. Any procedural link, with the
exception of invocation and exception links, connects a process with an object.
An object has some role with respect to a process. It can be an agent, an instrument, or a transformee.
Therefore, an object, or a state of an object, and a process cannot be connected by more than one
procedural link. This is the rationale behind the following procedural link uniqueness OPM principle.

The Procedural Link Uniqueness OPM Principle
At any level of detail, an object and a process can be connected with at most one procedural link,
which uniquely determines the role of the object with respect to the process.
The reason for qualifying this principle to a given level of abstraction is that at different abstraction
levels an object might be modeled differently. The role of an object can change with the level of detail.
The procedural link uniqueness guides the modeler to retain the most semantically meaningful model fact
at any given detail level.
### Figure 10.4
The procedural link uniqueness OPM principle demonstrated Left: Expressing Person as both agent and
affectee of Eating is made possible via state expression. Right: When the states are suppressed, only the effect link
remians
For example, in the OPD on the left of Fig. 10.4, when a Person is engaged in Eating, Person is both
the agent, since Person handles Eating, and the affectee of this process, since Eating changes Person from
hungry to satisfied. This is possible because the states hungry and satisfied of Person are expressed.
When the states are suppressed (on the right), we cannot have both agent and effect links between Person
and Eating, so we must make a choice. As we define formally and explain in more detail in Sect. 21.13,
the choice of the link is based on the precedence of the procedural links. Since a transforming (in our case
effect) link is semantically stronger than an enabling link (in our case agent), the effect link prevails. We
can still use both links if we zoom into Eating, exposing its three subprocesses: Food Picking, Food
Swallowing, and Food Digesting. Only the latter subprocess affects the Person, so now Person can be
linked with an agent link to Food Picking and Food Swallowing, and with an effect link to Food
Digesting. When zooming out of Eating and suppressing the states of Person, Person and Eating will
again be linked by the effect link, since overall the state of Person changed, in line with the link
precedence.
As another example, Truck is obviously an instrument for Transporting. Transporting zooms into
Loading, Moving, and Unloading. Loading changes Truck from unloaded to loaded, so Truck it is
obviously affected. However, after Moving is over, Unloading changes Truck back from loaded to
unloaded, so as a whole, inspecting Truck from the Transporting level, Truck is unaffected and hence can
be modeled as an instrument of Transporting rather than its affectee.

Things: Objects and Processes
### Figure 10.5
Role of abstraction with split state transforming links
An object may have the role of an instrument in an abstract OPD and a transformee in another
descendent, more detailed and concrete OPD. At the abstract OPD, the process does not appear to affect
the object, because the object’s initial state is the same as its final state. Therefore, at the abstract OPD the
object is an instrument, as indicated by an instrument link. However, at a descendent, more concrete
OPD, that same process does appear to change the state of that object from the initial state and then back
to the initial state.
As a final example, in Fig. 10.5, the left OPD (SD: Dish Washing System), a Dishwasher object is an
instrument for the Dish Washing process, since no change in state of the Dishwasher is visible at that
extent of abstraction. In the descendent OPD (SD1: Dish Washing in-zoomed), Dish Washing zooms into
Loading (of a dirty Dish Set), Cleaning (which changes Dish Set from dirty to clean), and Unloading (of a
clean Dish Set). Loading changes the state of Dishwasher from empty to loaded, while Unloading
changes it back from loaded to empty, so empty is both the initial and final state. While the Dishwasher
is an instrument in SD, the System Diagram, at the descendent, more detailed OPD, the Dishwasher is an

affectee—it becomes loaded and then empty again. The only effect visible in the System Diagram is the
effect on Dish Set.
## 10.6 The Process Test
As argued, while a basic tenet of OPM is the distinction between objects and processes, it is sometimes
difficult to tell an object from a process, especially if both are nouns. The object-process distinction
problem is stated simply as follows:
Given a noun, how can we tell if it is an object or a process?
The process test, specified in this section, is a formal procedure for solving the object-process
distinction problem. It enables identifying nouns that are processes rather than objects, a prerequisite for
successful system analysis and design.
By default, a noun is an object. To be a process, the noun must meet each one of the following three
process test criteria: (1) Object transformation, (2) time association, and (3) verb association.
Finally, if the outcome is still not clear, using common sense is of course the best option.
## 10.6.1 The Object Transformation Criterion
The object transformation process test criterion stipulates that a process must transform (consume, create,
or change the state of) at least one of the objects in the involved object set.
The object transformation criterion is satisfied if the noun in question transforms at
least one of the objects in the involved object set.
The membership of the transformee B of P is determined as follows.
If P consumes B then B ∈ Pre (P): B is only in the preprocess object set of P.
If P yields (creates) B, then B ∈ Post (P): B is only in the postprocess object set of P.
If P affects (changes the state of) B, then B ∈ Inv (P): B is in the involved object set, i.e., in both
the preprocess object set and the postprocess object set.
Enablers (agents or instruments) are also members of Inv (P) as their presence is required throughout
the entire duration of the process occurrence.
Continuing the previous examples, the Flight process transforms Airplane (by changing its Location
attribute from origin to destination). Hence, Airplane ∈ Inv (Flight). Manufacturing transforms two
objects: it consumes Raw Material and creates Product, hence Raw Material ∈ Pre (Manufacturing) while
Product ∈ Post (Manufacturing). Finally, Machine ∈ Inv (Manufacturing) since Machine is an instrument
for Manufacturing.

Things: Objects and Processes
## 10.6.2 The Time Association Criterion
The association with time process test criterion requires that the noun in question represent some
happening, occurrence, action, procedure, routine, execution, operation, or activity that takes a positive
amount of time along the timeline.
The time association criterion is satisfied if the noun in question can be thought of as
happening through time.
Continuing our example, both Flight and Manufacturing start at a certain point in time and take a
certain amount of time. Both time and duration are very relevant features of these two nouns in question.
## 10.6.3 The Verb Association Criterion
The association with verb process criterion requires that a process be associated with a verb.
The verb association criterion is satisfied if the noun in question can be derived from,
or has a common root with a verb or has a synonym which is a verb.
Flying is the verb associated with Flight. The sentence “The airplane flies” is a short way of
expressing the fact that the Airplane is engaged in the process of Flight. Similarly, to manufacture
(produce, yield, make, create, generate) is the verb associated with Manufacturing. The sentence “The
operator manufactures the product from raw material using a machine and a model.” is the natural
language short way of the OPL paragraph on the right in Fig. 10.1.
### Figure 10.6
An OPM model of the Process Test system
Here we rely on verb—a syntactic construct, but is not mandatory that the verb be syntactically from
the same root as the process name; it can be a synonym as long as the semantics is the same. For example,
Marrying is a process, which is associated with the verb to marry. To wed is also a legal verb, albeit less
frequently used. Alternatively, we could use Wedding to fit it to the verb wed. Many objects, such as

Apple and Airplane, are not associated with any verb, so they do not fulfill this process criterion. It is easy
to verify that both Apple and Airplane do not meet the other process test criteria either. Boundary cases of
things exist, as discussed in Sect. 10.10 with examples.
## 10.6.4 An OPM Model of the Process Test System
Figure 10.6 is an OPM model of the process test system.
The Noun in question is initially defined as object. Process Test is shown to be comprised of its three
criteria, Object Transformation Criterion, Time Association Criterion, and Verb Association Criterion,
each of which can be at a state accepted or rejected. The three instrument links from the three accepted
states of these three criteria indicate that only when all the three criteria are accepted, the Noun As
Process Defining process is enabled, changing Noun from object to process. The self-explanatory OPL
paragraph of this system is also recorded in Fig. 10.6.
## 10.7 Naming OPM Elements
Selecting appropriate names for OPM objects, processes, and states is very important, because names
affect how easily and how well our model is communicated to, and understood by, the target audience.
Naming conventions for processes and objects help humans to tell them apart. Moreover, since these
modeler-defined names are also embedded in the automatically-generated OPL sentences, these sentences
will make sense only to the extent that the entities names in them are meaningful and result in correctly
phrased OPL sentences. For example, in the OPL paragraph above, suppose we called this process simply
Process Testing. This would result in the following OPL sentences:
Process Testing requires accepted Verb Association Criterion of Noun, accepted Time Association Criterion
of Noun, and accepted Object Transformation Criterion of Noun.
Process Testing changes Noun from object to process.
After changing the process name, the following, more accurate OPL sentences are produced.
Noun As Process Defining requires accepted Verb Association Criterion of Noun, accepted Time Association
Criterion of Noun, and accepted Object Transformation Criterion of Noun.
Noun As Process Defining changes Noun from object to process.
## 10.7.1 Capitalization, Bolding, Phrase, and Thing Naming
The capitalization OPM convention is that the first letter in each word in the name of a thing (object or
process) is capitalized, while states are lower-case (non-capitalized). Thus, possibly injured Vehicle
Occupants Group denotes the object Vehicle Occupants Group at its possibly injured state.
### Figure 10.7
An OPM model of a box with one (left) and six (right) pencils

Things: Objects and Processes
Tags of tagged structural relations are also non-capitalized either, as in the OPL sentence “Box
contains Pencil.” which is the textual modality of the OPD on the left of Fig. 10.7. The tag contains along
the arrow from Box to Pencil is lower-case.
A phrase is a collection of one or more words that do not constitute a sentence.
Object naming is simple—it is a capitalized noun. Object names can be phrases with more than one
word, as in Apple Cake or Insurance Claim.
## 10.7.2 The Singular Name OPM Principle
An important OPM principle that must be adhered to while naming an object or a process is the singular
name OPM principle:
The Singular Name OPM Principle
A name of an OPM thing must be singular. Plural has to be converted to singular by adding the
word “Set” for inanimate things or “Group” for humans.
There are two reasons for defining this principle. First, an automated tool takes care of converting
singular to plural as needed. For example, in the OPD in the right of Fig. 10.7, when the participation
constraint (defined later) “6” is added, the OPL sentence now reads Box contains 6 Pencils. Second, we
want to be able to specify parts or attributes or specializations of a thing in its singular form.
So what should we do if we wish to model more than one instance? We convert the plural object in the
OPM model to singular by adding the word “Set” for inanimate things or “Group” for humans. Thus, the
object “Ingredients” (say, of a cake) becomes “Ingredient Set”, the process :“Modifications” becomes
“Modification Set”, and “Customers” becomes “Customer Group”.
## 10.7.3 Process Naming
Unless it makes no sense in English, the OPM process naming convention is to name a process by making
its last word a gerund, i.e., the root of the verb followed by the “ing” suffix, as in Igniting. We call this the
gerund process naming mode. If there are several choices, such as in Construction vs. Constructing, the
latter is preferable, unless domain experts indicate that the non-gerund form is the one that is commonly
used and understood in the domain.
This naming convention clarifies the dynamic nature of the process as a dynamic thing, a thing that
happens along the time dimension rather than a static thing that exists without change. To enhance clarity
and make the function of the process explicit, the gerund may be preceded by the primary object that the
process transforms, as in Engine Igniting. The object name that can precede the gerund qualifies the
process, making it a specialization of the original process. For example, Wall Painting and Car Painting
are two different (yet similar) processes that specialize Painting. Both transform the object being painted
by changing the color attribute value of the affectee (operand)—the object being painted. However, since
the objects being painted are different, the instruments and techniques of each kind of painting differ.

The process name in the running example in Part I of this book, Automatic Crash Responding, could
be simply Responding, but that might seem too general, since it does not specify what the response is for.
Even Crash Responding alone is not quite sufficient, as it could be done without an automated system.
We also avoid calling this process Response, as this name does not follow the gerund process naming
mode and can be justifiably conceived as an object—the outcome of the responding process.
The recommended gerund process naming mode comes in several versions of increasing length and
information content:
1. The transforming (verb) version: the process name (syntactically the gerund form of the verb, namely
verb + ing), as in Making or Responding.
2. The object transforming version: a concatenation of an OPM object (syntactically a noun) with the
process name (syntactically the verb’s gerund), as in Cake Making or Crash Responding. This is the
recommended naming mode in most cases.
3. The qualified transforming version: a concatenation of an attribute value (syntactically an adjective)
with the process name, as in Quick Making or Automated Responding.
4. The qualified object transforming version: a concatenation of an attribute value with an object and
the gerund. The attribute value can qualify the process, as in Quick Cake Making or Automatic Crash
Responding, or it can qualify the object, as in Sweet Cake Making or Fatal Crash Responding.
A second process naming option, often used by modelers, is the imperative process naming mode, as
in “respond” or more specifically, “respond to crash”, or “automatically respond to crash”. OPM
discourages this mode, because it is less compact and less elegant, and the OPL sentences created using
this mode in the current OPM 19450 are awkward. Modeling languages usually do not prescribe such
naming conventions. Modelers are therefore unaware of nuances such as the difference between the
gerund and imperative process name modes. The Functional Analysis approach advocates naming
functions imperatively: “Start Engine”. “Launch Missile”, “Turn Left”, but this does not seem to be a
premeditated and mandatory way, just a short and sometimes convenient way of expression.
Consequently, many modelers use both the gerund and the imperative process name modes
interchangeably or in a mixed way, making the model less coherent and unnecessarily more cognitively
demanding.
## 10.8 Thing Defined
We have seen that objects and processes are two types of tightly coupled and complementary things. Objects
cannot be transformed (generated, affected or eliminated) without processes, while processes have no
meaning without the objects they transform, and often also the objects that enable their occurrence. The
extent of this coupling is so intense that if we wish to be able to analyze and design systems in any
domain as intuitively and naturally as possible, we must consider objects and processes concurrently.
Objects exist as relatively persistent, static things, while processes occur as transient, dynamic things.
The extent to which objects and processes are interwoven is even lager; we must be able to specify
what state an object was at before the process affected it, which objects were consumed, and which were
generated. At the same time, we need to be able to show how parts, features and specializations
(discussed later) of these objects play role in subprocesses of the higher-level process.

Things: Objects and Processes
As we shall see, objects and processes have much in common in terms of being specified through
structural relations such as aggregation, generalization, and characterization. The need to talk about these
two concepts in a generalized way, without repeating “object or process” over and over again,
necessitates the advent of a yet more abstract term. We call this simply a “thing.”
Thing is a generalization of object and process.
The concept of “thing” enables us to think and express ourselves in terms of this abstraction and refer
to it without the need to reiterate the words “object or process”. Based on the ontology of Bunge (1987,
1989), Wand and Weber (1989, 1993) have used the term thing as a synonym to what we refer to as
object. Their first premise is that the world is made of things that have properties. According to this
definition, thing seems to be synonymous with object. However, during the last two decades, the term
object has become deeply rooted, at least in the software engineering community. In SysML and UML,
object has been replaced by the terms block and class, respectively. Interestingly, the emergence of the
term “Internet of Things” (IoT; Weber and Weber 2010) is in line with the notion of thing as a
generalization of object and process since IoT is about processes taking place among physical
interconnected objects.
## 10.9 Properties of OPM Things
A property is an attribute at the metamodel level. Property can be thought of as a meta-attribute—an
attribute of an element in a metamodel of OPM.
Property is an attribute of an OPM model element.
Unlike “regular” attribute, whose values can change during the execution of an OPM model, a property
value of any element in an OPM model is fixed. We will see an example at the end of this section. All
OPM things have the following three properties:
Perseverance, which pertains to the thing’s persistence and denotes whether the thing is static
(persistent), i.e. an Object, or dynamic (transient), i.e. a Process. Boundary examples of static,
persistent processes and dynamic, transient objects exist, as discussed later in this chapter. Based on
the value of Perseverance, this property of Thing discriminates between an Object and a Process. At
the model level we call such attributes discriminating attributes, as discussed in a later chapter.
Essence, which pertains to the thing’s nature and denotes whether the thing is physical or informatical.
Affiliation, which pertains to the thing’s scope and denotes whether the thing is systemic, i.e., part of
the system, or environmental, i.e., part of the system’s environment.
Graphically, as shown in Fig. 10.8, shading effects denote physical OPM things and dashed lines
denote environmental OPM things. All eight Perseverance-Essence-Affiliation property combinations of
an OPM thing shown in Fig. 10.8 may occur. The lower portion of Fig. 10.8 expresses, from left to right
and top to bottom, the OPL sentences corresponding to the graphical elements.
We noted that a property value of any element in an OPM model is fixed. Indeed looking at the
example of Perseverance, a property of an OPM Thing, if the value of a certain Thing in an OPM model
is set as static (i.e., the Thing is an Object), then this value is fixed and the Object cannot become a Process.

### Figure 10.8
OPM thing generic attribute combinations exemplified
## 10.9.1 Default Values of Thing Generic Properties
The Affiliation property of thing is by default systemic. With respect to Essence, we note that the
majority of things in non-trivial systems tends to have the same property value: either most of the things
in the system are physical or most of them are informatical. For example, Data processing systems are
informatical, although they have physical components. Transportation systems, such as a railway system
or an aviation system, are physical, although they have informatical components.
A system’s primary essence is the Essence value of the majority of the things in the
system.
The default essence value of a thing is the primary essence of the system. The motivation, based on
experience, for defining the primary essence is to save the modeler the need to mark the vast majority of
the things in the system as either informatical or physical. A supporting tool should therefore provide an
option for the modeler to specify a system’s primary essence as a means to reduce the amount of things
for which the modeler has to specify their essence.
The OPL paragraph corresponding to an OPD should not include an OPL sentence to indicate the
Essence or Affiliation value of a thing if it is the default, unless the thing is isolated—it has not yet been
connected to any other thing during the course of the modeling process. The reason for this is the need to
avoid violating the graphics-text OPM principle. Suppose the default essence of the OPDs in Fig. 10.9 is
physical. Upon drawing the physical object Car and prior to linking it to anything, the OPL sentence “Car
is physical” shall appear, as shown in the OPD on the left, otherwise there would be a thing (Car)
depicted in the OPD that has no mention in the OPL, violating the graphics-text OPM principle. However,

Things: Objects and Processes
as soon as the isolated thing becomes linked to another thing, as shown in the OPD on the right, the OPL
sentence dedicated to specifying the thing’s default Essence or Affiliation shall be removed.
### Figure 10.9
The primary essence of the Car Anti-lock Breaking System (ABS) is physical, therefore, once Car is linked to
ABS, the first sentence is removed from the OPL sentence
## 10.10 Boundary Cases of Things
While objects are persistent and processes are transient, boundary case of state-preserving (persistent)
processes and transient objects, exist. These are discussed in this section.
## 10.10.1 State-Preserving Processes
We have defined a process as a thing that transforms an object. There are cases in which the absence of a
process, rather than its occurrence, causes a change in the state of the object. One example is supporting:
Any object on Planet Earth (or on any other planet for that matter) is maintained in its vertical position by
a Supporting process that prevents it from freely falling. There is a whole family of such state-preserving
processes that have a static connotation as they act to maintain the state of an object rather than change it.
A state-preserving process is a process that acts to maintain a steady state or status
quo of an object rather than to change it.
The process of existing is the most prominent example, describing a situation of an object being “out
there” without specifying any change in that object. For biological objects, existing entails maintenance
of the necessary life processes, so they are definitely not static. Non-biological systems such as the solar
system or the global air traffic control system also exist while constantly changing.
Members of this state-preserving process family include such processes as Supporting, Holding,
Maintaining, Keeping, Staying, Waiting, Prolonging, Delaying, Occupying, Persisting, Including,
Containing, Continuing, Enclosing, Fastening, Connecting, Postponing, Dragging, Storing, Owning,
Restraining, Drawing, Attracting, and Remaining. Rather than induce any real change, the semantics of
these verbs is leaving the current state of the object as is, in its status quo, for some more time.

Each one of these processes can be considered as a change-preventing process—a process that works
against some “force” which would otherwise change the operand—the object being operated on. For
example, Supporting of a Laptop can be rephrased as Fall Preventing, Keeping of a Coin can be rephrased
as its Loss Preventing, and Holding of a Hostage can be rephrased as Escape Preventing of that Hostage.
Due to their nature as state-preserving, these “pseudo-processes” might rather be modeled using tagged
structural relations between two objects. We discuss this in the context of structural relations.
## 10.10.2 How to Model State-Preserving Processes with Tagged Structural
Links
Many of the state-preserving verbs can be considered as working against some “force,” which would
otherwise change some object. For example, a Pedestal supporting a Statue works against gravity, so we
can think of Supporting as a “fall preventing” process, without which the state of the Statue would
change from stabilized to fallen. The Supporting process starts as soon as the Statue is positioned and
keeps going until something in the system changes, e.g., the Pedestal undergoes a process of Breaking,
changing its state from intact to broken. As a more modern example, an Autopilot is a system that is
designed to maintain and stabilize an Aircraft in its course, working against lift, drag, gravity, and the
centrifugal force. Once the state-maintaining process ends, the state will change, so you need to capture
this process as a recurring one—whether through self-invocation, presented in Sect. 22.4.6 or controlled
response to an external trigger.
The static nature of state-preserving processes is contradictory to the definition of process, which
requires that it transforms some object. In such cases, it is often possible, and even desirable, to model the
relation between the two pertinent objects using a tagged structural link instead of a process. This
approach to modeling persistent processes is exemplified in Fig. 10.10, which shows Supporting as a
state-preserving process. On the left hand side is the dynamic version of the model, in which Supporting
is an explicit process, presented with its corresponding OPL paragraph. On the right is the static model
version, in which the tagged structural relation supports expresses the time-invariant relation between
Foundation and House, giving rise to a corresponding more compact and more expressive one-sentence
OPL paragraph: Foundation supports House.
## 10.10.3 Transient Objects and Their Invocation Link Substitute
Transient objects are the analogous counterparts of persistent processes. A transient object is a short-lived
physical or informatical object. Examples of transient objects are unstable materials, such as an interim
short-lived compound in a chemical reaction or an atom in an excited state that spontaneously decays to
the ground state by emission of X-rays and fluorescent radiation. Another example of a transient object is
a packet in a telecommunication network. Such a packet can reside for a short while at some router on its
way and leave no trace once the target node has received it.

Things: Objects and Processes
### Figure 10.10
Supporting as a state-preserving process
In an OPM model, a transient object that is created by a process and immediately consumed by the
next process can be skipped by using the invocation link, a lightning-shaped procedural link that directly
connects the two processes. Figure 10.11 demonstrates the notions of transient object and invocation link.
On the left hand side is a model in which Spark is an explicit object created by Igniting. The presence of
Spark is an event that initiates (triggers) Exploding, as denoted by the letter e next to the arrowhead
pointing to Exploding. Exploding immediately consumes Spark, so Spark is transient and short-lived. On
the right hand side is an alternative, more compact model, in which the transient Spark is suppressed by
the invocation link. The semantics of the invocation link is that the end of Igniting is the event that
triggers Exploding. The OPL paragraph in this case is also more compact.
### Figure 10.11
Spark as a transient object (left) and modeling without it using the invocation link (right)
Looking back at Fig. 10.10 and comparing it to Fig. 10.11, we can see the pattern: The use of the
invocation link as a shorter version of modeling generation and immediate consumption of a transient
object is analogous to the use of the tagged structural link as a shorter version of modeling a persistent
process. Another example is Signaling and the transient object Signal.

## 10.11 Operator, Operand, and Transform
Before concluding this chapter on the dynamics of systems, it may be interesting to compare the OPM
ontology to the definitions of Ashby (2001) regarding operand, operator and transform:
Consider the simple example in which, under the influence of sunshine, pale skin changes to dark
skin. Something, “the pale skin”, is acted on by a factor, “the sunshine”, and is changed to dark
skin. That which is acted on, the pale skin, will be called the OPERAND, the [causing] factor will
be called the OPERATOR, and that what the operand has changed to, will be called the
TRANSFORM.
### Figure 10.12
Tanning top level (left) and an in-zoomed view (right)
In the OPM ontology, Skin is an object, while dark and pale are states of an attribute of the object
Skin called Complexion. Skin is one of the parts of Person. Tanning is a process, and Sun is an instrument
that enables the Tanning process, the effect of which is to change the Complexion of the Skin from pale to
dark. This terminology and the OPM model in Fig. 10.12 seem more intuitive and appropriate for non-
mathematical systems than the operand, operator and transform ontology. The “sunshine factor” is a bit
problematic to describe. It is not clear whether it refers to the shining process of the sun or to the object
that aggregates the photons of energy radiated by the sun, which the skin absorbs.

Things: Objects and Processes
In OPM, we would model Radiating as a first subprocess of Tanning. Radiating requires (i.e., is
enabled by the instrument) Sun. Radiating, in turn, produces the object Solar Energy, which is absorbed
by the Skin via the second subprocess, Absorbing & Pigmenting, the one that changes the Complexion of
Skin from pale to dark. In summary, the operator is the process (Tanning). The operand is the affectee in
its state before the process occurred (Skin in its pale Complexion state), while the transform is its state
after the process occurred (Skin in its dark Complexion state).
## 10.12 Summary
A property is a metamodel attribute of an OPM element. A property value of each element in an
OPM model remains fixed.
The OPM approach considers processes as “first class citizens” alongside objects rather than
below object.
An object is a thing that exists or has the potential of physical or informatical existence.
Two instances of a physical object are identical if and only if they occupy the same space at the
same time.
From an informatical viewpoint, all the physical copies of some informatical object are the same.
Transformation is generation (construction, creation) or consumption (destruction, elimination)
or change (effect, state transition), of an object.
A process is a mental construct representing a pattern of object transformation.
In “cause and effect” analysis, cause is a triggering event that attempts to cause a process to start
executing.
The effect in “cause and effect” analysis is the transformation that one or more of the objects
linked to the executing process undergo.
Parts of speech (noun, verb, adjective, adverb …) are syntactic constructs, while OPM things
(object and process) are semantic constructs.
The preprocess object set of a process P, Pre(P), is the set of objects required to exist, possibly
in certain states, in order for P to start executing once it was triggered.
The postprocess object set of process P, Post(P), is the set of one or more objects that exist,
possibly in certain states, after P finished executing.
The involved object set of process P, Inv(P), is the union of P’s preprocess object set and
postprocess object set: Inv(P) = Pre(P) ∪ Post(P).
The object-process distinction problem is the problem of telling whether a given a noun is an
object or a process.
The process test is a formal procedure for solving the object-process distinction problem.
The process test assumes that by default, a noun is an object, so to be a process it must meet
three criteria: (1) object transformation, (2) time association, and (3) verb association.

o The object transformation criterion is satisfied if the noun in question transforms at least one of
the objects in the involved object set.
o The time association criterion is satisfied if the noun in question can be thought of as happening
through time.
o The verb association criterion is satisfied if the noun in question can be derived from, or has a
common root with a verb or has a synonym which is a verb.
The capitalization OPM convention is that the first letter in each word of the name of a thing is
capitalized, while states are lower-case.
The singular name OPM principle specifies that a name of an OPM thing must be singular.
The OPM process naming convention is to name a process by making its last word a gerund
whenever this is possible and is acceptable and makes sense in the domain nomenclature.
Thing is a generalization of object and process.
A state-preserving process is a process that maintains a steady state of status quo, and can be
suppressed by replacing it with a tagged structural relation.
A transient object is a short-lived object, and can be suppressed by replacing it with an
invocation link.
## 10.13 Problems
1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 11. 12. Give an example of a scientific discovery and explain how it can be thought of as reverse
engineering of nature.
Why is it impossible to touch a process even if it is physical?
Why is a process in an OPD that has no transforming link attached to it meaningless?
Who are the “players” in cause and effect analysis? What is the role of each one of them?
Give an example of two sentences that express the same fact but have different parts of speech.
What are the objects and processes in the first sentence above? And in the second?
Construct an OPM model of the system described in the previous question.
In the OPM model of the process test system in Fig. 10.6, what are the members in the
preprocess object set, in the postprocess object set, and in the involved object set?
Select two things from the OPD in Fig. 10.3 and apply the process test on each one of them.
What is the preferred way of modeling persistent processes?
What is a possible shortcut for modeling transient objects?
Model the following specification: Running of an internal combustion engine is contingent upon
the presence of the objects air and gasoline vapor mixture inside the object cylinder at the right
pressure and temperature (attributes of mixture). The triggering event is the point in time when a
spark (created by a previous timed process) ignites the mixture. As a result of this process, the
gasoline mixture is consumed and the piston’s kinetic energy value increases.
