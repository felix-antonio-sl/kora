---
_manifest:
  urn: urn:fxsl:kb:chapter0-operador-solitario-p02
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
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:chapter0-operador-solitario
---

# CHAPTER 0: EL OPERADOR SOLITARIO - Parte 02

## 8. Infraestructura Progresiva

La infraestructura crece con el proyecto. La tabla mapea fase a infraestructura concreta:

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

## 9. Observabilidad Progresiva

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

## 10. Seguridad Progresiva

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

## 11. Economía: Presupuesto Real por Fase

| Concepto | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
|---|---|---|---|---|
| **VPS** | €5-10/mes | €10-30/mes | €30-80/mes | €80-300/mes |
| **Dominio + DNS** | €1/mes | €1/mes | €2/mes | €5/mes |
| **API tokens (desarrollo)** | €20-50/mes | €30-80/mes | €50-150/mes | €100-500/mes |
| **API tokens (producción)** | €0 | €10-100/mes | €50-300/mes | €200-2000/mes |
| **Herramientas SaaS** | €0-20/mes | €0-30/mes | €20-60/mes | €50-200/mes |
| **Total estimado** | **€25-80/mes** | **€50-240/mes** | **€150-590/mes** | **€430-3000/mes** |

La curva de coste no es lineal; es exponencial. Cada fase multiplica el coste de la anterior. Esto es esperado y correcto: estás pasando de un proyecto personal a una plataforma. Lo que no es aceptable es saltar a costes de Fase 3 cuando estás en Fase 1. Cada euro gastado debe justificarse con valor entregado.

Control de costes como disciplina, no como restricción: configura alertas de facturación desde el Día 1, en toda API de LLM y en tu cloud provider. El presupuesto de tokens de Xanpan::Agents §6.3 no es burocracia; es supervivencia financiera del Operador Solitario.

---

## 12. Anti-patrones del Operador Solitario

### 12.1 Sobre-ingeniería prematura

**Síntoma:** Kubernetes en Fase 1. Terraform para un VPS. Feature flags cuando tienes 3 usuarios. Model Router de 4 tiers cuando usas un solo modelo.

**Causa:** Leer el corpus completo y querer implementar todo de golpe.

**Corrección:** Implementa lo que necesitas hoy. El corpus es un mapa del territorio completo, no una lista de requisitos mínimos.

### 12.2 Sub-ingeniería en seguridad

**Síntoma:** Secrets en el código. No HTTPS. No validación de inputs. LLM con acceso directo a la base de datos.

**Causa:** "Es solo mi proyecto personal, no necesita seguridad."

**Corrección:** La seguridad de Nivel 0-1 (§10) tiene coste cero y esfuerzo mínimo. No hay excusa para no implementarla.

### 12.3 Ausencia de backups

**Síntoma:** La base de datos en producción no tiene backup. O tiene backup pero nunca se ha probado que se pueda restaurar.

**Causa:** "No me va a pasar."

**Corrección:** `pg_dump` en un cron job es 5 minutos de setup. Restaurar el backup de prueba es otros 5 minutos. Hazlo el Día 1.

### 12.4 Context engineering ausente

**Síntoma:** Cada sesión con el LLM empieza desde cero. El modelo no sabe las convenciones de tu proyecto. Genera código inconsistente.

**Causa:** "El LLM es inteligente, debería entender mi proyecto."

**Corrección:** CONVENTIONS.md + SCHEMA.md en Fase 1. 30 minutos de escritura que ahorran horas de corrección.

### 12.5 Aislamiento del Operador

**Síntoma:** Llevas meses construyendo sin que nadie use lo que construyes. No has hablado con un usuario en semanas.

**Causa:** El sombrero Operador es adictivo. Construir es más cómodo que validar.

**Corrección:** El sombrero PO no es opcional. Al inicio de cada ciclo, fuerza la pregunta: "¿Para quién estoy construyendo esto y cuándo lo van a usar?" Si no hay respuesta, el ciclo está mal priorizado.

