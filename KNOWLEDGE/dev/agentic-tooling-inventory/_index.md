---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Inventario de Herramientas y Modelos para Ingenieria Agéntica"
domain: "dev"
tags: [tooling, models, pricing, cli, openrouter, cost-optimization]
last_updated: "2026-03-18"
update_policy: "permanente — cada ficha debe tener datos < 30 dias"
---

# Inventario de Herramientas y Modelos para Ingenieria Agéntica

Repositorio centralizado de fichas técnicas para CLIs, routers y modelos AI usados en producción agéntica. Cada ficha contiene datos verificados con fecha de actualización.

## Indice

### CLIs

| Herramienta | Version | Licencia | Ficha |
|-------------|---------|----------|-------|
| Claude Code | v2.1.78 | Propietario | [cli/claude-code.md](cli/claude-code.md) |
| Codex CLI | latest | Propietario | [cli/codex-cli.md](cli/codex-cli.md) |
| OpenCode | v1.2.26 | MIT | [cli/opencode.md](cli/opencode.md) |
| Gemini CLI | v0.33.2 | Apache 2.0 | [cli/gemini-cli.md](cli/gemini-cli.md) |

### Routers

| Router | Ficha |
|--------|-------|
| OpenRouter | [routers/openrouter.md](routers/openrouter.md) |

### Modelos por Provider

| Provider | Modelos | Ficha |
|----------|---------|-------|
| Anthropic | Opus 4.6, Sonnet 4.6, Haiku 4.5 | [models/anthropic.md](models/anthropic.md) |
| OpenAI | GPT-5.4, GPT-5.2-Codex, o3, o4-mini | [models/openai.md](models/openai.md) |
| Google | Gemini 2.5 Pro, 2.5 Flash | [models/google.md](models/google.md) |
| DeepSeek | V3.2, R1 | [models/deepseek.md](models/deepseek.md) |
| Kimi | K2, K2.5 | [models/kimi.md](models/kimi.md) |
| Qwen | Qwen3-Coder, Qwen3.5-Plus | [models/qwen.md](models/qwen.md) |
| GLM | GLM-4.6, GLM-4.7 | [models/glm.md](models/glm.md) |
| MiniMax | M1 | [models/minimax.md](models/minimax.md) |
| Mistral | Large 3, Codestral | [models/mistral.md](models/mistral.md) |
| Meta | Llama 4 Maverick, Scout | [models/meta.md](models/meta.md) |

### Matrices de Selección

| Matriz | Ficha |
|--------|-------|
| Selección racional tarea x modelo | [_selection-matrix.md](_selection-matrix.md) |
