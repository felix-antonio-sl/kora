---
_manifest:
  urn: "urn:dev:kb:claude-code-mastery"
  type: "knowledge_article"
  version: "1.0.0"
title: "Claude Code Mastery — Extensibilidad"
domain: "dev"
tags: [claude-code, hooks, skills, subagentes, mcp, plugins, channels]
last_updated: "2026-03-22"
parent: "urn:dev:kb:claude-code-mastery"
---

# Extensibilidad: Hooks, Skills, Agentes, MCP, Plugins, Channels

## 1. Hooks — 22 Eventos × 4 Tipos Handler

### Eventos del Lifecycle

| Evento | Cuándo | ¿Puede bloquear? | Matcher filtra por |
|--------|--------|-------------------|---------------------|
| `SessionStart` | Sesión inicia/resume | No | startup, resume, clear, compact |
| `SessionEnd` | Sesión termina | No | clear, resume, logout, prompt_input_exit |
| `InstructionsLoaded` | CLAUDE.md/.rules cargado | No | session_start, nested_traversal, include, compact |
| `UserPromptSubmit` | Prompt enviado, pre-proceso | Sí | — |
| `PreToolUse` | Antes de tool call | Sí | tool name: `Bash`, `Edit\|Write`, `mcp__.*` |
| `PermissionRequest` | Dialog de permiso aparece | Sí | tool name |
| `PostToolUse` | Tool call exitoso | No | tool name |
| `PostToolUseFailure` | Tool call falla | No | tool name |
| `Notification` | Notificación enviada | No | permission_prompt, idle_prompt, auth_success |
| `SubagentStart` | Subagente spawned | No | agent type: Bash, Explore, Plan, custom |
| `SubagentStop` | Subagente finaliza | Sí | agent type |
| `Stop` | Claude termina respuesta | Sí | — |
| `StopFailure` | Turno termina por error API | No | rate_limit, auth_failed, billing_error, etc. |
| `TeammateIdle` | Teammate a punto de idle | Sí | — |
| `TaskCompleted` | Task marcado completo | Sí | — |
| `ConfigChange` | Config file cambia | Sí | user/project/local/policy_settings, skills |
| `WorktreeCreate` | Worktree creándose | Sí* | — |
| `WorktreeRemove` | Worktree eliminándose | No | — |
| `PreCompact` | Antes de compaction | No | manual, auto |
| `PostCompact` | Después de compaction | No | manual, auto |
| `Elicitation` | MCP server pide input | Sí | MCP server name |
| `ElicitationResult` | User responde elicitation | Sí | MCP server name |

*WorktreeCreate: cualquier exit code ≠ 0 falla la creación. Solo type `command`.

### 4 Tipos de Handler

#### Command (default)
```json
{
  "type": "command",
  "command": "/path/to/script.sh",
  "timeout": 600,
  "async": false
}
```
Exit 0 = success, Exit 2 = bloqueo, Otro = non-blocking error.

#### HTTP
```json
{
  "type": "http",
  "url": "https://hooks.example.com/pre-tool",
  "headers": {"Authorization": "Bearer $MY_TOKEN"},
  "allowedEnvVars": ["MY_TOKEN"]
}
```
2xx = success, non-2xx = non-blocking error.

#### Prompt (LLM como juez)
```json
{
  "type": "prompt",
  "prompt": "Evaluate whether this file edit is safe. $ARGUMENTS",
  "model": "haiku",
  "timeout": 30
}
```
Retorna `{ok: true/false, reason: "..."}`. Default model: Haiku.

#### Agent (subagente verificador)
```json
{
  "type": "agent",
  "prompt": "Run tests and verify they pass. $ARGUMENTS",
  "timeout": 120
}
```
Multi-turn con tool access, hasta 50 tool-use turns, 60s default timeout.

### Configuración

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write \"$TOOL_INPUT_FILE_PATH\"",
            "statusMessage": "Formatting..."
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "npx eslint --fix \"$TOOL_INPUT_FILE_PATH\""
          }
        ]
      }
    ]
  }
}
```

### Decision Control — PreToolUse

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "Sandbox active",
    "updatedInput": { "command": "modified-command" },
    "additionalContext": "Extra info for Claude"
  }
}
```

