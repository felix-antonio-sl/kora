---
_manifest:
  urn: "urn:kora:kb:agent-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "KORA RAG-Native Standards"
version: "5.0.0"
status: published
tags: [spec, agent, architecture, fsm, llm-runtime, coalgebra, lens, categorical]
lang: es
---

# KORA/Agent-Spec — Especificación Categórica de Agentes v5.0.0

## 1. Ontología Categórica del Agente

> Este documento es prescriptivo y **ESTÁ GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md). Reemplaza el schema YAML declarativo `agent.yml` y la especificación previa `openclaw-agent-spec.md`, estableciendo el formalismo categórico como paradigma canónico.

### 1.1 Definición Formal

Un agente LLM es una **F-coalgebra con interfaz lens en una categoría de Kleisli**:

```
Agente = (U, c: U → F(U))

donde F(U) = (Out × U)^In    — funtor de autómata reactivo
y el update vive en Kl(M)    — M = mónada de efectos
```

El estado U es oculto; solo el comportamiento observable (la secuencia de outputs ante inputs) determina la identidad del agente. Dos agentes son sustituibles sii son **bisimilares**: producen outputs indistinguibles para todo input del dominio.

### 1.2 Los 5 Componentes Esenciales

Todo agente **DEBE** descomponerse en exactamente 5 componentes ortogonales. Estos componentes son la **esencia** del agente; toda materialización física (topología de archivos, formato de configuración) es una instanciación derivada de ellos.

| # | Componente                | Símbolo | Qué es                                       | Invariante                     |
|---|---------------------------|---------|-----------------------------------------------|--------------------------------|
| 1 | Morfismo de transición    | c       | Comportamiento: FSM (estados + transiciones)  | Determinismo en M              |
| 2 | Funtor de interfaz        | F       | Tipado I/O: qué acciones existen              | Álgebra cerrada                |
| 3 | Espacio de estados        | U       | Estado interno descomponible en fibras         | Completitud                    |
| 4 | Mónada de efectos         | M       | Constraints de seguridad y sandboxing          | Inmutabilidad desde el LLM     |
| 5 | Diagrama de wiring        | W       | Interfaz composicional con otros agentes       | Preservación bajo composición  |

### 1.3 Principios Arquitectónicos

De la fundamentación coalgebraica se derivan tres principios:

1. **Segregación por componente:** cada componente **DEBE** materializarse de forma aislada. La lógica de transición (c) **NO DEBE** mezclarse con la fenomenología (fibra de U) ni con las constraints (M).
2. **Evaluación diferida (Lazy Evaluation):** los endofuntores cognitivos (procesos densos sobre U) **DEBEN** cargarse on-demand, no en bootstrap.
3. **Token Economy:** la topología física **DEBE** minimizar el consumo de tokens por turno mediante inyección asimétrica de contexto — solo los componentes necesarios para el estado actual de la FSM se inyectan al LLM.

### 1.4 Fuentes

- Barbosa, L. "Coalgebra for the Working Software Engineer" — modelo coalgebraico
- Spivak, D. "Categorical Systems Theory" — lenses, wiring diagrams, sistemas monádicos
- Fong & Spivak. "Seven Sketches in Compositionality" — fundamentos categóricos

---

## 2. Definiciones

La tabla de esta sección **DEBE** incluir todo término clave con significado preciso dentro de esta especificación:

**Correcto:** `El documento usa "FSM" y "Bisimulación"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "Adjunción" como término clave y no existe entrada para "Adjunción".`

