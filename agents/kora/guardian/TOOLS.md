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
| Spec, keywords, YAML | urn:kora:kb:spec |
| Transform, 4 fases, metricas | urn:kora:kb:transform |
| Hub, URNs, catalogo, federacion | urn:kora:kb:hub-federation |
| Life, 5 fases, Git | urn:kora:kb:life |
| Agent, 7 principios, namespaces | urn:kora:kb:agent |
| Construccion, 5 fases, patterns | urn:kora:kb:agent-construct |
| Test, validacion, seguridad | urn:kora:kb:test |
| Federation, cross-repo, registry | urn:kora:kb:hub-federation |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Info externa para comparaciones, tendencias, estado del arte fuera de KB.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.
- **Config:** scope=general, max_results=5, freshness=month, citation_required=true
