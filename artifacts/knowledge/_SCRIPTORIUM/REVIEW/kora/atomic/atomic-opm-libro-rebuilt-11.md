---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-11
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
      n_propositions: 59
      segmented: true
      segment_role: segment
      segment_index: 11
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-11
---

# Atomic opm-libro-rebuilt - Segmento 11

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `59`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `11/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 7 Controlling the System’s Behavior / 7.3 Generalization-Specialization

- **P0540** · `constraint` · Let us now consider the text that follows: … The advisor then can conference in 911 dispatch or a public safety answering point (PSAP)… If there is no response from the occupants, the advisor can provide the emergency dispatcher with the crash information. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0541** · `constraint` · Three help entities are mentioned here: 911 Dispatch, Public Safety Answering Point, and Emergency Dispatcher. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0542** · `constraint` · From the text it is evident that the entity getting the crash information, Emergency Dispatcher, is a generalization of both 911 Dispatch and Public Safety Answering Point. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0543** · `constraint` · Conversely, 911 Dispatch and Public Safety Answering Point are both specializations of Emergency Dispatcher. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0544** · `fact` · Generalization-specialization is a powerful structural relation, which provides for abstracting any number of objects or process classes into superclasses. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0545** · `fact` · Syntactically, the generalization-specialization relation is a white triangle whose tip is linked to the generalizing link and whose base—to the specializing ones. In Fig. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0546** · `constraint` · 7.1, this link is shown connecting the general Emergency Dispatcher to the two specializations, 911 Dispatch and Public Safety Answering Point. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0547** · `fact` · The OPL phrase expressing this relation is “is a” (or “is an”). · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0548** · `constraint` · The following OPL sentences express this: 911 Dispatch is an Emergency Dispatcher. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0549** · `fact` · Public Safety Answering Point is an Emergency Dispatcher. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0550** · `constraint` · More succinctly, these two sentences can be expressed as one: 911 Dispatch and Public Safety Answering Point are Emergency Dispatchers. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0551** · `fact` · Semantically, the generalization-specialization link induces inheritance of features, states, and links from the generalizing superclass—the general to its subclasses—the specializations. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0552** · `fact` · For example, the single agent link from Emergency Dispatcher to Emergency Service Dispatching in Fig. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0553** · `constraint` · 7.1 is inherited to both 911 Dispatch and Public Safety Answering Point. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0554** · `constraint` · This is an example of the power of generalization and the inheritance it induces: instead of drawing six agent links from 911 Dispatch and Public Safety Answering Point to each one of the three bottom subprocesses in Fig. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)
- **P0555** · `constraint` · 7.1, only three are drawn, but they are interpreted as six. · [src:S01:L1736-L1760](../../../INBOX/opm-libro.txt#L1736-L1760)

## opm libro · Chapter 7 Controlling the System’s Behavior / 7.4 Zooming into Crash Severity Measuring

- **P0556** · `fact` · We left some of the system specification early in the text, so this part is not yet modeled. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0557** · `fact` · Let us back up and complete the model based on what we read: The … ACR system uses front and side sensors as well as the sensing capabilities of the Sensing and Diagnostic Module (SDM) itself. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0558** · `fact` · The accelerometer located within the SDM measures the crash severity. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0559** · `fact` · The focus here is on using sensors to measure the crash severity with objects that we have not yet included in our model. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0560** · `fact` · We already have modeled the process Crash Severity Measuring as the first subprocess of Automatic Crash Responding (see Fig. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0561** · `constraint` · 6.3) and the Sensing and Diagnostic Module as the instrument of this process. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0562** · `fact` · Therefore, to add details, such as the various sensors and their sensing processes, what we need to do now is zoom into Crash Severity Measuring. subprocesses: Sensing and Diagnosing, which are performed sequentially in the top-to-bottom order of their appearance in the in-zoomed process: First Sensing, then Diagnosing. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0563** · `fact` · Not surprisingly, the Sensing and Diagnostic Module is the instrument for both these subprocesses. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)
- **P0564** · `fact` · Therefore, the instrument link from Controlling the System's Behavior this object touches the outer Crash Severity Measuring process, acting like parentheses in algebra to denote that it applies to all the subprocesses within it. · [src:S01:L1764-L1782](../../../INBOX/opm-libro.txt#L1764-L1782)

## opm libro · Chapter 7 Controlling the System’s Behavior / 7.5 Participation Constraints

- **P0565** · `fact` · The instruments of Sensing are also front and side sensors, as well as a sensor inside the Sensing and Diagnostic Module, which we model as SDM Sensor. · [src:S01:L1784-L1790](../../../INBOX/opm-libro.txt#L1784-L1790)
- **P0566** · `fact` · Since the number of front and side sensors in not specified, and all we know is that there is more than one of each kind, we model Vehicle (which, in turn, is part of the ACR System) as having two to many objects of the class Front Sensor and two to many objects of the class Side Sensor. In the OPD in Fig. · [src:S01:L1784-L1790](../../../INBOX/opm-libro.txt#L1784-L1790)
- **P0567** · `constraint` · 7.2, this is expressed by the participation constraint 2..m appearing next to Front Sensor and Side Sensor. · [src:S01:L1784-L1790](../../../INBOX/opm-libro.txt#L1784-L1790)
- **P0568** · `constraint` · The corresponding OPL sentence is: Vehicle consists of Sensing and Diagnostic Module, 2 to many Front Sensors, and 2 to many Side Sensors. · [src:S01:L1784-L1790](../../../INBOX/opm-libro.txt#L1784-L1790)

## opm libro · Chapter 7 Controlling the System’s Behavior / 7.6 Logical Operators: OR Versus XOR

- **P0569** · `fact` · The Sensing process does not need all or even some of the sensors to generate a Shock Signal—one is enough. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0570** · `fact` · Yet, more than one sensor can generate the Shock Signal. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0571** · `fact` · This is the definition of the OR logical operator. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0572** · `fact` · OR is semantically more relaxed than its XOR counterpart, providing for one or more inputs or outputs rather than exactly one. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0573** · `fact` · XOR requires that exactly one of several alternatives be selected. For example, as Fig. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0574** · `constraint` · 7.2 shows, a XOR logical operation between three links of the same type from Diagnosing to the three states light, moderate, and severe, is expressed by the single dashed arc whose center is the common origin of these links. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0575** · `constraint` · While XOR is denoted by one dashed arc, OR is denoted by two dashed arcs, as shown by the three instrument links ending at the same point on the ellipse of the Sensing process in Fig. 7.2. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0576** · `fact` · The OPL sentence that expresses the OR operator is simply: Sensing requires SDM Sensor, Side Sensor, or Front Sensor. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0577** · `fact` · Comparing this to the XOR in the same OPD, we see that XOR is expressed by the reserved OPL phrase “exactly one of”, as in the following OPL sentence. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)
- **P0578** · `fact` · Diagnosing changes Crash Severity to exactly one of light, moderate, or severe. · [src:S01:L1792-L1805](../../../INBOX/opm-libro.txt#L1792-L1805)

## opm libro · Chapter 7 Controlling the System’s Behavior / 7.7 Crash Severity Measuring Refined

- **P0579** · `fact` · Reading the specification more carefully, we notice that we did not model the following sentence: The accelerometer located within the SDM measures the crash severity. Instead, in Fig. · [src:S01:L1807-L1814](../../../INBOX/opm-libro.txt#L1807-L1814)
- **P0580** · `constraint` · 7.2 we modeled the Accelerometer as the instrument for the Diagnosing subprocess. · [src:S01:L1807-L1814](../../../INBOX/opm-libro.txt#L1807-L1814)
- **P0581** · `fact` · From its name, we deduce that the function of the Accelerometer is the measure acceleration, so although this is not explicitly specified, in Fig. · [src:S01:L1807-L1814](../../../INBOX/opm-libro.txt#L1807-L1814)
- **P0582** · `constraint` · 7.3 we add the process Acceleration Measuring, with Accelerometer as its instrument and Acceleration Measuring as its resultee—the object that results from this process. · [src:S01:L1807-L1814](../../../INBOX/opm-libro.txt#L1807-L1814)

## opm libro · Chapter 7 Controlling the System’s Behavior / 7.8 Scope of Things: Signal as a Temporary Object

- **P0583** · `fact` · Inspecting the content of the in-zoomed Crash Severity Measuring in Fig. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0584** · `constraint` · 7.3, we realize that in addition to the two processes it also contains two objects, Shock Signal and Acceleration Signal. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0585** · `fact` · Indeed, this is also reflected in the following three corresponding OPL sentences. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0586** · `fact` · The first one is: Crash Severity Measuring zooms into Impact Sensing, Acceleration Measuring, and Diagnosing in that sequence, as well as Acceleration Signal and Shock Signal. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0587** · `fact` · This sentence lists the three subprocesses that get exposed in the in-zoomed Crash Severity Measuring: Impact Sensing, Acceleration Measuring, and Diagnosing. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0588** · `fact` · The reserved phrase “in that sequence” indicates that the top-to-bottom order in which the subprocesses are listed is their execution order. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0589** · `fact` · This list of processes is followed by the reserved OPL phrase “as well as”, followed by the list of two contained objects: Shock Signal and Acceleration Signal. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0590** · `fact` · The reserved OPL phrase “as well as” Controlling the System's Behavior separates between the list of processes and the list of objects in an in-zoomed process. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0591** · `fact` · The subprocesses are parts of the in-zoomed process while the objects are attributes of that in-zoomed process. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0592** · `fact` · For an in- zoomed object, the order would be reversed: The list of objects would come first, followed by “as well as”, followed by the list of processes. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0593** · `fact` · In this case, the internal objects are parts of the in-zoomed object, while the internal processes are operations of that in-zoomed object. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0594** · `fact` · The two informatical objects Shock Signal and Acceleration Signal are created inside the Crash Severity Measuring process by two of its subprocesses. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0595** · `fact` · They are then immediately consumed by the third subprocess, Diagnosing, and disappear. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0596** · `fact` · In general, objects inside an in-zoomed process are temporary: they exist and are recognized solely within the scope of that process. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0597** · `fact` · This would remain true even if we use two instrument links instead of the two consumption links. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
- **P0598** · `requirement` · If we wish to preserve these objects, they must reside outside the in-zoomed process. · [src:S01:L1816-L1839](../../../INBOX/opm-libro.txt#L1816-L1839)
