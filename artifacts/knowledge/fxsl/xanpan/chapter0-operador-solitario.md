---
_manifest:
  urn: urn:fxsl:kb:chapter0-operador-solitario
  provenance:
    created_by: kora/curator
    created_at: '2026-02-25'
    source: source/fxsl/xanpan/chapter0-operador-solitario.md
version: 1.1.0
status: published
tags:
- xanpan
- operador-solitario
- bootstrap
- llm
- agentes
- infrastructure
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:chapter0-operador-solitario
---

# CHAPTER 0: EL OPERADOR SOLITARIO


Bootstrap Path para Desarrollo Asistido por LLM — De una Persona a un Enjambre

---

## 0. Premisa: Por qué este documento existe

Los tres documentos del corpus — STACK::LLM, Swarm::Ops, Xanpan::Agents — describen un sistema maduro. Presuponen infraestructura existente, agentes operativos, pipelines de evals, y al menos dos roles humanos diferenciados (Product Owner y Operador). Son correctos pero incompletos: describen el destino sin trazar la ruta desde el origen.

El lector típico de Chapter 0 es una persona que cumple todas estas condiciones simultáneamente:

- Tiene capacidad técnica suficiente para escribir código y gestionar infraestructura básica.
- Tiene acceso a LLMs de frontera (API keys, suscripciones a Claude Pro, ChatGPT Plus, o equivalentes).
- Tiene un VPS o acceso a cloud computing básico.
- No tiene equipo. No tiene presupuesto para un equipo. Es, por ahora, una persona sola.

Esta persona es el **Operador Solitario.** No es un rol degradado ni una versión empobrecida del equipo descrito en Xanpan::Agents. Es el estado legítimo de inicio de cualquier proyecto de software asistido por LLM.

> ⚡ **EL PRINCIPIO DE ARRANQUE**
>
> Ningún enjambre nació como enjambre. Todo sistema complejo empezó como una persona resolviendo un problema concreto. Chapter 0 respeta esa realidad: no pide infraestructura que no tienes, no asume roles que no puedes llenar, y no impone ceremonias que serían absurdas para un equipo de uno. Lo que sí hace es asegurar que cada decisión que tomes sea compatible con el crecimiento futuro, de modo que cuando necesites escalar, no tengas que reescribir desde cero.

---

## 1. El Operador Solitario como rol legítimo

### 1.1 La violación consciente: dual-hat

Xanpan::Agents §2 define dos roles humanos distintos:

- **Product Owner (PO):** Decide qué construir. Define valor de negocio. Prioriza backlog. Negocia scope.
- **Operador:** Decide cómo construir. Configura agentes. Optimiza pipelines. Gestiona infraestructura.

En Xanpan clásico, la separación es obligatoria porque las tensiones entre "qué" y "cómo" son reales y productivas. Un PO que también opera tiende a optimizar la técnica a expensas del negocio (o viceversa).

El Operador Solitario viola esta separación conscientemente. No porque la separación sea incorrecta, sino porque el coste de dos personas para un proyecto embrionario es prohibitivo.

La compensación es disciplina: el Operador Solitario debe alternar sombreros explícitamente.

**Sombrero PO (cuándo):** Al inicio de cada ciclo de trabajo, al definir qué historias abordar, al decidir si un feature ship o necesita más iteración, al hablar con usuarios o stakeholders.

**Sombrero Operador (cuándo):** Al configurar herramientas, al interactuar con agentes LLM, al resolver problemas técnicos, al optimizar prompts, al gestionar infraestructura.

La disciplina está en no mezclar: cuando llevas el sombrero PO, priorizas por valor de negocio sin dejarte seducir por la elegancia técnica. Cuando llevas el sombrero Operador, optimizas la ejecución sin cuestionar las prioridades que ya definiste como PO.

### 1.2 El PCA como compensador

