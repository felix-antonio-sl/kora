---
_manifest:
  urn: urn:test:agent-bootstrap:sample-agents:1.0.0
  type: bootstrap_agents
version: 1.0.0
status: published
lang: es
---

# Sample Agent Bootstrap

## FSM

1. STATE: S-DISPATCHER -> ACT: Clasificar -> Trans: IF cerrar -> S-END.
2. STATE: S-END -> ACT: Terminar. -> Trans: [terminal].
