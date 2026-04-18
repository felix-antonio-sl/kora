# Chapter 15 Participation Constraints and Forks
Fork: the point or part at which a thing, as a river or a road, divides into branches.
Dictionary.com
In all the examples and discussions so far we have tacitly assumed that each thing, be it object or process,
participates in the relation singly, i.e., in a quantity of exactly 1. Indeed, the convention in OPDs is that
when no quantity is explicitly recorded by the side of a structural link, it is taken to be 1, which is the
default value. In general, however, we may wish to specify a certain number or a range of numbers of
instances of the same class of things that participate in the relation. Similarly, our models so far have
tacitly assumed that a process involves one object instance of each object class to which it is linked.
Indeed, this is the default. However, it is sometimes required to model the fact that more than one object
takes part in a process. Process participation constraints and link cardinalities are designed to take care of
this. We then turn to another useful notation—the fork—which is based on the observation that structural
relations are distributive in a sense analogous to the distributive law in algebra. This is graphically
represented via forks, as defined, discussed and demonstrated in this chapter.
## 15.1 Structural and Procedural Participation Constraints
When more than one object is involved in a relation, a participation constraint needs to be specified to
denote this.
A participation constraint is a property of a link expressing the number or a
mathematical expression recorded along a link next to an object, which denotes the
multiplicity (number of repetitions) of that object in that relation.
Since a relation and the link denoting it can be structural or procedural, there are two corresponding
kinds of participation constraints: structural and procedural.
A structural participation constraint is a participation constraint recorded along a
structural link.
A procedural participation constraint is a participation constraint recorded along a
procedural link.
The default participation constraint is 1, and it is implicit. Thus, if exactly one thing participates in
the relation, no participation constraint needs to be specified. When the participation constraint on the

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 15

Participation Constraints and Forks
destination side of the structural link is different than 1, it has to be specified explicitly, as shown in Fig.
## 15.1 for a structural relation.
A one-sided participation constraint is a participation constraint on either the source
## 15.2 Structural Participation Constraints
Structural participation constraints can be one- or two-sided.
A source participation constraint is a one-sided participation constraint on the source side of the link.
A destination participation constraint is a one-sided participation constraint on the destination side of the
link.
or the destination link side.
### Figure 15.1
A destination participation constraint example
The OPD in Fig. 15.1 is an example of a destination participation constraint—a tagged structural link,
for which the participation constraint is on the destination (link target) object. In this example, it is
expressed as a specific number, 6. The destination object Pencil in the OPD of Fig. 15.1 has the
participation constraint 6, while the object Box has the implicit default participation constraint, which is 1.
If the participation constraint is explicit, as it is for Pencil in the OPL sentence “Box contains six
Pencils”, it means that the participation constraint is greater than 1. In this case, while generating the OPL
sentence from the OPD, the numeric or symbolic value or mathematical expression of the participation
constraint is put before the object name and the object name becomes plural.1
To keep up with English grammar, the verb for any tag, including the null tag, has to conform to the
plurality of source and destination things in the sentence. For example, if the source Bedroom of a
unidirectional null tag has a participation constraint of 3, and the destination is Apartment, the OPL
sentence is: “Three Bedrooms relate to Apartment.” To follow the rule to “spell small numbers out”, the
numerals (symbols) of numbers from zero to nine should be written in letters or as digits (figures), so
“Three Bedrooms relate to Apartment.” is preferable. Therefore the OPL sentence in Fig. 15.1 has in it six
rather than 6.
Ignoring the participation constrain in Fig. 15.2, the OPL sentence would be simply “Bolt fasten
Flange.” Since the source object Bolt has the participation constraint 8, while the destination object
Flange has the implicit default participation constraint, we get OPL sentence in Fig. 15.2.
1Usually that means concatenating the letter s, but a program that generates OPL sentences from OPDs should also
account for exceptions of converting a noun from singular to plural. Indeed OPCAT handles most of the irregularities
associated with plurals.

