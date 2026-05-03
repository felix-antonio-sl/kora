---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-08
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
      n_propositions: 64
      segmented: true
      segment_role: segment
      segment_index: 8
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-08
---

# Atomic opm-libro-rebuilt - Segmento 08

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `64`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `08/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 5 Refinement Through In-Zooming

- **P0384** · `fact` · The deepest parts of the ocean are totally unknown to us… What goes on in those distant depths? · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0385** · `fact` · What creatures inhabit, or could inhabit, those regions twelve or fifteen miles beneath the surface of the water? It’s almost beyond conjecture. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0386** · `constraint` · Jules Verne, 20,000 Leagues under the Sea (1869) The previous chapters have exposed us to the basic concepts of OPM, yet we have barely scratched the surface of the system we are modeling. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0387** · `fact` · In this chapter, we specify more details about the system while revealing some more modeling concepts of OPM and how they can be utilized to represent our system in more detail. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0388** · `fact` · In order to examine the text that specifies the system we are modeling, we return our focus to information from the first sentences: “The accelerometer … measures the crash severity.” We combine this information with that from a sentence in the sequel: “Within seconds of a moderate-to-severe crash, the OnStar module will send a message …” The text skims over important information that we need to glean indirectly. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0389** · `fact` · We have already modeled the fact that the Vehicle is (at state) crashed. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0390** · `fact` · The phrase “moderate-to-severe crash” indicates that we need to model the crash severity, as this determines whether a message will be sent. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0391** · `fact` · The implicit assumption, which we model here, is that if the crash is light, it is unlikely to have caused an injury, so the system should not be activated. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)
- **P0392** · `fact` · Consequently, it makes sense to have Crash Severity Measuring as the next process to model. · [src:S01:L1325-L1342](../../../INBOX/opm-libro.txt#L1325-L1342)

## opm libro · Chapter 5 Refinement Through In-Zooming / 5.1 Measuring Crash Severity

- **P0393** · `fact` · We have already determined that Automatic Crash Responding is the function of our ACR System. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0394** · `fact` · This is the main process in the system diagram, SD—the top-level OPD. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0395** · `fact` · The Crash Severity Measuring process, which we are about to model, is clearly not at the same level of centrality as Automatic Crash Responding. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0396** · `fact` · Instead, it is a subprocess of Automatic Crash Responding. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0397** · `fact` · Moreover, as we understand the system now, it is going to be one (perhaps the first) of several subprocesses of the Automatic Crash Responding function. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0398** · `fact` · We could try modeling Crash Severity Measuring in a way similar to Crashing. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0399** · `fact` · However, this is probably not a good idea, for several reasons. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0400** · `fact` · Firstly, Crashing is an environmental process. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0401** · `fact` · Secondly, modeling Crash Severity Measuring at the same level as Automatic Crash Responding could be interpreted as meaning that these two processes are at the same level of importance, although they obviously are not. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)
- **P0402** · `fact` · Thirdly, our OPD is already starting to be somewhat crowded, and we would like to keep it simple and readily understandable. · [src:S01:L1344-L1355](../../../INBOX/opm-libro.txt#L1344-L1355)

## opm libro · Chapter 5 Refinement Through In-Zooming / 5.2 In-Zooming: Refining a Process in a New OPD

- **P0403** · `fact` · New-diagram in-zooming is an OPM modeling process that creates a new, descendant OPD, in which the details of the in-zoomed process—its subprocesses and objects associated with them—can be specified. · [src:S01:L1362-L1371](../../../INBOX/opm-libro.txt#L1362-L1371)
- **P0404** · `fact` · In our case, Automatic Crash Responding is in-zoomed, making it possible to refine this process by modeling its subprocesses and their interactions with lower-level objects in a new OPD at a level beneath the SD level. subprocess, Crash Severity Measuring, was drawn inside it near the top of the enclosing ellipse of the Automatic Crash Responding process. · [src:S01:L1362-L1371](../../../INBOX/opm-libro.txt#L1362-L1371)
- **P0405** · `fact` · The links that were attached to Automatic Crash Responding have migrated to be attached to Crash Severity Measuring. Measuring, nested inside it · [src:S01:L1362-L1371](../../../INBOX/opm-libro.txt#L1362-L1371)

## opm libro · Chapter 5 Refinement Through In-Zooming / 5.3 The OPD Tree

- **P0406** · `fact` · The OPD in Fig. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0407** · `constraint` · 5.1 does not replace the SD that we have been working on. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0408** · `fact` · Instead, it is a new OPD that comes in addition to and at a lower level than SD. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0409** · `fact` · SD is always the only top-level OPD—it is the root of the OPD tree. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0410** · `constraint` · Figure 5.2, which is a screenshot of OPCAT, shows both the top-level OPD, SD (in the left window), and the new one, called SD1—Automatic Crash Responding in-zoomed (to the right of SD). · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0411** · `constraint` · Figure 5.2 also shows at the OPD hierarchy pane on the left hand side the OPD process tree, which currently has just two OPDs: SD and SD1. zoomed (right). · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0412** · `fact` · The OPD hierarchy tree is presented on the left pane SD and SD1 are the two OPDs that currently constitute the OPD set; that is, the set of OPDs, organized as a process tree, which together specify the system. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0413** · `fact` · The OPD set keeps growing as additional OPDs are gradually constructed to increasingly refine the model and make it more concrete. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0414** · `fact` · The ability to add a descendant, subordinate OPD whenever the one currently under work reaches its congestion limits makes it possible to avoid over-cluttering any single OPD. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0415** · `fact` · The OPL sentence that links the OPL paragraph of SD to the OPL paragraph of SD1 is: Automatic Crash Responding from SD zooms in SD1 to Crash Severity Measuring. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0416** · `fact` · This kind of sentence indicates the hierarchical relationships between any two OPL paragraphs representing OPDs from adjacent hierarchy levels. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)
- **P0417** · `fact` · In our cases, it indicates that SD1 is a child of SD. · [src:S01:L1373-L1391](../../../INBOX/opm-libro.txt#L1373-L1391)

## opm libro · Chapter 5 Refinement Through In-Zooming / 5.4 The Model Fact Representation OPM Principle

- **P0418** · `fact` · The tagged structural link in SD from Vehicle Occupants Group to Vehicle, which in Fig. · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)
- **P0419** · `constraint` · 3.3 is labeled with the tag occupies, is not repeated in SD1 (Fig. 5.1). · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)
- **P0420** · `fact` · This omission is a presentation choice based on the following model fact representation OPM principle. · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)
- **P0421** · `fact` · The Model Fact Representation OPM Principle An OPM model fact needs to appear in at least one OPD in order for it to be represented in the model. · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)
- **P0422** · `fact` · This principle stipulates that it is enough for a model fact to appear only once in any OPD of the OPM model in order for it to be valid for the entire model. · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)
- **P0423** · `fact` · This principle does not preclude the possibility of representing any model fact any number of times in as many OPDs as the modeler wishes. · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)
- **P0424** · `fact` · However, although any number of entities can be included in any OPD, for the sake of clarity and avoiding clutter, it is often highly desirable to include only those elements that are necessary in order to grasp a certain aspect or view of the system. · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)
- **P0425** · `fact` · In our case, we have elected not to include the tagged structural link in SD1, as it does not add to comprehension of the point we want to make in this OPD. · [src:S01:L1393-L1407](../../../INBOX/opm-libro.txt#L1393-L1407)

## opm libro · Chapter 5 Refinement Through In-Zooming / 5.5 The Crash Severity Attribute and Its Measurement

- **P0426** · `fact` · The first Automatic Crash Responding subprocess, Crash Severity Measuring, determines Crash Severity. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0427** · `fact` · Crash Severity is a new object not yet modeled. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0428** · `fact` · Crash Severity is not just a new object; it describes Vehicle. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0429** · `fact` · In other words, it is an attribute of Vehicle. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0430** · `fact` · This attribute becomes relevant as a result of the Crashing process. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0431** · `fact` · An attribute is an object that characterizes a thing. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0432** · `fact` · In our case, Crash Severity is the attribute that characterizes the object Vehicle. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0433** · `constraint` · Figure 5.3 shows Crash Severity linked to Vehicle via an exhibition-characterization structural relation. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0434** · `fact` · The exhibition- characterization symbol is an equilateral black triangle inside a larger white one, like this: . · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0435** · `fact` · The tip of this triangle is linked to the exhibitor, which is the object Vehicle, and its base is linked to the object Crash Severity, which is an attribute of Vehicle. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0436** · `fact` · As an object in its own right, this attribute has four states. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0437** · `fact` · More precisely, since states of an attribute are called values, Crash Severity has four values: none, light, moderate, and severe. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0438** · `fact` · These are shown in Crash Severity can be none, light, moderate, or severe. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0439** · `fact` · As soon as Crashing occurs, the state of Vehicle changes from its initial intact state to its final crashed state. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0440** · `fact` · Upon entry of Vehicle to its crashed state, the state-specified instrument event link from the crashed state to Crash Severity Measuring initiates this subprocess. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0441** · `fact` · Crash Severity Measuring is the first (and currently the only) subprocess of the in-zoomed Automatic Crash Responding process. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0442** · `fact` · Crash Severity Measuring changes Crash Severity from its initial state, none, to exactly one of the three other states. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0443** · `constraint` · Severity to the Crash Severity Measuring process, and (2) the three alternative output links emanating from the same point on the ellipse of Crash Severity Measuring to each one of the three values, light, moderate, and severe, joined by a dashed arc. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0444** · `fact` · This dashed arc indicates the XOR (exclusive OR) logical operator among links. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0445** · `constraint` · In OPCAT it shows up automatically only when the XOR’ed links emerge from a common point, as is the case here, or arrive at a common point (as in Fig. 6.2). · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0446** · `fact` · The facts that these three output links originate from the same point and that a dashed arc connects them together symbolize the XOR logical operator between the links: Crash Severity Measuring determines that Crash Severity can have precisely one of its three possible output values: light, moderate, or severe, but not any two or all three at the same time. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
- **P0447** · `fact` · Indeed, the OPL sentence that describes this state change is: state, and light, moderate, and severe are the possible output states of the Crash Severity Measuring process Crash Severity Measuring changes Crash Severity from none to exactly one of light, moderate, or severe. · [src:S01:L1409-L1444](../../../INBOX/opm-libro.txt#L1409-L1444)
