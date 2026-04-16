# Dispatch patterns

## Quick topology matrix

| Situation | Topology | Why |
|---|---|---|
| Single risky refactor | Secuencial cuidadoso | Minimize conflict, preserve judgment |
| Main feature with bounded scope | 1-2 sequential actions | Keep control, close fast |
| Tests/docs/cleanup around a stable core | Parallel moderado | Independent outputs, low merge pain |
| Repo-wide exploration | Spawn agent or parallel discovery | Buy map-building speed |
| Architecture choice with high blast radius | Stay in-session | Judgment is the bottleneck |

## Fast triage prompts

### Diagnostico
- What is actually broken?
- Is the bottleneck observation, reproduction, or root cause?
- What is the fastest evidence-producing step?

### Implementacion
- Is the design already decided?
- How many files will this touch?
- Can I validate alone, or will I need system-level proof?

### Refactorizacion
- Is this hygiene or structural surgery?
- Can I preserve behavior with tests?
- What conflict surface will parallelism create?

### Cierre
- What loop remains open?
- Do I have build, tests, behavior, and repo state?
- What uncertainty still matters?

## Signs you are drifting into theater

- writing a big plan where one probe would answer the question
- spawning agents before framing intent
- reading broad swaths of code without leverage points
- reporting effort instead of evidence
- adding tooling because it feels sophisticated

## Good summaries

A good summary includes:
- what changed
- evidence of closure
- blast radius realized
- trade-offs taken
- next uncertainty or next move

A bad summary includes:
- generic reassurance
- long process narration
- claims of completion without validation
- no mention of risk
