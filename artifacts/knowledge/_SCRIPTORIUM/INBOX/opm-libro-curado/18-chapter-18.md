# Chapter 18 Exhibition-Characterization
I must be able to attribute properties to the objects.
Kant (1787)
To define and describe things in the world, natural languages use adjectives and adverbs. Without these
types of words, which describe objects and are also interchangeably called attributes, features, qualities,
characteristics, or properties, neither objects nor processes can be adequately distinguished and
understood. Exhibition-characterization is the fundamental structural relation that binds a refineable
(object or process)—the exhibitor, with a refinee—another object or process, called feature, which
characterizes the exhibitor.
## 18.1 Feature and Exhibitor
Exhibition-characterization is a fundamental structural relation. Like any binary structural relation, it
involves two things: the exhibitor and the feature.
Feature is a refinee that characterizes (describes) a thing.
Exhibitor is a refineable that exhibits (is characterized by) a feature.
Exhibition-Characterization is a fundamental structural relation which denotes the
fact that a feature characterizes an exhibitor (and conversely, the exhibitor exhibits
the feature).
To be consistent with the naming convention of the fundamental structural relations, the first word in
the exhibition-characterization relation pair describes the forward direction of the relation, from the
exhibitor to the feature, while the inverse direction goes from the exhibitor to the feature.
The relationship between feature and exhibitor in the exhibition-characterization relation is analogous
to that between a part and a whole in the aggregation-participation relation: Part is a refinee that
comprises a refineable—the whole, which aggregates the parts. Like aggregation-participation,
exhibition-characterization is transitive, giving rise to an exhibition hierarchy. The forward direction,
then, is also the downward direction: from a thing higher in the hierarchy—the exhibitor—to one or more
things lower in the hierarchy—the features.

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 18

Exhibition-Characterization
The forward (downward) direction of the exhibition-characterization relation, from the exhibitor to its
features, is the exhibition direction, while the reverse (upward) direction, from each feature to the
exhibitor, is the characterization direction. The above definition assumes the forward direction of the
exhibition-characterization relation. Viewed in the backward direction, the feature is said to characterize
the exhibitor. Figure 18.1 expresses on the left the exhibition-characterization relation as a bidirectional
tagged structural link, yielding two OPL sentences, while on the right, the relation’s designated symbol is
used, resulting in a single OPL sentence with the (non-bold) reserved OPL word exhibits.
### Figure 18.1
The exhibition-characterization relation expressed as a bidirectional tagged structural link (left) and with the
relation’s designated symbol (right)
The word for the backward relation, characterization, is much more commonly used in the context of
the relation than its forward counterpart, exhibition. Characterization is therefore the short name of the
relation. Based on this, we may occasionally drop the “exhibition” part of the name of this fundamental
structural relation and abbreviate it to characterization, bearing in mind that this is the direction up the
hierarchy level.1
## 18.1.1 Primary and Secondary Qualities
Many philosophers who discussed epistemology and metaphysics, including Galileo, Descartes, and
Locke, have made the conceptual distinction between primary and secondary qualities (or properties, or
attributes). Primary qualities are “independent” properties of objects, such as shape or mass, which
convey facts about the thing and do not rely on subjective judgments. Secondary qualities are properties
such as color, taste, smell, and sound, which depend on and produce sensations in observers and do not
provide objective facts about things.
As Galileo (1623) wrote in The Assayer, “… tastes, odors, colors, and so on are no more than mere
names so far as the object in which we locate them are concerned, and that they reside in consciousness.”
Further, Descartes (1647) wrote about secondary qualities that “we are not aware of their being anything
other than various arrangements of the size, figure, and motions of the parts of these objects which make
it possible for our nerves to move in various ways, and to excite in our soul all the various feelings which
1This concession exemplifies the kind of design tradeoff decisions that need to be made while conceiving OPM names. On one
hand, consistency and orderliness are imperative, but on the other hand, clarity and expressive power are enhanced when the
language is as natural and as terse as possible. Since English, like all natural languages, has its idiosyncrasies, compromises such as
this must often be made after weighing the pros and cons of each alternative. It may also be somewhat odd that we spend so much
intellectual effort in choosing good names for abstract ideas. However, a meaningful name can make the great difference between a
well-understood and appropriately used concept, and one that misses the point due to a term that while being formally correct, is
poorly understood.

