# Chapter 17 Aggregation-Participation
The whole is more than the sum of its parts.
Aristotle, Metaphysica
This large four-wheel chariot … consists of a number of parts
joined together by leather straps and wooden nails. … Each of
the four large wheels has 34 spokes …
Description of a wood and leather
Chariot, Eastern Altai, Russia (The
State Hermitage Museum, 2001)
This chapter discusses the first fundamental structural relation, possibly the most important one:
aggregation-participation—the relationship between the whole and its parts. Any interesting system can
be described as a whole decomposed into parts. The system as a whole and any one of its parts can then
be described separately using natural language adjectives to assign attribute values to objects and adverbs
to assign attribute values to processes. Without the ability to mentally take things apart and examine their
features, our ability to study systems would be greatly hindered. Aggregation-participation is also known
as whole-part (Coad and Yourdon 1991), composition (Kilov and Simmonds 1996), or the part-of
relationship (Fowler 1996).
## 17.1 Underlying Concepts
Aggregation-participation is a fundamental structural relation which denotes the fact that a refineable—a
relatively high-level, ancestor, parent thing (object or process) aggregates (i.e., consists of, composed of,
contains, or comprises) one or more refinees—lower-level, descendant, child things. The higher-level
thing is called the whole, or aggregate, while the lower-level things that comprise it are the parts. This
relationship is very central in conceptual modeling, and at least at a superficial level, is relatively easy to
comprehend. Aggregation-participation is a means to describe the composition of every non-trivial thing
by enumerating its parts in the whole-part hierarchy.
## 17.1.1 Gestalt Theory
Relating to the famous saying attributed to Aristotle quoted above that “The whole is more than the sum
of its parts”, Koffka (1935, p. 176) rephrased this observation as follows: “the whole is something else
than the sum of its parts”, arguing that the operation of summing up is often meaningless, but what is
always meaningful in a whole is its relationships with its parts.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 17

## 222 Aggregation-Participation
In 1924, Wertheimer and Reizler (1944) introduced the gestalt theory, which basically claims that
“what is happening in the whole cannot be deduced from the characteristics of the separate pieces” and
that what happens to parts of the whole is determined by laws relating to the structure of that whole. A
configuration or pattern of elements in any domain is unified as a whole so much that its properties
cannot be derived from a simple summation of its parts. In psychology, Rescher and Oppenheim (1995)
have provided a conceptual framework for the precise explication of the gestalt concept of “whole” and
summarized the intuitive requirements or conditions of talking about a whole and its parts:
The whole must possess some attribute in virtue of its status as a whole, an attribute peculiar to it
and characteristic of it as a whole. The parts of the whole must stand in some special and
characteristic relation of dependence with one another; they must satisfy some special condition in
virtue of their status as parts of a whole.
## 17.1.2 Holism and Emergence
To specify the concept of part, it is necessary at the very outset to state the conditions under which some
object is to be considered part of another whole thing. The specification of a particular part-whole relation
thus determines for a given thing, the whole, which things are its parts. (Latimer and Stevens 1997). From
a system’s viewpoint, the “special condition” that things must fulfil as parts of a whole is holism. Holism,
in turn, is the condition for emergence—the emerging function of a system that stems from the particular
whole-part relations and the way the parts are aggregated, which none of the parts alone exhibits.
We tend to think of aggregation as a relation between a whole object and its object parts. Indeed, this
is the usual context. However, unlike most trains of though, which attribute holism to object parts and the
whole to the aggregate object, in OPM the same relation is used with analogous semantics for processes
as it is for objects: A process can consist of parts, which are the subprocesses of that whole process, and
the outcome of the aggregate process is not a mere sum of the outcomes of its subprocess parts, but a
process with an emergent transformation of an object, which none of its subprocesses alone, nor their
simple “arithmetic” sum could have delivered.
Thus, an OPM object may consist of other, lower-level objects (and exhibit, but not consist of,
processes, which are its operations, as we discuss in Chap. 18). Analogously, an OPM process may
consist of other, lower-level processes (and exhibit, but not consist of, objects, which are its attributes, as
we discuss in Chap. 18). We elaborate on this idea while discussing refinement in Chap. 21.
## 17.1.3 Decomposition Depth
A question that arises frequently during modeling is: How far should the decomposition go? How deep
down should it continue? Naturally, most things can be decomposed further than the deepest
decomposition specified in a model of the system. In particular, physical objects can be decomposed all
the way down to the molecular and atomic or even sub-atomic levels. However, the specification of yet
deeper participation hierarchy levels always should stop at a point that is deemed sufficient by the system
modeler, architect, engineer, or analyst for the purpose of specifying the system under development or
study. That level of detail shall be sufficient to explain the function, structure, and behavior of the system
under study (as is typical in science) or prescribe how to go about its detailed design (typically in
engineering).

