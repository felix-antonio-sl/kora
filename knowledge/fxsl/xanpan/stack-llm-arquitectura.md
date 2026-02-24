---
_manifest:
  urn: "urn:fxsl:kb:stack-llm-arquitectura"
  provenance:
    created_by: "FS"
    created_at: "2026-02-24"
    source: "source/fxsl/xanpan/stack-llm-v1-arquitectura.md"
version: "1.0.0"
status: published
tags: [xanpan, stack, llm, arquitectura, typescript, python, infraestructura, agentes]
lang: es
---

# STACK::LLM — Arquitectura de Referencia para Desarrollo Asistido por LLM v1.0.0

## 1. Axiomas Fundacionales

Los seis axiomas que gobiernan toda decision de stack son invariantes del sistema. Las tecnologias concretas **PUEDEN** cambiar; los axiomas persisten. Toda decision tecnologica dentro de este documento se deriva de al menos un axioma.

> **AXIOMA 1: Tipado estatico como guardrail cognitivo**
>
> Los sistemas de tipos funcionan como capa de validacion que intercepta errores de generacion antes de runtime. TypeScript y Pydantic actuan como compiladores de cordura para el output del LLM.

Todo proyecto **DEBE** usar lenguajes con tipado estatico (TypeScript, Python con Pydantic) como lenguajes primarios. El codigo generado por LLM sin tipos estaticos **NO DEBE** desplegarse a produccion.

**Correcto:** `TypeScript con strict mode habilitado para todo el proyecto`
**Incorrecto:** `JavaScript vanilla sin tipos para "ir mas rapido"`

> **AXIOMA 2: Sobre-representacion en entrenamiento como ventaja competitiva**
>
> Las tecnologias dominantes en GitHub (Python, TypeScript, React, PostgreSQL) estan masivamente representadas en los datos de entrenamiento de todo LLM. Esto genera patrones de generacion con menor tasa de error y mayor coherencia estructural.

Toda seleccion de tecnologia **DEBERIA** priorizar aquellas con alta representacion en datos de entrenamiento de LLMs. Elegir una tecnologia nicho con 1/100 de la representacion en training data **NO DEBERIA** hacerse sin justificacion documentada.

> **AXIOMA 3: Declaratividad sobre imperatividad**
>
> Los LLMs generan codigo mas correcto cuando describen un estado final deseado (SQL, React JSX, Tailwind, Terraform HCL) que cuando orquestan secuencias imperativas paso a paso.

Toda decision de framework y herramienta **DEBERIA** preferir APIs declarativas sobre imperativas. React sobre jQuery, Tailwind sobre CSS imperativo, SQL directo sobre query builders imperativos.

> **AXIOMA 4: Contratos explicitos como limites de alucinacion**
>
> JSON Schema, OpenAPI, Zod, Pydantic y tipos estrictos definen los limites de lo que el modelo puede generar. Sin contratos, la creatividad del modelo se vuelve impredecibilidad.

Todo endpoint, formulario y transformacion de datos **DEBE** tener un contrato tipado. La instruccion "parsea esto" (invitacion a alucinar) **NO DEBE** reemplazar a "valida contra este schema" (instruccion precisa).

**Correcto:** `const ProductSchema = z.object({ name: z.string(), price: z.number() })`
**Incorrecto:** `const data = JSON.parse(input) // sin validacion de schema`

> **AXIOMA 5: Resiliencia como requisito arquitectonico, no como feature**
>
> Un sistema construido con asistencia de LLM sin tests, linting, CI y validacion automatica no es un sistema de produccion. Los LLMs son no-deterministas: dos generaciones del mismo prompt pueden producir codigo diferente. Los guardrails (tipos, tests, lint, CI) convierten ese no-determinismo en un problema manejable.

Todo proyecto **DEBE** incluir tests, linting, CI y validacion automatica antes de considerarse apto para produccion.

> **AXIOMA 6: Soberania y control de costos**
>
> Self-hosting donde sea posible. Routing inteligente de modelos para controlar costos de desarrollo asistido. Dependencias minimas de vendors con lock-in.

Todo stack **DEBE** minimizar dependencias de vendors con lock-in. Un stack que depende de un solo proveedor de LLM o cloud es un stack fragil y **NO DEBERIA** usarse para produccion sin plan de migracion documentado.

---

## 2. Frontend: Capa Visual

### 2.1 Lenguaje y Framework Core

Todo proyecto con interfaz visual **DEBE** usar **TypeScript + React + Next.js (App Router)** como stack frontend primario.

| Tecnologia | Funcion | Axioma |
|---|---|---|
| **TypeScript** | Intercepta el 70-80% de errores de generacion mas comunes: propiedades faltantes, tipos incompatibles, contratos rotos | 1 |
| **React** | Framework con mayor representacion en datos de entrenamiento. Los LLMs han internalizado miles de patrones composicionales | 2 |
| **Next.js App Router** | Unifica server components, server actions y routing. Los Server Actions eliminan la necesidad de APIs REST separadas para operaciones internas | 3 |

