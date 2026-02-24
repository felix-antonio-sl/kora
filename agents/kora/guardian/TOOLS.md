---
_manifest:
  urn: "urn:kora:agent-bootstrap:guardian-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Spec-MD, keywords, YAML prescriptivo, densidad | urn:kora:kb:spec-md |
| MD-spec, koraficacion, KORA/MD descriptivo | urn:kora:kb:md-spec |
| Hub agentes, URNs, catalogo, federacion | urn:kora:kb:hub-agentes |
| Agent spec, 7 principios, namespaces, P1-P7, Guard Set | urn:kora:kb:agent-spec-md |
| Construccion agentes, 5 fases, patterns, FTCF | urn:kora:kb:agent-spec-md |
| Workflow wikiguias, transformacion, editorial | urn:kora:kb:workflow-wikiguias |
| Federation, cross-repo, registry | urn:kora:kb:hub-agentes |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Info externa para comparaciones, tendencias, estado del arte fuera de KB.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.
- **Config:** scope=general, max_results=5, freshness=month, citation_required=true
