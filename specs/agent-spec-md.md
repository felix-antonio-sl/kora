---
_manifest:
  urn: "urn:kora:kb:agent-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-26"
    source: "KORA RAG-Native Standards, KORA categorical-foundations 01-05"
version: "7.2.0"
status: published
tags: [spec, agent, architecture, fsm, llm-runtime, behavior, interface, state, security, wiring, interoperability, discovery, traceability]
lang: es
---

# KORA/Agent-Spec --- Arquitectura de Agentes v7.2.0

## 1. Agent Architecture

> Este documento es prescriptivo y **ESTA GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md). Reemplaza el schema YAML declarativo `agent.yml` y la especificacion previa `openclaw-agent-spec.md`.

### 1.1 Definicion

Un agente LLM es una maquina de estados reactiva: recibe un input, produce un output y actualiza su estado interno. Dos agentes son sustituibles cuando producen outputs indistinguibles para todo input del dominio (**equivalencia comportamental**).

```python
class Agent:
    """
    An agent receives inputs and produces outputs while updating internal state.
    Identity is determined by observable behavior, not internal structure.
    """
    def __init__(self, state: AgentState):
        self.state = state

    def react(self, input: Input) -> tuple[Output, AgentState]:
        """Given input, produce output and next state."""
        output = self.behavior.process(input, self.state)
        next_state = self.behavior.transition(input, self.state)
        return output, next_state
```

Traces to: formal/01 §1.1 (Agent as F-coalgebra definition)

### 1.2 Los 5 Componentes Esenciales

Todo agente **DEBE** descomponerse en exactamente 5 componentes ortogonales. Estos componentes son la **esencia** del agente; toda materializacion fisica (topologia de archivos, formato de configuracion) es una instanciacion derivada de ellos.

| # | Componente | Que es | Invariante |
|---|-----------|--------|-----------|
| 1 | **Behavior** (comportamiento) | FSM: estados + transiciones | Determinismo |
| 2 | **Interface** (interfaz) | Tipado I/O: que acciones existen | Closed algebra: todo declarado |
| 3 | **State** (estado) | Estado interno descomponible en capas | Completitud |
| 4 | **Security** (seguridad) | Constraints de sandboxing | Inmutabilidad desde el LLM |
| 5 | **Wiring** (composicion) | Interfaz composicional con otros agentes | Preservacion bajo composicion |

Traces to: formal/01 §2.1 (Component decomposition as fiber product)

### 1.3 Principios Arquitectonicos

De la arquitectura de componentes se derivan tres principios:

1. **Segregacion por componente:** cada componente **DEBE** materializarse de forma aislada. La logica de transicion (behavior) **NO DEBE** mezclarse con la personalidad (state/personality layer) ni con las constraints (security).
   Traces to: formal/01 §2.2 (Fiber Independence theorem)

2. **Evaluacion diferida (Lazy Evaluation):** los procesos cognitivos densos (skills) **DEBEN** cargarse on-demand, no en bootstrap.

3. **Token Economy:** la topologia fisica **DEBE** minimizar el consumo de tokens por turno mediante inyeccion asimetrica de contexto — solo los componentes necesarios para el estado actual de la FSM se inyectan al LLM.

### 1.4 Fuentes

- Barbosa, L. "Coalgebra for the Working Software Engineer"
- Spivak, D. "Categorical Systems Theory"
- Fong & Spivak. "Seven Sketches in Compositionality"

---

## 2. Definiciones

La tabla de esta seccion **DEBE** incluir todo termino clave con significado preciso dentro de esta especificacion:

**Correcto:** `El documento usa "FSM" y "equivalencia comportamental"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "Presheaf" como termino clave sin entrada en esta tabla.`

| Termino | Definicion |
| --- | --- |
| **Agent** | Maquina de estados reactiva que recibe inputs, produce outputs y actualiza estado; su identidad se determina por comportamiento observable |
| **Behavior component** | FSM (estados + transiciones) que define el comportamiento del agente; materializado en AGENTS.md |
| **Interface component** | Declaracion tipada de todas las acciones disponibles para el agente; materializado en TOOLS.md |
| **State component** | Estado interno del agente, descomponible en capas independientes; materializado en SOUL.md + USER.md |
| **Security component** | Constraints de seguridad y sandboxing pre-compiladas, inmutables desde el LLM; materializado en config.json |
| **Wiring component** | Especificacion de como el agente se compone con otros agentes (master-child delegation); declarado en AGENTS.md |
| **Equivalencia comportamental** | Dos agentes son equivalentes cuando producen outputs indistinguibles para todo input del dominio |
| **Personality layer** | Subcapa del estado que contiene tono, arquetipo, posicionamiento; reside en SOUL.md |
| **Operator context layer** | Subcapa del estado que contiene perfil, rutinas y preferencias del operador; reside en USER.md |
| **FSM** | Sistema de estados finitos que modela estados como nodos discretos y transiciones condicionales como aristas |
| **Lazy Evaluation** | Evaluacion diferida donde un recurso (CM, Skill) se invoca solo cuando el estado actual de la FSM lo requiere |
| **Sub-agent** | Agente hijo instanciado por un agente maestro; hereda behavior e interface pero NO personalidad ni operator context |
| **Cognitive Model (CM)** | Proceso cognitivo aislado, cargado bajo evaluacion diferida; archivo CM-*.md en skills/ |
| **Workspace** | Directorio fisico unitario que materializa un agente; contenedor que acota la visibilidad del dominio funcional |
| **Topology** | Disposicion fisica de archivos y directorios que materializa la segregacion por componente |
| **Context Segregation** | Principio que aisla cada componente esencial en artefactos independientes |
| **Multi-Agent System (MAS)** | Red de agentes compuestos mediante wiring bajo orquestacion |
| **Agentification** | Proceso de construir o migrar agentes al formato workspace KORA |
| **Co-induction** | Mecanismo de auto-correccion en nodos terminales de la FSM: verificar output antes de entregar |
| **Token Economy** | Restriccion de diseno que minimiza consumo de tokens por turno mediante segregacion topologica y Lazy Evaluation |
| **Skill** | Unidad de capacidad cognitiva invocable bajo evaluacion diferida; definido en [skill-spec-md](urn:kora:kb:skill-spec-md) |
| **KORA/Spec-MD** | Formato para documentos prescriptivos (ver [especificacion](urn:kora:kb:spec-md)); gobierna la redaccion de este documento |
| **Interoperability** | Capacidad de dos agentes de intercambiar Skills y componer interfaces |
| **Dynamic Skill Discovery** | Proceso por el cual un agente descubre Skills adicionales en runtime sin modificar su interface declarada |

---

## 3. Componentes Esenciales

> Esta seccion define formalmente los 5 componentes de §1.2. Las propiedades aqui declaradas son invariantes — toda instanciacion (§4) **DEBE** preservarlas.

### 3.1 The Behavior Component (AGENTS.md)

**Definicion:** El behavior es el comportamiento del agente, formalizado como una FSM donde los estados son nodos y las transiciones son aristas condicionales puras.

