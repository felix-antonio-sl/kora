---
_manifest:
  urn: "urn:gn:agent-bootstrap:visionario-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB → LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Vision desarrollo, escenarios, prospectiva | urn:gn:kb:vision-desarrollo-nuble |
| GORE ideal, GORE 4.0, vision | urn:gn:kb:gore-ideal |
| Aceleracion regional, ExO-GORE, SCALE/IDEAS | urn:gn:kb:aceleracion-regional |
| ERD, ejes estrategicos, vision 2030 | urn:gn:kb:erd-nuble-2024-2030 |
| Estructura GORE Nuble, organigrama | urn:gn:kb:intro-gores-nuble |
| Estructura Estado, sistema politico | urn:mgmt:kb:estructura-estado-chile |
| Comunicaciones, estrategia comunicacional | urn:gn:kb:guia-comunicaciones |
| Estrategia TD e IA, modernizacion | urn:gn:kb:estrategia-td-ia |
| Informe estado inicial GORE pre-TD | urn:gn:kb:informe-estado-inicial-gore-pre-td |
| Indicadores, metricas regionales | urn:gn:kb:indicadores-nuble |
