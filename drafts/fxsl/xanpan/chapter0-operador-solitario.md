---
_manifest:
  urn: "urn:fxsl:kb:chapter0-operador-solitario"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-11"
    source: "chapter0-operador-solitario.md (source/fxsl/xanpan)"
version: "1.0.0"
status: draft
tags: [xanpan, llm, bootstrap, operador-solitario, metodologia]
lang: es
extensions:
  fxsl:
    family: methodology
---

# CHAPTER 0: EL OPERADOR SOLITARIO

Bootstrap path para desarrollo asistido por LLM desde una persona con un VPS hasta un sistema con enjambre. Punto de entrada del corpus `STACK::LLM -> Swarm::Ops -> Xanpan::Agents`.

## 0. Premisa y audiencia

Los documentos `STACK::LLM`, `Swarm::Ops` y `Xanpan::Agents` describen un estado maduro: infraestructura existente, agentes operativos, evals y al menos dos roles humanos diferenciados. Este documento cubre la ruta previa.

Perfil objetivo:

- persona sola, sin equipo y sin presupuesto para formar uno
- capacidad técnica para código e infraestructura básica
- acceso a LLMs de frontera por API o suscripción
- acceso a un VPS o cloud básico

Principio de arranque:

- ningún enjambre parte como enjambre
- la prioridad inicial es compatibilidad con crecimiento futuro, no sofisticación inmediata
- toda decisión temprana debe evitar reescritura completa al escalar

## 1. Operador Solitario como rol legítimo

### 1.1 Dual-hat deliberado

`Xanpan::Agents` separa `Product Owner` y `Operador`. En etapa embrionaria una sola persona ocupa ambos roles.

| Sombrero | Foco | Momentos |
| --- | --- | --- |
| `PO` | valor, backlog, scope, usuarios | inicio de ciclo, priorización, validación de ship |
| `Operador` | herramientas, agentes, prompts, infraestructura | implementación, debugging, automatización, operación |

Disciplina obligatoria:

- no mezclar valor de negocio con optimización técnica en la misma decisión
- priorizar como `PO`, ejecutar como `Operador`
- explicitar cambio de sombrero al inicio de cada ciclo y al cierre

### 1.2 PCA como compensador

El `Pensamiento Cíclico Asíncrono` reemplaza ceremonias de equipo:

1. Inicio de ciclo: revisar OKRs, seleccionar historias, priorizar.
2. Ejecución continua: implementar con LLMs y herramientas.
3. Cierre de ciclo: verificar valor entregado, revisar KRs, registrar aprendizaje.

Retrospectiva mínima: nota escrita de 5-10 líneas por ciclo.

## 2. Fase 0: Cimientos

Objetivo: entorno mínimo para construir cualquier proyecto con asistencia de LLM.

### 2.1 Componentes mínimos

| Componente | Elección | Coste |
| --- | --- | --- |
| Máquina local | computador actual | hundido |
| Editor | VS Code o Cursor | gratis / ~USD 20 mes |
| CLI LLM | Claude Code + Gemini CLI | consumo API |
| Control de versiones | GitHub privado | gratis |
| Runtime | Node.js LTS + Python 3.11+ | gratis |
| Package managers | pnpm + uv | gratis |
| VPS | Hetzner CX22 o equivalente, 2 vCPU, 4 GB RAM | ~EUR 4-8 mes |
| Dominio | 1 dominio del proyecto | ~USD 12 año |

### 2.2 Acciones del día 1

1. Instalar Node.js, Python, Docker Desktop y Git.
2. Configurar GitHub con SSH keys.
3. Instalar Claude Code y Gemini CLI.
4. Crear repositorio privado.
5. En el VPS: instalar Docker y Docker Compose.
6. Configurar SSH con claves y firewall `22/80/443`.
7. Crear `CONVENTIONS.md`.

No agregar todavía: Kubernetes, ArgoCD, Terraform, Langfuse, feature flags, model router.

Resultado de cierre: estación local operativa + VPS listo para recibir deploys.

## 3. Fase 1: Primer proyecto

Objetivo: construir y desplegar algo completo. La completitud importa más que el tamaño.

### 3.1 Perfil mínimo de stack

| Capa | Decisión |
| --- | --- |
| Stack | TypeScript full-stack |
| Framework | Next.js + Server Actions |
| Datos | Drizzle ORM + PostgreSQL |
| Infra | Docker Compose + Nginx + Let's Encrypt |
| CI/CD | GitHub Actions simple: build -> test -> deploy por SSH |
| Backups | `pg_dump` diario a volumen local; object storage opcional |

Restricción fuerte:

- sin Python
- sin FastAPI
- sin agentes en producción
- sin microservicios

### 3.2 Flujo de trabajo

1. Definir 3-5 historias por semana.
2. Abrir el repo en la CLI/IDE LLM.
3. Cargar `CONVENTIONS.md`.
4. Implementar historia acotada.
5. Revisar output, iterar y commit.
6. Push -> CI -> deploy.
7. Verificar en producción.

### 3.3 Context engineering mínimo

| Archivo | Contenido | Escala |
| --- | --- | --- |
| `CONVENTIONS.md` | lenguaje, framework, naming, estructura, errores | 30-50 líneas |
| `SCHEMA.md` | tablas, relaciones, tipos, invariantes de datos | compacto |

Esos dos archivos bastan para coherencia de generación.

### 3.4 IaC mínima

`docker-compose.yml` es la IaC suficiente de esta fase.

Regla:

- si la infraestructura cabe en `docker-compose.yml`, usar ese archivo como fuente de verdad
- la conversación con el LLM funciona como `IaConversation` degradada

### 3.5 Anti-acciones de fase 1

- no auth compleja sin necesidad
- no CI/CD sofisticado
- no observabilidad avanzada
- no microservicios
- no ORM sobrecomplicado

## 4. Fase 2: Primer agente

Objetivo: incorporar una capacidad cognitiva en producción.

Señal de transición: la aplicación necesita llamar a un LLM para usuarios finales.

### 4.1 Cambio arquitectónico

| Componente | Fase 1 | Fase 2 |
| --- | --- | --- |
| Lenguajes | TypeScript | TypeScript + Python |
| Capa IA | no existe | FastAPI |
| LLM en prod | no | sí |
| Proxy de modelos | no | LiteLLM |
| Observabilidad LLM | no | Langfuse |
| Vectores | no | pgvector opcional |

### 4.2 Arquitectura base

```text
Next.js frontend
  -> API routes / Server Actions
  <-> PostgreSQL
  -> FastAPI para cognición
  -> LiteLLM
  -> proveedores LLM
  -> pgvector opcional
```

### 4.3 Justificación de Python

Motivo: ecosistema IA más maduro para:

- tool-calling
- RAG
- embeddings
- procesamiento de datos
- librerías de ML/LLM con mejor cobertura documental y de training data

### 4.4 LiteLLM como proxy suficiente

Funciones mínimas:

- interfaz unificada multi-provider
- fallback entre modelos
- control de costos
- logging de tokens

### 4.5 Context engineering acumulado

Se agregan:

- `ARCHITECTURE.md`
- `CONSTRAINTS.md`

Total de contexto operativo: 4 archivos.

## 5. Fase 3: Múltiples agentes

Objetivo: pasar de una cadena cognitiva a roles diferenciados.

Señal de transición: un solo prompt o pipeline lineal ya no resuelve el problema.

### 5.1 Cambios operativos

| Componente | Fase 2 | Fase 3 |
| --- | --- | --- |
| Orquestación | cadenas lineales | framework multi-agente o capa custom |
| Router | LiteLLM básico | tiers formales |
| Evals | revisión manual | regresión + calidad + costo |
| Aislamiento | proceso compartido | contenedores o sandboxes por agente |
| Infra | Compose simple | Compose ampliado o primer contacto con K8s |

### 5.2 Regla de diversidad de modelos

Si un agente genera, otro modelo distinto debe verificar.

Ejemplos:

- coder con Claude, reviewer con GPT
- analista con Gemini, sintetizador con Claude

Razón: reducir intersección de blind spots.

### 5.3 Evals mínimas

1. Dataset de regresión por capacidad: 20-50 ejemplos.
2. Eval de costo por tarea.
3. Eval de calidad con modelo juez distinto al autor.

No hace falta Braintrust en esta etapa; basta un script reproducible.

### 5.4 Context engineering acumulado

Agregar `AGENTS.md`.

Total: 5 archivos de contexto.

## 6. Fase 4: Enjambre

Objetivo: activar el corpus completo cuando el sistema ya no cabe en operación manual ligera.

### 6.1 Activaciones

| Documento | Qué habilita | Cuándo |
| --- | --- | --- |
| `STACK::LLM` §9-10 | router formal, MCP, aislamiento fuerte | complejidad técnica sostenida |
| `Swarm::Ops` | sistema nervioso operativo, IaConversation real, observer | operación ya no cabe en scripts |
| `Xanpan::Agents` | separación PO/Operador, tablero neural, OKRs formales, Sentinel | coordinación multi-agente o multi-humano |

### 6.2 Compose vs Kubernetes

