---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:asesor-juridico-tools:4.0.0"
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
| Organigrama, estructura GORE | urn:gn:kb:organigrama |
| Flujos aprobacion, visado, resoluciones | urn:gn:kb:flujos-aprobacion-documentos |
| Plantillas actos juridicos | urn:gn:kb:modelos-actos-juridicos |
| Manual compras publicas | urn:gn:kb:manual-compras |
| Manual presupuesto | urn:gn:kb:manual-presupuesto |
| Rendiciones, control, CGR | urn:gn:kb:gestion-rendiciones |
| LOC 19.175, competencias GORE | urn:gn:kb:loc-gore |
| Marco legal complementario | urn:gn:kb:marco-legal-gores |
| Dictamenes CGR aplicables | urn:gn:kb:dictamenes-cgr-gore |
| Gestion IPR, ciclo proyectos | urn:gn:kb:gestion-ipr |
| Circular 33, STS | urn:gn:kb:guia-circular-33-sts |
| Transferencias PPR | urn:gn:kb:transferencia-ppr |
| Selector IPR, vias financiamiento | urn:gn:kb:selector-ipr |
| Gestion presupuestaria | urn:gn:kb:gestion-prpto |
| Ley Presupuestos 2026, Partida 31, umbrales | urn:gn:kb:ley-presupuestos-2026-partida-31 |