they produce there.” Similar observations were made by Newton (in Optica, 1721) about the color of
rays, and by Leibnitz (in Discourse on Metaphysics, 1686) about size, figure and motion.
This distinction was criticized by Berkeley (1710) in his “immaterialism” theory, which denied the
existence of material substance altogether. According to Berkeley, familiar objects, like a table, are only
ideas in the human perceiver’s mind, and cannot exist without being perceived. The ideas created by
sensations are all that people can know for sure. When an object is stripped of all its secondary qualities,
the idea that there is some object has no support, since without qualities one cannot give any content to
the idea of the object existence. Kant (1783) also went against this distinction, claiming that both primary
and secondary, qualities are subjective, as they are located in the brain of a knowing observer. This
discussion complements our previous treatment in Sect. 10.3 of object identity.
## 18.2 Attribute and Operation: The Two Kinds of Feature
Perseverance is a thing’s property with two values: static and dynamic. Perseverance is the property that
enables distinction between an object and a process. It determines that the thing is an object when the
perseverance value is persistent (static), and a process—when the perseverance value is transient
(dynamic). A feature—a thing that characterizes a thing—is also classified into two types based on
whether its perseverance value is static or dynamic.
An attribute is a static feature—an object that characterizes a thing, while operation is a dynamic
feature—a process that characterizes a thing. Being an object, the perseverance value of attribute is
persistent (static). Being a process, the perseverance value of operation is transient (dynamic).
The OPL sentence that relates an Exhibitor to two features, Feature 1 and Feature 2, is:
An attribute is a feature whose perseverance value is static.
An operation is a feature whose perseverance value is dynamic.
Exhibitor exhibits Feature 1 and Feature 2.
The OPL sentence that relates an Exhibitor to three features, Feature 1, Feature 2, and Feature 3, is:
Exhibitor exhibits Feature 1, Feature 2, and Feature 3.
All the features on the list must be of the same perseverance, i.e., all are attributes (object features) or
all are operations (process features). If some of the features are attributes while others are operations, we
divide the features into two lists, one of attributes and the other—of operations. If the exhibitor is an
object, then the first list of features is of (one, two, or more) attributes, and the second—of operations.
The list of attributes is connected to the list of operations by the reserved OPL phrase as well as. As an
example, the following OPL sentence specifies an Object exhibitor with three attributes and two operations:
Object exhibits Attribute 1, Attribute 2, and Attribute 3, as well as Operation 1 and Operation 2.
If the exhibiting thing is Process, the list of operations precedes the list of attributes:
Process exhibits Operation 1 and Operation 2, as well as Attribute 1, Attribute 2, and Attribute 3.

Exhibition-Characterization
## 18.3 Features in UML and SysML Versus OPM
Attributes and operations are concepts that exist also in the object-oriented (OO) approach. In OO
terminology, an attribute is also referred to as a data member, while an operation is also referred to as a
method or a service. All these words are meant to express “something that the object can do” or “a way in
which the object behaves.” In traditional procedural third generation programming languages, operation
is also referred to as a function, a procedure, or a routine. Table 18.1 summarizes the definitions of
attribute and operation as specializations of feature along with similar concepts in OO and traditional
programming languages.
Table 18.1 The specializations of thing and feature by perseverance and similar concepts in OO and traditional
programming languages
Perseverance value Thing Feature OO similar concepts Traditional similar concepts
persistent (static) Object Attribute Data member Variable, Parameter
transient (dynamic) Process Operation Method, Service Procedure, Routine,
Subroutine, Function,
OPM treats features as things that have their own right of existence, regardless of the fact they may
also characterize higher-level things. While aggregation-participation and generalization-specialization
are recognized relations in SysML (as in UML) and have their own symbols (black or white diamond for
the former, white triangle for the latter), exhibition-characterization is not an explicit relation and does not
have a symbol. Rather, an attribute is recognized as such in UML by its location in the second of the three
vertically-arranged compartments that comprise the UML object class symbol. In SysML there can be an
arbitrary number of compartments in a block, so each compartment must be labeled. For example, in Fig.
18.2, the label is “values”.
Paradoxically, although OPM does not attempt to be “purely” object-oriented, it is more object-
oriented in its treatment of characterization than the OO paradigm. In OO, attributes and methods are
encapsulated, or embedded, within objects. Are attributes not objects, but rather “different animals” that
reside within the object? If an attribute is not an object, then what is it? Does the world consist not only of
objects but also of attributes (and methods)? OPM does not encounter this dilemma, since it defines
feature generically as a thing that describes a thing and as one that specializes into an attribute—an
object—and an operation—a process.
To demonstrate the problem caused by not treating attributes as objects, consider a “classical”
example of Name and Address as attributes of the object class Person, and Moving as an operation of
Person.
## 2 As Fig. 18.2 shows on the left, in SysML this is done by assigning a title to each compartment.
The top compartment has the «Block» stereotype title, which is analogous to Object in UML and OPM,
with the name of the block, Person, underneath it. Below this top compartment are the “values”
(attributes) compartment, with Name and Address as the values, and at the bottom is the operations
2We assume here that Person is capable of Moving without the need for external objects, such that Moving can be
considered an operation of Person.