### Figure 15.2
A source participation constraint example
## 15.2.1 Parameterized Structural Participation Constraints
By default, a participation constraint is numeric, i.e., it is specified as a number, usually an integer, as
shown in the OPDs in Figs. 15.1 and 15.2. However, a participation constraint can also be parameterized,
i.e., it can be a mathematical expression containing one or more symbols.
A parameterized participation constraint is a participation constraint which is a
mathematical expression with one or more parameters.
Figure 15.3 is an example of a parameterized participation constraint. Here, n is a natural number and
the modeler expresses the fact that the number of Cylinders in Engine is even.
### Figure 15.3
A parameterized participation constraint example
When numbers, even small ones, are involved in a sentence with parameters, as in Fig. 15.3, or in a
range (as in Fig. 15.4, see next section), then the numbers are expressed as digit numerals and not in
letters. The syntax of participation constraint expressions and more elaborate example of parameterized
participation constraints are provided in Chap. 17 below on aggregation-participation.
## 15.2.2 Range Participation Constraints
A participation constraint can be more than just a single number or a single expression. It can also be a
range.
A range participation constraint is a participation constraint with lower and upper
bounds, each possibly an expression, on the number of possible objects that can take
part in the relation.
A compound participation constraint can be any combination of numbers, expressions, and ranges. A
range is denoted as “qmin .. qmax”. A single number or parameter can be thought of as a special case of
range with qmin = qmax.

Participation Constraints and Forks
Two compound participation constraints are exemplified in Fig. 15.4. In the left OPD, the compound
participation constraint comprises two ranges. In the first range, qmin = 3 is the lower bound and qmax = 5 is
the upper bound. The two quantities are separated by two consecutive dots. The second range is 8..10. In
the right OPD of Fig. 15.4, the compound participation constraint comprises one number, 2, and one
parameterized range, 3*n, where n 4.
Often, qmin is a small number, such as 0, 1, or 2, while qmax is the symbol *, which stands for many. The
symbol * is a “reserved symbol” in participation constraint, meaning that the exact value of “many” is not
fixed as in an algebraic equation. A letter stands for a parameter—a particular, yet unspecified number.
### Figure 15.4
A one-sided cardinality with a range participation constraint of 3..5
## 15.3 Shorthand Notations and Reserved Phrases
The reserved phrase “qmin to qmax” can be used for any of the participation constraints, where both qmin and
qmax can be any real number. However, it frequently makes more sense to use different phrases that
express the participation constraint more naturally.
As in UML and SysML, the asterisk symbol * stands for “many”, so “0..*” means zero or more, or, in
other words, “optional”, abbreviated as *. The range “1..*”, abbreviated as +
, means one or more, and as an
OPL reserved phrase: “at least one”.
The four abbreviated participation constraint symbols are:
“?” for 0..1,
“*” for 0..*,
nothing for 1..1, and
“+” for 1..*.
Each such abbreviation has a corresponding OPL reserved phrase. The abbreviated participation
constraint symbols, their bounds, OPL reserved phrases, and sample OPDs with corresponding OPL
sentences are shown in Table 15.1.
Combining particular values is also allowed. For example, the participation constraint “?, 3..*” is legal
and is translated in OPL as “optional or at least 3”. Finally, while all the examples so far referred to
objects, they can be applied to processes as well.

Table 15.1 The abbreviated participation constraint symbols, their bounds, phrases, and sample OPDs with
corresponding OPL sentences
## 15.4 Cardinality
In a structural relation, each link edge—one on the source side and the other on the destination side—can
have a participation constraint that is in general independent of the participation constraint on the other
edge.
Source participation constraint is the participation constraint on the source side of
the (structural or procedural) link.
Destination participation constraint is the participation constraint on the destination
side of the (structural or procedural) link.
The definition refers equally to structural and procedural links. The combination of the two
participation constraints is the link’s cardinality, which also applies to structural and procedural links
alike.

