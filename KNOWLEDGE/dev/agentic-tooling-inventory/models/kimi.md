---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Kimi Models — Ficha Técnica"
domain: "dev"
tags: [models, kimi, moonshot]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# Kimi Models (Moonshot AI)

## Kimi K2

| Campo | Valor |
|-------|-------|
| Provider | Moonshot AI |
| API Model ID | `kimi-k2` |
| Context Window | 128,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.60 |
| Output $/MTok | $2.50 |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** Buen balance precio/rendimiento, agent swarm capabilities, competitive en coding benchmarks.
**Weaknesses:** Disponibilidad fuera de China puede ser intermitente, documentación limitada en inglés.
**Best for:** Tasks de implementación budget, agent workflows, coding competitivo.
**Config OpenRouter:** `moonshot/kimi-k2`

## Kimi K2.5

| Campo | Valor |
|-------|-------|
| Provider | Moonshot AI |
| API Model ID | `kimi-k2.5` |
| Context Window | 128,000 tokens |
| Max Output | 16,384 tokens |
| Input $/MTok | $0.60 |
| Output $/MTok | $3.00 |
| Thinking/Reasoning | Yes |
| Vision | Yes |
| Tool Use | Yes |
| Latency | Moderate |

**Strengths:** Mejora sobre K2 en razonamiento, competitive con modelos frontier en ciertos benchmarks.
**Weaknesses:** Mismas limitaciones de disponibilidad que K2.
**Best for:** Tasks que requieren razonamiento moderado a bajo costo.
**Config OpenRouter:** `moonshot/kimi-k2.5`
