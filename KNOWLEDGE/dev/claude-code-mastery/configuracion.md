---
_manifest:
  urn: "urn:dev:kb:claude-code-mastery"
  type: "knowledge_article"
  version: "1.0.0"
title: "Claude Code Mastery — Configuración, Modelos y Costos"
domain: "dev"
tags: [claude-code, settings, permisos, sandbox, modelos, costos]
last_updated: "2026-03-22"
parent: "urn:dev:kb:claude-code-mastery"
---

# Configuración, Modelos y Costos

## 1. Jerarquía de Settings

Precedencia (mayor a menor):

| Scope | Ubicación | Compartido | Uso |
|-------|-----------|------------|-----|
| Managed | Server-managed / MDM / plist / registry / `managed-settings.json` | Sí (IT) | Políticas org |
| CLI args | `claude --model opus --effort high` | No | Override sesión |
| Local | `.claude/settings.local.json` (gitignored) | No | Personal por proyecto |
| Project | `.claude/settings.json` | Sí (git) | Equipo |
| User | `~/.claude/settings.json` | No | Preferencias globales |

**Arrays se mergan** (concatenan y deduplicam) entre scopes — no se reemplazan.

### Managed Settings Locations

| OS | Ubicación |
|----|-----------|
| macOS | `/Library/Application Support/ClaudeCode/managed-settings.json` |
| macOS MDM | dominio `com.anthropic.claudecode` |
| Linux/WSL | `/etc/claude-code/managed-settings.json` |
| Windows | `C:\Program Files\ClaudeCode\managed-settings.json` |
| Windows Registry | `HKLM\SOFTWARE\Policies\ClaudeCode` → `Settings` (REG_SZ) |

### Settings Clave

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "claude-opus-4-6",
  "effortLevel": "high",
  "language": "Español",
  "outputStyle": "Explanatory",
  "autoMemoryEnabled": true,
  "voiceEnabled": true,
  "autoUpdatesChannel": "stable",
  "plansDirectory": "./plans",
  "cleanupPeriodDays": 30,
  "sandbox": { "enabled": true },
  "permissions": {
    "allow": ["Bash(git *)", "Bash(npm run *)", "Read"],
    "deny": ["Read(.env)", "Read(.env.*)", "Bash(curl *)"]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1"
  },
  "hooks": {},
  "attribution": {
    "commit": "Co-Authored-By: Claude <noreply@anthropic.com>",
    "pr": ""
  }
}
```

### Settings Notables para Maximización

| Key | Propósito | Valor recomendado |
|-----|-----------|-------------------|
| `effortLevel` | Profundidad razonamiento | `"high"` (Opus), `"medium"` (Sonnet) |
| `sandbox.enabled` | Sandbox OS-level | `true` |
| `sandbox.autoAllowBashIfSandboxed` | Auto-approve bash en sandbox | `true` |
| `agent` | Main thread como subagente named | `"mi-agente"` |
| `worktree.symlinkDirectories` | Symlink dirs en worktrees | `["node_modules", ".cache"]` |
| `worktree.sparsePaths` | Sparse checkout en worktrees | `["packages/mi-app"]` |
| `fileSuggestion` | Custom `@` autocomplete | `{"type":"command","command":"..."}` |
| `statusLine` | Status line personalizada | `{"type":"command","command":"..."}` |
| `spinnerVerbs` | Verbos spinner custom | `{"mode":"append","verbs":["Transmutando"]}` |
| `fastModePerSessionOptIn` | Fast mode reset por sesión | `true` |

## 2. Sistema de Permisos

### 5 Modos de Permiso

| Modo | Comportamiento | Caso de uso |
|------|---------------|-------------|
| `default` | Prompt en primer uso | Desarrollo normal |
| `acceptEdits` | Auto-aprueba edits de archivo | Sesiones de coding activo |
| `plan` | Solo lectura, sin modificaciones | Análisis y planificación |
| `dontAsk` | Auto-deniega si no pre-aprobado | CI/CD restrictivo |
| `bypassPermissions` | Skip prompts (excepto .git/.claude/.vscode/.idea) | Automation confiable |

**Cambio rápido**: `Shift+Tab` o `Alt+M` durante sesión.

### Reglas de Permisos

**Evaluación**: deny → ask → allow (primera coincidencia gana, deny siempre prevalece).

**Sintaxis**: `Tool` o `Tool(specifier)`

```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(npm run *)",
      "Bash(python -m pytest *)",
      "Read",
      "Glob",
      "Grep",
      "WebFetch(domain:github.com)"
    ],
    "ask": [
      "Bash(git push *)"
    ],
    "deny": [
      "Read(.env)",
      "Read(.env.*)",
      "Read(./secrets/**)",
      "Bash(curl *)",
      "Bash(rm -rf *)",
      "Agent(Explore)"
    ]
  }
}
```

### Patrones de Path (Read/Edit)

| Patrón | Significado | Ejemplo |
|--------|-------------|---------|
| `//path` | Absoluto filesystem | `Read(//Users/alice/secrets/**)` |
| `~/path` | Desde home | `Read(~/Documents/*.pdf)` |
| `/path` | Relativo a raíz proyecto | `Edit(/src/**/*.ts)` |
| `path` o `./path` | Relativo a cwd | `Read(*.env)` |