Mantener `Docker Compose` si:

- <= 10 contenedores
- 1 VPS
- deploy manual en < 2 minutos

Migrar a `Kubernetes` si:

- > 10 contenedores
- autoscaling requerido
- zero-downtime obligatorio
- aislamiento de red por agente o servicio

Paso intermedio válido: `Docker Swarm`.

### 6.3 Fin del modo solitario

Señales:

- >50% del tiempo se va en operación
- incidentes requieren cobertura horaria imposible para una persona
- separación `PO/Operador` deja de ser ficción útil y pasa a ser necesidad

## 7. Context engineering progresivo

| Fase | Archivos | Tamaño orientativo | Propósito |
| --- | --- | --- | --- |
| 0 | ninguno | 0 | todavía sin proyecto |
| 1 | `CONVENTIONS`, `SCHEMA` | ~100 líneas | coherencia de código |
| 2 | + `ARCHITECTURE`, `CONSTRAINTS` | ~250 líneas | dualidad TS/Python y límites |
| 3 | + `AGENTS` | ~400 líneas | directorio del enjambre emergente |
| 4 | + `INFRA`, `RUNBOOKS` | 600+ líneas | operación compleja |

Regla 70/30:

- 70% del contexto cargado debe ser relevante para la tarea actual
- no cargar toda la suite en cada sesión

## 8. Infraestructura progresiva

| Capa | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
| --- | --- | --- | --- | --- |
| Compute | 1 VPS | 1-2 VPS | 2-3 VPS o cluster pequeño | Kubernetes |
| IaC | `docker-compose.yml` | Compose ampliado | Compose + scripts | Terraform + ArgoCD |
| CI/CD | Actions simple | Actions mediano | Actions + evals | Swarm::Ops |
| Proxy | Nginx | Nginx | Caddy o Traefik | Ingress controller |
| Backups | `pg_dump` local | + object storage | verificación automatizada | DR formal |
| Secrets | `.env` fuera de git | `.env` + Docker secrets | SOPS o Vault | Vault con rotación |

Principio: introducir complejidad solo cuando una necesidad actual la exija.

## 9. Observabilidad progresiva

| Nivel | Fase | Implementación | Coste |
| --- | --- | --- | --- |
| 0 | 1 | `docker logs` | 0 |
| 1 | 2 | uptime monitor + health endpoint | bajo |
| 2 | 3 | Prometheus + Grafana + Langfuse + Sentry | medio |
| 3 | 4 | agente-observer, correlación con deploys, rollback semi-automático | variable |

Ruta madura del observer:

1. alertas clásicas
2. correlación manual asistida por LLM
3. correlación semi-automática
4. agente-observer continuo

## 10. Seguridad progresiva

| Nivel | Fase | Implementación |
| --- | --- | --- |
| 0 | 1 | SSH con keys, firewall, HTTPS, secrets fuera de git |
| 1 | 1-2 | validación, auth, rate limiting, CORS correcto |
| 2 | 2-3 | sanitización previa a LLM, outputs no confiables, budget enforcement |
| 3 | 3-4 | aislamiento por agente, mínimo privilegio, diversidad de modelos |
| 4 | 4 | `Security-by-Swarm` con agente dedicado |

Meta-controles para el agente de seguridad:

1. modelo distinto al resto del enjambre
2. meta-eval periódica
3. veto asimétrico: puede bloquear, no aprobar solo
4. auditoría humana periódica

## 11. Economía por fase

| Concepto | Fase 1 | Fase 2 | Fase 3 | Fase 4 |
| --- | --- | --- | --- | --- |
| VPS | EUR 5-10 | EUR 10-30 | EUR 30-80 | EUR 80-300 |
| Dominio + DNS | EUR 1 | EUR 1 | EUR 2 | EUR 5 |
| Tokens desarrollo | EUR 20-50 | EUR 30-80 | EUR 50-150 | EUR 100-500 |
| Tokens producción | EUR 0 | EUR 10-100 | EUR 50-300 | EUR 200-2000 |
| SaaS | EUR 0-20 | EUR 0-30 | EUR 20-60 | EUR 50-200 |
| Total estimado | EUR 25-80 | EUR 50-240 | EUR 150-590 | EUR 430-3000 |

Disciplina obligatoria: alertas de facturación desde el día 1.

## 12. Anti-patrones del Operador Solitario

