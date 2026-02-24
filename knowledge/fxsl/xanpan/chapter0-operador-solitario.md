---
_manifest:
  urn: "urn:fxsl:kb:chapter0-operador-solitario"
  provenance:
    created_by: "FS"
    created_at: "2026-02-24"
    source: "source/fxsl/xanpan/chapter0-operador-solitario.md"
version: "1.0.0"
status: published
tags: [xanpan, operador-solitario, bootstrap, llm, agentes, infraestructura, fases]
lang: es
---

# Chapter 0: El Operador Solitario — Bootstrap Path para Desarrollo Asistido por LLM v1.0.0

## 1. Premisa

Los tres documentos del corpus --- [STACK::LLM](urn:fxsl:kb:stack-llm-arquitectura), [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia), [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia) --- describen un sistema maduro. Presuponen infraestructura existente, agentes operativos, pipelines de evals y al menos dos roles humanos diferenciados (Product Owner y Operador). Son correctos pero incompletos: describen el destino sin trazar la ruta desde el origen.

Este documento prescribe la ruta.

El lector de Chapter 0 **DEBE** cumplir todas estas condiciones simultáneamente:

- Tiene capacidad tecnica suficiente para escribir codigo y gestionar infraestructura basica.
- Tiene acceso a LLMs de frontera (API keys, suscripciones a Claude Pro, ChatGPT Plus, o equivalentes).
- Tiene un VPS o acceso a cloud computing basico.
- No tiene equipo. No tiene presupuesto para un equipo. Es una persona sola.

Esta persona es el **Operador Solitario**. No es un rol degradado ni una version empobrecida del equipo descrito en [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia). Es el estado legitimo de inicio de cualquier proyecto de software asistido por LLM.

> **PRINCIPIO DE ARRANQUE:** Todo sistema complejo empieza como una persona resolviendo un problema concreto. Chapter 0 no pide infraestructura que no existe, no asume roles que no se pueden llenar, y no impone ceremonias absurdas para un equipo de uno. Cada decision tomada en Chapter 0 **DEBE** ser compatible con el crecimiento futuro, de modo que al escalar no sea necesario reescribir desde cero.

---

## 2. El Operador Solitario como Rol Legitimo

### 2.1 La violacion consciente: dual-hat

[Xanpan::Agents §2](urn:fxsl:kb:xanpan-agents-metodologia) define dos roles humanos distintos:

- **Product Owner (PO):** Decide que construir. Define valor de negocio. Prioriza backlog. Negocia scope.
- **Operador:** Decide como construir. Configura agentes. Optimiza pipelines. Gestiona infraestructura.

En Xanpan clasico, la separacion es obligatoria porque las tensiones entre "que" y "como" son productivas. Un PO que tambien opera tiende a optimizar la tecnica a expensas del negocio (o viceversa).

El Operador Solitario viola esta separacion. El coste de dos personas para un proyecto embrionario es prohibitivo.

La compensacion es disciplina: el Operador Solitario **DEBE** alternar sombreros explicitamente.

**Sombrero PO --- cuando usarlo:** Al inicio de cada ciclo de trabajo, al definir que historias abordar, al decidir si un feature ship o necesita mas iteracion, al hablar con usuarios o stakeholders.

**Sombrero Operador --- cuando usarlo:** Al configurar herramientas, al interactuar con agentes LLM, al resolver problemas tecnicos, al optimizar prompts, al gestionar infraestructura.

El Operador Solitario **NO DEBE** mezclar sombreros: cuando lleva el sombrero PO, **DEBE** priorizar por valor de negocio sin dejarse seducir por la elegancia tecnica. Cuando lleva el sombrero Operador, **DEBE** optimizar la ejecucion sin cuestionar las prioridades ya definidas como PO.

**Correcto:** Iniciar el ciclo con sombrero PO seleccionando historias por valor de negocio, luego cambiar a sombrero Operador para implementarlas.
**Incorrecto:** Decidir que construir y como construirlo en la misma conversacion mental, sin separacion explicita de roles.

### 2.2 El PCA como compensador

El **Pensamiento Ciclico Asincrono** --- la estructura temporal de [Xanpan::Agents §4](urn:fxsl:kb:xanpan-agents-metodologia) con ciclos de 2-4 semanas y flujo continuo dentro --- funciona para el Operador Solitario sin ceremonias de coordinacion.

El ciclo del Operador Solitario **DEBE** contener exactamente tres fases:

1. **Inicio de ciclo (sombrero PO):** Revisar OKRs, seleccionar historias para el ciclo, priorizar.
2. **Ejecucion (sombrero Operador):** Trabajar con LLMs para implementar historias. Flujo continuo.
3. **Cierre de ciclo (ambos sombreros):** Evaluar si se entrego valor, si se cumplieron los KRs, que se aprendio.

La retrospectiva del Operador Solitario **DEBE** ser un documento de 5-10 lineas al final de cada ciclo. No es una reunion; es una reflexion escrita que alimenta el siguiente ciclo.

---

