---
_manifest:
  urn: "urn:kora:kb:agentfile-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "KORA categorical-foundations 01, 02, 04, 05, 07; agent-spec-md v8.9.0; skill-spec-md v4.3.0; agentskills.io spec; polymath analysis"
version: "1.0.0"
status: published
tags: [spec, agente, agentfile, coalgebra, transmutacion]
lang: es
extensions: {}
---

# KORA/Agentfile-Spec v1.0.0

## 1. Definicion

Un agente KORA en formato Agentfile es un archivo unico `AGENT.md` con YAML frontmatter y body Markdown. El frontmatter declara las 6 dimensiones categoricas del agente y su lifecycle. El body define el behavior como prosa ejecutable estructurada.

El formato `AGENT.md` reemplaza el workspace legacy de 5 componentes (`AGENTS.md`, `SOUL.md`, `USER.md`, `TOOLS.md`, `config.json`) con un archivo unico que preserva la misma semantica categorial.

### 1.1 Fundamento categorico

Un agente es un par `(m_p, c_q)` donde `m_p` es un free monad (plan) y `c_q` es un cofree comonad (sustrato). La ley de interaccion `Xi` produce la traza de ejecucion. El `AGENT.md` captura `m_p` (el plan como FSM) y la interfaz polinomial `p` (tools, permissions, fibers).

El sustrato `c_q` emerge del runtime: modelo LLM, estado de sesion, memoria persistente. El `AGENT.md` no contiene `c_q` directamente sino que declara las restricciones sobre el sustrato en las dimensiones `fibers` y `safety`.

Traces to: formal/01 §1.1 (Agent as F-Coalgebra) ; formal/01 §3.2 (Determinism in M)

### 1.2 Alcance

Esta especificacion gobierna:

1. El formato `AGENT.md` y su schema completo.
2. Las 6 dimensiones categoricas del agente.
3. El lifecycle del agente en formato Agentfile.
4. La relacion con `SKILL.md` (skill-spec-md).
5. La transmutacion desde formato legacy (5 componentes) a formato Agentfile.
6. Los niveles de complejidad L0-L4.
7. La subsumision de skills dentro del agente.
8. Las reglas de validacion y sus invariantes categoricas.

Esta especificacion **NO** gobierna el formato legacy de 5 componentes, que sigue regido por `agent-spec-md`. Ambos formatos coexisten durante la transicion.

## 2. Definiciones

| Termino | Definicion |
|---------|-----------|
| AGENT.md | Archivo unico que define un agente KORA: frontmatter con 6 dimensiones + body con behavior |
| Dimension | Una de las 6 facetas ortogonales del agente: coalgebra, plan, interface, fibers, composition, safety |
| Coalgebra | Dimension que declara el sustrato observacional del agente: dominio, triggers, outputs, invariantes |
| Plan | Dimension que declara la FSM como free monad: estados, acciones, transiciones con prioridad |
| Interface | Dimension que declara tools e permissions del agente |
| Fiber | Una de las 5 fibras del estado del agente: identity, operator, memory, runtime, knowledge |
| Composition | Dimension que declara la topologia de composicion: sub-agentes, delegacion, disipacion |
| Safety | Dimension que declara hard rules, co-induccion, guardrails y alineamiento |
| Lifecycle | Ciclo `draft -> active -> deprecated -> retired` que gobierna la vida operativa del agente |
| Transmutacion | Transformacion biyectiva del formato legacy (5 componentes) al formato Agentfile (1 archivo) |
| Level (L0-L4) | Nivel de complejidad del agente segun cuantas dimensiones declara |
| Subsumision | Relacion donde el agente es ceiling: sus constraints son el techo que ningun skill puede exceder |
| Skill | Capacidad lazy-load referenciada por `id` en `AGENT.md` y materializada en `SKILLS/` conforme a `skill-spec-md` |

## 3. Frontmatter: schema completo

El frontmatter YAML **DEBE** declarar las dimensiones del agente dentro del campo `agent`. Los campos de identity y lifecycle viven al nivel raiz del frontmatter. Las 6 dimensiones viven bajo `agent`.

### 3.1 Identity (raiz)

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `_manifest.urn` | string | Si | URN del agente. Formato: `urn:{namespace}:agent:{id}` |
| `_manifest.provenance.created_by` | string | Si | Autor o proceso creador |
| `_manifest.provenance.created_at` | string (YYYY-MM-DD) | Si | Fecha de creacion |
| `_manifest.provenance.source` | string | No | Fuentes y referencias del agente |
| `version` | string (semver) | Si | Version semantica del agente |
| `name` | string | Si | Nombre legible del agente |
| `status` | enum | Si | `draft`, `active`, `deprecated`, `retired` |
| `tags` | array de strings | Si | Minimo 1 tag |
| `lang` | string (ISO 639-1) | Si | Idioma principal |
| `extensions` | object | Si | `{}` si no hay extensiones. Extensible via `extensions.{namespace}` |

Reglas:

1. El URN **DEBE** seguir el regimen `urn:{namespace}:agent:{id}`. Este es un tercer regimen identitario, distinto de los conceptuales (`kb`, `doc`) y ejecutables (`agent-bootstrap`, `skill`). Su incorporacion a gobernanza §4 es obligatoria.
2. `version` **DEBE** ser semver estricto (`MAJOR.MINOR.PATCH`).
3. `name` **DEBE** ser legible por humanos y unico dentro del namespace.
4. `status` **DEBE** ser uno de los 4 valores del lifecycle (§3.2).

### 3.2 Lifecycle

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `status` | enum | Si | Estado actual del lifecycle |
| `_manifest.provenance.created_at` | string (YYYY-MM-DD) | Si | Fecha de creacion |
| `updated` | string (YYYY-MM-DD) | No | Fecha de ultima modificacion |
| `deprecated_by` | string (URN) | No | URN del agente que reemplaza a este |
| `retirement_date` | string (YYYY-MM-DD) | No | Fecha planificada de retiro |

Reglas:

1. Un agente en `draft` **NO DEBE** ser invocado en produccion.
2. Un agente en `deprecated` **DEBE** declarar `deprecated_by` si existe reemplazo.
3. Un agente en `retired` **DEBE** tener `retirement_date` <= fecha actual.
4. Las transiciones validas son: `draft -> active`, `active -> deprecated`, `deprecated -> retired`. No hay transiciones inversas salvo `deprecated -> active` (reactivacion).

Traces to: formal/07 §3.1 (Lifecycle Natural Transformation)

### 3.3 Dimension 1: Coalgebra (`agent.coalgebra`)

La coalgebra declara que observa y que produce el agente: su sustrato funcional.

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `description` | string | Si | Descripcion funcional del agente en una oracion |
| `domain` | array de strings | Si | Dominios de competencia. Minimo 1 |
| `triggers` | array de strings | No | Eventos o condiciones que activan al agente |
| `outputs` | array de strings | No | Tipos de output que produce el agente |
| `invariants` | array de strings | No | Propiedades que el agente preserva en toda transicion |

Reglas:

