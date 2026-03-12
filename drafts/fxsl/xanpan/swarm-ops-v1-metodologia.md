---
_manifest:
  urn: "urn:fxsl:kb:swarm-ops-metodologia"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-11"
    source: "swarm-ops-v1-metodologia.md (source/fxsl/xanpan)"
version: "1.0.0"
status: draft
tags: [swarm-ops, devops, cicd, agentes, operaciones]
lang: es
extensions:
  fxsl:
    family: methodology
---

# SWARM::OPS v1.0

Framework operacional para software construido y operado por enjambres de agentes IA. Reinterpreta CI/CD, DevOps y Platform Engineering sin eliminar sus funciones invariantes.

## Ruptura Operacional de CI/CD Lineal

**Premisa historica** - El pipeline lineal resolvia integracion de trabajo humano discreto: commits espaciados, tests escritos por humanos, deploys relevantes, infraestructura relativamente estable.

**Ruptura 2026** - El modelo deja de ser suficiente cuando:

- los commits llegan en rafagas de minutos, no horas
- el mismo enjambre genera codigo y tests
- los deploys pueden ocurrir decenas de veces por dia
- la infraestructura se expresa conversacionalmente y luego se materializa como IaC

**Diagnostico** - El pipeline lineal no "falla"; se vuelve cuello de botella. DevOps tampoco "muere"; muta su implementacion. Sobreviven sus fines: responsabilidad compartida, automatizacion y feedback corto.

## Funciones Invariantes de CI/CD y DevOps

Las funciones siguen siendo siete. Cambia la implementacion, no la necesidad.

| Id | Funcion | Problema permanente | Implementacion clasica |
| --- | --- | --- | --- |
| `F1` | Integracion | Verificar que trabajo paralelo coexiste | CI server |
| `F2` | Verificacion | Confirmar cumplimiento de especificacion | Test runners |
| `F3` | Empaquetado | Producir artefactos desplegables | Build systems |
| `F4` | Entrega | Mover artefactos a runtime | CD pipelines, registries, Helm |
| `F5` | Provisioning | Crear y configurar infraestructura | Terraform, Pulumi, CloudFormation |
| `F6` | Observabilidad | Ver estado real del sistema | Prometheus, Grafana, Datadog |
| `F7` | Recuperacion | Volver a estado funcional | Rollbacks, runbooks, on-call |

### Axiomas Culturales que Sobreviven

**DevOps** preserva tres axiomas:

1. Desarrollo y operacion comparten responsabilidad.
2. Lo repetitivo debe automatizarse.
3. El feedback debe llegar lo antes posible.

**Platform Engineering** agrega una conclusion pre-agente:

- el tool sprawl aumenta carga cognitiva
- "shift left" mal implementado termina en "dump left"
- se necesitan plataformas internas con self-service y abstraccion

**Swarm::Ops** absorbe ese movimiento y cambia el cliente primario de la plataforma: del developer humano al agente IA.

## Cinco Asunciones que Colapsan

| Asuncion heredada | Realidad con enjambre | Consecuencia operacional |
| --- | --- | --- |
| Commits discretos y espaciados | PRs cada 10-30 minutos por agente; 5 agentes pueden producir 10-30 PRs/hora | El pipeline secuencial se satura |
| Tests independientes del codigo | El mismo modelo puede generar codigo y tests | `CI verde` deja de probar correccion real |
| YAML mantenido por humanos | Los agentes pueden generar y mantener configuracion con mayor consistencia | El YAML artesanal pasa a ser anti-patron |
| Deploy como evento humano | El ritmo natural de cambio es continuo | La aprobacion humana queda reservada a cambios destructivos o de alto riesgo |
| Infraestructura definida solo en archivos escritos a mano | El operador puede declarar intencion y un agente materializar IaC | Nace `Infrastructure as Conversation` |

### Invariantes que No Cambian

- **Idempotencia** - La infraestructura debe tolerar re-aplicacion.
- **Inmutabilidad de artefactos** - Las imagenes construidas no se parchean en produccion.
- **Trazabilidad** - Todo cambio debe vincularse a commit, PR, decision y, con agentes, tambien a historia y OKR.
- **Minimo privilegio** - Cada humano o agente recibe solo los permisos estrictamente necesarios.
- **Control de blast radius** - Canary, feature flags y traffic splitting siguen siendo obligatorios.

