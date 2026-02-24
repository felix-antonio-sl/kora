---
_manifest:
  urn: "urn:kora:agent-bootstrap:transformer-tools:1.0.0"
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
| Formato KORA/Spec-MD prescriptivo, keywords, estructura YAML, densidad, lexicon | urn:kora:kb:spec-md |
| Transformar documentos, koraficacion, telegrafizacion, deduplicacion, KORA/MD | urn:kora:kb:md-spec |
