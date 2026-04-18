---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-37
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
      n_propositions: 63
      segmented: true
      segment_role: segment
      segment_index: 37
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-37
---

# Atomic opm-libro-rebuilt - Segmento 37

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `63`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `37/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 13 The Dynamic System Aspect / 13.4.1 Consumption and Result Timing

- **P1922** · `fact` · Existence of a consumee is a precondition, or part of the precondition, for process activation. · [src:S01:L5010-L5022](../../../INBOX/opm-libro.txt#L5010-L5022)
- **P1923** · `requirement` · If the required amount of consumee instances (usually 1) does not exist at the time of process initiation, then process activation shall wait for that amount of consumee instances to become existent. · [src:S01:L5010-L5022](../../../INBOX/opm-libro.txt#L5010-L5022)
- **P1924** · `fact` · The consumption of the consumee instance(s) is immediate upon process activation, unless the model expresses consumption of the object over time, in which case consumption rate, a specialization of transformation rate, is used, as explained below. created only when Machining ends In Fig. · [src:S01:L5010-L5022](../../../INBOX/opm-libro.txt#L5010-L5022)
- **P1925** · `constraint` · 13.5, Steel Rod is a consumee for the process Machining, which generates the resultee Shaft. · [src:S01:L5010-L5022](../../../INBOX/opm-libro.txt#L5010-L5022)
- **P1926** · `fact` · Once Machining has started, it consumes Steel Rod. · [src:S01:L5010-L5022](../../../INBOX/opm-libro.txt#L5010-L5022)
- **P1927** · `fact` · However, Shaft is considered to be created only upon termination of Machining. · [src:S01:L5010-L5022](../../../INBOX/opm-libro.txt#L5010-L5022)
- **P1928** · `fact` · During the process, Steel Rod does not exist anymore, but neither does Shaft. · [src:S01:L5010-L5022](../../../INBOX/opm-libro.txt#L5010-L5022)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.4.2 The Evolution of Effect Link

- **P1929** · `fact` · Explicitly expressing the states of an object in the diagram often yields an OPD that is too detailed, crowded or busy, making it hard to read. · [src:S01:L5024-L5035](../../../INBOX/opm-libro.txt#L5024-L5035)
- **P1930** · `constraint` · This is a manifestation of the comprehensiveness-clarity tradeoff: these two desired qualities of complex system models are in constant conflict. in Fig. 13.1. · [src:S01:L5024-L5035](../../../INBOX/opm-libro.txt#L5024-L5035)
- **P1931** · `fact` · In the middle OPD, the input and output links, which on the right OPD are attached to the state rountangles, migrate to the boundary of the Lamp object box. · [src:S01:L5024-L5035](../../../INBOX/opm-libro.txt#L5024-L5035)
- **P1932** · `fact` · They now link the process and the object directly, going from and to the object itself rather than from and to its states. · [src:S01:L5024-L5035](../../../INBOX/opm-libro.txt#L5024-L5035)
- **P1933** · `fact` · This interim representation is not valid in OPM. · [src:S01:L5024-L5035](../../../INBOX/opm-libro.txt#L5024-L5035)
- **P1934** · `fact` · To reduce the graphic clutter, the input and output links, denoted by two opposite unidirectional arrows, have been superimposed by joining them into one bidirectional arrow, yielding the symbol of the effect link. · [src:S01:L5024-L5035](../../../INBOX/opm-libro.txt#L5024-L5035)
- **P1935** · `fact` · Finally, on the left, the states of Lamp have been suppressed, because they are no longer vital since the links are not attached to them. · [src:S01:L5024-L5035](../../../INBOX/opm-libro.txt#L5024-L5035)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.5 Enablers

- **P1936** · `fact` · Suppose you wish to move from your place to an apartment in another city. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1937** · `fact` · To do this, you need a moving truck, which you rent from a moving truck rental company. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1938** · `fact` · You return the truck to the same place where you took it and with the same amount of gasoline as you took it. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1939** · `fact` · Hence, ignoring the amortization of the truck, nothing in it has changed. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1940** · `fact` · However, you would not be able to carry out the moving without it. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1941** · `fact` · We say that the Truck is an enabler of the Moving process. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1942** · `fact` · Moreover, since some of your furniture are very heavy, you need a Friend as a second enabler of the Moving process. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1943** · `fact` · An enabler of a process is an object that enables the process execution. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1944** · `fact` · Its presence is needed throughout the duration of the process, but when the process is over, the enabler exists at the same state as it was when the process started. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1945** · `requirement` · In other words, an enabler of a process is an object that must be present throughout the process duration in order for that process to occur and terminate successfully, but is not transformed as a result of the occurrence of the process. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1946** · `requirement` · An enabler E of a process P is an object that must exist and be available in order for P to start, and remain present throughout the occurrence of P in order for P to terminate normally, with E ultimately unaffected. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1947** · `fact` · The enabler might undergo state change during the process, but, as the enabler definition states, when the enabled process is over, the enabler is at the same state at which it started. For example, the enabler Oven in Fig. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1948** · `constraint` · 13.7 will change state from off to on at the beginning of the enabled Baking process, and from on back to off just prior to the end of Baking. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1949** · `fact` · As the Moving example has shown, some enables are human, while others are inanimate. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)
- **P1950** · `definition` · Hence, an enabler has two specializations: an agent or an instrument, as defined below. · [src:S01:L5037-L5058](../../../INBOX/opm-libro.txt#L5037-L5058)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.5.1 Agent: A Human Enabler

- **P1951** · `fact` · The term agent is reserved for a human enabler. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1952** · `fact` · An agent is an enabler who is a human or a group of humans. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1953** · `requirement` · An agent is an intelligent enabler, who can control the process it enables by exercising common sense or goal-oriented considerations, implying that it must consist of one or more humans. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1954** · `fact` · Usually, it is a single person—the system’s user or beneficiary. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1955** · `fact` · An agent can also be an organization, or a unit within a man-made organization, such as department, city council, government, group, team, etc. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1956** · `fact` · The notion of agent is important because it provides for modeling the “human in the loop”, i.e., how people interact with the system. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1957** · `fact` · This is a clear indication to the system designer of points of interaction with the system where human interface needs to be developed. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1958** · `fact` · Moreover, the hierarchy of processes that the agent is involved in provides an excellent guideline for the arrangement of a friendly graphic user interface, and creation of such interface can even be automated to some extent based on this model. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1959** · `fact` · In the world of software and embedded systems, robots are often referred to as agents, and software agents are common in the Internet, capitalizing on evolving agent technologies. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1960** · `constraint` · In OPM, which is geared to model all kinds of systems, including complex socio-technical systems and systems where humans are users and beneficiaries, humans (as individuals or groups) are privileged and distinguished from all the other inanimate enablers, so the term agent is reserved for humans only.1 This enables focusing the attention of system architects and designers to care for humans’ safety and special needs and desires while interacting with the rest if the system—the system’s usability and the users’ experience and delight from using a well-designed and human-friendly and accommodating system. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1961** · `fact` · The agent link is somewhat analogous to the actor—the “stick figure” in UML’s or SysML’s use-case diagram. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1962** · `fact` · In OPM, however, no separate kind of diagram is needed, as modeling the user is incorporated into the single OPM model. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1963** · `constraint` · Use cases in SysML notation can automatically be extracted from the OPM model, as can other SysML models (Grobshtein and Dori 2011). · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1964** · `fact` · Not any human or organization is necessarily only an agent. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1965** · `requirement` · For example, if a Student is engaged in the process of Studying, his or her Knowledge Level attribute change, say from shallow to deep. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1966** · `fact` · In this case, Student is not only an agent, but also a transformee. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1967** · `fact` · Likewise, if a department in an enterprise is undergoing business process reorganization, its structure and/or behavior changes as a result of this process, so in addition to being an agent, it is also a transformee. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1968** · `fact` · The procedural link uniqueness OPM principle states that at any level of detail, an object and a process can be connected with at most one procedural link. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1969** · `definition` · Semantic strength and link precedence are defined and discussed in detail in Chap. 21. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1970** · `fact` · Here we note only that transforming links are semantically stronger than enabling links, because the transforming links denote creation, consumption, or change of the linked object, while the enabling links only denote enablement. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1971** · `fact` · A transforming link has precedence over an enabling link as shown in Fig. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)
- **P1972** · `requirement` · 21.15, therefore if we need to choose between an agent link and an effect link, as in the examples above, effect link shall be chosen. · [src:S01:L5060-L5098](../../../INBOX/opm-libro.txt#L5060-L5098)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.5.2 Instrument: A Non-Human Enabler

- **P1973** · `fact` · An instrument of a process is any non-human, physical or informatical object, which does not change as a result of the execution of the process. An instrument is a non-human enabler. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1974** · `fact` · Examples of instruments include machines, tools, computers, robots, controllers, hardware, software, documents, orders, recipes, algorithms, prescriptions, files, commands, information, and data. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1975** · `fact` · Algorithms and recipes are prime examples of informatical instruments that can be used repeatedly, ideally without wearing out (in practice we may witness “software amortization” as well…). · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1976** · `fact` · Physical instruments usually change to some extent as they enable a process. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1977** · `fact` · In particular, they can wear out or degrade as they are being used as process enablers. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1978** · `definition` · Yet, from the viewpoint of the system under development, such objects would still be considered instruments, as these changes are either not significant enough to be accounted for, or they are out of the system’s scope. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1979** · `fact` · In other cases, wear and tear are factors to be considered. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1980** · `fact` · For example, in developing a Manufacturing System, a system architect may be required to account for Maintaining a Machine that wears out due to the Metal Cutting process it enables. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1981** · `fact` · In this case, the Machine should not be assigned the role of an instrument. Rather, it will be modeled as an affectee. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1982** · `fact` · The attribute of the Machine that changes as a result of its operation can be, for example, its Amortization Level, or hours of operation since the last overhaul. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1983** · `fact` · We will have to take this Machine Wearing process in account if our system encompasses the maintenance aspect of the Machine. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
- **P1984** · `definition` · The distinction in an OPD among the two types of enablers—agents and instruments—is made possible by their connection to the process they enable through the different enabling links, defined next. · [src:S01:L5100-L5119](../../../INBOX/opm-libro.txt#L5100-L5119)