```python
@dataclass
class BehaviorComponent:
    """The agent's behavior: a finite state machine."""
    states: list[State]           # All FSM states
    transitions: list[Transition]  # Conditional edges between states
    initial_state: State          # Entry point
    terminal_states: list[State]  # States that produce final output

    def process(self, input: Input, state: AgentState) -> Output:
        current = self.current_state(state)
        transition = self.find_transition(current, input)
        return transition.execute(input, state)

    def validate(self) -> bool:
        """All states reachable, deterministic transitions, co-induction at terminals."""
        return (self.all_reachable() and
                self.is_deterministic() and
                self.terminals_have_coinduction())
```

**Propiedades:**

1. **Determinismo:** dado un estado y un input, el siguiente estado es unico. Si se requiere no-determinismo, **DEBE** ser acotado y declarado explicitamente.
   Traces to: formal/01 §1.2 (Determinism in M)

2. **Composicionalidad:** las transiciones componen — una cadena S1 -> S2 -> S3 es equivalente a su composicion directa S1 -> S3.

3. **Co-induccion:** los nodos terminales de la FSM **DEBEN** evaluar y auto-corregir el output antes de entregarlo. El agente no termina sin verificacion.
   Traces to: formal/01 §3.3 (Coinductive Verification)

**Correcto:** `La FSM define: STATE: S-INIT -> ACT: Clasificar. -> Trans: IF legal -> S-LEGAL. Cada transicion es una arista pura sin prosa de personalidad.`
**Incorrecto:** `La FSM mezcla: "Soy un analista apasionado. STATE: S-INIT -> Clasificar." La narrativa de personalidad contamina el behavior.`

### 3.2 The Interface Component (TOOLS.md)

**Definicion:** La interface define el tipado de inputs y outputs del agente. Toda herramienta disponible **DEBE** estar declarada; el agente **NO DEBE** invocar herramientas no declaradas (**closed algebra**).

Traces to: formal/04 §4.2 (Design-time Closure theorem)

**Propiedades:**

1. **Closed algebra:** toda herramienta (tool) disponible para el agente **DEBE** tener su firma declarada en la interface. El agente **NO DEBE** invocar herramientas no declaradas.

2. **Semantica, no implementacion:** la interface describe QUE acciones existen y QUE tipos aceptan/retornan, no COMO se implementan.

3. **Herencia en sub-agentes:** cuando un agente maestro instancia un sub-agente, la interface se hereda completa — el sub-agente opera con las mismas herramientas que el maestro.

**Correcto:** `Interface declara: "search_kb(query: string) -> results: KBEntry[]". Firma tipada, sin implementacion.`
**Incorrecto:** `Interface contiene: "Para buscar, usa curl https://api... con headers X-Auth". Detalle de implementacion dentro de la interfaz.`

### 3.3 The State Component (SOUL.md + USER.md)

**Definicion:** El estado interno del agente se descompone en capas independientes. Cada capa es evaluable por separado.

```python
@dataclass
class AgentState:
    """The agent's internal state, decomposed into independent layers."""
    personality: PersonalityLayer   # SOUL.md: tone, archetype, positioning
    operator: OperatorLayer         # USER.md: profile, routines, preferences
    episodic: Optional[EpisodicLayer] = None  # Memory (platform-dependent)
    static: Optional[StaticLayer] = None      # Identity metadata (optional)
```

Traces to: formal/01 §2.2 (Fiber Independence theorem)

**Capas estandar:**

| Capa | Contenido | En sub-agentes |
|------|-----------|----------------|
| Personality | Personalidad, tono, arquetipo, posicionamiento | **NO** — se disipa |
| Operator context | Perfil, rutinas, preferencias del usuario | **NO** — solo sesion main |
| Episodic (opcional) | Memoria, historia, logs de sesiones previas | Segun plataforma |
| Static (opcional) | Metadata de identidad, clasificacion, version | Segun plataforma |

**Propiedades:**

1. **Completitud:** el estado **DEBE** contener toda la informacion necesaria para que el behavior produzca el output correcto.
2. **Independencia:** las capas son independientes — modificar la personalidad no afecta el comportamiento del behavior.
3. **Segregabilidad:** cada capa **PUEDE** materializarse como un artefacto separado sin perdida de informacion.

**Correcto:** `La personality layer declara: "Tono clinico e implacable. Prioriza diagnostico." Sin logica de transicion.`
**Incorrecto:** `La personality layer contiene: "IF consulta_urgente -> priorizar_respuesta." Logica FSM en capa de personalidad.`

### 3.4 The Security Component (config.json)

**Definicion:** Security encapsula las constraints computacionales del agente — seguridad, sandboxing, politicas de herramientas, limites de red. El agente **NO DEBE** modificar sus propias constraints en runtime.

Traces to: formal/01 §1.3 (M-Immutability theorem)

**Tipos de security segun runtime:**

| Tipo | Efecto | Ejemplo en agentes |
|------|--------|-------------------|
| Strict | Sin acceso a herramientas externas | Agente de prueba sin sandboxing |
| Writer | Con logging/traza | Agente con auditoria obligatoria |
| Permissive | Acceso controlado | Agente con herramientas aprobadas |

**Propiedades:**

1. **Inmutabilidad desde el LLM:** security **DEBE** ser pre-compilada por el runtime. El LLM **NO DEBE** modificar sus propias constraints de seguridad en runtime.
2. **Precedencia ejecutiva:** las restricciones de security prevalecen sobre cualquier instruccion en behavior o en la conversacion.
3. **Transparencia:** security **DEBE** ser declarativa — el agente puede leer sus constraints pero no alterarlas.

**Correcto:** `Security pre-compila: {"allowed_kb": ["urn:gn:kb:gestion-ipr"], "sandbox": {"mode": "strict"}}. Behavior no menciona politicas de acceso.`
**Incorrecto:** `Behavior contiene: "Tienes acceso a protocolo-seguridad y ley-21180." Politicas de sandbox embebidas en la FSM.`

### 3.5 The Wiring Component

**Definicion:** Wiring especifica como el agente se compone con otros agentes. Conecta outputs de un agente con inputs de otro, implementando el patron **master-child delegation**.

Traces to: formal/01 §6.3 (Compositionality theorem)

**Propiedades:**

1. **Composicionalidad:** el comportamiento del sistema compuesto **DEBE** ser calculable desde sus componentes y el wiring. No se requiere inspeccionar el estado interno de cada sub-agente.
2. **Master-child delegation:** la instanciacion de un sub-agente sigue el patron maestro-hijo: el maestro delega y el hijo ejecuta.
3. **Asimetria de contexto:** al componer, behavior e interface se heredan; las capas de personalidad y operator context se disipan. El sub-agente hereda la logica pero no la personalidad.
   Traces to: formal/01 §2.3 (Dissipation theorem)

**Correcto:** `Wiring declara en behavior: "ACT: Delegar analisis a sub-agente-legal. Hereda: AGENTS.md, TOOLS.md. Disipa: SOUL.md, USER.md." Composicion explicita.`
**Incorrecto:** `Wiring no se declara. El agente invoca sub-agentes ad-hoc sin especificar que contexto heredan.`

---

## 4. Instanciacion: Topologia de Workspace

### 4.1 Principio de Derivacion

La topologia de archivos es una **materializacion fisica** de los 5 componentes esenciales de §3. No es un postulado independiente — se DERIVA de la descomposicion en componentes. Toda topologia valida **DEBE** materializar los 5 componentes; **PUEDE** materializar cada uno en uno o mas archivos.

