---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-44
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
      n_propositions: 60
      segmented: true
      segment_role: segment
      segment_index: 44
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-44
---

# Atomic opm-libro-rebuilt - Segmento 44

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `60`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `44/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 15 Participation Constraints and Forks / 15.2 Structural Participation Constraints

- **P2290** · `fact` · Structural participation constraints can be one- or two-sided. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2291** · `fact` · A source participation constraint is a one-sided participation constraint on the source side of the link. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2292** · `fact` · A destination participation constraint is a one-sided participation constraint on the destination side of the link. or the destination link side. The OPD in Fig. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2293** · `constraint` · 15.1 is an example of a destination participation constraint—a tagged structural link, for which the participation constraint is on the destination (link target) object. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2294** · `constraint` · In this example, it is expressed as a specific number, 6. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2295** · `fact` · The destination object Pencil in the OPD of Fig. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2296** · `constraint` · 15.1 has the participation constraint 6, while the object Box has the implicit default participation constraint, which is 1. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2297** · `constraint` · If the participation constraint is explicit, as it is for Pencil in the OPL sentence “Box contains six Pencils”, it means that the participation constraint is greater than 1. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2298** · `constraint` · In this case, while generating the OPL sentence from the OPD, the numeric or symbolic value or mathematical expression of the participation constraint is put before the object name and the object name becomes plural.1 To keep up with English grammar, the verb for any tag, including the null tag, has to conform to the plurality of source and destination things in the sentence. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2299** · `constraint` · For example, if the source Bedroom of a unidirectional null tag has a participation constraint of 3, and the destination is Apartment, the OPL sentence is: “Three Bedrooms relate to Apartment.” To follow the rule to “spell small numbers out”, the numerals (symbols) of numbers from zero to nine should be written in letters or as digits (figures), so “Three Bedrooms relate to Apartment.” is preferable. Therefore the OPL sentence in Fig. 15.1 has in it six rather than 6. Ignoring the participation constrain in Fig. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)
- **P2300** · `constraint` · 15.2, the OPL sentence would be simply “Bolt fasten Flange.” Since the source object Bolt has the participation constraint 8, while the destination object Flange has the implicit default participation constraint, we get OPL sentence in Fig. 15.2. · [src:S01:L5954-L5977](../../../INBOX/opm-libro.txt#L5954-L5977)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.2.1 Parameterized Structural Participation Constraints

- **P2301** · `constraint` · By default, a participation constraint is numeric, i.e., it is specified as a number, usually an integer, as shown in the OPDs in Figs. 15.1 and 15.2. · [src:S01:L5985-L5996](../../../INBOX/opm-libro.txt#L5985-L5996)
- **P2302** · `fact` · However, a participation constraint can also be parameterized, i.e., it can be a mathematical expression containing one or more symbols. · [src:S01:L5985-L5996](../../../INBOX/opm-libro.txt#L5985-L5996)
- **P2303** · `fact` · A parameterized participation constraint is a participation constraint which is a mathematical expression with one or more parameters. the modeler expresses the fact that the number of Cylinders in Engine is even. · [src:S01:L5985-L5996](../../../INBOX/opm-libro.txt#L5985-L5996)
- **P2304** · `constraint` · When numbers, even small ones, are involved in a sentence with parameters, as in Fig. 15.3, or in a range (as in Fig. · [src:S01:L5985-L5996](../../../INBOX/opm-libro.txt#L5985-L5996)
- **P2305** · `constraint` · 15.4, see next section), then the numbers are expressed as digit numerals and not in letters. · [src:S01:L5985-L5996](../../../INBOX/opm-libro.txt#L5985-L5996)
- **P2306** · `constraint` · The syntax of participation constraint expressions and more elaborate example of parameterized participation constraints are provided in Chap. 17 below on aggregation-participation. · [src:S01:L5985-L5996](../../../INBOX/opm-libro.txt#L5985-L5996)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.2.2 Range Participation Constraints

- **P2307** · `fact` · A participation constraint can be more than just a single number or a single expression. It can also be a range. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2308** · `fact` · A range participation constraint is a participation constraint with lower and upper bounds, each possibly an expression, on the number of possible objects that can take part in the relation. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2309** · `fact` · A compound participation constraint can be any combination of numbers, expressions, and ranges. A range is denoted as “qmin .. qmax”. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2310** · `fact` · A single number or parameter can be thought of as a special case of range with qmin = qmax. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2311** · `constraint` · Two compound participation constraints are exemplified in Fig. 15.4. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2312** · `fact` · In the left OPD, the compound participation constraint comprises two ranges. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2313** · `constraint` · In the first range, qmin = 3 is the lower bound and qmax = 5 is the upper bound. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2314** · `constraint` · The two quantities are separated by two consecutive dots. The second range is 8..10. In the right OPD of Fig. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2315** · `constraint` · 15.4, the compound participation constraint comprises one number, 2, and one parameterized range, 3n, where n 4. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2316** · `constraint` · Often, qmin is a small number, such as 0, 1, or 2, while qmax is the symbol , which stands for many. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2317** · `fact` · The symbol is a “reserved symbol” in participation constraint, meaning that the exact value of “many” is not fixed as in an algebraic equation. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)
- **P2318** · `fact` · A letter stands for a parameter—a particular, yet unspecified number. · [src:S01:L5998-L6015](../../../INBOX/opm-libro.txt#L5998-L6015)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.3 Shorthand Notations and Reserved Phrases

- **P2319** · `fact` · The reserved phrase “qmin to qmax” can be used for any of the participation constraints, where both qmin and qmax can be any real number. · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2320** · `fact` · However, it frequently makes more sense to use different phrases that express the participation constraint more naturally. · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2321** · `constraint` · As in UML and SysML, the asterisk symbol stands for “many”, so “0..” means zero or more, or, in other words, “optional”, abbreviated as . · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2322** · `constraint` · The range “1..”, abbreviated as + , means one or more, and as an OPL reserved phrase: “at least one”. · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2323** · `constraint` · The four abbreviated participation constraint symbols are: “?” for 0..1, “” for 0.., nothing for 1..1, and “+” for 1... · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2324** · `fact` · Each such abbreviation has a corresponding OPL reserved phrase. · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2325** · `constraint` · The abbreviated participation constraint symbols, their bounds, OPL reserved phrases, and sample OPDs with corresponding OPL sentences are shown in Table 15.1. Combining particular values is also allowed. · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2326** · `constraint` · For example, the participation constraint “?, 3..” is legal and is translated in OPL as “optional or at least 3”. · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2327** · `fact` · Finally, while all the examples so far referred to objects, they can be applied to processes as well. · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)
- **P2328** · `constraint` · Table 15.1 The abbreviated participation constraint symbols, their bounds, phrases, and sample OPDs with corresponding OPL sentences · [src:S01:L6018-L6039](../../../INBOX/opm-libro.txt#L6018-L6039)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.4 Cardinality

- **P2329** · `fact` · In a structural relation, each link edge—one on the source side and the other on the destination side—can have a participation constraint that is in general independent of the participation constraint on the other edge. · [src:S01:L6041-L6061](../../../INBOX/opm-libro.txt#L6041-L6061)
- **P2330** · `fact` · Source participation constraint is the participation constraint on the source side of the (structural or procedural) link. · [src:S01:L6041-L6061](../../../INBOX/opm-libro.txt#L6041-L6061)
- **P2331** · `fact` · Destination participation constraint is the participation constraint on the destination side of the (structural or procedural) link. · [src:S01:L6041-L6061](../../../INBOX/opm-libro.txt#L6041-L6061)
- **P2332** · `fact` · The definition refers equally to structural and procedural links. · [src:S01:L6041-L6061](../../../INBOX/opm-libro.txt#L6041-L6061)
- **P2333** · `fact` · The combination of the two participation constraints is the link’s cardinality, which also applies to structural and procedural links alike. · [src:S01:L6041-L6061](../../../INBOX/opm-libro.txt#L6041-L6061)
- **P2334** · `fact` · Cardinality is a property of a link whose value depends on the combination of the source and destination participation constraints of the structural link. · [src:S01:L6041-L6061](../../../INBOX/opm-libro.txt#L6041-L6061)
- **P2335** · `fact` · We denote the cardinality as [qmin .. qmax, q′ min .. q′ max], where qmin and qmax are the lower and upper bounds of the participation constraint on the source side of the link, while q′ min and q′ max are the corresponding parameters on the link’s destination side. · [src:S01:L6041-L6061](../../../INBOX/opm-libro.txt#L6041-L6061)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.4.1 The Four Common Cardinality Kinds

- **P2336** · `fact` · Cardinality is an important factor in database schema design, which takes place during the design phase of information systems development. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)
- **P2337** · `fact` · The various kinds of participation constraints on the two structural link edges give rise to a number of combinations. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)
- **P2338** · `constraint` · Traditionally, these combinations were thought of as yielding four possible cardinality kinds: one-to-one, one-to-many, many-to-one and many-to-many. These are exemplified in Fig. 15.5. As the top OPD in Fig. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)
- **P2339** · `constraint` · 15.5 shows, a one-to-one cardinality exists when no participation constraint is recorded on either side of the structural link, in which case the default value 1 is assigned to both sides. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)
- **P2340** · `constraint` · A one-to-many cardinality exists when there is an explicit participation constraint with qmin > 0 and qmax > 1 on exactly one side of the structural link and 1 on the other. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)
- **P2341** · `fact` · This is exemplified in the second OPD in Fig. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)
- **P2342** · `constraint` · 15.5, while the third is an example of many-to-one cardinality. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)
- **P2343** · `constraint` · Finally, a many-to-many cardinality exists when the participation constraints on both sides of the structural link are explicit, and in both qmax > 1, as exemplified in the bottom OPD of Fig. 15.5. · [src:S01:L6063-L6075](../../../INBOX/opm-libro.txt#L6063-L6075)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.4.2 The 16 Cardinality Kinds

- **P2344** · `constraint` · Combining pairs of the four symbols “?”, “”, “1”, and “+”, we get 16 cardinality kinds. · [src:S01:L6077-L6085](../../../INBOX/opm-libro.txt#L6077-L6085)
- **P2345** · `constraint` · These are listed in the 4 4 array in Table 15.2. · [src:S01:L6077-L6085](../../../INBOX/opm-libro.txt#L6077-L6085)
- **P2346** · `constraint` · The array cells with the four customary cardinalities, [1, 1], which is “one- to-one”, [1, +], which is “one-to-many”, [+,1], which is “many-to-one”, and [+, +], which is “many-to- many”, are greyed at the bottom-right part of the table. · [src:S01:L6077-L6085](../../../INBOX/opm-libro.txt#L6077-L6085)
- **P2347** · `constraint` · These cardinality kinds are the ones recognized in entity relationship diagrams (ERDs), proposed by Chen (1976), which are used to design databases. · [src:S01:L6077-L6085](../../../INBOX/opm-libro.txt#L6077-L6085)
- **P2348** · `constraint` · Here we see that they comprise one quarter of the 16 possible combinations. · [src:S01:L6077-L6085](../../../INBOX/opm-libro.txt#L6077-L6085)
- **P2349** · `constraint` · Table 15.2 The 16 cardinality types obtained by combinations of pairs of the four participation constraint kinds · [src:S01:L6077-L6085](../../../INBOX/opm-libro.txt#L6077-L6085)