Para sitios estaticos sin interactividad rica (catalogos de lectura, blogs, landing pages), el proyecto **PUEDE** usar **Astro** como alternativa.

### 2.2 Estilos y Sistema de Diseno

Todo proyecto **DEBE** usar **Tailwind CSS** para estilos y **DEBERIA** usar **Shadcn/UI** como biblioteca de componentes.

- **Tailwind** convierte decisiones de diseno en tokens textuales atomicos (Axioma 3). Cada clase es un token predecible. No hay cascada CSS que predecir, no hay especificidad que calcular, no hay archivos .css separados que mantener en coherencia.
- **Shadcn/UI** proporciona componentes accesibles y tipados que se copian directamente al proyecto. No es dependencia npm: es codigo propio que el LLM **PUEDE** leer, modificar y extender.

### 2.3 Validacion y Estado

Todo proyecto **DEBE** usar **Zod** como capa de validacion unificada en frontend.

Un schema Zod definido una vez es ley en frontend y backend. El schema valida el formulario, valida el Server Action y genera el tipo TypeScript automaticamente.

**Correcto:**
```typescript
const ProductSchema = z.object({
  name: z.string().min(1),
  price: z.number().positive(),
  stock: z.number().int().nonnegative()
});
```
**Incorrecto:**
```typescript
// Validacion manual sin schema compartido
if (typeof data.name === "string") { ... }
```

Para gestion de estado del servidor, el proyecto **DEBERIA** usar **TanStack Query** (caching, revalidacion, optimistic updates).

---

## 3. Backend: Capa Logica

### 3.1 Lenguajes y Responsabilidades

El stack **DEBE** usar uno o dos lenguajes segun la complejidad del proyecto. Ambos lenguajes estan masivamente representados en training data (Axioma 2).

| Lenguaje | Rol | Cuando usarlo |
|---|---|---|
| **TypeScript (Hono / tRPC / Next.js Server Actions)** | API de producto, logica de negocio, BFF | Cuando el frontend es Next.js y se requieren types compartidos end-to-end. Para proyectos web: CRUD, dashboards, inventarios |
| **Python (FastAPI)** | Capa cognitiva, procesamiento de datos, ML, integracion con LLMs | Cuando se necesita procesamiento pesado, integracion con ecosistema ML/AI, o tool-calling para agentes |

Para proyectos simples (inventario, portal de gestion, SaaS basico), TypeScript full-stack con Next.js Server Actions **DEBERIA** ser suficiente. Un solo lenguaje, tipos compartidos, zero API boilerplate.

Para proyectos con capa cognitiva (chatbots, agentes, procesamiento ML), el stack **DEBE** usar Python con FastAPI para la logica de agentes + TypeScript para el frontend. FastAPI genera automaticamente JSON Schema desde Pydantic, que es el formato que los LLMs consumen para tool-calling. La cadena `Pydantic Model -> JSON Schema -> Tool Definition` es nativa y sin friccion.

### 3.2 FastAPI: Condiciones de Uso

FastAPI **NO DEBE** usarse para todo proyecto. FastAPI **DEBE** usarse cuando se requiere al menos una de estas capacidades:

- **Tool-calling para agentes:** La cadena Pydantic -> JSON Schema -> Tool es irremplazable.
- **APIs que otros sistemas consumen:** OpenAPI automatico desde tipos Python. Documentacion generada.
- **Procesamiento de datos:** El ecosistema Python (pandas, numpy, scikit-learn) no tiene equivalente en TypeScript.

Para CRUD simple, Server Actions de Next.js + Drizzle ORM + PostgreSQL **DEBERIAN** usarse sin salir de TypeScript.

### 3.3 Diseno de APIs y Herramientas

Independientemente del lenguaje, todo endpoint y toda herramienta **DEBE** cumplir:

- **Schema tipado para input y output.** Zod en TypeScript, Pydantic en Python. El tipo `any` **NO DEBE** usarse.
- **Docstrings/JSDoc estructurados.** El LLM los lee para entender que hace cada funcion cuando genera codigo que la invoca.
- **Validacion antes de ejecucion.** El input **DEBE** validarse contra schema antes de tocar base de datos o servicio externo.
- **Errores tipados.** Strings de error genericos **NO DEBEN** usarse. Los tipos de error **DEBEN** permitir que el frontend discrimine y maneje cada caso.

**Correcto:**
```typescript
// Zod schema para input + output tipado
const CreateProductInput = z.object({ name: z.string(), price: z.number() });
type CreateProductOutput = { id: string; created: boolean };
```
**Incorrecto:**
```typescript
// Sin tipos, sin validacion
async function createProduct(data: any): Promise<any> { ... }
```

---

## 4. Datos: Capa de Persistencia

### 4.1 Base de Datos

Todo proyecto **DEBE** usar **PostgreSQL** como base de datos primaria.

