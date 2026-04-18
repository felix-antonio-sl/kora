---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-28
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
      n_propositions: 56
      segmented: true
      segment_role: segment
      segment_index: 28
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-28
---

# Atomic opm-libro-rebuilt - Segmento 28

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `56`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `28/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 11 Object-Process Language: The Text / 11.5 Reserved and Non-Reserved OPL Phrases

- **P1439** · `fact` · While OPL is a subset of English, it is formal. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1440** · `constraint` · The formal syntax for OPL is expressed by a context-free grammar in Extended Backus-Naur Form (EBNF) in Annex A of ISO 19450 Publically Available Specification (see section 24.4.1). · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1441** · `constraint` · The EBNF OPL specification comprises about 400 production rules occupying 12 pages. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1442** · `definition` · Using EBNF, a set of production rules unambiguously defines how OPL sentences are to be constructed and parsed. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1443** · `constraint` · Figure 11.2 presents three production rules as examples of expressing the OPL syntax in EBNF. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1444** · `fact` · Each production rule has a right hand side and a left hand side, separated by the = sign. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1445** · `fact` · The first production rule specifies that an OPL paragraph comprises one or more OPL sentences, separated by a “new line” symbol. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1446** · `fact` · The second production rule specifies that an OPL sentences comprises an OPL formal sentence followed by a full stop (“.”) symbol. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1447** · `fact` · The third production rule specifies that an OPL formal sentence can be of one of four types: a thing description sentence, a procedural sentence, a structural sentence, or a context management sentence. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1448** · `fact` · In programming languages, the analogues of words are tokens—the atomic units resulting from lexical analysis. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1449** · `fact` · In most programming languages, spaces separates tokens apart. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1450** · `fact` · Tokens are input to the next process, parsing. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1451** · `fact` · OPL sentences are obviously far more readable than a script of any computer programming language. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1452** · `fact` · These sentences are carefully designed using a subset of English to convey a clear and straightforward meaning through well-phrased and humanly understandable constructs. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1453** · `fact` · Yet, using the OPL EBNF-based formal syntax definition, OPL sentences can undergo parsing just like commands or lines in a programming language. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1454** · `fact` · As in programming languages, parsing an OPL sentence yields phrases. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1455** · `fact` · A phrase is a combination of one or more words, separated by spaces, which constitutes a logical entity, but not a complete sentence. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1456** · `fact` · OPL phrases can be reserved and non-reserved. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1457** · `fact` · Any OPL sentence consists of non-reserved OPL phrases—domain- or system-specific words or word combinations—which the system architect or modeler uses, and reserved OPL phrases, which link the non-reserved phrases and provide for creating a sentence in a natural language. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1458** · `fact` · An OPL phrase is a sequence of one or more words in an OPL sentence. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1459** · `definition` · A non-reserved OPL phrase is a modeler-defined OPL phrase that expresses a system- or domain-specific OPM model entity or relation name. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1460** · `fact` · Non-reserved OPL phrases are names of OPM objects, processes, and states that the modeler assigns while creating the OPDs that comprise the OPM model. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1461** · `definition` · Non-reserved OPL phrases also include less frequently used ones, such as (user defined) tagged structural relations and participation constraints. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1462** · `fact` · A reserved OPL phrase is an OPL phrase built into the OPL EBNF syntax definition that connects two or more non-reserved OPL phrases. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1463** · `fact` · Reserved OPL phrases are parts of the sentence syntax that express relations or connections between non-reserved OPL phrases, or constrains on them. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1464** · `fact` · Examples of reserved OPL phrases are “requires”, “yields”, “consumes” “and”, “or”, “affects”, “exactly one of”, “at least one”, and “consists of”. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1465** · `fact` · These definitions of reserved and non-reserved phrases stipulate that the former are the mortar that “glues” and holds together in a meaningful way the model building blocks—the non-reserved phrases that express system-specific terms. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1466** · `fact` · The following bolding OPL convention helps distinguish between the two kinds of OPL phrases. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1467** · `fact` · The Bolding OPL Convention Non-reserved OPL phrases appear in Arial bold font, while reserved OPL phrases appear in Arial non-bold font. Punctuation marks are bolded. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1468** · `fact` · For example, the OPL phrase “Automatic Crash Responding” in the OPL sentence “Automatic Crash Responding affects Vehicle Occupants Group.” is non-reserved and therefore appears in Arial bold font. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1469** · `fact` · The non-bold phrases, such as “and”, “or”, “affects”, “exactly one of”, and “consists of”, are reserved OPL phrases. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1470** · `fact` · A CASE tool implementation needs to automatically translate the model facts expressed by the OPD constructs into OPL sentences. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1471** · `fact` · To further help distinguish between things, such tools should use colors in fonts of phrases that match their colors in the OPD. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1472** · `fact` · For objects, the default color in OPCAT is green, for processes—blue, for states—brown, and non-reserved OPL phrase are in black font. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1473** · `fact` · If your book version enables seeing colors, Fig. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)
- **P1474** · `constraint` · 10.6, which is an OPCAT-generated OPM model of the process test system, exemplifies this coloring convention. · [src:S01:L3853-L3908](../../../INBOX/opm-libro.txt#L3853-L3908)

## opm libro · Chapter 11 Object-Process Language: The Text / 11.6 Motivation for OPM’s Bimodal Expression

- **P1475** · `fact` · A legitimate question that can be raised with respect to OPL is why is text needed in addition to the diagram if we have a good graphic representation of our model? · [src:S01:L3910-L3915](../../../INBOX/opm-libro.txt#L3910-L3915)
- **P1476** · `fact` · One may indeed wonder why two modalities are needed. · [src:S01:L3910-L3915](../../../INBOX/opm-libro.txt#L3910-L3915)
- **P1477** · `constraint` · According to the graphics-text equivalence OPM principle, the text and the graphics express the same contents, so there is a 100% redundancy in terms of information content! Isn’t this a waste of resources? · [src:S01:L3910-L3915](../../../INBOX/opm-libro.txt#L3910-L3915)
- **P1478** · `fact` · Wouldn’t it make more sense to stick to just one modality—either graphics or text—and leave the other out? · [src:S01:L3910-L3915](../../../INBOX/opm-libro.txt#L3910-L3915)

## opm libro · Chapter 11 Object-Process Language: The Text / 11.6.1 The Dual-Channel Assumption

- **P1479** · `fact` · The graphics-text equivalence is a major source of OPM’s expressive power. OPL text complements the OPD graphics. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1480** · `constraint` · This duality implements the dual-channel assumption (Clark and Paivio 1991; Baddeley 1992). · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1481** · `constraint` · This is one of three major research-supported cognitive assumptions (Mayer 2003; · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1482** · `constraint` · Mayer and Moreno 2003), which stipulates that humans possess separate channels and mechanisms for processing visual and verbal representations. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1483** · `constraint` · The combination of OPD and OPL caters directly to this dual-channel assumption (Dori 2008). · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1484** · `fact` · Some humans are more visually inclined, while others are more text-oriented. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1485** · `fact` · The text and the graphics reinforce each other while the model creator or the model readers try to make sense of the semantics that model elements convey in various combinations. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1486** · `fact` · The cognitive-physiological basis for this principle is that the human mind is geared to accept both visual-pictorial-graphic signals and audio-verbal-written signals. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1487** · `fact` · Graphics and text trigger different areas in the brain. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1488** · `fact` · Popularly, this is often referred to as the left brain/right brain functions. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1489** · `fact` · Indeed, the left hemisphere is dominant in language, processing what one hears and handling most of the duties of speaking. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1490** · `fact` · The right hemisphere is mainly in charge of spatial abilities, face recognition, comprehending visual imagery and making sense of what we see. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1491** · `fact` · Thus, catering to “both sides of the brain” through language and pictures is more likely to get the message—the conceptual model—across. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1492** · `fact` · Accordingly, a model that can be presented bimodally in both graphic and text is preferred over a model that can be presented in only one of the modalities. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1493** · `fact` · Almost all conceptual modeling languages are either textual or graphical, but not both. · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
- **P1494** · `constraint` · OPM is the first to combine the two modalities (USPTO 7,099,809, 2006). · [src:S01:L3917-L3934](../../../INBOX/opm-libro.txt#L3917-L3934)
