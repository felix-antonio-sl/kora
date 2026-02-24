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
| Spec, YAML, keywords, densidad | urn:kora:kb:spec |
| Transform, 4 fases, telegrafizacion | urn:kora:kb:transform |
| Hub, URNs, manifiestos, catalogo, federacion | urn:kora:kb:hub-federation |
| Life, 5 fases, Git, deployment | urn:kora:kb:life |
| Agent spec, 7 principios, namespaces, Guard Set | urn:kora:kb:agent |
| Construir agentes, 5 fases, KB modes | urn:kora:kb:agent-construct |
| Test, pruebas, seguridad, regresion | urn:kora:kb:test |
| Schema versioning, migracion | urn:kora:kb:schema-versioning |
| Quickstart, templates, primer agente | urn:kora:kb:quickstart |
| JSON Schema, validacion | urn:kora:kb:agent-schema |
| Skills, federation, symlinks | urn:kora:kb:skills-federation |
| Federation, resolver, registry, cross-repo | urn:kora:kb:hub-federation |
