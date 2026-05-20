---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-21-poda-radical"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-21"
    source: "Directiva HITL operador 2026-05-21: sacar todo lo innecesario que no aporte a la finalidad de KORA."
version: "1.0.0"
status: publicado
tags: [handoff, poda-radical, convergencia, simpleza, retiro-masivo]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:adr-poda-radical-2026-05-21"
---

# Handoff 2026-05-21 — Poda radical

## Resumen ejecutivo

Directiva HITL del operador: "Sacar todo lo innecesario y que no aporte
a la finalidad de la existencia de kora". Aplicacion del criterio de
convergencia (KORA v9) sobre el corpus completo.

Decision arquitectural completa en
`urn:kora:kb:adr-poda-radical-2026-05-21`.

## Reduccion cuantitativa

| Categoria | Antes | Despues |
|-----------|-------|---------|
| Archivos en `toolchain/legacy_migration/` | 28 scripts one-shot | 0 (eliminados) |
| Archivos en `_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/` | 225 .md (4.2 MB) | 0 (eliminados) |
| Skills meta-KORA en `_rebuild_required/` | 4 legacy (~30+ archivos) | 0 (eliminados) |
| Handoffs antiguos en `docs/reports/` | 30+ docs | movidos a `governance/decisiones-archivadas/handoffs-historicos/` |
| Planes cumplidos en `docs/plans/` | 7 docs | movidos a `docs/plans/_archivo/` |
| `docs/superpowers/` | 6 archivos | eliminados |
| `docs/reports/` (directorio) | existia | eliminado (vacio tras archivo) |
| Constantes `ATOMIC_*` en validation.py | 71 ocurrencias | 0 |
| Funciones atomic-specific en validation.py | 6 funciones (~215 lineas) | 0 |
| `agent-skill-construction-spec.md` viva | 1 spec | archivada con `status: deprecado` |

**Reduccion total**: ~300 archivos eliminados/movidos; ~5+ MB; una
spec menos viva; ~250 lineas Python dead code removidas.

## Detalle por fase

### Fase A: Toolchain dead code

- Eliminado `toolchain/legacy_migration/` completo (28 scripts one-shot:
  `migrate_to_agentfile`, `move_agents`, `consolidate_catalogs`,
  `cleanup_*`, `atomize.py` 1230L, etc.).
- Eliminadas constantes `ATOMIC_*` en `toolchain/kora_lib/validation.py`
  (`ATOMIC_ALLOWED_TYPES`, `ATOMIC_HARD_MAX_PROPOSITIONS`,
  `ATOMIC_SOFT_SEGMENT_TARGET_CHARS`, `ATOMIC_PRODUCER_URN`,
  `ATOMIC_PROP_LINE_*`, `ATOMIC_SOURCE_*`, `ATOMIC_SEGMENT_*`).
- Eliminadas 6 funciones atomic-dedicated (`resolve_atomic_role`,
  `parse_atomic_source_index`, `parse_atomic_propositions`,
  `_atomic_source_target_resolves`, `_collect_atomic_bundle_paths`,
  `lint_atomic_markdown_parts`).
- Limpiados early-returns `if family == "atomic"` en
  `auto_fix_*`, `split_*`, `lint_published_*`.
- `VALID_FAMILIES` saca `atomic`.
- Mappings `FAMILY_MAX_*` sacan entrada `atomic`.

### Fase B: Material crudo retirado

- Eliminado
  `artifacts/knowledge/_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/`
  (225 archivos atomic-* retirados ayer; 4.2 MB).

### Fase C: Skills meta-KORA en `_rebuild_required`

- Eliminado `artifacts/skills/_TALLER/INBOX/_rebuild_required/2026-05-03/kora/`
  (4 skills legacy: `artifact-curator`, `curation-conductor`,
  `kora-agents` legacy, `kora-skills` legacy). Per
  `meta-kora-rebuild-directive v1.1` estaban CERRADOS sin reactivacion
  pendiente.

### Fase D: Docs historicos

- Movidos `docs/reports/handoff-*` (23 archivos) +
  audits/evaluaciones/prompts (~10 archivos) a
  `governance/decisiones-archivadas/handoffs-historicos/`.
- Eliminado directorio `docs/reports/` (vacio tras archivo).
- Movidos `docs/plans/` cumplidos (planes de usina, recomendaciones de
  personas, source-mapping) a `docs/plans/_archivo/`.
- Mantenido `docs/plans/2026-05-07-politica-handoffs.md` (politica
  viva).
- Eliminado `docs/superpowers/` completo (6 archivos: skills ya
  productivos).

### Fase E: agent-skill-construction-spec

- Movida `serialization/agent-skill-construction-spec.md` a
  `governance/decisiones-archivadas/specs-absorbidas/`.
