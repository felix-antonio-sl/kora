---
_manifest:
  urn: "urn:kora:kb:agentskills-runtime-extension"
  provenance:
    created_by: "FS"
    created_at: "2026-04-18"
    source: "autoria-spec v1.1 §5.5; transmutation-spec v1.0; matriz de proyeccion implementada en scripts/kora_lib/transmute.py (commit 2812c09)."
version: "1.0.0"
status: publicado
tags: [spec, runtime, agentskills, extension, transmutacion, proyeccion, byte-identical]
lang: es
extensions:
  kora:
    precedence_tier: 4
    platform: "agentskills"
    baseline_docs_release: "agentskills.io v1 (estandar abierto externo)"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:autoria-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:gobernanza"
---

# KORA/Agentskills-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el estandar externo
**agentskills.io**: paquetes portables de habilidades que cualquier
runtime compatible (Claude Code, Codex, Gemini, etc.) puede cargar. La
transmutacion es **byte-identical modulo rename**: la habilidad KORA y
la habilidad agentskills.io son el mismo artefacto expresado en dos
glosarios (espanol canonico vs ingles estandar).

### 1.1 Alcance

Gobierna:

1. Proyeccion `T_{agentskills}: KORA_IR → Agentskills` segun
   `transmutation-spec v1.0`.
2. Rename functorial de campos (es → en) — ver §3.
3. Rename functorial de subdirs y secciones — ver §4.
4. Dominio acotado a `forma_material: habilidad` (no aplica a
   subagente/agente-propiamente-tal/agente-plataforma).
5. Check `fidelidad-agentskills` — verificacion mecanica de la
   proyeccion (`scripts/kora_lib/checks.py`).

## 2. Formas materiales soportadas

| Forma material | Soportada | Razon |
|----------------|:---------:|-------|
| `habilidad` | si | Unico shape portable byte-identical. |
| `subagente` | no | Requiere runtime con concepto de sub-invocacion (Task, delegacion). |
| `agente-propiamente-tal` | no | Requiere workspace productivo + persistencia. |
| `agente-plataforma` | no | Requiere always-on / daemon. |

Si un artefacto con `forma_material != habilidad` intenta transmutar a
target `agentskills`, el transmutor emite `ValueError` y aborta —
conforme `autoria-spec §5.5`.

## 3. Matriz de preservacion por eje

Dominio del runtime (vectores fuera de estos rangos son rechazados por
el transmutor):

| Eje | Dominio | Semantica |
|-----|---------|-----------|
| Π   | {0, 1, 2} | Plan ramificado maximo; no fixed-points. |
| Μ   | {0, 1} | Sin memoria persistente (agentskills es pieza portable). |
| Ξ   | {0, 1, 2} | Lente bidireccional maximo; no coreografia ni operad. |
| Λ   | {0} | Individual solamente. |
| Φ   | {0, 1} | Disjunto o instrumental (tool metaphor). |
| Σ   | [{0..3}]×5 | Vector etico sin cota impuesta por runtime. |

Fuera de dominio implica `fidelity: none` y rechazo functorial. Los
ejes canonicos de una habilidad real (derivados de `harness-spec §5.1`
tabla de Arneses) caen naturalmente en este recinto.

## 4. Rename functorial (autoria-spec §5.5)

### 4.1 Rename de campos (frontmatter)

| Campo KORA (es) | Campo agentskills.io (en) | Notas |
|------------------|----------------------------|-------|
| `nombre` | `name` | Identificador humano. |
| `descripcion` | `description` | Disparador + uso (1 linea). |
| `allowed-tools` | `allowed-tools` | Preservado. |

Campos que **se eliminan en la proyeccion** (no son parte del estandar
externo):

- `_manifest` (sistema KORA interno).
- `version`, `status`, `tags`, `lang` (metadata KORA).
- `extensions.kora.*` (overlay KORA — no se exporta).
- Otros `extensions.{runtime}` (fibras de otros runtimes).
- `artefacto.*` (shape unificado KORA — se descarta).

### 4.2 Rename de subdirs

| Subdir KORA (es) | Subdir agentskills.io (en) |
|-------------------|-----------------------------|
| `referencias/` | `references/` |
| `recursos/` | `assets/` |
| `scripts/` | `scripts/` (preservado) |