`permissionDecision`: `allow` | `deny` | `ask`

### Patrones Comunes

1. **Auto-format tras edits**: PostToolUse matcher `Edit` → prettier/black
2. **Bloquear archivos protegidos**: PreToolUse matcher `Edit|Write` → check path contra denylist
3. **Re-inyectar contexto post-compaction**: PostCompact → enviar resumen o estado
4. **Notificaciones**: Notification → macOS `osascript`, Linux `notify-send`
5. **Auto-approve permisos**: PermissionRequest → `permissionDecision: "allow"` condicionalmente
6. **Audit config changes**: ConfigChange → log cambios
7. **Stop guard**: Stop → verificar que tests pasen antes de terminar (check `stop_hook_active` para evitar loop)

### Variables de Entorno en Hooks

- `$CLAUDE_PROJECT_DIR`: raíz del proyecto
- `${CLAUDE_PLUGIN_ROOT}`: directorio instalación plugin
- `${CLAUDE_PLUGIN_DATA}`: directorio datos persistentes plugin

### Deshabilitar

- `"disableAllHooks": true` en settings
- `"allowManagedHooksOnly": true` (managed only)
- `"allowedHttpHookUrls": ["https://hooks.example.com/*"]` (whitelist URLs)

## 2. Skills — Capacidades Lazy-Load

### Skills Bundled

| Skill | Uso | Notas |
|-------|-----|-------|
| `/batch <instrucción>` | Cambios masivos: 5-30 agentes paralelos en worktrees | Genera PRs individuales |
| `/simplify [foco]` | Review code quality: 3 review agents paralelos | Aplica fixes automáticamente |
| `/loop [intervalo] <prompt>` | Ejecutar prompt recurrente | Default 10min |
| `/debug [descripción]` | Troubleshoot sesión leyendo debug log | — |
| `/claude-api` | Cargar referencia API Claude + Agent SDK | — |

### Estructura de Skill

```
.claude/skills/mi-skill/
  SKILL.md           # Instrucciones (requerido)
  template.md        # Template para Claude
  examples/sample.md # Ejemplo output
  scripts/validate.sh # Script ejecutable
```

### Frontmatter SKILL.md

```yaml
---
name: deploy-staging
description: "Deploy to staging environment. Use when user asks to deploy or test in staging."
argument-hint: "[branch-name]"
allowed-tools:
  - Bash(kubectl *)
  - Bash(helm *)
  - Read
model: sonnet
effort: medium
context: fork
agent: deploy-agent
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate-deploy.sh"
---
```

| Campo | Requerido | Default | Descripción |
|-------|-----------|---------|-------------|
| `name` | No | dirname | Lowercase, hyphens, max 64 chars |
| `description` | Recomendado | — | Qué hace y cuándo usarlo |
| `argument-hint` | No | — | Hint autocomplete |
| `disable-model-invocation` | No | `false` | `true` = solo manual |
| `user-invocable` | No | `true` | `false` = solo Claude auto-invoca |
| `allowed-tools` | No | — | Tools auto-aprobados cuando skill activo |
| `model` | No | inherit | sonnet/opus/haiku |
| `effort` | No | inherit | low/medium/high/max |
| `context` | No | — | `fork` = subagente aislado |
| `agent` | No | — | Tipo subagente cuando context: fork |
| `hooks` | No | — | Hooks scoped al lifecycle del skill |

### Substituciones en SKILL.md

| Variable | Descripción |
|----------|-------------|
| `$ARGUMENTS` | Todos los argumentos |
| `$ARGUMENTS[N]` / `$N` | Argumento N (0-based) |
| `${CLAUDE_SESSION_ID}` | ID sesión actual |
| `${CLAUDE_SKILL_DIR}` | Directorio del SKILL.md |

### Dynamic Context

