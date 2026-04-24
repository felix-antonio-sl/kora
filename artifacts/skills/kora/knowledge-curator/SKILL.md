---
_manifest:
  urn: "urn:kora:artefacto:knowledge-curator"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-23"
    source: "Skill ejecutora para la curacion descriptiva de artefactos de conocimiento KORA; implementa la ruta KB normal orquestada por curation-conductor y por el agente curator."
version: "1.0.0"
status: activo
nombre: Knowledge Curator
descripcion: "Implementa la ruta descriptiva KB normal del pipeline de knowledge KORA: diseña draft, korafica o repara, audita y deja un artefacto en REVIEW con outcome operativo explicito."
tags: [knowledge, curator, koraficacion, review, audit, repair]
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
      - "urn:kora:artefacto:curation-conductor"
      - "urn:kora:artefacto:atomize"
      - "urn:kora:artefacto:lifecycle-orchestrator"
artefacto:
  perfil:
    dominio: [knowledge-curation, kb-normal, korafication, review-repair]
    disparadores:
      - "curation-conductor clasifico el caso como knowledge + KB normal"
      - "hay una fuente descriptiva que debe convertirse a draft en REVIEW"
      - "existe un draft descriptivo en REVIEW que requiere repair o re-auditoria"
      - "un artefacto publicado necesita repair antes de volver a REVIEW o promote"
    salidas:
      - "draft KORA/MD descriptivo en REVIEW"
      - "reporte de auditoria de draft"
      - "outcome operativo explicito"
      - "siguiente paso para conductor, review o promote"
  plan:
    estado_inicial: validar-handoff
    estado_terminal: emitir-outcome-review
    estados:
      - validar-handoff
      - disenar-draft
      - koraficar-o-reparar
      - auditar-borrador
      - consolidar-review
      - emitir-outcome-review
  interfaz:
    herramientas: [Read, Write, Glob, Grep, Bash]
    permisos: "Lectura/escritura sobre artifacts/knowledge/_SCRIPTORIUM/REVIEW y ejecucion controlada de toolchain KORA."
    protocolos:
      entrada: "fuente o draft + route contract de curation-conductor o diagnostico minimo equivalente"
      salida: "draft en REVIEW + reporte de auditoria + outcome operativo"
  invariantes:
    reglas_duras:
      - "Opera solo la ruta descriptiva `KB normal`."
      - "Si el diagnostico indica `atomic`, devolver handoff a `atomize`."
      - "Si el material es prescriptivo, fundacional o de gobierno, devolver `rerouted_to_spec`."
      - "No publica directo a productivo; deja el trabajo en `REVIEW`."
      - "No reemplaza `atomize`, `promote` ni `validation`; los prepara o invoca segun corresponda."
      - "Toda salida debe declarar URN, provenance, familia, estado y siguiente paso."
      - "Si la auditoria falla, el outcome final es `needs_repair` o `processing`, nunca `ready_to_promote` por sobreafirmacion."
---

# Knowledge Curator

## Proposito

Implementar la ruta descriptiva `KB normal` del pipeline de
`artifacts/knowledge/`. Esta skill ejecuta el trabajo que en `curator` se
reparte entre diseño, koraficación, auditoría, repair y consolidación de
review, pero acotado a artefactos de conocimiento descriptivos.

## Cuando Usar

- cuando `curation-conductor` resolvió `knowledge + KB normal`
- cuando una fuente descriptiva debe transformarse a draft KORA/MD en `REVIEW`
- cuando un draft descriptivo en `REVIEW` necesita repair, re-auditoría o
  clarificación de readiness
- cuando un artefacto publicado requiere repair descriptivo antes de volver al
  circuito de review

## Workflow

1. Validar el handoff o hacer intake mínimo equivalente.
2. Si la ruta no es `knowledge + KB normal`, devolver handoff explícito:
   - `atomic` -> `atomize`
   - `spec-like` -> `rerouted_to_spec`
3. Diseñar el draft:
   - namespace
   - URN
   - familia `note`/`guide`/`kb` u otra familia descriptiva aplicable
   - staging path en `REVIEW`
   - headings y estructura recuperable
4. Ejecutar la transformación descriptiva:
   - koraficar fuente cruda a KORA/MD
   - o reparar draft existente sin cambiar su régimen documental
5. Auditar el borrador contra `md-spec` y `knowledge-spec`.
6. Consolidar entregables visibles:
   - draft path
   - reporte de auditoría
   - bloqueos
   - estado resultante
7. Emitir outcome explícito:
   - `processing`
   - `needs_repair`
   - `ready_to_promote`
   - `rerouted_to_spec`

## Route Contract

- Si se invoca con diagnóstico previo, consumir el contrato de ruta emitido por
  `curation-conductor`.
- Si se invoca directo y falta contrato, hacer diagnóstico mínimo solo para
  decidir si corresponde ejecutar o devolver `pending`.
- Si el diagnóstico mínimo no alcanza para afirmar `KB normal`, no forzar la
  curación: emitir `pending` con bloqueo explícito.

## Reglas Duras

- `KB normal` es el único tramo que esta skill implementa.
- `atomic` no se ejecuta aquí; se deriva a `atomize`.
- material prescriptivo o fundacional no se fuerza a knowledge publicado.
- el target inmediato de esta skill es `REVIEW`, no publicación.
- todo repair debe preservar URN, familia y trazabilidad salvo cambio explícito
  de diseño.
- si el draft queda usable pero todavía defectuoso, declarar `needs_repair`
  antes que sobreafirmar readiness.

## Recursos

### Referencias

- `referencias/workflow-map.md`
- `referencias/handoff-contract.md`

## Salida Esperada

- diagnóstico de ruta consumido o reconstruido
- diseño del draft o repair plan aplicado
- path del draft en `REVIEW`
- resumen de auditoría
- outcome operativo final
- siguiente paso para `curation-conductor`, review o promote