| Término                     | Definición                                                                                                                         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **F-coalgebra**             | Par (U, c: U → F(U)) donde U es espacio de estados y c es el morfismo de transición; modelo formal de un agente                   |
| **Lens**                    | Par (expose, update) que modela la interfaz bidireccional del agente con su entorno; expose: U → Out, update: U × In → M(U)       |
| **Bisimulación**            | Relación R entre estados de dos agentes tal que estados relacionados producen outputs indistinguibles; criterio de sustituibilidad |
| **Fibra**                   | Subestructura ortogonal del espacio de estados U; cada fibra es independientemente evaluable y segregable                          |
| **Mónada de Efectos**       | Estructura algebraica M que encapsula el tipo de efectos computacionales del agente (Identity, Powerset, Distribution, Writer)     |
| **Diagrama de Wiring**      | Especificación de cómo los outputs de un agente alimentan los inputs de otro; morfismo en la categoría WD                         |
| **Categoría de Kleisli**    | Kl(M): categoría donde los morfismos son funciones A → M(B); permite componer transiciones con efectos                            |
| **FSM**                     | Sistema dinámico que modela estados como objetos discretos y transiciones condicionales como morfismos puros                       |
| **Morfismo**                | Transición determinista entre dos estados de la FSM; flecha en la categoría del agente                                            |
| **Endofuntor**              | Funtor de una categoría en sí misma; modela procesos cognitivos aislados que transforman el contexto preservando estructura        |
| **Lazy Evaluation**         | Evaluación diferida donde un recurso (CM, Skill) se invoca solo cuando el estado actual de la FSM lo requiere                     |
| **Sub-agente**              | Categoría adjunta; ejecución que hereda el esquema de control (c) pero disipa la fenomenología (fibra de U)                       |
| **Modelo Cognitivo (CM)**   | Endofuntor cognitivo; proceso aislado, asíncrono y convocado bajo evaluación diferida pura                                        |
| **Workspace**               | Directorio físico unitario que materializa un agente; contenedor que acota la visibilidad del dominio funcional                    |
| **Topología**               | Disposición física de archivos y directorios que materializa la segregación por componente; instanciación derivada de §3           |
| **Segregación de Contexto** | Principio que aísla cada componente esencial (c, F, U, M, W) en artefactos independientes                                        |
| **SMA**                     | Sistema Multi-Agente; red de agentes compuestos mediante wiring diagrams bajo orquestación categórica                             |
| **Adjunción**               | Relación entre dos funtores (Left ⊣ Right) que modela la instanciación de sub-agentes por un agente maestro                      |
| **Funtor**                  | Mapeo entre categorías que preserva estructura (objetos→objetos, morfismos→morfismos, composición→composición)                    |
| **Token Economy**           | Restricción de diseño que minimiza consumo de tokens por turno mediante segregación topológica y *Lazy Evaluation*                |
| **Co-inducción**            | Técnica de prueba dual a la inducción; en agentes, mecanismo de auto-corrección en nodos terminales de la FSM                     |
| **Categoría**               | Estructura algebraica: objetos, morfismos y leyes de composición asociativa con identidad                                         |
| **KORA/Spec-MD**            | Formato para documentos prescriptivos (ver [especificación](urn:kora:kb:spec-md)); gobierna la redacción de este documento        |

---

## 3. Componentes Esenciales

> Esta sección define formalmente los 5 componentes de §1.2. Las propiedades aquí declaradas son invariantes — toda instanciación (§4) **DEBE** preservarlas.

### 3.1 El Morfismo de Transición c

**Definición:** c es el comportamiento del agente, formalizado como una FSM donde los estados son objetos categóricos y las transiciones son morfismos puros.

**Propiedades:**
1. **Determinismo en M:** dado un estado u ∈ U y un input i ∈ In, el siguiente estado c(u, i) es único dentro de la mónada M. Si M = Identity, la transición es determinista pura. Si M = Powerset, se permite no-determinismo acotado.
2. **Composicionalidad:** los morfismos componen asociativamente — una cadena de transiciones S₁ → S₂ → S₃ es equivalente a su composición directa S₁ → S₃.
3. **Co-inducción:** los nodos terminales de la FSM **DEBEN** evaluar y auto-corregir el output antes de entregarlo. El agente no termina sin verificación.

**Correcto:** `La FSM define: STATE: S-INIT → ACT: Clasificar. → Trans: IF legal → S-LEGAL. Cada transición es un morfismo puro sin prosa fenomenológica.`
**Incorrecto:** `La FSM mezcla: "Soy un analista apasionado. STATE: S-INIT → Clasificar." La narrativa de personalidad contamina el morfismo.`

### 3.2 El Funtor de Interfaz F

**Definición:** F define el tipado de inputs y outputs del agente. Para un agente reactivo, F(U) = (Out × U)^In — dado un input, el agente produce un output y un nuevo estado.