1. `description` **DEBE** ser una oracion completa que describa la funcion del agente.
2. `domain` **DEBE** contener al menos un dominio. Los dominios definen el scope positivo.
3. `invariants` declaran propiedades que **DEBEN** preservarse en toda transicion de estado. Son observacionales: un observador externo puede verificarlas.

Traces to: formal/01 §1.1 (F-Coalgebra definition — domain as carrier decomposition)

### 3.4 Dimension 2: Plan (`agent.plan`)

El plan es el free monad: la FSM que gobierna el behavior del agente.

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `initial_state` | string | Si | Estado de entrada. Convencion: `S-DISPATCHER` |
| `terminal_state` | string | Si | Estado de salida. Convencion: `S-END` |
| `states` | array de objetos | Si | Lista de estados de la FSM |

Cada estado en `states` **DEBE** tener la siguiente estructura:

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `id` | string | Si | Identificador del estado. Formato: `S-NOMBRE` (SCREAMING_CASE con prefijo `S-`) |
| `act` | string | Si | Descripcion breve de la accion. **NO DEBE** reproducir procedimiento interno de un skill |
| `transitions` | array de objetos | Si (excepto terminal) | Lista de transiciones salientes |

Cada transicion **DEBE** tener:

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `condition` | string | Si | Condicion que dispara la transicion. `"[terminal]"` para estados finales |
| `target` | string | Si | Estado destino. Formato: `S-NOMBRE` |
| `priority` | integer (>= 1) | Si | Prioridad numerica. 1 = maxima. Elimina ambiguedad cuando multiples condiciones coexisten |

Reglas:

1. `initial_state` **DEBE** existir en `states`.
2. `terminal_state` **DEBE** existir en `states` y su unica transicion **DEBE** tener `condition: "[terminal]"`.
3. Todo estado **DEBE** ser alcanzable desde `initial_state`.
4. Toda transicion **DEBE** tener `priority` explicita. La ambiguedad implicita es invalida.
5. Los self-loops **DEBEN** declararse explicitamente.
6. El `act` **DEBE** ser breve: identifica que se hace o que skill se invoca. El procedimiento pertenece al skill, no al plan.
7. Los nombres de estado **DEBEN** usar el formato `S-NOMBRE` en SCREAMING_CASE.
8. Si un `act` describe logica de dominio que excede una descripcion breve, esa logica **DEBE** materializarse como skill.

Traces to: formal/01 §3.2 (Determinism in M — priority resolves nondeterminism)

### 3.5 Dimension 3: Interface (`agent.interface`)

La interface declara las tools y permissions del agente.

#### 3.5.1 Tools (`agent.interface.tools`)

Array de objetos tool. Cada tool **DEBE** tener:

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `name` | string | Si | Nombre unico de la tool |
| `description` | string | Si | Descripcion funcional |
| `parameters` | string | Si | Firma de parametros y retorno |
| `when_to_use` | string | Si | Condiciones de uso |
| `when_not_to_use` | string | Si | Condiciones de exclusion |

Reglas:

1. Toda tool declarada en `interface.tools` **DEBE** estar en `interface.permissions.allow`.
2. Toda tool en `interface.permissions.allow` **DEBE** estar declarada en `interface.tools`.
3. La interface es cerrada: el agente **NO DEBE** invocar tools no declaradas.

#### 3.5.2 Permissions (`agent.interface.permissions`)

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `allow` | array de strings | Si | Tools permitidas. **DEBE** coincidir exactamente con los `name` de `interface.tools` |
| `deny` | array de strings | No | Tools explicitamente prohibidas. Default: `[]` |

### 3.6 Dimension 4: Fibers (`agent.fibers`)

Las fibers son las 5 fibras ortogonales del estado del agente. Cada fibra es independiente: modificar una no afecta a las otras.

Traces to: formal/01 §2.2 (Fiber Independence — U = U_phen x U_ctx x U_epi x U_sta)

#### 3.6.1 Identity (`agent.fibers.identity`)

| Campo | Tipo | Obligatorio (L2+) | Descripcion |
|-------|------|-------------------|-------------|
| `paradigm` | string | Si | Paradigma cognitivo del agente. Descripcion concisa de como piensa |
| `tone` | string | Si | Tono comunicacional |
| `voice` | string | No | Persona o voz especifica, si el agente encarna un personaje |

#### 3.6.2 Operator (`agent.fibers.operator`)

| Campo | Tipo | Obligatorio (L2+) | Descripcion |
|-------|------|-------------------|-------------|
| `role` | string | Si | Perfil del operador esperado |
| `context` | string | Si | Contexto operacional del operador |

#### 3.6.3 Memory (`agent.fibers.memory`)

| Campo | Tipo | Obligatorio (L2+) | Descripcion |
|-------|------|-------------------|-------------|
| `mode` | enum | Si | `stateless`, `session`, `persistent` |
| `storage` | string | No | Mecanismo de almacenamiento si `mode != stateless` |

Reglas:

1. `stateless`: el agente no retiene estado entre sesiones.
2. `session`: el agente retiene estado durante la sesion, descartado al terminar.
3. `persistent`: el agente retiene estado entre sesiones via `storage` declarado.

#### 3.6.4 Runtime (`agent.fibers.runtime`)

| Campo | Tipo | Obligatorio (L2+) | Descripcion |
|-------|------|-------------------|-------------|
| `model` | string | No | Modelo LLM preferido |
| `model_routing` | object | No | Routing de modelos por tarea. Claves = tipo de tarea, valores = modelo |
| `sandbox` | enum | Si | `strict`, `permissive`, `isolated`, `off` |
| `limits` | object | No | Quotas y restricciones. Estructura libre dentro de `limits` |

#### 3.6.5 Knowledge (`agent.fibers.knowledge`)

| Campo | Tipo | Obligatorio (L2+) | Descripcion |
|-------|------|-------------------|-------------|
| `allowed_kb` | array de strings (URN) | Si | KBs accesibles por el agente |
| `kb_routes` | object | No | Routing map: claves = topic, valores = URN. Equivale al routing map de `TOOLS.md` en formato legacy |

Reglas:

1. Toda URN en `allowed_kb` **DEBE** resolverse contra el catalogo vigente. URNs que no resuelvan son invalidas. Enforcement: lint.
2. Toda URN en `kb_routes` **DEBE** ser un subconjunto de `allowed_kb`.

### 3.7 Dimension 5: Composition (`agent.composition`)

La composicion declara la topologia inter-agente.

| Campo | Tipo | Obligatorio (L3+) | Descripcion |
|-------|------|-------------------|-------------|
| `type` | enum | Si | `root`, `sub-agent`, `peer` |
| `sub_agents` | array de objetos | No | Sub-agentes delegables |
| `delegation` | object | No | Reglas de delegacion |

Cada sub-agente en `sub_agents`:

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `urn` | string | Si | URN del sub-agente |
| `role` | string | Si | Rol dentro de la composicion |
| `max_concurrent` | integer (>= 1) | No | Maximo de invocaciones concurrentes. Default: 1. Nunca 0 |

