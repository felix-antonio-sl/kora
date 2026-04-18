---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-64
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
      n_propositions: 50
      segmented: true
      segment_role: segment
      segment_index: 64
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-64
---

# Atomic opm-libro-rebuilt - Segmento 64

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `50`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `64/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction

- **P3305** · `fact` · The human mind, after all, can only juggle so many pieces of data at once before being overwhelmed. C. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3306** · `constraint` · Downton (1998) The very need for systems analysis and design strategies stems from complexity. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3307** · `fact` · If systems or problems were simple enough for humans to be grasped by merely glancing at them, no methodology would have been required. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3308** · `requirement` · Due to the need for tackling sizeable, complex problems, a system development methodology must be equipped with a comprehensive approach, backed by set of reliable and useful tools, for controlling and managing complexity. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3309** · `constraint` · OPM provides four refinement-abstraction mechanisms to manage systems’ inherent complexity: (1) unfolding–folding, (2) in-zooming–out-zooming, (3) state- expressing–state-suppressing, and (4) view creating. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3310** · `definition` · These mechanisms, defined and discussed in this chapter, make possible the specification of contextualized model segments as separate, yet interconnected OPDs. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3311** · `fact` · Taken together, they provide a complete model of the functional, value providing system. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3312** · `fact` · These mechanisms enable presenting and viewing the modelled system, and the elements it contains, in various contexts that are interrelated by the common objects, processes and relations. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3313** · `fact` · The set of clearly specified and compatible interconnected Object-Process Diagrams completely specify the entire system to an appropriate extent of detail and provide a comprehensive representation of that system with a corresponding textual statement of the model in OPL. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)
- **P3314** · `fact` · This chapter elaborates on complexity management issues and specifies the various abstracting-refining mechanisms. · [src:S01:L8488-L8505](../../../INBOX/opm-libro.txt#L8488-L8505)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.1 The Need for Complexity Management

- **P3315** · `fact` · Analyzing is the process of gradually increasing the human analyzer’s knowledge about and understanding of the system’s architecture—the system’s structure and behavior combination, which enables it to attain its function. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3316** · `fact` · This is typical of a scientist’s work, who, in a sense, is engaged in reverse- engineering nature and systems in it. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3317** · `fact` · Analogously, designing—a major engineering task—is the process of gradually increasing the amount of details about the system being architected. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3318** · `requirement` · Complexity is inherent in real-life systems: Soon enough during this architecting process, the sheer amount of details contained in any real-world system of reasonable size overwhelms the system analyzer or architect, who must be equipped with a concept and tools to tackle this detail explosion problem. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3319** · `definition` · We cannot do much about the inherent complexity of the system, but by using a simple modeling framework, we can significantly reduce the system’s complicatedness—how complicated it is perceived by a person looking at the model that specifies the system. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3320** · `fact` · OPM strives to minimize complicatedness through simplicity of the language. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3321** · `fact` · Requirements analysis and conceptual design are first steps in the lifecycle of a new system, product or project. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3322** · `fact` · Creating (sometimes unconscious) resistance on the side of the prospective audience—the various stakeholders—to accept the analysis and design results, because they look too complex and thus intimidating, may have the adverse effect of jeopardizing the likelihood of success of subsequent phases of the product development. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3323** · `fact` · The severity and frequency of the detail explosion problem calls for an adequate solution to meet the needs of the systems modeling and analysis community. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3324** · `fact` · A major test of any analysis methodology is therefore complexity management—the extent to which it provides reasonable tools for managing the ever-growing complexity of the modeling outcomes in a coherent, clear, and useful manner. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3325** · `fact` · Such complexity management tools are extremely important for organizing the knowledge that the system architects and designers accumulate and generate during the system architecting and design process. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3326** · `fact` · Equally important is the role of complexity management tools in facilitating the communication of the analysis and design results to other humans, including customers, beneficiaries, peers, superiors and system developers down the development cycle road—implementers, testers, operators, etc. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3327** · `fact` · Trying to incorporate the details into one big diagram, the amount of drawn symbols gets very large, and their interconnections quickly become an entangled web. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3328** · `fact` · Because the diagram has become so cluttered, it is increasingly unwieldy and difficult to comprehend. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3329** · `fact` · System architects experience this detail explosion phenomenon on a daily basis, and anyone who has tried to model a non-toy system of even modest complexity will sympathize with and endorse this description. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3330** · `fact` · This information overload happens even if the language (such as UML and SysML) advocates using multiple diagram kinds for the various system aspects. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3331** · `fact` · While some of the diagram kinds might be simpler than one kind (as in OPM), combining them all to obtain a holistic system view is cognitively much more difficult. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3332** · `requirement` · A system modeling language must include integral mechanisms for controlling and managing this complexity. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)
- **P3333** · `fact` · This entails being able to present and view the system at various levels of detail that are consistent with each other. · [src:S01:L8507-L8547](../../../INBOX/opm-libro.txt#L8507-L8547)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.2 The Model Complexity Assertion

- **P3334** · `fact` · The basic principle of OPM complexity management is the following detail hierarchy OPM principle. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3335** · `requirement` · The Detail Hierarchy OPM Principle Whenever an OPD becomes hard to comprehend due to an excessive amount of details, a new, descendant OPD shall be created. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3336** · `fact` · The creation of the new OPD is done by one of the first two complexity management mechanisms— in-zooming or unfolding—taking advantage of the model fact representation OPM principle. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3337** · `fact` · This principle states that an OPM model fact needs to appear in at least one OPD in order for it to be represented in the model. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3338** · `fact` · Based on this principle, we can omit from the descendant, newly created OPD, in which a specific thing was refined, any model fact that already appeared in the ancestor OPD and is not needed to make some point in the new OPD, without losing that fact from the model. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3339** · `fact` · This way, new OPDs can be kept simple as they need not carry all the “baggage” of their ancestors. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3340** · `fact` · This provides for maintaining any OPD sufficiently simple so it does not overwhelm the limited human cognitive capacity. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3341** · `definition` · The determination of when an OPD becomes too complex due to excessive amount of details is left to the discretion of the modeler, because it cannot be defined by merely fixing a maximal number of model elements in the OPD. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3342** · `fact` · There are other factors, such as regularity, layout, and link crossings that affect comprehension Nonetheless, a modeling tool such as OPCAT should limit the size of the canvas on which a single OPD is drawn. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3343** · `fact` · This indirectly limits the number of entities and enforces periodic use of in- zooming and unfolding. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3344** · `fact` · Since this refinement and detail removal can be done recursively and at any required number of times, we can tackle highly complex systems and still keep the model humanly accessible and comprehensible. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)
- **P3345** · `fact` · Hence we can make the following OPM model complexity assertion: The OPM Model Complexity Assertion Applying refinement mechanisms of in-zooming and unfolding to stateful objects or processes, OPM can conceptually model systems at any level of complexity. · [src:S01:L8549-L8574](../../../INBOX/opm-libro.txt#L8549-L8574)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.3 Aspect-Based Versus Detail-Level-Based Decomposition

- **P3346** · `constraint` · UML and SysML address the problem of managing systems complexity primarily by aspect decomposition—dividing the system model into 14 (UML) and 9 (SysML) different diagram types for modeling various aspects of the system – structure, dynamics, state transitions, timing, etc. difficult transition UML: aspect-based decomposition structure behavior states abstract detailed Advocating the integration of the various system aspects into a single model, the approach OPM takes is orthogonal, detail-based decomposition: Rather than applying a separate model for each system aspect, OPM handles the inherent system complexity by decomposition of the system into a hierarchy of self- similar diagrams of the same single kind—OPDs—via its abstracting-refining mechanisms. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3347** · `fact` · These enable presenting and viewing the system, and the things that comprise it, at various detail levels. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3348** · `fact` · The entire system is completely specified through its OPD set—a set of compatible OPDs, each providing a partial view of the system being investigated or developed, which together provide a full picture of the system. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3349** · `fact` · Each OPD is accompanied by its automatically generated OPL paragraph. decomposition, two thick, solid, vertical lines separate the structure, behavior and state transition aspects from each other. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3350** · `fact` · The thin bidirectional horizontal arrows across these lines symbolize difficult transition among the various models. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3351** · `fact` · The detail-based decomposition is represented by the two thin, dashed, horizontal lines that separate the various levels of detail—abstract, detailed and concrete, from each other. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3352** · `fact` · The thick bidirectional vertical arrows symbolize easy transition among the detail levels. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3353** · `fact` · The diagram is schematic; it by no means implies that horizontally there are only three levels of abstraction in OPM. In fact, this number is not bounded. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
- **P3354** · `fact` · The diagram should also not be interpreted as if vertically there are only three diagram types in a multi-diagram-type approach. · [src:S01:L8576-L8603](../../../INBOX/opm-libro.txt#L8576-L8603)
