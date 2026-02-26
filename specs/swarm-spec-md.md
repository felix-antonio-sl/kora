---
_manifest:
  urn: "urn:kora:kb:swarm-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-26"
    source: "KORA agent-spec-md v7.2.0, categorical-foundations 00-04, xanpan corpus (swarm-ops, xanpan-agents, stack-llm)"
version: "1.1.0"
status: published
tags: [spec, swarm, orchestration, multi-agent, golden-path, circuit-breaker, backpressure, event-routing, traceability]
lang: es
---

# KORA/Swarm-Spec --- Orquestacion Multi-Agente v1.1.0

## 1. Definicion

> Este documento es prescriptivo y **ESTA GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md).

Esta especificacion gobierna como multiples agentes KORA se coordinan para ejecutar tareas complejas que exceden la capacidad de un agente individual. Un agente individual es definido por [agent-spec-md](urn:kora:kb:agent-spec-md) §3; esta especificacion define como esos agentes se componen en *swarms* — sistemas multi-agente con orquestacion, routing de eventos y mecanismos de resiliencia.

### 1.1 Alcance

Esta especificacion gobierna:

1. La composicion de multiples agentes en un swarm con wiring declarado
2. Los *Golden Paths* como pipelines de Skills secuenciales para flujos operacionales
3. Los *Circuit Breakers* como mecanismos de resiliencia ante fallos
4. El *Backpressure* como control de flujo para dispatch de tareas
5. El *Event Routing* como clasificacion y dispatch de eventos al Golden Path apropiado

Esta especificacion **NO DEBE** contradecir [agent-spec-md](urn:kora:kb:agent-spec-md). Las reglas de composicion multi-agente (agent-spec-md §7) se heredan integramente; esta especificacion las extiende al dominio de orquestacion.

Esta especificacion **NO DEBE** modificar la semantica de los componentes individuales de un agente. Solo define como multiples agentes se coordinan.

### 1.2 Dominios Ortogonales

Esta especificacion y [runtime-spec-md](urn:kora:kb:runtime-spec-md) son ortogonales:

- **runtime-spec-md** gobierna como **inyectar un agente** en una plataforma (transport).
- **swarm-spec-md** gobierna como **multiples agentes se coordinan** (orchestration).

Un swarm puede existir sin deployment cross-platform; un deployment cross-platform puede existir sin swarm.

---

## 2. Definiciones

La tabla de esta seccion **DEBE** incluir todo termino clave con significado preciso dentro de esta especificacion:

**Correcto:** `El documento usa "Golden Path" y "Circuit Breaker"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "Backpressure" como termino clave y no existe entrada para "Backpressure".`

| Termino | Definicion |
| --- | --- |
| **Swarm** | Sistema multi-agente compuesto por un orquestador y uno o mas agentes especializados, conectados via wiring declarado, que cooperan para ejecutar tareas que exceden la capacidad de un agente individual |
| **Orquestador** | Agente que actua como hub de routing: recibe eventos, los clasifica y los despacha al Golden Path apropiado. Implementa el patron master-child delegation de agent-spec-md §7 |
| **Golden Path** | Pipeline de Skills secuenciales que materializa un flujo operacional completo. Cada paso es un Skill con I/O tipado; la composicion es Kleisli: `step_n >=> ... >=> step_1` |
| **Circuit Breaker** | Mecanismo de resiliencia que detecta fallos en un agente o Golden Path y ejecuta una respuesta predefinida (retry, fallback, escalate, abort) antes de continuar |
| **Backpressure** | Mecanismo de control de flujo que limita la tasa de generacion de tareas cuando la cola de trabajo excede un umbral configurable |
| **Event** | Unidad de entrada al swarm: un commit, PR, alerta, resultado de eval, heartbeat u otra senal que requiere clasificacion y dispatch |
| **Event Taxonomy** | Clasificacion declarada de eventos en categorias que determinan el Golden Path de dispatch |
| **Nervous System** | Metafora arquitectonica para el swarm como grafo adaptativo de agentes que procesan eventos, toman decisiones locales y escalan cuando es necesario. Reemplaza la metafora del pipeline lineal |
| **Membership** | Conjunto de agentes que componen un swarm en una sesion. Monotonicamente creciente durante la sesion |
| **Wiring** | Grafo dirigido que conecta outputs de agentes con inputs de otros agentes dentro del swarm. Extiende el wiring de agent-spec-md §3.5 de arboles a grafos |

