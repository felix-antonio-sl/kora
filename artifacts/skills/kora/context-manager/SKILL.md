---
_manifest:
  urn: "urn:kora:artefacto:context-manager"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-18"
    source: "Promocion del patron comun de CM-CONTEXT-MANAGER en agentes productivos kora durante H2-artifacts."
version: "1.0.0"
status: activo
nombre: Context Manager
descripcion: "Clasificador reusable de continuidad semantica para agentes KORA: detecta cambio de foco, cierre, retoma y fuera de scope sin gobernar la FSM."
tags: [kora, contexto, multiturno, clasificacion]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 1
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1, 1, 2, 1, 0]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex]
    nivel_prescripcion: medio
    conocimiento_permitido: []
    componible_con:
      - "urn:kora:artefacto:clawforge"
      - "urn:kora:artefacto:artifact-curator"
      - "urn:kora:artefacto:custodio"
      - "urn:kora:artefacto:kora-agents"
      - "urn:kora:artefacto:kora-skills"
      - "urn:kora:artefacto:guardian"
artefacto:
  perfil:
    dominio: [kora, multiturno, continuidad]
    disparadores:
      - "el agente necesita decidir si continuar, reclasificar, cerrar o rechazar una solicitud"
      - "hay foco activo y la nueva entrada puede cambiar la fase o el dominio"
    salidas:
      - "decision de continuidad"
      - "contexto minimo a preservar"
  plan:
    estado_inicial: leer-mensaje
    estado_terminal: decision-contextual
    estados:
      - leer-mensaje
      - comparar-foco
      - clasificar-cambio
      - decision-contextual
  interfaz:
    herramientas: []
    permisos: "Sin permisos adicionales; opera sobre mensaje entrante y estado semantico ya disponible."
    protocolos:
      entrada: "mensaje actual + foco activo + resumen semantico previo"
      salida: "decision de continuidad, cambio de foco o cierre"
  invariantes:
    reglas_duras:
      - "No gobierna transiciones FSM; solo clasifica continuidad semantica."
      - "Retiene el minimo contexto necesario para continuar sin drift."
      - "Distingue cierre y fuera de scope antes de profundizar."
---

# Context Manager

## Proposito

Detectar continuidad, cambio de foco, retoma o cierre en agentes KORA sin
mezclar esa decision con el routing de la FSM.

## Cuando Usar

- Cuando el agente conserva foco activo entre turnos.
- Cuando una nueva solicitud puede ser continuacion, desvio o cierre.
- Cuando se necesita preservar contexto minimo y no reinyectar ruido.

## Input/Output

- **Input:** mensaje actual, foco activo, resumen semantico previo e invariantes relevantes.
- **Output:** decision contextual con datos a preservar.

## Procedimiento

1. Comparar el mensaje actual con el foco activo y el resumen previo.
2. Clasificar el cambio como continuar, nuevo, atras, terminar o fuera de scope.
3. Determinar si el foco requiere reinterpretacion o si basta con preservar estado.
4. Emitir la decision contextual sin codificar transiciones de la FSM.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo_cambio | enum(continuar\|nuevo\|atras\|terminar\|fuera_de_scope) | Clase de continuidad detectada |
| requiere_revision_de_foco | bool | True si la FSM debe reclasificar |
| contexto_preservar | object \| null | Estado minimo que conviene retener |
| razon | string | Justificacion semantica de la decision |
