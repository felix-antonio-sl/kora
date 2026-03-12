---
_manifest:
  urn: "urn:fxsl:kb:stack-llm-arquitectura"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-11"
    source: "stack-llm-v1-arquitectura.md (source/fxsl/xanpan)"
version: "1.0.0"
status: draft
tags: [stack-llm, arquitectura, llm, desarrollo, agentes]
lang: es
extensions:
  fxsl:
    family: methodology
---

# STACK::LLM v1.0

Arquitectura de referencia para construir software con LLMs como co-desarrolladores. Aplica desde un CRUD simple hasta un sistema multi-agente. Criterios dominantes: reducir errores de generación, preservar soberanía técnica y controlar costos.

## 0. Axiomas fundacionales

| Axioma | Tesis | Consecuencia de stack |
| --- | --- | --- |
| Tipado estático | el tipo es guardrail cognitivo | TypeScript + Pydantic + Zod |
| Sobre-representación en training data | tecnologías dominantes generan menos alucinación estructural | React, TypeScript, Python, PostgreSQL |
| Declaratividad > imperatividad | los LLMs generan mejor estados deseados que secuencias manuales | SQL, React, Tailwind, IaC declarativa |
| Contratos explícitos | schemas limitan la creatividad peligrosa | JSON Schema, OpenAPI, Zod, Pydantic |
| Resiliencia arquitectónica | sin tests/lint/CI el sistema es demo | pipeline obligatorio desde el día 1 |
| Soberanía y costo | dependencia unilateral de vendor es fragilidad | self-hosting donde tenga sentido, routing y budgets |

## 1. Frontend

### 1.1 Core recomendado

| Capa | Opción principal | Motivo |
| --- | --- | --- |
| Lenguaje | TypeScript | detecta errores de generación antes de runtime |
| Framework | React + Next.js App Router | máxima cobertura en training data + server components + server actions |
| Sitios estáticos | Astro | solo si no se requiere interactividad rica |

Decisiones clave:

- `TypeScript` captura propiedades faltantes, contratos rotos y tipos incompatibles.
- `React` ofrece mayor repertorio de patrones internalizados por los modelos.
- `Next.js` reduce superficie al unificar UI, routing y acciones del servidor.

### 1.2 UI y estilos

| Decisión | Motivo |
| --- | --- |
| Tailwind CSS | clases atómicas, predecibles y fáciles de generar correctamente |
| Shadcn/UI | componentes accesibles y tipados dentro del repo, no ocultos en `node_modules` |

### 1.3 Validación y estado

Recomendaciones:

- `Zod` como contrato unificado frontend/backend en TypeScript
- `TanStack Query` para estado de servidor, cache y optimistic updates

Patrón:

```ts
const ProductSchema = z.object({
  name: z.string().min(1),
  price: z.number().positive(),
  stock: z.number().int().nonnegative(),
})
```

Un schema define formulario, validación de acción y tipos derivados.

## 2. Backend

### 2.1 División de responsabilidades por lenguaje

| Lenguaje | Rol | Cuándo usarlo |
| --- | --- | --- |
| TypeScript | lógica de producto, BFF, CRUD, dashboards, APIs internas | por defecto en proyectos web |
| Python | capa cognitiva, tool-calling, procesamiento de datos, ML | cuando hay IA en producción |

Regla:

- proyectos simples: TypeScript full-stack
- proyectos con cognición real: TypeScript para producto + Python para IA

### 2.2 FastAPI

Usar `FastAPI` cuando se necesita:

- tool-calling basado en `Pydantic -> JSON Schema`
- APIs consumidas por otros sistemas
- procesamiento intensivo de datos o integración con ecosistema ML

No usarlo en CRUDs simples donde `Next.js Server Actions` cubren el caso.

### 2.3 Diseño de APIs y herramientas

Invariantes:

- schema tipado para input y output
- validación previa a cualquier side effect
- docstrings/JSDoc legibles por humanos y LLMs
- errores tipados, no strings arbitrarios

## 3. Persistencia y memoria

### 3.1 Base de datos por defecto

`PostgreSQL` para el 95% de los casos.

Razones:

- excelente generación de SQL por LLMs
- `jsonb`, full-text search, `pgvector`, `PostGIS`
- permite crecer sin fragmentar storage demasiado pronto

### 3.2 ORM y acceso a datos

| Lenguaje | Opción | Motivo |
| --- | --- | --- |
| TypeScript | Drizzle | type-safe, cercano a SQL, legible para LLM |
| Python | SQLAlchemy 2.0 | estándar maduro para servicios Python |

### 3.3 Embeddings y búsqueda vectorial

Activar solo cuando el producto lo exija.

Reglas:

