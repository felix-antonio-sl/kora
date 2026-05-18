---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-18-mejoras-categoriales-1-2-3"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-18"
    source: "Resolucion de los tres problemas categoriales identificados como prioritarios: (1) cerrar adjuncion Check ⊣ Fix, (2) activar verificacion coalgebraica en agentes con FSM real, (3) declarar y enforcear leyes algebraicas de relations."
version: "1.0.0"
status: publicado
tags: [handoff, categorial, adjuncion, coalgebra, relations-laws, knowledge-spec, autoria-conformance]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:handoff-2026-05-18-simplificacion-curacion-agentes-skills"
---

# Handoff sesion 2026-05-18 (parte 2) — Mejoras categoriales 1, 2 y 3

## Resumen ejecutivo

Esta sesion resuelve los tres problemas categoriales priorizados como
**alto retorno / sin tocar specs en freeze**:

1. **Adjuncion `Check ⊣ Fix` cerrada** — el codemod `migrate_to_autoria`
   ahora cubre los 4 codes de envelope que ayer quedaron sin fix
   mecanico.
2. **Verificacion coalgebraica activada** en los 2 agentes productivos
   con FSM real declarado (`urgenciologo`, `salubrista`); termination +
   safety closure ahora son **invariantes verificables** y no solo
   campos opcionales.
3. **Leyes algebraicas de `relations` declaradas y enforced** — cada
   tipo de relacion declara su estructura categorial (poset, DAG,
   relacion libre); nuevo check `relations-laws` detecta ciclos en
   `supersedes`/`refines` y violaciones de antisimetria en `supersedes`.

## Alcance

### Capa serializacion

- **`serialization/knowledge-spec.md` §6.3 (nueva)** — leyes algebraicas
  por tipo de relacion, con tabla de propiedades (aciclica, transitiva,
  antisimetrica) y enforcement asignado por check.
- **`serialization/knowledge-spec.md` §6.4** — renumerada (era §6.3 en
  v2.0.0; conserva semantica).

### Capa toolchain

- **`toolchain/kora_lib/migration.py::_autoria_migrate_manifest`** —
  agrega "envelope hoist": detecta `_manifest.status` y `_manifest.version`,
  los mueve a root, preserva orden idiomatico (`_manifest`, `version`,
  `status`, resto). Politica de conflicto: root prevalece.
- **`toolchain/kora_lib/checks.py`**:
  - `_collect_relation_edges(relation_type)` — helper que itera nodos
    knowledge y extrae edges del tipo solicitado.
  - `_find_cycles(edges)` — DFS three-color para detectar ciclos en
    cualquier grafo dirigido.
  - `_check_relations_laws()` — verifica aciclicidad de `supersedes` y
    `refines`, antisimetria de `supersedes`.
  - Registro: nuevo check `relations-laws` con `spec_ref="knowledge-spec §6.3"`.

### Capa artefacto

- **`artifacts/agents/salud/urgenciologo/AGENT.md`** —
  `extensions.kora.verificacion_coalgebraica: true`. FSM con 13 estados
  pasa termination automaticamente.
- **`artifacts/agents/salud/salubrista/AGENT.md`** —
  `extensions.kora.verificacion_coalgebraica: true`. FSM con 10 estados
  pasa termination automaticamente.

### Capa tests

- **`tests/test_migrate_autoria.py`** — 2 tests nuevos:
  - `test_envelope_hoists_status_and_version_from_manifest` (cobertura
    de la mutacion, idempotencia, politica de conflicto).
  - `test_envelope_hoist_reduces_validator_diagnostics` (cobertura de
    la reduccion: `diagnose ∘ fix` no contiene los codes envelope-*-fuera-de-lugar).
- **`tests/test_check_pipeline.py::TestRelationsLaws`** — 4 tests
  nuevos: ciclos sintetic, no-ciclo en DAG, antisimetria de supersedes,
  ciclo en refines.

## Diseño categorial concreto

### Adjuncion `Check ⊣ Fix`

Antes del refactor, la adjuncion estaba **rota** porque las 4 reglas
nuevas que agregue el 2026-05-17 no tenian camino de reparacion
mecanico. El comentario interno del codigo lo reconocia:
`"FixFibra no existe"`.

