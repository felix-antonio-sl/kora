---
_manifest:
  urn: "urn:kora:kb:agent-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 01, 04, 07"
version: "8.0.0"
status: published
tags: [spec, agentes, workspace, discovery, validation]
lang: es
---

# KORA/Agent-Spec v8.0.0

## 1. Definicion

Un agente KORA es un workspace ejecutable compuesto por cinco componentes:

1. `AGENTS.md` — behavior
2. `TOOLS.md` — interfaz semántica
3. `SOUL.md` y `USER.md` — estado y contexto
4. `config.json` — security y runtime envelope
5. `skills/` — capabilities lazy-load

## 2. Topologia obligatoria

```text
agents/{namespace}/{nombre}/
  AGENTS.md
  SOUL.md
  USER.md
  TOOLS.md
  config.json
  skills/
```

Los cuatro `.md` bootstrap usan identidad `agent-bootstrap`. `config.json` **PUEDE** incluir `_manifest` y, si lo hace, usa tambien `agent-bootstrap`.

## 3. Segregacion

Reglas:

1. `AGENTS.md` **DEBE** contener FSM, reglas duras, contexto y wiring.
2. `SOUL.md` **DEBE** contener solo identidad, tono y paradigma.
3. `USER.md` **DEBE** contener solo contexto del operador.
4. `TOOLS.md` **DEBE** contener solo interfaz semántica.
5. `config.json` **DEBE** contener solo constraints, runtime capabilities y política operativa precompilada.

Traces to: formal/01 §2.2 (Fiber Independence)

## 4. Interfaz

`TOOLS.md` declara herramientas semánticas invocables por el LLM.

`config.json.tools.allow` **DEBE** ser exactamente el conjunto de nombres declarados en `TOOLS.md`.

`config.json.runtime_capabilities` declara permisos crudos del runtime y **NO DEBE** contaminar la interfaz semántica.

## 5. Security y runtime envelope

Campos relevantes de `config.json`:

- `allowed_kb`
- `sandbox.mode = strict | permissive | isolated | off`
- `tools.allow`
- `tools.deny`
- `runtime_capabilities.allow`
- `runtime_capabilities.deny`
- `sub_agents.max_depth`
- `sub_agents.max_concurrent`
- `limits`
- `model_routing`

Reglas:

1. `sub_agents.max_concurrent` **PUEDE** omitirse; si existe, **DEBE** ser `>= 1`.
2. `config.json` es inmutable desde el LLM.
3. Discovery de skills **DEBE** filtrarse por security.

Traces to: formal/01 §1.3 (M-Immutability) ; formal/04 §2.4 (Filtered Discovery)

## 6. Skills

Todo CM referenciado en `AGENTS.md` **DEBE** existir en `skills/` como Skill degenerado o referenciar un Skill extendido conforme a `skill-spec-md`.

El bootstrap del agente **NO DEBE** contener CM inline.

## 7. Wiring

Toda ruta a otro agente **DEBE** apuntar a un workspace resoluble. Las rutas lógicas no resolubles son inválidas.

## 8. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Topologia workspace | Existen los 5 componentes base | lint | Crear faltantes |
| Segregacion | Ningun componente invade el rol de otro | manual | Reescribir componente |
| Interfaz cerrada | `TOOLS.md` = `config.json.tools.allow` | lint | Alinear interfaz |
| Runtime segregado | Permisos crudos viven en `runtime_capabilities` | lint | Mover permisos |
| Skills resolubles | Todo CM referido existe | lint | Crear o corregir skill |
| Discovery filtrado | Security puede excluir skills incompatibles | runtime | Ajustar policy |
| Routing resoluble | Toda ruta inter-agente existe | lint | Corregir o crear destino |
