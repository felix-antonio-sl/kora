---
_manifest:
  urn: "urn:fxsl:kb:swarm-ops-metodologia"
  provenance:
    created_by: "FS"
    created_at: "2026-02-24"
    source: "source/fxsl/xanpan/swarm-ops-v1-metodologia.md"
version: "1.0.0"
status: published
tags: [xanpan, swarm-ops, cicd, devops, pipeline, agentes, observabilidad, seguridad, infraestructura]
lang: es
---

# Swarm::Ops --- Framework Operacional para Enjambres de Agentes v1.0.0

## 1. Definicion

**Swarm::Ops** es el framework operacional que reemplaza CI/CD y DevOps en el contexto de [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia). No es un producto ni una herramienta. Es un conjunto de principios, funciones y patrones para operar software cuando el enjambre de agentes IA es el ejecutor primario.

Swarm::Ops absorbe Platform Engineering y lo lleva al siguiente nivel: no solo los developers son clientes de la plataforma; los agentes IA son el cliente primario.

### 1.1 Alcance

Este documento **DEBE** usarse como referencia operacional para equipos que operan con enjambres de agentes IA. Prescribe como reconstruir las funciones clasicas de CI/CD y DevOps para un mundo donde los agentes generan codigo, tests e infraestructura a velocidad de maquina.

### 1.2 Relacion con el corpus

Swarm::Ops es companion document de [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia). Se activa en Fase 3-4 del bootstrap path descrito en [Chapter 0](urn:fxsl:kb:chapter0-operador-solitario). Para decisiones de stack tecnologico, ver [STACK::LLM](urn:fxsl:kb:stack-llm-arquitectura).

### 1.3 La discontinuidad operacional

Las cinco asunciones del CI/CD clasico colapsan simultaneamente cuando agentes IA son los ejecutores primarios:

| # | Asuncion clasica | Estado 2026 |
|---|---|---|
| 1 | Los commits son espaciados y discretos | Agentes generan PRs en rafagas de 10-30 PRs/hora |
| 2 | Los tests son independientes del codigo | El mismo modelo genera codigo Y tests; la independencia evaluador/evaluado se pierde |
| 3 | Los YAML de pipeline son escritos por humanos | La configuracion de pipelines se genera y mantiene por agentes |
| 4 | El deploy es un evento que requiere decision humana | El ritmo natural de deploy es continuo; el deploy humano se reserva para cambios destructivos |
| 5 | La infraestructura se define en archivos estaticos | La infraestructura se define conversacionalmente; IaC persiste como artefacto intermedio |

### 1.4 Lo que NO cambia

Cinco invariantes sobreviven intactos con o sin agentes:

- **Idempotencia:** Las operaciones de infraestructura **DEBEN** poder re-ejecutarse sin efectos secundarios indeseados.
- **Inmutabilidad de artefactos:** Una imagen de contenedor construida es inmutable. **NO DEBE** parchearse en produccion.
- **Trazabilidad:** Cada cambio en produccion **DEBE** ser rastreable hasta un commit, un PR, una decision. Con agentes, tambien **DEBE** ser rastreable hasta la historia de usuario y el OKR que la origino.
- **Principio de minimo privilegio:** Cada componente del sistema (humano o agente) **DEBE** tener exactamente los permisos que necesita y ninguno mas.
- **Blast radius control:** Un fallo **DEBE** contenerse. Canary deploys, feature flags, traffic splitting: los mecanismos cambian pero el principio es invariante.

---

## 2. Definiciones

| Termino | Definicion |
|---|---|
| **Swarm::Ops** | Framework operacional que reconstruye las funciones de CI/CD y DevOps para enjambres de agentes IA |
| **Pipeline lineal** | Secuencia clasica commit -> build -> test -> staging -> deploy. Modelo industrial que Swarm::Ops reemplaza |
| **Sistema nervioso** | Grafo adaptativo de operaciones donde multiples flujos coexisten, se bifurcan y convergen en tiempo real |
| **Agente-integrador** | Agente que verifica coherencia semantica (no solo sintactica) y resuelve conflictos triviales autonomamente |
| **Agente-verificador** | Agente que selecciona tests segun tipo de cambio y ejecuta evals independientes con modelo diferente al autor |
| **Agente-deployer** | Agente con estrategia adaptativa de deploy: canary para riesgo, fast-track para cambios triviales |
| **Agente-observer** | Agente que analiza metricas en tiempo real, correlaciona con deploys recientes, y propone diagnostico y accion |
| **Agente-security** | Agente activo que clasifica riesgo, analiza contexto arquitectonico y prioriza hallazgos por impacto real |
| **Agente-orquestador** | Agente que decide que acciones ejecutar basado en reglas declaradas por el Operador y clasificacion del evento |
| **IaConversation** | Infrastructure as Conversation: patron donde el Operador describe intencion en lenguaje natural, el agente genera IaC, y el humano verifica el diff |
| **Operador** | Rol humano que configura, optimiza y gobierna el enjambre. En Swarm::Ops, tambien es Platform Engineer |
| **Product Owner (PO)** | Rol humano que define constraints de negocio (SLAs, presupuestos, prioridades) que el Operador traduce a configuracion operacional |
| **Golden Path** | Camino pre-configurado y optimizado para que agentes ejecuten flujos operacionales sin friccion |
| **IDP** | Internal Developer Platform: plataforma interna que abstrae complejidad operacional y ofrece self-service |
| **Eval** | Evaluacion automatizada que verifica calidad, seguridad, regresion o coste del output de un agente |
| **LLM-as-a-Judge** | Patron donde un modelo de otro provider evalua la calidad del output de un agente |
| **Circuit breaker** | Mecanismo que detiene automaticamente un flujo operacional cuando detecta condiciones de fallo |
| **Backpressure** | Mecanismo que reduce la tasa de generacion de PRs cuando la cola de verificacion se satura |
| **Drift** | Divergencia entre el estado declarado de infraestructura (IaC) y el estado real en produccion |
| **Feature flag** | Primitiva que permite activar/desactivar funcionalidad en produccion sin deploy |
| **Canary deploy** | Estrategia de deploy a un porcentaje pequeno de trafico para verificar estabilidad antes de expandir |
| **OpenTelemetry** | Estandar de instrumentacion (traces, metrics, logs) que funciona como lingua franca de observabilidad |
| **Langfuse** | Herramienta de observabilidad especifica para LLMs: tokens, costes, calidad por modelo/agente |
| **Sentinel** | Agente de [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia) que audita el enjambre. El agente-security sigue su patron |
| **Veto asimetrico** | Principio donde un agente de seguridad puede bloquear pero no aprobar en solitario |
| **Korvo-Korax** | Sistema personal que implementa los patrones del corpus a escala minima como proof of concept |

