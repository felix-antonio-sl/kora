---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-05
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
      n_propositions: 51
      segmented: true
      segment_role: segment
      segment_index: 5
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-05
---

# Atomic opm-libro-rebuilt - Segmento 05

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `51`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `05/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 3 Connecting Things with Links / 3.3 Adding Structural Links

- **P0229** · `fact` · At this stage in the modeling of the system, we have already modeled a portion of the system diagram (SD), which is the top-level OPD. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0230** · `fact` · An additional thing (object or process) that we should include in the SD is the Vehicle, since this is the object that the driver and passengers occupy—the Vehicle Occupants Group—and it is also part of the ACR system. occupies Vehicle Occupants Group possibly injured being helped ACR System Vehicle Automatic Crash Responding Advisor Vehicle is added with the tag “occupies” two links are called structural links. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0231** · `fact` · The first is aggregation-participation link, from ACR System to Vehicle. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0232** · `fact` · The second link is tagged structural link from Vehicle Occupants Group to Vehicle. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0233** · `fact` · We next discuss each one of these structural links. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0234** · `fact` · Vehicle is connected via an aggregation-participation (whole-part) link as part of the ACR System. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0235** · `fact` · The aggregation-participation symbol is , a solid equilateral triangle with its tip directed upwards and linked to the whole, and its base linked to the part or parts. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0236** · `fact` · This graphical aggregation-participation link is expressed textually the following OPL sentence: ACR System consists of Vehicle. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0237** · `fact` · The OPL reserved phrase consists of denotes the aggregation-participation relation, with the whole (ACR System in our case) preceding it and the part (Vehicle in our case), or parts, following it. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0238** · `fact` · Vehicle is connected to Vehicle Occupants Group via a second type of structural link—the tagged structural link. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0239** · `fact` · A tagged structural link is an open arrow that points from one object to another. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0240** · `definition` · The tag is a “user-defined” phrase—a phrase that is defined by the modeler and recorded along the link, expressing the nature of the structural relation between the two connected objects (or processes). In our model, the link’s tag is occupies. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0241** · `definition` · It is bold since it is defined by the modeler and is not an OPL reserved phrase. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0242** · `fact` · Adding the tagged structural link initiates the generation of the following OPL sentence: Vehicle Occupants Group occupies Vehicle. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0243** · `fact` · Tags in tagged structural links provide the modeler with the ability to express the semantics of any structural relation between any two objects or any two processes in the system. · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)
- **P0244** · `fact` · As the above OPL sentence demonstrates, a tagged structural link gives rise to an OPL sentence in which the name of the object connected to the source of the link’s arrow appears first (Vehicle Occupants Group in our case), followed by the tag name (occupies), followed by the name of the object connected to the destination of the link’s arrow (Vehicle). · [src:S01:L947-L986](../../../INBOX/opm-libro.txt#L947-L986)

## opm libro · Chapter 3 Connecting Things with Links / 3.4 Physical Versus Informatical Things

- **P0245** · `fact` · Things (objects or processes) are classified by their essence attribute into two kinds: physical things and informatical things. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0246** · `constraint` · All the objects in our model so far have been physical, as denoted in Fig. 3.3 by the shadow behind each object. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0247** · `fact` · The default essence value of a thing can be determined by the system modeler. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0248** · `fact` · If the system is an information system, it makes sense to set the default essence value of a thing as informatical, because most of the things in such a system would be informatical. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0249** · `fact` · In this case, if a thing is informatical and it is already mentioned in at least one OPL sentence, no additional OPL sentence is required to indicate that this thing is informatical. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0250** · `fact` · If, however, the thing is physical, this is denoted in a dedicated OPL sentence. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0251** · `fact` · For example, assuming that the system we are modeling was set with informatical essence value, the OPL sentence below was added to denote the fact that the essence of Vehicle is physical. Vehicle is physical. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0252** · `fact` · As for Automatic Crash Responding, which is our main process and the system’s function, it is possible at this point to say that it is informatical, because it only involves conveying the information that the vehicle has been involved in a crash and that there has been a subsequent call for help for its occupants. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0253** · `fact` · The actual helping process, which is physical, is outside the scope of this system. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)
- **P0254** · `fact` · The essence of the Automatic Crash Responding process can be changed later to physical if we realize that it involves one or more physical subprocesses. · [src:S01:L988-L1004](../../../INBOX/opm-libro.txt#L988-L1004)

## opm libro · Chapter 3 Connecting Things with Links / 3.5 Model Facts and OPL Paragraphs

- **P0255** · `fact` · As we have seen, each time we introduced a link between two things or changed the essence of a thing from informatical to physical, at least one OPL sentence was added or modified. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0256** · `fact` · Thus, as we model, facts start accumulating and be expressed in the model. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0257** · `fact` · A model fact is a relation between things or states in the model. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0258** · `fact` · We have been gradually accumulating OPL sentences, which collectively constitute the OPL paragraph and together the textual modality. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0259** · `fact` · The OPL paragraph describes in plain English precisely what the OPD—the graphical modality—describes visually. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0260** · `fact` · Currently, the OPL paragraph reads as follows. Vehicle Occupants Group is physical. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0261** · `fact` · Vehicle Occupants Group can be possibly injured or being helped. Vehicle Occupants Group occupies Vehicle. Advisor is physical. Advisor handles Automatic Crash Responding. ACR System is physical. ACR System consists of Vehicle. Vehicle is physical. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0262** · `fact` · Automatic Crash Responding requires ACR System. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0263** · `fact` · Automatic Crash Responding changes Vehicle Occupants Group from possibly injured to being helped. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)
- **P0264** · `fact` · In order to save space, we take the liberty to omit the sentences expressing the physical essence of things in most of the OPL paragraph examples that follow, since this is obvious from the shading in the OPD. · [src:S01:L1008-L1028](../../../INBOX/opm-libro.txt#L1008-L1028)

## opm libro · Chapter 3 Connecting Things with Links / 3.6 Environmental Versus Systemic Things

- **P0265** · `fact` · The text that we have started using as the basis of our model is not written in a way that facilitates the modeling process. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0266** · `fact` · Details about the system’s structure and behavior are scattered throughout the text. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0267** · `fact` · We first encounter the crash in the sentence “The accelerometer … measures the crash severity.” Later we read: “Within seconds of a moderate-to-severe crash …” Combining these specifications with our previous personal knowledge about car crashes, we realize that the specification author meant to express the fact that a Crashing process has occurred. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0268** · `fact` · This process is not systemic; that is, it is not part of the system. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0269** · `fact` · Rather, it is external to the system—it happens in the system’s environment: Crashing adversely affects Vehicle and possibly the Vehicle Occupants Group, and the ACR System needs to respond to the outcomes of this unfortunate process. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0270** · `fact` · Things that are not part of the system, but interact with it, are referred to as environmental. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0271** · `fact` · These environmental things are contrasted with systemic things—things that are part of the system. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0272** · `fact` · Graphically, environmental things are marked by a dashed contour, as opposed to the solid contour of systemic things. In Fig. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0273** · `constraint` · 3.4, Crashing can be identified as an environmental process by its dashed contour and as a physical process by its shading. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0274** · `fact` · This is also reflected in the following OPL sentence: Crashing is environmental and physical. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0275** · `fact` · Vehicle Occupants Group can also be considered as environmental, because it is not part of the ACR System but rather the beneficiary and the operand—the object on which the system operates to transform it. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0276** · `fact` · In our case, the transformation is from the possibly injured state to the state of being helped. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0277** · `constraint` · Figure 3.4 displays Vehicle Occupants Group as a physical object by its shading. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0278** · `fact` · This is also reflected in the following OPL sentence: Vehicle Occupants Group is physical. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
- **P0279** · `fact` · The thing’s attribute whose values are systemic and environmental is called affiliation. · [src:S01:L1030-L1054](../../../INBOX/opm-libro.txt#L1030-L1054)
