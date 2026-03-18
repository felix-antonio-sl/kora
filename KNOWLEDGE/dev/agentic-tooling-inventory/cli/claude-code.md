---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Claude Code — CLI Ficha Técnica"
domain: "dev"
tags: [cli, claude-code, anthropic]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

## Claude Code — v2.1.78 (2026-03)

### Datos Básicos

| Campo | Valor |
|-------|-------|
| Versión | 2.1.78 |
| Instalación | `npm install -g @anthropic-ai/claude-code` |
| Requisitos | Node.js 18+ |
| Licencia | Propietario (Anthropic) |
| Repo | — |

### Acceso y API Keys

| Variable | Propósito |
|----------|-----------|
| `ANTHROPIC_API_KEY` | API directa |
| `OPENROUTER_API_KEY` | Via OpenRouter |
| `CLAUDE_CODE_USE_BEDROCK=1` | AWS Bedrock |
| `CLAUDE_CODE_USE_VERTEX=1` | Google Vertex |

Vías de autenticación: API key directa, OpenRouter, AWS Bedrock, Google Vertex, OAuth (Max plan).

### Modelos Soportados

| Modelo | Input $/MTok | Output $/MTok | Contexto | Notas |
|--------|-------------|--------------|----------|-------|
| Opus 4.6 | $5.00 | $25.00 | 1M | Default Max plan |
| Sonnet 4.6 | $3.00 | $15.00 | 200K | Default Pro plan |
| Haiku 4.5 | $1.00 | $5.00 | 200K | Budget option |

### Pricing

| Plan | Precio | Incluye |
|------|--------|---------|
| Pro | $20/mo | Sonnet 4.6, límites moderados |
| Max (5x) | $100/mo | Opus 4.6, 5x rate |
| Max (20x) | $200/mo | Opus 4.6, 20x rate |
| API | Pay-per-use | Todos los modelos |

### Features Clave para Producción

- **1M context window** (GA) — codebase completos en contexto
- **Hooks**: 17 lifecycle points (PreToolUse, PostToolUse, Notification, etc.)
- **CLAUDE.md**: Documento de instrucciones persistente por proyecto
- **Worktrees**: Aislamiento git para obreros paralelos
- **Agent mode**: Subagents con tipos especializados (Explore, Plan, code-reviewer)
- **MRCR**: 78.3% (Multi-turn Reasoning and Code Reasoning)
- **Background agents**: Ejecución asíncrona con notificación

### Fortalezas / Debilidades

**Fortalezas:**
- Contexto 1M GA — líder en contexto real usable
- Hooks system para automatización
- Worktrees nativos para paralelismo
- CLAUDE.md como memoria de proyecto

**Debilidades:**
- Solo modelos Anthropic (salvo OpenRouter/Bedrock/Vertex)
- Max plan costoso para uso intensivo
- Sin sandbox kernel-level nativo (depende de Docker)

### Config Snippet

```json
{
  "model": "claude-opus-4-6",
  "permissions": {
    "allow": ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]
  }
}
```
