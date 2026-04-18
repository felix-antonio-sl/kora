---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-77
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
      n_propositions: 57
      segmented: true
      segment_role: segment
      segment_index: 77
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-77
---

# Atomic opm-libro-rebuilt - Segmento 77

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `57`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `77/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.2 Logical NOT

- **P3961** · `fact` · “NOT” is a unary logical operator which simply reverses the state of any Boolean object (see Sect. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3962** · `constraint` · 7.1): A binary input of “yes” (positive, 1…) is converted to “no” (negative, 0…), and vice versa. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3963** · `fact` · There are several ways to implement NOT in OPM. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3964** · `constraint` · One is with the flip-flop mechanism, described in Sect. 19.5. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3965** · `fact` · Another way is to use states as constraints or conditions for process execution. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3966** · `fact` · If, for example, we want to model that a process P executes if and only if substance S is NOT present, we model the object S with two implicit states: existent and non-existent. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3967** · `constraint` · We link the non-existent state to P with an instrument link or an instrument condition link, so P can execute only if S is in its non-e, i.e., when it does not exist. non-existent states of molecules The mRNA Decay and Nuclear Import Process is the in-zoomed process in Fig. 23.4 (Somekh et al. 2014). · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3968** · `fact` · This OPD shows how the existent and non-existent states of molecules are used to implement “NOT”. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3969** · `fact` · For example, the existent state of the complex CCR4Not (no pun intended), depicted at the bottom right corner, is linked to Decaysome Import—the third subprocess from the top, so only if CCR4Not exists can this subprocess take place. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3970** · `fact` · However, in this case there are six other substances (such as Edc3) that can each enable the process, and they are linked with an OR logical operator (discussed below), so only lack of all the seven substances would prevent CCR4Not occurring. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3971** · `fact` · If the non-e (short for non-existent) state of CCR4Not would be linked with a condition link to Decaysome Import, that would mean (disregarding other links) that the absence of CCR4Not is the condition for the occurrence of Decaysome Import. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3972** · `constraint` · A link fan is a set of f (f ≥2) procedural links of the same kind that originate from a common point, or arrive at a common point, on the same object or process. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3973** · `fact` · The convergent end of a link fan is the end that is common to the f fan links. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)
- **P3974** · `fact` · The divergent end of a link fan is the end that is not common to the f fan links. · [src:S01:L10203-L10227](../../../INBOX/opm-libro.txt#L10203-L10227)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.3 Logical XOR and OR Link Fans

- **P3975** · `fact` · In order to express OR and XOR graphically, we use link fans. · [src:S01:L10229-L10239](../../../INBOX/opm-libro.txt#L10229-L10239)
- **P3976** · `fact` · The convergent end is attached to one thing, while the divergent end is attached to f things, where f is the size of the link fan set—the number of links in the fan. · [src:S01:L10229-L10239](../../../INBOX/opm-libro.txt#L10229-L10239)
- **P3977** · `fact` · A link can be a member of both a divergent fan on its source and a convergent fan on its target. · [src:S01:L10229-L10239](../../../INBOX/opm-libro.txt#L10229-L10239)
- **P3978** · `fact` · Since the links are procedural, one end is attached to object and the other to processes or vice versa. · [src:S01:L10229-L10239](../../../INBOX/opm-libro.txt#L10229-L10239)
- **P3979** · `fact` · Formally, the attribute value of the Perseverance of the Thing attached to the link fan’s convergent end is the opposite of the attribute value of the Perseverance of the f Things attached to the link fan’s divergent end. Thus, as the OPD in Fig. · [src:S01:L10229-L10239](../../../INBOX/opm-libro.txt#L10229-L10239)
- **P3980** · `constraint` · 23.5 shows, if the attribute value of the Perseverance of the thing attached to the link fan’s convergent end is dynamic (transient), then the thing is a Process. · [src:S01:L10229-L10239](../../../INBOX/opm-libro.txt#L10229-L10239)
- **P3981** · `fact` · In this case, the attribute value of the Perseverance of the f Things attached to the link fan's divergent end is static (persistent), implying that these f things are all Objects. · [src:S01:L10229-L10239](../../../INBOX/opm-libro.txt#L10229-L10239)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.3.1 The Logical XOR Operator

- **P3982** · `fact` · The semantics of the logical XOR operator is that exactly one of the f things connected to the divergent end of the link fan is transformed, enables, or occurs. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3983** · `fact` · If the divergent link end is attached to f objects, then exactly one object is transformed by the process at the convergent end of the link fan, or enables that process. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3984** · `fact` · If the divergent link end is attached to f processes, then exactly one process occurs. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3985** · `constraint` · This use of the XOR operator in OPM is in line with the definition of XOR in digital systems, but it may be different from some interpretations of the binary XOR operator with multiple inputs, where the output is 1 for an odd number of inputs and 0 for an even number of inputs. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3986** · `constraint` · Graphically, a single dashed arc across the f links of the link fan whose focal point is at the convergent end of contact denotes the XOR operator (see Fig. 23.5 left). · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3987** · `constraint` · The syntax of a link fan of f things with XOR semantics is different for f = 2 and for f > 2. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3988** · `constraint` · For f = 2, the reserved idiom (split reserved phrase) “either … or” is used. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3989** · `constraint` · Since this idiom in natural English is reserved for expressing selection of exactly one of two (but not many) items, for f > 2, the reserved phrase “exactly one of” is used. For example, since in Fig. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3990** · `constraint` · 23.5 (left) the link fan comprises 2 agent links, f = 2, so the OPL sentence is: Either Safe Owner A or Safe Owner B handle Safe Opening. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3991** · `constraint` · Suppose an agent link to a third safe owner, Safe Owner C, is added to the fan, making f = 3.
  - [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
  - [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P3992** · `fact` · The OPL sentence then becomes: Exactly one of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening. Safe can be closed or open. Safe can be closed or open. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3993** · `fact` · Either Safe Owner A or Safe Owner B handle Safe At least one of Safe Owner A and Safe Owner B handle Opening. Safe Opening. · [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
- **P3994** · `fact` · Safe Opening changes Safe from closed to open.
  - [src:S01:L10241-L10268](../../../INBOX/opm-libro.txt#L10241-L10268)
  - [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.3.2 The Logical OR Operator

- **P3995** · `fact` · The semantics of the logical OR operator is that at least one of the f things connected to the divergent end of the link fan is transformed, enables, or occurs. · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P3996** · `fact` · If the divergent link end is attached to f objects, then at least one object is transformed by the process at the convergent end of the link fan, or enables that process. · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P3997** · `fact` · If the divergent link end is attached to f processes, then at least one process occurs. · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P3998** · `fact` · This use of the OR operator in OPM is in line with the binary OR operator with two or more inputs. · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P3999** · `constraint` · Graphically, a double dashed arc across the f links of the link fan whose focal point is at the convergent end of contact denotes the OR operator (see Fig. 23.5 right). · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P4000** · `constraint` · The syntax of a link fan of f things with OR semantics is similar for f = 2 and f > 2. · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P4001** · `fact` · For both, the reserved phrase “At least one of” is used. For example, in Fig. · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P4002** · `constraint` · 23.5 (right), where the link fan comprises 2 agent links, the OPL sentence is: At least one of Safe Owner A or Safe Owner B handles Safe Opening. · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)
- **P4003** · `fact` · The OPL sentence then becomes: At least one of Safe Owner A, Safe Owner B, or Safe Owner C handles Safe Opening · [src:S01:L10271-L10284](../../../INBOX/opm-libro.txt#L10271-L10284)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.4 Diverging and Converging XOR and OR Links

- **P4004** · `fact` · A converging fan is a link fan whose links point to its convergent end. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4005** · `fact` · A diverging fan is a link fan whose links point to its divergent end. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4006** · `constraint` · Table 23.1 presents a summary of XOR and OR converging consumption and result links for f>2, showing in the top row that a converging consumption link fan is formed when the source things are objects and the destination thing is a process. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4007** · `fact` · In a converging result link fan, the source things are processes and the destination thing is an object. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4008** · `constraint` · Conversely, as Table 23.2 shows, when the source thing is an object and the destination things are processes, we get a diverging consumption link fan, while when the source thing is a process and the destination things are objects, a diverging result link fan is formed. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4009** · `constraint` · Table 23.1 Summary of XOR and OR converging fans for consumption and result links Table 23.2 Summary of XOR and OR diverging fans for consumption and result links XOR OR Diverging consumption link fan Exactly one of P, Q , or R consumes B. At least one of P, Q , or R consumes B. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4010** · `fact` · Diverging result link fan P yields exactly one of A, B, or C. P yields at least one of A, B, or C. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4011** · `fact` · An effect link is bidirectional, so the things linked by an effect link fan are both source and destination at the same time, voiding the definitions of convergent and divergent link fans. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4012** · `constraint` · Instead, as Table 23.3 shows, the distinction occurs with respect to multiple objects or multiple processes that a link fan connects. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4013** · `constraint` · Table 23.3 Summary of XOR and OR joint effect link fans Since an enabler is an object, both agent and instrument link fans can be diverging, with multiple processes as targets, as shown in Table 23.4, or converging, with multiple enablers as sources, as shown in Table 23.5. · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)
- **P4014** · `constraint` · Table 23.4 Diverging agent and instrument link fans Table 23.5 Converging agent and instrument link fans Invocation link fans can also be diverging or converging for both XOR and OR, as shown in Table 23.6, where the semantics of questionable combinations is specified. Table 23.6 Invocation link fans · [src:S01:L10288-L10326](../../../INBOX/opm-libro.txt#L10288-L10326)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.5 Combinatorial XOR and Combinatorial OR

- **P4015** · `fact` · The XOR and OR logic presented so far implies the selection of exactly one (for XOR) or at least one (for OR). · [src:S01:L10328-L10331](../../../INBOX/opm-libro.txt#L10328-L10331)
- **P4016** · `constraint` · In cases where the fan size f > 2, we can generalize the XOR and OR logic to combinatorial XOR and combinatorial OR logic. · [src:S01:L10328-L10331](../../../INBOX/opm-libro.txt#L10328-L10331)
- **P4017** · `constraint` · We extend the logic from 1 to any number m links (up to one less than f ) by replacing “one” in the OPL sentence by m, where m < f. · [src:S01:L10328-L10331](../../../INBOX/opm-libro.txt#L10328-L10331)