- **Sobre-representacion en training data** (Axioma 2): Los LLMs generan SQL para PostgreSQL con precision notable. Queries complejas, CTEs, window functions, JSON operations: todo se genera correctamente con mayor frecuencia que con cualquier otra base.
- **pgvector** integrado nativamente para busqueda vectorial. Se habilita sin migrar de base de datos. HNSW indexes para busqueda aproximada de alta velocidad.
- PostgreSQL almacena datos relacionales, JSON (jsonb), vectores (pgvector), full-text search, geospatial (PostGIS). El proyecto **NO DEBERIA** agregar Redis para cache simple (existen unlogged tables), Elasticsearch para busqueda basica (existe tsvector), ni una base vectorial separada para menos de 10M vectores (existe pgvector).

Para escalas masivas de vectores (>10M), el proyecto **PUEDE** agregar Qdrant, Pinecone o Milvus como tier especializado.

### 4.2 ORM y Query Builders

| Lenguaje | ORM Primario | Alternativa | Axioma |
|---|---|---|---|
| **TypeScript** | Drizzle ORM (type-safe, cercano a SQL puro, declarativo) | Prisma (si el equipo prioriza DX sobre cercania a SQL) | 3 |
| **Python** | SQLAlchemy 2.0 (estilo de queries tipadas) | -- | 2 |

### 4.3 Embeddings y Busqueda Vectorial

No todo proyecto necesita embeddings. El stack **DEBE** permitir anadirlos sin reescritura cuando se requieran.

- **Abstraccion obligatoria:** Si el proyecto usa embeddings, **DEBE** definir una interfaz comun (`EmbeddingProvider`) que permita intercambiar modelos. El `model_id` **DEBE** almacenarse junto al vector.
- **Modelos recomendados:** OpenAI text-embedding-3-small/large como default. Cohere embed-v4 o Nomic embed como fallback open-source (soberania, Axioma 6).
- **Estrategia de migracion:** Re-indexacion progresiva en background cuando se cambia de modelo. Dual-read durante transicion.

**Correcto:** `{ vector: Float32Array, model_id: "text-embedding-3-small", created_at: "2026-02-24" }`
**Incorrecto:** `{ vector: Float32Array } // sin model_id, imposible saber con que modelo se genero`

### 4.4 Memoria de Agentes

Tres niveles que se activan progresivamente segun la complejidad del proyecto:

| Nivel | Duracion | Implementacion | Condicion de activacion |
|---|---|---|---|
| **Working Memory** | Sesion | Ventana de contexto del LLM | Cualquier interaccion con LLM |
| **Episodic Memory** | Dias-semanas | PostgreSQL + busqueda por fecha/contexto | El sistema necesita recordar interacciones pasadas |
| **Semantic Memory** | Permanente | pgvector + documentos indexados | El sistema necesita conocimiento de dominio persistente |

Cuando la aplicacion use LLMs, **DEBE** implementar compresion progresiva de ventana de contexto. Los mensajes antiguos **DEBEN** resumirse automaticamente cuando la ventana supere el 70% de capacidad. El resumen **DEBERIA** generarse con un modelo economico (Haiku, Flash, Mini).

---

## 5. Infraestructura y Operaciones

### 5.1 Principio de Soberania

Axioma 6 gobierna la infraestructura: control sobre datos, costos y capacidad de migracion. "Soberania" no significa "todo on-premise." Significa: el equipo entiende donde estan sus datos, cuanto paga y **PUEDE** migrar si el vendor cambia terminos.

| Componente | Decision | Justificacion |
|---|---|---|
| **Empaquetado** | Docker (contenedores inmutables) | Reproducibilidad. Lo que corre en dev corre en prod |
| **Infra base** | Depende del perfil (ver [-> 11. Tres Perfiles de Proyecto]) | Desde un VPS de $5/mes hasta Kubernetes multi-cloud |
| **Repositorio** | GitHub | Fuente unica de verdad. El LLM lee el repo para generar codigo coherente |
| **CI/CD** | GitHub Actions | Build, test, lint, deploy. Automatico en cada PR |
| **CD (GitOps)** | ArgoCD (cuando se necesita K8s) | Sincronizacion declarativa continua entre GitHub y produccion. Drift detection |
| **IaC** | Terraform / OpenTofu | Para proyectos que necesitan infra declarativa. No necesario para un VPS simple |
| **Secrets** | SOPS o Vault | Secrets **NO DEBEN** almacenarse en codigo. Variables de entorno como minimo. Vault para equipos grandes |

### 5.2 Pipeline de CI/CD

Todo proyecto **DEBE** tener el siguiente pipeline minimo, independientemente del tamano:

```
Push / PR
  -> lint (TypeScript compiler, Ruff para Python, ESLint)
  -> type check (tsc --noEmit)
  -> tests (vitest / pytest)
  -> build
  -> deploy (automatico a staging, manual a prod)
```

Todo proyecto que integre LLMs **DEBE** agregar al pipeline:

```
  -> validacion de schemas (JSON Schema de herramientas valido)
  -> evals de regresion (agente contra dataset de test)
  -> estimacion de costo (tokens por suite antes de ejecutar contra modelos de produccion)
```

### 5.3 Feature Flags

Para produccion seria, el proyecto **DEBERIA** usar un servicio de feature flags (LaunchDarkly, Unleash o Flagsmith). Para proyectos simples, un JSON en la DB o una tabla `feature_flags` **PUEDE** ser suficiente.

