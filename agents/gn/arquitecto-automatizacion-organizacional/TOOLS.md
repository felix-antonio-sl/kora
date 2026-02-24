---
_manifest:
  urn: "urn:gn:agent-bootstrap:arquitecto-automatizacion-organizacional-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Resolver URNs de KBs cuando se necesite informacion especifica. catalog_master_kora.yml = SOURCE_OF_TRUTH.
- **Cuando NO usar:** Datos ya en contexto. Este agente opera primariamente con conocimiento LLM nativo.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Si hay KB especifica disponible, usarla. Si es conocimiento general de automatizacion/IA, usar LLM nativo.
- **Cuando NO usar:** Temas cubiertos por conocimiento internalizado de sistemas, automatizacion e IA.
- **Notas:** Este agente usa politica LLM_NATIVE. KB es complementario, no primario.

## web_search

- **Firma:** query: string -> results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, frameworks de automatizacion especificos, sintaxis de herramientas recientes, documentacion APIs externas.
- **Cuando NO usar:** Conceptos fundamentales de sistemas, automatizacion o IA ya internalizados.

## artifact_generate

- **Firma:** model: SystemModel, format: TargetFormat -> artifact: string
- **Cuando usar:** Generar artefactos de automatizacion: flujos n8n/Make, system prompts, configuraciones de agentes, diagramas de arquitectura.
- **Cuando NO usar:** Codigo de aplicacion (derivar a ingeniero-software-composicional).
- **Formatos:** Workflow JSON, System Prompt, Mermaid, PlantUML, BPMN
