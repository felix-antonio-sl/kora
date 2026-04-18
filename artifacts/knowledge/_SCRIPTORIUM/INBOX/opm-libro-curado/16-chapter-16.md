# Chapter 16 Fundamental Structural Relations
Four structural relations are most prevalent and play an especially important role in specifying and
understanding systems. Termed the fundamental structural relations, these relations are:
Aggregation-participation, which denotes the relation between a whole and its parts,
Exhibition-characterization, which denotes the relation between an exhibitor—a thing exhibiting a
one or more features (attributes and/or operations) and the things that characterize the exhibitor,
Generalization-specialization, which denotes the relation between a general thing and its
specializations, giving rise to inheritance, and
Classification-instantiation, which denotes the relation between a class of things and an instance of
that class.
This chapter is devoted to discussing these structural relations, while subsequent chapters deal with
each of them separately.
## 16.1 Relation Symbols and Participants
Due to the prevalence of the fundamental structural relations, in order to avoid writing their tags over and
over again and make them readily graphically identifiable, each one of the four fundamental structural
relations is assigned with a unique triangular symbol. Table 16.1 lists the fundamental structural relations
with their respective triangular symbols as they appear linked in an OPD, and the OPL sentence that
corresponds to each OPD. While all the OPD examples are of objects linked to objects (except for
Operation B), being structural relations, the four fundamental structural relations exist between processes
and can be depicted also linking processes. To begin, we next define refineable and refinee.
Refineable is a thing amenable to refinement via a fundamental structural relation.
Each Refineable is the ancestor (parent) of the two-level hierarchy induced by the fundamental
structural relation. Hence, as Table 16.1 presents in brackets in the leftmost column, a Refineable can be a
Whole, an Exhibitor, a General, or a Class. Each of the four refineables corresponds to one of the four
fundamental structural relation.
Refinee is a thing that refines a refineable.
Each Refinee is the descendant (child) of the two-level hierarchy induced by the fundamental
structural relation. Table 16.1 presents in brackets in the second-from-left column the four Refinees
corresponding to the refineables in the structural relations: a Part, a Feature, a Specialization, and an
Instance. As we discuss later, Feature, in turn, specializes into Attribute (a structural feature) and
Operation (a procedural feature).

D. Dori, Model-Based Systems Engineering with OPM and SysML, DOI 10.1007/978-1-4939-3295-5_ 16

Fundamental Structural Relations
Table 16.1 The fundamental structural relation names, OPD symbols, and OPL sentences
Structural Relation Name
[Participant Name] OPL Sentence(s)
Graphic Symbol
with OPD usage
Forward
[Refineable]
Backward
[Refinee] Forward Backward
Whole
Aggregation
[Whole]
Participation
[Part]
Whole consists of
Part A and Part B.
Part A Part B
Exhibition
[Exhibitor]
Characterization
[Feature:
Attribute or
Operation]
Exhibitor
Attribute A
Operation B
Exhibitor exhibits
Attribute A as
well as Operation
B.
General
Thing
Generalization
[General]
Specialization
[Specialization]
Specialization
A
Specialization
B
Specialization A
and
Specialization B
are General
Things.
Class
Classification
[Class]
Instantiation
[Instance]
Instance A Instance B
Instance A and
Instance B are
instances of
Class.
## 16.2 Relation Names and OPL Sentences
The name of each fundamental structural relation consists of a pair of dash-separated words.1 As Table
## 16.1 presents, the first word in each such pair is the forward relation name, i.e., the name of the relation
as seen from the viewpoint of the thing up in the hierarchy—the ancestor, or parent—while looking down
the hierarchy. The second word is the backward (or reverse) relation name, i.e., the name of the relation
as seen from the viewpoint of the thing down in the hierarchy—the descendant, or child—of that relation
while looking up the hierarchy.
The first fundamental structural relation, aggregation-participation, denotes the relation between a
whole thing and its parts. Exhibition-characterization denotes the relation between a thing and its features
(attributes and operations). Generalization-specialization denotes the relation between a general thing and
its specializations. Finally, classification-instantiation denotes the relation between a class of things and
the instances of that class.
Since the full names of these relations are rather long, each has a short version, which is either the
forward or backward structural relation name only. The short name, denoted in Table 16.1 by bold letters,
1The pair of words “dash-separated” is a pair of dash-separated words (pun intended).

