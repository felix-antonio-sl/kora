---
_manifest:
  urn: "urn:kora:kb:agent-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 01, 02, 04, 07"
version: "8.4.0"
status: published
tags: [spec, agentes, workspace, discovery, validation]
lang: es
---

# KORA/Agent-Spec v8.4.0

## 1. Definicion

Un agente KORA es un workspace ejecutable compuesto por cinco componentes:

1. `AGENTS.md` — behavior
2. `TOOLS.md` — interfaz semantica
3. `SOUL.md` y `USER.md` — estado y contexto
4. `config.json` — security y runtime envelope
5. `skills/` — capabilities lazy-load degeneradas o extendidas

## 2. Definiciones

| Termino     | Definicion                                                          |
| ----------- | ------------------------------------------------------------------- |
| Workspace   | Directorio autocontenido con los 5 componentes base del agente      |
| FSM         | Maquina de estados finitos que gobierna el behavior del agente      |
| Segregacion | Principio de que cada componente solo contiene su materia propia    |
| Wiring      | Declaracion explicita de rutas de composicion inter-agente          |
| CM          | Identificador simbolico de Skill activable por la FSM; se resuelve a `skills/CM-*.md` o `skills/CM-*/SKILL.md` |
| Discovery   | Proceso por el cual el agente encuentra y activa Skills disponibles |

## 3. Topologia obligatoria

```text
agents/{namespace}/{nombre}/
  AGENTS.md
  SOUL.md
  USER.md
  TOOLS.md
  config.json
  skills/
    CM-EJEMPLO.md
    CM-EJEMPLO/
      SKILL.md
      scripts/
      references/
      assets/
```

Los cuatro `.md` bootstrap usan identidad URN `agent-bootstrap`. `config.json` **PUEDE** incluir `_manifest` y, si lo hace, usa tambien `agent-bootstrap`.

`_manifest.type` expresa el kind estructural del componente y **DEBE** usar:

- `bootstrap_agents` para `AGENTS.md`
- `bootstrap_soul` para `SOUL.md`
- `bootstrap_user` para `USER.md`
- `bootstrap_tools` para `TOOLS.md`
- `bootstrap_config` para `config.json`

## 4. Segregacion

### 4.1 Gramatica canonica de `AGENTS.md`

Todo `AGENTS.md` **DEBE** incluir, en este orden logico, las siguientes secciones:

1. `## 1. FSM`
2. `## 2. Reglas Duras`
3. `## 3. Co-induccion`
4. `## 4. Contexto Multi-turno`
5. `## 5. Wiring`

Se permiten secciones adicionales solo si no sustituyen ni mezclan esa columna vertebral.

### 4.2 Sintaxis canonica de la FSM

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
6. Cuando multiples condiciones de transicion son evaluables simultaneamente, el estado **DEBE** declarar precedencia explicita (orden numerico, prioridad, o exclusion mutua). La ambiguedad implicita es invalida.
7. La FSM **DEBE** referir Skills por su identificador simbolico `CM-*`; la materializacion degenerada o extendida del Skill se resuelve fuera de `AGENTS.md`.

Correcto:

```markdown
3. STATE: S-ANALYSIS -> ACT: Evaluar input.
   -> Trans: IF error_critico -> S-ESCALATE [prioridad 1]
   -> Trans: IF requiere_revision -> S-REVIEW [prioridad 2]
   -> Trans: IF completo -> S-OUTPUT [prioridad 3]
```

Incorrecto:

```markdown
3. STATE: S-ANALYSIS -> ACT: Evaluar input.
   -> Trans: IF error_critico -> S-ESCALATE
   -> Trans: IF requiere_revision -> S-REVIEW
   -> Trans: IF completo -> S-OUTPUT
```

Rationale: Sin precedencia explicita, si `error_critico` y `requiere_revision` coexisten, el runtime no puede determinar cual transicion ejecutar.

### 4.3 Invariantes de behavior

1. La FSM **DEBE** tener `S-DISPATCHER` como punto de entrada y `S-END` como cierre canonico.
2. Toda rama declarada **DEBE** ser alcanzable desde `S-DISPATCHER`.
3. Para un mismo estado, las ramas **NO DEBEN** introducir ambiguedad no declarada; el determinismo es el default.
4. El agente **NO DEBE** terminar sin un regimen de verificacion terminal declarado en `## 3. Co-induccion`.
5. `AGENTS.md` **DEBE** expresar control puro: estados, acciones, transiciones, checks terminales y wiring declarado.

Traces to: formal/01 §3.2 (Determinism in M) ; formal/01 §3.3 (Co-induction at Terminal States)

### 4.4 Segregacion de componentes

