---
_manifest:
  urn: "urn:gn:agent-bootstrap:erp-gore-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema -> resolver URN -> priorizar KB -> LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Presupuesto, SIGFE, subtitulos, disponibilidad | urn:gn:kb:gestion-prpto |
| Ley presupuestos, Partida 31, glosas | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| Normas generales ley presupuestos | urn:gn:kb:ley-presupuestos-2026-normas-generales |
| Induccion, organizacion GORE | urn:gn:kb:manual-induccion-gore-nuble-2026 |
| DGI, operaciones, control gestion, reportes | urn:gn:kb:manual-operacional-dgi |
| Intro GOREs Nuble | urn:gn:kb:intro-gores-nuble |
| Glosas GORE, Ley Presupuestos | urn:gn:kb:ley-presupuestos-2026-glosas-gore |
| Compras, licitaciones, ChileCompra, convenio marco | urn:gn:kb:manual-compras-contrataciones |
| Contabilidad gubernamental, SIGFE, NICSP, devengos | urn:gn:kb:manual-contabilidad |
| Tesoreria, pagos, garantias, conciliacion bancaria | urn:gn:kb:manual-tesoreria |
| RRHH, remuneraciones, ciclo vida funcionario | urn:gn:kb:manual-gestion-personas |
| Inventarios, activo fijo, bodegas, patrimonio | urn:gn:kb:manual-inventarios-activo-fijo |
| Flota vehicular, logistica, mantencion | urn:gn:kb:manual-flota-servicios-generales |
| Organigrama, estructura GORE | urn:gn:kb:organigrama |
| Rendiciones, SISREC, control CGR | urn:gn:kb:gestion-rendiciones |
| Flujos aprobacion, visado, resoluciones | urn:gn:kb:flujos-aprobacion-documentos |
| Modelos actos juridicos, plantillas | urn:gn:kb:modelos-actos-juridicos |