is selected to be the more meaningful of the two: Aggregation, Characterization, Generalization, and
Classification.
As Table 16.1 shows, all the four fundamental structural relation symbols are equilateral triangles
linked via orthonormal polylines, i.e., lines whose segments are parallel to either one of the diagram axes
(also called Manhattan lines). The tip of the triangle is linked through an orthonormal polyline to the root
of the hierarchy tree—the aggregate or whole in our case (Whole, in the first row of Table 16.1, for
example). The triangle’s base is linked through other orthonormal polylines to each one of the parts of the
aggregate (Part A and Part B in our example). The fact that the links of the fundamental structural
relations run horizontally or vertically but not diagonally (like all the procedural links) helps differentiate
them visually from procedural links. Using different colors for different links that cross each other (which
should be avoided as much as possible) is also helpful in crowded OPDs.
The OPL sentences of the fundamental structural relations are also either in the forward or the
backward direction. The direction was similarly determined by how natural the sentence sounds in plain
English. The forward direction is used for aggregation and characterization:
Whole consists of Part A and Part B.
Exhibitor exhibits Attribute A, as well as Operation B.
The backward direction is used for generalization and classification:
Specialization A and Specialization B are General Things.
Instance A and Instance B are instances of Class.
As usual, the multiple versions of these two OPL sentences, which include three or more refinees, are:
Specialization A, Specialization B, and Specialization C are General Things.
Instance A, Instance B, and Instance C are instances of Class.
## 16.3 Structural Hierarchies, Transitivity, User-Defined Symbols
The special graphic symbols assigned to the four fundamental structural relations due to their prevalence
and usefulness do not make them particularly special; diagramming convenience, avoiding multiple tags,
and ease of diagram reading have motivated the introduction of these symbols. Yet, the first three of these
four relations do have in common the hierarchy and transitivity they induce (examples are given in the
relevant chapters that follow, discussing each relation separately):
In Aggregation, a part can be the whole of yet smaller parts, creating an aggregation-participation
hierarchy. This hierarchy is transitive: If A consists of B (and other parts) and B consists of C (and other
parts), then A (indirectly) consists of C (and other parts).
In Characterization, a feature (attribute or operation) can be the exhibitor of lower-level features,
creating an exhibition-characterization hierarchy. This hierarchy is transitive: If A exhibits B and B
exhibits C, then A (indirectly) exhibits C.
In Generalization, a specialization can generalize lower-level specializations, creating a
generalization-specialization hierarchy. This hierarchy is transitive: If A generalizes B (and possibly other
specializations) and B consists of C (and possibly other specializations), then A (indirectly) generalizes C
(and possibly other specializations). With respect to Classification, as explained in Chap. 20, an instance

Fundamental Structural Relations
can only be a leaf in a generalization-specialization hierarchy. Therefore, the classification-instantiation
relation cannot be transitive.
Complex hierarchies can be created by mixing combinations of the four relations. Following this idea
of denoting a frequently used relation by a special symbol, it is possible to add a symbol for one or more
structural relations that are widely used within a specialized domain. Consider an example from the
domain of chemical laboratory testing of industrial lots. In this domain, the phrase “is a sample of” is a
very prevalent and useful structural relation between a sample and the lot from which it was taken. A
dedicated graphic symbol and a corresponding reserved phrase “is a sample of” can be introduced in this
domain to enable quicker and easier modeling. The symbol selected in a real case in work done at ISCAR
Ltd.—an enterprise operating in the domain of metal cutting tool manufacturing by sintering
technology—was a piece cut out of a cake, symbolizing that the taste of the piece of cake—the sample—
is the same of the entire cake—the lot from which the sample was taken. The four fundamental structural
relations are so central to conceptual modeling that the next chapters are devoted to discussing each one
of them.
## 16.4 Summary
Four structural relations are fundamental and therefore are assigned graphic symbols.
Refineable is a thing amenable to refinement via a fundamental structural relation.
Refinee is a thing that refines a refineable.
The four fundamental structural relations are:
Aggregation-participation;
Exhibition-characterization;
Generalization-specialization; and
Classification-instantiation.
Each fundamental structural relation has a unique triangular symbol.
The symbol replaces the tag, making the OPD more graphic and more quickly comprehensible.
Each fundamental structural relation induces a hierarchy.
Complex hierarchies can be created by mixing the four relations.
In certain domains, additional structural relations might be fundamental and user-defined dedicated
symbols can be allocated for them.
## 16.5 Problems
1. 2. 3. For each thing in Table 16.1 indicate whether it is a refineable or a refinee.
For each OPD in Table 16.1 draw an alternative OPD without using a fundamental relation.
For each OPL sentence in Sect. 16.2 provide a concrete OPL example and its corresponding
OPD.
Having laid down in Part II the fundamentals and foundations of model-based systems engineering in
both OPM and SysML, Part III goes to the heart of conceptual modeling. In the first four chapters of this
Part, we delve into the details and usage of each one of the four fundamental structural relations. Chapters
## 17 and 18 discuss aggregation-participation and exhibition-characterization, respectively. Chapter 19 is
about states and values, concepts that are needed for the two remaining fundamental structural relations—
generalization-specialization and classification-instantiation, both elaborated on in Chap. 20. Chapter 21
concerns complexity management. It defines and describes the four refinement and abstraction
mechanisms of OPM while also discussing complexity management in SysML. Chapter 22 is about OPM
operational semantics and control links—the way control is managed during execution of the system. In
Chap. 23 we specify how to model logical operators and probabilities. Finally, Chap. 24 is an overview of
ISO 19450 Publically Available Specification (PAS)—Automation Systems and Integration—Object-
Process Methodology, adopted by the International organization for Standardization in 2014.
