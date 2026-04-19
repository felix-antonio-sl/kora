---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-19-portabilidad-asegurada"
  provenance:
    created_by: "Claude Opus 4.7 (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Cierre del bloque de portabilidad: mecanismos de aseguramiento Linux x macOS instalados sobre el cierre estructural previo."
version: "1.0.0"
status: publicado
tags: [handoff, portabilidad, ci, check, arquitecto-categorico]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-cierre-estructural-post-reorg-v5"
    - "urn:kora:kb:operational-memory-2026-04-19-portabilidad-asegurada"
  refines:
    - "urn:kora:kb:handoff-2026-04-19-cierre-estructural-post-reorg-v5"
---

# Handoff explicito — portabilidad asegurada por mecanismos

## Resumen ejecutivo

La sesion del **19 de abril de 2026** (segundo bloque, posterior al cierre
estructural) instala los mecanismos que convierten la portabilidad de KORA
de conjetura a invariante verificable en CI.

Motivacion inmediata: el test `test_promote_atomic_accepts_explicit_review_override`
fallaba en macOS por comparar paths de `tempfile.TemporaryDirectory()` sin
aplicar `Path.resolve()` (symlink `/var/folders/...` → `/private/var/folders/...`).
El fix puntual estaba disponible — pero hacerlo sin mecanismo hubiera dejado
la deuda abierta: ningun sistema aseguraba que un bug analogo no reaparezca.

Esta sesion resuelve el problema como invariante, no como parche.

## Lectura categorica

Una asercion `output == expected` donde `output` depende del entorno solo
es functorial si existe un normalizador canonico

    kappa : OutputC -> CanonicalC

que colapse los isomorfismos de plataforma (symlinks, line endings, case
sensitivity). Portabilidad = existencia y uso consistente de `kappa` en
todo borde entorno ↔ test.

El bug del atomize fue romper la naturalidad comparando representaciones no
canonicas. El mecanismo correcto: toda comparacion de output externo debe
factorizar por el normalizador.

## Cambios consolidados

### 1. Nivel 1 — higiene canonica en codigo

**Helpers en `tests/common.py`** (el normalizador kappa):

- `canonical_path(p)` — aplica `Path.resolve()` y devuelve str; idempotente
  en Linux, colapsa `/var/folders/...` en macOS.
- `assert_path_in_output(test_case, output, path, msg=None)` — reemplazo
  canonico del anti-patron `assertIn(str(path), output)`.

**Remediacion de anti-patrones** (5 sitios reales + 1 previo):

- `tests/test_atomize.py:735` — ya arreglado en sesion previa; ahora usa
  `assert_path_in_output` para consistencia.
- `tests/test_atomize.py:55, 67, 369` — `/tmp/fuente.md` en heredocs de
  fixture reemplazado por `./fuente.md` (path neutro).
- `tests/test_atomize.py:391` — `source_corpus: /tmp/fuente.md` reemplazado
  por `fuente.md`.
- `tests/test_check_pipeline.py:178` — `run_cli("promote", "/tmp/nonexistent.md")`
  reemplazado por path dentro de `tempfile.TemporaryDirectory()`.
- `tests/test_semantic_validation.py:772-775` — `file:///tmp/bar.md` →
  `file:///example/bar.md`.

**Check nuevo `portabilidad-tests`** (severidad medium, phase=lint):

- Ubicado en `toolchain/kora_lib/checks.py`.
- Escanea `tests/` y `toolchain/` buscando patrones `/tmp/`, `/var/folders/`,
  `/Users/`, `/home/`, `/private/var/`.
- Respeta `# portable-exempt` al final de la linea como escape hatch.
- Ignora contenido de docstrings (heuristica de triple-quote toggle).
- Excluye el subarbol `toolchain/legacy_migration/` (scripts one-shot
  historicos, ver siguiente bloque).
- Registry sube de **16 a 17 checks**.

**4 scripts one-shot movidos a `toolchain/legacy_migration/`**:

