---
_manifest:
  urn: "urn:kora:kb:swarm-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 01, 02, 03, 04, 07, repair of orchestration contract"
version: "2.2.0"
status: published
tags: [spec, swarm, orchestration, golden-path, circuit-breaker, backpressure]
lang: es
---

# KORA/Swarm-Spec v2.2.0

## 1. Definicion

Un swarm KORA es una composicion tipada de agentes coordinados por eventos, rutas, gates y politicas de resiliencia.

### 1.1 Alcance

Esta especificacion gobierna:

1. composicion multi-agente
2. golden paths
3. circuit breakers
4. backpressure
5. event routing
6. seguridad inter-agente
7. sentinel pattern

### 1.2 Dominios ortogonales

`swarm-spec-md` gobierna coordinacion. `runtime-spec-md` gobierna transporte y despliegue. Son dominios relacionados pero distintos.

## 2. Definiciones

| Termino         | Definicion                                                      |
| --------------- | --------------------------------------------------------------- |
| Swarm           | Sistema multi-agente coordinado por un orquestador              |
| Orquestador     | Hub de clasificacion y dispatch                                 |
| Golden Path     | Pipeline operacional canonico para una clase de evento          |
| Circuit Breaker | Mecanismo de contencion ante fallo                              |
| Backpressure    | Control de flujo ante saturacion                                |
| Event Taxonomy  | Clasificacion declarada de eventos y su path                    |
| Sentinel        | Agente observador que diagnostica sin ejecutar cambios directos |

## 3. Modelo de composicion

Todo swarm **DEBE** tener:

1. exactamente un orquestador
2. uno o mas agentes especializados
3. wiring declarado
4. criterio explicito de gates y abort

Traces to: formal/01 §6.2 (Sub-Agent Adjunction) ; formal/01 §6.3 (Compositionality of Wiring)

### 3.1 Reglas de composicion

1. Toda delegacion **DEBE** apuntar a un agente resoluble.
2. El comportamiento del swarm **DEBE** poder razonarse desde agentes + wiring.
3. Los agentes especializados **NO DEBEN** heredar `SOUL.md` ni `USER.md` del orquestador salvo declaracion superior explicita.
4. Las politicas de resiliencia **NO DEBEN** ocultarse dentro de una FSM informal.
5. El wiring del swarm se materializa en el `AGENTS.md` del orquestador. `agent-spec-md` §8 gobierna la topologia de cada agente participante; esta spec gobierna la coordinacion.

## 4. Golden Paths

Un golden path es la composicion operacional canonica para un tipo de evento.

Todo golden path **DEBE** declarar:

1. trigger
2. secuencia de pasos o agentes
3. gates
4. criterio de abort
5. criterio de exito

Traces to: formal/02 §6.1 (Sequential Composition)

### 4.1 Reglas

1. Cada paso **DEBE** tener input/output compatible con el siguiente.
2. Todo golden path **DEBE** tener Circuit Breaker asociado.
3. Los pasos **PUEDEN** activarse via Skills o agentes especializados, pero la composicion **DEBE** quedar declarada.

Correcto:

```markdown
### Golden Path: Intake de documento

- **Trigger:** evento `doc.submitted`
- **Secuencia:** `S-CLASSIFY` (clasificador) -> `S-EXTRACT` (extractor) -> `S-VALIDATE` (validador)
- **Gates:** clasificacion exitosa, extraccion completa
- **Abort:** documento corrupto o tipo no soportado
- **Exito:** artefacto KORA/MD generado y registrado en catalogo
- **Circuit Breaker:** Retry x2 en extraccion; Escalate si falla clasificacion
```

Incorrecto:

```markdown
### Intake

Se recibe el documento y se procesa.
```

Rationale: Sin trigger, secuencia, gates, abort ni exito declarados, el golden path es prosa aspiracional no verificable.

## 5. Circuit Breakers

Todo swarm operativo **DEBE** materializar respuestas para, al menos:

- `Retry`
- `Fallback`
- `Escalate`
- `Abort`