## 3. Fase 0: Cimientos (Dia 1)

**Objetivo:** Tener un entorno de desarrollo funcional donde construir cualquier cosa con asistencia de LLM.

### 3.1 Componentes requeridos

El Operador Solitario **DEBE** tener disponibles todos los componentes de la siguiente tabla al finalizar el Dia 1:

| Componente | Eleccion | Coste |
|---|---|---|
| **Maquina local** | Computadora actual (cualquier OS) | Ya la tiene |
| **Editor** | VS Code o Cursor | Gratis / $20/mes |
| **CLI de LLM** | Claude Code + Gemini CLI (ambos) | API usage |
| **Control de versiones** | GitHub (repo privado) | Gratis |
| **Runtime** | Node.js LTS + Python 3.11+ | Gratis |
| **Package managers** | pnpm (Node), uv (Python) | Gratis |
| **VPS** | Hetzner CX22 o equivalente (2 vCPU, 4GB RAM) | ~EUR 4-8/mes |
| **Dominio** | Uno. Para el proyecto. | ~$12/anio |

### 3.2 Componentes excluidos en Fase 0

El Operador Solitario **NO DEBE** instalar ni configurar en Fase 0: Kubernetes, ArgoCD, Terraform, Langfuse, feature flags, Model Router, ni ningun componente del stack extendido de [STACK::LLM §10.2](urn:fxsl:kb:stack-llm-arquitectura).

### 3.3 Acciones concretas de Dia 1

El Operador Solitario **DEBE** ejecutar las siguientes acciones en orden:

1. Instalar Node.js LTS, Python 3.11+, Docker Desktop, Git.
2. Configurar GitHub con SSH keys.
3. Instalar Claude Code (`npm install -g @anthropic-ai/claude-code`) y configurar la API key.
4. Instalar Gemini CLI como segunda opinion.
5. Crear un repo en GitHub para el proyecto.
6. En el VPS: instalar Docker y Docker Compose. Configurar SSH con key-only auth. Configurar firewall basico (ufw: solo puertos 22, 80, 443).
7. Escribir el primer archivo de context engineering: `CONVENTIONS.md` (ver [-> 9. Context Engineering Progresivo]).

**Resultado verificable:** El Operador Solitario **DEBE** poder abrir Claude Code en su computadora y empezar a construir. El VPS **DEBE** estar listo para recibir deploys.

---

## 4. Fase 1: El Primer Proyecto (Semana 1)

**Objetivo:** Construir y desplegar algo funcional. El tamano no importa; la completitud si.

### 4.1 Perfil Minimo de STACK::LLM

El primer proyecto **DEBE** usar exclusivamente el **Perfil Minimo** de [STACK::LLM §11.1](urn:fxsl:kb:stack-llm-arquitectura):

- **Stack:** TypeScript full-stack. Next.js + Server Actions + Drizzle ORM + PostgreSQL.
- **Infraestructura:** Docker Compose en el VPS. Nginx como reverse proxy. Let's Encrypt para HTTPS.
- **CI/CD:** GitHub Actions con un workflow simple: push -> build -> test -> deploy via SSH.
- **Base de datos:** PostgreSQL en un contenedor Docker. Backup diario con pg_dump a un volumen local (y opcionalmente a object storage).

El primer proyecto **NO DEBE** incluir capa Python, FastAPI, agentes, ni microservicios. Es un monolito TypeScript desplegado con Docker Compose.

### 4.2 Flujo de trabajo

El Operador Solitario **DEBE** seguir este flujo en cada iteracion:

```
1. [Sombrero PO] Definir 3-5 historias para la primera semana
2. [Sombrero Operador] Abrir Claude Code en el repo
3. Dar contexto: "Lee CONVENTIONS.md. Implementa esta historia: [descripcion]"
4. Revisar el output. Iterar. Commitear.
5. Push -> GitHub Actions -> test -> deploy al VPS
6. Verificar en produccion
7. Siguiente historia
```

### 4.3 Context engineering minimo viable

En Fase 1, el Operador Solitario **DEBE** mantener exactamente **dos archivos** de context engineering:

- **CONVENTIONS.md:** Lenguaje (TypeScript), framework (Next.js), estilo de codigo, estructura de carpetas, convenciones de naming, patrones de manejo de errores. 30-50 lineas.
- **SCHEMA.md:** Modelo de datos de la aplicacion. Tablas, relaciones, tipos. Lo que Drizzle necesita saber.

Estos dos archivos, cargados en el contexto del LLM al inicio de cada sesion, son suficientes para que el modelo genere codigo coherente con el proyecto.

### 4.4 IaC minimo

La infraestructura como codigo en Fase 1 **DEBE** ser un unico archivo: `docker-compose.yml`. El Operador Solitario **NO DEBE** usar Terraform ni Pulumi en esta fase. El `docker-compose.yml` se versiona en git, se despliega con `docker compose up -d`, y define completamente la infraestructura.