## 17.1.4 Why Use “consists of” and not “has a”?
Some early object-oriented (OO) methods referred to the aggregation-participation relation as the “has-a”
relation (as opposed to the “is-a” relation for the generalization-specialization relation, which is the
subject of Chap. 20). It may indeed seem natural to use some form of the verb “to have” to denote the
relation between the whole and its parts, as in “A car has a body, an engine, and four wheels.” However,
we avoid the use of this verb to denote aggregation because it is overloaded and may have1 various
interpretations. To see this, suffice it to look at the sentence examples “Dave has a step mother.”, “Jack
has a yellow motorcycle.”, “We are having a discussion.” “I am having hard time understanding.” “The
patient has cold.” and “The object has an attribute.” OPM’s choice of the reserved phrase consists of for
denoting the aggregation-participation relation is explained below.
## 17.2 Aggregation-Participation as a Fork
Like all structural relations, aggregation-participation is a pair of forward and backward structural
relations. Aggregation is the forward structural relation—the relation as seen from the aspect of the
aggregate, the whole, or the ancestor, when it refers to its parts—the descendants. The backward
structural relation, i.e., the relation as seen from the aspect of each part, is participation.
Aggregation and participation are inverse relations: Aggregating can be thought of as the process of
creating a whole from its parts, while participating is being one of the parts that comprise the aggregate.
However, as we have noted in the discussion on structural relations in Sect. 14.3, aggregating is a state-
preserving process. Its semantics is of parts being held together to create the whole, with time having little
or no relevance to this relation.
The forward (or hierarchically downward) direction of the aggregation-participation relation, from the
whole to its parts, is the aggregation direction. The reserved phrase used to express the forward direction
of the relation is “consists of.” The backward, (or upward, or reverse) direction, from each part to the
whole, is the participation direction. The phrase used to express the backward direction of the relation is
“is part of”, but this is not an OPL reserved phrase.
The two OPDs in Fig. 17.1 exemplify how the aggregation-participation relation replaces the tagged
structural relation. In the OPD on the left, the relations between Lamp and its three parts are expressed
using three bidirectional tagged structural link, as we have been using so far. All three forward tags are
“consists of”, with the source object Lamp being the whole and the destination objects—Base, Light
Bulb, and Electric Chord—the parts. The tag in the backward direction for each one of these three links is
“is part of”. Thus we get six OPL sentences—one forward and one backward for each of the three links.
The phrase “consists of” in the OPL paragraph on the left hand side of Fig. 17.1 is bolded since it is
not reserved—it comes from a user-defined tag, put on a bidirectional tagged structural link, rather than
from a dedicated aggregation symbol. The opposite is true for the reserved phrase “consists of” in OPL
1Already in this sentence, as well as in this footnote, we have a built-in example that shows the multiple uses of
“have.”
## 224 Aggregation-Participation
paragraph on the right hand side of Fig. 17.1, in which one OPL sentence, “Lamp consists of Light Bulb,
Base, and Electric Cord.” replaces six OPL sentence on the left.
Lamp
Lamp
is part of
consists of
is part of
consists of
consists of
is part of
is screwed to is screwed to
passes through passes through
Electric
Light Bulb Light Bulb
Base
Base
Chord
in contact in contact
Electric
Chord
Lamp consists of Light Bulb.
Light Bulb is part of Lamp.
Lamp consists of Base.
Lamp consists of Light Bulb, Base, and Electric Cord.
Base is part of Lamp.
Light Bulb is screwed to Base.
Lamp consists of Electric Cord.
Electric Cord passes through Base.
Electric Cord is part of Lamp.
Light Bulb and Electric Cord are in contact.
Light Bulb is screwed to Base.
Electric Cord passes through Base.
Light Bulb and Electric Cord are in contact.
### Figure 17.1
Aggregation expressed by three tagged structural links (left) and the aggregation-participation symbol (right)
The solid black triangle —the aggregation-participation relation symbol—replaces the pair of
forward and backward textual tags of the bidirectional structural link that express textually the
aggregation-participation relation. Like the rest of the fundamental structural relation symbols, the
aggregation-participation relation symbol is a helpful shorthand graphic notation convention for this
important and widely used structural relation. The symbol helps identify the relation easily in the OPD,
saving graphic clutter and excessive text typing and reading.
Being a structural relation, the aggregation-participation relation abides by the distributive law, two or
more structural links can be represented as a fork. In the OPD at the right of Fig. 17.1, the relations
between Lamp and its three parts are expressed using the specific symbol designated for the aggregation-
participation relation, a solid black equilateral triangle, , whose base is horizontal. The whole is linked
to the top of the triangle and the parts—to its base. This enables replacing the first six OPL sentences on
the left with a single one—the first on the right. Unlike the tag “consists of” in Fig. 17.1, which, being
user-defined, is bold, the phrase “consists of” in Fig. 17.1 is a reserved OPL phrase and therefore it is not
bold.
## 17.3 A Semantic Web Example
RDF, the Resource Description Framework (W3C Consortium 2014), integrates a variety of applications
from library catalogs and world-wide directories to syndication and aggregation of news, software, and
content to personal collections of music, photos, and events using XML as interchange syntax. The RDF
specifications provide a lightweight ontology system to support the exchange of knowledge on the Web.