Los feature flags permiten deploy continuo sin riesgo: activar la feature para el 5% de usuarios, verificar que funciona, expandir.

---

## 6. Observabilidad

### 6.1 Stack Base

| Capa | Que observa | Herramientas | Obligatorio |
|---|---|---|---|
| **Infraestructura** | Server health, latencia, errores | OpenTelemetry + Prometheus + Grafana | **DEBE** existir al menos uptime monitoring |
| **Aplicacion** | Errores, performance, user flows | Sentry (errores), OpenTelemetry (traces) | **DEBE** existir |
| **LLM/Agente** | Costos, latencia, calidad de generacion | Langfuse (self-hosted) | **DEBE** existir si el proyecto usa LLMs |
| **Negocio** | Metricas de producto, conversion | PostHog / Plausible | **DEBERIA** existir |

### 6.2 Alerting

Todo proyecto **DEBE** tener alertas para: uptime, errores 5xx y latencia p95.

Todo proyecto que integre LLMs **DEBE** agregar alertas para:

- Degradacion de calidad de respuestas (hallucination rate).
- Incremento subito en costo por sesion (loops infinitos del agente).
- Caida en tool selection accuracy.
- Rate limiting de proveedores cercano al limite.

---

## 7. Seguridad

### 7.1 Baseline para Todo Proyecto

Todo proyecto **DEBE** cumplir estos requisitos de seguridad minimos:

- **HTTPS.** Sin excepciones. Todo trafico **DEBE** ir cifrado.
- **Autenticacion:** Auth.js (NextAuth) para proyectos TypeScript full-stack. Para APIs: JWT o API keys con rotacion.
- **Autorizacion:** Row-level security en PostgreSQL cuando los datos son multi-tenant.
- **Input validation:** Zod/Pydantic en cada boundary. El proyecto **NO DEBE** confiar en datos del cliente sin validacion.
- **Secrets:** **NO DEBEN** almacenarse en codigo. Variables de entorno como minimo.
- **Dependencies:** Dependabot o Renovate **DEBEN** configurarse para actualizaciones automaticas de dependencias con vulnerabilidades conocidas.

### 7.2 Seguridad para LLMs

Cuando la aplicacion integra LLMs, **DEBEN** implementarse los siguientes controles:

| Amenaza | Control | Implementacion |
|---|---|---|
| **Prompt Injection** | Separacion system/user | User input **NO DEBE** concatenarse en system prompts. Templates con placeholders tipados |
| **Agent-to-agent injection** | Sanitizacion inter-agente | El output de un agente **DEBE** tratarse como untrusted input para el siguiente. Validar contra schema en cada interfaz interna |
| **Output inseguro** | Todo output LLM = untrusted | Validar contra schema antes de ejecutar cualquier accion derivada |
| **Data leakage** | Clasificacion de datos | PII **NO DEBE** enviarse a LLMs externos si no es necesario. Scrubbing automatico |
| **Excessive agency** | Allowlists de herramientas | Toda herramienta invocable por LLM **DEBE** estar en allowlist explicito |
| **Costo descontrolado** | Budget enforcement | Limites por sesion/usuario. Circuit breaker si se excede |

### 7.3 Aislamiento de Ejecucion para Agentes

Cuando los agentes ejecutan herramientas que tocan el sistema operativo o servicios externos, **DEBE** aplicarse el nivel de aislamiento correspondiente:

| Nivel | Runtime | Permisos | Caso de uso |
|---|---|---|---|
| **Nivel 1 (Read)** | Container read-only | Filesystem RO, red restringida | Queries, lectura de APIs |
| **Nivel 2 (Write)** | Container efimero | Destruido post-ejecucion | Escritura a DB, generacion de archivos |
| **Nivel 3 (Shell)** | MicroVM (Firecracker) | Sin red externa, timeout estricto | Ejecucion de codigo arbitrario, tests |

**Correcto:** `Agente con permiso Write ejecuta en container efimero que se destruye post-ejecucion`
**Incorrecto:** `Agente con permiso Shell ejecuta en el host sin aislamiento ni timeout`

---

## 8. Flujo de Desarrollo AI-First

### 8.1 CLIs de Desarrollo

El equipo **DEBERIA** usar las siguientes herramientas de linea de comandos segun la tarea:

| Herramienta | Fortaleza | Cuando usarla |
|---|---|---|
| **Claude Code** | Refactorizaciones de contexto amplio, razonamiento multi-archivo | Cambios arquitectonicos, migraciones, features complejas que tocan multiples archivos |
| **Gemini CLI** | Contexto masivo (1M+ tokens), analisis multicapa | Revision de codigo completa, documentacion de sistemas existentes, analisis de logs |
| **Codex CLI** | Iteracion rapida en terminal, acceso a OS | Scripts, one-liners, operaciones de sistema, automatizacion rapida |

Las herramientas **NO** son mutuamente excluyentes. El equipo **DEBE** seleccionar la herramienta que mejor se adapte a cada tarea.