---

## 3. Las Siete Funciones Invariantes

Todo el aparato de CI/CD y DevOps cumple exactamente siete funciones. Estas funciones son invariantes: **NO DEBEN** eliminarse. Lo que cambia es quien las ejecuta, como se coordinan, y a que velocidad operan.

| # | Funcion | Implementacion clasica | Implementacion Swarm::Ops |
|---|---|---|---|
| **F1** | Integracion | CI server ejecuta merge + build | Agente-integrador verifica coherencia semantica, no solo sintactica. Merge inteligente que resuelve conflictos triviales autonomamente |
| **F2** | Verificacion | Test runners ejecutan suites estaticas | Agente-verificador selecciona tests segun tipo de cambio + eval independiente con modelo diferente al autor. Cobertura adaptativa |
| **F3** | Empaquetado | Build determinista -> imagen inmutable | Preservado. Docker build sigue siendo la respuesta. El Dockerfile lo genera/mantiene un agente |
| **F4** | Entrega | Pipeline de deploy con stages fijos | Agente-deployer con estrategia adaptativa: canary para riesgo, fast-track para triviales. Feature flags como primitiva base |
| **F5** | Provisioning | IaC estatica (Terraform/Pulumi) | IaConversation: el Operador describe intencion, el agente genera IaC, aplica, verifica. El artefacto IaC se versiona como antes |
| **F6** | Observabilidad | Dashboards pasivos + alertas | Agente-observer analiza metricas en tiempo real, detecta anomalias, correlaciona con deploys recientes, propone diagnostico y accion |
| **F7** | Recuperacion | Rollback manual + runbooks | Rollback automatico cuando evals post-deploy fallan. Runbooks ejecutados por agentes. Humano interviene solo en recuperaciones complejas |

**Correcto:** `Reemplazar la implementacion de F2 (de test runner estatico a agente-verificador) manteniendo la funcion intacta`
**Incorrecto:** `Eliminar F6 (observabilidad) porque "el agente-observer se encarga de todo"`

---

## 4. Del Pipeline al Sistema Nervioso

### 4.1 Los tres cambios de paradigma

Todo equipo que adopte Swarm::Ops **DEBE** internalizar tres cambios de paradigma:

**Cambio 1: De pipeline a sistema nervioso.** El pipeline era una secuencia lineal: commit -> build -> test -> staging -> deploy. En Swarm::Ops, las operaciones son un grafo adaptativo donde multiples flujos coexisten, se bifurcan y convergen. El sistema nervioso **DEBE** responder en tiempo real a eventos: nuevos commits, nuevos evals, alertas de produccion, propuestas del Sentinel, cambios de configuracion.

**Cambio 2: De configuracion estatica a intencion declarada.** En CI/CD clasico, la configuracion es imperativa: "ejecuta estos pasos en este orden." En Swarm::Ops, la configuracion **DEBE** ser declarativa de intencion: "quiero que cada historia pase por verificacion de tipos, tests unitarios, eval de seguridad y eval de regresion antes de ser candidata a deploy." El enjambre determina el como. El humano declara el que.

**Cambio 3: De herramienta pasiva a agente activo.** Las herramientas de CI/CD clasico son pasivas: se configuran, se ejecutan cuando se les invoca, reportan resultados. En Swarm::Ops, los componentes operacionales **DEBEN** ser agentes activos que toman decisiones: el agente de eval decide que tests ejecutar; el agente de deploy decide si hacer canary o full; el agente-observer detecta anomalias y propone rollback.

### 4.2 Anatomia del sistema nervioso