An example of the use of the aggregation-participation fundamental structural relation can be found in the
following excerpt taken from Sect. 2.2 of the RDF Primer (Manola and Miller 2004):
“…each statement consists of a subject, a predicate, and an object.”
The use of the phrase “consists of” is a clear indication of the existence of a whole-part, or
aggregation-participation relation between the whole and its part. Indeed, as we have seen, OPM uses this
as a reserved phrase to denote this relation. The OPD that is equivalent to this OPL sentence (and should
be generated from it by any OPM-supporting tool such as OPCAT) is depicted in Fig. 17.2. Indeed, this
OPL sentence is almost identical to the original one above.
### Figure 17.2
OPD of the sentence “RDF Statement consists of Subject, Predicate, and Object”
The black triangle, which denotes the aggregation-participation fundamental structural relation, has its
tip is linked to the aggregate (the whole, which is the object RDF Statement), while its (always horizontal)
base is linked to its three parts: Subject, Predicate, and Object. This is a fork, in which RDF Statement is
the handle object, and the set {Subject, Predicate, Object} is the tine object set. If forks did not exist, the
OPD would have required three separate aggregation links, each with its own black triangle symbol. As
we will soon see in Fig. 17.4, since UML and SysML do not have the notion of fork, we would indeed
need three separate aggregation (diamond symbols) to express the same three model facts.
## 17.3.1 Different Phrases, Same Semantics
In the case of the RDF Statement analyzed above, we were lucky to find out that the phrase in the natural
language sentence “…each statement consists of a subject, a predicate, and an object,” contained the
reserved OPL phrase consists of. This made it easy to deduce that a whole-part relationship exists
between an object RDF Statement and a set of other objects. There are, however, many other syntactical
expressions with the same whole-part semantics. These include “has parts,” “comprised of,” “is made of,”
and “comprises.” Other expressions, such as “is divided into,” “make up,” or “contains,” may, under some
interpretation, also be considered as having the same whole-part relation semantics, while in a different
context they may convey a somewhat different meaning. Consider, for example, the following definition
of an RDF triple, found in Sect. 3.1 of the W3C Proposed Recommendation Resource Description
Framework (RDF): Concepts and Abstract Syntax (Klyne et al. 2004):
“Each triple has three parts: a subject, an object, and a predicate (also called a property) that
denotes a relationship.”
In Sect. 6.1 of the same document, we find that:
## 226 Aggregation-Participation
“An RDF triple contains three components: the subject, which is an RDF URI reference or a
blank node, the predicate, which is an RDF URI reference, and the object, which is an RDF URI
reference, a literal or a blank node.”
Comparing these two excerpts from the same document, we must deduce that “has three parts” has
the exact same meaning as “contains three components,” as both relate to the composition or structure of
an RDF triple. Moreover, if we accept that the semantics of the verbs “contains” and “has parts” in this
context is the same as “consists of,” then we can summarize the two citations above in the following OPL
sentence:
RDF Triple consists of Subject, Predicate, and Object.
The problem of multiple words, idioms, or phrases that have the same or almost the same semantics,
which is demonstrated here, is a major issue in natural language processing (NLP) and understanding.
Using their natural human intelligence, human beings normally have no problem assigning the same
semantics to such different syntactic entities, and grasp subtle differences when they exist and are
relevant. The example above shows that even in highly formal documents, such as one defining the
semantic Web, in which semantics is the issue of discourse, free use is made of equivalent idioms and
phrases, justifiably counting on the human intelligence to resolve it.
Indeed, people interpret meaningful sentences effortlessly all the time without even paying attention to
the fact that other words and a totally different syntax was used to express the same semantics. When
NLP techniques are considered, this issue becomes of prime importance, and has to be dealt with
meticulously. OPL solves this problem by being a subset of English that is defined formally via a context-
free grammar. Future developments in automated sematic sentence understanding can be key to model
evolution of ground-truth, humanly validated kernel OPM models, such as the one developed by Somekh
et al. (2014) for the mRNA lifecycle.
## 17.4 Aggregate Naming
Frequently during the analysis, we encounter situations in which we need to name an aggregate, which
has no single word in natural language. To illustrate the point of aggregate naming and the importance of
appropriate phrase generation, consider a transportation, civil, and systems engineering development
team, whose assignment is to improve the traffic in a city. After some thought and discussion, the team
agrees that an essential object in the system is the composition of a car and the person that drives it in the
city streets. This object is much more central to the system than a car alone or a driver alone.
The role a car without a driver plays is restricted to parking issues, while the driver without the car
should be considered a pedestrian. Nonetheless, having agreed that the car along with its driver is a major
object that needs to be accounted for in the system, our team still lacks an elegant way of referring to it.
Since there is no single word in English (and most likely in any other natural language) for this object, the
team has come up with the name Car-Driver Complex, as illustrated in Fig. 17.3. As we will see, these
situations are not unique to aggregates; they are also encountered in a variety of other circumstances, such

