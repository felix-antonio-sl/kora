---
_manifest:
  urn: "urn:kora:artefacto:lifecycle-orchestrator"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-18"
    source: "Promocion del patron comun de CM-LIFECYCLE-ORCHESTRATOR en agentes productivos kora durante H2-artifacts."
version: "1.0.0"
status: activo
nombre: Lifecycle Orchestrator
descripcion: "Consolidador reusable de checkpoints guiados para agentes KORA: resume fases, entregables y pendientes sin secuenciar la FSM."
tags: [kora, guided, lifecycle, checkpoints]
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
      - "urn:kora:artefacto:kora-agents"
      - "urn:kora:artefacto:kora-skills"
artefacto:
  perfil:
    dominio: [kora, guided, checkpoints]
    disparadores:
      - "el agente opera en modo guiado y necesita consolidar checkpoints"
      - "hay varias fases parciales con entregables y pendientes"
    salidas:
      - "resumen acumulado de ciclo guiado"
      - "pendientes visibles para la siguiente fase"
  plan:
    estado_inicial: recibir-checkpoint
    estado_terminal: resumen-guiado
    estados:
      - recibir-checkpoint
      - normalizar-fase
      - consolidar-pendientes
      - resumen-guiado
  interfaz:
    herramientas: []
    permisos: "Sin permisos adicionales; opera sobre checkpoints y entregables ya producidos."
    protocolos:
      entrada: "fase actual + entregables + observaciones + pendientes"
      salida: "resumen consolidado del ciclo guiado"
  invariantes:
    reglas_duras:
      - "No gobierna transiciones ni secuencia la FSM."
      - "Resume checkpoints existentes; no inventa entregables."
      - "Mantiene visibles pendientes y riesgos acumulados."
---

# Lifecycle Orchestrator

## Proposito

Consolidar checkpoints de un ciclo guiado en un resumen operativo reutilizable,
sin absorber el control de la FSM del agente anfitrion.

## Cuando Usar

- Cuando el agente opera en modo guiado por fases.
- Cuando hay entregables parciales y se requiere continuidad entre ellas.
- Cuando conviene separar control secuencial de consolidacion de evidencia.

## Input/Output

- **Input:** fase actual, checkpoints previos, entregables, observaciones y pendientes.
- **Output:** resumen acumulado del ciclo guiado.

## Procedimiento

1. Recibir la fase actual y sus entregables visibles.
2. Normalizar el checkpoint para que sea comparable con fases previas.
3. Consolidar entregables, riesgos y pendientes acumulados.
4. Emitir un resumen que permita continuar el ciclo sin gobernarlo.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| fase_activa | string | Fase actualmente consolidada |
| fases_registradas | string[] | Fases con checkpoint disponible |
| pendientes | string[] | Pendientes visibles para continuar |
| observaciones | string[] | Notas o riesgos relevantes del ciclo |
