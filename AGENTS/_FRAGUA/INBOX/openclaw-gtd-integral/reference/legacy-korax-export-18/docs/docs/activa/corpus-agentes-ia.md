# Corpus Agentes IA — Documento Consolidado

> **URN:** `urn:knowledge:koda:core:corpus-agentes:1.0.0`
> **Fecha:** 2026-02-25
> **Fuentes:** 8 documentos (agent_01–04 + skill_00–03)

---

## Parte I — Fundamentos Conceptuales

### 1. El Paradigma del Agente IA

La IA evolucionó de sistemas predictivos pasivos (responden a prompts) hacia el **paradigma agéntico**: software capaz de **razonar, planificar y actuar de forma autónoma** para alcanzar un objetivo.

Un Agente IA no es "solo un LLM". Es una **aplicación completa orientada a objetivos**.

#### Anatomía Canónica (convergencia Google / Anthropic / OpenAI)

| Pilar | Alias | Rol |
|---|---|---|
| El Modelo | "El Cerebro" | Motor de razonamiento (Claude, GPT, Gemini) |
| Las Herramientas | "Las Manos" | Conexión determinista con el mundo real (APIs, RAG, código) |
| Capa de Orquestación | "El Sistema Nervioso" | Ciclo Think → Act → Observe; gestiona estado y planificación |
| Entorno de Ejecución | "El Cuerpo" | Servicios de producción, identidad, logs (Agent Ops) |

#### Diferencia clave: Automation vs. Agente

- **Automation tradicional:** El desarrollador ("bricklayer") escribe lógica explícita (`if A → B`). LLM = nodo estático.
- **Agente:** El desarrollador actúa como "director". Define reglas, provee herramientas y contexto. El agente planifica el camino autónomamente.

---

### 2. Taxonomía de Madurez Agéntica (5 Niveles)

| Nivel | Nombre | Capacidad |
|---|---|---|
| 0 | Sistema de Razonamiento Core | LLM aislado. Sin herramientas. "Ciego" a tiempo real. |
| 1 | Solucionador Conectado | Conectado a herramientas. RAG, APIs simples, tareas de un paso. |
| 2 | Planificador Estratégico | Multi-paso. Ingeniería de contexto activa. ReAct. |
| 3 | Sistema Multi-Agente Colaborativo | Agentes especialistas coordinados. Se tratan mutuamente como herramientas. |
| 4 | Sistema Auto-Evolutivo | Crea herramientas y subagentes al vuelo. Aprende experimentalmente. |

---

### 3. Perspectivas por Vendor

**Google / OpenClaw**
- Ciclo de 5 pasos: *Get Mission → Scan Scene → Think it Through → Take Action → Observe and Iterate*
- Unidad operacional de 4 piezas: **Workspace** (bootstrap files), **Agent Dir** (auth aislado), **Config/Gateway** (declarativo), **Identity Runtime** (snapshot por sesión)
- Distingue: **Tools** (acción) vs **Skills** (instrucciones on-demand de cómo combinar herramientas)

**Anthropic**
- Énfasis en el contraste determinismo (herramientas) vs no-determinismo (agente)
- "Ingeniería de Contexto" severa por sobre autonomía descontrolada
- Pionero en estandarización: **Model Context Protocol (MCP)**

**OpenAI**
- Énfasis en **Function Calling** y **Handoffs**: agente orquestador transfiere contexto a especialistas
- Responses API (reemplaza Assistants API desde 2025)
- Skills en Codex (GPT-5.3): paquetes reutilizables de instrucciones + scripts + recursos

**Google Gemini CLI**
- **Subagentes**: especialistas contratados por el agente principal con context window independiente y herramientas restringidas — ahorra tokens, permite paralelismo real

---

## Parte II — Diseño y Arquitectura

### 4. El Nuevo Paradigma de Desarrollo: Dirección vs. Albañilería

El principio fundamental: **las herramientas son contratos deterministas para un sistema no determinista**.

- El comportamiento del agente varía (puede consultar clima, buscar web, preguntar al usuario)
- El resultado de la herramienta `getWeather("NYC")` siempre debe ser idéntico

### 5. Agente Único: Componentes de Diseño

**Ingeniería de Contexto**
- *Memoria a Corto Plazo*: scratchpad de la sesión actual
- *Memoria a Largo Plazo*: bases vectoriales RAG con historial y preferencias
- Ambas se empaquetan en el context window antes de cada llamada al LLM