compartment, with Moving as the listed operation. In UML and many of its predecessors, such as Object
Modeling Technique, OMT (Rumbaugh et al. 1991) the attributes and operations are listed always in the
second and third class box compartments, respectively, so no titles are needed.
On the right hand side, Fig. 18.5 shows the corresponding OPM notation: Name and Address are
separate objects, and Moving is a process. Since Name and Address are linked to Person with the
exhibition-characterization symbol, they are also attributes of Person. For the same reason, Moving is an
operation of Person. A side benefit of this notation is that we can connect Moving to Address with an
effect link to denote the fact that Moving has an effect on the Address of Person, already combining
structure and behavior in this simple OPD.
### Figure 18.2
Expressing attributes (values) and operations in SysML (left) and in OPM (right)
Outside the context of Person, both Name and Address are bona fide objects in their own right.
Moreover, as shown in Fig. 18.3, each one of them consists of parts: Name consists of First Name
followed by Last Name; Address consists of Street, City, Zip Code, State and Country, in that sequence.
## 18.4 OPM Thing and Feature Name Uniqueness
Different things in an OPM model must have different names in order for them to be distinguishable and
to avoid confusion. However, when it comes to features, which are things that describe things, it becomes
difficult to come up with a different name for each feature. For example, in Fig. 18.3, there is an attribute
of Person called Name, but Street and City might, in turn, also have an attribute called Name. Hence,
features of things are allowed to have the same name as features of other things.
The uniqueness of features is maintained by adding “of Exhibitor”, where of is a reserved OPL phrase
(word in this case) and Exhibitor is the name of the thing that exhibits the feature. Thus, a feature of a
feature shall have two “of” reserved OPL words, as in Length of Name of Person. The following name
uniqueness OPM principle summarizes this.

Exhibition-Characterization
### Figure 18.3
Expressing parts of attributes in SysML (left) and in OPM (right)
The Thing Name Uniqueness OPM Principle
Different things in an OPM model which are not features must have different names. Features are
distinguishable by appending to them the reserved word “of” and the name of their exhibitor.
## 18.5 The Four Thing-Feature Combinations
Exhibition-characterization is unique among the structural relations in that it is the only one that allows
relating objects to processes and processes to objects. All the other structural relations, including in
particular the remaining three fundamental structural relations, allow linking things with the same
perseverance value only: objects (things whose perseverance value is persistent, or static) can be linked
only to objects and processes—(things whose perseverance value is transient, or dynamic) only to
processes. Thus, objects can be parts or specializations or instances only of objects, and processes can be
parts or specializations or instances only of processes. However, when it comes to exhibition-
characterization, all the four object-process (exhibitor-feature) combinations are possible. In other words,
as shown also in Fig. 18.4, since both thing and its feature can be an object or a process, the 2 2 Cartesian
product yields a state-space of four different combinations of a thing and the feature that characterizes it,
namely, from left to right and from top to bottom in Fig. 18.4: (1) an attribute of an object, (2) an
operation of an object, (3) an attribute of a process, and (4) an operation of a process.

### Figure 18.4
The four thing-feature combinations
As an example of an object-attribute combination, Address is an object in its own right, but it is also
an attribute of Person, as it is one of the things that characterize it. As an example of an object-operation
combination, Printing is a process, which is also an operation of Printer, as it is a thing that characterizes
what a Printer is capable of—what its function is. All four combinations are discussed and further
demonstrated in this section. In the following subsections we elaborate on each one of these
combinations.
## 18.5.1 The Object-Attribute Combination
The first thing-feature combination—object and its attribute—is the customary attribute of classical OO
approaches. Here we refer to an object B2—the attribute—that characterizes (describes) a higher level
object B1. Conversely, we say that B1 exhibits B2. A few examples for such pairs of objects and their
attributes are Material—Specific Weight, Person—Age, Chemical Element—Atomic Weight, Laptop—
Manufacturer, Book—Author, Officer—Rank, and Dog—Breed. The first four of these examples are
depicted in the four OPM models in Fig. 18.5.
### Figure 18.5
Examples of attributes of objects