### 4.3 Rename de secciones en body Markdown

| Heading KORA (es) | Heading agentskills.io (en) |
|--------------------|------------------------------|
| `## Recursos` | `## Resources` |
| `### Referencias` | `### References` |
| `### Recursos` | `### Assets` |
| `### Scripts` | `### Scripts` (preservado) |

Renames se aplican solo a **headings exactos** en niveles `##` o
`###`. No afectan prosa que contenga la palabra.

## 5. Output de transmutacion

El transmutor emite a `{skill_dir}/_BUILD/agentskills/`:

```
_BUILD/agentskills/
├── SKILL.md                 # frontmatter renombrado + body renombrado
├── references/              # renombrado desde referencias/
├── assets/                  # renombrado desde recursos/ si existia
├── scripts/                 # preservado tal cual
└── _transmutation.yml       # proof-carrying manifest
```

`_BUILD/agentskills/` es gitignored (output derivado). Se regenera con
`kora transmute --target agentskills --agent {ns}/{nombre}`.

## 6. Proof-carrying: `_transmutation.yml`

Emitido junto al paquete. Contiene:

- `transmutation.functor`: `T_agentskills_v1.0`.
- `transmutation.source_hash`: sha256 del SKILL.md fuente (para detectar drift).
- `transmutation.source_vector`: vector IR completo.
- `transmutation.projections`: proyeccion por eje con fidelity declarada.
- `transmutation.field_renames`: mapa §4.1.
- `transmutation.subdir_renames`: mapa §4.2 aplicado (solo los que ocurrieron).
- `transmutation.section_renames`: mapa §4.3.
- `transmutation.structural_preservation`:
  - `composition: preserved`
  - `identity: preserved`
  - `semantic_body: preserved`
- `transmutation.bisimulation_claim: byte-identical-modulo-renames`.

## 7. Verificacion

### 7.1 Check `fidelidad-agentskills`

Implementado en `scripts/kora_lib/checks.py`. Severity `high`. Itera
sobre todas las habilidades productivas (`SKILLS/**/SKILL.md` con
`forma_material: habilidad`) y verifica:

1. La proyeccion dry-run no falla por dominio.
2. No hay perdida estructural (perdida en ejes no-sigma implica bug).
3. Existe `nombre` (o `name`) y `descripcion` (o `description`).

### 7.2 Round-trip (dualidad `T_agentskills` ⊣ `Lift_agentskills`)

`Lift_agentskills` (ingest inverso desde un paquete agentskills.io)
esta **fuera de alcance** de v1.0 de esta extension. La dualidad
formal queda como deuda declarada: un paquete externo puede importarse
via `kora ingest --from claude-code` tratandolo como skill Claude Code
(misma shape minima), pero no hay importador dedicado.

## 8. Retrocompatibilidad

- La proyeccion **reemplaza** cualquier output anterior en
  `_BUILD/agentskills/` sin warning (es regenerable).
- Cambios a los mapeos §4 requieren bump minor de esta extension y
  re-ejecucion del transmutor sobre todas las habilidades productivas.

## 9. Invariantes

1. La proyeccion es **idempotente**: aplicar el transmutor dos veces
   produce el mismo output byte-a-byte (modulo timestamp de
   `_transmutation.yml`).
2. La proyeccion **no muta** la fuente: `SKILLS/{ns}/{nombre}/SKILL.md`
   queda intacta.
3. La proyeccion **no depende de LLM**: es rename mecanico. Si
   requiere intervencion semantica, la habilidad no cumple shape
   portable y debe corregirse antes de transmutar.
4. `TARGET_ADAPTERS["agentskills"] = None` por diseño: no hay skill
   adapter — la proyeccion es directa.

## 10. Relacion con otras extensiones

- `claude-code-runtime-extension`: Claude Code consume paquetes
  agentskills.io como skills estandar. Una habilidad KORA transmutada
  a `agentskills` es cargable en `~/.claude/skills/` sin modificacion.
- `codex-runtime-extension`: idem `~/.codex/skills/`.
- `gemini-runtime-extension`: idem Gemini skills dir.
- `openclaw-runtime-extension`: los agentes OpenClaw pueden referenciar
  skills agentskills.io como subordinados.

Es decir: `agentskills` es el **minimum common denominator** para
habilidades portables; los otros runtimes lo superset.