`` !`command` `` ejecuta shell command antes de enviar skill content. Output reemplaza placeholder.

### Ubicaciones

| Ubicación | Path | Aplica a |
|-----------|------|----------|
| Enterprise | Managed settings | Toda la org |
| Personal | `~/.claude/skills/<name>/SKILL.md` | Todos tus proyectos |
| Project | `.claude/skills/<name>/SKILL.md` | Solo este proyecto |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Donde plugin habilitado |

Prioridad: enterprise > personal > project.

### Permisos para Skills

- Denegar Skill tool: `"deny": ["Skill"]`
- Específico: `Skill(deploy-staging)`, `Skill(review-pr *)`

### Budget

2% del context window, fallback 16,000 chars. Override: `SLASH_COMMAND_TOOL_CHAR_BUDGET`.

## 3. Subagentes

### Built-in

| Tipo | Modelo | Tools | Uso |
|------|--------|-------|-----|
| Explore | Haiku | Read-only (Read, Glob, Grep) | Búsqueda/exploración codebase |
| Plan | Inherit | Read-only | Research para planificación |
| General-purpose | Inherit | Todos | Tareas complejas multi-step |
| Bash | Inherit | Bash | Comandos terminal en contexto separado |
| statusline-setup | Sonnet | Read, Edit | Config status line |
| Claude Code Guide | Haiku | Read-only + WebFetch | Documentación features |

### Custom Subagent — Frontmatter

```yaml
---
name: code-reviewer
description: "Reviews code for quality. Use after completing features."
tools: Read, Grep, Glob, Bash(npm run lint *)
disallowedTools: Write, Edit
model: sonnet
permissionMode: plan
maxTurns: 20
effort: medium
skills:
  - review-checklist
mcpServers:
  - github
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate.sh"
memory: project
background: false
isolation: worktree
---

# System Prompt del Subagente

Eres un code reviewer experto. Revisa el código para:
- Bugs y errores lógicos
- Vulnerabilidades de seguridad
- Code smells y debt técnico
```

### Scope y Prioridad

| Ubicación | Scope | Prioridad |
|-----------|-------|-----------|
| `--agents` CLI flag | Sesión actual | 1 (mayor) |
| `.claude/agents/` | Proyecto | 2 |
| `~/.claude/agents/` | Global | 3 |
| Plugin `agents/` | Plugin habilitado | 4 (menor) |

### CLI-Defined Subagents

```bash
claude --agents '{"debugger": {"description": "Debug issues", "prompt": "...", "tools": ["Read", "Bash"], "model": "opus"}}'
```

### Invocación

1. **Lenguaje natural**: "usa el code-reviewer para revisar"
2. **@-mention**: `@"code-reviewer (agent)"` — garantiza ejecución
3. **`--agent` flag**: `claude --agent code-reviewer` — toda la sesión
4. **Setting**: `"agent": "code-reviewer"` en settings.json

### Foreground vs Background

| Modo | Comportamiento |
|------|---------------|
| Foreground | Bloquea conversación, permisos passed-through |
| Background | Concurrente, pre-aprueba permisos upfront, auto-deny unapproved |

