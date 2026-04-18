---
_manifest:
  urn: "urn:legal:kb:namespace-curation-map"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Curacion H7: mapa canónico del namespace `legal` para absorber nodos aislados del kb-graph mediante relacion declarada de pertenencia corpus."
version: "1.0.0"
status: publicado
tags: [namespace-map, kb-graph, curation, legal]
lang: es
extensions:
  kora:
    family: note
relations:
  depends:
    - "urn:kora:kb:knowledge-spec"
  cites:
    - "urn:legal:kb:certificados-tramites-post-constitucion"
    - "urn:legal:kb:eirl-empresa-individual"
    - "urn:legal:kb:firma-electronica-empresas"
    - "urn:legal:kb:ley-21658-segdig"
    - "urn:legal:kb:ley-21719-datos-personales"
    - "urn:legal:kb:marco-legal-sociedades-chile"
    - "urn:legal:kb:patente-comercial-res"
    - "urn:legal:kb:reglamento-ley-20659"
    - "urn:legal:kb:sociedad-anonima-cerrada"
    - "urn:legal:kb:sociedad-colectiva-comercial"
    - "urn:legal:kb:sociedad-comandita"
    - "urn:legal:kb:sociedad-por-acciones"
    - "urn:legal:kb:sociedad-responsabilidad-limitada"
---

# LEGAL/Namespace-Curation-Map v1.0.0

## 1. Definicion

Mapa canonico de curacion del namespace `legal`. Su funcion es declarar una
relacion minima, explicita y auditable entre el namespace y los documentos
publicados que permanecian aislados en `kb-graph`.

## 2. Regla de lectura

Cada arista de `relations.cites` en este documento debe leerse como:

> el artefacto citado pertenece al corpus operativo curado de `legal` aunque
> aun no tenga una relacion mas fina por familia, supersedes o dependencia.

## 3. Alcance

1. Esta pieza corrige orfandad real por ausencia de aristas declaradas.
2. No reemplaza curacion posterior por familia ni supersedes detallado.
3. No altera el contenido de los documentos citados; solo materializa su
   pertenencia al tejido del namespace.