### 8.2 Principios del Desarrollo AI-First

Todo proyecto que use LLMs como co-desarrolladores **DEBE** adoptar estos principios:

- **Type-first development:** Tipos e interfaces **DEBEN** definirse ANTES de implementar. El LLM genera implementaciones mas correctas cuando tiene el contrato completo.

**Correcto:**
```typescript
// Definir tipo primero
interface Product { id: string; name: string; price: number; stock: number }
// Luego pedir: "implementa el CRUD de Product"
```
**Incorrecto:**
```
// Pedir "implementa el CRUD de productos" sin tipo previo
```

- **Small PRs:** Los LLMs **DEBEN** usarse para cambios pequenos y enfocados, no para refactorizaciones masivas.
- **Context engineering como practica diaria:** Archivos de contexto **DEBEN** mantenerse actualizados y el LLM **DEBE** consumirlos en cada sesion. Ver [-> 9. Context Engineering: La Nueva Disciplina].
- **Eval-driven (para agentes):** Los evals **DEBEN** escribirse antes de la implementacion. Los evals definen el comportamiento esperado. Es TDD para agentes.
- **Review todo lo generado:** Todo output de LLM **DEBE** revisarse como si viniera de un desarrollador junior brillante pero propenso a errores sutiles.

---

## 9. Context Engineering: La Nueva Disciplina

### 9.1 Definicion

Context engineering es el diseno, creacion y mantenimiento de los artefactos que alimentan la ventana de contexto del LLM para que produzca outputs correctos. Es documentacion tecnica escrita para ser consumida por maquinas ademas de humanos.

Un LLM de primera linea con context engineering pobre produce peor resultado que un LLM de segunda linea con context engineering excelente. Todo proyecto **DEBE** invertir en context engineering como multiplicador de calidad.

### 9.2 Artefactos de Context Engineering

Todo proyecto **DEBE** mantener al menos los artefactos marcados como obligatorios:

| Artefacto | Contenido | Obligatorio | Ejemplo para inventario de kiosco |
|---|---|---|---|
| **CONVENTIONS.md** | Estilo de codigo, patrones, naming, estructura de archivos | **DEBE** existir | "Usamos camelCase en TS, snake_case en Python. Server Actions en `app/actions/`. Componentes en `components/ui/`." |
| **ARCHITECTURE.md** | Diagrama de componentes, flujo de datos, decisiones clave | **DEBERIA** existir | "Next.js full-stack. PostgreSQL en Supabase. Auth con Auth.js. Deploy en Vercel." |
| **STACK.md** | Tecnologias, versiones, quirks conocidos | **DEBERIA** existir | "Next.js 15.1, Drizzle 0.38, PostgreSQL 16. Nota: Drizzle no soporta `returning()` en SQLite." |
| **SCHEMA.md** | Modelo de datos con relaciones | **DEBE** existir | "Productos -> Categorias (N:1). Movimientos de inventario con timestamp y usuario." |

Para proyectos mas complejos, **DEBERIAN** agregarse:

| Artefacto | Condicion de activacion |
|---|---|
| **INFRA.md** | Cuando existe infra propia (no solo PaaS) |
| **CONSTRAINTS.md** | Cuando hay restricciones de compliance, budget o regulatorias |
| **RUNBOOKS.md** | Cuando se opera produccion y se necesitan procedimientos de recuperacion |
| **AGENTS.md** | Cuando el proyecto incluye agentes IA con roles y permisos |

### 9.3 Economia del Contexto

La ventana de contexto tiene un precio literal (tokens) y un precio cognitivo (dilucion de atencion del modelo).

- **Regla 70/30:** El 70% de la ventana **DEBE** ser relevante para la tarea actual. El 30% restante es contexto de sistema. Si el ratio se invierte, el output se degrada.
- **Carga selectiva:** El proyecto **NO DEBE** cargar todos los artefactos en cada sesion. Un cambio de estilos necesita CONVENTIONS.md y los componentes afectados; no necesita INFRA.md.
- **Densidad:** Los context files **DEBEN** ser densos y sin redundancia. Cada palabra es un token que se paga.

**Correcto:** `"Usamos Drizzle ORM con PostgreSQL. Migraciones en drizzle/migrations/. Schema en src/db/schema.ts."` (20 tokens que ahorran 200 tokens de explicacion por sesion)
**Incorrecto:** `"En nuestro proyecto hemos decidido que vamos a utilizar Drizzle ORM como nuestra capa de acceso a datos porque nos parece que..."` (tokens desperdiciados en filler)

---

## 10. Capa de Agentes

Esta seccion se activa cuando el proyecto integra LLMs como parte de la funcionalidad: chatbots, asistentes, procesamiento inteligente, agentes autonomos.

### 10.1 Model Router

No todas las tareas requieren el mismo modelo. Todo proyecto con LLMs **DEBE** implementar routing de modelos por tier.