`Ctrl+B` para background un task running. Disable: `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.

### Persistent Memory

| Scope | Ubicación |
|-------|-----------|
| `user` | `~/.claude/agent-memory/<name>/` |
| `project` | `.claude/agent-memory/<name>/` |
| `local` | `.claude/agent-memory-local/<name>/` |

Incluye primeras 200 líneas de MEMORY.md, auto-habilita Read/Write/Edit.

### Denegar Subagentes

```json
{"permissions": {"deny": ["Agent(Explore)", "Agent(mi-agente)"]}}
```

## 4. Agent Teams (Experimental)

**Habilitar**: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

### Arquitectura

| Componente | Rol |
|------------|-----|
| Team lead | Sesión principal, crea equipo, coordina |
| Teammates | Instancias Claude Code independientes |
| Task list | Lista compartida: pending/in-progress/completed + dependencias |
| Mailbox | Messaging inter-agente |

### Teams vs Subagents

| | Subagents | Agent Teams |
|--|----------|-------------|
| Contexto | Own window, result back | Own window, independent |
| Comunicación | Solo report al main | Inter-teammate messaging |
| Coordinación | Main maneja todo | Task list compartida, self-coordination |
| Costo tokens | Menor | ~7x mayor |

### Display Modes

| Modo | Comportamiento |
|------|---------------|
| `in-process` | Todo en terminal main, `Shift+Down` para ciclar |
| `tmux` | Cada teammate en su propio pane |
| `auto` | Decide automáticamente |

Setting: `"teammateMode": "in-process"` o `claude --teammate-mode tmux`.

### Features

- **Plan approval**: Requerir que teammates planifiquen antes de implementar
- **Direct messaging**: Hablar con teammates vía `Shift+Down` o click pane
- **Task dependencies**: Auto-unblock cuando deps completan; file-locking previene race conditions
- **Quality gates**: hooks `TeammateIdle` y `TaskCompleted`

### Limitaciones

- No session resumption con in-process teammates
- Un equipo por sesión, no nested, lead fijo
- Shutdown puede ser lento
- Split panes requiere tmux o iTerm2

## 5. MCP — Model Context Protocol

### Tipos de Transporte

| Tipo | Configuración |
|------|--------------|
| stdio | `{"type": "stdio", "command": "npx", "args": ["my-mcp-server"]}` |
| HTTP | `{"type": "http", "url": "http://localhost:3000"}` |
| SSE | `{"type": "sse", "url": "http://localhost:3000/sse"}` |
| SDK in-process | `createSdkMcpServer()` (solo Agent SDK) |

### Configuración

**CLI**: `claude mcp add stdio github npx -y @anthropic-ai/github-mcp`

**Archivo** (`.mcp.json` en project root o `~/.claude.json`):
```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic-ai/github-mcp"],
      "env": { "GITHUB_TOKEN": "..." }
    }
  }
}
```

### Jerarquía MCP

1. Session-level (`.mcp.json` en session dir)
2. Project-level (`.mcp.json` en project root)
3. User-level (`~/.claude/.mcp.json` o `~/.claude.json`)
4. Managed policy (mayor precedencia)

### Tool Search

Cuando hay muchos MCP tools, Tool Search defiere los que excedan umbral de contexto (default 10%).
- `ENABLE_TOOL_SEARCH=auto` — auto-defer
- `ENABLE_TOOL_SEARCH=auto:5` — defer si tool > 5% contexto
- `ENABLE_TOOL_SEARCH=true` — siempre buscar
- `ENABLE_TOOL_SEARCH=false` — cargar todo

### Enterprise Controls

```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": ["github", "memory"],
  "disabledMcpjsonServers": ["filesystem"],
  "allowedMcpServers": [{"serverName": "github"}],
  "deniedMcpServers": [{"serverName": "filesystem"}],
  "allowManagedMcpServersOnly": true
}
```

### Elicitation

MCP servers pueden solicitar input estructurado del usuario durante ejecución (forms o browser URLs).

## 6. Plugins

### Estructura

```
mi-plugin/
  .claude-plugin/plugin.json   # Manifest (requerido)
  commands/                     # Legacy skills
  agents/                       # Custom agents
  skills/                       # Skills con SKILL.md
  hooks/hooks.json              # Hooks
  .mcp.json                     # MCP servers
  .lsp.json                     # LSP servers
  settings.json                 # Settings (solo key `agent`)
  scripts/                      # Utility scripts
