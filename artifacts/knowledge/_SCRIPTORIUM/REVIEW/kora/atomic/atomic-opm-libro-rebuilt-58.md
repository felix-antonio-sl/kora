---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-58
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
      n_propositions: 45
      segmented: true
      segment_role: segment
      segment_index: 58
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-58
---

# Atomic opm-libro-rebuilt - Segmento 58

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `45`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `58/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 19 States and Values / 19.1.1 State Enumeration

- **P2986** · `fact` · An example of valid states of a Planet is visible and invisible, and the OPL sentence specifying it is “Planet can be visible or invisible.” A Planet can change its invisible state to a visible state by rising above the horizon and when there are no clouds. · [src:S01:L7692-L7700](../../../INBOX/opm-libro.txt#L7692-L7700)
- **P2987** · `fact` · A state enumeration OPL sentence such as “Planet can be visible or invisible.” enumerates all the states that the object can be at. · [src:S01:L7692-L7700](../../../INBOX/opm-libro.txt#L7692-L7700)
- **P2988** · `fact` · It starts with the object name, followed by the reserved phrase “can be” (or “is” in the case of just one state) followed by a list of states, which are comma-separated in the case of three or more states, and ending with the reserved phrase “or” between the last and second to last states. · [src:S01:L7692-L7700](../../../INBOX/opm-libro.txt#L7692-L7700)
- **P2989** · `fact` · An object cannot be at more than one state at a time. · [src:S01:L7692-L7700](../../../INBOX/opm-libro.txt#L7692-L7700)
- **P2990** · `fact` · Therefore, the semantics of the state enumeration sentence is that of the logical exclusive OR, called XOR for short. · [src:S01:L7692-L7700](../../../INBOX/opm-libro.txt#L7692-L7700)
- **P2991** · `fact` · The default capitalization of a state name is lower-case letter. · [src:S01:L7692-L7700](../../../INBOX/opm-libro.txt#L7692-L7700)

## opm libro · Chapter 19 States and Values / 19.1.2 Initial, Final, and Default States

- **P2992** · `fact` · It is often convenient or desirable to specify what the initial state, the final state, and the default state of an object are. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P2993** · `fact` · The initial state of an object B is the state at which B is upon its generation or as the system starts executing. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P2994** · `fact` · The final state of an object B is the state at which B is upon its consumption or as the system finishes executing. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P2995** · `fact` · The default state of an object B is the state at which B is expected to be when its state is not specified. (bold frame) and adult is both the final state (double frame) and the default state (the open arrow pointing at adult). · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P2996** · `fact` · The simulation emphasizes closing the lifecycle An object can have zero or more initial states, zero or more final states, and at most one default states. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P2997** · `fact` · The same state can be any combination of initial, final and/or default. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P2998** · `constraint` · The initial and final states are especially useful for objects that exhibit a lifecycle pattern, such as a product, a system, or our familiar frog from Chap. 13. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P2999** · `fact` · The default state is useful for specifying the state at which an object is when no state is specified. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P3000** · `fact` · The symbols for initial, final, and default states are a bold state frame, a double state frame, and a state frame pointed to by an open arrow, respectively. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P3001** · `fact` · These are demonstrated in the simulated lifecycle of Frog in Fig. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P3002** · `constraint` · 19.1: The initial state of Frog is spawn (cell mass), denoted by the bold state frame. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P3003** · `fact` · The state adult is both the final state, denoted by the double frame, and the default state—the open arrow pointing at the adult state frame. The conceptual simulation in Fig. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P3004** · `constraint` · 19.1 shows the process Mating & Fertilizing (Amplexus)—the highlighted solid ellipse—operating on Frog to change it from the state adult to the state spawn (cell mass). · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P3005** · `fact` · The corresponding OPL sentence is: Mating & Fertilizing (Amplexus) changes Frog from adult to spawn (cell mass). · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)
- **P3006** · `fact` · This state transition emphasizes the cyclical nature of Frog, as the final (and default) state of Frog, adult, yields Frog in the initial state, spawn (cell mass), through the Mating & Fertilizing (Amplexus) process. · [src:S01:L7707-L7735](../../../INBOX/opm-libro.txt#L7707-L7735)

## opm libro · Chapter 19 States and Values / 19.2 State Suppression and Expression

- **P3007** · `fact` · The elimination of the state symbols from the object is termed state suppression. · [src:S01:L7737-L7746](../../../INBOX/opm-libro.txt#L7737-L7746)
- **P3008** · `fact` · State suppression is one of several abstracting options. · [src:S01:L7737-L7746](../../../INBOX/opm-libro.txt#L7737-L7746)
- **P3009** · `fact` · Abstracting is a means to simplify the OPD at the cost of hiding details related to things in the OPD. · [src:S01:L7737-L7746](../../../INBOX/opm-libro.txt#L7737-L7746)
- **P3010** · `fact` · Expectedly, as both the OPDs and in their equivalent OPL sentences demonstrate, state suppression eliminates the information about how exactly the process affects the object. · [src:S01:L7737-L7746](../../../INBOX/opm-libro.txt#L7737-L7746)
- **P3011** · `fact` · This information can be provided in lower-level OPDs, where the states of the process are made explicit. · [src:S01:L7737-L7746](../../../INBOX/opm-libro.txt#L7737-L7746)
- **P3012** · `fact` · The reverse of state suppression is state expression: refining the OPD by adding relevant states. · [src:S01:L7737-L7746](../../../INBOX/opm-libro.txt#L7737-L7746)
- **P3013** · `fact` · As and output link components, state suppression is accompanied by merging the input-output link pair into a single effect link. · [src:S01:L7737-L7746](../../../INBOX/opm-libro.txt#L7737-L7746)

## opm libro · Chapter 19 States and Values / 19.2.1 State Specializations and Their Participation Constraints

- **P3014** · `fact` · Default State, and their participation constraints. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3015** · `fact` · This is also specified in the OPL to the right of the OPD. Object State Set Object exhibits State Set. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3016** · `fact` · State State Set consists of optional States, optional Initial States, an optional Default State, and optional Final States. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3017** · `fact` · Initial State Initial State, Default State, and Final State are States. ? · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3018** · `fact` · Default State Final State with their participation constraints In the metamodel in Fig. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3019** · `constraint` · 19.3, State and its three specialization—Initial State, Default State, and Final State—are all objects. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3020** · `fact` · This metamodel specifies the participation constraints for the three State specializations. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3021** · `fact` · The OPL on the right states that State Set can consist of “optional Initial States” and “optional Final States”, i.e., zero, one, or more than one initial states and zero, one, or more than one final states. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3022** · `fact` · Indeed, while usually an object has at most one initial state, it can have more than one. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3023** · `fact` · For example, some process can create the object in one initial state while another process can create the same object in a different initial state. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3024** · `fact` · Alternatively, as we show below, the same process can create an object stochastically at one of two or more initial states. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3025** · `fact` · An object may also have more than one final state, from which it cannot exit. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)
- **P3026** · `fact` · However, State Set can consist of “an optional Default State”, i.e., there may be at most one default state. · [src:S01:L7752-L7778](../../../INBOX/opm-libro.txt#L7752-L7778)

## opm libro · Chapter 19 States and Values / 19.3 Value: A Specialization of State

- **P3027** · `fact` · Value is a state of an attribute. · [src:S01:L7780-L7787](../../../INBOX/opm-libro.txt#L7780-L7787)
- **P3028** · `fact` · Since value is a state of an attribute, it is a specialization of state. · [src:S01:L7780-L7787](../../../INBOX/opm-libro.txt#L7780-L7787)
- **P3029** · `fact` · The nuance in semantics between state and value is demonstrated in Fig. · [src:S01:L7780-L7787](../../../INBOX/opm-libro.txt#L7780-L7787)
- **P3030** · `constraint` · 19.4, where in the OPD on the left, off and on are states of the object Lantern, while on the right, off and on are values of the attribute Operational Status of the object Lantern. and on are values of the attribute Operational Status of the object Lantern · [src:S01:L7780-L7787](../../../INBOX/opm-libro.txt#L7780-L7787)