| Tier | Modelos (febrero 2026) | Costo relativo | Caso de uso |
|---|---|---|---|
| **T1 (Economico)** | Haiku 3.5, GPT-4o Mini, Flash 2.0, DeepSeek-V3 | $ | Clasificacion, formateo, resumenes, orquestacion |
| **T2 (Balance)** | Sonnet 4, GPT-4.1, Gemini 2.5 Pro | $$ | Generacion de codigo, analisis, tool-calling |
| **T3 (Frontier)** | Opus 4.5, GPT-4.5, Gemini Ultra | $$$ | Razonamiento complejo, planificacion, arquitectura |
| **T4 (Reasoning)** | o3, Gemini Thinking | $$$$ | Problemas matematicos, logicos, evaluacion critica |

**Implementacion:** LiteLLM proxy **DEBERIA** usarse como solucion base (interfaz OpenAI-compatible para todos los providers, fallback chains, budget tracking). Para el 100% de control: router custom con clasificador de complejidad.

**Budget enforcement:** Limites por sesion, por usuario y por agente **DEBEN** configurarse. Cuando se alcanza el limite, el sistema **DEBE** degradar al tier inferior con notificacion. Sin budget enforcement, un loop infinito de un agente **PUEDE** costar cientos de dolares en minutos.

### 10.2 Orquestacion de Agentes

El ecosistema de frameworks cambia cada 3 meses. Todo proyecto **DEBE** definir una capa de abstraccion (`AgentOrchestrator`) con metodos estandar (`route`, `execute_tool`, `manage_memory`). La implementacion concreta sobre el framework del momento **PUEDE** cambiar sin afectar agentes ni herramientas.

| Framework | Fortaleza | Caso de uso ideal |
|---|---|---|
| **OpenClaw** | Multi-agente nativo, multi-canal, persistencia local | Enjambres de agentes colaborativos |
| **LangGraph** | Flujos complejos con estado, visualizacion | Workflows multi-paso con branching |
| **Agents SDK (OpenAI)** | API limpia, handoffs nativos | Equipos centrados en GPT |
| **Custom** | Control total | Necesidades unicas |

### 10.3 Model Context Protocol (MCP)

MCP es el estandar para interoperabilidad de herramientas entre agentes. Las herramientas expuestas como MCP servers son consumibles desde Claude Code, Cursor, IDEs y el orquestador sin reescritura. Todo proyecto con agentes **DEBERIA** exponer sus herramientas como MCP servers.

### 10.4 Evals: El TDD de los Agentes

| Tipo | Que verifica | Obligatoriedad |
|---|---|---|
| **Regresion** | Calidad se mantiene ante cambios | **DEBE** ejecutarse pre-deploy |
| **Alucinacion** | Output no contiene informacion fabricada | **DEBE** ejecutarse pre-deploy |
| **Tool-calling** | Selecciona herramientas correctas | **DEBE** ejecutarse pre-deploy |
| **Costo** | Tokens en rango esperado | **DEBE** ejecutarse pre-deploy |
| **Seguridad** | No expone datos, no escala privilegios | **DEBE** ejecutarse pre-deploy |
| **Adversarial** | Resiste intentos de comprometerlo | **DEBERIA** ejecutarse cada ciclo |

**LLM-as-a-Judge:** Un modelo de otro provider **DEBE** evaluar la calidad. Si el agente usa Claude, el judge **DEBE** usar GPT. Diversidad de modelos reduce blind spots compartidos.

### 10.5 Modelos Fundacionales

El sistema es agnostico por diseno. Ninguna decision **DEBE** asumir un proveedor unico:

- **Claude (Anthropic):** Razonamiento, tool-calling preciso, instrucciones complejas.
- **Gemini (Google):** Contexto masivo (1M+), multimodalidad, eficiencia de costo.
- **GPT (OpenAI):** Ecosistema maduro, function calling robusto, reasoning (o-series).
- **Eficiencia (DeepSeek, Qwen):** Costo/rendimiento superior para T1. Self-hosteable.

Las capacidades, precios y disponibilidad de modelos cambian semanalmente. Todo proyecto con LLMs **DEBE** mantener un archivo `MODELS.md` como artefacto de context engineering: modelos permitidos, tiers asignados, precios actuales, benchmarks internos. El archivo **DEBE** actualizarse mensualmente o ante cada cambio significativo de provider. Tratar la informacion de modelos como dato estatico en un documento es un anti-patron.

### 10.6 Modos de Fallo del Stack

Todo equipo **DEBE** conocer y prevenir estos modos de fallo especificos de stacks con LLMs:

| Modo de fallo | Descripcion | Prevencion |
|---|---|---|
| **Model version drift** | Un provider actualiza el modelo y el comportamiento cambia. Tests pasan pero el output degrada en calidad, estilo o precision | Pinning de versiones de modelo cuando el provider lo permita. Evals de regresion ante cada cambio de modelo |
| **Embedding drift** | Los embeddings generados con una version de modelo no son compatibles con los generados con otra. La busqueda semantica degrada sin error visible | Regenerar embeddings completos ante cambios de modelo de embedding. Monitorear hit rate de busqueda semantica |
| **Corrupcion de memoria semantica** | Datos incorrectos entran en la memoria de agentes ([-> 4. Datos: Capa de Persistencia]) y se amplifican con el uso | Validacion de escritura en memoria. TTL para memorias. Mecanismo de purge manual. Auditoria periodica |
| **Cost explosion por loop** | Un agente entra en un loop de reintentos, consumiendo tokens sin converger. Prompt injection **PUEDE** provocar esto deliberadamente | Budget enforcement por sesion y por agente. Circuit breaker: si tokens consumidos > N*esperado, abort |
| **Context window overflow** | El contexto acumulado excede la ventana y el LLM empieza a olvidar instrucciones tempranas, generando output inconsistente | Monitoreo de uso de contexto. Summarization estrategica. Regla 70/30 de [-> 9. Context Engineering: La Nueva Disciplina] |
| **Provider downtime cascade** | El provider principal cae y no hay fallback configurado | LiteLLM con fallback a segundo provider. El proyecto **NO DEBE** depender de un solo provider para funcionalidad critica en produccion |

---

## 11. Stack Completo: Tabla de Referencia

### 11.1 Stack Base (Todo Proyecto)

| Capa | Tecnologia | Alternativa | Axioma |
|---|---|---|---|
| **Lenguaje frontend** | TypeScript | -- | 1, 2 |
| **Framework frontend** | Next.js (App Router) | Astro (estaticos) | 2, 3 |
| **Estilos** | Tailwind CSS | -- | 3 |
| **Componentes UI** | Shadcn/UI | Radix primitives | 2 |
| **Validacion** | Zod (TS) / Pydantic (Py) | -- | 1, 4 |
| **Backend (TS)** | Next.js Server Actions / Hono | tRPC | 3 |
| **Backend (Python)** | FastAPI | -- | 4 |
| **Base de datos** | PostgreSQL | -- | 2 |
| **ORM (TS)** | Drizzle | Prisma | 3 |
| **ORM (Python)** | SQLAlchemy 2.0 | -- | 2 |
| **Empaquetado** | Docker | -- | 5 |
| **Repositorio** | GitHub | GitLab | 2 |
| **CI/CD** | GitHub Actions | GitLab CI | 5 |
| **Observabilidad** | OpenTelemetry + Sentry | Datadog | 6 |
| **Auth** | Auth.js (NextAuth) | Clerk, Supabase Auth | 6 |

### 11.2 Stack Extendido (Proyectos con LLMs/Agentes)

| Capa | Tecnologia | Alternativa | Axioma |
|---|---|---|---|
| **Vectores** | pgvector (< 10M) | Qdrant (>10M) | 2 |
| **Embeddings** | OpenAI text-embedding-3 | Cohere, Nomic | 6 |
| **Observabilidad LLM** | Langfuse (self-hosted) | LangSmith | 6 |
| **Evals** | Braintrust / Arize Phoenix | TruLens | 4, 5 |
| **Model Router** | LiteLLM proxy / custom | -- | 5, 6 |
| **Orquestacion** | OpenClaw (tras abstraccion) | LangGraph, Agents SDK | 5 |
| **Interop** | MCP | -- | 5 |
| **Aislamiento** | gVisor / Firecracker | Docker rootless | 5 |
| **GitOps** | ArgoCD | Flux | 5 |
| **Feature flags** | Unleash / Flagsmith | LaunchDarkly | 6 |
| **Dev tools** | Claude Code + Gemini CLI + Codex CLI | Cursor, Windsurf | 2 |

---

## 12. Tres Perfiles de Proyecto

### 12.1 Perfil Minimo: "El Kiosco"

Inventario de kiosco, SaaS de agenda, portal de gestion interna. CRUD con logica de negocio. Sin agentes.

| Decision | Eleccion |
|---|---|
| **Stack** | TypeScript full-stack. Next.js + Server Actions + Drizzle + PostgreSQL |
| **Infra** | Vercel (frontend) + Supabase o Neon (PostgreSQL). O un VPS de $5-10/mes con Docker Compose |
| **CI/CD** | GitHub Actions: lint + type check + test + deploy |
| **Observabilidad** | Sentry (errores) + Vercel Analytics o Plausible |
| **Context engineering** | CONVENTIONS.md + SCHEMA.md. Dos archivos |
| **Desarrollo** | Un humano + Claude Code / Cursor |
| **Costo operativo mensual** | $5-50 |

### 12.2 Perfil Medio: "El SaaS con IA"

Plataforma con usuarios, pagos y capa de IA: chatbot de soporte, analisis inteligente de datos, generacion de contenido. LLMs integrados pero sin agentes autonomos.

| Decision | Eleccion |
|---|---|
| **Stack** | TypeScript (Next.js) + Python (FastAPI para capa IA). PostgreSQL + pgvector |
| **Infra** | Docker en VPS (Hetzner) o cloud manejado. ArgoCD si Kubernetes |
| **CI/CD** | GitHub Actions: lint + types + tests + evals de IA + deploy |
| **Model Router** | LiteLLM proxy con budget enforcement |
| **Observabilidad** | Sentry + Langfuse + Prometheus + Grafana |
| **Context engineering** | CONVENTIONS.md + ARCHITECTURE.md + STACK.md + SCHEMA.md |
| **Desarrollo** | 1-3 humanos + LLMs como co-developers |
| **Costo operativo mensual** | $50-500 |

