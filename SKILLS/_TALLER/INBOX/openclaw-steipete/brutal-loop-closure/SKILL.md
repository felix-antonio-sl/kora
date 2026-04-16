---
name: brutal-loop-closure
description: Close the loop after code or configuration changes with strict evidence standards. Use after implementation, refactors, bug fixes, generated code, agent-delivered patches, or any change that is not done until build, tests, validation, repo state, and real remaining risk are checked.
---

# Brutal Loop Closure

Do not confuse movement with completion.

## Closure standard

A change is not done until the relevant loop is closed with evidence.

## Minimum closure pass

1. Identify what changed.
2. Run the narrowest meaningful validation first.
3. Run broader validation if blast radius requires it.
4. Check repo state.
5. Summarize evidence, realized blast radius, and remaining uncertainty.

## Validation ladder

### Level 1, local proof
Use when the change is isolated.
- targeted tests
- typecheck for touched area
- focused build or lint slice

### Level 2, subsystem proof
Use when multiple files or one subsystem moved.
- subsystem tests
- feature build
- realistic fixture or scenario run

### Level 3, system proof
Use when boundaries, contracts, runtime behavior, or deploy surfaces changed.
- full test suite when justified
- end-to-end path or live-system verification when possible
- explicit check of side effects and repo cleanliness

## Repo state check

Always know:
- what files changed
- whether unrelated dirt exists
- whether generated artifacts should be kept
- whether the final state is safe to hand off

## Good final summary

Include:
- what changed
- what validation ran
- what passed or failed
- actual blast radius
- what remains uncertain

## Avoid

- declaring success because code looks right
- hiding skipped validation
- vague phrases like "should work"
- forgetting repo dirt or side effects

## When to read more

For examples of closure depth by blast radius, read `references/closure-patterns.md`.