1. `AGENTS.md` **DEBE** contener FSM, reglas duras, co-induccion, contexto multi-turno y wiring.
2. `SOUL.md` **DEBE** contener solo identidad, tono y paradigma.
3. `USER.md` **DEBE** contener solo contexto del operador.
4. `TOOLS.md` **DEBE** contener solo interfaz semantica: nombre, firma, parametros, cuando usar, cuando NO usar, notas semanticas y descripcion funcional. **NO DEBE** contener politica operativa (confirmaciones, aprobaciones, restricciones de uso) ni comportamiento condicional runtime; esas reglas viven en `config.json`.
5. `config.json` **DEBE** contener solo constraints, runtime capabilities y politica operativa precompilada.
6. Ningun componente **DEBE** contener contenido rector de otro; en especial, la fenomenologia **NO DEBE** contaminar la FSM y la seguridad **NO DEBE** vivir en prosa de bootstrap.

Traces to: formal/01 §2.2 (Fiber Independence)

## 5. Interfaz

`TOOLS.md` declara herramientas semanticas invocables por el LLM.

`config.json.tools.allow` **DEBE** ser exactamente el conjunto de nombres declarados en `TOOLS.md`.

`config.json.runtime_capabilities` declara permisos crudos del runtime y **NO DEBE** contaminar la interfaz semantica.

## 6. Security y runtime envelope

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
3. Discovery de Skills, degenerados o extendidos, **DEBE** filtrarse por security.

Traces to: formal/01 §1.3 (M-Immutability) ; formal/04 §2.4 (Filtered Discovery)

## 7. Skills

Todo `CM-*` referenciado en `AGENTS.md` **DEBE** resolverse en `skills/` como:

1. Skill degenerado: `skills/CM-*.md`, o
2. Skill extendido: `skills/CM-*/SKILL.md`

conforme a `skill-spec-md`.

El bootstrap del agente **NO DEBE** contener CM inline.

Los directorios adjuntos de un Skill extendido permanecen dentro de la fibra `skills/` y **NO** constituyen un sexto componente del workspace.

## 8. Wiring

Toda ruta a otro agente **DEBE** apuntar a un workspace resoluble. Las rutas logicas no resolubles son invalidas.

Reglas:

1. Toda composicion inter-agente **DEBE** declararse en `AGENTS.md`; el wiring implicito es invalido.
2. El sub-agente **PUEDE** heredar behavior e interface solo en la medida declarada por el wiring.
3. `SOUL.md` y `USER.md` **DEBEN** disiparse en sub-agentes salvo que una spec superior declare explicitamente otra cosa.
4. El sistema compuesto **DEBE** ser razonable desde agentes + rutas declaradas, no desde side effects ocultos.
5. En composiciones multi-agente (swarms), el wiring del swarm se materializa en el `AGENTS.md` del orquestador. `swarm-spec-md` gobierna la coordinacion; esta spec gobierna la topologia de cada agente participante.

Traces to: formal/01 §2.3 (Dissipation) ; formal/01 §6.2 (Sub-Agent Adjunction) ; formal/01 §6.3 (Compositionality of Wiring)

## 9. Validacion

| Check                     | Criterio                                                                            | Enforcement | Accion si falla                          |
| ------------------------- | ----------------------------------------------------------------------------------- | ----------- | ---------------------------------------- |
| Gramatica de behavior     | `AGENTS.md` contiene FSM, Reglas Duras, Co-induccion, Contexto Multi-turno y Wiring | lint        | Normalizar bootstrap                     |
| FSM canonica              | Estados `S-*`, transiciones explicitas, `S-DISPATCHER` y `S-END` presentes          | lint        | Reescribir FSM                           |
| Topologia workspace       | Existen los 5 componentes base                                                      | lint        | Crear faltantes                          |
| Segregacion               | Ningun componente invade el rol de otro                                             | manual      | Reescribir componente                    |
| Behavior puro             | La FSM no mezcla fenomenologia ni security                                          | lint        | Extraer contenido al componente correcto |
| Interfaz cerrada          | `TOOLS.md` = `config.json.tools.allow`                                              | lint        | Alinear interfaz                         |
| Runtime segregado         | Permisos crudos viven en `runtime_capabilities`                                     | lint        | Mover permisos                           |
| Skills resolubles         | Todo `CM-*` referido resuelve a `skills/CM-*.md` o `skills/CM-*/SKILL.md`          | lint        | Crear o corregir skill                   |
| Discovery filtrado        | Security puede excluir skills incompatibles                                         | runtime     | Ajustar policy                           |
| Co-induccion terminal     | Existe verificacion terminal antes del output final                                 | manual      | Declarar o reforzar protocolo terminal   |
| Skill no relaja bootstrap | Ningun CM redefine, relaja o condiciona reglas duras de `AGENTS.md`                 | manual      | Mover regla al bootstrap o spec          |
| Bundle no relaja bootstrap | Ningun `SKILL.md` ni bundle extendido relaja reglas duras, interfaz o envelope     | manual      | Corregir bundle o mover regla            |
| Routing resoluble         | Toda ruta inter-agente existe                                                       | lint        | Corregir o crear destino                 |