**Ruteo de Modelos**
- Modelos rápidos/económicos (Flash, Haiku) → ruteo de intención, tareas triviales
- Modelos pesados (Opus, GPT-5, Gemini Pro) → planificación profunda, escritura compleja

### 6. Patrones Multi-Agente

| Patrón | Descripción | Cuándo usar |
|---|---|---|
| **Coordinador / Manager-Worker** | Manager divide tarea → especialistas → consolida | Tareas complejas con subtareas paralelas |
| **Secuencial (Assembly Line)** | Output de A = Input de B | Flujos lineales estrictos |
| **Evaluator-Optimizer** | Generador + Crítico iteran hasta calidad aceptable | Auditorías, código, compliance |
| **Human-in-the-Loop (HITL)** | Pausa deliberada para aprobación humana antes de acción de alto riesgo | Pagos, permisos masivos, envíos críticos |

### 7. Estructuras de Ruteo y Delegación

**Handoffs (OpenAI):** Un agente Triage único atiende todo, identifica semánticamente la necesidad y transfiere el control a un especialista pre-configurado.

**Multi-Agent Routing (OpenClaw):** Un Gateway único hospeda múltiples agentes aislados. Bindings declarativos enrutan mensajes *antes* de que toquen el LLM — sin costo de triage.

**Subagentes (Gemini / OpenClaw):** Worker temporal con context window aislado. El agente principal le pasa la tarea vía Tool Call. El subagente procesa asíncronamente y emite un "announce" con resultados filtrados. Permite paralelismo real sin contaminar el contexto principal.

**Agent2Agent (A2A):** Para flotas de cientos de agentes. "Agent Cards" (JSON con endpoint, credenciales, capacidades) permiten descubrimiento y comunicación asíncrona entre agentes de distintos vendors. Reemplaza APIs acopladas a mano.

---

## Parte III — Implementación y Herramientas

### 8. El Costo del Context Window

El context window es el recurso más escaso. Riesgos principales:

- **Esquemas de herramientas:** Cada herramienta activa inyecta un bloque JSON en el system prompt aunque no se llame → usar "Tool Profiles" para limitar las activas
- **Bootstrap files gigantes:** Anti-patrón. La información debe vivir en memoria a largo plazo, accesible on-demand. Los bootstrap files deben ser concisos.

### 9. Tipos de Extensión del Agente

| Tipo | Qué es | Riesgo | Ejemplo |
|---|---|---|---|
| **Tools** | Acciones directas (Browser, Exec, File System) | Medio | `web_search`, `exec` |
| **Plugins** | Código TS/JS que amplía el orquestador con nuevas APIs locales | Alto (determinista, alto privilegio) | Puentes a DBs internas |
| **Skills** | Archivos `SKILL.md` inyectados on-demand. Enseñan *cómo combinar* herramientas | Bajo | `coding-agent`, `gog`, `weather` |

### 10. Diseño de Herramientas para Agentes

Reglas de oro (a diferencia de APIs para sistemas deterministas):

- **Consolidar:** `get_customer_context` (un llamado) > `get_id` + `get_payments` + `get_history` (tres llamados)
- **Paginar:** `search_contacts(query)` > `list_contacts()` que devuelve 5.000 registros
- **Errores legibles:** El error debe decirle al agente *cómo corregir su llamada*, no un stack trace

### 11. Estandarización: Function Calling vs. MCP

**Function Calling (nativo OpenAI/Gemini):** Schema JSON al modelo → modelo devuelve JSON argumentado → código local ejecuta → devuelve resultado. Requiere "glue code" acoplado.

**Model Context Protocol (MCP):** "USB-C para agentes". La app levanta un servidor MCP local o remoto. El agente usa un cliente MCP para descubrir herramientas, prompts y recursos dinámicamente. Elimina acoplamiento directo. Complementario (no sustituto) de los Agent Skills.

---

## Parte IV — Agent Skills: Especificación Completa

### 12. Qué son los Agent Skills

**Agent Skills** es un estándar de formato abierto promovido desde `agentskills.io` (con apoyo de Anthropic). Permite extender las capacidades de agentes de forma **predecible, segura y portable**.

Operan bajo el paradigma de **Revelación Progresiva (Progressive Disclosure)**:

1. **Descubrimiento:** Solo se carga nombre + descripción (~100 tokens)
2. **Activación:** Match semántico → se inyecta el `SKILL.md` completo (<5.000 tokens)
3. **Ejecución:** El agente sigue las instrucciones, puede leer `references/` o ejecutar `scripts/`

### 13. Estructura de Directorios

