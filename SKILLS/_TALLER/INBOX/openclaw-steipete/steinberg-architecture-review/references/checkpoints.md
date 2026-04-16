# Architecture review checkpoints

## Structural hotspots

### Boundaries
- unclear ownership between modules
- cycles or back-edges hidden behind helpers
- API surfaces wider than necessary

### Schemas and models
- names that encode implementation instead of domain
- entities that should really be events, states, or projections
- shape drift between DB, API, and UI models

### Runtime split
- server/client boundaries chosen by convenience
- side effects leaking into rendering paths
- state duplication without a single source of truth

### Repo shape
- critical operations impossible without tribal knowledge
- giant files hiding multiple responsibilities
- docs detached from actual code paths

## Strong recommendations style

Good:
- "This boundary is wrong because X depends on Y in the wrong direction."
- "This schema will hurt once Z appears."
- "This naming collapses two distinct concepts."

Weak:
- "Could be improved"
- "Consider maybe refactoring"
- "Might want to revisit"

## Human-only zones

Escalate to the human when the change affects:
- platform choice
- dependency adoption
- durable schema direction
- product feel or interaction philosophy
- organizational ownership across subsystems