**Propiedades:**
1. **Álgebra cerrada:** toda herramienta (tool) disponible para el agente **DEBE** tener su firma inferencial declarada en F. El agente no **DEBE** invocar herramientas no declaradas.
2. **Semántica, no implementación:** F describe QUÉ acciones existen y QUÉ tipos aceptan/retornan, no CÓMO se implementan.
3. **Herencia en sub-agentes:** cuando un agente maestro instancia un sub-agente, F se hereda completo — el sub-agente opera con las mismas herramientas que el maestro.

**Correcto:** `F declara: "search_kb(query: string) → results: KBEntry[]". Firma tipada, sin implementación.`
**Incorrecto:** `F contiene: "Para buscar, usa curl https://api... con headers X-Auth". Detalle de implementación dentro de la interfaz.`

### 3.3 El Espacio de Estados U

**Definición:** U es el estado interno del agente, descomponible como producto de **fibras** ortogonales: U = Π(fibras). Cada fibra es independientemente evaluable y segregable.

**Fibras estándar:**

| Fibra                | Contenido                                    | Participación en sub-agentes |
|----------------------|----------------------------------------------|------------------------------|
| Fenomenológica       | Personalidad, tono, arquetipo, posicionamiento | **NO** — se disipa            |
| Contexto operador    | Perfil, rutinas, preferencias del usuario     | **NO** — solo sesión main     |
| Episódica (opcional) | Memoria, historia, logs de sesiones previas   | Según plataforma             |
| Estática (opcional)  | Metadata de identidad, clasificación, versión | Según plataforma             |

**Propiedades:**
1. **Completitud:** U **DEBE** contener toda la información necesaria para que c produzca el output correcto.
2. **Ortogonalidad:** las fibras son independientes — modificar la fibra fenomenológica no afecta el comportamiento de c.
3. **Segregabilidad:** cada fibra **PUEDE** materializarse como un artefacto separado sin pérdida de información.

**Correcto:** `La fibra fenomenológica declara: "Tono clínico e implacable. Prioriza diagnóstico." Sin lógica de transición.`
**Incorrecto:** `La fibra fenomenológica contiene: "IF consulta_urgente → priorizar_respuesta." Lógica FSM en fibra cualitativa.`

### 3.4 La Mónada de Efectos M

**Definición:** M encapsula las constraints computacionales del agente — seguridad, sandboxing, políticas de herramientas, límites de red. El update de c vive en Kl(M): las transiciones producen estados envueltos en M, no estados puros.

**Tipos de M según runtime:**

| Mónada       | Efecto                          | Ejemplo en agentes                           |
|--------------|---------------------------------|----------------------------------------------|
| Identity     | Puro (sin restricciones extra)  | Agente de prueba sin sandboxing              |
| Writer       | Con logging/traza               | Agente con auditoría obligatoria             |
| Powerset     | No-determinístico               | Agente que genera múltiples alternativas     |
| Distribution | Estocástico                     | Agente con muestreo probabilístico           |

**Propiedades:**
1. **Inmutabilidad desde el LLM:** M **DEBE** ser pre-compilada por el runtime. El LLM **NO DEBE** modificar sus propias constraints de seguridad en runtime.
2. **Precedencia ejecutiva:** las restricciones de M prevalecen sobre cualquier instrucción en c o en la conversación.
3. **Transparencia:** M **DEBE** ser declarativa — el agente puede leer sus constraints pero no alterarlas.

**Correcto:** `M pre-compila: {"allowed_kb": ["urn:gn:kb:protocolo-seguridad"], "sandbox": {"mode": "strict"}}. c no menciona políticas de acceso.`
**Incorrecto:** `c contiene: "Tienes acceso a protocolo-seguridad y ley-21180." Políticas de sandbox embebidas en la FSM.`

### 3.5 El Diagrama de Wiring W

**Definición:** W especifica cómo el agente se compone con otros agentes. Es un morfismo en la categoría de wiring diagrams WD que conecta outputs de un agente con inputs de otro.

