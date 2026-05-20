---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-78
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
      n_propositions: 47
      segmented: true
      segment_role: segment
      segment_index: 78
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-78
---

# Atomic opm-libro-rebuilt - Segmento 78

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `47`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `78/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.5.1 Combinatorial XOR

- **P4018** · `constraint` · Consider the following OPL sentence, which extends the model in Fig. 23.5. · [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)
- **P4019** · `fact` · Exactly one of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening. Safe can be closed or open. Safe can be closed or open. · [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)
- **P4020** · `constraint` · Exactly 2 of Safe Owner A, Safe Owner B, or Safe At least 2 of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening. Owner C handle Safe Opening. · [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)
- **P4021** · `constraint` · Safe Opening changes Safe from closed to open. The link fan size here is f = 3. · [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)
- **P4022** · `constraint` · If we want to model that exactly two safe owners are needed to open the safe, instead of “one” we write m = 2, effectively introducing a combinatorial number of possibilities, in this case “3 choose 2”, 3 2 3: Exactly 2 of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening. · [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)
- **P4023** · `constraint` · In the OPD, we add the number m outside and next to the XOR arc, as demonstrated by the number 2 recorded in the OPD on the left of Fig. 23.6. · [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)
- **P4024** · `fact` · In general, in combinatorial XOR we constrain the model to select exactly m of f links, we use the reserved phrase “exactly m of” where m < f , and the number of possibilities is . · [src:S01:L10333-L10354](../../../INBOX/opm-libro.txt#L10333-L10354)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.5.2 Combinatorial OR

- **P4025** · `fact` · Similar to the combinatorial XOR, we generalize the OR logic to combinatorial OR. · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)
- **P4026** · `constraint` · We do so by extending the logic from 1 to any number m (up to one less than f ) links by replacing “at least one of” in an OPL sentence by “ at least m of”, where m < f. · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)
- **P4027** · `fact` · Using again the OPL sentence above, which extends the model in Fig. · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)
- **P4028** · `constraint` · 23.5, where the link fan size is f = 3, instead of “one” we can write m = 2, effectively introducing a sum combinatorial number of possibilities. · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)
- **P4029** · `constraint` · At least 2 of Safe Owner A, Safe Owner B, or Safe Owner C handle Safe Opening. · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)
- **P4030** · `constraint` · In this case, the number of possibilities is 3 3 = 3+1=4. · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)
- **P4031** · `constraint` · In the OPD, we add the number m outside and next to the OR arc, as demonstrated by the number 2 recorded in the OPD on the right of Fig. 23.6. · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)
- **P4032** · `constraint` · In general, for constraining the model to select at least m of f links, we use the reserved phrase “at least m of” where m < f, and the number of possibilities is 1 . · [src:S01:L10356-L10369](../../../INBOX/opm-libro.txt#L10356-L10369)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.6 State-Specified XOR and OR Link Fans

- **P4033** · `fact` · Each one of the link fans described above has a corresponding state-specified version, where the source and destination may be specific object states or objects without a state specification. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4034** · `fact` · Combinations of state-specified and stateless links as destinations of a link fan may occur. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4035** · `constraint` · Figure 23.7 shows on the left a XOR state-specified instrument link fan and on the right an OR mixed result link fan where the links are state-specified for objects A and C but not for B. Exactly one of P, Q, or R requires s2 B. P yields at least one of s3 A, B, or s5 C. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4036** · `fact` · Two or more processes can have the same state as their source. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4037** · `fact` · For example, as the OPD on the right hand side of Fig. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4038** · `constraint` · 23.8 shows, either P1 or P2 (but not both) can consume B when it is at state s1: Either P1 or P2 consumes s1 B. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4039** · `fact` · If there are more than two processes, the OPL sentence becomes: Exactly one of P1, P2, or P3 consumes s1 B. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4040** · `fact` · A similar situation occurs with state change in the OPD on the right of Fig. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4041** · `constraint` · 23.8: Either P1 or P2 changes B from s1 to s2. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)
- **P4042** · `fact` · And for more than two processes: Exactly one of P1, P2, or P3 changes B from s1 to s2. · [src:S01:L10373-L10385](../../../INBOX/opm-libro.txt#L10373-L10385)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.6.1 Control-Modified Link Fans

- **P4043** · `fact` · Each one of the XOR link fans for consumption, result, effect, and enabling links and their state-specified versions has a corresponding control-modified link fan: an event link fan and a condition link fan. · [src:S01:L10388-L10394](../../../INBOX/opm-libro.txt#L10388-L10394)
- **P4044** · `constraint` · Table 23.7 presents the event and condition effect link fans, as representatives of the basic (non-state-specified) links version of the modified link fans. · [src:S01:L10388-L10394](../../../INBOX/opm-libro.txt#L10388-L10394)
- **P4045** · `constraint` · Table 23.7 Event and condition XOR effect link fans · [src:S01:L10388-L10394](../../../INBOX/opm-libro.txt#L10388-L10394)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.6.2 State-Specified Control-Modified Link Fans

- **P4046** · `fact` · Each one of the control-modified link fans, except the control-modified effect link fan, has a corresponding state-specified control-modified link fan. · [src:S01:L10396-L10401](../../../INBOX/opm-libro.txt#L10396-L10401)
- **P4047** · `constraint` · Since these state-specified versions are more complicated than their non-state-specified version, Table 23.8 presents the OPD and OPL of the state- specified cases, and below each such case—the OPL sentence for the corresponding stateless case. · [src:S01:L10396-L10401](../../../INBOX/opm-libro.txt#L10396-L10401)
- **P4048** · `constraint` · Each XOR link fan in Table 23.7 and in Table 23.8 has its OR counterpart (designated by a double dashed arc) with a corresponding OPL sentence in which the reserved phrase “at least” replaces “exactly”. · [src:S01:L10396-L10401](../../../INBOX/opm-libro.txt#L10396-L10401)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.7 Multiple Control Links Have OR Semantics

- **P4049** · `fact` · Event triggers a process independently of any other event link that might be linked to the same process. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4050** · `fact` · Therefore, two or more event links attached to a process have the logical OR semantics. Cancelling in both to coexist. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4051** · `constraint` · In fact, the likelihood that these two objects will be created in the system at the same point in time is practically zero. Therefore, the OPD on the right of Fig. 23.9 is correct. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4052** · `fact` · The one on the left is a case when the event that initiates the Cancelling is Bad Weather Forecast, but if that is the case, Artist Sickness is also required. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4053** · `fact` · The OPD in the middle is the complementary case: the event that initiates the Cancelling is Artist Sickness, but if that is the case, Bad Weather Forecast is also required. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4054** · `requirement` · In a similar way, if more than one condition link is the target of a process P with AND semantics, then all of the conditions must be true in order for P not to be skipped. Suppose the conditions are C1, C2, and C3. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4055** · `fact` · Suffice it that one condition is not fulfilled to cause P to be skipped: C1 or C2 or C3. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4056** · `fact` · Hence, while the AND semantics holds from the viewpoint of the requirement for process performance, from the skip semantics viewpoint, we are looking at OR semantics. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4057** · `constraint` · If we want to model that any non-empty subset of the conditions is sufficient, we need to use the OR link fan, as was done in the model in Fig. 23.5. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4058** · `constraint` · Table 23.8 State-specified and stateless XOR control-modified link fans Link fan kind Event control modifier Condition control modifier State-specified consumption link fan Exactly one of P, Q, or R occurs if B is s2, in S2 B initiates exactly one of P, Q, or R, which which case the occurring process consumes B, otherwise these processes are skipped. consumes the initiated process. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4059** · `fact` · The stateless case: The stateless case: B initiates exactly one of P, Q, or R, which Exactly one of P, Q, or R occurs if B exists, in which case the occurring process consumes B, consumes the initiated process. otherwise these processes are skipped. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4060** · `fact` · State-specified agent link fan S2 B initiates and handles exactly one of P, B handles exactly one of P, Q, or R if B is s2, Q, or R. otherwise these processes are skipped. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4061** · `fact` · The stateless case: The stateless case: B initiates and handles exactly one of P, Q, B handles exactly one of P, Q, or R if B exists, or R. otherwise these processes are skipped. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4062** · `fact` · State-specified instrument link fan S2 B initiates exactly one of P, Q, or R, which Exactly one of P, Q, or R requires that B is s2, requires s2 B. otherwise these processes are skipped. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4063** · `fact` · The stateless case: The stateless case: S2 B initiates exactly one of P, Q, or R, which Exactly one of P, Q, or R requires that B is s2, requires B. otherwise these processes are skipped. · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
- **P4064** · `fact` · Link Probabilities and Probabilistic Link Fans · [src:S01:L10403-L10464](../../../INBOX/opm-libro.txt#L10403-L10464)