---

## 13. Caso Real: Korvo-Korax como Proof of Concept

### 13.1 El sistema

Korvo-Korax es un sistema personal que implementa involuntariamente la mayoría de los patrones del corpus a escala mínima:

- **1 humano** como PO + Operador (dual-hat, §1.1).
- **1 agente principal** (Korax) que genera sub-agentes según la tarea.
- **1 VPS** en Hetzner como infraestructura.
- **Docker** para browser automation y servicios auxiliares.
- **Telegram** como canal de comunicación humano-agente.
- **PCA** (Pensamiento Cíclico Asíncrono) como estructura temporal light.

### 13.2 Mapeo al corpus

| Concepto del corpus | Implementación en Korvo-Korax |
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

### 13.3 Lecciones observadas

1. **La separación PO/Operador es real aun siendo ficticia.** Alternar sombreros conscientemente previene la deriva hacia la optimización técnica infinita. Sin sombrero PO explícito, es fácil pasar tres semanas refactorizando infraestructura mientras el producto no avanza.

2. **El context engineering es el multiplicador más barato.** La diferencia entre darle CONVENTIONS.md al LLM y no dárselo es la diferencia entre código coherente y código que necesita reescritura. Es el máximo ROI/tiempo invertido.

3. **Docker Compose es suficiente para más tiempo del que crees.** La tentación de migrar a Kubernetes llega mucho antes de la necesidad real. Korvo-Korax opera con Docker Compose en un solo VPS y no ha encontrado el techo.

4. **Los costes de API tokens son el gasto más difícil de predecir.** La variabilidad es alta: una tarea compleja puede consumir 10x más tokens que una tarea simple del mismo tipo. El proxy de LiteLLM con presupuestos es esencial desde Fase 2.

5. **Telegram como interfaz es sorprendentemente funcional.** Para un Operador Solitario, una interfaz de chat asíncrona donde puedes dar instrucciones al enjambre desde el teléfono mientras caminas es más útil que un dashboard web sofisticado. La interfaz mínima no es la peor; es la que usas.

### 13.4 Lo que Korvo-Korax no cubre

Korvo-Korax opera en Fase 2-3 del bootstrap path. No tiene:

- Separación real PO/Operador (violación consciente).
- Pipeline de evals formal (en transición de etapa 2 a 3).
- Agente-observer (en etapa 2: correlación manual asistida).
- Security-by-Swarm (seguridad nivel 2: LLM-specific, pero no agente dedicado).
- Kubernetes ni IaC formal (Docker Compose es suficiente).

Esto no es una deficiencia; es el estado correcto para su fase actual.

---

## 14. Cuándo dejar de ser solitario

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

## 15. Mapa de Navegación del Corpus

### 15.1 Orden de lectura recomendado

1. **Chapter 0** (este documento): Bootstrap path. Empieza aquí.
2. **STACK::LLM v1.0**: Stack de referencia. Consulta según tu fase actual.
3. **Swarm::Ops v1.0**: Cuando entres en Fase 3-4, lee completo.
4. **Xanpan::Agents v2.1**: Cuando necesites metodología formal de enjambre, lee completo.

### 15.2 Qué documento responde cada pregunta

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

### 15.3 Arquitectura del corpus

```
CHAPTER 0: El Operador Solitario
 "Empieza aquí. Crece desde aquí."
 │
 ├── STACK::LLM v1.0
 │ "Qué tecnologías usar. Universal."
 │ Se usa desde Fase 1.
 │
 ├── SWARM::OPS v1.0
 │ "Cómo operar. Para enjambres."
 │ Se activa en Fase 3-4.
 │
 └── XANPAN::AGENTS v2.1
 "Cómo organizar. Metodología completa."
 Se activa en Fase 4.
```

Chapter 0 es el punto de entrada. STACK::LLM acompaña desde el inicio. Swarm::Ops y Xanpan::Agents se activan cuando la complejidad lo exige.