Si la infraestructura cabe en un `docker-compose.yml`, la Infrastructure as Conversation ([Swarm::Ops §5](urn:fxsl:kb:swarm-ops-metodologia)) es el chat con el LLM: "Necesito agregar un servicio de Redis para caching. Actualiza el docker-compose."

### 4.5 Restricciones de Fase 1

El Operador Solitario **NO DEBE** en Fase 1:

- Implementar autenticacion compleja si no la necesita. Auth.js cuando sea necesario.
- Anadir un ORM complejo. Drizzle + SQL directo para consultas complejas.
- Configurar CI/CD elaborado. Un workflow de GitHub Actions de 30 lineas es suficiente.
- Intentar microservicios. Monolito sin excepciones.
- Instalar herramientas de observabilidad. Si algo falla, los logs se consultan con `docker logs`.

---

## 5. Fase 2: Primer Agente (Mes 1)

**Objetivo:** El proyecto necesita un componente inteligente (chatbot, analizador de documentos, clasificador) que requiere un LLM en produccion, no solo en desarrollo.

**Senal de transicion:** La aplicacion necesita llamar a un LLM para servir a usuarios, no solo para que el Operador Solitario desarrolle.

### 5.1 Cambios respecto a Fase 1

| Componente | Fase 1 | Fase 2 |
|---|---|---|
| **Lenguajes** | TypeScript only | TypeScript (producto) + Python (cognicion) |
| **Backend extra** | --- | FastAPI para la capa de IA |
| **LLM en produccion** | No | Si (via API) |
| **Proxy de modelos** | --- | LiteLLM (rotacion de providers, fallback, control de costes) |
| **Observabilidad LLM** | --- | Langfuse (trazas, costes, calidad) |
| **Vectores** | --- | pgvector (si necesita RAG o busqueda semantica) |

### 5.2 Arquitectura de Fase 2

La arquitectura en Fase 2 **DEBE** seguir esta topologia:

```
[Next.js frontend]
    | API calls
[Next.js API routes / Server Actions] <-> [PostgreSQL]
    | cuando necesita cognicion
[FastAPI (Python)] <-> [LiteLLM proxy] <-> [LLM providers]
    | opcional
[pgvector para embeddings]
```

El frontend y el backend de producto **DEBEN** permanecer en TypeScript. FastAPI **DEBE** entrar solo para la capa cognitiva: el codigo que orquesta llamadas a LLMs, procesa respuestas, maneja RAG, ejecuta cadenas de prompts.

### 5.3 Justificacion de Python en Fase 2

Python entra en Fase 2 por pragmatismo: el ecosistema de IA en Python (LangChain, LlamaIndex, CrewAI, OpenAI SDK, Anthropic SDK, sentence-transformers, scikit-learn) es 10x mas maduro que sus equivalentes en TypeScript. Python tiene las mejores abstracciones, la mejor documentacion, y la mayor representacion en training data para el dominio de IA.

El Operador Solitario **NO DEBE** introducir Python antes de Fase 2.

### 5.4 LiteLLM como proxy

LiteLLM **DEBE** ser el primer proxy de modelos. No es un Model Router sofisticado ([STACK::LLM §9.1](urn:fxsl:kb:stack-llm-arquitectura)); es un proxy que provee:

- **Interfaz unificada:** Llama a OpenAI, Anthropic, Google, Mistral con la misma API.
- **Fallback:** Si Claude esta caido, redirige a GPT automaticamente.
- **Control de costes:** Presupuesto diario/mensual por API key.
- **Logging:** Cada llamada loggeada con tokens consumidos.

El Model Router de 4 tiers **NO DEBE** implementarse antes de Fase 3-4.

### 5.5 Context engineering Fase 2

En Fase 2, el Operador Solitario **DEBE** agregar dos archivos de contexto:

- **ARCHITECTURE.md:** Documenta como se comunican los dos lenguajes y dos procesos. Endpoints internos, formato de mensajes, flujo de datos entre Next.js y FastAPI.
- **CONSTRAINTS.md:** Presupuesto de tokens mensuales. Providers permitidos. Latencia maxima aceptable para llamadas a LLM. Datos que nunca deben ir a un LLM externo.

Total de archivos de contexto en Fase 2: 4 (CONVENTIONS, SCHEMA, ARCHITECTURE, CONSTRAINTS).

---

## 6. Fase 3: Multiples Agentes (Mes 2-3)

**Objetivo:** El proyecto requiere mas de una capacidad cognitiva independiente. Un agente que escribe, otro que revisa. Un agente que busca, otro que sintetiza. Se necesita orquestacion.

**Senal de transicion:** Un solo prompt/cadena no puede resolver el problema y se necesitan agentes con roles diferenciados que se coordinan.

### 6.1 Cambios respecto a Fase 2

| Componente | Fase 2 | Fase 3 |
|---|---|---|
| **Orquestacion** | Cadenas lineales de prompts | Framework de orquestacion (Agents SDK, CrewAI, o custom) |
| **Model Router** | LiteLLM proxy basico | Router con tiers (economico/balance/frontera/razonamiento) |
| **Evals** | Verificacion manual de outputs | Pipeline de evals automatizado (regresion, calidad, coste) |
| **Aislamiento** | Todo en el mismo proceso | Contenedores separados por agente (read-only minimo) |
| **Infraestructura** | Docker Compose | Docker Compose con mas servicios (o primer contacto con K8s) |