Exhibition-Characterization
## 18.5.2 The Object-Operation Combination
The second thing-feature combination is object and its operation. As noted, in OO approaches an
operation is also called method or service (see Table 18.1 ). Here we refer to a process P1—the
operation—that characterizes a higher level object B1. Conversely, we say that B1 exhibits the operation P1.
### Figure 18.6
Examples of operations of objects
An operation of an object is a process that is internal to the object: it can be performed by the object or
its part(s) and affects only objects that are parts, features, or specializations of that object. In other words,
an operation of an object B1 has no side effect on, nor does it require any object that is outside of B1.
Under this condition, the operation can be identified as being “owned” by B1. The OO approach, and
consequently UML and SysML, view all processes as operations that are encapsulated within and owned
by objects. This encapsulation is a major source of confusion and an impediment to faithful system
modeling. In OPM, encapsulation is valid only when the process is internal to the object. In cases like
this, the process is defined as an operation of the encapsulating object.
A few examples of pairs of an object and its operation are Airplane—Flight, Person—Walking,
Printer—Printing, Officer—Commanding, and Dog—Watching. Figure 18.6 presents four OPM models
that correspond to these pairs. As these examples show, an operation is a specialization of a process. As
such, a name given to an operation should be a gerund, i.e., a verb form ending with the “ing” suffix.
Many objects, in particular physical and artificial ones, exhibit a major operation that expresses the
main function that the object is designed to perform; the service it is expected to provide. Such objects are
systems. A system (which is artificial) provides value to the system’s beneficiary. For example, the
function that the object Printer supplies is Printing, the function of Airplane is Flying, the function of
Crane is Lifting, and the function of Dryer is Drying. This is in line with our definition of an artificial
system as an object that carries out a function.
## 18.5.3 The Process-Attribute Combination
Like objects, processes require adequate representation in the model of any system. Just like objects,
processes might require attributes—objects that describe them. The idea of attributes for processes is a
natural extension to attributes for objects and poses no special conceptual difficulty.
So far, we have seen that the first and second thing-feature combinations—an object describing an
object and a process describing an object—are the corresponding object-oriented concepts for attribute
and operation (or service, or method). However, the third thing-feature combination—an object

describing a process—is not explicitly defined in the OO approach. Here we refer to an object B1—the
attribute—that characterizes a higher level process P1. Conversely, we say that the process P1 exhibits the
attribute B1. Few examples of pairs of a process and its attribute are Diving—Depth, Commanding—
Language, Printing—Quality, Striking—Duration, Manufacturing—Quantity, Watching—Effectiveness,
Singing—Volume, Skiing—Location, and Flying—Speed.
### Figure 18.7
Examples of attributes of processes
Figure 18.7 presents OPM models that correspond to the first four process-attribute pairs. Each of
these process-attribute pairs can be embedded in a natural language sentence. Here are possible examples,
where the processes are bold and their attributes are italicized:
(1) Diving at a depth of 30 meters or more requires the diver to make decompression stops.
(2) The language the office was using for commanding was foreign and strange.
(3) The printing of this device is of poor quality.
(4) The employees have been striking for duration of over two weeks.
While all the processes in these examples are nouns having the gerund form, they can be easily
converted into sentences where the processes are verbs, with the same semantics as before:
(1) A diver who dives at a depth of 30 meters or more is required to make decompression stops.
(2) The officer commands in a foreign language.
(3) This device prints with poor quality.
(4) The employees strike, and this has been lasting for a duration of over two weeks.
As these examples show, this OPM extension of the OO, UML and SysML attribute and operation
concepts is a direct consequence of recognizing processes as bona fide independent kind of things
besides, rather than being necessarily subordinates of objects, or second-class citizens that are owned
objects.
## 18.5.4 The Process-Operation Combination
The fourth and last thing-feature combination—process and its operation—is the second one that is not
explicitly defined in the object-oriented (OO), UML and SysML approaches. It is the least prevalent
combination and may be somewhat difficult to grasp. Here we refer to a process P2—the operation—that
characterizes a higher level process P1. Conversely, we say that the process P1 exhibits the operation P2.
Following OPM definition of a process, only a process can change a thing. In other words, the process is
the thing, which is “responsible” for this change. That process can be an operation. An operation of an