`*` = archivos en un directorio, `**` = recursivo.

### Bash: Seguridad con Operadores Shell

Bash rules son prefix-match pero **aware de `&&`**. `Bash(safe-cmd *)` NO permite `safe-cmd && rm -rf /`. Aprobando comandos compuestos guarda reglas separadas por subcomando (hasta 5).

## 3. Sandbox

### Activación y Soporte

| OS | Backend | Instalación |
|----|---------|-------------|
| macOS | Seatbelt | Built-in |
| Linux/WSL2 | bubblewrap | `apt-get install bubblewrap socat` |
| WSL1 | No soportado | — |

**Activar**: `/sandbox` o `"sandbox": {"enabled": true}` en settings.

### Configuración Filesystem

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "filesystem": {
      "allowWrite": ["/tmp/build", "~/.kube"],
      "denyWrite": ["/etc", "/usr/local/bin"],
      "denyRead": ["~/.aws/credentials"],
      "allowRead": ["."]
    },
    "network": {
      "allowedDomains": ["github.com", "*.npmjs.org", "api.anthropic.com"],
      "allowLocalBinding": true
    },
    "excludedCommands": ["git", "docker"]
  }
}
```

### Prefijos de Path en Sandbox

| Prefijo | Desde | Ejemplo |
|---------|-------|---------|
| `/` | Filesystem root | `/tmp/build` |
| `~/` | Home dir | `~/.ssh` |
| `./` o sin prefijo | Project root (project settings) o `~/.claude` (user settings) | `./dist` |

### Escape Hatch

Cuando un comando falla por sandbox, Claude puede reintentar con `dangerouslyDisableSandbox` (pasa por permisos normales). Deshabilitar: `"allowUnsandboxedCommands": false`.

**Limitaciones de seguridad**: Network = solo restricción de dominio (no inspección), domain fronting posible, `allowUnixSockets` puede bypass, `enableWeakerNestedSandbox` reduce seguridad significativamente.

## 4. Memoria e Instrucciones

### CLAUDE.md — 3 Niveles

| Scope | Ubicación | Compartido |
|-------|-----------|------------|
| Managed | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) | Org-wide |
| Project | `./CLAUDE.md` o `./.claude/CLAUDE.md` | Equipo (git) |
| User | `~/.claude/CLAUDE.md` | Personal |

**Carga**: Sube por árbol de directorios desde cwd. CLAUDE.md de subdirectorios se carga on-demand.

**Imports**: `@path/to/import` — relativo/absoluto, recursivo hasta 5 niveles.

**Best practices**:
- < 500 líneas (idealmente < 300)
- Prueba de poda: "¿Eliminar esto causaría errores?"
- Si debe pasar 100% → hacerlo hook, no instrucción
- Especializado → skill, no CLAUDE.md

### .claude/rules/ — Reglas Path-Specific

```
.claude/rules/
├── code-style.md          # Aplica a todos
├── testing.md
├── frontend/react.md      # Solo src/**/*.tsx
└── backend/api.md         # Solo api/**/*.ts
```

Frontmatter para scoping:
```yaml
---
paths:
  - "src/**/*.ts"
  - "src/**/*.tsx"
---
```

### Auto Memory

- **Storage**: `~/.claude/projects/<project>/memory/`
- **Carga**: Primeras 200 líneas de MEMORY.md en cada sesión
- **Toggle**: `/memory`, `autoMemoryEnabled` setting, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`
- **Custom dir**: `autoMemoryDirectory` setting
- Claude escribe automáticamente learnings (build commands, debugging insights, patrones)

### Exclusiones

```json
{
  "claudeMdExcludes": ["**/vendor/CLAUDE.md", "/path/**"]
}
```

## 5. Modelos y Thinking

### Aliases de Modelo

| Alias | Modelo | Contexto | Notas |
|-------|--------|----------|-------|
| `default` | Según plan | — | Opus (Max/Team Premium), Sonnet (Pro/Team Standard) |
| `sonnet` | Sonnet 4.6 | 200K→1M | Más eficiente en costo |
| `opus` | Opus 4.6 | 1M | Máxima capacidad |
| `haiku` | Haiku 4.5 | 200K | Background, subagentes |
| `sonnet[1m]` | Sonnet 4.6 | 1M | Requiere extra usage (Pro) |
| `opus[1m]` | Opus 4.6 | 1M | Incluido Max/Team/Enterprise |
| `opusplan` | Opus plan + Sonnet exec | 1M | Mejor balance costo/calidad |