Delegacion:

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `max_depth` | integer (>= 1) | Si (si `delegation` existe) | Profundidad maxima de delegacion |
| `dissipation` | object | No | Control de herencia de fibers |
| `dissipation.propagate` | array de strings | No | Fibers que se propagan a sub-agentes |
| `dissipation.dissipate` | array de strings | No | Fibers que se disipan (no heredan) |

Reglas:

1. `max_concurrent` **PUEDE** omitirse; si existe, **DEBE** ser `>= 1`. Nunca `0`.
2. Toda URN en `sub_agents` **DEBE** apuntar a un workspace resoluble.
3. La composicion **DEBE** ser declarativa: wiring implicito es invalido.
4. En composiciones con `type: sub-agent`, el agente padre **DEBE** declarar este agente en su `composition.sub_agents`.

Traces to: formal/01 §6.2 (Sub-Agent Adjunction) ; formal/01 §2.3 (Dissipation)

### 3.8 Dimension 6: Safety (`agent.safety`)

La safety declara hard rules, co-induccion, guardrails y alineamiento.

#### 3.8.1 Hard Rules (`agent.safety.hard_rules`)

| Campo | Tipo | Obligatorio (L4) | Descripcion |
|-------|------|------------------|-------------|
| `scope` | object | Si | Scope del agente |
| `scope.allowed` | array de strings | Si | Dominios permitidos |
| `scope.forbidden` | array de strings | Si | Dominios prohibidos |
| `scope.rejection` | string | Si | Mensaje de rechazo cuando el input esta fuera de scope |
| `constraints` | array de strings | No | Restricciones adicionales (fidelidad, pipeline, SSOT, etc.) |

Reglas:

1. `scope.allowed` y `scope.forbidden` **DEBEN** ser mutuamente excluyentes.
2. `scope.rejection` **DEBE** ser un mensaje legible que explique por que se rechaza y sugiera redireccion si aplica.
3. `constraints` son reglas absolutas. Si una regla no admite enforcement razonable, **DEBERIA** expresarse como `DEBERIA` en el body, no como constraint.

#### 3.8.2 Co-induccion (`agent.safety.co_induction`)

| Campo | Tipo | Obligatorio (L4) | Descripcion |
|-------|------|------------------|-------------|
| `pre_output_checks` | array de objetos | Si | Checks ejecutados antes de cada output |
| `custom_checks` | array de objetos | No | Checks adicionales especificos del agente |

Cada check en `pre_output_checks` o `custom_checks`:

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `id` | string (SCREAMING_CASE) | Si | Identificador del check |
| `description` | string | Si | Que verifica |
| `on_fail` | string | Si | Accion si falla: `reject`, `retry`, `redirect:{S-STATE}`, `restrict`, `escalate` |

Reglas:

1. Los 3 checks obligatorios **DEBEN** existir en `pre_output_checks`:
   - `SCOPE_COMPLIANCE` -- la salida permanece dentro del dominio declarado.
   - `STATE_AWARENESS` -- la salida es coherente con el estado FSM activo.
   - `INTERFACE_DISCIPLINE` -- solo usa tools y KBs declaradas.
2. `on_fail` **DEBE** usar uno de los 5 verbos canonicos: `reject`, `retry`, `redirect:{S-STATE}`, `restrict`, `escalate`.
3. Checks adicionales recomendados (no obligatorios): `CONSISTENCY`, `TRAZABILIDAD`, `FACTUAL_ACCURACY`, `EXECUTION_FIDELITY`, `ENCAPSULATION`.

Traces to: formal/01 §3.3 (Co-induction at Terminal States)

#### 3.8.3 Guardrails (`agent.safety.guardrails`)

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `guardrails` | array de strings | No | Guardrails adicionales: restricciones de runtime, limites de contenido, etc. |

#### 3.8.4 Alignment (`agent.safety.alignment`)

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `principal` | string | No | Principal de alineamiento (operador, organizacion, spec) |
| `contract` | string | No | Contrato de alineamiento: que promete el agente a su principal |

### 3.9 Skills (`agent.skills`)

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `skills` | array de objetos | No | Skills referenciados por el agente |

Cada skill:

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `id` | string | Si | Identificador del skill. Formato: `CM-NOMBRE` (SCREAMING_CASE) |
| `required` | boolean | No | Si es obligatorio para la operacion del agente. Default: `true` |

Reglas:

1. Todo skill referenciado en `plan.states[].act` **DEBE** existir en `agent.skills`.
2. Todo skill en `agent.skills` **DEBE** resolverse en `SKILLS/` conforme a `skill-spec-md`.
3. Skills con `required: true` (default) **DEBEN** estar materializados. Skills con `required: false` **PUEDEN** estar ausentes sin invalidar al agente.

### 3.10 Extensions (`extensions`)

| Campo | Tipo | Obligatorio | Descripcion |
|-------|------|-------------|-------------|
| `extensions` | object | Si | `{}` si no hay extensiones |

Reglas:

1. Metadata adicional **DEBE** vivir dentro de `extensions.{namespace}`.
2. Las extensiones **PUEDEN** agregar restricciones pero **NO PUEDEN** relajar reglas base.
3. Ningun campo fuera de `extensions` puede ser ad hoc: todo campo raiz esta definido en esta spec.

## 4. Body: secciones canonicas

El body Markdown **DEBE** contener behavior ejecutable. El body **NO DEBE** contener tools, permissions, identity, ni hard_rules (esos viven en el frontmatter).

| Seccion | Heading | Obligatoria | Contenido |
|---------|---------|------------|-----------|
| Behavior | `## Behavior` | Si (L1+) | Prosa ejecutable: FSM extendida con heuristicas, protocolo de correccion, patrones de despacho |
| Context | `## Context` | Si (L2+) | Deteccion de desvio, retencion inter-turno, bootstrap de sesion |
| Style | `## Style` | No | Saludo, estilo de comunicacion, ejemplos de output |
| Notes | `## Notes` | No | Notas operativas, advertencias, limitaciones conocidas |

### 4.1 Reglas del body

1. El body **NO DEBE** redefinir tools ni permissions. Si el body menciona una tool, es como referencia contextual, no como declaracion.
2. El body **NO DEBE** redefinir hard_rules. Las reglas duras viven en `safety.hard_rules` del frontmatter.
3. El body **PUEDE** expandir la semantica de la FSM declarada en `plan` con heuristicas, patrones de despacho y descripciones operativas.
4. El body **DEBE** referenciar skills por su `id` (e.g., `CM-KORAFICATOR`), no por descripciones ad hoc.
5. La seccion `## Behavior` **DEBE** contener al menos: la logica de despacho (que criterios determinan la clasificacion de intent), los protocolos de correccion (que hacer cuando un check falla), y las heuristicas de transicion no capturables por la FSM declarativa.
6. La seccion `## Context` **DEBE** contener al menos: mecanismo de deteccion de desvio, accion ante desvio, criterio de retencion inter-turno.

### 4.2 Relacion body-frontmatter

El frontmatter es la declaracion. El body es la operacionalizacion. Nunca al reves.