**Propiedades:**
1. **Composicionalidad:** el comportamiento del sistema compuesto **DEBE** ser calculable desde sus componentes y W. No se requiere inspeccionar el estado interno de cada sub-agente.
2. **Adjunciones para sub-agentes:** la instanciación de un sub-agente se modela como adjunción Left ⊣ Right, donde el maestro (Left) delega y el esclavo (Right) ejecuta.
3. **Asimetría de contexto:** al componer, c y F se heredan; las fibras fenomenológica y de contexto operador se disipan. El sub-agente hereda la lógica pero no la personalidad.

**Correcto:** `W declara en c: "ACT: Delegar análisis a sub-agente-legal. Hereda: FSM, TOOLS. Disipa: SOUL, USER." Composición explícita.`
**Incorrecto:** `W no se declara. El agente invoca sub-agentes ad-hoc sin especificar qué contexto heredan.`

---

## 4. Instanciación: Topología de Workspace

### 4.1 Principio de Derivación

La topología de archivos es una **materialización física** de los 5 componentes esenciales de §3. No es un postulado independiente — se DERIVA de la descomposición categórica. Toda topología válida **DEBE** materializar los 5 componentes; **PUEDE** materializar cada uno en uno o más archivos.

### 4.2 Esquema Canónico KORA

| Componente §3           | Archivo         | Justificación                                           |
|--------------------------|-----------------|--------------------------------------------------------|
| c — Morfismo de transición (§3.1) | AGENTS.md       | FSM aislada como grafo de control puro                 |
| F — Funtor de interfaz (§3.2)     | TOOLS.md        | Semántica de herramientas segregada del control         |
| U — Fibra fenomenológica (§3.3)   | SOUL.md         | Personalidad aislada de la lógica algorítmica           |
| U — Fibra contexto operador (§3.3) | USER.md         | Contexto operador, solo inyectado en sesión main       |
| M — Mónada de efectos (§3.4)      | config.json     | Policies pre-compiladas, inmutables desde el LLM        |
| Endofuntores sobre U              | skills/CM-*.md  | Modelos cognitivos bajo evaluación diferida              |
| W — Diagrama de wiring (§3.5)     | Declarado en AGENTS.md | No requiere archivo propio; vive en los morfismos de c |

IDENTITY.md es **OPCIONAL**: fibra estática de U para plataformas que requieren separar metadata de identidad (nombre, versión, clasificación) de fenomenología (personalidad, tono).

```text
/agents/{nombre-del-agente}/
├── AGENTS.md        ← c (morfismo de transición)
├── SOUL.md          ← U, fibra fenomenológica
├── USER.md          ← U, fibra contexto operador
├── TOOLS.md         ← F (funtor de interfaz)
├── config.json      ← M (mónada de efectos)
└── skills/          ← endofuntores sobre U
    ├── CM-evaluador.md
    └── CM-analisis-normativo.md
```

### 4.3 Extensiones de Plataforma

Un runtime **PUEDE** extender la topología canónica con archivos adicionales que materialicen capacidades específicas de la plataforma. Cada extensión **DEBE** mapearse a exactamente un componente de §3.

**Ejemplo — extensión tipo OpenClaw:**

| Archivo extensión | Componente §3 | Propósito                                              |
|-------------------|---------------|--------------------------------------------------------|
| HEARTBEAT.md      | c (extensión) | Checklist periódico ejecutado por la FSM en heartbeats |
| MEMORY.md         | U, fibra episódica | Memoria curada de largo plazo, inyectada en main      |
| memory/           | U, fibra episódica | Logs diarios, acceso on-demand via search              |
| BOOTSTRAP.md      | c (efímero)   | Ritual de primer arranque, auto-destruible             |
| hooks/            | M (extensión) | Event handlers pre/post transición                     |

Estas extensiones **NO** forman parte del esquema canónico KORA. Un agente **DEBE** ser válido sin ellas (§4.4 criterio 4).

### 4.4 Regla de Validez

Una topología es válida sii cumple los 4 criterios:

1. **Completitud:** materializa los 5 componentes de §3.
2. **Exclusividad:** cada archivo pertenece a exactamente un componente.
3. **Compatibilidad:** las extensiones no violan invariantes de §8.
4. **Autonomía de c:** la FSM (AGENTS.md) es evaluable sin archivos de extensión — si HEARTBEAT.md, MEMORY.md o hooks/ faltan, c sigue operando correctamente.

---

## 5. Segregación de Contexto

La arquitectura KORA postula que la eficiencia de inferencia de un LLM depende de aislar qué información opera funcionalmente como motor sistémico y qué información opera como matiz identitario.

### 5.1 FSM y Leyes de Composición (AGENTS.md)

`AGENTS.md` **DEBE** operar como el grafo de control categórico aislado. Gobernado por el rigor de [KORA/Spec-MD](urn:kora:kb:spec-md), **DEBE** definir:

1. **La Categoría FSM:** Estados iniciales, terminales y transiciones puras gobernadas por lógica de rama (ej. `IF condición -> S-TARGET`).
2. **Funtores de Orquestación:** Lógica explícita de adjunción para instanciar sub-agentes paralelos o delegar cálculos pesados (Skills).
3. **Morfismos de Evaluación:** Nodos terminales condicionales que fuerzan auto-corrección (co-inducción) antes del output final.

`AGENTS.md` **NO DEBE** contener la narrativa dialéctica de la personalidad del agente. Mezclar control de flujo (lógica formal) con características interpretativas de personalidad es una aberración procedimental.

**Correcto:**

```markdown
## 1. FSM
1. STATE: S-INIT → ACT: Clasificar intención. → Trans: IF legal → S-LEGAL.
```

**Incorrecto:**

```markdown
## 1. FSM
Soy un analista apasionado por los datos. Cuando recibo una consulta...
1. STATE: S-INIT → ACT: Clasificar intención.
```

### 5.2 Fenomenología y Posicionamiento (SOUL.md)

El archivo `SOUL.md` **DEBE** definir exclusivamente el tono, arquetipo, prejuicios analíticos y posicionamiento del sistema. Todo aspecto fenoménico del agente reside aquí. Dado que los procesos delegados (Sub-agentes efímeros) o tareas en lote prescinden funcionalmente de la "identidad", `SOUL.md` **NO DEBE** hospedar rutinas lógicas, comprobaciones matemáticas o leyes vitales de validación.

**Correcto:** `SOUL.md declara: "Tono clínico e implacable. Prioriza diagnóstico sobre cortesía."`
**Incorrecto:** `SOUL.md declara: "IF consulta_urgente → priorizar_respuesta_rápida" (lógica FSM en archivo fenomenológico).`

### 5.3 Mónada de Efectos (config.json)

`config.json` materializa el componente M (§3.4). El agente encapsulado (LLM) **NO DEBE** administrar su propio confinamiento. Toda regla sobre qué KBs puede montar, qué herramientas puede invocar o qué límites de red aplican **DEBE** pre-existir compilada estáticamente en `config.json`.

**JSON Schema:**

```json
{
  "type": "object",
  "required": ["allowed_kb", "sandbox"],
  "properties": {
    "allowed_kb": {
      "type": "array",
      "items": { "type": "string", "pattern": "^urn:" },
      "description": "URNs de KBs accesibles por el agente"
    },
    "sandbox": {
      "type": "object",
      "required": ["mode"],
      "properties": {
        "mode": { "enum": ["strict", "permissive", "off"] }
      }
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
    }
  }
}
```

**Invariante:** `config.json` es inmutable desde el LLM. Las restricciones declaradas en M prevalecen sobre cualquier instrucción en c (§8.2).

**Correcto:** `config.json pre-compila: {"allowed_kb": ["urn:gn:kb:protocolo-seguridad"]}. AGENTS.md no menciona la política de acceso.`
**Incorrecto:** `AGENTS.md contiene: "Tienes acceso a las bases: protocolo-seguridad, ley-21180". La FSM mezcla política de sandboxing con lógica de transición.`

### 5.4 Contexto del Operador (USER.md)

`USER.md` materializa la fibra de contexto operador de U (§3.3). **DEBE** definir exclusivamente el perfil, las rutinas y las preferencias del operador humano.

**Grammar — Secciones obligatorias:**

