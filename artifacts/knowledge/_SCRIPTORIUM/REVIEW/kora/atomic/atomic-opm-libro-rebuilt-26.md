---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-26
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
      n_propositions: 60
      segmented: true
      segment_role: segment
      segment_index: 26
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-26
---

# Atomic opm-libro-rebuilt - Segmento 26

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `60`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `26/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 10 Things: Objects and Processes / 10.10.2 How to Model State-Preserving Processes with Tagged Structural

- **P1346** · `fact` · Links Many of the state-preserving verbs can be considered as working against some “force,” which would otherwise change some object. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1347** · `fact` · For example, a Pedestal supporting a Statue works against gravity, so we can think of Supporting as a “fall preventing” process, without which the state of the Statue would change from stabilized to fallen. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1348** · `fact` · The Supporting process starts as soon as the Statue is positioned and keeps going until something in the system changes, e.g., the Pedestal undergoes a process of Breaking, changing its state from intact to broken. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1349** · `fact` · As a more modern example, an Autopilot is a system that is designed to maintain and stabilize an Aircraft in its course, working against lift, drag, gravity, and the centrifugal force. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1350** · `fact` · Once the state-maintaining process ends, the state will change, so you need to capture this process as a recurring one—whether through self-invocation, presented in Sect. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1351** · `constraint` · 22.4.6 or controlled response to an external trigger. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1352** · `fact` · The static nature of state-preserving processes is contradictory to the definition of process, which requires that it transforms some object. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1353** · `fact` · In such cases, it is often possible, and even desirable, to model the relation between the two pertinent objects using a tagged structural link instead of a process. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1354** · `fact` · This approach to modeling persistent processes is exemplified in Fig. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1355** · `constraint` · 10.10, which shows Supporting as a state-preserving process. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1356** · `fact` · On the left hand side is the dynamic version of the model, in which Supporting is an explicit process, presented with its corresponding OPL paragraph. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)
- **P1357** · `fact` · On the right is the static model version, in which the tagged structural relation supports expresses the time-invariant relation between Foundation and House, giving rise to a corresponding more compact and more expressive one-sentence OPL paragraph: Foundation supports House. · [src:S01:L3526-L3545](../../../INBOX/opm-libro.txt#L3526-L3545)

## opm libro · Chapter 10 Things: Objects and Processes / 10.10.3 Transient Objects and Their Invocation Link Substitute

- **P1358** · `fact` · Transient objects are the analogous counterparts of persistent processes. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1359** · `fact` · A transient object is a short-lived physical or informatical object. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1360** · `fact` · Examples of transient objects are unstable materials, such as an interim short-lived compound in a chemical reaction or an atom in an excited state that spontaneously decays to the ground state by emission of X-rays and fluorescent radiation. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1361** · `fact` · Another example of a transient object is a packet in a telecommunication network. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1362** · `fact` · Such a packet can reside for a short while at some router on its way and leave no trace once the target node has received it. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1363** · `fact` · In an OPM model, a transient object that is created by a process and immediately consumed by the next process can be skipped by using the invocation link, a lightning-shaped procedural link that directly connects the two processes. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1364** · `constraint` · Figure 10.11 demonstrates the notions of transient object and invocation link. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1365** · `fact` · On the left hand side is a model in which Spark is an explicit object created by Igniting. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1366** · `fact` · The presence of Spark is an event that initiates (triggers) Exploding, as denoted by the letter e next to the arrowhead pointing to Exploding. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1367** · `fact` · Exploding immediately consumes Spark, so Spark is transient and short-lived. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1368** · `fact` · On the right hand side is an alternative, more compact model, in which the transient Spark is suppressed by the invocation link. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1369** · `fact` · The semantics of the invocation link is that the end of Igniting is the event that triggers Exploding. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1370** · `constraint` · The OPL paragraph in this case is also more compact. Looking back at Fig. 10.10 and comparing it to Fig. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1371** · `constraint` · 10.11, we can see the pattern: The use of the invocation link as a shorter version of modeling generation and immediate consumption of a transient object is analogous to the use of the tagged structural link as a shorter version of modeling a persistent process. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)
- **P1372** · `fact` · Another example is Signaling and the transient object Signal. · [src:S01:L3547-L3569](../../../INBOX/opm-libro.txt#L3547-L3569)

## opm libro · Chapter 10 Things: Objects and Processes / 10.11 Operator, Operand, and Transform

- **P1373** · `constraint` · Before concluding this chapter on the dynamics of systems, it may be interesting to compare the OPM ontology to the definitions of Ashby (2001) regarding operand, operator and transform: Consider the simple example in which, under the influence of sunshine, pale skin changes to dark skin. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1374** · `fact` · Something, “the pale skin”, is acted on by a factor, “the sunshine”, and is changed to dark skin. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1375** · `fact` · That which is acted on, the pale skin, will be called the OPERAND, the [causing] factor will be called the OPERATOR, and that what the operand has changed to, will be called the TRANSFORM. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1376** · `fact` · In the OPM ontology, Skin is an object, while dark and pale are states of an attribute of the object Skin called Complexion. Skin is one of the parts of Person. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1377** · `fact` · Tanning is a process, and Sun is an instrument that enables the Tanning process, the effect of which is to change the Complexion of the Skin from pale to dark. This terminology and the OPM model in Fig. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1378** · `constraint` · 10.12 seem more intuitive and appropriate for non- mathematical systems than the operand, operator and transform ontology. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1379** · `fact` · The “sunshine factor” is a bit problematic to describe. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1380** · `fact` · It is not clear whether it refers to the shining process of the sun or to the object that aggregates the photons of energy radiated by the sun, which the skin absorbs. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1381** · `fact` · In OPM, we would model Radiating as a first subprocess of Tanning. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1382** · `fact` · Radiating requires (i.e., is enabled by the instrument) Sun. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1383** · `fact` · Radiating, in turn, produces the object Solar Energy, which is absorbed by the Skin via the second subprocess, Absorbing & Pigmenting, the one that changes the Complexion of Skin from pale to dark. · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1384** · `fact` · In summary, the operator is the process (Tanning). · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)
- **P1385** · `fact` · The operand is the affectee in its state before the process occurred (Skin in its pale Complexion state), while the transform is its state after the process occurred (Skin in its dark Complexion state). · [src:S01:L3573-L3595](../../../INBOX/opm-libro.txt#L3573-L3595)

## opm libro · Chapter 11 Object-Process Language: The Text

- **P1386** · `fact` · Among general-purpose modeling languages dominate the graphical ones such as UML; textual modeling languages are not as popular though they have a big potential. · [src:S01:L3664-L3670](../../../INBOX/opm-libro.txt#L3664-L3670)
- **P1387** · `constraint` · Mazanec and Macek (2012) OPM is bimodal: it employs both the visual (graphical) modality—OPD, and the verbal (textual) modality—OPL. · [src:S01:L3664-L3670](../../../INBOX/opm-libro.txt#L3664-L3670)
- **P1388** · `fact` · The textual OPL representation of the OPM model has both human-oriented and machine-oriented goals. · [src:S01:L3664-L3670](../../../INBOX/opm-libro.txt#L3664-L3670)
- **P1389** · `fact` · This chapter is devoted to presenting OPL and discussing its merits. · [src:S01:L3664-L3670](../../../INBOX/opm-libro.txt#L3664-L3670)

## opm libro · Chapter 11 Object-Process Language: The Text / 11.1 OPL: The Textual Modality

- **P1390** · `fact` · To enhance OPM’s expressive power, we associate with each OPD a collection of sentences in Object- Process Language (OPL) as a textual, natural interpretation of the OPD’s graphic representation. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1391** · `fact` · Object-Process Language (OPL) is a subset of English that expresses textually the OPM model that the OPD set expresses graphically. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1392** · `fact` · OPL is the textual counterpart of the graphic OPM system specification. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1393** · `fact` · It is extracted from the diagrammatic description in the OPD set. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1394** · `fact` · Using a tool such as OPCAT, OPL is an automatically generated textual description of the system in a subset of natural English. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1395** · `fact` · Devoid of the idiosyncrasies and excessive cryptic details that characterize programming languages, OPL sentences are understandable to people without technical or programming experience. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1396** · `fact` · A model fact is a relation between two or more things in an OPM model. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1397** · `fact` · Each model fact is expressed in the OPM model in two modalities: in the graphic modality in one or more OPDs, and in the textual modality in an OPM sentence for each graphical expression of that model fact. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1398** · `fact` · Each OPD element (thing or link) has a graphic symbol. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1399** · `fact` · An OPD construct is a syntactically valid combination of OPM graphic symbols, which expresses a model fact. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1400** · `fact` · That model fact is equivalently expressed by a sentence or part of a sentence in Object-Process Language (OPL) text. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1401** · `fact` · This is summarized in the following set of definitions. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1402** · `fact` · A model fact is expressed graphically by an OPD construct and textually by an equivalent OPL sentence or sentence part. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1403** · `fact` · An OPD element is the graphical expression of a thing or a link. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)
- **P1404** · `fact` · An OPD construct is a collection of connected OPD elements. · [src:S01:L3672-L3692](../../../INBOX/opm-libro.txt#L3672-L3692)

## opm libro · Chapter 11 Object-Process Language: The Text / 11.2 The Dual Purpose of OPL

- **P1405** · `fact` · OPL serves two goals, oriented to two directions: humans and machines. · [src:S01:L3699](../../../INBOX/opm-libro.txt#L3699)
