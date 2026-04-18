---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-12
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
      segment_index: 12
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-12
---

# Atomic opm-libro-rebuilt - Segmento 12

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `49`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `12/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 7 Controlling the System’s Behavior / 7.9 How Is Diagnosing Done?

- **P0599** · `fact` · As we retargeted the Accelerometer to be the instrument of Acceleration Measuring, we stripped Diagnosing off its instrument. How then is Diagnosing carried out? · [src:S01:L1841-L1853](../../../INBOX/opm-libro.txt#L1841-L1853)
- **P0600** · `requirement` · Pondering into the name Sensing and Diagnostic Module as the part of the system that has a sensing capability and the Accelerometer as one of its parts, we conclude that Sensing and Diagnostic Module must also contain a part that is in charge of the diagnosis. · [src:S01:L1841-L1853](../../../INBOX/opm-libro.txt#L1841-L1853)
- **P0601** · `fact` · Hence we model the Sensing and Diagnostic Module as consisting of three parts: the Accelerometer and two other parts. One is the Sensing Unit (which in Fig. · [src:S01:L1841-L1853](../../../INBOX/opm-libro.txt#L1841-L1853)
- **P0602** · `constraint` · 7.2 was called SDM Sensor), and the other is the Diagnostics Unit. This structure is modeled in Fig. · [src:S01:L1841-L1853](../../../INBOX/opm-libro.txt#L1841-L1853)
- **P0603** · `constraint` · 7.3 and is expressed in the following OPL sentence: Sensing and Diagnostic Module consists of Accelerometer, Sensing Unit, and Diagnostics Unit. Examining Fig. · [src:S01:L1841-L1853](../../../INBOX/opm-libro.txt#L1841-L1853)
- **P0604** · `constraint` · 7.3 we see that Sensing Unit is part not just of Sensing and Diagnostic Module, but also of the newly introduced object Sensors Set. · [src:S01:L1841-L1853](../../../INBOX/opm-libro.txt#L1841-L1853)
- **P0605** · `fact` · Indeed, another OPL sentence in our OPL paragraph reads: Sensing and Diagnostic Module consists of Accelerometer, Sensing Unit, and Diagnostics Unit. · [src:S01:L1841-L1853](../../../INBOX/opm-libro.txt#L1841-L1853)

## opm libro · Chapter 8 Abstracting and Refining

- **P0606** · `fact` · Make everything as simple as possible, but not simpler. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)
- **P0607** · `fact` · Albert Einstein So far we always increased the refinement (detail) level of our model and we did it via zooming into processes. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)
- **P0608** · `fact` · There are cases where we need to decrease the refinement level, or, in other words, abstract the model. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)
- **P0609** · `fact` · This can happen when we realize that there are too many details already squeezed into a single diagram, making it too crowded and hence less comprehensible. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)
- **P0610** · `fact` · We do not want to delete details of the model, as they are important for complete system specification. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)
- **P0611** · `fact` · Yet we want then taken out of a specific crowded diagram. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)
- **P0612** · `fact` · We do this by creating a new OPD at an intermediate detail level by zooming out of the too detailed OPD and creating one at a higher level of abstraction. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)
- **P0613** · `fact` · In this chapter we focus on this abstracting process and then discuss and improve a structural view of the system. · [src:S01:L1889-L1898](../../../INBOX/opm-libro.txt#L1889-L1898)

## opm libro · Chapter 8 Abstracting and Refining / 8.1 In-Zooming: Refining a Process in a New OPD

- **P0614** · `fact` · Reading carefully the sentence: Regardless of whether the air bags deploy, the SDM [Sensing and Diagnostic Module] transmits crash information to the vehicle's OnStar module. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0615** · `fact` · It looks like airbags are not really essential in our model. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0616** · `fact` · However, examining the sentence further, we notice that our model is missing a subprocess of transmitting the crash information from the Sensing and Diagnostic Module to the OnStar Module, which apparently is another part of the ACR System located inside the Vehicle that we have not yet modeled. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0617** · `fact` · The natural place to add the OnStar Module object and the Crash Info Transmitting process is in the OPD in Fig. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0618** · `constraint` · 6.2, which, for the sake of convenience, is shown here again as Fig. 8.1. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0619** · `fact` · As we see, this OPD is already crowded, so adding it OnStar Module as an object and Crash Info Transmitting as a fifth subprocess inside Automatic Crash Responding would further complicate it, making it even less comprehensible. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0620** · `fact` · An important objective in OPM modeling is to keep each OPD sufficiently clear and readable in order to avoid overwhelming the diagram reader. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0621** · `fact` · Thus, we need to figure out a way to add the new things without overcomplicating this or any other OPD. Examining the four subprocesses in Fig. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0622** · `constraint` · 8.1 we notice that the two middle ones, Message Creating and Message Sending, are of similar nature to that of Crash Info Transmitting, the new subprocess we wish to introduce. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0623** · `fact` · The solution will therefore be to merge Message Creating and Message Sending into a new subprocess which we will call Message Handling. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0624** · `fact` · Then, we will zoom into this new process in a new, separate OPD, exposing three subprocesses: Message Creating, Message Sending, and Crash Info Transmitting. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0625** · `fact` · The merging of Message Creating and Message Sending results in process out-zooming, in which two or more processes are abstracted them into a higher-level process. Doing so has another advantage: in Fig. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0626** · `definition` · 8.2 we define an aggregate object, called In-vehicle ACR Subsystem as a part of Vehicle. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0627** · `fact` · Having done this, we can now model only In-vehicle ACR Subsystem as part of ACR System rather than modeling the entire Vehicle as part of ACR System. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0628** · `fact` · This new In-vehicle ACR Subsystem object consists of OnStar Module and all the other objects inside Vehicle that are part of the ACR System. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0629** · `fact` · This modification further simplifies the OPD. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0630** · `constraint` · Figure 8.2 indeed looks simpler than its previous version in Fig. 8.1. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0631** · `fact` · This simplified version enables us to explicate the relation between Advisor and OnStar Call Center without overcomplicating it. · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)
- **P0632** · `fact` · We add a tagged structural link with the tag operates from, yielding the following OPL sentence: Advisor operates from OnStar Call Center. facilitate OPD comprehension and highlight the c of instrument condition links inside the circle · [src:S01:L1900-L1940](../../../INBOX/opm-libro.txt#L1900-L1940)

## opm libro · Chapter 8 Abstracting and Refining / 8.2 Message Handling In-Zoomed

- **P0633** · `fact` · be Crash Info Creating. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0634** · `fact` · As the two XOR'ed event links from the moderate and severe states of Crash Severity, this process is triggered either by a moderate or a severe crash. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0635** · `constraint` · Only two of the four values of are modeled in Fig. 8.3: moderate and severe. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0636** · `fact` · To remind the diagram reader that there are additional values that are not shown here, the “at least one other state” symbol—a small state symbol with ellipsis (three dots)—is added at the bottom of Crash Severity. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0637** · `fact` · The corresponding OPL sentence is: Crash Severity can be moderate, severe, or at least one other state. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0638** · `fact` · When a process like Message Handling is in-zoomed, there are initially no internal subprocesses, so all the procedural links that start from or end at the in-zoomed process are placed along that process ellipse contour. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0639** · `requirement` · As the modeler specifies the internal subprocesses, each one of these links must be migrated (in GUI terms, its process end needs to be dragged) to the appropriate subprocess. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0640** · `constraint` · Gradually, all the links surrounding the parent, in-zoomed process trickle inwards until none is linked to the parent process, as shown in Fig. 8.3. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0641** · `fact` · This should be done unless the link applies to all the subprocesses inside the in-zoomed process, in which case it should be left there. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0642** · `fact` · A link touching the parent process is supposed to be linked to each one of the subprocesses inside that process. An example appears in Fig. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0643** · `constraint` · 8.2, where crashed Vehicle is instrument to all the four subprocesses inside Automatic Crash Responding.
  - [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
  - [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P0644** · `fact` · The Message Creating process creates the informatical object Message, which consists of two parts: Crash Severity Info and Crash Location. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0645** · `fact` · Crash Severity Info is created by the Sensing and Diagnostic Module, while Crash Location—by the GPS. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0646** · `fact` · These two objects are therefore modeled as instruments of Crash Info Creating. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
- **P0647** · `fact` · These details of which module creates what part are not modeled at this level; they would be shown in the next level down, when Message Creating is in-zoomed. · [src:S01:L1943-L1966](../../../INBOX/opm-libro.txt#L1943-L1966)
