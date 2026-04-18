---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-27
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
      n_propositions: 33
      segmented: true
      segment_role: segment
      segment_index: 27
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-27
---

# Atomic opm-libro-rebuilt - Segmento 27

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `33`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `27/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 11 Object-Process Language: The Text / 11.2.1 The Human-Oriented OPL Goal

- **P1406** · `fact` · The human-oriented OPL goal is to convert the set of OPDs comprising the OPM model into a natural language text that can be used to express and communicate analysis and design results among the various stakeholders involved in the system under construction. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1407** · `fact` · Users include domain experts and their executives on the customer side of the system under development, as well as architects and modelers on the supplier side of the same system. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1408** · `fact` · OPL enables involving the customer-side stakeholders, who are often non-technical, in the requirements elicitation and initial conceptual modeling of the system under development. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1409** · `fact` · Engaging these stakeholders as active participants helps streamline requirements, obtain stakeholders buy-in, and detect errors soon after their inadvertent introduction. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1410** · `fact` · Usually, these stakeholders do not have a command of programming languages, and it is not realistic to expect them to read diagrams in a conceptual modeling language, let alone program code. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1411** · `fact` · Being used to reading text (or viewing high-level slide presentations) rather than relating to diagrams, they (or their engineers or lawyers) are likely to prefer reading text over examining and interpreting OPDs. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1412** · `fact` · For them, OPL serves the purpose of verification and validation of the requirements, which are usually provided initially in text and then modeled in OPM. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1413** · `fact` · This requirement model helps identify gaps and inconsistencies so requirements can be improved and be acceptable to both sides—the customer and the contractor or developer. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1414** · `fact` · For the system architects and modelers on the supplier side, the bimodal representation of the OPM model is instrumental in getting immediate feedback on each graphic editing operation, enabling them to spot modeling errors as soon as they are made, before they propagate and start to cause damage whose magnitude increases exponentially with the error detection latency. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1415** · `fact` · Moreover, novice OPM users can experience steep learning curve by quickly gaining familiarity with the semantics of the OPM graphic modality by inspecting the text and corresponding graphic in tandem. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1416** · `fact` · Since textual documents are still the prominent way for communicating requirements and specifications of systems among parties, a formal textual modality that is generated “for free” and always matches the graphical specification is of great value. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1417** · `definition` · There are various other ways beside text to define and specify requirements including storyboards and mockups, which are gaining popularity in the software industry where people have decreasing patience neither for tiring text documents nor for complex conceptual models. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1418** · `fact` · The formal OPM model can serve as a basis for generating such popular means. · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)
- **P1419** · `constraint` · Indeed, work in this direction has started by creating an animated cartoon from the simulated animation of OPM models in OPCAT (Bolshchikov et al. 2015). · [src:S01:L3701-L3731](../../../INBOX/opm-libro.txt#L3701-L3731)

## opm libro · Chapter 11 Object-Process Language: The Text / 11.2.2 The Machine-Oriented OPL Goal

- **P1420** · `fact` · The machine-oriented OPL goal has to do with its formality. · [src:S01:L3733-L3741](../../../INBOX/opm-libro.txt#L3733-L3741)
- **P1421** · `fact` · OPL provides a firm basis for automatically generating the designed application—the infrastructure needed to continue the application development. · [src:S01:L3733-L3741](../../../INBOX/opm-libro.txt#L3733-L3741)
- **P1422** · `definition` · OPL is defined formally using a context-free grammar, so the OPL text file can serve as a basis for generating application artifacts that include executable code and database schema. · [src:S01:L3733-L3741](../../../INBOX/opm-libro.txt#L3733-L3741)
- **P1423** · `fact` · This approach enables round-trip engineering, in which changes in the analysis, design and specification are almost automatically reflected in the final application. · [src:S01:L3733-L3741](../../../INBOX/opm-libro.txt#L3733-L3741)
- **P1424** · `fact` · These traits make the combination of the graphic-oriented OPD and its equivalent text-based OPL counterpart an ideal infrastructure for systems specification. · [src:S01:L3733-L3741](../../../INBOX/opm-libro.txt#L3733-L3741)

## opm libro · Chapter 11 Object-Process Language: The Text / 11.3 The Graphics-Text Equivalence OPM Principle

- **P1425** · `fact` · The default OPL is English, but any natural language can serve as a basis for OPL. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1426** · `fact` · Since the OPD is based on graphics and iconic symbols, it can serve as a common platform for translation among OPLs in various natural languages. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1427** · `fact` · At each point in time during the modeling (when there are no unlinked things in the model), one can precisely reconstruct the OPD from its OPL paragraph and vice versa. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1428** · `fact` · This is expressed in the following graphics-text equivalence OPM principle. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1429** · `fact` · An OPL paragraph of an OPD is a collection of OPL sentences that express textually the same model facts that this OPD expresses graphically. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1430** · `fact` · The Graphics-Text Equivalence OPM Principle Any model fact expressed graphically in an OPD is also expressed textually in the corresponding OPL paragraph. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1431** · `fact` · The OPD set is complete graphical representation of the OPM model. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1432** · `fact` · It is the set of (hierarchically organized) OPDs that together specify all the model facts in the OPM model. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)
- **P1433** · `fact` · An OPL specification (OPL Spec) of an OPM model is the collection of all the unique OPL sentences that express textually all the model facts that the OPD set expresses graphically. · [src:S01:L3743-L3758](../../../INBOX/opm-libro.txt#L3743-L3758)

## opm libro · Chapter 11 Object-Process Language: The Text / 11.4 Metamodel of OPM Model Structure

- **P1434** · `constraint` · While a comprehensive metamodel of OPM appears in an annex of ISO 19450 (see Chap. 24), in Fig. · [src:S01:L3760-L3780](../../../INBOX/opm-libro.txt#L3760-L3780)
- **P1435** · `constraint` · 11.1 we provide a high-level model of the structure of an OPM model that puts the above definitions in context. A model of a model is a metamodel. Therefore, this OPM model is a metamodel. · [src:S01:L3760-L3780](../../../INBOX/opm-libro.txt#L3760-L3780)
- **P1436** · `fact` · Using OPM to specify the structure of an OPM model of a system, it depicts the conceptual aspects of OPM as parallel hierarchies of the graphic and textual OPM modalities and their correspondence to produce equivalent model expressions. · [src:S01:L3760-L3780](../../../INBOX/opm-libro.txt#L3760-L3780)
- **P1437** · `fact` · This OPD is the system diagram (SD, or SD0)—the top-level diagram (level zero) of the entire OPM metamodel. + can be in-zoomed to create specifies OPM Model System graphically specifies OPD Set textually specifies OPL Spec · [src:S01:L3760-L3780](../../../INBOX/opm-libro.txt#L3760-L3780)
- **P1438** · `constraint` · + graphically specifies OPL OPD textually specifies Paragraph OPD Construct graphically specifies + textually specifies OPL Sentence Link Set Punctuation Mark + 3.. Phrase Word + graphically specifies Reserved Phrase textually specifies + 2.. Link Thing Set Thing Name OPM Model specifies System. OPM Model consists of OPD Set and OPL Spec. OPL Spec consists of at least one OPL Paragraph. OPD Set consists of at least one OPD. OPD Set graphically specifies OPL Spec. OPL Spec textually specifies OPD Set. OPD consists of at least one OPD Construct. OPL Paragraph consists of at least one OPL Sentence. OPD graphically specifies OPL Paragraph. OPL Paragraph textually specifies OPD. OPD Construct graphically specifies OPL Sentence. OPL Sentence textually specifies OPD Construct. OPD Construct consists of Thing Set and Link Set. Thing Set consists of 2 to many Things. Link Set consists of at least one Link. Thing exhibits Name. OPL Sentence consists of 3 to many Phrases and at least one Punctuation Mark. Phrase consists of at least one Word. OPL Reserved Phrase and Name of Thing are Phrases. Link graphically specifies Reserved Phrase. Reserved Phrase textually specifies Link. Thing can be in-zoomed to create OPD The two objects at the top of the OPD in Fig. 11.1 are OPM Model and System, connected with a unidirectional tagged structural link from the former to the latter, yielding the OPL sentence OPM Model specifies System. Further, OPM Model consists of OPD Set and OPL Spec. These are the two complementary modalities—the graphical and the textual. From this point on, the OPD shows two parallel hierarchies—the graphical and the textual—where going down entails increased level of detail. The graphical hierarchy is OPD Set, OPD, OPD Construct, and (at the same level) Link Set and Thing Set. The textual hierarchy that is parallel to the graphical OPD Set and OPD is OPL Paragraph and OPL Sentence. An OPD and its corresponding OPL Paragraph are collections of model facts that a modeler places into the same diagram—the same model context. At the next refinement level in this hierarchy, an OPD Construct is the graphical counterpart of its corresponding textual OPL Sentence, and again, both express the same model fact. Then, Link, which is a graphic element, is paralleled by Reserved OPL Phrase, since the latter textually specifies the former, as in the reserved OPL phrase consists of, which is the textual counterpart of the aggregation-participation symbol, , and in affects, which is the textual counterpart of the effect link, . · [src:S01:L3781-L3851](../../../INBOX/opm-libro.txt#L3781-L3851)
