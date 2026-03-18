---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Gemini CLI — CLI Ficha Técnica"
domain: "dev"
tags: [cli, gemini-cli, google]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

## Gemini CLI — v0.33.2 (2026-03)

### Datos Básicos

| Campo | Valor |
|-------|-------|
| Versión | 0.33.2 |
| Instalación | `npm install -g @anthropic-ai/gemini-cli` o `npx @anthropic-ai/gemini-cli` |
| Requisitos | Node.js 18+ |
| Licencia | Apache 2.0 |
| Repo | github.com/google-gemini/gemini-cli |

### Acceso y API Keys

| Variable | Propósito |
|----------|-----------|
| `GOOGLE_API_KEY` | API directa (opcional — free tier usa OAuth) |
| `GOOGLE_CLOUD_PROJECT` | Vertex AI |

Vías de autenticación: Google OAuth (free tier), API key, Vertex AI service account.

### Modelos Soportados

| Modelo | Input $/MTok | Output $/MTok | Contexto | Notas |
|--------|-------------|--------------|----------|-------|
| Gemini 2.5 Pro | $1.25 (<=200K) / $2.50 (>200K) | $10.00 (<=200K) / $15.00 (>200K) | 1M | Default |
| Gemini 2.5 Flash | $0.15 (<=200K) / $0.30 (>200K) | $0.60 (<=200K) / $2.50 (>200K) | 1M | Budget |

### Pricing

| Plan | Precio | Incluye |
|------|--------|---------|
| Free tier | $0 | 1,000 req/día, Gemini 2.5 Pro, 1M context |
| API | Pay-per-use | Todos los modelos, rate limits superiores |

### Features Clave para Producción

- **FREE TIER genuino**: 1,000 req/día con Gemini 2.5 Pro y 1M context — ideal para prototipado y tareas budget
- **GEMINI.md**: Equivalente a CLAUDE.md para instrucciones de proyecto
- **Apache 2.0**: Open source
- **Multimodal nativo**: Imágenes, video, audio en prompts
- **Google Search grounding**: Búsqueda web integrada

### Fortalezas / Debilidades

**Fortalezas:**
- Free tier genuino — $0 para 1,000 req/día con modelo frontier
- 1M context window
- Multimodal líder (video, audio nativos)
- Google Search grounding integrado

**Debilidades:**
- Modelos solo Google
- Free tier con rate limits (1K req/día)
- Menos maduro que Claude Code/Codex para coding agentic
- Calidad de código inferior a Opus/GPT-5.4 en tareas complejas

### Config Snippet

```
# GEMINI.md (en raíz del proyecto)
You are working on [project]. Follow these conventions:
- Use TypeScript strict mode
- Run `npm test` before committing
```
