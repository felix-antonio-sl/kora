---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-72
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
      n_propositions: 48
      segmented: true
      segment_role: segment
      segment_index: 72
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-72
---

# Atomic opm-libro-rebuilt - Segmento 72

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `48`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `72/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.4.3 State-Specified Enabling and Transforming Event Links

- **P3717** · `constraint` · Table 22.3 describes the two state-specified enabling event links—one for agent, the other for instrument. · [src:S01:L9494-L9496](../../../INBOX/opm-libro.txt#L9494-L9496)
- **P3718** · `constraint` · There are four kinds of state-specified transforming event links. These are summarized in Table 22.4. · [src:S01:L9494-L9496](../../../INBOX/opm-libro.txt#L9494-L9496)
- **P3719** · `constraint` · Table 22.3 State-specified enabling event link summary · [src:S01:L9494-L9496](../../../INBOX/opm-libro.txt#L9494-L9496)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.4.4 Invocation Links

- **P3720** · `fact` · Process invocation is an event by which a process initiates a process. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3721** · `fact` · An invocation link connects a source process to the destination process that it initiates, signifying that when the source process completes successfully, it immediately initiates the destination process—the process at the destination end of the invocation link. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3722** · `fact` · In a normal or expected flow of execution control, the source process does not initiate the new process if the former does not complete successfully. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3723** · `fact` · It is up to the modeler to take care of modeling what should happen with any process that aborts, e.g., due to a time exception. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3724** · `fact` · Since by definition an OPM process transforms an object, the invocation link semantically implies the creation of an interim object by the invoking source process that the subsequent invoked destination process immediately consumes. As discussed in Sect. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3725** · `constraint` · 10.10.3 in an OPM model, an invocation link may replace a transient, short-lived physical or informatical object that a source process creates to initiate the destination process, which immediately consumes the transient object. The physical object Spark in Fig. 10.11 is one example; Record ID in a query is another. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3726** · `fact` · Graphically, a lightening symbol jagged (and possibly curved) line from the invoking source process to the invoked destination process ending with a closed arrowhead at the invoked process denotes an invocation link. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3727** · `fact` · This is the symbol of the common invocation link. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3728** · `constraint` · Table 22.4 State-specified transforming event link summary Table 22.5 Invocation link summary There is a second kind of invocation link—self-invocation link, which enables modeling invocation of a process by itself: Upon process completion, the process immediately invokes itself. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3729** · `requirement` · A self-invocation link is symbolized by a pair of invocation links, originating at the process and joining head to tail before ending back at the original process shall denote the self-invocation link. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3730** · `constraint` · Invocation links are summarized in Table 22.5. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3731** · `fact` · If a waiting period is needed between two consecutive invocations, a Waiting process with specified time constraints (see below) can be inserted as a destination from the invoking process and as a target back to the same process. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)
- **P3732** · `fact` · An invocation link from the last subprocess to its parent in-zoomed process can be used to create loops. · [src:S01:L9498-L9526](../../../INBOX/opm-libro.txt#L9498-L9526)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.5 Condition Links

- **P3733** · `fact` · A process condition semantics is skipping the execution of that process if its precondition is not met. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3734** · `fact` · A condition link is a procedural link with the control modifier c, indicating the addition of condition semantics to the link’s destination process. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3735** · `fact` · A condition link provides a bypass mechanism, which enables system execution control to skip, or bypass, the destination process if its precondition satisfaction evaluation fails. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3736** · `fact` · Without the condition link bypass mechanism, failure to satisfy the precondition causes the process to wait for another event. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3737** · `fact` · Upon the arrival of the new event, that process precondition is evaluated again, and if it is satisfied, the process starts executing, otherwise it is again waiting for the next event. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3738** · `fact` · This can cause the control to get stuck indefinitely in that process in an infinite loop. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3739** · `fact` · Using the condition link prevents such situations. As discussed in Sect. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3740** · `constraint` · 21.17, as is the case with all control links, if a condition link is attached to a process P, and P is in-zoomed, the condition link migrates automatically to the first subprocess (or two or more first concurrent subprocesses) of P. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)
- **P3741** · `fact` · The modeler may move the link from that first subprocess to another subprocess or add another link from the same source to one or more subprocesses other than the first one. · [src:S01:L9528-L9544](../../../INBOX/opm-libro.txt#L9528-L9544)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.5.1 Skipping Takes Precedence Over Waiting

- **P3742** · `fact` · A preprocess object set may include both condition links and non-condition links, i.e. procedural links without the condition control modifier. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3743** · `fact` · The distinguishing aspect of condition links is their skip semantics—skipping or bypassing a process if the source object operational instance of the condition link does not exist or is not a the required state. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3744** · `fact` · Without the condition control modifier, the non-existence of an operational instance of the procedural link source object causes the process to wait for another event and operational instances of all source objects to exist, possibly in a specified state, thus satisfying the precondition. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3745** · `fact` · Meeting all the conditions associated with all the objects or states in the preprocess object set connected with condition links is necessary to satisfy the precondition and start the process. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3746** · `fact` · If the preprocess object set has one or more objects or states connected with non-condition links and one or more objects or states connected with condition links, a conflict may arise between the wait semantics induced by the non-condition link(s) and the skip semantics induced by the condition link(s). · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3747** · `definition` · To resolve the conflict, the skip semantics is defined to be stronger than wait semantics, as stated by the following skip semantics precedence OPM principle. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3748** · `fact` · The Skip Semantics Precedence OPM Principle Skip semantics takes precedence over wait semantics. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3749** · `requirement` · Even if just one of the conditions associated with the condition links connecting with the process does not exist, the precondition satisfaction evaluation shall fail, execution control skips the process, and an event occurs that initiates the next sequential process (or the next two or more parallel processes). · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3750** · `fact` · Conditions associated with condition links are the first to be considered during precondition evaluation, because if they are not met, the process being considered for execution is skipped, regardless of the evaluation result of the remaining part of its precondition. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3751** · `fact` · If the skipped process is within an in- zoom context and there is a subsequent process in this context, execution control initiates that next process, otherwise execution control transfers back to the in-zoomed process. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)
- **P3752** · `fact` · There are two kinds of basic condition links: condition transforming links and condition enabling links. · [src:S01:L9546-L9570](../../../INBOX/opm-libro.txt#L9546-L9570)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.5.2 Condition Transforming Links

- **P3753** · `fact` · A condition consumption link connects a consumee to a process with the addition of the control modifier c. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3754** · `constraint` · Table 22.6 summarizes the basic condition transforming links.
  - [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
  - [src:S01:L9634-L9655](../../../INBOX/opm-libro.txt#L9634-L9655)
- **P3755** · `constraint` · Table 22.6 Condition transforming link summary Name Semantics Sample OPD & OPL Source Destination Condition consumption link If an object instance exists and the rest of the process precondition is satisfied, then the process performs and consumes the object instance, otherwise execution control advances to initiate the next process. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3756** · `fact` · Conditioning object Conditioned process Process occurs if Object exists, in which case Process consumes Object, otherwise Process is skipped. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3757** · `fact` · Condition effect link If an object instance exists and the rest of the process precondition is satisfied, then the process performs and affects the object instance, otherwise execution control advances to initiate the next process. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3758** · `fact` · Conditioning object Conditioned process Process occurs if Object exists, in which case Process affects Object, otherwise Process is skipped. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3759** · `fact` · If at runtime (i.e., during execution of the system model) a consumee instance exists when an event initiates the process, then the presence of that consumee instance satisfies the process precondition with respect to that object. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3760** · `fact` · If evaluation of the entire precondition, which accounts for the entire preprocess object set (of which the consumee is a part) is satisfied, the process starts and consumes that consumee instance. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3761** · `fact` · However, if a consumee instance does not exist when an event initiates the process, then, regardless of the rest of the preprocess object set, the process precondition evaluation fails, and the flow of execution control bypasses (skips) the process without executing that process. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3762** · `fact` · A condition effect link like its regular, non-condition effect link counterpart, connects an affectee to a process, with the addition of the control modifier c. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3763** · `fact` · If at runtime an affectee instance exists when an event initiates the process, then the presence of that affectee instance satisfies the process precondition with respect to that object. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
- **P3764** · `fact` · As with the condition consumption link, if evaluation of the entire precondition, which accounts for the entire preprocess object set (of which the affectee is a part) is satisfied, the process starts and affects that affectee instance, but if not, then the process precondition evaluation fails, and the flow of execution control bypasses the process without executing that process. · [src:S01:L9572-L9632](../../../INBOX/opm-libro.txt#L9572-L9632)