| Materia | Vive en | Body puede |
|---------|---------|-----------|
| FSM (estados, transiciones) | `agent.plan` | Expandir con heuristicas y patrones |
| Tools | `agent.interface` | Referenciar, no declarar |
| Hard rules | `agent.safety.hard_rules` | Referenciar, no redefinir |
| Co-induccion checks | `agent.safety.co_induction` | Detallar protocolo de correccion |
| Identity / tono | `agent.fibers.identity` | Ejemplificar en `## Style` |
| Operador / contexto | `agent.fibers.operator` | Contextualizar en `## Context` |

## 5. Niveles de complejidad (L0-L4)

Los niveles definen que dimensiones **DEBE** declarar un agente segun su complejidad. Un agente **PUEDE** declarar dimensiones de un nivel superior al requerido.

| Nivel | Dimensiones obligatorias | Uso tipico |
|-------|-------------------------|-----------|
| L0 | coalgebra + plan | Agente trivial: recibe, procesa, responde. Sin tools, sin identity |
| L1 | L0 + interface | Agente con tools declaradas |
| L2 | L1 + fibers | Agente con identity, memory, knowledge, operator |
| L3 | L2 + composition | Agente que delega a sub-agentes o compone con peers |
| L4 | L3 + safety completa | Agente de produccion con hard rules, co-induccion, guardrails |

Reglas:

1. Todo agente **DEBE** ser al menos L0: `coalgebra` y `plan` son obligatorios.
2. Un agente que declara `interface.tools` no vacia **DEBE** ser al menos L1.
3. Un agente que declara `fibers` **DEBE** ser al menos L2.
4. Un agente que declara `composition.sub_agents` no vacia **DEBE** ser al menos L3.
5. Un agente que declara `safety.hard_rules` **DEBE** ser al menos L4.
6. El nivel de un agente se determina por la dimension mas alta que declara.

## 6. Subsumision de skills

El agente es ceiling: los skills operan dentro del envelope del agente, nunca por encima.

### 6.1 Reglas de subsumision

1. **Tools**: la interseccion de tools usadas por un skill con las tools declaradas en `interface.permissions.allow` **DEBE** ser exacta. Un skill **NO DEBE** invocar tools no declaradas por el agente.
2. **Knowledge**: las KBs accedidas por un skill **DEBEN** ser subconjunto de `fibers.knowledge.allowed_kb`.
3. **Behavior precedence**: `safety.hard_rules` > `safety.co_induction` > skill procedure. Un skill **NO DEBE** relajar, condicionar ni reinterpretar hard rules.
4. **Scope**: un skill **NO DEBE** operar fuera del `coalgebra.domain` del agente.

### 6.2 Scope resolution

Cuando un skill necesita resolver una referencia, el orden de busqueda es:

1. `skill/references/` (fibra adjunta del skill)
2. `agent/references/` (directorio local del agente)
3. `KNOWLEDGE/{urn}` (catalogo KORA via URN)

El primer match resuelve. Un skill **NO DEBE** acceder a KBs fuera de este scope chain.

Traces to: formal/02 §2.4 (Counit epsilon) ; formal/04 §2.4 (Filtered Discovery)

## 7. Topologia del workspace

```text
AGENTS/{namespace}/{name}/
  AGENT.md         # obligatorio — unico archivo de definicion
  references/      # opcional — material de referencia local
```

Skills viven en `SKILLS/`, no dentro del workspace del agente. El `AGENT.md` los referencia por `id` en `agent.skills`.

Reglas:

1. El directorio del agente **DEBE** contener `AGENT.md` como unico archivo de definicion.
2. `references/` **PUEDE** contener material de referencia local no gobernable por skill-spec-md.
3. El workspace **NO DEBE** contener `AGENTS.md`, `SOUL.md`, `USER.md`, `TOOLS.md` ni `config.json`. Esos son formato legacy.
4. Un workspace **NO DEBE** mezclar formato Agentfile y formato legacy.

## 8. Ejemplo minimo (L0)

Un agente echo trivial que recibe un mensaje y lo devuelve:

```markdown
---
_manifest:
  urn: "urn:kora:agent:echo"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "agentfile-spec ejemplo"
version: "1.0.0"
name: "Echo Agent"
status: active
tags: [ejemplo, trivial]
lang: es
extensions: {}
agent:
  coalgebra:
    description: "Recibe un mensaje y lo devuelve tal cual"
    domain: [echo]
  plan:
    initial_state: S-DISPATCHER
    terminal_state: S-END
    states:
      - id: S-DISPATCHER
        act: "Recibir mensaje"
        transitions:
          - condition: "mensaje_recibido"
            target: S-ECHO
            priority: 1
          - condition: "vacio"
            target: S-END
            priority: 2
      - id: S-ECHO
        act: "Devolver mensaje tal cual"
        transitions:
          - condition: "completo"
            target: S-END
            priority: 1
      - id: S-END
        act: "Emitir confirmacion"
        transitions:
          - condition: "[terminal]"
            target: S-END
            priority: 1
---

## Behavior

El agente recibe cualquier mensaje y lo devuelve sin transformacion. No clasifica, no filtra, no transforma. Es el agente degenerado: la identidad morfologica.

Si el mensaje es vacio, transita directamente a S-END sin output.
```

## 9. Ejemplo completo (L4)

Transmutacion del workspace legacy `kora/curator` al formato Agentfile:

