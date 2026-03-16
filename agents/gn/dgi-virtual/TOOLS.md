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
| TDE, Ley 21.180, modernizacion | urn:tde:kb:ley-21180-transformacion-digital-estado |
| Introduccion TDE | urn:tde:kb:guia-metodologica-sistema-transformacion-digital-2025 |
| Control de gestion, indicadores, dashboards, alertas | urn:gn:kb:manual-operacional-dgi |
| Procesos, BPMN, modelado, automatizacion | urn:gn:kb:manual-operacional-dgi |
| DMAIC, Lean, Six Sigma, mejora continua | urn:gn:kb:lean6-gestion-core |
| Estructura organizacional, principios Meyer | urn:gn:kb:meyer-estructura-organizacional |
| Stakeholders, ADKAR, gestion del cambio, navegacion social | urn:gn:kb:plan-potenciamiento-dgi |
| Presupuesto, gestion financiera | urn:gn:kb:gestion-prpto |
| Estructura Estado Chile | urn:gn:kb:estructura-estado-chile |
| Modernizacion Estado, Waissbluth | urn:gn:kb:modernizacion-estado-waissbluth |
| BPMN actos administrativos, tramitacion | urn:gn:kb:bpmn-actos-administrativos |
| CIES, SITIA, seguridad publica, videovigilancia | urn:gn:kb:bpmn-cies-sitia |
| Geoespacial, IDE, Geonodo, SIG | urn:gn:kb:bpmn-geoespacial-ide |