as naming an attribute when only the names of its values are explicit.2 In cases like these, we must
exercise our creativity to generate an appropriate phrase that best captures the essence of what we wish to
express.
The capability of inventing meaningful names, or generating expressive phrases, is a very important
component of the analysis process. It provides us with the power to abstract into a whole a collection of
things that would otherwise be very difficult to think about and relate to as a unity. Recall that indeed the
first OPM principle—the Function-as-a-Seed OPM Principle—calls for starting the process of modeling a
system by defining, naming, and depicting the function of the system. The name of the function shall
express what the system is designed to do, and what value its beneficiaries will gain from using it.
### Figure 17.3
Naming an aggregate which has no single word in natural language
## 17.5 Composite and Shared Aggregation in UML and SysML
SysML adopted from UML 2 all the definitions related to class diagram (and several other diagram kinds)
“as is.” SysML block diagram inherits the same semantics as UML 2 class diagram. Hence, in UML 2
and SysML class diagrams there are two types of aggregation: composite aggregation and shared
aggregation (Object Management Group 2010, p. 39).
Composite aggregation, depicted as a black diamond next to the whole end of the link, (see Fig.
17.4) “indicates that the composite object has responsibility for the existence and storage of the
composed objects (parts).” Composite aggregation, also referred to as strong aggregation, or the
composition relationship, or standard composite aggregation, or non-shared association, is
considered a “strong” form of containment or aggregation: A part can belong to just one aggregate,
and if the aggregate is consumed, all its parts are consumed along with it. Originally defined for
UML, responsibility and storage in the composite aggregation definition are software-related
concepts. SysML, which is supposed to accommodate systems of any kind, not just software, has
inherited this definition, as is the case with many other definitions.
2For example, what is the name of the attribute the values of which are wide and narrow? Width? Narrowness?
Something in-between? Such a neutral word does not exist. Section 18.7 contains a detailed discussion on this topic.
## 228 Aggregation-Participation
Shared aggregation, also called simply aggregation, denoted as a white (blank) diamond next to
the whole end of the link, is a loose, “weak” type of whole-part relationship. Unlike composite
aggregation, in shared aggregation, the part has “life of its own,” and it can be part of more than one
whole. According to Object Management Group (2010, p. 39), “precise semantics of shared
aggregation varies by application area and modeler.” While usually, in shared aggregation each
part can exist independently of the whole, leaving the semantics of a relation vague is not a good
idea to begin with. The tagged structural relation in OPM is user-defined, and this would be a better
way to express specific semantics by application area or modeler, rather than leaving the semantics
of a language symbol open to a variety of interpretations by various modelers even in the same
domain and even if all of them relate to the same system model.
The connecting lines of the aggregation relation in UML need not be orthonormal and are usually
diagonally straight, as Fig. 17.4 demonstrates. UML and SysML do not have the fork construct, so as Fig.
## 17.4 shows, each part in a UML (and SysML) class diagram needs to be connected with a dedicated
aggregation symbol.
Composition is stronger than aggregation in that the whole is “responsible” for its parts, so when the
whole is consumed so are all the objects of which it is composed. Hence, the part cannot be owned by
more than one whole. Here is what the UML 2.0 Superstructure document v 2.2 (2005) says about
composite aggregation (p. 41):
“An association may represent a composite aggregation (i.e., a whole/part relationship). …
Composite aggregation is a strong form of aggregation that requires a part instance [to] be
included in at most one composite at a time. If a composite is deleted, all of its parts are normally
deleted with it. Note that a part can (where allowed) be removed from a composite before the
composite is deleted, and thus not be deleted as part of the composite.”
Window

