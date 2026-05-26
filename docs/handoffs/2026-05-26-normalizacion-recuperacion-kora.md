---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-26-normalizacion-recuperacion-kora"
  provenance:
    created_by: "Codex"
    created_at: "2026-05-26"
    source: "Cierre operativo solicitado por HITL: documentar estado, memoria, pendientes, riesgos, commit y push controlado del pase de normalizacion/recuperacion KORA."
version: "1.0.0"
status: publicado
tags: [handoff, recuperacion, normalizacion, agents, skills, knowledge, codex, claude-code, openclaw]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:plan-normalizacion-recuperacion-kora-2026-05-26"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:transmutation-spec"
---

# Handoff 2026-05-26 - normalizacion y recuperacion KORA

## Estado actual

Se completo un primer pase ejecutable para normalizar y recuperar artefactos KORA
desde el IR local y desde runtimes Codex, Claude Code y OpenClaw.

Inventario reproducible:

```bash
python3 toolchain/kora recovery-inventory --json
```

Snapshot verificado el 2026-05-26:

| Area | Estado |
|------|--------|
| Agents canonicos | 6 |
| Skills canonicos | 32 |
| Knowledge canonico | 575 |
| Gaps `provenance.source` en knowledge canonico | 0 |
| Codex skills externos | 43 totales, 38 mapeados, 5 orfanos de sistema |
| Claude skills externos | 34 totales, 34 mapeados |
| Claude agents externos | 13 totales; 9 mapeados o staged en el commit atomico; 4 pendientes |
| OpenClaw workspaces | 9 totales; 7 mapeados en canon; `main` y `fugaz` quedan fuera del commit atomico |

## Decisiones

1. La direccion de verdad sigue siendo:

```text
fuentes originales -> KORA IR -> runtime outputs
runtime outputs mejores -> REVIEW -> KORA IR -> runtime outputs
```

2. Los runtimes externos no pisan artefactos productivos. Entran como candidatos
en `_FRAGUA/INBOX` o `_TALLER/INBOX`, con trazabilidad de fuente y gates antes
de promocion.

3. Se excluyen los Codex `.system` skills (`imagegen`, `openai-docs`,
`plugin-creator`, `skill-creator`, `skill-installer`) como fuente KORA: son
capacidades del runtime, no artefactos propios.

4. No se promueven memorias OpenClaw crudas. Las memorias y workspaces pueden
contener PII, endpoints, credenciales o continuidad operacional sensible. Solo
se recuperan deltas doctrinales redactados.

5. `_BUILD`, `_archivo` y `_rebuild_required` no son fuentes vigentes para el
gate de construccion; son derivados, archivo o zonas de reconstruccion.

## Artefactos relevantes

Tooling:

- `toolchain/kora_lib/recovery.py`
- `toolchain/kora_lib/cli.py`
- `toolchain/kora_lib/checks.py`

Tests:

- `tests/test_recovery_inventory.py`
- `tests/test_cli_smoke.py`
- `tests/test_check_pipeline.py`

Plan:

- `docs/plans/2026-05-26-normalizacion-recuperacion-kora.md`

Skills recuperados a staging:

- `artifacts/skills/_TALLER/INBOX/jobs-web-ux/SKILL.md`
- `artifacts/skills/_TALLER/INBOX/database-designer/SKILL.md`

Agentes recuperados a staging y refinados:

- `artifacts/agents/_FRAGUA/INBOX/agent-architect/AGENT.md`
- `artifacts/agents/_FRAGUA/INBOX/polymath/AGENT.md`

Knowledge normalizado:

- `artifacts/knowledge/tde/**`
- `artifacts/knowledge/salud/med-emergencia/body-of-knowledge-diferencial.md`

## Verificacion

Gates ejecutados en el pase:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora kb-graph --json --orphans
python3 -m unittest discover -s tests
```

Ultimo resultado verificado antes del cierre:

- `index`: 641 artefactos indexados.
- `check --strict`: 34/34 checks OK.
- `kb-graph`: 598 nodos, 977 aristas, 6 orfanos reales, 0 broken edges.
- `unittest`: 336 tests OK.

## Pendientes

1. Promocionar o rechazar `jobs-web-ux`, `database-designer`,
`agent-architect` y `polymath` desde staging despues de revision HITL.

2. Comparar candidatos Claude Code con artefactos existentes antes de crear
nuevos productivos:

- `ifml-architect` contra `urn:kora:artefacto:ifml`.
- `opm-specialist` contra `urn:kora:artefacto:modelamiento-opm`.
- `ux-research-design-ai` contra `urn:kora:artefacto:ux-design`.

3. Reconstruir `forjador-openclaw` solo desde specs vivas y material redactado;
no usarlo como canon bruto.

4. Mantener `fugaz` y `main` OpenClaw fuera del canon hasta extraer doctrina
no sensible.

5. Continuar recuracion profunda desde fuentes originales por namespaces:
`salud`, `gn`, `legal`, `sii`, `fxsl`, `agengai`, `ops`, `pro`, `dev`.

## Supuestos

- El repo local estaba sucio antes del pase, con poda y cambios ajenos en
documentacion, skills productivas y toolchain. El commit de cierre debe aislar
solo este trabajo.
- Los artefactos en staging son borradores recuperados, no producto canonico.
- El catalogo generado no se usa como fuente de verdad; se regenera desde IR.
- El worktree local puede contener candidatos crudos no comiteados; no usarlos
  como canon ni asumir que existen tras clonar `origin/master`.

## Riesgos

- Riesgo de sobre-ingesta: material runtime puede parecer mejor que el IR, pero
mezcla contexto operacional y secretos. Mitigacion: staging + revision.
- Riesgo de deriva en runtimes: los hashes externos rara vez coinciden con IR.
Mitigacion: `recovery-inventory` muestra mapping y hash por item.
- Riesgo de commit contaminado: el worktree incluye cambios ajenos. Mitigacion:
stage explicito por path y revision de `git diff --cached`.

## Memoria operativa

El estado util para retomar es:

- El primer pase ya dejo inventario, gates y provenance base normalizados.
- La recuperacion productiva todavia no esta cerrada; esta en etapa de staging.
- La siguiente decision relevante no es tecnica sino de curadoria: que candidatos
se promueven, fusionan o descartan.
- Nunca tomar OpenClaw `MEMORY.md` como fuente directa.
- Usar `docs/plans/2026-05-26-normalizacion-recuperacion-kora.md` como ledger
del plan y este handoff como punto de reentrada.

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde
docs/handoffs/2026-05-26-normalizacion-recuperacion-kora.md.

Objetivo inmediato: revisar candidatos staging recuperados
(`jobs-web-ux`, `database-designer`, `agent-architect`, `polymath`) y decidir
promocion, fusion o descarte. No ingieras memorias OpenClaw crudas. Verifica
con `python3 toolchain/kora recovery-inventory --json`,
`python3 toolchain/kora check --strict` y tests acotados antes de promover.
```
