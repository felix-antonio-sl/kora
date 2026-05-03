---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-59
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
      n_propositions: 63
      segmented: true
      segment_role: segment
      segment_index: 59
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-59
---

# Atomic opm-libro-rebuilt - Segmento 59

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `63`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `59/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 19 States and Values / 19.4 State Transition: When a Process Is Active

- **P3031** · `fact` · At any point in time, an object can be in at most one of its states. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3032** · `fact` · We say “at most”, because the object can also be in transition between two states—the input state and the output state of the affectee with respect to the process currently affecting that affectee. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3033** · `fact` · During the time at which the process affecting the object takes place, the object has already left its input state, but it has not yet entered its output state. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3034** · `fact` · This is an unstable situation of an object which occurs when a process is changing the object from being at its input state—the state at which the object was before the process started, to being at its output state—the state where it is going to be once the process is over. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3035** · `fact` · During this time the object undergoes state transition. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3036** · `fact` · State transition is an unstable period of time for an object, which takes place when a process acts on it to change its state. Consider the following car painting example. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3037** · `fact` · When a white Car is painted red, its input state (the value of its Color attribute when it enters the body shop for painting) is white. This is shown in the top left OPD in Fig. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3038** · `constraint` · 19.5 by the state white of Color highlighted. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3039** · `fact` · The output state of Car (the value of its Color attribute when it leaves the body shop) is red. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3040** · `constraint` · This is shown in the bottom right OPD in Fig. 19.5 by the state red of Color highlighted. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3041** · `fact` · In-between these two stable states, Painting takes place. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3042** · `fact` · During this time interval, when the Car is being painted, i.e., throughout the Painting process, which may be a couple of days, the value of its Color attribute is not completely white any more, but it is not yet red either. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3043** · `fact` · Indeed, while the Car is being painted, it is in transition between two Car states. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3044** · `fact` · We say that while undergoing the Painting process, the Color of Car is unstable. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3045** · `fact` · This is shown in the top right and bottom left OPDs in Fig. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3046** · `constraint` · 19.5, where the highlighting of the red and white states gradually change from red and white. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3047** · `fact` · The duration of the transition, the time when Car is neither completely red nor white, is equal to the duration of the painting process. diagrams at the bottom of each OPD are the lifespan diagrams As the car painting example demonstrates, objects and processes in the system have history, which is accumulated as the system performs its function. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3048** · `fact` · The history of an object begins at the time when it is created and becomes an identifiable entity, and it ends at the time when it is consumed so it is no longer the same identifiable entity. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3049** · `fact` · The history includes a time record of when the object was created, by what process, the state changes the object went through while it maintained its identity, when the object was consumed, and by what process. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3050** · `fact` · History is meaningful only with respect to a particular system execution, i.e., the system at the operational level, or instance level, but not the conceptual level, or class level, because only when a system executes its function, it is possible to track and record what process instance started and ended when, and what object instance was transformed, whether it was created or consumed, or whether its state was changed. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3051** · `fact` · The history of a process includes, for each execution of each process in the system, the time at which it started and ended. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3052** · `fact` · A particular process execution constitutes a process instance. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3053** · `fact` · The history also includes the transformee and enabler instances in the involved object set. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3054** · `fact` · A useful tool to view, trace, and analyze the history of objects and their states, and of processes in a system is the lifespan diagram, which OPCAT indeed includes. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3055** · `fact` · A lifespan diagram is a diagram which, for any point in time during the life of the system, shows what objects exists in the system, what state each object is at, and what processes are active. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3056** · `fact` · The four lifespan diagrams shown at the bottom of each one of the four OPDs in Fig. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3057** · `constraint` · 19.5 record the history of the car painting system as time progresses. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3058** · `fact` · In the diagram below the OPD in the top-left, only the first time period is displayed. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3059** · `fact` · Painting is not active, and the Car is white. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3060** · `fact` · In the second diagram, the first three time periods are displayed. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3061** · `fact` · In the third period, Painting is active, and the Car is no longer white. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3062** · `fact` · The same happens in the fourth period, as shown in the third diagram. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3063** · `fact` · Finally, in the fifth period, shown in the bottom diagram, Painting is no longer active, and the Car is red. As another example, in the OPD in Fig. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3064** · `constraint` · 19.6, Cutting takes Raw Metal Bar from its pre-cut to its cut state. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3065** · `fact` · As long as Cutting is active, the state of Raw Metal Bar is in transition and bound to the Cutting process: Cutting takes it out of its pre-cut state but has not yet brought it to its cut state with process completion. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3066** · `fact` · During Cutting, the state of Raw Metal Bar is unstable and therefore indeterminate: it could be partly cut and reusable or mostly cut and unusable. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3067** · `fact` · In either case, it is not available for Machining, since it is not in its cut state. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3068** · `fact` · Likewise, during Testing, Part is already not pre-tested, yet it is still not tested. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3069** · `fact` · If an active affecting process stops prematurely or takes too long, the state of any affectee remains indeterminate, unless exception handling resolves the object to one of its permissible states. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)
- **P3070** · `fact` · This can be done using overtime or undertime exception link, discussed in the chapter on OPM operational semantics. · [src:S01:L7789-L7854](../../../INBOX/opm-libro.txt#L7789-L7854)

## opm libro · Chapter 19 States and Values / 19.5 Path Labels and Flip-Flop

- **P3071** · `fact` · When two or more procedural links exit from the same process, it is not possible to know what link to follow unless the links are labeled. which solves this problem. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3072** · `fact` · If Tomato, Cucumber and Meat all exist, then the result is the generation of Salad, Stew, and Steak. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3073** · `fact` · However, we cannot tell what ingredients went into what dish. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3074** · `fact` · And what if we want to model that for vegetarians we wish to prepare only Salad and for meat eaters only Stew and Steak? · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3075** · `constraint` · This is solved by using the path labels carnivore and herbivore, recorded along the procedural links, as shown in Fig. 19.7 and expressed by the OPL. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3076** · `fact` · Path labels uniquely determine which link to follow on exiting the process: The link to be followed is the one having the same label as the one with which we entered the process. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3077** · `fact` · Using path labels, it is possible to follow a specific scenario in the model that span multiple consecutive procedural links. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3078** · `fact` · As this example demonstrates, path labels remove the logical AND requirement from the objects in the preprocess object set. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3079** · `requirement` · Here, only all the objects in the preprocess object set whose links have the same label must exist in order for the precondition to be met. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3080** · `fact` · Thus, Tomato and Cucumber alone, or Meat alone, meet the precondition for Food Preparing, and the outcome is dictated by the path label. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3081** · `fact` · A path label is a label on a procedural link which specifies that the link to be followed is the one with the same label as the one with which the process was entered. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3082** · `fact` · Path labels remove the ambiguity arising from multiple outgoing procedural links, and they can also be used for state-specified links. For example, in Fig. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3083** · `constraint` · 19.8 there are two output links: one from Heating to the state liquid of Water and the other to state gas. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3084** · `fact` · Entering this process from state ice, it is not clear whether the flow of control should go to state liquid or to state gas, unless we use path labels. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3085** · `constraint` · An alternative would be to have two separate processes, one called “Ice-to-Liquid Heating” and the other— “Liquid-to-Gas Heating”. A similar solution can be applied to Fig. 19.7. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3086** · `requirement` · Without path labels, every pair of incoming and outgoing procedural links must have its own process. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3087** · `fact` · Path labels provide a memory mechanism, which is required for state machines, where the next state transition depends on the state of the system and on the previous move. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3088** · `requirement` · When the process precondition involves an object or state connected via a path-labeled procedural link, and the postprocess object set has more than one possibility for destination object or state, the appropriate postprocess object set destination shall be the one obtained following the link with the same path label as the link connecting one or more objects and/or states from the preprocess object set. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3089** · `fact` · From a metamodel perspective, Path Label is an (optional) property of Procedural Link. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3090** · `requirement` · The memory mechanism dictates that if the scenario unfolded through a path with some path label, then it must proceed to the next step following the direction marked with same path label. lamp that is turned on and turns it on if it is shut off. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3091** · `fact` · The Push Button “remembers” its state, so whenever it is pushed, it switches states. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3092** · `fact` · We can use the same idea to model a “flip-flop”, a two-state device which offer basic memory for sequential logic operations and used for digital data storage of binary numerical data. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
- **P3093** · `constraint` · This OPM model mechanism can also be used to achieve the “NOT” logical operator, as discussed in Sect. 23.2. · [src:S01:L7856-L7899](../../../INBOX/opm-libro.txt#L7856-L7899)
