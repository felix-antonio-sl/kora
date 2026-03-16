# OpenClaw Documentacion Oficial

Este directorio es un mirror mantenido desde la documentacion oficial de OpenClaw.

- Upstream git: `https://github.com/openclaw/openclaw.git`
- Clone local operativo: `/Users/felixsanhueza/Developer/_workspaces/openclaw`
- Raiz espejada: `docs/`
- Politica: copia casi 1:1, sin frontmatter KORA por archivo

El objetivo aqui no es transmutar ni reinterpretar el corpus, sino mantener una copia versionada y navegable dentro de KORA.

## Operacion

Sincronizar el mirror:

```bash
python3 scripts/sync_openclaw_docs_mirror.py
```

Dry run:

```bash
python3 scripts/sync_openclaw_docs_mirror.py --dry-run
```

Los metadatos de sincronizacion viven en [`_mirror.yml`](/Users/felixsanhueza/Developer/kora/KNOWLEDGE/agengai/openclaw/documentacion-oficial/_mirror.yml).

## Alcance

- Se preserva la estructura original de `openclaw/docs`.
- Se excluye solo ruido minimo (`.DS_Store`).
- `manual-openclaw/` sigue siendo un corpus separado y curado.