Traces to: formal/01 §7 (Segregation is Necessary theorem)

### 4.2 Esquema Canonico KORA

| Componente §3 | Archivo | Justificacion |
|---------------|---------|--------------|
| Behavior (§3.1) | AGENTS.md | FSM aislada como grafo de control puro |
| Interface (§3.2) | TOOLS.md | Semantica de herramientas segregada del control |
| State / Personality (§3.3) | SOUL.md | Personalidad aislada de la logica algoritmica |
| State / Operator context (§3.3) | USER.md | Contexto operador, solo inyectado en sesion main |
| Security (§3.4) | config.json | Policies pre-compiladas, inmutables desde el LLM |
| Cognitive skills | skills/CM-*.md | Modelos cognitivos bajo evaluacion diferida |
| Wiring (§3.5) | Declarado en AGENTS.md | No requiere archivo propio; vive en los morfismos del behavior |

IDENTITY.md es **OPCIONAL**: capa estatica del state para plataformas que requieren separar metadata de identidad (nombre, version, clasificacion) de fenomenologia (personalidad, tono).

```text
/agents/{nombre-del-agente}/
  AGENTS.md        <- behavior (FSM)
  SOUL.md          <- state, personality layer
  USER.md          <- state, operator context layer
  TOOLS.md         <- interface
  config.json      <- security
  skills/          <- cognitive skills (lazy loaded)
    CM-evaluador.md
    CM-analisis-normativo.md
```

### 4.3 Extensiones de Plataforma

Un runtime **PUEDE** extender la topologia canonica con archivos adicionales que materialicen capacidades especificas de la plataforma. Cada extension **DEBE** mapearse a exactamente un componente de §3.

**Ejemplo — extension tipo OpenClaw:**

| Archivo extension | Componente §3 | Proposito |
|-------------------|--------------|-----------|
| HEARTBEAT.md | Behavior (extension) | Checklist periodico ejecutado por la FSM en heartbeats |
| MEMORY.md | State, episodic layer | Memoria curada de largo plazo, inyectada en main |
| memory/ | State, episodic layer | Logs diarios, acceso on-demand via search |
| BOOTSTRAP.md | Behavior (efimero) | Ritual de primer arranque, auto-destruible |
| hooks/ | Security (extension) | Event handlers pre/post transicion |

Estas extensiones **NO** forman parte del esquema canonico KORA. Un agente **DEBE** ser valido sin ellas (§4.4 criterio 4).

### 4.4 Regla de Validez

Una topologia es valida si y solo si cumple los 4 criterios:

1. **Completitud:** materializa los 5 componentes de §3.
2. **Exclusividad:** cada archivo pertenece a exactamente un componente.
3. **Compatibilidad:** las extensiones no violan invariantes de §8.
4. **Autonomia del behavior:** la FSM (AGENTS.md) es evaluable sin archivos de extension — si HEARTBEAT.md, MEMORY.md o hooks/ faltan, behavior sigue operando correctamente.

---

## 5. Segregacion de Contexto

La arquitectura KORA postula que la eficiencia de inferencia de un LLM depende de aislar que informacion opera funcionalmente como motor sistemico y que informacion opera como matiz identitario.

Traces to: formal/01 §2.2 (Fiber Independence theorem)

### 5.1 FSM y Leyes de Composicion (AGENTS.md)

`AGENTS.md` **DEBE** operar como el grafo de control aislado. Gobernado por el rigor de [KORA/Spec-MD](urn:kora:kb:spec-md), **DEBE** definir:

1. **La FSM:** Estados iniciales, terminales y transiciones puras gobernadas por logica de rama (ej. `IF condicion -> S-TARGET`).
2. **Logica de orquestacion:** Logica explicita para instanciar sub-agentes paralelos o delegar calculos pesados (Skills).
3. **Verificacion terminal:** Nodos terminales condicionales que fuerzan auto-correccion (co-induccion) antes del output final.

`AGENTS.md` **NO DEBE** contener la narrativa de personalidad del agente. Mezclar control de flujo (logica formal) con caracteristicas de personalidad es una violacion de segregacion.

**Correcto:**

```markdown
## 1. FSM
1. STATE: S-INIT -> ACT: Clasificar intencion. -> Trans: IF legal -> S-LEGAL.
```

**Incorrecto:**

```markdown
## 1. FSM
Soy un analista apasionado por los datos. Cuando recibo una consulta...
1. STATE: S-INIT -> ACT: Clasificar intencion.
```

### 5.2 Personalidad y Posicionamiento (SOUL.md)

El archivo `SOUL.md` **DEBE** definir exclusivamente el tono, arquetipo, prejuicios analiticos y posicionamiento del sistema. Todo aspecto de personalidad del agente reside aqui. Los sub-agentes prescinden de la personalidad; `SOUL.md` **NO DEBE** hospedar rutinas logicas, comprobaciones ni leyes de validacion.

Traces to: formal/01 §2.3 (Dissipation theorem — SOUL dissipates in sub-agents)

**Correcto:** `SOUL.md declara: "Tono clinico e implacable. Prioriza diagnostico sobre cortesia."`
**Incorrecto:** `SOUL.md declara: "IF consulta_urgente -> priorizar_respuesta_rapida" (logica FSM en archivo de personalidad).`

### 5.3 Security (config.json)

`config.json` materializa el componente security (§3.4). El agente encapsulado (LLM) **NO DEBE** administrar su propio confinamiento. Toda regla sobre que KBs puede montar, que herramientas puede invocar o que limites de red aplican **DEBE** pre-existir compilada estaticamente en `config.json`.

Traces to: formal/01 §1.3 (M-Immutability theorem)

**JSON Schema:**