Participation Constraints and Forks
Cardinality is a property of a link whose value depends on the combination of the
source and destination participation constraints of the structural link.
We denote the cardinality as [qmin .. qmax, q′
min .. q′
max], where qmin and qmax are the lower and upper
bounds of the participation constraint on the source side of the link, while q′
min and q′
max are the
corresponding parameters on the link’s destination side.
## 15.4.1 The Four Common Cardinality Kinds
Cardinality is an important factor in database schema design, which takes place during the design phase
of information systems development. The various kinds of participation constraints on the two structural
link edges give rise to a number of combinations. Traditionally, these combinations were thought of as
yielding four possible cardinality kinds: one-to-one, one-to-many, many-to-one and many-to-many. These
are exemplified in Fig. 15.5.
### Figure 15.5
The four cardinality kinds exemplified
As the top OPD in Fig. 15.5 shows, a one-to-one cardinality exists when no participation constraint is
recorded on either side of the structural link, in which case the default value 1 is assigned to both sides. A
one-to-many cardinality exists when there is an explicit participation constraint with qmin > 0 and qmax > 1
on exactly one side of the structural link and 1 on the other. This is exemplified in the second OPD in Fig.
15.5, while the third is an example of many-to-one cardinality. Finally, a many-to-many cardinality exists
when the participation constraints on both sides of the structural link are explicit, and in both qmax > 1, as
exemplified in the bottom OPD of Fig. 15.5.
## 15.4.2 The 16 Cardinality Kinds
Combining pairs of the four symbols “?”, “*”, “1”, and “+”, we get 16 cardinality kinds. These are listed
in the 4 4 array in Table 15.2. The array cells with the four customary cardinalities, [1, 1], which is “one-
to-one”, [1, +], which is “one-to-many”, [+,1], which is “many-to-one”, and [+, +], which is “many-to-
many”, are greyed at the bottom-right part of the table. These cardinality kinds are the ones recognized in

entity relationship diagrams (ERDs), proposed by Chen (1976), which are used to design databases. Here
we see that they comprise one quarter of the 16 possible combinations.
Table 15.2 The 16 cardinality types obtained by combinations of pairs of the four participation constraint kinds
## 15.5 Procedural Participation Constraints
By its definition, a process must transform at least one object, but there could be more. Moreover, we
want to be able to model the fact that an enabler, be it an agent or an instrument, is optional or is required
in a certain amount. A procedural participation constraint, defined above as a number or an expression
recorded along a procedural link next to the source or destination object, denotes the multiplicity of that
object in that procedural relation. The quantity of processes is always assumed to be one, so there is no
participation constraint next to the process end of the procedural link.
Figure 15.6 shows two procedural participation constraints, one on an agent link and the other—on an
effect link. As with the structural participation constraints, the + (plus) symbol stands for “at least one”,
while the * (asterisk) symbol—for “optional”. Following the grammatical rule that numbers up to ten
should be spelled out in text rather than as digits, the number 3 in the OPD is written as Three in the
corresponding OPL paragraph sentence. This is an optional convention and it is not used in conjunction
with parameters, as Fig. 15.7 demonstrates.
### Figure 15.6
Examples of two participation constraints on procedural links

Participation Constraints and Forks
## 15.5.1 Parameterized Procedural Participation Constraints
Figure 15.7 shows the use of a variety of participation constraints in procedural links with parameters,
ranges, and parameter constraints.
### Figure 15.7
Participation constraints in procedural links with parameters, ranges, and parameter constraints
As both the OPD and the OPL express, in this Blade Replacing system, a Jet Engine has b Installed
Blades. Two to four (a number set to k) Aviation Engine Mechanics handle the process, for which they
use k Blade Fastening Tools. The Blade Replacing process is also handled by one or two Aerospace
Engineers. This process yields b Dismantled Blades, which undergo Blade Inspecting, an environmental
process that yields a number a (which is at most b) of inspected Blades. The process consumes a total of
b Blades, of which i are inspected and b–i are new. This is the number of new Blades obtained by
Purchasing them. This example shows not only how parameterized participation constraints are used with
procedural links, but also how they can serve to express parameter constraints—constraints among the
parameters. Additional constraints can be added. For example we could specify that i≤b to avoid getting a
negative number for b–i.

