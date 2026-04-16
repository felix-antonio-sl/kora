---
name: steinberg-composition-router
description: Route requests to the right local composition skill. Use when the task could fit multiple steinberg-* skills, when you need to choose between dispatch, architecture review, loop closure, repo shaping, foreman coordination, or taste review, or when the agent risks using the wrong lens for the problem.
---

# Steinberg Composition Router

Choose the right lens before expanding effort.

## Purpose

Prevent skill overlap, drift, and wrong framing.

## Routing order

1. Identify the actual bottleneck.
2. Choose the most specific composition skill.
3. Use one primary skill first.
4. Pull a second skill only if the problem genuinely crosses lenses.
5. Avoid loading multiple skills just because they all sound relevant.

## Primary routes

### `steinberg-dispatch`
Use when the problem is:
- ambiguous but actionable
- about topology, sequencing, or delegation
- at risk of ceremony or tool theater

### `steinberg-architecture-review`
Use when the problem is:
- boundaries
- dependencies
- schema direction
- runtime split
- naming with structural impact
- overall system shape

### `brutal-loop-closure`
Use when the problem is:
- proving a change is actually done
- deciding validation depth
- checking repo state and remaining risk after changes

### `steinberg-repo-shaping`
Use when the problem is:
- repo navigability
- context cost
- operational surfaces
- docs locality
- file/package structure

### `steinberg-agent-foreman`
Use when the problem is:
- multi-agent coordination
- slice framing
- overlap prevention
- worker supervision and integration

### `steinberg-taste-review`
Use when the problem is:
- UX feel
- naming feel
- polish
- friction
- product coherence despite technical correctness

## Cross-skill pairs

Use pairs only when the split is real:

- dispatch + foreman
- architecture review + repo shaping
- architecture review + taste review
- dispatch + brutal loop closure
- foreman + brutal loop closure

## Avoid

- starting with loop closure before the change exists
- doing architecture review when the real issue is repo operability
- using taste review to avoid naming a structural architecture problem
- using dispatch forever instead of moving to execution

## When to read more

For a compact matrix, read `references/matrix.md`.