```
nombre-del-skill/
├── SKILL.md          # (Obligatorio) Core: metadatos + instrucciones
├── scripts/          # (Opcional) Código ejecutable
├── references/       # (Opcional) Documentación prolija (se lee on-demand)
└── assets/           # (Opcional) Plantillas, esquemas, assets estáticos
```

### 14. El Archivo SKILL.md

#### Frontmatter YAML (obligatorio)

```yaml
---
name: nombre-del-skill           # 1-64 chars, minúsculas, solo guiones
description: |                   # 1-1024 chars — EL GATILLADOR SEMÁNTICO
  Qué hace y CUÁNDO usarlo (palabras clave explícitas).
license: Apache-2.0              # Opcional
compatibility: Requiere docker   # Opcional, <500 chars
metadata:
  author: koda-engineering
  version: "1.0"
allowed-tools: Bash(python:*) Read  # Opcional/experimental
---
```

**Regla crítica del `name`:** debe coincidir exactamente con el nombre de la carpeta. Solo minúsculas, guiones y alfanuméricos. Sin guiones al inicio/final ni consecutivos (`--`).

**Regla crítica del `description`:** Es el mecanismo de routing. Debe incluir la motivación Y los detonantes léxicos exactos para evitar falsos positivos.

❌ Malo: `Scripts para manipular texto.`

✅ Correcto: `Herramienta para auditorías gramaticales e ingesta de documentos legales (.doc, .pdf). Usar EXCLUSIVAMENTE cuando el usuario mencione auditorías normativas, contratos chilenos o pida extracción legal desde PDFs.`

#### Cuerpo del SKILL.md

Instrucciones prescriptivas en Markdown (<5.000 tokens). Estructura recomendada:

```markdown
## Flujo de Trabajo (Obligatorio)
Cuando se active esta habilidad, DEBES:
1. Validar entrada: `scripts/validate.py --json <data>`
2. Leer modelo base en `references/modelo_base.md`
3. Si paso 1 falla → notificar error exacto. NUNCA adivinar.
```

### 15. Carpetas Opcionales

**`scripts/`** — Sistema Nervioso Motor del skill. Reglas:
- Código **idempotente**: mismo resultado si se ejecuta N veces
- **Errores verbosos para el agente**: `[ERROR] Formato esperado: {...}. Corrige y reintenta.` — no `exit 1` silencioso
- Dependencias documentadas explícitamente

**`references/`** — Documentación que sobrecargaría el context si se cargara siempre. Solo se accede cuando el `SKILL.md` lo instruye. Ejemplos: especificaciones técnicas, tablas de error, manuales de dominio legal/médico.

**`assets/`** — Elementos estáticos sin lógica dinámica: plantillas, imágenes de arquitectura, esquemas JSON/YAML, bases de datos SQLite pequeñas. Preferir texto plano sobre PDFs.

### 16. Checklist de Validación de un Skill

- [ ] Nombre de directorio = valor `name` en frontmatter (minúsculas, solo guiones)
- [ ] `description` incluye casos de uso inconfundibles (gatilladores semánticos precisos)
- [ ] Cuerpo <5.000 tokens — lo que no se usa en 90% de casos va a `references/`
- [ ] Scripts: idempotentes, errores verbosos, dependencias documentadas
- [ ] Assets en formato texto/Markdown/JSON (no PDFs)
- [ ] Validado con `skills-ref validate ./mi-skill` (si disponible)
- [ ] Referencias internas usando rutas relativas estrictas

---

## Parte V — Interoperabilidad, Operaciones y Gobierno

### 17. Agent Ops: Evaluación en Sistemas Probabilísticos

Los tests unitarios clásicos (`output == expected`) fallan en agentes. Reemplazos:

**LLM as a Judge:** Un modelo poderoso evalúa el output del agente de desarrollo contra un *golden dataset* bajo una rúbrica: ¿Hubo alucinación? ¿Respetó el tono? ¿Usó las herramientas correctas?

**Trazabilidad (OpenTelemetry):** Se registra la "trayectoria" completa: prompt entrada → razonamiento interno → herramienta seleccionada → parámetros → output. Sin breakpoints en el LLM, las trazas son el único debugger.

### 18. Seguridad e Identidad

#### Triple capa de Principal (IAM)

| Principal | Autenticación | Responsabilidad |
|---|---|---|
| Usuario | OAuth / SSO | Máxima |
| Cuenta de servicio | IAM | Cero intención (determinista) |
| Agente | SPIFFE (criptográfico) | Delegada; estocástica; least privilege |

#### Aislamiento (modelo OpenClaw)