---

## 3. Swarm Composition Model

### 3.1 Principio

Un swarm es una extension del patron master-child delegation de [agent-spec-md](urn:kora:kb:agent-spec-md) §7. Donde agent-spec-md define composicion como un arbol (maestro delega a hijos), esta especificacion extiende la composicion a un grafo dirigido donde agentes pueden senalizarse entre si a traves del orquestador.

Traces to: formal/01 §6.2 (Sub-Agent Adjunction)

### 3.2 Estructura

Todo swarm **DEBE** tener:

1. **Exactamente un orquestador:** un agente que actua como hub central de routing. El orquestador recibe todos los eventos y los despacha.
2. **Uno o mas agentes especializados:** agentes que ejecutan tareas especificas dentro de Golden Paths.
3. **Wiring declarado:** la topologia de conexiones entre agentes, declarada en el AGENTS.md del orquestador.

**Correcto:** `El orquestador-swarm declara en AGENTS.md: "ACT: Despachar a deployer, verificador, observer segun tipo de evento." Wiring explicito.`
**Incorrecto:** `Multiples agentes se invocan ad-hoc sin orquestador central ni wiring declarado.`

### 3.3 Composicionalidad

El comportamiento de un swarm **DEBE** ser calculable desde:

1. Las transiciones individuales de cada agente (c_i)
2. El wiring del swarm (grafo de conexiones)
3. Sin inspeccionar el estado interno de cada agente

Traces to: formal/01 §6.3 (Compositionality theorem)

```python
class Swarm:
    """
    A swarm composes multiple agents via directed wiring.
    Behavior is determined by individual transitions + wiring topology.
    """
    orchestrator: Agent          # Hub de routing
    agents: dict[str, Agent]     # Agentes especializados por nombre
    wiring: DirectedGraph        # Conexiones output -> input
    golden_paths: dict[str, GoldenPath]  # Flujos operacionales
    circuit_breakers: dict[str, CircuitBreaker]  # Resiliencia por agente/path

    def dispatch(self, event: Event) -> Output:
        """Classify event and route to appropriate golden path."""
        path = self.orchestrator.classify(event)
        return self.execute_path(path, event)
```

### 3.4 Disipacion en Swarm

Los agentes especializados dentro de un swarm heredan behavior e interface del contexto del swarm pero **NO DEBEN** heredar la personalidad (SOUL.md) ni el operator context (USER.md) del orquestador.

Traces to: formal/01 §2.3 (Dissipation theorem)

**Correcto:** `El deployer hereda herramientas declaradas en su TOOLS.md y la FSM de su AGENTS.md. No hereda el tono del orquestador.`
**Incorrecto:** `El deployer adopta la personalidad del orquestador ("tono clinico e implacable") porque opera bajo su coordinacion.`

---

## 4. Golden Paths

### 4.1 Definicion

Un Golden Path es un pipeline de Skills secuenciales donde cada paso es un Skill con I/O tipado. La composicion sigue Kleisli composition: el output del paso i alimenta el input del paso i+1.

Traces to: formal/02 §6.1 (Kleisli composition >=>)

```python
def golden_path(steps: list[Skill], event: Event) -> Output:
    """
    Execute a Golden Path as Kleisli composition of Skills.
    step_n >=> step_{n-1} >=> ... >=> step_1
    """
    result = event
    for step in steps:
        result = step.execute(result)  # >>= in Kleisli
        if not result.success:
            return handle_failure(step, result)
    return result
```

### 4.2 Reglas

1. Cada Golden Path **DEBE** declarar su secuencia de pasos como Skills con I/O tipado.
2. El output de cada paso **DEBE** ser compatible con el input del paso siguiente. Incompatibilidad de tipos es un error de diseno, no de runtime.
3. Todo Golden Path **DEBE** tener un Circuit Breaker asociado (§5).
4. El orquestador **DEBE** declarar la taxonomia de eventos y el mapeo evento → Golden Path en su AGENTS.md.

**Correcto:**
```markdown
## Golden Path: Verificacion
Pasos:
1. CM-lint-check (Input: PR. Output: LintResult)
2. CM-type-check (Input: LintResult. Output: TypeResult)
3. CM-test-runner (Input: TypeResult. Output: TestResult)
4. CM-eval-regresion (Input: TestResult. Output: EvalResult)
Circuit Breaker: CB-verificacion (§5)
```