| Anti-patrón | Síntoma | Corrección |
| --- | --- | --- |
| sobre-ingeniería prematura | K8s, Terraform o router complejo en Fase 1 | implementar solo necesidades actuales |
| sub-ingeniería de seguridad | secrets en código, sin HTTPS, LLM con permisos excesivos | aplicar nivel 0-1 inmediatamente |
| sin backups | no existe restauración probada | `pg_dump` + restore de prueba |
| sin context engineering | cada sesión parte de cero | `CONVENTIONS.md` + `SCHEMA.md` tempranos |
| aislamiento del operador | construir sin usuarios ni validación | forzar sombrero `PO` al inicio de cada ciclo |

## 13. Korvo-Korax como proof of concept

### 13.1 Composición

- 1 humano dual-hat `PO + Operador`
- 1 agente principal que delega subagentes
- 1 VPS en Hetzner
- Docker para servicios auxiliares
- Telegram como interfaz
- PCA como estructura temporal

### 13.2 Mapeo al corpus

| Concepto | Implementación en Korvo-Korax |
| --- | --- |
| Product Owner | el humano |
| Operador | el humano |
| agente-coder | Korax delegando a Claude Code / Gemini CLI |
| model router | LiteLLM con reglas manuales |
| evals | revisión humana + tests básicos |
| observabilidad | logs + uptime + revisión manual |
| context engineering | `CONVENTIONS.md` + docs del proyecto |
| IaC | `docker-compose.yml` |
| CI/CD | GitHub Actions básico |
| tablero neural | lista de tareas en herramienta de gestión personal |
| retrospectiva | notas al final de cada ciclo |

### 13.3 Lecciones

1. La separación `PO/Operador` sigue siendo útil aunque sea ficticia.
2. `Context engineering` es el multiplicador con mejor ROI.
3. `Docker Compose` aguanta más de lo que parece.
4. Los costos de tokens son el gasto menos predecible.
5. Una interfaz mínima pero usada supera un dashboard sofisticado ignorado.

### 13.4 Lo que no cubre

- separación real `PO/Operador`
- evals formales
- observer maduro
- `Security-by-Swarm`
- IaC formal o Kubernetes

Eso no es carencia; es alineación con Fase 2-3.

## 14. Cuándo dejar de ser solitario

Señales de que hace falta un segundo humano:

- el backlog crece más rápido de lo que se ejecuta durante 3+ ciclos
- los incidentes caen fuera de la capacidad horaria personal
- el dominio de negocio excede el conocimiento de una sola persona
- los archivos de contexto empiezan a contradecirse por falta de mantenimiento

Señales de que hace falta más infraestructura:

- reiniciar todo con Compose toma > 3 minutos
- hay usuarios activos todo el día y se necesita zero-downtime
- backup y DR dejan de ser triviales
- un VPS más grande ya no resuelve el cuello de botella

Señales de que hace falta activar el corpus completo:

- 4+ agentes coordinándose
- gasto en tokens > EUR 500 mes
- evals manuales insuficientes
- un incidente causado por agentes tarda horas en diagnosticarse

## 15. Mapa de navegación del corpus

Orden recomendado:

1. `Chapter 0`
2. `STACK::LLM`
3. `Swarm::Ops`
4. `Xanpan::Agents`

Preguntas frecuentes:

| Pregunta | Documento | Sección |
| --- | --- | --- |
| qué tecnologías usar | `STACK::LLM` | §0-10 según fase |
| cómo partir solo | `Chapter 0` | §2-6 |
| cómo organizar trabajo y ciclos | `Chapter 0` + `Xanpan::Agents` | PCA adaptado |
| cómo operar agentes en producción | `Swarm::Ops` | §3-7 |
| cómo hacer CI/CD para agentes | `Swarm::Ops` | §4, §6 |
| cómo definir roles de agentes | `Xanpan::Agents` | §9 |
| cómo hacer evals | `STACK::LLM` + `Xanpan::Agents` | §9.4 + §7.2 |
| cuánto costará | `Chapter 0` | §11 |
| cómo asegurar el sistema | `STACK::LLM` + `Chapter 0` | §6 + §10 |
| cuándo pasar a Kubernetes | `Chapter 0` | §6.2 + §14 |

Arquitectura del corpus:

```text
Chapter 0
  "Empieza aquí. Crece desde aquí."
    -> STACK::LLM
       "Qué tecnologías usar. Universal."
       Se usa desde Fase 1.
    -> Swarm::Ops
       "Cómo operar. Para enjambres."
       Se activa en Fase 3-4.
    -> Xanpan::Agents
       "Cómo organizar. Metodología completa."
       Se activa en Fase 4.
```

`Chapter 0` es bootstrap. `STACK::LLM` acompaña desde Fase 1. `Swarm::Ops` y `Xanpan::Agents` se activan cuando la complejidad lo exige.