```

### Manifest (`.claude-plugin/plugin.json`)

```json
{
  "name": "mi-plugin",
  "version": "1.2.0",
  "description": "Descripción",
  "author": {"name": "Felix"},
  "keywords": ["code-quality"],
  "commands": "./commands/",
  "agents": "./agents/",
  "skills": "./skills/",
  "hooks": "./hooks/hooks.json",
  "mcpServers": "./.mcp.json",
  "lspServers": "./.lsp.json"
}
```

### CLI Commands

```bash
claude plugin install mi-plugin@marketplace -s user
claude plugin uninstall mi-plugin -s user
claude plugin enable mi-plugin
claude plugin disable mi-plugin
claude plugin update mi-plugin
```

### Testing Local

```bash
claude --plugin-dir ./mi-plugin
/reload-plugins  # Pick up changes sin restart
```

### LSP Servers en Plugins

```json
{
  "command": "pyright-langserver",
  "args": ["--stdio"],
  "extensionToLanguage": { ".py": "python" },
  "transport": "stdio"
}
```

Available: `pyright-lsp` (Python), `typescript-lsp`, `rust-lsp`.

### Plugin Environment

- `${CLAUDE_PLUGIN_ROOT}`: directorio instalación (cambia on update)
- `${CLAUDE_PLUGIN_DATA}`: directorio persistente (`~/.claude/plugins/data/{id}/`, sobrevive updates)

## 7. Channels (Research Preview)

**Requisitos**: v2.1.80+, login claude.ai, Team/Enterprise debe habilitar explícitamente.

### Channels Disponibles

| Channel | Setup |
|---------|-------|
| Telegram | BotFather token → plugin install → pair |
| Discord | Developer Portal bot → plugin install → pair |
| Fakechat | Localhost demo port 8787 |

### Setup

```bash
/plugin install telegram@claude-plugins-official
/telegram:configure <bot-token>
claude --channels plugin:telegram@claude-plugins-official
/telegram:access pair <code>
/telegram:access policy allowlist
```

### Cómo Funciona

MCP server que pushea eventos a sesión Claude Code activa via `notifications/claude/channel`. Eventos llegan como `<channel source="name">content</channel>`.

### Permission Relay

Channels pueden reenviar prompts de permisos al teléfono:
- Request: `notifications/claude/channel/permission_request` con `request_id` (5 chars)
- Verdict: user responde `y/n <request_id>`
- Requiere capability `claude/channel/permission: {}`

### Channels vs Otras Features

| Feature | Para qué |
|---------|----------|
| Web | Sandbox cloud async |
| Slack | Tasks desde conversación equipo |
| MCP estándar | Claude consulta on-demand |
| Remote Control | Dirigir sesión local desde móvil |
| Channels | Push events desde fuentes externas |

## 8. 28 Tools Built-in — Referencia Rápida

| Tool | Permiso | Descripción |
|------|---------|-------------|
| `Agent` | No | Spawn subagente |
| `AskUserQuestion` | No | Preguntas multiple-choice |
| `Bash` | Sí | Comandos shell |
| `CronCreate` | No | Programar tarea recurrente/one-shot |
| `CronDelete` | No | Cancelar tarea programada |
| `CronList` | No | Listar tareas programadas |
| `Edit` | Sí | Ediciones targeted de archivos |
| `EnterPlanMode` | No | Entrar plan mode |
| `EnterWorktree` | No | Crear worktree aislado |
| `ExitPlanMode` | Sí | Presentar plan, salir |
| `ExitWorktree` | No | Salir worktree |
| `Glob` | No | Buscar archivos por patrón |
| `Grep` | No | Buscar contenido en archivos |
| `ListMcpResourcesTool` | No | Listar recursos MCP |
| `LSP` | No | Code intelligence (diagnostics, nav, types) |
| `NotebookEdit` | Sí | Modificar celdas Jupyter |
| `Read` | No | Leer archivos |
| `ReadMcpResourceTool` | No | Leer recurso MCP por URI |
| `Skill` | Sí | Ejecutar skill |
| `TaskCreate` | No | Crear task |
| `TaskGet` | No | Get task details |
| `TaskList` | No | Listar tasks |
| `TaskOutput` | No | Output de background task |
| `TaskStop` | No | Kill background task |
| `TaskUpdate` | No | Actualizar task |
| `ToolSearch` | No | Buscar/cargar deferred tools |
| `WebFetch` | Sí | Fetch URL content |
| `WebSearch` | Sí | Web search |
| `Write` | Sí | Crear/sobreescribir archivos |
