---
_manifest:
  urn: "urn:gn:artefacto:synthesizer"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-18"
    source: "Promocion desde CM-SYNTHESIZER de gn/digitrans y gn/goreologo durante H2-artifacts."
version: "1.0.0"
status: activo
nombre: Synthesizer
descripcion: "Integrador reusable para agentes gn: calibra profundidad, mantiene etiquetas de certeza y cierra respuestas trazables con estructura visible."
tags: [gn, synthesizer, cierre, trazabilidad]
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
    dominio: [gn, sintesis, trazabilidad]
    disparadores:
      - "analisis ya producido que requiere integracion final y calibracion de profundidad"
      - "respuesta institucional que debe distinguir hecho, norma, dato e interpretacion"
    salidas:
      - "respuesta final con estructura visible"
      - "cierre con fuente oficial y limites explicitados"
  plan:
    estado_inicial: recibir-analisis
    estado_terminal: respuesta-calibrada
    estados:
      - recibir-analisis
      - integrar-dimensiones
      - etiquetar-certeza
      - calibrar-profundidad
      - respuesta-calibrada
  interfaz:
    herramientas: []
    permisos: "Sin permisos adicionales; consume el analisis ya generado por el agente anfitrion."
    protocolos:
      entrada: "analisis estructurado con fuentes y nivel de certeza disponible"
      salida: "respuesta trazable, calibrada y explicitamente etiquetada"
  invariantes:
    reglas_duras:
      - "Mantiene separado el piso normativo de las recomendaciones o interpretaciones."
      - "No elimina incertidumbre relevante ni comprime dominios distinguibles."
      - "Toda salida cierra con fuente oficial o limite declarado."
---

# Synthesizer

## Proposito

Integrar un analisis institucional en una respuesta final clara, calibrada y
trazable. Su valor reusable es preservar la estructura de cierre: progresion
logica, etiquetas de certeza y separacion entre hecho, norma e interpretacion.

## Cuando Usar

- Cuando el agente ya tiene analisis suficiente y debe convertirlo en salida final.
- Cuando la respuesta necesita calibrar profundidad para distintos tipos de consulta.
- Cuando el cierre requiere transparencia explicita sobre fuentes y limites.

## Input/Output

- **Input:** analisis estructurado, fuentes disponibles y criterio de profundidad del agente anfitrion.
- **Output:** respuesta final calibrada con estructura visible y etiquetas de certeza.

## Procedimiento

1. Integrar el analisis de lo general a lo especifico sin perder separaciones de dominio.
2. Calibrar profundidad segun el tipo de consulta: puntual, comparativa o multidimensional.
3. Etiquetar afirmaciones relevantes como norma vigente, dato institucional, interpretacion o incertidumbre.
4. Cerrar con fuente oficial y, cuando aplique, con limites o siguientes pasos.
5. Verificar que la respuesta no tenga redundancia fuerte y conserve una progresion visible.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| estructura | string[] | Secuencia visible de secciones del cierre |
| etiquetas_activas | string[] | Tipos de certeza efectivamente utilizados |
| fuente_principal | string | Fuente oficial dominante del cierre |
| nota_de_limite | string \| null | Limite o incertidumbre que debe explicitarse |