Exhibition-Characterization
object changes the object that exhibits (“owns” in OO terms) that operation. Likewise, an operation of a
process changes the exhibiting process—the process that exhibits that operation.
In daily life we do not think so much about operations of processes. The best way to understand the
meaning of an operation of a process is to look at time. A change of an object along the timeline means
that the state of an object (or its value, in case that object is an attribute) inspected at time t is different
from its state at a later time t + t. Extending this idea from objects to processes, if we sample a process
at two different points in time, we may notice a change in that process, manifested as a difference in the
value of one of the attributes of that process, which is caused by an operation of that process.
### Figure 18.8
Examples of operations of processes
Figure 18.8 contains four partial OPM models, each showing a process and its operation. In the model
on the left, Accelerating is an operation that changes the value of the attribute Velocity of the Moving
process. Similarly, the operation Stabilizing of the Fluctuating process changes the value of the Amplitude
attribute of Fluctuating. Next, Delaying is an operation of Transmitting that changes its Duration attribute.
Finally, Interfering is an operation of the Communicating process, which changes the value of the Signal-
to-Noise Ratio attribute of the Communicating process.
In mathematical terms, a change of an object along the timeline is a first derivative of some quantity
(which is an attribute value of that object) with respect to time. In an analogous manner, since a process is
a pattern of transformation (responsible for transforming an object), an operation of a process is a
transformation of a transformation, or a change of a change. In mathematical terms, this is a second
derivative (derivative of the derivative) of some quantity with respect to time. Indeed, the examples of
pairs of a process and its operation shown in Fig. 18.8 have the notion of changing a process and can be
quantified mathematically using second order derivatives. For example, in the OPM model on the left of
Fig. 18.8, if we denote the attribute Velocity of the process Moving of an object as a function of time by
v(t), then we know that v(t) is the first derivative of the attribute Position s of the object as a function of
time: v(t) = s′(t). Denoting by a(t) the attribute Acceleration of the Accelerating process, we have a(t) =
v′(t) = s″(t), where a(t) is the first derivative of Velocity and the second derivative of Position.
## 18.6 Fundamental Structural Hierarchies
Feature is a relative term. A thing is a feature if it describes another thing. This feature itself can have
parts or be further described by another, lower level feature. Since both exhibition-characterization and

aggregation-participation are fork relations, structural hierarchies of these relations (as well as
generalization-specialization, discussed in a couple of chapters) can be formed.
Consider the object City, whose feature hierarchy is depicted in Fig. 18.9. Three important attributes
of City, in addition to its Name, are Location, Population, and Climate. Besides being attributes of City,
Location, Population and Climate are objects in their own right, so each may have its own set of features
or parts. Location has the attributes of the Continent, Country, Region, and Coordinate Set. Population
exhibits the attributes Size and Demographics and the operations Aging and Earning. Demographics, in
turn, consists of Average Age and Average Income. Aging and Earning are two operations that
respectively affect the two parts of Demographics, and Precipitating is an operation of Climate that
affects Average Precipitation.
## 18.7 The Attribute Naming Problem
Natural languages often provide us with a definite noun for naming the attribute. For example, the
attribute whose two extremes are the adjectives “short” and “long” is called Length. The attribute whose
two extreme adjectives are “narrow” and “wide” is called Width, and the attribute whose two extremes are
“heavy” and “light” is called Weight. Sometimes, the attribute name (the noun) is from the same radical
(root word) as one of the (often extreme) values (the adjective) along the spectrum of possible values for
that attribute. Examples for such attribute-value (noun-adjective) pairs are Length—long, Width—wide,
Readiness—ready, and Beauty—beautiful. Of these pairs, the radical (root) may be either the name of the
attribute—the noun (e.g., Beauty) or the name of one of the values of that attribute—the adjective (e.g.,
ready).
### Figure 18.9
A structural hierarchy example of City
The names of some attributes are neutral nouns, while others are taken from one of the extreme values
of the attribute and are biased towards it. The attribute Shape, for example, is a neutral noun. Its values

