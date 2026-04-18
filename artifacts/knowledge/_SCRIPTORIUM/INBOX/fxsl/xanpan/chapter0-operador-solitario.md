# CHAPTER 0: EL OPERADOR SOLITARIO

## Bootstrap Path para Desarrollo Asistido por LLM — De una Persona a un Enjambre

*El capítulo que le faltaba al corpus: cómo empezar cuando eres uno, tienes un VPS, y quieres construir algo real*

Documento fundacional del corpus Xanpan::Agents
Febrero 2026

---

## Índice

0. [Premisa: Por qué este documento existe](#0-premisa-por-qué-este-documento-existe)
1. [El Operador Solitario como rol legítimo](#1-el-operador-solitario-como-rol-legítimo)
2. [Fase 0: Cimientos (Día 1)](#2-fase-0-cimientos-día-1)
3. [Fase 1: El Primer Proyecto (Semana 1)](#3-fase-1-el-primer-proyecto-semana-1)
4. [Fase 2: Primer Agente (Mes 1)](#4-fase-2-primer-agente-mes-1)
5. [Fase 3: Múltiples Agentes (Mes 2-3)](#5-fase-3-múltiples-agentes-mes-2-3)
6. [Fase 4: Enjambre (cuando el proyecto lo exija)](#6-fase-4-enjambre-cuando-el-proyecto-lo-exija)
7. [Context Engineering Progresivo](#7-context-engineering-progresivo)
8. [Infraestructura Progresiva](#8-infraestructura-progresiva)
9. [Observabilidad Progresiva](#9-observabilidad-progresiva)
10. [Seguridad Progresiva](#10-seguridad-progresiva)
11. [Economía: Presupuesto Real por Fase](#11-economía-presupuesto-real-por-fase)
12. [Anti-patrones del Operador Solitario](#12-anti-patrones-del-operador-solitario)
13. [Caso Real: Korvo–Korax como Proof of Concept](#13-caso-real-korvo-korax-como-proof-of-concept)
14. [Cuándo dejar de ser solitario](#14-cuándo-dejar-de-ser-solitario)
15. [Mapa de Navegación del Corpus](#15-mapa-de-navegación-del-corpus)

---

# 0. Premisa: Por qué este documento existe

Los tres documentos del corpus — STACK::LLM, Swarm::Ops, Xanpan::Agents — describen un sistema maduro. Presuponen infraestructura existente, agentes operativos, pipelines de evals, y al menos dos roles humanos diferenciados (Product Owner y Operador). Son correctos pero incompletos: describen el destino sin trazar la ruta desde el origen.

Este documento es la ruta.

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

# 1. El Operador Solitario como rol legítimo

## 1.1 La violación consciente: dual-hat

Xanpan::Agents §2 define dos roles humanos distintos:

- **Product Owner (PO):** Decide qué construir. Define valor de negocio. Prioriza backlog. Negocia scope.
- **Operador:** Decide cómo construir. Configura agentes. Optimiza pipelines. Gestiona infraestructura.

En Xanpan clásico, la separación es obligatoria porque las tensiones entre "qué" y "cómo" son reales y productivas. Un PO que también opera tiende a optimizar la técnica a expensas del negocio (o viceversa).

El Operador Solitario viola esta separación. Conscientemente. No porque la separación sea incorrecta, sino porque el coste de dos personas para un proyecto embrionario es prohibitivo.

La compensación es disciplina: el Operador Solitario debe alternar sombreros explícitamente.

**Sombrero PO (cuándo):** Al inicio de cada ciclo de trabajo, al definir qué historias abordar, al decidir si un feature ship o necesita más iteración, al hablar con usuarios o stakeholders.

**Sombrero Operador (cuándo):** Al configurar herramientas, al interactuar con agentes LLM, al resolver problemas técnicos, al optimizar prompts, al gestionar infraestructura.

La disciplina está en no mezclar: cuando llevas el sombrero PO, priorizas por valor de negocio sin dejarte seducir por la elegancia técnica. Cuando llevas el sombrero Operador, optimizas la ejecución sin cuestionar las prioridades que ya definiste como PO.

## 1.2 El PCA como compensador

El **Pensamiento Cíclico Asíncrono** — la estructura temporal de Xanpan::Agents §4 con ciclos de 2-4 semanas y flujo continuo dentro — funciona naturalmente para el Operador Solitario. No hay ceremonias de coordinación porque no hay equipo que coordinar. El ciclo se reduce a:

1. **Inicio de ciclo (sombrero PO):** Revisa OKRs, selecciona historias para el ciclo, prioriza.
2. **Ejecución (sombrero Operador):** Trabaja con LLMs para implementar historias. Flujo continuo.
3. **Cierre de ciclo (ambos sombreros):** ¿Se entregó valor? ¿Se cumplieron los KRs? ¿Qué aprendí?

La retrospectiva del Operador Solitario es un documento de 5-10 líneas al final de cada ciclo. No es una reunión; es una reflexión escrita que alimenta el siguiente ciclo.

---

# 2. Fase 0: Cimientos (Día 1)

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

**Lo que NO necesitas todavía:** Kubernetes. ArgoCD. Terraform. Langfuse. Feature flags. Model Router. Nada del stack extendido de STACK::LLM §10.2.

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

# 3. Fase 1: El Primer Proyecto (Semana 1)

**Objetivo:** Construir y desplegar algo funcional. Cualquier cosa. El tamaño no importa; la completitud sí.

## 3.1 Elige el Perfil Mínimo de STACK::LLM

Tu primer proyecto usa exclusivamente el **Perfil Mínimo** de STACK::LLM §11.1:

- **Stack:** TypeScript full-stack. Next.js + Server Actions + Drizzle ORM + PostgreSQL.
- **Infraestructura:** Docker Compose en tu VPS. Nginx como reverse proxy. Let's Encrypt para HTTPS.
- **CI/CD:** GitHub Actions con un workflow simple: push → build → test → deploy via SSH.
- **Base de datos:** PostgreSQL en un contenedor Docker. Backup diario con pg_dump a un volumen local (y opcionalmente a object storage).

No hay capa Python. No hay FastAPI. No hay agentes. Es un monolito TypeScript desplegado con Docker Compose. Esto no es una limitación; es lo correcto para esta fase.

## 3.2 El flujo de trabajo

```
1. [Sombrero PO] Define 3-5 historias para la primera semana
2. [Sombrero Operador] Abre Claude Code en tu repo
3. Dale contexto: "Lee CONVENTIONS.md. Implementa esta historia: [descripción]"
4. Revisa el output. Itera. Commitea.
5. Push → GitHub Actions → test → deploy al VPS
6. Verifica en producción
7. Siguiente historia
```

## 3.3 Context engineering mínimo viable

En Fase 1, necesitas exactamente **dos archivos** de context engineering:

- **CONVENTIONS.md:** Lenguaje (TypeScript), framework (Next.js), estilo de código, estructura de carpetas, convenciones de naming, patrones de manejo de errores. 30-50 líneas.
- **SCHEMA.md:** Modelo de datos de tu aplicación. Tablas, relaciones, tipos. Lo que Drizzle necesita saber.

Esos dos archivos, cargados en el contexto del LLM al inicio de cada sesión, son suficientes para que el modelo genere código coherente con tu proyecto.

## 3.4 IaC mínimo

Tu infraestructura como código es un archivo: `docker-compose.yml`. Eso es tu IaC. No necesitas Terraform. No necesitas Pulumi. Tu `docker-compose.yml` se versiona en git, se despliega con `docker compose up -d`, y define completamente tu infraestructura.

Si tu infraestructura cabe en un `docker-compose.yml`, tu Infrastructure as Conversation (Swarm::Ops §5) es literalmente el chat con tu LLM: "Necesito agregar un servicio de Redis para caching. Actualiza el docker-compose."

## 3.5 Qué NO hacer en Fase 1

- No implementes autenticación compleja si no la necesitas. Auth.js cuando sea necesario.
- No añadas un ORM complejo. Drizzle + SQL directo para consultas complejas.
- No configures CI/CD elaborado. Un workflow de GitHub Actions de 30 líneas es suficiente.
- No intentes hacer microservicios. Monolito. Sin excepciones.
- No instales herramientas de observabilidad. Si algo falla, miras los logs con `docker logs`.

---

# 4. Fase 2: Primer Agente (Mes 1)

**Objetivo:** Tu proyecto necesita un componente inteligente. Un chatbot. Un analizador de documentos. Un clasificador. Algo que requiere un LLM en producción, no solo en desarrollo.

**Señal de transición:** Cuando tu aplicación necesita llamar a un LLM para servir a usuarios, no solo para que tú desarrolles.

## 4.1 Qué cambia

Se activa la segunda mitad del stack de STACK::LLM. Aparece Python como lenguaje cognitivo.

| Componente | Fase 1 | Fase 2 |
|---|---|---|
| **Lenguajes** | TypeScript only | TypeScript (producto) + Python (cognición) |
| **Backend extra** | — | FastAPI para la capa de IA |
| **LLM en producción** | No | Sí (via API) |
| **Proxy de modelos** | — | LiteLLM (rotación de providers, fallback, control de costes) |
| **Observabilidad LLM** | — | Langfuse (trazas, costes, calidad) |
| **Vectores** | — | pgvector (si necesitas RAG o búsqueda semántica) |

## 4.2 Arquitectura de Fase 2

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

## 4.3 Por qué Python aquí y no antes

No por preferencia estética sino por pragmatismo duro: el ecosistema de IA en Python (LangChain, LlamaIndex, CrewAI, OpenAI SDK, Anthropic SDK, sentence-transformers, scikit-learn) es 10x más maduro que sus equivalentes en TypeScript. Cuando tu aplicación necesita llamar a un LLM en producción, Python tiene las mejores abstracciones, la mejor documentación, y la mayor representación en training data para este dominio específico.

## 4.4 LiteLLM como proxy

LiteLLM es tu primer proxy de modelos. No es un Model Router sofisticado (STACK::LLM §9.1); es un proxy que te da:

- **Interfaz unificada:** Llamas a OpenAI, Anthropic, Google, Mistral con la misma API.
- **Fallback:** Si Claude está caído, redirige a GPT automáticamente.
- **Control de costes:** Presupuesto diario/mensual por API key.
- **Logging:** Cada llamada loggeada con tokens consumidos.

Es todo lo que necesitas. El Model Router de 4 tiers llega en Fase 3-4.

## 4.5 Context engineering Fase 2

Se agregan dos archivos:

- **ARCHITECTURE.md:** Ahora que tienes dos lenguajes y dos procesos, necesitas documentar cómo se comunican. Endpoints internos, formato de mensajes, flujo de datos entre Next.js y FastAPI.
- **CONSTRAINTS.md:** Presupuesto de tokens mensuales. Providers permitidos. Latencia máxima aceptable para llamadas a LLM. Datos que nunca deben ir a un LLM externo.

Total de archivos de contexto: 4 (CONVENTIONS, SCHEMA, ARCHITECTURE, CONSTRAINTS).

---

# 5. Fase 3: Múltiples Agentes (Mes 2-3)

**Objetivo:** Tu proyecto requiere más de una capacidad cognitiva independiente. Un agente que escribe, otro que revisa. Un agente que busca, otro que sintetiza. Necesitas orquestación.

**Señal de transición:** Cuando te das cuenta de que un solo prompt/cadena no puede resolver el problema y necesitas agentes con roles diferenciados que se coordinan.

## 5.1 Qué cambia

| Componente | Fase 2 | Fase 3 |
|---|---|---|
| **Orquestación** | Cadenas lineales de prompts | Framework de orquestación (Agents SDK, CrewAI, o custom) |
| **Model Router** | LiteLLM proxy básico | Router con tiers (económico/balance/frontera/razonamiento) |
| **Evals** | Verificación manual de outputs | Pipeline de evals automatizado (regresión, calidad, coste) |
| **Aislamiento** | Todo en el mismo proceso | Contenedores separados por agente (read-only mínimo) |
| **Infraestructura** | Docker Compose | Docker Compose con más servicios (o primer contacto con K8s) |

## 5.2 La regla de diversidad de modelos

Principio cardinal tomado de Xanpan::Agents §9.3: si un agente genera algo, el agente que lo verifica debe usar un modelo diferente. Si el coder usa Claude, el reviewer usa GPT. Si el analizador usa Gemini, el sintetizador usa Claude. La razón es simple: un modelo no puede detectar sus propios blind spots. Dos modelos tienen blind spots diferentes; la intersección es más pequeña.

## 5.3 Evals: el momento en que se vuelven obligatorios

En Fase 2, verificabas manualmente. En Fase 3, la verificación manual no escala. Necesitas evals automatizados.

Empieza con lo mínimo:

1. **Dataset de regresión:** 20-50 ejemplos de input→output esperado para cada capacidad de cada agente. Se ejecutan en cada cambio.
2. **Eval de coste:** ¿Cuántos tokens consumió esta tarea? ¿Está dentro del presupuesto?
3. **Eval de calidad:** Para tareas con output subjetivo, un modelo-juez (diferente al modelo-autor) evalúa calidad con rubric.

No necesitas Braintrust ni frameworks de eval complejos todavía. Un script de Python que ejecuta el dataset, compara outputs, y reporta pass/fail es suficiente.

## 5.4 Context engineering Fase 3

Se agrega:

- **AGENTS.md:** Quién es cada agente, qué modelo usa, qué herramientas tiene, qué puede y qué no puede hacer. Es el directorio del enjambre emergente.

Total de archivos de contexto: 5 (CONVENTIONS, SCHEMA, ARCHITECTURE, CONSTRAINTS, AGENTS).

---

# 6. Fase 4: Enjambre (cuando el proyecto lo exija)

**Objetivo:** Tu sistema tiene suficientes agentes, suficiente complejidad operacional, y suficiente escala que necesitas los frameworks completos del corpus.

**Señal de transición:** Cuando el Docker Compose se vuelve inmanejable. Cuando los deploys manuales son un cuello de botella. Cuando los agentes necesitan coordinarse sin tu intervención directa.

## 6.1 Activación del corpus completo

Aquí es donde dejan de ser opcionales:

| Documento | Qué activas | Por qué ahora |
|---|---|---|
| **STACK::LLM §9-10** | Stack extendido completo. Model Router formal. MCP. Aislamiento con Firecracker. | La complejidad técnica lo exige |
| **Swarm::Ops** | Sistema nervioso adaptativo. IaConversation real. Agente-observer. Security-by-Swarm | Los deploys y la operación ya no caben en scripts simples |
| **Xanpan::Agents** | Metodología completa. Separación PO/Operador. Tablero Neural. OKRs formales. Sentinel | Ya no eres uno; necesitas estructura para coordinar |

## 6.2 La transición de Docker Compose a Kubernetes

No es obligatoria. Es condicional:

- **Quédate en Docker Compose** si tienes ≤10 contenedores, un solo VPS, y el deploy manual con `docker compose pull && docker compose up -d` tarda menos de 2 minutos.
- **Migra a Kubernetes** si tienes >10 contenedores, necesitas auto-scaling, necesitas zero-downtime deploys, o necesitas aislamiento de red entre agentes.

La migración intermedia existe: Docker Swarm. Es Kubernetes sin la complejidad. Para muchos Operadores Solitarios que están escalando, Docker Swarm es suficiente y llegará hasta bastante lejos.

## 6.3 Cuándo dejas de ser Operador Solitario

Fase 4 es típicamente donde el Operador Solitario necesita ayuda. Las señales:

- Pasas más del 50% del tiempo en operación y menos del 50% en construcción.
- Los incidentes en producción requieren atención que no puedes dar por horario/capacidad.
- La separación PO/Operador deja de ser una ficción útil y se vuelve una necesidad real.

En este punto, Xanpan::Agents §16 (Modelo de Transición) se activa completamente.

---

# 7. Context Engineering Progresivo

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

# 8. Infraestructura Progresiva

La infraestructura crece con el proyecto. La tabla mapea fase → infraestructura concreta:

| Capa | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
|---|---|---|---|---|
| **Compute** | 1 VPS (Hetzner CX22) | 1-2 VPS | 2-3 VPS o cluster pequeño | Kubernetes |
| **IaC** | `docker-compose.yml` | `docker-compose.yml` (más servicios) | Docker Compose + scripts de provisioning | Terraform + ArgoCD |
| **CI/CD** | GitHub Actions (30 líneas) | GitHub Actions (~100 líneas) | GitHub Actions + evals automatizados | Swarm::Ops completo |
| **Reverse proxy** | Nginx + Let's Encrypt | Nginx + Let's Encrypt | Caddy o Traefik (routing por servicio) | Ingress controller |
| **Backups** | pg_dump cron + volumen local | pg_dump + object storage (S3/R2) | Backup automatizado con verificación | Backup con disaster recovery |
| **DNS** | 1 dominio, 1-2 registros | Subdominos para servicios | DNS programático (Cloudflare API) | DNS como código |
| **Secrets** | `.env` file (NO en git) | `.env` + Docker secrets | SOPS o Vault | Vault con rotation |

**Principio rector:** Cada incremento de infraestructura debe ser motivado por una necesidad real, no por una expectativa de necesidad futura. La sobre-ingeniería de infraestructura es el anti-patrón más caro del Operador Solitario porque consume el recurso más escaso: tu tiempo.

> ⚡ **LA REGLA DEL DOCKER-COMPOSE**
>
> Si tu infraestructura cabe en un `docker-compose.yml`, tu IaC es ese archivo. Tu IaConversation (Swarm::Ops §5) es el chat con tu LLM: "Agrega un servicio de Redis para caching." Tu drift detection es `docker compose config --quiet` comparado con lo que corre en producción. No necesitas más. Cuando necesites más, lo sabrás porque Docker Compose dejará de ser suficiente — no porque un documento te lo dijo.

---

# 9. Observabilidad Progresiva

| Nivel | Fase | Implementación | Coste |
|---|---|---|---|
| **Nivel 0: Logs** | Fase 1 | `docker logs` + grep. Nada más. | $0 |
| **Nivel 1: Métricas básicas** | Fase 2 | Uptime monitor externo (UptimeRobot, Betterstack free tier). Health endpoint en tu app. | $0-7/mes |
| **Nivel 2: Stack de observabilidad** | Fase 3 | Prometheus + Grafana en tu Docker Compose. Langfuse para trazas LLM. Sentry para errores. | $0-30/mes |
| **Nivel 3: Inteligencia activa** | Fase 4 | Agente-observer (Swarm::Ops §7). Alertas correlacionadas con deploys. Rollback semi-automático. | Variable |

**La ruta del agente-observer** (corrección a Swarm::Ops §7.2, que lo describía como straightforward cuando es un proyecto entero):

El agente-observer no nace adulto. Se construye en 4 etapas:

1. **Etapa 1: Alertas clásicas.** Prometheus + reglas de alerta estáticas. Si latencia > X ms, alerta a Telegram/Slack. Esto ya existe y funciona. No necesita IA.
2. **Etapa 2: Correlación manual asistida.** Cuando recibes una alerta, le preguntas a tu LLM: "La latencia subió a las 14:30. Estos son los deploys de hoy [lista]. ¿Cuál pudo causar el problema?" El LLM te ayuda a diagnosticar, pero tú inicias la conversación.
3. **Etapa 3: Correlación semi-automática.** Un script que, ante cada alerta, recoge métricas + timeline de deploys recientes + logs relevantes, y los envía a un LLM para análisis. El output es un diagnóstico propuesto que tú revisas.
4. **Etapa 4: Agente-observer completo.** Un agente que monitorea continuamente, detecta anomalías pre-alerta, correlaciona automáticamente, y propone (o ejecuta) acciones. Esto es Swarm::Ops §7.2 en su forma madura.

Cada etapa es funcional por sí misma. No necesitas llegar a la etapa 4 para tener observabilidad útil. La mayoría de los Operadores Solitarios vivirán felices en la etapa 2-3 durante meses o años.

---

# 10. Seguridad Progresiva

| Nivel | Fase | Implementación |
|---|---|---|
| **Nivel 0: Higiene básica** | Fase 1 | SSH con keys (no passwords). Firewall (ufw). HTTPS (Let's Encrypt). Dependencias actualizadas. Secrets en `.env`, nunca en git. |
| **Nivel 1: Aplicación** | Fase 1-2 | Validación de inputs (Zod en frontend y backend). Auth.js cuando necesites autenticación. CORS configurado correctamente. Rate limiting. |
| **Nivel 2: LLM-specific** | Fase 2-3 | Sanitización de inputs antes de enviarlos a LLMs. Nunca incluir secrets en prompts. Validación de outputs del LLM antes de ejecutar acciones. Presupuesto de tokens como mecanismo anti-abuse. |
| **Nivel 3: Agentes** | Fase 3-4 | Aislamiento de ejecución por agente (contenedores read-only). Principio de mínimo privilegio por agente. Diversidad de modelos entre generador y verificador. |
| **Nivel 4: Security-by-Swarm** | Fase 4 | Agente-security dedicado (Swarm::Ops §8). Análisis contextual de PRs. Monitoreo de comportamiento en runtime. |

**La cuestión del quis custodiet** (corrección a Swarm::Ops §8, que no abordaba la seguridad del agente-security mismo):

El agente-security tiene un problema de bootstrap: ¿quién lo asegura a él? Si el agente de seguridad usa un modelo con blind spots en seguridad, tienes un guardia ciego.

Cuatro controles meta (alineados con el patrón del Sentinel en Xanpan::Agents §9.4):

1. **Modelo diferente al enjambre.** Si tus agentes productivos usan Claude, el security-agent usa GPT (o viceversa). Los blind spots no se solapan.
2. **Meta-eval periódico.** Cada mes, somete al security-agent a un conjunto de pruebas adversariales conocidas. Si falla alguna, recalibra.
3. **Veto asimétrico.** El security-agent puede bloquear cualquier PR pero no puede aprobar sin pasar por los otros layers de verificación. Un falso positivo causa delay; un falso negativo en cualquier otra capa lo atrapa.
4. **Auditoría externa periódica.** Cada trimestre (o cuando el presupuesto lo permita), un humano con experiencia en seguridad revisa los logs del security-agent: qué aprobó, qué rechazó, qué debió detectar y no detectó.

---

# 11. Economía: Presupuesto Real por Fase

| Concepto | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
|---|---|---|---|---|
| **VPS** | €5-10/mes | €10-30/mes | €30-80/mes | €80-300/mes |
| **Dominio + DNS** | €1/mes | €1/mes | €2/mes | €5/mes |
| **API tokens (desarrollo)** | €20-50/mes | €30-80/mes | €50-150/mes | €100-500/mes |
| **API tokens (producción)** | €0 | €10-100/mes | €50-300/mes | €200-2000/mes |
| **Herramientas SaaS** | €0-20/mes | €0-30/mes | €20-60/mes | €50-200/mes |
| **Total estimado** | **€25-80/mes** | **€50-240/mes** | **€150-590/mes** | **€430-3000/mes** |

**La curva de coste no es lineal; es exponencial.** Cada fase multiplica el coste de la anterior. Esto es esperado y correcto: estás pasando de un proyecto personal a una plataforma. Lo que no es aceptable es saltar a costes de Fase 3 cuando estás en Fase 1. Cada euro gastado debe justificarse con valor entregado.

**Control de costes como disciplina, no como restricción:** Configura alertas de facturación desde el Día 1. En toda API de LLM. En tu cloud provider. El presupuesto de tokens de Xanpan::Agents §6.3 no es burocracia; es supervivencia financiera del Operador Solitario.

---

# 12. Anti-patrones del Operador Solitario

## 12.1 Sobre-ingeniería prematura

**Síntoma:** Kubernetes en Fase 1. Terraform para un VPS. Feature flags cuando tienes 3 usuarios. Model Router de 4 tiers cuando usas un solo modelo.

**Causa:** Leer el corpus completo y querer implementar todo de golpe.

**Corrección:** Implementa lo que necesitas hoy. El corpus es un mapa del territorio completo, no una lista de requisitos mínimos.

## 12.2 Sub-ingeniería en seguridad

**Síntoma:** Secrets en el código. No HTTPS. No validación de inputs. LLM con acceso directo a la base de datos.

**Causa:** "Es solo mi proyecto personal, no necesita seguridad."

**Corrección:** La seguridad de Nivel 0-1 (§10) tiene coste cero y esfuerzo mínimo. No hay excusa para no implementarla.

## 12.3 Ausencia de backups

**Síntoma:** La base de datos en producción no tiene backup. O tiene backup pero nunca se ha probado que se pueda restaurar.

**Causa:** "No me va a pasar."

**Corrección:** `pg_dump` en un cron job es 5 minutos de setup. Restaurar el backup de prueba es otros 5 minutos. Hazlo el Día 1.

## 12.4 Context engineering ausente

**Síntoma:** Cada sesión con el LLM empieza desde cero. El modelo no sabe las convenciones de tu proyecto. Genera código inconsistente.

**Causa:** "El LLM es inteligente, debería entender mi proyecto."

**Corrección:** CONVENTIONS.md + SCHEMA.md en Fase 1. 30 minutos de escritura que ahorran horas de corrección.

## 12.5 Aislamiento del Operador

**Síntoma:** Llevas meses construyendo sin que nadie use lo que construyes. No has hablado con un usuario en semanas.

**Causa:** El sombrero Operador es adictivo. Construir es más cómodo que validar.

**Corrección:** El sombrero PO no es opcional. Al inicio de cada ciclo, fuerza la pregunta: "¿Para quién estoy construyendo esto y cuándo lo van a usar?" Si no hay respuesta, el ciclo está mal priorizado.

---

# 13. Caso Real: Korvo–Korax como Proof of Concept

## 13.1 El sistema

Korvo–Korax es un sistema personal que implementa involuntariamente la mayoría de los patrones del corpus a escala mínima:

- **1 humano** como PO + Operador (dual-hat, §1.1).
- **1 agente principal** (Korax) que genera sub-agentes según la tarea.
- **1 VPS** en Hetzner como infraestructura.
- **Docker** para browser automation y servicios auxiliares.
- **Telegram** como canal de comunicación humano-agente.
- **PCA** (Pensamiento Cíclico Asíncrono) como estructura temporal light.

## 13.2 Mapeo al corpus

| Concepto del corpus | Implementación en Korvo–Korax |
|---|---|
| Product Owner | El humano (sombrero PO) |
| Operador | El humano (sombrero Operador) |
| Agente-coder | Korax delegando a Claude Code / Gemini CLI |
| Model Router | LiteLLM proxy con reglas manuales |
| Evals | Verificación humana + tests automatizados básicos |
| Observabilidad | Logs + uptime monitor + revisión manual |
| Context engineering | CONVENTIONS.md + documentos de proyecto |
| IaC | docker-compose.yml |
| CI/CD | GitHub Actions básico |
| Tablero Neural | Lista de tareas en herramienta de gestión personal |
| Retrospectiva | Notas al final de cada ciclo |

## 13.3 Lecciones observadas

1. **La separación PO/Operador es real aun siendo ficticia.** Alternar sombreros conscientemente previene la deriva hacia la optimización técnica infinita. Sin sombrero PO explícito, es fácil pasar tres semanas refactorizando infraestructura mientras el producto no avanza.

2. **El context engineering es el multiplicador más barato.** La diferencia entre darle CONVENTIONS.md al LLM y no dárselo es la diferencia entre código coherente y código que necesita reescritura. Es el máximo ROI/tiempo invertido.

3. **Docker Compose es suficiente para más tiempo del que crees.** La tentación de migrar a Kubernetes llega mucho antes de la necesidad real. Korvo–Korax opera con Docker Compose en un solo VPS y no ha encontrado el techo.

4. **Los costes de API tokens son el gasto más difícil de predecir.** La variabilidad es alta: una tarea compleja puede consumir 10x más tokens que una tarea simple del mismo tipo. El proxy de LiteLLM con presupuestos es esencial desde Fase 2.

5. **Telegram como interfaz es sorprendentemente funcional.** Para un Operador Solitario, una interfaz de chat asíncrona donde puedes dar instrucciones al enjambre desde el teléfono mientras caminas es más útil que un dashboard web sofisticado. La interfaz mínima no es la peor; es la que usas.

## 13.4 Lo que Korvo–Korax no cubre

Korvo–Korax opera en Fase 2-3 del bootstrap path. No tiene:

- Separación real PO/Operador (violación consciente).
- Pipeline de evals formal (en transición de etapa 2 a 3).
- Agente-observer (en etapa 2: correlación manual asistida).
- Security-by-Swarm (seguridad nivel 2: LLM-specific, pero no agente dedicado).
- Kubernetes ni IaC formal (Docker Compose es suficiente).

Esto no es una deficiencia; es el estado correcto para su fase actual.

---

# 14. Cuándo dejar de ser solitario

El Operador Solitario es un estado legítimo pero no necesariamente permanente. Las señales de que es hora de escalar:

**Señales de que necesitas un segundo humano:**

- El backlog crece más rápido de lo que puedes ejecutar, consistentemente, durante 3+ ciclos.
- Los incidentes de producción ocurren en horarios donde no puedes responder.
- La complejidad del dominio de negocio excede tu conocimiento individual (necesitas un PO real, no tu sombrero PO).
- El contexto del proyecto ya no cabe en tu cabeza. Los archivos de context engineering empiezan a contradecirse porque no tienes tiempo de mantenerlos coherentes.

**Señales de que necesitas más infraestructura:**

- Docker Compose tarda más de 3 minutos en reiniciar todo.
- Necesitas zero-downtime deploys porque hay usuarios activos a todas horas.
- El backup y la recuperación ante desastres se vuelven complejos.
- Los contenedores compiten por recursos en un solo VPS y la respuesta no es solo "comprar un VPS más grande."

**Señales de que necesitas los frameworks completos:**

- Tienes 4+ agentes que se coordinan entre sí.
- El gasto en tokens excede €500/mes y necesitas optimización formal.
- Los evals manuales ya no cubren la superficie de verificación necesaria.
- Un bug en un agente causó un incidente que tardó horas en diagnosticarse.

Cuando estas señales aparecen, Xanpan::Agents §16 (Modelo de Transición) y Swarm::Ops completo se activan. Chapter 0 termina. El corpus comienza.

---

# 15. Mapa de Navegación del Corpus

## 15.1 Orden de lectura recomendado

1. **Chapter 0** (este documento): Bootstrap path. Empieza aquí.
2. **STACK::LLM v1.0**: Stack de referencia. Consulta según tu fase actual.
3. **Swarm::Ops v1.0**: Cuando entres en Fase 3-4, lee completo.
4. **Xanpan::Agents v2.1**: Cuando necesites metodología formal de enjambre, lee completo.

## 15.2 Qué documento responde cada pregunta

| Pregunta | Documento | Sección |
|---|---|---|
| "¿Qué tecnologías uso?" | STACK::LLM | §0-10 según tu fase |
| "¿Cómo empiezo si soy uno solo?" | Chapter 0 | §2-6 |
| "¿Cómo organizo mi trabajo?" | Chapter 0 §1 + Xanpan::Agents §4 | PCA adaptado |
| "¿Cómo gestiono agentes en producción?" | Swarm::Ops | §3-7 |
| "¿Cómo hago CI/CD para agentes?" | Swarm::Ops | §4, 6 |
| "¿Cómo defino roles de agentes?" | Xanpan::Agents | §9 |
| "¿Cómo hago evals?" | STACK::LLM §9.4 + Xanpan::Agents §7.2 | Pipeline concreto + principios |
| "¿Cuánto va a costar?" | Chapter 0 | §11 |
| "¿Cómo aseguro mi sistema?" | STACK::LLM §6 + Chapter 0 §10 | Baseline + progresivo |
| "¿Cuándo necesito Kubernetes?" | Chapter 0 §6.2 + §14 | Señales concretas |

## 15.3 Arquitectura del corpus

```
CHAPTER 0: El Operador Solitario
  "Empieza aquí. Crece desde aquí."
    │
    ├── STACK::LLM v1.0
    │     "Qué tecnologías usar. Universal."
    │     Se usa desde Fase 1.
    │
    ├── SWARM::OPS v1.0
    │     "Cómo operar. Para enjambres."
    │     Se activa en Fase 3-4.
    │
    └── XANPAN::AGENTS v2.1
          "Cómo organizar. Metodología completa."
          Se activa en Fase 4.
```

Chapter 0 es el punto de entrada. STACK::LLM acompaña desde el inicio. Swarm::Ops y Xanpan::Agents se activan cuando la complejidad lo exige. No antes.

---

*Chapter 0: El Operador Solitario. Documento fundacional del corpus Xanpan::Agents. Febrero 2026.*

*Este documento existe porque todo enjambre empezó siendo una persona con una idea y un VPS. El camino desde ese punto hasta un sistema complejo no requiere un big bang de infraestructura ni un salto de fe hacia frameworks que todavía no necesitas. Requiere decisiones correctas que no cierren puertas futuras, disciplina para distinguir lo necesario de lo deseable, y la humildad de reconocer que el 80% de los proyectos nunca necesitarán el 80% del corpus — y que eso está perfectamente bien.*