## Definicion de Swarm::Ops

**Swarm::Ops** - Framework operacional para software donde el ejecutor primario es un enjambre de agentes IA. No es un producto; es un conjunto de principios, patrones y capacidades para ejecutar las funciones `F1-F7` en un entorno agentico.

### Tres Cambios de Paradigma

| Cambio | Antes | Swarm::Ops |
| --- | --- | --- |
| Topologia | Pipeline lineal | Sistema nervioso adaptativo |
| Configuracion | Pasos imperativos | Intencion declarada |
| Naturaleza de la herramienta | Runner pasivo | Agente activo con decision local |

#### Pipeline -> Sistema Nervioso

No existe una unica linea `commit -> build -> test -> deploy`. Existen flujos concurrentes que responden a eventos: commits, evals, alertas, cambios de configuracion, drift o propuestas del Sentinel.

#### Configuracion Estatica -> Intencion Declarada

El operador declara politicas como:

- tipos + tests unitarios + eval de regresion antes de merge
- eval de seguridad extra para modulos de autenticacion
- canary al `5%` con expansion si las metricas se mantienen por `15` minutos
- presupuesto maximo diario de tokens para operaciones CI/CD

El enjambre traduce esa intencion a configuracion ejecutable.

#### Herramienta Pasiva -> Agente Activo

Los componentes operacionales ya no solo ejecutan comandos. Seleccionan estrategias:

- que tests correr
- cuando hacer canary vs fast-track
- cuando pausar despliegues
- cuando proponer rollback

## Las Siete Funciones Reinterpretadas

| Funcion | Implementacion clasica | Implementacion Swarm::Ops |
| --- | --- | --- |
| Integracion | Merge + build en CI | Agente-integrador valida coherencia semantica y resuelve conflictos triviales |
| Verificacion | Suites fijas | Agente-verificador selecciona tests por tipo de cambio y agrega eval independiente con modelo distinto al autor |
| Empaquetado | Build determinista | Se preserva Docker; cambia el autor del Dockerfile y de la configuracion |
| Entrega | Stages fijos | Agente-deployer con estrategia adaptativa y feature flags como primitiva base |
| Provisioning | IaC escrita a mano | IaConversation: intencion -> IaC generada -> plan -> diff -> apply -> verificacion |
| Observabilidad | Dashboards pasivos | Agente-observer analiza metricas, correlaciona eventos y propone accion |
| Recuperacion | Rollback manual | Rollback automatico cuando fallan evals post-deploy; runbooks ejecutables por agentes |

## Sistema Nervioso Operacional

### Componentes

| Componente | Funcion |
| --- | --- |
| Receptores | Commit, PR, alerta, cambio de configuracion, propuesta del Sentinel, heartbeat, resultado de eval |
| Nervios aferentes | Clasificacion automatica: tipo de cambio, riesgo, zona afectada, necesidad de aprobacion humana |
| Centro de procesamiento | Orquestador que decide acciones segun reglas declaradas |
| Nervios eferentes | Agentes de build, test, eval, deploy, rollback y notificacion |
| Feedback loop | Cada resultado re-clasifica el estado del cambio y del sistema |

### Flujos Concurrentes

**Verificacion continua**

| Tipo de cambio | Acciones | Latencia esperada |
| --- | --- | --- |
| `lectura` | lint + type check + tests unitarios | minutos |
| `escritura` | lo anterior + eval de regresion + tests de integracion | minutos |
| `destructivo` | lo anterior + eval de seguridad + hold humano | horas |

**Deploy continuo**

- **Modo rafaga** - Deploy cada `N` minutos cuando hay cambios verificados. Uso: desarrollo.
- **Modo canary** - Despliegue a una fraccion del trafico, observacion y expansion. Uso: produccion.
- **Modo manual** - Hold explicito. Uso: cambios destructivos o de alto riesgo.

**Observacion permanente**

El agente-observer monitorea sin espera activa. Correlaciona anomalias con deploys recientes y propone rollback cuando la confianza lo justifica.

### Fin de "`CI verde = listo`"

La confianza minima pasa a ser multicapa:

1. `CI verde` - lint, tipos, tests.
2. Eval de regresion - dataset parcialmente humano.
3. Eval de diversidad - modelo revisor distinto al modelo autor.
4. Eval de seguridad - analisis estatico, dinamico y privilegios.
5. Aprobacion humana - ultima barrera para cambios riesgosos.

## Infraestructura como Conversacion

### IaC Clasica vs IaConversation

| Paso | IaC clasica | IaConversation |
| --- | --- | --- |
| Declaracion | Humano escribe Terraform/Pulumi | Operador expresa intencion en lenguaje natural |
| Plan | Herramienta genera plan | Agente genera IaC y plan |
| Revision | Humano revisa plan | Operador revisa diff contra estado actual |
| Apply | Humano ejecuta | Agente aplica tras aprobacion |
| Post-condicion | Manual o parcial | Agente verifica estado y monitorea drift |

**Invariante** - El artefacto IaC no desaparece. Sigue versionado, auditable y reproducible.

### Modo Degradado para 1 VPS + Docker Compose

Si la infraestructura cabe en `docker-compose.yml`, ese archivo es IaC suficiente. El patron completo se degrada a:

1. Intencion conversacional.
2. Actualizacion del `docker-compose`.
3. Revision del diff.
4. `docker compose up -d`.
5. Verificacion posterior.

No se justifica Terraform, Pulumi o una capa conversacional dedicada mientras Docker Compose siga siendo suficiente.

### Proto-patron Comercial 2025-2026

- **Pulumi Neo** - Genera plan IaC desde lenguaje natural, abre PR y espera aprobacion.
- **AWS Kiro** - Sigue el mismo patron.
- **Cloud providers** - Google Cloud y Azure convergen hacia esa interfaz.

### Context Engineering para Infraestructura

- **INFRA.md** - Providers, regiones, servicios, networking.
- **CONSTRAINTS.md** - Presupuesto, residencia de datos, cifrado, SLA.
- **RUNBOOKS.md** - Procedimientos de recuperacion escritos para ejecucion por agentes.

## El Agente como Ciudadano de Primera Clase del Pipeline

### Por que un Agente no es un Script

- es no-determinista
- requiere contexto amplio, no solo diff puntual
- consume tokens y recursos de forma variable
- puede fallar produciendo salida plausible pero incorrecta

### Cuatro Primitivas Necesarias

| Primitiva | Funcion |
| --- | --- |
| Workflow Definition | Define disparadores, permisos, artefactos accesibles y outputs |
| Execution Sandbox | Aisla filesystem, red, secretos y registra acciones |
| Safe Operation Primitives | Establece read-only por defecto, outputs estructurados y escalamiento explicito |
| State Management | Conserva memoria entre ejecuciones y la versiona junto con el codigo |

### Caveat de Madurez

GitHub Agentic Workflows seguia en preview en febrero de 2025 y AWS AgentCore era reciente. Mientras esas plataformas maduran, ejecutar agentes en contenedores Docker con filesystem read-only, red limitada, secretos selectivos y logging completo cubre las funciones esenciales.

### Runner Clasico vs Runtime Agente

| Entidad | Naturaleza |
| --- | --- |
| Execution Environment | Donde corre build/test. Determinista. |
| Agent Runtime | Donde el agente razona y produce output. No determinista. |

Ambos requieren lifecycle, permisos y monitoreo distintos.

## Observabilidad Activa

### Evolucion

| Era | Modelo | Salida |
| --- | --- | --- |
| Monitoreo | Umbrales de CPU/RAM/disco | Alertas basicas |
| Observabilidad | Logs + metricas + traces | Dashboards interpretados por humanos |
| Inteligencia activa | Agente-observer sobre esos tres pilares | Deteccion, correlacion, diagnostico y recomendacion |

### Ruta Progresiva del Agente-observer

1. **Etapa 1** - Alertas clasicas con reglas estaticas.
2. **Etapa 2** - Correlacion manual asistida por LLM.
3. **Etapa 3** - Script que recolecta contexto y pide diagnostico al LLM.
4. **Etapa 4** - Agente-observer completo con monitoreo continuo y propuesta de accion.

La mayoria de equipos puede permanecer largo tiempo en etapas `2-3`.