1. **Perfil:** rol profesional, área de expertise, contexto organizacional.
2. **Rutinas:** horarios, patrones de trabajo, flujos recurrentes.
3. **Preferencias de Output:** formato preferido (markdown, tablas, bullets), idioma, nivel de detalle.

**Invariantes:**
- `USER.md` **NO DEBE** contener lógica algorítmica, restricciones de seguridad ni instrucciones de personalidad del agente.
- `USER.md` **NO DEBE** inyectarse en sesiones de sub-agentes; su alcance es estrictamente la sesión *Main*.

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

### 5.5 Funtor de Interfaz (TOOLS.md)

`TOOLS.md` materializa el componente F (§3.2). **DEBE** declarar la semántica operacional de cada herramienta disponible para el agente, otorgando al LLM los tipos y firmas inferenciales necesarios para interactuar con funtores externos.

**Grammar — Por cada herramienta:**

1. **Nombre:** identificador de la herramienta.
2. **Firma inferencial:** tipos de input y output.
3. **Cuándo usar:** condiciones bajo las cuales la FSM invoca esta herramienta.
4. **Cuándo NO usar:** restricciones explícitas de uso.

**Invariantes:**
- `TOOLS.md` describe semántica, **NO** implementación. No contiene endpoints, API keys ni detalles de deployment.
- `TOOLS.md` se inyecta en sesión main **Y** en sub-agentes (F se hereda).

**Template:**

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-tools:{version}"
  type: "bootstrap_tools"
