---
_manifest:
  urn: urn:kora:artefacto:intent-classifier
  type: artefacto
  provenance:
    created_by: OpenAI Codex
    created_at: '2026-04-18'
    source: Promocion del patron comun de CM-INTENT-CLASSIFIER en agentes productivos
      kora durante H2-artifacts.
version: 1.0.0
status: retirado
nombre: Intent Classifier
descripcion: 'Clasificador reusable de intencion para agentes KORA: ubica la solicitud
  en la capacidad correcta del dominio y distingue modo guiado/libre cuando aplica.'
tags:
- kora
- intent
- clasificacion
- dispatch
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 1
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma:
      - 1
      - 1
      - 2
      - 1
      - 0
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    nivel_prescripcion: medio
    rebuild:
      required: true
      current_is_source: false
      directive: urn:kora:kb:meta-kora-rebuild-directive
    conocimiento_permitido:
    - urn:kora:kb:meta-kora-rebuild-directive
    - urn:kora:kb:autoria-spec
    - urn:kora:kb:catalogo-patrones-skills
    componible_con:
    - urn:kora:artefacto:clawforge
    - urn:kora:artefacto:artifact-curator
    - urn:kora:artefacto:custodio
    - urn:kora:artefacto:kora-agents
    - urn:kora:artefacto:kora-skills
artefacto:
  perfil:
    dominio:
    - kora
    - dispatch
    - intent
    disparadores:
    - el agente necesita ubicar una solicitud en una capacidad del dominio
    - el modo guiado o libre condiciona la fase inicial
    salidas:
    - clasificacion de capacidad
    - senal de modo y confianza
  plan:
    estado_inicial: leer-solicitud
    estado_terminal: intent-clasificado
    estados:
    - leer-solicitud
    - identificar-capacidad
    - medir-confianza
    - intent-clasificado
  interfaz:
    herramientas: []
    permisos: Sin permisos adicionales; consume solicitud, foco previo y taxonomia
      local del agente anfitrion.
    protocolos:
      entrada: solicitud del usuario + taxonomia de capacidades del agente anfitrion
      salida: clasificacion de capacidad, modo y cierre solicitado
  invariantes:
    reglas_duras:
    - Clasifica dentro del dominio del agente anfitrion; no ejecuta acciones.
    - Explicita confianza y ambiguedad antes de forzar routing.
    - Distingue cierre solicitado cuando el usuario no busca mas trabajo.
---

# Intent Classifier

## Proposito

Clasificar una solicitud en la capacidad correcta del dominio del agente
anfitrion, distinguiendo tambien modo guiado/libre, continuidad y confianza.

## Cuando Usar

- Cuando el agente tiene varias capacidades mutuamente excluyentes.
- Cuando el primer paso depende de si la solicitud es guiada o directa.
- Cuando una clasificacion ambigua debe visibilizarse antes de actuar.

## Input/Output

- **Input:** solicitud del usuario, foco previo, taxonomia de capacidades y reglas locales.
- **Output:** clasificacion de capacidad y metadatos de despacho.

## Procedimiento

1. Analizar la solicitud y extraer artefactos, dominios y verbos operativos.
2. Proyectar la solicitud sobre la taxonomia local del agente anfitrion.
3. Determinar si la operacion es guiada, libre o requiere aclaracion.
4. Emitir la clasificacion con confianza y cierre solicitado.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | string | Capacidad clasificada en la taxonomia del agente anfitrion |
| modo | string \| null | GUIADO, LIBRE u otra variante local si aplica |
| continuidad | string \| null | Relacion semantica con el foco previo |
| confianza | enum(alta\|media\|baja) | Nivel de confianza de la clasificacion |
| cierre_solicitado | bool | True si el mensaje indica cierre del trabajo actual |
