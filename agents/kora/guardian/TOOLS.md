---
_manifest:
  urn: urn:kora:agent-bootstrap:guardian-tools:1.0.0
  type: bootstrap_tools
---

## kb_route
- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Cuando se requiere resolver conocimiento formal de KORA.
- **Cuando NO usar:** Cuando la respuesta no depende de la KB.

## repo_health
- **Firma:** {} -> {issues: object[]}
- **Cuando usar:** Cuando se requiere auditar integridad del repo o de las specs.
- **Cuando NO usar:** Cuando basta con una respuesta conceptual sin auditoria.