+scrollbar

+title +body 1

Slider
Header Panel
### Figure 17.4
The symbol of composite aggregation in UML and SysML
In OPM the distinction between composite and shared aggregation is not necessary, since one can
model exactly what part or parts are consumed when the whole is consumed and what parts remain, as the
OPM model in Fig. 17.5 demonstrates: After Crashing, the whole Car and its Chassis are gone, but the
Powertrain remains (and can be reused).

### Figure 17.5
OPM model demonstrating how UML/SysML shared and composite aggregation can be modeled in tandem
## 17.6 Expressing Parts Order
Sometimes, the order of the parts that comprise the whole is significant. Sets are abstract collections of
things that consist of elements or members. A set may therefore be thought of as an aggregate (whole) and
its elements—as parts. Each element in the set is unique. Since aggregation-participation is a structural
relation, everything that applies to a fork is true for aggregation-participation, including the way
orderability is indicated. Being a fork, the Aggregation-Participation relation exhibits the Boolean
Orderability property, which denotes whether or not the set of parts is ordered. The two values of
Orderability are ordered and unordered, with the default value being unordered. Let us again consider the
RDF triple case (Klyne et al. 2004):
An RDF triple is conventionally written in the order subject, predicate, object.
### Figure 17.6
The OPD label “ordered” and the OPL reserved phrase “in that sequence” indicate the order of the parts of
RDF Triple from left to right (in the OPD on the left) or top-down (in the OPD on the right)
We model graphically the fact that the three elements of an RDF triple are ordered by adding the label
ordered next to the black triangle symbolizing the aggregation-participation relation, as shown in the OPD
in Fig. 17.6. The parts can be ordered with no sematic difference either from left to right, as the OPD on
## 230 Aggregation-Participation
the left shows, or top-down, as the OPD on the right shows. The corresponding OPL phrase is “in that
sequence”, which follows a comma after the name of the last part in the ordered list.
The OPD in Fig. 17.7 is an example of an aggregation hierarchy, which specifies the reading order of
a scientific paper, i.e., the order in which the parts of the paper should be read, with participation
constraints, which are discussed in Chap. 15.
When dealing with processes, orderability is intimately related to the top-to-bottom timeline within an
in-zoomed process, which dictates the process execution order. We elaborate on this in Chap. 21 while
discussing complexity management.
## 17.7 Aggregation and Tagged Structural Relations
In the next example, we illustrate an OPM model that combines aggregation-participation with tagged
structural relations. Consider the sentence extracted from the RDF Primer (Manola and Miller 2003):
RDF models statements as nodes and arcs in a graph.
### Figure 17.7
The ordered aggregation hierarchy of a scientific paper with participation constraints
In order to model this sentence in OPM, using our prior knowledge about graphs and assuming that a
graph has at least two nodes and one arc (which is the case with RDF graphs), we break the sentence
above into the following three simpler, more explicit sentences:

1. A graph consists of at least two nodes and one arc.
2. RDF graph is a graph.
3. An RDF graph models at least one RDF statement.
Sentence (1) above is modeled in Fig. 17.8. As in the previous example, the black triangle denotes
aggregation, where the object Graph is the whole, while Node and Arc are the parts. The plus (+) symbol
above Arc denotes the “at least one” (+) participation constraint, while the “2..*” symbol above Node
denotes the participation constraint “2 to many”.
The fact that has been added in the second OPL sentence is that an RDF Graph is a (specialization of)
Graph. As such, it inherits the structure of Graph. To express the fact that an RDF Graph models at least
one RDF Statement, a unidirectional tagged structural relation is used, and the tag reads “models”.
We ended up with two similar OPL sentences, obtained from two W3C proposed recommendations:
“RDF Statement consists of Subject, Predicate, and Object.” (Manola and Miller 2003), and
“RDF Triple consists of Subject, Predicate, and Object.” (Klyne et al. 2004)
### Figure 17.8
The OPM model of a graph consisting of at least one node and optional arcs
Under the assumption that if two things consist of exactly the same set of parts, or components, they
are equivalent (if not the same), one can deduce that RDF Triple and RDF Statement are equivalent. This
statement is expressed in the OPM model depicted in Fig. 17.9 by the (vertical) null tag bidirectional
structural link between these two objects, which combines model facts from Figs. 17.6 and 17.8. This
OPD also expresses that Subject and Object in an RDF Graph are Nodes in a general Graph, and that
Predicate in an RDF Graph is an Arc in a Graph.
Another example for the use of the null tag bidirectional structural relation is when we model the
sentence from Sect. 6.1 of (Klyne et al. 2004)
The predicate is also known as the property of the triple.
This is expressed in the OPD of Fig. 17.9, where Property is linked to Predicate with a null tag
bidirectional structural link to indicate that they are equivalent, assuming that the null tag default is
“equivalent”. This translates to the OPL sentence “RDF Triple and RDF Statement are equivalent.”
## 232 Aggregation-Participation
### Figure 17.9
An OPM model demonstrating a bidirectional tagged structural link with one tag
## 17.8 Non-Comprehensive Aggregation
Being a specialization of fork, aggregation inherits the Boolean Comprehensiveness property just as it
inherits the Boolean Orderability property. The default aggregation Comprehensiveness value is
comprehensive: we assume that if nothing is indicated, then all the parts are specified in the model. If we
wish to denote that the aggregation is non-comprehensive, we add the non-comprehensiveness symbol—
a short horizontal bar below the aggregation black triangle symbol, as shown in Figs. 17.10 and 17.11.
The corresponding OPL phrase is “and at least one other part”, used in the last OPL sentence in Fig. 17.10.
If an aggregation symbol is both ordered and non-comprehensive, the OPL phrase for non-
comprehensiveness precedes that for the orderability. For example, if in Fig. 17.10 the aggregation
symbol attached to Body, which is non-comprehensive, would also be ordered, the resulting OPL
sentence would be:
Body consists of at least one Section, optional Figures, and at least one other part, in that sequence.
## 17.8.1 Partial Aggregation Consumption
When we wish to specify that the whole and a specific subset of its part are consumed, we can model this
succinctly using partial aggregation consumption, as exemplified in Fig. 17.12. In the OPM model on the
left of Fig. 17.12, the Consuming process consumes Whole along with its Part B and Part D, while Part A
and Part C remain intact as separate objects. This is similar to the car crashing example in Fig. 17.5. In the
OPM model on the right of Fig. 17.12, the terse version using partial aggregation shows that the
Consuming process consumes Whole and only Part B and Part D, while all the other parts of Whole,
which are not shown in the partial aggregation, remain as distinct, unchanged objects.