El **Pensamiento Cíclico Asíncrono** — la estructura temporal de Xanpan::Agents §4 con ciclos de 2-4 semanas y flujo continuo dentro — funciona naturalmente para el Operador Solitario. No hay ceremonias de coordinación porque no hay equipo que coordinar. El ciclo se reduce a:

1. **Inicio de ciclo (sombrero PO):** Revisa OKRs, selecciona historias para el ciclo, prioriza.
2. **Ejecución (sombrero Operador):** Trabaja con LLMs para implementar historias. Flujo continuo.
3. **Cierre de ciclo (ambos sombreros):** ¿Se entregó valor? ¿Se cumplieron los KRs? ¿Qué aprendí?

La retrospectiva del Operador Solitario es un documento de 5-10 líneas al final de cada ciclo. No es una reunión; es una reflexión escrita que alimenta el siguiente ciclo.

---

## 2. Fase 0: Cimientos (Día 1)

**Objetivo:** Tener un entorno de desarrollo funcional donde puedas construir cualquier cosa con asistencia de LLM.

**Lo que necesitas:**

| Componente | Elección | Coste |
|---|---|---|
| **Máquina local** | Tu computadora actual (cualquier OS) | Ya la tienes |
| **Editor** | VS Code o Cursor | Gratis / $20/mes |
| **CLI de LLM** | Claude Code + Gemini CLI (ambos) | API usage |
| **Control de versiones** | GitHub (repo privado) | Gratis |
| **Runtime** | Node.js LTS + Python 3.11+ | Gratis |
| **Package managers** | pnpm (Node), uv (Python) | Gratis |
| **VPS** | Hetzner CX22 o equivalente (2 vCPU, 4GB RAM) | ~€4-8/mes |
| **Dominio** | Uno. Para tu proyecto. | ~$12/año |

**Lo que NO necesitas todavía:**

- Kubernetes
- ArgoCD
- Terraform
- Langfuse
- Feature flags
- Model Router
- Nada del stack extendido de STACK::LLM §10.2

**Acciones concretas de Día 1:**

1. Instala Node.js LTS, Python 3.11+, Docker Desktop, Git.
2. Configura GitHub con SSH keys.
3. Instala Claude Code (`npm install -g @anthropic-ai/claude-code`) y configura tu API key.
4. Instala Gemini CLI como segunda opinión.
5. Crea un repo en GitHub para tu proyecto.
6. En tu VPS: instala Docker y Docker Compose. Configura SSH con key-only auth. Configura firewall básico (ufw: solo 22, 80, 443).
7. Escribe tu primer archivo de context engineering: `CONVENTIONS.md` (ver §7).

**Resultado:** Puedes sentarte frente a tu computadora, abrir Claude Code, y empezar a construir. El VPS está listo para recibir deploys.

---

## 3. Fase 1: El Primer Proyecto (Semana 1)

**Objetivo:** Construir y desplegar algo funcional. Cualquier cosa. El tamaño no importa; la completitud sí.

### 3.1 Elige el Perfil Mínimo de STACK::LLM

Tu primer proyecto usa exclusivamente el **Perfil Mínimo** de STACK::LLM §11.1:

- **Stack:** TypeScript full-stack. Next.js + Server Actions + Drizzle ORM + PostgreSQL.
- **Infraestructura:** Docker Compose en tu VPS. Nginx como reverse proxy. Let's Encrypt para HTTPS.
- **CI/CD:** GitHub Actions con un workflow simple: push → build → test → deploy via SSH.
- **Base de datos:** PostgreSQL en un contenedor Docker. Backup diario con pg_dump a un volumen local (y opcionalmente a object storage).

No hay capa Python. No hay FastAPI. No hay agentes. Es un monolito TypeScript desplegado con Docker Compose. Esto no es una limitación; es lo correcto para esta fase.

### 3.2 El flujo de trabajo

