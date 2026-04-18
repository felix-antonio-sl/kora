---
_manifest:
  urn: "urn:tde:kb:namespace-curation-map"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Curacion H7: mapa canónico del namespace `tde` para absorber nodos aislados del kb-graph mediante relacion declarada de pertenencia corpus."
version: "1.0.0"
status: publicado
tags: [namespace-map, kb-graph, curation, tde]
lang: es
extensions:
  kora:
    family: note
relations:
  depends:
    - "urn:kora:kb:knowledge-spec"
  cites:
    - "urn:tde:kb:decreto-10-documentos-expedientes-electronicos"
    - "urn:tde:kb:decreto-11-plataformas-electronicas"
    - "urn:tde:kb:decreto-12-interoperabilidad"
    - "urn:tde:kb:decreto-4-procedimientos-electronicos"
    - "urn:tde:kb:decreto-4-procedimientos-electronicos-p02"
    - "urn:tde:kb:decreto-4-procedimientos-electronicos-p03"
    - "urn:tde:kb:decreto-4-procedimientos-electronicos-p04"
    - "urn:tde:kb:decreto-4-procedimientos-electronicos-p05"
    - "urn:tde:kb:decreto-4-procedimientos-electronicos-p06"
    - "urn:tde:kb:decreto-4-procedimientos-electronicos-p07"
    - "urn:tde:kb:decreto-8-norma-notificaciones"
    - "urn:tde:kb:decreto-9-norma-autenticacion"
    - "urn:tde:kb:estandares-apertura-reutilizacion-datos-abiertos"
    - "urn:tde:kb:estrategia-capacitaciones-transformacion-digital"
    - "urn:tde:kb:estrategia-datos-administracion-estado"
    - "urn:tde:kb:estrategia-gobierno-digital-2030"
    - "urn:tde:kb:estrategia-identidad-digital"
    - "urn:tde:kb:glosario-plataforma-simple"
    - "urn:tde:kb:guia-calidad-web"
    - "urn:tde:kb:guia-introductoria-anonimizacion-datos"
    - "urn:tde:kb:guia-metodologica-sistema-transformacion-digital-2025-p02"
    - "urn:tde:kb:guia-rapida-cpat"
    - "urn:tde:kb:guia-tecnica-evaltic-inversiones-gobierno-digital"
    - "urn:tde:kb:guia-tecnica-metadatos-documentos-expedientes"
    - "urn:tde:kb:guia-tecnica-seguridad-informacion-ciberseguridad"
    - "urn:tde:kb:guia-tecnica-seguridad-informacion-ciberseguridad-p02"
    - "urn:tde:kb:guia-voz-y-tono"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos-p02"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos-p03"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos-p04"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos-p05"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos-p06"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos-p07"
    - "urn:tde:kb:ley-19880-bases-procedimientos-administrativos-p08"
    - "urn:tde:kb:ley-21180-transformacion-digital-estado"
    - "urn:tde:kb:ley-21658"
    - "urn:tde:kb:manual-atencion-ciudadana-notificaciones"
    - "urn:tde:kb:manual-coordinadora-transformacion-digital"
    - "urn:tde:kb:manual-inicio-notificaciones-electronicas"
    - "urn:tde:kb:manual-integracion-claveunica"
    - "urn:tde:kb:manual-integracion-notificaciones"
    - "urn:tde:kb:manual-integracion-notificaciones-p02"
    - "urn:tde:kb:manual-uso-boton-claveunica"
    - "urn:tde:kb:manual-uso-simple-saas"
    - "urn:tde:kb:manual-usuario-institucional-notificaciones"
    - "urn:tde:kb:metodologia-gestion-proyectos"
    - "urn:tde:kb:orientaciones-basicas-gestion-tic"
    - "urn:tde:kb:recomendaciones-diseno-servicios-estado"
    - "urn:tde:kb:recomendaciones-tecnicas-cloud-publica"
    - "urn:tde:kb:registro-actividades-tratamiento"
    - "urn:tde:kb:terminos-condiciones-claveunica"
---

# TDE/Namespace-Curation-Map v1.0.0

## 1. Definicion

Mapa canonico de curacion del namespace `tde`. Su funcion es declarar una
relacion minima, explicita y auditable entre el namespace y los documentos
publicados que permanecian aislados en `kb-graph`.

## 2. Regla de lectura

Cada arista de `relations.cites` en este documento debe leerse como:

> el artefacto citado pertenece al corpus operativo curado de `tde` aunque
> aun no tenga una relacion mas fina por familia, supersedes o dependencia.

## 3. Alcance

1. Esta pieza corrige orfandad real por ausencia de aristas declaradas.
2. No reemplaza curacion posterior por familia ni supersedes detallado.
3. No altera el contenido de los documentos citados; solo materializa su
   pertenencia al tejido del namespace.