- Auth Isolation: credenciales no compartidas entre agentes → blast radius limitado si un agente es comprometido
- Cada agente: Workspace + AgentDir propios bajo un solo daemon

#### Guardrails

- **Deterministas:** Reglas de software duro en servidor (ej. no ejecutar pagos >$1.000 sin HITL)
- **Basados en razonamiento:** "Guard Model" ligero que escanea prompts contra Prompt Injection y filtra salidas para prevenir fuga de PII

### 19. Protocolos de Interoperabilidad (Estándares 2026)

| Protocolo | Propósito | Mecanismo |
|---|---|---|
| **MCP** | Conectar agente a fuentes de datos/herramientas | Cliente-servidor; descubrimiento dinámico de resources/tools/prompts |
| **A2A** | Comunicación agente-a-agente entre vendors | Agent Cards JSON; Tasks asíncronas (no Request/Response) |
| **AP2 / HTTP 402** | Economía agéntica; micropagos B2B | Mandatos criptográficamente firmados; sin fricción humana |

### 20. Control Plane: Evitando el Agent Sprawl

Cuando la organización despliega múltiples agentes con dependencias entrelazadas:

- Gateway central: punto único de auth, autorización, rate-limiting
- Registry interno (App Store): descubrir agentes disponibles, evitar duplicidad
- CI/CD formal con evaluaciones de seguridad pre-deploy

---

## Parte VI — Ecosistema 2026

### 21. Convergencia de la Industria

Q1 2026: la industria convergió de "Function Calling" simple (2023) hacia **composición modular (Skills)** y protocolos unificados (MCP). El núcleo ontológico compartido:

1. Todos exigen nombre + descripción semántica fuerte como detonador de invocación
2. Paso de argumentos siempre via JSON Schema tipado
3. Ciclo invariante: `Razonamiento → Tool Call → Resultado → Retorno al modelo`
4. Sandboxing de ejecución (Docker, subprocesos limitados)

### 22. Divergencias por Plataforma

| Plataforma | Enfoque | Particularidad Skills |
|---|---|---|
| **Anthropic** | Local-First | Claude lee `SKILL.md` en Markdown crudo sin conversión JSON. Progressive Disclosure pura. |
| **Google Gemini** | Cloud-First | Requiere OpenAPI Spec. SKILL.md en texto libre = desafío de parseo. Prefiere empaquetados firmados. |
| **OpenAI** | Cajas Negras / WebSockets | Skills via Responses API o instrucciones pre-insertadas. Esquema imperativo más que declarativo. |

### 23. Frameworks Multi-Modelo (LangChain / AutoGen / CrewAI)

2026: Sistemas Multi-Agente son la arquitectura empresarial por defecto (planners + executors + verifiers colaborando).

Cambio de paradigma:
- **Tool (2023):** Binario pasivo. "Calculadora".
- **Skill (2026):** Paquete completo de contexto. Código (`scripts/`) + explicación de cuándo usarlo (`references/`) + instrucciones de razonamiento (`SKILL.md`).

AutoGen Studio y CrewAI AMP adaptaron sus interfaces para ingerir y gobernar roles mapeando estos directorios de instrucciones a cada agente.

---

## Apéndice — Glosario Rápido

| Término | Definición |
|---|---|
| **Agent Card** | JSON que publica endpoint, credenciales y capacidades de un agente (protocolo A2A) |
| **Agent Sprawl** | Crecimiento descontrolado de agentes con dependencias entrelazadas |
| **Bootstrap Files** | Archivos inyectados permanentemente al contexto del agente (SOUL.md, AGENTS.md) |
| **Context Window** | Límite de tokens que el LLM puede procesar en una sola llamada |
| **Guardrails** | Mecanismos de control que limitan acciones del agente (deterministas o basados en razonamiento) |
| **HITL** | Human-in-the-Loop: pausa deliberada para aprobación humana |
| **Idempotente** | Propiedad de una función: mismo resultado si se ejecuta N veces |
| **LM as a Judge** | Usar un LLM poderoso para evaluar el output de otro agente contra una rúbrica |
| **MCP** | Model Context Protocol: estándar cliente-servidor para conectar agentes a fuentes de datos |
| **Progressive Disclosure** | Cargar solo lo necesario en cada momento para no saturar el context window |
| **RAG** | Retrieval-Augmented Generation: búsqueda semántica en base de datos vectorial para augmentar contexto |
| **SPIFFE** | Estándar de identidad criptográfica para agentes (Secure Production Identity Framework) |
| **Subagente** | Worker temporal con context window aislado, lanzado por el agente principal para una tarea específica |
