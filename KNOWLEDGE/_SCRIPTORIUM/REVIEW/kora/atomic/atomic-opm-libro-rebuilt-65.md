---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-65
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
      segment_index: 65
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-65
---

# Atomic opm-libro-rebuilt - Segmento 65

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `59`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `65/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.4 The Completeness-Clarity Trade-off

- **P3355** · `requirement` · Like most classical engineering problems, complexity management entails a tradeoff that must be balanced between two conflicting requirements: completeness and clarity. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3356** · `requirement` · Completeness means that the system must be specified to the last relevant, necessary detail. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3357** · `requirement` · Clarity means that to communicate the analysis and design outcomes, the documentation, be it textual or diagrammatic, must be legible and comprehensible. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3358** · `fact` · The complexity challenge entails balancing these two forces that pull in opposite directions and need to be reconciled: On one hand, completeness requires that the system details be stipulated to the fullest extent possible. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3359** · `fact` · On the other hand, the need for clarity imposes an upper limit on the level of complexity of each individual diagram and does not allow for a diagram that is too cluttered or loaded. Completeness and Clarity attributes. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3360** · `requirement` · Complexity management must address and solve this problem of completeness-clarity tradeoff by striking the right balance between these two contradicting demands. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3361** · `fact` · OPM achieves clarity through abstracting and completeness through refining. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3362** · `fact` · Abstracting, the inverse of refining, saves space and reduces complexity, but it comes at the price of completeness. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3363** · `fact` · Conversely, refining, which contributes to completeness, comes at the price of loss of clarity. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3364** · `fact` · There are “no free meals”; as is typically the case with engineering problems, there is a clear tradeoff between completeness of details and clarity of their presentation. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3365** · `fact` · The solution OPM proposes is to keep each OPD simple enough, and to distribute the system specification over a set of consistently inter-related and mutually- aware OPDs that contain things at various detail levels. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)
- **P3366** · `fact` · Abstracting and refining are the analytical tools that provide for striking the right balance between clarity and completeness. · [src:S01:L8605-L8624](../../../INBOX/opm-libro.txt#L8605-L8624)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.5 State Expression and State Suppression

- **P3367** · `fact` · Explicitly depicting the states of an object in an OPD may result in a diagram that is too crowded or busy, making it hard to read or comprehend. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3368** · `fact` · OPM enables state suppression—hiding the appearance of some or all the states of an object as represented in a particular OPD when those states are not necessary in that OPD’s context. In Fig. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3369** · `constraint` · 21.4, the two states of each one of the two attributes form the OPD in Fig. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3370** · `constraint` · 21.2 were suppressed, so the input-output link pair changes to an effect link (Fig. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3371** · `constraint` · 21.3). attributes The inverse operation of state suppression—state expression—exposes one or more hidden object states. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3372** · `fact` · The modeler may suppress any subset of states. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3373** · `fact` · The complete set of states of an object is the union of the set of states of that same object appearing in all of the OPDs in the OPD set—the set of OPDs of the entire OPM model. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3374** · `requirement` · Graphically, the annotation indicating that an object presents a proper subset (i.e., at least one but not all) of its states, shall be a small state suppression symbol in the object’s right bottom corner. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)
- **P3375** · `requirement` · This symbol appears as a small state with an ellipsis label, which signifies the existence of one or more states that the view is suppressing, The textual equivalence of the state suppression symbol shall be the OPL reserved phrase “or at least one other state”. · [src:S01:L8628-L8646](../../../INBOX/opm-libro.txt#L8628-L8646)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.6 Unfolding and Folding

- **P3376** · `fact` · Unfolding is a mechanism for refinement, elaboration, or decomposition. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3377** · `fact` · Unfolding reveals a set of things that relate to the unfolded thing—the refineable. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3378** · `fact` · The result of unfolding is a hierarchy tree, the root of which is the refineable. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3379** · `fact` · Linked to the root are the refinees—one or more things—parts, specializations, features, or instances—that adds details about the refineable through one or more of the four fundamental structural relations. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3380** · `fact` · Any refinee can, in turn, be the refineable for the next level of unfolding. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3381** · `fact` · Folding is the inverse operation of unfolding. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3382** · `fact` · It is a collapsing and abstracting mechanism, which can be applied to a hierarchy of an unfolded refineable. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3383** · `fact` · Folding is applied from the bottom of the hierarchy upward. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3384** · `fact` · Each folding operation hides some or all of the refineables. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3385** · `fact` · Folding all the refineables leaves just the refineable—the root of the tree hierarchy. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)
- **P3386** · `fact` · Since each of the four fundamental structural relation links may undergo unfolding and folding, the four kinds of unfolding-folding pairs are the following. aggregation unfolding—exposing the parts of a whole, and participation folding—hiding the parts of the whole, exhibition unfolding—exposing the exhibitor’s features, and characterization folding—hiding the features of the exhibitor, generalization unfolding—exposing the specializations of the general, and specialization folding— hiding specializations of the general, and classification unfolding—exposing the class instances, and instantiation folding—hiding the instances of the class. · [src:S01:L8648-L8669](../../../INBOX/opm-libro.txt#L8648-L8669)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.7 In-Diagram and New-Diagram Unfolding

- **P3387** · `fact` · Unfolding can be done either in the current OPD or in a new OPD. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3388** · `fact` · In-diagram unfolding is unfolding in which the refineable and its refinees appear unfolded in the same OPD in which the refinee was originally. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3389** · `fact` · Since unfolding uses one of the four the fundamental structural links, in-diagram unfolding is graphically, syntactically, and semantically equivalent to using the corresponding fundamental structural links. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3390** · `fact` · While in-diagram unfolding increases the load of the diagram, it saves the need to create a new diagram, but if there are many refinees, or the current OPD is already busy, we will prefer new-diagram unfolding. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3391** · `fact` · New-diagram unfolding is unfolding in which the refineable and its refinees appear unfolded in a new OPD. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3392** · `fact` · Both in- and new-diagram unfolding can be applied to both objects and processes. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3393** · `fact` · Graphically, in new-diagram unfolding, the unfolded refineable is denoted by a thick contour in both the more abstract OPD in which the refineable appears folded, without refinees, and in the new, more detailed OPD, in which the refineable appears unfolded and connected to its refinees with one or more fundamental structural link. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3394** · `fact` · The modeler should make a decision as to whether to use in-diagram or new-diagram unfolding based on clarity considerations: If the current OPD is already crowded and tends to be cluttered, a new OPD should be created to prevent the current OPD from becoming unwieldy. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3395** · `fact` · If in-diagram unfolding had been applied and later the OPD became too crowded, the modeler can then switch from in-diagram to new- diagram unfolding, thereby alleviating the complicatedness of the current OPD (at the price of an additional OPD in the OPD set). · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3396** · `fact` · Thus, the modeler decision whether to use in-diagram or new-diagram unfolding should account for the trade-off between the clutter added to the current OPD and the need to create a new OPD for displaying the refinees and associated links amongst them. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3397** · `fact` · Partial unfolding may be depicted using the non-comprehensiveness symbol for aggregation, exhibition, and classification. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3398** · `fact` · To satisfy a particular contextual relevance for an OPD, a modeler may choose which refinees appear unfolded. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3399** · `fact` · While unfolding and folding can be applied to both objects and processes, it is more prevalent for objects, while processes can be refined via in-zooming, discussed next, or via unfolding. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3400** · `fact` · Process unfolding is useful for functional decomposition which is very important in complex systems. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3401** · `fact` · Such systems have many more auxiliary functions, in addition to the core function, that are concurrent or independent of the core function’s flow. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3402** · `fact` · There is usually at least one more function—system setup and management, a set of many services. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3403** · `fact` · Service-oriented systems offer several parallel or concurrent services that cannot be thought of as working serially. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)
- **P3404** · `fact` · Real-time systems perform several functions in parallel rather than serially, while each component continuously samples its input from the other components and acts upon it. · [src:S01:L8671-L8707](../../../INBOX/opm-libro.txt#L8671-L8707)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.8 Port Folding

- **P3405** · `fact` · A procedural link from an operation of an object exhibitor to another object is lost during the operation unfolding, because two objects cannot be directly connected by a procedural link. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3406** · `fact` · Similarly, a procedural link from an attribute of a process exhibitor to another process is lost during the operation unfolding, because two objects cannot be directly connected by a procedural link. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3407** · `constraint` · However, it is often desirable to maintain these links (Fig. 21.5). · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3408** · `constraint` · Based on Mordecai and Dori (2013), a possible solution is port folding, shown in Fig. 21.6. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3409** · `fact` · Port folding is a specialization of folding, an intermediate state between complete folding and complete unfolding, in which we shift the process refinee—the operation—to the contour of the object refineable— the exhibitor. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3410** · `fact` · Graphically, this looks similar to a SysML activity diagram port on the folded exhibitor. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3411** · `fact` · Port folding is a useful representation if the modeler wants to use the object rectangles to give an idea about the physical layout and relative sizes of the various system components. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3412** · `fact` · The reserved phrase “as ports” (or “as a port” for singular) at the end of the exhibition sentence indicates port folding. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
- **P3413** · `fact` · Port folding can also be applied to attributes of processes. · [src:S01:L8709-L8722](../../../INBOX/opm-libro.txt#L8709-L8722)
