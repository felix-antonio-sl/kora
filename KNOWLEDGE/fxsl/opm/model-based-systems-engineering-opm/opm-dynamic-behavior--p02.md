---
_manifest:
  urn: urn:fxsl:kb:opm-dynamic-behavior-p02
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
    shard_index: 2
    shard_count: 3
    shard_root_urn: urn:fxsl:kb:opm-dynamic-behavior
---

# OPM Dynamic Behavior — Procedural Links, Control Flow, and Logical Operators - Parte 02

## Event Links

An **event link** is a procedural link with the control modifier `e`, indicating process initiation upon event occurrence. The event triggers precondition evaluation; if satisfied, the process becomes active; if not, process initiation does not occur until another event activates it.

### Event Link Taxonomy

#### Enabling Event Links

| Name | Semantics | OPL pattern |
|------|-----------|-------------|
| Agent event link | Human both initiates and enables the process | `[Agent] initiates and handles [Process]` |
| Instrument event link | Object initiates process as instrument (not transformed, must persist) | `[Instrument] initiates [Process], which requires [Instrument]` |

#### Transforming Event Links

| Name | Semantics | OPL pattern |
|------|-----------|-------------|
| Consumption event link | Object initiates process, which consumes it | `[Consumee] initiates [Process], which consumes [Consumee]` |
| Effect event link | Object initiates process, which affects it | `[Affectee] initiates [Process], which affects [Affectee]` |

All four basic event links have **state-specified** counterparts: event originates from a specific state of the object, adding state-entry as the triggering event.

### Event Link Migration

If an event link is attached to an in-zoomed process P, it migrates automatically to the first (topmost) subprocess. Attaching an event link to a non-first subprocess is dangerous: it skips predecessor subprocesses, potentially leaving preconditions unsatisfied.

## Condition Links

A **condition link** is a procedural link with the control modifier `c`, providing skip-bypass semantics: if the source object/state does not exist, the destination process is skipped rather than waited for.

### Condition vs Instrument Link Semantics

| Aspect | Instrument link | Condition link |
|--------|----------------|----------------|
| Object absent | Process waits (system halts) | Process skipped (execution advances) |
| Analogy | `wait until...` | `if...then` |
| OPL phrase | `requires` | `occurs if` |

### The Skip Semantics Precedence OPM Principle

> Skip semantics takes precedence over wait semantics.

If a preprocess object set contains both condition links and non-condition links, and any condition-linked object/state is absent, the process is skipped regardless of non-condition link status. Condition evaluation occurs first.

### Condition Transforming Links

| Name | Semantics | OPL pattern |
|------|-----------|-------------|
| Condition consumption link | If consumee exists, process performs and consumes it; else skip | `Process occurs if Object exists, in which case Process consumes Object, otherwise Process is skipped` |
| Condition effect link | If affectee exists, process performs and affects it; else skip | `Process occurs if Object exists, in which case Process affects Object, otherwise Process is skipped` |

### Condition Enabling Links

| Name | Semantics | OPL pattern |
|------|-----------|-------------|
| Condition agent link | If agent exists, process performs with agent handling; else skip | `[Agent] handles [Process] if [Agent] exists, otherwise [Process] is skipped` |
| Condition instrument link | If instrument exists, process performs; else skip | `[Process] requires [Instrument] if [Instrument] exists, otherwise [Process] is skipped` |

### Condition State-Specified Links

All four condition transforming links and both condition enabling links have state-specified counterparts. Semantics: process performs if object is in the specified state; otherwise skipped.

Key variants for condition state-specified transforming links:
- **Condition state-specified consumption** — consume if object at specified state
- **Condition input-output-specified effect** — change from input to output state if object at input state
- **Condition input-specified effect** — change from input state to any state
- **Condition output-specified effect** — change to output state if object exists

## Invocation Links

**Process invocation**: a process-to-process event. When the source process completes successfully, it immediately initiates the destination process.

| Type | Semantics | Symbol |
|------|-----------|--------|
| Common invocation link | Source process completion initiates destination process | Lightning/jagged line with closed arrowhead |
| Self-invocation link | Process invokes itself upon completion (loop) | Pair of invocation links forming a loop |

Invocation semantics implies creation of an implicit interim object by the source process, immediately consumed by the destination process. A Waiting process with time constraints can be inserted between consecutive invocations.

### Implicit Invocation Links

An **implicit invocation link** is not visible graphically but implied by vertical layout within an in-zoomed process context. Three kinds:

1. **Process to first subprocess(es)** — control transfers to topmost subprocess(es) upon entering in-zoomed context
2. **Subprocess to next subprocess(es)** — completion of source subprocess initiates subsequent one(s)
3. **Last subprocess to enclosing process** — control returns to in-zoomed process upon last subprocess completion

When two or more subprocesses have topmost ellipse points at the same height, they start in parallel (implicit parallel invocation link set). Synchronization: the last one to finish initiates the next subprocess(es).

### Link Distribution Across In-Zoomed Context

A procedural link attached to the contour of an in-zoomed process distributes to all subprocesses (algebraic parenthesis semantics). Restrictions:
- **Agent and instrument links**: valid distribution (enabler present throughout)
- **Consumption and result links**: invalid distribution (cannot consume/create same instance multiple times). Must attach to specific subprocesses.
- **Effect links (in-out-specified)**: may split — input link to one subprocess, output link to another (**split in-out-specified link pair**)

## Exception Links

Exception links model temporal anomalies in process execution. Two kinds:

| Link | Trigger | Connects | OPL pattern |
|------|---------|----------|-------------|
| **Overtime exception link** | Process duration exceeds Maximal Duration | Maximal-timed process -> overtime handling process | `[Handler] occurs if duration of [Process] exceeds [max] [unit]` |
| **Undertime exception link** | Process duration falls below Minimal Duration | Minimal-timed process -> undertime handling process | `[Handler] occurs if duration of [Process] falls short of [min] [unit]` |

