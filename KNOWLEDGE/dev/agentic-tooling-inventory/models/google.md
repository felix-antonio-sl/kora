---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Google Models — Ficha Técnica"
domain: "dev"
tags: [models, google, gemini]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# Google Models

## Gemini 2.5 Pro

| Campo | Valor |
|-------|-------|
| Provider | Google |
| API Model ID | `gemini-2.5-pro` |
| Context Window | 1,000,000 tokens |
| Max Output | 65,536 tokens |
| Input $/MTok | $1.25 (<=200K) / $2.50 (>200K) |
| Output $/MTok | $10.00 (<=200K) / $15.00 (>200K) |
| Context Caching | 75-90% ahorro |
| Thinking/Reasoning | Yes |
| Vision | Yes (imagen, video, audio) |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** 1M context, multimodal líder (video/audio nativos), context caching agresivo, free tier en Gemini CLI.
**Weaknesses:** Pricing escalonado (>200K más caro), calidad de código un peldaño debajo de Opus/GPT-5.4.
**Best for:** Tasks multimodales, prototipado con free tier, large context analysis.
**Config CLI:** `gemini -m gemini-2.5-pro`
**Config OpenRouter:** `google/gemini-2.5-pro`

## Gemini 2.5 Flash

| Campo | Valor |
|-------|-------|
| Provider | Google |
| API Model ID | `gemini-2.5-flash` |
| Context Window | 1,000,000 tokens |
| Max Output | 65,536 tokens |
| Input $/MTok | $0.15 (<=200K) / $0.30 (>200K) |
| Output $/MTok | $0.60 (<=200K) / $2.50 (>200K) |
| Context Caching | 75-90% ahorro |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Fast |

**Strengths:** Muy barato, rápido, 1M context, thinking incluido, free tier disponible.
**Weaknesses:** Calidad inferior para coding complejo, output costoso en contextos >200K.
**Best for:** Bulk processing, tareas simples, prototipado, clasificación, pre-procesamiento.
**Config CLI:** `gemini -m gemini-2.5-flash`
**Config OpenRouter:** `google/gemini-2.5-flash`