### 6.2 Regla de diversidad de modelos

Principio cardinal de [Xanpan::Agents §9.3](urn:fxsl:kb:xanpan-agents-metodologia): si un agente genera algo, el agente que lo verifica **DEBE** usar un modelo diferente. Si el coder usa Claude, el reviewer **DEBE** usar GPT. Si el analizador usa Gemini, el sintetizador **DEBE** usar Claude.

Un modelo no puede detectar sus propios blind spots. Dos modelos tienen blind spots diferentes; la interseccion es mas pequena.

**Correcto:** Agente-coder con Claude Opus, agente-reviewer con GPT-4o.
**Incorrecto:** Agente-coder con Claude Opus, agente-reviewer con Claude Sonnet.

### 6.3 Evals obligatorios en Fase 3

En Fase 2, la verificacion era manual. En Fase 3, la verificacion manual no escala. El Operador Solitario **DEBE** implementar evals automatizados.

Evals minimos requeridos:

1. **Dataset de regresion:** 20-50 ejemplos de input->output esperado para cada capacidad de cada agente. **DEBEN** ejecutarse en cada cambio.
2. **Eval de coste:** Cuantos tokens consumio la tarea. **DEBE** verificar que esta dentro del presupuesto.
3. **Eval de calidad:** Para tareas con output subjetivo, un modelo-juez (diferente al modelo-autor) **DEBE** evaluar calidad con rubric.

El Operador Solitario **PUEDE** implementar evals como un script de Python que ejecuta el dataset, compara outputs, y reporta pass/fail. Frameworks de eval complejos (Braintrust, etc.) **NO DEBE** adoptarse antes de Fase 4.

### 6.4 Context engineering Fase 3

En Fase 3, el Operador Solitario **DEBE** agregar:

- **AGENTS.md:** Quien es cada agente, que modelo usa, que herramientas tiene, que puede y que no puede hacer. Es el directorio del enjambre emergente.

Total de archivos de contexto en Fase 3: 5 (CONVENTIONS, SCHEMA, ARCHITECTURE, CONSTRAINTS, AGENTS).

---

## 7. Fase 4: Enjambre (Cuando el Proyecto lo Exija)

**Objetivo:** El sistema tiene suficientes agentes, suficiente complejidad operacional, y suficiente escala para necesitar los frameworks completos del corpus.

**Senal de transicion:** Docker Compose se vuelve inmanejable. Los deploys manuales son un cuello de botella. Los agentes necesitan coordinarse sin intervencion directa del Operador.

### 7.1 Activacion del corpus completo

En Fase 4, los siguientes documentos dejan de ser opcionales:

| Documento | Que se activa | Justificacion |
|---|---|---|
| **[STACK::LLM §9-10](urn:fxsl:kb:stack-llm-arquitectura)** | Stack extendido completo. Model Router formal. MCP. Aislamiento con Firecracker. | La complejidad tecnica lo exige |
| **[Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia)** | Sistema nervioso adaptativo. IaConversation real. Agente-observer. Security-by-Swarm | Los deploys y la operacion ya no caben en scripts simples |
| **[Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia)** | Metodologia completa. Separacion PO/Operador. Tablero Neural. OKRs formales. Sentinel | Ya no es un solo operador; se necesita estructura para coordinar |

### 7.2 Transicion de Docker Compose a Kubernetes

La migracion a Kubernetes **NO DEBE** tratarse como obligatoria. Es condicional:

- **DEBE** permanecer en Docker Compose si tiene <=10 contenedores, un solo VPS, y el deploy manual con `docker compose pull && docker compose up -d` tarda menos de 2 minutos.
- **DEBERIA** migrar a Kubernetes si tiene >10 contenedores, necesita auto-scaling, necesita zero-downtime deploys, o necesita aislamiento de red entre agentes.

Docker Swarm **PUEDE** usarse como migracion intermedia. Es Kubernetes sin la complejidad. Para operadores solitarios que estan escalando, Docker Swarm es suficiente.

**Correcto:** Migrar a Kubernetes cuando Docker Compose tarda >2 minutos en reiniciar y hay >10 contenedores.
**Incorrecto:** Migrar a Kubernetes en Fase 2 porque "eventualmente lo necesitare".

### 7.3 Senales de fin del Operador Solitario

Fase 4 es donde el Operador Solitario necesita ayuda. Las senales:

- Pasa mas del 50% del tiempo en operacion y menos del 50% en construccion.
- Los incidentes en produccion requieren atencion que no puede dar por horario/capacidad.
- La separacion PO/Operador deja de ser una ficcion util y se vuelve una necesidad real.

Cuando estas senales aparecen, [Xanpan::Agents §16](urn:fxsl:kb:xanpan-agents-metodologia) (Modelo de Transicion) se activa completamente.

---