### 5.1 Reglas

1. Todo path **DEBE** tener un Circuit Breaker asociado.
2. Los umbrales de retry, timeout o saturacion **DEBERIAN** vivir en config operativa, no en la FSM textual.
3. Tras un fallo, el swarm **NO DEBE** continuar sin una verificacion de health suficiente.

Traces to: formal/01 §3.3 (Co-induction at Terminal States)

## 6. Backpressure

Backpressure es el control de flujo que reduce o encola trabajo cuando la cola supera un umbral operativo.

### 6.1 Reglas

1. El orquestador **DEBE** declarar un umbral de backpressure verificable.
2. Cuando se supera el umbral, el dispatch **DEBE** reducirse, encolarse o rechazarse explicitamente.
3. Backpressure **NO DEBE** quedar como prosa aspiracional sin politica verificable.

## 7. Event Routing

El orquestador clasifica eventos y los despacha al golden path apropiado.

Traces to: formal/03 §3.1 (Classification)

### 7.1 Taxonomia de eventos

Todo swarm **DEBE** declarar:

1. tipos de evento
2. path por defecto o escalamiento
3. filtros de seguridad previos al dispatch

### 7.2 Reglas

1. Ningun evento **DEBE** saltarse la clasificacion.
2. La taxonomia **DEBE** ser exhaustiva o tener fallback explicito.
3. Security **DEBE** filtrar eventos fuera de scope antes del dispatch.

Traces to: formal/04 §2.4 (Filtered Discovery)

## 8. Invariantes

1. `SOUL.md` y `USER.md` del orquestador se disipan en sub-agentes.
2. El wiring del swarm **DEBE** seguir siendo razonable sin inspeccionar estados ocultos.
3. Un agente del swarm **NO DEBE** modificar `config.json` de otro agente.
4. La composicion de paths **NO DEBE** romper las interfaces efectivas declaradas.

Traces to: formal/01 §2.3 (Context Asymmetry in Sub-Agents) ; formal/07 §4.2 (Compositional Preservation)

## 9. Security inter-agente

1. El output inter-agente **DEBE** tratarse como datos estructurados, no como instrucciones rectoras.
2. El orquestador **DEBE** filtrar inputs contra el scope del receptor.
3. Contenido sospechoso de prompt injection **DEBE** escalarse por Circuit Breaker y no continuar automaticamente.
4. Los mensajes inter-agente **DEBERIAN** incluir metadata minima de origen y contexto.

Traces to: formal/04 §2.4 (Filtered Discovery) ; formal/01 §1.3 (Effect Monad M)

## 10. Sentinel pattern

Un Sentinel es un agente observador del swarm.

Reglas:

1. **PUEDE** existir como maximo uno por swarm.
2. **NO DEBE** ejecutar acciones destructivas directas.
3. **DEBE** producir diagnostico estructurado y propuesta de intervencion.
4. **DEBERIA** operar con diversidad de provider respecto del swarm auditado.

## 11. Validacion

| Check                   | Criterio                                            | Enforcement | Accion si falla       |
| ----------------------- | --------------------------------------------------- | ----------- | --------------------- |
| Orquestador unico       | Existe exactamente un hub de routing                | manual      | Reestructurar swarm   |
| Rutas resolubles        | Toda delegacion apunta a workspace existente        | lint        | Corregir wiring       |
| Golden paths completos  | Trigger, secuencia, gates, abort y exito declarados | manual      | Completar declaracion |
| Circuit Breakers reales | Hay politicas verificables, no solo prosa           | runtime     | Materializar policy   |
| Backpressure            | Existe umbral o politica operativa verificable      | runtime     | Declarar policy       |
| Eventos tipados         | Cada evento tiene clase y path                      | lint        | Tipar evento          |
| Security inter-agente   | Inputs se filtran y estructuran                     | runtime     | Endurecer gateway     |
| Dissipation             | `SOUL.md` / `USER.md` no se heredan indebidamente   | runtime     | Corregir bootstrap    |