Exhibition-Characterization
may be the adjectives round, square, elliptic, etc. There is no bias in Shape toward any of its values.
Conversely, Length is biased towards the long extreme of the short—long value spectrum. Picking up
Shortness instead would tilt the bias to the other extreme. Hence, a sentence such as “The shape of the
house is square.” makes perfect sense, whereas “The length of the stick is long,” while syntactically
correct, is semantically awkward. Skipping the name of the attribute, we would rather say “The stick is
long.” In this case, the attribute Length is implicit in the sentence. We could also skip the attribute name
of the attribute Shape in the sentence “The shape of the house is square.” and say “The house is square.”
We call such an attribute implicit. Implicit attribute sentences are usually used when the attribute name is
taken from one of its extreme values. Examples are Length, taken form the pair long–short, Beauty, taken
from the pair beautiful–ugly, and Width, taken from the pair wide–narrow. Interestingly, the choice of
which of the extremes is chosen as the name of the attribute tends to favor the one that is considered
better or larger. Thus, it is much less natural to respectively name these attributes Shortness, Ugliness,
and Narrowness, although these words are legal nouns.
The use of implicit attribute sentences in natural language is the rule rather than the exception.
Skipping the name of the attribute to which the value belongs and make direct reference to the object that
exhibits the value is most prevalent. Implicit attributes are so widespread, that in many cases the natural
language does not have a dedicated noun for the attribute itself, while the adjectives, which are the values
or states of that attribute, do have widely recognized and used names.
As an example, consider the implicit attribute sentence “This book is interesting.” The adjective
interesting refers to an attribute of this book, whose possible values may be “interesting” and “boring.”
There is no single noun for an attribute whose values are interesting and boring. Plausible names of this
attribute may be either Interest Level or Boredom Level. However, each is biased toward one of the
extremes of the spectrum or the other. Ideally, we would like a word that is neutral and not biased toward
any one of the possible attribute values.
In other cases, it is obvious that the name of the attribute was invented after the value was already in
use. For example, Laziness is a name of an attribute which has lazy as one of its values (and energetic or
industrious or hardworking as another), and the suffix “ness” hints to its later introduction into the
language. Obviously, if we attach to a Person an attribute called Laziness, we would expect the value of
this attribute to be lazy rather than hardworking. More simply and more naturally, we would like to say
that “Person is lazy.” This sentence is much shorter, clearer, and straightforward compared with the two
OPL sentences “Person exhibits Laziness.” and “Laziness of Person is lazy.” Indeed, as discussed Sect.
## 18.8 OPM has the option of implicit attribute, where lazy and hardworking are directly modeled as states
of Person rather than values of its Laziness attribute, which, in this case, becomes redundant.
However, in the general case, in OPM, where modeling is formal, we often have to explicitly model
the attribute before we can model its states or values, and if there is no word for the attribute, we have to
invent it. Indeed, in OPM there is the problem of finding adequate names for properties (metamodel
attributes) of Thing. The name of the property of Thing whose values are natural and artificial is Origin.
We have also called Essence the property of Thing whose values are physical and informatical.
Perseverance has been chosen as the name for the property whose values are persistent (in which case
the thing is an object) and transient (in which case the thing is a process). The choice of these property
names points to the difficulty in finding the right word to name an attribute (or property) whose values are
prevalent. For example, transient and persistent, which are the values of the property Perseverance, are

widely used, while Perseverance is not recognized in conjunction with these adjectives. Origin and
Essence are neutral. Perseverance is less neutral; the American Heritage Dictionary (1996) defines
perseverance as “steady persistence in adhering to a course of action, a belief, or a purpose;
steadfastness.” Steady persistence inclines toward the notion of Object, since its Perseverance value is
indeed persistent. However, course of action has the notion of a process…
## 18.8 Properties of Features and Links
Features and Links have several properties (metamodel-level attributes), which are discussed in this
section. These include Explicitness, Mode, Touch, and Emergence. Some of these properties are relevant
to Feature in general, i.e., to both Attribute and Operation, while others—just to Attribute.
## 18.8.1 Explicitness
OPM caters to the natural language tendency to skip attributes and jump directly to their values, as Sect.
## 18.7 discusses, by providing the option to model attributes implicitly, as Fig. 18.10 demonstrates.
exhibition-characterization relation.
implicit.
An attribute is implicit if its values are assigned as states directly to the exhibitor with
no specification of the attribute name.
An attribute is explicit if it is a separate object that is linked to the exhibitor with an
Explicitness is an attribute of an attribute whose values are explicit (the default) and
### Figure 18.10
Explicit and implicit attribute modeling
It is easy to identify an implicit attribute: If an object has states that are placed directly inside its
rectangle rather than in its attribute, then the attribute whose values are within the object is implicit. By
default, an attribute is explicit—its Explicitness value is explicit. It often makes sense to use an implicit
attribute, as this circumvents the attribute naming problem discussed in the previous section—the need to
invent a name for the attribute. We saw the example of Laziness in the previous section. As another

