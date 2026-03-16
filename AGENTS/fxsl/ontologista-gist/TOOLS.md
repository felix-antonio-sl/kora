---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ontologista-gist-tools:1.0.0"
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
| Direcciones, Address patterns | urn:fxsl:kb:fx-address-guidance |
| Magnitudes, UoM, Aspects | urn:fxsl:kb:fx-uom-model |
| Namespace, IRI, prefijos | urn:fxsl:kb:fx-namespace |
| Overview, getting started | urn:fxsl:kb:fx-readme |
| Audit protocol, Gist guidance | urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, novedades Gist, integraciones no documentadas en KB.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.
