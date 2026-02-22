---
_manifest:
  urn: "urn:kora:kb:agent-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "KORA RAG-Native Standards"
version: "4.0.0"
status: published
tags: [spec, agent, architecture, fsm, llm-runtime]
lang: es
---

# KORA/Agent-Spec — Especificación Categórica de Agentes v4.0.0

## 1. Ontología Categórica del Agente

> Este documento es prescriptivo y **ESTÁ GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md). Reemplaza al schema YAML declarativo anterior (`agent.yml`) y a la especificación OpenClaw previa (`openclaw-agent-spec.md`), estableciendo el formalismo categórico como paradigma canónico.

**KORA/Agent-Spec** es la arquitectura fundacional que modela agentes LLM como **categorías rigurosas**. Abandona la definición procedimental (estilo Python/imperativo) a favor de una estructura declarativa y puramente funcional (estilo Haskell/categórico).

Bajo este estándar, un agente no es un script que ejecuta acciones paso a paso, sino un sistema dinámico definido por invariantes estructurales:
- **Objetos (Obj)**: Los Estados del sistema.
- **Morfismos (Morph)**: Las Transiciones deterministas entre estados.
- **Factores Límite (Lim)**: Los aislamientos de seguridad (`config.json`).
- **Funtores (F)**: Las invocaciones a sub-agentes o modelos cognitivos externalizados que preservan la estructura del contexto.

Para sostener este paradigma y maximizar la economía de tokens (Token Economy), todo agente **DEBE** materializarse mediante una **topología física segregada**. Esta topología aísla la lógica matemática (FSM) de la semántica cualitativa (Identidad), forzando evaluaciones diferidas (*Lazy Evaluation*) mediante funciones asimétricas.

---

## 2. Definiciones

La tabla de esta sección **DEBE** incluir todo término clave con significado preciso dentro de esta especificación:

**Correcto:** `El documento usa "FSM" y "Endofuntor"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "Adjunción" como término clave y no existe entrada para "Adjunción".`

| Término | Definición |
| --- | --- |
| **Workspace** | Directorio físico unitario que materializa un agente; morfismo identidad que acota la visibilidad del dominio funcional |
| **FSM** | Sistema dinámico que modela estados como objetos discretos y transiciones condicionales como morfismos puros |
| **Morfismo** | Transición determinista entre dos estados de la FSM; flecha en la categoría del agente |
| **Endofuntor** | Funtor de una categoría en sí misma; modela procesos cognitivos aislados que transforman el contexto preservando estructura |
| **Lazy Evaluation** | Evaluación diferida donde un recurso (CM, Skill) se invoca solo cuando el estado actual de la FSM lo requiere |
| **Sub-agente** | Categoría adjunta; ejecución esclava que hereda el esquema de control (FSM) pero disipa la fenomenología (SOUL) |
| **Factor Límite (Lim)** | Contrato estricto del *runtime* (`config.json`) que impone barreras físicas de red y aserción de restricciones |
| **Modelo Cognitivo (CM)** | Endofuntor cognitivo; proceso aislado, asíncrono y convocado bajo evaluación diferida pura |
| **Topología** | Disposición física obligatoria de archivos y directorios que materializa la segregación de contexto |
| **Segregación de Contexto** | Principio que aísla la lógica algorítmica (FSM) de la semántica cualitativa (Identidad) |
| **SMA** | Sistema Multi-Agente; red de agentes modelados como funtores adjuntos bajo orquestación categórica |
| **Adjunción** | Relación entre dos funtores (Left ⊣ Right) que modela la instanciación de sub-agentes por un agente maestro |
| **Funtor** | Mapeo entre categorías que preserva estructura (objetos→objetos, morfismos→morfismos, composición→composición) |
| **Token Economy** | Restricción de diseño que minimiza consumo de tokens por turn mediante segregación topológica y *Lazy Evaluation* |
| **KORA/Spec-MD** | Formato para documentos prescriptivos (ver [especificación](urn:kora:kb:spec-md)); gobierna la redacción de este documento |
| **Categoría** | Estructura algebraica: objetos, morfismos y leyes de composición asociativa con identidad |
| **Co-inducción** | Mecanismo de auto-corrección en nodos terminales de la FSM; el agente evalúa y corrige su output antes de entregarlo |

---

## 3. Primitivas Topológicas