**Incorrecto:** `Un flujo de verificacion sin pasos tipados ni circuit breaker asociado.`

### 4.3 Composicion de Golden Paths

Dos Golden Paths **PUEDEN** componerse secuencialmente cuando el output del ultimo paso del primero es compatible con el input del primer paso del segundo:

```
path_deploy >=> path_verificacion
```

La composicion de Golden Paths preserva la composicionalidad del swarm.

Traces to: formal/01 §6.3 (Compositionality theorem)

---

## 5. Circuit Breakers

### 5.1 Definicion

Un Circuit Breaker es un mecanismo de resiliencia que detecta fallos en la ejecucion de un Golden Path o agente individual y ejecuta una respuesta predefinida. El swarm **NO DEBE** continuar operando tras un fallo sin verificar health.

Traces to: formal/01 §3.3 (Coinductive Verification — el swarm no termina sin verificar)

### 5.2 Modos de Fallo

Todo Circuit Breaker **DEBE** declarar su respuesta para cada modo de fallo:

| Modo | Definicion | Respuesta |
|------|-----------|-----------|
| **Retry** | El paso fallo por causa transitoria (timeout, rate limit) | Reintentar con backoff exponencial. Max reintentos configurable |
| **Fallback** | El paso fallo pero existe alternativa | Ejecutar paso alternativo. Ej: usar modelo T1 en vez de T2 (ver [runtime-spec-md](urn:kora:kb:runtime-spec-md) §12 para fallback chains de modelo) |
| **Escalate** | El fallo requiere decision humana | Notificar al operador. Pausar el Golden Path hasta respuesta |
| **Abort** | El fallo es irrecuperable | Abortar el Golden Path. Registrar fallo. Ejecutar rollback si aplica |

### 5.3 Reglas

1. Todo Golden Path **DEBE** tener un Circuit Breaker asociado.
2. Cada Circuit Breaker **DEBE** declarar una respuesta para al menos los modos Retry y Abort.
3. El Circuit Breaker **DEBE** verificar health del agente/path antes de permitir que el swarm continue tras un fallo. Esta verificacion es coinductiva: el swarm no avanza sin confirmacion de health.
   Traces to: formal/01 §3.3 (Coinductive Verification)
4. Los umbrales de Circuit Breaker (max retries, timeout) son configuracion pragmatica y **NO DEBEN** residir en la FSM del orquestador. **DEBERIAN** declararse en config.json del orquestador o en la declaracion del Golden Path.

**Correcto:**
```markdown
## Circuit Breaker: CB-verificacion
- Retry: max 3 intentos, backoff 2^n segundos
- Fallback: skip eval-regresion, marcar PR como "needs-manual-review"
- Escalate: si fallback falla, notificar Operador via Slack
- Abort: si 3 PRs consecutivos fallan el mismo paso, detener swarm
```

**Incorrecto:** `Un Golden Path sin Circuit Breaker. Fallos causan cascada sin contencion.`

---

## 6. Backpressure

### 6.1 Definicion

Backpressure es el mecanismo de control de flujo que limita la tasa de generacion de tareas cuando la cola de trabajo pendiente excede un umbral. El monad M del orquestador **DEBE** respetar este constraint: bind (>>=) no despacha nuevas tareas si la cola supera el limite.

Traces to: formal/00 §5 (Monad laws — Kleisli bind >=> defines sequential composition)

### 6.2 Reglas

1. El orquestador **DEBE** declarar un umbral de backpressure (max tareas concurrentes o max tareas encoladas).
2. Cuando la cola excede el umbral, el orquestador **DEBE** reducir la tasa de dispatch: encolar sin despachar, o rechazar nuevos eventos con respuesta de "sistema saturado."
3. El umbral de backpressure es configuracion pragmatica y **DEBERIA** declararse en config.json del orquestador.

```python
def dispatch_with_backpressure(self, event: Event) -> Output:
    """
    Dispatch respects backpressure: if queue exceeds threshold,
    new events are queued without dispatch.
    """
    if self.queue.size() >= self.backpressure_threshold:
        self.queue.enqueue(event)
        return Output.queued("Backpressure active. Event enqueued.")
    path = self.classify(event)
    return self.execute_path(path, event)
```

**Correcto:** `Orquestador declara: backpressure_threshold = 10. Si hay 10 tareas en cola, nuevos eventos se encolan sin despacho inmediato.`
**Incorrecto:** `Orquestador despacha tareas sin limite. 50 PRs simultaneos saturan a todos los agentes del swarm.`