---
## {nombre_herramienta}
- **Firma:** {input_type} → {output_type}
- **Cuándo usar:** {condición de invocación}
- **Cuándo NO usar:** {restricción}
- **Notas:** {observaciones operacionales}
```

**Correcto:** `TOOLS.md declara: "search_kb(query: string) → KBEntry[]. Usar cuando se necesite información de la KB. NO usar para búsquedas web."`
**Incorrecto:** `TOOLS.md contiene: "curl -H 'Authorization: Bearer xxx' https://api.internal/search". Detalle de implementación en vez de semántica.`

### 5.6 Modelos Cognitivos (skills/CM-*.md)

Los archivos `CM-*.md` en `skills/` materializan endofuntores cognitivos sobre U. Son procesos aislados, computacionalmente densos, convocados exclusivamente bajo evaluación diferida (*Lazy Load*).

**Grammar — Secciones obligatorias:**

1. **Propósito:** qué transformación cognitiva realiza este CM.
2. **Input/Output:** qué recibe del estado actual y qué produce.
3. **Procedimiento:** pasos del proceso cognitivo.
4. **Signature Output:** formato esperado del resultado.

**Invariantes:**
- Un CM **DEBE** residir en `skills/`. No puede estar inline en AGENTS.md.
- Un CM se carga **solo** cuando la FSM lo invoca explícitamente (Lazy Evaluation).
- Todo CM referenciado en AGENTS.md **DEBE** existir como archivo en `skills/`.
- Un CM **NO DEBE** contener lógica de transición de la FSM. Es un endofuntor puro.

**Template:**

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-cm-{id}:{version}"
  type: "lazy_load_endofunctor"
---
## Propósito
{Qué transformación cognitiva realiza.}
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
**Incorrecto:** `AGENTS.md contiene inline 200 líneas de un árbol de análisis legal embebido en el bootstrap.`

---

## 6. Endofuntores Cognitivos (*Lazy Load*)

Procesos como árboles analíticos densos o rutinas lógicas pesadas encarnan transformaciones complejas en la ruta del agente. Estos **NO DEBEN** evaluarse estáticamente en la inicialización (el *bootstrap*).

1. Todo Modelo Cognitivo (CM) o razonamiento procesal extenso **DEBE** ser modelado categóricamente como un endofuntor, escindido del morfismo base `AGENTS.md` y formalizado como un archivo individual dentro del subdirectorio `skills/`.
2. La instrucción residente en `AGENTS.md` **DEBE** forzar evaluación diferida (*Lazy Evaluation*); el LLM invoca dicho *Skill* explícitamente mediante *tool calls* únicamente cuando el nodo (Estado) actual dicte la necesidad operatoria.

**Correcto:** `AGENTS.md: "ACT: Evaluar riesgo usando skill CM-analisis-legal." El CM reside en skills/ y se carga on-demand.`
**Incorrecto:** `AGENTS.md contiene inline 200 líneas de un árbol de análisis legal embebido en el bootstrap.`

---

## 7. Orquestación y Adjunciones

La arquitectura KORA soporta el diseño de Sistemas Multi-Agente (SMA) modelándolos categóricamente como funtores adjuntos. El componente W (§3.5) se materializa como declaraciones de adjunción dentro de AGENTS.md, no como archivo separado.

1. Todo Agente Maestro (Functor Left) **DEBE** declarar sus reglas de instanciación hacia sub-agentes (Functor Right) en los morfismos de transición de su `AGENTS.md`. Esta declaración constituye el diagrama de wiring W del agente.
2. Toda sesión de sub-agente engendrada **DEBE** operar bajo asimetría pura de contexto: heredará imperativamente c (`AGENTS.md`) y F (`TOOLS.md`) para garantizar el encuadre matemático, pero las fibras fenomenológica (`SOUL.md`) y de contexto operador (`USER.md`) **NO DEBEN** transferirse, preservando Token Economy y aislamiento computacional.
3. W **DEBE** declarar explícitamente qué componentes hereda cada sub-agente. La omisión de esta declaración viola la composicionalidad (§3.5 propiedad 1).

---

## 8. Invariantes Topológicos

### 8.1 Evaluabilidad bajo Asimetría

Todo morfismo validado en `AGENTS.md` **DEBE** formularse pura e independientemente. Su ejecución cíclica **DEBE** retornar exitosamente sin generar excepciones nulas aun si todos los artefactos fenoménicos (`SOUL.md`, `USER.md`) fallan de inyectarse en el ensamble computacional de turno.

**Correcto:** `AGENTS.md ejecuta su FSM completa (S-INIT → S-EVAL → S-END) sin errores aunque SOUL.md y USER.md no estén presentes.`
**Incorrecto:** `AGENTS.md tiene: "IF user_prefers_formal → S-FORMAL". Transición depende de USER.md; si USER.md falta, la FSM falla.`

### 8.2 Conservación de Perímetros (Limit Preservation)

Toda evaluación matemática en `AGENTS.md` asume la inmutabilidad dura de su confinamiento. Las políticas imperativas sancionadas en el Límite (`config.json` o capa base del O.S.) **DEBEN** tener precedencia ejecutiva irrefutable sobre cualquier instrucción insertada en los nodos conversacionales del LLM.

## 9. Verificación

| Check                    | Criterio                                                                       | Acción si falla                  |
| ------------------------ | ------------------------------------------------------------------------------ | -------------------------------- |
| Segregación Topológica   | `config.json` y archivos `.md` base en raíz del workspace                      | Crear elementos faltantes        |
| FSM como Morfismos Puros | `AGENTS.md` contiene solo nodos y transiciones; cero prosa fenomenológica      | Trasladar narrativa a `SOUL.md`  |
| Autonomía Lógica         | La FSM no evalúa condicionantes basados en variables de `SOUL.md` o `USER.md`  | Redirigir dependencias al núcleo |
| Endofuntores Aislados    | Todo CM reside en `skills/`; no contamina el bootstrap                         | Extirpar CM hacia `skills/`      |
| Seguridad Determinista   | Política RAG/Sandboxing en `config.json`, no en lenguaje natural               | Trasladar al runtime (JSON/CLI)  |
| Contexto del Operador    | `USER.md` existe, sin lógica FSM, no inyectado en sub-agentes                  | Segregar contenido               |
| Completitud Topológica   | Workspace contiene todos los archivos obligatorios de §4.2                     | Crear archivos faltantes         |
| TOOLS.md completo        | Cada herramienta tiene nombre, firma, cuándo usar/no usar (§5.5)               | Completar entradas faltantes     |
| config.json válido       | Parsea contra JSON Schema de §5.3                                              | Corregir schema                  |
| CM en skills/            | Todo CM referenciado en AGENTS.md existe como archivo en `skills/`              | Crear CM faltante                |
| CM grammar               | Cada CM tiene: Propósito, I/O, Procedimiento, Signature Output (§5.6)          | Completar secciones faltantes    |
| Wiring declarado         | Si AGENTS.md instancia sub-agentes, W declara herencia explícita (§7)          | Agregar declaración de herencia  |

---

## 10. Ejemplo

### 10.1 Workspace Bien Formado

```text
/agents/analista-legal/
├── AGENTS.md      ← c: FSM pura, estados, transiciones, wiring W
├── SOUL.md        ← U fibra fenomenológica: tono, arquetipo
├── USER.md        ← U fibra contexto: perfil operador (solo main)
├── TOOLS.md       ← F: firmas inferenciales de herramientas
├── config.json    ← M: sandboxing pre-compilado, allowed_kb
└── skills/
    ├── CM-evaluador-riesgo.md    ← endofuntor lazy
    └── CM-analisis-normativo.md  ← endofuntor lazy
