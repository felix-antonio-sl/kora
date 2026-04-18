---
_manifest:
  urn: urn:fxsl:kb:stack-llm-arquitectura
  provenance:
    created_by: kora/curator
    created_at: '2026-02-25'
    source: source/fxsl/xanpan/stack-llm-v1-arquitectura.md
version: 1.1.0
status: published
tags:
- xanpan
- stack-llm
- arquitectura
- desarrollo-ai
- axiomas
- tech-stack
- typescript
- python
- agentes
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:stack-llm-arquitectura
---

# STACK::LLM v1.0


Stack de Desarrollo para la Era de Asistencia por LLM

---

## 0. Axiomas Fundacionales

Este documento no es un catalogo de tecnologias favoritas. Cada decision emerge de **seis axiomas** que reflejan como los LLMs realmente procesan y generan codigo. Aplican igual si estas construyendo un sistema de inventario para un kiosco, una plataforma SaaS, o un enjambre de agentes autonomos. Porque en los tres casos, tu co-desarrollador es un modelo de lenguaje.

Entender los axiomas es mas importante que memorizar la tabla final. Las tecnologias cambiaran. Los axiomas sobreviviran.

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

## 1. Frontend: La Capa Visual

Ya sea un dashboard de inventario de kiosco, un portal de clientes, o la interfaz del Tablero Neural de Xanpan::Agents: todo es frontend. Y es frontend que un LLM va a ayudarte a generar, mantener y evolucionar.

### 1.1 Lenguaje y Framework Core

**TypeScript + React + Next.js (App Router)**

**TypeScript** intercepta el 70-80% de los errores de generación más comunes: propiedades faltantes, tipos incompatibles, contratos rotos. Cuando un LLM genera un componente y el compilador rechaza `<Button onClick={handler} labell="Guardar" />`, ese typo se atrapa antes de que exista. Sin TypeScript, llega a producción.

**React** es el framework con mayor representación en datos de entrenamiento (**Axioma 2**). Los LLMs han internalizado miles de patrones composicionales. Pides "un formulario de registro con validación" y recibes un componente funcional con hooks, estados y manejo de errores coherente. Con frameworks menos representados, recibes más alucinaciones estructurales.

**Next.js App Router** unifica server components, server actions y routing. Los Server Actions son particularmente poderosos: eliminan la necesidad de APIs REST separadas para operaciones internas. Un formulario de "agregar producto al inventario" puede tener su lógica de validación, persistencia y redirect en el mismo archivo. Menos superficie = menos errores de generación = el LLM genera flujos completos con coherencia.

**Alternativa para sitios estáticos:** Astro cuando no necesitas interactividad rica. Un catálogo de productos de lectura, un blog, una landing page.

### 1.2 Estilos y Sistema de Diseño

**Tailwind CSS + Shadcn/UI**

**Tailwind** convierte las decisiones de diseño en tokens textuales atómicos (**Axioma 3**). Cada clase es un token predecible. `className="flex items-center gap-2 text-sm font-medium text-gray-700"` — el LLM combina estas clases con la misma precisión con la que combina palabras en una oración. No hay cascada CSS que predecir, no hay especificidad que calcular, no hay archivos .css separados que mantener en coherencia.

**Shadcn/UI** proporciona componentes accesibles y tipados que se copian directamente al proyecto. No es dependencia npm — es código tuyo que el LLM puede leer, modificar y extender. Un `<DataTable>` de Shadcn que necesitas personalizar para tu inventario de kiosco: el LLM lo modifica directamente porque está en tu repo, no escondido en node_modules.

### 1.3 Validación y Estado

**Zod** como capa de validación unificada:

Un schema Zod definido una vez es ley en frontend Y backend. Para un inventario de kiosco: `const ProductSchema = z.object({ name: z.string.min(1), price: z.number.positive, stock: z.number.int.nonnegative })`. Ese schema valida el formulario, valida el Server Action, y genera el tipo TypeScript automáticamente. El LLM no puede inventar un campo `precio` cuando el schema dice `price`.

**TanStack Query** para gestión de estado del servidor: caching, revalidación, y optimistic updates. Un LLM genera un hook de TanStack Query con mucha más fiabilidad que una solución custom de state management.

---

## 2. Backend: La Capa Lógica

### 2.1 Dos lenguajes, responsabilidades divididas

No es indecisión. Es especialización. Ambos lenguajes están masivamente representados en training data (**Axioma 2**) y el LLM genera código de alta calidad en ambos.

| Lenguaje | Rol | Cuándo |
|---|---|---|
| **TypeScript (Hono / tRPC / Next.js Server Actions)** | API de producto, lógica de negocio, BFF | Cuando el frontend es Next.js y quieres types compartidos end-to-end. Para la mayoría de proyectos web: CRUD, dashboards, inventarios. |
| **Python (FastAPI)** | Capa cognitiva, procesamiento de datos, ML, integración con LLMs | Cuando necesitas procesamiento pesado, integración con ecosistema ML/AI, o tool-calling para agentes. |

