---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-70
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
      n_propositions: 55
      segmented: true
      segment_role: segment
      segment_index: 70
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-70
---

# Atomic opm-libro-rebuilt - Segmento 70

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `55`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `70/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.19 Middle-Out as the De-facto Architecting Practice

- **P3604** · `fact` · Ideally, analysis and design start at the top and make their way gradually to the bottom—from the general to the detailed. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3605** · `fact` · In real life, however, analysis typically starts at some arbitrary detail level and is rarely linear. The design is not linear either. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3606** · `fact` · Usually, these are iterative processes, during which knowledge, followed by understanding, is gradually accumulated and refined. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3607** · `fact` · The system architect cannot know in advance the precise structure and behavior of the very top of the system—this requires analysis and becomes apparent at some point along the analysis process. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3608** · `fact` · Step by step, the analyst builds the system specification by accumulating and recording facts and observations about things in the system and relations among them. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3609** · `fact` · Due to the non-linear nature of the analysis and design processes, linear, unidirectional “bottom-up” or “top-down” approaches, while seeming highly methodical, are rarely applicable to real-world systems. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3610** · `fact` · Rather, it is frequently the case that the system under construction or investigation is so complex and unexplored, that neither its top nor its bottom is known with certainty from the outset. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3611** · `fact` · More commonly, analysis and design of real-life systems start in an unknown place along the system’s detail level hierarchy. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3612** · `fact` · The analysis proceeds “middle-out” by combining top-down and bottom-up techniques to obtain a complete comprehension and specification of the system at all the detail levels. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3613** · `fact` · It thus turns out that even though architects usually strive to work in an orderly top-down fashion, more often than not, the de-facto practice is the middle-out mode of analysis and design. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)
- **P3614** · `requirement` · Rather than trying to fight it, system modeling approaches and tools must provide facilities to handle this middle-out architecting mode along with support for top-down and bottom up approaches. · [src:S01:L9150-L9168](../../../INBOX/opm-libro.txt#L9150-L9168)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.19.1 OPM Caters to the Mixed Approach

- **P3615** · `fact` · Using OPM, the accumulated knowledge is documented and represented as interconnected model facts through a set of OPDs and their corresponding OPL paragraphs. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3616** · `fact` · If the OPD that is being augmented becomes too crowded, busy, or unintelligible, a new OPD is created. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3617** · `fact` · This descendant OPD repeats one or more of the things in its ancestor OPD in a refined form. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3618** · `fact` · These repeated things establish the link between the ancestor and descendant OPDs. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3619** · `fact` · The descendant OPD does not usually replicate all the details of is ancestor, as some of them are abstracted, while others are simply not included. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3620** · `fact` · This new OPD is therefore amenable to refinement of new things to be laid out in the space that was saved by not including things from the ancestor OPD. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3621** · `fact` · In other words, there is room in it to insert a certain amount of additional details before it gets too cluttered. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3622** · `fact` · When this happens, a new cycle of refinement takes place, and this goes on until the entire system has been completely specified. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)
- **P3623** · `fact` · As we have seen in this chapter, OPM caters not only to this top-down approach, but also to bottom-up and middle-out via abstracting and OPD simplifying along with the addition of an interim detail level. · [src:S01:L9170-L9181](../../../INBOX/opm-libro.txt#L9170-L9181)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.19.2 When Should a New OPD Be Created?

- **P3624** · `fact` · An OPD set has to be readable and easy to follow and comprehend. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3625** · `fact` · The following rules of thumb are helpful in deciding when a new OPD should be created so OPDs are as easy to read and grasp as possible. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3626** · `fact` · The OPD should not stretch over more than one page or one average-size monitor screen. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3627** · `constraint` · The OPD should not contain more than 20–25 entities (objects, processes or states). · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3628** · `requirement` · Things (objects or processes) must not occlude each other. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3629** · `fact` · They are either completely contained within higher-level things, in case of zooming, or have no overlapping area. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3630** · `constraint` · An exception to this guideline is when port folding (See Sect. 21.8) is applied. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3631** · `fact` · The diagram should not contain too many links. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3632** · `fact` · A link should not cross the area occupied by a thing. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)
- **P3633** · `fact` · The number of links crossing each other should be minimized. · [src:S01:L9183-L9194](../../../INBOX/opm-libro.txt#L9183-L9194)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.20 Navigating Within an OPM System Model

- **P3634** · `fact` · Since, as we have seen, an OPM model can be very large navigation inside the model and orientation becomes an issue. · [src:S01:L9196-L9197](../../../INBOX/opm-libro.txt#L9196-L9197)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.20.1 OPM Diagram Labels and Tree Edge Labels

- **P3635** · `fact` · The OPM system name is the name of the OPM model that specifies the system. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3636** · `fact` · An OPD name is the name that identifies each OPD in the OPD process tree. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3637** · `requirement` · SD shall contain one and only one systemic process, which represents the overarching system function that delivers functional value to stakeholders. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3638** · `fact` · It may, in addition, to contain one or more environmental processes. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3639** · `fact` · SD is the label of the root OPD in the OPD tree. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3640** · `constraint` · The OPD tree root, SD, occupies level (tier) 0 in the OPD tree and it is the single node at this level. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3641** · `fact` · Higher numbered tiers, i.e., those corresponding to successive refinements, may have more than one OPD. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3642** · `fact` · Not only the nodes in the OPD tree are labeled; the edges are too. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3643** · `fact` · Each edge (an arc connecting two nodes—two OPDs) in the OPD tree has a unique label. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3644** · `fact` · The label expresses a refinement relation that corresponds to the implicit invocation link or unfolding relation. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3645** · `fact` · Considering each OPD to be an object and the entire OPD process tree to be a single OPD, each edge is a unidirectional tagged structural link with a tag that reads: “is refined by in-zooming in ”, or “is refined by unfolding in ”. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3646** · `constraint` · An OPD refinement OPL sentence is an OPL sentence describing the refinement relation between a refineable present in a tierN OPD and its refining OPD in tierN+1. · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3647** · `fact` · The syntax of an in- zoomed OPD refinement OPL sentence is: is refined by in-zooming in . · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)
- **P3648** · `fact` · Similarly, the syntax of an unfolded OPD refinement OPL sentence is: is refined by unfolding in . · [src:S01:L9199-L9216](../../../INBOX/opm-libro.txt#L9199-L9216)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.20.2 Whole System OPL Specification

- **P3649** · `fact` · An OPL paragraph is the collection of OPL sentences that together specify in text what the corresponding OPD specifies graphically. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3650** · `fact` · An OPL paragraph name, using the OPD name, may precede the first OPL sentence of each OPL paragraph. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3651** · `fact` · An OPD model specification is the collection of successive OPDs in the system’s OPD tree. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3652** · `fact` · An OPL model specification is the collection of successive OPL paragraphs corresponding to the OPDs in the system’s OPD tree, from which duplicate OPL sentences were removed. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3653** · `fact` · An OPM model specification is a side-by-side presentation of the OPD model specification and the corresponding OPL paragraph is presented to the right of each OPD. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3654** · `constraint` · An example of an OPM model specification is presented in Table 21.2, which contains the entire OPM model of the Dish Washing system in Fig. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3655** · `constraint` · 10.5.An OPM model specification of a system begins with a starting title, as in Dish Washing System OPM model specification. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3656** · `fact` · The left column contains the OPDs in the OPM system’s OPD set in a breadth-first order, but the modeler may override this default order. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)
- **P3657** · `fact` · The corresponding OPL paragraphs are listed on the right column, such that each OPL paragraph is to the right of its OPD. · [src:S01:L9218-L9236](../../../INBOX/opm-libro.txt#L9218-L9236)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links

- **P3658** · `constraint` · Control Flow Semantics presents a unified, formal treatment of the semantics of a wide spectrum of control flow notions as found in sequential, concurrent, logic, object-oriented, and functional programming languages. de Bakker and de Vink (1996) To control the flow of system execution, OPM has precise operational semantics, based on the event- condition-action paradigm and expressed by modifying the procedural links with control modifiers— event and condition symbols. This is the focus of this chapter. · [src:S01:L9328-L9334](../../../INBOX/opm-libro.txt#L9328-L9334)
