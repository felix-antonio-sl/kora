---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:pensador-generador-tools:2.0.0"
  type: "bootstrap_tools"
---

## search_kb

- **Firma:** query: string -> KBEntry[]
- **Cuando usar:** Consultar taxonomia MBT de tensiones u otros artefactos de conocimiento cuando el analisis lo requiera.
- **Cuando NO usar:** Para busquedas web o informacion en tiempo real. El agente opera principalmente con razonamiento LLM nativo.
- **Notas:** Politica ALLOW_GENERAL_KNOWLEDGE. KB potencia pero no limita el razonamiento.

## resolve_urn

- **Firma:** urn: string -> file_path: string
- **Cuando usar:** Resolver URN a path fisico antes de acceder contenido KB. Primer paso obligatorio.
- **Cuando NO usar:** Si path ya resuelto en turno actual.
- **Notas:** Catalogo SOURCE_OF_TRUTH. Fallback routing estatico. El path devuelto debe emplearse para operación de lectura directa e inyección en la memoria contextual del agente durante su session prep (runtime OpenClaw).

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB antes de invocar search_kb.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Tensiones creativas, MBT, dialectica, paradojas | `urn:fxsl:kb:fx-tensiones` |
