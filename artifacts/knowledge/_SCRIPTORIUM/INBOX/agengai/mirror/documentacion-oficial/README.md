# OpenClaw Documentacion Oficial

Este directorio es un mirror mantenido desde la documentacion oficial de OpenClaw.

- Upstream git: `https://github.com/openclaw/openclaw.git`
- Clone local operativo: configurable con `KORA_OPENCLAW_SOURCE_REPO`
- Raiz espejada: `docs/`
- Politica: copia casi 1:1, sin frontmatter KORA por archivo

El objetivo aqui no es transmutar ni reinterpretar el corpus, sino mantener una copia versionada y navegable dentro de KORA.

## Operacion

### Sincronizacion automatica (desde 2026-03-17)

El mirror se actualiza automaticamente cada vez que se hace `git pull` en el clone local upstream, mediante un hook `post-merge` en `_workspaces/openclaw/.git/hooks/post-merge`.

No se requiere intervencion manual salvo que se reclone el repo upstream (ver la documentacion operativa del hook local para reinstalarlo).

### Sincronizacion manual

```bash
python3 toolchain/sync_openclaw_docs_mirror.py --source-repo ~/Developer/_workspaces/openclaw
```

Dry run:

```bash
python3 toolchain/sync_openclaw_docs_mirror.py --dry-run --source-repo ~/Developer/_workspaces/openclaw
```

Los metadatos de sincronizacion viven en `_mirror.yml` dentro de este directorio.

## Alcance

- Se preserva la estructura original de `openclaw/docs`.
- Se excluye solo ruido minimo (`.DS_Store`).
- `manual-openclaw/` sigue siendo un corpus separado y curado.
