---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "GLM Models — Ficha Técnica"
domain: "dev"
tags: [models, glm, zhipu]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# GLM Models (Zhipu AI)

## GLM-4.6

| Campo | Valor |
|-------|-------|
| Provider | Zhipu AI |
| API Model ID | `glm-4.6` |
| Context Window | 128,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | ~$0.35 |
| Output $/MTok | ~$1.50 |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** #1 en LiveCodeBench (al momento de medición), excelente en coding competitivo, precio competitivo.
**Weaknesses:** Disponibilidad fuera de China limitada, documentación API limitada en inglés, contexto 128K.
**Best for:** Coding competitivo, implementación que requiere razonamiento, benchmarks.
**Config OpenRouter:** `zhipu/glm-4.6` (si disponible)

## GLM-4.7

| Campo | Valor |
|-------|-------|
| Provider | Zhipu AI |
| API Model ID | `glm-4.7` |
| Context Window | 128,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.40 |
| Output $/MTok | $1.75 |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** Evolución de GLM-4.6, mejoras en razonamiento y coding.
**Weaknesses:** Mismas limitaciones de disponibilidad internacional.
**Best for:** Coding tasks cuando se necesita diversidad de modelo a bajo costo.