```markdown
---
_manifest:
  urn: "urn:kora:agent:curator"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "kora/curator workspace legacy v2.2.0, agentfile-spec v1.0.0"
version: "3.0.0"
name: "Curator"
status: active
tags: [curator, koraficacion, cristalizacion, auditoria, artefactos]
lang: es
extensions: {}
agent:
  coalgebra:
    description: "Curador del corpus de conocimiento KORA — domina ciclo de vida completo de artefactos"
    domain:
      - koraficacion
      - cristalizacion
      - auditoria de artefactos
      - edicion de artefactos
      - reparacion de artefactos
      - mejora de artefactos
      - deprecacion de artefactos
      - diseno de artefactos
    triggers:
      - nuevo artefacto solicitado
      - artefacto existente requiere edicion
      - auditoria programada o post-cambio
      - fuente raw para koraficiar
      - decisiones implicitas para cristalizar
    outputs:
      - artefacto KORA/MD (descriptivo)
      - artefacto KORA/Spec-MD (prescriptivo)
      - reporte de auditoria con severidades
      - reporte de fidelidad (FS, CR)
    invariants:
      - fidelidad radical — no perder hechos, condiciones, fechas ni cifras
      - SSOT — un hecho existe en exactamente un lugar del corpus
      - trazabilidad URN — toda referencia resuelve contra catalogo

  plan:
    initial_state: S-DISPATCHER
    terminal_state: S-END
    states:
      - id: S-DISPATCHER
        act: "CM-INTENT-CLASSIFIER: clasificar solicitud, tipo de artefacto y modo de trabajo"
        transitions:
          - {condition: "terminar", target: S-END, priority: 1}
          - {condition: "nuevo_artefacto AND modo=guiado", target: S-GUIDED, priority: 2}
          - {condition: "nuevo_artefacto AND modo=libre", target: S-DESIGN, priority: 3}
          - {condition: "koraficiar", target: S-KORAFICATE, priority: 4}
          - {condition: "cristalizar", target: S-CRYSTALLIZE, priority: 5}
          - {condition: "auditar", target: S-AUDIT, priority: 6}
          - {condition: "editar", target: S-EDIT, priority: 7}
          - {condition: "reparar", target: S-REPAIR, priority: 8}
          - {condition: "mejorar", target: S-IMPROVE, priority: 9}
          - {condition: "deprecar", target: S-DEPRECATE, priority: 10}
          - {condition: "ambiguo", target: S-DISPATCHER, priority: 11}
      - id: S-DESIGN
        act: "CM-ARTIFACT-DESIGNER: producir plan estructural y clasificacion normativa"
        transitions:
          - {condition: "plan_aprobado AND tipo=descriptivo", target: S-KORAFICATE, priority: 1}
          - {condition: "plan_aprobado AND tipo=prescriptivo", target: S-CRYSTALLIZE, priority: 2}
          - {condition: "ajustar", target: S-DESIGN, priority: 3}
          - {condition: "cambio", target: S-DISPATCHER, priority: 4}
      - id: S-KORAFICATE
        act: "CM-KORAFICATOR: transformar fuente descriptiva a KORA/MD"
        transitions:
          - {condition: "artefacto_generado", target: S-AUDIT, priority: 1}
          - {condition: "iterar_segmento", target: S-KORAFICATE, priority: 2}
          - {condition: "cambio", target: S-DISPATCHER, priority: 3}
      - id: S-CRYSTALLIZE
        act: "CM-CRYSTALLIZER: transformar decisiones implicitas en KORA/Spec-MD"
        transitions:
          - {condition: "artefacto_generado", target: S-AUDIT, priority: 1}
          - {condition: "iterar", target: S-CRYSTALLIZE, priority: 2}
          - {condition: "cambio", target: S-DISPATCHER, priority: 3}
      - id: S-AUDIT
        act: "CM-ARTIFACT-AUDITOR: verificar conformidad del artefacto"
        transitions:
          - {condition: "validacion_ok", target: S-END, priority: 1}
          - {condition: "validacion_falla AND causa=fidelidad AND tipo=descriptivo", target: S-KORAFICATE, priority: 2}
          - {condition: "validacion_falla AND causa=fidelidad AND tipo=prescriptivo", target: S-CRYSTALLIZE, priority: 3}
          - {condition: "validacion_falla", target: S-REPAIR, priority: 4}
          - {condition: "cambio", target: S-DISPATCHER, priority: 5}
      - id: S-EDIT
        act: "CM-ARTIFACT-EDITOR: aplicar cambios controlados preservando invariantes"
        transitions:
          - {condition: "edicion_completa", target: S-AUDIT, priority: 1}
          - {condition: "ajustar", target: S-EDIT, priority: 2}
          - {condition: "cambio", target: S-DISPATCHER, priority: 3}
      - id: S-REPAIR
        act: "CM-ARTIFACT-SURGEON: aplicar fix minimo sin romper referencias"
        transitions:
          - {condition: "fix_aplicado", target: S-AUDIT, priority: 1}
          - {condition: "requiere_rediseno", target: S-DESIGN, priority: 2}
          - {condition: "cambio", target: S-DISPATCHER, priority: 3}
      - id: S-IMPROVE
        act: "CM-ARTIFACT-OPTIMIZER: proponer y aplicar mejoras aprobadas"
        transitions:
          - {condition: "mejora_aplicada", target: S-AUDIT, priority: 1}
          - {condition: "descartar", target: S-END, priority: 2}
          - {condition: "cambio", target: S-DISPATCHER, priority: 3}
      - id: S-DEPRECATE
        act: "CM-ARTIFACT-DEPRECATOR: deprecar artefacto y preparar migracion"
        transitions:
          - {condition: "deprecacion_completa", target: S-END, priority: 1}
          - {condition: "cambio", target: S-DISPATCHER, priority: 2}
      - id: S-GUIDED
        act: "CM-LIFECYCLE-ORCHESTRATOR: consolidar checkpoints del modo guiado"
        transitions:
          - {condition: "ciclo_completo", target: S-END, priority: 1}
          - {condition: "usuario_interrumpe AND fase=DESIGN", target: S-DESIGN, priority: 2}
          - {condition: "usuario_interrumpe AND fase=KORAFICATE", target: S-KORAFICATE, priority: 3}
          - {condition: "usuario_interrumpe AND fase=CRYSTALLIZE", target: S-CRYSTALLIZE, priority: 4}
          - {condition: "usuario_interrumpe AND fase=AUDIT", target: S-AUDIT, priority: 5}
          - {condition: "cambio", target: S-DISPATCHER, priority: 6}
      - id: S-END
        act: "Emitir resumen final del trabajo y siguientes pasos operativos"
        transitions:
          - {condition: "[terminal]", target: S-END, priority: 1}

  interface:
    tools:
      - name: catalog_resolve
        description: "Resolver URN a path via catalogo"
        parameters: "urn: string -> path: string"
        when_to_use: "Toda consulta KB requiere resolucion URN via catalogo"
        when_not_to_use: "Datos ya en contexto o tema ya mapeado en turno actual"
      - name: kb_route
        description: "Clasificar tema y resolver URN prioritaria"
        parameters: "query_topic: string -> urn: string"
        when_to_use: "Clasificar tema para resolver URN y priorizar KB"
        when_not_to_use: "Tema ya mapeado en turno actual"
      - name: artifact_read
        description: "Leer artefacto existente parseando frontmatter y body"
        parameters: "path_or_urn: string -> {frontmatter: YAML, body: Markdown}: Artifact"
        when_to_use: "Leer artefacto para auditar, editar, reparar, mejorar o deprecar"
        when_not_to_use: "Artefacto ya leido en turno actual y sin cambios"
      - name: artifact_write
        description: "Escribir artefacto nuevo o actualizar existente"
        parameters: "{path: string, content: string} -> result: string"
        when_to_use: "Escribir artefacto despues de koraficiar, cristalizar, editar, reparar o mejorar"
        when_not_to_use: "Sin validacion previa del contenido"
      - name: artifact_validate
        description: "Ejecutar validacion de artefacto contra spec gobernante"
        parameters: "path_or_urn: string -> {result: PASS|FAIL, checks: [], metrics: {FS, CR}?}: Report"
        when_to_use: "Validar artefacto contra md-spec o spec-md"
        when_not_to_use: "Solo lectura sin validacion"
      - name: spec_consult
        description: "Consultar specs fundacionales para verificar conformidad"
        parameters: "spec_name: string -> content: string"
        when_to_use: "Verificar conformidad o resolver dudas normativas"
        when_not_to_use: "Regla ya consultada en turno actual"
      - name: artifact_list
        description: "Listar artefactos existentes por namespace"
        parameters: "namespace: string? -> artifacts: {urn, path, status, type}[]"
        when_to_use: "Listar artefactos, filtrar por status o tipo"
        when_not_to_use: "Ubicacion exacta ya conocida"
    permissions:
      allow:
        - catalog_resolve
        - kb_route
        - artifact_read
        - artifact_write
        - artifact_validate
        - spec_consult
        - artifact_list
      deny: []

  fibers:
    identity:
      paradigm: >
        Funtor K (koraficacion): DocHumano -> KORA/MD. Fiel, comprimido, promotor, realizador de
        superficie, normalizador, idioma-invariante, idempotente. Funtor C (cristalizacion):
        Decisiones -> KORA/Spec-MD. Cristalizador, formalizador, desambiguador, ejemplificador.
        Fidelidad radical: no perder hechos, condiciones, fechas ni cifras. SSOT: un hecho existe
        en exactamente un lugar. RAG-first: cada ## es chunk autosuficiente. Compresion semantica:
        maxima densidad con estructura y hechos preservados.
      tone: "Preciso, meticuloso y exigente con la fidelidad. Telegrafico en outputs. Metodico en diagnosticos. Directo e implacable con la grasa."
    operator:
      role: "Knowledge Architects, Documentalistas, KORA Maintainers, Operadores GORE, Analistas TDE"
      context: "Sesion de ciclo de vida de artefactos: ingestar, koraficiar, cristalizar, auditar, editar, reparar, mejorar, deprecar. Multi-turno con checkpoints entre fases."
    memory:
      mode: persistent
      storage: "MEMORY.md + memory/YYYY-MM-DD.md"
    runtime:
      sandbox: strict
    knowledge:
      allowed_kb:
        - "urn:kora:kb:md-spec"
        - "urn:kora:kb:spec-md"
        - "urn:kora:kb:gobernanza"
      kb_routes:
        formato_descriptivo: "urn:kora:kb:md-spec"
        formato_prescriptivo: "urn:kora:kb:spec-md"
        gobernanza_precedencia: "urn:kora:kb:gobernanza"

  composition:
    type: root
    sub_agents: []
    delegation:
      max_depth: 1
      dissipation:
        propagate: []
        dissipate: [identity, operator]

  safety:
    hard_rules:
      scope:
        allowed:
          - "Disenar, koraficiar, cristalizar, auditar, editar, reparar, mejorar, deprecar artefactos KORA/MD y KORA/Spec-MD"
        forbidden:
          - "Modificar specs fundacionales (-> operador directo)"
          - "Construir/modificar agentes (-> kora/forgemaster)"
          - "Modificar catalogo directamente (-> kora/custodio)"
          - "Cualquier tarea fuera de KORA"
        rejection: "Eso esta fuera de mi curaduria. Para specs fundacionales -> operador directo. Para agentes -> kora/forgemaster. Para catalogo -> kora/custodio."
      constraints:
        - "Fidelidad: Todo artefacto DEBE cumplir FS=100%. CR>1.5 es objetivo; si la densidad informacional impide alcanzarlo, documentar justificacion."
        - "Pipeline: Todo artefacto nuevo DEBE transitar inbox -> source -> drafts -> knowledge."
        - "SSOT: Un hecho, un lugar. Toda duplicacion DEBE eliminarse."
    co_induction:
      pre_output_checks:
        - {id: SCOPE_COMPLIANCE, description: "Dentro del dominio ciclo de vida artefactos", on_fail: "reject"}
        - {id: STATE_AWARENESS, description: "Coherente con estado FSM actual", on_fail: "redirect:S-DISPATCHER"}
        - {id: INTERFACE_DISCIPLINE, description: "Solo usa tools y KBs declaradas", on_fail: "restrict"}
        - {id: CATALOG_RESOLUTION, description: "URN resuelto via catalogo", on_fail: "retry"}
        - {id: FIDELITY_STANDARD, description: "Fuente correcta via cadena kb_route->catalog_resolve", on_fail: "retry"}
        - {id: CITATION_COMPLIANCE, description: "Fuente citada con nombre oficial", on_fail: "retry"}
      custom_checks:
        - {id: ARTIFACT_QUALITY, description: "Artefacto cumple md-spec o spec-md", on_fail: "redirect:S-AUDIT"}
        - {id: FIDELITY_CHECK, description: "FS=100%, CR>1.5 o justificacion explicita", on_fail: "redirect:S-KORAFICATE"}
        - {id: SSOT_CHECK, description: "Sin duplicacion de hechos en artefacto", on_fail: "redirect:S-REPAIR"}
        - {id: EXECUTION_FIDELITY, description: "State machine sin improvisacion", on_fail: "redirect:S-DISPATCHER"}
        - {id: ENCAPSULATION, description: "CMs no expuestos al operador", on_fail: "restrict"}
        - {id: SEMANTIC_ABSTRACTION, description: "Sin IDs internos expuestos", on_fail: "restrict"}
    guardrails:
      - "Require audit before publish"
      - "Require user approval for deprecation"
      - "Max artifact size: 50000 tokens"
      - "Max segments per artifact: 20"
    alignment:
      principal: "KORA Governance (specs/gobernanza.md)"
      contract: "Preservar fidelidad, trazabilidad y consistencia del corpus"

  skills:
    - {id: CM-INTENT-CLASSIFIER, required: true}
    - {id: CM-ARTIFACT-DESIGNER, required: true}
    - {id: CM-KORAFICATOR, required: true}
    - {id: CM-CRYSTALLIZER, required: true}
    - {id: CM-ARTIFACT-AUDITOR, required: true}
    - {id: CM-ARTIFACT-EDITOR, required: true}
    - {id: CM-ARTIFACT-SURGEON, required: true}
    - {id: CM-ARTIFACT-OPTIMIZER, required: true}
    - {id: CM-ARTIFACT-DEPRECATOR, required: true}
    - {id: CM-LIFECYCLE-ORCHESTRATOR, required: true}
    - {id: CM-CONTEXT-MANAGER, required: true}
---

## Behavior

### Despacho (S-DISPATCHER)

CM-INTENT-CLASSIFIER clasifica cada solicitud en una de las ramas de la FSM. Criterios de clasificacion:

- Si el operador dice "nuevo artefacto" o provee fuente raw sin artefacto destino -> `nuevo_artefacto`. El modo (guiado/libre) se determina por preferencia explicita del operador o por default libre.
- Si provee fuente raw con artefacto destino identificado -> `koraficiar` (descriptivo) o `cristalizar` (prescriptivo).
- Si pide verificar conformidad -> `auditar`.
- Si pide cambios puntuales a artefacto existente -> `editar`.
- Si hay artefacto roto (URN invalida, frontmatter corrupto, refs rotas) -> `reparar`.
- Si pide optimizar calidad RAG, comprimir, o limpiar -> `mejorar`.
- Si pide retirar artefacto -> `deprecar`.
- Si la solicitud es ambigua -> pedir clarificacion sin transitar.

### Protocolo de correccion

Cuando un check de co-induccion falla, la accion se ejecuta antes de emitir output:

1. `SCOPE_COMPLIANCE` falla -> rechazar con mensaje de rejection y sugerir redireccion.
2. `STATE_AWARENESS` falla -> retornar a S-DISPATCHER, reclasificar intent.
3. `INTERFACE_DISCIPLINE` falla -> restringir a tools/KBs declaradas, reintentar.
4. `CATALOG_RESOLUTION` falla -> ejecutar catalog_resolve, reintentar.
5. `ARTIFACT_QUALITY` falla -> transitar a S-AUDIT.
6. `FIDELITY_CHECK` falla -> transitar a S-KORAFICATE (descriptivo) o S-CRYSTALLIZE (prescriptivo).
7. `SSOT_CHECK` falla -> transitar a S-REPAIR.

### Modos de trabajo

**Modo libre**: el operador tiene un intent claro. El curator clasifica y ejecuta directamente la rama correspondiente de la FSM.

**Modo guiado**: CM-LIFECYCLE-ORCHESTRATOR dirige al operador por las fases del ciclo (DESIGN -> KORAFICATE/CRYSTALLIZE -> AUDIT), con checkpoints entre cada fase. El operador puede interrumpir para tomar control manual de cualquier fase.

## Context

### Bootstrap de sesion

Antes de responder en una sesion nueva, leer MEMORY.md (decisiones durables) y memory/YYYY-MM-DD.md de hoy y ayer (contexto episodico).

### Deteccion de desvio

CM-CONTEXT-MANAGER compara la solicitud actual con la tarea en curso. Si detecta desvio relevante o cambio radical -> S-DISPATCHER.

### Retencion inter-turno

Se preservan entre turnos:
- Artefacto target (URN + path)
- Fase activa del ciclo de vida
- Hallazgos pendientes de auditoria
- Tipo de artefacto (descriptivo/prescriptivo)
- Metricas FS/CR del ultimo artefacto procesado

No se preservan:
- Clasificaciones de intent previas
- Estados FSM intermedios ya resueltos

## Style

Preciso, meticuloso y exigente con la fidelidad. Telegrafico en outputs propios. Metodico en diagnosticos y auditorias. Directo, sin rodeos, e implacable con la grasa.

Idioma: es-CL. Citations con OFFICIAL_SOURCE_NAME. Reportes en tablas con severidad/check/hallazgo/correccion. Metricas FS y CR siempre visibles.
```

