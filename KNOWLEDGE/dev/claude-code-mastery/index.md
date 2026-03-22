---
_manifest:
  urn: "urn:dev:kb:claude-code-mastery"
  type: "knowledge_article"
  version: "1.0.0"
title: "Claude Code Mastery — Guía Operativa de Maximización"
domain: "dev"
tags: [claude-code, anthropic, mastery, operaciones, referencia]
last_updated: "2026-03-22"
sources:
  - "https://code.claude.com/docs/en/overview (67 páginas)"
  - "https://platform.claude.com/docs/en/home (124 páginas)"
  - "GitHub anthropics/claude-code releases"
  - "Community: builder.io, claudefa.st, datacamp, sfeir, ykdojo/claude-code-tips"
---

# Claude Code Mastery — Guía Operativa de Maximización

Base de conocimiento curada para exprimir al máximo Claude Code v2.1.81 (marzo 2026).

## Mapa de Capacidades

```
Claude Code v2.1.81
├── CONFIGURACIÓN
│   ├── Settings (4 scopes: managed > local > project > user)
│   ├── Permisos (deny > ask > allow, 5 modos)
│   ├── Sandbox (Seatbelt macOS, bubblewrap Linux)
│   ├── Modelos (aliases, effort, adaptive thinking, fast mode)
│   ├── Variables de entorno (90+)
│   └── Costos y contexto (compaction, /clear, /compact)
│
├── MEMORIA
│   ├── CLAUDE.md (proyecto + user + managed)
│   ├── .claude/rules/ (path-specific)
│   ├── Auto memory (~/.claude/projects/.../memory/)
│   └── Imports (@path/to/file.md)
│
├── EXTENSIBILIDAD
│   ├── Hooks (22 eventos × 4 tipos handler)
│   ├── Skills (bundled + custom, frontmatter YAML)
│   ├── Subagentes (built-in + custom, isolation: worktree)
│   ├── Agent Teams (experimental, shared task list)
│   ├── MCP (stdio/HTTP/SSE + SDK in-process)
│   ├── Plugins (marketplace + custom, LSP servers)
│   └── Channels (Telegram, Discord — research preview)
│
├── AUTOMATIZACIÓN
│   ├── Headless (-p, --bare, JSON/stream output)
│   ├── GitHub Actions (anthropics/claude-code-action@v1)
│   ├── GitLab CI/CD
│   ├── Scheduled tasks (/loop, CronCreate)
│   └── /batch (5-30 agentes paralelos en worktrees)
│
└── AGENT SDK
    ├── TypeScript (@anthropic-ai/claude-agent-sdk)
    ├── Python (claude-agent-sdk)
    ├── query() → AsyncGenerator<Message>
    ├── Custom tools (createSdkMcpServer + tool())
    ├── Hooks programáticos
    └── Hosting (Modal, Cloudflare, Vercel, Docker)
```

## Artículos Detallados

| Artículo | Cobertura |
|----------|-----------|
| [configuracion.md](configuracion.md) | Settings, env vars, permisos, sandbox, modelos, thinking, costos, contexto |
| [extensibilidad.md](extensibilidad.md) | Hooks, skills, subagentes, agent teams, MCP, plugins, channels |
| [sdk-y-automatizacion.md](sdk-y-automatizacion.md) | Agent SDK, headless, CI/CD, GitHub Actions, fuentes de actualización |

## Quick Wins — Lo Primero que Configurar

1. **`/init`** — Genera CLAUDE.md starter para tu proyecto
2. **`/sandbox`** — Activa sandbox OS-level, reduce prompts de permisos
3. **`/permissions`** — Pre-aprueba tus comandos frecuentes (`git *`, `npm run *`)
4. **MCP servers** — `claude mcp add` los que uses (GitHub, etc.)
5. **Hooks PostToolUse** — Auto-format (prettier/black) tras cada edit
6. **Skills custom** — Empaqueta flujos repetibles (`/deploy`, `/review-pr`)
7. **Subagentes** — Define `code-reviewer`, `debugger` en `.claude/agents/`

## Principios de Maximización

### 1. Contexto es el recurso más valioso
- Rendimiento LLM degrada con contexto lleno
- `/clear` entre tareas no relacionadas
- `/compact <instrucciones>` a ~60% utilización (antes del auto ~95%)
- CLAUDE.md < 500 líneas; instrucciones especializadas → skills
- `SLASH_COMMAND_TOOL_CHAR_BUDGET` controla budget de skills metadata

### 2. Verificación > instrucción
- Siempre dar tests, screenshots, outputs esperados
- Single highest-leverage practice según docs oficiales
- Hooks para enforcement determinístico (si debe pasar 100% → hook, no CLAUDE.md)

### 3. Explorar → Planificar → Implementar → Commit
- Plan Mode (`Shift+Tab`) para análisis read-only
- `opusplan` = Opus planifica, Sonnet ejecuta (ahorro ~40%)
- Ctrl+G abre plan en editor externo
- `/rewind` o `Esc+Esc` para branching exploratorio

### 4. Paralelismo nativo
- Subagentes para tareas independientes
- `/batch` para cambios masivos (5-30 worktrees)
- Agent teams para coordinación compleja
- `claude -w feature-x` para worktree aislado

### 5. Automatización progresiva
- Nivel 1: CLAUDE.md + permissions
- Nivel 2: Hooks + skills custom
- Nivel 3: Subagentes + MCP servers
- Nivel 4: `claude -p --bare` en CI/CD
- Nivel 5: Agent SDK embedding en apps propias

## Versión Actual y Changelog

- **v2.1.81** (2026-03-22): `--bare` flag, channels permission relay, OAuth fix concurrente
- **v2.1.80**: MCP tool output mejorado, color fix VS Code
- **v2.1.79**: `--console` login, turn duration toggle, 80MB reducción memoria

Changelog completo: https://code.claude.com/docs/en/changelog