### Effort Levels

| Nivel | Efecto | Disponible |
|-------|--------|------------|
| `low` | Mínimo thinking | Todos |
| `medium` | Balanceado (default Opus) | Todos |
| `high` | Razonamiento profundo | Todos |
| `max` | Máximo tokens, sin restricción | Solo Opus 4.6, solo sesión |

**Setear**: `/effort`, `--effort`, `CLAUDE_CODE_EFFORT_LEVEL`, `effortLevel` setting, frontmatter skill/subagent.

### Adaptive Thinking (Opus 4.6 / Sonnet 4.6)

- Automático: Claude decide cuánto pensar por turno
- `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` → fallback a `MAX_THINKING_TOKENS`
- Extended thinking toggle: `Alt+T` o `Option+T`

### Fast Mode (Research Preview)

- Opus 4.6 a 2.5x velocidad, 6x costo ($30/$150 MTok)
- Toggle: `/fast` o `"fastMode": true`
- Switching mid-conversation paga full uncached input
- Rate limits separados, auto-fallback a standard on limit
- Disable: `CLAUDE_CODE_DISABLE_FAST_MODE=1`
- Per-session opt-in: `fastModePerSessionOptIn: true`

### Extended Context 1M

| Plan | Opus 1M | Sonnet 1M |
|------|---------|-----------|
| Max, Team, Enterprise | Incluido | Requiere extra usage |
| Pro | Requiere extra usage | Requiere extra usage |
| API pay-as-you-go | Full access | Full access |

Sin surcharge de precio (eliminado el 2x multiplier legacy). Hasta 600 imágenes/PDFs.
Disable: `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`

## 6. Gestión de Costos y Contexto

### Costos Típicos

| Métrica | Valor |
|---------|-------|
| Promedio por dev/día | ~$6 |
| 90th percentile | < $12/día |
| Team promedio | $100-200/dev/mes (Sonnet) |
| Agent teams | ~7x tokens vs sesión normal |
| Background overhead | ~$0.04/sesión |

### Estrategias de Reducción

1. **`/clear` entre tareas** — evita "kitchen sink session"
2. **`/compact <instrucciones>`** — compactar a ~60% (antes del auto ~95%)
3. **Modelo correcto**: Sonnet para 90% del trabajo, Opus para complejidad alta, Haiku para bulk
4. **`opusplan`**: Opus planifica, Sonnet ejecuta → ahorro ~40%
5. **Reducir overhead MCP**: `/mcp` para deshabilitar servidores no usados
6. **Tool search**: `ENABLE_TOOL_SEARCH=auto:N` — defer tools que excedan N% contexto
7. **Code intelligence plugins**: LSP para lenguajes tipados
8. **CLAUDE.md → Skills**: Mover instrucciones especializadas a skills (se cargan on-demand)
9. **Subagentes para verbose ops**: Aíslan contexto en su propia ventana
10. **`/effort low`**: Para tareas simples

### Control de Presupuesto

```bash
claude -p --max-budget-usd 5.00 "query"    # Límite de gasto
claude --max-turns 3 "query"                # Límite de turnos
```

### Gestión de Contexto

| Comando | Efecto | Cuándo usar |
|---------|--------|-------------|
| `/clear` | Borra historial, re-lee CLAUDE.md | Entre tareas distintas |
| `/compact [instrucciones]` | Resume y condensa | Dentro de tarea larga, ~60% uso |
| `/context` | Visualiza uso de contexto | Diagnóstico |
| `/cost` | Estadísticas de tokens | Monitoreo |
| `Esc+Esc` → Summarize | Comprime desde checkpoint | Liberar espacio selectivo |

**Auto-compaction**: Dispara a ~95% capacidad. Override: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=60`.

### Prompt Caching

Automático. Cache dura 5min (default) o 1hr (2x base price). Read = 0.1x base price.
- Mínimo cacheable: 4096 tokens (Opus/Haiku), 2048 (Sonnet), 1024 (Sonnet 4.5/4)
- Hasta 4 breakpoints por request
- Invalidado por: cambio de tools, web search toggle, citations, speed setting, imágenes

## 7. Variables de Entorno Clave

### Modelo y Thinking

| Variable | Propósito |
|----------|-----------|
| `ANTHROPIC_MODEL` | Override modelo |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | ID modelo para alias `opus` |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | ID modelo para alias `sonnet` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | ID modelo para alias `haiku` |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Modelo para subagentes |
| `CLAUDE_CODE_EFFORT_LEVEL` | Nivel effort (máxima precedencia) |
| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | Deshabilitar adaptive thinking |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT` | Deshabilitar contexto 1M |
| `MAX_THINKING_TOKENS` | Budget thinking manual. 0 = disable |

