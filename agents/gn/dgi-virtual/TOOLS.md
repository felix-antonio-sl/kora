---
_manifest:
  urn: "urn:gn:agent-bootstrap:dgi-virtual-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. catalog_master_kora.yml = SOURCE_OF_TRUTH.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema -> resolver URN -> priorizar KB -> LLM solo pegamento. Incluye routing heredado de AR Virtual + especializacion DGI.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Estructura Estado, LOC, competencias GORE | urn:gn:kb:loc-gore |
| Estructura GORE Nuble, organigrama, divisiones | urn:gn:kb:intro-gores-nuble |
| Flujos aprobacion, visado, resoluciones | urn:gn:kb:flujos-aprobacion-documentos |
| ERD, ejes estrategicos, vision 2030 | urn:gn:kb:erd-nuble-2024-2030 |
| TDE, Ley 21.180, modernizacion | urn:tde:kb:ley-21180 |
| Introduccion TDE | urn:gov:kb:intro-tde |
| Control de gestion, indicadores, dashboards, alertas | urn:gn:kb:manual-operacional-dgi |
| Procesos, BPMN, modelado, automatizacion | urn:gn:kb:manual-operacional-dgi |
| DMAIC, Lean, Six Sigma, mejora continua | urn:mgmt:kb:lean6 |
| Estructura organizacional, principios Meyer | urn:mgmt:kb:meyer-org-structure |
| Stakeholders, ADKAR, gestion del cambio, navegacion social | urn:gn:kb:plan-potenciamiento-dgi |
| Presupuesto, gestion financiera | urn:gn:kb:gestion-prpto |
| Estructura Estado Chile | urn:mgmt:kb:estructura-estado-chile |
