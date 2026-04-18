---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:neriomath-tools:1.3.0"
  type: "bootstrap_tools"
  status: active
---

## search_kb

- **Firma:** `query: string -> KBEntry[]`
- **Cuando usar:** Consultar taxonomia MBT de tensiones u otros artefactos de conocimiento cuando el analisis lo requiera.
- **Cuando NO usar:** Para busquedas web o informacion en tiempo real.
- **Notas:** La KB complementa el razonamiento del agente; no reemplaza la clasificacion ni la produccion final.

## catalog_resolve

- **Firma:** `urn: string -> path: string`
- **Cuando usar:** Resolver una URN a path fisico antes de acceder contenido KB.
- **Cuando NO usar:** Si el path ya fue resuelto en el turno actual.
- **Notas:** `catalog_master_*.yml` es la fuente de verdad del catalogo.

## kb_route

- **Firma:** `query_topic: string -> urn: string`
- **Cuando usar:** Clasificar tema y priorizar una URN KB antes de invocar `search_kb` o `catalog_resolve`.
- **Cuando NO usar:** Cuando el tema ya fue mapeado en el turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Tensiones creativas, MBT, dialectica, paradojas | `urn:fxsl:kb:fx-tensiones` |