### Figure 17.10
The non-comprehensive aggregation symbol is a short vertical line below the aggregation triangle expressing
that not all the parts are shown
### Figure 17.11
Application of non-comprehensive aggregation in the Resource Description Framework Statement
### Figure 17.12
Partial aggregation consumption exemplified
## 234 Aggregation-Participation
### Figure 17.13
The non-comprehensivemness symbol demonstrated for aggregation and characterization. Left: Original
Process Test model. Right: Updated model after removing Verb Association Criterion
Being a fork property, the non-comprehensiveness symbol can be used not only for aggregation, but
also for each of the other three fundamental structural relations—exhibition, specialization, and
classification. To correctly use the non-comprehensive symbol, an OPM modeling tool must keep track of
the set of refinees for each refineable and adjust the symbol and corresponding OPL sentences as the
modeler changes the collection of refinees. This is demonstrated in Fig. 17.13, where we reuse the OPM
Model of the Process Test from Fig. 10.6, this time providing only the two relevant OPL sentence. On the
left is the original model, while on the right the object Verb Association Criterion, which is both a part of
Process Test and an attribute of Noun, has been removed, causing an automatic update of the OPD to
include the non-comprehensive symbol for both the aggregation and the exhibition. The OPL sentences
were updated as well.
As we can see, the OPL phrase for non-comprehensive exhibition-characterization is “and at least one
other feature”. We use feature rather than attribute because, as we discussed in Chap. 16 and will elaborate
in Chap. 18, feature can be an attribute (object) or an operation (process), both of which can be attached
to the base of the same exhibition symbol, . Similarly, the OPL phrase for non-comprehensive
generalization-specialization is “and at least one other specialization”, and the OPL phrase for non-
comprehensive classification-instantiation is “and at least one other instance”.

## 17.9 Language
The Parameterized Participation Constraints Mini-
The use of participation constraints in the aggregation-participation relation is similar to their use in a
general tagged structural relation. A different participation constraint can be attached to each one of the
parts in the tine set of the whole. As with the general tagged structural relation, the implicit default for the
number of parts of a whole is 1. A participation constraint other than 1 is recorded outside the part next to
the point connecting the part with the orthonormal line from the solid triangle’s base.
### Figure 17.14
Parameterized participation constraints applied to aggregation-participation links
The OPD in Fig. 17.14 and the OPL that follows it exemplify this. Since an Airplane consists of two
Wings, the participation constraint 2 is recorded next to the object Wing. Airplane also consists of a
certain number of Engines, the exact number of which is determined by a couple of parameters. The
example in Fig. 17.14 uses three parameters, E, B, and W, to express the number of Engines in an
Airplane, the number of Engines attached to the Body, and the number of Engines attached to a Wing,
respectively.
As exemplified in Fig. 17.14, there is a specific syntax of parameterized participation constraints as
they are recorded in an OPD. This syntax defines a small-syntax language, called Parameterized
Participation Constraints (PPC) mini-language. It draws from, and is similar to, the syntax of arithmetics
and set notation in conventional third-generation and OO programming languages, such as C, C++ and
Java. This syntax, specified informally next using this example, must not be confused with the much more
complex syntax of OPL, which is presented formally in EBNF in the OPM ISO 19450 PAS (see Chap.
24). The PPC mini-language must also not be confused with UML’s OCL, which is also designed as an
add-on to UML to specify constraints that cannot be expressed graphically in UML, as Sect. 22.10
discusses briefly.
To demonstrate the PPC mini-language syntax, let us follow the example in Fig. 17.14. The set of four
constraints, each expressed in a line of text in Fig. 17.14 above the object Engine are the E parameter
constraint set—the set of four constraints for E, where E is the parameter for the number of Engines in
the Airplane. The parameter (E in our case) appears first, followed by semicolon, followed by zero or
## 236 Aggregation-Participation
more (four in our case) constraints separated by semicolons. Each constraint is an equality or inequality,
or a set membership notation. The left hand side is the parameter name, the right hand side is a
mathematical expression, and the two sides are separated by one of the equality or inequality symbols =,
≠ (or != when only the ASCII character set is available), <, >, ≤ (or <=), ≥ (or >=), or by the membership
notations ∈ (or “in”), or ∉ (or “not in”).
As noted, the symbols and syntax used in the constraint expressions are based on common
conventions of programming languages. For example, multiplication is denoted by an asterisk, as in E =
B+2*W. The reserved phrase in is the set-theoretic symbol ϵ, so “b in {0, 1}” is the same as “b ϵ {0, 1}”. In
our example, the first constraint, E >= 1, constrains the number of Engines in the Airplane to be at least
one. The second constraint, E = B+2*W, is the total number of Engines, which is equal to the number of
Engines in the Body (which can be 0 or 1), and W is the number of Engines in each Wing (which can be 0,
1, 2, or 3).
### Figure 17.15
The parameterized participation constraints from Fig. 17.14 expressed differently
As this example shows, the OPL syntax for the parameterized constraints set is such that the main
parameter precedes the name of the object to which it relates, followed by a comma and the reserved
phrase where, followed by a comma-separated list of constraints with the reserved phrase and preceding
the last constraint.
Figure 17.15 presents another way to specify the parameterized participation constraints, which is
different than that in Fig. 17.14, but it uses the same parameterized constraint syntax and has the same
semantics. The PPC mini-language is compared in Sect. 22.10 with Object Constraints Language (OCL)
that augments UML.
## 17.10 Summary
Aggregation-participation is a fundamental structural relation which denotes the fact that a
refineable—the whole—aggregates one or more refineables—the parts.
Aggregation-participation is a pair of forward and backward structural relations.