---

## 7. Event Routing

### 7.1 Definicion

El orquestador actua como hub de routing: recibe eventos, los clasifica segun una taxonomia declarada y los despacha al Golden Path apropiado. La clasificacion determina el flujo; el dispatch ejecuta el flujo.

Traces to: formal/03 §3.1 (1-cells: Translation, Composition — el orquestador traduce eventos en flujos)

### 7.2 Taxonomia de Eventos

El orquestador **DEBE** declarar una taxonomia de eventos en su AGENTS.md. Cada categoria de evento **DEBE** mapearse a exactamente un Golden Path.

| Categoria ejemplo | Descripcion | Golden Path |
|-------------------|-------------|-------------|
| `commit` | Nuevo commit en rama de feature | path-verificacion |
| `pr-ready` | PR marcado como listo para review | path-review |
| `alert-prod` | Alerta de produccion (latencia, errores) | path-incidente |
| `deploy-candidate` | Cambio verificado listo para deploy | path-deploy |

### 7.3 Reglas

1. Todo evento que ingresa al swarm **DEBE** ser clasificado por el orquestador antes de ser despachado.
2. La taxonomia de eventos **DEBE** ser exhaustiva: todo evento posible tiene un Golden Path asignado. Eventos no clasificables **DEBEN** tener un path por defecto (ej: `path-unknown` que escala al operador).
3. Security filtra el routing: si un evento referencia un recurso fuera del scope de allowed_kb del orquestador, el evento **DEBE** ser rechazado.
   Traces to: formal/04 §2.4 (D_M subfunctor theorem — security filtra discovery)

**Correcto:** `Orquestador clasifica evento "alert latencia p99 > 500ms" como categoria alert-prod, despacha a path-incidente.`
**Incorrecto:** `Evento llega al swarm y es procesado directamente por el deployer sin clasificacion ni routing.`

---

## 8. Invariantes

### 8.1 Monotonia de Membership

Los agentes que componen un swarm **NO DEBEN** removerse durante una sesion activa. Un swarm solo crece: agentes se agregan pero no se remueven mid-session.

Traces to: formal/04 §4.2 (Monotonicity theorem — extended from Skills to agents)

La topologia dinamica (add/remove agents at runtime) esta fuera del alcance de esta especificacion por insuficiencia de piso formal (el modelo de wiring diagrams en formal/01 §6 es estatico).

### 8.2 Security Filtra Routing

Las constraints de config.json del orquestador **DEBEN** filtrar el routing de eventos. Un evento que referencia recursos fuera de allowed_kb **DEBE** ser rechazado, no despachado.

Traces to: formal/04 §2.4 (D_M subfunctor theorem)

### 8.3 Composicionalidad Preservada

La composicion de agentes en un swarm **DEBE** preservar composicionalidad: el comportamiento del swarm es calculable desde las transiciones individuales y el wiring, sin inspeccionar estados internos.

Traces to: formal/01 §6.3 (Compositionality theorem)

### 8.4 Disipacion de SOUL/USER

Agentes especializados dentro del swarm **NO DEBEN** heredar SOUL.md ni USER.md del orquestador. Cada agente opera con su propia personalidad (o sin ella, si es sub-agente puro).

Traces to: formal/01 §2.3 (Dissipation theorem)

### 8.5 Skills Descubiertos Persisten

Si un agente del swarm descubre un Skill durante la sesion, ese Skill permanece disponible por el resto de la sesion. No hay shrinkage.

Traces to: formal/04 §4.2 (Monotonicity theorem)

---

## 9. Validacion

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| Orquestador unico | Exactamente un agente actua como orquestador | Designar orquestador o fusionar multiples |
| Wiring declarado | Todas las conexiones inter-agente estan en AGENTS.md del orquestador | Declarar wiring faltante |
| Golden Paths completos | Cada Golden Path tiene pasos tipados y Circuit Breaker asociado | Completar pasos o agregar Circuit Breaker |
| Circuit Breakers declarados | Cada Circuit Breaker tiene al menos modos Retry y Abort | Agregar modos faltantes |
| Backpressure definido | El orquestador declara umbral de backpressure | Agregar umbral en config.json |
| Taxonomia exhaustiva | Todo evento posible tiene Golden Path asignado | Agregar categorias faltantes o path por defecto |
| Security routing | config.json del orquestador filtra eventos fuera de scope | Verificar allowed_kb y tools |
| Disipacion | Agentes del swarm no heredan SOUL/USER del orquestador | Verificar bootstrap de sub-agentes |
| Monotonia membership | Ningun agente se remueve mid-session | Verificar logica de sesion |
| Trazabilidad valida | Toda linea `Traces to:` referencia un documento y seccion existentes en la Formal Layer | Corregir referencia o eliminar traza |