## 15.5.2 Enabler and Transformee Participation Constraints
A process must contain at least one transformee and it can have one or more enables. This is expressed in
the OPD in Fig. 15.8, showing a metamodel of the kinds of objects involved in Processing, classified into
Enablers and Transformees.
### Figure 15.8
Participation constraints on Enablers and Transformees
If A, B, and C are all objects or are all processes, and is a structural relation, then
## 15.6 The Distributive Law of Structural Relations
In algebra, when we have an expression of the form ab + ac, we can factor it out and write it as a (b+c).
In a similar vein, the distributive law of structural relations is as follows.
This is not just a law in mathematics and in OPM, but, as we see next, the same idea is applicable also
in natural languages. The two OPDs in Fig. 15.9 provide an example of the graphical application of the
distributive law of structural relations. In the OPD on the left hand side of Fig. 15.9 there are two disjoint
tagged structural links, both bearing the same tag employs. One employs tag is recorded along the link
from Firm to Graphic Designer and the other—along the link from Firm to Systems Engineer. This OPD
A B, A C A (B, C ).

Participation Constraints and Forks
has exactly two graphic sentences, each giving rise to one OPL sentence. Denoting the relation employs
by , Firm by A, Graphic Designer by B and Systems Engineer by C, ignoring the added participation
constraints, this is like writing A B, A C.
### Figure 15.9
The distributive law of structural relations applied in OPDs. Left: disjoint links. Right: joint links
This is not just a law in mathematics and in OPM, but, as we see next, the same idea is applicable also
in natural languages. The two OPDs in Fig. 15.9 provide an example of the graphical application of the
distributive law of structural relations. In the OPD on the left hand side of Fig. 15.9 there are two disjoint
tagged structural links, both bearing the same tag employs. One employs tag is recorded along the link
from Firm to Graphic Designer and the other—along the link from Firm to Systems Engineer. This OPD
has exactly two graphic sentences, each giving rise to one OPL sentence. Denoting the relation employs
by , Firm by A, Graphic Designer by B and Systems Engineer by C, ignoring the added participation
constraints, this is like writing A B, A C.
In the OPD on the right hand side of Fig. 15.9, the two employs tagged structural links are joined at
their origin and fork (diverge) somewhere along the link. Since now only one structural link emanates
from the source object, the two OPL sentences become one. Using our notation, again ignoring the added
participation constraints, this is like writing A (B, C). The expressions representing the left and right
OPDs are the same as those in the algebraic formula of the distributive law above (with the addition of the
participation constraints). Indeed, they are semantically equivalent both graphically and textually.
Processes can also be related by structural relations that are distributive, but since the use of structural
relations is much more prevalent for objects, we focus on objects.
Graphically, joining of the origin of the two structural links in Fig. 15.9 having the same tag employs
has the same function as the algebraic parentheses. The parentheses in the distributive law expression
A (B, C) A B, A C enable using just once. Analogously, the joint tagged link enables using
employs just once in both the OPD and is corresponding OPL sentence. Finally, the OPL reserved word
and is analogous to the comma in the distributive law expression. Joining structural relations with the
same tag gives rise to forks, which are discussed next.