### Process Time Duration

Optional Duration property with specializations: Minimal Duration, Expected Duration, Maximal Duration. Units per ISO 80000-3 (ms, sec, min, hr, dy, wk, mo, yr). Duration Distribution specifies probability distribution function; at runtime, duration sampled per-instance.

Overtime control modifier: single slanted bar crossing the link. Undertime control modifier: pair of parallel slanted bars. A source process may have both overtime and undertime links to separate exception-handling processes.

Exception links can model execution exceptions: if a process with minimal duration is skipped (duration = 0), the undertime exception handler activates.

## Transformation Rate

**Transformation rate** is a property of a transforming link specifying the rate of transformation.

| Rate type | Definition |
|-----------|-----------|
| Consumption rate | Rate of consumption of consumee B by process P |
| Yield rate | Rate of creation of resultee B by process P |
| Effect rate | Rate of state change of affectee B by process P |
| State change rate | Rate of changing affectee B from input state `bi` to output state `bo` |

Enables modeling continuous or discrete multi-unit transformations over time.

## Computing with OPM

OPM models support numeric calculations. Atomic processes: Adding, Subtracting, Multiplying, Dividing. Compound processes (Averaging, etc.) compose these. Non-commutative operations (Dividing) require explicit role designation (Dividend, Divisor, Quotient). Formulae can be embedded in process names (e.g., `Residue Computing (residue=il-u)`).

## Sets and Iterations

A **set** is a collection of object instances of the same class. Iteration template: when a process is attached with two procedural links of the same kind — one to a set of n members and one to a member of the set — the semantics is iteration (n repetitions of the process).

Iteration combines with any subset of procedural links. Applicable to both physical and informatical objects. Provides a formal shorthand for loops usable in automated code generation.

## Logical Operators

Four logical operators govern link fans: AND, OR, XOR, NOT.

### Link Fans

A **link fan** is a set of f >= 2 procedural links of the same kind originating from or arriving at a common point on the same object or process.

| Term | Definition |
|------|-----------|
| Convergent end | End common to all f fan links |
| Divergent end | End not common; attached to f distinct things |
| Converging fan | Links point toward convergent end |
| Diverging fan | Links point away from convergent end |

### Logical AND

Default operator. Two or more procedural links of the same kind arriving at/originating from different points on the process ellipse. Links do not touch each other on the process contour. OPL reserved phrase: `and`.

All linked objects/processes participate simultaneously.

### Logical XOR (Exclusive OR)

Semantics: exactly one of f things at the divergent end is transformed/enables/occurs.

Graphical symbol: single dashed arc across links with focal point at convergent end. OPL phrases:
- f = 2: `either...or`
- f > 2: `exactly one of`

### Logical OR (Inclusive OR)

Semantics: at least one of f things at the divergent end is transformed/enables/occurs.

Graphical symbol: double dashed arc across links with focal point at convergent end. OPL phrase: `at least one of` (for all f).

### Logical NOT

Unary operator reversing Boolean state. Implementation methods:
1. Flip-flop mechanism
2. Using `existent`/`non-existent` states: link the `non-existent` state to a process with instrument/condition link — process executes only if object is absent

### XOR and OR Fan Directions

| Fan type | Source things | Destination thing |
|----------|-------------- |-------------------|
| Converging consumption fan | f objects | 1 process |
| Converging result fan | f processes | 1 object |
| Diverging consumption fan | 1 object | f processes |
| Diverging result fan | 1 process | f objects |
| Effect link fan (bidirectional) | Distinction by multiple objects vs multiple processes (not convergent/divergent) |
| Enabling link fan (agent/instrument) | Converging: multiple enablers -> 1 process; Diverging: 1 enabler -> multiple processes |
| Invocation link fan | Converging or diverging for both XOR and OR |

### Combinatorial XOR and OR

Generalization for f > 2: select exactly m (combinatorial XOR) or at least m (combinatorial OR) of f links, where m < f.

- **Combinatorial XOR**: `exactly m of` — number of possibilities: C(f, m)
- **Combinatorial OR**: `at least m of` — number of possibilities: sum of C(f, k) for k = m to f

Graphical: number m appears next to the XOR/OR arc.

### State-Specified Link Fans

Every link fan has a state-specified version where may be specific object states. Mixed fans (some links state-specified, others not) are valid.

### Control-Modified Link Fans

Every XOR/OR fan for consumption, result, effect, and enabling links has event and condition variants. State-specified control-modified fans also exist. Each XOR fan has an OR counterpart obtained by replacing `exactly` with `at least` in OPL.

## Multiple Control Links: OR Semantics

Multiple event links attached to the same process have OR semantics — any single event suffices to trigger the process. Multiple condition links attached to the same process have AND semantics for process execution (all must be satisfied), but OR semantics for skipping (any single unsatisfied condition causes skip).

## Probabilities and Timeout

### Link Probabilities

**Link probability**: optional attribute value on a procedural link within a XOR diverging fan, specifying probability of following that path. For a **probabilistic link fan**, the sum of all link probabilities equals 1.

Default probability (no fan, stateful resultee with n states): each state has probability 1/n. If resultee has initial state `si`, P creates B at `si` with probability 1; if m initial states, probability 1/m each.

OPL syntax: replaces `exactly one of` with per-link `with probability p` annotations.

Probabilities apply to all procedural link kinds including state-specified and control-modified fans.

### Process Duration as Timeout

Process Duration (Minimal, Expected, Maximal) combined with exception links provides timeout modeling. Duration Distribution enables stochastic simulation.
