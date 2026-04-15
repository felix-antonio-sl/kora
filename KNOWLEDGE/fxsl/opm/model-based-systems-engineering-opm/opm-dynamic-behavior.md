---
_manifest:
  urn: urn:fxsl:kb:opm-dynamic-behavior
  provenance:
    created_by: kora/curator
    created_at: '2026-03-25'
    source: OPERATIONS/source/fxsl/opm-methodology/opm-libro-dynamic-behavior.md
version: 1.0.0
status: published
tags:
- opm
- dynamic-aspect
- procedural-links
- transforming-links
- enabling-links
- control-flow
- eca
- logical-operators
- event-links
- condition-links
lang: en
extensions:
  kora:
    family: textbook
    depends_on:
    - urn:fxsl:kb:opm-iso-19450
    - urn:fxsl:kb:opm-mbse-foundations
    book_source: Dori, D. (2015). Model-Based Systems Engineering with OPM and SysML.
      Springer.
    chapters:
    - 3
    - 6
    - 7
    - 13
    - 22
    - 23
    shard_index: 1
    shard_count: 3
    shard_root_urn: urn:fxsl:kb:opm-dynamic-behavior
relations:
  cites:
  - urn:fxsl:kb:opm-iso-19450
  - urn:fxsl:kb:opm-mbse-foundations
---


# OPM Dynamic Behavior — Procedural Links, Control Flow, and Logical Operators


## Resumen