## 15.7 Fork, Handle, and Tine
In algebra, the distributive law A (B, C) A B, A C is extensible to any number n of elements. Thus,
A (B1, B2, … Bn) A B1, A B2, … A Bn. The same is true for OPM and natural languages. To
express this in OPM we define fork below.
A fork is a combination of two or more structural links with the same semantics
expressed by the same tag.
A fork has a common joint edge on the origin side of the link, called handle, which splits into two or
more edges on the destination side of the link, each of which is a tine.
Handle is the joint origin-side edge of the fork.
Tine is the split destination-side edge of the fork.
Handle thing is the thing linked to the handle of the fork link
Tine thing is a thing linked to a tine of the fork link.
Object fork is a set of objects connected by a fork.
Process fork is a set of processes connected by a fork.
Since a structural relation is between objects or between processes, if the handle thing is an object, all
the tine things are also objects, and the same applies to processes. The two OPDs in Figs. 15.10 and 15.11
exemplify the value of using fork relations. The OPD in Fig. 15.10 contains 10 separate structural links,
all having the tag passes through. It is therefore equivalent to the OPL paragraph in Fig. 15.10, which
has 10 OPL sentences. This OPL paragraph reflects the redundancy of links in its corresponding OPD.
Though syntactically and semantically correct, the 10-sentnece paragraph is mechanical, repetitive, and
not suitable for human reading.
The application of the distributive law provides for aggregating the ten links into a fork. Using the
expression A B1, A B2, … A Bn A (B1, B2, … Bn), and substituting A= Danube River, B1=
Germany, B2= Austria, etc., the result is presented in Fig. 15.11, where only one structural link, labeled
passes through, emanates from The Danube River, forking into ten tine. The OPL paragraph of this OPD
shrinks from ten sentences to just one fork OPL sentence—a single perfect and more humanly readable
English sentence. The handle of the fork in Fig. 15.11 is the segment emanating from the handle object
Danube River, while each of the 10 tines is the line segment with the arrowhead reaching to a tine object
(a country box in this example) and the segment connecting this line segment to the handle.
The participation constraints on the various tines may be different from the default, 1, for each tine
object separately. Since the handle is common to all the tines, its participation constraint is also common.
If a different participation constraint is required on the handle side for some link, then this link needs to
be separated from the fork.

Participation Constraints and Forks
Germany Austria Danube
passes through
passes through
passes through
passes through passes through passes through
River
passes through
passes through
passes through
passes through
Romania Moldova Slovakia
Hungary Croatia Serbia Bulgaria Ukraine
Danube River passes through Moldova.
Danube River passes through Germany.
Danube River passes through Romania.
Danube River passes through Hungary.
Danube River passes through Serbia.
Danube River passes through Austria.
Danube River passes through Slovakia.
Danube River passes through Bulgaria.
Danube River passes through Ukraine.
Danube River passes through Croatia.
### Figure 15.10
The 10 countries through which the Danube River passes through
### Figure 15.11
The 10 “passes through” tagged links in Fig. 15.10 are replaced by a single fork with the same tag
### Figure 15.12
An example of a fork with processes