| Primitiva                 | Rol Funcional Categórico                                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Workspace de Agente**   | El morfismo identidad del agente; contenedor físico unitario que acota la visibilidad del dominio funcional.                                                  |
| **FSM (Categorical FSM)** | Sistema dinámico que modela `Estados` como **Objetos** discretos y `Transiciones` condicionales como **Morfismos** puros.                                     |
| **AGENTS.md**             | El archivo núcleo. Actúa como la función declarativa principal que rige la FSM bajo las reglas invariables de [KORA/Spec-MD](urn:kora:kb:spec-md).            |
| **SOUL.md**               | El álgebra cualitativa. Define la instancia de personalidad y tono. **No** forma parte del grafo de control; es puramente fenomenológico.                     |
| **USER.md**               | Contexto fenoménico del operador. Define perfil, rutinas y preferencias del usuario. Inyectado solo en sesión *Main*; **NO** participa en sub-agentes. |
| **IDENTITY.md**           | Archivo de metadatos estáticos o "etiqueta type" (clasificación, versión).                                                                                    |
| **TOOLS.md**              | Semántica operacional. Otorga al LLM los tipos y firmas inferenciales para interactuar con funtores externos.                                                 |
| **config.json**           | Factor Límite (Limit). Contrato estricto del *runtime* que impone barreras físicas de red y aserción de restricciones (sandboxing).                           |
| **Modelo Cognitivo (CM)** | Un endofuntor cognitivo; un proceso aislado computacionalmente, asíncrono y convocado bajo evaluación diferida pura (*Lazy Load*).                            |
| **Sub-agente**            | Una categoría adjunta. Ejecución esclava que hereda la lógica base matemática (FSM) pero disipa la fenomenología (SOUL) para acelerar inferencia concurrente. |

## 4. Topología Estructural

Todo agente **DEBE** existir como un directorio único, organizado bajo una topología determinista. Todo *Workspace* **DEBE** contener en su raíz estrictamente los componentes base de inicialización y un subdirectorio dedicado a recursos intermitentes.

**Esquema Obligatorio:**
```text
/agents/nombre-del-agente/
├── AGENTS.md        (Lógica algorítmica y orquestación)
├── SOUL.md          (Arquetipo y fenomenología)
├── USER.md          (Contexto del operador: perfil, rutinas, preferencias)
├── IDENTITY.md      (Metadatos de red)
├── TOOLS.md         (Semántica de herramientas)
├── config.json      (Políticas de ejecución y seguridad)
└── skills/          (Módulos cognitivos bajo demanda)
    ├── CM-evaluador.md
    └── CM-analisis-normativo.md
```

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

### 5.3 Barreras de Seguridad Estricta (config.json)

El agente encapsulado (LLM) **NO DEBE** administrar recursivamente su propio confinamiento de estado base (Límite). Toda regla sobre qué bases de conocimiento (KB) puede montar o qué contenedores aislar **DEBE** pre-existir compilada estáticamente en el entorno o runtime como `config.json`. Instanciar listas "hard-codeadas" de acceso al conocimiento dentro de la FSM ensucia la pureza de la transición lógica e infla los costos con datos que la máquina operadora resolvería mejor sin intervención de LLM.

**Correcto:** `config.json pre-compila: {"allowed_kb": ["urn:gn:kb:protocolo-seguridad"]}. AGENTS.md no menciona la política de acceso.`
**Incorrecto:** `AGENTS.md contiene: "Tienes acceso a las bases: protocolo-seguridad, ley-21180". La FSM mezcla política de sandboxing con lógica de transición.`

### 5.4 Contexto del Operador (USER.md)

El archivo `USER.md` **DEBE** definir exclusivamente el perfil, las rutinas y las preferencias del operador humano. `USER.md` **NO DEBE** contener lógica algorítmica, restricciones de seguridad ni instrucciones de personalidad del agente. `USER.md` **NO DEBE** inyectarse en sesiones de sub-agentes; su alcance es estrictamente la sesión *Main*.

**Correcto:** `USER.md describe el rol profesional del usuario, sus horarios y preferencias de formato de output.`
**Incorrecto:** `USER.md contiene reglas de seguridad o transiciones de la FSM.`

## 6. Endofuntores Cognitivos (*Lazy Load*)

Procesos como árboles analíticos densos o rutinas lógicas pesadas encarnan transformaciones complejas en la ruta del agente. Estos **NO DEBEN** evaluarse estáticamente en la inicialización (el *bootstrap*).

1. Todo Modelo Cognitivo (CM) o razonamiento procesal extenso **DEBE** ser modelado categóricamente como un endofuntor, escindido del morfismo base `AGENTS.md` y formalizado como un archivo individual dentro del subdirectorio `skills/`.
2. La instrucción residente en `AGENTS.md` **DEBE** forzar evaluación diferida (*Lazy Evaluation*); el LLM invoca dicho *Skill* explícitamente mediante *tool calls* únicamente cuando el nodo (Estado) actual dicte la necesidad operatoria.