## 8. Mapa de Fases y Senales de Transicion

El Operador Solitario **DEBE** avanzar de fase solo cuando la senal de transicion correspondiente se manifiesta. **NO DEBE** saltar fases por anticipacion.

| Fase | Horizonte | Senal de entrada | Senal de salida |
|---|---|---|---|
| **Fase 0** | Dia 1 | Decision de iniciar proyecto | Entorno de desarrollo funcional |
| **Fase 1** | Semana 1 | Entorno listo | Aplicacion desplegada en produccion |
| **Fase 2** | Mes 1 | La aplicacion necesita LLM para servir usuarios | Agente funcionando en produccion |
| **Fase 3** | Mes 2-3 | Un solo prompt/cadena no resuelve el problema | Multiples agentes coordinados con evals |
| **Fase 4** | Cuando el proyecto lo exija | Docker Compose inmanejable, deploys como cuello de botella | Corpus completo activado |

---

## 9. Context Engineering Progresivo

El context engineering **DEBE** crecer con el proyecto. El Operador Solitario **NO DEBE** crear archivos de contexto antes de la fase que los requiere.

| Fase | Archivos | Contenido total | Notas |
|---|---|---|---|
| **Fase 0** | --- | --- | Sin proyecto todavia |
| **Fase 1** | CONVENTIONS.md, SCHEMA.md | ~100 lineas | Lo minimo para coherencia de codigo |
| **Fase 2** | + ARCHITECTURE.md, CONSTRAINTS.md | ~250 lineas | Aparece la dualidad TS/Python y los limites de coste |
| **Fase 3** | + AGENTS.md | ~400 lineas | Directorio del enjambre emergente |
| **Fase 4** | + INFRA.md, RUNBOOKS.md | ~600+ lineas | Infraestructura compleja exige documentacion formal |

### 9.1 Regla de relevancia de contexto

El 70% del contexto que se entrega al LLM **DEBE** ser relevante para la tarea actual ([STACK::LLM §8.3](urn:fxsl:kb:stack-llm-arquitectura)). El Operador Solitario **NO DEBE** cargar todos los archivos de contexto en cada sesion. **DEBE** cargar solo los que necesita para la tarea en curso.

### 9.2 Context engineering vs. documentacion

Los archivos de context engineering son artefactos operacionales que alimentan directamente a los LLMs. Si un archivo no cambia como el LLM genera codigo, no es context engineering --- es documentacion tradicional. Ambos tienen valor, pero sirven a propositos diferentes y el Operador Solitario **NO DEBE** confundirlos.

---

## 10. Infraestructura Progresiva

La infraestructura **DEBE** crecer con el proyecto. Cada incremento de infraestructura **DEBE** ser motivado por una necesidad real, no por una expectativa de necesidad futura.

| Capa | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
|---|---|---|---|---|
| **Compute** | 1 VPS (Hetzner CX22) | 1-2 VPS | 2-3 VPS o cluster pequeno | Kubernetes |
| **IaC** | `docker-compose.yml` | `docker-compose.yml` (mas servicios) | Docker Compose + scripts de provisioning | Terraform + ArgoCD |
| **CI/CD** | GitHub Actions (30 lineas) | GitHub Actions (~100 lineas) | GitHub Actions + evals automatizados | [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) completo |
| **Reverse proxy** | Nginx + Let's Encrypt | Nginx + Let's Encrypt | Caddy o Traefik (routing por servicio) | Ingress controller |
| **Backups** | pg_dump cron + volumen local | pg_dump + object storage (S3/R2) | Backup automatizado con verificacion | Backup con disaster recovery |
| **DNS** | 1 dominio, 1-2 registros | Subdominios para servicios | DNS programatico (Cloudflare API) | DNS como codigo |
| **Secrets** | `.env` file (NO en git) | `.env` + Docker secrets | SOPS o Vault | Vault con rotation |

La sobre-ingenieria de infraestructura es el anti-patron mas caro del Operador Solitario porque consume el recurso mas escaso: tiempo.

> **REGLA DEL DOCKER-COMPOSE:** Si la infraestructura cabe en un `docker-compose.yml`, el IaC es ese archivo. La IaConversation ([Swarm::Ops §5](urn:fxsl:kb:swarm-ops-metodologia)) es el chat con el LLM: "Agrega un servicio de Redis para caching." La drift detection es `docker compose config --quiet` comparado con lo que corre en produccion. Cuando Docker Compose deje de ser suficiente, sera evidente --- no porque un documento lo diga.

---

## 11. Observabilidad Progresiva

La observabilidad **DEBE** crecer por niveles. El Operador Solitario **NO DEBE** implementar un nivel sin haber completado los niveles anteriores.