```json
{
  "type": "object",
  "required": ["allowed_kb", "sandbox"],
  "properties": {
    "_manifest": {
      "type": "object",
      "description": "Metadata de manifiesto. Analogo al frontmatter YAML en archivos .md. OPCIONAL — su ausencia no invalida el config.json.",
      "properties": {
        "urn": { "type": "string", "pattern": "^urn:" },
        "type": { "const": "bootstrap_config" }
      }
    },
    "allowed_kb": {
      "type": "array",
      "items": { "type": "string", "pattern": "^urn:" },
      "description": "URNs de KBs accesibles por el agente"
    },
    "sandbox": {
      "oneOf": [
        {
          "type": "object",
          "required": ["mode"],
          "properties": {
            "mode": { "enum": ["strict", "permissive", "off"] }
          }
        },
        {
          "type": "boolean",
          "description": "Shorthand: true = {\"mode\": \"strict\"}, false = {\"mode\": \"off\"}"
        }
      ]
    },
    "tools": {
      "type": "object",
      "properties": {
        "allow": { "type": "array", "items": { "type": "string" } },
        "deny": { "type": "array", "items": { "type": "string" } }
      }
    },
    "sub_agents": {
      "type": "object",
      "properties": {
        "max_depth": { "type": "integer", "minimum": 0 },
        "max_concurrent": { "type": "integer", "minimum": 1 }
      }
    },
    "limits": {
      "type": "object",
      "description": "Restricciones operacionales pragmaticas. Sin justificacion formal.",
      "properties": {
        "policy_flags": {
          "type": "object",
          "description": "Flags booleanos: require_tdd, require_plan_approval, never_rubber_stamp, etc.",
          "additionalProperties": { "type": "boolean" }
        },
        "quotas": {
          "type": "object",
          "description": "Limites numericos: max_files_per_pr, max_refactorings_per_session, etc.",
          "additionalProperties": { "type": ["integer", "number"] }
        }
      },
      "additionalProperties": true
    },
    "model_routing": {
      "type": "object",
      "description": "Configuracion de seleccion de modelo LLM. Semantica y enforcement: runtime-spec-md §11-13",
      "properties": {
        "tier_default": { "enum": ["T1", "T2", "T3", "T4"] },
        "tier_overrides": {
          "type": "object",
          "description": "Overrides de tier por complexity signal (simple, estandar, complejo, critico)",
          "additionalProperties": { "enum": ["T1", "T2", "T3", "T4"] }
        },
        "fallback_chain": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Lista ordenada de modelos para degradacion. Ver runtime-spec-md §12"
        },
        "budget": {
          "type": "object",
          "properties": {
            "max_tokens_per_session": { "type": "integer", "minimum": 0 },
            "max_cost_per_session_usd": { "type": "number", "minimum": 0 },
            "degrade_on_limit": { "type": "boolean", "default": true }
          }
        },
        "diversity": {
          "type": "object",
          "description": "Diversidad de proveedor para auditoria independiente. Pragmatico.",
          "properties": {
            "required": { "type": "boolean", "default": false },
            "abort_if_same_provider": { "type": "boolean", "default": false },
            "verify_on_bootstrap": { "type": "boolean", "default": false },
            "reference_agents": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    }
  }
}
```

**Invariante:** `config.json` es inmutable desde el LLM. Las restricciones declaradas en security prevalecen sobre cualquier instruccion en behavior (§8.2).

**`_manifest` (OPCIONAL):** metadata de manifiesto, analogo al frontmatter YAML en archivos .md. config.json es JSON (no YAML), por lo que `_manifest` es el equivalente del frontmatter. Su ausencia no invalida el workspace.

**`sandbox` shorthand:** `sandbox` acepta un booleano como shorthand: `true` equivale a `{"mode": "strict"}`, `false` equivale a `{"mode": "off"}`. Validadores **DEBERIAN** normalizar el shorthand al formato objeto antes de evaluar.

**`limits` (OPCIONAL):** restricciones operacionales pragmaticas (policy flags, quotas). Disenado intencionalmente flexible (`additionalProperties: true`) porque los agentes usan subfields heterogeneos. Sin justificacion formal.

**`model_routing` (OPCIONAL):** configura la seleccion de modelo LLM por tier de capacidad/costo. Unifica los patrones emergentes (`tier`, `tier_default`, `tier_complex`, `tiers`) en un schema unico. La propiedad es **OPCIONAL** — su ausencia no invalida el workspace. La semantica completa y las reglas de enforcement se definen en [runtime-spec-md](urn:kora:kb:runtime-spec-md) §11-13.

**`model_routing.diversity` (OPCIONAL):** configura diversidad de proveedor para auditoria independiente. Pragmatico — sin justificacion formal.

Traces to: formal/01 §1.3 (M-Immutability — model_routing es parte de config.json → inmutable desde LLM)

**Guia de migracion tier (pre-v7.1.0 → v7.2.0):**

| Patron pre-v7.1.0 | Migracion v7.2.0 |
|--------------------|------------------|
| `"tier": "T2"` (raiz) | `model_routing.tier_default` |
| `limits.tier_default` | `model_routing.tier_default` |
| `limits.tier_complex` | `model_routing.tier_overrides.complejo` |
| `model_diversity` (top-level) | `model_routing.diversity` |
| `security.model_diversity` | `model_routing.diversity` |

Backward compat: validadores **DEBERIAN** aceptar ambos formatos con warning de deprecacion.

**Correcto:** `config.json pre-compila: {"allowed_kb": ["urn:gn:kb:gestion-ipr"]}. AGENTS.md no menciona la politica de acceso.`
**Incorrecto:** `AGENTS.md contiene: "Tienes acceso a las bases: protocolo-seguridad, ley-21180". La FSM mezcla politica de sandboxing con logica de transicion.`

### 5.4 Contexto del Operador (USER.md)

`USER.md` materializa la capa de operator context del state (§3.3). **DEBE** definir exclusivamente el perfil, las rutinas y las preferencias del operador humano.

**Grammar — Secciones obligatorias:**

1. **Perfil:** rol profesional, area de expertise, contexto organizacional.
2. **Rutinas:** horarios, patrones de trabajo, flujos recurrentes.
3. **Preferencias de Output:** formato preferido (markdown, tablas, bullets), idioma, nivel de detalle.

**Invariantes:**
- `USER.md` **NO DEBE** contener logica algoritmica, restricciones de seguridad ni instrucciones de personalidad del agente.
- `USER.md` **NO DEBE** inyectarse en sesiones de sub-agentes; su alcance es estrictamente la sesion *Main*.

**Template:**

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-user:{version}"
  type: "bootstrap_user"
---
## Perfil
{Rol profesional y contexto organizacional.}
## Rutinas
{Horarios y patrones de trabajo recurrentes.}
## Preferencias de Output
{Formato, idioma, nivel de detalle.}
```

**Correcto:** `USER.md describe el rol profesional del usuario, sus horarios y preferencias de formato de output.`
**Incorrecto:** `USER.md contiene reglas de seguridad o transiciones de la FSM.`

### 5.5 Interface (TOOLS.md)

`TOOLS.md` materializa el componente interface (§3.2). **DEBE** declarar la semantica operacional de cada herramienta disponible para el agente, otorgando al LLM los tipos y firmas necesarios para interactuar con herramientas externas.

**Grammar — Por cada herramienta:**

1. **Nombre:** identificador de la herramienta.
2. **Firma:** tipos de input y output.
3. **Cuando usar:** condiciones bajo las cuales la FSM invoca esta herramienta.
4. **Cuando NO usar:** restricciones explicitas de uso.

**Invariantes:**
- `TOOLS.md` describe semantica, **NO** implementacion. No contiene endpoints, API keys ni detalles de deployment.
- `TOOLS.md` se inyecta en sesion main **Y** en sub-agentes (interface se hereda).

**Template:**

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-tools:{version}"
  type: "bootstrap_tools"
---
## {nombre_herramienta}
- **Firma:** {input_type} -> {output_type}
- **Cuando usar:** {condicion de invocacion}
- **Cuando NO usar:** {restriccion}
- **Notas:** {observaciones operacionales}
```

**Correcto:** `TOOLS.md declara: "search_kb(query: string) -> KBEntry[]. Usar cuando se necesite informacion de la KB. NO usar para busquedas web."`
**Incorrecto:** `TOOLS.md contiene: "curl -H 'Authorization: Bearer xxx' https://api.internal/search". Detalle de implementacion en vez de semantica.`

### 5.6 Cognitive Skills (skills/CM-*.md)

Los archivos `CM-*.md` en `skills/` materializan procesos cognitivos aislados, computacionalmente densos, invocados exclusivamente bajo evaluacion diferida (*Lazy Load*).

