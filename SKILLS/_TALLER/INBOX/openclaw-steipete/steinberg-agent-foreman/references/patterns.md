# Foreman patterns

## Minimal report format

Use compact reports like:

- what I did
- files touched
- state
- evidence
- next step

## Topology examples

### Two-worker pattern
- Worker A: exploration or audit
- Worker B: implementation
- Lead: integration and direction

### Three-worker pattern
- Worker A: core feature slice
- Worker B: tests/validation
- Worker C: docs or visual verification
- Lead: architectural review and merge decisions

## Signs of subagent soup

- workers touching the same files without coordination
- long reports with no evidence
- the lead reading every line because slices were badly framed
- workers blocked on design the lead never resolved

## Good interventions

- narrow the slice
- stop one worker and reassign
- merge parallel paths back to one session
- escalate structural decisions to the human
