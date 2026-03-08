---
_manifest:
  urn: "urn:kora:kb:swarm-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 03, KORA/Runtime-Spec v3.0.0"
version: "2.0.0"
status: published
tags: [spec, swarm, orchestration, events, safety]
lang: es
---

# KORA/Swarm-Spec v2.0.0

## 1. Definicion

Un swarm KORA es una composición tipada de agentes coordinados por eventos, rutas y gates de seguridad.

## 2. Objetos del swarm

- orquestador
- agentes especializados
- eventos
- rutas
- gates
- golden paths

## 3. Reglas

1. Toda delegación **DEBE** apuntar a un agente resoluble.
2. Todo evento **DEBE** tener tipo explícito.
3. Toda acción destructiva **DEBE** pasar por gate humano.
4. Backpressure y circuit breakers **DEBEN** expresarse como políticas operativas verificables.
5. Analogías o extensiones no estrictas **NO DEBEN** presentarse como `Traces to:`; van en `Rationale:`.

## 4. Golden paths

Un golden path es una composición operacional canónica para una clase de evento. Debe declarar:

- trigger
- secuencia
- gates
- criterio de abort
- criterio de éxito

## 5. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Rutas resolubles | Toda delegación apunta a workspace existente | lint | Corregir wiring |
| Eventos tipados | Todo evento tiene tipo y payload esperable | lint | Tipar evento |
| Gates destructivos | Toda operación destructiva pasa por gate humano | runtime | Añadir gate |
| Politicas verificables | Backpressure/circuit breakers no son solo prosa | runtime | Materializar policy |
