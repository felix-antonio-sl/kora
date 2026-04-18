---
_manifest:
  urn: "urn:sii:kb:namespace-curation-map"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Curacion H7: mapa canónico del namespace `sii` para absorber nodos aislados del kb-graph mediante relacion declarada de pertenencia corpus."
version: "1.0.0"
status: publicado
tags: [namespace-map, kb-graph, curation, sii]
lang: es
extensions:
  kora:
    family: note
relations:
  depends:
    - "urn:kora:kb:knowledge-spec"
  cites:
    - "urn:sii:kb:faq-activos-digitales"
    - "urn:sii:kb:faq-actualizacion-de-informacion"
    - "urn:sii:kb:faq-acuerdos-anticipados-de-precios-de-transferencia"
    - "urn:sii:kb:faq-avaluos-y-contribuciones-de-bienes-raices"
    - "urn:sii:kb:faq-beneficios-tributarios"
    - "urn:sii:kb:faq-boletas-de-honorarios-electronicas"
    - "urn:sii:kb:faq-boletas-electronicas-de-ventas-y-servicios"
    - "urn:sii:kb:faq-clave-tributaria-mandatario-digital-y-representantes-electronicos"
    - "urn:sii:kb:faq-clave-tributaria-y-representantes-electronicos"
    - "urn:sii:kb:faq-declaracion-de-renta"
    - "urn:sii:kb:faq-declaraciones-juradas"
    - "urn:sii:kb:faq-factura-electronica"
    - "urn:sii:kb:faq-herencias"
    - "urn:sii:kb:faq-impuesto-a-aviones-helicopteros-yates-y-vehiculos-de-alto-valor"
    - "urn:sii:kb:faq-impuestos-mensuales"
    - "urn:sii:kb:faq-infracciones-pago-de-giros-y-condonaciones"
    - "urn:sii:kb:faq-iva-a-los-servicios-profesionales-y-culturales"
    - "urn:sii:kb:faq-libros-contables-electronicos"
    - "urn:sii:kb:faq-otros-impuestos"
    - "urn:sii:kb:faq-peticiones-administrativas-y-otras-solicitudes"
    - "urn:sii:kb:faq-preguntas-generales"
    - "urn:sii:kb:faq-rut-e-inicio-de-actividades"
    - "urn:sii:kb:faq-situacion-tributaria"
    - "urn:sii:kb:faq-tasacion-fiscal-de-vehiculos"
    - "urn:sii:kb:faq-termino-de-giro"
    - "urn:sii:kb:index-documentos-derivados"
---

# SII/Namespace-Curation-Map v1.0.0

## 1. Definicion

Mapa canonico de curacion del namespace `sii`. Su funcion es declarar una
relacion minima, explicita y auditable entre el namespace y los documentos
publicados que permanecian aislados en `kb-graph`.

## 2. Regla de lectura

Cada arista de `relations.cites` en este documento debe leerse como:

> el artefacto citado pertenece al corpus operativo curado de `sii` aunque
> aun no tenga una relacion mas fina por familia, supersedes o dependencia.

## 3. Alcance

1. Esta pieza corrige orfandad real por ausencia de aristas declaradas.
2. No reemplaza curacion posterior por familia ni supersedes detallado.
3. No altera el contenido de los documentos citados; solo materializa su
   pertenencia al tejido del namespace.
