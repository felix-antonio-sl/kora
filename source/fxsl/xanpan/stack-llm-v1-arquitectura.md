# STACK::LLM v1.0

## Stack de Desarrollo para la Era de Asistencia por LLM

*La arquitectura de referencia para construir cualquier cosa — desde un inventario de kiosco hasta un enjambre de agentes — cuando los LLMs son tus co-desarrolladores*

Febrero 2026

---

## Índice

0. [Axiomas Fundacionales: Por qué estas tecnologías y no otras](#0-axiomas-fundacionales)
1. [Frontend: La Capa Visual](#1-frontend-la-capa-visual)
2. [Backend: La Capa Lógica](#2-backend-la-capa-lógica)
3. [Datos: La Capa de Persistencia](#3-datos-la-capa-de-persistencia)
4. [Infraestructura y Operaciones](#4-infraestructura-y-operaciones)
5. [Observabilidad](#5-observabilidad)
6. [Seguridad](#6-seguridad)
7. [El Flujo de Desarrollo AI-First](#7-el-flujo-de-desarrollo-ai-first)
8. [Context Engineering: La Nueva Disciplina](#8-context-engineering-la-nueva-disciplina)
9. [Capa de Agentes (cuando el proyecto lo requiere)](#9-capa-de-agentes-cuando-el-proyecto-lo-requiere)
10. [Stack Completo: La Tabla de Referencia](#10-stack-completo-la-tabla-de-referencia)
11. [Tres Perfiles de Proyecto](#11-tres-perfiles-de-proyecto)
12. [Conexión con el Corpus Xanpan::Agents (opcional)](#12-conexión-con-el-corpus-xanpanagents-opcional)

---

# 0. Axiomas Fundacionales

Este documento no es un catálogo de tecnologías favoritas. Cada decisión emerge de **seis axiomas** que reflejan cómo los LLMs realmente procesan y generan código. Aplican igual si estás construyendo un sistema de inventario para un kiosco, una plataforma SaaS, o un enjambre de agentes autónomos. Porque en los tres casos, tu co-desarrollador es un modelo de lenguaje.

Entender los axiomas es más importante que memorizar la tabla final. Las tecnologías cambiarán. Los axiomas sobrevivirán.

> 🧬 **AXIOMA 1: Tipado estático como guardrail cognitivo**
>
> Los sistemas de tipos no son solo herramientas para desarrolladores humanos: funcionan como una capa de validación que intercepta errores de generación antes de que alcancen runtime. TypeScript y Pydantic actúan como compiladores de cordura para el output del LLM. Un LLM que genera código sin tipos es un LLM sin barandillas al borde del precipicio.

> 🧬 **AXIOMA 2: Sobre-representación en entrenamiento como ventaja competitiva**
>
> Las tecnologías dominantes en GitHub (Python, TypeScript, React, PostgreSQL) están masivamente representadas en los datos de entrenamiento de todo LLM. Esto no es una preferencia estética: genera patrones de generación con menor tasa de error y mayor coherencia estructural. Elegir una tecnología nicho porque es "técnicamente superior" pero tiene 1/100 de la representación en training data es sabotear a tu co-desarrollador.

> 🧬 **AXIOMA 3: Declaratividad sobre imperatividad**
>
> Los LLMs generan código más correcto cuando describen un estado final deseado (SQL, React JSX, Tailwind, Terraform HCL) que cuando deben orquestar secuencias imperativas paso a paso. Esto explica por qué React supera a jQuery para generación, por qué Tailwind supera a CSS imperativo, y por qué SQL directo supera a query builders imperativos.

> 🧬 **AXIOMA 4: Contratos explícitos como límites de alucinación**
>
> JSON Schema, OpenAPI, Zod, Pydantic, y tipos estrictos definen los límites de lo que el modelo puede generar. Sin contratos, la creatividad del modelo se vuelve impredecibilidad. Cada endpoint, cada formulario, cada transformación de datos debe tener un contrato tipado. Es la diferencia entre pedir "parsea esto" (invitación a alucinar) y "valida contra este schema" (instrucción precisa).

> 🧬 **AXIOMA 5: Resiliencia como requisito arquitectónico, no como feature**
>
> Un sistema construido con asistencia de LLM sin tests, linting, CI y validación automática no es un sistema de producción. Es un demo. Los LLMs son no-deterministas: dos generaciones del mismo prompt pueden producir código diferente. Los guardrails (tipos, tests, lint, CI) convierten esa no-determinismo en un problema manejable.

> 🧬 **AXIOMA 6: Soberanía y control de costos**
>
> Self-hosting donde sea posible. Routing inteligente de modelos para controlar costos de desarrollo asistido. Dependencias mínimas de vendors con lock-in. Un stack que depende de un solo proveedor de LLM o cloud es un stack frágil.

---

# 1. Frontend: La Capa Visual

Ya sea un dashboard de inventario de kiosco, un portal de clientes, o la interfaz del Tablero Neural de Xanpan::Agents: todo es frontend. Y es frontend que un LLM va a ayudarte a generar, mantener y evolucionar.

## 1.1 Lenguaje y Framework Core

**TypeScript + React + Next.js (App Router)**

- **TypeScript** intercepta el 70-80% de los errores de generación más comunes: propiedades faltantes, tipos incompatibles, contratos rotos. Cuando un LLM genera un componente y el compilador rechaza `<Button onClick={handler} labell="Guardar" />`, ese typo se atrapa antes de que exista. Sin TypeScript, llega a producción.
- **React** es el framework con mayor representación en datos de entrenamiento (**Axioma 2**). Los LLMs han internalizado miles de patrones composicionales. Pides "un formulario de registro con validación" y recibes un componente funcional con hooks, estados y manejo de errores coherente. Con frameworks menos representados, recibes más alucinaciones estructurales.
- **Next.js App Router** unifica server components, server actions y routing. Los Server Actions son particularmente poderosos: eliminan la necesidad de APIs REST separadas para operaciones internas. Un formulario de "agregar producto al inventario" puede tener su lógica de validación, persistencia y redirect en el mismo archivo. Menos superficie = menos errores de generación = el LLM genera flujos completos con coherencia.

**Alternativa para sitios estáticos:** Astro cuando no necesitas interactividad rica. Un catálogo de productos de lectura, un blog, una landing page.

## 1.2 Estilos y Sistema de Diseño

**Tailwind CSS + Shadcn/UI**

- **Tailwind** convierte las decisiones de diseño en tokens textuales atómicos (**Axioma 3**). Cada clase es un token predecible. `className="flex items-center gap-2 text-sm font-medium text-gray-700"` — el LLM combina estas clases con la misma precisión con la que combina palabras en una oración. No hay cascada CSS que predecir, no hay especificidad que calcular, no hay archivos .css separados que mantener en coherencia.
- **Shadcn/UI** proporciona componentes accesibles y tipados que se copian directamente al proyecto. No es dependencia npm — es código tuyo que el LLM puede leer, modificar y extender. Un `<DataTable>` de Shadcn que necesitas personalizar para tu inventario de kiosco: el LLM lo modifica directamente porque está en tu repo, no escondido en node_modules.

## 1.3 Validación y Estado

**Zod** como capa de validación unificada:

- Un schema Zod definido una vez es ley en frontend Y backend. Para un inventario de kiosco: `const ProductSchema = z.object({ name: z.string().min(1), price: z.number().positive(), stock: z.number().int().nonnegative() })`. Ese schema valida el formulario, valida el Server Action, y genera el tipo TypeScript automáticamente. El LLM no puede inventar un campo `precio` cuando el schema dice `price`.
- **TanStack Query** para gestión de estado del servidor: caching, revalidación, y optimistic updates. Un LLM genera un hook de TanStack Query con mucha más fiabilidad que una solución custom de state management.

---

# 2. Backend: La Capa Lógica

## 2.1 Dos lenguajes, responsabilidades divididas

No es indecisión. Es especialización. Ambos lenguajes están masivamente representados en training data (**Axioma 2**) y el LLM genera código de alta calidad en ambos.

| Lenguaje | Rol | Cuándo |
|---|---|---|
| **TypeScript (Hono / tRPC / Next.js Server Actions)** | API de producto, lógica de negocio, BFF | Cuando el frontend es Next.js y quieres types compartidos end-to-end. Para la mayoría de proyectos web: CRUD, dashboards, inventarios. |
| **Python (FastAPI)** | Capa cognitiva, procesamiento de datos, ML, integración con LLMs | Cuando necesitas procesamiento pesado, integración con ecosistema ML/AI, o tool-calling para agentes. |

**Para proyectos simples** (inventario de kiosco, portal de gestión, SaaS básico): TypeScript full-stack con Next.js Server Actions es suficiente. No necesitas Python. Un solo lenguaje, tipos compartidos, zero API boilerplate.

**Para proyectos con capa cognitiva** (chatbots, agentes, procesamiento ML): Python con FastAPI para la lógica de agentes + TypeScript para el frontend. FastAPI genera automáticamente JSON Schema desde Pydantic, que es el formato que los LLMs consumen para tool-calling. La cadena `Pydantic Model → JSON Schema → Tool Definition` es nativa y sin fricción.

## 2.2 FastAPI: cuándo y por qué

FastAPI no es obligatorio para todo proyecto. Es obligatorio cuando necesitas:

- **Tool-calling para agentes:** La cadena Pydantic → JSON Schema → Tool es irremplazable.
- **APIs que otros sistemas consumen:** OpenAPI automático desde tipos Python. Documentación gratis.
- **Procesamiento de datos:** El ecosistema Python (pandas, numpy, scikit-learn) no tiene equivalente en TS.

Para un inventario de kiosco con CRUD simple, FastAPI es overkill. Server Actions de Next.js + Drizzle ORM + PostgreSQL resuelven sin salir de TypeScript.

## 2.3 Diseño de APIs y herramientas

Independientemente del lenguaje, cada endpoint y cada herramienta sigue los mismos principios:

- **Schema tipado para input Y output.** Zod en TS, Pydantic en Python. No `any`. Nunca.
- **Docstrings/JSDoc estructurados.** El LLM los lee para entender qué hace cada función cuando genera código que la llama.
- **Validación antes de ejecución.** Input validado contra schema antes de tocar la base de datos o un servicio externo.
- **Errores tipados.** No strings de error. Tipos de error que el frontend puede discriminar y manejar.

---

# 3. Datos: La Capa de Persistencia

## 3.1 Base de Datos

**PostgreSQL.** Sin excepciones para el 95% de los casos de uso.

- **Sobre-representación en training data** (**Axioma 2**): Los LLMs generan SQL para PostgreSQL con precisión notable. Queries complejas, CTEs, window functions, JSON operations: todo sale bien generado al primer intento con más frecuencia que con cualquier otra base.
- **pgvector** integrado nativamente para búsqueda vectorial cuando lo necesites. Empiezas con CRUD simple para tu inventario. Un día quieres búsqueda semántica ("muéstrame productos similares a X"). pgvector lo habilita sin migrar de base de datos. HNSW indexes para búsqueda aproximada de alta velocidad.
- **Es la base de datos, no una base de datos.** Almacena datos relacionales, JSON (jsonb), vectores (pgvector), full-text search, geospatial (PostGIS). No necesitas Redis para cache simple (tienen unlogged tables), no necesitas Elasticsearch para búsqueda básica (tienen tsvector), no necesitas una base vectorial separada (tienen pgvector hasta ~10M vectores).

**Para escalas masivas de vectores** (>10M): Qdrant, Pinecone, o Milvus como tier especializado.

## 3.2 ORM y Query Builders

- **TypeScript:** Drizzle ORM. Type-safe, cercano a SQL puro, excelente para generación por LLM (**Axioma 3**: declarativo). El LLM genera queries Drizzle que son casi SQL legible. Alternativa: Prisma si el equipo prioriza DX sobre cercanía a SQL.
- **Python:** SQLAlchemy 2.0 con el nuevo estilo de queries tipadas.

## 3.3 Embeddings y búsqueda vectorial (cuando lo necesites)

No todo proyecto necesita embeddings. Un inventario de kiosco no los necesita al día 1. Pero el stack debe permitir añadirlos sin reescritura:

- **Abstracción obligatoria:** Si decides usar embeddings, una interfaz común (`EmbeddingProvider`) que permita intercambiar modelos. Almacenar siempre el `model_id` junto al vector.
- **Modelos recomendados:** OpenAI text-embedding-3-small/large como default. Cohere embed-v4 o Nomic embed como fallback open-source (soberanía, **Axioma 6**).
- **Estrategia de migración:** Re-indexación progresiva en background cuando se cambia de modelo. Dual-read durante transición.

## 3.4 Memoria de agentes (cuando el proyecto lo requiere)

Tres niveles que se activan progresivamente según la complejidad del proyecto:

| Nivel | Duración | Implementación | Necesitas si... |
|---|---|---|---|
| **Working Memory** | Sesión | Ventana de contexto del LLM | Tienes cualquier interacción con LLM |
| **Episodic Memory** | Días-semanas | PostgreSQL + búsqueda por fecha/contexto | El sistema necesita recordar interacciones pasadas |
| **Semantic Memory** | Permanente | pgvector + documentos indexados | El sistema necesita conocimiento de dominio persistente |

**Gestión de ventana de contexto:** Cuando uses LLMs en tu app, implementar compresión progresiva. Los mensajes antiguos se resumen automáticamente cuando la ventana supera el 70% de capacidad. El resumen se genera con un modelo económico (Haiku, Flash, Mini).

---

# 4. Infraestructura y Operaciones

## 4.1 Principio de soberanía

**Axioma 6:** Control sobre tu infraestructura. No significa "todo on-premise." Significa: entiendes dónde están tus datos, cuánto pagas, y puedes migrar si el vendor cambia términos.

| Componente | Decisión | Justificación |
|---|---|---|
| **Empaquetado** | Docker (contenedores inmutables) | Reproducibilidad. Lo que corre en dev corre en prod. |
| **Infra base** | Depende del perfil (ver §11) | Desde un VPS de $5/mes hasta Kubernetes multi-cloud |
| **Repositorio** | GitHub | Fuente única de verdad. El LLM lee tu repo para generar código coherente. |
| **CI/CD** | GitHub Actions | Build, test, lint, deploy. Automático en cada PR. |
| **CD (GitOps)** | ArgoCD (cuando necesitas K8s) | Sincronización declarativa continua entre GitHub y producción. Drift detection. |
| **IaC** | Terraform / OpenTofu | Para proyectos que necesitan infra declarativa. No necesario para un VPS simple. |
| **Secrets** | SOPS o Vault | Nunca en código. Variables de entorno como mínimo. Vault para equipos grandes. |

## 4.2 Pipeline de CI/CD

El pipeline mínimo que todo proyecto debe tener, independientemente del tamaño:

```
Push / PR
  → lint (TypeScript compiler, Ruff para Python, ESLint)
  → type check (tsc --noEmit)
  → tests (vitest / pytest)
  → build
  → deploy (automático a staging, manual a prod)
```

**Para proyectos con LLMs integrados**, agregar:

```
  → validación de schemas (JSON Schema de herramientas válido)
  → evals de regresión (agente contra dataset de test)
  → estimación de costo (tokens por suite antes de ejecutar contra modelos de producción)
```

## 4.3 Feature flags

**LaunchDarkly, Unleash, o Flagsmith.** Para proyectos simples, un JSON en la DB o una tabla `feature_flags` basta. Para producción seria: un servicio de feature flags es la red de seguridad que permite deploy continuo sin miedo. Activas la feature para el 5% de usuarios, verificas que funciona, expandes.

---

# 5. Observabilidad

## 5.1 Stack base

| Capa | Qué observa | Herramientas | Todo proyecto lo necesita? |
|---|---|---|---|
| **Infraestructura** | Server health, latencia, errores | OpenTelemetry + Prometheus + Grafana | Sí (al menos uptime monitoring) |
| **Aplicación** | Errores, performance, user flows | Sentry (errores), OpenTelemetry (traces) | Sí |
| **LLM/Agente** | Costos, latencia, calidad de generación | Langfuse (self-hosted) | Solo si usas LLMs en la app |
| **Negocio** | Métricas de producto, conversión | PostHog / Plausible | Recomendado |

## 5.2 Alerting

Alertas básicas para todo proyecto: uptime, errores 5xx, latencia p95. Para proyectos con LLMs, agregar:

- Degradación de calidad de respuestas (hallucination rate).
- Incremento súbito en costo por sesión (loops infinitos del agente).
- Caída en tool selection accuracy.
- Rate limiting de proveedores cercano al límite.

---

# 6. Seguridad

## 6.1 Baseline para todo proyecto

- **HTTPS siempre.** Sin excepciones.
- **Autenticación:** Auth.js (NextAuth) para proyectos TS full-stack. Para APIs: JWT o API keys con rotación.
- **Autorización:** Row-level security en PostgreSQL cuando los datos son multi-tenant. El kiosco ve solo su inventario.
- **Input validation:** Zod/Pydantic en cada boundary. Nunca confíes en datos del cliente.
- **Secrets:** Nunca en código. Variables de entorno como mínimo.
- **Dependencies:** Dependabot o Renovate para actualizaciones automáticas de dependencias con vulnerabilidades conocidas.

## 6.2 Seguridad adicional para LLMs

Cuando tu aplicación integra LLMs:

| Amenaza | Control | Implementación |
|---|---|---|
| **Prompt Injection** | Separación system/user | Nunca concatenar user input en system prompts. Templates con placeholders tipados. |
| **Agent-to-agent injection** | Sanitización inter-agente | Cuando agentes pasan datos entre sí, tratar el output de un agente como untrusted input para el siguiente. Validar contra schema en cada interfaz interna. |
| **Output inseguro** | Todo output LLM = untrusted | Validar contra schema antes de ejecutar cualquier acción derivada. |
| **Data leakage** | Clasificación de datos | No enviar PII a LLMs externos si no es necesario. Scrubbing automático. |
| **Excessive agency** | Allowlists de herramientas | Si el LLM puede llamar herramientas: cada una en allowlist explícito. |
| **Costo descontrolado** | Budget enforcement | Límites por sesión/usuario. Circuit breaker si se excede. |

## 6.3 Aislamiento de ejecución (para agentes)

Cuando los agentes ejecutan herramientas que tocan el sistema operativo o servicios externos:

| Nivel | Runtime | Permisos | Caso de uso |
|---|---|---|---|
| **Nivel 1 (Read)** | Container read-only | Filesystem RO, red restringida | Queries, lectura de APIs |
| **Nivel 2 (Write)** | Container efímero | Destruido post-ejecución | Escritura a DB, generación de archivos |
| **Nivel 3 (Shell)** | MicroVM (Firecracker) | Sin red externa, timeout estricto | Ejecución de código arbitrario, tests |

---

# 7. El Flujo de Desarrollo AI-First

## 7.1 CLIs de desarrollo

En 2026, tres herramientas han convergido como los co-desarrolladores de línea de comandos más efectivos:

| Herramienta | Fortaleza | Cuándo usarla |
|---|---|---|
| **Claude Code** | Refactorizaciones de contexto amplio, razonamiento multi-archivo | Cambios arquitectónicos, migraciones, features complejas que tocan múltiples archivos |
| **Gemini CLI** | Contexto masivo (1M+ tokens), análisis multicapa | Revisión de código completa, documentación de sistemas existentes, análisis de logs |
| **Codex CLI** | Iteración rápida en terminal, acceso a OS | Scripts, one-liners, operaciones de sistema, automatización rápida |

No son mutuamente excluyentes. Son herramientas con fortalezas diferentes. Usa la que mejor se adapte a la tarea.

## 7.2 Principios del desarrollo AI-first

Desarrollar con asistencia de LLM no es "autocompletado glorificado." Es un paradigma diferente:

- **Type-first development:** Define tipos e interfaces ANTES de implementar. El LLM genera implementaciones más correctas cuando tiene el contrato completo. Escribir `interface Product { id: string; name: string; price: number; stock: number }` antes de pedir "implementa el CRUD de productos" produce código dramáticamente mejor que pedir el CRUD sin el tipo.
- **Small PRs:** Los LLMs generan mejor código en cambios pequeños y enfocados que en refactorizaciones masivas. "Agrega validación de stock negativo al formulario de producto" > "Refactoriza todo el módulo de inventario."
- **Context engineering como práctica diaria:** Mantener archivos de contexto actualizados que el LLM consume en cada sesión. Ver §8.
- **Eval-driven (para agentes):** Cuando construyes agentes, escribir los evals antes de la implementación. Los evals definen el comportamiento esperado. Es TDD para el mundo de agentes.
- **Review todo lo generado:** El LLM es un co-desarrollador junior con conocimiento enciclopédico pero sin juicio. Revisa cada PR como si viniera de un junior brillante pero propenso a errores sutiles.

---

# 8. Context Engineering: La Nueva Disciplina

## 8.1 ¿Qué es?

Context engineering es el diseño, creación y mantenimiento de los artefactos que alimentan la ventana de contexto del LLM para que produzca outputs correctos. Es el equivalente a la documentación técnica, pero escrita para ser consumida por máquinas además de humanos.

**El contexto es el multiplicador.** Un LLM de primera línea con context engineering pobre produce peor resultado que un LLM de segunda línea con context engineering excelente. Si le pides a Claude Opus que genere un endpoint sin decirle tus convenciones, patrones, o estructura del proyecto, obtienes código genérico. Si le das CONVENTIONS.md + ARCHITECTURE.md + el schema de la DB, obtienes código que encaja en tu proyecto como si lo hubiera escrito alguien del equipo.

## 8.2 Artefactos de context engineering

La inversión en estos archivos se paga sola en la primera semana de desarrollo asistido:

| Artefacto | Contenido | Ejemplo para inventario de kiosco |
|---|---|---|
| **CONVENTIONS.md** | Estilo de código, patrones, naming, estructura de archivos | "Usamos camelCase en TS, snake_case en Python. Server Actions en `app/actions/`. Componentes en `components/ui/`." |
| **ARCHITECTURE.md** | Diagrama de componentes, flujo de datos, decisiones clave | "Next.js full-stack. PostgreSQL en Supabase. Auth con Auth.js. Deploy en Vercel." |
| **STACK.md** | Tecnologías, versiones, quirks conocidos | "Next.js 15.1, Drizzle 0.38, PostgreSQL 16. Nota: Drizzle no soporta `returning()` en SQLite." |
| **SCHEMA.md** | Modelo de datos con relaciones | "Productos → Categorías (N:1). Movimientos de inventario con timestamp y usuario." |

**Para proyectos más complejos**, agregar:

| Artefacto | Cuándo lo necesitas |
|---|---|
| **INFRA.md** | Cuando tienes infra propia (no solo PaaS) |
| **CONSTRAINTS.md** | Cuando hay restricciones de compliance, budget, o regulatorias |
| **RUNBOOKS.md** | Cuando operas producción y necesitas procedimientos de recuperación |
| **AGENTS.md** | Cuando tu proyecto incluye agentes IA con roles y permisos |

## 8.3 La economía del contexto

La ventana de contexto tiene un precio literal (tokens) y un precio cognitivo (dilución de atención del modelo):

- **Regla 70/30:** El 70% de la ventana debe ser relevante para la tarea actual. El 30% restante es contexto de sistema. Si el ratio se invierte, el output se degrada.
- **Carga selectiva:** No cargar todo en cada sesión. Un cambio de estilos necesita CONVENTIONS.md y los componentes afectados. No necesita INFRA.md.
- **Densidad:** Los context files deben ser densos y sin redundancia. Cada palabra es un token que se paga. "Usamos Drizzle ORM con PostgreSQL. Migraciones en `drizzle/migrations/`. Schema en `src/db/schema.ts`." — 20 tokens que ahorran 200 tokens de explicación en cada sesión.

---

# 9. Capa de Agentes (cuando el proyecto lo requiere)

**No todo proyecto necesita agentes.** Un inventario de kiosco no necesita un enjambre auto-evolutivo. Pero cuando tu proyecto sí integra LLMs como parte de la funcionalidad (chatbots, asistentes, procesamiento inteligente, agentes autónomos), esta capa se activa.

## 9.1 Model Router

No todas las tareas requieren el mismo modelo. Un resumen de texto no necesita Opus; Haiku lo resuelve. Una decisión arquitectónica compleja sí necesita Opus.

| Tier | Modelos (febrero 2026) | Costo relativo | Caso de uso |
|---|---|---|---|
| **T1 (Económico)** | Haiku 3.5, GPT-4o Mini, Flash 2.0, DeepSeek-V3 | $ | Clasificación, formateo, resúmenes, orquestación |
| **T2 (Balance)** | Sonnet 4, GPT-4.1, Gemini 2.5 Pro | $$ | Generación de código, análisis, tool-calling |
| **T3 (Frontier)** | Opus 4.5, GPT-4.5, Gemini Ultra | $$$ | Razonamiento complejo, planificación, arquitectura |
| **T4 (Reasoning)** | o3, Gemini Thinking | $$$$ | Problemas matemáticos, lógicos, evaluación crítica |

**Implementación práctica:** LiteLLM proxy como 80% de la solución. Interfaz OpenAI-compatible para todos los providers, fallback chains, budget tracking. Para el 100%: router custom con clasificador de complejidad.

**Budget enforcement:** Límites por sesión, por usuario, por agente. Cuando se alcanza el límite, degrada al tier inferior con notificación. Sin esto, un loop infinito de un agente te puede costar cientos de dólares en minutos.

## 9.2 Orquestación de agentes

El ecosistema cambia cada 3 meses. La respuesta correcta: **capa de abstracción.**

Define una interfaz `AgentOrchestrator` con métodos estándar (`route`, `execute_tool`, `manage_memory`). Implementa sobre el framework del momento. Si el framework cambia, reescribes el adaptador, no los agentes ni las herramientas.

| Framework | Fortaleza | Caso de uso ideal |
|---|---|---|
| **OpenClaw** | Multi-agente nativo, multi-canal, persistencia local | Enjambres de agentes colaborativos |
| **LangGraph** | Flujos complejos con estado, visualización | Workflows multi-paso con branching |
| **Agents SDK (OpenAI)** | API limpia, handoffs nativos | Equipos centrados en GPT |
| **Custom** | Control total | Necesidades únicas |

## 9.3 Model Context Protocol (MCP)

MCP es el estándar para interoperabilidad de herramientas entre agentes. Las herramientas expuestas como MCP servers son consumibles desde Claude Code, Cursor, IDEs, y tu orquestador sin reescritura. Es HTTP para el mundo de agentes: infraestructura, no feature.

## 9.4 Evals: el TDD de los agentes

| Tipo | Qué verifica | Obligatorio? |
|---|---|---|
| **Regresión** | Calidad se mantiene ante cambios | Sí, pre-deploy |
| **Alucinación** | Output no contiene información fabricada | Sí, pre-deploy |
| **Tool-calling** | Selecciona herramientas correctas | Sí, pre-deploy |
| **Costo** | Tokens en rango esperado | Sí, pre-deploy |
| **Seguridad** | No expone datos, no escala privilegios | Sí, pre-deploy |
| **Adversarial** | Resiste intentos de romperlo | Recomendado, cada ciclo |

**LLM-as-a-Judge:** Un modelo de otro provider evalúa la calidad. Si tu agente usa Claude, el judge usa GPT. Diversidad de modelos reduce blind spots compartidos.

## 9.5 Modelos fundacionales

El sistema es agnóstico por diseño. Ninguna decisión asume un proveedor:

- **Claude (Anthropic):** Razonamiento, tool-calling preciso, instrucciones complejas.
- **Gemini (Google):** Contexto masivo (1M+), multimodalidad, eficiencia de costo.
- **GPT (OpenAI):** Ecosistema maduro, function calling robusto, reasoning (o-series).
- **Eficiencia (DeepSeek, Qwen):** Costo/rendimiento superior para T1. Self-hosteable.

> ⚡ **MODELS.md COMO ARTEFACTO VIVO**
>
> Las capacidades, precios, y disponibilidad de modelos cambian semanalmente. Esta lista es orientativa al momento de escritura (febrero 2026). La recomendación operativa es mantener un archivo `MODELS.md` en el repositorio del proyecto como artefacto de context engineering: modelos permitidos, tiers asignados, precios actuales, benchmarks internos. Este archivo se actualiza mensualmente (o ante cada cambio significativo de provider) y alimenta al Model Router. Tratar la información de modelos como dato estático en un documento es un anti-patrón; tratarla como artefacto versionado y actualizable es context engineering.

## 9.6 Modos de fallo del stack (prevención)

Todo stack tiene modos de fallo específicos. Estos son los más probables cuando LLMs participan en el desarrollo y operación:

| Modo de fallo | Descripción | Prevención |
|---|---|---|
| **Model version drift** | Un provider actualiza silenciosamente el modelo y el comportamiento cambia. Tests pasan pero el output degrada en calidad, estilo, o precisión. | Pinning de versiones de modelo cuando el provider lo permita. Evals de regresión ante cada cambio de modelo. |
| **Embedding drift** | Los embeddings generados con una versión de modelo no son compatibles con los generados con otra. La búsqueda semántica degrada sin error visible. | Regenerar embeddings completos ante cambios de modelo de embedding. Monitorear hit rate de búsqueda semántica. |
| **Corrupción de memoria semántica** | Si usas memoria persistente para agentes (§3.4), datos incorrectos entran en la memoria y se amplifican con el uso. | Validación de escritura en memoria. TTL para memorias. Mecanismo de purge manual. Auditoría periódica. |
| **Cost explosion por loop** | Un agente entra en un loop de reintentos, consumiendo tokens sin converger. Prompt injection puede provocar esto deliberadamente. | Budget enforcement por sesión y por agente. Circuit breaker: si tokens consumidos > N×esperado, abort. |
| **Context window overflow** | El contexto acumulado excede la ventana y el LLM empieza a "olvidar" instrucciones tempranas, generando output inconsistente. | Monitoreo de uso de contexto. Summarization estratégica. Regla 70/30 de §8.3. |
| **Provider downtime cascade** | Tu provider principal cae y no tienes fallback configurado. | LiteLLM con fallback a segundo provider. Nunca depender de un solo provider para funcionalidad crítica en producción. |

---

# 10. Stack Completo: La Tabla de Referencia

## 10.1 Stack base (todo proyecto)

| Capa | Tecnología | Alternativa | Axioma |
|---|---|---|---|
| **Lenguaje frontend** | TypeScript | — | 1, 2 |
| **Framework frontend** | Next.js (App Router) | Astro (estáticos) | 2, 3 |
| **Estilos** | Tailwind CSS | — | 3 |
| **Componentes UI** | Shadcn/UI | Radix primitives | 2 |
| **Validación** | Zod (TS) / Pydantic (Py) | — | 1, 4 |
| **Backend (TS)** | Next.js Server Actions / Hono | tRPC | 3 |
| **Backend (Python)** | FastAPI | — | 4 |
| **Base de datos** | PostgreSQL | — | 2 |
| **ORM (TS)** | Drizzle | Prisma | 3 |
| **ORM (Python)** | SQLAlchemy 2.0 | — | 2 |
| **Empaquetado** | Docker | — | 5 |
| **Repositorio** | GitHub | GitLab | 2 |
| **CI/CD** | GitHub Actions | GitLab CI | 5 |
| **Observabilidad** | OpenTelemetry + Sentry | Datadog | 6 |
| **Auth** | Auth.js (NextAuth) | Clerk, Supabase Auth | 6 |

## 10.2 Stack extendido (proyectos con LLMs/agentes)

| Capa | Tecnología | Alternativa | Axioma |
|---|---|---|---|
| **Vectores** | pgvector (< 10M) | Qdrant (>10M) | 2 |
| **Embeddings** | OpenAI text-embedding-3 | Cohere, Nomic | 6 |
| **Observabilidad LLM** | Langfuse (self-hosted) | LangSmith | 6 |
| **Evals** | Braintrust / Arize Phoenix | TruLens | 4, 5 |
| **Model Router** | LiteLLM proxy / custom | — | 5, 6 |
| **Orquestación** | OpenClaw (tras abstracción) | LangGraph, Agents SDK | 5 |
| **Interop** | MCP | — | 5 |
| **Aislamiento** | gVisor / Firecracker | Docker rootless | 5 |
| **GitOps** | ArgoCD | Flux | 5 |
| **Feature flags** | Unleash / Flagsmith | LaunchDarkly | 6 |
| **Dev tools** | Claude Code + Gemini CLI + Codex CLI | Cursor, Windsurf | 2 |

---

# 11. Tres Perfiles de Proyecto

## 11.1 Perfil Mínimo: "El Kiosco"

Un inventario de kiosco. Un SaaS de agenda. Un portal de gestión interna. CRUD con algo de lógica de negocio. Sin agentes.

| Decisión | Elección |
|---|---|
| **Stack** | TypeScript full-stack. Next.js + Server Actions + Drizzle + PostgreSQL |
| **Infra** | Vercel (frontend) + Supabase o Neon (PostgreSQL). O un VPS de $5-10/mes con Docker Compose. |
| **CI/CD** | GitHub Actions: lint + type check + test + deploy |
| **Observabilidad** | Sentry (errores) + Vercel Analytics o Plausible |
| **Context engineering** | CONVENTIONS.md + SCHEMA.md. Dos archivos. |
| **Desarrollo** | Un humano + Claude Code / Cursor. |
| **Costo operativo mensual** | $5-50 |

## 11.2 Perfil Medio: "El SaaS con IA"

Una plataforma con usuarios, pagos, y una capa de IA: chatbot de soporte, análisis inteligente de datos, generación de contenido. LLMs integrados pero no agentes autónomos.

| Decisión | Elección |
|---|---|
| **Stack** | TypeScript (Next.js) + Python (FastAPI para capa IA). PostgreSQL + pgvector. |
| **Infra** | Docker en VPS (Hetzner) o cloud manejado. ArgoCD si Kubernetes. |
| **CI/CD** | GitHub Actions: lint + types + tests + evals de IA + deploy |
| **Model Router** | LiteLLM proxy con budget enforcement |
| **Observabilidad** | Sentry + Langfuse + Prometheus + Grafana |
| **Context engineering** | CONVENTIONS.md + ARCHITECTURE.md + STACK.md + SCHEMA.md |
| **Desarrollo** | 1-3 humanos + LLMs como co-developers |
| **Costo operativo mensual** | $50-500 |

## 11.3 Perfil Completo: "El Enjambre"

Un sistema con agentes autónomos que ejecutan tareas, toman decisiones, y se auto-optimizan. El escenario de Xanpan::Agents.

| Decisión | Elección |
|---|---|
| **Stack** | Stack completo §10.1 + §10.2. Dual language. Model Router custom. |
| **Infra** | Kubernetes con ArgoCD. Firecracker para aislamiento de agentes. IaC con Terraform. |
| **CI/CD** | Pipeline completo con evals (regresión, alucinación, tool-calling, seguridad, adversarial) |
| **Model Router** | Custom con clasificador de complejidad + circuit breakers + budget enforcement |
| **Observabilidad** | Stack completo: OTEL + Prometheus + Grafana + Langfuse + alerting AI-native |
| **Context engineering** | Suite completa §8.2: CONVENTIONS, ARCHITECTURE, STACK, SCHEMA, INFRA, CONSTRAINTS, RUNBOOKS, AGENTS |
| **Desarrollo** | PO + Operador + enjambre (Xanpan::Agents) |
| **Costo operativo mensual** | $500-5000+ |

---

# 12. Conexión con el Corpus Xanpan::Agents (opcional)

Este documento funciona de forma autónoma. Es un stack de referencia para cualquier proyecto construido con asistencia de LLM. Pero cuando se usa en conjunto con el corpus Xanpan::Agents, forma parte de una trinidad:

```
┌──────────────────────────────────────────┐
│        CHAPTER 0: El Operador            │
│        Solitario                         │
│   Bootstrap: DÓNDE empezar              │
│   (Punto de entrada al corpus)           │
└────────────────┬─────────────────────────┘
                 │
┌────────────────┴─────────────────────────┐
│          STACK::LLM v1.0                 │ ← Este documento
│   Arquitectura: CON QUÉ construir       │
│   (Universal, desde Fase 1)             │
└────────────────┬─────────────────────────┘
                 │
      ┌──────────┴──────────┐
      │                     │
┌─────┴───────┐     ┌──────┴──────────┐
│ SWARM::OPS  │     │ XANPAN::AGENTS  │
│ v1.0        │     │ v2.1            │
│ Operaciones │     │ Metodología     │
│ (Fase 3-4)  │     │ (Fase 4)        │
└─────────────┘     └─────────────────┘
```

**Orden de lectura recomendado:** Chapter 0 → STACK::LLM → Swarm::Ops → Xanpan::Agents. Chapter 0 dice por dónde empezar. STACK::LLM dice con qué construir. Swarm::Ops dice cómo operar. Xanpan::Agents dice cómo gobernar.

**STACK::LLM es universal.** Aplica a los tres perfiles de proyecto. Xanpan::Agents y Swarm::Ops se activan solo cuando el proyecto alcanza el Perfil Completo.

**Mapa de referencias para Perfil Completo:**

| Concepto | STACK::LLM | Xanpan::Agents | Swarm::Ops |
|---|---|---|---|
| Model Router | §9.1 (tiers, budget) | §9.3 (conceptual) | — |
| Evals | §9.4 (pipeline) | §7.2 (práctica obligatoria) | §4.3 (CI insuficiente) |
| Context Engineering | §8 (artefactos, economía) | §2.2 (responsabilidad Operador) | — |
| Seguridad | §6 (OWASP, aislamiento) | §13 (gobernanza) | §8 (Security-by-Swarm) |
| Observabilidad | §5 (3 capas) | §12 (dashboard 5D) | §7 (agente-observer) |
| CI/CD | §4.2 (pipeline) | — | §4 (sistema nervioso) |
| Deploy | §4.3 (feature flags) | §10.1 (aprobación humana) | §4.2 (flujos concurrentes) |

---

*STACK::LLM v1.0. Febrero 2026.*

*Este stack no es una lista de tecnologías favoritas. Es una arquitectura diseñada desde la perspectiva de cómo los LLMs realmente procesan y generan código. Cada decisión prioriza: (1) reducir errores de generación, (2) mantener costos controlados, (3) permitir evolución sin lock-in, y (4) operar de forma segura en producción. Aplica igual al inventario de un kiosco que al enjambre más ambicioso. Porque en ambos casos, tu co-desarrollador es un modelo de lenguaje, y merece las mejores condiciones de trabajo.*
