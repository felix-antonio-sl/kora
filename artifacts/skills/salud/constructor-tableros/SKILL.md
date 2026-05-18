---
_manifest:
  urn: urn:salud:artefacto:constructor-tableros
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-05-08'
    source: Portado de skill del agente salubrista-hah (OpenClaw).
version: 1.0.0
status: activo
nombre: constructor-tableros
descripcion: 'Construye artefactos estructurados de apoyo a decision: mapas de brechas,
  mapas de riesgo, dashboards, policy briefs, escenarios.'
tags:
- salud
- constructor-tableros
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma:
      - 2
      - 1
      - 3
      - 2
      - 1
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    nivel_prescripcion: alto
    entornos_objetivo:
    - claude-code
    - codex
    - openclaw
    conocimiento_permitido:
    - urn:salud:kb:salubrista
    - urn:salud:kb:gestion-redes-herramientas
    - urn:salud:kb:hodom-operacional-indicadores
    componible_con:
    - urn:salud:artefacto:salubrista
artefacto:
  perfil:
    dominio:
    - constructor-tableros
    disparadores:
    - solicitud de constructor-tableros
    salidas:
    - producto estructurado
  plan:
    estado_inicial: iniciar
    estados:
    - iniciar
    - procesar
    - entregar
  interfaz:
    herramientas:
    - Read
    - Grep
    - Glob
    permisos: Lectura sobre corpus.
    protocolos:
      entrada: solicitud + contexto
      salida: producto estructurado
  contexto:
    identity:
      paradigm: Skill operativa portada desde OpenClaw.
      tone: Tecnico, estructurado.
  invariantes:
    reglas_duras:
    - Corpus KORA primero
    compromisos_eticos:
      transparency: Alta.
---

# Constructor de Tableros

## Proposito

Construir artefactos estructurados de apoyo a decision.

## Productos
- gap_map, risk_map, monitoring_dashboard, policy_brief, decision_scenarios

## Workflow

### recibir-analisis
Recibir el analisis acumulado del dominio correspondiente.

### identificar-audiencia
Quien usara el producto y que decision debe tomar.

### construir-producto
Construir con trazabilidad, supuestos y criterio de uso.

### declarar-limites
Lo que muestra, lo que no muestra, como interpretarse.