Figure 15.12 is an example of a fork in which all the linked things are processes, demonstrating that
all the things connected by a fork are of the same persistence: either all are object or all are processes.
This is so because structural relations are between things of the same persistence, i.e., between two
objects or between two processes. Therefore, if the handle thing is an object, the tine things are all objects
too, and vice versa.
## 15.8 The Tine Thing Set
A set is an abstract collection of things (also called elements or members). Each thing in the set is unique.
The tine thing set of a fork is the set of all the things linked to the tines of the fork.
The tine object set of a fork is the set of all the objects linked to the tines of the fork, while the tine
process set of a fork is the set of all the processes linked to the tines of the fork.
The tine object set of the fork labeled employs in the OPD in Fig. 15.9 includes the two types of
occupations that the Firm employs. The tine object set of the fork labeled employs in the OPD in Fig. 15.9
is {Graphic Designer, Systems Engineer}. The tine object set of the fork labeled passes through in the
OPD Fig. 15.11 is {Germany, Austria, Slovakia, Hungary, Croatia, Serbia, Bulgaria, Romania, Moldova,
Ukraine}.
Frequently, showing all the fork things overloads the OPD both graphically and mentally, as is the
case in Fig. 15.11. If the tine object set is significantly greater than 2, as in Fig. 15.11, it may be
convenient to omit some of the objects in the tine object set that are not relevant for what that particular
OPD is designed to convey. Indeed, recall that the model fact representation OPM principle stipulates that
an OPM model fact needs to appear in at least one OPD in order for it to be represented in the model;
objects that are not relevant in a particular OPD do not need to be shown in it. Following this principle,
not each OPD in a system’s OPD set that contains the handle thing must contain all the things in the tine
thing set. Suffice it that each one of the tine things appears once in a relation to the handle thing in
order for it to be part of the set of tine things. We exemplify and elaborate on this when we define and
discuss the fork degree and comprehensiveness properties next. One OPD may contain one subset of the
tine thing set, while in other OPDs that belong to the same OPD set, other subsets of things connected to
tines can be hidden to alleviate cognitive load and enhance the diagram readability.
Three fork properties help refine the OPM model: degree, comprehensiveness, and orderability. These
are discussed next in this section.
## 15.8.1 Fork Degree
The size (number of elements) of the tine object set is equal to the fork degree.
Fork degree is a property of fork whose value is the size of the tine object set.

Participation Constraints and Forks
For example, the degree of the fork in Fig. 15.9 whose handle is Firm is 2.The degree of the fork from
Danube River in Fig. 15.11 is 10, as the tine object set of the fork labeled passes through in the OPD in
### Figure 15.11
includes all ten countries through which the Danube River passes.2
The tine thing set of a fork is the union of the tine sets emanating from the same
handle and having the same tag in all the OPDs in the OPD set.
For example, suppose another OPD in the OPM model to which the OPD in Fig. 15.9 belongs has the
following tine object set of size 4: {Systems Engineer, Programmer, Software Engineer, Project Leader}.
Suppose also that these are the only two OPDs in the OPD set of that OPM model where the object Firm
appears with the tagged structural link labeled employs. The tine object set of the fork labeled employs
would then be: Tine-object-set (Firm employs) = {Graphic Designer, Systems Engineer} {Systems
Engineer, Programmer, Software Engineer, Project Leader} = {Graphic Designer, Systems Engineer,
Programmer, Software Engineer, Project Leader}. The fork degree of the OPD that shows all the
occupations that the firm employs is 5—the size of the tine object set.
## 15.8.2 Fork Comprehensiveness
While omission of irrelevant tine things helps eliminate the excess clutter frequently caused in OPDs of
real life systems, it may also mislead the reader of an individual OPD into thinking that the tine thing set
presented in that particular OPD is comprehensive, i.e., all the tine things that can be linked to the handle
thing are indeed linked. To avoid such confusion, it is important to indicate whether all the things in the
tine thing set that can be linked to the handle are indeed linked. To this end, we define the fork’s
comprehensiveness property value as follows.
Fork comprehensiveness is a Boolean property of a fork which is positive if all the
things in the tine thing set are attached to the fork’s handle and negative otherwise.
Being a Boolean property, Comprehensiveness has two values: positive, if the fork is comprehensive,
i.e., all the things in the tine thing set are attached to the fork’s handle, and negative otherwise. Using the
fork’s comprehensiveness property, one can indicate whether the structure implied by the fork is
comprehensive or non-comprehensive. The importance of fork comprehensiveness is that it tells the
diagram reader whether all the tine things that can potentially be linked to the handle object are indeed
linked. A non-comprehensive fork is marked by a short bar perpendicular to the fork near the handle thing.
Continuing the example in Fig. 15.11, suppose in some OPD we wish to show only those countries or
areas that were historically “behind the iron curtain”. Examining the OPD in Fig. 15.13, we see that
Germany and Austria were removed. Graphically, the non-comprehensiveness of this fork is marked by
the non-comprehensive fork symbol—the short bar perpendicular to the fork near the handle object. This
non-comprehensive fork symbol expresses the fact that not all the countries through which the Danube
River passes are represented in this OPD. The OPL reserved phrase that expresses the fact that the fork is
non-comprehensive is “and more”, which is appended at the end of the list of fork objects, as the OPL
sentence in Fig. 15.13 demonstrates.
2For trivia lovers: The Danube river passes across the most national borders (askville.amazon.com).

