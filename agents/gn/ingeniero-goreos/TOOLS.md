---
_manifest:
  urn: "urn:gn:agent-bootstrap:ingeniero-goreos-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path. catalog_master_kora.yml = SOURCE_OF_TRUTH.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** Federacion multi-catalogo: catalog_master_kora.yml cubre todos los namespaces.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema -> resolver URN -> priorizar KB. Detectar dominio consulta y enrutar al namespace apropiado.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic / Domain | URN |
|----------------|-----|
| **GORE_OS** | |
| Blueprint, dominios, vision | Leer /Users/felixsanhueza/Developer/goreos/docs/blueprint/* |
| Stack, arquitectura | Leer /Users/felixsanhueza/Developer/goreos/stack.md |
| **GORENUBLE** | |
| Estructura GORE, organigrama | urn:gn:kb:intro-gores-nuble |
| Organigrama, divisiones, departamentos | urn:gn:kb:organigrama |
| LOC 19.175, competencias | urn:gn:kb:loc-gore |
| Presupuesto, FNDR, FRPD | urn:gn:kb:gestion-prpto |
| IPR, inversion, proyectos | urn:gn:kb:gestion-ipr |
| Matriz integracion | urn:gn:kb:matriz-integracion-organica |
| ERD, ejes estrategicos | urn:gn:kb:erd-nuble-2024-2030 |
| Flujos aprobacion | urn:gn:kb:flujos-aprobacion-documentos |
| **TDE** | |
| Ley 21.180, procedimientos electronicos | urn:tde:kb:ley-21180 |
| Ley 19.880, LBPA | urn:tde:kb:ley-19880 |
| Expediente electronico, DS 10 | urn:tde:kb:nt-documentos-expedientes |
| Interoperabilidad, PISEE | urn:tde:kb:nt-interoperabilidad |
| Seguridad, ciberseguridad | urn:tde:kb:nt-seguridad-ciberseguridad |
| ClaveUnica | urn:tde:kb:claveunica |
| SIMPLE | urn:tde:kb:simple-saas |
| DocDigital | urn:tde:kb:docdigital |
| CPAT, madurez | urn:tde:kb:cpat-completa |
| **ORKO** | |
| Axiomas, primitivos P1-P5 | urn:orko:kb:orko-fundamentos |
| Arquitectura ORKO | urn:orko:kb:orko-arquitectura |
| Metodologia ORKO | urn:orko:kb:orko-metodologia |

- **Domain Detection Keywords:**

| Domain | Keywords | State |
|--------|----------|-------|
| GORE | GORE, Nuble, FNDR, FRPD, division, departamento, IPR, rendicion, convenio, LOC, 19.175, presupuesto regional, CORE, gobernador, organigrama | S-GORE-KNOWLEDGE |
| TDE | TDE, 21.180, ClaveUnica, SIMPLE, DocDigital, expediente electronico, interoperabilidad, PISEE, norma tecnica, decreto 7/10/12, CPAT, transformacion digital | S-TDE-KNOWLEDGE |
| METODOLOGIA | categoria, functor, composicion, IFML, C4, user story, test, tipo, morfismo, Effect | S-CONSULTANT |

## file_read

- **Firma:** path: string -> content: string
- **Cuando usar:** Leer archivos del proyecto GORE_OS (blueprint, arquitectura, codigo fuente).
- **Cuando NO usar:** Archivos fuera del proyecto GORE_OS.

## file_write

- **Firma:** path: string, content: string -> success: boolean
- **Cuando usar:** Crear o modificar archivos del proyecto GORE_OS (modelos, rutas, templates, tests).
- **Cuando NO usar:** Archivos fuera del proyecto GORE_OS. Archivos de configuracion sensible.

## web_search

- **Firma:** query: string -> results: SearchResult[]
- **Cuando usar:** Documentacion de frameworks (Flask, SQLAlchemy, HTMX), sintaxis versiones recientes, mejores practicas.
- **Cuando NO usar:** Temas cubiertos por KB. KB siempre tiene prioridad.