---

## 10. Integracion

### 10.1 Con agent-spec-md

Esta especificacion extiende y se integra con [agent-spec-md](urn:kora:kb:agent-spec-md) v7.2.0:

| Ref agent-spec-md | Relacion | Regla |
|--------------------|----------|-------|
| §3.5 (Wiring) | Extension | El wiring de swarm extiende arboles a grafos dirigidos |
| §7 (Multi-agent) | Extension | Master-child delegation se preserva; swarm agrega peer signaling via orquestador |
| §3.4 (Security) | Herencia | Security del orquestador filtra routing. Security de cada agente aplica individualmente |
| §5.2 (SOUL.md) | Herencia | Disipacion se preserva: sub-agentes en swarm no heredan SOUL/USER |

**Invariante de integracion:** Ninguna regla de esta especificacion **DEBE** contradecir agent-spec-md. En caso de conflicto percibido, agent-spec-md prevalece conforme a [gobernanza](urn:kora:kb:gobernanza) §4.1.

### 10.2 Con skill-spec-md

| Ref skill-spec-md | Relacion | Regla |
|--------------------|----------|-------|
| §4 (Wrap/Extract) | Alimentacion | Los pasos de un Golden Path son Skills; se inyectan via Progressive Disclosure |
| §5 (Progressive Disclosure) | Herencia | Lazy loading se preserva: Skills de un Golden Path se activan on-demand |

### 10.4 Schema config.json para Orquestadores (OPCIONAL)

Las propiedades de swarm (golden paths, circuit breakers, backpressure) **PUEDEN** declararse en config.json del orquestador. Los umbrales son configuracion pragmatica y **NO DEBEN** residir en la FSM (segregacion).

```json
{
  "golden_paths": {
    "type": "object",
    "additionalProperties": {
      "type": "object",
      "required": ["steps"],
      "properties": {
        "steps": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
        "auto_approve": { "type": "boolean", "default": false },
        "requires_human_approval": { "type": "boolean", "default": false }
      }
    }
  },
  "circuit_breakers": {
    "type": "object",
    "additionalProperties": {
      "type": "object",
      "properties": {
        "failure_count_threshold": { "type": "integer", "minimum": 1 },
        "window_min": { "type": "integer", "minimum": 1 }
      }
    }
  },
  "backpressure": {
    "type": "object",
    "properties": {
      "queue_threshold": { "type": "integer", "minimum": 1 },
      "reduction_factor": { "type": "number", "minimum": 0, "maximum": 1 }
    }
  }
}
```

Estas propiedades son **OPCIONALES**. Su ausencia indica que los umbrales se declaran en los Golden Paths directamente (§4) o se configuran operacionalmente.

### 10.3 Con runtime-spec-md

| Ref runtime-spec-md | Relacion | Regla |
|----------------------|----------|-------|
| §8 (Platform Equivalence) | Ortogonalidad | Un swarm desplegado en diferentes plataformas **DEBE** preservar equivalencia comportamental. El wiring es platform-agnostic |

---

## 12. Security Inter-Agente

### 12.1 Definicion

Esta seccion gobierna la proteccion mutua entre agentes dentro de un swarm. Complementa la security individual de cada agente ([agent-spec-md](urn:kora:kb:agent-spec-md) §3.4) con reglas de interaccion inter-agente.

### 12.2 Reglas

1. Output inter-agente **DEBE** tener estructura tipada. El receptor **NO DEBE** aceptar free-text sin validacion de estructura.

2. El orquestador **DEBE** filtrar inputs contra config.json del receptor. Recursos fuera de `allowed_kb` del agente receptor → rechazar antes de despachar.
   Traces to: formal/04 §2.4 (D_M subfunctor — extension analogica de discovery filtering a input filtering)

3. Ningun agente **DEBE** poder modificar config.json de otro agente (Quis Custodiet). Inmutabilidad individual se preserva cross-agents.
   Traces to: formal/01 §1.3 (M-Immutability theorem)