- guardar siempre `model_id` junto al vector
- abstraer provider con interfaz estable
- `pgvector` es suficiente hasta ~10M vectores
- sobre ese umbral, evaluar Qdrant, Pinecone o Milvus

Embeddings recomendados:

- OpenAI `text-embedding-3-*` como default
- Cohere o Nomic como alternativas

### 3.4 Memoria de agentes

| Nivel | Duración | Implementación | Uso |
| --- | --- | --- | --- |
| Working memory | sesión | ventana de contexto | cualquier interacción LLM |
| Episodic memory | días-semanas | PostgreSQL con búsqueda contextual | recordar interacciones pasadas |
| Semantic memory | persistente | documentos + `pgvector` | conocimiento de dominio recuperable |

Regla operativa:

- resumir conversación cuando la ventana exceda ~70% de capacidad
- usar modelos económicos para compresión de contexto

## 4. Infraestructura y operaciones

### 4.1 Principio de soberanía

Soberanía no implica on-premise obligatorio. Implica:

- saber dónde viven datos y secretos
- saber cuánto cuesta cada capa
- poder migrar sin rehacer el sistema completo

### 4.2 Stack operativo mínimo

| Función | Opción |
| --- | --- |
| Empaquetado | Docker |
| Repo | GitHub |
| CI/CD | GitHub Actions |
| GitOps en K8s | ArgoCD |
| IaC | Terraform / OpenTofu |
| Secrets | variables de entorno, SOPS o Vault |

Pipeline base:

```text
push / PR
  -> lint
  -> type check
  -> tests
  -> build
  -> deploy
```

Agregar para proyectos con IA:

- validación de schemas de herramientas
- evals de regresión
- estimación o control de costo antes de ejecutar suites caras

### 4.3 Feature flags

`Feature flags` son red de seguridad para deploy continuo.

Opciones:

- tabla simple en DB para proyectos pequeños
- Unleash / Flagsmith / LaunchDarkly en entornos serios

## 5. Observabilidad

### 5.1 Capas

| Capa | Qué observa | Herramientas |
| --- | --- | --- |
| Infraestructura | salud del servidor, latencia, errores | OTEL + Prometheus + Grafana |
| Aplicación | errores, performance, flujos | Sentry + OTEL |
| LLM/Agente | costo, latencia, calidad | Langfuse |
| Negocio | uso, conversión, producto | PostHog / Plausible |

### 5.2 Alertas mínimas

Para todo proyecto:

- uptime
- errores 5xx
- latencia p95

Para proyectos con LLM:

- degradación de calidad
- alza súbita de costo por sesión
- caída de `tool selection accuracy`
- rate limiting cercano al límite

## 6. Seguridad

### 6.1 Baseline universal

- HTTPS siempre
- autenticación: Auth.js o JWT/API keys según arquitectura
- autorización: RLS en PostgreSQL para multi-tenant
- validación en cada boundary
- secrets fuera del código
- Dependabot o Renovate para vulnerabilidades conocidas

### 6.2 Controles específicos para LLM

| Amenaza | Control |
| --- | --- |
| prompt injection | separar `system` y `user`; usar templates tipados |
| agent-to-agent injection | tratar output inter-agente como input no confiable |
| output inseguro | validar contra schema antes de ejecutar acciones |
| data leakage | clasificación y scrubbing automático |
| excessive agency | allowlists explícitas de herramientas |
| costo descontrolado | límites por sesión, usuario y agente |

### 6.3 Aislamiento de ejecución

| Nivel | Runtime | Caso de uso |
| --- | --- | --- |
| Read | container read-only | queries y lecturas |
| Write | container efímero | escritura controlada |
| Shell | microVM tipo Firecracker | ejecución arbitraria y tests peligrosos |

## 7. Flujo de desarrollo AI-first

### 7.1 Herramientas de desarrollo

| Herramienta | Fortaleza |
| --- | --- |
| Claude Code | refactorizaciones de contexto amplio |
| Gemini CLI | contexto masivo y análisis multicapa |
| Codex CLI | iteración rápida de terminal y SO |

No son excluyentes.

### 7.2 Principios

- `type-first development`
- PRs pequeños
- context engineering mantenido como práctica diaria
- eval-driven cuando se construyen agentes
- review humano de todo lo generado

## 8. Context engineering

### 8.1 Definición

Disciplina de diseñar y mantener artefactos que alimentan la ventana de contexto del LLM. Su función es producir salidas correctas y coherentes con el proyecto.

### 8.2 Artefactos

