---
_manifest:
  urn: "urn:kora:kb:handoff-2026-06-04-agentes-prioridad-alta-opencode"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Cierre operativo solicitado por HITL: promover agentes desplegados desde staging sin fuente productiva, reactivar OpenCode, documentar estado, consolidar memoria, commitear y pushear."
version: "1.0.0"
status: publicado
tags: [handoff, agentes, opencode, runtime, despliegue, prioridad-alta]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-06-04 - agentes prioridad alta y OpenCode

## Estado actual

Se cerraron dos lineas de trabajo relacionadas:

1. Siete agentes desplegados desde staging quedaron promovidos a fuentes
   productivas KORA agnosticas:
   - `urn:dev:artefacto:agent-architect`
   - `urn:dev:artefacto:forjador-openclaw`
   - `urn:dev:artefacto:fugaz`
   - `urn:dev:artefacto:ifml-architect`
   - `urn:fxsl:artefacto:opm-specialist`
   - `urn:dev:artefacto:polymath`
   - `urn:dev:artefacto:ux-research-design-ai`
2. `opencode` fue reactivado como runtime canonico KORA por HITL del
   2026-06-04. La spec vive ahora en `runtime/opencode-runtime-extension.md`.

Los siete drafts equivalentes fueron removidos de
`artifacts/agents/_FRAGUA/INBOX/` para evitar divergencia staging/productivo.

## Decisiones

1. `forjador-openclaw` se reconstruyo como agente agnostico base, no como copia
   literal del runtime desplegado. Se excluyeron rutas operacionales, estado vivo
   y detalles sensibles del host.
2. `opm-specialist`, `ifml-architect` y `ux-research-design-ai` quedaron como
   agentes de conduccion/juicio que componen con skills productivas
   (`modelamiento-opm`, `ifml`, `ux-design`) en vez de duplicar mecanica.
3. La reactivacion de `opencode` se registro en `gobernanza` v6.2.0. OpenCode
   ya no requiere `--force-paused` y puede declararse en `entornos_objetivo`.
4. Los siete agentes promovidos declaran targets canonicos:
   `claude-code`, `codex`, `openclaw`, `opencode`.
5. `hermes` sigue canonico, pero estos siete agentes no lo declaran porque la
   extension Hermes continua en stub y no se verifico el caso concreto.

## Artefactos relevantes

- `runtime/opencode-runtime-extension.md`
- `governance/gobernanza.md`
- `CLAUDE.md`
- `toolchain/kora_lib/transmute.py`
- `toolchain/kora_lib/cli.py`
- `tests/test_cli_smoke.py`
- `tests/test_agent_transmute_runtime_outputs.py`
- `tests/test_skill_transmute_opencode.py`
- `artifacts/agents/dev/agent-architect/AGENT.md`
- `artifacts/agents/dev/forjador-openclaw/AGENT.md`
- `artifacts/agents/dev/fugaz/AGENT.md`
- `artifacts/agents/dev/ifml-architect/AGENT.md`
- `artifacts/agents/fxsl/opm-specialist/AGENT.md`
- `artifacts/agents/dev/polymath/AGENT.md`
- `artifacts/agents/dev/ux-research-design-ai/AGENT.md`

## Despliegue

Los siete agentes fueron transmutados y desplegados localmente en:

- Claude Code: `/home/felix/.claude/agents/{name}.md`
- Codex: `/home/felix/.codex/skills/{name}/`
- OpenCode: `/home/felix/.config/opencode/agents/{name}.md`
- OpenClaw: `/home/felix/openclaw-fleet/workspaces/{name}/`

OpenClaw aparece como `unsupported` en `deploy-status` porque esa vista no
compara hashes de workspaces OpenClaw; la existencia de destinos y el deploy se
verificaron con `deploy-builds`.

## Validacion ejecutada

- `python3 toolchain/kora index`
- `python3 toolchain/kora resolve urn:kora:kb:opencode-runtime-extension`
- `python3 toolchain/kora transmute --target opencode --agent dev/steipete --dry-run`
- `python3 toolchain/kora validate --profile strict`
- `python3 toolchain/kora check --strict`
- `python3 -m unittest tests.test_cli_smoke tests.test_agent_transmute_runtime_outputs tests.test_skill_transmute_opencode`
- `python3 -m unittest discover -s tests`
- `git diff --check`

Resultados finales antes de commit:

- `check --strict`: 34/34 OK.
- `validate --profile strict`: 14 workspaces validos, 0 invalidos.
- tests especificos OpenCode/CLI: 30 tests OK.
- suite completa: 336 tests OK.
- `git diff --check`: OK.

## Pendientes

- Auditar los siguientes grupos del inventario de despliegues sin fuente KORA:
  - skills desplegadas con fuente staging o sin fuente productiva.
  - artefactos desplegados con mismatch de tipo agente/skill.
  - runtime workspaces no propios o no autorales antes de promover.
- Evaluar si algun agente productivo debe declarar `hermes` cuando la extension
  Hermes salga de stub o se verifique un caso concreto.

## Supuestos

- La instruccion HITL "despausa opencode" es autoridad suficiente para
  reactivar OpenCode conforme a gobernanza §8.4, que exigia HITL explicito.
- Los siete agentes son de autoria/propiedad del operador y por eso deben tener
  fuente productiva KORA.
- Los outputs `_BUILD/` siguen siendo derivados e ignorados por git.

## Riesgos

- OpenCode tiene perdidas declaradas en memoria/identidad persistente y algunos
  ejes de interaccion; cada transmutacion conserva esas perdidas en
  `_transmutation.yml`.
- OpenClaw deploy-status no compara hash de workspace, por lo que la evidencia
  de deploy OpenClaw se basa en `deploy-builds --apply --overwrite` y presencia
  de directorios destino.
- Los nuevos agentes son bases agnosticas normalizadas; pueden requerir
  enriquecimiento posterior por uso vivo.
