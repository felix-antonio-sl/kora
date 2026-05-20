---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-20-kora-v7-esencial"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-20"
    source: "Directiva HITL del operador 2026-05-20: KORA gestiona ciclo de vida de 3 tipos de artefacto (conocimiento, agentes, skills) en IR agnostico, transmutables a 4 runtimes (claude-code, codex, openclaw, hermes). Maxima simpleza, manteniendo rigor y potencia."
version: "1.0.0"
status: publicado
tags: [handoff, kora-v7, esencial, hermes, runtimes-canonicos, freeze-parcial]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:adr-kora-v7-esencial"
    - "urn:kora:kb:hermes-runtime-extension"
---

# Handoff 2026-05-20 — KORA Esencial v7

## Resumen ejecutivo

Esta sesion implementa la directiva HITL del operador (2026-05-20): KORA
converge a su lectura minima esencial — sistema que gestiona el ciclo
de vida de tres tipos de artefacto (conocimiento, agentes, skills) en
IR agnostico, transmutables a cuatro runtimes canonicos (claude-code,
codex, openclaw, hermes).

Decision arquitectural en `urn:kora:kb:adr-kora-v7-esencial`.

## Alcance

### Activacion HITL de hermes

- `governance/gobernanza.md` §8.2 reescrita: `Hermes ES runtime canonico
  desde 2026-05-20`. La regla previa de bloqueo queda historica en el
  catalogo via versionado.
- `runtime/hermes-runtime-extension.md` v0.1.0 publicado como **stub**:
  URN canonico declarado, dominio inicial provisional, deuda explicita
  para Fase 2b.

### Bajado parcial del freeze formal

- `governance/gobernanza.md` §8.3 reescrita:
  - `harness-spec` **sigue en freeze** (core ontologico PMI × LFS).
  - `autoria-spec` **editable** (autoriza compactacion Fase 2b).
  - `transmutation-spec` **editable** (autoriza compactacion Fase 2b).
- `governance/gobernanza.md` §8.4 nueva: registra los 4 runtimes
  archivados con URNs resolubles.

### Gobernanza v5.0.0 → v6.0.0

Major bump justificado por cambio de freeze + activacion de runtime.
§14 nueva documenta la migracion v5 → v6.

### Limpieza de drift `entornos_objetivo`

5 skills productivos tenian `gemini` y/o `mastra` en `entornos_objetivo`
(runtimes archivados desde 2026-05-07). Limpiados:

| Skill | Removidos |
|-------|-----------|
| `artifacts/skills/dev/ship-discipline/SKILL.md` | gemini, mastra |
| `artifacts/skills/pro/gtd-flow/SKILL.md` | gemini, mastra |
| `artifacts/skills/fxsl/cell-design/SKILL.md` | gemini, mastra |
| `artifacts/skills/kora/ux-design/SKILL.md` | gemini |
| `artifacts/skills/kora/mente-omega/SKILL.md` | gemini, mastra |

Adicional: `artifacts/skills/kora/custodio-kora/SKILL.md` y su
`referencias/canon-operativo.md` actualizados para listar las 4
runtime-extensions canonicas (claude-code, codex, openclaw, hermes) en
lugar de las 7 historicas.

### Toolchain

- `toolchain/kora_lib/transmute.py`:
  - `PRESERVATION_MATRIX["hermes"]` agregada como stub provisional con
    fidelity `pending` (verificacion empirica en Fase 2b).
  - `TARGET_ADAPTERS["hermes"]` agregado (adapter None por ahora;
    Fase 2b cierra el adapter).
  - `TRACE_FIDELITY_BY_TARGET["hermes"]` agregado.
- `tests/common.py`: `ACTIVE_TARGETS` ahora incluye `hermes`.

## Lo que NO se toca

- **`harness-spec.md`**: queda en freeze. Core ontologico PMI × LFS.
- **`autoria-spec.md` y `transmutation-spec.md`**: editables ahora pero
  NO modificadas en esta sesion. La compactacion es Fase 2b dedicada.
- **`md-spec.md`**: sin cambios.
- **Vector PMI × LFS, atlas, familias documentales, pipelines de
  curacion, regimenes URN, leyes algebraicas de relations, adjuncion
  Check ⊣ Fix**: todo lo categorial vigente se preserva.

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 640 artefactos indexados (era 638; +ADR v7 + hermes-runtime-extension) |
| `python3 toolchain/kora check --strict` | 28/29 verdes; 1 HIGH preexistente en `HANDOFF.md` del WIP del operador (status: handoff no canonico, no es mi cambio) |
| `python3 -m unittest discover -s tests` | resultado en commit (en background) |

## Decisiones doctrinales explicitas

### Hermes pasa de bloqueado a canonico

Antes (gobernanza v5.0 §8.2): *"`Hermes` NO es runtime target vigente.
Toda mencion a Hermes fuera de docs historicas se interpreta como
bloqueada hasta que exista una decision HITL nueva..."*.

