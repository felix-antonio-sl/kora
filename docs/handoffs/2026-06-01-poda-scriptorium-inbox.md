---
_manifest:
  urn: "urn:kora:kb:poda-scriptorium-inbox-2026-06-01"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-01"
    source: "Handoff del saneamiento de material crudo versionado en _SCRIPTORIUM/INBOX."
version: "1.0.0"
status: publicado
tags: [saneamiento, scriptorium, inbox, raw-sources, context-hygiene]
lang: es
extensions:
  kora:
    family: note
---

# Poda _SCRIPTORIUM/INBOX 2026-06-01

## Estado

Se ejecuto el primer recorte seguro de KORA para reducir contexto y peso sin
perder capacidad productiva:

- `artifacts/knowledge/_SCRIPTORIUM/INBOX/` deja de ser bodega versionada de
  corpus crudo.
- 343 archivos crudos versionados fueron retirados del repo.
- La copia completa previa al retiro quedo preservada localmente en
  `/home/felix/kora-external-sources/2026-06-01-scriptorium-inbox/`.
- El repo conserva `README.md` y `source-inventory-2026-06-01.tsv` como
  trazabilidad minima.

## Decisiones

- No se tocaron artefactos productivos bajo `artifacts/knowledge/{ns}/`,
  `artifacts/agents/{ns}/` ni `artifacts/skills/{ns}/`.
- La politica queda declarada en `CLAUDE.md`, `serialization/knowledge-spec.md`
  y `artifacts/knowledge/_SCRIPTORIUM/INBOX/README.md`.
- `.gitignore` bloquea nuevos crudos bajo `_SCRIPTORIUM/INBOX/**` y permite
  solo README e inventarios.
- No se retiro todavia `_FRAGUA/INBOX`, `_FRAGUA/_archivo` ni
  `_TALLER/INBOX`: contienen artefactos agenticos/skills con semantica no
  promovida. Sacarlos requiere una auditoria de promocion/retiro por URN, no
  una poda mecanica.
- `docs/generated/` y `.claude/trace/` ya estaban fuera del control de version;
  no requirieron cambios de politica.

## Artefactos relevantes

- `.gitignore`
- `CLAUDE.md`
- `serialization/knowledge-spec.md`
- `artifacts/knowledge/_SCRIPTORIUM/INBOX/README.md`
- `artifacts/knowledge/_SCRIPTORIUM/INBOX/source-inventory-2026-06-01.tsv`

## Verificacion

Ejecutado antes del commit:

```bash
git diff --check
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora kb-graph --json --orphans
python3 -m unittest discover -s tests
```

Resultados:

- `git diff --check`: OK.
- `index`: 644 artefactos indexados.
- `check --strict`: 34/34 OK.
- `kb-graph`: 601 nodos, 995 aristas, 0 huerfanos, 0 broken edges.
- `unittest`: 336 tests OK en 274.283s.

## Pendientes

- Auditar `_FRAGUA/INBOX`, `_FRAGUA/_archivo` y `_TALLER/INBOX` con criterio
  semantico: promover lo vivo, retirar lo obsoleto y solo despues externalizar
  o eliminar staging restante.
- Decidir si la copia externa local debe moverse a almacenamiento remoto o
  backup institucional.
- Si se requiere reproducibilidad fuera del host primary, sustituir rutas
  locales del inventario por URI de almacenamiento compartido.

## Prompt de continuacion

Retomar desde `docs/handoffs/2026-06-01-poda-scriptorium-inbox.md`. Verificar
que `master` siga limpio y sincronizado. Siguiente corte recomendado: auditar
staging agentico (`_FRAGUA`/`_TALLER`) por promocion, retiro o externalizacion,
sin tocar productivos ni specs congeladas.