- Marcada como `status: deprecado` con nota de retiro.
- 7 refs vivas actualizadas:
  - `governance/gobernanza.md` §3 lista jerarquica, §3.2 capa
    serializacion, §3.4 regla de especializacion: eliminadas refs.
  - `artifacts/skills/kora/kora-agents/SKILL.md`: refs eliminadas o
    redirigidas a autoria-spec.
  - `artifacts/skills/kora/kora-skills/SKILL.md`: idem.
  - `artifacts/skills/kora/custodio-kora/SKILL.md` + canon-operativo:
    idem.

### Toolchain — exclusion archivado del scan URN

- `toolchain/kora_lib/config.py`: nueva constante `ARCHIVED_SCAN_MARKERS`
  con paths de `governance/decisiones-archivadas/*`.
- `toolchain/kora_lib/graph.py::build_reference_graph()`: paths
  archivados se INDEXAN (URNs siguen resolviendo) pero NO se ESCANEAN
  para validar refs URN salientes. Sus refs a artefactos retirados son
  legitimas en contexto historico.

## Lo que NO se toca

- **artifacts/agents/, artifacts/skills/, artifacts/knowledge/**
  productivos: 6 agents + 35 skills + ~640 knowledge.
- **Specs activas** (9): gobernanza, harness-spec, qa-spec,
  risk-register-spec, autoria-spec v2, md-spec v11, spec-md v1,
  knowledge-spec v3, runtime-spec-md, transmutation-spec, multiagente,
  + 4 runtime-extensions canonicas (claude-code, codex, openclaw) +
  hermes stub.
- **ADRs en `artifacts/knowledge/kora/adr/`**: trazabilidad
  arquitectural.
- **`docs/handoffs/2026-05-*`**: handoffs recientes convencion vigente.
- **`governance/decisiones-archivadas/`**: preservacion URN del retiro
  reciente (atomize skill, host-roles spec absorbida, 4 runtime-
  extensions archivadas, agent-skill-construction-spec deprecada).
- **`meta-kora-rebuild-directive`**: doctrina activa sobre el rebuild.
- **`docs/start-prompt.md`**, **`docs/README.md`**.

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 696 artefactos indexados (sube por inclusion de archivados en catalog para preservar URNs) |
| `python3 toolchain/kora check --strict` | 28/29 verdes; 1 HIGH preexistente WIP operador (`HANDOFF.md` con `status: handoff` no canonico) |
| `python3 -m unittest discover -s tests` | resultado en commit |

## Resultado

Codigo:

- `toolchain/legacy_migration/` desaparece como directorio.
- `validation.py`: ~250 lineas dead code removidas. Funciones atomic
  desaparecen; familias auxiliares (bok, source, source-alias,
  generic) se preservan.
- `graph.py`: build_reference_graph distingue catalog scope (indexa
  archivados) de URN-refs scope (no scanea archivados).

Catalogo:

- 696 artefactos activos. URNs de skills retirados (`atomize`),
  runtime-extensions archivadas (`gemini`, `mastra`, `opencode`,
  `agentskills`), spec absorbida (`agent-skill-construction-spec`) y
  spec absorbida (`host-roles`) **siguen resolviendo** para
  trazabilidad. Sus refs salientes hacia artefactos retirados no
  rompen `urn-integrity` (contexto historico legitimo).

Convergencia:

- Una spec viva menos (`agent-skill-construction-spec`).
- Un sub-arbol toolchain menos (`legacy_migration/`).
- Un sub-arbol docs menos (`docs/reports/` + `docs/superpowers/`).
- Cuatro skills meta-KORA legacy menos en staging.
- 225 artefactos crudos atomic-retirados menos.

KORA queda en su forma minima fiel post-poda. Lo que existe, **tiene
que existir** para sostener la finalidad declarada.

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-21-poda-radical.md`.

Estado vigente:
- 9 specs vivas: gobernanza v6, harness-spec, qa-spec,
  risk-register-spec, autoria-spec v2, md-spec v11, spec-md v1,
  knowledge-spec v3, runtime-spec-md, transmutation-spec,
  multiagente-spec, + 4 runtime-extensions canonicas + hermes stub.
- agent-skill-construction-spec deprecada (contenido en autoria-spec
  v2.0).
- toolchain sin legacy_migration; validation.py sin codigo atomic
  dead code.
- decisiones-archivadas/ preserva URNs pero no scanea refs.

Para mantenimiento continuo:
- Refs en handoffs antiguos archivados a artefactos retirados son
  legitimas en contexto historico; no requieren correccion.
- WIP del operador en HANDOFF.md (status: handoff no canonico) sigue
  pendiente; ese fix lo decide el operador (no es mio).

No reintroducir material retirado sin HITL + ADR dedicado.
```
