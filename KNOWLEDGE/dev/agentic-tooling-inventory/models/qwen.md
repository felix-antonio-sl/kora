---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Qwen Models — Ficha Técnica"
domain: "dev"
tags: [models, qwen, alibaba]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# Qwen Models (Alibaba)

## Qwen3-Coder

| Campo | Valor |
|-------|-------|
| Provider | Alibaba Cloud |
| API Model ID | `qwen3-coder` |
| Context Window | 256,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $1.50 |
| Output $/MTok | $7.50 |
| Thinking/Reasoning | Yes |
| Vision | No |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** Especializado en coding, 256K context, 88% calidad frontier, open weights disponibles.
**Weaknesses:** Sin vision, pricing medio (no budget no frontier), disponibilidad API variable.
**Best for:** Coding tasks que necesitan contexto largo (256K) a precio intermedio, coding competitivo.
**Config OpenRouter:** `qwen/qwen3-coder`

## Qwen3.5-Plus

| Campo | Valor |
|-------|-------|
| Provider | Alibaba Cloud |
| API Model ID | `qwen3.5-plus` |
| Context Window | 1,000,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.30 |
| Output $/MTok | $1.56 |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** 1M context a precio muy bajo, multimodal, buena calidad general.
**Weaknesses:** Calidad de coding inferior a modelos especializados, output corto.
**Best for:** Large context analysis barata, tareas generalistas, pre-procesamiento de documentos largos.
**Config OpenRouter:** `qwen/qwen3.5-plus`
