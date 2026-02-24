---
_manifest:
  urn: "urn:kora:skill:smith-agent-builder:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-AGENT-BUILDER

## Proposito
Genera el agent.yaml completo con los 7 namespaces KODA, ensamblando todos los artefactos producidos en fases anteriores (FTCF, FSM, CMs, Guard Set) en un artefacto valido y coherente.

## Procedimiento
1. Ensamblar `_manifest`: urn (urn:koda:agent:{nombre}:{version}), type:agent, version, created_at, Runtime Directive.
2. Ensamblar `KODA_Runtime`: runtime_version, catalog_source, kb_resolver, guard_set reference.
3. Ensamblar `agent_identity`: name, role, paradigm, tone (del FTCF-Tono), greeting.
4. Ensamblar `knowledge_base`: mode (del Knowledge Mode), allowed_urns (del CM-KNOWLEDGE-MODE-SELECTOR), kb_priority_order.
5. Ensamblar `workflows_states`: initial_state, states (del CM-STATE-DESIGNER), cada estado con action y transitions.
6. Ensamblar `reasoning_processes`: lista de CMs (del CM-CM-DESIGNER), cada uno con _meta expose:false.
7. Ensamblar `io_style`: format, verbosity, safety (del CM-GUARD-CONFIGURATOR), eval (checklist co-induccion), few_shot (ejemplos de comportamiento).
8. Generar YAML con comentarios de trazabilidad (# origen: FTCF, # origen: Guard Set, etc.).
9. Verificar estructura: los 7 namespaces presentes, sin campos vacios obligatorios.

## Output
agent.yaml completo y comentado con los 7 namespaces. Listo para pasar a CM-AGENT-VALIDATOR.