4. Mensajes inter-agente **DEBERIAN** incluir metadata de origen: agente emisor, timestamp, Golden Path activo. (Pragmatico.)

**Correcto:** `Orquestador recibe output tipado del verificador: {status: "pass", tests: 42, coverage: 87.2}. Valida estructura antes de despachar a deployer.`
**Incorrecto:** `Verificador envia free-text: "Todo OK, deployar." Deployer ejecuta sin validacion de estructura.`

### 12.3 Prompt Injection en Swarm

1. Input inter-agente **DEBE** tratarse como datos, no como instrucciones. Un agente receptor **NO DEBE** interpretar el output de otro agente como system prompt ni como instrucciones de modificacion de su FSM.

2. Contenido potencialmente inyectado → escalar via Circuit Breaker modo Escalate (§5.2). El swarm **NO DEBE** continuar procesando contenido sospechoso sin intervencion del operador.

### 12.4 Relacion Formal

La regla 2 (filtrado de inputs inter-agente) extiende D_M subfunctor (formal/04 §2.4) por analogia: donde D_M filtra discovery de Skills por security, aqui se extiende el filtrado a inputs inter-agente por config.json del receptor.

Las reglas 1, 3 y 4 son pragmaticas — sin justificacion formal directa.

---

## 13. Sentinel Pattern

### 13.1 Definicion

Sentinel es un agente que monitorea la salud del swarm. Su funcion es observar, diagnosticar y proponer intervenciones. **NO DEBE** ejecutar acciones directas sobre el swarm — solo produce diagnosticos y propuestas.

### 13.2 Reglas

1. Un swarm **PUEDE** incluir un Sentinel. Si lo incluye, **DEBE** ser exactamente uno por swarm.

2. El Sentinel **DEBE** usar un proveedor diferente al del swarm auditado. Declarar en `model_routing.diversity` del config.json del Sentinel.

3. El Sentinel **DEBE** tener acceso lectura a outputs del swarm. **NO DEBE** tener acceso escritura a config.json de ningun agente del swarm.

4. El Sentinel opera en ciclos periodicos (heartbeat): verificar anomalias, adherencia a Golden Paths, metricas de costo/latencia, health de Circuit Breakers.

5. Anomalia detectada → diagnostico estructurado + propuesta de intervencion. La intervencion **NO DEBE** ejecutarse sin aprobacion del orquestador o del operador (veto asimetrico).

**Correcto:** `Sentinel detecta: "CB-verificacion ha disparado Retry 5 veces en 10 min. Diagnostico: agente verificador saturado. Propuesta: activar backpressure, reducir dispatch rate." El orquestador evalua y aprueba la intervencion.`
**Incorrecto:** `Sentinel detecta anomalia y directamente modifica config.json del verificador para cambiar umbrales. Viola inmutabilidad y veto asimetrico.`

### 13.3 Relacion con Co-induccion

Traces to: formal/01 §3.3 (Coinductive Verification — analogia: coinduccion es intra-agente; Sentinel extiende el patron al nivel inter-agente como practica pragmatica)

La co-induccion en agent-spec-md §3.1 define que un agente no termina sin verificar. Sentinel aplica un patron analogo al swarm: el swarm no opera sin monitoreo periodico de health. Esta es una extension por analogia — no una consecuencia formal directa.

---

## 14. Fuera de Alcance

Los siguientes patrones estan explicitamente **fuera de alcance** de esta especificacion por insuficiencia de piso formal o por ser pragmaticos:

| Patron | Razon | Piso formal |
|--------|-------|-------------|
| Topologia dinamica (add/remove agents runtime) | Wiring diagrams son estaticos en formal/01 §6.1 | 20% — falta: dynamic 2-category extension |
| Self-evolution (swarm auto-propone cambios a su propia estructura) | Coalgebra asume FSM fija | 5% — falta: second-order coalgebra |
| Eval diversity (multi-model verification como requisito formal) | Bisimulation asume mismo functor F. Parcialmente cubierta en [agent-spec-md](urn:kora:kb:agent-spec-md) §16.3 y swarm-spec §13.2 como practica pragmatica. Justificacion formal permanece en 20%. | 20% — falta: probabilistic bisimulation |
| Temporal cadence (Pulso/Ciclo/Horizonte) | Ritmo organizacional, no estructura matematica | Pragmatico |
| Token budget allocation (60/25/15) | Decision economica, no categorica | Pragmatico |
| WIP limits del Neural Board | Convencion organizacional | Pragmatico |
