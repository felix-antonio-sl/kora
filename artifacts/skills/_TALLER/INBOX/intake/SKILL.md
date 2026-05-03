---
_manifest:
  urn: "urn:gn:artefacto:intake"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-18"
    source: "Promocion desde CM-INTAKE de gn/digitrans y gn/goreologo durante H2-artifacts."
version: "1.0.0"
status: activo
nombre: Intake
descripcion: "Clasificador inicial reusable para agentes gn: posiciona una consulta, detecta alcance, complejidad y criterio de cierre antes del analisis de dominio."
tags: [gn, intake, clasificacion, triage]
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
      - "urn:gn:artefacto:digitrans"
      - "urn:gn:artefacto:goreologo"
artefacto:
  perfil:
    dominio: [gn, triage, clasificacion]
    disparadores:
      - "consulta entrante que requiere ubicar dominio, alcance o profundidad antes del analisis"
      - "agente gn necesita decidir si responde, deriva o pide aclaracion"
    salidas:
      - "clasificacion estructurada de la consulta"
      - "senal de cierre, ambiguedad o fuera de scope"
  plan:
    estado_inicial: leer-consulta
    estado_terminal: clasificacion-emitiida
    estados:
      - leer-consulta
      - identificar-dominio
      - medir-complejidad
      - declarar-alcance
      - clasificacion-emitiida
  interfaz:
    herramientas: []
    permisos: "Sin permisos adicionales; opera sobre el mensaje ya disponible en el agente anfitrion."
    protocolos:
      entrada: "consulta del usuario + taxonomia de dominios del agente anfitrion"
      salida: "clasificacion estructurada con dominio, alcance, complejidad y cierre solicitado"
  invariantes:
    reglas_duras:
      - "Clasifica sin ejecutar routing irreversible ni producir respuesta sustantiva."
      - "Distingue cierre, ambiguedad y fuera de scope antes de profundizar."
      - "No mezcla clasificacion del problema con recomendacion final."
---

# Intake

## Proposito

Clasificar consultas entrantes para agentes del namespace `gn` antes del
analisis especializado. Factoriza un problema comun: identificar dominio,
alcance, complejidad y condicion de cierre con una salida neutral y reusable.

## Cuando Usar

- Cuando una consulta puede caer en varios dominios institucionales.
- Cuando el agente necesita decidir entre responder, derivar o pedir precision.
- Cuando la profundidad o el alcance condicionan la FSM posterior.

## Input/Output

- **Input:** consulta del usuario, taxonomia de dominios del agente anfitrion, reglas de alcance local.
- **Output:** clasificacion estructurada para despacho inicial.

## Procedimiento

1. Extraer el tema central y los posibles dominios institucionales implicados.
2. Medir la complejidad requerida: puntual, multidimensional o ambigua.
3. Declarar el alcance: dominio unico, cruce de dominios, fuera de scope o cierre solicitado.
4. Identificar etiquetas que la respuesta posterior debe distinguir con claridad, por ejemplo norma, dato institucional, interpretacion o incertidumbre.
5. Emitir una clasificacion neutral que pueda ser consumida por la FSM del agente anfitrion.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| dominio_principal | string | Dominio institucional dominante detectado |
| dominios_involucrados | string[] | Dominios implicados en la consulta |
| complejidad | enum(puntual\|multidimensional\|ambigua) | Complejidad de analisis requerida |
| alcance | enum(single_domain\|cross_domain\|fuera_scope\|cierre) | Posicion de la consulta para despacho |
| etiquetas_requeridas | string[] | Distinciones que la respuesta posterior debe preservar |