### Bash y Output

| Variable | Propósito |
|----------|-----------|
| `BASH_DEFAULT_TIMEOUT_MS` | Timeout default bash |
| `BASH_MAX_TIMEOUT_MS` | Timeout máximo |
| `BASH_MAX_OUTPUT_LENGTH` | Max chars output (trunca medio) |
| `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` | Reset a project dir tras cada comando |
| `CLAUDE_ENV_FILE` | Shell script sourced antes de cada Bash |

### Contexto y Memoria

| Variable | Propósito |
|----------|-----------|
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | % trigger auto-compaction (1-100) |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | Override tamaño ventana para cálculos |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | 1=off, 0=force on |
| `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` | Override token limit file read |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET` | Budget chars metadata skills (default 2% context) |

### API y Auth

| Variable | Propósito |
|----------|-----------|
| `ANTHROPIC_API_KEY` | API key directa |
| `ANTHROPIC_AUTH_TOKEN` | Custom Authorization header |
| `ANTHROPIC_BASE_URL` | Override endpoint (proxy/gateway) |
| `ANTHROPIC_CUSTOM_HEADERS` | Headers custom (Name: Value, newline-sep) |
| `CLAUDE_CODE_USE_BEDROCK` | Usar AWS Bedrock |
| `CLAUDE_CODE_USE_VERTEX` | Usar Google Vertex |
| `CLAUDE_CODE_USE_FOUNDRY` | Usar Azure Foundry |

### MCP y Tools

| Variable | Propósito |
|----------|-----------|
| `MCP_TIMEOUT` | Timeout startup MCP server (ms) |
| `MCP_TOOL_TIMEOUT` | Timeout ejecución tool MCP (ms) |
| `MAX_MCP_OUTPUT_TOKENS` | Max tokens respuesta MCP (default 25000) |
| `ENABLE_TOOL_SEARCH` | Tool search: true, auto, auto:N, false |

### Sistema

| Variable | Propósito |
|----------|-----------|
| `CLAUDECODE` | =1 en shells spawned por Claude (no en hooks) |
| `CLAUDE_CONFIG_DIR` | Custom config dir |
| `CLAUDE_CODE_TMPDIR` | Override temp dir |
| `CLAUDE_CODE_SHELL` | Override shell detection |
| `HTTP_PROXY` / `HTTPS_PROXY` | Proxy server |
| `DISABLE_AUTOUPDATER` | Deshabilitar auto-updates |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Disable updater+feedback+telemetry |

## 8. Output Styles

### Built-in

| Style | Efecto |
|-------|--------|
| Default | System prompt estándar ingeniería |
| Explanatory | "Insights" educativos entre coding |
| Learning | Colaborativo, marcadores `TODO(human)` |

### Custom Styles

Ubicación: `~/.claude/output-styles/` (user) o `.claude/output-styles/` (project).

```markdown
---
name: Mi Estilo
description: Descripción breve
keep-coding-instructions: false
---
# Instrucciones de estilo
...
```

`keep-coding-instructions: true` mantiene instrucciones de coding del system prompt.

## 9. Checkpoints

- Cada prompt crea checkpoint automático
- Persisten across sessions (30 días, configurable `cleanupPeriodDays`)
- `Esc+Esc` o `/rewind` → menú con opciones:
  - Restore code + conversation
  - Restore solo conversation
  - Restore solo code
  - Summarize from here (comprime contexto)
- **Limitación**: No trackea cambios de `rm`, `mv`, `cp` ni edits manuales externos
- Fork: `claude --continue --fork-session` para branching

## 10. Interactive Mode — Shortcuts Esenciales

| Shortcut | Acción |
|----------|--------|
| `Ctrl+C` | Cancelar generación |
| `Ctrl+D` | Salir |
| `Ctrl+G` | Abrir en editor externo |
| `Ctrl+L` | Limpiar terminal (mantiene conversación) |
| `Ctrl+O` | Toggle verbose output |
| `Ctrl+T` | Toggle task list |
| `Ctrl+B` | Background running task |
| `Ctrl+V` / `Alt+V` | Pegar imagen |
| `Ctrl+R` | Buscar en historial |
| `Ctrl+F` | Kill all background agents (2x confirm) |
| `Esc+Esc` | Rewind / checkpoint menu |
| `Shift+Tab` / `Alt+M` | Ciclar modos de permiso |
| `Alt+P` / `Option+P` | Cambiar modelo |
| `Alt+T` / `Option+T` | Toggle extended thinking |
| Space (hold) | Push-to-talk voice |
| `/vim` | Toggle modo Vim |
| `!command` | Bash mode directo |
| `@file` | Referencia archivo |
| `/btw question` | Side question sin agregar al historial |
