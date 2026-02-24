---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:banca-inversion-tools:2.0.0"
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
| Presupuesto inversion, subtitulos 31/33 | urn:gn:kb:gestion-prpto |
| Partida 31, glosas inversion | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| Ciclo proyectos, IDI, BIP | urn:gn:kb:gestion-ipr |
| Rendiciones, control, CGR | urn:gn:kb:gestion-rendiciones |
| Estrategia gestion GORE | urn:gn:kb:estrategia-gestion |
| Aceleracion regional, metodologia | urn:gn:kb:aceleracion-regional |
| ERD, ejes estrategicos, vision 2030 | urn:gn:kb:erd-nuble-2024-2030 |
| Nuble 250, proyectos emblematicos | urn:gn:kb:nuble-250 |
| GORE ideal, GORE 4.0, vision | urn:gn:kb:gore-ideal |
| Selector FNDR/FRPD/FRIL | urn:gn:kb:selector-ipr |
| Problemas sociales, necesidades | urn:gn:kb:problemas-sociales-cl |
| Geoespacial, IDE, planificacion territorial | urn:gn:kb:gestion-info-geoespacial |
| Seguridad, CIES, SITIA | urn:gn:kb:cies-sitia |
| Indicadores, metricas, estadisticas | urn:gn:kb:indicadores-nuble |
