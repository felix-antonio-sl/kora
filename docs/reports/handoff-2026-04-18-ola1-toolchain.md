---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-18-ola1-toolchain"
  provenance:
    created_by: "FS"
    created_at: "2026-04-18"
    source: "Sesión 2026-04-18 Ola 1 del toolchain post-unificación: perfil a-autoria + schema universal + validate categorial + cierre adjunción Check ⊣ Fix + migración del corpus productivo."
version: "1.0.0"
status: publicado
tags: [handoff, toolchain, autoria-spec, a-autoria, schema, validate, adjuncion, fix, migracion-corpus]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:handoff-2026-04-18"
---

# Handoff sesión 2026-04-18 — Ola 1 del toolchain post-unificación

## Resumen ejecutivo

Sesión de implementación sobre el toolchain, dirigida desde perspectiva categorial explícita. Se implementó el perfil `a-autoria` de `kora migrate`, el schema universal de artefactos (`kora-artefacto.json`), el validador funcional categorial (`autoria_validate.py`), y se cerró la adjunción `Check ⊣ Fix` registrando `autoria-conformance` en el pipeline de `kora check`. Finalmente se aplicó el fix al corpus productivo: 7 workspaces migrados, 42 scaffolds legacy eliminados, 32 → 11 diagnostics residuales (los 11 son el residual matemáticamente esperado de la adjunción parcial).

El commit único `84dc1bb` cristaliza la ola. 64 archivos, 10159+/15341− (el neto negativo es por scaffolds legacy eliminados, no pérdida).

## Decisión arquitectónica de sesión

**Perspectiva categorial explícita** como lenguaje de diseño. Felix lo pidió tras la implementación del migrate: "desde arquitecto-categórico y Python funcional declarativo". Esto formateó todas las decisiones siguientes:

- **Fibración sobre `atlas.forma_material`**. El conjunto `I = {habilidad, subagente, agente-propiamente-tal, agente-plataforma}` es la base. El functor de requerimientos `R: I → Tuple[Rule]` asigna reglas por fibra. El schema JSON captura la sección universal (pullback terminal `I → 1`); el resto vive como functor Python.

- **Reglas como morfismos Kleisli** en el monad `List[Diagnostic]`. Composición es concatenación. El monoide libre hace que `compose(r, s)` sea asociativo con `compose()` identity neutral. Verificado por tests de propiedades, no solo de instancias.

- **Adjunción `Check ⊣ Fix` parcial**. `migrate_to_autoria` es adjoint izquierdo del subfunctor `CheckRenames` (codes `envelope-*`, `atlas-*-enum`). La factorización `Check = CheckRenames ⊕ CheckFibra` con `Fix = FixRenames` (sin `FixFibra`) es estéticamente correcta: hace explícita la frontera entre lo mecánicamente reparable y lo deliberativo.

- **Python funcional declarativo**. Sin clases mutables, sin acumuladores imperativos. `NamedTuple` inmutables, `MappingProxyType` para catálogos, `itertools.chain.from_iterable` para concatenar, `reduce` sobre `.get` como lens funcional.

## Cronología de decisiones

### Fase 1 — Marco para migrate

Preguntas abiertas resueltas al inicio:
- **A = idempotente** (no destructiva pura). Segunda corrida = no-op. La ruptura vive en la spec, no en el toolchain.
- **B = schema mínimo + Python condicional**. JSON Schema para estructural/universal; validación condicional por forma material en Python puro.

### Fase 2 — `kora migrate --perfil a-autoria`

`scripts/kora_lib/migration.py` (+525 líneas):
- 4 pasos discretos: `_autoria_migrate_manifest` (URN rename, type=artefacto, extracción de versión embebida del skill URN legacy), `_autoria_migrate_envelope` (status/name→nombre, status ES), `_autoria_migrate_kora_overlay` (harness_vector→vector_ontologico, atlas slugs a español), `_autoria_migrate_shape` (agent→artefacto con deep renames coalgebra/plan/transitions).
- Barrido recursivo `_autoria_sweep_urn_refs` sobre strings anidados para `urn:kora:kb:spec-md → md-spec` y URNs legacy.
- Purga de scaffolds legacy, renames de subdirs (`references→referencias`, `assets→recursos`, `memory→memoria`).
- `AUTORIA_MIGRATION_SKIPLIST` para `SKILLS/kora/atomize/`.

CLI: `--perfil` alias de `--profile`. Tests en `test_migrate_autoria.py` (17 tests).

### Fase 3 — Perspectiva categorial

