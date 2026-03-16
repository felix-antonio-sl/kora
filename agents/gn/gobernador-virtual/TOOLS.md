---
_manifest:
  urn: "urn:gn:agent-bootstrap:gobernador-virtual-tools:3.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema -> resolver URN -> priorizar KB -> LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| LOC, atribuciones GR, competencias | urn:gn:kb:loc-gore |
| ERD, vision 2030, ejes estrategicos | urn:gn:kb:erd-nuble-2024-2030 |
| Nuble 250, proyectos emblematicos | urn:gn:kb:nuble-250 |
| GORE Ideal, vision institucional | urn:gn:kb:gore-ideal |
| Presupuesto, Partida 31 | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| IPR, inversion, proyectos | urn:gn:kb:gestion-ipr |
| Estructura Estado Chile | urn:gn:kb:estructura-estado-chile |
| Intro GOREs Nuble | urn:gn:kb:intro-gores-nuble |
| Marco legal GOREs | urn:gn:kb:marco-legal-gores |
| Gestion presupuestaria | urn:gn:kb:gestion-prpto |
| Cuentas publicas 2021-2024 | urn:gn:kb:cuentas-publicas-2021-2024 |
| Estrategia gestion | urn:gn:kb:estrategia-gestion |
| Flujos aprobacion documentos | urn:gn:kb:flujos-aprobacion-documentos |
| Vision desarrollo, escenarios, prospectiva | urn:gn:kb:vision-desarrollo-nuble |
| Comunicaciones, estrategia comunicacional | urn:gn:kb:guia-comunicaciones |
| Comunicaciones OC, protocolo | urn:gn:kb:comunicaciones-oc |
