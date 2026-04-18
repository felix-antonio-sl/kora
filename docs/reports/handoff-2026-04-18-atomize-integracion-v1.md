---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-18-atomize-integracion-v1"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-04-18"
    source: "Cierre de la integracion de atomize al nuevo KORA (autoria-spec v1.0): migracion de SKILL.md + glosario espanol en check skill-structure + rename references/->referencias/."
version: "1.0.0"
status: publicado
tags: [handoff, atomize, autoria-spec, skill-structure, glosario-espanol, integracion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:handoff-2026-04-18-atomize-skill"
  refines:
    - "urn:kora:kb:handoff-2026-04-18-atomize-skill"
---

# Handoff sesion 2026-04-18 — Integracion de `atomize` al nuevo KORA

## Resumen ejecutivo

Esta sesion completa la integracion del unico skill productivo top-level
(`SKILLS/kora/atomize/`) al shape de autoria unificada definido por
`autoria-spec v1.0`, y endurece el toolchain para que el enforcement del
check `skill-structure` deje de pedir nomenclatura pre-unificacion.

El handoff anterior (`handoff-2026-04-18-atomize-skill.md`) consolido la
linea `atomize` como productor canonico con review de calidad y acceptance
gate en el wrapper. Esta sesion reinterpreta el objetivo principal:
redirigir el commit acotado desde "subir el acceptance gate al core" hacia
"integrar atomize al nuevo KORA", porque el SKILL.md aun vivia en el shape
`agentfile-spec v2` + `skill-overlay-spec v2` previo a la unificacion.

## Alcance

La sesion se ejecuto en dos fases encadenadas, ambas acotadas a la linea
`atomize` y al check que la gobierna:

### Fase 1 — Migracion `SKILL.md` a autoria-spec v1.0

Objetivo: que `SKILLS/kora/atomize/SKILL.md` pase `autoria-conformance`
sin diagnosticos y que ningun artefacto del repo siga declarando el URN
viejo como productor canonico.

Cambios:

- **Frontmatter de SKILL.md** reescrito al shape unificado:
  - URN regimen unico: `urn:kora:artefacto:atomize` (antes
    `urn:kora:skill:atomize:1.0.0`).
  - `_manifest.type: artefacto`, `version: 1.0.0` declarada fuera del URN.
  - `extensions.kora.vector_ontologico` en espanol (pi=2, mu=0, xi=1,
    lambda=0, phi=1, sigma=[1,1,3,1,0]); cumple el dominio de proyeccion
    valido para `forma_material: habilidad` (pi<=2, mu<=1).
  - `extensions.kora.atlas.{arnes_categorico: disciplina,
    forma_material: habilidad, metafora_relacional: supertool}`.
  - `extensions.kora.entornos_objetivo: [claude-code, codex]`,
    `nivel_prescripcion: medio`.
  - Shape `artefacto.{perfil, plan, interfaz, invariantes}` condicional a
    habilidad; `contexto.memoria_config` y `composicion` ausentes (ambos
    prohibidos por el validador para habilidad).

- **Constantes de emisor y validador** actualizadas a
  `urn:kora:artefacto:atomize`:
  - `scripts/kora_lib/atomize.py::ATOMIC_PRODUCER_URN`.
  - `scripts/kora_lib/validation.py::ATOMIC_PRODUCER_URN`.

- **Referencias cruzadas** actualizadas:
  - `specs/knowledge-spec.md §12.2` — tabla de productor canonico.
  - `SKILLS/kora/atomize/referencias/atomic-output-contract.md` —
    frontmatter emitido documentado.
  - `SKILLS/kora/atomize/SKILL.md` body — referencia a
    `extensions.kora.atomic.producer`.

- **Tests** ajustados:
  - `tests/test_atomize.py` — fixtures que probaban el linter de
    frontmatter atomic con el URN viejo.
  - `tests/test_artifacts.py::test_knowledge_spec_registers_atomize_as_canonical_producer`
    — assertion sobre el URN presente en la spec.

### Fase 2 — Check `skill-structure` al glosario espanol

Objetivo: que el check normativo que valida la topologia de habilidades
deje de contradecir `autoria-spec §5.1/§5.5/§15.3`, donde el glosario
canonico es espanol (`referencias/`, `recursos/`, `## Recursos`) y los
nombres en ingles (`references/`, `assets/`, `## Resources`) son
proyecciones del transmutor a agentskills.io (fidelidad-agentskills).

Cambios:

- **`scripts/kora_lib/checks.py::_check_skill_structure`** reescrito:
  - `CANONICAL_SUBDIRS = {"scripts", "referencias", "recursos"}`.
  - Heading exigido: `## Recursos` (regex sin `IGNORECASE`).
  - Mapping explicito subdir -> heading (`Scripts`, `Referencias`,
    `Recursos`) — antes se usaba `subdir.capitalize()`, que con los
    nombres en espanol seguiria funcionando pero la tabla explicita deja
    claro el contrato.
  - `spec_ref` del check actualizado a
    `autoria-spec §5.1, §5.5, §15.3` (antes `skill-overlay-spec §5`,
    spec retirada).
  - Mensajes de diagnostico y `fix_hint` en espanol, apuntando a
    `autoria-spec` y al nuevo identificador `componible_con` en vez de
    `composable_with`.
  - Docstring documenta explicitamente que los nombres en ingles son
    proyeccion a agentskills.io, no shape de autoria valido.

- **`SKILLS/kora/atomize/`** — rename fisico:
  - `git mv references/ referencias/` (9 archivos preservados tal cual).
  - `SKILL.md` body: `## Resources` -> `## Recursos`,
    `### References` -> `### Referencias`, 11 menciones
    `references/*.md` -> `referencias/*.md`.

- **`tests/test_artifacts.py::test_atomize_skill_is_runtime_agnostic_and_llm_first`**
  — `required_terms` y `required_paths` actualizados al glosario espanol,
  mas assertion nueva `### Referencias` para cubrir la subseccion
  canonica.

Los tests que verifican `references/`/`assets/` sobre bundles
`skills/CM-*/SKILL.md` de forgemaster/curator (legacy exentos por el
check via prefijo `CM-`) se mantuvieron intactos: son documentacion del
subsistema legacy, no shape de autoria productivo.

## Validacion ejecutada

- `python3 scripts/kora index` — 599 artefactos indexados, warnings
  triviales por archivos de `referencias/` sin frontmatter KORA
  (comportamiento esperado: son docs auxiliares).
- `python3 scripts/kora check` filtrado por `atomize` y
  `SKILLS/kora/atomize`: **0 diagnosticos**.
- `python3 -m unittest discover -s tests`: **288 tests OK** (2 skips).
- `python3 scripts/kora sync-docs` — docs generadas regeneradas.

## Estado consolidado

### Que cerramos definitivamente

- `SKILLS/kora/atomize/SKILL.md` conforma a `autoria-spec v1.0` sin
  residuos de `skill-overlay-spec v2` ni `agentfile-spec v2`.
- El URN viejo `urn:kora:skill:atomize:1.0.0` ya no existe en ningun
  artefacto productivo, spec, emisor o validador (se conserva solo en
  tests de migracion que intencionalmente reciben el URN legacy como
  input del codemod y en el handoff historico previo).
- El check `skill-structure` es normativo segun `autoria-spec v1.0` y
  referencia las secciones correctas.
- Atomize usa el glosario espanol canonico (`referencias/`, `recursos/`
  no aplica por no tener assets, `## Recursos`, `### Referencias`).

### Que quedo como deuda real

1. **Promotor `kora promote` sigue sin replicar el acceptance gate fuerte
   que vive en `SKILLS/kora/atomize/scripts/publish_atomic.py`.** Es la
   deuda original del handoff anterior, sin tocar en esta sesion. El
   wrapper bloquea bien pero el core sigue laxo. Mientras exista la
   diferencia, hay dos niveles de rigor.

2. **`scripts/kora migrate --perfil a-autoria` no toca `SKILLS/`.** La
   migracion manual de `atomize` se hizo a mano. Si en el futuro aparecen
   mas habilidades productivas fuera de staging con shape legacy, habra
   que extender el migrator o migrarlas manualmente.

3. **`atomic-opm-libro-rebuilt-*`** sigue rechazado por acceptance review
   vigente. Decision pendiente: curarlo hasta publicable o dejarlo como
   baseline de referencia. No bloquea nada.

4. **Worktree tiene cambios pre-existentes de otra linea** (7 AGENT.md
   modificados, 5 scripts/tests modificados, `INBOX/opm-libro-curado/`
   untracked). No son propios de esta sesion y quedaron deliberadamente
   fuera del commit.

### Que NO debe asumirse

- No asumir que `scripts/kora promote` ya impone el gate de acceptance
  review. Sigue laxo.
- No asumir que el catalogo refleja el estado pos-commit sin correr
  `kora index` + `kora sync-docs`.
- No asumir que los bundles historicos de `atomic-opm-libro-*` ya usan
  el nuevo URN productor en su frontmatter. Son output emitido antes de
  la migracion; si se regeneran con `atomize`, tomaran el URN nuevo.

## Artefactos dejados versionados

### Codigo
- `SKILLS/kora/atomize/SKILL.md` — migrado a autoria-spec v1.0.
- `SKILLS/kora/atomize/referencias/*` (rename desde `references/`).
- `scripts/kora_lib/atomize.py` — `ATOMIC_PRODUCER_URN` actualizado.
- `scripts/kora_lib/validation.py` — `ATOMIC_PRODUCER_URN` actualizado.
- `scripts/kora_lib/checks.py::_check_skill_structure` — glosario
  espanol, spec_ref autoria-spec, mapping SUBDIR_HEADINGS.

### Specs
- `specs/knowledge-spec.md §12.2` — tabla de productores canonicos.

### Tests
- `tests/test_atomize.py` — fixtures con URN nuevo.
- `tests/test_artifacts.py` — paths/terms en espanol + assertion
  `### Referencias`.

### Docs
- `docs/reports/handoff-2026-04-18-atomize-integracion-v1.md` (este).

## Prompt de continuacion

```text
Retoma la linea `atomize` en /home/felix/kora desde el estado consolidado
en `docs/reports/handoff-2026-04-18-atomize-integracion-v1.md`.

Objetivo principal:
- subir el acceptance gate de `atomic` al core del repo para que
  `scripts/kora promote` y el wrapper
  `SKILLS/kora/atomize/scripts/publish_atomic.py` tengan el mismo rigor.

Contexto que debes asumir como vigente:
- `SKILLS/kora/atomize/SKILL.md` ya conforma `autoria-spec v1.0` con
  URN `urn:kora:artefacto:atomize`, vector ontologico espanol y shape
  `artefacto.*` condicional a `forma_material: habilidad`.
- El check `skill-structure` ya enforza el glosario espanol
  (`referencias/`, `recursos/`, `## Recursos`); nuevas habilidades deben
  nacer con ese layout. Los nombres en ingles son proyeccion a
  agentskills.io, no shape de autoria.
- `ATOMIC_PRODUCER_URN = "urn:kora:artefacto:atomize"` en atomize.py y
  validation.py; cualquier atomic nuevo se valida contra ese URN.
- `scripts/kora migrate --perfil a-autoria` no cubre `SKILLS/`; migrar
  habilidades a mano si aparecen nuevas con shape legacy.

Primero:
1. Inspecciona `scripts/kora_lib/promote.py`,
   `SKILLS/kora/atomize/scripts/publish_atomic.py`,
   `tests/test_atomize.py` y este handoff.
2. Disena la subida del gate al core sin romper la promocion normal de
   familias no-atomic.
3. Agrega tests de regresion para:
   - promote de `atomic` sin acceptance review
   - promote de `atomic` con review stale
   - promote de `atomic` con review aceptada y fresca
4. Solo despues evalua si conviene seguir limpiando
   `atomic-opm-libro-rebuilt-*` o dejarlo como baseline rechazado.

Mantener commit acotado a esa linea. No arrastrar cambios no
relacionados del worktree (hay deuda pre-existente en 7 AGENT.md,
5 scripts/tests, e INBOX/opm-libro-curado/ untracked).
```