```

Propiedades: 5 componentes materializados (§4.4 criterio 1), AGENTS.md sin prosa fenomenológica, CMs en skills/ con carga diferida, config.json inmutable, TOOLS.md con firmas tipadas.

### 10.2 Workspace Mal Formado

```text
/agents/analista-legal/
├── AGENTS.md      ← Contiene personalidad + FSM mezcladas
├── config.json    ← Modificado por el LLM en runtime
└── CM-evaluador.md ← CM suelto en raíz (fuera de skills/)
```

Violaciones: segregación violada (§5.1/§5.2), SOUL/USER/TOOLS ausentes (§4.4 criterio 1), CM fuera de topología (§5.6), inmutabilidad violada (§5.3).

---

## 11. Template (Esqueleto Mínimo)

```text
/agents/{nombre-del-agente}/
├── AGENTS.md       ← c (obligatorio)
├── SOUL.md         ← U fibra fenomenológica (obligatorio)
├── USER.md         ← U fibra contexto (obligatorio)
├── TOOLS.md        ← F (obligatorio)
├── config.json     ← M (obligatorio)
├── IDENTITY.md     ← U fibra estática (OPCIONAL)
└── skills/
    └── CM-{nombre}.md  ← endofuntores (si aplica)
```

> Los archivos internos de un workspace siguen un frontmatter simplificado conforme al schema de bootstrap, no el schema completo de KORA/Spec-MD. Los templates de §5.4-§5.6 definen la grammar de cada archivo.

**AGENTS.md** (c — §5.1):

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-agents:{version}"
  type: "bootstrap_agents"
---
## 1. Máquina de Estados (FSM)
1. STATE: S-INIT → ACT: {acción}. → Trans: IF {cond} → S-{TARGET}.
2. STATE: S-{TARGET} → ACT: {acción}. → Trans: IF {cond} → S-END.

## 2. Reglas Duras
- {Restricción de seguridad o formato}.

## 3. Adjunciones (W)
- Sub-agente: {nombre}. Hereda: AGENTS.md, TOOLS.md. Disipa: SOUL.md, USER.md.
```

**SOUL.md** (U fibra fenomenológica — §5.2):

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-soul:{version}"
  type: "bootstrap_soul"
---
## Identidad Dialéctica
{Rol y posicionamiento.}
## Tono
{Arquetipo y estilo comunicativo.}
```

**TOOLS.md** (F — §5.5):

```markdown
---
_manifest:
  urn: "urn:{namespace}:agent-bootstrap:{nombre}-tools:{version}"
  type: "bootstrap_tools"
---
## {nombre_herramienta}
- **Firma:** {input_type} → {output_type}
- **Cuándo usar:** {condición de invocación}
- **Cuándo NO usar:** {restricción}
```

**config.json** (M — §5.3):

```json
{
  "allowed_kb": ["urn:{namespace}:kb:{id}"],
  "sandbox": { "mode": "strict" },
  "tools": { "allow": [], "deny": [] },
  "sub_agents": { "max_depth": 1, "max_concurrent": 3 }
}
```

**USER.md** (U fibra contexto — §5.4) y **skills/CM-*.md** (endofuntores — §5.6): ver templates en sus respectivas secciones.
