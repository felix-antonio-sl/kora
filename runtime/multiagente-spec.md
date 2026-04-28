---
_manifest:
  urn: "urn:kora:kb:multiagente-spec"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-19"
    source: "Cierra H5 del backlog post-olas: formaliza coreografia multiagente como sheaf operacional para OpenClaw + ACP y otros runtimes que proyecten ejecucion distribuida."
version: "1.0.0"
status: publicado
tags: [spec, runtime, multiagente, coreografia, sheaf, acp, openclaw]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:cat-ecosystem-2cat"
    - "urn:kora:kb:cat-behavioral-preservation"
    - "urn:kora:kb:cat-governance-lattice"
    - "urn:fxsl:kb:icas-protocolos"
    - "urn:fxsl:kb:icas-topoi"
    - "urn:agengai:kb:openclaw-runtime-extension"
---

# KORA/Multiagente-Spec v1.0.0

## 1. Definicion

`multiagente-spec` gobierna la **coreografia multiagente** de KORA: la ley
global que hace coherente un conjunto de agentes, handoffs, backends y puntos
de control humano cuando el sistema se ejecuta como un solo artefacto
distribuido.

La decision canonica de esta spec es:

> Una ejecucion multiagente **SOLO ES VALIDA** si las vistas locales de cada
> agente pegan en una seccion global coherente sobre los solapamientos
> obligatorios del protocolo.

En terminos categoricos:

1. La **coreografia** se modela como un sheaf de secciones locales.
2. La **orquestacion** es la eleccion operativa de un arbol o wiring diagram
   que realiza esa coreografia.
3. Un runtime **NO DEBE** sustituir la ley global por decisiones locales
   opacas; si no puede pegar, debe declarar degradacion o abortar.

Rationale: el corpus ICAS-BoK distingue coreografia (ley global) de
orquestacion (ejecutor local), y usa sheaves para capturar coherencia
local-global. OpenClaw/ACP realiza esta necesidad de forma concreta porque
distribuye fases entre agentes y backends heterogeneos.

## 2. Definiciones

| Termino | Definicion |
|---------|------------|
| Protocolo | Secuencia tipada de fases, roles y handoffs que define una ejecucion distribuida. |
| Fase | Paso observable del protocolo sobre el que un agente publica una seccion local. |
| Seccion local | Vista parcial de un agente sobre una fase o subconjunto de fases. |
| Solapamiento | Interseccion entre dos vistas locales; contiene la informacion que ambas deben compartir. |
| Pegado | Construccion de una vista global a partir de secciones locales compatibles. |
| Coreografia | Ley global del protocolo independiente del scheduler concreto. |
| Orquestacion | Realizacion runtime de la coreografia mediante un orquestador, workflow o wiring diagram. |
| Handoff | Morfismo tipado entre una salida local y la entrada del siguiente rol. |
| Compensador | Morfismo inverso aproximado que deshace o mitiga un paso no idempotente. |
| Ticket de procedencia | Objeto minimo que preserva `session_id`, `protocol_id`, `actor_id`, vector de calidad aplicable y referencia al paso previo. |

## 3. Modelo canonico

### 3.1 Sheaf de coreografia

Una ejecucion multiagente se describe mediante el objeto:

```text
Ch = (Roles, Fases, Cover, Sec, Glue)
```

donde:

1. `Roles` es el conjunto de roles o agentes participantes.
2. `Fases` es el conjunto ordenado de fases observables del protocolo.
3. `Cover` asigna a cada rol la subfamilia de fases que puede observar o
   realizar.
4. `Sec` asigna a cada rol una seccion local compatible con su cover.
5. `Glue` construye una seccion global solo si las secciones locales coinciden
   sobre todos los solapamientos obligatorios.

Una coreografia valida **DEBE** declarar al menos:

1. `protocol_id`,
2. `roles`,
3. `fases`,
4. criterio de handoff entre fases,
5. criterio de compensacion para pasos irreversibles.

### 3.2 Solapamientos obligatorios

Todo handoff multiagente **DEBE** preservar, como minimo, los siguientes
solapamientos:

1. `session_id` o identificador de corrida equivalente.
2. `protocol_id`.
3. `ticket de procedencia` del paso previo.
4. `qa_budget.sigma_min` o, en su ausencia, el piso duro derivado de `Σ`.
5. subconjunto de herramientas/autorizaciones efectivamente delegado.
6. `resume_token` o equivalente si la fase puede suspenderse y reanudarse.

Correcto: delegar una fase adjuntando `session_id`, `protocol_id`,
`parent_step_id`, budget vigente y capabilities efectivas.

Incorrecto: disparar un backend distinto con prompt suelto sin propagar
identidad de corrida ni piso de calidad.

Rationale: sin estos solapamientos el sheaf no pega; la corrida global se
fractura en episodios independientes sin prueba de coherencia.

## 4. Coreografia vs orquestacion

La coreografia y la orquestacion **NO SON** sinonimos.