| Nivel | Fase | Implementacion | Coste |
|---|---|---|---|
| **Nivel 0: Logs** | Fase 1 | `docker logs` + grep. Nada mas. | $0 |
| **Nivel 1: Metricas basicas** | Fase 2 | Uptime monitor externo (UptimeRobot, Betterstack free tier). Health endpoint en la app. | $0-7/mes |
| **Nivel 2: Stack de observabilidad** | Fase 3 | Prometheus + Grafana en Docker Compose. Langfuse para trazas LLM. Sentry para errores. | $0-30/mes |
| **Nivel 3: Inteligencia activa** | Fase 4 | Agente-observer ([Swarm::Ops §7](urn:fxsl:kb:swarm-ops-metodologia)). Alertas correlacionadas con deploys. Rollback semi-automatico. | Variable |

### 11.1 Ruta del agente-observer

[Swarm::Ops §7.2](urn:fxsl:kb:swarm-ops-metodologia) describe el agente-observer como un componente maduro. En la practica, **DEBE** construirse en 4 etapas:

1. **Etapa 1: Alertas clasicas.** Prometheus + reglas de alerta estaticas. Si latencia > X ms, alerta a Telegram/Slack. No necesita IA.
2. **Etapa 2: Correlacion manual asistida.** Ante una alerta, el Operador pregunta al LLM: "La latencia subio a las 14:30. Estos son los deploys de hoy [lista]. Cual pudo causar el problema?" El LLM ayuda a diagnosticar, pero el Operador inicia la conversacion.
3. **Etapa 3: Correlacion semi-automatica.** Un script que, ante cada alerta, recoge metricas + timeline de deploys recientes + logs relevantes, y los envia a un LLM para analisis. El output es un diagnostico propuesto que el Operador revisa.
4. **Etapa 4: Agente-observer completo.** Un agente que monitorea continuamente, detecta anomalias pre-alerta, correlaciona automaticamente, y propone (o ejecuta) acciones. Esto es [Swarm::Ops §7.2](urn:fxsl:kb:swarm-ops-metodologia) en su forma madura.

Cada etapa es funcional por si misma. El Operador Solitario **NO DEBE** intentar implementar la etapa 4 directamente. La mayoria de los operadores solitarios operaran en etapa 2-3 durante meses o anos.

---

## 12. Seguridad Progresiva

La seguridad **DEBE** crecer por niveles. Los niveles 0 y 1 **DEBEN** implementarse desde Fase 1 por tener coste cero y esfuerzo minimo.

