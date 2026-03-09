---
_manifest:
  urn: urn:kora:agent-bootstrap:guardian-tools:1.0.0
  type: bootstrap_tools
---

## kb_route
- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Cuando se requiere resolver conocimiento formal de KORA.
- **Cuando NO usar:** Cuando la respuesta no depende de la KB.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Gobernanza, precedencia, meta-reglas | urn:kora:kb:gobernanza |
| Formato prescriptivo, cristalizacion, RFC 2119 | urn:kora:kb:spec-md |
| Formato descriptivo, KORA/MD, constraints documentales | urn:kora:kb:md-spec |
| Agentes, segregacion, FSM, wiring | urn:kora:kb:agent-spec-md |
| Skills, CM Core, lazy-load | urn:kora:kb:skill-spec-md |
| Runtime, wrappers, equivalencia cross-platform | urn:kora:kb:runtime-spec-md |
| Swarms, multi-agent, circuit breakers | urn:kora:kb:swarm-spec-md |

## spec_consult
- **Firma:** spec_name: string -> content: string
- **Cuando usar:** Cuando se requiere leer una spec fundacional concreta para sustentar una decision normativa o una auditoria.
- **Cuando NO usar:** Cuando la regla ya fue consultada y sigue vigente en el turno actual.
- **Notas:** Specs disponibles: gobernanza, spec-md, md-spec, agent-spec-md, skill-spec-md, runtime-spec-md, swarm-spec-md.

## repo_health
- **Firma:** {} -> {issues: object[]}
- **Cuando usar:** Cuando se requiere auditar integridad del repo o de las specs.
- **Cuando NO usar:** Cuando basta con una respuesta conceptual sin auditoria.
- **Notas:** Limitar a evidencia observable del repo y toolchain visible; no inferir capacidades externas no declaradas.
