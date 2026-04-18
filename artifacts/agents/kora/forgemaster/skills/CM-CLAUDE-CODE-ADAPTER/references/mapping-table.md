# Mapping Completo KORA → Claude Code Nativo

Referencia normativa para CM-CLAUDE-CODE-ADAPTER. Cada mapping incluye justificacion spec.

## Componentes Principales

| KORA | CC Nativo | Tipo | Spec |
|------|-----------|------|------|
| AGENTS.md (FSM + rules + co-induction + wiring) | Body del subagent (seccion principal) | behavior puro | agent-spec §4.1 |
| AGENTS.md Co-induccion | Hook Stop tipo prompt en frontmatter | enforcement mecanico | agent-spec §4.3 |
| AGENTS.md Contexto Multi-turno | Body del subagent (seccion §4) | instruccional | agent-spec §4.1 |
| AGENTS.md Wiring | tools: Agent(ns--name) en frontmatter | enforcement server-side | agent-spec §8, swarm-spec §3.1 |
| SOUL.md | Body del subagent (seccion superior) | identity only | agent-spec §4.4.2 |
| USER.md | EXCLUIDO | plataforma lo provee | runtime-spec §6.1 |
| TOOLS.md semantico | Body del subagent (routing maps) | instruccional | agent-spec §5 |
| TOOLS.md → config.json.tools.allow | tools field en frontmatter | enforcement server-side | agent-spec §5 |
| config.json tools.deny | disallowedTools field | enforcement server-side | runtime enforcement |
| config.json sandbox.mode | permissionMode field | enforcement server-side | runtime-spec §3.2 |
| config.json model_routing | model field | enforcement server-side | runtime-spec §7 |
| config.json limits | maxTurns + effort fields | enforcement server-side | runtime-spec §8 |
| config.json sub_agents | tools: Agent(...) restriction | enforcement server-side | swarm-spec §3.1 |
| config.json allowed_kb | Instruccion en body | DEGRADADO a instruccional | runtime-spec §3.2 (gap) |
| config.json runtime_capabilities | Absorcion parcial en permissionMode + disallowedTools | parcial | M6 |
| Cada CM-* | .claude/skills/{ns}--{name}--{cm}/SKILL.md | lazy-load nativo | skill-spec §3 |
| CM Core (4 secciones) | SKILL.md body | preservado intacto | skill-spec §3 |
| CM scripts/refs/assets | SKILL.md directory (copiados) | preservado | skill-spec §3.2 |

## Mapping Sandbox Mode

| KORA sandbox.mode | CC permissionMode | Semantica |
|-------------------|-------------------|-----------|
| strict | plan | Solo lectura, sin ejecucion |
| isolated | acceptEdits | Edits auto-aprobados, bash con prompt |
| permissive | default | Prompts normales |
| off | bypassPermissions | Sin restricciones (no recomendado) |

## Naming Convention (M5)

- Separador de namespace: doble guion `--`
- Formato subagent: `{namespace}--{nombre}`
- Formato skill: `{namespace}--{nombre}--{cm}`
- Ejemplos:
  - `kora--custodio` (subagent)
  - `kora--custodio--intent-classifier` (skill)
  - `dev--steipete--code-reviewer` (skill)

## Exclusiones Documentadas

| Componente | Razon | Justificacion |
|------------|-------|---------------|
| USER.md | Plataforma provee contexto operador nativamente | runtime-spec §6.1 (H1) |
| config.json (como texto) | Informo frontmatter server-side; no se copia | runtime-spec §9.2 |
| _manifest frontmatter | Stripping obligatorio | runtime-spec §9.2 (R-TRANSMUTE-2) |

## Enforcement Gaps Conocidos

| Constraint | Nivel Original (KORA) | Nivel Efectivo (CC) | Mitigacion |
|------------|----------------------|---------------------|------------|
| allowed_kb | server-side (config.json) | instruccional (body) | MCP kb-reader o hook pre-tool (H3) |
| runtime_capabilities | server-side | parcial (permissionMode + disallowedTools) | Documentar gaps en manifest (M6) |
| swarm depth > 1 | declarativo (wiring) | no soportado (depth 1) | Orquestador como main thread (M1) |
| circuit breakers | declarativo (swarm-spec) | instruccional + hooks | hooks parcial, documentar (M2) |

## Swarm: Patron de Composicion (M1)

Para namespaces tipo swarm:

```
# Orquestador como main thread (agente degradado):
.claude/settings.json → "agent": "{ns}--orchestrator"

# Workers como subagents invocables:
.claude/agents/{ns}--worker1.md
.claude/agents/{ns}--worker2.md

# Orquestador tiene wiring en tools:
tools: Agent({ns}--worker1, {ns}--worker2), Read, Glob, Grep
```

Limitacion aceptada: depth 1. El orquestador pierde config.json enforcement y lifecycle auditable propio (M1).