Despues del refactor, la adjuncion esta **cerrada para el envelope
completo**:

- **Funtorialidad**: `_autoria_migrate_manifest` muta el dict
  preservando referencia.
- **Idempotencia**: `fix ∘ fix = fix` (verificado por test).
- **Reduccion**: `diagnose ∘ fix` no contiene los 4 codes
  envelope-*-fuera-de-lugar / envelope-*-requerido (verificado por
  test).
- **Politica de conflicto**: `_manifest.k vs root.k` resuelve a root
  (preserva la voluntad del autor sobre la deuda mecanica).

La fibra que aun NO esta cubierta por fix mecanico es la "fibra
condicional por forma material" — esa requiere autor humano y no se
puede mecanizar sin perder semantica.

### Verificacion coalgebraica

`autoria-spec §3.5` declara que un artefacto puede ser tratado como
**coalgebra** (FSM como functor polinomial) con safety closure como
sub-coalgebra cerrada. El check `coalgebra-conformance` verifica
mecanicamente:

1. **FSM bien formado** — estados/inicial/terminales/transiciones
   consistentes.
2. **Termination** — desde el estado inicial, todo camino alcanza un
   terminal en finitos pasos (no hay ciclos sin salida).
3. **Sub-coalgebra de safety** (cuando declarada) — el subset es cerrado
   bajo transiciones.

Para `urgenciologo` (13 estados, 14 transiciones declaradas) y
`salubrista` (10 estados, 9 transiciones declaradas), el check pasa
con 0 diagnostics. Esto materializa la disciplina de safety **mas alla
del lint estructural**: ahora la maquina dice "ese flujo de visita
clinica nunca se cuelga en un loop sin salida".

Los otros 4 agentes productivos (`steipete`, `allan-kelly`,
`medico-hospitalista`, `gtd-integral`) tienen `plan.estados` como lista
narrativa de fases sin transiciones explicitas. Activar coalgebra ahi
requiere reconstruir transiciones, lo cual es work mayor — queda como
deuda documentada.

### Leyes algebraicas de `relations`

Antes del refactor, `relations` era declarada como "morfismos de
KnowCat" sin leyes algebraicas explicitas. Hoy:

| Relacion | Estructura | Aciclica | Antisimetrica | Check |
|----------|------------|----------|----------------|-------|
| `cites` | binaria libre | no | no | `urn-integrity` |
| `depends` | DAG estricto | **si** | irreflexiva | `kb-graph-cycles` |
| `supersedes` | poset estricto | **si** | **si** | `relations-laws` |
| `refines` | preorder estricto | **si** | no exigida | `relations-laws` |
| `traces_requirements` | many-to-many | no | no | `traces-requirements-semantics` |

La nueva tabla en `knowledge-spec §6.3` deja explicito que cada tipo
define una **subcategoria de KnowCat** con sus propiedades. Las
violaciones (ciclos, supersedes bidireccional) son ahora **bugs
detectables**, no zonas grises.

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 625 artefactos indexados (sin cambios; los 2 agentes mantuvieron URN) |
| `python3 toolchain/kora check --strict` | 33/34 verdes; 1 LOW preexistente en `glosario-hodom-v1.3.0` (WIP del operador) |
| `python3 -m unittest discover -s tests` | suite completa verde (incluye 6 tests nuevos: 2 migrate + 4 relations-laws) |

Cambios cuantitativos:

- Total checks: 33 → 34 (`+relations-laws`).
- Tests totales: 351 → 357 (`+6`).
- Catalogo: estable en 625 artefactos.

## Estado consolidado

### Que cerramos definitivamente

- **Adjuncion `Check ⊣ Fix` para envelope completo**: los 4 codes nuevos
  introducidos ayer son hoy mecanicamente fixables por
  `kora migrate --perfil a-autoria`.
- **Coalgebra como invariante operativo** para los 2 agentes clinicos
  productivos mas criticos.
- **Leyes algebraicas de `relations` enforced**: ningun ciclo de
  `supersedes`/`refines` puede llegar a productivo sin diagnostico.

### Que queda como deuda real

