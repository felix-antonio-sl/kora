---
_manifest:
  urn: urn:kora:skill:custodio-catalog-steward:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CATALOG-STEWARD

## Proposito
Gestiona el catalogo maestro del repo KORA a traves de la interfaz semantica del workspace: sincroniza, detecta URNs rotas y resuelve referencias.

## Input/Output
- **Input:** accion: enum(sync|health|resolve), urn_target: string | null (si accion=resolve)
- **Output:** CatalogReport (ver Signature Output)

## Procedimiento
1. Invocar `catalog_sync` para reconstruir el catalogo desde los artefactos del repo.
2. Capturar resultado: entradas nuevas, actualizadas, eliminadas y total publicado.
3. Invocar `repo_health` para detectar URNs rotas post-sincronizacion.
4. Si hay URNs rotas: listar con ruta esperada vs ruta real y clasificar causa (archivo movido, eliminado, renombrado, typo).
5. Proponer fix para cada URN rota. Esperar aprobacion antes de ejecutar.
6. Si se solicita resolver una URN especifica: invocar `urn_resolve`.
7. Reporte final: tabla con estado del catalogo.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| sincronizado | bool | Catalogo sincronizado sin errores |
| nuevas | int | Entradas nuevas agregadas |
| actualizadas | int | Entradas actualizadas |
| eliminadas | int | Entradas eliminadas |
| rotas | {urn, causa, fix_propuesto}[] | URNs rotas con diagnostico |