| Componente | Funcion |
|---|---|
| **Receptores** (eventos de entrada) | Commit, PR, alerta de produccion, cambio de configuracion, propuesta del Sentinel, heartbeat del enjambre, resultado de eval |
| **Nervios aferentes** (analisis) | Clasificacion automatica del evento: tipo de cambio, riesgo, zona del codebase afectada, necesidad de intervencion humana |
| **Centro de procesamiento** (orquestador) | El agente-orquestador decide que acciones ejecutar basado en reglas declaradas por el Operador y clasificacion del evento |
| **Nervios eferentes** (ejecucion) | Agentes especializados ejecutan: build, test, eval, deploy, rollback, notificacion |
| **Feedback loop** | El resultado de cada accion alimenta al sistema. Un test fallido re-clasifica el PR. Un eval exitoso avanza el deploy. Una anomalia post-deploy dispara rollback |

### 4.3 Flujos concurrentes

En Swarm::Ops, el equipo **DEBE** pensar en flujos concurrentes que se coordinan, no en pasos secuenciales.

#### Flujo de verificacion (continuo)

Cada PR del enjambre **DEBE** entrar en verificacion inmediata. Los evals se ejecutan en paralelo con priorizacion por riesgo del cambio:

| Tipo de cambio | Verificacion requerida | Tiempo esperado |
|---|---|---|
| `lectura` | Lint + type check + tests unitarios | Minutos |
| `escritura` | Lo anterior + eval de regresion + tests de integracion | Minutos |
| `destructivo` | Lo anterior + eval de seguridad + hold para aprobacion humana | Horas |

#### Flujo de deploy (continuo)

Los cambios verificados se acumulan en un buffer de deploy. El agente-deployer **DEBE** tener una estrategia configurable:

- **Modo rafaga:** Deploy cada N minutos si hay cambios verificados. Para ambientes de desarrollo.
- **Modo canary:** Deploy a porcentaje pequeno de trafico, monitorea, expande. Para produccion.
- **Modo manual:** Hold para aprobacion humana. Para cambios destructivos o de alto riesgo.

#### Flujo de observacion (permanente)

El agente-observer **DEBE** monitorear produccion independientemente de los otros flujos. Detecta anomalias en latencia, errores, consumo de recursos. Si correlaciona una anomalia con un deploy reciente, **DEBE** proponer rollback automaticamente.

### 4.4 El fin del "CI verde = listo"

En Swarm::Ops, CI verde es condicion necesaria pero radicalmente insuficiente cuando los agentes generan tanto el codigo como los tests. La senal de confianza **DEBE** ser multi-capa:

| Capa | Verificacion | Rol |
|---|---|---|
| 1 | CI verde (lint, types, tests) | Condicion minima |
| 2 | Eval de regresion (con dataset parcialmente humano) | Verificacion de que no rompe lo existente |
| 3 | Eval de diversidad (reviewer-agent con modelo diferente al coder-agent) | Verificacion de que otro "cerebro" llega a la misma conclusion |
| 4 | Eval de seguridad (analisis estatico + dinamico + check de privilegios) | Verificacion de postura de seguridad |
| 5 | Aprobacion humana (para cambios de riesgo) | Ultimo firewall |

Solo cuando las 5 capas pasan, el cambio es candidato a deploy. Esto protege contra el modo de fallo de alucinacion sistemica ([Xanpan::Agents &sect;15.1](urn:fxsl:kb:xanpan-agents-metodologia)).

**Correcto:** `Deploy solo despues de CI verde + eval de regresion + eval de diversidad + eval de seguridad`
**Incorrecto:** `Deploy automatico inmediatamente despues de CI verde`

---

## 5. Infraestructura como Conversacion

### 5.1 De IaC a IaConversation

Infrastructure as Code (HashiCorp, 2014) fue revolucionario: la infraestructura se define en archivos versionados y aplicados con herramientas deterministas. Ese principio es eterno. Lo que cambia es quien escribe los archivos.

**IaC clasico:**
```
Humano escribe Terraform -> terraform plan -> humano revisa plan -> terraform apply
```

**IaConversation (Swarm::Ops):**
```
Operador describe intencion en lenguaje natural ->
Agente genera Terraform/Pulumi ->
Agente ejecuta plan ->
Operador revisa diff y aprueba ->
Agente aplica ->
Agente verifica estado post-aplicacion
```

El artefacto IaC **DEBE** seguir existiendo. Se versiona en git. Es auditable. Es reproducible. Lo que desaparece es la escritura manual de HCL/YAML/CDK por humanos.

### 5.2 Las cinco fases del patron

El patron IaConversation **DEBE** contener exactamente cinco fases, independientemente del provider:

| Fase | Accion | Responsable |
|---|---|---|
| 1. Intent declaration | El Operador declara intencion en lenguaje natural | Operador |
| 2. Plan generation | El agente genera el plan IaC completo | Agente |
| 3. Diff review | El Operador revisa el diff contra el estado actual | Operador |
| 4. Apply with verification | El agente aplica y verifica que el estado real coincide con el declarado | Agente |
| 5. Drift detection | El agente monitorea continuamente que la infraestructura real no derive del estado declarado | Agente |

### 5.3 Modo degradado

IaConversation asume infraestructura compleja. Para un equipo con 1 VPS y Docker Compose, todo este aparato es innecesario. El modo degradado **DEBE** usarse cuando la infraestructura cabe en un `docker-compose.yml`:

- El `docker-compose.yml` es el IaC.
- La IaConversation es el chat con el LLM: "Necesito agregar Redis para caching."
- El agente actualiza el docker-compose.
- El Operador revisa el diff.
- `docker compose up -d`.

Las cinco fases del patron (intent, plan, diff, apply, verify) se cumplen sin Terraform, sin Pulumi, sin plataforma conversacional. IaConversation escala hacia arriba, no hacia abajo: **DEBE** empezar con docker-compose y crecer hacia Terraform/Pulumi cuando la complejidad de infraestructura lo exija, no antes.

### 5.4 Context engineering para infraestructura

El agente de infraestructura **DEBE** alimentarse de archivos de contexto para que sus propuestas sean coherentes con la realidad y las restricciones del sistema:

| Archivo | Contenido |
|---|---|
| **INFRA.md** | Arquitectura de infraestructura actual: providers, regiones, servicios principales, patrones de networking |
| **CONSTRAINTS.md** | Restricciones operacionales: presupuesto cloud, compliance (data residency, encryption), SLAs comprometidos |
| **RUNBOOKS.md** | Procedimientos de recuperacion para incidentes conocidos. Escritos para ser ejecutados por agentes |

---

## 6. El Agente como Ciudadano de Primera Clase

### 6.1 Por que los pipelines clasicos son insuficientes para agentes

Los pipelines de CI/CD ejecutan scripts: comandos deterministas que producen el mismo output dado el mismo input. Los agentes IA **NO** son scripts:

- **Son no-deterministas:** El mismo prompt **PUEDE** producir outputs diferentes.
- **Necesitan contexto amplio:** No solo el diff del PR; necesitan arquitectura, convenciones, dependencias.
- **Consumen recursos impredeciblemente:** Un agente **PUEDE** necesitar 1K tokens o 100K tokens.
- **Pueden fallar de formas no-discretas:** Un script falla con exit code 1. Un agente **PUEDE** generar output incorrecto que parece correcto.

### 6.2 Cuatro primitivas obligatorias

Todo sistema Swarm::Ops **DEBE** implementar cuatro primitivas para que agentes sean ciudadanos de primera clase:

#### Primitiva 1: Workflow Definition (que y como)

Que dispara al agente, que permisos tiene, que artefactos puede leer/escribir, que outputs produce. **DEBE** funcionar como contrato entre el pipeline y el agente.

#### Primitiva 2: Execution Sandbox (aislamiento)

El agente **DEBE** ejecutar en un entorno aislado con filesystem limitado, acceso a red controlado, secrets inyectados selectivamente, y logging determinista de cada accion. Cada accion del agente **DEBE** ser auditable. No hay "caja negra."

#### Primitiva 3: Safe Operation Primitives (seguridad por defecto)

Por defecto: read-only sobre el repo, acciones limitadas y auditables, outputs estructurados que herramientas downstream pueden validar. Escalar privilegios **DEBE** requerir declaracion explicita y aprobacion.

#### Primitiva 4: State Management (memoria entre ejecuciones)

Los agentes **PUEDEN** necesitar estado entre ejecuciones. El estado del agente **DEBE** versionarse como el codigo.

**Correcto:** `Agente ejecuta en container Docker con permisos restrictivos (filesystem read-only, red limitada, secrets inyectados selectivamente, logging de cada accion)`
**Incorrecto:** `Agente ejecuta en el host con acceso completo a red y filesystem`

#### Caveat de madurez

GitHub Agentic Workflows (preview 2025, GA esperado 2026) y AWS AgentCore son emergentes. Mientras tanto, ejecutar agentes en containers Docker con permisos restrictivos **DEBE** usarse como implementacion base que cumple las cuatro primitivas.

### 6.3 La bifurcacion del runner

En Swarm::Ops, el concepto clasico de "runner" se bifurca en dos entidades que **DEBEN** gestionarse como entidades distintas con lifecycle, permisos y monitoreo diferentes:

| Entidad | Naturaleza | Funcion |
|---|---|---|
| **Execution Environment** | Determinista | Maquina/container donde corre el codigo generado (build, test) |
| **Agent Runtime** | No-determinista | Entorno donde el agente IA razona y produce outputs. Necesita acceso a modelo de lenguaje, contexto del proyecto y estado previo |

---

## 7. Observabilidad: Inteligencia Activa

### 7.1 Las tres eras

| Era | Periodo | Capacidad | Herramientas |
|---|---|---|---|
| Era 1: Monitoreo | 2000s | "Esta arriba?" CPU, RAM, disco | Nagios, Zabbix |
| Era 2: Observabilidad | 2010s | Logs, metricas, traces. Dashboards que un humano interpreta | Prometheus, Grafana, Jaeger, ELK |
| Era 3: Inteligencia Activa | 2026+ | Agente-observer analiza los tres pilares en tiempo real, correlaciona, detecta anomalias pre-alerta, propone acciones | Prometheus + Grafana + agente-observer |

Swarm::Ops opera en Era 3. El agente-observer **NO** reemplaza Prometheus+Grafana. Los usa como fuente de datos. Lo que reemplaza es al humano que mira dashboards.