### Figure 15.13
A non-comprehensive fork is marked by the short bar perpendicular to the fork near the handle object
The default value of the fork’s Comprehensiveness property is positive, meaning that the fork is
comprehensive and indicating that all the objects in the tine set of the fork are attached to the fork’s
handle. In this default case the handle will not be marked with the non-comprehensive fork symbol. The
other value of Comprehensiveness is negative, so the fork is non-comprehensive, implying that the tine
set is incomplete, as at least one tine thing is missing. The OPL reserved phrase “and at least one more” at
the end of the OPL sentence in Fig. 15.13 expresses this. A non-comprehensive fork can be made
comprehensive by completing the missing things in the forks’ tine thing set while removing the non-
comprehensive fork symbol, thereby changing its Comprehensiveness state from negative to positive.
## 15.8.3 Fork Orderability
The elements of a set in general, and the things in the tine thing set of a fork in particular, can be ordered
or unordered. This is determined by the fork’s orderability property.
Orderability is a Boolean property of a fork’s thing tine set, which is positive if the
things in the tine thing set are ordered and negative otherwise.
Like Comprehensiveness, Orderability is a Boolean attribute of the Tine Set of a Fork, whose values
are positive and negative. A Tine Set with negative Orderability is an Unordered Tine Set, and this is the
default, so it requires no special indication.
For a thing tine set with positive orderability, there often (but not always) exists some logical relation
of the things in the tine thing set {T1 … TN} such that T (j) T (j+1) for each T (j) in {T (1)
,T (2)
,..,T (N)}. For
example, if Ti; 1 < i < N is a set of N natural numbers, and is the < inequality symbol, then the
orderability of the tine thing set is positive. If the tine thing set is the parts of a scientific paper {header,
body, footer} there is no that determines this order.
A Tine Set with positive Orderability is an Ordered Tine Set. To denote that a fork’s tine set is
ordered, the word ordered appears next to the handle of the fork, as demonstrated in the OPD in Fig.
15.14. The word ordered is a graphic symbol rather than a reserved OPL phrase, because it is part of the
OPD just like the non-comprehensiveness fork symbol.

Participation Constraints and Forks
As Fig. 15.14 shows, the OPL reserved phrase for denoting that a tine thing set is ordered, is “in this
order”, which is added after a comma at the end of the sentence. For a non-comprehensive and ordered
fork, the OPL phrase is “and at least one more, in that sequence”.
### Figure 15.14
An ordered tine set of a fork relation is marked by the word “ordered” next to the fork’s handle
To express the order graphically, the things in the tine thing set must be arranged either horizontally
from left to right, as in Fig. 15.15, or vertically, from top to bottom. The object boxes may not be ordered
nicely even though the orderability of the tine thing set is positive.
To resolve this potential ambiguity, the ordering algorithm is to arrange the objects by the left-to-right
order of their leftmost side of the object box (increasing x coordinate), and for those with the same left
side coordinate, arrange by top-to-bottom order of the topmost side of the object box (decreasing y
coordinate, or increasing if we consider the coordinates of pixels in a monitor). The same applies to
processes, where the box is the one that encloses the process ellipse.
## 15.8.4 Tine Thing Set Order Rule
The order of the things in the tine thing set can be based on some rule.
Order rule is a property of an ordered tine thing set, which specifies textually in the
OPD the rule or criterion according to which the things in the tine thing set are
ordered.
The Order Rule can be null, which is the default, or any other phrase written in lower-case letters.
Order Rule whose value is null means that there is no order criterion, and nothing (if there is no order) or
“ordered” (if there is order but the rule is trivial, such as the order of the days of the week) is written next
to the handle.
If there is an ordering rule that needs to be specified, the phrase “ordered by” rather than “ordered” is
used in the OPD next to the fork, and recorded below it is the
order criterion itself. For example, the
OPD in Fig. 15.15 indicates an ordered tine set with the order rule “river flow”, implying that the countries
are ordered by following the flow of the Danube River.

