---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ar-virtual-tools:2.0.0"
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
| Estructura Estado, sistema politico | urn:mgmt:kb:estructura-estado-chile |
| LOC 19.175, competencias GORE, atribuciones | urn:gn:kb:loc-gore |
| Estructura GORE Nuble, organigrama, divisiones | urn:gn:kb:intro-gores-nuble |
| Marco legal complementario | urn:gn:kb:marco-legal-gores |
| Glosario GORE Nuble | urn:gn:kb:glosario-gore-nuble |
| Flujos aprobacion, visado, resoluciones | urn:gn:kb:flujos-aprobacion-documentos |
| Presupuesto, SIGFE, subtitulos, saldos | urn:gn:kb:gestion-prpto |
| Ley Presupuestos, Partida 31, glosas | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| Estrategia gestion GORE | urn:gn:kb:estrategia-gestion |
| Manual induccion GORE | urn:gn:kb:manual-induccion-gore-nuble-2026 |
| Cuentas publicas 2021-2024 | urn:gn:kb:cuentas-publicas-2021-2024 |
| ERD, ejes estrategicos, vision 2030 | urn:gn:kb:erd-nuble-2024-2030 |
| Nuble 250, proyectos emblematicos | urn:gn:kb:nuble-250 |
| Indicadores, estadisticas regionales | urn:gn:kb:indicadores-nuble |
| TDE, introduccion | urn:gov:kb:intro-tde |
| Ley 21.180, TDE, modernizacion | urn:tde:kb:ley-21180 |
| Clave Unica | urn:tde:kb:claveunica |
| SIMPLE SaaS | urn:tde:kb:simple-saas |
