---
_manifest:
  urn: "urn:dev:kb:claude-code-mastery"
  type: "knowledge_article"
  version: "1.0.0"
title: "Claude Code Mastery — Agent SDK y Automatización"
domain: "dev"
tags: [claude-code, agent-sdk, headless, cicd, github-actions, automatizacion]
last_updated: "2026-03-22"
parent: "urn:dev:kb:claude-code-mastery"
---

# Agent SDK, Headless Mode y Automatización

## 1. Claude Agent SDK

### Identidad

| Campo | Valor |
|-------|-------|
| Nombre anterior | Claude Code SDK |
| Nombre actual | Claude Agent SDK |
| TS package | `@anthropic-ai/claude-agent-sdk` (v0.2.71) |
| Python package | `claude-agent-sdk` (v0.1.48) |
| GitHub TS | `anthropics/claude-agent-sdk-typescript` |
| GitHub Python | `anthropics/claude-agent-sdk-python` |
| Branding | "Claude Agent" (no "Claude Code Agent") |
| Docs | https://platform.claude.com/docs/en/agent-sdk/overview |

### Core API — query()

**Python**:
```python
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Analiza utils.py para bugs y corrígelos",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Glob", "Bash(npm run test *)"],
            permission_mode="acceptEdits",
            model="claude-opus-4-6",
            max_turns=20,
            max_budget_usd=5.0,
            cwd="/path/to/project",
            setting_sources=["user", "project"],
        ),
    ):
        if hasattr(message, 'type'):
            if message.type == "result":
                print(f"Cost: ${message.cost_usd:.4f}")
                print(f"Session: {message.session_id}")
```

**TypeScript**:
```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

const q = query({
  prompt: "Analyze utils.ts for bugs",
  options: {
    allowedTools: ["Read", "Edit", "Glob"],
    permissionMode: "acceptEdits",
    model: "claude-opus-4-6",
    maxTurns: 20,
    maxBudgetUsd: 5.0,
    cwd: "/path/to/project",
    settingSources: ["user", "project"],
  },
});

for await (const message of q) {
  if (message.type === "result") {
    console.log(`Cost: $${message.costUsd}`);
    console.log(`Session: ${message.sessionId}`);
  }
}
```

### ClaudeAgentOptions — Parámetros Principales

| Parámetro (Python / TS) | Tipo | Propósito |
|--------------------------|------|-----------|
| `allowed_tools` / `allowedTools` | list[str] | Auto-aprobados sin prompt |
| `disallowed_tools` / `disallowedTools` | list[str] | Removidos del contexto |
| `permission_mode` / `permissionMode` | str | default/acceptEdits/dontAsk/bypassPermissions/plan |
| `model` | str | Modelo específico |
| `fallback_model` / `fallbackModel` | str | Fallback si modelo primary no disponible |
| `system_prompt` / `systemPrompt` | str | Custom o preset |
| `max_turns` / `maxTurns` | int | Límite round trips |
| `max_budget_usd` / `maxBudgetUsd` | float | Límite gasto |
| `effort` | str | low/medium/high/max |
| `cwd` | str/Path | Working directory |
| `mcp_servers` / `mcpServers` | dict/str | MCP server config |
| `continue_conversation` / `continue` | bool | Continuar última sesión |
| `resume` | str | Resume session ID específico |
| `output_format` / `outputFormat` | dict | Formato output |
| `setting_sources` / `settingSources` | list | ["user","project","local"] |
| `hooks` | dict | Hooks programáticos |
| `can_use_tool` / `canUseTool` | callback | Callback permiso custom |
| `sandbox` | dict | Config sandbox |
| `plugins` | dict | Plugins config |
| `thinking` | dict | Config thinking |
| `agents` | dict | Subagent definitions |
| `env` | dict | Environment variables |
| `add_dirs` / `addDirs` | list | Directorios adicionales |
| `enable_file_checkpointing` | bool | Habilitar checkpoints |

### Tipos de Mensaje (5 Core)

