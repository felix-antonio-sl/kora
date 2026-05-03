---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-79
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
      n_propositions: 54
      segmented: true
      segment_role: segment
      segment_index: 79
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-79
---

# Atomic opm-libro-rebuilt - Segmento 79

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `54`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `79/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.8 A process P with a result link that yields a stateful object B with n states, s1 through sn, without specifying

- **P4065** · `fact` · a particular state, as in the OPD on the left of Fig. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4066** · `requirement` · 23.9, mean that the probability of generating B at any one particular state shall be 1/n. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4067** · `fact` · In this case, the single result link to the object replaces the result link fan to each of its states, so the OPD on the left of Fig. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4068** · `constraint` · 23.9 is equivalent to and, being simpler than the one on the right, is the preferred version. In the left OPD of Fig. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4069** · `constraint` · 23.10, the result link from P to B, which has 3 states, means that P with equal probability, Pr = 1/3, for being created at each one of the three states. will create B P yields s1 B with probability 0.32, s2 B with P yields A with probability 0.3, B with probability q, or sc1 C probability 0.24, or s3 B with probability 0.44. with probability 0.7–q. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4070** · `fact` · The analogous deterministic case: The analogous deterministic case: P yields exactly one of s1 B, s2 B, or s3 B. P yields exactly one of A, B, or sc1 C. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4071** · `fact` · Generally, probabilities of following a specific link in a link fan are not equal. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4072** · `fact` · Link probability is an optional attribute value assigned to a procedural link in a XOR diverging link fan that specifies the probability of following that particular link among the possible links in the fan link. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4073** · `constraint` · A probabilistic link fan is a link fan with a probability value assigned to each of its links, such that the sum of the probability values of all the links is exactly 1. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4074** · `constraint` · Graphically, in a probabilistic link fan, a probability value in the form , where is the link probability numeric value or a parameter, such that ∑ 1. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4075** · `fact` · This symbol, which appears along each one of the f links in the probabilistic link fan, denotes the probability that the system execution control mechanism will select that particular link and follow that path. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4076** · `fact` · The corresponding OPL sentence is the XOR diverging link fan OPL sentence without link probabilities omitting the phrase “exactly one of…” and adding instead the phrase “…with probability ” following each participating thing name with a probability annotation . OPL analogues. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4077** · `constraint` · In the OPD on the left, process P can create object B in three possible states, s1, s2, or s3, with corresponding probabilities 0.32, 0.24, and 0.44 (totaling 1), as indicated along each result link of the result link fan. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4078** · `constraint` · In the OPD on the right, P can create one of the objects A, B, or sc1 C, i.e., C at state sc1, with the probabilities 0.3, q, and 0.7–q (totaling 1), respectively. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4079** · `constraint` · For a process P with a result link that yields a stateful object B with states s1 through sn, and with initial state si, P creates B at state si with probability 1. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4080** · `requirement` · If B has m < n initial states, P shall create B at one of the initial states with probability 1/m. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4081** · `fact` · For a probabilistic result link fan, any one of the resultees may be an object without or with a specified state. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4082** · `fact` · For all the link fans comprising other procedural link kinds (including those with the event and condition control modifiers), where the targets of the links in the link fan are processes, the source may be an object or a specified state of an object. probabilistic result to one of three final states (middle), and probabilistic change from one state to another (right) The OPD on the left hand side of Fig. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4083** · `constraint` · 23.12 shows a probabilistic result link fan in which P yields one of the objects A or B, or C at state sc1, or D at state sd1 or sd2, each with its specified probabilities. The OPD in the middle of Fig. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4084** · `constraint` · 23.12 shows a probabilistic consumption link fan in which A is consumed, with specified probabilities, by one of the processes P or Q or R. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4085** · `requirement` · The OPD in the bottom expresses the same, with the additional fact that A must be at state s2. a state change from a state to one of two final states. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)
- **P4086** · `fact` · In the middle—probabilistic creation (result), and on the right—probabilistic change from one state to another. · [src:S01:L10466-L10523](../../../INBOX/opm-libro.txt#L10466-L10523)

## opm libro · Chapter 24 Overview of ISO 19450

- **P4087** · `constraint` · This book contains a comprehensive coverage of OPM that is compatible with ISO 19450 Publically Available Specification (PAS) titled “Automation systems and integration—Object-Process Methodology”, and in French: “Systèmes d’automatisation et intégration—Méthodologie du processus- objet”. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4088** · `constraint` · The ISO 19450 PAS has been adopted by the International Organization for Standardization (ISO) in December 2015 through the work of ISO Technical Committee 184/ Sub-committee 5 (TC184/SC5) after a six-year effort, mainly by Richard Martin, David Shorter, Alex Blekhman, and this author. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4089** · `constraint` · This book was prepared in parallel with the ISO 19450 PAS standard, so the two are almost completely aligned with each other. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4090** · `requirement` · Since the standard (formally PAS) must conform to the rules of ISO for standard authoring, it is structured differently and is not as elaborate as the book. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4091** · `constraint` · Rather, it is an orderly exposition of OPM that enables tool developers to use it, along with this book, as a solid basis for developing an ISO 19450- complaint software tool to support OPM-based conceptual modeling. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4092** · `constraint` · ISO standards like ISO 19450 PAS contain normative parts and often also one or more informative parts. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4093** · `requirement` · To be compliant with the standard, a normative part must be strictly followed, while an informative part is not mandatory. This book is a superset of ISO 19450 PAS. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4094** · `constraint` · About 90% of the material in this book is aligned with ISO 19450. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4095** · `constraint` · The rest can be considered as the equivalent of an addition to the informative part of the standard—it should be followed, but ISO 19450 in its current initial form does not mandate it. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)
- **P4096** · `constraint` · This closing chapter describes briefly the content of the ISO 19450 PAS, where each section is devoted to a summary of one or more sections of ISO 19450. · [src:S01:L10561-L10578](../../../INBOX/opm-libro.txt#L10561-L10578)

## opm libro · Chapter 24 Overview of ISO 19450 / 24.1 The ISO 19450 Introduction

- **P4097** · `constraint` · The first paragraph of the ISO 19450 document’s introduction (p.v) is the following. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4098** · `fact` · Object-Process Methodology (OPM) is a compact conceptual approach, language, and methodology for modelling and knowledge representation of automation systems. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4099** · `fact` · The application of OPM ranges from simple assemblies of elemental components to complex, multidisciplinary, dynamic systems. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4100** · `fact` · OPM is suitable for implementation and support by tools using information and computer technology. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4101** · `fact` · This document specifies both the language and methodology aspects of OPM in order to establish a common basis for system architects, designers, and OPM-compliant tool developers to model all kinds of systems. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4102** · `fact` · The introduction goes on to discuss the generality and industry- and business-wide applicability of OPM as a basis for model-based systems engineering: OPM notation supports the conceptual modelling of systems with formal syntax and semantics. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4103** · `fact` · This formality serves as the basis for model-based systems engineering in general, including systems architecting, engineering, development, life cycle support, communication, and evolution. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4104** · `fact` · Furthermore, the domain-independent nature of OPM opens system modelling to the entire scientific, commercial and industrial community for developing, investigating and analysing manufacturing and other industrial and business systems inside their specific application domains; thereby enabling companies to merge and provide for interoperability of different skills and competencies into a common intuitive yet formal framework. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4105** · `fact` · OPM facilitates a common view of the system under construction, test, integration, and daily maintenance, providing for working in a multidisciplinary environment. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4106** · `fact` · Moreover, using OPM, companies can improve their overall, big-picture view of the system’s functionality, flexibility in assignment of personnel to tasks, and managing exceptions and error recovery. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4107** · `fact` · System specification is extensible for any necessary detail, encompassing the functional, structural and behavioural aspects of a system. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4108** · `fact` · Toward the end of the Introduction section, there is reference to the drafting and authoring of technical documents in general and international standards in particular: One particular application of OPM is in the drafting and authoring of technical standards. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4109** · `definition` · OPM helps sketch the implementation of a standard and identify weaknesses in the standard to reduce, thereby significantly improving the quality of successive drafts. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4110** · `fact` · With OPM, even as the model-based text of a system expands to include more details, the underlying model keeps maintaining its high degree of formality and consistency. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4111** · `fact` · The initial motivation for making OPM an ISO standard is to use it as a basis for model-based standards—the contemplated new generation of ISO standards. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4112** · `constraint` · Indeed, in Dori et al. (2010) we proposed a combined, model-based structured graphical and textual meta-standard approach for specification, verification and validation of complex systems in general and ISO enterprise standards in particular. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4113** · `constraint` · This methodology, developed under the auspices of the ISO TC 184/SC 5 OPM Study Group, is designed to cope with current inconsistencies and incompleteness of technical documents (Blekhman et al., 2011). · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4114** · `fact` · To support authors of technical specifications while creating and editing model-based technical documents, we developed Model-Based Authoring of Specifications Environment (MBASE). · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4115** · `constraint` · In order to overcome the problem of the difficulty humans have with reading long OPL texts due to its mechanistic, repetitive nature, the MBASE framework includes Tesperanto (short for Technical Esperanto)—an evolution of OPL that is still automatically generated from the OPD but is much more amenable to being read by humans than OPL, even if the text is long (Blekhman and Dori 2013).This framework has been successfully applied in modeling communication in an operation room (Blekhman et al. 2015). · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4116** · `constraint` · Tesperanto can be considered as a textual version of The Imitation Game, better known as Turing Test—a test proposed in 1951 by Alan Turing, which was designed to settle the issue of machine intelligence. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4117** · `fact` · While in the original Turing Test a human judge has to decide whether she or he is interacting with a human or a computer, in the textual version of Turing Test, the judge has to decide whether a given text was written by a computer or by a human. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
- **P4118** · `fact` · Quite clearly, OPL text, while being comprised of syntactically correct English sentences will quickly be identified as written by a computer, it will be more difficult for a human to reveal this when presented with a Tesperanto text. · [src:S01:L10580-L10645](../../../INBOX/opm-libro.txt#L10580-L10645)
