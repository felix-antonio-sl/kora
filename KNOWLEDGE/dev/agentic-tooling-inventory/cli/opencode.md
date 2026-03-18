---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "OpenCode — CLI Ficha Técnica"
domain: "dev"
tags: [cli, opencode, open-source]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

## OpenCode — v1.2.26 (2026-03)

### Datos Básicos

| Campo | Valor |
|-------|-------|
| Versión | 1.2.26 |
| Instalación | `go install github.com/opencode-ai/opencode@latest` o binarios |
| Requisitos | Go 1.21+ (para build) o binario standalone |
| Licencia | MIT |
| Repo | github.com/opencode-ai/opencode |

### Acceso y API Keys

| Variable | Propósito |
|----------|-----------|
| `ANTHROPIC_API_KEY` | Anthropic models |
| `OPENAI_API_KEY` | OpenAI models |
| `GOOGLE_API_KEY` | Google models |
| `OPENROUTER_API_KEY` | OpenRouter (75+ providers) |
| `DEEPSEEK_API_KEY` | DeepSeek models |

Vías de autenticación: API key por provider. Soporta 75+ providers via configuración.

### Modelos Soportados

Todos los modelos de cualquier provider compatible con OpenAI API format, Anthropic API, Google API, o custom endpoints. 75+ providers out of the box.

### Pricing

| Plan | Precio | Incluye |
|------|--------|---------|
| Software | $0 | MIT, sin costo de herramienta |
| API | Pay-per-use por provider | Según modelo elegido |

### Features Clave para Producción

- **Multi-provider**: 75+ providers con una sola herramienta
- **opencode.json**: Configuración JSONC por proyecto
- **TUI**: Terminal UI rica con paneles de contexto
- **$0 tool cost**: Sin markup, sin suscripción
- **LSP integration**: Language server protocol para contexto
- **Go binary**: Single binary, sin dependencias runtime

### Fortalezas / Debilidades

**Fortalezas:**
- Agnóstico de provider — ideal para cost optimization
- MIT license, sin vendor lock-in
- Binary standalone, deploy trivial
- TUI superior para monitoring

**Debilidades:**
- Comunidad más pequeña que Claude Code/Codex
- Sin sandbox nativo
- Sin hooks/lifecycle events
- Menos polish en edge cases

### Config Snippet

```jsonc
// opencode.json
{
  "provider": "anthropic",
  "model": "claude-sonnet-4-6",
  "mcpServers": {}
}
```