OPM models system dynamics through procedural links connecting processes with objects/states. Two families: **transforming links** (consumption, result, effect) create/destroy/change objects; **enabling links** (agent, instrument) require object presence without transformation. Control flow follows the **Event-Condition-Action (ECA)** paradigm: event triggers precondition evaluation; satisfied condition activates the process; unsatisfied condition either waits (non-control link) or skips (condition link). **Event links** (modifier `e`) initiate processes; **condition links** (modifier `c`) enable skip-bypass. **Exception links** (overtime, undertime) handle temporal anomalies. **Invocation links** chain process-to-process activation. **Logical operators** (AND, OR, XOR, NOT) govern link fans for branching/merging. Probabilities annotate XOR diverging fans. Sets and iteration model repetitive transformations. For core ontology definitions (object, process, state, transformee, enabler), see [OPM MBSE Foundations](urn:fxsl:kb:opm-mbse-foundations). For ISO formal glossary, see [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## Procedural vs Structural Links

A **procedural link** connects a process to an object (or state), specifying a dynamic aspect. A **structural link** connects object-to-object or process-to-process, specifying a static aspect.

Procedural links subdivide into:
- **Transforming links** — object undergoes generation, consumption, or state change
- **Enabling links** — object enables process without being transformed

Structural links include aggregation-participation (whole-part), generalization-specialization, and tagged structural links. Both link types coexist in the same OPD, integrating structure and behavior.

> Cross-ref: full structural link taxonomy in [OPM ISO 19450 Glossary](urn:fxsl:kb:opm-iso-19450). Transformee/enabler role definitions in [OPM MBSE Foundations](urn:fxsl:kb:opm-mbse-foundations).

## Transforming Links

A **transforming link** connects a process with a transformee (consumee, affectee, or resultee). Three specializations:

| Link | Direction | Symbol | OPL phrase | Semantics |
|------|-----------|--------|------------|-----------|
| Consumption link | consumee -> process | unidirectional arrow | `consumes` | Object ceases to exist upon process activation |
| Result link | process -> resultee | unidirectional arrow | `yields` | Object created upon process termination |
| Effect link | process <-> affectee | bidirectional arrow | `affects` / `changes...from...to` | Object state changes; identity preserved |

### Consumption and Result Timing

- **Consumption**: immediate upon process activation. Consumee existence is a precondition for process start. If consumee does not exist, process waits.
- **Result**: resultee created only upon process termination. During process execution, neither consumee (already consumed) nor resultee (not yet created) exists.
- **Effect**: affectee exits input state at subprocess start; enters output state at subprocess completion. Between these points, object is "in transition."

### Effect Link Evolution

The effect link is an abstraction of the input-output link pair. When states are expressed, an input link (state -> process) and output link (process -> state) replace the single bidirectional arrow. State suppression collapses the pair back to a single effect link. This enables the comprehensiveness-clarity tradeoff.

## Enabling Links

An **enabler** must exist and remain available throughout process duration; it is unaffected by process completion. Two specializations:

| Link | Enabler type | Symbol | OPL phrase |
|------|-------------|--------|------------|
| Agent link | Human (individual/group) | black lollipop (filled circle) | `[Agent] handles [Process]` |
| Instrument link | Non-human (physical/informatical) | white lollipop (hollow circle) | `[Process] requires [Instrument]` |

Agent designation implies human-in-the-loop, signaling interface design requirements. Instruments include machines, tools, software, algorithms, documents.

### Link Precedence

Transforming links are semantically stronger than enabling links. Per the Procedural Link Uniqueness OPM Principle, if an object is both agent/instrument and affectee of the same process, the transforming link (effect) takes precedence. Optional stick-figure annotation retains human identity when effect link replaces agent link.

### Enabler vs Affectee

An object can hold different roles for different processes: enabler for one process, affectee for another. An enabler may undergo internal state changes during the process (e.g., Oven: off -> on -> off during Baking), but returns to its original state upon process completion.

## Preprocess and Postprocess Object Sets

| Set | Members | Membership rule |
|-----|---------|-----------------|
| Preprocess object set | Consumees, affectees, enablers (agents + instruments) | Must exist (possibly in specified states) before process start |
| Postprocess object set | Resultees, affectees, enablers | Exist after process completion |
| Involved object set | Pre(P) union Post(P) | All objects participating in process P |

Overlap: enablers and affectees belong to both Pre(P) and Post(P). Consumees belong only to Pre(P) (destroyed). Resultees belong only to Post(P) (created). In a complete OPM model, each process must link with at least one transformee.

> Cross-ref: formal Pre(P)/Post(P)/Inv(P) definitions in [OPM MBSE Foundations](urn:fxsl:kb:opm-mbse-foundations).

## State-Specified Procedural Links

A **state-specified procedural link** connects a process to a specific state of an object rather than to the object itself. Every procedural link has a state-specified version.

### State-Specified Enabling Links

| Link | Semantics | OPL example |
|------|-----------|-------------|
| State-specified agent link | Agent must be at state `s` throughout process duration | `Sober Pilot handles Flying` |
| State-specified instrument link | Instrument must be at state `s` throughout process duration | `Moving requires serviced Moving Truck` |

Difference from non-state-specified: regular instrument link imposes no state constraint; state-specified version requires a particular state for enablement.

### State-Specified Transforming Links

| Link | Semantics | OPL example |
|------|-----------|-------------|
| State-specified consumption link | Consumee must be at input state `si` to be consumed | `Machining consumes cut Raw Metal Bar` |
| State-specified result link | Resultee created at output state `s` | `Machining yields pre-tested Part` |
| In-out-specified effect link pair | Input link from `si`, output link to `so` | `Purifying changes Copper from raw to pure` |
| Input-specified effect link pair | Input link from `si`, output link to object (any state) | `Testing changes Sample from awaiting test` |
| Output-specified effect link pair | Input link from object, output link to `so` | `Cleaning & Painting changes Engine Hood to painted` |

### Value-Specified Procedural Links

A **value-specified procedural link** connects a process to values of an attribute (not states of a non-attribute object).

| Link | Semantics |
|------|-----------|
| Value setting link | Unidirectional; sets attribute value regardless of prior value |
| Value effect link | Bidirectional; changes attribute from unspecified value to another |
| In-out-specified value effect link pair | Changes attribute from specified input value to specified output value |

## Timeline OPM Principle

> The timeline within an in-zoomed process is directed by default from the top of the in-zoomed process ellipse to its bottom.

Subprocess execution order determined by the height of each subprocess ellipse's topmost point (higher = earlier). If two or more subprocess ellipses have topmost points at the same height (within tolerance), they start simultaneously — this models process synchronization.

Deviations from top-to-bottom timeline: internal events, loops, explicit invocation links.

## Scenarios and Threads of Execution

A **scenario** (thread of execution) is a specific path through the system's process hierarchy, traced by following the state of each object. At each branching point (Boolean object, condition links, XOR fan), exactly one path materializes. The complete set of scenarios constitutes the system's behavioral repertoire.

## Boolean Objects for Branching

A **Boolean object** is an informatical dual-state decision object generated by a decision process. States form a Boolean pair (yes/no, true/false, pass/fail, etc.). Each state connects via condition links to alternative subsequent processes, implementing if-then-else control flow.

Predefined Boolean pairs: true/false, positive/negative, on/off, approved/denied, passed/failed, >=x / <x.

General case: any object with n states functions as a case statement — each state can serve as condition or instrument source for a subsequent process.

## Event-Condition-Action (ECA) Control Mechanism

OPM process activation follows the ECA paradigm: "On event, if condition, then action."

| ECA component | OPM interpretation |
|---------------|-------------------|
| **Event** | Point in time: object creation, object appearance, or entrance to a state. Triggers precondition evaluation. Events are instantaneous and lost after occurrence. |
| **Condition** | Logical test on the preprocess object set. If satisfied, process activates. If not, process waits for next event (non-condition link) or is skipped (condition link). |
| **Action** | Process activation. Upon completion, transforms one or more objects (postprocess object set). |

Flow of execution control: successive ECA sequences beginning with external event initiating system function and ending with successful completion or abnormal termination.
