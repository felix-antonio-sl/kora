---
_manifest:
  urn: "urn:gn:agent-bootstrap:eacs-tools:2.0.0"
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
| Flujos aprobacion, resoluciones, decretos, convenios, firmas | urn:gn:kb:flujos-aprobacion-documentos |
| Modelos, plantillas, formatos, estructura actos | urn:gn:kb:modelos-actos-juridicos |
| LOC 19.175, competencias, atribuciones, articulos | urn:gn:kb:loc-gore |
| Leyes relacionadas, reformas, Ley 19.880, CGR | urn:gn:kb:marco-legal-gores |
| Terminologia, definiciones, glosario | urn:gn:kb:glosario-gore-nuble |
| Rendiciones, control CGR, transparencia | urn:gn:kb:gestion-rendiciones |
| Estrategia de gestion, planificacion | urn:gn:kb:estrategia-gestion |
| Cuentas publicas, rendicion de gestion | urn:gn:kb:cuentas-publicas-2021-2024 |
