---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-29-steipete-opencode-transmutation"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-29"
    source: "Cierre de sesion: auditoria estricta de personas steipete/allan-kelly, transmutacion multi-runtime de steipete y skills composables, y cierre de brechas toolchain para opencode/openclaw."
version: "1.0.0"
status: publicado
tags: [handoff, steipete, allan-kelly, opencode, openclaw, codex, claude-code, transmutacion, skills]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:dev:artefacto:steipete"
    - "urn:fxsl:artefacto:allan-kelly"
    - "urn:dev:artefacto:ship-discipline"
    - "urn:kora:artefacto:kora-agents"
    - "urn:kora:artefacto:kora-skills"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:opencode-runtime-extension"
    - "urn:agengai:kb:openclaw-runtime-extension"
---

# Handoff - Steipete Multi-Runtime Transmutation

## Estado actual

La auditoria estricta de `fxsl/allan-kelly` y `dev/steipete` quedo cerrada.
Ambos agentes fueron ajustados para evitar lenguaje de clon/impersonation,
declarar API observable, registrar riesgos y no afirmar seguridad
coalgebraica verificable sin `plan.fsm` formal.

`dev/steipete` y `fxsl/allan-kelly` quedaron transmutados a:

- `claude-code`
- `codex`
- `opencode`
- `openclaw`

Sus skills composables productivas tambien quedaron transmutadas a esos cuatro
targets:

- `dev/ship-discipline`
- `fxsl/cell-design`
- `kora/mente-omega`
- `kora/cat-thinking`
- `kora/artifact-curator`
- `kora/kora-agents`
- `kora/kora-skills`

Los outputs bajo `_BUILD/` son derivados y gitignored. Se regeneran con
`python3 toolchain/kora transmute`.

## Decisiones

1. `steipete` y `allan-kelly` son personas sinteticas inspiradas, no clones ni
   representantes reales de Peter Steinberger o Allan Kelly.
2. `ship-discipline` y `steipete` no pueden tratar commit como parte implicita
   del loop closure: el default es patch listo; commit solo con autorizacion
   explicita o protocolo de repo.
3. `opencode` es target formal de transmutacion tambien en
   `serialization/schemas/kora-artefacto.json` y en `autoria-spec`.
4. Para agentes, la toolchain ya no debe quedarse solo en
   `_transmutation.yml` cuando el target es `codex`, `opencode` u
   `openclaw`.
5. Salidas materiales de agentes:
   - Claude Code: `{agent}.md`
   - Codex: `{agent}.md`
   - OpenCode: `agents/{agent}.md`
   - OpenClaw: workspace markdown completo + `config/openclaw.json5` +
     `DEPLOY.md`
6. Para skills, `openclaw` usa layout `skills/{skill}/SKILL.md`; Codex y
   OpenCode usan bundles agentskills-compatible con `referencias/ ->
   references/` y `recursos/ -> assets/`.
7. Se corrigio una flake real de `atomize`: slugs largos numericos no deben
   confundirse con sufijos de segmento `-01`/`-100` al calcular
   `bundle_root` y review path.

## Artefactos versionados relevantes

- `artifacts/agents/dev/steipete/AGENT.md`
- `artifacts/agents/fxsl/allan-kelly/AGENT.md`
- `artifacts/skills/dev/ship-discipline/SKILL.md`
- `serialization/autoria-spec.md`
- `serialization/schemas/kora-artefacto.json`
- `serialization/schemas/kora-transmutation-schema.json`
- `toolchain/kora_lib/transmute.py`
- `toolchain/kora_lib/promote.py`
- `artifacts/skills/kora/atomize/scripts/review_atomic_acceptance.py`
- `tests/test_agent_transmute_runtime_outputs.py`
- `tests/test_skill_transmute_openclaw.py`
- `tests/test_skill_transmute_opencode.py`
- `tests/test_atomize.py`

## Artefactos derivados locales

Agente `steipete`:

- `artifacts/agents/dev/steipete/_BUILD/claude-code/steipete.md`
- `artifacts/agents/dev/steipete/_BUILD/codex/steipete.md`
- `artifacts/agents/dev/steipete/_BUILD/opencode/agents/steipete.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/AGENTS.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/SOUL.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/IDENTITY.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/USER.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/TOOLS.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/BOOT.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/MEMORY.md`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/config/openclaw.json5`
- `artifacts/agents/dev/steipete/_BUILD/openclaw/DEPLOY.md`

Agente `allan-kelly`:

- `artifacts/agents/fxsl/allan-kelly/_BUILD/claude-code/allan-kelly.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/codex/allan-kelly.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/opencode/agents/allan-kelly.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/workspace/AGENTS.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/workspace/SOUL.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/workspace/IDENTITY.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/workspace/USER.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/workspace/TOOLS.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/workspace/BOOT.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/workspace/MEMORY.md`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/config/openclaw.json5`
- `artifacts/agents/fxsl/allan-kelly/_BUILD/openclaw/DEPLOY.md`

