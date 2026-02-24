---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-sistemas-composicional-tools:1.0.0"
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
| Categorical Systems Theory, lenses, wiring | urn:fxsl:kb:categorical-systems-theory |
| MBSE, S2ML, consistency | urn:fxsl:kb:mbse-consistency |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff, regulaciones vigentes especificas, tecnologias emergentes, costos actuales.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.

## artifact_generate

- **Firma:** model: SystemModel, format: TargetFormat → artifact: string
- **Cuando usar:** S-ARTIFACT-GENERATION. Traducir modelo de sistema a formato de salida.
- **Cuando NO usar:** Modelo no formalizado aun (requiere S-SYSTEM-MODELING o S-BREAKDOWN-DESIGN primero).
- **Formatos:** OPD, OPL, FBS/PBS/LBS Tree, SRS, Traceability Matrix, Wiring Diagram, Work System Snapshot, Interface Control Document
