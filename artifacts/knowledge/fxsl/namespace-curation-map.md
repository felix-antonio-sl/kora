---
_manifest:
  urn: "urn:fxsl:kb:namespace-curation-map"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Curacion H7: mapa canónico del namespace `fxsl` para absorber nodos aislados del kb-graph mediante relacion declarada de pertenencia corpus."
version: "1.0.0"
status: publicado
tags: [namespace-map, kb-graph, curation, fxsl]
lang: es
extensions:
  kora:
    family: note
relations:
  depends:
    - "urn:kora:kb:knowledge-spec"
  cites:
    - "urn:fxsl:kb:action-primary-key"
    - "urn:fxsl:kb:algebraic-model-management"
    - "urn:fxsl:kb:allan-kelly-gemelo-digital-intelectual"
    - "urn:fxsl:kb:audit-patterns"
    - "urn:fxsl:kb:categorical-data-structures"
    - "urn:fxsl:kb:chapter0-operador-solitario"
    - "urn:fxsl:kb:chapter0-operador-solitario-p02"
    - "urn:fxsl:kb:cognitive-toolkit"
    - "urn:fxsl:kb:data-access-layers"
    - "urn:fxsl:kb:fx-address-guidance"
    - "urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol"
    - "urn:fxsl:kb:fx-guide-onto-gist-001-audit-protocol-p02"
    - "urn:fxsl:kb:fx-namespace"
    - "urn:fxsl:kb:fx-readme"
    - "urn:fxsl:kb:fx-rules"
    - "urn:fxsl:kb:fx-tensiones"
    - "urn:fxsl:kb:fx-uom-model"
    - "urn:fxsl:kb:icas-adjunciones"
    - "urn:fxsl:kb:icas-comparacion"
    - "urn:fxsl:kb:icas-composicion"
    - "urn:fxsl:kb:icas-composicion-estructura"
    - "urn:fxsl:kb:icas-extension"
    - "urn:fxsl:kb:icas-higher-categories"
    - "urn:fxsl:kb:icas-identidad-relacion"
    - "urn:fxsl:kb:icas-infraestructura"
    - "urn:fxsl:kb:icas-lifecycle"
    - "urn:fxsl:kb:icas-patrones"
    - "urn:fxsl:kb:icas-procesos"
    - "urn:fxsl:kb:icas-protocolos"
    - "urn:fxsl:kb:icas-sintesis"
    - "urn:fxsl:kb:icas-tiempo"
    - "urn:fxsl:kb:icas-topoi"
    - "urn:fxsl:kb:icas-universales"
    - "urn:fxsl:kb:metodologia-modelamiento-opm-p02"
    - "urn:fxsl:kb:metodologia-modelamiento-opm-p03"
    - "urn:fxsl:kb:metodologia-modelamiento-opm-p04"
    - "urn:fxsl:kb:multicategory-multimodel-query-processing"
    - "urn:fxsl:kb:opcloud-tutorial-visual-observations"
    - "urn:fxsl:kb:opcloud-tutorial-visual-observations-p02"
    - "urn:fxsl:kb:opm-dynamic-behavior-p02"
    - "urn:fxsl:kb:opm-dynamic-behavior-p03"
    - "urn:fxsl:kb:opm-iso-19450-p02"
    - "urn:fxsl:kb:opm-iso-19450-p03"
    - "urn:fxsl:kb:opm-iso-19450-p04"
    - "urn:fxsl:kb:opm-iso-19450-p05"
    - "urn:fxsl:kb:procrastination-sirois"
    - "urn:fxsl:kb:procrastination-sirois-p02"
    - "urn:fxsl:kb:stack-llm-arquitectura"
    - "urn:fxsl:kb:stack-llm-arquitectura-p02"
    - "urn:fxsl:kb:swarm-ops-metodologia"
    - "urn:fxsl:kb:xanpan-agents-metodologia"
---

# FXSL/Namespace-Curation-Map v1.0.0

## 1. Definicion

Mapa canonico de curacion del namespace `fxsl`. Su funcion es declarar una
relacion minima, explicita y auditable entre el namespace y los documentos
publicados que permanecian aislados en `kb-graph`.

## 2. Regla de lectura

Cada arista de `relations.cites` en este documento debe leerse como:

> el artefacto citado pertenece al corpus operativo curado de `fxsl` aunque
> aun no tenga una relacion mas fina por familia, supersedes o dependencia.

## 3. Alcance

1. Esta pieza corrige orfandad real por ausencia de aristas declaradas.
2. No reemplaza curacion posterior por familia ni supersedes detallado.
3. No altera el contenido de los documentos citados; solo materializa su
   pertenencia al tejido del namespace.