Skills `steipete`:

- `artifacts/skills/dev/ship-discipline/_BUILD/{claude-code,codex,opencode}/ship-discipline/SKILL.md`
- `artifacts/skills/dev/ship-discipline/_BUILD/openclaw/skills/ship-discipline/SKILL.md`
- `artifacts/skills/fxsl/cell-design/_BUILD/{claude-code,codex,opencode}/cell-design/SKILL.md`
- `artifacts/skills/fxsl/cell-design/_BUILD/openclaw/skills/cell-design/SKILL.md`
- `artifacts/skills/kora/mente-omega/_BUILD/{claude-code,codex,opencode}/mente-omega/SKILL.md`
- `artifacts/skills/kora/mente-omega/_BUILD/openclaw/skills/mente-omega/SKILL.md`
- `artifacts/skills/kora/cat-thinking/_BUILD/{claude-code,codex,opencode}/cat-thinking/SKILL.md`
- `artifacts/skills/kora/cat-thinking/_BUILD/openclaw/skills/cat-thinking/SKILL.md`
- `artifacts/skills/kora/artifact-curator/_BUILD/{claude-code,codex,opencode}/artifact-curator/SKILL.md`
- `artifacts/skills/kora/artifact-curator/_BUILD/openclaw/skills/artifact-curator/SKILL.md`
- `artifacts/skills/kora/kora-agents/_BUILD/{claude-code,codex,opencode}/kora-agents/SKILL.md`
- `artifacts/skills/kora/kora-agents/_BUILD/openclaw/skills/kora-agents/SKILL.md`
- `artifacts/skills/kora/kora-skills/_BUILD/{claude-code,codex,opencode}/kora-skills/SKILL.md`
- `artifacts/skills/kora/kora-skills/_BUILD/openclaw/skills/kora-skills/SKILL.md`

## Verificacion ejecutada

- `python3 toolchain/kora index`: OK, 649 artefactos indexados antes de este
  handoff.
- `python3 toolchain/kora check --strict`: 30/30 OK.
- `python3 -m unittest discover -s tests`: 334 tests OK, 1 skipped.
- `git diff --check`: OK.

## Pendientes

1. Decidir si los outputs `_BUILD/` deben instalarse en runtimes locales:
   `~/.claude/agents`, `~/.codex/skills`, `.opencode/agents`,
   `.opencode/skills` u OpenClaw fleet.
2. Ejecutar validacion runtime real fuera de KORA:
   - Claude Code: invocacion del agente `steipete`.
   - Codex: uso del prompt/bundle `steipete.md`.
   - OpenCode: carga de `agents/steipete.md` y skills asociadas.
   - OpenClaw: sync de `workspace/` y `openclaw doctor`.
3. Si se requiere paridad total, evaluar emisores materiales de agente para
   `gemini` y `mastra`; hoy el cierre fue sobre los targets pedidos.
4. Si se va a publicar PR o release, revisar si conviene separar en dos commits:
   auditoria de artefactos vs toolchain multi-runtime.

## Supuestos

- `master` es la rama principal activa.
- `_BUILD/` sigue siendo derivado y gitignored.
- El contrato de OpenClaw productivo requiere runtime state externo:
  credenciales, pairing stores, sesiones, caches y config de gateway.
- `opencode` ya existe como runtime extension y target de CLI; faltaba
  aceptarlo en schema de autoría y emitir material de agente.

## Riesgos

- Los bundles de agente Codex/OpenCode son proyecciones mecanicas. La prueba
  runtime real aun debe hacerse en los CLIs correspondientes.
- El workspace OpenClaw emitido es blueprint sincronizable; no instala tokens ni
  registra systemd/gateway por si mismo.
- La semantica de permisos OpenCode usa defaults conservadores (`ask`/`deny`)
  salvo override futuro en `extensions.opencode`.
- Si se cambia la convencion de segmentos atomic, mantener sincronizados
  `review_atomic_acceptance.py` y `toolchain/kora_lib/promote.py`.