| Nivel | Fase | Implementacion |
|---|---|---|
| **Nivel 0: Higiene basica** | Fase 1 | SSH con keys (no passwords). Firewall (ufw). HTTPS (Let's Encrypt). Dependencias actualizadas. Secrets en `.env`, nunca en git. |
| **Nivel 1: Aplicacion** | Fase 1-2 | Validacion de inputs (Zod en frontend y backend). Auth.js cuando se necesite autenticacion. CORS configurado correctamente. Rate limiting. |
| **Nivel 2: LLM-specific** | Fase 2-3 | Sanitizacion de inputs antes de enviarlos a LLMs. Nunca incluir secrets en prompts. Validacion de outputs del LLM antes de ejecutar acciones. Presupuesto de tokens como mecanismo anti-abuse. |
| **Nivel 3: Agentes** | Fase 3-4 | Aislamiento de ejecucion por agente (contenedores read-only). Principio de minimo privilegio por agente. Diversidad de modelos entre generador y verificador. |
| **Nivel 4: Security-by-Swarm** | Fase 4 | Agente-security dedicado ([Swarm::Ops §8](urn:fxsl:kb:swarm-ops-metodologia)). Analisis contextual de PRs. Monitoreo de comportamiento en runtime. |

### 12.1 Controles meta del agente-security (quis custodiet)

[Swarm::Ops §8](urn:fxsl:kb:swarm-ops-metodologia) no aborda la seguridad del agente-security mismo. El agente-security tiene un problema de bootstrap: quien lo asegura a el.

El Operador Solitario **DEBE** implementar cuatro controles meta, alineados con el patron del Sentinel en [Xanpan::Agents §9.4](urn:fxsl:kb:xanpan-agents-metodologia):

1. **Modelo diferente al enjambre.** Si los agentes productivos usan Claude, el security-agent **DEBE** usar GPT (o viceversa). Los blind spots no se solapan.
2. **Meta-eval periodico.** Cada mes, el security-agent **DEBE** ser sometido a un conjunto de pruebas adversariales conocidas. Si falla alguna, se recalibra.
3. **Veto asimetrico.** El security-agent **PUEDE** bloquear cualquier PR pero **NO DEBE** aprobar sin pasar por los otros layers de verificacion. Un falso positivo causa delay; un falso negativo en cualquier otra capa lo atrapa.
4. **Auditoria externa periodica.** Cada trimestre (o cuando el presupuesto lo permita), un humano con experiencia en seguridad **DEBE** revisar los logs del security-agent: que aprobo, que rechazo, que debio detectar y no detecto.

---

## 13. Economia: Presupuesto Real por Fase

El Operador Solitario **DEBE** conocer y respetar los rangos de coste por fase. Cada euro gastado **DEBE** justificarse con valor entregado.

| Concepto | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
|---|---|---|---|---|
| **VPS** | EUR 5-10/mes | EUR 10-30/mes | EUR 30-80/mes | EUR 80-300/mes |
| **Dominio + DNS** | EUR 1/mes | EUR 1/mes | EUR 2/mes | EUR 5/mes |
| **API tokens (desarrollo)** | EUR 20-50/mes | EUR 30-80/mes | EUR 50-150/mes | EUR 100-500/mes |
| **API tokens (produccion)** | EUR 0 | EUR 10-100/mes | EUR 50-300/mes | EUR 200-2000/mes |
| **Herramientas SaaS** | EUR 0-20/mes | EUR 0-30/mes | EUR 20-60/mes | EUR 50-200/mes |
| **Total estimado** | **EUR 25-80/mes** | **EUR 50-240/mes** | **EUR 150-590/mes** | **EUR 430-3000/mes** |

### 13.1 Curva de coste

La curva de coste es exponencial: cada fase multiplica el coste de la anterior. El Operador Solitario **NO DEBE** incurrir en costes de Fase 3 cuando esta en Fase 1.

### 13.2 Control de costes

El Operador Solitario **DEBE** configurar alertas de facturacion desde el Dia 1 en toda API de LLM y en el cloud provider. El presupuesto de tokens de [Xanpan::Agents §6.3](urn:fxsl:kb:xanpan-agents-metodologia) es supervivencia financiera del Operador Solitario, no burocracia.

---

## 14. Anti-patrones del Operador Solitario

### 14.1 Sobre-ingenieria prematura

**Sintoma:** Kubernetes en Fase 1. Terraform para un VPS. Feature flags cuando hay 3 usuarios. Model Router de 4 tiers cuando se usa un solo modelo.

**Causa:** Leer el corpus completo y querer implementar todo de golpe.

**Regla:** El Operador Solitario **DEBE** implementar lo que necesita hoy. El corpus es un mapa del territorio completo, no una lista de requisitos minimos.

### 14.2 Sub-ingenieria en seguridad

**Sintoma:** Secrets en el codigo. No HTTPS. No validacion de inputs. LLM con acceso directo a la base de datos.

**Causa:** Asumir que un proyecto personal no necesita seguridad.

**Regla:** La seguridad de Nivel 0-1 ([-> 12. Seguridad Progresiva]) tiene coste cero y esfuerzo minimo. El Operador Solitario **DEBE** implementarla sin excepcion.

### 14.3 Ausencia de backups

**Sintoma:** La base de datos en produccion no tiene backup. O tiene backup pero nunca se ha probado que se pueda restaurar.

**Causa:** Asumir que la perdida de datos no va a ocurrir.

**Regla:** El Operador Solitario **DEBE** configurar `pg_dump` en un cron job el Dia 1 (5 minutos de setup). **DEBE** probar la restauracion del backup el mismo dia (5 minutos adicionales).

### 14.4 Context engineering ausente

**Sintoma:** Cada sesion con el LLM empieza desde cero. El modelo no sabe las convenciones del proyecto. Genera codigo inconsistente.

**Causa:** Asumir que el LLM entiende el proyecto sin contexto explicito.

**Regla:** El Operador Solitario **DEBE** crear CONVENTIONS.md + SCHEMA.md en Fase 1. Son 30 minutos de escritura que ahorran horas de correccion.

### 14.5 Aislamiento del Operador

**Sintoma:** Meses construyendo sin que nadie use lo construido. Sin contacto con usuarios en semanas.

**Causa:** El sombrero Operador es adictivo. Construir es mas comodo que validar.

**Regla:** El sombrero PO **NO DEBE** ser opcional. Al inicio de cada ciclo, el Operador Solitario **DEBE** responder: "Para quien estoy construyendo esto y cuando lo van a usar?" Si no hay respuesta, el ciclo esta mal priorizado.

---

## 15. Caso Real: Korvo-Korax como Proof of Concept

### 15.1 El sistema

Korvo-Korax es un sistema personal que implementa la mayoria de los patrones del corpus a escala minima:

- **1 humano** como PO + Operador (dual-hat, [-> 2. El Operador Solitario como Rol Legitimo]).
- **1 agente principal** (Korax) que genera sub-agentes segun la tarea.
- **1 VPS** en Hetzner como infraestructura.
- **Docker** para browser automation y servicios auxiliares.
- **Telegram** como canal de comunicacion humano-agente.
- **PCA** (Pensamiento Ciclico Asincrono) como estructura temporal light.

### 15.2 Mapeo al corpus

| Concepto del corpus | Implementacion en Korvo-Korax |
|---|---|
| Product Owner | El humano (sombrero PO) |
| Operador | El humano (sombrero Operador) |
| Agente-coder | Korax delegando a Claude Code / Gemini CLI |
| Model Router | LiteLLM proxy con reglas manuales |
| Evals | Verificacion humana + tests automatizados basicos |
| Observabilidad | Logs + uptime monitor + revision manual |
| Context engineering | CONVENTIONS.md + documentos de proyecto |
| IaC | docker-compose.yml |
| CI/CD | GitHub Actions basico |
| Tablero Neural | Lista de tareas en herramienta de gestion personal |
| Retrospectiva | Notas al final de cada ciclo |

### 15.3 Lecciones como reglas

1. **La separacion PO/Operador es real aun siendo ficticia.** El Operador Solitario **DEBE** alternar sombreros conscientemente. Sin sombrero PO explicito, es facil pasar tres semanas refactorizando infraestructura mientras el producto no avanza.

2. **El context engineering es el multiplicador mas barato.** La diferencia entre darle CONVENTIONS.md al LLM y no darselo es la diferencia entre codigo coherente y codigo que necesita reescritura. **DEBE** priorizarse desde Fase 1.

3. **Docker Compose es suficiente mas tiempo del esperado.** El Operador Solitario **NO DEBE** migrar a Kubernetes hasta que las senales de [-> 7. Fase 4: Enjambre] se manifiesten. Korvo-Korax opera con Docker Compose en un solo VPS y no ha encontrado el techo.

4. **Los costes de API tokens son el gasto mas dificil de predecir.** La variabilidad es alta: una tarea compleja puede consumir 10x mas tokens que una tarea simple del mismo tipo. LiteLLM con presupuestos **DEBE** estar activo desde Fase 2.

5. **Telegram como interfaz es funcional.** Para un Operador Solitario, una interfaz de chat asincrona donde puede dar instrucciones al enjambre desde el telefono es mas util que un dashboard web sofisticado. La interfaz minima **PUEDE** ser la interfaz definitiva.

### 15.4 Alcance actual de Korvo-Korax

Korvo-Korax opera en Fase 2-3 del bootstrap path. No tiene:

- Separacion real PO/Operador (violacion consciente).
- Pipeline de evals formal (en transicion de etapa 2 a 3).
- Agente-observer (en etapa 2: correlacion manual asistida).
- Security-by-Swarm (seguridad nivel 2: LLM-specific, sin agente dedicado).
- Kubernetes ni IaC formal (Docker Compose es suficiente).

Esto no es una deficiencia; es el estado correcto para su fase actual.

---

## 16. Mapa de Navegacion del Corpus

### 16.1 Orden de lectura

El Operador Solitario **DEBE** leer los documentos del corpus en este orden:

1. **Chapter 0** (este documento): Bootstrap path. Punto de entrada.
2. **[STACK::LLM](urn:fxsl:kb:stack-llm-arquitectura) v1.0**: Stack de referencia. Consultar segun la fase actual.
3. **[Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) v1.0**: Cuando entre en Fase 3-4, leer completo.
4. **[Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia) v2.1**: Cuando necesite metodologia formal de enjambre, leer completo.

### 16.2 Que documento responde cada pregunta

| Pregunta | Documento | Seccion |
|---|---|---|
| "Que tecnologias uso?" | [STACK::LLM](urn:fxsl:kb:stack-llm-arquitectura) | §0-10 segun la fase |
| "Como empiezo si soy uno solo?" | Chapter 0 | [-> 3. Fase 0: Cimientos] a [-> 7. Fase 4: Enjambre] |
| "Como organizo mi trabajo?" | Chapter 0 + [Xanpan::Agents §4](urn:fxsl:kb:xanpan-agents-metodologia) | PCA adaptado |
| "Como gestiono agentes en produccion?" | [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) | §3-7 |
| "Como hago CI/CD para agentes?" | [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) | §4, 6 |
| "Como defino roles de agentes?" | [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia) | §9 |
| "Como hago evals?" | [STACK::LLM §9.4](urn:fxsl:kb:stack-llm-arquitectura) + [Xanpan::Agents §7.2](urn:fxsl:kb:xanpan-agents-metodologia) | Pipeline concreto + principios |
| "Cuanto va a costar?" | Chapter 0 | [-> 13. Economia: Presupuesto Real por Fase] |
| "Como aseguro mi sistema?" | [STACK::LLM §6](urn:fxsl:kb:stack-llm-arquitectura) + Chapter 0 | [-> 12. Seguridad Progresiva] |
| "Cuando necesito Kubernetes?" | Chapter 0 | [-> 7. Fase 4: Enjambre] + [-> 14. Anti-patrones del Operador Solitario] |

### 16.3 Arquitectura del corpus

```
CHAPTER 0: El Operador Solitario
  "Empieza aqui. Crece desde aqui."
    |
    +-- STACK::LLM v1.0
    |     "Que tecnologias usar. Universal."
    |     Se usa desde Fase 1.
    |
    +-- SWARM::OPS v1.0
    |     "Como operar. Para enjambres."
    |     Se activa en Fase 3-4.
    |
    +-- XANPAN::AGENTS v2.1
          "Como organizar. Metodologia completa."
          Se activa en Fase 4.
```

Chapter 0 es el punto de entrada. [STACK::LLM](urn:fxsl:kb:stack-llm-arquitectura) acompana desde el inicio. [Swarm::Ops](urn:fxsl:kb:swarm-ops-metodologia) y [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia) se activan cuando la complejidad lo exige. No antes.