Exhibition-Characterization
example, Lamp can be on or off. It would be cumbersome to define a dedicated explicit attribute for these
states and difficult to find a good name for it: “Onness”? “Offness”? “Operational Status”? None of these
makes sense.
It is not possible to have more than one implicit attribute for the same thing, because this would mix
values of different attributes in the same sentence without affiliating them with the proper “owning”
attributes. For example, examining Fig. 18.10, we observe that sentences such as “Stick can be light,
heavy, short, or long” do not make sense, because values of the Weight and Length of Stick are mixed.
We can have either Weight or Length as implicit attributes, but not both. In the OPM model on the left of
Fig. 18.10, both Weight and Length are explicit attributes of Stick. In the middle, Length is an explicit
attribute, with values long and short, while Weight is implicit, with states light and heavy. Finally, in the
OPM model on the right, the opposite is true: Weight is an explicit attribute, with values light and heavy,
while Length is implicit.
## 18.8.2 Mode
Some attributes are qualitative while others are quantitative. We have seen the example of the attribute
Shape of House, where possible values can be round, square, and rectangular. These values cannot be
quantified by a numeric value. They are just qualitatively different from each other. We say therefore that
Shape is a qualitative attribute. Other examples of qualitative attributes include Mood, with states happy,
sad, angry, etc., Health, with states healthy and sick, and Marital Status, with states single, married,
divorced, etc. Examples of quantitative attributes are Weight [Kg] and Height [m]. As these examples show,
quantitative attributes need to be followed by the unit of measurement in brackets, as discussed in Chap.
22. Since an attribute can be qualitative or quantitative, qualitative and quantitative are values of a
property of Attribute called Mode.
An attribute is quantitative if its values are numerical or parametric.
An attribute is qualitative if its values are non-numerical.
An operation is quantitative if it transforms a quantitative attribute, otherwise it is
quantitative.
Mode is a property of a feature that determines whether it is qualitative (the default)
or quantitative.
The definition of numerical here includes parametric—a parameter is a symbol that stands for some
numerical value. We could assign numeric values, or “codes” to values of a qualitative attribute, for
example, single = 1; married = 2. Indeed, this was a common practice in early information processing
systems and is still often the practice, especially when data has to be analyzed statistically. However,
semantically this does not render a qualitative attribute quantitative.
An example of quantitative operations is Height Measuring, which creates a value for the quantitative
attribute Height. Another example is Weighing, which creates a value for the quantitative attribute Weight.
Section 13.10 discusses how to model setting or updating values using value-specified procedural links.

## 18.8.3 Touch: A Property of a Quantitative Attribute
A quantitative attribute can be hard or soft, depending on whether it can be computed from other
attributes or not. For example, Date of Birth of a Person is a hard attribute, while Age of Person is a soft
attribute. By knowing the Date of Birth of a Person and the current value of Date, Age of Person can be
computed. As another example, the Weight of each part of Airplane is a hard attribute, while the total
Weight of Airplane is a soft attribute since it can be computed by summing the weights of the individual
parts. The name of the property of Attribute whose values are hard and soft is Touch.
A quantitative attribute is hard if its value cannot be deduced or computed from other
attributes.
A quantitative attribute is soft if its value can be deduced or computed from other
attributes.
Touch is a property of a quantitative attribute which determines whether it is hard
(the default) or soft.
Deciding whether a soft attribute should be pre-computed has practical implications during the
detailed design stage of an information system. Pre-computed values can be stored for quick response
time at the cost of storage space. Alternatively, soft attributes can be computed on demand, saving space
but also delaying the response time of the information system. This is a common tradeoff in databases,
where the need for high response speed is weighed against storage overhead.
## 18.8.4 Emergence
Depending on whether a feature is exhibited only by the object as a whole or only by one or more (but not
all) of its parts, a Feature (an Attribute or an Operation) can be inherent or emergent.
A feature of an object is inherent if a least one of the object’s parts exhibits it.
A feature of an object is emergent if no one of the object’s parts alone exhibits it.
Emergence is a property of an object whose values are inherent (the default) and
emergent.
To understand the difference between emergent and inherent features, consider Airplane’s attribute
Weight and its operation Flying. Weight of Airplane is the sum of the individual Weight values of each one
of the parts that make up the Airplane. Flying, on the other hand, was not an operation that any part of
Airplane could exhibit on its own. Rather, this feature emerges from the unique ensemble of the parts of
Airplane that endows Airplane with the ability to carry out the Flying operation. Hence, Flying is an
emergent feature (operation in this case) of Airplane, while Weight is an inherent feature (attribute in this
case) of the Airplane.
In systems, operations are frequently emergent, because systems are built with the intent of achieving
some function that is not localized in or achievable by any part of the system alone. Flying of Airplane is
an excellent example. Bar-Yam (1997) distinguishes between simple and complex systems and claims

