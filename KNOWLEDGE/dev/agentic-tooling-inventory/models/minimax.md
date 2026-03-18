---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "MiniMax Models — Ficha Técnica"
domain: "dev"
tags: [models, minimax, long-context]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# MiniMax Models

## MiniMax M1

| Campo | Valor |
|-------|-------|
| Provider | MiniMax |
| API Model ID | `minimax-m1` |
| Context Window | 1,000,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.40 |
| Output $/MTok | $1.76 |
| Thinking/Reasoning | Yes |
| Vision | No |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** 1M context a precio muy bajo ($0.40 input), lightning attention architecture para long context eficiente, rápido para su tamaño de contexto.
**Weaknesses:** Sin vision, calidad general inferior a frontier models, ecosistema limitado, documentación escasa.
**Best for:** Large context analysis budget, procesamiento de documentos largos donde el contexto es más importante que la calidad de razonamiento.
**Config OpenRouter:** `minimax/minimax-m1`
