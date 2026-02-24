---
_manifest:
  urn: "urn:kora:agent-bootstrap:orquestador-generico-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Resolver URNs de participantes y artefactos. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o participante ya resuelto en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de invocar participante.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Guiar consultas a fuentes/participantes correctos. Identificar intencion/tema → determinar fuente principal → entregar guia.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Notas:** Declarar incertidumbre si no existe fuente.

## orchestrate

- **Firma:** participants: URN[], protocol: SECUENCIAL|PARALELO|DINAMICO|CONSENSO, objective: string → result: SynthesisResult
- **Cuando usar:** Ejecutar protocolo de orquestacion con participantes configurados.
- **Cuando NO usar:** Sin participantes confirmados o sin protocolo seleccionado.
