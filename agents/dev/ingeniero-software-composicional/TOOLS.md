---
_manifest:
  urn: "urn:dev:agent-bootstrap:ingeniero-software-composicional-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog_master_*.yml → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB → LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Seven Sketches, composicionality, functors | urn:fxsl:kb:seven-sketches |
| Coalgebras, bisimulacion, coinduccion | urn:fxsl:kb:coalgebras |
| Cognitive toolkit, FDM, DIK, Lenses | urn:fxsl:kb:cognitive-toolkit |
| Categorical data structures | urn:fxsl:kb:categorical-data-structures |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, frameworks especificos, sintaxis versiones recientes.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.