| Archivo | Contenido |
| --- | --- |
| `CONVENTIONS.md` | estilo, patrones, naming, estructura |
| `ARCHITECTURE.md` | componentes, flujos, decisiones clave |
| `STACK.md` | tecnologías, versiones, quirks |
| `SCHEMA.md` | modelo de datos |
| `INFRA.md` | topología operacional |
| `CONSTRAINTS.md` | budget, compliance, límites |
| `RUNBOOKS.md` | recuperación operativa |
| `AGENTS.md` | roles, modelos, permisos |

### 8.3 Economía del contexto

Reglas:

- 70% del contexto debe ser relevante para la tarea actual
- no cargar todo en cada sesión
- cada línea del contexto debe ahorrar más tokens de los que consume

## 9. Capa de agentes

### 9.1 Model Router

| Tier | Perfil | Casos de uso |
| --- | --- | --- |
| T1 | económico | clasificación, formato, resúmenes |
| T2 | balance | generación de código, análisis, tool-calling |
| T3 | frontier | arquitectura, planificación compleja |
| T4 | reasoning | lógica dura, evaluación crítica |

Implementación práctica:

- LiteLLM cubre ~80% del problema
- routers custom se justifican con escala, budgets complejos o políticas más finas

### 9.2 Orquestación

Regla estructural: exponer una interfaz propia `AgentOrchestrator` y conectar frameworks detrás.

| Opción | Fortaleza |
| --- | --- |
| OpenClaw | multi-agente colaborativo |
| LangGraph | workflows con estado y branching |
| Agents SDK | handoffs simples |
| custom | control total |

### 9.3 MCP

`Model Context Protocol` es la capa estándar para interoperabilidad de herramientas. Tratarlo como infraestructura, no como feature opcional.

### 9.4 Evals

| Tipo | Obligación |
| --- | --- |
| regresión | obligatoria |
| alucinación | obligatoria |
| tool-calling | obligatoria |
| costo | obligatoria |
| seguridad | obligatoria |
| adversarial | recomendada por ciclo |

Regla de diversidad: el juez debe usar modelo distinto al autor.

### 9.5 Modelos fundacionales

Orientación:

- Claude: razonamiento y tool-calling preciso
- Gemini: contexto masivo y multimodalidad
- GPT: ecosistema maduro y function calling fuerte
- modelos eficientes/open: T1 o soberanía

Mantener `MODELS.md` versionado con:

- modelos permitidos
- tiers
- precios
- benchmarks internos

### 9.6 Modos de fallo del stack

| Modo de fallo | Prevención |
| --- | --- |
| model drift | pinning y evals de regresión |
| embedding drift | reindexado controlado y monitoreo |
| corrupción de memoria | validación, TTL, purge, auditoría |
| loop de costo | budgets y circuit breaker |
| overflow de contexto | monitoreo y summarization |
| caída de provider | fallback multi-provider |

## 10. Tabla de referencia

### 10.1 Stack base

| Capa | Tecnología | Alternativa | Axioma |
| --- | --- | --- | --- |
| Lenguaje frontend | TypeScript | - | 1, 2 |
| Framework frontend | Next.js (App Router) | Astro (estáticos) | 2, 3 |
| Estilos | Tailwind CSS | - | 3 |
| Componentes UI | Shadcn/UI | Radix primitives | 2 |
| Validación | Zod (TS) / Pydantic (Py) | - | 1, 4 |
| Backend (TS) | Next.js Server Actions / Hono | tRPC | 3 |
| Backend (Python) | FastAPI | - | 4 |
| Base de datos | PostgreSQL | - | 2 |
| ORM (TS) | Drizzle | Prisma | 3 |
| ORM (Python) | SQLAlchemy 2.0 | - | 2 |
| Empaquetado | Docker | - | 5 |
| Repositorio | GitHub | GitLab | 2 |
| CI/CD | GitHub Actions | GitLab CI | 5 |
| Observabilidad | OpenTelemetry + Sentry | Datadog | 6 |
| Auth | Auth.js (NextAuth) | Clerk, Supabase Auth | 6 |

### 10.2 Stack extendido

| Capa | Tecnología | Alternativa | Axioma |
| --- | --- | --- | --- |
| Vectores | pgvector (< 10M) | Qdrant (>10M) | 2 |
| Embeddings | OpenAI text-embedding-3 | Cohere, Nomic | 6 |
| Observabilidad LLM | Langfuse (self-hosted) | LangSmith | 6 |
| Evals | Braintrust / Arize Phoenix | TruLens | 4, 5 |
| Model Router | LiteLLM proxy / custom | - | 5, 6 |
| Orquestación | OpenClaw (tras abstracción) | LangGraph, Agents SDK | 5 |
| Interop | MCP | - | 5 |
| Aislamiento | gVisor / Firecracker | Docker rootless | 5 |
| GitOps | ArgoCD | Flux | 5 |
| Feature flags | Unleash / Flagsmith | LaunchDarkly | 6 |
| Dev tools | Claude Code + Gemini CLI + Codex CLI | Cursor, Windsurf | 2 |

