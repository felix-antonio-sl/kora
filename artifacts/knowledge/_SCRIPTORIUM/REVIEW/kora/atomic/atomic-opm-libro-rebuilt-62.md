---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-62
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
      n_propositions: 56
      segmented: true
      segment_role: segment
      segment_index: 62
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-62
---

# Atomic opm-libro-rebuilt - Segmento 62

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `56`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `62/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 20 Generalization and Instantiation / 20.2.2 Feature Inheritance

- **P3207** · `fact` · A general thing inherits its features—attributes and operation—to each one of its specializations. For example, Fig. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3208** · `constraint` · 20.4 is an OPD of a Camera, which has two features: The attribute Optical Zoom and the operation Image Capturing. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3209** · `fact` · This OPD has the following corresponding OPL paragraph, where the last OPL sentence expresses the unidirectional tagged structural relation. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3210** · `fact` · Since Digital Camera and Analog Camera are specializations of Camera, we can replace Camera with its Digital Camera and its Analog Camera specializations. This has indeed been done in Fig. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3211** · `constraint` · 20.5, which demonstrates the basic semantics of inheritance: the specialization—the refinee— inherits features (attributes and operations) from the general—the refineable. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3212** · `fact` · In OPM not only features are inherited; links and states are inherited as well. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3213** · `fact` · The inheritor can therefore replace the ancestor. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3214** · `constraint` · Digital Camera and Analog Camera inherit not only the features of Camera, which are the attribute Optical Zoom and the operation Image Capturing; they also inherit the tagged 282 Generalization and Instantiation structural relation uses from Camera to Capturing Medium. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3215** · `fact` · Moreover, not only structural relations are inherited; procedural relations are inherited as well. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)
- **P3216** · `fact` · The inheritor, however, may have more features, links, or states. · [src:S01:L8217-L8234](../../../INBOX/opm-libro.txt#L8217-L8234)

## opm libro · Chapter 20 Generalization and Instantiation / 20.2.3 Inheritance of Structural Relations

- **P3217** · `fact` · Consider the OPD in Fig. · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)
- **P3218** · `constraint` · 20.6, in which we specify the parts of Camera and the specializations of Capturing Medium. · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)
- **P3219** · `fact` · Medium This implies that the parts Camera consists of are inherited to the two Camera specializations: Digital Camera consists of Lens, Body, and Image Capturing Mechanism. · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)
- **P3220** · `fact` · Analog Camera consists of Lens, Body, and Image Capturing Mechanism. Not only aggregation is inherited. · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)
- **P3221** · `fact` · Any tagged structural relation, such as uses, is inherited. · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)
- **P3222** · `fact` · Since the tagged relation uses links Camera to Capturing Medium, when we specify the specializations of both Camera and Capturing Medium without taking care of the structural relation uses, we introduce link under-specification. · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)
- **P3223** · `fact` · This under-specification, encountered earlier, stems from the fact that the structural relation uses from Camera to Capturing Medium does not specify which Camera specialization (Analog Camera or Digital Camera) uses which Capturing Medium specialization (Image Storage Medium or Film). · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)
- **P3224** · `fact` · To set this straight, we specify which Camera specialization uses which Capturing Medium specialization. · [src:S01:L8236-L8250](../../../INBOX/opm-libro.txt#L8236-L8250)

## opm libro · Chapter 20 Generalization and Instantiation / 20.2.4 State and Link Inheritance

- **P3225** · `fact` · In OPM, states and links are inherited too. · [src:S01:L8254-L8260](../../../INBOX/opm-libro.txt#L8254-L8260)
- **P3226** · `fact` · Prior to the Image Capturing process in the Camera example, the Capturing Medium, which the Camera uses, is blank. · [src:S01:L8254-L8260](../../../INBOX/opm-libro.txt#L8254-L8260)
- **P3227** · `fact` · After the process Image Capturing occurs, Capturing Medium is recorded. · [src:S01:L8254-L8260](../../../INBOX/opm-libro.txt#L8254-L8260)
- **P3228** · `fact` · Hence, blank and recorded are two states of Capturing Medium. The OPD in Fig. · [src:S01:L8254-L8260](../../../INBOX/opm-libro.txt#L8254-L8260)
- **P3229** · `constraint` · 20.7 has two generalization links, one for Camera and the other for Capturing Medium. · [src:S01:L8254-L8260](../../../INBOX/opm-libro.txt#L8254-L8260)
- **P3230** · `constraint` · These two relations induce the two OPDs in Fig. 20.8. from Image Capturing · [src:S01:L8254-L8260](../../../INBOX/opm-libro.txt#L8254-L8260)

## opm libro · Chapter 20 Generalization and Instantiation / 20.3 Specialization Through a Discriminating Attribute

- **P3231** · `definition` · Quite often, a general has specializations that are distinguished from the general in that there is a certain attribute of the general whose restricted value defines the specialization. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3232** · `definition` · A discriminating attribute is an inherited attribute whose different values define corresponding specializations. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3233** · `constraint` · 284 Generalization and Instantiation ground, air, and water surface. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3234** · `definition` · Travelling Medium is the discriminating attribute of Vehicle, because the three values of Travelling Medium define the three specializations of Vehicle. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3235** · `fact` · These are Car, Aircraft, and Ship, with the corresponding Travelling Medium values ground, air, and water surface. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3236** · `fact` · A general may have more than one discriminating attribute. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3237** · `fact` · The maximum number of specializations with more than one discriminating attribute is the Cartesian product of the number of possible values for each discriminating attribute, where some combination of attribute values may be invalid. For example, extending the content of Fig. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3238** · `constraint` · 20.10, another attribute of Vehicle might be Purpose with the two values civilian and military. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3239** · `fact` · Based on these two values, there are two Vehicle specializations: civilian Vehicle and military Vehicle. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3240** · `constraint` · Due to multiple inheritance, the result is an inheritance lattice where the number of the most detailed specializations would be 3 × 2 = 6 as follows: civilian Car, civilian Aircraft, civilian Ship, military Car, military Aircraft, and military Ship. Capturing Medium—by Image Storage Medium. · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)
- **P3241** · `fact` · Right: Camera is substituted by Analog Camera, and Capturing Medium—by Film · [src:S01:L8262-L8281](../../../INBOX/opm-libro.txt#L8262-L8281)

## opm libro · Chapter 20 Generalization and Instantiation / 20.4 State-Specified Characterization Link

- **P3242** · `fact` · A state-specified characterization link is an exhibition-characterization link from a specialization to a specific value of a discriminating attribute of its general, which expresses the fact that the specialization can have only that value for that discriminating attribute. · [src:S01:L8286-L8298](../../../INBOX/opm-libro.txt#L8286-L8298)
- **P3243** · `fact` · Graphically, the state-specified characterization link is the triangular exhibition-characterization symbol, with its apex connected to the specialization and its base—to the specific value. · [src:S01:L8286-L8298](../../../INBOX/opm-libro.txt#L8286-L8298)
- **P3244** · `fact` · Using the state- specified characterization relation link, the OPD in Fig. · [src:S01:L8286-L8298](../../../INBOX/opm-libro.txt#L8286-L8298)
- **P3245** · `definition` · 20.11 is significantly more compact than its equivalent OPD in Fig. 20.10. · [src:S01:L8286-L8298](../../../INBOX/opm-libro.txt#L8286-L8298)
- **P3246** · `constraint` · Here, the discriminating attribute Travelling Medium of Vehicle with values ground, air, and water surface appears only once, as opposed to four times in Fig. 20.10. · [src:S01:L8286-L8298](../../../INBOX/opm-libro.txt#L8286-L8298)
- **P3247** · `constraint` · The model expresses Car, Aircraft, and Ship as specializations of Vehicle, connecting each specialization with a state- specified characterization relation link to the corresponding Travelling Medium value of ground, air, and water surface, respectively. 286 Generalization and Instantiation · [src:S01:L8286-L8298](../../../INBOX/opm-libro.txt#L8286-L8298)

## opm libro · Chapter 20 Generalization and Instantiation / 20.5 Classification-Instantiation

- **P3248** · `constraint` · An instance is an actual thing of some class of things, all having the same set of features, same structure, and same behavior. For example, Lassie and Blackie in Fig. 20.12 are instances of Dog. · [src:S01:L8301-L8308](../../../INBOX/opm-libro.txt#L8301-L8308)
- **P3249** · `fact` · Dog is the class of all the dogs, and Lassie is an actual exemplar of that class. · [src:S01:L8301-L8308](../../../INBOX/opm-libro.txt#L8301-L8308)
- **P3250** · `fact` · The symbol of instantiation is a black inverted triangle inside a larger white triangle. · [src:S01:L8301-L8308](../../../INBOX/opm-libro.txt#L8301-L8308)
- **P3251** · `fact` · In spoken English, the sentence “Lassie is a dog” is more natural, but the phrase “is a” is reserved for the specialization sentence, so to avoid conflicts and be explicit, the phrase “is an instance of” links an instance with its class in an OPL sentence that expresses instantiation. · [src:S01:L8301-L8308](../../../INBOX/opm-libro.txt#L8301-L8308)
- **P3252** · `fact` · The plural version, used for more than one instance, is “are instances of,” as in “Bach, Beethoven and Brahms are instances of Composers.” · [src:S01:L8301-L8308](../../../INBOX/opm-libro.txt#L8301-L8308)

## opm libro · Chapter 20 Generalization and Instantiation / 20.5.1 Classes and Instances

- **P3253** · `fact` · The things we have encountered while discussing generalization-specialization are classes of things, either object classes or process classes. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3254** · `fact` · When we talked about objects, we were actually referring to a typical example of its object class, a pattern of objects from which objects could be generated. A class is a template of a thing. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3255** · `fact` · An instance of a class is an incarnation of a particular identifiable member of that class. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3256** · `fact` · The definitions of class and instance are more general than their OO counterparts, as they refer to things rather than to objects. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3257** · `fact` · In metamodel terms, since a Thing is an Object or a Process, Class specializes into an Object Class and a Process Class. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3258** · `fact` · Likewise, Instance specializes into an Object Instance and a Process Instance: An Object Instance is an incarnation of the pattern specified by the Object Class and a Process Instance is an incarnation of the pattern specified by the Process Class. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3259** · `definition` · The template that the class defines includes everything that is inherited. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3260** · `fact` · As we have seen, in OPM it means that not only features, but also structural relations and procedural relations are inherited, and for object classes states are also inherited. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3261** · `fact` · Unlike a specialized class, an instance cannot exhibit any feature that its class does not exhibit, nor can an instance of an object be at a state that is not a state of its class. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
- **P3262** · `fact` · An object instance can be uniquely identified in the system, so at any given point in time it is possible to observe whether it exists, and if so—what its states and attribute values are. · [src:S01:L8310-L8329](../../../INBOX/opm-libro.txt#L8310-L8329)
