---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-23
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
      n_propositions: 58
      segmented: true
      segment_role: segment
      segment_index: 23
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-23
---

# Atomic opm-libro-rebuilt - Segmento 23

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `58`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `23/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 10 Things: Objects and Processes / 10.4.5 The Involved Object Set

- **P1168** · `definition` · The involved object set is defined as follows. · [src:S01:L3202-L3207](../../../INBOX/opm-libro.txt#L3202-L3207)
- **P1169** · `fact` · The involved object set of process P, Inv(P), is the union of P’s preprocess object set and postprocess object set. · [src:S01:L3202-L3207](../../../INBOX/opm-libro.txt#L3202-L3207)
- **P1170** · `fact` · In set notation: Inv (P) = Pre (P) ∪ Post (P). In the examples in Fig. · [src:S01:L3202-L3207](../../../INBOX/opm-libro.txt#L3202-L3207)
- **P1171** · `constraint` · 10.1, Inv (Flight) = {Runway, Pilot, Airplane}, and Inv (Manufacturing) = {Operator, Machine, Model, Raw Material, Product}. · [src:S01:L3202-L3207](../../../INBOX/opm-libro.txt#L3202-L3207)

## opm libro · Chapter 10 Things: Objects and Processes / 10.5 The Procedural Link Uniqueness OPM Principle

- **P1172** · `requirement` · By the definition of process, a process transforms at least one object, so in a complete OPM model a process must be linked to at least one object, or any one of its states, via a transforming link, either directly or indirectly. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1173** · `fact` · A process and an object can be connected only via a procedural link, with the exception of exhibition-characterization, which is a structural link. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1174** · `fact` · Any procedural link, with the exception of invocation and exception links, connects a process with an object. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1175** · `fact` · An object has some role with respect to a process. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1176** · `fact` · It can be an agent, an instrument, or a transformee. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1177** · `fact` · Therefore, an object, or a state of an object, and a process cannot be connected by more than one procedural link. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1178** · `fact` · This is the rationale behind the following procedural link uniqueness OPM principle. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1179** · `fact` · The Procedural Link Uniqueness OPM Principle At any level of detail, an object and a process can be connected with at most one procedural link, which uniquely determines the role of the object with respect to the process. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1180** · `fact` · The reason for qualifying this principle to a given level of abstraction is that at different abstraction levels an object might be modeled differently. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1181** · `fact` · The role of an object can change with the level of detail. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1182** · `fact` · The procedural link uniqueness guides the modeler to retain the most semantically meaningful model fact at any given detail level. affectee of Eating is made possible via state expression. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1183** · `fact` · Right: When the states are suppressed, only the effect link remians For example, in the OPD on the left of Fig. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1184** · `constraint` · 10.4, when a Person is engaged in Eating, Person is both the agent, since Person handles Eating, and the affectee of this process, since Eating changes Person from hungry to satisfied. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1185** · `fact` · This is possible because the states hungry and satisfied of Person are expressed. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1186** · `requirement` · When the states are suppressed (on the right), we cannot have both agent and effect links between Person and Eating, so we must make a choice. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1187** · `definition` · As we define formally and explain in more detail in Sect. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1188** · `constraint` · 21.13, the choice of the link is based on the precedence of the procedural links. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1189** · `fact` · Since a transforming (in our case effect) link is semantically stronger than an enabling link (in our case agent), the effect link prevails. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1190** · `fact` · We can still use both links if we zoom into Eating, exposing its three subprocesses: Food Picking, Food Swallowing, and Food Digesting. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1191** · `fact` · Only the latter subprocess affects the Person, so now Person can be linked with an agent link to Food Picking and Food Swallowing, and with an effect link to Food Digesting. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1192** · `fact` · When zooming out of Eating and suppressing the states of Person, Person and Eating will again be linked by the effect link, since overall the state of Person changed, in line with the link precedence. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1193** · `fact` · As another example, Truck is obviously an instrument for Transporting. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1194** · `fact` · Transporting zooms into Loading, Moving, and Unloading. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1195** · `fact` · Loading changes Truck from unloaded to loaded, so Truck it is obviously affected. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1196** · `fact` · However, after Moving is over, Unloading changes Truck back from loaded to unloaded, so as a whole, inspecting Truck from the Transporting level, Truck is unaffected and hence can be modeled as an instrument of Transporting rather than its affectee. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1197** · `fact` · An object may have the role of an instrument in an abstract OPD and a transformee in another descendent, more detailed and concrete OPD. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1198** · `fact` · At the abstract OPD, the process does not appear to affect the object, because the object’s initial state is the same as its final state. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1199** · `fact` · Therefore, at the abstract OPD the object is an instrument, as indicated by an instrument link. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1200** · `fact` · However, at a descendent, more concrete OPD, that same process does appear to change the state of that object from the initial state and then back to the initial state. As a final example, in Fig. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1201** · `constraint` · 10.5, the left OPD (SD: Dish Washing System), a Dishwasher object is an instrument for the Dish Washing process, since no change in state of the Dishwasher is visible at that extent of abstraction. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1202** · `fact` · In the descendent OPD (SD1: Dish Washing in-zoomed), Dish Washing zooms into Loading (of a dirty Dish Set), Cleaning (which changes Dish Set from dirty to clean), and Unloading (of a clean Dish Set). · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1203** · `fact` · Loading changes the state of Dishwasher from empty to loaded, while Unloading changes it back from loaded to empty, so empty is both the initial and final state. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1204** · `fact` · While the Dishwasher is an instrument in SD, the System Diagram, at the descendent, more detailed OPD, the Dishwasher is an affectee—it becomes loaded and then empty again. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)
- **P1205** · `fact` · The only effect visible in the System Diagram is the effect on Dish Set. · [src:S01:L3209-L3266](../../../INBOX/opm-libro.txt#L3209-L3266)

## opm libro · Chapter 10 Things: Objects and Processes / 10.6 The Process Test

- **P1206** · `fact` · As argued, while a basic tenet of OPM is the distinction between objects and processes, it is sometimes difficult to tell an object from a process, especially if both are nouns. · [src:S01:L3268-L3277](../../../INBOX/opm-libro.txt#L3268-L3277)
- **P1207** · `fact` · The object-process distinction problem is stated simply as follows: Given a noun, how can we tell if it is an object or a process? · [src:S01:L3268-L3277](../../../INBOX/opm-libro.txt#L3268-L3277)
- **P1208** · `fact` · The process test, specified in this section, is a formal procedure for solving the object-process distinction problem. · [src:S01:L3268-L3277](../../../INBOX/opm-libro.txt#L3268-L3277)
- **P1209** · `fact` · It enables identifying nouns that are processes rather than objects, a prerequisite for successful system analysis and design. By default, a noun is an object. · [src:S01:L3268-L3277](../../../INBOX/opm-libro.txt#L3268-L3277)
- **P1210** · `requirement` · To be a process, the noun must meet each one of the following three process test criteria: (1) Object transformation, (2) time association, and (3) verb association. · [src:S01:L3268-L3277](../../../INBOX/opm-libro.txt#L3268-L3277)
- **P1211** · `fact` · Finally, if the outcome is still not clear, using common sense is of course the best option. · [src:S01:L3268-L3277](../../../INBOX/opm-libro.txt#L3268-L3277)

## opm libro · Chapter 10 Things: Objects and Processes / 10.6.1 The Object Transformation Criterion

- **P1212** · `requirement` · The object transformation process test criterion stipulates that a process must transform (consume, create, or change the state of) at least one of the objects in the involved object set. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1213** · `fact` · The object transformation criterion is satisfied if the noun in question transforms at least one of the objects in the involved object set. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1214** · `fact` · The membership of the transformee B of P is determined as follows. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1215** · `fact` · If P consumes B then B ∈ Pre (P): B is only in the preprocess object set of P. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1216** · `fact` · If P yields (creates) B, then B ∈ Post (P): B is only in the postprocess object set of P. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1217** · `fact` · If P affects (changes the state of) B, then B ∈ Inv (P): B is in the involved object set, i.e., in both the preprocess object set and the postprocess object set. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1218** · `fact` · Enablers (agents or instruments) are also members of Inv (P) as their presence is required throughout the entire duration of the process occurrence. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1219** · `fact` · Continuing the previous examples, the Flight process transforms Airplane (by changing its Location attribute from origin to destination). Hence, Airplane ∈ Inv (Flight). · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1220** · `fact` · Manufacturing transforms two objects: it consumes Raw Material and creates Product, hence Raw Material ∈ Pre (Manufacturing) while Product ∈ Post (Manufacturing). · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)
- **P1221** · `fact` · Finally, Machine ∈ Inv (Manufacturing) since Machine is an instrument for Manufacturing. · [src:S01:L3279-L3294](../../../INBOX/opm-libro.txt#L3279-L3294)

## opm libro · Chapter 10 Things: Objects and Processes / 10.6.2 The Time Association Criterion

- **P1222** · `fact` · The association with time process test criterion requires that the noun in question represent some happening, occurrence, action, procedure, routine, execution, operation, or activity that takes a positive amount of time along the timeline. · [src:S01:L3298-L3304](../../../INBOX/opm-libro.txt#L3298-L3304)
- **P1223** · `fact` · The time association criterion is satisfied if the noun in question can be thought of as happening through time. · [src:S01:L3298-L3304](../../../INBOX/opm-libro.txt#L3298-L3304)
- **P1224** · `fact` · Continuing our example, both Flight and Manufacturing start at a certain point in time and take a certain amount of time. · [src:S01:L3298-L3304](../../../INBOX/opm-libro.txt#L3298-L3304)
- **P1225** · `fact` · Both time and duration are very relevant features of these two nouns in question. · [src:S01:L3298-L3304](../../../INBOX/opm-libro.txt#L3298-L3304)