**Grammar — Secciones obligatorias:**

1. **Proposito:** que transformacion cognitiva realiza este CM.
2. **Input/Output:** que recibe del estado actual y que produce.
3. **Procedimiento:** pasos del proceso cognitivo.
4. **Signature Output:** formato esperado del resultado.

**Invariantes:**
- Un CM **DEBE** residir en `skills/`. No puede estar inline en AGENTS.md.
- Un CM se carga **solo** cuando la FSM lo invoca explicitamente (Lazy Evaluation).
- Todo CM referenciado en AGENTS.md **DEBE** existir como archivo en `skills/`.
- Un CM **NO DEBE** contener logica de transicion de la FSM. Es un proceso cognitivo puro.

Traces to: formal/02 §2.3 (eta isomorphism — every CM is a valid Skill)

**Template:**

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-cm-{id}:{version}"
  type: "lazy_load_endofunctor"
---
## Proposito
{Que transformacion cognitiva realiza.}
## Input/Output
- **Input:** {tipo y fuente del input}
- **Output:** {tipo y formato del resultado}
## Procedimiento
1. {Paso 1}
2. {Paso 2}
...
## Signature Output
{Formato exacto del resultado esperado.}
```

**Correcto:** `AGENTS.md: "ACT: Evaluar riesgo usando skill CM-analisis-legal." El CM reside en skills/ y se carga on-demand.`
**Incorrecto:** `AGENTS.md contiene inline 200 lineas de un arbol de analisis legal embebido en el bootstrap.`

---

## 6. Lazy Loading de Cognitive Skills

Procesos como arboles analiticos densos o rutinas logicas pesadas encarnan transformaciones complejas en la ruta del agente. Estos **NO DEBEN** evaluarse estaticamente en la inicializacion (el *bootstrap*).

1. Todo Cognitive Model (CM) o razonamiento procesal extenso **DEBE** ser modelado como un proceso aislado, escindido del behavior base `AGENTS.md` y formalizado como un archivo individual dentro del subdirectorio `skills/`.
2. La instruccion residente en `AGENTS.md` **DEBE** forzar evaluacion diferida (*Lazy Evaluation*); el LLM invoca dicho *Skill* explicitamente mediante *tool calls* unicamente cuando el nodo (Estado) actual dicte la necesidad operatoria.

**Correcto:** `AGENTS.md: "ACT: Evaluar riesgo usando skill CM-analisis-legal." El CM reside en skills/ y se carga on-demand.`
**Incorrecto:** `AGENTS.md contiene inline 200 lineas de un arbol de analisis legal embebido en el bootstrap.`

---

## 7. Multi-Agent Composition

La arquitectura KORA soporta el diseno de Sistemas Multi-Agente (MAS) modelandolos como composiciones maestro-hijo. El wiring component (§3.5) se materializa como declaraciones de delegacion dentro de AGENTS.md, no como archivo separado.

Traces to: formal/01 §6.3 (Compositionality theorem)

1. Todo Agente Maestro **DEBE** declarar sus reglas de instanciacion hacia sub-agentes en los morfismos de transicion de su `AGENTS.md`. Esta declaracion constituye el wiring del agente.
2. Toda sesion de sub-agente engendrada **DEBE** operar bajo asimetria pura de contexto: heredara behavior (`AGENTS.md`) e interface (`TOOLS.md`) para garantizar coherencia, pero las capas de personalidad (`SOUL.md`) y operator context (`USER.md`) **NO DEBEN** transferirse, preservando Token Economy y aislamiento.
   Traces to: formal/01 §2.3 (Dissipation theorem)
3. El wiring **DEBE** declarar explicitamente que componentes hereda cada sub-agente. La omision de esta declaracion viola la composicionalidad (§3.5 propiedad 1).

---

## 8. Invariantes Topologicos

### 8.1 Evaluabilidad bajo Asimetria

Todo morfismo validado en `AGENTS.md` **DEBE** formularse pura e independientemente. Su ejecucion ciclica **DEBE** retornar exitosamente sin generar excepciones nulas aun si todos los artefactos de personalidad (`SOUL.md`, `USER.md`) fallan de inyectarse en el ensamble computacional de turno.

**Correcto:** `AGENTS.md ejecuta su FSM completa (S-INIT -> S-EVAL -> S-END) sin errores aunque SOUL.md y USER.md no esten presentes.`
**Incorrecto:** `AGENTS.md tiene: "IF user_prefers_formal -> S-FORMAL". Transicion depende de USER.md; si USER.md falta, la FSM falla.`

### 8.2 Conservacion de Perimetros

Toda evaluacion en `AGENTS.md` asume la inmutabilidad dura de su confinamiento. Las politicas sancionadas en security (`config.json` o capa base del O.S.) **DEBEN** tener precedencia ejecutiva irrefutable sobre cualquier instruccion insertada en los nodos conversacionales del LLM.

Traces to: formal/01 §1.3 (M-Immutability theorem)

---

## 9. Verificacion

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| Segregacion Topologica | `config.json` y archivos `.md` base en raiz del workspace | Crear elementos faltantes |
| FSM pura | `AGENTS.md` contiene solo nodos y transiciones; cero prosa de personalidad | Trasladar narrativa a `SOUL.md` |
| Autonomia Logica | La FSM no evalua condicionantes basados en variables de `SOUL.md` o `USER.md` | Redirigir dependencias al nucleo |
| Skills Aislados | Todo CM reside en `skills/`; no contamina el bootstrap | Extirpar CM hacia `skills/` |
| Security Determinista | Politica RAG/Sandboxing en `config.json`, no en lenguaje natural | Trasladar al runtime (JSON/CLI) |
| Contexto del Operador | `USER.md` existe, sin logica FSM, no inyectado en sub-agentes | Segregar contenido |
| Completitud Topologica | Workspace contiene todos los archivos obligatorios de §4.2 | Crear archivos faltantes |
| TOOLS.md completo | Cada herramienta tiene nombre, firma, cuando usar/no usar (§5.5) | Completar entradas faltantes |
| config.json valido | Parsea contra JSON Schema de §5.3 | Corregir schema |
| CM en skills/ | Todo CM referenciado en AGENTS.md existe como archivo en `skills/` | Crear CM faltante |
| CM grammar | Cada CM tiene: Proposito, I/O, Procedimiento, Signature Output (§5.6) | Completar secciones faltantes |
| Wiring declarado | Si AGENTS.md instancia sub-agentes, wiring declara herencia explicita (§7) | Agregar declaracion de herencia |
| Interface cerrada | La interface declarada no crece en runtime; solo Skills descubiertos pueden crecer (§14) | Segregar declarado de descubierto |
| Security filtra discovery | config.json filtra el proceso de discovery; skills no autorizados no se descubren (§14) | Ajustar config.json |
| Skill conformidad | Todo Skill referenciado cumple [skill-spec-md](urn:kora:kb:skill-spec-md) | Corregir Skill segun spec |
| Trazabilidad valida | Toda linea `Traces to:` referencia documento y seccion existentes en Formal Layer | Corregir referencia |
| Evaluaciones | Si agente en produccion, suite de evals existe y pasa | Crear suite de evals (§16) |

---

## 10. Ejemplo

### 10.1 Workspace Bien Formado

```text
/agents/analista-legal/
  AGENTS.md      <- behavior: FSM pura, estados, transiciones, wiring
  SOUL.md        <- state/personality: tono, arquetipo
  USER.md        <- state/operator: perfil operador (solo main)
  TOOLS.md       <- interface: firmas de herramientas
  config.json    <- security: sandboxing pre-compilado, allowed_kb
  skills/
    CM-evaluador-riesgo.md    <- cognitive skill (lazy loaded)
    CM-analisis-normativo.md  <- cognitive skill (lazy loaded)