### 7.2 El agente-observer

| Funcion | Humano (clasico) | Agente-observer (Swarm::Ops) |
|---|---|---|
| Detectar anomalia | Nota patron raro en dashboard o recibe alerta | Analiza metricas continuamente; detecta anomalias estadisticas pre-alerta |
| Correlacionar causa | "Hubo un deploy reciente?" | Cruza automaticamente con timeline de deploys, cambios de config, cambios de trafico |
| Diagnosticar | Revisa logs, traces, busca root cause | Analiza logs/traces filtrando por ventana temporal de anomalia; propone top-3 hipotesis |
| Proponer accion | "Creo que deberiamos rollback" | "Anomalia correlacionada con deploy X. Confianza 87%. Recomendacion: rollback. Aprobar?" |
| Ejecutar | Ejecuta rollback manual o via script | Si aprobado (o en modo auto para anomalias severas), ejecuta rollback y verifica |

### 7.3 Ruta de implementacion progresiva

El agente-observer **NO DEBE** implementarse directamente en su forma madura. La ruta **DEBE** seguir cuatro etapas:

1. **Etapa 1: Alertas clasicas.** Prometheus + reglas de alerta estaticas. Si latencia > umbral, alerta a Slack/Telegram. Sin IA.
2. **Etapa 2: Correlacion manual asistida.** Ante una alerta, el Operador consulta un LLM con metricas + timeline de deploys. El LLM ayuda a diagnosticar.
3. **Etapa 3: Correlacion semi-automatica.** Un script que ante cada alerta recopila contexto (metricas, deploys, logs) y los envia a un LLM para diagnostico propuesto. El Operador revisa.
4. **Etapa 4: Agente-observer completo.** Monitoreo continuo, deteccion pre-alerta, correlacion automatica, propuesta de acciones.

Cada etapa es funcional por si misma. La mayoria de los equipos operaran en etapas 2-3 durante meses antes de necesitar la etapa 4.

### 7.4 OpenTelemetry como lingua franca

Cada agente del enjambre **DEBE** instrumentar sus operaciones con OpenTelemetry:

- **Traces:** Cada historia **DEBE** tener un trace end-to-end: desde que entra al backlog hasta que esta en produccion. Cada agente que toca la historia es un span.
- **Metrics:** Tokens consumidos, latencia de inferencia, tasa de exito de tool-calling, por agente y por modelo.
- **Logs:** Cada decision del agente **DEBE** registrarse con contexto. No solo "que hizo" sino "por que lo hizo" (reasoning trace).

### 7.5 Langfuse como observabilidad de LLM

Para la capa especifica de agentes IA, Langfuse (o equivalente) **DEBE** instrumentar lo que OpenTelemetry no cubre nativamente:

- Coste de tokens por trace.
- Calidad de output por modelo (scores de eval).
- Patrones de alucinacion por tipo de tarea.
- Drift de rendimiento entre versiones de modelo.

---

## 8. Seguridad: Security-by-Swarm

### 8.1 Por que DevSecOps es insuficiente

DevSecOps (2016+) intento "shift left" la seguridad. Cuatro problemas lo invalidan en el contexto de enjambres:

- **Alert fatigue:** SAST genera cientos de hallazgos por PR, la mayoria falsos positivos. Los developers aprenden a ignorar.
- **Shift left = dump left:** Responsabilizar al developer de seguridad sin herramientas ni conocimiento.
- **Escaneo estatico insuficiente:** Las vulnerabilidades mas peligrosas en 2026 no son patrones estaticos conocidos (OWASP Top 10). Son errores de logica de negocio, race conditions, y vulnerabilidades emergentes de interaccion entre componentes.
- **Agent-to-agent prompt injection:** Amenaza que DevSecOps no contempla. Cuando los agentes pasan datos entre si, un agente comprometido **PUEDE** inyectar instrucciones maliciosas en el output que otro agente consume como input.

### 8.2 El agente-security

En Swarm::Ops, la seguridad **NO DEBE** ser un "paso" del pipeline. **DEBE** ser un agente activo.

#### Agente-security en analisis

- **Clasificacion de riesgo automatica:** Cada PR **DEBE** clasificarse por superficie de ataque afectada (autenticacion, autorizacion, datos sensibles, interfaces externas, criptografia).
- **Analisis contextual:** El agente-security **NO DEBE** limitarse a buscar patrones conocidos. **DEBE** analizar el cambio en contexto de la arquitectura completa (alimentado por ARCHITECTURE.md) y evaluar si introduce nuevas superficies de ataque.
- **Priorizacion inteligente:** En vez de 200 hallazgos igualmente "medium," el agente **DEBE** priorizar por impacto real basado en la postura de seguridad actual del sistema.

**Correcto:** `Agente-security analiza PR en contexto de ARCHITECTURE.md y reporta: "Este cambio expone un endpoint sin autenticacion que accede a datos sensibles."`
**Incorrecto:** `SAST reporta 200 hallazgos medium sin contexto arquitectonico ni priorizacion por impacto`

#### Agente-security en produccion