### 12.3 Perfil Completo: "El Enjambre"

Sistema con agentes autonomos que ejecutan tareas, toman decisiones y se auto-optimizan. El escenario de [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia).

| Decision | Eleccion |
|---|---|
| **Stack** | Stack completo [-> 11. Stack Completo: Tabla de Referencia] (11.1 + 11.2). Dual language. Model Router custom |
| **Infra** | Kubernetes con ArgoCD. Firecracker para aislamiento de agentes. IaC con Terraform |
| **CI/CD** | Pipeline completo con evals (regresion, alucinacion, tool-calling, seguridad, adversarial) |
| **Model Router** | Custom con clasificador de complejidad + circuit breakers + budget enforcement |
| **Observabilidad** | Stack completo: OTEL + Prometheus + Grafana + Langfuse + alerting AI-native |
| **Context engineering** | Suite completa [-> 9. Context Engineering: La Nueva Disciplina]: CONVENTIONS, ARCHITECTURE, STACK, SCHEMA, INFRA, CONSTRAINTS, RUNBOOKS, AGENTS |
| **Desarrollo** | PO + Operador + enjambre ([Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia)) |
| **Costo operativo mensual** | $500-5000+ |

---

## 13. Conexion con el Corpus Xanpan::Agents

Este documento funciona de forma autonoma como stack de referencia para cualquier proyecto construido con asistencia de LLM. Cuando se usa en conjunto con el corpus Xanpan::Agents, forma parte de una trinidad:

```
+-----------------------------------------+
|        CHAPTER 0: El Operador           |
|        Solitario                        |
|   Bootstrap: DONDE empezar             |
|   (Punto de entrada al corpus)          |
+-----------------+-----------------------+
                  |
+-----------------+-----------------------+
|          STACK::LLM v1.0               |  <- Este documento
|   Arquitectura: CON QUE construir      |
|   (Universal, desde Fase 1)            |
+-----------------+-----------------------+
                  |
       +----------+----------+
       |                     |
+------+------+     +-------+---------+
| SWARM::OPS  |     | XANPAN::AGENTS  |
| v1.0        |     | v2.1            |
| Operaciones |     | Metodologia     |
| (Fase 3-4)  |     | (Fase 4)        |
+-------------+     +-----------------+
```

**Orden de lectura:** [Chapter 0](urn:fxsl:kb:chapter0-operador-solitario) -> STACK::LLM -> [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) -> [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia). Chapter 0 dice por donde empezar. STACK::LLM dice con que construir. Swarm::Ops dice como operar. Xanpan::Agents dice como gobernar.

STACK::LLM es universal: aplica a los tres perfiles de proyecto. [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia) y [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) se activan cuando el proyecto alcanza el Perfil Completo.

### 13.1 Mapa de Referencias para Perfil Completo

| Concepto | STACK::LLM | [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia) | [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) |
|---|---|---|---|
| Model Router | [-> 10. Capa de Agentes] (tiers, budget) | [Xanpan::Agents &sect;9.3](urn:fxsl:kb:xanpan-agents-metodologia) (conceptual) | -- |
| Evals | [-> 10. Capa de Agentes] (pipeline) | [Xanpan::Agents &sect;7.2](urn:fxsl:kb:xanpan-agents-metodologia) (practica obligatoria) | [Swarm::Ops &sect;4.3](urn:fxsl:kb:swarm-ops-metodologia) (CI insuficiente) |
| Context Engineering | [-> 9. Context Engineering: La Nueva Disciplina] (artefactos, economia) | [Xanpan::Agents &sect;2.2](urn:fxsl:kb:xanpan-agents-metodologia) (responsabilidad Operador) | -- |
| Seguridad | [-> 7. Seguridad] (OWASP, aislamiento) | [Xanpan::Agents &sect;13](urn:fxsl:kb:xanpan-agents-metodologia) (gobernanza) | [Swarm::Ops &sect;8](urn:fxsl:kb:swarm-ops-metodologia) (Security-by-Swarm) |
| Observabilidad | [-> 6. Observabilidad] (capas) | [Xanpan::Agents &sect;12](urn:fxsl:kb:xanpan-agents-metodologia) (dashboard 5D) | [Swarm::Ops &sect;7](urn:fxsl:kb:swarm-ops-metodologia) (agente-observer) |
| CI/CD | [-> 5. Infraestructura y Operaciones] (pipeline) | -- | [Swarm::Ops &sect;4](urn:fxsl:kb:swarm-ops-metodologia) (sistema nervioso) |
| Deploy | [-> 5. Infraestructura y Operaciones] (feature flags) | [Xanpan::Agents &sect;10.1](urn:fxsl:kb:xanpan-agents-metodologia) (aprobacion humana) | [Swarm::Ops &sect;4.2](urn:fxsl:kb:swarm-ops-metodologia) (flujos concurrentes) |
