# Dev Stack Oficial — Agentes LLM

*Adoptado: 2026-02-24 | Fuente: "Stack de Desarrollo para Agentes LLM" (Claude/Anthropic, Feb 2026)*

---

## Axiomas fundacionales

1. **Tipado estático como guardrail cognitivo** — TypeScript + Pydantic interceptan errores de generación antes de runtime.
2. **Sobre-representación en entrenamiento** — Python, TypeScript, React, PostgreSQL maximizan coherencia del output LLM.
3. **Declaratividad > imperatividad** — SQL, JSX, Tailwind → menor tasa de error generativo.
4. **Contratos explícitos** — JSON Schema / OpenAPI limitan la superficie de alucinación.
5. **Resiliencia como requisito** — Circuit breakers, fallbacks, degradación graceful. Sin esto no es producción.
6. **Soberanía de datos** — Self-hosting donde sea posible. Routing inteligente para controlar costos.

---

## Stack completo (tabla de referencia)

| Capa | Tecnología principal | Alternativa |
|---|---|---|
| Frontend | TypeScript + Next.js (App Router) + Tailwind | Astro (sitios estáticos) |
| UI Components | Shadcn/UI | Radix primitives |
| Validación | Zod (TS) / Pydantic v2 (Python) | — |
| Backend API | FastAPI (Python) / Hono (TS) | tRPC (monorepo TS) |
| Base de datos | PostgreSQL + pgvector | Qdrant (>10M vectors) |
| ORM | Drizzle (TS) / SQLAlchemy 2.0 (Py) | Prisma (TS) |
| Orquestación | **OpenClaw** (tras capa de abstracción) | LangGraph, Agents SDK |
| Interop Tools | MCP (Model Context Protocol) | — |
| Model Router | Custom (clasificador + circuit breaker) | LiteLLM proxy |
| Embeddings | OpenAI text-embedding-3-small/large + abstracción | Cohere, Nomic (fallback) |
| Observabilidad | Langfuse + OpenTelemetry + Grafana | LangSmith |
| Evals | Arize Phoenix + datasets custom | TruLens, Braintrust |
| Infra | Docker + Ubuntu LTS (Hetzner) | — |
| CI/CD | GitHub Actions + ArgoCD | — |
| Seguridad sandbox | gVisor/Firecracker + allowlists | — |
| Dev Tools | Claude Code + Gemini CLI + Codex CLI | — |
| IaC | Terraform | — |
| Secrets | SOPS o Vault | — |

---

## Model Router — Tiers

| Tier | Modelos | Uso |
|---|---|---|
| 1 (Económico) | Haiku 4.5, GPT-4o Mini, Flash 2.0 | Clasificación, extracción, formateo, queries simples |
| 2 (Balance) | Sonnet 4.5, GPT-4.1, Gemini Pro | Tool-calling complejo, síntesis, código estándar |
| 3 (Frontera) | Opus 4.5+, GPT-4.5/o3, Gemini Ultra | Razonamiento multi-paso, análisis crítico, planificación |
| 4 (Pensamiento) | o3, Gemini Flash Thinking | Problemas matemáticos/lógicos complejos, evaluación |

Impacto esperado: 40–70% reducción de costos LLM en producción con router bien implementado.

---

## Memoria del agente — 3 niveles

| Tipo | Persistencia | Implementación |
|---|---|---|
| Sesión | Dura una conversación | Contexto LLM + buffer FIFO |
| Episódica | Días a semanas | PostgreSQL + resumen automático |
| Semántica | Permanente | pgvector + grafos de conocimiento |

Compresión progresiva al 70% de ventana de contexto → resumen con modelo Tier 1.

---

## AgentSkills — Contrato formal de herramienta

Cada herramienta debe declarar: `name`, `input_schema`, `output_schema`, `timeout_ms`, `retry_policy`, `idempotent`, `risk_level`, `requires_approval`.

**Regla crítica:** Herramientas destructivas (borrar datos, enviar emails, ejecutar transacciones) SIEMPRE requieren aprobación humana explícita.

---

## Orquestación — Patrón de abstracción

Definir interfaz `AgentOrchestrator` con métodos estándar (`route`, `execute_tool`, `manage_memory`). Implementar sobre el framework elegido. Si el framework cambia, solo se reescribe el adaptador.

**OpenClaw es el framework primario** — gestión nativa multi-agente, integración multi-canal, persistencia local.

---

## MCP (Model Context Protocol)

Las AgentSkills deben exponerse como MCP servers. Permite que las mismas herramientas sean consumibles desde Claude Code, Cursor, IDEs, y el orquestador sin reescritura.

---

## Seguridad — Niveles de sandbox

- **Nivel 1 (Lectura):** Docker + filesystem read-only + red restringida.
- **Nivel 2 (Escritura):** Contenedor efímero con gVisor/Firecracker, destruido tras cada ejecución.
- **Nivel 3 (OS Shell):** MicroVM dedicada + timeout + sin red externa + logs completos.

**Regla de oro:** El agente nunca tiene más permisos de los estrictamente necesarios para su tarea actual.

---

## Pipeline CI/CD AI-Native

Pasos adicionales vs. CI tradicional:
1. Validación de schemas (JSON Schema válido en tool definitions)
2. Tests de regresión de agentes (Evals con datasets predefinidos)
3. Cost estimation pre-producción
4. Drift detection con ArgoCD

---

## Desarrollo AI-First — Principios

- **Context engineering:** mantener `CONVENTIONS.md`, `ARCHITECTURE.md` actualizados.
- **Type-first:** definir tipos/interfaces antes de implementar.
- **Small PRs:** cambios atómicos y revisables.
- **Eval-driven:** escribir evals antes de la implementación (análogo a TDD).

---

## Modelos fundacionales soportados

- **Claude (Anthropic):** razonamiento, tool-calling de alta precisión.
- **Gemini (Google):** contexto masivo, multimodalidad nativa, eficiencia de costo.
- **GPT (OpenAI):** ecosistema maduro, function calling robusto, o-series reasoning.
- **Eficiencia (DeepSeek, Qwen):** costo/rendimiento superior para inferencias lógicas/matemáticas.
