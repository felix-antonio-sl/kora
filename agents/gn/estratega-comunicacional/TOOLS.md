---
_manifest:
  urn: "urn:gn:agent-bootstrap:estratega-comunicacional-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Si el usuario provee documentos o se referencia un artifact KORA, resolver URN via catalogo.
- **Cuando NO usar:** Operacion LLM_NATIVE sin artefactos KB. Este agente opera primariamente con razonamiento general.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Este agente usa policy LLM_NATIVE: su valor esta en el metodo estrategico, no en datos especificos de KB.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Solo si el usuario provee documentos de marca o contexto organizacional que requiera localizacion en catalogo.
- **Cuando NO usar:** Consultas generales de comunicacion estrategica. Este agente opera con razonamiento LLM nativo.
- **Notas:** Routing map vacio por default. Se construye dinamicamente si el usuario aporta contexto documental.