- **Analisis de comportamiento en runtime:** **DEBE** monitorear patrones de acceso, payloads anomalos, intentos de escalada de privilegios. No es un WAF estatico; es un agente que entiende que es "normal" para la aplicacion.
- **Correlacion con intelligence feeds:** Cuando sale un nuevo CVE que afecta una dependencia del proyecto, el agente-security **DEBE** evaluar la exposicion real (no solo "dependencia vulnerable" sino "dependencia vulnerable Y expuesta a input externo") y proponer mitigacion.

#### Principio de diversidad de modelos

La seguridad en Swarm::Ops sigue el principio de [Xanpan::Agents &sect;15.1](urn:fxsl:kb:xanpan-agents-metodologia): diversidad de modelos. El agente-security **DEBE** usar un modelo/provider diferente al agente-coder. Si el coder genera un patron inseguro porque su modelo tiene un blind spot, el security-agent con modelo diferente tiene mayor probabilidad de detectarlo.

### 8.3 Quis custodiet: seguridad del agente de seguridad

El agente-security tiene un problema de bootstrap. Cuatro controles meta **DEBEN** implementarse, alineados con el patron del Sentinel en [Xanpan::Agents &sect;9.4](urn:fxsl:kb:xanpan-agents-metodologia):

1. **Modelo diferente al enjambre.** Si los agentes productivos usan Claude como base, el security-agent **DEBE** usar GPT (o viceversa). Los blind spots de diferentes modelos no se solapan completamente; la diversidad reduce la superficie ciega.

2. **Meta-eval periodico.** Mensualmente, el security-agent **DEBE** someterse a un conjunto de pruebas adversariales conocidas: prompt injection patterns, bypass de validacion, escalada de privilegios, OWASP Top 10 adaptados a LLMs. Si falla alguna categoria, recalibrar prompts o cambiar modelo.

3. **Veto asimetrico.** El security-agent **PUEDE** bloquear cualquier PR pero **NO DEBE** aprobar en solitario --- la aprobacion requiere que las otras capas de verificacion (CI, evals de regresion, review de diversidad) tambien pasen. Un falso positivo causa delay; un falso negativo sera atrapado por otra capa. La asimetria esta a favor de la seguridad.

4. **Auditoria externa periodica.** Trimestralmente (o con la frecuencia que el presupuesto permita), un humano con experiencia en seguridad **DEBE** revisar los logs del security-agent: que aprobo, que rechazo, que patterns debio detectar y no detecto.

---

## 9. El Operador como Platform Engineer

### 9.1 Convergencia de roles

En [Xanpan::Agents](urn:fxsl:kb:xanpan-agents-metodologia), el Operador configura y optimiza el enjambre. En Swarm::Ops, esa funcion se expande: el Operador es tambien el Platform Engineer que construye y mantiene la plataforma que el enjambre consume.

El Operador **NO DEBE** escribir YAML de pipelines linea por linea. **DEBE** declarar intenciones y restricciones:

- "Cada PR debe pasar por lint, types, tests unitarios y eval de regresion antes de merge."
- "Los cambios en modulos de autenticacion requieren eval de seguridad adicional y aprobacion humana."
- "Deploy a produccion en modo canary al 5% de trafico. Expandir si metricas estables durante 15 minutos."
- "Presupuesto maximo de $X/dia en tokens de inferencia para operaciones de CI/CD."

El enjambre traduce estas declaraciones en configuracion ejecutable. El Operador revisa, ajusta y aprueba.

La trazabilidad negocio -> operacion es: PO define constraint -> Operador lo implementa en la plataforma -> Enjambre lo respeta.

### 9.2 Golden Paths para agentes

Platform Engineering popularizo el concepto de "Golden Paths." En Swarm::Ops, los Golden Paths **DEBEN** estar definidos para agentes:

| Golden Path | Flujo |
|---|---|
| **Historia estandar** | PR -> lint -> types -> tests -> eval regresion -> merge -> deploy canary -> expand |
| **Historia destructiva** | PR -> lint -> types -> tests -> eval regresion -> eval seguridad -> hold -> aprobacion Operador -> deploy canary con rollback agresivo |
| **Infraestructura** | Intent -> IaC generation -> plan -> diff review -> apply -> verify -> drift monitor |
| **Hotfix** | Bug report -> agente diagnostica -> genera fix + test -> eval express -> deploy directo (con rollback automatico si metricas degradan) |

### 9.3 Self-service para el enjambre

El IDP **DEBE** ofrecer self-service al enjambre:

- **Template de servicio:** Un agente **PUEDE** crear un nuevo microservicio desde un template estandarizado. El template **DEBE** incluir estructura, CI/CD, monitoring, alerting.
- **Provisioning de entornos:** Un agente **PUEDE** solicitar un entorno efimero para testing. **DEBE** crearse en segundos y destruirse automaticamente post-uso.
- **Registro de artefactos:** Los agentes **DEBEN** publicar y consumir artefactos (imagenes Docker, paquetes npm/pip, modelos) desde registros centralizados.
- **Catalogo de servicios:** Los agentes **DEBEN** consultar un catalogo de servicios internos (APIs, bases de datos, colas) con documentacion actualizada automaticamente.

---

## 10. Modos de Fallo y Circuit Breakers

### 10.1 Cascada de deploys defectuosos