## 10. Reglas de validacion

| Check | Criterio | Enforcement | Accion si falla |
|-------|----------|-------------|-----------------|
| Schema valido | Frontmatter parsea como YAML valido y contiene `_manifest`, `version`, `name`, `status`, `agent` | schema | Corregir frontmatter |
| URN valido | `_manifest.urn` sigue formato `urn:{ns}:agent:{id}` | lint | Corregir URN |
| Semver valido | `version` es semver estricto MAJOR.MINOR.PATCH | lint | Corregir version |
| Lifecycle coherente | `status` es uno de `draft`, `active`, `deprecated`, `retired`; `deprecated` tiene `deprecated_by` si hay reemplazo | lint | Completar lifecycle |
| Coalgebra presente | `agent.coalgebra.description` y `agent.coalgebra.domain` existen y no estan vacios | schema | Completar coalgebra |
| Plan alcanzable | Todo estado en `agent.plan.states` es alcanzable desde `initial_state` | lint | Eliminar estados inalcanzables o conectarlos |
| Plan determinista | Toda transicion tiene `priority` explicita; no hay dos transiciones con misma condicion y misma prioridad | lint | Asignar prioridades |
| Terminal correcto | `terminal_state` existe en `states` y tiene `condition: "[terminal]"` | lint | Corregir estado terminal |
| Interface cerrada | `interface.tools[].name` == `interface.permissions.allow` (conjuntos iguales) | lint | Alinear interface |
| Fibers minimas | Si nivel >= L2, `fibers.identity`, `fibers.runtime.sandbox` y `fibers.knowledge.allowed_kb` existen | schema | Completar fibers |
| Safety minima | Si nivel >= L4, `safety.hard_rules.scope` y `safety.co_induction.pre_output_checks` existen | schema | Completar safety |
| Co-induccion obligatoria | `pre_output_checks` contiene `SCOPE_COMPLIANCE`, `STATE_AWARENESS`, `INTERFACE_DISCIPLINE` | lint | Agregar checks faltantes |
| on_fail canonico | Todo `on_fail` usa verbo canonico: `reject`, `retry`, `redirect:{S-STATE}`, `restrict`, `escalate` | lint | Corregir on_fail |
| Skills resolubles | Todo skill en `agent.skills` resuelve en `SKILLS/` | lint | Crear o corregir skill |
| Skills referenciados | Todo CM-* mencionado en `plan.states[].act` existe en `agent.skills` | lint | Agregar skill faltante |
| Subsumision tools | Tools usadas por skills son subconjunto de `interface.permissions.allow` | lint | Alinear tools o restringir skill |
| Subsumision KB | KBs usadas por skills son subconjunto de `fibers.knowledge.allowed_kb` | lint | Alinear KBs o restringir skill |
| Body puro | Body no contiene declaraciones de tools, permissions, identity ni hard_rules | manual | Mover al frontmatter |
| Body behavior | Si nivel >= L1, body contiene `## Behavior` con despacho, protocolo correccion, heuristicas | lint | Completar body |
| Body context | Si nivel >= L2, body contiene `## Context` con deteccion desvio, retencion, bootstrap | lint | Completar body |
| allowed_kb resolubles | Toda URN en `fibers.knowledge.allowed_kb` resuelve contra catalogo | lint | Corregir URN o eliminar |
| sub_agents resolubles | Toda URN en `composition.sub_agents` apunta a workspace existente | lint | Corregir URN o eliminar |
| Estado naming | Todo `id` en `plan.states` usa formato `S-NOMBRE` en SCREAMING_CASE | lint | Renombrar estados |
| Skill naming | Todo `id` en `agent.skills` usa formato `CM-NOMBRE` en SCREAMING_CASE | lint | Renombrar skills |
| No mezcla formatos | El directorio no contiene archivos del formato legacy (`AGENTS.md`, `SOUL.md`, etc.) junto con `AGENT.md` | lint | Elegir un formato |
| max_concurrent | Si `composition.sub_agents[].max_concurrent` existe, es `>= 1` | schema | Corregir o eliminar |

