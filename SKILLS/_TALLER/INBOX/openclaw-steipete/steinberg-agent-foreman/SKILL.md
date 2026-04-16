---
name: steinberg-agent-foreman
description: Supervise multiple agents like a working foreman with visibility and control. Use when coordinating 2 or more agents, splitting a coding effort into slices, integrating reports, preventing overlap, deciding what should stay with the human vs be delegated, or when parallelism risks becoming subagent soup.
---

# Steinberg Agent Foreman

Use agents as workers, not as theater.

## Goal

Increase throughput without losing steerability, visibility, or architectural control.

## Foreman stance

- The human or lead agent owns direction, taste, and structural decisions.
- Workers own bounded execution slices.
- Reports must be short, concrete, and integrable.
- If overlap is likely, coordinate before code moves.
- Kill or redirect workers when they drift.

## Workflow

1. Frame the work in the smallest meaningful slices.
2. Keep architecture and boundary decisions in the lead seat.
3. Delegate only slices with clear outputs.
4. Require compact reports with files, status, evidence, and next step.
5. Integrate continuously, not only at the end.

## Good delegation targets

- isolated feature slices
- repo exploration
- audits in parallel to implementation
- test expansion
- visual validation
- repetitive mechanical refactors after design is fixed

## Bad delegation targets

- fuzzy intent
- boundary decisions
- naming decisions with broad impact
- schema direction
- changes that will obviously conflict if done in parallel

## Foreman checks

Ask continuously:
- Is each worker on a bounded slice?
- Is any worker duplicating another?
- Did the bottleneck move back to design?
- Do I have enough evidence to integrate now?
- Should this worker continue, pivot, or stop?

## Integration rule

Never assume a worker report is enough by itself.
Read the leverage points, verify the loop, and integrate with judgment.

## When to read more

For concrete coordination patterns and report formats, read `references/patterns.md`.
