---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-73
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
      n_propositions: 40
      segmented: true
      segment_role: segment
      segment_index: 73
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-73
---

# Atomic opm-libro-rebuilt - Segmento 73

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `40`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `73/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.5.3 Condition Enabling Links

- **P3765** · `fact` · There are two kinds of basic (non-state-specified) condition enabling links: condition agent link and condition instrument link. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3766** · `fact` · A condition agent link is an agent link from an agent to a process with the addition of the control modifier c. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3767** · `fact` · If at runtime an agent instance exists when an event initiates the process, then the presence of that agent instance satisfies the process precondition with respect to that object. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3768** · `fact` · If evaluation of the remaining precondition is satisfied as well, the process starts and that agent handles its performance. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3769** · `fact` · However, if an agent instance does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’ the process without process performance. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3770** · `fact` · A condition instrument link is an instrument link from an instrument to a process, annotated with the control modifier c. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3771** · `fact` · If at runtime an instrument instance exists when an event initiates the process, then the presence of that instrument instance satisfies the process precondition with respect to that object. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3772** · `fact` · If evaluation of the entire preprocess object set satisfies the precondition, the process starts. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3773** · `constraint` · However, if an instrument instance does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’ the process without process performance (Table 22.7). · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3774** · `constraint` · Table 22.7 Condition enabling link summary Network Signal Amplifying, which occurs only if an environmental object Nearby Mobile Device exists and is otherwise skipped, as there is no point in amplifying if no device is nearby. · [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.5.4 Condition State-Specified Transforming Links

- **P3775** · `constraint` · Like their event state-specified transforming link counterparts, there are four kinds of condition state- specified transforming links. These are summarized in Table 22.8. · [src:S01:L9660-L9661](../../../INBOX/opm-libro.txt#L9660-L9661)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.5.5 Condition State-Specified Enabling Links

- **P3776** · `fact` · Like their regular, non-state-specified counterparts, there are two state-specified enabling links: state- specified agent link and state-specified instrument link. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3777** · `fact` · A condition state-specified agent link is a state-specified agent link, annotated with the control modifier c, from a specified state of an agent to a process. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3778** · `fact` · If at runtime an instance of the agent exists, or is present, at the specified state when an event initiates the process, then this satisfies the process precondition with respect to that object. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3779** · `fact` · If evaluation of the entire preprocess object set satisfies the precondition, the process starts and that agent has to be present to handle it until it ends. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3780** · `fact` · Otherwise, the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, performing the process. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3781** · `fact` · A condition state-specified instrument link is a state-specified instrument link, annotated with the control modifier c, from a specified state of an instrument to a process. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3782** · `constraint` · Name Condition state- specified consumption link Condition input- output- specified effect link Condition input- specified effect link Table 22.8 Condition state-specified transforming link summary Semantics Sample OPD & PL Source Destination The process performs if the object is in the state from which the link originates, otherwise the process is skipped. conditioning specified state of the object conditioned process Testing occurs if Raw Material Sample is pre-approved, in which case Raw Material Sample is consumed, otherwise Testing is skipped. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3783** · `fact` · The process performs if the object is in the input state (from which the link originates) and changes the object from its input state to its output state, otherwise the process is skipped. conditioning specified input state of the object conditioned process Testing occurs if Raw Material is pre- tested, in which case Testing changes Raw Material from pre-tested to tested, otherwise Testing is skipped. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3784** · `fact` · The process performs if the object is in the input state (from which the link originates) and changes the object from its input state to any one of its states, otherwise the process is skipped. conditioning specified input state of the object conditioned process Delivery Attempting occurs if Message is created, in which case Delivery Attempting changes Message from created, otherwise Delivery Attempting is skipped. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3785** · `fact` · Condition output- specified effect link The process performs if the object is in the input state (from which the link originates) and changes the object from its input state to any one of its states, otherwise the process is skipped. conditioning object Stress Testing occurs if Suspicious Component exists, in which case Stress Testing changes Suspicious Component to stress-tested, otherwise Stress Testing is skipped. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3786** · `constraint` · Table 22.9 Condition state-specified enabling link summary conditioned process If at runtime an instance of the instrument exists and is at the specified state when an event initiates the process, then the process precondition is satisfied with respect to that object. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3787** · `requirement` · If evaluation of the entire preprocess object set satisfies the precondition, the process starts and that instrument must remain existent and at the same state throughout the duration of the process If at runtime an instance of the instrument does not exist or exists at a different state than the one attached to the link source, then the process precondition with respect to that object is not satisfied, the process precondition evaluation fails, and the flow of execution control bypasses performing the process. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)
- **P3788** · `constraint` · Table 22.9 summarizes the condition state-specified enabling links. · [src:S01:L9663-L9784](../../../INBOX/opm-libro.txt#L9663-L9784)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.6 Exception Links

- **P3789** · `fact` · Exception links enable modeling what to do in case of exception in the time execution of a process below a minimal threshold or above a maximal one. · [src:S01:L9786-L9787](../../../INBOX/opm-libro.txt#L9786-L9787)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.6.1 Process Time Duration and Its Distribution

- **P3790** · `requirement` · Process may have a Duration property (metamodel attribute) with a value expressed in time units, which shall be compatible with ISO 80000-3:2006—Quantities and units—Part 3: Space and time, which is part of the group of ISO/IEC 80000 standards that form the International System of Quantities. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3791** · `fact` · Units of time can be milliseconds [ms], seconds [sec], minutes [min], hours [hr], days [dy], weeks [wk], months [mo], or years [yr]. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3792** · `fact` · Duration may specialize into Minimal Duration, Expected Duration, and Maximal Duration. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3793** · `fact` · Minimal Duration and Maximal Duration designate the minimum and maximum allowable time for process completion. Time duration is an optional, and, as Fig. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3794** · `constraint` · 22.2 shows, the modeler can choose to indicate only the expected (nominal) time, minimal and maximal, or all three durations. right—minimal, expected, and maximal time durations The value of the process’ Expected Duration is the statistical mean of the duration of that process. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3795** · `fact` · Duration optionally exhibits the Duration Distribution attribute with a value identifying the name and parameters for a probability distribution function associated with the process duration or a non-analytical distribution. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3796** · `fact` · At run-time, the value of Duration is determined separately for each process instance (i.e., for each individual process occurrence) by sampling from the process Duration Distribution. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3797** · `fact` · The Duration property provides for defining exception links. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)
- **P3798** · `fact` · There are two kinds of exception link: overtime exception link and undertime exception link. · [src:S01:L9789-L9805](../../../INBOX/opm-libro.txt#L9789-L9805)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.6.2 Overtime Exception Link

- **P3799** · `fact` · The overtime exception link connects the source process with a destination overtime handling process to specify that if at runtime, the performance time of the source process instance exceeds its Maximal Duration value, then an event initiates the destination process, which is an overtime handling process. · [src:S01:L9809-L9822](../../../INBOX/opm-libro.txt#L9809-L9822)
- **P3800** · `fact` · A maximal-timed process is a process for which the modeler determines a maximal duration. · [src:S01:L9809-L9822](../../../INBOX/opm-libro.txt#L9809-L9822)
- **P3801** · `fact` · An overtime handling process is a time exception process that determines what to do in case the time performance of a maximal-timed process exceeds its maximal allowable time. · [src:S01:L9809-L9822](../../../INBOX/opm-libro.txt#L9809-L9822)
- **P3802** · `fact` · An overtime exception link is a procedural link from a maximal-timed process to an overtime handling process, indicating that if the duration of a maximal-timed process exceeds its maximal duration, then the overtime exception process is initiated. · [src:S01:L9809-L9822](../../../INBOX/opm-libro.txt#L9809-L9822)
- **P3803** · `fact` · The control modifier for the overtime exception link is a single slanted short bar crossing the link near the overtime exception process (see Fig. · [src:S01:L9809-L9822](../../../INBOX/opm-libro.txt#L9809-L9822)
- **P3804** · `constraint` · 22.3 for the control modifier of the undertime exception link, which is a pair of such bars). · [src:S01:L9809-L9822](../../../INBOX/opm-libro.txt#L9809-L9822)