- `analyze_hd_routes.py` — analisis HDOS enero–marzo 2026 (ejecutado).
- `migrate_to_agentfile.py` — migracion 5-file → AGENT.md (ejecutado; los 7
  productivos ya estan en `autoria-spec v1.0`).
- `migrate_hodom_to_ideal.py` + `generate_hodom_ideal_workbook.py` —
  migracion workbook HODOM 2025 (ejecutado; directorios de trabajo
  `output/spreadsheet/` y `tmp/` ya no existen).

Ninguno era importado por codigo productivo. `toolchain/legacy_migration/README.md`
incorpora la seccion con los 4 archivos incorporados y la nota explicita
de exclusion del check de portabilidad.

### 2. Nivel 2 — aseguramiento estructural

**CI matrix en `.github/workflows/ci.yml`**:

- Jobs: `kora-verify` en `ubuntu-latest` y `macos-latest`, `fail-fast: false`.
- Python: `3.12`.
- Pasos: setup-python, install requirements, `kora index`, `kora check --strict`,
  `unittest discover -s tests`, verificacion `kb-graph` (orphans_real=0,
  broken_edges=0).
- Trigger: `push` a `master`, `pull_request` a `master`.

Sin este workflow la portabilidad sigue siendo conjetura. Con el workflow,
cada PR queda observable en ambos OS antes de merge.

**Pin de Python y entorno**:

- `requirements.txt` — header documentado: Python ≥3.11 (probado en 3.12 y 3.13),
  OS Linux + macOS, Windows fuera de alcance (WSL best-effort).
- `.python-version` — `3.12` (respetado por pyenv y herramientas compatibles).
- `toolchain/kora` — runtime guard: exit 2 con mensaje claro si detecta
  Python < 3.11.

### 3. Politica formal en `CLAUDE.md`

Nueva seccion `## Portabilidad` entre `## Notas practicas` y `## Estado del
fleet`. Contenido:

- Alcance oficial (Linux + macOS, Python ≥3.11).
- 4 mecanismos de aseguramiento (CI, check, helpers, runtime guard).
- Regla para tests: toda asercion que compare output CLI con path
  construido debe pasar por `assert_path_in_output`.
- Escape hatch `# portable-exempt` con uso restringido.

## Estado estable resultante

Comandos corridos en la sesion:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```

Resultado verificado:

- `check --strict`: `Checks run: 17`, `Passed: 17`, `Failed: 0`
- `unittest`: `Ran 299 tests`, `OK (skipped=2)`
- `kb-graph`: `Nodes 521`, `Edges 654`, `Orphans real 0`, `Broken edges 0`

## Invariantes para la proxima sesion

1. Un PR que introduzca paths literales no portables en `tests/` o
   `toolchain/` (fuera de `legacy_migration/`) falla en `check --strict`.
2. Un PR que rompa en macOS queda expuesto por la matriz CI antes de merge.
3. Un PR que asuma Python < 3.11 falla al primer `kora` en ambos OS.
4. Los scripts arqueologicos siguen vivos en `legacy_migration/` pero no
   contaminan la superficie activa del toolchain.
5. La regla kappa (normalizador canonico de paths) es la unica forma
   aceptable de comparar path construido contra output CLI.

## Pipeline minimo de retoma

```bash
cd /home/felix/kora
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```

Si cualquiera deja de coincidir con este handoff, diagnosticar drift antes
de tocar. Orden de diagnostico:

1. `git status` — verificar si hay residuos de otra sesion (por ejemplo un
   directorio `AGENTS/` residual como le paso al colega la sesion anterior).
2. `git log --oneline -10` — confirmar HEAD.
3. Correr el test especifico que falla con `-v`.

## Siguiente frente recomendado

Con portabilidad asegurada y cierre estructural cerrado, el siguiente
trabajo de mayor retorno sigue siendo **deuda de artefactos**:

1. `H2-artifacts`: clasificar los `168 CM-*` embebidos en productivos en
   `promover / absorber / descartar`.
2. Promocion de staging: `21` agentes en `_FRAGUA/INBOX/` y `7` skills en
   `_TALLER/INBOX/`.
3. Menores diferibles: `H9`, `H17`, `H20`, `H22`.
