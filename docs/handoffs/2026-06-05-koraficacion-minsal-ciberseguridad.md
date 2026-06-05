---
_manifest:
  urn: "urn:kora:kb:handoff-2026-06-05-koraficacion-minsal-ciberseguridad"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-05"
    source: "Cierre operativo: koraficacion completa del corpus SGSI MINSAL Chile"
version: "1.0.0"
status: publicado
tags: [handoff, koraficacion, minsal, ciberseguridad, sgsi, conocimiento]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-06-05 — Koraficacion corpus SGSI MINSAL

## Que se hizo

Koraficacion completa del corpus normativo SGSI del Ministerio de Salud de Chile
(~1.2 MB fuente -> ~460 KB salida, CR ~2.6 global, FS=100%).

## Artefactos generados

| Familia | Cantidad | Ubicacion |
|---------|----------|-----------|
| Instructivos | 6 | `artifacts/knowledge/salud/ciberseguridad-minsal/instructivos/` |
| Procedimientos | 14 | `artifacts/knowledge/salud/ciberseguridad-minsal/procedimientos/` |
| Politicas | 24 | `artifacts/knowledge/salud/ciberseguridad-minsal/politicas/` |
| Resoluciones | 19 | `artifacts/knowledge/salud/ciberseguridad-minsal/resoluciones/` |
| **Total** | **63** | |

## Fuentes

- `/home/felix/projects/he-hsc/auditorias/minsal-seguridad-info/markdown/instructivos/`
- `/home/felix/projects/he-hsc/auditorias/minsal-seguridad-info/markdown/procedimientos/`
- `/home/felix/projects/he-hsc/auditorias/minsal-seguridad-info/markdown/politica-general/`
- `/home/felix/projects/he-hsc/auditorias/minsal-seguridad-info/markdown/politicas-secundarias/`
- `/home/felix/projects/he-hsc/auditorias/minsal-seguridad-info/markdown/resoluciones/`

Inventarios en `_SCRIPTORIUM/INBOX/minsal-seguridad-info-*/` (no versionados por gitignore).

## Validacion

- `kora check --strict`: 34/34
- `kora lint-md`: 0 issues
- `kb-graph --orphans`: 0 en namespace salud
- Catalogo: 743 artefactos

## Commits

```
20d5972 feat(knowledge): koraficar 20 artefactos MINSAL ciberseguridad — instructivos y procedimientos SGSI
cb9b5a1 feat(knowledge): koraficar 24 politicas MINSAL SGSI — general + 23 secundarias
1ad4c1e feat(knowledge): koraficar 19 resoluciones MINSAL SGSI
```

## Pendientes

- Los --p0x son auto-shards generados por el promote pipeline. Son artefactos validos con shard_root_urn.
- El archivo 09 y 18 de resoluciones son duplicados (mismo SHA256). El 18 se korafico con URN separada (sufijo -716b) para evitar colision.
- Los INBOX con inventarios no se versionan por gitignore; el corpus bruto vive fuera del repo.
