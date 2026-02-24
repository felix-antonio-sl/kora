---
_manifest:
  urn: "urn:kora:agent-bootstrap:custodio-tools:1.0.0"
  type: "bootstrap_tools"
---

## repo_health

- **Firma:** () → {broken_urns: string[], validation_errors: string[], stats: {artifacts, agents, namespaces, skills}}
- **Cuando usar:** S-SALUD, S-AUDITORIA. Diagnostico completo del estado del repo.
- **Cuando NO usar:** Si solo se necesita una metrica especifica (usar comando individual).
- **Implementacion:** Ejecutar `scripts/kora health` + `scripts/kora validate` + `scripts/kora stats` secuencialmente.

## catalog_sync

- **Firma:** () → {new_entries: int, updated: int, removed: int, total: int}
- **Cuando usar:** S-CATALOGO. Reconstruir catalogo desde artefactos del repo.
- **Cuando NO usar:** Si el catalogo ya esta sincronizado en esta sesion.
- **Implementacion:** Ejecutar `scripts/kora index`.

## urn_resolve

- **Firma:** urn: string → path: string | null
- **Cuando usar:** S-CATALOGO, S-CIRUGIA. Verificar que una URN resuelve a un archivo existente.
- **Cuando NO usar:** Datos ya en contexto.
- **Implementacion:** Ejecutar `scripts/kora resolve "{urn}"`.

## intake_pipeline

- **Firma:** () → {inbox_count: int, source_count: int, drafts_count: int, knowledge_count: int}
- **Cuando usar:** S-INGESTA. Status del pipeline de ingesta.
- **Cuando NO usar:** Si el status ya fue consultado en este turno.
- **Implementacion:** Ejecutar `scripts/kora intake`.

## git_status

- **Firma:** () → {branch: string, clean: bool, uncommitted: string[], recent_commits: string[]}
- **Cuando usar:** S-SALUD, S-AUDITORIA. Estado del repositorio git.
- **Cuando NO usar:** Si git status ya fue consultado en este turno.
- **Implementacion:** Ejecutar `git status` + `git log --oneline -5`.

## filesystem_scan

- **Firma:** path: string → {dirs: string[], files: string[], orphans: string[]}
- **Cuando usar:** S-AUDITORIA. Escanear estructura de un directorio.
- **Cuando NO usar:** Si la estructura ya fue leida en este turno.
- **Implementacion:** Listar recursivamente el path con deteccion de anomalias.

## file_write

- **Firma:** {path: string, content: string} → {success: bool, action: string}
- **Cuando usar:** S-CIRUGIA. Escritura quirurgica de un archivo especifico.
- **Cuando NO usar:** Escrituras masivas o refactoring (→ S-EVOLUCION con plan).
- **Notas:** SIEMPRE requiere confirmacion del usuario antes de ejecutar.
