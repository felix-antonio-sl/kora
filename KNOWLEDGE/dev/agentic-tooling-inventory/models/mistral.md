---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Mistral Models — Ficha Técnica"
domain: "dev"
tags: [models, mistral, codestral]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# Mistral Models

## Mistral Large 3

| Campo | Valor |
|-------|-------|
| Provider | Mistral AI |
| API Model ID | `mistral-large-latest` |
| Context Window | 128,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.50 |
| Output $/MTok | $1.50 |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** Barato para un modelo generalista competente, buen tool use, multilingüe fuerte.
**Weaknesses:** Calidad de coding inferior a frontier, contexto 128K.
**Best for:** Tareas generalistas budget, herramientas multi-idioma, clasificación.
**Config OpenRouter:** `mistral/mistral-large-latest`

## Codestral

| Campo | Valor |
|-------|-------|
| Provider | Mistral AI |
| API Model ID | `codestral-latest` |
| Context Window | 256,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.20 |
| Output $/MTok | $0.60 |
| Thinking/Reasoning | No |
| Vision | No |
| Tool Use | Yes |
| Latency | Very Fast |

**Strengths:** Ultra-barato para coding ($0.20/$0.60), 86.6% HumanEval, 256K context, muy rápido.
**Weaknesses:** Sin vision, sin reasoning, calidad 80% frontier, no apto para tareas complejas.
**Best for:** Bug fixes simples, code completion, bulk refactoring, tareas de código repetitivas.
**Config OpenRouter:** `mistral/codestral-latest`
