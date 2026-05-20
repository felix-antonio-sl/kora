---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-54
  provenance:
    created_by: atomize
    created_at: '2026-04-18'
    source: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
version: 1.0.0
status: draft
tags:
- atomic
- knowledge
- opm-libro-rebuilt
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:artefacto:atomize
      source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
      n_propositions: 50
      segmented: true
      segment_role: segment
      segment_index: 54
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-54
---

# Atomic opm-libro-rebuilt - Segmento 54

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `50`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `54/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 18 Exhibition-Characterization / 18.3 Features in UML and SysML Versus OPM

- **P2757** · `fact` · Attributes and operations are concepts that exist also in the object-oriented (OO) approach. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2758** · `fact` · In OO terminology, an attribute is also referred to as a data member, while an operation is also referred to as a method or a service. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2759** · `fact` · All these words are meant to express “something that the object can do” or “a way in which the object behaves.” In traditional procedural third generation programming languages, operation is also referred to as a function, a procedure, or a routine. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2760** · `constraint` · Table 18.1 summarizes the definitions of attribute and operation as specializations of feature along with similar concepts in OO and traditional programming languages. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2761** · `constraint` · Table 18.1 The specializations of thing and feature by perseverance and similar concepts in OO and traditional programming languages Perseverance value Thing Feature OO similar concepts Traditional similar concepts persistent (static) Object Attribute Data member Variable, Parameter transient (dynamic) Process Operation Method, Service Procedure, Routine, Subroutine, Function, OPM treats features as things that have their own right of existence, regardless of the fact they may also characterize higher-level things. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2762** · `fact` · While aggregation-participation and generalization-specialization are recognized relations in SysML (as in UML) and have their own symbols (black or white diamond for the former, white triangle for the latter), exhibition-characterization is not an explicit relation and does not have a symbol. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2763** · `fact` · Rather, an attribute is recognized as such in UML by its location in the second of the three vertically-arranged compartments that comprise the UML object class symbol. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2764** · `requirement` · In SysML there can be an arbitrary number of compartments in a block, so each compartment must be labeled. For example, in Fig. 18.2, the label is “values”. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2765** · `fact` · Paradoxically, although OPM does not attempt to be “purely” object-oriented, it is more object- oriented in its treatment of characterization than the OO paradigm. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2766** · `fact` · In OO, attributes and methods are encapsulated, or embedded, within objects. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2767** · `fact` · Are attributes not objects, but rather “different animals” that reside within the object? · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2768** · `fact` · If an attribute is not an object, then what is it? · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2769** · `fact` · Does the world consist not only of objects but also of attributes (and methods)? · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2770** · `definition` · OPM does not encounter this dilemma, since it defines feature generically as a thing that describes a thing and as one that specializes into an attribute—an object—and an operation—a process. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2771** · `constraint` · To demonstrate the problem caused by not treating attributes as objects, consider a “classical” example of Name and Address as attributes of the object class Person, and Moving as an operation of Person. 2 As Fig. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2772** · `constraint` · 18.2 shows on the left, in SysML this is done by assigning a title to each compartment. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2773** · `fact` · The top compartment has the «Block» stereotype title, which is analogous to Object in UML and OPM, with the name of the block, Person, underneath it. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2774** · `fact` · Below this top compartment are the “values” (attributes) compartment, with Name and Address as the values, and at the bottom is the operations compartment, with Moving as the listed operation. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2775** · `fact` · In UML and many of its predecessors, such as Object Modeling Technique, OMT (Rumbaugh et al. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2776** · `constraint` · 1991) the attributes and operations are listed always in the second and third class box compartments, respectively, so no titles are needed. On the right hand side, Fig. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2777** · `constraint` · 18.5 shows the corresponding OPM notation: Name and Address are separate objects, and Moving is a process. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2778** · `fact` · Since Name and Address are linked to Person with the exhibition-characterization symbol, they are also attributes of Person. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2779** · `fact` · For the same reason, Moving is an operation of Person. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2780** · `fact` · A side benefit of this notation is that we can connect Moving to Address with an effect link to denote the fact that Moving has an effect on the Address of Person, already combining structure and behavior in this simple OPD. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2781** · `fact` · Outside the context of Person, both Name and Address are bona fide objects in their own right. Moreover, as shown in Fig. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2782** · `constraint` · 18.3, each one of them consists of parts: Name consists of First Name followed by Last Name; · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)
- **P2783** · `fact` · Address consists of Street, City, Zip Code, State and Country, in that sequence. · [src:S01:L7227-L7278](../../../INBOX/opm-libro.txt#L7227-L7278)

## opm libro · Chapter 18 Exhibition-Characterization / 18.4 OPM Thing and Feature Name Uniqueness

- **P2784** · `requirement` · Different things in an OPM model must have different names in order for them to be distinguishable and to avoid confusion. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2785** · `fact` · However, when it comes to features, which are things that describe things, it becomes difficult to come up with a different name for each feature. For example, in Fig. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2786** · `constraint` · 18.3, there is an attribute of Person called Name, but Street and City might, in turn, also have an attribute called Name. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2787** · `fact` · Hence, features of things are allowed to have the same name as features of other things. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2788** · `fact` · The uniqueness of features is maintained by adding “of Exhibitor”, where of is a reserved OPL phrase (word in this case) and Exhibitor is the name of the thing that exhibits the feature. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2789** · `requirement` · Thus, a feature of a feature shall have two “of” reserved OPL words, as in Length of Name of Person. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2790** · `fact` · The following name uniqueness OPM principle summarizes this. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2791** · `requirement` · The Thing Name Uniqueness OPM Principle Different things in an OPM model which are not features must have different names. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)
- **P2792** · `fact` · Features are distinguishable by appending to them the reserved word “of” and the name of their exhibitor. · [src:S01:L7280-L7294](../../../INBOX/opm-libro.txt#L7280-L7294)

## opm libro · Chapter 18 Exhibition-Characterization / 18.5 The Four Thing-Feature Combinations

- **P2793** · `fact` · Exhibition-characterization is unique among the structural relations in that it is the only one that allows relating objects to processes and processes to objects. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2794** · `fact` · All the other structural relations, including in particular the remaining three fundamental structural relations, allow linking things with the same perseverance value only: objects (things whose perseverance value is persistent, or static) can be linked only to objects and processes—(things whose perseverance value is transient, or dynamic) only to processes. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2795** · `fact` · Thus, objects can be parts or specializations or instances only of objects, and processes can be parts or specializations or instances only of processes. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2796** · `fact` · However, when it comes to exhibition- characterization, all the four object-process (exhibitor-feature) combinations are possible. In other words, as shown also in Fig. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2797** · `constraint` · 18.4, since both thing and its feature can be an object or a process, the 2 2 Cartesian product yields a state-space of four different combinations of a thing and the feature that characterizes it, namely, from left to right and from top to bottom in Fig. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2798** · `constraint` · 18.4: (1) an attribute of an object, (2) an operation of an object, (3) an attribute of a process, and (4) an operation of a process. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2799** · `fact` · As an example of an object-attribute combination, Address is an object in its own right, but it is also an attribute of Person, as it is one of the things that characterize it. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2800** · `fact` · As an example of an object-operation combination, Printing is a process, which is also an operation of Printer, as it is a thing that characterizes what a Printer is capable of—what its function is. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2801** · `fact` · All four combinations are discussed and further demonstrated in this section. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)
- **P2802** · `fact` · In the following subsections we elaborate on each one of these combinations. · [src:S01:L7296-L7316](../../../INBOX/opm-libro.txt#L7296-L7316)

## opm libro · Chapter 18 Exhibition-Characterization / 18.5.1 The Object-Attribute Combination

- **P2803** · `fact` · The first thing-feature combination—object and its attribute—is the customary attribute of classical OO approaches. · [src:S01:L7318-L7323](../../../INBOX/opm-libro.txt#L7318-L7323)
- **P2804** · `fact` · Here we refer to an object B2—the attribute—that characterizes (describes) a higher level object B1. Conversely, we say that B1 exhibits B2. · [src:S01:L7318-L7323](../../../INBOX/opm-libro.txt#L7318-L7323)
- **P2805** · `fact` · A few examples for such pairs of objects and their attributes are Material—Specific Weight, Person—Age, Chemical Element—Atomic Weight, Laptop— Manufacturer, Book—Author, Officer—Rank, and Dog—Breed. · [src:S01:L7318-L7323](../../../INBOX/opm-libro.txt#L7318-L7323)
- **P2806** · `constraint` · The first four of these examples are depicted in the four OPM models in Fig. 18.5. · [src:S01:L7318-L7323](../../../INBOX/opm-libro.txt#L7318-L7323)