### Funciones del Agente-observer

| Funcion | Humano clasico | Agente-observer |
| --- | --- | --- |
| Detectar anomalia | Mira dashboard o recibe alerta | Detecta anomalias estadisticas pre-alerta |
| Correlacionar causa | Revisa deploys o cambios | Cruza automaticamente deploys, trafico y configuracion |
| Diagnosticar | Inspeccion manual de logs y traces | Filtra ventana temporal y propone hipotesis |
| Proponer accion | Sugiere rollback | Recomienda accion con nivel de confianza |
| Ejecutar | Manual o script | Automatico solo si la politica lo permite |

### OpenTelemetry y Langfuse

**OpenTelemetry** se vuelve lingua franca operacional:

- trazas end-to-end por historia
- metricas de tokens, latencia y exito por agente/modelo
- logs de decision, no solo de accion

**Langfuse** cubre la capa LLM:

- coste de tokens por trace
- calidad de salida por modelo
- patrones de alucinacion
- drift entre versiones de modelo

## Security-by-Swarm

### Limites de DevSecOps Clasico

- SAST/DAST generan fatiga de alertas
- "shift left" suele descargar trabajo sin aumentar capacidad
- el analisis estatico no cubre errores de logica o interaccion compleja
- aparece una superficie nueva: `agent-to-agent prompt injection`

### Seguridad como Agente Activo

**En analisis**

- clasificacion automatica de riesgo por PR
- analisis contextual usando la arquitectura completa
- priorizacion por impacto real, no por volumen de hallazgos

**En produccion**

- monitoreo de comportamiento anomalo
- correlacion con intelligence feeds y CVEs
- evaluacion de exposicion real, no solo de dependencia vulnerable

### Principio de Diversidad

El agente-security debe usar modelo distinto al agente-coder. El objetivo es reducir blind spots compartidos.

### Quis Custodiet del Agente-security

| Control meta | Funcion |
| --- | --- |
| Modelo distinto al enjambre | Reduce zonas ciegas compartidas |
| Meta-eval mensual | Detecta fallas frente a patrones adversariales conocidos |
| Veto asimetrico | Puede bloquear, no aprobar en solitario |
| Auditoria externa periodica | Evalua decisiones aprobadas y rechazadas |

## Operador como Platform Engineer del Enjambre

### Convergencia de Roles

El operador deja de escribir YAML linea por linea y pasa a declarar intenciones y restricciones operacionales. El PO no desaparece: define restricciones de negocio, SLA y presupuestos que el operador traduce a politica operacional.

### Ejemplos de Politica Declarada

- cada PR pasa por lint, tipos, tests y eval de regresion antes de merge
- autenticacion exige eval de seguridad y aprobacion humana
- produccion usa canary de `5%` y expansion tras `15` minutos estables
- existe un presupuesto maximo diario de tokens para CI/CD

### Golden Paths para Agentes

| Path | Secuencia base |
| --- | --- |
| Historia estandar | PR -> lint -> types -> tests -> eval regresion -> merge -> deploy canary -> expand |
| Historia destructiva | PR -> lint -> types -> tests -> eval regresion -> eval seguridad -> hold -> aprobacion -> deploy canary |
| Infraestructura | intent -> IaC generation -> plan -> diff review -> apply -> verify -> drift monitor |
| Hotfix | bug -> diagnostico agente -> fix + test -> eval express -> deploy con rollback automatico |

### Self-service para el Enjambre

- templates de servicio con estructura, CI/CD y monitoreo
- entornos efimeros para testing
- registros centralizados de artefactos
- catalogo vivo de servicios internos

## Modos de Fallo y Circuit Breakers

| Modo de fallo | Sintoma | Circuit breakers |
| --- | --- | --- |
| Cascada de deploys defectuosos | Cambios individualmente validos fallan en combinacion | deploy batching; canary con correlacion; rollback atomico por batch |
| Saturacion del pipeline por rafaga | 5 agentes pueden producir 30 PRs/hora | backpressure; priorizacion por valor; merge queues inteligentes |
| Drift de infraestructura no detectado | Estado real diverge del declarado | drift detection continua; prohibicion de cambios manuales; reconciliacion automatica para drift trivial |
| Fallo del agente-observer | No detecta anomalias | alertas clasicas como backstop; heartbeat; separacion de provider/infraestructura |

