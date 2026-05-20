---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-19-portabilidad-asegurada"
  provenance:
    created_by: "Claude Opus 4.7 (encarnando cat-thinking)"
    created_at: "2026-04-19"
    source: "Memoria operativa compacta del bloque de portabilidad asegurada."
version: "1.0.0"
status: publicado
tags: [operational-memory, snapshot, portabilidad, ci, check]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-portabilidad-asegurada"
    - "urn:kora:kb:next-session-prompt-2026-04-19-portabilidad-asegurada"
---

# Memoria operativa — portabilidad asegurada

Snapshot operativo al cierre del bloque de portabilidad, posterior al cierre
estructural de la sesion `2026-04-19`.

## Snapshot numerico

| Metrica | Valor | Comando |
|---------|-------|---------|
| Checks registry | 17 | `python3 toolchain/kora check --strict` |
| Suite unittest | 299 (`skipped=2`) | `python3 -m unittest discover -s tests` |
| Nodos KB | 521 | `python3 toolchain/kora kb-graph --json --orphans` |
| Aristas KB | 654 | `python3 toolchain/kora kb-graph --json --orphans` |
| Huerfanos reales KB | 0 | `python3 toolchain/kora kb-graph --json --orphans` |
| Aristas rotas KB | 0 | `python3 toolchain/kora kb-graph --json --orphans` |
| Scripts arqueologicos | 4 nuevos en `legacy_migration/` | — |
| CI workflows | 1 (`ci.yml`) | — |
| OS soportados | Linux + macOS | CLAUDE.md §Portabilidad |
| Python target | >= 3.11 (probado 3.12) | `requirements.txt`, `toolchain/kora` |

## Mecanismos instalados

### Check

- `portabilidad-tests` (medium, lint) — registry de 16 a 17.
- Escanea `tests/` y `toolchain/`; excluye `toolchain/legacy_migration/`.
- Respeta `# portable-exempt` y salta contenido de triple-quoted strings.

### Helpers

- `tests/common.py` — `canonical_path(p)`, `assert_path_in_output(tc, out, p)`.
- El normalizador canonico kappa que colapsa `/var/folders/...` →
  `/private/var/folders/...` en macOS.

### CI

- `.github/workflows/ci.yml` — matrix `[ubuntu-latest, macos-latest]` × 3.12.
- Pasos: `kora index`, `kora check --strict`, `unittest`, kb-graph clean.
- Trigger: push/pr a master; `fail-fast: false`.

### Runtime guard

- `toolchain/kora` aborta con exit 2 si Python < 3.11.

### Politica

- `CLAUDE.md` §Portabilidad con alcance, mecanismos, regla kappa, escape hatch.

## Invariantes duras

1. Todo test que compare output CLI con path debe usar
   `assert_path_in_output` o aplicar `canonical_path` manualmente.
2. Todo path literal `/tmp/`, `/Users/`, `/home/`, `/var/folders/`,
   `/private/var/` en `tests/` o `toolchain/` (fuera de `legacy_migration/`)
   rompe el strict salvo `# portable-exempt`.
3. `legacy_migration/` es subarbol arqueologico — no agregar codigo nuevo
   ahi, no tomar sus scripts como referencia.
4. Windows no es target. No hay fallback prometido.
5. Python < 3.11 no es target.

## Higiene de trabajo

1. `artifacts/knowledge/fxsl/opm/opm-ssot-es/*` sigue con drift ajeno NO
   commiteado; no mezclar con cambios de toolchain/specs.
2. Los handoffs de esta sesion y los regenerados `docs/generated/*` son
   consecuencia legitima del check nuevo (17 vs 16) — commit separado.
3. El check `portabilidad-tests` deberia aparecer en `catalog.yml`,
   `fxsl-cat-ledger`, `operating-core-contracts`, `repo-stats`; todos son
   regeneracion por `kora sync-docs`.

## Siguiente bloque recomendado

1. `168 CM-*` embebidos en productivos (`promover / absorber / descartar`).
2. Promotion backlog en `_FRAGUA/INBOX/` (21) y `_TALLER/INBOX/` (7).
3. Menores `H9/H17/H20/H22`.