```
1. [Sombrero PO] Define 3-5 historias para la primera semana
2. [Sombrero Operador] Abre Claude Code en tu repo
3. Dale contexto: "Lee CONVENTIONS.md. Implementa esta historia: [descripción]"
4. Revisa el output. Itera. Commitea.
5. Push → GitHub Actions → test → deploy al VPS
6. Verifica en producción
7. Siguiente historia
```

### 3.3 Context engineering mínimo viable

En Fase 1, necesitas exactamente **dos archivos** de context engineering:

- **CONVENTIONS.md:** Lenguaje (TypeScript), framework (Next.js), estilo de código, estructura de carpetas, convenciones de naming, patrones de manejo de errores. 30-50 líneas.
- **SCHEMA.md:** Modelo de datos de tu aplicación. Tablas, relaciones, tipos. Lo que Drizzle necesita saber.

Esos dos archivos, cargados en el contexto del LLM al inicio de cada sesión, son suficientes para que el modelo genere código coherente con tu proyecto.

### 3.4 IaC mínimo

Tu infraestructura como código es un archivo: `docker-compose.yml`. No necesitas Terraform. No necesitas Pulumi. Tu `docker-compose.yml` se versiona en git, se despliega con `docker compose up -d`, y define completamente tu infraestructura.

Si tu infraestructura cabe en un `docker-compose.yml`, tu Infrastructure as Conversation (Swarm::Ops §5) es literalmente el chat con tu LLM: "Necesito agregar un servicio de Redis para caching. Actualiza el docker-compose."

### 3.5 Qué NO hacer en Fase 1

- No implementes autenticación compleja si no la necesitas. Auth.js cuando sea necesario.
- No añadas un ORM complejo. Drizzle + SQL directo para consultas complejas.
- No configures CI/CD elaborado. Un workflow de GitHub Actions de 30 líneas es suficiente.
- No intentes hacer microservicios. Monolito. Sin excepciones.
- No instales herramientas de observabilidad. Si algo falla, miras los logs con `docker logs`.

---

## 4. Fase 2: Primer Agente (Mes 1)

**Objetivo:** Tu proyecto necesita un componente inteligente. Un chatbot, un analizador de documentos, un clasificador — algo que requiere un LLM en producción, no solo en desarrollo.

**Señal de transición:** Cuando tu aplicación necesita llamar a un LLM para servir a usuarios, no solo para que tú desarrolles.

### 4.1 Qué cambia

Se activa la segunda mitad del stack de STACK::LLM. Aparece Python como lenguaje cognitivo.

| Componente | Fase 1 | Fase 2 |
|---|---|---|
| **Lenguajes** | TypeScript only | TypeScript (producto) + Python (cognición) |
| **Backend extra** | — | FastAPI para la capa de IA |
| **LLM en producción** | No | Sí (via API) |
| **Proxy de modelos** | — | LiteLLM (rotación de providers, fallback, control de costes) |
| **Observabilidad LLM** | — | Langfuse (trazas, costes, calidad) |
| **Vectores** | — | pgvector (si necesitas RAG o búsqueda semántica) |

### 4.2 Arquitectura de Fase 2

```
[Next.js frontend]
 ↓ API calls
[Next.js API routes / Server Actions] ←→ [PostgreSQL]
 ↓ cuando necesita cognición
[FastAPI (Python)] ←→ [LiteLLM proxy] ←→ [LLM providers]
 ↓ opcional
[pgvector para embeddings]
```

El frontend y el backend de producto siguen en TypeScript. FastAPI entra solo para la capa cognitiva: el código que orquesta llamadas a LLMs, procesa respuestas, maneja RAG, ejecuta cadenas de prompts.

### 4.3 Por qué Python aquí y no antes