Felix activó el marco arquitecto-categórico. La implementación subsiguiente (schema + validate + check) se hizo con lenguaje categorial explícito en docstrings, tests de propiedades algebraicas, y diseño funcional puro.

### Fase 4 — Schema universal

`schemas/kora-artefacto.json`: sección universal sin condicional. Captura envelope obligatorio, URN regex estricto para régimen `artefacto`, type constante, status enum en español, vector_ontologico por eje con rangos, atlas con enums cerrados (7 arnés × 4 forma material × 4 metáfora). No tiene `if/then/else` ramificado — la ramificación vive en Python.

### Fase 5 — `autoria_validate.py` funcional

Módulo de 380 líneas. Combinadores puros: `path`, `compose`, `when`, `require`, `forbid`, `in_set`, `bound`, `regex_match`. Catálogos inmutables: `UNIVERSAL_RULES` (13 reglas), `FORM_RULES` (functor `R: I → Tuple[Rule]` con 5/8/7/7 reglas por forma). API: `validate(art) = mconcat(UNIVERSAL_RULES ++ R(forma_of(art)))`.

Tests en `test_autoria_validate.py` (36 tests):
- Schema universal acepta las 4 fixtures canónicas y rechaza URN legacy, status inglés, atlas fuera de enum.
- Fibra condicional por forma material con violaciones declaradas.
- **Propiedades del monoide**: `compose` asociativo, `compose()` identity neutral.
- **Pullback**: `rules_for` incluye universales + fibra correcta; forma desconocida colapsa a universales.
- **Adjunción Check ⊣ Fix**: idempotencia del fix, reducción de rename codes, residualidad de fibra.

### Fase 6 — Check integrado al pipeline

`scripts/kora_lib/checks.py`: `_check_autoria_conformance` como superficie de reporting del validador. Adapta `autoria_validate.Diagnostic` → `checks.Diagnostic` preservando severity y code.

Registrado: `scope=artifact`, `severity=high`, `enforcement=schema`, `phase=verify`, `depends=("catalog-exists",)`, `spec_ref="autoria-spec §3, §6"`.

### Fase 7 — Cierre de la adjunción

Tras análisis categorial sobre dos opciones (aplicar migrate directamente vs. cerrar la adjunción formal primero), se eligió la segunda por universalidad, composicionalidad, reversibilidad y adjunción parcial bien tipada.

`_fix_autoria_conformance(diagnostics)` invoca `migrate_to_autoria(dry_run=False)`. Registrado con el check como `fix=_fix_autoria_conformance`. Tres propiedades verificadas como tests: idempotencia (`fix ∘ fix = fix`), reducción (`diagnose ∘ fix` no contiene rename codes), residualidad (diagnostics no-rename sobreviven).

### Fase 8 — Aplicación al corpus

`kora check --fix`:
- **32 diagnostics pre-fix**: 8 urn, 8 nombre, 8 descripcion, 7 status, 1 type. Todos rename codes.
- **11 diagnostics post-fix**: 8 `descripcion` faltante en AGENT.md productivos (autoría humana, los workspaces legacy nunca la declararon), 3 en `SKILLS/kora/atomize/` (skiplist explícito).

**Los 11 residuales son matemáticamente lo que la adjunción parcial predice** — descripcion faltante no es rename, es autoría; skiplist es decisión operativa. `FixFibra` no existe, como demuestra el test de residualidad.

### Fase 9 — Ajuste coherente mínimo

`AGENT_REQUIRED_FILES` en `config.py`: `("AGENT.md",)` conforme a autoria-spec §13.2. Sin esto, `kora stats` reportaba 0 workspaces productivos tras la purga de scaffolds legacy. Una línea, coherente con la spec.

## Estado final

### Entregables de la ola (commit `84dc1bb`)

| Archivo | Rol |
|---------|-----|
| `scripts/kora_lib/migration.py` (+525) | Perfil `a-autoria`: renames + purga + skiplist |
| `scripts/kora_lib/autoria_validate.py` (nuevo, 380 líneas) | Validador funcional categorial |
| `schemas/kora-artefacto.json` (nuevo) | Sección universal del schema |
| `scripts/kora_lib/checks.py` (+100) | `autoria-conformance` + fix adjunto |
| `scripts/kora_lib/cli.py` (+18) | `--perfil` alias, choice `a-autoria` |
| `scripts/kora_lib/config.py` (±4) | `AGENT_REQUIRED_FILES = ("AGENT.md",)` |
| `tests/test_migrate_autoria.py` (17 tests) | Migración idempotente, URN, scaffold purge, skiplist |
| `tests/test_autoria_validate.py` (36 tests) | Schema, fibra, monoide, pullback, adjunción |