| Tipo | Descripción |
|------|-------------|
| `SystemMessage` | Subtype `init` (metadata) o `compact_boundary` |
| `AssistantMessage` | Texto + tool call blocks por turno |
| `UserMessage` | Tool results devueltos a Claude |
| `StreamEvent` | Mensajes parciales (requiere `include_partial_messages`) |
| `ResultMessage` | Final: texto, usage, cost, session_id, subtype |

**Result subtypes**: `success`, `error_max_turns`, `error_max_budget_usd`, `error_during_execution`, `error_max_structured_output_retries`

### Multi-Turn con ClaudeSDKClient (Python)

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async with ClaudeSDKClient(options=ClaudeAgentOptions(...)) as client:
    await client.query("Analiza el módulo auth")
    async for msg in client.receive_response():
        handle(msg)

    await client.query("Ahora refactoriza a JWT")
    async for msg in client.receive_response():
        handle(msg)
```

### Custom Tools — In-Process MCP Server

**TypeScript**:
```typescript
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

const getWeather = tool("get_weather", "Get weather for a city", {
  city: z.string(),
  units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
}, async ({ city, units }) => ({
  content: [{ type: "text", text: `${city}: 22°${units === "celsius" ? "C" : "F"}` }]
}));

const server = createSdkMcpServer({
  name: "weather-tools",
  version: "1.0.0",
  tools: [getWeather],
});

for await (const msg of query({
  prompt: "What's the weather in Santiago?",
  options: { mcpServers: { "weather-tools": server } },
})) { /* handle */ }
```

**Python**:
```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("get_weather", "Get weather for a city", {"city": str})
async def get_weather(args):
    return {"content": [{"type": "text", "text": f"{args['city']}: 22°C"}]}

server = create_sdk_mcp_server(name="weather-tools", version="1.0.0", tools=[get_weather])
```

Tool naming: `mcp__<server_name>__<tool_name>` (e.g., `mcp__weather-tools__get_weather`).

### Subagents en SDK

```typescript
const options = {
  agents: {
    "code-reviewer": {
      description: "Reviews code for quality",
      prompt: "You are an expert code reviewer...",
      tools: ["Read", "Grep", "Glob"],
      model: "sonnet",
      maxTurns: 15,
    },
  },
  allowedTools: ["Agent", "Read", "Edit"],
};
```

**Reglas clave**:
- Incluir `"Agent"` en `allowedTools`
- Subagentes NO pueden spawnar sus propios subagentes
- Cada subagente tiene contexto fresh (no hereda conversación parent)
- Recibe: su system prompt + Agent tool prompt + CLAUDE.md del proyecto

### Hooks Programáticos en SDK

```python
async def pre_tool_hook(input_data, tool_use_id, context):
    if input_data.get("tool_name") == "Bash":
        cmd = input_data.get("tool_input", {}).get("command", "")
        if "rm -rf" in cmd:
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Destructive command blocked"
                }
            }
    return {}

