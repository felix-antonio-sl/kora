---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Codex CLI — CLI Ficha Técnica"
domain: "dev"
tags: [cli, codex-cli, openai]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

## Codex CLI — latest (2026-03)

### Datos Básicos

| Campo | Valor |
|-------|-------|
| Versión | latest (rolling) |
| Instalación | `npm install -g @openai/codex` |
| Requisitos | Node.js 22+ |
| Licencia | Apache 2.0 |
| Repo | github.com/openai/codex |

### Acceso y API Keys

| Variable | Propósito |
|----------|-----------|
| `OPENAI_API_KEY` | API directa (requerida) |

Vías de autenticación: API key directa.

### Modelos Soportados

| Modelo | Input $/MTok | Output $/MTok | Contexto | Notas |
|--------|-------------|--------------|----------|-------|
| GPT-5.4 | $2.50 | $15.00 | 1.05M | Default |
| GPT-5.3-Codex | $1.75 | $14.00 | 1.05M | Optimizado código |

### Pricing

| Plan | Precio | Incluye |
|------|--------|---------|
| API | Pay-per-use | Todos los modelos |

### Features Clave para Producción

- **Kernel sandbox**: Seatbelt (macOS) / Landlock (Linux) — aislamiento a nivel OS
- **config.toml**: Configuración por proyecto o global
- **Full auto mode**: `codex --approval-mode full-auto` para ejecución sin intervención
- **Multimodal**: Soporte imágenes en prompts
- **Open source**: Apache 2.0, extensible

### Fortalezas / Debilidades

**Fortalezas:**
- Sandbox kernel-level nativo (superior a Docker para CLI)
- GPT-5.4 con 1.05M context
- Full auto mode para batch processing
- Open source, auditable

**Debilidades:**
- Solo modelos OpenAI
- Config menos rica que Claude Code (sin hooks)
- Sin worktrees nativos
- Node 22+ requerido

### Config Snippet

```toml
# ~/.codex/config.toml
model = "gpt-5.4"
approval_mode = "suggest"

[history]
persistence = "global"
save_history = true
```
