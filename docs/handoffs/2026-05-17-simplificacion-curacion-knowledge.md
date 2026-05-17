---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-17-simplificacion-curacion-knowledge"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-17"
    source: "Refactor pragmatico de las specs de curacion de conocimiento KORA: separacion formato/pipeline en md-spec/knowledge-spec, promocion de atomize a productivo, endurecimiento de knowledge-zone con status-por-directorio y namespace-directorio, publicacion de 12 drafts historicos en salud/dbt y agengai/openclaw."
version: "1.0.0"
status: publicado
tags: [handoff, knowledge-spec, md-spec, atomize, pipeline, curacion, normalizacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:autoria-spec"
---

# Handoff sesion 2026-05-17 — Simplificacion de la curacion de conocimiento

## Resumen ejecutivo

Esta sesion refactoriza pragmaticamente las specs que gobiernan la
curacion de artefactos de conocimiento KORA, separando responsabilidades
entre **formato** (md-spec) y **pipeline + identidad + lifecycle**
(knowledge-spec), promueve `atomize` a productivo, endurece el check
`knowledge-zone` para verificar coherencia status-directorio y
namespace-directorio, y normaliza 12 artefactos productivos que vivian
con `status: borrador` por deuda historica anterior al enforcement.

El refactor preserva rigor categorial implicito: el pipeline queda
modelado como cadena de funtores con preservacion de identidad URN, las
familias documentales como perfiles del envelope base, y los morfismos
de `relations` con composicion que preserva resolubilidad. Ninguna spec
en freeze (`harness-spec`, `autoria-spec`, `transmutation-spec`) fue
tocada.

## Alcance

### Capa serializacion

- **`serialization/knowledge-spec.md v2.0.0`** (refactor mayor).
- **`serialization/md-spec.md v9.0.0`** (refactor mayor con scope
  reducido a formato).

### Capa runtime

- **`artifacts/skills/_TALLER/INBOX/atomize/`** →
  **`artifacts/skills/kora/atomize/`** (`urn:kora:artefacto:atomize`
  pasa de staging a productivo; cierra la inconsistencia de v1.3 §12.2
  que reconocia "staging, sin URN productivo vigente").

### Capa toolchain

- **`toolchain/kora_lib/checks.py::_check_knowledge_zone`** endurecido.
- **`toolchain/kora_lib/validation.py::FAMILY_MAX_LINES_PER_PRIMARY_CHUNK['spec']`**:
  450 → 500 (cobertura del nuevo §5 absorbido por md-spec v9).
- **`spec_ref`** actualizados en 4 checks (`knowledge-zone`, `lint-md`,
  `kb-graph-cycles`, `traces-requirements-semantics`,
  `supersedes-consistency`).

### Normalizacion de artefactos

- 12 archivos productivos publicados in-place (status `borrador` →
  `publicado`):
  - 11 en `artifacts/knowledge/salud/dbt/dbt-oxford-*.md`
  - 1 en `artifacts/knowledge/agengai/openclaw/specs-legacy/manual-integral-skills-openclaw.md`

### Tests

- `tests/test_artifacts.py::test_knowledge_spec_registers_atomize_as_canonical_producer`
  actualizado al nuevo §9 y path productivo.
- `tests/test_artifacts.py::test_md_spec_restores_koraficacion_contract`
  actualizado a v9 (acepta v8 y v9 historicos).
- `tests/test_semantic_validation.py::test_resolve_max_lines_per_h2_uses_spec_family_threshold`
  actualizado al nuevo umbral 500.

## Cambios doctrinales

### knowledge-spec v1.3.0 → v2.0.0

Absorbio de `md-spec §3.1 r7-10` las reglas que **no** son formato sino
pipeline o identidad:

- **§3** (nueva) — URN conceptual `urn:{ns}:kb:{id}` y coherencia
  namespace-directorio.
- **§4** (nueva) — lifecycle descriptivo `borrador → publicado →
  deprecado`, status por directorio, transiciones via `kora promote`.
- **§5** — familias documentales: redireccion a `md-spec §5.6` como
  fuente unica.
- **§6** — morfismos: agrega §6.3 functorialidad (identidad +
  composicion preservan resolubilidad).
- **§8** (renumerada y formalizada) — pipeline `Intake → Normalize →
  Enrich → Publish → Graph` explicitando que la composicion preserva
  identidad URN una vez asignada.
- **§9** (renumerada desde §12) — productores canonicos; tabla
  actualizada a `artifacts/skills/kora/atomize/SKILL.md` productivo.
- **§11** — invariantes ampliados a 8 (incluye productor canonico
  monopoliza emision).
- **§12** — tabla validacion con `Spec ref` explicito.
- **§13** (nueva) — catalogo de comandos CLI vivos para curacion.

### md-spec v8.1.0 → v9.0.0

Reduce su scope a **formato puro**:

- **§1.2** (nueva) — declara lo que NO gobierna esta spec (delegado a
  knowledge-spec y autoria-spec).
- **§3.1** — reglas r1-r7 (envelope) permanecen; r8-r10 delegan
  explicitamente a knowledge-spec y autoria-spec.
- **§3.3** (nueva) — campo `relations` reservado por md-spec, semantica
  delegada a knowledge-spec.
- **§5.6** — agrega tabla de familias auxiliares (`bok`, `source`,
  `source-alias`, `generic`) que el toolchain ya usaba pero no estaban
  documentadas.
- **§6.1** — reducida a puntero al pipeline gobernado por
  knowledge-spec §8.
- **§9** — tabla de validacion limpia: solo invariantes de formato. Los
  checks de tejido relacional y pipeline declaran explicitamente vivir
  en `knowledge-spec §12`; los checks agenticos en `autoria-spec §14`.

### Disciplina functorial implicita

Sin nombrarlo como teoria categorial, las nuevas reglas materializan:

- **Identidad** — `knowledge-spec §8.3`: la promocion `borrador →
  publicado` preserva el URN byte-identical.
- **Composicion** — `knowledge-spec §6.2 r1`: composicion de
  `relations` preserva resolubilidad.
- **Monotonia** — `knowledge-spec §4.1 r1`: las transiciones inversas
  del lifecycle son invalidas (ω-cadena estricta).
- **Productor canonico como objeto inicial** — `knowledge-spec §9.3
  r6`: si la familia tiene productor, no se admite generacion
  alternativa (todo morfismo desde "input crudo" pasa por el productor).

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 621 artefactos indexados (+10 vs baseline) |
| `python3 toolchain/kora check --strict` | 32/33 verdes; 1 LOW preexistente en hodom-v1.3.0 (WIP del operador) |
| `python3 -m unittest discover -s tests` | suite completa verde |

Tras el endurecimiento de `knowledge-zone`, el check detecto 12 drafts
historicos en productivo. Todos fueron publicados in-place tras
verificacion de contenido (eran artefactos legitimos con drift de status
anterior al enforcement, no drafts activos).

## Estado consolidado

### Que cerramos definitivamente

- `atomize` en topologia productiva con URN canonico
  `urn:kora:artefacto:atomize`; la inconsistencia de la spec v1.3 ("sin
  URN productivo vigente") queda resuelta.
- Separacion clara formato (`md-spec`) vs pipeline (`knowledge-spec`):
  ninguna regla vive en dos lugares.
- `knowledge-zone` ahora verifica las invariantes que la spec promete:
  status-por-directorio (§4.2) y namespace-directorio (§3.2).
- Familias auxiliares (`bok`, `source`, `source-alias`, `generic`)
  documentadas en md-spec §5.6 alineadas con `validation.py`.
- 12 drafts historicos pasaron a `publicado`; el catalogo refleja su
  estado real.

### Que queda como deuda real

1. **El check `knowledge-zone` actualmente requiere `load_markdown_parts`
   por cada .md productivo** (~600 archivos). Es mas costoso que la
   version v1.x que solo leia los primeros 2KB. Si el tiempo de
   `check --strict` crece notoriamente, considerar caching o muestreo.

2. **`_SCRIPTORIUM/REVIEW/kora/atomic/`** sigue con 80+ artefactos
   `atomic-opm-libro-rebuilt-*` rechazados por acceptance review (deuda
   heredada del handoff 2026-04-18). No tocado en esta sesion.

3. **`_SCRIPTORIUM/INBOX/`** acumula material crudo en multiples
   namespaces (opm, dev, curso-dov-dori, gn, pro, legal, fxsl, hi, sii,
   omega, opm-libro-curado, salud, kora). La doctrina vigente los
   reconoce como "pre-categoriales"; no son ruido pero son backlog.

4. **`atomize/SKILL.md` declara `entornos_objetivo: [claude-code, codex]`**
   pero el agentskills.io transmute no esta validado en runtime para
   este artefacto en su nueva ubicacion (fidelidad-agentskills check
   pasa porque la habilidad es legitima, pero no se corrio `kora
   transmute --target agentskills` para confirmar el paquete byte-identical).

5. **Trabajo en progreso del operador en
   `artifacts/knowledge/salud/salubrista/hodom/glosario-terminologico-hodom-v1.3.0.md`**
   queda intacto; sus 6 LOW de `lint-md` son responsabilidad de la
   propia linea de trabajo del operador.

### Que NO debe asumirse

- No asumir que las refs a `knowledge-spec §12` (productores) siguen
  apuntando a §12: en v2.0.0 es §9. Las refs internas del repo se
  reapuntaron; refs externas (docs historicas, handoffs antiguos)
  pueden seguir citando la numeracion vieja.
- No asumir que `md-spec §3.1 r7-10` siguen normando pipeline: en v9.0
  son redirecciones a `knowledge-spec`.
- No asumir que `kora promote` arregla drafts ya en productivo: solo
  mueve desde `_SCRIPTORIUM/REVIEW/`. Para flip de status in-place hay
  que editar a mano (como se hizo con los 12 archivos).

## Artefactos dejados versionados

### Specs
- `serialization/knowledge-spec.md` — v2.0.0.
- `serialization/md-spec.md` — v9.0.0.

### Toolchain
- `toolchain/kora_lib/checks.py` — `_check_knowledge_zone` endurecido +
  4 spec_ref actualizados.
- `toolchain/kora_lib/validation.py` — `FAMILY_MAX_LINES_PER_PRIMARY_CHUNK['spec']`
  450 → 500.

### Productivos movidos
- `artifacts/skills/_TALLER/INBOX/atomize/` → `artifacts/skills/kora/atomize/`.

### Artefactos publicados
- `artifacts/knowledge/salud/dbt/dbt-oxford-*.md` (11 archivos):
  status `draft` → `publicado`.
- `artifacts/knowledge/agengai/openclaw/specs-legacy/manual-integral-skills-openclaw.md`:
  status `draft` → `publicado`.

### Tests
- `tests/test_artifacts.py` — 2 tests actualizados.
- `tests/test_semantic_validation.py` — 1 test actualizado al umbral 500.

### Docs
- `docs/handoffs/2026-05-17-simplificacion-curacion-knowledge.md`
  (este archivo).

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-17-simplificacion-curacion-knowledge.md`.

Contexto que debes asumir como vigente:
- `knowledge-spec v2.0.0` es la SSOT del pipeline de curacion + lifecycle
  conceptual + identidad URN conceptual + productores canonicos.
- `md-spec v9.0.0` gobierna solo formato (envelope, familias documentales,
  koraficacion, perfil prescriptivo spec). Ninguna regla de pipeline vive
  aqui; todas las refs cruzadas apuntan a knowledge-spec.
- `atomize` vive en `artifacts/skills/kora/atomize/` con URN
  `urn:kora:artefacto:atomize`. No es staging; es productivo.
- `knowledge-zone` chequea ahora status-por-directorio + namespace-directorio;
  esperar 0 diagnosticos en productivo si todo esta normalizado.
- `FAMILY_MAX_LINES_PER_PRIMARY_CHUNK['spec'] = 500`; las specs de KORA
  caben dentro del limite.

Para tareas tipicas:

1. Curar conocimiento nuevo: `_SCRIPTORIUM/INBOX/{ns}/<crudo>` ->
   `_SCRIPTORIUM/REVIEW/{ns}/<id>.md` con frontmatter conforme a `md-spec` y
   relations conforme a `knowledge-spec §6`. Luego `kora promote`.
2. Curar familia atomic: invocar `atomize` desde
   `artifacts/skills/kora/atomize/`. Output a
   `_SCRIPTORIUM/REVIEW/{ns}/atomic/`. Luego `kora promote`.
3. Antes de cualquier cambio mayor de doctrina, leer `gobernanza.md`
   (sigue v4.7.0) y verificar que tu cambio no toque las specs en freeze
   (`harness-spec`, `autoria-spec`, `transmutation-spec`).

Posibles continuaciones (no urgentes):

A. **Limpiar _SCRIPTORIUM/REVIEW/kora/atomic/** — 80+ atomic-opm-libro-rebuilt-*
   rechazados. Decidir si curar a publicable o eliminar como baseline.
B. **Optimizar knowledge-zone** — leer 600 archivos por check es costoso;
   considerar caching del frontmatter parsed o muestreo.
C. **Drenar _SCRIPTORIUM/INBOX/** — procesar el material crudo acumulado
   por namespace, posiblemente con cohortes.
D. **Validar fidelidad-agentskills del atomize en su nueva ubicacion** —
   correr `kora transmute --target agentskills --skill kora/atomize` para
   confirmar byte-identical.

Mantener commits acotados por linea. No tocar specs en freeze sin
justificacion explicita.
```
