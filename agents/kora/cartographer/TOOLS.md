---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-tools:1.0.0"
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
- **Notas:** Routing vacio — usa ALLOW_GENERAL_KNOWLEDGE + domain_knowledge patterns.

## pattern_advise

- **Firma:** query: string → pattern: GistPattern, example: string
- **Cuando usar:** S-CONSULTANT o cualquier estado que requiera recomendar patron de modelado.
- **Cuando NO usar:** Si el usuario ya especifico patron deseado.
- **Routing Map:**

| Topic | Pattern | Example |
|-------|---------|---------|
| Taxonomia, clasificacion, tipos, estados | Category Pattern (Gist) | category(scheme, code, label, parent_id) |
| Metricas, mediciones, KPIs, porcentajes | Magnitude + Aspect Pattern (Gist) | magnitude(subject_type/id, aspect, value, unit) |
| Eventos, transacciones, auditoria, historico | Event Pattern (Gist) | event(event_type, subject_type/id, occurred_at, data) |
| Relaciones temporales, vigencias, asignaciones | Temporal Validity Pattern | valid_from/valid_to con EXCLUDE constraint |
