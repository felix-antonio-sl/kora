---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Anthropic Models — Ficha Técnica"
domain: "dev"
tags: [models, anthropic, opus, sonnet, haiku]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# Anthropic Models

## Claude Opus 4.6

| Campo | Valor |
|-------|-------|
| Provider | Anthropic |
| API Model ID | `claude-opus-4-6` |
| Context Window | 1,000,000 tokens |
| Max Output | 128,000 tokens |
| Input $/MTok | $5.00 |
| Output $/MTok | $25.00 |
| Cache Write | $6.25/MTok |
| Cache Hit | $0.50/MTok (90% ahorro) |
| Batch Discount | 50% |
| Thinking/Reasoning | Yes (extended thinking) |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** Máxima calidad en coding, 1M context real usable, extended thinking para problemas complejos, SWE-bench ~80%.
**Weaknesses:** Caro ($25/MTok output), latencia moderada, no el más rápido para tareas simples.
**Best for:** Implementación de features complejas, refactoring profundo, arquitectura, debugging difícil.
**Config CLI:** `claude --model claude-opus-4-6`
**Config OpenRouter:** `anthropic/claude-opus-4-6`

## Claude Sonnet 4.6

| Campo | Valor |
|-------|-------|
| Provider | Anthropic |
| API Model ID | `claude-sonnet-4-6` |
| Context Window | 200,000 tokens |
| Max Output | 64,000 tokens |
| Input $/MTok | $3.00 |
| Output $/MTok | $15.00 |
| Cache Write | $3.75/MTok |
| Cache Hit | $0.30/MTok (90% ahorro) |
| Batch Discount | 50% |
| Thinking/Reasoning | Yes (extended thinking) |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** Excelente balance calidad/velocidad/costo, 95% calidad frontier, rápido.
**Weaknesses:** 200K context (vs 1M de Opus), output más corto.
**Best for:** Orquestación, bug fixes, implementación estándar, tareas donde velocidad importa.
**Config CLI:** `claude --model claude-sonnet-4-6`
**Config OpenRouter:** `anthropic/claude-sonnet-4-6`

## Claude Haiku 4.5

| Campo | Valor |
|-------|-------|
| Provider | Anthropic |
| API Model ID | `claude-haiku-4-5-20251001` |
| Context Window | 200,000 tokens |
| Max Output | 8,192 tokens |
| Input $/MTok | $1.00 |
| Output $/MTok | $5.00 |
| Cache Write | $1.25/MTok |
| Cache Hit | $0.10/MTok (90% ahorro) |
| Batch Discount | 50% |
| Thinking/Reasoning | No |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Very Fast |

**Strengths:** Muy barato, muy rápido, suficiente para tareas simples.
**Weaknesses:** Output limitado (8K), sin reasoning, calidad inferior para coding complejo.
**Best for:** Clasificación, tareas simples, tests triviales, orquestación budget.
**Config CLI:** `claude --model claude-haiku-4-5-20251001`
**Config OpenRouter:** `anthropic/claude-haiku-4-5-20251001`