options = ClaudeAgentOptions(
    hooks={"PreToolUse": [pre_tool_hook]},
    ...
)
```

**Eventos disponibles (Python)**: PreToolUse, PostToolUse, PostToolUseFailure, UserPromptSubmit, Stop, PermissionRequest, SubagentStart, SubagentStop, PreCompact, Notification.

**TS adicionales**: SessionStart, SessionEnd, Setup, TeammateIdle, TaskCompleted, ConfigChange, WorktreeCreate, WorktreeRemove.

### Sessions

| Patrón | Cómo |
|--------|------|
| One-shot | Single `query()` call |
| Multi-turn | `ClaudeSDKClient` (Python) o `continue: true` (TS) |
| Resume | Capturar `session_id` del ResultMessage, pasar a `resume` |
| Fork | `fork_session=True` / `forkSession: true` |
| Stateless (TS) | `persistSession: false` |

**Storage**: `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`

**Helpers**: `list_sessions()` / `listSessions()`, `get_session_messages()` / `getSessionMessages()`

### settingSources — Control de Carga

| Source | Qué carga |
|--------|-----------|
| `"project"` | Project CLAUDE.md, rules, skills, hooks, settings.json |
| `"user"` | User CLAUDE.md, rules, skills, settings |
| `"local"` | CLAUDE.local.md, settings.local.json |

**Default SDK**: no carga nada (a diferencia de CLI que carga todo).

### Hosting

**Requisitos**: Python 3.10+ o Node.js 18+, Claude Code CLI instalado, 1GiB RAM / 5GiB disk / 1 CPU, outbound HTTPS a api.anthropic.com.

**Patrones**:
1. **Ephemeral**: Un container por tarea, kill after
2. **Long-running**: Container persistente, multi-turn
3. **Hybrid**: Ephemeral + state hydrated
4. **Single container**: Múltiples SDK processes

**Providers**: Modal, Cloudflare, Daytona, E2B, Fly Machines, Vercel.

### Secure Deployment

- **Proxy pattern**: Inyectar credenciales vía proxy, agente nunca ve secrets
- `ANTHROPIC_BASE_URL` para routing API calls
- `HTTP_PROXY`/`HTTPS_PROXY` para tráfico sistema
- Docker hardening: `--cap-drop ALL`, `--security-opt no-new-privileges`
- Filesystem: read-only mounts, tmpfs para writes efímeros
- Network: `--network none` + Unix socket proxy

## 2. Headless Mode — Programmatic CLI

### Uso Básico

```bash
claude -p "prompt"                                    # Text output
claude -p "prompt" --output-format json               # JSON structured
claude -p "prompt" --output-format stream-json         # Streaming NDJSON
claude -p "prompt" --bare                              # Skip autodiscovery
```

### `--bare` Mode (Recomendado para CI)

Skip: hooks, skills, plugins, MCP, auto memory, CLAUDE.md.

Para cargar selectivamente:
```bash
claude -p --bare \
  --append-system-prompt "Custom instructions" \
  --settings ./ci-settings.json \
  --mcp-config ./ci-mcp.json \
  --allowedTools "Read,Edit,Bash(npm run *)" \
  "Run tests and fix failures"
```

### Structured Output

```bash
claude -p --output-format json --json-schema '{
  "type": "object",
  "properties": {
    "bugs": {"type": "array", "items": {"type": "string"}},
    "severity": {"type": "string", "enum": ["low","medium","high"]}
  }
}' "Analyze auth.py for bugs"
```

Retorna schema-conforming data en campo `structured_output`.

### Streaming Events

```bash
claude -p --output-format stream-json --verbose --include-partial-messages "task"
```

Eventos incluyen `system/api_retry` con attempt, max_retries, retry_delay_ms.

### Continuar Conversaciones

```bash
claude -p --continue "Follow up question"              # Última sesión
claude -p --resume <session_id> "Follow up"            # Sesión específica
```

### System Prompt

```bash
claude -p --append-system-prompt "Always use TypeScript" "Create a web server"
claude -p --system-prompt "Full replacement prompt" "task"
```

### Control de Presupuesto

```bash
claude -p --max-budget-usd 5.00 --max-turns 10 "task"
```

## 3. GitHub Actions

### Action Oficial

`anthropics/claude-code-action@v1`

### Modo Interactivo (Trigger por @claude en comentarios)

```yaml
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]

jobs:
  claude:
    if: contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Modo Automatización (Prompt explícito)

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    prompt: "Review this PR for security issues and code quality"
    claude_args: "--model claude-sonnet-4-6 --max-turns 10"
