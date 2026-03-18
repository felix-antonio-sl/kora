---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "OpenAI Models — Ficha Técnica"
domain: "dev"
tags: [models, openai, gpt-5, o3, o4]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# OpenAI Models

## GPT-5.4

| Campo | Valor |
|-------|-------|
| Provider | OpenAI |
| API Model ID | `gpt-5.4` |
| Context Window | 1,050,000 tokens |
| Max Output | 100,000 tokens |
| Input $/MTok | $2.50 |
| Output $/MTok | $15.00 |
| Cache Hit | $1.25/MTok (50% ahorro) |
| Batch Discount | 50% |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Computer Use | Yes (nativo) |
| Latency | Moderate |

**Strengths:** 1.05M context, computer use nativo, excelente para coding, diversidad de blind spots vs Claude.
**Weaknesses:** Output caro ($15/MTok), computer use consume muchos tokens.
**Best for:** Code review (diversidad vs Claude), implementación compleja, tasks que requieren computer use.
**Config CLI:** `codex --model gpt-5.4`
**Config OpenRouter:** `openai/gpt-5.4`

## GPT-5.2-Codex

| Campo | Valor |
|-------|-------|
| Provider | OpenAI |
| API Model ID | `gpt-5.2-codex` |
| Context Window | 1,050,000 tokens |
| Max Output | 100,000 tokens |
| Input $/MTok | $1.75 |
| Output $/MTok | $14.00 |
| Cache Hit | $0.88/MTok (50% ahorro) |
| Batch Discount | 50% |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** Optimizado para coding, más barato que GPT-5.4, calidad comparable en código.
**Weaknesses:** Menos generalista que GPT-5.4.
**Best for:** Implementación de código puro, refactoring, batch coding tasks.
**Config CLI:** `codex --model gpt-5.2-codex`

## o3

| Campo | Valor |
|-------|-------|
| Provider | OpenAI |
| API Model ID | `o3` |
| Context Window | 200,000 tokens |
| Max Output | 100,000 tokens |
| Input $/MTok | $2.00 |
| Output $/MTok | $8.00 |
| Thinking/Reasoning | Yes (chain of thought) |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Slow (reasoning) |

**Strengths:** Razonamiento profundo, excelente para problemas algorítmicos complejos.
**Weaknesses:** Lento, contexto limitado 200K, no ideal para tareas simples.
**Best for:** Debugging complejo, algoritmos, problemas matemáticos, arquitectura profunda.

## o4-mini

| Campo | Valor |
|-------|-------|
| Provider | OpenAI |
| API Model ID | `o4-mini` |
| Context Window | 200,000 tokens |
| Max Output | 100,000 tokens |
| Input $/MTok | $0.55 |
| Output $/MTok | $2.20 |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** Reasoning barato, buena relación calidad/precio para tareas que necesitan pensar.
**Weaknesses:** Calidad inferior a o3/GPT-5.4 en tareas complejas.
**Best for:** Razonamiento budget, clasificación inteligente, tareas que necesitan "pensar" sin costo alto.
