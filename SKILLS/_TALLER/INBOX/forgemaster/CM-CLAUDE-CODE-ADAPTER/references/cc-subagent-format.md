# Claude Code — Formato Nativo de Subagent

Referencia operativa para CM-CLAUDE-CODE-ADAPTER. Fuente: KNOWLEDGE/dev/claude-code-mastery/extensibilidad.md (CC v2.1.81, 2026-03-22).

## Ubicacion

- Proyecto: `.claude/agents/{name}.md` o `.claude/agents/{name}/AGENT.md`
- Global: `~/.claude/agents/`

## Frontmatter (Server-Side Enforcement)

El frontmatter YAML es aplicado por el runtime CC, NO inyectado como texto al LLM.

```yaml
---
name: kebab-case-identifier          # max 64 chars, requerido
description: "Que hace + cuando usar" # requerido
model: opus | sonnet | haiku          # opcional, hereda del padre
effort: low | medium | high | max     # opcional
maxTurns: 50                          # integer, cap de tool-use turns
permissionMode: default | plan | acceptEdits | dontAsk | bypassPermissions
tools: Read, Grep, Glob, Bash(npm run *), Agent(worker-1, worker-2)
disallowedTools: Write, Edit
skills:
  - skill-name-1
  - skill-name-2
memory: user | project | local
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verificacion... $ARGUMENTS"
          model: haiku
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate.sh"
---
```

## Campos clave

| Campo | Tipo | Server-side | Notas |
|-------|------|-------------|-------|
| name | string | Si | Identificador unico, kebab-case |
| description | string | Si | Usado para discovery; siempre en contexto |
| model | enum | Si | No se inyecta al LLM; runtime lo aplica |
| permissionMode | enum | Si | Enforcement mecanico de sandbox |
| tools | list | Si | Whitelist de tools permitidas |
| disallowedTools | list | Si | Blacklist de tools prohibidas |
| maxTurns | int | Si | Budget de turns mecanico |
| skills | list | Si | Skills pre-cargadas para el subagent |
| hooks | object | Si | Lifecycle hooks con 4 tipos de handler |

## Body (System Prompt)

Todo contenido despues del cierre `---` del frontmatter es el system prompt del subagent. Formato Markdown.

## Tipos de Hook Handler

| Tipo | Mecanismo | Uso |
|------|-----------|-----|
| command | Script local, exit 0=ok, exit 2=block | Validacion, lint |
| http | POST a URL, 2xx=ok | Webhook externo |
| prompt | LLM como juez, retorna {ok, reason} | Co-induccion |
| agent | Subagente multi-turn con tools | Verificacion compleja |

## Eventos de Hook relevantes

- `Stop`: Cuando el agente termina respuesta (co-induccion)
- `PreToolUse`: Antes de ejecutar tool (gate)
- `PostToolUse`: Despues de ejecutar tool (audit)
- `SubagentStart`/`SubagentStop`: Lifecycle de subagentes

## Limitaciones

- Subagents NO pueden spawnar sub-subagents (depth 1 unicamente).
- tools field es whitelist; no hay wildcards.
- description siempre en contexto (~100 tokens por subagent registrado).
- Sin mecanismo nativo para filtrar acceso a knowledge bases.
