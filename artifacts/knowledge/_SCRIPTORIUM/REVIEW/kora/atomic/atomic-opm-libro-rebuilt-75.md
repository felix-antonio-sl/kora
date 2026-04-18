---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-75
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
      n_propositions: 49
      segmented: true
      segment_role: segment
      segment_index: 75
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-75
---

# Atomic opm-libro-rebuilt - Segmento 75

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `49`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `75/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.10 Operational Semantics in In-Zoomed Process Contexts

- **P3867** · `fact` · In-zooming of a process specifies transfer of execution control to subprocesses at the next detail level. · [src:S01:L9942-L9951](../../../INBOX/opm-libro.txt#L9942-L9951)
- **P3868** · `fact` · Executing a process with an in-zoomed context recursively transfers execution control to the top-most subprocess(es) within the context of the deepest process. · [src:S01:L9942-L9951](../../../INBOX/opm-libro.txt#L9942-L9951)
- **P3869** · `constraint` · Control returns to the in-zoomed process after its last subprocess completes its execution (Fig. 22.8). · [src:S01:L9942-L9951](../../../INBOX/opm-libro.txt#L9942-L9951)
- **P3870** · `constraint` · Batch implies iteration of Machining nine times, each time producing one Shaft performed sequentially and iteratively 9 times to yield the nine Shafts · [src:S01:L9942-L9951](../../../INBOX/opm-libro.txt#L9942-L9951)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.10.1 Implicit Invocation Link

- **P3871** · `fact` · An implicit invocation link is a link that is not visible graphically but is implied from the vertical layout of processes within the context of an in-zoomed process. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3872** · `fact` · Similar to its explicit counterpart, the implicit invocation link signifies initiation of a subsequent process or concurrently beginning processes. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3873** · `fact` · Since invocation is an event, satisfaction of the precondition for each subprocess is necessary to allow that subprocess to start executing. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3874** · `constraint` · An implicit invocation link can be (1) from a process to its first (or several) subprocess(es), (2) from a subprocess to one or more subprocesses just below it along the time line inside the context of an in- zoomed process, or (3) from the last in-zoomed subprocess(es) to their enclosing, context defining process. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3875** · `constraint` · Specifically, (1) upon arriving at an in-zoomed process context, control immediately transfers to the subprocess (es) with the highest ellipse (oval) top-most point within this in-zoomed process context. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3876** · `constraint` · The implicit invocation link from an in-zoomed process to its top-most subprocess transfers execution control. (2) Along the process timeline, the completion of a source subprocess (or the last subprocess to finish executing in the case of two or more subprocesses that started concurrently) immediately initiates the subsequent subprocess(es) using the implicit invocation link. (3) Upon completion of performing the subprocess with an ellipse top-most point that is lowest within this in-zoomed process context, execution control returns to the in-zoomed process. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3877** · `fact` · When two or more subprocesses have their top-most ellipse points at the same height, then an implicit invocation link initiates each process and they start in parallel upon individual precondition satisfaction. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3878** · `fact` · The process that completes last initiates the next subprocess or set of parallel subprocesses. In the OPD on the left hand side of Fig. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3879** · `constraint` · 22.9, Cleaning invokes Coating, so Cleaning affects Product first and then Coating affects Product. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3880** · `fact` · The invocation link dictates this process sequence. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3881** · `fact` · In the equivalent OPD on the right hand side of Fig. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3882** · `constraint` · 22.9, Finishing zooms into Cleaning and Coating, with the former’s ellipse top point above the latter’s, so when Finishing starts, control immediately transfers to Cleaning, and when Cleaning ends, the implicit invocation link invokes Coating. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)
- **P3883** · `fact` · The two OPDs are semantically equivalent, but the one on the left does not have Finishing as an enclosing context, making it less expressive from a system viewpoint while using two links more than the OPD on the left. · [src:S01:L9953-L9981](../../../INBOX/opm-libro.txt#L9953-L9981)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.10.2 Implicit Parallel Invocation Link Set

- **P3884** · `fact` · Graphically, when the ellipse top points of two or more subprocesses within the scope of an in-zoomed process are at the same height (with possible allowable tolerance), these subprocesses are initiated and begin in parallel, and each starts executing subject to the satisfaction of its precondition. · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)
- **P3885** · `fact` · In this situation, there is a set of implicit invocation links from the source in-zoomed process to each one of the parallel subprocesses. · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)
- **P3886** · `fact` · Process synchronization is such that when the last one of these subprocesses ends, execution control initiates the next subprocess(es). · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)
- **P3887** · `fact` · If there are two or more subprocesses with a lower ellipse top point at the same height, the control initiates them in parallel. · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)
- **P3888** · `fact` · If there are no more subprocesses to invoke, control returns to the in-zoomed refineable process. G). B and C start upon completion of A. · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)
- **P3889** · `fact` · D starts upon completion of the longer process from among B and C. E, F, and G start upon completion of D. · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)
- **P3890** · `fact` · Execution control returns to Processing upon completion of the longest process from among E, F, and G. . · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)
- **P3891** · `constraint` · Table 22.11 summarizes the implicit invocation link kinds. · [src:S01:L9984-L10000](../../../INBOX/opm-libro.txt#L9984-L10000)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.10.3 Link Distribution Across Context

- **P3892** · `fact` · Graphically, a procedural link attached to the contour of an in-zoomed process has distributive semantics. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3893** · `fact` · Leaving a link attached to the contour of the in-zoomed process means that the link is distributed and attached to each one of the subprocesses. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3894** · `fact` · The contour of the in-zoomed process has semantics analogous to that of algebraic parentheses following a multiplication symbol, which distribute the multiplication operator to the expressions inside the parentheses. In Fig. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3895** · `constraint` · 22.11, the OPDs on the left and right are equivalent, but the one on the left is clearer and less cluttered. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3896** · `fact` · An agent link from A to P means that A handles the subprocesses P1, P2, and P3. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3897** · `fact` · An instrument link from B to P means that the subprocesses P1, P2, and P3 require B. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3898** · `fact` · Analogously in algebra, suppose the agent (or instrument) link was a multiplication operator, A was a multiplier and in-zooming was addition, such that P = P1 + P2 + P3, and P was a multiplicand, then AP = A(P1 + P2 + P3) = AP1 + AP2 + AP3. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3899** · `requirement` · If an enabler connects to the outer contour of an in-zoomed contour it must connect to at least one of its subprocesses. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3900** · `requirement` · Consumption and result links must not be attached to the outer contour of an in-zoomed process because this violates temporal logical conditions. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3901** · `fact` · With a distributed consumption link, an attempt would be made to consume an already-consumed object by a subprocesses that is not the first to perform. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3902** · `fact` · Similarly, a distributed result link would attempt to create an already existing object instance. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3903** · `fact` · The modeler needs to be careful when more than one process creates the same object, i.e. more than one instance of the object exists, or two or more processes affect or consume the same object. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3904** · `fact` · OPM modeling tools need to track the number of instances of an object. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3905** · `constraint` · Table 22.11 Implicit invocation link summary In Fig. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3906** · `constraint` · 22.12, the OPD on the left contains invalid consumption and result links, as annotated in the OPL. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3907** · `fact` · The consumption link gives rise to the OPL sentence “P consumes C.” The reason is that applying link distribution, the consequence is the three OPL sentences “P1 consumes C.”, “P2 consumes C.”, and “P3 consumes C.”. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3908** · `fact` · However, since P1 consumes C first according to its temporal order, the same instance of C does not exist when P2 or P3 performs, and therefore neither P2 nor P3 can consume C again. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3909** · `fact` · Similarly, the same instance of B results only once. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3910** · `fact` · The OPD on the right depicts valid links since they specify which of the subprocesses of P consumes C (it is P1) and which one yields B (P2). · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3911** · `requirement` · Since attaching a consumption or result link to an in-zoomed process is invalid, when a process is in- zoomed, all the consumption and result links that were attached to it shall be attached initially or by default to its first subprocess. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3912** · `fact` · It is the modeler’s responsibility to move the links to subsequent subprocesses as needed. version As soon as the modeler in-zooms P in Fig. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3913** · `constraint` · 22.12 and inserts P1 into its context, the modeling tool should migrate the destination end of the consumption link emanating from C from P to P1. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3914** · `fact` · Similarly, the source end of the result link to B should also migrate from P to P1. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
- **P3915** · `constraint` · When the modeler adds P2, the modeler may migrate the destination end of the consumption link and/or the source end of the result link from P1 to P2, as Fig. 22.12 shows. · [src:S01:L10002-L10044](../../../INBOX/opm-libro.txt#L10002-L10044)
