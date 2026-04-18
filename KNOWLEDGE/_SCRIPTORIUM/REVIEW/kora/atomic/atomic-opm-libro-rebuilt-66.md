---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-66
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
      n_propositions: 43
      segmented: true
      segment_role: segment
      segment_index: 66
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-66
---

# Atomic opm-libro-rebuilt - Segmento 66

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `43`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `66/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.9 In-Zooming and Out-Zooming

- **P3414** · `fact` · In-zooming is a refinement operation, usually applied to processes, which specifies the subprocesses of the process being in-zoomed, as well as their (possibly partial) performance or execution order. As an example, in Fig. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3415** · `constraint` · 21.6, the process Check-Based Paying from Fig. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3416** · `constraint` · 19.13 is in-zoomed in the descendant OPD on the right, showing its four subprocesses, as expressed in the OPL sentence: Check-Based Paying zooms into Writing & Signing, Delivering & Accepting, Endorsing & Submitting, and Cashing & Cancelling, in that sequence. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3417** · `fact` · The execution order of these four processes follows the timeline OPM principle, repeated here: The Timeline OPM Principle The timeline within an in-zoomed process is directed by default from the top of the in-zoomed process ellipse to its bottom. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3418** · `fact` · The execution order is expressed in OPL by the reserved phrase in that sequence at the end of the in- zooming sentence. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3419** · `fact` · The exposition of the four subprocesses in the context of the Check-Based Paying process provides for explicitly specifying how the states of both Check and Keeper change throughout the lifecycle of check, as also expressed in the OPL sentence to the left of the OPD. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3420** · `fact` · Within the context of the in-zoomed process there may be partial order: overall there is an order dictated by the timeline, but two or more processes can be performed in parallel. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3421** · `fact` · As an example, suppose a process P zooms into seven subprocesses, SP1, SP2 … SP7, such that SP1 executes first, then SP2 and SP3 in parallel, then SP4, and finally SP5, SP6, and SP7 in parallel. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3422** · `fact` · Then the OPL sentence will be: P zooms into SP1, parallel SP2 and SP3, SP4, and parallel SP5, SP6, and SP7, in that sequence. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)
- **P3423** · `fact` · Check and Keeper undergo, as well as the agents involved in each subprocess OPM can be considered process-oriented from the aspect of giving priority to modeling processes first (initially the system’s function, the process that delivers the external value) and recursively zooming into this function while modeling the objects that are relevant to each process at the corresponding detail level. · [src:S01:L8724-L8751](../../../INBOX/opm-libro.txt#L8724-L8751)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.9.1 In-Diagram and New-Diagram In-Zooming

- **P3424** · `fact` · Like unfolding, in-zooming can be done either in the current OPD or in a new OPD. · [src:S01:L8753-L8762](../../../INBOX/opm-libro.txt#L8753-L8762)
- **P3425** · `fact` · In-diagram in-zooming is in-zooming in which no new OPD is created, and the refineable appear in-zoomed along with its refinees in the same OPD. · [src:S01:L8753-L8762](../../../INBOX/opm-libro.txt#L8753-L8762)
- **P3426** · `fact` · New-diagram in-zooming is in-zooming in which the refineable and its refinees appear in-zoomed in a new OPD. · [src:S01:L8753-L8762](../../../INBOX/opm-libro.txt#L8753-L8762)
- **P3427** · `fact` · All the examples so far were of new-diagram in-zooming. · [src:S01:L8753-L8762](../../../INBOX/opm-libro.txt#L8753-L8762)
- **P3428** · `fact` · Indeed this is the more prevalent way of in- zooming, since in-zooming requires a lot of “real estate” to specify the internal subprocesses and the process being in-zoomed, as well as for depicting the additional relevant objects with links to these new subprocesses, making the current OPD often too crowded. However, as Fig. · [src:S01:L8753-L8762](../../../INBOX/opm-libro.txt#L8753-L8762)
- **P3429** · `constraint` · 21.12 shows, in-diagram in- zooming is also useful. · [src:S01:L8753-L8762](../../../INBOX/opm-libro.txt#L8753-L8762)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.9.2 In-Zooming and Out-Zooming of Objects

- **P3430** · `fact` · Just like process in-zooming has the aggregation-participation semantics between the in-zoomed process and its temporally-ordered subprocesses, so does object in-zooming has the aggregation-participation semantics between the in-zoomed object and its spatially-ordered parts. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3431** · `fact` · In other words, the spatial order according to the top-down or left-to-right layout of the parts determines their order. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3432** · `fact` · This is demonstrated in the metamodel in Fig. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3433** · `constraint` · 21.7: Whole from SD zooms in SD1 into Part A and Part B, in that vertical sequence. If Part A and Part B in Fig. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3434** · `constraint` · 21.7 would be arranged horizontally, the OPL sentence would be: Whole from SD zooms in SD1 into Part A and Part B, in that horizontal sequence. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3435** · `definition` · The ability to define order within objects opens the way to modeling tables and matrices of any dimension. For example, we can rename Whole in Fig. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3436** · `constraint` · 21.7 to be Table, and Part A and Part B can be called Row 1 and Row 2, respectively. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3437** · `constraint` · In the next in-zoom level, each row can be in-zoomed to expose its elements, arranged horizontally, e.g., Row 1 zooms into Element (1,1), Element (1,2), and Element 1,3), in that horizontal sequence. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3438** · `constraint` · Thus, Element (1,2) will be the second element in the first row of the matrix. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3439** · `fact` · A third dimension can be achieved by zooming into each element, this time vertically, and this can proceed recursively. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3440** · `fact` · Each in-zooming operation, applied to all the elements at the current level, adds one more dimension. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3441** · `fact` · Since each element can have a value, we can use OPM to do matrix operations, such as addition or multiplication, and OPM tables can be used for relational databases. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3442** · `fact` · Time is one-dimensional and flows only forward, so to determine process execution order—the timing—we only needed the vertical axis to specify the order of the subprocesses in an in-zoomed process. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3443** · `fact` · Physical objects, however, are three-dimensional, so for object in-zooming we can at least schematically model the relative layout of object parts in two dimensions, taking advantage of the fact that the paper or computer screen used for conceptual modeling are two-dimensional. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3444** · `definition` · The limitation here is that objects are rectangular rather than arbitrarily shaped, but we can still get a schematic, albeit rough, Since the aggregation-participation fundamental structural relation does not prescribe any partial order of process performance, the modeling of synchronous process refinement must use in-zooming, in which order can be defined. The system in Fig. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3445** · `definition` · 10.5 is synchronous: there is a fixed, well-defined order of each subprocess within the in-zoom context of Dish Washing. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3446** · `fact` · To model asynchronous process refinement we use the aggregation-participation fundamental structural link, either through in-diagram aggregation unfolding or as a new-diagram aggregation unfolding of the process. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3447** · `constraint` · Figure 21.8 depicts a portion of a Home Safety System that carries out the function Home Safety Maintaining, which includes the subprocesses Burglary Handling, Fire Protecting, and Earthquake Alarming. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3448** · `fact` · Since the order of these three subprocesses is unknown, the OPD uses in- diagram aggregation unfolding with an aggregation-participation link from this function rather than an in- zoomed version of Home Safety Maintaining. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)
- **P3449** · `fact` · Home Safety Maintaining in-zooms to a recurring systemic process, Monitoring & Detecting, for which Detection Module is an instrument and Threat Appearing is an environmental process. · [src:S01:L8764-L8827](../../../INBOX/opm-libro.txt#L8764-L8827)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.11 The Equivalence between In-Zooming and Unfolding

- **P3450** · `fact` · One can express the details of a synchronous process via both in-zooming and unfolding. · [src:S01:L8830-L8841](../../../INBOX/opm-libro.txt#L8830-L8841)
- **P3451** · `constraint` · Figure 21.9 presents a process P in-zoomed, in the OPM model on the left, and its equivalent OPM model on the right, in which P is unfolded. However, as we can see in Fig. · [src:S01:L8830-L8841](../../../INBOX/opm-libro.txt#L8830-L8841)
- **P3452** · `constraint` · 21.9, in-zooming is preferable as it requires less symbols and yield a shorter OPL paragraph. · [src:S01:L8830-L8841](../../../INBOX/opm-libro.txt#L8830-L8841)
- **P3453** · `fact` · Using in-zooming rather than unfolding, we can use instrument and result links instead of instrument event link and result event link, because the events within an in-zoomed context are implicit. · [src:S01:L8830-L8841](../../../INBOX/opm-libro.txt#L8830-L8841)
- **P3454** · `fact` · Importantly, when a process is in-zoomed, its subprocesses are its parts, while the objects exposed as a result of this in-zooming are the process’ attributes. · [src:S01:L8830-L8841](../../../INBOX/opm-libro.txt#L8830-L8841)
- **P3455** · `fact` · Symmetrically, when an object is in-zoomed, its internal objects are its parts, while its internal processes are its operations. · [src:S01:L8830-L8841](../../../INBOX/opm-libro.txt#L8830-L8841)
- **P3456** · `fact` · The latter fact provides for depicting processes as operations of an object by putting them inside the in-zoomed view of that object. · [src:S01:L8830-L8841](../../../INBOX/opm-libro.txt#L8830-L8841)