### Figure 15.15
Order criterion marked by the phrase “ordered by”, followed by the order criterion river flow” below it “
## 15.9 Summary
A participation constraint is a number or a mathematical expression recorded along a link next
to an object, which denotes the multiplicity (number of repetitions) of that object in that relation.
A structural participation constraint is a participation constraint recorded along a structural
link.
A procedural participation constraint is a participation constraint recorded along a procedural
link.
The default participation constraint is 1, and it is implicit.
A parameterized participation constraint is a participation constraint which is a mathematical
expression with one or more parameters.
A range participation constraint is a participation constraint with lower and upper bounds, each
possibly an expression, on the number of possible objects that can take part in the relation.
Source participation constraint is the participation constraint on the source side of the
(structural or procedural) link.
Destination participation constraint is the participation constraint on the destination side of the
(structural or procedural) link.
Cardinality is a property of a link whose value depends on the combination of the source and
destination participation constraints of the structural link.
The distributive law of structural relations: If A, B, and C are all objects or are all processes,
and is a structural relation, then A B, A C A (B, C ).
A fork is a combination of two or more structural links with the same semantics expressed by the
same tag.
Handle is the joint origin-side edge of the fork.
Tine is the split destination-side edge of the fork.
Handle thing is the thing linked to the handle of the fork link

Participation Constraints and Forks
Tine thing is a thing linked to a tine of the fork link.
Object fork is a set of objects connected by a fork.
Process fork is a set of processes connected by a fork.
The tine thing set of a fork is the set of all the things linked to the tines of the fork.
Fork degree is a fork property that specifies the size of the tine object set.
Fork comprehensiveness is a Boolean fork property which is positive if all the things in the tine
thing set are attached to the fork’s handle and negative otherwise.
Orderability is a Boolean fork property which is positive if the things in the tine thing set are
ordered and negative otherwise.
Order criterion is a property of an ordered tine thing set, which specifies textually in the OPD
the criterion according to which the things in the tine thing set are ordered.
## 15.10 Problems
1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 11. 12. 13. Model a system in which three cranes are used to lift an elevator to the top of a new building.
Change the objects, the tag in the tagged structural relations, and the participation constraints in
each of the four OPDs in in Fig. 15.5 such that meaningful sentences are obtained.
Select from Table 15.2 3 of the 16 cardinality types. For each, create and OPD that demonstrates
it.
Model a library comprised of n shelves, each of which can hold up to 20 books.
For the library in the previous question, model a process Maximal Number of Books Computing
that does what its name says.
Model two object forks with objects and two process forks, and write their OPL paragraphs.
For each fork in the previous problem, draw an OPD assuming that the distributive law of
structural relations does not exist. Which option is more compact? Why?
Specify the tine thing set and the fork degree for each one of the four forks in the previous
problem.
For one object fork or one process fork from the previous question add a new fork whose tine
thing set has a non-empty intersection with the old fork.
Add a non-comprehensiveness fork symbol where appropriate in the forks of the previous
question.
Draw the comprehensive fork of the two forks from the previous question.
Is there any potential order criterion in any one of the four forks from the first question? If so,
pick one and add to it is orderability criterion. If not—design a new ordered fork and specify its
order criterion.
Write the OPL sentences for all the OPDs in your answers to the questions in this chapter.