```

### Code Review Automatizado

Funcionalidad lanzada 2026-03-09. Multi-agent review:
1. Equipo de agentes analiza PR en paralelo
2. Filtra false positives
3. Rankea por severidad

Costo promedio: $15-$25 por review. Disponible Team/Enterprise.

Resultados internos Anthropic: comentarios sustantivos subieron de 16% a 54% de PRs.

### Setup Rápido

```bash
/install-github-app  # Dentro de Claude Code terminal
```

## 4. Scheduled Tasks

### /loop — Tareas Recurrentes

```bash
/loop 5m check if the deployment finished
/loop 30m /review-pr 1234
/loop ... every 2 hours                    # Trailing syntax
```

Default: 10 minutos. Units: s, m, h, d.

### One-Time Reminders

Lenguaje natural: `remind me at 3pm to push the release branch`

### Tools Programáticos

| Tool | Propósito |
|------|-----------|
| `CronCreate` | Crear tarea (5-field cron, prompt, recurrence) |
| `CronList` | Listar con IDs, schedules |
| `CronDelete` | Cancelar por ID (8 chars) |

Max 50 tasks por sesión. Expiry 3 días en recurring. Solo dispara cuando Claude idle.

Disable: `CLAUDE_CODE_DISABLE_CRON=1`

## 5. /batch — Cambios Masivos Paralelos

3 fases:
1. **Research/Plan**: Explore agent descompone en 5-30 unidades independientes
2. **Parallel execution**: Un agente por unidad en worktree aislado
3. **Completion**: Cada agente implementa, /simplify, tests, commit, PR

Hasta 10x más rápido que prompts secuenciales.

```bash
/batch "Migrate all API endpoints from Express to Fastify"
```

## 6. Fuentes para Mantener Actualizado el KB

### Fuentes Oficiales (Autoritativas)

| Fuente | URL | Frecuencia check |
|--------|-----|-------------------|
| Claude Code Docs | https://code.claude.com/docs/en/overview | Semanal |
| Claude Code Changelog | https://code.claude.com/docs/en/changelog | Semanal |
| Platform Docs | https://platform.claude.com/docs/en/home | Semanal |
| GitHub Releases | https://github.com/anthropics/claude-code/releases | Semanal |
| Anthropic Blog | https://www.anthropic.com/news | Semanal |
| Anthropic Engineering | https://www.anthropic.com/engineering | Quincenal |
| Release Notes | https://support.claude.com/en/articles/12138966-release-notes | Semanal |
| Docs llms.txt | https://code.claude.com/docs/llms.txt | Mensual (índice) |

### Fuentes Comunitarias (Curadas)

| Fuente | URL | Tipo |
|--------|-----|------|
| Builder.io Tips | https://www.builder.io/blog/claude-code-tips-best-practices | Best practices |
| ykdojo/claude-code-tips | https://github.com/ykdojo/claude-code-tips | Tips crowdsourced |
| Awesome Claude Code | https://github.com/hesreallyhim/awesome-claude-code | Curated links |
| Claude Code Ultimate Guide | https://github.com/FlorianBruniaux/claude-code-ultimate-guide | Comprehensive |
| claudefa.st | https://claudefa.st/blog/ | Guides avanzados |
| ClaudeLog Changelog | https://claudelog.com/claude-code-changelog/ | Changelog tracker |
| Releasebot | https://releasebot.io/updates/anthropic/claude-code | Release tracker |

### Fuentes Técnicas (Deep Dive)

| Fuente | URL | Foco |
|--------|-----|------|
| Agent SDK TS GitHub | https://github.com/anthropics/claude-agent-sdk-typescript | SDK source |
| Agent SDK Python GitHub | https://github.com/anthropics/claude-agent-sdk-python | SDK source |
| MCP SDK | https://github.com/modelcontextprotocol/typescript-sdk | MCP tooling |
| Anthropic Skills repo | https://github.com/anthropics/skills | Official skills |
| claude-code-action | https://github.com/anthropics/claude-code-action | GitHub Actions |
| npm @anthropic-ai/claude-agent-sdk | https://www.npmjs.com/package/@anthropic-ai/claude-agent-sdk | TS package |
| PyPI claude-agent-sdk | https://pypi.org/project/claude-agent-sdk/ | Python package |

### Procedimiento de Actualización

1. Check changelog: `https://code.claude.com/docs/en/changelog`
2. Comparar version en ficha (`v2.1.81`) con latest release
3. Si hay cambios significativos:
   - Actualizar ficha técnica (`urn:dev:kb:agentic-tooling-inventory` → `claude-code.md`)
   - Actualizar secciones afectadas del mastery KB
   - Actualizar `last_updated` en frontmatter
4. Run: `python3 scripts/kora index && python3 scripts/kora health --strict`
