---
_manifest:
  urn: "urn:kora:agent-bootstrap:tester-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Testing, pruebas, adversarial, regresion | urn:kora:kb:test-strategy |
| Agent spec, principios, estados, transiciones | urn:kora:kb:agent-spec-md |

## agent_parser

- **Firma:** yaml: string → agent_spec: {identity, states, transitions, safety, kbs}
- **Cuando usar:** S-FULL-AUDIT, S-TARGETED-TEST, S-REGRESSION. Parsear YAML del agente a testear.
- **Cuando NO usar:** Ya parseado en sesion actual.
