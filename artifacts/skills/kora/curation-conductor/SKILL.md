---
_manifest:
  urn: "urn:kora:artefacto:curation-conductor"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-23"
    source: "Skill conductora del proceso de curación de artefactos de conocimiento KORA de comienzo a fin."
version: "1.0.0"
status: activo
nombre: Curation Conductor
descripcion: "Determina y acompaña el proceso de curación de artefactos de conocimiento KORA de comienzo a fin: clasifica input, elige familia, funtor, staging, productor, validaciones y readiness de promote."
tags: [curation, knowledge, pipeline, kora, review, promote]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma: [2, 2, 3, 2, 1]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex]
    nivel_prescripcion: alto
    conocimiento_permitido:
      - "urn:kora:kb:gobernanza"
      - "urn:kora:kb:harness-spec"
      - "urn:kora:kb:autoria-spec"
      - "urn:kora:kb:md-spec"
      - "urn:kora:kb:knowledge-spec"
      - "urn:kora:kb:pipeline-ingesta"
    componible_con:
      - "urn:kora:artefacto:atomize"
      - "urn:kora:artefacto:knowledge-curator"
      - "urn:kora:artefacto:intent-classifier"
      - "urn:kora:artefacto:lifecycle-orchestrator"
artefacto:
  perfil:
    dominio: [knowledge-curation, family-selection, pipeline-orchestration]
    disparadores:
      - "ingreso de nueva fuente a KORA"
      - "duda sobre si corresponde KB normal, atomic o reroute a spec"
      - "necesidad de conducir la curación hasta review o promote"
      - "repair o publicación de artefacto de conocimiento existente"
    salidas:
      - "diagnóstico de curación"
      - "ruta de proceso elegida"
      - "outcome operativo final"
      - "bloqueos y siguiente paso"
  plan:
    estado_inicial: diagnosticar-input
    estado_terminal: outcome-operativo-declarado
    estados:
      - diagnosticar-input
      - validar-scope-knowledge
      - elegir-familia
      - elegir-funtor
      - decidir-staging
      - ejecutar-o-acompanar
      - validar-gates
      - outcome-operativo-declarado
  interfaz:
    herramientas: [Read, Write, Glob, Grep, Bash]
    permisos: "Lectura/escritura sobre staging de knowledge y ejecución controlada de toolchain KORA."
    protocolos:
      entrada: "fuente o artefacto + intención de curación"
      salida: "diagnóstico de proceso, acciones ejecutadas y outcome operativo final"
  invariantes:
    reglas_duras:
      - "No usar `atomic` como curación universal."
      - "No publicar sin pasar por `REVIEW`."
      - "No reemplazar `atomize`, `promote` ni `validation`; coordinarlos."
      - "No tratar inputs prescriptivos/fundacionales como knowledge publicado; rerutearlos al circuito `spec`."
      - "No tratar `docs/generated/*` como fuente de verdad."
      - "Declarar siempre la razón de la familia elegida."
      - "Declarar siempre si el outcome operativo quedó `pending`, `processing`, `ready_to_promote`, `published`, `needs_repair` o `rerouted_to_spec`."
---

# Curation Conductor

## Proposito

Conducir la curación de artefactos de conocimiento KORA de comienzo a fin sin
confundir productor, pipeline y publicación. Esta skill decide el proceso
correcto dentro del pipeline de `artifacts/knowledge/` y, si detecta material
prescriptivo o fundacional, lo deriva explícitamente fuera de ese pipeline en
lugar de curarlo como knowledge publicado.

## Cuando Usar

- cuando entra una fuente nueva y hay que decidir cómo curarla
- cuando no está claro si corresponde `KB normal`, `atomic` o reroute a `spec`
- cuando un draft está en `_SCRIPTORIUM/REVIEW` y hay que validar readiness
- cuando un artefacto publicado requiere repair o mejora antes de re-promover

## Workflow

1. Diagnosticar el input:
   - crudo
   - curado parcial
   - draft existente
   - publicado con necesidad de repair
2. Validar scope:
   - si el material es descriptivo y pertenece al pipeline de knowledge -> continuar
   - si el material es prescriptivo, fundacional o de gobierno -> `rerouted_to_spec`
3. Determinar:
   - descriptivo vs prescriptivo
   - familia documental descriptiva (`KB normal` o `atomic`)
   - funtor aplicable (`F` koraficación)
4. Determinar staging:
   - `INBOX`
   - `REVIEW`
   - repair sobre publicado
5. Elegir productor o ruta:
   - `atomic` -> usar `atomize`
   - `KB normal` -> usar `knowledge-curator`
6. Ejecutar o acompañar el tramo correspondiente.
7. Correr validaciones y gates.
8. Declarar outcome operativo y siguiente paso.

## Reglas Duras

- `atomic` solo cuando la granularidad proposicional sea parte real del objetivo.
- `atomize` es una ruta especializada, no el curador universal.
- `promote` solo cuando el artefacto ya pasó las validaciones aplicables.
- si el input deriva a `spec`, no forzarlo dentro de `artifacts/knowledge/`.
- No mezclar la clasificación del artefacto con la decisión de publicarlo.
- Si el outcome queda ambiguo, declarar `needs_repair` en vez de sobreafirmar readiness.

## Recursos

### Referencias

- `referencias/process-map.md`
- `referencias/family-decision-table.md`

## Salida Esperada

- diagnóstico del input
- veredicto de scope (`knowledge` o `reroute`)
- familia elegida
- funtor elegido
- staging elegido
- productor o ruta elegida
- validaciones aplicadas
- outcome operativo final
- bloqueos y siguiente paso
