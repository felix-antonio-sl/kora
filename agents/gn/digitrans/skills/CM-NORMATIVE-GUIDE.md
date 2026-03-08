---
_manifest:
  urn: urn:gn:skill:digitrans-normative-guide:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-NORMATIVE-GUIDE

## Proposito
Identificar, priorizar y sintetizar la normativa TDE aplicable a una consulta, preservando el piso normativo vigente.

## Input/Output
- **Input:** Consulta normativa sobre TDE Chile
- **Output:** Mapa normativo con instrumento, seccion relevante, nivel de obligatoriedad y relacion con la consulta

## Procedimiento
1. Clasificar si la consulta apunta a ley marco, decreto tecnico, obligacion procedimental o proteccion de datos.
2. Resolver via kb_route y catalog_resolve los artefactos TDE y legales pertinentes.
3. Separar obligaciones vigentes de contexto operativo o interpretacion institucional.
4. Entregar sintesis normativa con citas del instrumento y seccion relevante.

## Signature Output
Mapa normativo: [instrumento] + [seccion relevante] + [obligacion o alcance] + [relacion con la consulta].
