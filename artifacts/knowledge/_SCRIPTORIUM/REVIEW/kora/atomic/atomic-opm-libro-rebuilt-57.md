---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-57
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
      producer: urn:kora:skill:atomize:1.0.0
      source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
      n_propositions: 59
      segmented: true
      segment_role: segment
      segment_index: 57
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-57
---

# Atomic opm-libro-rebuilt - Segmento 57

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `59`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `57/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 18 Exhibition-Characterization / 18.8.2 Mode

- **P2927** · `fact` · Some attributes are qualitative while others are quantitative. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2928** · `fact` · We have seen the example of the attribute Shape of House, where possible values can be round, square, and rectangular. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2929** · `fact` · These values cannot be quantified by a numeric value. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2930** · `fact` · They are just qualitatively different from each other. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2931** · `fact` · We say therefore that Shape is a qualitative attribute. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2932** · `fact` · Other examples of qualitative attributes include Mood, with states happy, sad, angry, etc., Health, with states healthy and sick, and Marital Status, with states single, married, divorced, etc. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2933** · `fact` · Examples of quantitative attributes are Weight [Kg] and Height [m]. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2934** · `fact` · As these examples show, quantitative attributes need to be followed by the unit of measurement in brackets, as discussed in Chap. · [src:S01:L7530-L7536](../../../INBOX/opm-libro.txt#L7530-L7536)
- **P2935** · `constraint` · Since an attribute can be qualitative or quantitative, qualitative and quantitative are values of a property of Attribute called Mode. An attribute is quantitative if its values are numerical or parametric. An attribute is qualitative if its values are non-numerical. An operation is quantitative if it transforms a quantitative attribute, otherwise it is quantitative. Mode is a property of a feature that determines whether it is qualitative (the default) or quantitative. The definition of numerical here includes parametric—a parameter is a symbol that stands for some numerical value. We could assign numeric values, or “codes” to values of a qualitative attribute, for example, single = 1; married = 2. Indeed, this was a common practice in early information processing systems and is still often the practice, especially when data has to be analyzed statistically. However, semantically this does not render a qualitative attribute quantitative. An example of quantitative operations is Height Measuring, which creates a value for the quantitative attribute Height. Another example is Weighing, which creates a value for the quantitative attribute Weight. Section 13.10 discusses how to model setting or updating values using value-specified procedural links. · [src:S01:L7537-L7552](../../../INBOX/opm-libro.txt#L7537-L7552)

## opm libro · Chapter 18 Exhibition-Characterization / 18.8.3 Touch: A Property of a Quantitative Attribute

- **P2936** · `fact` · A quantitative attribute can be hard or soft, depending on whether it can be computed from other attributes or not. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2937** · `fact` · For example, Date of Birth of a Person is a hard attribute, while Age of Person is a soft attribute. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2938** · `fact` · By knowing the Date of Birth of a Person and the current value of Date, Age of Person can be computed. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2939** · `fact` · As another example, the Weight of each part of Airplane is a hard attribute, while the total Weight of Airplane is a soft attribute since it can be computed by summing the weights of the individual parts. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2940** · `fact` · The name of the property of Attribute whose values are hard and soft is Touch. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2941** · `fact` · A quantitative attribute is hard if its value cannot be deduced or computed from other attributes. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2942** · `fact` · A quantitative attribute is soft if its value can be deduced or computed from other attributes. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2943** · `fact` · Touch is a property of a quantitative attribute which determines whether it is hard (the default) or soft. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2944** · `fact` · Deciding whether a soft attribute should be pre-computed has practical implications during the detailed design stage of an information system. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2945** · `fact` · Pre-computed values can be stored for quick response time at the cost of storage space. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2946** · `fact` · Alternatively, soft attributes can be computed on demand, saving space but also delaying the response time of the information system. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)
- **P2947** · `fact` · This is a common tradeoff in databases, where the need for high response speed is weighed against storage overhead. · [src:S01:L7556-L7572](../../../INBOX/opm-libro.txt#L7556-L7572)

## opm libro · Chapter 18 Exhibition-Characterization / 18.8.4 Emergence

- **P2948** · `fact` · Depending on whether a feature is exhibited only by the object as a whole or only by one or more (but not all) of its parts, a Feature (an Attribute or an Operation) can be inherent or emergent. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2949** · `fact` · A feature of an object is inherent if a least one of the object’s parts exhibits it. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2950** · `fact` · A feature of an object is emergent if no one of the object’s parts alone exhibits it. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2951** · `fact` · Emergence is a property of an object whose values are inherent (the default) and emergent. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2952** · `fact` · To understand the difference between emergent and inherent features, consider Airplane’s attribute Weight and its operation Flying. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2953** · `fact` · Weight of Airplane is the sum of the individual Weight values of each one of the parts that make up the Airplane. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2954** · `fact` · Flying, on the other hand, was not an operation that any part of Airplane could exhibit on its own. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2955** · `fact` · Rather, this feature emerges from the unique ensemble of the parts of Airplane that endows Airplane with the ability to carry out the Flying operation. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2956** · `fact` · Hence, Flying is an emergent feature (operation in this case) of Airplane, while Weight is an inherent feature (attribute in this case) of the Airplane. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2957** · `fact` · In systems, operations are frequently emergent, because systems are built with the intent of achieving some function that is not localized in or achievable by any part of the system alone. Flying of Airplane is an excellent example. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2958** · `constraint` · Bar-Yam (1997) distinguishes between simple and complex systems and claims that complexity can emerge from a collection of simple parts that comprise a system. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2959** · `fact` · The converse can be true as well: a system composed of complex parts may exhibit simple behavior at a larger scale. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)
- **P2960** · `fact` · For example, planet Earth is a highly complex system, but when viewed from the perspective of its movement around the sun, it is relatively simple, pointing to the relativity of the term complexity. · [src:S01:L7574-L7595](../../../INBOX/opm-libro.txt#L7574-L7595)

## opm libro · Chapter 18 Exhibition-Characterization / 18.8.5 The Link Homogeneity Property

- **P2961** · `fact` · The property that specifies whether a link connects things with the same Perseverance—static (persistent, defining an object) or dynamic (transient, defining a process) is called Homogeneity. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2962** · `fact` · The values of Homogeneity are homogeneous, which applies if the two things that the link connects exhibit the same Perseverance (either both are objects or both are processes), and non-homogeneous otherwise (one is an object and the other—a process). · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2963** · `fact` · Since most structural links are between two objects or between two processes, the Homogeneity value homogeneous is the default for structural links. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2964** · `fact` · Conversely, since most procedural links are between an object and a process, the Homogeneity value non- homogeneous is the default for procedural links. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2965** · `fact` · A link is homogeneous if it connects two things that exhibit the same perseverance value. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2966** · `fact` · A link is non-homogeneous if it connects two things that exhibit opposite perseverance values. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2967** · `fact` · Homogeneity is a property of a link whose values are homogeneous (the default for structural links) and non-homogeneous (the default for procedural links). · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2968** · `fact` · Almost all the structural links are only homogeneous: they either connect two objects or two processes. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2969** · `fact` · The only exceptional structural link that is Exhibition-Characterization, which can be both homogeneous (in case it connects an object with an attribute or a process with an operation) or non- homogeneous (in case it connects an object with an operation or a process with an attribute). · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2970** · `fact` · All the other structural links, and in particular the remaining three fundamental structural relations, are homogeneous. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2971** · `fact` · Analogously, almost all the procedural links are non-homogeneous, as they connect an object to a process. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2972** · `fact` · The only procedural links that are homogeneous are the invocation link discussed in Sect. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)
- **P2973** · `constraint` · 10.10.3 and the overtime and undertime exception links discussed in Chap. 22. · [src:S01:L7597-L7618](../../../INBOX/opm-libro.txt#L7597-L7618)

## opm libro · Chapter 19 States and Values

- **P2974** · `fact` · The Caterpillar … got down off the mushroom and crawled away into the grass merely remarking as it went, “One side will make you grow taller, and the other side will make you grow shorter.” Alice in Wonderland. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2975** · `constraint` · Lewis Carroll, 1899 To be able to talk explicitly about a change in an object over time, we assign to it a number of possible, “legal” states. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2976** · `fact` · Hence, a state is a situation an object can be at. States and values add expressiveness to OPM. A value is a state of an attribute. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2977** · `fact` · As such, it is a specialization of state: Whereas objects can have states, only states of attributes, which are objects that describe other object, are called values. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2978** · `fact` · States and values enable modeling change in an object while that object retains its identity. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2979** · `fact` · We have been using the terms states and values quite intuitively since the early chapters of this book. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2980** · `fact` · If objects and processes are the building blocks of OPM, and links are the mortar, states can be considered as the finish of the house: the paint job, the furniture, and architectural elements. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2981** · `fact` · At any time in the life of the object, when no process is acting on it, that object is at one of its states. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2982** · `fact` · Cause and effect are tightly linked with the concepts of change of state over time. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)
- **P2983** · `fact` · This chapter formalizes the concepts of states and values, and shows how they can be used to enhance model expressiveness. · [src:S01:L7671-L7685](../../../INBOX/opm-libro.txt#L7671-L7685)

## opm libro · Chapter 19 States and Values / 19.1 State Defined

- **P2984** · `fact` · To be able to talk explicitly about a change in an object, we assign to it a number of mutually exclusive situations, positions, or values, which we refer to as states. · [src:S01:L7687-L7690](../../../INBOX/opm-libro.txt#L7687-L7690)
- **P2985** · `fact` · A State is a situation or position at which an object can exist for some period of time during its existence. · [src:S01:L7687-L7690](../../../INBOX/opm-libro.txt#L7687-L7690)