## 11. Tres perfiles de proyecto

### 11.1 Perfil mínimo: "El Kiosco"

Un inventario de kiosco. Un SaaS de agenda. Un portal de gestión interna. CRUD con algo de lógica de negocio. Sin agentes.

| Decisión | Elección |
| --- | --- |
| Stack | TypeScript full-stack. Next.js + Server Actions + Drizzle + PostgreSQL |
| Infra | Vercel (frontend) + Supabase o Neon (PostgreSQL). O un VPS de USD 5-10/mes con Docker Compose |
| CI/CD | GitHub Actions: lint + type check + test + deploy |
| Observabilidad | Sentry (errores) + Vercel Analytics o Plausible |
| Context engineering | `CONVENTIONS.md` + `SCHEMA.md`. Dos archivos |
| Desarrollo | Un humano + Claude Code / Cursor |
| Costo operativo mensual | USD 5-50 |

### 11.2 Perfil medio: "El SaaS con IA"

Una plataforma con usuarios, pagos y una capa de IA: chatbot de soporte, análisis inteligente de datos, generación de contenido. LLMs integrados pero no agentes autónomos.

| Decisión | Elección |
| --- | --- |
| Stack | TypeScript (Next.js) + Python (FastAPI para capa IA). PostgreSQL + pgvector |
| Infra | Docker en VPS (Hetzner) o cloud manejado. ArgoCD si Kubernetes |
| CI/CD | GitHub Actions: lint + types + tests + evals de IA + deploy |
| Model Router | LiteLLM proxy con budget enforcement |
| Observabilidad | Sentry + Langfuse + Prometheus + Grafana |
| Context engineering | `CONVENTIONS.md` + `ARCHITECTURE.md` + `STACK.md` + `SCHEMA.md` |
| Desarrollo | 1-3 humanos + LLMs como co-developers |
| Costo operativo mensual | USD 50-500 |

### 11.3 Perfil completo: "El Enjambre"

Un sistema con agentes autónomos que ejecutan tareas, toman decisiones y se auto-optimizan. El escenario de `Xanpan::Agents`.

| Decisión | Elección |
| --- | --- |
| Stack | Stack completo §10.1 + §10.2. Dual language. Model Router custom |
| Infra | Kubernetes con ArgoCD. Firecracker para aislamiento de agentes. IaC con Terraform |
| CI/CD | Pipeline completo con evals: regresión, alucinación, tool-calling, seguridad, adversarial |
| Model Router | Custom con clasificador de complejidad + circuit breakers + budget enforcement |
| Observabilidad | Stack completo: OTEL + Prometheus + Grafana + Langfuse + alerting AI-native |
| Context engineering | Suite completa §8.2: `CONVENTIONS`, `ARCHITECTURE`, `STACK`, `SCHEMA`, `INFRA`, `CONSTRAINTS`, `RUNBOOKS`, `AGENTS` |
| Desarrollo | `PO + Operador + enjambre` |
| Costo operativo mensual | USD 500-5000+ |

## 12. Relación con el corpus Xanpan

Este documento funciona de forma autónoma. Es un stack de referencia para cualquier proyecto construido con asistencia de LLM. Cuando se usa junto al corpus `Xanpan::Agents`, forma parte de una trinidad:

```text
CHAPTER 0: El Operador Solitario
  Bootstrap: dónde empezar
    |
    +-- STACK::LLM v1.0
    |     Arquitectura: con qué construir
    |     Universal, desde Fase 1
    |
    +-- SWARM::OPS v1.0
    |     Operaciones
    |     Fase 3-4
    |
    +-- XANPAN::AGENTS v2.1
          Metodología
          Fase 4
```

Orden recomendado: `Chapter 0 -> STACK::LLM -> Swarm::Ops -> Xanpan::Agents`.

`STACK::LLM` es universal. `Swarm::Ops` y `Xanpan::Agents` se activan cuando el proyecto alcanza el Perfil Completo.

Mapa de referencias para Perfil Completo:

| Concepto | STACK::LLM | Xanpan::Agents | Swarm::Ops |
| --- | --- | --- | --- |
| Model Router | §9.1 | §9.3 | - |
| Evals | §9.4 | §7.2 | §4.3 |
| Context Engineering | §8 | §2.2 | - |
| Seguridad | §6 | §13 | §8 |
| Observabilidad | §5 | §12 | §7 |
| CI/CD | §4.2 | - | §4 |
| Deploy | §4.3 | §10.1 | §4.2 |