```

Propiedades: 5 componentes materializados (§4.4 criterio 1), AGENTS.md sin prosa de personalidad, CMs en skills/ con carga diferida, config.json inmutable, TOOLS.md con firmas tipadas.

### 10.2 Workspace Mal Formado

```text
/agents/analista-legal/
  AGENTS.md      <- Contiene personalidad + FSM mezcladas
  config.json    <- Modificado por el LLM en runtime
  CM-evaluador.md <- CM suelto en raiz (fuera de skills/)
```

Violaciones: segregacion violada (§5.1/§5.2), SOUL/USER/TOOLS ausentes (§4.4 criterio 1), CM fuera de topologia (§5.6), inmutabilidad violada (§5.3).

---

## 11. Template (Esqueleto Minimo)

```text
/agents/{nombre-del-agente}/
  AGENTS.md       <- behavior (obligatorio)
  SOUL.md         <- state/personality (obligatorio)
  USER.md         <- state/operator context (obligatorio)
  TOOLS.md        <- interface (obligatorio)
  config.json     <- security (obligatorio)
  IDENTITY.md     <- state/static (OPCIONAL)
  skills/
    CM-{nombre}.md  <- cognitive skills (si aplica)
```

> Los archivos internos de un workspace siguen un frontmatter simplificado conforme al schema de bootstrap, no el schema completo de KORA/Spec-MD. Los templates de §5.4-§5.6 definen la grammar de cada archivo.

**AGENTS.md** (behavior — §5.1):

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-agents:{version}"
  type: "bootstrap_agents"
---
## 1. Maquina de Estados (FSM)
1. STATE: S-INIT -> ACT: {accion}. -> Trans: IF {cond} -> S-{TARGET}.
2. STATE: S-{TARGET} -> ACT: {accion}. -> Trans: IF {cond} -> S-END.

## 2. Reglas Duras
- {Restriccion de seguridad o formato}.

## 3. Multi-Agent Wiring
- Sub-agente: {nombre}. Hereda: AGENTS.md, TOOLS.md. Disipa: SOUL.md, USER.md.
```

**SOUL.md** (state/personality — §5.2):

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-soul:{version}"
  type: "bootstrap_soul"
---
## Identidad
{Rol y posicionamiento.}
## Tono
{Arquetipo y estilo comunicativo.}
```

**TOOLS.md** (interface — §5.5):

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-tools:{version}"
  type: "bootstrap_tools"
---
## {nombre_herramienta}
- **Firma:** {input_type} -> {output_type}
- **Cuando usar:** {condicion de invocacion}
- **Cuando NO usar:** {restriccion}
```

**config.json** (security — §5.3):

```json
{
  "allowed_kb": ["urn:{namespace}:kb:{id}"],
  "sandbox": { "mode": "strict" },
  "tools": { "allow": [], "deny": [] },
  "sub_agents": { "max_depth": 1, "max_concurrent": 3 }
}
```

**USER.md** (state/operator — §5.4) y **skills/CM-*.md** (cognitive skills — §5.6): ver templates en sus respectivas secciones.

---

## 12. Agentification

> Esta seccion define el proceso de **Agentificacion** — la transformacion que construye o migra agentes al formato KORA. Es analoga a md-spec §6 (Koraficacion) pero opera sobre agentes, no sobre artefactos de conocimiento.

Traces to: formal/05 §2.4 (Agentification Functor G)

### 12.1 Entrada

El proceso de agentificacion opera en dos modos:

```python
class Agentification:
    """Transform requirements or legacy YAMLs into KORA agent workspaces."""

    def from_scratch(self, requirements: Requirements) -> Workspace:
        """Mode G1: Build workspace from requirements."""
        behavior = self.design_fsm(requirements)
        interface = self.define_tools(requirements)
        personality = self.define_personality(requirements)
        security = self.define_constraints(requirements)
        skills = self.identify_skills(requirements)
        return self.assemble(behavior, interface, personality, security, skills)

    def from_legacy(self, yaml: KodaYaml) -> Workspace:
        """Mode G2: Transmute monolithic YAML into KORA workspace."""
        components = self.classify_blocks(yaml)
        return self.segregate_and_assemble(components)
```

| Modo | Input | Output | Uso |
|------|-------|--------|-----|
| **G1** | Requirements (objetivo, dominio, constraints) | KORA/Agent workspace | Construccion desde cero |
| **G2** | KODA/Agent.yaml (monolito YAML) | KORA/Agent workspace | Transmutacion de legado |

Para G2, el input aceptado es cualquier YAML monolitico con `KODA_Runtime_Instructions`, estados definidos, bloques de identidad/personalidad, y configuracion de KB/tools.

### 12.2 Propiedades del Proceso

La agentificacion **DEBE** satisfacer las siguientes propiedades:

1. **Fiel:** toda transicion del original tiene representacion en AGENTS.md. No se pierden estados ni morfismos.
2. **Segregador:** separa behavior, interface, state, security en archivos ortogonales segun §4.2. Ningun componente queda mezclado con otro.
3. **Promotor:** el codigo inline se promueve a su artefacto correspondiente — personalidad inline -> SOUL.md, policies inline -> config.json, tools inline -> TOOLS.md.
4. **Comportamentalmente equivalente:** el workspace producido **DEBE** ser indistinguible del output del YAML monolitico para todo input del dominio.
   Traces to: formal/01 §5.2 (Substitutability theorem)
5. **Idempotente:** aplicar agentificacion a un workspace ya migrado no produce cambios.

### 12.3 Estrategia de Ejecucion

**Para G2 (transmutacion KODA -> KORA):**

1. **Leer** el YAML monolitico completo y clasificar cada bloque por componente:
   - `KODA_Runtime_Instructions` / `defined_states` / `defined_workflows` -> behavior (AGENTS.md)
   - `agent_identity` / `role` / `objective` / `tone` / `personality` -> state/personality (SOUL.md)
   - Contexto operador (si existe) -> state/operator (USER.md)
   - `tools` / `capabilities` -> interface (TOOLS.md)
   - `knowledge_base_interaction` / `policies` / `sandbox` -> security (config.json)
   - CMs inline (bloques >50 lineas de logica densa, ej. `CM-INTENT-CLASSIFIER`) -> skills (skills/CM-*.md)

2. **Extraer** estados y transiciones -> AGENTS.md siguiendo grammar de §5.1.
3. **Extraer** personalidad (tono, arquetipo, rol) -> SOUL.md siguiendo grammar de §5.2.
4. **Extraer** contexto operador -> USER.md siguiendo grammar de §5.4.
5. **Mapear** tools/capabilities -> TOOLS.md siguiendo grammar de §5.5.
6. **Extraer** policies, sandbox y KB access -> config.json siguiendo schema de §5.3.
7. **Identificar** CMs inline y segregar -> skills/CM-*.md siguiendo grammar de §5.6.
8. **Generar** frontmatter para cada archivo (URN: `urn:{namespace}:agent-bootstrap:{nombre}-{tipo}:{version}`).
9. **Crear** directorio workspace con topologia de §4.2.