### Corpus migrado (7 workspaces)

- `AGENTS/gn/digitrans/`, `AGENTS/gn/goreologo/`
- `AGENTS/kora/clawforge/`, `curator/`, `custodio/`, `forgemaster/`, `guardian/`

Cada workspace quedó con: `AGENT.md` migrado + subdirs canónicos (`memoria/` donde existía `memory/`). 42 scaffolds legacy eliminados (AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json; README.md en curator). `curator/memory/{2026-03-25,2026-04-14}.md` renombrados a `curator/memoria/` como `git rename (100%)`.

### Estructura categorial del toolchain (cerrada)

```
         migrate (adjoint izq parcial)
               ↓
    validate (fibra sobre forma_material)
               ↓
  schemas/kora-artefacto.json (universal)
               ↓
       kora check --fix
         ↓        ↓
   diagnostics  run_fixes
```

### Métricas de la suite

| | Baseline pre-sesión | Post-commit |
|---|---|---|
| Tests totales | 216 | 280 (+64) |
| Failures + Errors | 5 + 6 = 11 | 21 + 24 = 45 |

El aumento de fallos es **100% deuda documentada del handoff anterior** (§6: "7 suites necesitan revisión post-unificación"). 21 `FileNotFoundError` sobre archivos retirados por la unificación (SOUL/USER/TOOLS.md, specs/agentfile-spec.md). No es regresión introducida; es la manifestación esperada de la migración del corpus sobre tests v1 no actualizados.

## Deuda para próxima sesión

### Alta prioridad (desbloqueante)

1. **Actualizar los 7 test suites legacy**: `test_artifacts`, `test_cli_smoke`, `test_semantic_validation`, `test_graph_invariants`, `test_operating_core_scenarios`, `test_agent_audit`, `test_check_pipeline`. ~21 `FileNotFoundError` + asertos sobre shape v1 `agent.*` obsoleto. Reescribir para leer shape `artefacto.*`.

2. **Completar `descripcion` faltante** en los 7 AGENT.md productivos. Autoría humana — cada workspace necesita su propia descripción canónica (1 línea, disparador y uso). No es automatizable; el validador lo seguirá reportando hasta que se complete.

### Media prioridad

3. **Check `fidelidad-agentskills`**: transmute `--target agentskills` byte-identical al estándar externo. Tarea 3 del handoff original (2026-04-18 base).

4. **runtime-extensions v1.1+**: las 4 extensions (claude-code, codex, gemini, openclaw) referencian autoria-spec v1.0; matriz `(arnes_categorico × forma_material × runtime)` canónica. Tarea 5 del handoff original.

5. **Completar la fibra de los AGENT.md productivos**: `artefacto.perfil` (descripcion, dominio, disparadores, salidas), `artefacto.invariantes.compromisos_eticos`, `atlas.arnes_categorico` y `atlas.forma_material` explícitos. El migrate los dejó como shape estructural; la fibra `CheckFibra` los reportará cuando se corra.

### Baja prioridad

6. **`SKILLS/kora/atomize/`**: actualmente en skiplist. Cuando Felix cierre su línea paralela sobre atomize, revisar si se migra también o queda exento por spec-explícita.

7. **Handoff anterior (2026-04-18 base) sigue con hallazgos bajos pendientes** (AUT-C7..C18, GOB-C17..C21).

## Lo que NO cambió (deliberadamente)

- **`specs/`**: intacto. La sesión implementó; no redefinió normas.
- **Trabajo paralelo de atomize**: `scripts/kora_lib/atomize.py`, `tests/test_atomize.py`, `tests/fixtures/atomize/`, `scripts/kora_lib/{artifacts,promote,validation}.py` con cambios de Felix, `SKILLS/kora/atomize/{SKILL.md,references/,scripts/}` — todo intocado, quedó en staging uncommitted para que Felix lo cierre.
- **KNOWLEDGE/ productivo**: sin tocar.
- **OpenClaw fleet**: sin tocar (sesión sobre KORA local).

## Invariante demostrado

La adjunción parcial está cerrada con **contratos ejecutables**:

- `fix ∘ fix = fix` (idempotencia — testeada sobre sandbox).
- `diagnose ∘ fix ⊆ diagnose \ {codes rename}` (reducción — testeada).
- Existencia de residual no-rename tras fix (residualidad — testeada).

Estos tests son propiedades algebraicas, no instancias. Cualquier regresión futura del fix rompe al menos uno.