**Modo de fallo:** Multiples agentes generan cambios que individualmente pasan evals pero en combinacion causan un fallo. El deploy continuo los pone en produccion en sucesion rapida.

**Circuit breakers:**

- **Deploy batching:** Los cambios **DEBEN** agruparse en ventanas de deploy. Despues de cada batch, **DEBE** haber periodo de observacion antes del siguiente.
- **Canary con correlacion:** El agente-observer **NO DEBE** solo mirar metricas absolutas; **DEBE** correlacionar con el numero y tipo de cambios recientes. Si detecta que la tasa de cambio se correlaciona con degradacion, **DEBE** pausar deploys automaticamente.
- **Rollback atomico a batch:** Si un batch causa problemas, **DEBE** rollbackearse el batch completo, no cambios individuales.

### 10.2 Saturacion del pipeline por rafaga de agentes

**Modo de fallo:** 5 agentes generan 30 PRs/hora. El pipeline se satura. Los tiempos de feedback se extienden de minutos a horas.

**Circuit breakers:**

- **Backpressure:** Cuando la cola de verificacion excede un umbral, el orquestador **DEBE** reducir la tasa de generacion de PRs del enjambre. Los agentes trabajan en tareas que no generan PRs (analisis, refactoring de context, planificacion) hasta que la cola se drena.
- **Priorizacion por valor:** Los PRs **DEBEN** priorizarse por valor de negocio de la historia asociada. Historias de alta prioridad pasan primero.
- **Merge queues inteligentes:** GitHub Merge Queue + priorizacion. Los PRs **NO DEBEN** competir por CI time igualmente.

### 10.3 Drift de infraestructura no detectado

**Modo de fallo:** Alguien (humano o agente) hace un cambio manual en produccion que no se refleja en IaC. El estado real diverge del declarado.

**Circuit breakers:**

- **Drift detection continua:** El agente de infraestructura **DEBE** ejecutar `terraform plan` (o equivalente) periodicamente sin aplicar. Si detecta drift, **DEBE** alertar al Operador.
- **Prohibicion de cambios manuales:** Nadie (humano ni agente) **DEBE** tocar produccion directamente. Todo **DEBE** pasar por IaC -> plan -> apply. Los permisos de consola **DEBEN** restringirse a read-only excepto para break-glass emergencias.
- **Reconciliacion automatica:** Para drift trivial (tags, configuraciones menores), el agente **PUEDE** reconciliar automaticamente. Para drift significativo, **DEBE** pausar y consultar al Operador.

### 10.4 Fallo del agente-observer

**Modo de fallo:** El agente-observer mismo falla o se degrada. No detecta anomalias. Un problema en produccion crece sin ser notado.

**Circuit breakers:**

- **Alertas clasicas como backstop:** Las alertas tradicionales de Prometheus/Grafana **DEBEN** seguir activas como capa independiente del agente-observer.
- **Heartbeat del observer:** El agente-observer **DEBE** emitir un heartbeat periodico. Si el heartbeat se pierde, el sistema **DEBE** alertar al Operador: "el observador ha dejado de observar."
- **Separacion de provider:** El agente-observer **DEBE** correr en infraestructura diferente a la aplicacion que observa. Si la aplicacion cae, el observer sigue arriba.

---

## 11. Stack de Referencia

Esta seccion es referencial, no prescriptiva. Cada organizacion elige sus herramientas. Lo que importa son las funciones, no los nombres.

| Funcion | Herramientas de referencia | Notas |
|---|---|---|
| **Repositorio + Code Review** | GitHub, GitLab | Merge queues para gestionar rafagas de PRs de agentes |
| **CI (build + test)** | GitHub Actions, GitLab CI | Con soporte para agent runners como ciudadanos de primera clase |
| **Evals de LLM** | Langfuse, Braintrust, custom | Corazon de la verificacion post-agente. Instrumentacion OTEL |
| **CD (deploy)** | ArgoCD, Flux (GitOps) | Deploys declarativos, reconciliacion continua, rollback automatico |
| **Feature Flags** | LaunchDarkly, Unleash, Flagsmith | Primitiva base para deploy continuo sin riesgo |
| **IaC** | Terraform, Pulumi, OpenTofu | Artefacto versionado. Generado por agente, aprobado por humano |
| **IaConversation** | Pulumi Neo, AWS Kiro | Capa conversacional sobre IaC |
| **Container Runtime** | Docker, Kubernetes | K8s para escala; Docker Compose para equipos pequenos |
| **Observabilidad** | Prometheus + Grafana + Loki (LGTM stack) | OpenTelemetry como instrumentacion universal |
| **Observabilidad LLM** | Langfuse, Helicone | Tokens, costes, calidad por modelo/agente |
| **Seguridad** | Trivy, Semgrep, Snyk + agente-security | SAST/DAST como input; agente-security como analisis contextual |
| **Secrets** | HashiCorp Vault, SOPS, AWS Secrets Manager | Inyeccion en runtime, nunca en codigo ni en contexto de agente |
| **Service Catalog** | Backstage (Spotify) | Catalogo de servicios que agentes y humanos consultan |
| **Agent Runtime** | GitHub Agentic Workflows, AWS AgentCore | Emergiendo (preview/nuevo). Mientras tanto: containers Docker con permisos restrictivos |

