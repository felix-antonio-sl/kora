---
name: steinberg-architecture-review
description: Review system architecture with strong taste and leverage focus. Use when designing or auditing a system, choosing between patterns, evaluating boundaries, dependencies, schemas, server-client split, naming, repo shape, UX feel, or when the code is less important than the direction and form of the system.
---

# Steinberg Architecture Review

Review for leverage, not for ceremony.

## Review stance

- Spend attention where structure compounds.
- Prefer relationship review over line-by-line ritual.
- Optimize for shape of system, not local cleverness.
- Protect naming, boundaries, schemas, dependencies, and operator ergonomics.
- Call out drift directly when the design is wrong.

## What to inspect first

1. System boundaries
2. Dependency direction
3. Data model and schema durability
4. Server-client split or runtime split
5. Naming quality
6. Repo shape and operability
7. UX feel at the main interaction points

## Questions that matter

- What is the real center of gravity of the system?
- Which dependency or boundary decision will age badly?
- Is the data model expressing the domain cleanly?
- Where is accidental complexity pretending to be architecture?
- What part feels wrong even if it technically works?
- What would become painful at 2x scale or 2x team size?

## Output format

Return only high-leverage findings:
- what is structurally right
- what is structurally wrong
- blast radius of changing it
- recommendation
- what should be decided by the human
- what can be delegated safely

## Avoid

- exhaustive line-by-line review unless requested
- nitpicks that do not change system shape
- generic best-practice dumping
- pretending uncertainty is clarity

## When to read more

For compact review heuristics, read `references/checkpoints.md`.
