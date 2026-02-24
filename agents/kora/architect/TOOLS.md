---
_manifest:
  urn: "urn:kora:agent-bootstrap:architect-tools:1.0.0"
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
| Spec-MD, formato KORA/Spec-MD, prescriptivo, keywords, densidad | urn:kora:kb:spec-md |
| MD-spec, formato KORA/MD, descriptivo, koraficacion, RAG | urn:kora:kb:md-spec |
| Hub agentes, URNs, manifiestos, catalogo, federacion | urn:kora:kb:hub-agentes |
| Agent spec, 7 principios, namespaces, Guard Set, F-coalgebra | urn:kora:kb:agent-spec-md |
| Construir agentes, 5 fases, KB modes, FTCF, validacion | urn:kora:kb:agent-spec-md |
| Workflow wikiguias, transformacion documentos, proceso editorial | urn:kora:kb:workflow-wikiguias |
| Federation, resolver, registry, cross-repo | urn:kora:kb:hub-agentes |
