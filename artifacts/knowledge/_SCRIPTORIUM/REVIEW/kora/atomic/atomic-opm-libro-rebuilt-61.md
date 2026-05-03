---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-61
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
      n_propositions: 55
      segmented: true
      segment_role: segment
      segment_index: 61
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-61
---

# Atomic opm-libro-rebuilt - Segmento 61

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `55`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `61/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 19 States and Values / 19.8.2 Using Processes to Determine Compound States

- **P3152** · `fact` · Processes can be used to determine compound states. In Fig. · [src:S01:L8038-L8046](../../../INBOX/opm-libro.txt#L8038-L8046)
- **P3153** · `constraint` · 19.17, Table Lamp, which can have the compound states dark and lit, consists of three parts: Switch, Power Plug, and Light Bulb, each having two states. · [src:S01:L8038-L8046](../../../INBOX/opm-libro.txt#L8038-L8046)
- **P3154** · `fact` · Some of the points in the object’s state space are not feasible, for example: (Table Lamp = dark, Switch = on, Power Chord = plugged in, Light Bulb = intact). · [src:S01:L8038-L8046](../../../INBOX/opm-libro.txt#L8038-L8046)
- **P3155** · `fact` · The processes determine what points in the object state space are feasible. · [src:S01:L8038-L8046](../../../INBOX/opm-libro.txt#L8038-L8046)
- **P3156** · `fact` · For two dimensions, this can be also presented in a table, possibly as a two- dimensional array inside an in-zoomed object. · [src:S01:L8038-L8046](../../../INBOX/opm-libro.txt#L8038-L8046)
- **P3157** · `fact` · However, a table does not express the reasoning behind the feasibility or infeasibility of each point. · [src:S01:L8038-L8046](../../../INBOX/opm-libro.txt#L8038-L8046)

## opm libro · Chapter 20 Generalization and Instantiation

- **P3158** · `fact` · As this term is most commonly used, a generalization is an “all” statement, to the effect that all objects of a certain general kind possess a certain property. · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3159** · `constraint` · Lowe (1983) While discussing aggregation and exhibition, we talked about entire groups of objects or processes—any scientific paper, any employee, any running. · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3160** · `fact` · However, what if we wanted to consider the example of a specific paper, written by a certain John Doe? · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3161** · `fact` · Or if we wanted to consider a group of employees, namely managers, who receive a certain salary out of the range of salaries available for the company? · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3162** · `fact` · Perhaps we would like to discuss running in a marathon, as opposed to just any kind of running? · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3163** · `fact` · We need to be able to pay particular attention to a specialized group, which belongs to a more general group, or even a specific instance out of a class of objects. · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3164** · `fact` · As its name clearly points out, generalization-specialization is the relation between a general and a special case of a thing. · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3165** · `fact` · Classification-instantiation is the relation between a class of things and a unique instance from the class. · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)
- **P3166** · `fact` · Since these two concepts are important to systems modeling, we consider them two of the four fundamental relations; and since they are intimately related, they are discussed and explained together in this chapter. · [src:S01:L8092-L8105](../../../INBOX/opm-libro.txt#L8092-L8105)

## opm libro · Chapter 20 Generalization and Instantiation / 20.1 Generalization-Specialization: Introduction

- **P3167** · `constraint` · Let us first consider several simple examples to set the stage for discussing generalization-specialization, or “gen-spec.”1 Person in the left OPD of Fig. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3168** · `constraint` · 20.1 is the general case, while Man and Woman are its special cases. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3169** · `requirement` · Other examples are “Dog and Cat are Pets.”, “Pascal, Java, and C++ are Programming Languages.”, 278 Generalization and Instantiation “Airplane and Car are Vehicles.”, “Flying and Sailing are Transporting.”, and “Ketchup and Mustard are Condiments.” Generalization-specialization is a fundamental structural relation between a general thing G and one or more things S1, S2, … Sn, which are specializations of G. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3170** · `fact` · An alternative way of expressing the OPL sentence might have been “Digital Camera and Analog Camera specialize Cameras.” However, sticking to the principle of keeping the OPL language as natural and as simple as possible, OPL uses the clearer and more intuitive reserved phrases “is a” (or “are” for plural) rather than “specializes” or “specialize” for denoting the gen-spec relation from the reverse, or bottom-up direction, from the specialized thing—the specialization—to the generalizing thing—the general. Any number of specializations is possible. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3171** · `fact` · The following example is of three specializing objects. Cucumber is a Vegetable. Tomato is a Vegetable. Carrot is a Vegetable. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3172** · `fact` · We combine the three specialization sentences above into one: Cucumber, Tomato, and Carrot are Vegetables. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3173** · `fact` · Generalization-specialization is a transitive relation, meaning that if A is a B, and B is a C, then A is a C. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3174** · `fact` · More concretely, consider the following two specialization sentences: Tomato is a Vegetable. Vegetable is a Plant. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3175** · `fact` · Since generalization-specialization is transitive, we can deduce that: Tomato is a Plant. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3176** · `fact` · Generalization-specialization means that a refineable, the general, generalizes two or more refinees, which are specializations of the general. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3177** · `fact` · The generalization-specialization relation binds one or more specializations with the same perseverance as the general, such that both the general and all its specializations are objects (in metamodel terms, if the Thing’s Perseverance is persistent) or the general and all its specializations are processes (if the Thing’s Perseverance is transient). · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3178** · `fact` · Graphically, an empty triangle with its apex connecting by a line to the general and the specializations connecting by lines to the opposite base denotes the generalization-specialization relation link. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3179** · `fact` · UML and SysML use a white (blank) triangle to denote generalization-specialization, (as in OPM), but in UML and SysML the triangle’s tip is linked directly to the generalizing object, and the white triangle base is not necessarily horizontal, but rather perpendicular to the line connected to the specialization. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3180** · `requirement` · Moreover, similar to the case with aggregation, since there is no fork in UML, each specialization in a UML class diagram and SysML block definition diagram must have its own symbol. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)
- **P3181** · `fact` · Since UML and SysML do not have processes in class diagrams, the aggregation and specialization relations in UML and SysML apply to objects only. · [src:S01:L8107-L8153](../../../INBOX/opm-libro.txt#L8107-L8153)

## opm libro · Chapter 20 Generalization and Instantiation / 20.1.1 Process Specialization

- **P3182** · `fact` · Not only objects are subject to generalization-specialization. · [src:S01:L8155-L8171](../../../INBOX/opm-libro.txt#L8155-L8171)
- **P3183** · `constraint` · The same relation applies to processes as well. Figure 20.2 shows two simple examples. · [src:S01:L8155-L8171](../../../INBOX/opm-libro.txt#L8155-L8171)
- **P3184** · `constraint` · In order to comply with the English grammar, the process specialization sentence is slightly different than the (object) specialization sentence in that (1) instead of the reserved phrase “is a,” the reserved word “is” is used, and (2) while the generalizing object is plural, as in Vegetables, in multiple process specialization sentence it is singular, as in Cooking. · [src:S01:L8155-L8171](../../../INBOX/opm-libro.txt#L8155-L8171)
- **P3185** · `fact` · Consider the following OPL sentences. specialized links between these specializations Specializations of objects and processes can be combined to specify specialized procedural links between the object and process specializations. · [src:S01:L8155-L8171](../../../INBOX/opm-libro.txt#L8155-L8171)
- **P3186** · `constraint` · Figure 20.3 shows on the left a pattern of Cooking, which uses Cooking Tool as an instrument and yields Food. · [src:S01:L8155-L8171](../../../INBOX/opm-libro.txt#L8155-L8171)
- **P3187** · `fact` · On the right are three specializations of Cooking Tool, Cooking, and Food. · [src:S01:L8155-L8171](../../../INBOX/opm-libro.txt#L8155-L8171)
- **P3188** · `constraint` · Each Cooking Tool specialization is an instrument of a specialization of Cooking, yielding a specialization of Food. 280 Generalization and Instantiation · [src:S01:L8155-L8171](../../../INBOX/opm-libro.txt#L8155-L8171)

## opm libro · Chapter 20 Generalization and Instantiation / 20.1.2 Link Under- and Over-Specification

- **P3189** · `fact` · Link under-specification would occur if on the right OPD of Fig. · [src:S01:L8173-L8180](../../../INBOX/opm-libro.txt#L8173-L8180)
- **P3190** · `constraint` · 20.3 we would have left the two links as in the OPD on the left and not specify the six procedural links on the right. · [src:S01:L8173-L8180](../../../INBOX/opm-libro.txt#L8173-L8180)
- **P3191** · `fact` · This would mean that any tool can be used for any cooking. · [src:S01:L8173-L8180](../../../INBOX/opm-libro.txt#L8173-L8180)
- **P3192** · `fact` · Link over-specification would occur if, in addition to the six procedural links in the OPD on the right, we would have added the two links as in the OPD on the left. Both should be avoided. · [src:S01:L8173-L8180](../../../INBOX/opm-libro.txt#L8173-L8180)
- **P3193** · `fact` · In under-specification, leaving the single instrument link from Cooking Tool to Cooking on the right means that any Cooking Tool could be considered as instrument of any Cooking process and to yield any Food. · [src:S01:L8173-L8180](../../../INBOX/opm-libro.txt#L8173-L8180)
- **P3194** · `fact` · On the other hand, in over-specification, the two generalizing links, left along with the six specialized links, become redundant. · [src:S01:L8173-L8180](../../../INBOX/opm-libro.txt#L8173-L8180)
- **P3195** · `fact` · Under- and over-specification can occur also with structural links. · [src:S01:L8173-L8180](../../../INBOX/opm-libro.txt#L8173-L8180)

## opm libro · Chapter 20 Generalization and Instantiation / 20.2 Inheritance

- **P3196** · `fact` · The most prominent and immediate benefit gained from using the gen-spec relation is the inheritance it induces. · [src:S01:L8182-L8200](../../../INBOX/opm-libro.txt#L8182-L8200)
- **P3197** · `fact` · Inheritance is assignment of OPM elements—things and links—of a general to its specializations. · [src:S01:L8182-L8200](../../../INBOX/opm-libro.txt#L8182-L8200)
- **P3198** · `fact` · In OO design, the meaning of inheritance is that attributes, and to some extent also operations, of the generalizing object are inherited to the specialized objects. · [src:S01:L8182-L8200](../../../INBOX/opm-libro.txt#L8182-L8200)
- **P3199** · `fact` · In OPM, the effect of inheritance is stronger, as, in addition to inheriting features and parts, it includes inheriting structural and procedural links, as well as states. · [src:S01:L8182-L8200](../../../INBOX/opm-libro.txt#L8182-L8200)
- **P3200** · `fact` · Through the generalization-specialization relation, each specialization inherits from the general each of the following four kinds of inheritable elements: all the parts of a general from its aggregation-participation link, all the features of the general from its exhibition-characterization link, all the tagged structural links to which the general connects, and all the procedural links to which the general connects. · [src:S01:L8182-L8200](../../../INBOX/opm-libro.txt#L8182-L8200)
- **P3201** · `fact` · OPM provides the opportunity for multiple inheritance by allowing a thing to inherit from more than one general each of the refinees—the four inheritable elements (parts, features, tagged structural links, and procedural links) that exist for that general. · [src:S01:L8182-L8200](../../../INBOX/opm-libro.txt#L8182-L8200)
- **P3202** · `fact` · The modeler may override any of the parts of the general, which are by default inherited by the specialization, by specifying for any participant inherited from a general, a specialization of that participant with a different name and a different set of states. · [src:S01:L8182-L8200](../../../INBOX/opm-libro.txt#L8182-L8200)

## opm libro · Chapter 20 Generalization and Instantiation / 20.2.1 Creating a General from Candidate Specializations

- **P3203** · `fact` · To create a general from one or more candidate specializations, the inheritable elements common to each of the candidates migrated “upward” to a generalizing thing. · [src:S01:L8202-L8215](../../../INBOX/opm-libro.txt#L8202-L8215)
- **P3204** · `requirement` · The manipulation of inheritable elements shall be as follows: Combine all of the common features and common participants of the specializations into one newly created general; · [src:S01:L8202-L8215](../../../INBOX/opm-libro.txt#L8202-L8215)
- **P3205** · `fact` · Connect the new general using the generalization-specialization relation link to the specializations; · [src:S01:L8202-L8215](../../../INBOX/opm-libro.txt#L8202-L8215)
- **P3206** · `fact` · Remove from the specializations all of the common features and common parts that the specializations now inherit from the new general; and Migrate any common tagged structural link and any common procedural link that connects a thing T to each one of the specializations from the specializations to the general, such that there will be a single link from T to the general. · [src:S01:L8202-L8215](../../../INBOX/opm-libro.txt#L8202-L8215)
