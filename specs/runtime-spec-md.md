---
_manifest:
  urn: "urn:kora:kb:runtime-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 01, 07, adapters Anthropic/OpenAI/Google/OpenClaw"
version: "3.0.0"
status: published
tags: [spec, runtime, deployment, adapters, preservation]
lang: es
---

# KORA/Runtime-Spec v3.0.0

## 1. Definicion

Esta especificacion gobierna la adaptación de un workspace KORA a un runtime concreto.

`runtime-spec` **NO** redefine el agente; gobierna su proyección a un substrato operacional.

## 2. Escalera de preservacion

Todo runtime KORA **DEBE** preservar:

1. estructura del workspace
2. security envelope
3. interfaz semántica declarada

Todo runtime KORA **DEBERIA** aproximar equivalencia semántica objetivo para el mismo input.

Nunca se promete bisimulación estricta entre modelos o providers distintos.

Traces to: formal/07 §2 (Behavioral Preservation Ladder)

## 3. Model routing

`model_routing` pertenece a `config.json`, no al bootstrap en Markdown.

Campos relevantes:

- `tier_default`
- `tier_overrides`
- `fallback_chain`
- `budget`
- `diversity`

## 4. Adapters

Un adapter de runtime **DEBE** mapear:

- `AGENTS.md` -> instrucciones de behavior
- `TOOLS.md` -> tools/functions del runtime
- `SOUL.md` / `USER.md` -> contexto aplicable
- `config.json` -> enforcement server-side
- skills -> discovery / lazy load

## 5. Reglas

1. El runtime **NO DEBE** inyectar `config.json` como texto al LLM.
2. El runtime **DEBE** aplicar `config.json` server-side.
3. Fallback entre modelos **NO DEBE** alterar FSM, skills disponibles ni constraints.
4. Cambios de tier **PUEDEN** degradar calidad semántica, pero **NO DEBEN** romper preservación estructural.

## 6. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Preservacion estructural | FSM, skills e interfaz declarada se preservan | runtime | Corregir adapter |
| Security server-side | `config.json` no se delega al LLM | runtime | Mover enforcement |
| Model routing segregado | Tier, fallback y budget viven en `config.json` | lint | Reubicar config |
| Fallback seguro | Cambia el modelo, no la topología del agente | runtime | Corregir adapter |
