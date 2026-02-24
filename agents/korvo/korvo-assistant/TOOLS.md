---
_manifest:
  urn: "urn:korvo:agent-bootstrap:korvo-assistant-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Temas personales/cotidianos sin necesidad de KB formal.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Spec agentes, principios | urn:kora:kb:agent-spec-md |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion actual sobre temas de Felix (noticias, herramientas, cursos, salud, finanzas).
- **Cuando NO usar:** Opiniones personales o consejos donde experiencia directa es suficiente.

## domain_route

- **Firma:** query: string → domain: string
- **Cuando usar:** Clasificar consulta de Felix en dominio(s) relevante(s).
- **Cuando NO usar:** Dominio ya identificado en turno actual.
- **Routing:**

| Pattern | Domain |
|---------|--------|
| salud, bienestar, dormir, ejercicio, medico | salud |
| dinero, ahorro, gasto, inversion, presupuesto | finanzas |
| meta, objetivo, proyecto, deadline, OKR | metas |
| aprender, curso, libro, skill, conocimiento | aprendizaje |
| contacto, networking, relacion, reunion | relaciones |
| problema, reto, obstaculo, bloqueado | problemas |
| sistema, korvo, agente, regla, update | korvo |
