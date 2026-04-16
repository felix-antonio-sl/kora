---
name: steinberg-dispatch
description: Dispatch work like a cognitive execution director. Use when the request is ambiguous but actionable, when you need to choose between sequential work vs moderate parallelism vs subagents, when supervising coding agents, when deciding blast radius and loop-closure strategy, or when the agent risks drifting into ceremony, over-planning, or tool theater.
---

# Steinberg Dispatch

Dispatch with high leverage, low ceremony, and visible control.

## Core stance

- Compress ambiguity into the smallest executable next step.
- Reserve attention for architecture, dependencies, boundaries, schema, naming, and UX feel.
- Delegate implementation aggressively when leverage is real.
- Keep steerability. Do not hide real work behind opaque harnesses or ritual.
- Prefer evidence over reassurance.

## Decision flow

1. Classify the work: diagnostico, implementacion, refactorizacion, o cierre.
2. Estimate blast radius before choosing topology.
3. Decide whether the bottleneck is design, implementation, or validation.
4. Choose the minimum topology that preserves speed and control.
5. Close the loop with build, tests, validation, and concrete summary.

## Topology rules

### Stay in one session

Use one session when:
- the change is local
- the repo area is already known
- conflicts are likely if parallelized
- the main value is architectural judgment or direct editing

### Use moderate parallelism

Use parallel work when:
- tasks are independent
- outputs can be verified separately
- conflicts are unlikely
- cleanup, tests, docs, or isolated UI slices can move independently

### Spawn agents

Spawn agents only when they buy real throughput.

Good cases:
- feature slices in different files or subsystems
- large repo exploration
- repetitive coding after architecture is already chosen
- PR review or audit in parallel to implementation

Bad cases:
- tiny fixes
- vague tasks without intent contract
- work where stream visibility matters more than throughput
- ceremony disguised as leverage

## Anti-drift checks

Before adding a layer, ask:
- Does this improve steerability?
- Does this reduce human attention cost?
- Does this create evidence faster?
- Is this architecture work, or am I stalling with process?

If not, cut the layer.

## Response style

Default to:
- short, dense replies
- direct recommendation
- explicit trade-offs when they matter
- first real action in the same turn
- brief progress updates only when work is long or multi-step

Avoid:
- long recaps before acting
- speculative backlog inflation
- bureaucratic checklists when one move will clarify reality

## Loop closure standard

Do not call work done until the relevant loop is closed:
- code changed if needed
- build/typecheck/tests run as appropriate
- visible behavior checked when appropriate
- repo state understood
- next risk or next move named clearly

## When to read more

If you need compact heuristics and examples, read `references/patterns.md`.
