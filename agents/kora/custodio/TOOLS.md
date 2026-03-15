---
_manifest:
  urn: "urn:kora:agent-bootstrap:custodio-tools:1.0.0"
  type: "bootstrap_tools"
---

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema y resolver URN antes de acceder KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Agent spec, 5 componentes, FSM, segregacion, co-induccion | urn:kora:kb:agent-spec-md |
| Gobernanza, precedencia, meta-reglas, URN bootstrap | urn:kora:kb:gobernanza |
| Formato descriptivo, koraficacion, md-spec | urn:kora:kb:md-spec |
| Formato prescriptivo, cristalizacion, RFC 2119, spec-md | urn:kora:kb:spec-md |

## repo_health

- **Firma:** () → {broken_urns: string[], validation_errors: string[], stats: {artifacts, agents, namespaces, skills}}
- **Cuando usar:** Diagnostico completo del estado del repo cuando se requiere vision consolidada de salud estructural.
- **Cuando NO usar:** Si solo se necesita una metrica especifica (usar comando individual).
- **Notas:** Consolida salud estructural, conformidad y metricas del repositorio en un solo chequeo operacional.

## catalog_sync

- **Firma:** () → {new_entries: int, updated: int, removed: int, total: int}
- **Cuando usar:** Reconstruir catalogo desde artefactos del repo cuando se sospecha drift o despues de cambios estructurales.
- **Cuando NO usar:** Si el catalogo ya esta sincronizado en esta sesion.
- **Notas:** Recalcula el estado publicado del catalogo y detecta drift entre artefactos y entradas catalogadas.

## urn_resolve

- **Firma:** urn: string → path: string | null
- **Cuando usar:** Verificar que una URN resuelve a un archivo existente durante diagnostico o reparacion.
- **Cuando NO usar:** Datos ya en contexto.
- **Notas:** Debe responder con una ruta resoluble o explicitar que la referencia esta rota.

## intake_pipeline

- **Firma:** () → {inbox_count: int, source_count: int, drafts_count: int, knowledge_count: int}
- **Cuando usar:** Consultar status del pipeline de ingesta y detectar atascos o pendientes.
- **Cuando NO usar:** Si el status ya fue consultado en este turno.
- **Notas:** Expone el estado agregado del pipeline de ingesta y sus atascos visibles.

## git_status

- **Firma:** () → {branch: string, clean: bool, uncommitted: string[], recent_commits: string[]}
- **Cuando usar:** Diagnosticar estado del repositorio git y contexto reciente de cambios.
- **Cuando NO usar:** Si git status ya fue consultado en este turno.
- **Notas:** Resume limpieza del worktree y contexto reciente de cambios sin exponer plumbing adicional.

## filesystem_scan

- **Firma:** path: string → {dirs: string[], files: string[], orphans: string[]}
- **Cuando usar:** Escanear estructura de un directorio para verificar topologia y detectar anomalias.
- **Cuando NO usar:** Si la estructura ya fue leida en este turno.
- **Notas:** Devuelve topologia observable y anomalias estructurales de la ruta auditada.

## file_write

- **Firma:** {path: string, content: string} → {success: bool, action: string}
- **Cuando usar:** Escritura quirurgica de un archivo especifico durante reparacion acotada.
- **Cuando NO usar:** Escrituras masivas o refactoring que requieren planificacion previa.
- **Notas:** Escritor quirurgico para cambios acotados y verificables dentro del envelope operativo del agente.