No por preferencia estética sino por pragmatismo duro: el ecosistema de IA en Python (LangChain, LlamaIndex, CrewAI, OpenAI SDK, Anthropic SDK, sentence-transformers, scikit-learn) es 10x más maduro que sus equivalentes en TypeScript. Cuando tu aplicación necesita llamar a un LLM en producción, Python tiene las mejores abstracciones, la mejor documentación, y la mayor representación en training data para este dominio específico.

### 4.4 LiteLLM como proxy

LiteLLM es tu primer proxy de modelos. No es un Model Router sofisticado (STACK::LLM §9.1); es un proxy que te da:

- **Interfaz unificada:** Llamas a OpenAI, Anthropic, Google, Mistral con la misma API.
- **Fallback:** Si Claude está caído, redirige a GPT automáticamente.
- **Control de costes:** Presupuesto diario/mensual por API key.
- **Logging:** Cada llamada loggeada con tokens consumidos.

Es todo lo que necesitas. El Model Router de 4 tiers llega en Fase 3-4.

### 4.5 Context engineering Fase 2

Se agregan dos archivos:

- **ARCHITECTURE.md:** Ahora que tienes dos lenguajes y dos procesos, necesitas documentar cómo se comunican. Endpoints internos, formato de mensajes, flujo de datos entre Next.js y FastAPI.
- **CONSTRAINTS.md:** Presupuesto de tokens mensuales. Providers permitidos. Latencia máxima aceptable para llamadas a LLM. Datos que nunca deben ir a un LLM externo.

Total de archivos de contexto: 4 (CONVENTIONS, SCHEMA, ARCHITECTURE, CONSTRAINTS).

---

## 5. Fase 3: Múltiples Agentes (Mes 2-3)

**Objetivo:** Tu proyecto requiere más de una capacidad cognitiva independiente. Un agente que escribe, otro que revisa. Un agente que busca, otro que sintetiza. Necesitas orquestación.

**Señal de transición:** Cuando te das cuenta de que un solo prompt/cadena no puede resolver el problema y necesitas agentes con roles diferenciados que se coordinan.

### 5.1 Qué cambia

| Componente | Fase 2 | Fase 3 |
|---|---|---|
| **Orquestación** | Cadenas lineales de prompts | Framework de orquestación (Agents SDK, CrewAI, o custom) |
| **Model Router** | LiteLLM proxy básico | Router con tiers (económico/balance/frontera/razonamiento) |
| **Evals** | Verificación manual de outputs | Pipeline de evals automatizado (regresión, calidad, coste) |
| **Aislamiento** | Todo en el mismo proceso | Contenedores separados por agente (read-only mínimo) |
| **Infraestructura** | Docker Compose | Docker Compose con más servicios (o primer contacto con K8s) |

### 5.2 La regla de diversidad de modelos

Principio cardinal tomado de Xanpan::Agents §9.3: si un agente genera algo, el agente que lo verifica debe usar un modelo diferente. Si el coder usa Claude, el reviewer usa GPT. Si el analizador usa Gemini, el sintetizador usa Claude. La razón es simple: un modelo no puede detectar sus propios blind spots. Dos modelos tienen blind spots diferentes; la intersección es más pequeña.

### 5.3 Evals: el momento en que se vuelven obligatorios

En Fase 2, verificabas manualmente. En Fase 3, la verificación manual no escala. Necesitas evals automatizados.

Empieza con lo mínimo:

1. **Dataset de regresión:** 20-50 ejemplos de input→output esperado para cada capacidad de cada agente. Se ejecutan en cada cambio.
2. **Eval de coste:** ¿Cuántos tokens consumió esta tarea? ¿Está dentro del presupuesto?
3. **Eval de calidad:** Para tareas con output subjetivo, un modelo-juez (diferente al modelo-autor) evalúa calidad con rubric.

No necesitas Braintrust ni frameworks de eval complejos todavía. Un script de Python que ejecuta el dataset, compara outputs, y reporta pass/fail es suficiente.

### 5.4 Context engineering Fase 3

Se agrega:

- **AGENTS.md:** Quién es cada agente, qué modelo usa, qué herramientas tiene, qué puede y qué no puede hacer. Es el directorio del enjambre emergente.

Total de archivos de contexto: 5 (CONVENTIONS, SCHEMA, ARCHITECTURE, CONSTRAINTS, AGENTS).

---

## 6. Fase 4: Enjambre (cuando el proyecto lo exija)

**Objetivo:** Tu sistema tiene suficientes agentes, suficiente complejidad operacional, y suficiente escala que necesitas los frameworks completos del corpus.

**Señal de transición:** Cuando el Docker Compose se vuelve inmanejable. Cuando los deploys manuales son un cuello de botella. Cuando los agentes necesitan coordinarse sin tu intervención directa.

### 6.1 Activación del corpus completo

Aquí es donde dejan de ser opcionales:

| Documento | Qué activas | Por qué ahora |
|---|---|---|
| **STACK::LLM §9-10** | Stack extendido completo. Model Router formal. MCP. Aislamiento con Firecracker. | La complejidad técnica lo exige |
| **Swarm::Ops** | Sistema nervioso adaptativo. IaConversation real. Agente-observer. Security-by-Swarm | Los deploys y la operación ya no caben en scripts simples |
| **Xanpan::Agents** | Metodología completa. Separación PO/Operador. Tablero Neural. OKRs formales. Sentinel | Ya no eres uno; necesitas estructura para coordinar |

### 6.2 La transición de Docker Compose a Kubernetes

No es obligatoria. Es condicional:

- **Quédate en Docker Compose** si tienes ≤10 contenedores, un solo VPS, y el deploy manual con `docker compose pull && docker compose up -d` tarda menos de 2 minutos.
- **Migra a Kubernetes** si tienes >10 contenedores, necesitas auto-scaling, necesitas zero-downtime deploys, o necesitas aislamiento de red entre agentes.

La migración intermedia existe: Docker Swarm. Es Kubernetes sin la complejidad. Para muchos Operadores Solitarios que están escalando, Docker Swarm es suficiente y llegará hasta bastante lejos.

### 6.3 Cuándo dejas de ser Operador Solitario

Fase 4 es típicamente donde el Operador Solitario necesita ayuda. Las señales:

- Pasas más del 50% del tiempo en operación y menos del 50% en construcción.
- Los incidentes en producción requieren atención que no puedes dar por horario/capacidad.
- La separación PO/Operador deja de ser una ficción útil y se vuelve una necesidad real.

En este punto, Xanpan::Agents §16 (Modelo de Transición) se activa completamente.

---

## 7. Context Engineering Progresivo

El context engineering no nace completo. Crece con el proyecto. Esta es la ruta:

| Fase | Archivos | Contenido total | Notas |
|---|---|---|---|
| **Fase 0** | — | — | Sin proyecto todavía |
| **Fase 1** | CONVENTIONS.md, SCHEMA.md | ~100 líneas | Lo mínimo para coherencia de código |
| **Fase 2** | + ARCHITECTURE.md, CONSTRAINTS.md | ~250 líneas | Aparece la dualidad TS/Python y los límites de coste |
| **Fase 3** | + AGENTS.md | ~400 líneas | Directorio del enjambre emergente |
| **Fase 4** | + INFRA.md, RUNBOOKS.md | ~600+ líneas | Infraestructura compleja exige documentación formal |

**Regla fundamental (STACK::LLM §8.3):** El 70% del contexto que le das al LLM debe ser relevante para la tarea actual. No cargues los 7 archivos en cada sesión. Carga los que necesitas para lo que estás haciendo ahora.

Los archivos de context engineering no son documentación pasiva. Son artefactos operacionales que alimentan directamente a los LLMs. Si un archivo no cambia cómo el LLM genera código, no es context engineering — es documentación tradicional (que también es valiosa, pero sirve a un propósito diferente).

---
