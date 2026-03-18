---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Meta Models — Ficha Técnica"
domain: "dev"
tags: [models, meta, llama, open-source]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# Meta Models

## Llama 4 Maverick

| Campo | Valor |
|-------|-------|
| Provider | Meta (via providers) |
| API Model ID | `meta-llama/llama-4-maverick` |
| Context Window | 1,000,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.15 |
| Output $/MTok | $0.60 |
| Thinking/Reasoning | No |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** Ultra-barato, 1M context, open source, multimodal, amplia disponibilidad via providers.
**Weaknesses:** Calidad 82% frontier en coding, sin reasoning nativo, output corto.
**Best for:** Bulk processing, tareas simples masivas, pre-procesamiento, filtrado de datos.
**Config OpenRouter:** `meta-llama/llama-4-maverick`

## Llama 4 Scout

| Campo | Valor |
|-------|-------|
| Provider | Meta (via providers) |
| API Model ID | `meta-llama/llama-4-scout` |
| Context Window | 10,000,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.08 |
| Output $/MTok | $0.30 |
| Thinking/Reasoning | No |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** 10M context (mayor del mercado), ultra-barato ($0.08 input), open source.
**Weaknesses:** Calidad general baja para coding, diseñado para retrieval no generación, output muy corto.
**Best for:** Análisis de codebases masivos, búsqueda en contexto ultra-largo, tareas de retrieval.
**Config OpenRouter:** `meta-llama/llama-4-scout`
