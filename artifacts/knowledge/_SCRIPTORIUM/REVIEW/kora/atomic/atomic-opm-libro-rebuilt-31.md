---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-31
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
      n_propositions: 47
      segmented: true
      segment_role: segment
      segment_index: 31
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-31
---

# Atomic opm-libro-rebuilt - Segmento 31

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `47`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `31/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.5 Activity Diagram

- **P1596** · `fact` · As expressed in Fig. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1597** · `constraint` · 12.2, SysML specifies four types of behavioral diagrams: activity diagram, sequence diagram, state machine diagram, and use case diagram. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1598** · `fact` · Control Flow Fill Order Ship Order Create Invoice Invoice Send Invoice Object Flow Object Flow Activity is the fundamental behavioral element in the various SysML behavioral diagrams (excluding the use case diagram). The role of the activity diagram (see Fig. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1599** · `constraint` · 12.3) is to represent the flow of inputs and outputs and the flow of control between actions. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1600** · `fact` · To this end, the activity diagram incorporates sequences and conditions for coordinating activities. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1601** · `tension` · Activities and activity diagrams exist also in UML, but SysML provides several extensions (Bock 2006), including means to support “continuous” flow modeling, such as rate restrictions. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1602** · `tension` · Support for probabilities and extensions to control (known as “control as data”) were added to SysML activity diagrams. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1603** · `fact` · In addition, to smoothly align SysML with the widely- used classical systems engineering behavior diagram (known as EFFBD—Enhanced Functional Flow Block Diagrams; · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1604** · `constraint` · Bock, 2005), the «effbd» stereotype is specified. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1605** · `requirement` · When this stereotype is applied to an activity, it means that the activity must conform to the constraints necessary for EFFBD. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1606** · `fact` · The use case diagram is intended to describe basic high-level functionally by specifying the usage of the system by its actors to achieve a goal. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1607** · `definition` · It is often the first kind of diagram used to specify semi- formally with the customer to define the function and scope of the system to be developed. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1608** · `constraint` · Activity diagram is the only behavioral diagram kind that is extended in SysML with respect to UML 2, while the other three SysML behavioral diagram kinds remain unchanged or were eliminated. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1609** · `fact` · Sequence diagram is used to represent message-based flow of control between interacting entities, which may be actors, systems, or parts of a system. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1610** · `fact` · The state machine diagram models state-based behavior using object states and transitions. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1611** · `fact` · An action (denoted by a rountangle) is a basic (usually atomic) unit of process in an activity diagram. As Fig. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)
- **P1612** · `constraint` · 12.3 shows, an activity diagram is composed of nodes and edges, where a node can be an action or a block (denoted by a rectangle), and an edge can be a control flow if it is between actions, or an object flow (or block flow) if it is between a block and an action. · [src:S01:L4199-L4240](../../../INBOX/opm-libro.txt#L4199-L4240)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.5.1 Refining an Action into an Activity

- **P1613** · `fact` · If an action, such as Order Processing at the left of Fig. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1614** · `constraint` · 12.4, has a little rake (or trident) symbol at its bottom right, this denotes a call action that it is elaborated into an activity with its own diagram (Fig. 12.4, right). · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1615** · `fact` · This is a similar idea to OPM’s process in-zooming. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1616** · `fact` · The blocks Order, Invoice, and Product are denoted as pins—they serve as input and output parameters. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1617** · `fact` · The blocks Order, Invoice, and Product are denoted as pins—input and output parameters Actor name Stakeholder Requirements Analyst Enterprise Architect Prioritize Enterprise Requirements Model Enterprise Business Architecture Actions ordered time-wise from top to bottom Model Enterprise Requirements Support Project Teams Describe Enterprise Requirements Model Enterprise Technical Architecture The Order Processing activity diagram has initial and final pseudo nodes—the black and black-on- white circles—to denote the activity start and end, respectively. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1618** · `fact` · It also has two synchronization nodes: a fork node—the thick vertical line from the initOrder action to the Create Invoice and Ship Order actions, and a join node—the thick vertical line from these two actions to the final pseudo node. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1619** · `fact` · The fork node indicates concurrent beginning of actions exiting from it, while the join node—the termination of all the actions incoming into it. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1620** · `fact` · A swimlane is a kind of activity diagram that provides a way to group activities performed by the same actor or to group activities in a single thread. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1621** · `constraint` · Figure 12.5, adapted from Agile Modeling (2015), is an example of a swimlane activity diagram. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)
- **P1622** · `fact` · The actors are indicated in the vertical swimlanes and the diagram timeline runs from top to bottom with horizontal links crossing the swimlane borders where necessary. · [src:S01:L4242-L4289](../../../INBOX/opm-libro.txt#L4242-L4289)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.5.2 Accept, Send, and Time Event Action Nodes

- **P1623** · `fact` · Three special actions have specific notations (see Fig. · [src:S01:L4291-L4306](../../../INBOX/opm-libro.txt#L4291-L4306)
- **P1624** · `constraint` · 12.6): (a) accept event, which waits for the occurrence of an event (signal), (b) send signal, which creates and sends a signal when activated, and (c) time event, which waits for a moment in time or a specific (possibly periodic) duration. “Virus alert” type), and a join node implying that scanned messages with no detected viruses are forwarded to the user every 20 seconds. · [src:S01:L4291-L4306](../../../INBOX/opm-libro.txt#L4291-L4306)
- **P1625** · `constraint` · Virus alert Message arrived Scan for viruses Notify Admin Forward to User Every 20 seconds · [src:S01:L4291-L4306](../../../INBOX/opm-libro.txt#L4291-L4306)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.6 Sequence Diagram

- **P1626** · `fact` · The sequence diagram describes the flow of control between actors and blocks. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1627** · `fact` · This diagram represents the sending and receiving of messages between the interacting entities called lifelines. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1628** · `fact` · Time is represented along the vertical axis from top to bottom, like the swimlanes in an activity diagram. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1629** · `constraint` · As specified in SysML 1.3, sequence diagrams can represent highly complex interactions with special constructs to represent various types of control logic, reference interactions on other sequence diagrams, and decomposition of lifelines into their constituent parts. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1630** · `fact` · Here we show only the basic symbols and construct a relatively simple sequence diagram. Accelerometer, and Diagnostics Unit. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1631** · `fact` · A corresponding life line, designated by a dashed line, goes down vertically from each block. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1632** · `fact` · Horizontal arrows designate messages between blocks. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1633** · `fact` · First, a Crash message is received by Sensor Set, upon which it performs some operation, called execution occurrence and designated as a wide line or elongated rectangle along the life line, such as the one just beneath Sensor Set. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1634** · `fact` · Upon execution completion, Sensor Set sends a Shock Signal message to the Accelerometer. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1635** · `fact` · The Accelerometer starts operating and sends Shock Signal further to the Diagnostic Unit, which, in turn, performs its operation and sends back to Sensor Set a message with the value of Crash Severity, which can be light, moderate, or severe. As Fig. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1636** · `constraint` · 12.9 shows, messages can be of various types. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1637** · `fact` · They can be synchronous or asynchronous, and can provide return values. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1638** · `fact` · Messages can start from execution occurrences, external source (gates) or unknown sources (found messages). · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1639** · `constraint` · They can end at execution occurrences, external targets (gates) or unknown destination (lost messages). Blocks, such as Order in Fig. 12.9, can be created and/or destroyed. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1640** · `fact` · A message arrow can be tilted downward rather than being horizontal to denote the fact that the passing of the message itself takes a non-zero amount of time and quantify the latency. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1641** · `fact` · Interactions (messages) can start or end on gates to other blocks or systems. · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
- **P1642** · `fact` · Found Message : TradingSystem Investor need to buy buySecurity(name) : StockExchange sendOrder(Order) Other Trading System acknowledge Other Trading System Gates validatePurchase Synchronous Message Order Creation Message Return Message sendOrder(Order) acknowledge sendUpdates Lost Message Destroy Message · [src:S01:L4309-L4364](../../../INBOX/opm-libro.txt#L4309-L4364)
