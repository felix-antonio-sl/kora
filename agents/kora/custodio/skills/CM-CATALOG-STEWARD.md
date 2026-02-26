---
_manifest:
  urn: "urn:kora:skill:custodio-catalog-steward:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CATALOG-STEWARD

## Proposito
Gestiona el catalogo maestro del repo KORA: sincroniza, detecta URNs rotas, resuelve referencias.

## I/O

- **Input:** accion: enum(sync|health|resolve), urn_target: string | null (si accion=resolve)
- **Output:** CatalogReport (ver Signature Output)

## Procedimiento
1. Ejecutar `scripts/kora index` → reconstruir catalog_master_kora.yml desde artefactos.
2. Capturar output: entradas nuevas, actualizadas, eliminadas.
3. Ejecutar `scripts/kora health` → detectar URNs rotas post-indexacion.
4. Si hay URNs rotas: listar con ruta esperada vs ruta real. Clasificar causa (archivo movido, eliminado, renombrado, typo).
5. Proponer fix para cada URN rota. Esperar aprobacion antes de ejecutar.
6. Si se solicita resolver URN especifica: ejecutar `scripts/kora resolve "{urn}"`.
7. Reporte final: tabla con estado del catalogo.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| sincronizado | bool | Catalogo sincronizado sin errores |
| nuevas | int | Entradas nuevas agregadas |
| actualizadas | int | Entradas actualizadas |
| eliminadas | int | Entradas eliminadas |
| rotas | {urn, causa, fix_propuesto}[] | URNs rotas con diagnostico |