**Para proyectos simples** (inventario de kiosco, portal de gestión, SaaS básico): TypeScript full-stack con Next.js Server Actions es suficiente. No necesitas Python. Un solo lenguaje, tipos compartidos, zero API boilerplate.

**Para proyectos con capa cognitiva** (chatbots, agentes, procesamiento ML): Python con FastAPI para la lógica de agentes + TypeScript para el frontend. FastAPI genera automáticamente JSON Schema desde Pydantic, que es el formato que los LLMs consumen para tool-calling. La cadena `Pydantic Model → JSON Schema → Tool Definition` es nativa y sin fricción.

### 2.2 FastAPI: cuándo y por qué

FastAPI no es obligatorio para todo proyecto. Es obligatorio cuando necesitas:

- **Tool-calling para agentes:** La cadena Pydantic → JSON Schema → Tool es irremplazable.
- **APIs que otros sistemas consumen:** OpenAPI automático desde tipos Python. Documentación gratis.
- **Procesamiento de datos:** El ecosistema Python (pandas, numpy, scikit-learn) no tiene equivalente en TS.

Para un inventario de kiosco con CRUD simple, FastAPI es overkill. Server Actions de Next.js + Drizzle ORM + PostgreSQL resuelven sin salir de TypeScript.

### 2.3 Diseño de APIs y herramientas

Independientemente del lenguaje, cada endpoint y cada herramienta sigue los mismos principios:

- **Schema tipado para input Y output.** Zod en TS, Pydantic en Python. No `any`. Nunca.
- **Docstrings/JSDoc estructurados.** El LLM los lee para entender qué hace cada función cuando genera código que la llama.
- **Validación antes de ejecución.** Input validado contra schema antes de tocar la base de datos o un servicio externo.
- **Errores tipados.** No strings de error. Tipos de error que el frontend puede discriminar y manejar.

---

## 3. Datos: La Capa de Persistencia

### 3.1 Base de Datos

**PostgreSQL.** Sin excepciones para el 95% de los casos de uso.

**Sobre-representación en training data** (**Axioma 2**): Los LLMs generan SQL para PostgreSQL con precisión notable. Queries complejas, CTEs, window functions, JSON operations: todo sale bien generado al primer intento con más frecuencia que con cualquier otra base.

**pgvector** integrado nativamente para búsqueda vectorial cuando lo necesites. Empiezas con CRUD simple para tu inventario. Un día quieres búsqueda semántica ("muéstrame productos similares a X"). pgvector lo habilita sin migrar de base de datos. HNSW indexes para búsqueda aproximada de alta velocidad.

**Es la base de datos, no una base de datos.** Almacena datos relacionales, JSON (jsonb), vectores (pgvector), full-text search, geospatial (PostGIS). No necesitas Redis para cache simple (tienen unlogged tables), no necesitas Elasticsearch para búsqueda básica (tienen tsvector), no necesitas una base vectorial separada (tienen pgvector hasta ~10M vectores).

**Para escalas masivas de vectores** (>10M): Qdrant, Pinecone, o Milvus como tier especializado.

### 3.2 ORM y Query Builders

**TypeScript:** Drizzle ORM. Type-safe, cercano a SQL puro, excelente para generación por LLM (**Axioma 3**: declarativo). El LLM genera queries Drizzle que son casi SQL legible. Alternativa: Prisma si el equipo prioriza DX sobre cercanía a SQL.

**Python:** SQLAlchemy 2.0 con el nuevo estilo de queries tipadas.

### 3.3 Embeddings y búsqueda vectorial (cuando lo necesites)

No todo proyecto necesita embeddings. Un inventario de kiosco no los necesita al día 1. Pero el stack debe permitir añadirlos sin reescritura:

- **Abstracción obligatoria:** Si decides usar embeddings, una interfaz común (`EmbeddingProvider`) que permita intercambiar modelos. Almacenar siempre el `model_id` junto al vector.
- **Modelos recomendados:** OpenAI text-embedding-3-small/large como default. Cohere embed-v4 o Nomic embed como fallback open-source (soberanía, **Axioma 6**).
- **Estrategia de migración:** Re-indexación progresiva en background cuando se cambia de modelo. Dual-read durante transición.

### 3.4 Memoria de agentes (cuando el proyecto lo requiere)

Tres niveles que se activan progresivamente según la complejidad del proyecto:

