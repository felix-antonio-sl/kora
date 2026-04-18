---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-71
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
      n_propositions: 58
      segmented: true
      segment_role: segment
      segment_index: 71
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-71
---

# Atomic opm-libro-rebuilt - Segmento 71

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `58`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `71/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.1 The Event-Condition-Action Control Mechanism

- **P3659** · `constraint` · The OPM process activation mechanism is the way OPM deploys the event-condition-action (ECA) paradigm, mentioned in Dittrich et al. (1995) to structure active rules in event driven architecture and active database systems. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3660** · `fact` · ECA follows the rule “On event if condition then action,” namely, if an event occurs, and an associated condition is fulfilled at the time of the event occurrence, then the associated action is triggered. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3661** · `fact` · In OPM terminology, action is an OPM process. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3662** · `fact` · Such a rule traditionally consisted of three parts, which are listed below along with their OPM interpretations. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3663** · `fact` · The event part specifies the object—the trigger, or the object’s state or value that triggers the process. carried out; in OPM the condition is evaluated on the preprocess object set. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3664** · `fact` · The ECA paradigm provide the basis for OPM operational semantics and flow of execution control. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3665** · `fact` · At the point in time of object creation, or appearance of the object from the system’s perspective, or entrance of an object to a particular state, an event occurs. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3666** · `fact` · The object or object state involved in the event can be the source of a procedural link. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3667** · `fact` · At runtime, i.e., at the instance level during the system’s execution, the occurrence of that event initiates evaluation of the The condition part is a logical test that, if satisfied or evaluates to true, enables the action to be The action part consists of updates or invocations on the local data; in OPM this amounts to activating the process, which, upon completion, transforms one or more objects. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3668** · `definition` · An event is a point in time at which something significant to the system execution happens. precondition for every process to which the object is a source of the link, and the event ceases to exist. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3669** · `fact` · If and only if the evaluation reveals satisfaction of the precondition, then the process starts executing. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3670** · `fact` · Events can occur also through the end of a subprocess inside an in-zoomed process, as well as through invocation link and exception link, which occur between processes. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3671** · `constraint` · Thus, according to the event- condition-action paradigm, starting the performance of a process (the “action”) has two prerequisites: (1) an initiating event (the “event”), and (2) satisfaction of a precondition (the “condition”). · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3672** · `fact` · Events and preconditions in concert specify OPM flow of execution control for process performance. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)
- **P3673** · `fact` · The flow of execution control is the consequence of successive event-condition-action sequences that begin with initiation of the system function by an external event and end when the system function either completes executing successfully or terminates abnormally. · [src:S01:L9336-L9369](../../../INBOX/opm-libro.txt#L9336-L9369)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.2 Precondition, Preprocess and Postprocess Object Sets

- **P3674** · `fact` · Every process has a preprocess object set with at least one object, possibly in a specified state. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3675** · `requirement` · The preprocess object set of a process determines the precondition that must be satisfied before performance of that process starts. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3676** · `fact` · The preprocess object set may simply include the existence of one or more objects, possibly in specified states, but it can also be complex and include compound logical expressions using logical AND, OR, and XOR operators. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3677** · `fact` · Typical objects in a preprocess object set are transformees— consumees and/or affectees, and enablers. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3678** · `fact` · Some of these objects may have a further stipulation regarding flow of execution control, expressed as a condition link, which, as explained below, provides for skipping the process if its precondition is not satisfied. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3679** · `fact` · The postprocess object set determines the process postcondition that the process completion satisfies. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3680** · `fact` · Typical objects in a postprocess object set are resultees and affectees. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3681** · `fact` · The intersection of the preprocess object set and the postprocess object set of the same process includes the process enablers and affectees. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3682** · `fact` · Consumees are only members of the preprocess object set, while resultees are only members of the postprocess object set. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3683** · `fact` · The involved object set is the union of the preprocess and postprocess object sets. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3684** · `requirement` · If the involved object set has only one object, it must be a transformee, otherwise it does not conform to the OPM definition of process as a thing that transforms at least one object. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)
- **P3685** · `requirement` · Therefore, in a complete OPM model, each process must be linked with at least one transformee, and an OPM modeling tool should check this as a basic part of its model validation. · [src:S01:L9371-L9388](../../../INBOX/opm-libro.txt#L9371-L9388)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.3 Kinds of Control Links

- **P3686** · `fact` · As part of the event-condition-action paradigm underlying OPM’s operational semantics, an event link, a condition link, and an exception link express an event, a condition, and a time exception, respectively. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3687** · `fact` · These three link kinds are OPM’s control links. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3688** · `fact` · Control links occur either between an object and a process or between two processes. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3689** · `fact` · Event and condition links do not exist independently. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3690** · `fact` · Rather, they are modified versions of the various procedural links. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3691** · `fact` · Each procedural link from an object or a state to a process (i.e., object or state in the preprocess object state) has a corresponding event link and a corresponding condition link. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3692** · `fact` · A control modifier is one of the two letter symbols e and c, added to a procedural link, which add to the semantics of that link the event and condition semantics, respectively. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3693** · `fact` · A control link is a procedural link with the addition of a control modifier. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3694** · `fact` · There is no result event link or result condition link, since these are outgoing procedural links, relating to the postprocess object set. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3695** · `fact` · When a process completes, it creates the postprocess object set without further condition. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)
- **P3696** · `fact` · Hence, assuming that the process terminates successfully, creation of resultees and change of affectees are automatic and unconditional. · [src:S01:L9390-L9405](../../../INBOX/opm-libro.txt#L9390-L9405)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.4 Event Links

- **P3697** · `fact` · A process event semantics is the initiation of that process, which triggers evaluation of that process’ precondition. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)
- **P3698** · `fact` · An event link is a procedural link with the control modifier e, indicating the addition of event semantics to the link’s destination process. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)
- **P3699** · `fact` · An event link specifies a source event and a destination process—the process that is initiated upon the event occurrence. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)
- **P3700** · `fact` · The event occurrence triggers evaluation of the process’ precondition. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)
- **P3701** · `fact` · Satisfying the precondition allows process performance (execution) to proceed, rendering the process active. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)
- **P3702** · `requirement` · If the process precondition is not satisfied, then process performance shall not occur. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)
- **P3703** · `fact` · Regardless of whether the evaluation is successful or not, being a point in time, the event is lost. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)
- **P3704** · `requirement` · If the process precondition is not satisfied, process initiation shall not occur until another event activates the process. · [src:S01:L9407-L9416](../../../INBOX/opm-libro.txt#L9407-L9416)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.4.1 Initiating a Non-first Subprocess via an Event Link

- **P3705** · `fact` · If an event link is attached to a process P, and P is in-zoomed, like all the other procedural links attached to P, the event link migrates automatically to the first (top-most) subprocess—the one that executes first. · [src:S01:L9418-L9427](../../../INBOX/opm-libro.txt#L9418-L9427)
- **P3706** · `requirement` · The modeler must be very cautious when modeling an event link that is attached to any subprocess other than the first one, because this is akin to interfering with the inner operation of a black box! · [src:S01:L9418-L9427](../../../INBOX/opm-libro.txt#L9418-L9427)
- **P3707** · `fact` · While trying to trigger a non-first subprocess, one or more of that subprocess’ preconditions may not be met because previous subprocesses were skipped. For example, if in Fig. · [src:S01:L9418-L9427](../../../INBOX/opm-libro.txt#L9418-L9427)
- **P3708** · `constraint` · 6.2 the event link is attached to Message Creating rather than to Crash Severity Measuring, the latter process is skipped, so Crash Severity remains none, and therefore Message Creating will be skipped too. · [src:S01:L9418-L9427](../../../INBOX/opm-libro.txt#L9418-L9427)
- **P3709** · `fact` · Moreover, since there is no Message, Help Sending is also skipped, leaving Vehicle Occupants Group at their initial possibly injured state, rather than being helped. · [src:S01:L9418-L9427](../../../INBOX/opm-libro.txt#L9418-L9427)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.4.2 Enabling and Transforming Event Links

- **P3710** · `constraint` · There are two kinds of transforming event links (Table 22.1) and two enabling event links (Table 22.2). Table 22.1. · [src:S01:L9431-L9490](../../../INBOX/opm-libro.txt#L9431-L9490)
- **P3711** · `fact` · Enabling event link summary Name Semantics Sample OPD & OPL Source Destination Agent event link The agent—a human—both initiates and enables the process. · [src:S01:L9431-L9490](../../../INBOX/opm-libro.txt#L9431-L9490)
- **P3712** · `requirement` · The agent must be present throughout the process duration. initiating agent initiated process Miner initiates and handles Copper Mining. · [src:S01:L9431-L9490](../../../INBOX/opm-libro.txt#L9431-L9490)
- **P3713** · `requirement` · Instrument event link The object initiates the process as an instrument, so it does not change, but it must exist throughout the process duration. initiating instrument initiated process Drill initiates Copper Mining, which requires Drill. Table 22.2. · [src:S01:L9431-L9490](../../../INBOX/opm-libro.txt#L9431-L9490)
- **P3714** · `fact` · Transforming event link summary Name Semantics Sample OPD & OPL Source Destination Consumption event link The object initiates the process, which, if performed, consumes the object. initiating consumee Food initiates Eating, which initiated process, which consumes the initiating consumee consumes Food. · [src:S01:L9431-L9490](../../../INBOX/opm-libro.txt#L9431-L9490)
- **P3715** · `fact` · Effect event link The object initiates the process, which, if performed, affects the object. · [src:S01:L9431-L9490](../../../INBOX/opm-libro.txt#L9431-L9490)
- **P3716** · `fact` · The event link is the link from the object to the process; the link from the process to the object is not an event link. initiating affectee is abstracted as: initiated process, which affects the initiating affectee Copper initiates Purifying, which affects Copper. · [src:S01:L9431-L9490](../../../INBOX/opm-libro.txt#L9431-L9490)
