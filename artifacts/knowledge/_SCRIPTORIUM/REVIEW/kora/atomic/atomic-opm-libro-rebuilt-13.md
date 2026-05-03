---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-13
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
      n_propositions: 35
      segmented: true
      segment_role: segment
      segment_index: 13
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-13
---

# Atomic opm-libro-rebuilt - Segmento 13

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `35`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `13/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 8 Abstracting and Refining / 8.3 Structural View of the ACR System

- **P0648** · `constraint` · 8.5 shows, the structure of the ACR System has undergone quite a few changes. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0649** · `fact` · I would be beneficial to examine the entire structure alone without any dynamic aspects of processes and state transitions. OPCAT provides such an automatic facility. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0650** · `constraint` · Figure 8.4 shows the automatically-generated structural view of the ACR System, after manual rearrangements for improved readability. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0651** · `fact` · A four-level hierarchy is exposed, which is also expressed in the following OPL sentences, where the indentation helps realize the hierarchy. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0652** · `constraint` · ACRSystem OnStar Call Center In-vehicle ACR Subsystem GPS Sensors Set Cellular System 2.m 2.m Side Sensor Front Sensor Sensing and Diagnostic Module OnStar Module Diagnostics Unit Accelerometer Sensing Unit ACR System consists of OnStar Call Center, Cellular System, GPS, and In-vehicle ACR Subsystem. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0653** · `fact` · In-vehicle ACR Subsystem consists of Sensing and Diagnostic Module, Cellular System, GPS, OnStar Module, and Sensors Set. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0654** · `fact` · Sensing and Diagnostic Module consists of Accelerometer, Sensing Unit, and Diagnostics Unit. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0655** · `constraint` · Sensors Set consists of 2 to many Front Sensors, 2 to many Side Sensors, and Sensing Unit. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0656** · `fact` · Examining the OPD and the corresponding OPL, two objects stick out as ones in need of remodeling: GPS and Cellular System. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0657** · `fact` · The reason is that each one of these objects is part of both ACR Subsystem and In-vehicle ACR Subsystem. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0658** · `fact` · However, In-vehicle ACR Subsystem is also part of ACR System. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0659** · `fact` · While this is not a contradiction, it is an inconsistency, because GPS and Cellular System are both direct and indirect parts of ACR System. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0660** · `fact` · As we know, neither GPS nor Cellular System in their entirety are parts of the In- vehicle ACR Subsystem; each has components both inside and outside the vehicle. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0661** · `constraint` · ACR System OnStar Call Center In-vehicle ACR Subsystem GPS Cellular System In-vehicle GPS Ex-vehicle GPS Ex-vehicle Cell Phone Cell System Sensors Set 2.m Side Sensor 2.m Front Sensor OnStar Module Sensing and Diagnostic Module Accelerometer Diagnostics Unit Sensing Unit The solution for this inconsistency, presented in Fig. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0662** · `constraint` · 8.5, is to break each of these two objects into two parts: GPS is split into In-vehicle GPS and Ex-vehicle GPS, while Cellular System is divided into Cell Phone and Ex-vehicle Cell System. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)
- **P0663** · `fact` · Both In-vehicle GPS and Cell Phone are parts of In-vehicle ACR Subsystem, while Ex-vehicle GPS and Ex-vehicle Cell System are both parts of ACR System but not of the In-vehicle ACR Subsystem. · [src:S01:L1970-L2034](../../../INBOX/opm-libro.txt#L1970-L2034)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context

- **P0664** · `fact` · A conceptual model is a formal model, in which every entity being modeled in the real world has a transparent and one-to-one correspondence to an object in the model. · [src:S01:L2111-L2117](../../../INBOX/opm-libro.txt#L2111-L2117)
- **P0665** · `constraint` · Simmons (1994) Before going into formal presentations of OPM and SysML as conceptual system modeling languages and OPM as a systems engineering methodology, we discuss the theoretical aspects underlying the framework of systems, systems architecture, and systems engineering, within which conceptual modeling is a valuable intellectual activity. · [src:S01:L2111-L2117](../../../INBOX/opm-libro.txt#L2111-L2117)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.1 Systems, Modeling, and Systems Engineering

- **P0666** · `fact` · Systems are all around us. · [src:S01:L2119-L2126](../../../INBOX/opm-libro.txt#L2119-L2126)
- **P0667** · `fact` · Natural systems have been around for eons, and biological organisms have evolved into extremely complex systems. · [src:S01:L2119-L2126](../../../INBOX/opm-libro.txt#L2119-L2126)
- **P0668** · `fact` · Artificial, human-made systems, products, and services are also becoming increasingly complex. · [src:S01:L2119-L2126](../../../INBOX/opm-libro.txt#L2119-L2126)
- **P0669** · `fact` · Systems of infrastructural nature, such as air traffic control, the Internet, and electronic economy, are orders of magnitude more complex than products individuals normally use. · [src:S01:L2119-L2126](../../../INBOX/opm-libro.txt#L2119-L2126)
- **P0670** · `fact` · The combination of miniaturization and computational power has been so pervasive that even common household products exhibit intelligent features embedded within increasingly minuscule, commodity-like hardware, giving rise to the emerging Internet of Things—a conglomerate of weakly interconnected devices of all kinds, creating a loosely coupled mega system-of-systems. · [src:S01:L2119-L2126](../../../INBOX/opm-libro.txt#L2119-L2126)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.1.1 Science and Engineering: Commonalities and Differences

- **P0671** · `fact` · The main difference between science and engineering is that scientists aim to explore and understand observable physical, informatical (cybernetic) and human phenomena, while engineers, who are informed by scientific discoveries, architect, design, develop, maintain and evolve artificial systems for the benefit of humans. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)
- **P0672** · `fact` · Sometimes, engineers are required to perform reverse engineering—the exploration of an existing system whose function, structure, behavior, or working principles are not available and unknown. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)
- **P0673** · `fact` · Considering this exploratory character of reverse engineering, science can be thought of as reverse engineering of nature. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)
- **P0674** · `fact` · When a system is being designed (by engineers) or investigated (by scientists), details about it accumulate quickly. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)
- **P0675** · `fact` · The collected facts, be they real, assumed, contemplated or conjectured, become so voluminous that they are hard to master without an orderly way of making sense of what is being revealed. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)
- **P0676** · `fact` · Managing these facts is mandatory in order for them to make sense as a whole. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)
- **P0677** · `fact` · In view of the rapid development of systems’ complexities, the need for an intuitive yet formal way of documenting designs of new systems or collected information about existing ones becomes ever more apparent. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)
- **P0678** · `fact` · This, in turn, requires a solid infrastructure for recording, storing, organizing, querying, and presenting the knowledge being accumulated and the creative ideas that build on this knowledge. · [src:S01:L2128-L2146](../../../INBOX/opm-libro.txt#L2128-L2146)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.1.2 Conceptual Modeling and Model-Based Systems Engineering

- **P0679** · `fact` · The process of representing system-related knowledge in both science and engineering is conventionally referred to as conceptual modeling, and the outcome of this activity is a conceptual model. · [src:S01:L2148-L2152](../../../INBOX/opm-libro.txt#L2148-L2152)
- **P0680** · `fact` · Subsequent, higher order cognitive activities, including understanding, analyzing, designing, presenting, and communicating the analysis findings and design ideas, can be based on the evolving conceptual model. · [src:S01:L2148-L2152](../../../INBOX/opm-libro.txt#L2148-L2152)
- **P0681** · `fact` · The vision of the Massachusetts Institute of Technology Engineering Systems Division (MIT ESD, · [src:S01:L2148-L2152](../../../INBOX/opm-libro.txt#L2148-L2152)
- **P0682** · `requirement` · is that “the fundamental principles and properties of engineering systems are well-understood, so that these systems can be modeled, designed, and managed effectively.” Conceptual modeling, which often precedes or done alongside mathematical and physical modeling, is the primary activity required for engineering systems to be understood, designed, and managed. Modeling is the process underlying model-based systems engineering (MBSE), the focus of this book. MBSE is not just about modeling, as some people mistakenly perceive; it is systems engineering (SE) that is based on formal modeling of various kinds—conceptual, mathematical, and physical). The conceptual model is the comprehensive underlying blueprint—the reference artifact that constitutes the source of authority of the various system aspects—requirements, performance, functionality, structure, dynamics, and many other physical and informatical (cybernetic) aspects. Thus, MBSE requires a rigorous conceptual modeling methodology that encompasses a universal ontology, a language, a set of principles and guideline, and a supportive modeling software environment. Understanding physical, biological, artificial, and social systems requires a well-founded, formal, yet intuitive methodology and language that is capable of modeling the complexities inherent in these systems in a coherent, straightforward manner. The same modeling paradigm, the heart of the methodology, should serve for both designing new systems (engineering) and for studying (science) and improving existing ones. It should apply to artificial as well as natural systems and represent both equally faithfully. A common, unified conceptual modeling framework for both artificial and natural systems is most important, because complex engineered systems and physical phenomena often mutually affect each other. For example, in order to model a system such as an aircraft, a satellite, a ballistic missile defense system, or a medical device, one must understand the relevant mechanical, electrical, chemical, biological, and physical principles that govern both the system and the environment in which it operates and with which it interacts. · [src:S01:L2153-L2175](../../../INBOX/opm-libro.txt#L2153-L2175)
