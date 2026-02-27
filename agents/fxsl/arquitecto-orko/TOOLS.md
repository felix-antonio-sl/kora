---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-orko-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB → LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Teoria, Genoma, Fundamentos (L0) | urn:orko:kb:orko-fundamentos |
| Arquitectura, Estructura (L1) | urn:orko:kb:orko-arquitectura |
| Tejidos, Implementacion (L2) | urn:orko:kb:orko-tejidos |
| Metodologia, Proceso (L3) | urn:orko:kb:orko-metodologia |
| Toolkit, Herramientas (L4-5) | urn:orko:kb:orko-toolkit |
| Implementacion Toolkit (L4-5) | urn:orko:kb:impl-orko-toolkit |
