---
_manifest:
  urn: "urn:fxsl:kb:opm-readme"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-30"
    source: "synthesis:opm-corpus"
version: "1.1.0"
status: published
tags: [opm, readme, corpus, index, navigation, precedence]
lang: es
extensions:
  kora:
    family: readme
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:metodologia-modelamiento-opm"
      - "urn:fxsl:kb:opm-opl-es"
---

# README — Corpus OPM

Este directorio contiene el corpus KORA sobre **Object-Process Methodology (OPM)** dentro de `fxsl`.

Desde `2026-03-30`, el corpus canónico queda concentrado en **tres artefactos**:

1. [opm-iso-19450.md](opm-iso-19450.md)
2. [opm-opl-es.md](opm-opl-es.md)
3. [metodologia-modelamiento-opm.md](metodologia-modelamiento-opm.md)

Los demás artefactos OPM del directorio quedan como material deprecado o de migración, sin conocimiento único que deba consultarse para gobernar el ciclo de vida de modelos OPM.

## Alcance

- Dominio: modelamiento conceptual de sistemas con OPM.
- Ontologia: objetos, procesos, estados, relaciones estructurales y links procedurales.
- Modalidades: OPD grafico, OPL textual, realizacion en ingles canonico y OPL-ES.
- Tooling: OPCloud como implementacion operativa principal.
- Extension relacionada: comparacion con SysML en el subcorpus `model-based-systems-engineering-opm/`.

## Orden de precedencia

Cuando dos artefactos del corpus parezcan tensionarse, usar este orden:

1. [opm-iso-19450.md](opm-iso-19450.md): semantica OPM, notacion, definiciones y base normativa.
2. [opm-opl-es.md](opm-opl-es.md): realizacion OPL en espanol sin alterar la semantica OPM.
3. [metodologia-modelamiento-opm.md](metodologia-modelamiento-opm.md): integracion operativa del corpus, procedimiento SD/SD1+, invariantes y checklist.

Los artefactos deprecados no participan en precedencia. Solo preservan routing de migración.

## Mapa del corpus

### Fuentes Canónicas

- [opm-iso-19450.md](opm-iso-19450.md): especificacion formal compacta de OPM, notacion visual, OPL, metamodelo, dinamica y ejemplos normativos.
- [opm-opl-es.md](opm-opl-es.md): especificacion OPL-ES, plantillas de sentencias, reglas EN→ES y notas de roundtrip.
- [metodologia-modelamiento-opm.md](metodologia-modelamiento-opm.md): protocolo de modelamiento, construccion del SD, refinamiento, complejidad, simulacion, requirements e invariantes.
  Incluye el wizard agnóstico del SD como protocolo canónico, independiente de herramienta.

### Artefactos Deprecados o de Migracion

- [opm-sd-wizard.md](opm-sd-wizard.md): migrado a metodología. Conserva solo routing de deprecación.
- [opcloud-tutorial-videos.md](opcloud-tutorial-videos.md): conocimiento útil absorbido en metodología y OPL-ES.
- [opm-applied-system-modeling.md](opm-applied-system-modeling.md): conocimiento útil absorbido en metodología.
- [opm-canonical-example.md](opm-canonical-example.md): conocimiento útil absorbido como heurísticas y ejemplos mínimos; sin rol canónico residual.

### Subcorpus MBSE y apoyo

Directorio: [model-based-systems-engineering-opm](model-based-systems-engineering-opm)

- [opm-mbse-foundations.md](model-based-systems-engineering-opm/opm-mbse-foundations.md): fundamentos ontologicos y conceptuales.
- [opm-dynamic-behavior.md](model-based-systems-engineering-opm/opm-dynamic-behavior.md): links procedurales, control y operadores logicos.
- [opm-structural-relations.md](model-based-systems-engineering-opm/opm-structural-relations.md): relaciones estructurales, jerarquias, states y constraints.
- [opm-complexity-management.md](model-based-systems-engineering-opm/opm-complexity-management.md): in-zooming, unfolding, out-zooming, system maps y claridad/completitud.
- [opm-opl-bimodal.md](model-based-systems-engineering-opm/opm-opl-bimodal.md): equivalencia grafico-texto y rol cognitivo/operacional de OPL.
- [opm-mbse-acr-tutorial.md](model-based-systems-engineering-opm/opm-mbse-acr-tutorial.md): historia de OPM y tutorial ACR.
- [sysml-foundations-diagrams.md](model-based-systems-engineering-opm/sysml-foundations-diagrams.md): panorama SysML y contraste con OPM.

## Rutas de lectura recomendadas

### 1. Para entender OPM desde cero

1. [opm-mbse-foundations.md](model-based-systems-engineering-opm/opm-mbse-foundations.md)
2. [opm-iso-19450.md](opm-iso-19450.md)
3. [opm-opl-bimodal.md](model-based-systems-engineering-opm/opm-opl-bimodal.md)
4. [opm-dynamic-behavior.md](model-based-systems-engineering-opm/opm-dynamic-behavior.md)
5. [opm-structural-relations.md](model-based-systems-engineering-opm/opm-structural-relations.md)

### 2. Para modelar un sistema en la practica

1. [metodologia-modelamiento-opm.md](metodologia-modelamiento-opm.md)
2. [opm-iso-19450.md](opm-iso-19450.md)
3. [opm-opl-es.md](opm-opl-es.md)

### 3. Para implementar OPL en espanol

1. [opm-opl-es.md](opm-opl-es.md)
2. [opm-iso-19450.md](opm-iso-19450.md)
3. [opm-opl-bimodal.md](model-based-systems-engineering-opm/opm-opl-bimodal.md)

### 4. Para refinar modelos complejos

1. [opm-complexity-management.md](model-based-systems-engineering-opm/opm-complexity-management.md)
2. [metodologia-modelamiento-opm.md](metodologia-modelamiento-opm.md)
3. [opm-canonical-example.md](opm-canonical-example.md)

## Convenciones editoriales del corpus

- `lang: en` suele indicar surface form canonica cercana a ISO/OPCloud.
- `lang: es` indica prosa o especificacion orientada a espanol; no obliga por si sola a que todas las sentencias OPL esten en espanol.
- Cuando un artefacto `lang: es` mantiene OPL en ingles canonico, debe declararlo explicitamente.
- `OPL-ES` gobierna solo la realizacion textual en espanol; no altera ontologia ni semantica.
- `OPCloud` operacionaliza el modelamiento pero no redefine el lenguaje OPM.
- El `SD Wizard` y los tutoriales de OPCloud ya no son fuentes canónicas; su conocimiento útil fue absorbido en metodología/OPL-ES.

## Estado del corpus

- Estado editorial: corpus canónico consolidado a tres artefactos al `2026-03-30`.
- Inconsistencias criticas reparadas: alineacion entre wizard/metodologia/OPCloud y correccion de `agent` no humanos en material de ejemplo.
- Riesgo residual conocido: el subcorpus MBSE de apoyo sigue existiendo como material complementario en ingles; no reemplaza a las tres fuentes canónicas.

## Regla operativa rapida

Si buscas:

- verdad normativa: parte por [opm-iso-19450.md](opm-iso-19450.md)
- surface form en espanol: parte por [opm-opl-es.md](opm-opl-es.md)
- como modelar: parte por [metodologia-modelamiento-opm.md](metodologia-modelamiento-opm.md)
- como usar la herramienta: parte por [metodologia-modelamiento-opm.md](metodologia-modelamiento-opm.md) y [opm-opl-es.md](opm-opl-es.md)
- material historico de migracion: abre los artefactos deprecados solo para routing, no como fuente de verdad