The solid black triangle, , is the aggregation-participation relation symbol. It replaces the pair
of forward and backward textual tags of the aggregation-participation relation.
Aggregating is the process of creating a whole from its parts, while participating is enumerating
the parts that comprise the aggregate.
In UML 2 and SysML, there are two types of aggregation in class diagrams: shared—weak
aggregation, marked as a white diamond, and composite—strong aggregation, marked as a black
diamond.
In OPM the distinction between composite and shared aggregation is not necessary, since one
can model exactly what part or parts are consumed when the whole is consumed and what parts
remain.
Orderability is a Boolean property of the aggregation relation, inherited from fork.
To denote that the aggregation is ordered, we add the symbol next to the aggregation
triangle.
Comprehensiveness is another Boolean property of the aggregation relation, inherited from fork.
To denote that the aggregation is non-comprehensive, we add a short horizontal bar below the
aggregation triangle.
The Parameterized Participation Constraints (PPC) mini-language has a small syntax that
determines how to phrase a set of constraints for a parameter in a participation constraint.
ordered 17.11 Problems
1. 2. 3. 4. 5. 6. 7. 8. Draw two OPDs of a two-story house and its major parts, one without and one with the
aggregation participation link.
Which OPD was easier to draw? Why?
Use the second OPD from the first problem to demonstrate the use of orderability in terms of
vertical location of the parts of the house, the highest one being the first. Add parts as needed.
Demonstrate non-comprehensiveness by removing one or more parts from the OPD in the
previous question.
Add at least two participation constraints to an OPD from one of the previous question.
Draw OPDs describing two objects for which the parts are ordered and two for which they are
not.
Draw two OPDs for an object consisting of at least eight different parts at the first participation
level, with non-comprehensive aggregation. A subset of the parts should appear in one OPD and
another subset in the other OPD such that the union of the subsets is comprehensive.
According to Figs. 17.13 and 17.14 what are the possible numbers of engines in an Airplane?
## 238 Aggregation-Participation
9. Use parameterized participation constraints to create the aggregation hierarchy of a high rise
building. The building has a certain number of floors, each having two types of apartments,
standard and luxury. In each floor from floor 4 and above there are three standard and two
luxury apartments. In the first three floors, there is one small and two large offices. Decide how
many floors there are and how many faucets are required for each unit, and create the
appropriate OPD with participation constraints. Complete details as you see fit. Using your
OPD, compute the number of faucets the contractor needs to order for a 22 story building.