Ahora (v6.0 §8.2): *"`Hermes` ES runtime target canonico de KORA desde
la decision HITL del 2026-05-20. Critical path: claude-code, codex,
openclaw, hermes (cuatro)."*

La regla previa funciono — Hermes estaba bloqueado, no apareciaen
artefactos productivos. La activacion ahora es deliberada y trazable.

### Freeze parcial: harness queda, autoria y transmutation se bajan

Antes (gobernanza v5.0 §8.3): freeze formal sobre las 3 specs core.

Ahora (v6.0 §8.3): solo `harness-spec` sigue en freeze (es ontologia
PMI × LFS, base de todo lo categorial). `autoria-spec` y
`transmutation-spec` son editables porque su compactacion es la mayor
oportunidad de simplificacion que queda en KORA.

### Lista de runtimes definitiva (KORA v7)

Cuatro canonicos: `claude-code`, `codex`, `openclaw`, `hermes`.

Cuatro archivados (preservan URN para trazabilidad): `gemini`,
`mastra`, `opencode`, `agentskills`.

Cualquier reactivacion futura requiere HITL + ADR dedicado.

## Estado consolidado

### Que cerramos

- KORA esencial v7 declarado y materializado.
- Hermes activado como runtime canonico (stub publicado).
- Freeze parcial: harness preservado, autoria/transmutation editables.
- Drift `entornos_objetivo` en 5 skills limpiado.
- `custodio-kora` actualizado para reflejar el canon vigente.
- ADR v7 producido (refina y supersede aspectos de ADR v6).

### Que queda como Fase 2b (sesion dedicada futura)

1. **Compactar `autoria-spec` v1.2 → v2.0** (1194 → ~700 lineas).
2. **Compactar `transmutation-spec`** y consolidar con
   `runtime-spec-md`.
3. **Compactar `md-spec` v9 → v10** (1034 → ~700 lineas).
4. **Completar `hermes-runtime-extension` v0.1 → v1.0**: matriz de
   realizabilidad final, fidelity claims, shape runtime, mecanismos
   de capture, ejemplos.
5. **Verificacion empirica de hermes**: el dominio inicial es
   provisional; antes de transmutaciones productivas, verificar contra
   el runtime Hermes real.

### Que NO debe asumirse

- No asumir que hermes ya es target maduro: v0.1 es stub. Las
  transmutaciones a hermes son experimentales hasta v1.0.
- No asumir que el freeze cayo para harness: sigue en freeze. Solo
  `autoria-spec` y `transmutation-spec` son editables.
- No asumir que los runtimes archivados estan retirados
  permanentemente: el URN resuelve; el archivo persiste; cualquier
  reactivacion requiere HITL + ADR.

## Artefactos dejados versionados

### Specs
- `governance/gobernanza.md` v6.0.0.
- `runtime/hermes-runtime-extension.md` v0.1.0 (nuevo, stub).

### Toolchain
- `toolchain/kora_lib/transmute.py` (hermes en PRESERVATION_MATRIX, TARGET_ADAPTERS, TRACE_FIDELITY_BY_TARGET).
- `tests/common.py` (`ACTIVE_TARGETS` incluye hermes).

### Knowledge
- `artifacts/knowledge/kora/adr/adr-kora-v7-esencial.md` (publicado, familia adr).

### Artefactos productivos modificados (limpieza drift)
- 5 SKILL.md con `entornos_objetivo` limpiado.
- `custodio-kora/SKILL.md` + `custodio-kora/referencias/canon-operativo.md` actualizados.

### Docs
- `docs/handoffs/2026-05-20-kora-v7-esencial.md` (este).

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-20-kora-v7-esencial.md`.

Contexto vigente:

- gobernanza v6.0.0 establece KORA esencial v7:
  - 4 runtimes canonicos: claude-code, codex, openclaw, hermes.
  - Hermes activado (gobernanza §8.2 reescrita).
  - Freeze parcial: solo harness-spec sigue en freeze.
- hermes-runtime-extension v0.1.0 es stub; Fase 2b lo completa.
- ADR v7: urn:kora:kb:adr-kora-v7-esencial.

Para Fase 2b (sesion dedicada):

1. Compactar autoria-spec v1.2 → v2.0 (~700 lineas).
2. Compactar transmutation-spec + consolidar con runtime-spec-md.
3. Compactar md-spec v9 → v10.
4. Completar hermes-runtime-extension v1.0:
   - Matriz de realizabilidad final por (arnes, forma_material, vector).
   - Shape runtime (estructura de carpetas, archivos, metadata).
   - Mecanismos de aprobacion, sandbox, persistencia.
   - Fidelity claims verificadas empiricamente contra Hermes real.
   - Ejemplos de artefactos transmuted a hermes.
5. Verificacion empirica de hermes contra runtime real.

Mantener commits acotados. No tocar harness-spec sin ADR dedicado.
```
