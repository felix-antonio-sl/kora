---
_manifest:
  urn: "urn:kora:kb:agent-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 01, 04, 07"
version: "8.1.0"
status: published
tags: [spec, agentes, workspace, discovery, validation]
lang: es
---

# KORA/Agent-Spec v8.1.0

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

Los cuatro `.md` bootstrap usan identidad URN `agent-bootstrap`. `config.json` **PUEDE** incluir `_manifest` y, si lo hace, usa tambien `agent-bootstrap`.

`_manifest.type` expresa el kind estructural del componente y **DEBE** usar:

- `bootstrap_agents` para `AGENTS.md`
- `bootstrap_soul` para `SOUL.md`
- `bootstrap_user` para `USER.md`
- `bootstrap_tools` para `TOOLS.md`
- `bootstrap_config` para `config.json`

## 3. Segregacion

### 3.1 Gramatica canonica de `AGENTS.md`

Todo `AGENTS.md` **DEBE** incluir, en este orden logico, las siguientes secciones:

1. `## 1. FSM`
2. `## 2. Reglas Duras`
3. `## 3. Co-induccion`
4. `## 4. Contexto Multi-turno`
5. `## 5. Wiring`

Se permiten secciones adicionales solo si no sustituyen ni mezclan esa columna vertebral.

### 3.2 Sintaxis canonica de la FSM

Cada estado **DEBE** declararse como una linea numerada con esta forma:

```markdown
1. STATE: S-DISPATCHER -> ACT: Clasificar ... -> Trans: IF condicion -> S-DESTINO.
```

Reglas:

1. Los nombres de estado **DEBEN** usar identidad `S-*`.
2. Toda transicion **DEBE** ser explicita.
3. Los self-loops **DEBEN** declararse de forma explicita.
4. Los estados terminales **DEBEN** usar `Trans: [terminal]` o devolver control a un estado no terminal declarado.
5. `ACT` **PUEDE** invocar Skills, pero **NO DEBE** mezclar tono, security ni wiring oculto.

### 3.3 Invariantes de behavior

1. La FSM **DEBE** tener `S-DISPATCHER` como punto de entrada y `S-END` como cierre canonico.
2. Toda rama declarada **DEBE** ser alcanzable desde `S-DISPATCHER`.
3. Para un mismo estado, las ramas **NO DEBEN** introducir ambiguedad no declarada; el determinismo es el default.
4. El agente **NO DEBE** terminar sin un regimen de verificacion terminal declarado en `## 3. Co-induccion`.
5. `AGENTS.md` **DEBE** expresar control puro: estados, acciones, transiciones, checks terminales y wiring declarado.

Traces to: formal/01 §3.2 (Determinism in M) ; formal/01 §3.3 (Co-induction at Terminal States)

### 3.4 Segregacion de componentes

1. `AGENTS.md` **DEBE** contener FSM, reglas duras, co-induccion, contexto multi-turno y wiring.
2. `SOUL.md` **DEBE** contener solo identidad, tono y paradigma.
3. `USER.md` **DEBE** contener solo contexto del operador.
4. `TOOLS.md` **DEBE** contener solo interfaz semantica.
5. `config.json` **DEBE** contener solo constraints, runtime capabilities y politica operativa precompilada.
6. Ningun componente **DEBE** contener contenido rector de otro; en especial, la fenomenologia **NO DEBE** contaminar la FSM y la seguridad **NO DEBE** vivir en prosa de bootstrap.

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

Todo CM referenciado en `AGENTS.md` **DEBE** existir en `skills/` como Skill degenerado conforme a `skill-spec-md`.

El bootstrap del agente **NO DEBE** contener CM inline.

## 7. Wiring

Toda ruta a otro agente **DEBE** apuntar a un workspace resoluble. Las rutas lógicas no resolubles son inválidas.

Reglas:

1. Toda composicion inter-agente **DEBE** declararse en `AGENTS.md`; el wiring implicito es invalido.
2. El sub-agente **PUEDE** heredar behavior e interface solo en la medida declarada por el wiring.
3. `SOUL.md` y `USER.md` **DEBEN** disiparse en sub-agentes salvo que una spec superior declare explicitamente otra cosa.
4. El sistema compuesto **DEBE** ser razonable desde agentes + rutas declaradas, no desde side effects ocultos.

Traces to: formal/01 §2.3 (Dissipation) ; formal/01 §6.2 (Sub-Agent Adjunction) ; formal/01 §6.3 (Compositionality of Wiring)

## 8. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Gramatica de behavior | `AGENTS.md` contiene FSM, Reglas Duras, Co-induccion, Contexto Multi-turno y Wiring | lint | Normalizar bootstrap |
| FSM canonica | Estados `S-*`, transiciones explicitas, `S-DISPATCHER` y `S-END` presentes | lint | Reescribir FSM |
| Topologia workspace | Existen los 5 componentes base | lint | Crear faltantes |
| Segregacion | Ningun componente invade el rol de otro | manual | Reescribir componente |
| Behavior puro | La FSM no mezcla fenomenologia ni security | lint | Extraer contenido al componente correcto |
| Interfaz cerrada | `TOOLS.md` = `config.json.tools.allow` | lint | Alinear interfaz |
| Runtime segregado | Permisos crudos viven en `runtime_capabilities` | lint | Mover permisos |
| Skills resolubles | Todo CM referido existe | lint | Crear o corregir skill |
| Discovery filtrado | Security puede excluir skills incompatibles | runtime | Ajustar policy |
| Co-induccion terminal | Existe verificacion terminal antes del output final | manual | Declarar o reforzar protocolo terminal |
| Routing resoluble | Toda ruta inter-agente existe | lint | Corregir o crear destino |