Exhibition-Characterization
that complexity can emerge from a collection of simple parts that comprise a system. The converse can be
true as well: a system composed of complex parts may exhibit simple behavior at a larger scale. For
example, planet Earth is a highly complex system, but when viewed from the perspective of its movement
around the sun, it is relatively simple, pointing to the relativity of the term complexity.
## 18.8.5 The Link Homogeneity Property
The property that specifies whether a link connects things with the same Perseverance—static
(persistent, defining an object) or dynamic (transient, defining a process) is called Homogeneity. The
values of Homogeneity are homogeneous, which applies if the two things that the link connects exhibit
the same Perseverance (either both are objects or both are processes), and non-homogeneous otherwise
(one is an object and the other—a process). Since most structural links are between two objects or
between two processes, the Homogeneity value homogeneous is the default for structural links.
Conversely, since most procedural links are between an object and a process, the Homogeneity value non-
homogeneous is the default for procedural links.
A link is homogeneous if it connects two things that exhibit the same perseverance
value.
A link is non-homogeneous if it connects two things that exhibit opposite
perseverance values.
Homogeneity is a property of a link whose values are homogeneous (the default for
structural links) and non-homogeneous (the default for procedural links).
Almost all the structural links are only homogeneous: they either connect two objects or two
processes. The only exceptional structural link that is Exhibition-Characterization, which can be both
homogeneous (in case it connects an object with an attribute or a process with an operation) or non-
homogeneous (in case it connects an object with an operation or a process with an attribute). All the
other structural links, and in particular the remaining three fundamental structural relations, are
homogeneous. Analogously, almost all the procedural links are non-homogeneous, as they connect an
object to a process. The only procedural links that are homogeneous are the invocation link discussed in
Sect. 10.10.3 and the overtime and undertime exception links discussed in Chap. 22.
## 18.9 Summary
Exhibition-characterization is a relation between a thing and the features that characterize it.
The shorthand name of this relation is characterization and its symbol is .
Characterization is the only fundamental structural relation for which all four combinations of an
object and a process, as an exhibitor and a feature, are possible.
A feature which is an object, is called an attribute, while a feature which is a process is an
operation.

An attribute is implicit if its values are assigned directly to the exhibitor with no specification of
the attribute name.
An attribute is explicit if it is a separate object that is linked to the exhibitor with an exhibition-
characterization relation.
Explicitness is an attribute of an attribute whose values are explicit (the default) and implicit.
An attribute is qualitative if its values are non-numerical.
An attribute is quantitative if its values are numerical.
An operation is quantitative if it transforms a quantitative attribute, otherwise it is quantitative.
Mode is a property of a feature that determines whether it is qualitative (the default) or
quantitative.
A quantitative attribute is hard if its value cannot be deduced or computed from other attributes.
A quantitative attribute is soft if its value can be deduced or computed from other attributes.
Touch is an attribute of a quantitative attribute which determines whether it is hard (the default)
or soft.
A feature of an object is inherent if a least one of the object’s parts exhibits it.
A feature of an object is emergent if no one of the object’s parts alone exhibits it.
Emergence is a property of an object whose values are inherent (the default) and emergent.
A link is homogeneous if it connects two things that exhibit the same perseverance value.
A link is non-homogeneous if it connects two things that exhibit opposite perseverance values.
Homogeneity is a property of a link whose values are homogeneous (the default for structural
links) and non-homogeneous (the default for procedural links).
## 18.10 Problems
1. 2. 3. 4. 5. For each one of the four exhibitor-feature combinations, draw an OPD that is not provided as an
example in this chapter.
“The quick brown fox jumps over the lazy dog” is an English-language sentence called
pangram—a phrase that contains all of the letters of the alphabet. Create an OPM model of this
sentence in which Jumping is an operation of Fox.
In the model you created in the previous question change each explicit attribute to an implicit
one and vice versa.
Provide two examples of inherent features and two of emergent features.
Create an OPM model of the structure—parts and features—of the Pazyryk burial mounds
chariot in the Hermitage Museum in St. Petersburg according to the following description
(image available in URL).
This large four-wheel chariot is one of the striking finds of the Pazyryk burial mounds. It consists of a number of
parts joined together by leather straps and wooden nails. The trunk is made of two frames joined by means of short
carved poles and leather straps. The frames constitute the basis for the canopy. Each of the four large wheels has 34

Exhibition-Characterization
spokes. The axles do not have a rotary device, and the distance between the back and front wheels is only 5 cm, which
meant that the chariot could only be used on flat ground. It could, however, be easily disassembled and transported
on horses. Thanks to the permafrost, the chariot is in an excellent state of preservation.
