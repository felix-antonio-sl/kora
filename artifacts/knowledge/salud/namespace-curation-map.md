---
_manifest:
  urn: "urn:salud:kb:namespace-curation-map"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Curacion H7: mapa canónico del namespace `salud` para absorber nodos aislados del kb-graph mediante relacion declarada de pertenencia corpus."
version: "1.0.0"
status: publicado
tags: [namespace-map, kb-graph, curation, salud]
lang: es
extensions:
  kora:
    family: note
relations:
  depends:
    - "urn:kora:kb:knowledge-spec"
  cites:
    - "urn:salud:kb:firs-framework-integrado-razonamiento-salud"
    - "urn:salud:kb:gestion-redes-general-p02"
    - "urn:salud:kb:gestion-redes-general-p03"
    - "urn:salud:kb:gestion-redes-general-p04"
    - "urn:salud:kb:gestion-redes-general-p05"
    - "urn:salud:kb:gestion-redes-general-p06"
    - "urn:salud:kb:gestion-redes-general-p07"
    - "urn:salud:kb:gestion-redes-general-p08"
    - "urn:salud:kb:gestion-redes-general-p09"
    - "urn:salud:kb:gestion-redes-herramientas-p02"
    - "urn:salud:kb:gestion-redes-salud-mental-p02"
    - "urn:salud:kb:gestion-redes-salud-mental-p06"
    - "urn:salud:kb:gestion-redes-unidades-p02"
    - "urn:salud:kb:gestion-redes-unidades-p03"
    - "urn:salud:kb:gestion-redes-unidades-p04"
    - "urn:salud:kb:gestion-redes-urgencias-p03"
    - "urn:salud:kb:gestion-redes-urgencias-p05"
    - "urn:salud:kb:hodom-decreto-exento-31-2024"
    - "urn:salud:kb:hodom-direccion-tecnica"
    - "urn:salud:kb:hodom-direccion-tecnica-p02"
    - "urn:salud:kb:hodom-direccion-tecnica-p03"
    - "urn:salud:kb:hodom-manual-alta-complejidad"
    - "urn:salud:kb:hodom-manual-alta-complejidad-p02"
    - "urn:salud:kb:hodom-manual-alta-complejidad-p03"
    - "urn:salud:kb:hodom-manual-alta-complejidad-p04"
    - "urn:salud:kb:hodom-norma-tecnica-2024"
    - "urn:salud:kb:hodom-reglamento-ds1-2022"
    - "urn:salud:kb:hodom-situacion-chile-2026"
    - "urn:salud:kb:hodom-situacion-chile-2026-p02"
    - "urn:salud:kb:hodom-situacion-chile-2026-p03"
    - "urn:salud:kb:hodom-situacion-chile-2026-p04"
    - "urn:salud:kb:hodom-situacion-chile-2026-p05"
---

# SALUD/Namespace-Curation-Map v1.0.0

## 1. Definicion

Mapa canonico de curacion del namespace `salud`. Su funcion es declarar una
relacion minima, explicita y auditable entre el namespace y los documentos
publicados que permanecian aislados en `kb-graph`.

## 2. Regla de lectura

Cada arista de `relations.cites` en este documento debe leerse como:

> el artefacto citado pertenece al corpus operativo curado de `salud` aunque
> aun no tenga una relacion mas fina por familia, supersedes o dependencia.

## 3. Alcance

1. Esta pieza corrige orfandad real por ausencia de aristas declaradas.
2. No reemplaza curacion posterior por familia ni supersedes detallado.
3. No altera el contenido de los documentos citados; solo materializa su
   pertenencia al tejido del namespace.
