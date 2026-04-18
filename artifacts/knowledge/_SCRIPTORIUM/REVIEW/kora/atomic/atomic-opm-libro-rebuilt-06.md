---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-06
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
      n_propositions: 41
      segmented: true
      segment_role: segment
      segment_index: 6
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-06
---

# Atomic opm-libro-rebuilt - Segmento 06

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `41`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `06/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 3 Connecting Things with Links / 3.7 Initial and Final States

- **P0280** · `fact` · As soon as Crashing occurs, Vehicle is affected. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0281** · `constraint` · Figure 3.4 shows this via the effect link, which is the bidirectional arrow between Crashing and Vehicle. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0282** · `fact` · However, the exact nature of the effect—the state change—is not yet specified in the model. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0283** · `fact` · To make the model clearer, we have omitted, for now, the aggregation-participation link from ACR System to Vehicle. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0284** · `constraint` · To make the change explicit, the input and output states of Vehicle in Fig. 3.5 are specified as intact and crashed. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0285** · `fact` · The corresponding OPL sentence is: Vehicle can be intact or crashed. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0286** · `fact` · The input state, intact, is the initial state; that is, the state at which the object starts its lifecycle after being generated. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0287** · `fact` · This is denoted graphically by the thick contour around intact. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0288** · `fact` · The output state, crashed, is the final state; that is, the state from which the object cannot exit. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0289** · `fact` · This is denoted graphically by the double contour around crashed. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0290** · `fact` · Textually, by the corresponding OPL sentence specifies the two states: Vehicle is initially intact and finally crashed. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0291** · `fact` · Using the initial and final state symbols, possibly injured and being helped are designated in Fig. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0292** · `constraint` · 3.5 as the initial and final states of Vehicle Occupants Group, respectively: Vehicle Occupants Group is initially possibly injured and finally being helped. the input and output states of Vehicle. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0293** · `fact` · The event link from the crashed state of Vehicle triggers Automatic Crash Responding Having specified the states of Vehicle, we replace the single effect link between Crashing and Vehicle by an input-output link pair. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0294** · `fact` · The semantics of this change can be best understood by examining the OPL sentences generated before and after this replacement. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0295** · `fact` · Originally, the OPL sentence that corresponded to the OPD in Fig. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0296** · `constraint` · 3.4 read as follows: Crashing affects Vehicle. After replacing the effect link in Fig. 3.4 by the input-output link pair in Fig. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0297** · `constraint` · 3.5, the OPL sentence is: Crashing changes Vehicle from intact to crashed. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0298** · `fact` · The latter sentence is clearly more informative, as it tells us specifically from what input state to what output state the Crashing process changed Vehicle. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)
- **P0299** · `fact` · However, this additional detail comes at the expense of loading the OPD with two links—the input and output links—instead of the single effect link. · [src:S01:L1056-L1086](../../../INBOX/opm-libro.txt#L1056-L1086)

## opm libro · Chapter 3 Connecting Things with Links / 3.8 Triggering State and Event Link

- **P0300** · `fact` · As soon as Vehicle enters its crashed state, the function of the ACR System—Automatic Crash Responding—is triggered. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0301** · `fact` · To model this, we draw an instrument event link from the state crashed to the process Automatic Crash Responding. As Fig. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0302** · `constraint` · 3.5 shows, an instrument event link is a procedural link that is graphically similar to an instrument link with an additional control modifier—the letter e next to the circle. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0303** · `fact` · The semantics of this link is a combination of the semantics of the instrument link with that of triggering an event. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0304** · `fact` · In our case, this links denotes the fact that entry of Vehicle into its crashed state is an event that initiates the process to which it is linked. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0305** · `fact` · In other words, the semantics of the event link is that once Vehicle enters the crashed state (from which the event link originates), the Automatic Crash Responding process (to which the event link is directed) is initiated. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0306** · `fact` · The instrument component of the link indicates that Vehicle is not transformed (neither consumed nor changes its state) by the Automatic Crash Responding process it triggers. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0307** · `fact` · The OPL sentence generated in response to inserting this event link is: Crashed Vehicle initiates Automatic Crash Responding, which requires crashed Vehicle. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0308** · `fact` · This OPL sentence reflects the combined semantics of the event control modifier, which is expressed by the reserved OPL word initiates, with that of the instrument link, which is expressed by the reserved OPL word requires. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)
- **P0309** · `fact` · AS the sentence demonstrates, Vehicle at its crashed state is simply crashed Vehicle. · [src:S01:L1090-L1105](../../../INBOX/opm-libro.txt#L1090-L1105)

## opm libro · Chapter 4 SysML: Use Case, Block, and State Machine Diagrams

- **P0310** · `fact` · SysML supports the specification, analysis, design, verification, and validation of a broad range of complex systems. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0311** · `fact` · These systems may include hardware, software, information, processes, personnel, and facilities. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0312** · `constraint` · OMG SysML, v1.3 p.1 ( ) Accessed June 20, 2014 We leave OPM for a while and turn to start our parallel SysML model. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0313** · `fact` · SysML is a multi-view language, where each view uses a different type of diagram. There are nine SysML diagram types in total. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0314** · `fact` · In this chapter we are exposed to three diagram types: the use case diagram, the block definition diagram, and the state machine diagram. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0315** · `fact` · The use case diagram shows the context of the system and how the system is used to bring value to at least one of its actors. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0316** · `fact` · The block definition diagram presents the blocks of the system—major entities of interest. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0317** · `fact` · The state machine diagram shows how states of blocks in the system are changed. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0318** · `fact` · Comparing OPM and SysML, we already see that the approaches they take are different and complementary. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0319** · `fact` · OPM uses a single model that combines the various system aspects, while SysML uses a number of diagram types, each focusing on some particular aspect of the system. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
- **P0320** · `fact` · A use case is a way the system is used, a service it provides to at least one of its users. · [src:S01:L1145-L1159](../../../INBOX/opm-libro.txt#L1145-L1159)
