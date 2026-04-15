---
_manifest:
  urn: urn:fxsl:kb:opm-dynamic-behavior-p03
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
    shard_index: 3
    shard_count: 3
    shard_root_urn: urn:fxsl:kb:opm-dynamic-behavior
---

# OPM Dynamic Behavior — Procedural Links, Control Flow, and Logical Operators - Parte 03

## Operational Semantics in In-Zoomed Contexts

Executing a process with an in-zoomed context recursively transfers control to the topmost subprocess(es) at the deepest level. Control returns to the in-zoomed process after its last subprocess completes.

### Involved Object Set Instance Transformations

- Each consumee instance ceases to exist at the beginning of the deepest subprocess that consumes it
- Each affectee exits input state at the beginning of the deepest subprocess that changes it; enters output state at the completion of that (or a subsequent) subprocess
- Each resultee is created at the completion of the deepest subprocess that yields it
- A stateful object in transition: has left input state but not yet arrived at output state (positive time duration)

### Split State-Specified Link Pairs

When an in-zoomed process changes an object from input state to output state, the input and output links may attach to different subprocesses:
- **Split input link**: from input state to earlier subprocess
- **Split output link**: from later subprocess to output state

No control-modified versions of split links (would distort effect semantics if one subprocess is skipped).
