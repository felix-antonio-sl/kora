---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-04
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
      segment_index: 4
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-04
---

# Atomic opm-libro-rebuilt - Segmento 04

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `63`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `04/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 2 Text and Simulation Enhancements / 2.3 Animated Execution of the OPM Model

- **P0166** · `constraint` · One of the most attractive and useful features of an OPM model, which enables it to be visualized and tested, is its executability; that is, the ability to simulate a system by executing its model via animation in a properly designed software environment.2 hand side shows the system before the Automatic Crash Responding process occurs. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0167** · `fact` · At this stage, Vehicle Occupants Group is at its input state, possibly injured, which is marked by the state being solid (colored brown). Responding process starts. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0168** · `fact` · Center: the process in action; the object is in transition from its input state to its output state. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0169** · `fact` · Right: the system after the Automatic Crash Responding process has terminated The screenshot in the center of Fig. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0170** · `constraint` · 2.4 shows the process in action, marked as solid (colored blue). · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0171** · `fact` · During the time that the Automatic Crash Responding process is active (that is, when it executes), the object Vehicle Occupants Group is in transition from its input state, possibly injured, to its output state, being helped. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0172** · `fact` · This is marked by both states being semi-solid (light brown). · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0173** · `fact` · Observing the animation in action reveals that the input state gradually fades out while the output state becomes solid. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0174** · `fact` · At the same time, two red dots, shown in the middle of both arrows, travel along the input-output link pair, denoting the “control” of the system; that is, where the system is at each time point. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0175** · `fact` · One red dot travels from the input state to the affecting process. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0176** · `fact` · At the same time, the second dot travels from the process along the output link to the output state. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0177** · `fact` · Finally, the screenshot on the right shows the system after the Automatic Crash Responding process had terminated. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0178** · `fact` · At this stage, Vehicle Occupants Group is at its output state, being helped. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0179** · `fact` · The animated execution of the system model has several benefits. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0180** · `fact` · Firstly, it is a dynamic visualization aid, which helps both the modeler and the target audience to follow and understand the behavior of the system over time. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0181** · `fact` · Secondly, similar to a debugger of a programming language, it facilitates verification of the system’s dynamics and spotting of logical design errors in its flow of control. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)
- **P0182** · `fact` · Therefore, it is highly recommended that the system model be animated frequently as it is being constructed, so that design errors do not accumulate, but are corrected as soon as they are made. · [src:S01:L792-L821](../../../INBOX/opm-libro.txt#L792-L821)

## opm libro · Chapter 3 Connecting Things with Links

- **P0183** · `fact` · express the relationships between the two concepts. … Picking the appropriate linking words to clearly express the relationship between two concepts is possibly the most difficult task during the construction of concept maps. Alberto J. · [src:S01:L850-L856](../../../INBOX/opm-libro.txt#L850-L856)
- **P0184** · `constraint` · Cañas, cmap.ihmc.us/docs/linkingwords.html (retrieved 2014) Links are graphical expressions of relations between things. · [src:S01:L850-L856](../../../INBOX/opm-libro.txt#L850-L856)
- **P0185** · `fact` · OPM links connect processes with objects or their states, providing meaning to relationships among them. · [src:S01:L850-L856](../../../INBOX/opm-libro.txt#L850-L856)
- **P0186** · `fact` · This chapter expands the use of links in our model and explains the semantics of various kinds of links. · [src:S01:L850-L856](../../../INBOX/opm-libro.txt#L850-L856)

## opm libro · Chapter 3 Connecting Things with Links / 3.1 Procedural Links Versus Structural Links

- **P0187** · `fact` · The links we have been using so far—the effect link and the input and output links—are procedural links. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)
- **P0188** · `fact` · A procedural link is a link that specifies a dynamic aspect of the system by connecting an object (or one of its states) and a process. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)
- **P0189** · `fact` · Procedural links can be transforming or enabling. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)
- **P0190** · `fact` · Transforming links express transformation— generation, consumption, or state change—of the object by the process to which it is linked. Enabling links express enablement. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)
- **P0191** · `fact` · They connect a process to an enabler—an object that enables the occurrence of that process but is not transformed by that process. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)
- **P0192** · `fact` · Structural links model the structure of the system by expressing long-term relations between things in the model. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)
- **P0193** · `fact` · Structural links include aggregation-participation (whole-part), generalization-specialization, and other long-lasting relations. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)
- **P0194** · `fact` · A structural link is a link that specifies a static aspect of the system by connecting an object to another object or a process to another process. · [src:S01:L858-L869](../../../INBOX/opm-libro.txt#L858-L869)

## opm libro · Chapter 3 Connecting Things with Links / 3.2 Adding Enablers

- **P0195** · `fact` · The top-level OPD that we have been modeling is called the System Diagram (SD). · [src:S01:L871-L886](../../../INBOX/opm-libro.txt#L871-L886)
- **P0196** · `constraint` · Often called a context diagram, the SD provides a “50,000-foot view” of the system. · [src:S01:L871-L886](../../../INBOX/opm-libro.txt#L871-L886)
- **P0197** · `fact` · It allows the modeler and all the stakeholders interested in understanding the system via its OPM model to quickly grasp the function—the main process of the system, which in this case is Automatic Crash Responding. The SD also shows the beneficiary. · [src:S01:L871-L886](../../../INBOX/opm-libro.txt#L871-L886)
- **P0198** · `fact` · In our case, Vehicle Occupants Group is also the operand of the system; it is the main object transformed by the system’s function, with its input and output states. · [src:S01:L871-L886](../../../INBOX/opm-libro.txt#L871-L886)
- **P0199** · `fact` · We are not quite done yet; while the function and the operand are important, they do not provide the full picture of the system, even at this most abstract level. · [src:S01:L871-L886](../../../INBOX/opm-libro.txt#L871-L886)
- **P0200** · `fact` · Objects that enable this function should be presented in addition to the beneficiary. · [src:S01:L871-L886](../../../INBOX/opm-libro.txt#L871-L886)
- **P0201** · `fact` · These enablers include human and non-human objects, which in OPM are referred to as agents and instruments, respectively. · [src:S01:L871-L886](../../../INBOX/opm-libro.txt#L871-L886)

## opm libro · Chapter 3 Connecting Things with Links / 3.2.1 Adding an Agent and an Agent Link

- **P0202** · `fact` · Reading through our system description, we note that the advisor is a major human player in our system, so we would like to model her. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0203** · `fact` · A human, as part of an OPM system, is an object referred to as an agent. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0204** · `fact` · An agent of a process is a human or a group of humans that interacts with the system to enable and/or control that process, but is not transformed by it. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0205** · `fact` · Vehicle Occupants Group possibly injured being helped Automatic Crash Responding Advisor Automatic Crash Responding. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0206** · `fact` · The optional stick figure also indicates that the object is a human The agent link, , shown in Fig. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0207** · `constraint` · 3.1, is a “black lollipop”—a connecting line starting at the object and ending with a black circle at the process end. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0208** · `fact` · This symbol denotes that the object linked to the process is a human whose presence is mandatory for the process to happen. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0209** · `fact` · The agent link indicates that there is a “human in the loop”, usually indicating that an interface is required between the human—the agent—and the system in order for the agent to interact with it. Fig. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0210** · `constraint` · 3.1 shows Advisor added as an agent to the Automatic Crash Responding process. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0211** · `fact` · The process cannot start or be sustained without the agent, but the process does not transform the agent: It does not create or consume it, nor does it change the agent’s state. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0212** · `fact` · Hence, agent is a human enabler of the process. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0213** · `fact` · The OPL sentence that is generated as a result of adding the agent link is: Advisor handles Automatic Crash Responding. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0214** · `fact` · The OPL reserved word handles denotes the need for an agent to enable the process. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0215** · `fact` · While the Vehicle Occupants Group object is a group of people, they not an agent. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)
- **P0216** · `fact` · These people are the beneficiary and operand of the system—they do change and are hence transformed by the system’s function and benefit from it. · [src:S01:L888-L915](../../../INBOX/opm-libro.txt#L888-L915)

## opm libro · Chapter 3 Connecting Things with Links / 3.2.2 Adding an Instrument and an Instrument Link

- **P0217** · `fact` · While Advisor is an agent (a human enabler), our system also has an inanimate enabler—an instrument. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0218** · `requirement` · The instrument that enables the system’s function, Automatic Crash Responding, is the automatic crash response (ACR) system, which we shall call ACR System. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0219** · `fact` · The instrument is denoted by an instrument link—a white lollipop, . · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0220** · `fact` · Similar to the agent link, the instrument link is a line that connects the object to the process that requires that instrument. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0221** · `fact` · Like the agent, while the instrument is needed for the process to happen, the instrument is not transformed (created, consumed, or affected) by the occurrence of this process. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0222** · `fact` · An instrument of a process is a non-human that interacts with the system to enable and/or control that process, but is not transformed by it. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0223** · `fact` · Vehicle Occupants Group possibly injured being helped ACR System Automatic Crash Responding Advisor System to Vehicle Occupants Group Occupants Group. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0224** · `fact` · The instrument link is the line ending with a blank circle at the process end, which denotes that the object at the origin of the link is an instrument with respect to this process. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0225** · `fact` · An instrument is an inanimate, non-human enabler of the process; in other words, the process cannot start or take place without the existence and availability of the instrument throughout the process duration. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0226** · `fact` · Like the agent, the instrument is not transformed as a result of the process occurrence. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0227** · `fact` · The OPL sentence that OPCAT generated as a result of adding the instrument link is: Automatic Crash Responding requires ACR System. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
- **P0228** · `fact` · The OPL reserved word requires denotes the need for an instrument to enable the process. An enabler is an agent or an instrument. · [src:S01:L917-L945](../../../INBOX/opm-libro.txt#L917-L945)
