# Intent framing examples

## Good compressed frame

- Beneficiary: operator who needs X
- Desired change: make Y possible with Z constraint
- Expected benefit: less ambiguity / faster execution / better reliability
- Success criterion: one concrete proof point
- Minimum eval: build + one realistic scenario
- Autonomy limit: agent may choose implementation details, not platform direction
- Main risk: schema drift / UX confusion / wrong boundary

## Anti-patterns

### Fake clarity
Saying "build the best possible system" without beneficiary, scope, or eval.

### Hidden architecture decision
Treating a major platform or schema decision as if it were just implementation.

### Throughput compensation
Spawning agents and coding fast before intent is stable.

## Escalation rule

If beneficiary, success criterion, or autonomy limit are missing and the blast radius is high, stop and frame before dispatch.
