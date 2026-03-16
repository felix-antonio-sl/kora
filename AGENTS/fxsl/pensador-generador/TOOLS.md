---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:pensador-generador-tools:2.0.0"
  type: "bootstrap_tools"
---

## search_kb

- **Firma:** `query: string -> KBEntry[]`
- **Parametros:** `query` con el tema o tension a consultar en la KB autorizada.
- **Cuando usar:** Consultar taxonomia MBT de tensiones u otros artefactos de conocimiento cuando el analisis lo requiera.
- **Cuando NO usar:** Para busquedas web o informacion en tiempo real.
- **Descripcion funcional:** Recupera entradas KB relevantes para apoyar el analisis dialectico del agente.
- **Notas:** La KB complementa el razonamiento del agente; no reemplaza la clasificacion ni la produccion final.

## catalog_resolve

- **Firma:** `urn: string -> path: string`
- **Parametros:** `urn` conceptual del artefacto KB a resolver.
- **Cuando usar:** Resolver una URN a path fisico antes de acceder contenido KB.
- **Cuando NO usar:** Si el path ya fue resuelto en el turno actual.
- **Descripcion funcional:** Resuelve una URN valida del catalogo a una ruta local consultable por el agente.
- **Notas:** `catalog_master_*.yml` es la fuente de verdad del catalogo.

## kb_route

- **Firma:** `query_topic: string -> urn: string`
- **Parametros:** `query_topic` con el tema o familia conceptual a priorizar.
- **Cuando usar:** Clasificar tema y priorizar una URN KB antes de invocar `search_kb` o `catalog_resolve`.
- **Cuando NO usar:** Cuando el tema ya fue mapeado en el turno actual.
- **Descripcion funcional:** Asigna el tema analitico a la fuente KB primaria del corpus MBT.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Tensiones creativas, MBT, dialectica, paradojas | `urn:fxsl:kb:fx-tensiones` |
