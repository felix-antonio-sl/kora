---
_manifest:
  urn: urn:fxsl:kb:stack-llm-arquitectura-p02
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
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:stack-llm-arquitectura
---

# STACK::LLM v1.0 - Parte 02

## 9. Capa de Agentes (cuando el proyecto lo requiere)

**No todo proyecto necesita agentes.** Un inventario de kiosco no necesita un enjambre auto-evolutivo. Pero cuando tu proyecto sí integra LLMs como parte de la funcionalidad (chatbots, asistentes, procesamiento inteligente, agentes autónomos), esta capa se activa.

### 9.1 Model Router

No todas las tareas requieren el mismo modelo. Un resumen de texto no necesita Opus; Haiku lo resuelve. Una decisión arquitectónica compleja sí necesita Opus.

| Tier | Modelos (febrero 2026) | Costo relativo | Caso de uso |
|---|---|---|---|
| **T1 (Económico)** | Haiku 3.5, GPT-4o Mini, Flash 2.0, DeepSeek-V3 | $ | Clasificación, formateo, resúmenes, orquestación |
| **T2 (Balance)** | Sonnet 4, GPT-4.1, Gemini 2.5 Pro | $$ | Generación de código, análisis, tool-calling |
| **T3 (Frontier)** | Opus 4.5, GPT-4.5, Gemini Ultra | $$$ | Razonamiento complejo, planificación, arquitectura |
| **T4 (Reasoning)** | o3, Gemini Thinking | $$$$ | Problemas matemáticos, lógicos, evaluación crítica |

**Implementación práctica:** LiteLLM proxy como 80% de la solución. Interfaz OpenAI-compatible para todos los providers, fallback chains, budget tracking. Para el 100%: router custom con clasificador de complejidad.

**Budget enforcement:** Límites por sesión, por usuario, por agente. Cuando se alcanza el límite, degrada al tier inferior con notificación. Sin esto, un loop infinito de un agente te puede costar cientos de dólares en minutos.

### 9.2 Orquestación de agentes

El ecosistema cambia cada 3 meses. La respuesta correcta: **capa de abstracción.** Define una interfaz `AgentOrchestrator` con métodos estándar (`route`, `execute_tool`, `manage_memory`). Implementa sobre el framework del momento. Si el framework cambia, reescribes el adaptador, no los agentes ni las herramientas.

| Framework | Fortaleza | Caso de uso ideal |
|---|---|---|
| **OpenClaw** | Multi-agente nativo, multi-canal, persistencia local | Enjambres de agentes colaborativos |
| **LangGraph** | Flujos complejos con estado, visualización | Workflows multi-paso con branching |
| **Agents SDK (OpenAI)** | API limpia, handoffs nativos | Equipos centrados en GPT |
| **Custom** | Control total | Necesidades únicas |

### 9.3 Model Context Protocol (MCP)

MCP es el estándar para interoperabilidad de herramientas entre agentes. Las herramientas expuestas como MCP servers son consumibles desde Claude Code, Cursor, IDEs, y tu orquestador sin reescritura. Es HTTP para el mundo de agentes: infraestructura, no feature.

### 9.4 Evals: el TDD de los agentes

| Tipo | Qué verifica | Obligatorio? |
|---|---|---|
| **Regresión** | Calidad se mantiene ante cambios | Sí, pre-deploy |
| **Alucinación** | Output no contiene información fabricada | Sí, pre-deploy |
| **Tool-calling** | Selecciona herramientas correctas | Sí, pre-deploy |
| **Costo** | Tokens en rango esperado | Sí, pre-deploy |
| **Seguridad** | No expone datos, no escala privilegios | Sí, pre-deploy |
| **Adversarial** | Resiste intentos de romperlo | Recomendado, cada ciclo |

**LLM-as-a-Judge:** Un modelo de otro provider evalúa la calidad. Si tu agente usa Claude, el judge usa GPT. Diversidad de modelos reduce blind spots compartidos.

### 9.5 Modelos fundacionales

El sistema es agnóstico por diseño. Ninguna decisión asume un proveedor:

- **Claude (Anthropic):** Razonamiento, tool-calling preciso, instrucciones complejas.
- **Gemini (Google):** Contexto masivo (1M+), multimodalidad, eficiencia de costo.
- **GPT (OpenAI):** Ecosistema maduro, function calling robusto, reasoning (o-series).
- **Eficiencia (DeepSeek, Qwen):** Costo/rendimiento superior para T1. Self-hosteable.

> ⚡ **MODELS.md COMO ARTEFACTO VIVO**
>
> Las capacidades, precios, y disponibilidad de modelos cambian semanalmente. Esta lista es orientativa al momento de escritura (febrero 2026). La recomendación operativa es mantener un archivo `MODELS.md` en el repositorio del proyecto como artefacto de context engineering: modelos permitidos, tiers asignados, precios actuales, benchmarks internos. Este archivo se actualiza mensualmente (o ante cada cambio significativo de provider) y alimenta al Model Router. Tratar la información de modelos como dato estático en un documento es un anti-patrón; tratarla como artefacto versionado y actualizable es context engineering.

### 9.6 Modos de fallo del stack (prevención)

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

## 10. Stack Completo: La Tabla de Referencia

### 10.1 Stack base (todo proyecto)

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

### 10.2 Stack extendido (proyectos con LLMs/agentes)

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

## 11. Tres Perfiles de Proyecto

### 11.1 Perfil Mínimo: "El Kiosco"

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

### 11.2 Perfil Medio: "El SaaS con IA"

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

### 11.3 Perfil Completo: "El Enjambre"

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

## 12. Conexión con el Corpus Xanpan::Agents (opcional)

Este documento funciona de forma autónoma. Es un stack de referencia para cualquier proyecto construido con asistencia de LLM. Pero cuando se usa en conjunto con el corpus Xanpan::Agents, forma parte de una trinidad:

```
┌──────────────────────────────────────────┐
│ CHAPTER 0: El Operador │
│ Solitario │
│ Bootstrap: DÓNDE empezar │
│ (Punto de entrada al corpus) │
└────────────────┬─────────────────────────┘
 │
┌────────────────┴─────────────────────────┐
│ STACK::LLM v1.0 │ ← Este documento
│ Arquitectura: CON QUÉ construir │
│ (Universal, desde Fase 1) │
└────────────────┬─────────────────────────┘
 │
 ┌──────────┴──────────┐
 │ │
┌─────┴───────┐ ┌──────┴──────────┐
│ SWARM::OPS │ │ XANPAN::AGENTS │
│ v1.0 │ │ v2.1 │
│ Operaciones │ │ Metodología │
│ (Fase 3-4) │ │ (Fase 4) │
└─────────────┘ └─────────────────┘
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