| Nivel | Duración | Implementación | Necesitas si... |
|---|---|---|---|
| **Working Memory** | Sesión | Ventana de contexto del LLM | Tienes cualquier interacción con LLM |
| **Episodic Memory** | Días-semanas | PostgreSQL + búsqueda por fecha/contexto | El sistema necesita recordar interacciones pasadas |
| **Semantic Memory** | Permanente | pgvector + documentos indexados | El sistema necesita conocimiento de dominio persistente |

**Gestión de ventana de contexto:** Cuando uses LLMs en tu app, implementar compresión progresiva. Los mensajes antiguos se resumen automáticamente cuando la ventana supera el 70% de capacidad. El resumen se genera con un modelo económico (Haiku, Flash, Mini).

---

## 4. Infraestructura y Operaciones

### 4.1 Principio de soberanía

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

### 4.2 Pipeline de CI/CD

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

### 4.3 Feature flags

**LaunchDarkly, Unleash, o Flagsmith.** Para proyectos simples, un JSON en la DB o una tabla `feature_flags` basta. Para producción seria: un servicio de feature flags es la red de seguridad que permite deploy continuo sin miedo. Activas la feature para el 5% de usuarios, verificas que funciona, expandes.

---

## 5. Observabilidad

### 5.1 Stack base

| Capa | Qué observa | Herramientas | Todo proyecto lo necesita? |
|---|---|---|---|
| **Infraestructura** | Server health, latencia, errores | OpenTelemetry + Prometheus + Grafana | Sí (al menos uptime monitoring) |
| **Aplicación** | Errores, performance, user flows | Sentry (errores), OpenTelemetry (traces) | Sí |
| **LLM/Agente** | Costos, latencia, calidad de generación | Langfuse (self-hosted) | Solo si usas LLMs en la app |
| **Negocio** | Métricas de producto, conversión | PostHog / Plausible | Recomendado |

### 5.2 Alerting

Alertas básicas para todo proyecto: uptime, errores 5xx, latencia p95. Para proyectos con LLMs, agregar:

- Degradación de calidad de respuestas (hallucination rate).
- Incremento súbito en costo por sesión (loops infinitos del agente).
- Caída en tool selection accuracy.
- Rate limiting de proveedores cercano al límite.

---

## 6. Seguridad

### 6.1 Baseline para todo proyecto

- **HTTPS siempre.** Sin excepciones.
- **Autenticación:** Auth.js (NextAuth) para proyectos TS full-stack. Para APIs: JWT o API keys con rotación.
- **Autorización:** Row-level security en PostgreSQL cuando los datos son multi-tenant. El kiosco ve solo su inventario.
- **Input validation:** Zod/Pydantic en cada boundary. Nunca confíes en datos del cliente.
- **Secrets:** Nunca en código. Variables de entorno como mínimo.
- **Dependencies:** Dependabot o Renovate para actualizaciones automáticas de dependencias con vulnerabilidades conocidas.

### 6.2 Seguridad adicional para LLMs

Cuando tu aplicación integra LLMs:

| Amenaza | Control | Implementación |
|---|---|---|
| **Prompt Injection** | Separación system/user | Nunca concatenar user input en system prompts. Templates con placeholders tipados. |
| **Agent-to-agent injection** | Sanitización inter-agente | Cuando agentes pasan datos entre sí, tratar el output de un agente como untrusted input para el siguiente. Validar contra schema en cada interfaz interna. |
| **Output inseguro** | Todo output LLM = untrusted | Validar contra schema antes de ejecutar cualquier acción derivada. |
| **Data leakage** | Clasificación de datos | No enviar PII a LLMs externos si no es necesario. Scrubbing automático. |
| **Excessive agency** | Allowlists de herramientas | Si el LLM puede llamar herramientas: cada una en allowlist explícito. |
| **Costo descontrolado** | Budget enforcement | Límites por sesión/usuario. Circuit breaker si se excede. |

### 6.3 Aislamiento de ejecución (para agentes)

Cuando los agentes ejecutan herramientas que tocan el sistema operativo o servicios externos:

| Nivel | Runtime | Permisos | Caso de uso |
|---|---|---|---|
| **Nivel 1 (Read)** | Container read-only | Filesystem RO, red restringida | Queries, lectura de APIs |
| **Nivel 2 (Write)** | Container efímero | Destruido post-ejecución | Escritura a DB, generación de archivos |
| **Nivel 3 (Shell)** | MicroVM (Firecracker) | Sin red externa, timeout estricto | Ejecución de código arbitrario, tests |

---

## 7. El Flujo de Desarrollo AI-First

### 7.1 CLIs de desarrollo

En 2026, tres herramientas han convergido como los co-desarrolladores de línea de comandos más efectivos:

