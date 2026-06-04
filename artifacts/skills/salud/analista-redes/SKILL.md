---
_manifest:
  urn: urn:salud:artefacto:analista-redes
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-05-08'
    source: Portado de skill del agente salubrista-hah (OpenClaw).
version: 1.0.1
status: activo
nombre: analista-redes
descripcion: Analiza o disena unidades, establecimientos, redes, modelos territoriales,
  flujos, capacidad, accesibilidad y gobernanza en sistemas de salud.
tags:
- salud
- analista-redes
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
    - opencode
    - openclaw
    conocimiento_permitido:
    - urn:salud:kb:salubrista
    - urn:salud:kb:gestion-redes-general
    - urn:salud:kb:gestion-redes-unidades
    - urn:salud:kb:gestion-redes-urgencias
    - urn:salud:kb:health-systems-science-operativa
    - urn:salud:kb:management-engineering-ext-capacidad
    componible_con:
    - urn:salud:artefacto:salubrista
artefacto:
  perfil:
    dominio:
    - analista-redes
    disparadores:
    - solicitud de analista-redes
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

# Analista de Redes

## Proposito

Analizar o disenar redes asistenciales. Dos modos: analysis (mapear) y design (arquitectura).

## Workflow

### posicionar-escala
Determinar: unidad, establecimiento, red, territorio.

### mapear
Mapear demanda, oferta, capacidad, flujos, cuellos de botella, brechas.

### disenar
Definir arquitectura: nodos, roles, complejidad, derivacion, gobernanza.

### recomendar
Proponer con KPIs. Tradeoffs explicitos: eficiencia vs equidad vs resiliencia.