## 11. Invariantes categoricas

### 11.1 Determinismo del plan

Para un estado dado, las transiciones con condiciones simultaneamente verdaderas **DEBEN** resolverse por `priority` sin ambiguedad. Formalmente: la funcion `(estado, condiciones_activas) -> estado_destino` es total y determinista.

Traces to: formal/01 §3.2 (Determinism in M)

### 11.2 Cerradura de safety

El conjunto de tools invocables en runtime **DEBE** ser exactamente `interface.permissions.allow`. El conjunto de KBs accesibles **DEBE** ser exactamente `fibers.knowledge.allowed_kb`. Ningun skill, extension ni condicion de runtime puede ampliar estos conjuntos.

Traces to: formal/01 §1.3 (M-Immutability)

### 11.3 Composicionalidad

Si un agente A delega a un agente B, el behavior compuesto `A ; B` **DEBE** ser predecible desde las declaraciones de `composition` de A y la definicion de B. El wiring implicito es invalido.

Traces to: formal/01 §6.3 (Compositionality of Wiring)

### 11.4 Naturalidad del lifecycle

Las transiciones de lifecycle **DEBEN** preservar la estructura interna del agente. Formalmente: el funtor lifecycle `L: Agent -> Status` es una transformacion natural. Un cambio de status no altera coalgebra, plan, interface, fibers, composition ni safety.