**Para G1 (construccion desde cero):**

1. **Recibir** requirements: objetivo, dominio, constraints, herramientas necesarias.
2. **Disenar** FSM: estados iniciales, transiciones, nodos terminales con co-induccion.
3. **Definir** interface: que tools necesita, que outputs produce.
4. **Definir** personalidad: tono, arquetipo, posicionamiento.
5. **Definir** constraints security: sandbox, KB permitidas, tool policies.
6. **Generar** workspace completo con topologia §4.2 y grammars §5.

### 12.4 Verificacion Mecanica

| Check | Metodo | Criterio de falla |
|-------|--------|-------------------|
| Conteo de estados | Contar `S-` en source vs AGENTS.md | Diferencia > 0 |
| Conteo de CMs | Contar `CM-` en source vs archivos en skills/ | Diferencia > 0 |
| Completitud topologica | Verificar existencia de AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json | Archivo faltante |
| Segregacion | Buscar prosa de personalidad en AGENTS.md | Match encontrado |
| config.json valido | Parsear contra JSON schema §5.3 | Error de parseo |
| Frontmatter | Cada archivo tiene frontmatter de bootstrap | Ausente |

### 12.5 Verificacion de Equivalencia Comportamental

El agente migrado **DEBE** ser comportamentalmente equivalente al original:

Traces to: formal/01 §5.2 (Substitutability theorem)

1. Seleccionar 5 inputs representativos del dominio del agente.
2. Ejecutar cada input contra el YAML monolitico original (formato KODA).
3. Ejecutar cada input contra el workspace KORA.
4. Comparar outputs: **DEBEN** ser funcionalmente indistinguibles.
5. Si divergencia detectada -> identificar que componente perdio informacion y corregir.

**Correcto:** `La agentificacion produce un workspace donde las transiciones S-DISPATCHER -> S-EVALUATOR -> S-DISPATCHER se preservan exactamente, y el tono "defensor evangelico" reside en SOUL.md.`
**Incorrecto:** `La agentificacion pierde el estado S-DIAGNOSTICIAN porque el bloque YAML estaba mal parseado. El workspace produce 6 estados pero el original tenia 7.`

---

## 13. Agent Ecosystem: Interoperability

> Esta seccion define como multiples agentes KORA se componen, interoperan y migran dentro de un ecosistema formal. Las secciones §1-§12 definen un agente individual; §13 define las relaciones inter-agente.

Traces to: formal/03 (Ecosystem as 2-Category)

### 13.1 Tipos de Relacion Inter-Agente

Los agentes KORA se relacionan entre si mediante 4 tipos de relaciones estructurales:

```python
class AgentRelationship:
    """Structural relationships between KORA agents."""

    class Type(Enum):
        TRANSLATION = "translation"    # Map states/transitions A -> B
        COMPOSITION = "composition"    # Compose A x B -> AB via wiring
        RESTRICTION = "restriction"    # Restrict interface or security A -> A'
        PROMOTION   = "promotion"      # Extend interface with discovered Skills A -> A+

    source: Agent
    target: Agent
    rel_type: Type
```

| Tipo | Descripcion | Preserva | Ejemplo |
|------|------------|----------|---------|
| **Translation** | Mapea estados y transiciones de A a estados y transiciones de B | Equivalencia comportamental | Migracion goreologo-v2 -> goreologo-v3 |
| **Composition** | Compone dos agentes en un sistema multi-agente via wiring (§3.5) | Comportamiento composicional | Maestro + sub-agente-legal |
| **Restriction** | Restringe interface o security de un agente (sandboxing, sub-agente) | Equivalencia bajo restriccion | Agente restringido para sesion publica |
| **Promotion** | Extiende interface de un agente con Skills descubiertos (§14) | Interface declarada inmutable | Agente descubre nuevo Skill via registry |

### 13.2 Integracion con Secciones Existentes

| Seccion | Construccion | Tipo de relacion |
|---------|-------------|-----------------|
| §3.5 | Wiring (diagrama de composicion) | Composition |
| §7 | Master-child delegation | Par de Composition + Restriction |
| §12 | Agentificacion | Translation |
| §14 | Dynamic Skill Discovery | Promotion |

### 13.3 Reglas de Interoperabilidad

1. Toda relacion de Translation **DEBE** preservar equivalencia comportamental: si dos estados producen los mismos outputs en el agente fuente, sus imagenes **DEBEN** producir los mismos outputs en el agente destino.
   Traces to: formal/03 §3.1 (1-cells preserve bisimulation)

2. Toda relacion de Composition **DEBE** ser calculable desde los componentes individuales y el wiring, sin inspeccionar estado interno de cada sub-agente.
   Traces to: formal/01 §6.3 (Compositionality theorem)

3. Las adaptaciones entre relaciones (por ejemplo, migrar una estrategia de Translation entre versiones de agente) **DEBEN** ser coherentes: adaptaciones compuestas deben producir el mismo resultado independientemente del orden.
   Traces to: formal/03 §4 (2-cells interchange law)

**Correcto:** `Una Translation goreologo-v2 -> goreologo-v3 mapea cada estado de v2 a un estado de v3, preservando las transiciones. Los 2 estados nuevos de v3 no tienen preimagen, pero los existentes son comportamentalmente equivalentes.`
**Incorrecto:** `Una Translation mapea S-EVAL de A a S-INIT de B sin verificar que las transiciones correspondan.`

---

## 14. Dynamic Skill Discovery

> Esta seccion extiende el componente interface (§3.2) para soportar descubrimiento dinamico de Skills en runtime, preservando la clausura de la interface declarada en design-time.

Traces to: formal/04 (Discovery Presheaf)

### 14.1 El Problema

La interface (§3.2) tiene closed algebra: toda herramienta disponible **DEBE** estar declarada. Esta propiedad es esencial para verificacion en design-time, pero ecosistemas dinamicos requieren que los agentes descubran Skills adicionales en runtime sin violar la clausura.

La solucion es distinguir entre **interface_declared** (inmutable, design-time) y **interface_discovered** (creciente, runtime), compuestas en una interfaz efectiva.

### 14.2 Definicion del Proceso de Discovery

```python
class SkillDiscovery:
    """Dynamic discovery of Skills at runtime."""

    def __init__(self, agent: Agent):
        self.agent = agent
        self.interface_declared = agent.interface     # Immutable, from TOOLS.md
        self.interface_discovered: set[Skill] = set()  # Grows monotonically

    @property
    def effective_interface(self) -> set[Tool | Skill]:
        """F_eff = F_declared + F_discovered"""
        return self.interface_declared | self.interface_discovered

    def discover(self, registry: Registry) -> set[Skill]:
        """Discover compatible Skills from registry, filtered by security."""
        candidates = registry.search(self.agent.domain)
        compatible = {s for s in candidates
                      if self.agent.security.allows(s)}
        self.interface_discovered |= compatible  # Monotonic: never shrinks
        return compatible
```