1. **FSM reconstruction** para `steipete`, `allan-kelly`,
   `medico-hospitalista`, `gtd-integral`: tienen `plan.estados` como
   lista de fases narrativas sin transiciones declaradas. Activar
   coalgebra ahi requiere agregar transiciones explicitas, lo que es
   work editorial significativo.
2. **Problema 4 (matriz de preservacion `Build ∘ Transmute`)**: queda
   sin tocar porque requiere modificar `transmutation-spec` (en freeze
   por gobernanza §8.3). Postergar hasta cierre de Fase 3 HITL.
3. **Operad / sheaf / naturalidad de transmutaciones**: oportunidades
   de **valor a 6 meses**, no resolvieron dolor hoy.
4. **WIP del operador** en
   `artifacts/knowledge/salud/salubrista/hodom/glosario-terminologico-hodom-v1.3.0.md`
   y `artifacts/skills/dev/hermes-agent-specialist/` queda intacto.

### Que NO debe asumirse

- No asumir que el check `relations-laws` corrige los ciclos: solo los
  detecta. El operador debe romper la cadena editorial (eliminar la
  arista que cierra el ciclo).
- No asumir que `verificacion_coalgebraica: true` se activa
  automaticamente; es opt-in por artefacto.
- No asumir que el codemod cubre TODAS las reglas del validador: solo
  cubre las del envelope universal y los renames. La fibra condicional
  por forma material sigue siendo manual.

## Artefactos dejados versionados

### Specs
- `serialization/knowledge-spec.md` — §6.3 nueva + §6.4 renumerada
  (sin bump de version porque el cambio es aditivo y refina semantica
  ya implicita).

### Toolchain
- `toolchain/kora_lib/migration.py::_autoria_migrate_manifest` —
  envelope hoist.
- `toolchain/kora_lib/checks.py` — `_collect_relation_edges`,
  `_find_cycles`, `_check_relations_laws` + registro.

### Artefactos
- `artifacts/agents/salud/urgenciologo/AGENT.md` —
  `verificacion_coalgebraica: true`.
- `artifacts/agents/salud/salubrista/AGENT.md` —
  `verificacion_coalgebraica: true`.

### Tests
- `tests/test_migrate_autoria.py` — 2 tests nuevos (adjuncion).
- `tests/test_check_pipeline.py` — TestRelationsLaws con 4 tests.

### Docs
- `docs/handoffs/2026-05-18-mejoras-categoriales-1-2-3.md` (este).

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-18-mejoras-categoriales-1-2-3.md`.

Contexto que debes asumir como vigente:

- Adjuncion `Check ⊣ Fix` cerrada para envelope universal: los 4 codes
  envelope-status-/-version-requerido/fuera-de-lugar son mecanicamente
  fixables por `kora migrate --perfil a-autoria`.
- `verificacion_coalgebraica: true` activado en `urgenciologo` y
  `salubrista`. Los otros 4 agentes (`steipete`, `allan-kelly`,
  `medico-hospitalista`, `gtd-integral`) tienen estados narrativos sin
  transiciones — activarlos requiere reconstruir FSM.
- Nuevo check `relations-laws` enforza aciclicidad de `supersedes` y
  `refines` + antisimetria de `supersedes`. `knowledge-spec §6.3`
  documenta las leyes.

Posibles continuaciones:

A. **Reconstruir FSM para los 4 agentes restantes** (deuda 1). Requiere
   curaduria editorial: identificar transiciones desde el body actual.
B. **Naturalidad de transmutaciones**: extender `roundtrip-check` a
   `naturality-check` con par (f, T_R(f)). Esto es problema 4 alternado
   — verifica functorialidad de cada T_R bajo morfismos del IR.
C. **Polynomial functor** en `interfaz` para los skills productivos.
   `autoria-spec §3.5.1` ya lo permite; activarlo es declarar
   `interfaz.polinomio` y obtener composicion automatica via
   composable_con.
D. **Problema 4 (matriz Build ∘ Transmute)**: postergar hasta cierre
   Fase 3 HITL — requiere tocar `transmutation-spec` (freeze).

Mantener commits acotados por linea. No tocar specs en freeze sin
justificacion HITL explicita.
```