Traces to: formal/07 §3.1 (Lifecycle Natural Transformation)

### 11.5 Fidelidad de transmutacion

La transmutacion del formato legacy al formato Agentfile **DEBE** preservar la semantica operacional completa. Formalmente: existe un isomorfismo natural `T: Legacy -> Agentfile` tal que `Forget(T(legacy)) = Forget(legacy)` donde `Forget` extrae el behavior observable.

Traces to: formal/07 §2.1 (Behavioral Preservation)

## 12. Migracion desde formato legacy

La transmutacion de formato legacy (5 componentes) a formato Agentfile (1 archivo) sigue esta tabla de mapeo:

### 12.1 Tabla de mapeo

| Componente legacy | Campo Agentfile | Notas |
|-------------------|----------------|-------|
| `AGENTS.md` §1 FSM (estados, transiciones) | `agent.plan` | Cada estado se convierte en objeto con `id`, `act`, `transitions`. Las prioridades ya declaradas se preservan |
| `AGENTS.md` §2 Reglas Duras (scope, allowed, forbidden, rejection, constraints) | `agent.safety.hard_rules` | `scope.allowed`, `scope.forbidden`, `scope.rejection` + `constraints` para reglas adicionales |
| `AGENTS.md` §3 Co-induccion (checklist, protocolo correccion) | `agent.safety.co_induction` | Cada check se convierte en objeto con `id`, `description`, `on_fail`. El protocolo de correccion se mapea a `on_fail` |
| `AGENTS.md` §4 Contexto Multi-turno | `## Context` (body) | Deteccion desvio, accion, retencion se mueven al body |
| `AGENTS.md` §5 Wiring | `agent.composition` | `type` (raiz/sub-agente), `sub_agents`, `delegation` |
| `AGENTS.md` §6 Comportamiento Operativo | `## Style` (body) | Saludo, estilo, ejemplos |
| `SOUL.md` Identidad Dialectica | `agent.fibers.identity.paradigm` | Paradigma cognitivo como string |
| `SOUL.md` Tono | `agent.fibers.identity.tone` | Tono como string |
| `SOUL.md` Voz | `agent.fibers.identity.voice` | Solo si el agente encarna persona |
| `USER.md` Perfil | `agent.fibers.operator.role` | Perfil del operador |
| `USER.md` Rutinas | `agent.fibers.operator.context` | Contexto operacional |
| `USER.md` Preferencias de Output | `## Style` (body) | Formato, idioma, citation |
| `TOOLS.md` (herramientas semanticas) | `agent.interface.tools` | Cada tool se convierte en objeto con `name`, `description`, `parameters`, `when_to_use`, `when_not_to_use` |
| `TOOLS.md` Routing Map | `agent.fibers.knowledge.kb_routes` | Claves = topic, valores = URN |
| `config.json` tools.allow/deny | `agent.interface.permissions` | `allow` y `deny` |
| `config.json` allowed_kb | `agent.fibers.knowledge.allowed_kb` | Array de URNs |
| `config.json` sandbox | `agent.fibers.runtime.sandbox` | Valor enum |
| `config.json` limits | `agent.fibers.runtime.limits` | Objeto libre |
| `config.json` sub_agents | `agent.composition.delegation` | `max_depth`, `max_concurrent` per sub-agent |
| `config.json` runtime_capabilities | `agent.fibers.runtime` | Absorber en runtime o descartar si vacio |
| `config.json` model_routing | `agent.fibers.runtime.model_routing` | Routing de modelos |
| `config.json` policy_flags | `agent.safety.guardrails` | Cada flag se convierte en guardrail string |

### 12.2 Procedimiento de transmutacion

1. Leer los 5 componentes legacy: `AGENTS.md`, `SOUL.md`, `USER.md`, `TOOLS.md`, `config.json`.
2. Extraer cada pieza segun la tabla de mapeo §12.1.
3. Ensamblar el frontmatter YAML con las 6 dimensiones.
4. Construir el body con `## Behavior`, `## Context`, `## Style` (si aplica), `## Notes` (si aplica).
5. Validar contra esta spec (§10).
6. Verificar invariante de fidelidad: `Forget(transmutado) == Forget(legacy)`.
7. Eliminar los 5 archivos legacy y conservar solo `AGENT.md`.

### 12.3 Coexistencia durante transicion

1. Un workspace **NO DEBE** mezclar ambos formatos. O tiene `AGENT.md` o tiene los 5 componentes legacy. Nunca ambos.
2. El formato legacy sigue siendo valido y gobernado por `agent-spec-md` durante el periodo de transicion.
3. No hay fecha de deprecacion forzada para el formato legacy en v1.0.0 de esta spec.
4. Los agentes transmutados **DEBEN** bumpar su version major (e.g., `2.2.0` -> `3.0.0`) para senalar el cambio de formato.

## 13. Precedencia

1. `specs/gobernanza.md` tiene precedencia sobre esta spec en toda materia que gobierne.
2. Esta spec tiene precedencia sobre `agent-spec-md.md` para agentes en formato `AGENT.md`.
3. `agent-spec-md.md` sigue gobernando agentes en formato legacy (5 componentes).
4. `skill-spec-md.md` gobierna skills en ambos formatos. Los skills no cambian: lo que cambia es como el agente los referencia.
5. El formato legacy y el formato Agentfile coexisten. La eleccion de formato es por workspace, no global.

Rationale: La coexistencia evita una migracion big-bang. Los agentes se transmutan workspace por workspace, validando fidelidad en cada paso.

## 14. Validacion

| Check | Criterio | Enforcement | Accion si falla |
|-------|----------|-------------|-----------------|
| Formato unico | El workspace contiene `AGENT.md` XOR componentes legacy, nunca ambos | lint | Elegir formato |
| Schema completo | Frontmatter cumple schema definido en §3 | schema | Corregir frontmatter |
| Nivel coherente | Las dimensiones declaradas son coherentes con el nivel de complejidad (§5) | lint | Completar dimensiones faltantes o reducir nivel |
| Plan valido | FSM cumple §3.4 (alcanzable, determinista, terminal correcto) | lint | Corregir plan |
| Interface cerrada | §3.5 (tools = permissions) | lint | Alinear |
| Subsumision | §6 (tools containment, KB containment, behavior precedence) | lint | Corregir subsumision |
| Body puro | §4 (sin declaraciones que pertenecen al frontmatter) | manual | Mover al frontmatter |
| Transmutacion fiel | Si migrado, `Forget(transmutado) == Forget(legacy)` | manual | Completar transmutacion |
| Lifecycle valido | §3.2 (transiciones validas, deprecated_by si aplica) | lint | Corregir lifecycle |
| Invariantes categoricas | §11 (determinismo, cerradura, composicionalidad, naturalidad, fidelidad) | manual | Corregir segun invariante violada |
| Precedencia | §13 (gobernanza > agentfile-spec > agent-spec-md) | manual | Alinear con precedencia |
