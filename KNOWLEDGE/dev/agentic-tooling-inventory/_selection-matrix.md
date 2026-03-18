---
_manifest:
  urn: "urn:dev:kb:agentic-tooling-inventory"
  type: "knowledge_article"
  version: "1.0.0"
title: "Matriz de Selección Racional: Tarea x Modelo"
domain: "dev"
tags: [selection-matrix, cost-optimization, model-routing]
last_updated: "2026-03-18"
parent: "urn:dev:kb:agentic-tooling-inventory"
---

# Matriz de Selección Racional

## Por Tarea

| Tarea | Tier 1 (Quality) | Tier 2 (Balance) | Tier 3 (Budget) |
|-------|-------------------|-------------------|-------------------|
| Arquitectura/diseño | Opus 4.6 ($5/$25) | GPT-5.4 ($2.50/$15) | — |
| Implementación feature | Codex GPT-5.4 | Sonnet 4.6 | DeepSeek V3.2 |
| Refactoring/cleanup | Opus 4.6 | Sonnet 4.6 | DeepSeek V3.2 |
| Code review | Modelo != implementor | — | — |
| Tests | Mismo que implementó | — | Haiku 4.5 |
| Bug fix simple | Sonnet 4.6 | Flash ($0.30/$2.50) | Codestral ($0.20/$0.60) |
| Bulk/repetitivo | — | Flash | DeepSeek / Scout |
| Orquestación (steipete) | Sonnet 4.6 | Haiku 4.5 | — |
| Prototipado | — | Gemini Free Tier | — |

## Ratio Calidad/Costo (coding tasks, blended 3:1 input:output)

| Rank | Modelo | $/blended MTok | Calidad relativa |
|------|--------|----------------|------------------|
| 1 | DeepSeek V3.2 | ~$0.35 | 90% frontier |
| 2 | Gemini 2.5 Flash | ~$1.40 | 85% frontier |
| 3 | Codestral | ~$0.40 | 80% frontier |
| 4 | Llama 4 Maverick | ~$0.38 | 82% frontier |
| 5 | Qwen3-Coder (DI) | ~$0.41 | 88% frontier |
| 6 | Sonnet 4.6 | ~$9.00 | 95% frontier |
| 7 | GPT-5.4 | ~$8.75 | 97% frontier |
| 8 | Opus 4.6 | ~$15.00 | 100% frontier |

## Técnicas de Reducción de Costo Transversales

| Técnica | Ahorro | Cuándo |
|---------|--------|--------|
| Prompt Caching (Anthropic) | 90% input | System prompts repetidos |
| Context Caching (Google) | 75-90% input | Contextos grandes repetidos |
| DeepSeek Cache Hit | 90% input | Queries secuenciales relacionadas |
| Batch API (todos) | 50% | Procesamiento no-urgente |
| Model routing | Variable | Modelo barato para tareas simples |
