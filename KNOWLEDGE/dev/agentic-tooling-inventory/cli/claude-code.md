---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "2.0.0"
title: "Claude Code — CLI Ficha Técnica"
domain: "dev"
tags: [cli, claude-code, anthropic, agent-sdk]
last_updated: "2026-03-22"
parent: "urn:dev:kb:agentic-tooling-inventory"
see_also: "urn:dev:kb:claude-code-mastery"
---

## Claude Code — v2.1.81 (2026-03-22)

### Datos Básicos

| Campo | Valor |
|-------|-------|
| Versión | 2.1.81 |
| Instalación | `curl -fsSL https://claude.ai/install.sh \| bash` |
| Alt. instalación | `npm i -g @anthropic-ai/claude-code`, `brew install --cask claude-code`, `winget install Anthropic.ClaudeCode` |
| SDK (TS) | `npm i @anthropic-ai/claude-agent-sdk` (v0.2.71) |
| SDK (Python) | `pip install claude-agent-sdk` (v0.1.48) |
| Requisitos | Node.js 18+ |
| Licencia | Propietario (Anthropic) |
| Superficies | Terminal, VS Code, JetBrains, Desktop (macOS/Win), Web, Chrome, Slack, iOS |
| Docs CC | https://code.claude.com/docs/en/overview (67 páginas) |
| Docs SDK | https://platform.claude.com/docs/en/agent-sdk/overview |

### Acceso y API Keys

| Variable | Propósito |
|----------|-----------|
| `ANTHROPIC_API_KEY` | API directa |
| `CLAUDE_CODE_USE_BEDROCK=1` | AWS Bedrock |
| `CLAUDE_CODE_USE_VERTEX=1` | Google Vertex |
| `CLAUDE_CODE_USE_FOUNDRY=1` | Microsoft Azure Foundry |
| OAuth | Login via claude.ai (Pro/Max/Team/Enterprise) |

### Modelos Soportados

| Modelo | Input $/MTok | Output $/MTok | Contexto | Max Output | Notas |
|--------|-------------|--------------|----------|------------|-------|
| Opus 4.6 | $5.00 | $25.00 | 1M | 128K | Default Max/Team Premium |
| Sonnet 4.6 | $3.00 | $15.00 | 1M | 64K | Default Pro/Team Standard |
| Haiku 4.5 | $1.00 | $5.00 | 200K | 64K | Subagentes background |
| Fast Mode | $30.00 | $150.00 | 1M | 128K | Opus 4.6 a 2.5x velocidad |

Aliases: `default`, `sonnet`, `opus`, `haiku`, `sonnet[1m]`, `opus[1m]`, `opusplan`

### Pricing

| Plan | Precio | Modelo default | Notas |
|------|--------|----------------|-------|
| Pro | $20/mo | Sonnet 4.6 | ~5x uso free |
| Team Standard | $25/user/mo | Sonnet 4.6 | Admin controls |
| Team Premium | $150/user/mo | Opus 4.6 | Incluye Claude Code |
| Max (5x) | $100/mo | Opus 4.6 | 5x rate limit |
| Max (20x) | $200/mo | Opus 4.6 | 20x rate limit |
| API | Pay-per-use | Cualquiera | Sin surcharge 1M context |

### Capacidades Core

| Capacidad | Detalle |
|-----------|---------|
| 1M context | GA, sin surcharge, hasta 600 imágenes/PDFs |
| 28 tools built-in | Bash, Read, Edit, Write, Glob, Grep, WebFetch, WebSearch, Agent, Task*, Cron*, LSP, etc. |
| 22 hook events | SessionStart→SessionEnd lifecycle completo |
| Skills system | Bundled (/batch, /simplify, /loop, /debug, /claude-api) + custom |
| Subagentes | Built-in (Explore, Plan, General) + custom con frontmatter YAML |
| Agent Teams | Experimental: múltiples instancias coordinadas |
| Plugins | Marketplace oficial, 72+ plugins, LSP servers |
| Channels | Research preview: Telegram, Discord push events |
| MCP | stdio, HTTP, SSE + in-process SDK servers |
| Sandbox | OS-level: Seatbelt (macOS), bubblewrap (Linux) |
| Worktrees | Aislamiento git nativo para paralelismo |
| Voice | Push-to-talk dictation, 20 idiomas |
| Fast Mode | Opus 4.6 a 2.5x velocidad (research preview) |
| Headless | `claude -p` para CI/CD, JSON/stream output |
| Checkpoints | Rewind automático por prompt |
| Output Styles | Default, Explanatory, Learning + custom |

### Fortalezas / Debilidades

**Fortalezas:**
- Contexto 1M GA sin premium — líder en contexto real usable
- 22 hooks + 4 tipos (command, HTTP, prompt, agent) — automatización completa
- Worktrees + subagentes + /batch — paralelismo nativo de producción
- Sandbox OS-level (Seatbelt/bubblewrap) — seguridad sin Docker
- Agent SDK dual (TS+Python) — embedding en apps propias
- Ecosystem: plugins, channels, skills, MCP, LSP servers

**Debilidades:**
- Solo modelos Anthropic (salvo gateway/proxy)
- Fast mode 6x costo (research preview)
- Agent teams experimental, ~7x tokens vs sesión normal
- Channels solo research preview, requiere plugin install manual

### Config Snippet

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "claude-opus-4-6",
  "effortLevel": "high",
  "permissions": {
    "allow": ["Read", "Edit", "Bash(npm run *)", "Bash(git *)"],
    "deny": ["Read(.env)", "Read(.env.*)", "Bash(curl *)"]
  },
  "sandbox": { "enabled": true }
}
```

### KB Detallado

Ver `urn:dev:kb:claude-code-mastery` para guía operativa completa de maximización.