---

## 12. Los 9 Axiomas de Swarm::Ops

> **Axioma 1:** Las siete funciones son invariantes. Las implementaciones son efimeras.

> **Axioma 2:** El pipeline lineal esta muerto. El sistema nervioso adaptativo lo reemplaza.

> **Axioma 3:** La configuracion es intencion declarada, no YAML artesanal.

> **Axioma 4:** CI verde es condicion necesaria pero radicalmente insuficiente.

> **Axioma 5:** Los agentes son ciudadanos de primera clase del pipeline, no scripts glorificados.

> **Axioma 6:** La seguridad es un agente omnipresente, no un paso que se "shift left."

> **Axioma 7:** La observabilidad es inteligencia activa, no dashboards pasivos.

> **Axioma 8:** Cada accion de cada agente es auditable. No hay cajas negras.

> **Axioma 9:** El Operador declara el que. El enjambre resuelve el como. El humano tiene veto absoluto.

---

## 13. Tabla de Correspondencia Prehistoria -> Swarm::Ops

| Concepto clasico | Estado | Transformacion Swarm::Ops |
|---|---|---|
| Jenkins pipeline | Colapsa | Sistema nervioso adaptativo con orquestador inteligente |
| YAML de CI/CD artesanal | Colapsa | Intencion declarada por Operador -> config generada por agente |
| Build server / runner | Muta | Se bifurca en Execution Environment (determinista) + Agent Runtime (no-determinista) |
| "CI verde = listo" | Colapsa | CI verde es condicion necesaria pero insuficiente. 5 capas de verificacion |
| Staging environment | Colapsa | Feature flags + canary deploys + eval post-deploy + rollback automatico |
| Deploy manual/aprobado | Muta | Automatico para riesgo bajo. Humano solo para cambios destructivos/alto riesgo |
| Terraform/Pulumi (escrito a mano) | Muta | IaC sigue como artefacto. Generado por agente via IaConversation. Humano revisa diff |
| Dashboard de Grafana | Muta | Sigue existiendo como visualizacion. Un agente-observer lo interpreta activamente |
| On-call humano 24/7 | Muta | Agente-observer como primera linea. Humano como escalacion para incidentes complejos |
| Runbooks manuales | Colapsa | Runbooks ejecutados por agentes. Escritos para ser machine-readable |
| DevSecOps (scan estatico) | Muta | Agente-security con analisis contextual + diversidad de modelos. SAST como input, no como solucion |
| "Shift left" | Colapsa | La seguridad/calidad es un agente omnipresente, no una responsabilidad que se "mueve" |
| Helm charts manuales | Colapsa | GitOps declarativo (ArgoCD/Flux) con manifests generados por agente |
| Docker build | Sobrevive | Inmutabilidad de artefactos es invariante. Dockerfile generado por agente |
| Feature flags | Sobrevive (amplificado) | De "nice to have" a primitiva base obligatoria para deploy continuo |
| OpenTelemetry | Sobrevive (amplificado) | Lingua franca de instrumentacion. Ahora tambien instrumenta operaciones de agentes IA |
| GitOps | Sobrevive (amplificado) | Git como fuente de verdad para codigo, infra, config y estado del enjambre |
| Principio de minimo privilegio | Invariante | Cada agente y cada componente: exactamente los permisos necesarios |
| Idempotencia | Invariante | Operaciones de infra **DEBEN** poder re-ejecutarse sin efectos laterales |
| Blast radius control | Invariante | Canary, traffic splitting, feature flags. El mecanismo cambia; el principio no |

---

## 14. Validacion

| Check | Criterio | Accion si falla |
|---|---|---|
| 7 funciones cubiertas | F1-F7 tienen implementacion definida y agente responsable | Agregar funcion faltante |
| Agentes con modelo asignado | Cada agente-* tiene modelo/provider documentado | Asignar modelo |
| Diversidad de modelos | Agente-security usa modelo diferente al agente-coder | Cambiar modelo de security |
| 5 capas de verificacion | Cada PR pasa las 5 capas de [-> 4.4] antes de deploy | Agregar capa faltante |
| IaConversation en 5 fases | El flujo de infraestructura cumple las 5 fases de [-> 5.2] | Completar fase faltante |
| 4 primitivas de agente | Cada agente en pipeline cumple las 4 primitivas de [-> 6.2] | Implementar primitiva faltante |
| Circuit breakers activos | Los 4 modos de fallo de [-> 10] tienen circuit breakers implementados | Implementar circuit breaker |
| Observabilidad instrumentada | Agentes instrumentan con OpenTelemetry; LLMs con Langfuse | Agregar instrumentacion |
| Alertas clasicas como backstop | Alertas de Prometheus/Grafana activas independientemente del agente-observer | Configurar alertas clasicas |
| Heartbeat del observer | Agente-observer emite heartbeat periodico | Implementar heartbeat |
| Golden Paths definidos | Al menos los 4 Golden Paths de [-> 9.2] documentados y funcionales | Definir Golden Path faltante |
| Controles meta de security | Los 4 controles de [-> 8.3] implementados | Implementar control faltante |
| 9 axiomas respetados | Ninguna decision operacional contradice los axiomas de [-> 12] | Corregir decision |