| Herramienta | Fortaleza | Cuándo usarla |
|---|---|---|
| **Claude Code** | Refactorizaciones de contexto amplio, razonamiento multi-archivo | Cambios arquitectónicos, migraciones, features complejas que tocan múltiples archivos |
| **Gemini CLI** | Contexto masivo (1M+ tokens), análisis multicapa | Revisión de código completa, documentación de sistemas existentes, análisis de logs |
| **Codex CLI** | Iteración rápida en terminal, acceso a OS | Scripts, one-liners, operaciones de sistema, automatización rápida |

No son mutuamente excluyentes. Son herramientas con fortalezas diferentes. Usa la que mejor se adapte a la tarea.

### 7.2 Principios del desarrollo AI-first

Desarrollar con asistencia de LLM no es "autocompletado glorificado." Es un paradigma diferente:

- **Type-first development:** Define tipos e interfaces ANTES de implementar. El LLM genera implementaciones más correctas cuando tiene el contrato completo. Escribir `interface Product { id: string; name: string; price: number; stock: number }` antes de pedir "implementa el CRUD de productos" produce código dramáticamente mejor que pedir el CRUD sin el tipo.
- **Small PRs:** Los LLMs generan mejor código en cambios pequeños y enfocados que en refactorizaciones masivas. "Agrega validación de stock negativo al formulario de producto" > "Refactoriza todo el módulo de inventario."
- **Context engineering como práctica diaria:** Mantener archivos de contexto actualizados que el LLM consume en cada sesión. Ver §8.
- **Eval-driven (para agentes):** Cuando construyes agentes, escribir los evals antes de la implementación. Los evals definen el comportamiento esperado. Es TDD para el mundo de agentes.
- **Review todo lo generado:** El LLM es un co-desarrollador junior con conocimiento enciclopédico pero sin juicio. Revisa cada PR como si viniera de un junior brillante pero propenso a errores sutiles.

---

## 8. Context Engineering: La Nueva Disciplina

### 8.1 ¿Qué es?

Context engineering es el diseño, creación y mantenimiento de los artefactos que alimentan la ventana de contexto del LLM para que produzca outputs correctos. Es el equivalente a la documentación técnica, pero escrita para ser consumida por máquinas además de humanos.

**El contexto es el multiplicador.** Un LLM de primera línea con context engineering pobre produce peor resultado que un LLM de segunda línea con context engineering excelente. Si le pides a Claude Opus que genere un endpoint sin decirle tus convenciones, patrones, o estructura del proyecto, obtienes código genérico. Si le das CONVENTIONS.md + ARCHITECTURE.md + el schema de la DB, obtienes código que encaja en tu proyecto como si lo hubiera escrito alguien del equipo.

### 8.2 Artefactos de context engineering

La inversión en estos archivos se paga sola en la primera semana de desarrollo asistido:

| Artefacto | Contenido | Ejemplo para inventario de kiosco |
|---|---|---|
| **CONVENTIONS.md** | Estilo de código, patrones, naming, estructura de archivos | "Usamos camelCase en TS, snake_case en Python. Server Actions en `app/actions/`. Componentes en `components/ui/`." |
| **ARCHITECTURE.md** | Diagrama de componentes, flujo de datos, decisiones clave | "Next.js full-stack. PostgreSQL en Supabase. Auth con Auth.js. Deploy en Vercel." |
| **STACK.md** | Tecnologías, versiones, quirks conocidos | "Next.js 15.1, Drizzle 0.38, PostgreSQL 16. Nota: Drizzle no soporta `returning` en SQLite." |
| **SCHEMA.md** | Modelo de datos con relaciones | "Productos → Categorías (N:1). Movimientos de inventario con timestamp y usuario." |

**Para proyectos más complejos**, agregar:

| Artefacto | Cuándo lo necesitas |
|---|---|
| **INFRA.md** | Cuando tienes infra propia (no solo PaaS) |
| **CONSTRAINTS.md** | Cuando hay restricciones de compliance, budget, o regulatorias |
| **RUNBOOKS.md** | Cuando operas producción y necesitas procedimientos de recuperación |
| **AGENTS.md** | Cuando tu proyecto incluye agentes IA con roles y permisos |

### 8.3 La economía del contexto

La ventana de contexto tiene un precio literal (tokens) y un precio cognitivo (dilución de atención del modelo):

- **Regla 70/30:** El 70% de la ventana debe ser relevante para la tarea actual. El 30% restante es contexto de sistema. Si el ratio se invierte, el output se degrada.
- **Carga selectiva:** No cargar todo en cada sesión. Un cambio de estilos necesita CONVENTIONS.md y los componentes afectados. No necesita INFRA.md.
- **Densidad:** Los context files deben ser densos y sin redundancia. Cada palabra es un token que se paga. "Usamos Drizzle ORM con PostgreSQL. Migraciones en `drizzle/migrations/`. Schema en `src/db/schema.ts`." — 20 tokens que ahorran 200 tokens de explicación en cada sesión.

---
