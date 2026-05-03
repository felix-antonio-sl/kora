---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-02
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
      n_propositions: 58
      segmented: true
      segment_role: segment
      segment_index: 2
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-02
---

# Atomic opm-libro-rebuilt - Segmento 02

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `58`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `02/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 1 Ready to Start Modeling?

- **P0049** · `fact` · to be to not be useful. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)
- **P0050** · `constraint` · Box and Draper (1987) With diagrams the meaning is obvious, because once you understand how the basic elements of the diagrams fit together, the meaning literally stares you in the face. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)
- **P0051** · `constraint` · Steve Cook (1999) We live in a world of interconnected systems. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)
- **P0052** · `fact` · In fact, as humans, each of us is a highly complex system living in a host of socio-political-technological systems that are no less complex. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)
- **P0053** · `fact` · In order to understand and design complex systems, it is necessary to have a methodology and a language for building models that can express what these systems do, why they do it, how they do it, and what they need in order to do it. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)
- **P0054** · `fact` · While the visual and intuitive nature of diagrams has made them widely used means for building models of systems, natural language text is also an important way of conveying complex ideas. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)
- **P0055** · `fact` · Formal diagrams are a graphic language in that they contain interconnected symbols, expressing meaningful facts and statements about the world. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)
- **P0056** · `fact` · Combining graphics with text reinforces our ability to specify complex ideas in science and engineering. · [src:S01:L502-L516](../../../INBOX/opm-libro.txt#L502-L516)

## opm libro · Chapter 1 Ready to Start Modeling? / 1.1 The Automatic Crash Response System

- **P0057** · `fact` · We introduce conceptual modeling using OPM, and later SysML, using a running example of specifying the GM OnStar Automatic Crash Response (ACR) system. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0058** · `fact` · The specification that we model provided below was taken almost literally from an early version of OnStar Technology’s description on the OnStar company website. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0059** · `fact` · OnStar’s in-vehicle safety, security, and information services use Global Positioning System (GPS) satellite and cellular technology to link the vehicle and driver to the OnStar Center. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0060** · `constraint` · At the OnStar Center, advisors offer real-time, personalized help 24 hours a day, 365 days a year. … The accelerometer located within the Sensing and Diagnostic Module (SDM) measures the crash’s severity. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0061** · `fact` · In the event of a moderate-to-severe frontal or side-impact crash, data is transmitted from the affected sensors to the SDM. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0062** · `fact` · The SDM sensor also can identify a rear impact of sufficient severity. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0063** · `fact` · Regardless of whether the air bags deploy, the SDM transmits crash information to the vehicle’s OnStar module. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0064** · `fact` · Within seconds of a moderate-to-severe crash, the OnStar module will send a message to the OnStar Call Center (OCC) through a cellular connection, informing the advisor that a crash has occurred. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0065** · `fact` · A voice connection between the advisor and the vehicle occupants is established.
  - [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
  - [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0066** · `constraint` · The advisor can then conference in 911 [emergency] dispatch or a public safety answering point (PSAP), which determines if emergency services are necessary. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0067** · `fact` · If there is no response from the occupants, the advisor can provide the emergency dispatcher with the crash information from the SDM that reveals the severity of the crash.
  - [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
  - [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0068** · `fact` · The dispatcher can identify what emergency services may be appropriate.
  - [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
  - [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0069** · `fact` · Using the Global Positioning System (GPS) satellite, OnStar advisors are able to tell emergency workers the location of the vehicle.
  - [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
  - [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0070** · `fact` · The “big picture” that emerges from this system description is that the ACR system aims to provide an automatic response in case of a severe car crash. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)
- **P0071** · `fact` · In the following sections we methodically model this system using OPM and then SysML. · [src:S01:L518-L548](../../../INBOX/opm-libro.txt#L518-L548)

## opm libro · Chapter 1 Ready to Start Modeling? / 1.2 The Function-as-a-Seed OPM Principle

- **P0072** · `fact` · In order to start an OPM model of a system, the first step is to determine the function of the system. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0073** · `fact` · The function is the main process of the system, which is designed to deliver value—benefit at cost—to the system beneficiary. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0074** · `fact` · The system beneficiaries are the person or people who get value from using the system. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0075** · `fact` · Identifying the system’s function is critical, as it expresses the motivation for engineering the system. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0076** · `fact` · This function will be the top-level process of our OPM model. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0077** · `constraint` · Determining the system’s function is not just important and recommended, it is also a basic principle, known as the function-as-a-seed OPM principle:2 The Function-as-a-Seed OPM Principle Modeling a system starts by defining, naming, and depicting the function of the system, which is also its top-level process. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0078** · `fact` · The term “function-as-a-seed” underscores the centrality of starting off the modeling process in a way that focuses on the function of the system; that is, the value that the system provides to its beneficiary. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0079** · `fact` · As the next few chapters show, this function is the seed from which the entire model gradually evolves. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0080** · `fact` · This guideline may be counterintuitive, since many engineers tend to start with the form—the objects, the substance of which the system is comprised—rather than the function, which is the process due to which beneficiaries would use the system in the first place. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0081** · `requirement` · Function delivers value, while form draws cost that must be paid to achieve that system’s function. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0082** · `fact` · Given the centrality of the system’s function, it is worth contemplating what this function really is and what it should best be called so everybody involved in the modeling will be on the same page. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0083** · `fact` · An appropriate function clarifies and emphasizes the central goal of the system being modeled. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0084** · `fact` · Deliberation regarding the function often provokes a debate between the system architecture team members at this early stage, but this is highly valuable. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0085** · `fact` · Such discussions frequently expose differences and often even misconceptions among the participants regarding the system that they set out to architect, model, and design. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)
- **P0086** · `fact` · Thus, agreement on the system’s function and its most appropriate name increases the likelihood of ending up with a useful model. · [src:S01:L550-L577](../../../INBOX/opm-libro.txt#L550-L577)

## opm libro · Chapter 1 Ready to Start Modeling? / 1.3 Identifying the System’s Function

- **P0087** · `fact` · The OnStar system description above makes it clear that the main function of the system—its purpose and the value it delivers—is to automatically provide response in case of a car crash. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0088** · `fact` · Therefore, we call this function Automatic Crash Responding, and this is the top-level process of the system we are about to start modeling. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0089** · `fact` · OPM has just one type of diagram, which is called the object-process diagram (OPD). · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0090** · `fact` · Any OPD is built using two OPM building blocks: objects and processes. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0091** · `fact` · An object is a thing that exists or might exist. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0092** · `fact` · While objects exist, processes happen or occur, and they transform objects by generating, consuming, or affecting them. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0093** · `fact` · A process is a thing that transforms an object.
  - [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
  - [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0094** · `fact` · Collectively, objects and processes are called things. A thing is an object or a process. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0095** · `fact` · We start by modeling the system diagram—the top-level object-process diagram (OPD)—in our OPM model. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0096** · `fact` · The OPM symbol for a process is an ellipse with the process name recorded within it. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0097** · `constraint` · OPM-based modeling software environment such as OPCAT (Dori et al. 2003). · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0098** · `fact` · It is highly recommended that the reader installs OPCAT and follows the modeling activities presented here. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0099** · `fact` · Based on the definition of a process as a thing that transforms an object, no process is meaningful unless it transforms at least one object. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)
- **P0100** · `fact` · That object is known as the transformee of the transforming process or the operand of the system’s function. · [src:S01:L579-L600](../../../INBOX/opm-libro.txt#L579-L600)

## opm libro · Chapter 1 Ready to Start Modeling? / 1.4 Identifying the System’s Beneficiary

- **P0101** · `fact` · A man-made, artificial system is designed to benefit at least some of its stakeholders. · [src:S01:L602-L608](../../../INBOX/opm-libro.txt#L602-L608)
- **P0102** · `fact` · The stakeholders that benefit are the system’s beneficiaries. · [src:S01:L602-L608](../../../INBOX/opm-libro.txt#L602-L608)
- **P0103** · `fact` · The beneficiary of the Automatic Crash Responding process, which is also the transformee in our case, is the driver and any additional passengers who occupy the crashed vehicle. · [src:S01:L602-L608](../../../INBOX/opm-libro.txt#L602-L608)
- **P0104** · `constraint` · This group of people is the object Vehicle Occupants Group. Figure 1.2 shows the OPD of Fig. 1.1 updated with this object. · [src:S01:L602-L608](../../../INBOX/opm-libro.txt#L602-L608)
- **P0105** · `fact` · The OPM symbol for object is a rectangle with the object name recorded within it. · [src:S01:L602-L608](../../../INBOX/opm-libro.txt#L602-L608)
- **P0106** · `fact` · This is also the standard symbol used in UML—the Unified Modeling Language (OMG UML 2011I, 2011S)—and SysML, where it is referred to as a block. · [src:S01:L602-L608](../../../INBOX/opm-libro.txt#L602-L608)
