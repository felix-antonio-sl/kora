---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "DeepSeek Models — Ficha Técnica"
domain: "dev"
tags: [models, deepseek, budget, open-source]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# DeepSeek Models

## DeepSeek V3.2

| Campo | Valor |
|-------|-------|
| Provider | DeepSeek |
| API Model ID | `deepseek-chat` |
| Context Window | 128,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.28 |
| Output $/MTok | $0.42 |
| Cache Hit | $0.028/MTok (90% ahorro) |
| Batch Discount | 50% ($0.14/$0.21) |
| Thinking/Reasoning | No |
| Vision | No |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** Extremadamente barato, ~90% calidad frontier en coding, cache hit 90% off, open weights.
**Weaknesses:** Contexto 128K (limitado vs 1M), sin vision, output corto (16K), servicio ocasionalmente inestable.
**Best for:** Bulk coding tasks, implementación estándar budget, batch processing.
**Config OpenRouter:** `deepseek/deepseek-chat`

## DeepSeek R1

| Campo | Valor |
|-------|-------|
| Provider | DeepSeek |
| API Model ID | `deepseek-reasoner` |
| Context Window | 128,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.28 |
| Output $/MTok | $0.42 |
| Cache Hit | $0.028/MTok (90% ahorro) |
| Thinking/Reasoning | Yes (chain of thought) |
| Vision | No |
| Tool Use | Yes |
| Latency | Slow |

**Strengths:** Reasoning a precio ultra-bajo, comparable a o3 en ciertos benchmarks.
**Weaknesses:** Lento, mismo contexto limitado, reasoning tokens consumen output budget.
**Best for:** Problemas algorítmicos budget, debugging que requiere razonamiento, análisis profundo barato.
**Config OpenRouter:** `deepseek/deepseek-reasoner`
