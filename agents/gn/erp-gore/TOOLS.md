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
| Manual presupuesto, ejecucion presupuestaria | urn:gn:kb:manual-presupuesto |
| Ley presupuestos, Partida 31, glosas | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| Normas generales ley presupuestos | urn:gn:kb:ley-presupuestos-2026-normas-generales |
| Contabilidad, registros contables, NICSP | urn:gn:kb:manual-contabilidad |
| Tesoreria, pagos, flujo caja | urn:gn:kb:manual-tesoreria |
| Compras, adquisiciones, licitaciones, Mercado Publico | urn:gn:kb:manual-compras |
| Inventarios, bodegas, stock | urn:gn:kb:manual-inventarios-bodegas |
| Activo fijo, patrimonio, bienes | urn:gn:kb:manual-activo-fijo |
| Remuneraciones, liquidaciones, sueldos | urn:gn:kb:manual-remuneraciones |
| Asistencia, control horario, ausentismo | urn:gn:kb:manual-asistencia |
| Bienestar, beneficios, prestaciones funcionarias | urn:gn:kb:manual-bienestar |
| Ciclo vida funcionario, ingreso, egreso | urn:gn:kb:manual-ciclo-vida |
| RRHH, capacitacion, desarrollo | urn:gn:kb:manual-desarrollo-organizacional |
| Induccion, organizacion GORE | urn:gn:kb:manual-induccion-gore-nuble-2026 |
| Flotas, vehiculos, flota vehicular | urn:gn:kb:manual-flotas |
| DGI, operaciones, control gestion, reportes | urn:gn:kb:manual-operacional-dgi |
| Indicadores, metricas regionales | urn:gn:kb:indicadores-nuble |
| Intro GOREs Nuble | urn:gn:kb:intro-gores-nuble |