**Correcto:** `AGENTS.md: "ACT: Evaluar riesgo usando skill CM-analisis-legal." El CM reside en skills/ y se carga on-demand.`
**Incorrecto:** `AGENTS.md contiene inline 200 líneas de un árbol de análisis legal embebido en el bootstrap.`

## 7. Orquestación y Adjunciones

La arquitectura KORA soporta el diseño de Sistemas Multi-Agente (SMA) modelándolos categóricamente como functores adjuntos.

1. Todo Agente Maestro (Functor Left) **DEBE** declarar sus reglas de instanciación hacia sub-agentes (Functor Right) en los morfismos de transición de su `AGENTS.md`.
2. Toda sesión de sub-agente engendrada **DEBE** operar bajo asimetría pura de contexto: heredará imperativamente el esquema de control (`AGENTS.md` y `TOOLS.md`) para garantizar el encuadre matemático, pero las capas pasivas de identidad (`SOUL.md`) **NO DEBEN** transferirse, preservando la inviolabilidad computacional y mitigando costos superfluos.

## 8. Invariantes Topológicos

### 8.1 Evaluabilidad bajo Asimetría
Todo morfismo validado en `AGENTS.md` **DEBE** formularse pura e independientemente. Su ejecución cíclica **DEBE** retornar exitosamente sin generar excepciones nulas aun si todos los artefactos fenoménicos (`SOUL.md`, `USER.md`) fallan de inyectarse en el ensamble computacional de turno.

**Correcto:** `AGENTS.md ejecuta su FSM completa (S-INIT → S-EVAL → S-END) sin errores aunque SOUL.md y USER.md no estén presentes.`
**Incorrecto:** `AGENTS.md tiene: "IF user_prefers_formal → S-FORMAL". Transición depende de USER.md; si USER.md falta, la FSM falla.`

### 8.2 Conservación de Perímetros (Limit Preservation)
Toda evaluación matemática en `AGENTS.md` asume la inmutabilidad dura de su confinamiento. Las políticas imperativas sancionadas en el Límite (`config.json` o capa base del O.S.) **DEBEN** tener precedencia ejecutiva irrefutable sobre cualquier instrucción insertada en los nodos conversacionales del LLM.

## 9. Verificación

| Check | Criterio | Acción si falla |
| --- | --- | --- |
| Segregación Topológica | `config.json` y archivos `.md` base en raíz del workspace | Crear elementos faltantes |
| FSM como Morfismos Puros | `AGENTS.md` contiene solo nodos y transiciones; cero prosa fenomenológica | Trasladar narrativa a `SOUL.md` |
| Autonomía Lógica | La FSM no evalúa condicionantes basados en variables de `SOUL.md` o `USER.md` | Redirigir dependencias al núcleo |
| Endofuntores Aislados | Todo CM reside en `skills/`; no contamina el bootstrap | Extirpar CM hacia `skills/` |
| Seguridad Determinista | Política RAG/Sandboxing en `config.json`, no en lenguaje natural | Trasladar al runtime (JSON/CLI) |
| Contexto del Operador | `USER.md` existe, sin lógica FSM, no inyectado en sub-agentes | Segregar contenido |
| Completitud Topológica | Workspace contiene todos los archivos obligatorios de §4 | Crear archivos faltantes |

---

## 10. Ejemplo

### 10.1 Workspace Bien Formado

```text
/agents/analista-legal/
├── AGENTS.md      ← FSM pura: estados, transiciones, reglas duras
├── SOUL.md        ← Tono, arquetipo, posicionamiento
├── USER.md        ← Perfil del operador (solo sesión Main)
├── IDENTITY.md    ← Metadatos estáticos
├── TOOLS.md       ← Firmas inferenciales de herramientas
├── config.json    ← Sandboxing pre-compilado
└── skills/
    ├── CM-evaluador-riesgo.md
    └── CM-analisis-normativo.md
```

Propiedades: topología completa, AGENTS.md sin prosa fenomenológica, CMs en skills/ con carga diferida, config.json inmutable.

### 10.2 Workspace Mal Formado

```text
/agents/analista-legal/
├── AGENTS.md      ← Contiene personalidad + FSM mezcladas
├── config.json    ← Modificado por el LLM en runtime
└── CM-evaluador.md ← CM suelto en raíz
```

Violaciones: segregación violada (§5.1/§5.2), SOUL/USER/IDENTITY/TOOLS ausentes (§4), CM fuera de topología (§6), inmutabilidad violada (§5.3).

---

## 11. Template (Esqueleto Mínimo)

```text
/agents/{nombre-del-agente}/
├── AGENTS.md
├── SOUL.md
├── USER.md
├── IDENTITY.md
├── TOOLS.md
├── config.json
└── skills/
    └── CM-{nombre}.md
```

**AGENTS.md:**
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
```

**SOUL.md:**
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
