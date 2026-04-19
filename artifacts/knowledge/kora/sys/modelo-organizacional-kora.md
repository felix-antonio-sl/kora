---
_manifest:
  urn: "urn:kora:kb:modelo-organizacional-kora"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-19"
    source: "Cierre H22: modela KORA como sistema organizacional de Part IX usando la topologia real del repo y sus pipelines de promocion."
version: "1.0.0"
status: publicado
tags: [organization, sociotechnical, kora, part-ix, model]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:procesos-spec"
    - "urn:kora:kb:multiagente-spec"
    - "urn:kora:kb:cat-ecosystem-2cat"
---

# Modelo organizacional de KORA

## 1. Tesis

KORA no es solo un repositorio. Es una organizacion sociotecnica minima donde
norma, staging, promocion y runtime forman un sistema coherente de produccion de
artefactos.

## 2. Objetos organizacionales

Los objetos principales del sistema son:

- constitucion (`governance/`)
- ontologia (`ontology/`)
- serializacion (`serialization/`)
- runtime (`runtime/`)
- conocimiento productivo (`artifacts/knowledge/`)
- agentes productivos (`artifacts/agents/`)
- skills productivas (`artifacts/skills/`)
- staging (`_SCRIPTORIUM`, `_FRAGUA`, `_TALLER`)

## 3. Morfismos organizacionales

Las flechas organizacionales dominantes son:

- gobernar: constitucion -> todas las capas
- serializar: ontologia -> authoring
- promover: staging -> productivo
- transmutar: IR -> runtime target
- verificar: repo state -> diag
- cristalizar: decision informal -> artefacto publicado

## 4. Lectura de Part IX

Part IX del `arquitecto-categorico` pide modelar organizaciones como sistemas
compuestos, no como organigramas decorativos. En KORA eso significa:

- la organizacion se parece mas a una comma category entre norma y ejecucion
  que a una jerarquia humana
- las unidades operativas son pipelines y cohortes, no solo carpetas
- la coherencia organizacional se mide por preservacion de estructura entre
  capas y por gates de promocion

## 5. KORA como comma category

Una lectura util es:

- objeto izquierdo: ley/norma (`gobernanza`, specs, invariantes)
- objeto derecho: ejecucion (`toolchain`, staging, runtime)
- objeto coma: artefactos promovidos que satisfacen ambas caras

En esta lectura, un artefacto productivo existe organizacionalmente solo si:

- conforma a la ley
- paso por el pipeline
- puede ser regenerado o auditado

## 6. Sistemas dentro del sistema

KORA contiene al menos tres subsistemas organizacionales:

- sistema de conocimiento
- sistema de agentes
- sistema de skills

Cada uno tiene staging propio, promotabilidad propia y deuda residual propia.
La organizacion global aparece al coordinarlos con una sola constitucion y una
sola toolchain.

## 7. Implicacion

El modelo organizacional correcto de KORA no es “equipo + repo”. Es:

- una organizacion de transformaciones gobernadas
- con role separation entre authoring, review, promotion y transmutation
- y con evidencia mecanica de coherencia (`check`, `unittest`, `kb-graph`)

## 8. Uso

Este modelo sirve para:

- razonar sobre promotion backlog
- decidir que vive en productivo vs staging
- formalizar futuros roles o cohortes
- justificar wiring multiagente como estructura organizacional y no solo tecnica
