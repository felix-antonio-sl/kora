---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-07
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
      segment_index: 7
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-07
---

# Atomic opm-libro-rebuilt - Segmento 07

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `63`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `07/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 4 SysML: Use Case, Block, and State Machine Diagrams / 4.1 The SysML Use Case Diagram

- **P0321** · `fact` · We start our model with the use case diagram, since this is the view that is used to elicit requirements and to provide initial understanding of the system and its surroundings. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0322** · `constraint` · According to the OMG SysML 1.3 (2012) standard, a use case diagram “describes the usage of a system (subject) by its actors (environment) to achieve a goal that is realized by the subject providing a set of services to selected actors” (OMG SysML 1.3, 2012, p.145). · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0323** · `fact` · Before drawing use case diagrams, use cases need to be written in text. This text takes on different formats. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0324** · `fact` · Depending on need, use cases are written in varying degrees of formality. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0325** · `fact` · They can be brief—short one-paragraph summary, usually of the main success scenario; casual—informal paragraph format, where multiple paragraphs describe various scenarios; and fully dressed—the most elaborate level, where all the steps and variations are written in detail, and there are supporting sections, such as preconditions and success guarantees. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0326** · `fact` · The name of the use case in our use case model is “Automatically respond to crash.” As Fig. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0327** · `constraint` · 4.1 shows, the use case is depicted as an oval with the name inside it. The system users are called actors. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0328** · `fact` · An actor is an external entity that interacts with the system and can get services from it. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0329** · `constraint` · An actor is depicted either as a human stick figure, or as the stereotype «actor»; see Table 4.1. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0330** · `constraint` · Two actors appear in the use case diagram in Fig. 4.1: Vehicle Occupants and Advisor. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0331** · `fact` · An actor is by definition an external entity. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0332** · `fact` · Unlike OPM, SysML does not require that the actor be a person; it can be anything with which the system interacts. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0333** · `fact` · Vehicle Occupants are undoubtedly an external entity, since they are not part of the system, but rather its users and beneficiaries. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0334** · `fact` · The case for the Advisor is not that clear-cut, since the Advisor can be considered as part of the system, and rather than getting a service from the system, she is the one that provides the service. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0335** · `fact` · However, the requirement that an actor gets a service is not mandatory, and as a human, the Advisor interacts with the system. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0336** · `fact` · In this model, we exclude humans from being considered part of the system; hence Advisor is also an actor. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0337** · `fact` · Each one of the two actors is linked to the use case via a communication path—a line between the actor and the use case. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0338** · `fact` · The system which provides the required function in a use case diagram is called subject. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0339** · `fact` · A subject in a use case diagram is the system that provides the service. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0340** · `fact` · A use case subject is depicted as a rectangle with the subject name at the rectangle's top center. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0341** · `fact` · As The entire use case diagram is depicted within a diagram frame—a rectangle that is required for any SysML diagram. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0342** · `fact` · In its upper leftmost corner, a diagram frame has name tag—a rectangle with a tapered bottom right corner—which contains the heading name. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0343** · `fact` · The heading name has the following syntax: [modelElementType] [diagramName] The fields diagramKind, which is bolded, and modelElementName are mandatory. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0344** · `fact` · Each diagramKind has a two or three lower case letter abbreviation. As shown in Fig. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0345** · `constraint` · 4.1, the diagramKind of our use case is uc, while the diagramName is ACR-System. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0346** · `fact` · The two other tokens, modelElementType and diagramName are optional, and if they appear, they are enclosed within brackets, enabling the diagram reader to tell them apart. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0347** · `constraint` · Table 4.1 lists the main elements of a use case diagram, their semantics and symbols. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0348** · `constraint` · Table 4.1 The main elements of a use case diagram, their semantics and symbols Guillemets, also known as the symbols for rewind («) and fast forward (»), are angle quotes, as the ones surrounding the following word: «guillemets». · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0349** · `fact` · In SysML, a word within a pair of guillemets denotes a stereotype—an extensibility mechanism that enables creating new model elements. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0350** · `constraint` · A stereotype is depicted as a rectangular box with the stereotype name, such as “block” within a pair of guillemets, «block», recorded in the top middle of the box, as is the case with «actor» in Table 4.1. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)
- **P0351** · `fact` · The name of the actor, ActorName, is recorded beneath the «actor» stereotype notation. · [src:S01:L1161-L1217](../../../INBOX/opm-libro.txt#L1161-L1217)

## opm libro · Chapter 4 SysML: Use Case, Block, and State Machine Diagrams / 4.2 SysML Blocks and the Block Definition Diagram

- **P0352** · `definition` · A SysML block is a modular component which defines a collection of features that describe a part of the system or another element of interest. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0353** · `fact` · A SysML block, which roughly corresponds to a UML class, may include both structural and behavioral features, such as properties and operations. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0354** · `fact` · A block can include properties to specify its values, parts, and references to other blocks. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0355** · `fact` · The block definition diagram captures the definition of blocks in terms of properties and operations, and relationships, such as a system hierarchy or a system classification tree. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0356** · `fact` · A related SysML diagram is the internal block diagram (ibd), which captures the internal structure of a block in terms of properties and connectors between properties. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0357** · `definition` · A SysML block definition diagram (bdd) defines features of blocks and relationships between blocks, such as associations, generalizations, and dependencies. system. The diagramKind, bdd, denotes this. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0358** · `fact` · This bdd expresses the two major blocks of the system and the relation between them, as well as the major actors and their relations the blocks. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0359** · `fact` · This two blocks in the bdd are ACR-System and Automatic-Crash-Response. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0360** · `fact` · They are linked by the ReferenceAssociation labeled “provides”. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0361** · `fact` · Advisor is shown as an actor which is part of the ACR-System. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0362** · `fact` · This whole-part relation is expressed by the black diamond, the SysML symbol for whole-part relation. Vehicle Occupants is another actor. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0363** · `constraint` · It is linked by the ReferenceAssociation labeled “benefit from” to the Automatic-Crash-Response block (Fig. 4.2). · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0364** · `definition` · Table 4.2 The main elements of a block definition diagram, their semantics and symbols Element: Symbol Semantics Block A modular component which defines a col- lection of features to describe a part of the system or another element of interest. «block» BlockName Actor: An external entity that interacts with the system and can get services from it «actor» ActorName ActorName ReferenceAssociation: A link between blocks indicating the nature of their association association1 property1 0..1 {ordered} 1.. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0365** · `constraint` · PartAssociation: A link between blocks indicating that the block linked to the diamond is the whole association1 property1 0..1 {ordered} 1.. · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)
- **P0366** · `fact` · Generalization: A link between two block indicating that the block linked to the triangle is the general one · [src:S01:L1221-L1272](../../../INBOX/opm-libro.txt#L1221-L1272)

## opm libro · Chapter 4 SysML: Use Case, Block, and State Machine Diagrams / 4.3 SysML State Machine Diagram

- **P0367** · `fact` · SysML has a diagram type that is dedicated to modeling states of a block and possible transitions among them—the state machine diagram, or stm in short. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0368** · `definition` · Following the idea presented initially by Harel (1987, 1988), the SysML State Machine package defines a set of concepts that can model discrete behavior through state transitions. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0369** · `fact` · The state machine can represent behavior, expressed as the state history of an object in terms of its transitions and states. the OPD in Fig. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0370** · `constraint` · 2 .3 in that both contain the same two states for the Vehicle Occupants Group. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0371** · `fact` · The stm symbol used to denote a state is a rountangle—the same as in OPM. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0372** · `fact` · The main difference between the two is that stm is not of the entire ACR system. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0373** · `fact` · Rather, it is only of the Vehicle Occupants Group block. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0374** · `constraint` · The OPM process Automatic Crash Responding is expressed in the stm as a trigger by the same name, which causes the transition from the possibly injured state to the being helped state. The black circle in Fig. 4.3 is the initial state. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0375** · `fact` · This state is referred to as a pseudo state since it is not a real state, just an indication to the diagram reader where to start. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0376** · `fact` · It is linked to the initial state, possibly injured, of the block whose state machine is modeled, which in our case is Vehicle Occupants Group. The black circle with the white rim in Fig. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0377** · `constraint` · 4.3 is the final (pseudo) state—it is pointed to by the (real) final state—being helped. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0378** · `fact` · These two symbols enable identification of the initial and final states in a state machine diagram, respectively. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0379** · `requirement` · As we shall see later, OPM denotes an initial state using a bold line of the state rountangle frame, and a final state—by a double rountangle frame. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0380** · `fact` · This eliminates the need for the two kinds of pseudo states that SysML uses. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0381** · `constraint` · Table 4.3 The main elements of a state machine diagram, their semantics and symbols Table 4.3 shows the main elements of a state machine diagram, their semantics and symbols. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0382** · `fact` · As the table shows, a state can be composite and contain inner, lower-level processes. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
- **P0383** · `fact` · A transition can be labeled, in addition to a trigger, also by an optional guard in brackets and one or more optional activities that syntactically follow the backslash symbol (\), which are actions done during the transition. · [src:S01:L1274-L1302](../../../INBOX/opm-libro.txt#L1274-L1302)
