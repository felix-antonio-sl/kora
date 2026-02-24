---
_manifest:
  urn: "urn:kora:agent-bootstrap:sim-orchestrator-tools:2.0.0"
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
| Testing, pruebas | urn:kora:kb:test-strategy |
| Agentes, spec | urn:kora:kb:agent-spec-md |

## delegate_tester

- **Firma:** task: string, context: object → result: TestResult
- **Cuando usar:** Generar suite de tests (S-PLAN-TESTS) o evaluar evidencia (S-EVALUATE). Delegar al sub-agente TESTER.
- **Cuando NO usar:** Simulacion directa (eso lo hace el orchestrator).