## Stack de Referencia 2026

Stack referencial, no prescriptivo.

| Funcion | Herramientas de referencia | Nota |
| --- | --- | --- |
| Repositorio y review | GitHub, GitLab | Merge queues para rafagas de PRs |
| CI | GitHub Actions, GitLab CI | Soporte para agent runners |
| Evals de LLM | Langfuse, Braintrust, custom | Verificacion post-agente |
| CD | ArgoCD, Flux | GitOps, reconciliacion continua, rollback |
| Feature flags | LaunchDarkly, Unleash, Flagsmith | Primitiva base de deploy continuo |
| IaC | Terraform, Pulumi, OpenTofu | Artefacto versionado; generado por agente, aprobado por humano |
| IaConversation | Pulumi Neo, AWS Kiro | Capa conversacional sobre IaC |
| Runtime de contenedores | Docker, Kubernetes | Compose para equipos pequenos; K8s para escala |
| Observabilidad | Prometheus, Grafana, Loki | OTEL como instrumentacion comun |
| Observabilidad LLM | Langfuse, Helicone | Tokens, coste y calidad |
| Seguridad | Trivy, Semgrep, Snyk + agente-security | SAST/DAST como input, no como solucion completa |
| Secrets | Vault, SOPS, AWS Secrets Manager | Nunca en codigo ni contexto del agente |
| Catalogo de servicios | Backstage | Consulta por humanos y agentes |
| Agent Runtime | GitHub Agentic Workflows, AWS AgentCore | Categoria emergente; Docker endurecido cubre mientras tanto |

## Correspondencia Prehistoria -> Swarm::Ops

| Concepto heredado | Estado | Transformacion |
| --- | --- | --- |
| Jenkins pipeline | colapsa | sistema nervioso adaptativo |
| YAML artesanal | colapsa | intencion declarada -> config generada por agente |
| Runner | muta | `Execution Environment` + `Agent Runtime` |
| `CI verde = listo` | colapsa | cinco capas de confianza |
| Staging permanente | colapsa | feature flags + canary + eval post-deploy + rollback |
| Deploy manual como norma | muta | automatico para riesgo bajo; humano para riesgo alto |
| Terraform/Pulumi escritos a mano | muta | IaC generada por agente, diff revisado por humano |
| Dashboard pasivo | muta | dashboard + agente-observer |
| On-call humano 24/7 | muta | agente-observer como primera linea; humano como escalacion para incidentes complejos |
| Runbook manual | colapsa | runbook ejecutable por agentes |
| DevSecOps como paso | muta | seguridad omnipresente via agente-security |
| Shift left | colapsa | seguridad y calidad omnipresentes; no responsabilidad que se "mueve" |
| Helm charts manuales | colapsa | GitOps declarativo con manifests generados por agente |
| Docker build | sobrevive | la inmutabilidad sigue siendo invariante |
| Feature flags | sobrevive y se amplifica | pasan de opcionales a obligatorias |
| OpenTelemetry | sobrevive y se amplifica | observabilidad de software y de agentes |
| GitOps | sobrevive y se amplifica | git como fuente de verdad de codigo, infra y estado |
| Minimo privilegio | invariante | aplica a humanos y agentes |
| Idempotencia | invariante | obligatoria en provisioning y reconciliacion |
| Blast radius control | invariante | canary, traffic splitting y feature flags; cambia el mecanismo, no el principio |

## Axiomas de Swarm::Ops

1. Las siete funciones son invariantes; sus implementaciones son efimeras.
2. El pipeline lineal es insuficiente; lo reemplaza un sistema nervioso adaptativo.
3. La configuracion expresa intencion declarada, no YAML artesanal.
4. `CI verde` es necesario pero insuficiente.
5. Los agentes son ciudadanos de primera clase del pipeline.
6. La seguridad es omnipresente; no un paso que se mueve "a la izquierda".
7. La observabilidad es inteligencia activa, no solo visualizacion.
8. Cada accion de cada agente debe ser auditable.
9. El operador declara el que; el enjambre resuelve el como; el humano mantiene veto absoluto.
