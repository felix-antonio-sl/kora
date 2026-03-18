---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "OpenRouter — Router Ficha Técnica"
domain: "dev"
tags: [router, openrouter, multi-provider]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

## OpenRouter

### Datos Básicos

| Campo | Valor |
|-------|-------|
| URL | openrouter.ai |
| Modelos | 290+ |
| Markup inference | 0% |
| Markup créditos | 5.5% en compra |
| API format | OpenAI-compatible |

### Acceso y API Keys

| Variable | Propósito |
|----------|-----------|
| `OPENROUTER_API_KEY` | API key única para todos los providers |

### Features Clave

- **0% markup en inference**: Pagas precio del provider, sin recargo
- **290+ modelos**: Todos los providers principales en un solo endpoint
- **Anthropic Skin**: Endpoint compatible con Anthropic API — permite usar Claude Code via OpenRouter
- **Fallback routing**: Configurar modelo primario + fallbacks automáticos
- **Rate limit pooling**: Agrega rate limits de múltiples providers
- **Usage tracking**: Dashboard de costos por modelo, por key

### Uso con CLIs

| CLI | Configuración |
|-----|---------------|
| Claude Code | `OPENROUTER_API_KEY` + seleccionar modelo OpenRouter |
| OpenCode | Provider "openrouter" en opencode.json |
| Codex CLI | No soportado nativamente |
| Gemini CLI | No soportado nativamente |

### Anthropic Skin

Endpoint que habla protocolo Anthropic (Messages API) pero rutea via OpenRouter. Permite usar Claude Code con cualquier modelo disponible en OpenRouter, no solo Anthropic.

```bash
export OPENROUTER_API_KEY="sk-or-..."
# Claude Code detecta automáticamente
```

### Fortalezas / Debilidades

**Fortalezas:**
- Single API key para todo
- 0% inference markup
- Anthropic Skin para Claude Code
- Ideal para cost optimization y model routing

**Debilidades:**
- 5.5% markup en compra de créditos
- Latencia adicional (~50-100ms) por hop
- No todos los features de cada provider (ej. prompt caching limitado)
- Disponibilidad depende de upstream providers
