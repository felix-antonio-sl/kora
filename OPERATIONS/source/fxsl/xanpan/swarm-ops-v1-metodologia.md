# SWARM::OPS v1.0

## La Reconstrucción del CI/CD y DevOps para la Era de Enjambres de Agentes

*Cuando el pipeline era una línea recta y el futuro es un sistema nervioso*

Companion document de **Xanpan::Agents v2.1**
Febrero 2026

---

## Índice

0. [Obituario del Pipeline Lineal](#0-obituario-del-pipeline-lineal)
1. [Arqueología: Qué eran CI/CD y DevOps y por qué existían](#1-arqueología-qué-eran-cicd-y-devops-y-por-qué-existían)
2. [La Gran Fractura: Por qué el modelo se rompe](#2-la-gran-fractura-por-qué-el-modelo-se-rompe)
3. [Swarm::Ops — El nuevo paradigma](#3-swarmops--el-nuevo-paradigma)
4. [Del Pipeline al Sistema Nervioso](#4-del-pipeline-al-sistema-nervioso)
5. [Infraestructura como Conversación](#5-infraestructura-como-conversación)
6. [El Agente como Ciudadano de Primera Clase del Pipeline](#6-el-agente-como-ciudadano-de-primera-clase-del-pipeline)
7. [Observabilidad: De Dashboards Pasivos a Inteligencia Activa](#7-observabilidad-de-dashboards-pasivos-a-inteligencia-activa)
8. [Seguridad: DevSecOps Muere, Nace Security-by-Swarm](#8-seguridad-devsecops-muere-nace-security-by-swarm)
9. [El Operador como Platform Engineer del Enjambre](#9-el-operador-como-platform-engineer-del-enjambre)
10. [Modos de Fallo y Circuit Breakers Operacionales](#10-modos-de-fallo-y-circuit-breakers-operacionales)
11. [Stack de Referencia 2026](#11-stack-de-referencia-2026)
12. [Síntesis: Tabla de Correspondencia Prehistoria → Swarm::Ops](#12-síntesis-tabla-de-correspondencia-prehistoria--swarmops)

---

# 0. Obituario del Pipeline Lineal

> *"If you've been building CI/CD pipelines for any length of time, you know the rhythm. A commit triggers a build. Tests run. Artifacts get pushed. Maybe a deployment fires. It's linear, predictable, and honestly a little boring in the best possible way. That's about to change."*
> — Micheal Lanham, febrero 2026

Nació en los años 90 como "nightly build." Creció en los 2000 como "Continuous Integration" gracias a Martin Fowler y Kent Beck. Maduró en los 2010 como "CI/CD pipeline" con Jenkins, Travis, CircleCI. Se sofisticó en los 2020 con GitHub Actions, GitLab CI, y la explosión de YAML.

**Y en 2026 llega al final de su forma reconocible.**

No porque falle. Porque el mundo para el que fue diseñado ya no existe. El pipeline lineal fue la respuesta genial a una pregunta simple: *¿cómo integramos el trabajo de múltiples desarrolladores humanos que escriben código en paralelo y necesitan verificar que su código combinado funciona?*

Esa pregunta asumía:

- **Los autores del código son humanos** que cometen errores impredecibles.
- **Los commits son discretos y espaciados** (horas o días entre ellos).
- **Los tests son escritos por los mismos humanos** que escriben el código.
- **El deploy es un evento significativo** que requiere coordinación.
- **La infraestructura es estable** entre deploys.

Cada una de esas asunciones está colapsando.

> ⚡ **LA DISCONTINUIDAD OPERACIONAL**
>
> Cuando los agentes IA generan código, los commits llegan en ráfagas de minutos, no horas. Cuando el mismo enjambre que codifica también genera tests, la independencia evaluador/evaluado se pierde. Cuando los deploys pueden ocurrir decenas de veces al día, el "evento significativo" se disuelve en flujo continuo. Cuando la infraestructura se define conversacionalmente, el YAML manual se vuelve arqueología. El pipeline lineal no se rompe. Se vuelve insuficiente.

DevOps como movimiento cultural tampoco muere. Su esencia —destruir el muro entre dev y ops, automatizar todo lo automatizable, hacer feedback loops más cortos— es eterna. Lo que muere es la **implementación específica** de esa esencia: el YAML artesanal, el Jenkins con 47 plugins, el Helm chart que nadie entiende, el dashboard de Grafana que nadie mira hasta que hay incidente.

**Swarm::Ops** es la reconstrucción desde primeros principios de las funciones que CI/CD y DevOps cumplían, rediseñadas para un mundo donde el enjambre de agentes IA es el ejecutor primario del código.

---

# 1. Arqueología: Qué eran CI/CD y DevOps y por qué existían

Antes de demoler, hay que entender. Cada pieza del edificio existía por una razón. Demoler sin entender es vandalismo; demoler entendiendo es arquitectura.

## 1.1 Las funciones fundamentales (lo que hacían, no cómo lo hacían)

Todo el aparato de CI/CD y DevOps cumplía exactamente **siete funciones**:

| # | Función | Problema que resolvía | Implementación clásica |
|---|---|---|---|
| **F1** | Integración | Verificar que código de múltiples autores funciona junto | CI server (Jenkins, GitHub Actions, GitLab CI) |
| **F2** | Verificación | Confirmar que el código cumple especificaciones | Test runners (pytest, Jest, JUnit) |
| **F3** | Empaquetado | Crear artefactos desplegables desde código fuente | Build systems (Docker, Webpack, Maven) |
| **F4** | Entrega | Mover artefactos a ambientes de ejecución | CD pipelines, registros de contenedores, Helm |
| **F5** | Provisioning | Crear y configurar infraestructura | IaC (Terraform, Pulumi, CloudFormation) |
| **F6** | Observabilidad | Ver qué está pasando en producción | Monitoring stacks (Prometheus+Grafana, Datadog) |
| **F7** | Recuperación | Volver a un estado funcional cuando algo falla | Rollback mechanisms, runbooks, on-call rotations |

**Estas siete funciones no desaparecen.** Son invariantes del software como sistema vivo (igual que el valor de negocio por historia es invariante en Xanpan::Agents). Lo que cambia radicalmente es **quién las ejecuta, cómo se coordinan, y a qué velocidad operan.**

## 1.2 DevOps: el movimiento cultural

DevOps (Debois, 2009; Humble & Farley, 2010) no era una herramienta ni un rol. Era un movimiento cultural con tres axiomas:

1. **Destruir el muro dev/ops:** Los que construyen y los que operan deben ser el mismo equipo o al menos compartir responsabilidad.
2. **Automatizar todo lo automatable:** Si un humano lo hace más de dos veces, debería ser un script.
3. **Feedback loops cortos:** Cuanto antes sepas que algo falló, más barato es arreglarlo.

Estos tres axiomas son **atemporales**. Sobreviven intactos. Pero su implementación a través de "ingenieros DevOps" que escriben YAML, mantienen Jenkins, y rotan on-call es lo que está mutando.

## 1.3 Platform Engineering: la evolución pre-agente

Ya antes de los enjambres de agentes, DevOps estaba evolucionando. Platform Engineering (Gartner predice 80% de adopción en organizaciones grandes para 2026) reconoce que DevOps a escala genera problemas:

- **Tool sprawl:** Demasiadas herramientas, cada equipo con su propia configuración.
- **Cognitive load:** Los developers cargan con responsabilidad operacional que no quieren ni saben manejar.
- **"Shift left" mal ejecutado:** "Shift left" suena bien pero en la práctica significó "dump left"—tirar más responsabilidad sobre los developers.

Platform Engineering responde con **Internal Developer Platforms (IDPs)**: plataformas internas que abstraen la complejidad operacional y ofrecen self-service a los developers. Es DevOps empaquetado como producto.

**Swarm::Ops absorbe Platform Engineering** y lo lleva al siguiente nivel: no solo los developers son clientes de la plataforma; **los agentes IA son el cliente primario.**

---

# 2. La Gran Fractura: Por qué el modelo se rompe

## 2.1 Cinco asunciones que colapsan

### Asunción 1: "Los commits son espaciados y discretos"

En equipos humanos, un developer hace 2-5 commits significativos al día. Un pipeline que tarda 15-30 minutos en ejecutar puede absorber ese volumen. Con un enjambre de agentes, los commits llegan en ráfagas: un agente puede generar un PR cada 10-30 minutos. Si hay 5 agentes trabajando en paralelo, el pipeline recibe 10-30 PRs/hora.

**Consecuencia:** El pipeline secuencial se convierte en cuello de botella. No falla; se satura.

### Asunción 2: "Los tests son independientes del código"

En TDD clásico, un humano escribe tests con su comprensión del dominio, y otro humano (o el mismo en otro momento) escribe código. Hay cierta independencia cognitiva. Con agentes, **el mismo modelo que genera el código genera los tests.** Si el modelo tiene un error de comprensión, genera código incorrecto Y tests que validan el código incorrecto. Los tests pasan. El bug se esconde.

**Consecuencia:** CI verde no garantiza corrección. Se necesita una capa adicional: evals independientes con modelos diferentes (ver §8 y Xanpan::Agents §15.1).

### Asunción 3: "Los YAML de pipeline son escritos y mantenidos por humanos"

En 2025, un pipeline de GitHub Actions medianamente complejo tiene 200-500 líneas de YAML. Un monorepo puede tener 20-50 archivos de workflow. Mantener esto es un trabajo a tiempo completo. Y es exactamente el tipo de trabajo que los agentes hacen bien: seguir reglas, generar configuración, mantener coherencia.

**Consecuencia:** El YAML artesanal se vuelve un anti-patrón. La configuración de pipelines se genera y mantiene por agentes, con aprobación humana de cambios significativos.

### Asunción 4: "El deploy es un evento que requiere decisión humana"

Cuando deployas una vez al día o a la semana, cada deploy es un "evento." Alguien aprueba, alguien observa, alguien está listo para rollback. Con agentes generando historias completas en horas, el ritmo natural de deploy es continuo. Hacer de cada deploy un evento humano recrear el cuello de botella que Xanpan::Agents eliminó.

**Consecuencia:** El deploy humano se reserva para cambios destructivos o de alto riesgo. El resto es deploy continuo con feature flags + eval + rollback automático.

### Asunción 5: "La infraestructura se define en archivos estáticos"

Terraform, Pulumi, CloudFormation: todos asumen que un humano escribe definiciones de infraestructura, las versiona, las aplica. Con agentes, la infraestructura se puede definir conversacionalmente: "necesito un cluster de 3 nodos con GPU para el agente de embeddings." El agente traduce a IaC, aplica, verifica.

**Consecuencia:** IaC no muere (el archivo de Terraform sigue siendo el artefacto versionado y auditable), pero el humano deja de escribirlo directamente. Es "Infrastructure as Conversation" con IaC como artefacto intermedio.

## 2.2 Lo que NO cambia

Antes de seguir demoliendo, anclar los invariantes:

- **Idempotencia:** Las operaciones de infraestructura deben poder re-ejecutarse sin efectos secundarios indeseados. Esto es verdad con o sin agentes.
- **Inmutabilidad de artefactos:** Una imagen de contenedor construida es inmutable. No se parchea en producción. Esto es verdad con o sin agentes.
- **Trazabilidad:** Cada cambio en producción debe ser rastreable hasta un commit, un PR, una decisión. Con agentes, esto se amplifica: también debe ser rastreable hasta la historia de usuario y el OKR que la originó.
- **Principio de mínimo privilegio:** Cada componente del sistema (humano o agente) tiene exactamente los permisos que necesita y ninguno más.
- **Blast radius control:** Un fallo debe contenerse. Un deploy defectuoso no debería afectar al 100% de los usuarios. Canary deploys, feature flags, traffic splitting: los mecanismos cambian pero el principio es eterno.

---

# 3. Swarm::Ops — El nuevo paradigma

## 3.1 Definición

**Swarm::Ops** es el framework operacional que reemplaza CI/CD y DevOps en el contexto de Xanpan::Agents. No es un producto ni una herramienta. Es un conjunto de principios, funciones y patrones para operar software cuando el enjambre de agentes IA es el ejecutor primario.

## 3.2 Los tres cambios de paradigma

### Cambio 1: De Pipeline a Sistema Nervioso

El pipeline era una secuencia lineal: commit → build → test → staging → deploy. En Swarm::Ops, las operaciones son un **grafo adaptativo** donde múltiples flujos coexisten, se bifurcan y convergen. No hay un "pipeline" único; hay un sistema nervioso que responde en tiempo real a eventos: nuevos commits, nuevos evals, alertas de producción, propuestas del Sentinel, cambios de configuración.

### Cambio 2: De Configuración Estática a Intención Declarada

En CI/CD clásico, la configuración es imperativa: "ejecuta estos pasos en este orden." En Swarm::Ops, la configuración es declarativa de intención: "quiero que cada historia pase por verificación de tipos, tests unitarios, eval de seguridad y eval de regresión antes de ser candidata a deploy." El enjambre determina el cómo. El humano declara el qué.

### Cambio 3: De Herramienta Pasiva a Agente Activo

Las herramientas de CI/CD son pasivas: se configuran, se ejecutan cuando se les invoca, reportan resultados. En Swarm::Ops, los componentes operacionales son **agentes activos** que toman decisiones: el agente de eval decide qué tests ejecutar basado en el tipo de cambio; el agente de deploy decide si hacer canary o full basado en el riesgo; el agente de observabilidad detecta anomalías y propone rollback antes de que un humano lo note.

## 3.3 Las siete funciones, reconstruidas

| # | Función (invariante) | Implementación Prehistórica | Implementación Swarm::Ops |
|---|---|---|---|
| **F1** | Integración | CI server ejecuta merge + build | Agente-integrador verifica coherencia semántica, no solo sintáctica. Merge inteligente que resuelve conflictos triviales autónomamente. |
| **F2** | Verificación | Test runners ejecutan suites estáticas | Agente-verificador selecciona tests según tipo de cambio + eval independiente con modelo diferente al autor. Cobertura adaptativa. |
| **F3** | Empaquetado | Build determinista → imagen inmutable | Preservado. Docker build sigue siendo la respuesta. Lo que cambia: el Dockerfile lo genera/mantiene un agente. |
| **F4** | Entrega | Pipeline de deploy con stages fijos | Agente-deployer con estrategia adaptativa: canary para cambios de riesgo, fast-track para cambios triviales. Feature flags como primitiva base. |
| **F5** | Provisioning | IaC estática (Terraform/Pulumi) | Infrastructure as Conversation: el Operador describe intención, el agente genera IaC, aplica, verifica. El artefacto IaC se versiona como antes. |
| **F6** | Observabilidad | Dashboards pasivos + alertas | Agente-observer analiza métricas en tiempo real, detecta anomalías, correlaciona con deploys recientes, propone diagnóstico y acción. |
| **F7** | Recuperación | Rollback manual + runbooks | Rollback automático cuando evals post-deploy fallan. Runbooks ejecutados por agentes. Humano interviene solo en recuperaciones complejas. |

---

# 4. Del Pipeline al Sistema Nervioso

## 4.1 Anatomía del sistema nervioso

El "pipeline" clásico era una metáfora industrial: una línea de ensamblaje donde cada estación añade algo y pasa al siguiente. El sistema nervioso de Swarm::Ops es una metáfora biológica: una red de nodos conectados que procesan señales, toman decisiones locales y escalan a decisiones globales cuando es necesario.

### Componentes del sistema nervioso

- **Receptores (eventos de entrada):** commit, PR, alerta de producción, cambio de configuración, propuesta del Sentinel, heartbeat del enjambre, resultado de eval.
- **Nervios aferentes (análisis):** Clasificación automática del evento. ¿Es cambio de código, de infra, de config? ¿Qué riesgo tiene? ¿Qué zona del codebase afecta? ¿Requiere intervención humana?
- **Centro de procesamiento (orquestador):** El agente-orquestador decide qué acciones ejecutar basado en las reglas declaradas por el Operador y la clasificación del evento.
- **Nervios eferentes (ejecución):** Los agentes especializados ejecutan: build, test, eval, deploy, rollback, notificación.
- **Feedback loop:** El resultado de cada acción alimenta al sistema. Un test fallido re-clasifica el PR. Un eval exitoso avanza el deploy. Una anomalía post-deploy dispara rollback.

## 4.2 Flujos, no pasos

En CI/CD clásico, piensas en "pasos" secuenciales. En Swarm::Ops, piensas en **flujos concurrentes** que se coordinan:

**Flujo de verificación (continuo):**
Cada PR del enjambre entra en verificación inmediata. No espera a que "termine el pipeline anterior." Los evals se ejecutan en paralelo con priorización por riesgo del cambio:

- Cambio tipo `lectura` → lint + type check + tests unitarios. Minutos.
- Cambio tipo `escritura` → lo anterior + eval de regresión + tests de integración. Minutos.
- Cambio tipo `destructivo` → lo anterior + eval de seguridad + hold para aprobación humana. Horas.

**Flujo de deploy (continuo):**
Los cambios verificados se acumulan en un buffer de deploy. El agente-deployer tiene una estrategia configurable:

- **Modo ráfaga:** Deploy cada N minutos si hay cambios verificados. Para ambientes de desarrollo.
- **Modo canary:** Deploy a % pequeño de tráfico, monitorea, expande. Para producción.
- **Modo manual:** Hold para aprobación humana. Para cambios destructivos o de alto riesgo.

**Flujo de observación (permanente):**
El agente-observer monitorea producción independientemente de los otros flujos. No espera que alguien le pregunte. Detecta anomalías en latencia, errores, consumo de recursos. Si correlaciona una anomalía con un deploy reciente, propone rollback automáticamente.

## 4.3 El fin del "CI verde = listo"

En CI/CD clásico, "CI verde" era la señal de confianza. En Swarm::Ops, CI verde es **condición necesaria pero radicalmente insuficiente** cuando los agentes generan tanto el código como los tests. La señal de confianza es multi-capa:

1. **CI verde** (lint, types, tests): condición mínima.
2. **Eval de regresión pasado** (con dataset parcialmente humano): verificación de que no rompe lo existente.
3. **Eval de diversidad** (reviewer-agent con modelo diferente al coder-agent): verificación de que otro "cerebro" llega a la misma conclusión.
4. **Eval de seguridad** (análisis estático + dinámico + check de privilegios): verificación de postura de seguridad.
5. **Aprobación humana** (para cambios de riesgo): el último firewall es humano.

Solo cuando las 5 capas pasan, el cambio es candidato a deploy. Esto es más lento que "CI verde → deploy" pero más robusto contra el modo de fallo de alucinación sistémica (Xanpan::Agents §15.1).

---

# 5. Infraestructura como Conversación

## 5.1 De IaC a IaConversation (pasando por IaC)

Infrastructure as Code (HashiCorp, 2014) fue revolucionario: en vez de clicks en consolas, la infraestructura se define en archivos versionados y aplicados con herramientas deterministas. Ese principio es eterno. Lo que cambia es quién escribe los archivos.

**IaC clásico:**
```
Humano escribe Terraform → terraform plan → humano revisa plan → terraform apply
```

**Infrastructure as Conversation (Swarm::Ops):**
```
Operador describe intención en lenguaje natural →
Agente genera Terraform/Pulumi →
Agente ejecuta plan →
Operador revisa diff y aprueba →
Agente aplica →
Agente verifica estado post-aplicación
```

**El artefacto IaC sigue existiendo.** Se versiona en git. Es auditable. Es reproducible. Lo que desaparece es la escritura manual de HCL/YAML/CDK por humanos. El humano describe la intención; el agente produce el artefacto; el humano verifica que el artefacto captura la intención.

> ⚡ **MODO DEGRADADO: Cuando tu infra cabe en un docker-compose.yml**
>
> IaConversation asume infraestructura compleja. Para un equipo con 1 VPS y Docker Compose, todo este aparato es innecesario. El modo degradado es simple: **tu `docker-compose.yml` es tu IaC, y tu IaConversation es el chat con tu agente LLM.** "Necesito agregar Redis para caching" → el agente actualiza el docker-compose → tú revisas el diff → `docker compose up -d`. Eso cumple las 5 fases del patrón (intent, plan, diff, apply, verify) sin Terraform, sin Pulumi, sin plataforma conversacional. IaConversation escala hacia arriba, no hacia abajo: empieza con docker-compose y crece hacia Terraform/Pulumi cuando la complejidad de infraestructura lo exija, no antes.

## 5.2 Pulumi Neo como proto-patrón

Pulumi Neo (2025-2026) es el ejemplo más avanzado de este patrón: describes lo que necesitas en lenguaje natural, Neo genera el plan de ejecución, crea un PR con el código IaC, y espera aprobación. AWS Kiro sigue el mismo patrón. Google Cloud y Azure están convergiendo.

El patrón es universal e independiente del provider:

1. **Intent declaration:** El Operador declara intención ("necesito un cluster PostgreSQL de alta disponibilidad con réplica de lectura en us-east-1 y eu-west-1").
2. **Plan generation:** El agente genera el plan IaC completo.
3. **Diff review:** El Operador revisa el diff contra el estado actual.
4. **Apply with verification:** El agente aplica y verifica que el estado real coincide con el declarado.
5. **Drift detection:** El agente monitorea continuamente que la infraestructura real no derive del estado declarado.

## 5.3 Context engineering para infraestructura

Igual que Xanpan::Agents tiene CONVENTIONS.md y ARCHITECTURE.md para el código, Swarm::Ops tiene archivos de contexto para infraestructura:

- **INFRA.md:** Arquitectura de infraestructura actual. Providers, regiones, servicios principales, patrones de networking.
- **CONSTRAINTS.md:** Restricciones operacionales: presupuesto cloud, compliance requirements (data residency, encryption), SLAs comprometidos.
- **RUNBOOKS.md:** Procedimientos de recuperación para incidentes conocidos. Escritos para ser ejecutados por agentes, no por humanos con sueño a las 3am.

Estos archivos alimentan al agente de infraestructura para que sus propuestas sean coherentes con la realidad y las restricciones del sistema.

---

# 6. El Agente como Ciudadano de Primera Clase del Pipeline

> *"Agent runners are doing for 'how AI executes safely inside your delivery system' what containers did for 'how code runs.'"*
> — Micheal Lanham, 2026

## 6.1 El problema: pipelines diseñados para scripts, no para agentes

Los pipelines de CI/CD actuales ejecutan scripts: comandos deterministas que producen el mismo output dado el mismo input. Los agentes IA NO son scripts:

- **Son no-deterministas:** El mismo prompt puede producir outputs diferentes.
- **Necesitan contexto amplio:** No solo el diff del PR; necesitan entender la arquitectura, las convenciones, las dependencias.
- **Consumen recursos impredeciblemente:** Un agente puede necesitar 1K tokens o 100K tokens dependiendo de la complejidad.
- **Pueden fallar de formas no-discretas:** Un script falla con exit code 1. Un agente puede "fallar" generando output incorrecto que parece correcto.

## 6.2 Cuatro primitivas para agentes en pipelines

GitHub Agentic Workflows (preview febrero 2025, GA esperado 2026) identifica cuatro primitivas necesarias para que agentes sean ciudadanos de primera clase:

> ⚠️ **CAVEAT DE MADUREZ:** Estas primitivas están emergiendo. GitHub Agentic Workflows está en preview; AWS AgentCore es nuevo. Lo que sigue describe el modelo conceptual correcto, pero las implementaciones comerciales todavía no son GA. **Mientras tanto, ejecutar agentes en containers Docker con permisos restrictivos (filesystem read-only, red limitada, secrets inyectados selectivamente, logging de cada acción) cumple las cuatro funciones descritas abajo.** No es necesario esperar a plataformas comerciales para implementar el patrón.

### Primitiva 1: Workflow Definition (qué y cómo)
Qué dispara al agente, qué permisos tiene, qué artefactos puede leer/escribir, qué outputs produce. Es el "contrato" entre el pipeline y el agente.

### Primitiva 2: Execution Sandbox (aislamiento)
El agente ejecuta en un entorno aislado con filesystem limitado, acceso a red controlado, secretos inyectados selectivamente, y logging determinista de cada acción. **Cada acción del agente es auditable.** No hay "caja negra."

### Primitiva 3: Safe Operation Primitives (seguridad por defecto)
Por defecto: read-only sobre el repo, acciones limitadas y auditables, outputs estructurados que herramientas downstream pueden validar. Escalar privilegios requiere declaración explícita y aprobación.

### Primitiva 4: State Management (memoria entre ejecuciones)
Los agentes pueden necesitar estado entre ejecuciones: "la última vez que evalué este módulo, la cobertura era X." AWS AgentCore introduce "memory snapshots" que se promueven junto con artefactos de código a través del pipeline. El estado del agente se versiona como el código.

## 6.3 La muerte del "runner" como concepto

En CI/CD clásico, un "runner" es una máquina que ejecuta scripts. En Swarm::Ops, el concepto se bifurca:

- **Execution Environment:** La máquina/container donde corre el código generado (build, test). Esto sigue existiendo y sigue siendo determinista.
- **Agent Runtime:** El entorno donde el agente IA razona y produce outputs. No es determinista. Necesita acceso a modelo de lenguaje, contexto del proyecto, y estado previo. Es un animal completamente diferente.

El pipeline debe gestionar ambos como entidades distintas con lifecycle, permisos y monitoreo diferentes.

---

# 7. Observabilidad: De Dashboards Pasivos a Inteligencia Activa

## 7.1 La evolución de la observabilidad

**Era 1 — Monitoreo (2000s):** ¿Está arriba? CPU, RAM, disco. Nagios, Zabbix. Alertas cuando un umbral se cruza.

**Era 2 — Observabilidad (2010s):** Logs, métricas, traces. Los "tres pilares." Prometheus, Grafana, Jaeger, ELK. Dashboards que un humano interpreta.

**Era 3 — Inteligencia Activa (2026+):** Un agente-observer analiza los tres pilares en tiempo real, correlaciona con eventos recientes (deploys, cambios de config), detecta anomalías antes de que crucen umbrales de alerta, y propone acciones.

## 7.2 El agente-observer

El agente-observer no reemplaza Prometheus+Grafana. Los usa como fuente de datos. Lo que reemplaza es al **humano que mira dashboards:**

> ⚠️ **RUTA DE IMPLEMENTACIÓN PROGRESIVA:** El agente-observer tal como se describe abajo es un sistema complejo — analizar métricas en real-time, correlacionar con deploys, y proponer rollbacks requiere un nivel de context engineering y evals que es un proyecto en sí mismo. No nace adulto. La ruta progresiva tiene cuatro etapas:
>
> 1. **Etapa 1: Alertas clásicas.** Prometheus + reglas de alerta estáticas. Si latencia > umbral, alerta a Slack/Telegram. Sin IA.
> 2. **Etapa 2: Correlación manual asistida.** Ante una alerta, el Operador consulta un LLM con métricas + timeline de deploys. El LLM ayuda a diagnosticar.
> 3. **Etapa 3: Correlación semi-automática.** Un script que ante cada alerta recopila contexto (métricas, deploys, logs) y los envía a un LLM para diagnóstico propuesto. El Operador revisa.
> 4. **Etapa 4: Agente-observer completo.** Lo descrito en esta sección. Monitoreo continuo, detección pre-alerta, correlación automática, propuesta de acciones.
>
> Cada etapa es funcional por sí misma. La mayoría de los equipos operarán en etapas 2-3 durante meses antes de necesitar la etapa 4.

| Función | Humano (clásico) | Agente-observer (Swarm::Ops) |
|---|---|---|
| Detectar anomalía | Nota patrón raro en dashboard o recibe alerta | Analiza métricas continuamente; detecta anomalías estadísticas pre-alerta |
| Correlacionar causa | "¿Hubo un deploy reciente? ¿Cambió algo?" | Cruza automáticamente con timeline de deploys, cambios de config, cambios de tráfico |
| Diagnosticar | Revisa logs, traces, busca root cause | Analiza logs/traces filtrando por ventana temporal de anomalía; propone top-3 hipótesis |
| Proponer acción | "Creo que deberíamos rollback" | "Anomalía correlacionada con deploy X. Confianza 87%. Recomendación: rollback. ¿Aprobar?" |
| Ejecutar | Ejecuta rollback manual o via script | Si aprobado (o en modo auto para anomalías severas), ejecuta rollback y verifica |

## 7.3 OpenTelemetry como lingua franca

OpenTelemetry se ha convertido en el estándar de instrumentación. En Swarm::Ops, cobra una importancia adicional: es la fuente de verdad que alimenta al agente-observer Y al dashboard del Operador de Xanpan::Agents. Cada agente del enjambre instrumenta sus operaciones con OpenTelemetry:

- **Traces:** Cada historia tiene un trace end-to-end: desde que entra al backlog hasta que está en producción. Cada agente que toca la historia es un span.
- **Metrics:** Tokens consumidos, latencia de inferencia, tasa de éxito de tool-calling, por agente y por modelo.
- **Logs:** Cada decisión del agente loggeada con contexto. No solo "qué hizo" sino "por qué lo hizo" (reasoning trace).

## 7.4 Langfuse como observabilidad de LLM

Para la capa específica de agentes IA, Langfuse (o equivalente) instrumenta lo que OpenTelemetry no cubre nativamente:

- Coste de tokens por trace (no solo latencia).
- Calidad de output por modelo (scores de eval).
- Patrones de alucinación por tipo de tarea.
- Drift de rendimiento entre versiones de modelo.

Esto alimenta directamente las métricas de "Coste" y "Modelo" del dashboard de Xanpan::Agents (§12).

---

# 8. Seguridad: DevSecOps Muere, Nace Security-by-Swarm

## 8.1 El problema con DevSecOps

DevSecOps (2016+) intentó "shift left" la seguridad: integrar escaneo de vulnerabilidades, SAST, DAST, y compliance checks en el pipeline de CI/CD. Buena idea. Mala ejecución frecuente:

- **Alert fatigue:** SAST genera cientos de hallazgos por PR, la mayoría falsos positivos. Los developers aprenden a ignorar.
- **Shift left = dump left:** Responsabilizar al developer de seguridad sin darle las herramientas ni el conocimiento.
- **Escaneo estático insuficiente:** Las vulnerabilidades más peligrosas en 2026 no son patrones estáticos conocidos (OWASP Top 10). Son errores de lógica de negocio, race conditions, y vulnerabilidades emergentes de interacción entre componentes.
- **Agent-to-agent prompt injection:** Una amenaza nueva que DevSecOps no contempla. Cuando los agentes pasan datos entre sí, un agente comprometido (por prompt injection vía input de usuario) puede inyectar instrucciones maliciosas en el output que otro agente consume como input. El pipeline de seguridad clásico no tiene visibilidad de esta superficie de ataque porque ocurre en las interfaces internas del enjambre, no en el código fuente.

## 8.2 Security-by-Swarm: seguridad como agente, no como paso

En Swarm::Ops, la seguridad no es un "paso" del pipeline. Es un **agente activo** con las siguientes responsabilidades:

### Agente-security en análisis

- **Clasificación de riesgo automática:** Cada PR es clasificado por superficie de ataque afectada (autenticación, autorización, datos sensibles, interfaces externas, criptografía).
- **Análisis contextual, no solo estático:** El agente-security no solo busca patrones conocidos; analiza el cambio en contexto de la arquitectura completa (alimentado por ARCHITECTURE.md) y evalúa si introduce nuevas superficies de ataque.
- **Priorización inteligente:** En vez de 200 hallazgos igualmente "medium," el agente prioriza por impacto real basado en la postura de seguridad actual del sistema.

### Agente-security en producción

- **Análisis de comportamiento en runtime:** Monitorea patrones de acceso, payloads anómalos, intentos de escalada de privilegios. No es un WAF estático; es un agente que entiende qué es "normal" para tu aplicación.
- **Correlación con intelligence feeds:** Cuando sale un nuevo CVE que afecta una dependencia del proyecto, el agente-security evalúa la exposición real (no solo "dependencia vulnerable" sino "dependencia vulnerable Y expuesta a input externo") y propone mitigación.

### El principio: capas de diversidad

La seguridad en Swarm::Ops sigue el principio de Xanpan::Agents §15.1: **diversidad de modelos.** El agente-security usa un modelo/provider diferente al agente-coder. Si el coder genera un patrón inseguro porque su modelo tiene un blind spot, el security-agent con modelo diferente tiene mayor probabilidad de detectarlo.

## 8.3 Quis custodiet: Seguridad del agente de seguridad

El agente-security tiene un problema de bootstrap: ¿cómo aseguras al guardia mismo? Si el modelo del security-agent tiene vulnerabilidades en su comprensión de seguridad, tienes un guardia ciego. Cuatro controles meta resuelven este problema (alineados con el patrón del Sentinel en Xanpan::Agents §9.4):

1. **Modelo diferente al enjambre.** Si los agentes productivos usan Claude como base, el security-agent usa GPT (o viceversa). Los blind spots de diferentes modelos no se solapan completamente; la diversidad reduce la superficie ciega.

2. **Meta-eval periódico.** Mensualmente, someter al security-agent a un conjunto de pruebas adversariales conocidas: prompt injection patterns, bypass de validación, escalada de privilegios, OWASP Top 10 adaptados a LLMs. Si falla alguna categoría, recalibrar prompts o cambiar modelo.

3. **Veto asimétrico.** El security-agent puede bloquear cualquier PR pero no puede aprobar en solitario — la aprobación requiere que las otras capas de verificación (CI, evals de regresión, review de diversidad) también pasen. Un falso positivo del security-agent causa delay; un falso negativo será atrapado por otra capa. La asimetría está a favor de la seguridad.

4. **Auditoría externa periódica.** Trimestralmente (o con la frecuencia que el presupuesto permita), un humano con experiencia en seguridad revisa los logs del security-agent: qué aprobó, qué rechazó, qué patterns debió detectar y no detectó. Esta revisión es un eval humano del agente, no un pentest del sistema — aunque el pentest también es recomendable.

---

# 9. El Operador como Platform Engineer del Enjambre

## 9.1 Convergencia de roles

En Xanpan::Agents, el Operador configura y optimiza el enjambre. En Swarm::Ops, esa función se expande: el Operador es también el **Platform Engineer** que construye y mantiene la plataforma que el enjambre consume.

**Nota sobre el PO:** El Product Owner (Xanpan::Agents §2.1) no aparece en Swarm::Ops porque este documento es operacional, no de negocio. Pero el PO no desaparece: es quien define los constraints de negocio (SLAs, presupuestos, prioridades de features) que el Operador traduce a configuración operacional. Cuando el Operador declara "presupuesto máximo de $X/día en tokens de CI/CD," ese $X viene del PO. La trazabilidad negocio → operación es: PO define constraint → Operador lo implementa en la plataforma → Enjambre lo respeta.

El Operador no escribe YAML de pipelines línea por línea. Declara intenciones y restricciones:

- "Cada PR debe pasar por lint, types, tests unitarios y eval de regresión antes de merge."
- "Los cambios en módulos de autenticación requieren eval de seguridad adicional y aprobación humana."
- "Deploy a producción en modo canary al 5% de tráfico. Expandir si métricas estables durante 15 minutos."
- "Presupuesto máximo de $X/día en tokens de inferencia para operaciones de CI/CD."

El enjambre traduce estas declaraciones en configuración ejecutable. El Operador revisa, ajusta y aprueba.

## 9.2 Golden Paths para agentes

Platform Engineering popularizó el concepto de "Golden Paths": caminos pre-configurados y optimizados para que los developers creen y desplieguen servicios sin friccón. En Swarm::Ops, los Golden Paths son para agentes:

- **Golden Path de historia estándar:** PR → lint → types → tests → eval regresión → merge → deploy canary → expand.
- **Golden Path de historia destructiva:** PR → lint → types → tests → eval regresión → eval seguridad → hold → aprobación Operador → deploy canary con rollback agresivo.
- **Golden Path de infraestructura:** Intent → IaC generation → plan → diff review → apply → verify → drift monitor.
- **Golden Path de hotfix:** Bug report → agente diagnóstica → genera fix + test → eval express → deploy directo (con rollback automático si métricas degradan).

## 9.3 Self-service para el enjambre

El IDP clásico ofrece self-service a developers humanos. En Swarm::Ops, el IDP ofrece self-service al enjambre:

- **Template de servicio:** Un agente puede crear un nuevo microservicio desde un template estandarizado con un comando. El template incluye estructura, CI/CD, monitoring, alerting.
- **Provisioning de entornos:** Un agente puede solicitar un entorno efímero para testing. Se crea en segundos, se destruye automáticamente post-uso.
- **Registro de artefactos:** Los agentes publican y consumen artefactos (imágenes Docker, paquetes npm/pip, modelos) desde registros centralizados.
- **Catálogo de servicios:** Los agentes consultan un catálogo de servicios internos (APIs, bases de datos, colas) con documentación actualizada automáticamente.

---

# 10. Modos de Fallo y Circuit Breakers Operacionales

## 10.1 Cascada de deploys defectuosos

**Modo de fallo:** Múltiples agentes generan cambios que individualmente pasan evals pero en combinación causan un fallo. El deploy continuo los pone en producción en sucesión rápida. Cada uno parece ok. La combinación explota.

**Circuit breakers:**
- **Deploy batching:** Los cambios se agrupan en ventanas de deploy. Después de cada batch, periodo de observación antes del siguiente.
- **Canary con correlación:** El agente-observer no solo mira métricas absolutas; correlaciona con el número y tipo de cambios recientes. Si detecta que la tasa de cambio se correlaciona con degradación, pausa deploys automáticamente.
- **Rollback atómico a batch:** Si un batch causa problemas, se rollbackea el batch completo, no cambios individuales.

## 10.2 Saturación del pipeline por ráfaga de agentes

**Modo de fallo:** 5 agentes generan 30 PRs/hora. El pipeline se satura. Los tiempos de feedback se extienden de minutos a horas. Los agentes siguen generando commits sobre código que no saben si pasó o no.

**Circuit breakers:**
- **Backpressure:** Cuando la cola de verificación excede un umbral, el orquestador reduce la tasa de generación de PRs del enjambre. Los agentes trabajan en tareas que no generan PRs (análisis, refactoring de context, planificación) hasta que la cola se drena.
- **Priorización por valor:** Los PRs se priorizan en la cola por valor de negocio de la historia asociada. Historias de alta prioridad pasan primero.
- **Merge queues inteligentes:** GitHub Merge Queue + priorización. Los PRs no compiten por CI time igualmente.

## 10.3 Drift de infraestructura no detectado

**Modo de fallo:** Alguien (humano o agente) hace un cambio manual en producción que no se refleja en IaC. El estado real diverge del declarado. El siguiente apply de IaC causa destrucción o conflicto.

**Circuit breakers:**
- **Drift detection continua:** El agente de infraestructura ejecuta `terraform plan` (o equivalente) periódicamente sin aplicar. Si detecta drift, alerta al Operador.
- **Prohibición de cambios manuales:** Nadie (humano ni agente) toca producción directamente. Todo pasa por IaC → plan → apply. Los permisos de consola están restringidos a read-only excepto para break-glass emergencias.
- **Reconciliación automática:** Para drift trivial (tags, configuraciones menores), el agente puede reconciliar automáticamente. Para drift significativo, pausa y consulta al Operador.

## 10.4 Fallo del agente-observer (quis custodiet?)

**Modo de fallo:** El agente-observer mismo falla o se degrada. No detecta anomalías. Un problema en producción crece sin ser notado.

**Circuit breakers:**
- **Alertas clásicas como backstop:** Las alertas tradicionales de Prometheus/Grafana siguen activas como capa independiente del agente-observer. Si la latencia cruza un umbral absoluto, la alerta dispara aunque el agente-observer no la detecte.
- **Heartbeat del observer:** El agente-observer emite un heartbeat periódico. Si el heartbeat se pierde, el sistema alerta al Operador: "el observador ha dejado de observar."
- **Separación de provider:** El agente-observer corre en infraestructura diferente a la aplicación que observa. Si la aplicación cae, el observer sigue arriba.

---

# 11. Stack de Referencia 2026

No prescriptivo; referencial. Cada organización elige sus herramientas. Lo que importa son las funciones, no los nombres.

| Función | Herramientas de referencia | Notas |
|---|---|---|
| **Repositorio + Code Review** | GitHub, GitLab | Merge queues para gestionar ráfagas de PRs de agentes |
| **CI (build + test)** | GitHub Actions, GitLab CI | Con soporte para agent runners como ciudadanos de primera clase |
| **Evals de LLM** | Langfuse, Braintrust, custom | El corazón de la verificación post-agente. Instrumentación OTEL. |
| **CD (deploy)** | ArgoCD, Flux (GitOps) | Deploys declarativos, reconciliación continua, rollback automático |
| **Feature Flags** | LaunchDarkly, Unleash, Flagsmith | Primitiva base para deploy continuo sin riesgo |
| **IaC** | Terraform, Pulumi, OpenTofu | El artefacto versionado. Generado por agente, aprobado por humano |
| **IaConversation** | Pulumi Neo, AWS Kiro | Capa conversacional sobre IaC |
| **Container Runtime** | Docker, Kubernetes | K8s para escala; Docker Compose para equipos pequeños |
| **Observabilidad** | Prometheus + Grafana + Loki (LGTM stack) | OpenTelemetry como instrumentación universal |
| **Observabilidad LLM** | Langfuse, Helicone | Tokens, costes, calidad por modelo/agente |
| **Seguridad** | Trivy, Semgrep, Snyk + agente-security | SAST/DAST como input; agente-security como análisis contextual |
| **Secrets** | HashiCorp Vault, SOPS, AWS Secrets Manager | Inyección en runtime, nunca en código ni en contexto de agente |
| **Service Catalog** | Backstage (Spotify) | Catálogo de servicios que agentes y humanos consultan |
| **Agent Runtime** | GitHub Agentic Workflows, AWS AgentCore | ⚠️ Emergiendo (preview/nuevo). Mientras tanto: containers Docker con permisos restrictivos cumplen la función |

---

# 12. Síntesis: Tabla de Correspondencia Prehistoria → Swarm::Ops

## 12.1 La gran tabla

| Concepto Prehistórico | Estado | Transformación Swarm::Ops |
|---|---|---|
| Jenkins pipeline | 💀 Colapsa | Sistema nervioso adaptativo con orquestador inteligente |
| YAML de CI/CD artesanal | 💀 Colapsa | Intención declarada por Operador → config generada por agente |
| Build server / runner | 🔄 Muta | Se bifurca en Execution Environment (determinista) + Agent Runtime (no-determinista) |
| "CI verde = listo" | 💀 Colapsa | CI verde es condición necesaria pero insuficiente. 5 capas de verificación |
| Staging environment | 💀 Colapsa | Feature flags + canary deploys + eval post-deploy + rollback automático |
| Deploy manual/aprobado | 🔄 Muta | Automático para riesgo bajo. Humano solo para cambios destructivos/alto riesgo |
| Terraform/Pulumi (escrito a mano) | 🔄 Muta | IaC sigue como artefacto. Generado por agente via IaConversation. Humano revisa diff |
| Dashboard de Grafana | 🔄 Muta | Sigue existiendo como visualización. Pero un agente-observer lo interpreta activamente |
| On-call humano 24/7 | 🔄 Muta | Agente-observer como primera línea. Humano como escalación para incidentes complejos |
| Runbooks manuales | 💀 Colapsa | Runbooks ejecutados por agentes. Escritos para ser machine-readable |
| DevSecOps (scan estático) | 🔄 Muta | Agente-security con análisis contextual + diversidad de modelos. SAST como input, no como solución |
| "Shift left" | 💀 Colapsa | No "shift" en ninguna dirección. La seguridad/calidad es un agente omnipresente, no una responsabilidad que se "mueve" |
| Helm charts manuales | 💀 Colapsa | GitOps declarativo (ArgoCD/Flux) con manifests generados por agente |
| Docker build | ✅ Sobrevive | Inmutabilidad de artefactos es invariante. Dockerfile generado por agente |
| Feature flags | ✅ Sobrevive (amplificado) | De "nice to have" a primitiva base obligatoria para deploy continuo |
| OpenTelemetry | ✅ Sobrevive (amplificado) | Lingua franca de instrumentación. Ahora también instrumenta operaciones de agentes IA |
| GitOps | ✅ Sobrevive (amplificado) | Git como fuente de verdad para código, infra, config y estado del enjambre |
| Principio de mínimo privilegio | ✅ Invariante | Cada agente y cada componente: exactamente los permisos necesarios |
| Idempotencia | ✅ Invariante | Operaciones de infra deben poder re-ejecutarse sin efectos laterales |
| Blast radius control | ✅ Invariante | Canary, traffic splitting, feature flags. El mecanismo cambia; el principio no |

## 12.2 Los 9 Axiomas de Swarm::Ops

1. **Las siete funciones son invariantes. Las implementaciones son efímeras.**
2. **El pipeline lineal está muerto. El sistema nervioso adaptativo lo reemplaza.**
3. **La configuración es intención declarada, no YAML artesanal.**
4. **CI verde es condición necesaria pero radicalmente insuficiente.**
5. **Los agentes son ciudadanos de primera clase del pipeline, no scripts glorificados.**
6. **La seguridad es un agente omnipresente, no un paso que se "shift left".**
7. **La observabilidad es inteligencia activa, no dashboards pasivos.**
8. **Cada acción de cada agente es auditable. No hay cajas negras.**
9. **El Operador declara el qué. El enjambre resuelve el cómo. El humano tiene veto absoluto.**

---

*Swarm::Ops v1.0. Companion document de Xanpan::Agents v2.1. Febrero 2026.*

*Los que construyeron Jenkins, Travis, CircleCI, GitHub Actions, Terraform, Kubernetes, Prometheus, Grafana y ArgoCD no estaban equivocados. Estaban resolviendo los problemas de su era con las herramientas de su era. Honramos su trabajo heredando sus invariantes y reconstruyendo sus implementaciones para un mundo que se mueve a velocidad de máquina. La arqueología no es desprecio. Es el respeto profundo de quien entiende que cada ruina fue alguna vez un templo funcional.*
