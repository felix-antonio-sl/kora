---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-31-cierre-contextualizacion-y-recuperacion-kora"
  provenance:
    created_by: "Codex"
    created_at: "2026-05-31"
    source: "Cierre operativo solicitado por HITL: documentar estado, memoria, pendientes, riesgos, commit semantico y push controlado de cambios acumulados sin commit."
version: "1.0.0"
status: publicado
tags: [handoff, contexto, recuperacion, opm, codex, claude-code, openclaw, hermes, continuidad]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-05-31 - contextualizacion y recuperacion KORA

## Estado actual

Se cierra un lote acumulado de cambios sin commit que consolida el arranque
contextualizado de agentes, limpia material historico redundante y deja nuevos
candidatos de recuperacion en staging.

El commit anterior de la misma fecha ya restauro `AGENTS.md` como entrypoint
Codex minimo, redirigido a `CLAUDE.md`. Este handoff documenta el siguiente
cierre: el resto del worktree pendiente.

## Cambios principales

1. Contexto operativo de agentes:
   - `CLAUDE.md` pasa a expresar de forma compacta la fuente operativa unica.
   - `.gemini/GEMINI.md` queda reducido a una guia de entrada que remite a
     `CLAUDE.md`, `governance/gobernanza.md` y `docs/start-prompt.md`.
   - `docs/start-prompt.md` incorpora la definicion vigente de KORA como
     repositorio, catalogo y sistema de produccion/mantenimiento de tres tipos
     de artefacto.
   - `docs/README.md` explicita que `docs/` es auxiliar y no normativo.
   - `README.md` root se retira para evitar segunda puerta operativa.

2. Gobernanza:
   - `governance/gobernanza.md` incorpora la definicion HITL del 2026-05-31:
     KORA gestiona conocimiento, agentes y skills; las specs son ley, no
     artefactos; la ecuacion categorial es garantia formal, no definicion.

3. Poda y reduccion de archivo historico:
   - Se retiran handoffs historicos archivados bajo
     `governance/decisiones-archivadas/handoffs-historicos/`.
   - Se retira corpus HODOM/glosario versionado en
     `artifacts/knowledge/salud/salubrista/hodom/`.
   - Se elimina `.claude/scheduled_tasks.lock`.

4. Recuperacion y staging:
   - Se agregan candidatos `AGENT.md` en `_FRAGUA/INBOX`: `forjador-openclaw`,
     `fugaz`, `ifml-architect`, `opm-specialist`, `ux-research-design-ai`.
   - Se agrega `artifacts/skills/dev/hermes-agent-specialist/SKILL.md`.
   - Se consolida `urn:fxsl:kb:metodologia-forja-opm-es` como SSOT
     metodologica para OPM-en-opforja.
   - Se referencian `urn:fxsl:kb:reglas-opm-estrictas-es` y
     `urn:fxsl:kb:spec-forja-opl-es` como capas operativas de canon OPM/OPL
     para opforja/deep-opm-pro.

5. Skills y transmutacion:
   - Varias skills declaran `conocimiento_permitido` explicito.
   - `modelamiento-opm` sube a v1.3.0 e incorpora
     `urn:fxsl:kb:metodologia-forja-opm-es` como metodo primario para
     opforja/deep-opm-pro.
   - `transmute.py` preserva el contrato de conocimiento en bundles Codex y
     evita duplicar secciones inline `## Knowledge Contract`.

6. Toolchain/tests:
   - `doctor.py` deja de buscar `docs/reports`.
   - `config.py` deja de tratar handoffs historicos archivados como zona
     escaneable/indexable especial tras su retiro.
   - Tests se ajustan al retiro de memoria historica OpenClaw y a la nueva
     proyeccion de knowledge contract en Codex.

## Decisiones

- `CLAUDE.md` queda como puerta operativa canonica; wrappers de runtime solo
  redirigen.
- `docs/handoffs/` sigue siendo continuidad viva; los handoffs historicos
  archivados retirados no deben reintroducirse sin nueva decision HITL.
- Los artefactos en `_FRAGUA/INBOX` son borradores recuperados, no canon.
- `metodologia-forja-opm-es` orienta el metodo de trabajo en opforja, pero no
  redefine validez semantica OPM, que sigue en `opm-es`, `opd-es` y `opl-es`.
- El commit debe ser unico porque el worktree ya estaba acoplado por referencias
  cruzadas entre contexto, poda, recovery, toolchain y tests.

## Artefactos relevantes

- `CLAUDE.md`
- `.gemini/GEMINI.md`
- `docs/start-prompt.md`
- `docs/README.md`
- `governance/gobernanza.md`
- `artifacts/knowledge/fxsl/opm/opm-ssot-es/metodologia-forja-es.md`
- `artifacts/knowledge/fxsl/opm/opm-ssot-es/reglas-opm-estrictas-es.md`
- `artifacts/knowledge/fxsl/opm/opm-ssot-es/spec-forja-opl-es.md`
- `artifacts/skills/kora/modelamiento-opm/SKILL.md`
- `artifacts/skills/dev/hermes-agent-specialist/SKILL.md`
- `toolchain/kora_lib/transmute.py`
- `tests/test_skill_transmute_codex.py`

## Pendientes

1. Revisar y decidir promocion, fusion o descarte de los agentes en
   `_FRAGUA/INBOX`.
2. Revisar `hermes-agent-specialist` contra `runtime/hermes-runtime-extension.md`
   antes de proyectarlo como canon estable.
3. Mantener la coherencia entre `metodologia-forja-opm-es`,
   `reglas-opm-estrictas-es`, `spec-forja-opl-es` y la skill
   `modelamiento-opm` cuando evolucione opforja/deep-opm-pro.
4. Si reaparece necesidad historica de handoffs retirados, recuperar desde git
   con ADR/HITL explicito, no por restauracion silenciosa.

## Supuestos

- El host local es `primary` y puede pushear `master` a `origin`.
- El usuario pidio cerrar todos los cambios sin commit como lote operativo.
- Los cambios acumulados son coherentes como cierre de normalizacion y
  contextualizacion, aunque internamente mezclen docs, poda, staging y toolchain.
- La memoria persistente local se actualiza fuera del repo; no viaja en git.

## Riesgos

- Riesgo de commit amplio: mitigado por handoff explicito, diff revisado y
  verificacion antes de push.
- Riesgo de referencias rotas por retiro de archivos historicos: mitigado por
  `kora check --strict` y tests.
- Riesgo de sobrecanonizar staging recuperado: mitigado declarando esos agentes
  como borradores en `_FRAGUA/INBOX`.
- Riesgo de drift en wrappers de runtime: mitigado al reducirlos a redireccion
  hacia `CLAUDE.md`.

## Prompt de continuacion

Ver `docs/handoffs/2026-05-31-cierre-contextualizacion-y-recuperacion-kora-prompt-continuacion.md`.