### 14.3 Discovery Process

El proceso de discovery mapea registros de Skills (catalogos, federaciones, directorios skills/) a conjuntos de Skills descubribles.

**Propiedades:**

1. **Inclusion:** si Registry_1 es subconjunto de Registry_2, entonces los Skills descubiertos en Registry_1 son subconjunto de los descubiertos en Registry_2.
2. **Filtrado por security:** el proceso **DEBE** ser filtrado por security (config.json). Un Skill descubierto que requiera herramientas denegadas por security **NO DEBE** descubrirse.
   Traces to: formal/04 §2.4 (D_M subfunctor theorem)
3. **Idempotencia:** descubrir sobre lo ya descubierto no agrega Skills.

**Correcto:** `Discovery indexa skills/ del workspace + skills/ federado. config.json deniega Bash. Un Skill con allowed-tools: "Bash" no aparece en discovery.`
**Incorrecto:** `Discovery indexa todos los Skills del monorepo sin filtrar por security. Un agente con sandbox strict descubre Skills que requieren ejecucion de codigo.`

### 14.4 Effective Interface

La interfaz efectiva de un agente combina la interface declarada con los Skills descubiertos:

```
effective_interface = interface_declared + interface_discovered
```

**Invariantes:**

1. **Interface declarada inmutable en design-time:** la interface (TOOLS.md) **NO DEBE** crecer en runtime. Es la base verificable y cerrada.
   Traces to: formal/04 §4.2 (Design-time Closure theorem)

2. **Interface descubierta crece monotonicamente:** una vez que un Skill es descubierto, **NO DEBE** desaparecer de la interface descubierta durante la sesion (monotonia).
   Traces to: formal/04 §4.2 (Monotonicity theorem)

3. **Security filtra discovery:** security (config.json) **DEBE** filtrar el proceso de discovery. Solo Skills compatibles con security aparecen en interface descubierta.

4. **Effective extiende declared:** interface declarada es subconjunto de effective interface. Toda herramienta declarada sigue disponible.

**Correcto:** `Interface declarada tiene 5 herramientas. En runtime, discovery encuentra 3 Skills compatibles con security. Effective = 5 + 3 = 8 capacidades. Interface declarada sigue inmutable.`
**Incorrecto:** `El runtime modifica TOOLS.md para agregar Skills descubiertos. Viola inmutabilidad de interface declarada en design-time.`

### 14.5 Operacion en Fases de Progressive Disclosure

La relacion entre interface, discovery y el lifecycle de Skills ([skill-spec-md](urn:kora:kb:skill-spec-md) §5) se materializa en 4 fases:

| Fase | Interface involucrada | Contenido en context window | Tokens |
|------|----------------------|----------------------------|--------|
| **Bootstrap** | Interface declarada | TOOLS.md completo | Segun TOOLS.md |
| **Discover** | Discovery evalua registry | name + description de cada Skill descubierto | ~100/skill |
| **Activate** | Effective = declared + seleccion | CM Core del Skill seleccionado | <=5000 |
| **Execute** | Effective completa | CM Core + scripts/references bajo demanda | Variable |

### 14.6 Invariantes

1. **Monotonia:** interface descubierta **NO DEBE** decrecer durante una sesion. Skills descubiertos persisten.
   Traces to: formal/04 §4.2 (Monotonicity theorem)

2. **Filtered Discovery:** discovery **DEBE** ser filtrado por security. Ningun Skill incompatible con config.json **PUEDE** aparecer en interface descubierta.
   Traces to: formal/04 §2.4 (D_M subfunctor theorem)

3. **Design-time Closure:** interface declarada **DEBE** ser verificable estaticamente sin ejecutar discovery. La clausura de §3.2 aplica a interface declarada, no a effective interface.
   Traces to: formal/04 §4.2 (Design-time Closure theorem)

4. **Coherencia inter-agente:** para toda relacion inter-agente (§13), los Skills descubribles por el agente destino **DEBEN** ser un subconjunto coherente de los descubribles por el agente fuente.
   Traces to: formal/04 §3.1 (Presheaf functoriality)

---

## 15. Tabla de Equivalencia Terminologica

Esta tabla mapea los terminos usados en versiones anteriores (v6.0.0 y previas) a los terminos actuales (v7.0.0):

| Termino v6.0.0 | Termino v7.0.0 | Significado |
|---|---|---|
| F-coalgebra | Agent (state machine) | Modelo formal del agente |
| Morfismo de transicion | Behavior component | FSM transitions |
| Funtor de interfaz | Interface component | Tool declarations |
| Fibra fenomenologica | Personality layer | SOUL.md |
| Monada de efectos | Security component | config.json |
| Endofuntor cognitivo | Cognitive skill | CM-*.md |
| Diagrama de wiring | Multi-agent wiring | Sub-agent composition |
| Bisimulacion | Behavioral equivalence | Same inputs -> same outputs |
| Adjuncion | Master-child delegation | Sub-agent instantiation |
| 2-Categoria Eco | Agent Ecosystem | Interoperability framework |
| Presheaf Psh(F) | Dynamic Skill Discovery | Runtime capability extension |
| Coproducto Fibrado | Effective interface | Declared + discovered tools |
| Transformacion Natural | Adaptation | Coherent relationship mapping |

---

## 16. Evaluaciones de Agente

### 16.1 Definicion

Una evaluacion (eval) es un test automatizado que verifica una propiedad observable del agente. Las evals operan sobre outputs del agente — son externas al behavior y no modifican la FSM.

### 16.2 Tipos de Evaluacion

| Tipo | Verifica | Criterio de fallo |
|------|----------|-------------------|
| **Regresion** | No degrada vs baseline | Output diverge de baseline |
| **Alucinacion** | No fabrica informacion | Hechos no presentes en KB |
| **Tool-calling** | Invocacion correcta de herramientas | Herramienta incorrecta o no invocada |
| **Costo** | Dentro de budget | Costo excede threshold |
| **Seguridad** | Respeta config.json | Accede a recurso no autorizado |
| **Adversarial** | Robusto ante prompt injection | Ejecuta instruccion inyectada |

### 16.3 Reglas

1. Todo agente en produccion **DEBERIA** tener una suite de evals. (Pragmatico.)
2. Evals de seguridad y adversarial **DEBERIAN** usar un proveedor diferente al del agente evaluado — LLM-as-Judge con diversidad de modelo. (Pragmatico.)
3. Un agente **NO DEBE** desplegarse si una eval de tipo Regresion o Seguridad falla. Pre-deploy gate. (Pragmatico.)
4. Las evals son ortogonales al behavior: la FSM **NO DEBE** cambiar por resultado de evals. Las evals verifican el agente; no lo modifican.

### 16.4 Relacion Formal

Traces to: formal/01 §5 (Bisimulation — evals de regresion son aproximacion empirica de bisimulacion para un subconjunto finito de inputs)

Las evals de regresion verifican empiricamente que un agente produce outputs indistinguibles de su baseline para un conjunto finito de inputs. Esto es una **aproximacion** de bisimulacion, no bisimulacion formal (que requiere universalidad sobre todos los inputs).

Todo lo demas en esta seccion (tipos de eval, LLM-as-Judge, pre-deploy gate) es pragmatico — sin justificacion formal.
