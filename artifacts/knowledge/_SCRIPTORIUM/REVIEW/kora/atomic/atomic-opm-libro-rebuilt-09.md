---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-09
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
      n_propositions: 48
      segmented: true
      segment_role: segment
      segment_index: 9
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-09
---

# Atomic opm-libro-rebuilt - Segmento 09

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `48`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `09/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 5 Refinement Through In-Zooming / 5.6 Simulating the System: An Animated Execution Test

- **P0448** · `fact` · At this point, it is worthwhile to start carrying out an animated execution of the system at its current design, in order to test its conceptual operation. · [src:S01:L1446-L1455](../../../INBOX/opm-libro.txt#L1446-L1455)
- **P0449** · `constraint` · Figure 5.4 shows the system after the (environmental) process Crashing has changed the state of Vehicle from intact to crashed, which was the event that has initiated the Automatic Crash Responding process. · [src:S01:L1446-L1455](../../../INBOX/opm-libro.txt#L1446-L1455)
- **P0450** · `fact` · Within this process, Crash Severity Measuring is about to be finished, changing the attribute Crash Severity of Vehicle from none to one of the light, moderate, or severe states. Crash Severity from none to severe · [src:S01:L1446-L1455](../../../INBOX/opm-libro.txt#L1446-L1455)

## opm libro · Chapter 6 The Dynamic Aspect of Systems

- **P0451** · `constraint` · The expert may, in the process of explaining some idea or description of a behavior, suddenly reach for pad and draw sketches of what he/she does, and say “it has to look like this” or “I know just by looking at the chart if something is wrong.” Firlej and Helens (1991) Continuing with modeling our case study, in this chapter we further discuss process issues, such as execution order and how to specify that processes are sequential, concurrent, or alternative. · [src:S01:L1481-L1487](../../../INBOX/opm-libro.txt#L1481-L1487)
- **P0452** · `fact` · These issues are related to the system's dynamic aspect and to its operational semantics. · [src:S01:L1481-L1487](../../../INBOX/opm-libro.txt#L1481-L1487)

## opm libro · Chapter 6 The Dynamic Aspect of Systems / 6.1 Exiting in Case of Light Severity

- **P0453** · `fact` · Recall that the ACR system specification stipulates: Within seconds of a moderate-to-severe crash, the OnStar module will send a message … Hence, if Crash Severity is light, we wish to model that the Automatic Crash Responding process is exited and the system finished its execution. To do this, in Fig. · [src:S01:L1489-L1501](../../../INBOX/opm-libro.txt#L1489-L1501)
- **P0454** · `constraint` · 6.1, we add to Vehicle Occupants Group a third state, uninjured, which is also final. · [src:S01:L1489-L1501](../../../INBOX/opm-libro.txt#L1489-L1501)
- **P0455** · `fact` · Using a condition link (an instrument link with the control modifier c next to its circle end) we connect the state light of Crash Severity with a new subprocess, Exiting, which changes the state of Vehicle Occupants Group to uninjured. · [src:S01:L1489-L1501](../../../INBOX/opm-libro.txt#L1489-L1501)
- **P0456** · `fact` · In this case, the execution of the system terminates. · [src:S01:L1489-L1501](../../../INBOX/opm-libro.txt#L1489-L1501)
- **P0457** · `fact` · The semantics of the condition link is that if the object to which the link is attached exists, or if the state to which the link is attached is the current object state, then the process executes, otherwise the process is skipped. · [src:S01:L1489-L1501](../../../INBOX/opm-libro.txt#L1489-L1501)
- **P0458** · `fact` · The condition instrument link semantics is weaker than that of the (non- condition) instrument link. · [src:S01:L1489-L1501](../../../INBOX/opm-libro.txt#L1489-L1501)
- **P0459** · `fact` · The semantics of the latter is that if the linked object does not exist (or is not at the required state), then the execution of the system stops, waiting for the instrument to become existent (or at the required state). · [src:S01:L1489-L1501](../../../INBOX/opm-libro.txt#L1489-L1501)

## opm libro · Chapter 6 The Dynamic Aspect of Systems / 6.2 Message Creating and Sending

- **P0460** · `fact` · We continue with modeling what happens in case Crash Severity Measuring has changed Crash Severity from none to moderate or severe, based on the following text: Within seconds of a moderate to severe crash, the OnStar module will send a message to the OnStar Call Center (OCC) through a cellular connection, informing the advisor that a crash has occurred. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0461** · `fact` · Based on the message received, the advisor sends help as needed. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0462** · `fact` · Vehicle Occupants Group to uninjured According to this description, following Crash Severity Measuring, as a result of a crash whose Crash Severity is moderate or severe, a message is created and then sent via the OnStar Call Center to the advisor, who sends help based on the message. Accordingly, as Fig. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0463** · `constraint` · 6.2 shows, we add three subsequent subprocesses: Message Creating, Message Sending, and Help Sending. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0464** · `fact` · The following OPL sentence expresses the XOR relation between the condition links from the moderate and severe states of Crash Severity to Message Creating. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0465** · `fact` · Message Creating occurs if Crash Severity is exactly one of moderate or severe. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0466** · `fact` · As we recall, the model fact representation OPM principle states that an OPM element needs to appear in at least one OPD in order for it to be represented. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0467** · `constraint` · Based on this principle and in order to simplify the OPD, the environmental process Crashing, which appeared in Fig. 6.1, has been removed from Fig. 6.2. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)
- **P0468** · `fact` · This enables us to add objects mentioned in the text that are relevant here: the OnStar Call Center and the Cellular System, which are parts of the ACR System (in addition to the Vehicle), as well as the Advisor and the Message. · [src:S01:L1503-L1527](../../../INBOX/opm-libro.txt#L1503-L1527)

## opm libro · Chapter 6 The Dynamic Aspect of Systems / 6.3 Process Execution Order: The Timeline OPM Principle

- **P0469** · `fact` · Message Creating process creates Message within the scope of the Automatic Crash Responding process. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0470** · `fact` · Message Creating requires both OnStar Call Center and Cellular System as instruments. along with the objects OnStar Call Center, Cellular System, Message, and Advisor The five subprocesses in Fig. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0471** · `constraint` · 6.2 are arranged by their execution order (the timeline perspective) from top to bottom. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0472** · `fact` · This is based on the following timeline OPM principle. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0473** · `fact` · The Timeline OPM Principle The timeline within an in-zoomed process is directed by default from the top of the in-zoomed process ellipse to its bottom. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0474** · `fact` · The timeline OPM principle is followed by default, unless there is indication to deviate from the timeline. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0475** · `fact` · Indications to deviate from the top-to-bottom timeline within an in-zoomed process include internal events within the scope of the process which can cause loops. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0476** · `fact` · The top-most point of the process ellipse serves as a reference point, so a process whose reference point is higher than its peer starts earlier. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0477** · `fact` · If the reference points of two or more processes are at the same height (within some tolerance), these processes start simultaneously. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)
- **P0478** · `fact` · According to the timeline OPM principle, Crash Severity Measuring is executed first, followed by Exiting (in case of light Crash Severity) or, in case of moderate Crash Severity or severe Crash Severity, by Message Creating, followed by Message Sending and Help Sending. · [src:S01:L1532-L1551](../../../INBOX/opm-libro.txt#L1532-L1551)

## opm libro · Chapter 6 The Dynamic Aspect of Systems / 6.4 Help Is on the Way!

- **P0479** · `fact` · We go on to model the following text, which describes what happens when the Advisor gets the Message. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0480** · `constraint` · The advisor then can conference in 911 dispatch or a public safety answering point (PSAP), which determines if emergency services are necessary, and if so, is it ambulance, helicopter, or both. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0481** · `fact` · This description covers a lot of ground and includes a number of new processes, including Voice Connection Attempting, Public Aid Conferencing, Crash Information Providing, and Emergency Service Dispatching. which can be impossible (if the passengers do not respond or there is no cellular connection; not modeled) or established. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0482** · `fact` · If Voice Connection is impossible, the Advisor informs the Emergency Dispatcher about the value of the Crash Severity and location via the Severity & Location Informing process. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0483** · `constraint` · The Emergency Dispatcher is a generalization of 911 Dispatch and Public Safety Answering Point. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0484** · `fact` · If Voice Connection is established, the conferencing involves Passenger Inquiring by the Advisor and the Emergency Dispatcher. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0485** · `fact` · Either Passenger Inquiring or Severity & Location Informing determines the Required Emergency Service, which can be none, ambulance, helicopter, or ambulance & helicopter. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)
- **P0486** · `fact` · This decision is used for Emergency Service Dispatching, which, if needed, sends the appropriate Emergency Workers Group, an environmental object, on its way to help, changing the state of Vehicle Occupants Group to being helped. · [src:S01:L1553-L1575](../../../INBOX/opm-libro.txt#L1553-L1575)

## opm libro · Chapter 6 The Dynamic Aspect of Systems / 6.5 Scenarios: Threads of Execution

- **P0487** · `fact` · state of each object. · [src:S01:L1580-L1589](../../../INBOX/opm-libro.txt#L1580-L1589)
- **P0488** · `fact` · Voice Connection Attempting creates Voice Connection at state established, leading to Passenger Inquiring. · [src:S01:L1580-L1589](../../../INBOX/opm-libro.txt#L1580-L1589)
- **P0489** · `fact` · If this process creates Required Emergency Service at state none, Exiting takes place, otherwise Emergency Service Dispatching takes place. · [src:S01:L1580-L1589](../../../INBOX/opm-libro.txt#L1580-L1589)
- **P0490** · `fact` · Either way, the Vehicle Occupants Group transition to the state of being helped. state of being helped. (Note: in this and in the next OPD the c of the condition link is drawn inside the circle) state of each object · [src:S01:L1580-L1589](../../../INBOX/opm-libro.txt#L1580-L1589)

## opm libro · Chapter 7 Controlling the System’s Behavior

- **P0491** · `fact` · The picture... corresponds to the concept or memory image associated with the words. · [src:S01:L1634-L1640](../../../INBOX/opm-libro.txt#L1634-L1640)
- **P0492** · `constraint` · Schapiro (1996) Control in the context of conceptual modeling is the ability to determine the flow of processes and how they transform objects under various conditions and circumstances. · [src:S01:L1634-L1640](../../../INBOX/opm-libro.txt#L1634-L1640)
- **P0493** · `fact` · Several control structures enable us to determine how the system will behave over time. · [src:S01:L1634-L1640](../../../INBOX/opm-libro.txt#L1634-L1640)
- **P0494** · `fact` · These include Boolean objects for branching and control modifiers—condition and event indicators that are added to procedural links and augment their semantics. · [src:S01:L1634-L1640](../../../INBOX/opm-libro.txt#L1634-L1640)
- **P0495** · `fact` · In this chapter we discuss and show how control structures are used to model system behavior. · [src:S01:L1634-L1640](../../../INBOX/opm-libro.txt#L1634-L1640)