| Aspecto | Coreografia | Orquestacion |
|---------|-------------|--------------|
| Naturaleza | Ley global | Ejecucion local |
| Objeto | Sheaf de protocolo | Operad / wiring diagram / workflow |
| Autoridad | Previa al runtime | Elegida por runtime |
| Fallo tipico | Solapamientos incompatibles | Scheduler invalido o incompleto |

Reglas:

1. Un orquestador **PUEDE** elegir el orden local de ejecucion si no rompe la
   ley global.
2. Un orquestador **NO DEBE** omitir fases obligatorias del protocolo.
3. Un workflow runtime **NO DEBE** introducir handoffs no tipados.
4. Si una orquestacion colapsa dos fases en una sola, la perdida **DEBE**
   declararse como degradacion de `Ξ`.

## 5. Handoffs canonicos

### 5.1 Envelope minimo

Forma canonica recomendada para un handoff:

```yaml
handoff:
  protocol_id: triage-clinico-v1
  session_id: ses-2026-04-19-001
  from_role: intake
  to_role: analisis
  parent_step_id: step-03
  qa_floor: [0.67, 0.33, 0.67, 0.67, 0.33]
  capabilities:
    tools: [search, summarize]
    authority: delegated
  payload_ref: urn:salud:kb:firs-framework-integrado-razonamiento-salud
  compensator: rollback-analisis
```

### 5.2 Reglas

1. Todo handoff **DEBE** ser tipado: emisor, receptor, payload y capacidad
   delegada tienen que ser observables.
2. El receptor **NO DEBE** asumir herramientas que no vengan delegadas.
3. Un handoff irreversible **DEBE** declarar compensador o marcar deuda
   terminal explicita.
4. Un handoff que cruza de backend **DEBE** preservar `session_id` y el piso de
   calidad vigente.
5. El payload **DEBERIA** viajar por referencia resoluble (`payload_ref`) antes
   que por copia textual si existe un artefacto canonico indexado.

## 6. Compensacion y sagas

Los protocolos con efectos no idempotentes **DEBEN** tratarse como sagas
parciales, no como transacciones fingidas.

Reglas:

1. Un paso reversible **PUEDE** declararse sin compensador si el runtime
   garantiza idempotencia.
2. Un paso no reversible **DEBE** declarar `compensator` o `debt_terminal`.
3. Una compensacion **NO DEBE** prometer restauracion perfecta si solo logra
   mitigacion parcial; debe declararse como aproximacion.
4. Si la compensacion rebaja el piso de calidad, esa rebaja **DEBE**
   materializarse como perdida declarada en `qa_budget` o en el registro de
   riesgo.

## 7. Realizacion en OpenClaw + ACP

OpenClaw es la realizacion de referencia de esta spec porque opera como
meta-runtime ACP sobre 15 backends. La regla es:

1. `acp.dispatch` cambia backend, **NO** cambia `protocol_id`.
2. `agentToAgent` y `dispatch` son handoffs validos solo si transportan el
   envelope minimo de §5.1.
3. Un backend alterno **NO DEBE** seleccionarse si su proyeccion cruza el piso
   duro derivado de `Σ` o `qa_budget.sigma_min`.
4. Un checkpoint humano cuenta como fase valida del protocolo; su suspension y
   reanudacion **DEBEN** conservar `session_id`, `resume_token` y procedencia.

Rationale: ACP amplifica el problema de coherencia porque la ejecucion se mueve
entre backends heterogeneos. Precisamente por eso la ley global no puede quedar
implicita.

## 8. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| `protocol-id-preserved` | Cada handoff declara y preserva `protocol_id` | manual |
| `session-id-preserved` | `session_id` no se pierde en cruces de agente/backend | manual |
| `qa-floor-preserved` | El handoff propaga o estrecha el piso, nunca lo relaja silenciosamente | manual |
| `handoff-capability-typed` | Herramientas/autorizaciones delegadas estan declaradas | manual |
| `compensator-declared` | Pasos irreversibles declaran compensador o deuda terminal | manual |
| `local-global-glue` | Las secciones locales pegan sin contradiccion en los solapamientos | manual |

## 9. Relacion con otras specs

1. `harness-spec` define los ejes `Π/Μ/Ξ/Λ/Φ/Σ` que esta spec debe preservar
   en la corrida distribuida.
2. `qa-spec` fija el piso de calidad que un handoff no puede relajar
   silenciosamente.
3. `runtime-spec-md` gobierna invariantes runtime comunes.
4. `transmutation-spec` gobierna la proyeccion IR -> target; esta spec gobierna
   la coherencia multiagente dentro de esa proyeccion.
5. `openclaw-runtime-extension` especializa esta ley para ACP y backends
   concretos.

## 10. Migracion

`multiagente-spec v1.0.0` es aditiva.

Reglas de migracion:

1. Los agentes existentes **NO REQUIEREN** cambiar shape por el solo hecho de
   no participar en coreografias multiagente.
2. Todo artefacto que declare `Ξ>=3` **DEBERIA** documentar sus handoffs
   conforme a esta spec.
3. Todo artefacto que declare `Ξ=4` **DEBERIA** explicitar `roles`, `fases` y
   compensadores de forma auditable.
