---
_manifest:
  urn: "urn:gn:agent-bootstrap:digitrans-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Parametros:** `urn` conceptual del artefacto TDE a resolver.
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Descripcion funcional:** Resuelve una URN del catalogo vivo a una ruta local consultable por el agente.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Parametros:** `query_topic` con el tema institucional a clasificar.
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Descripcion funcional:** Mapea un tema TDE a la fuente de conocimiento prioritaria del corpus base.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| **CORE** | |
| Introduccion TDE, sistema TDE, panorama general | urn:kora:kb:tde:lineamientos-guias:guia-metodologica-sistema-transformacion-digital-2025:1.0.0 |
| Gobierno Digital 2030, Principios, Objetivos | urn:kora:kb:tde:estrategias:estrategia-gobierno-digital-2030:1.0.0 |
| Glosario, lenguaje institucional, terminos de plataforma | urn:kora:kb:tde:plataformas-manuales:glosario-plataforma-simple:1.0.0 |
| **LEYES** | |
| Ley 21.180, TDE | urn:kora:kb:tde:regulacion:ley-21180-transformacion-digital-estado:1.0.0 |
| Ley 19.880, LBPA, Procedimiento Administrativo | urn:kora:kb:tde:regulacion:ley-19880-bases-procedimientos-administrativos:1.0.0 |
| Ley 21.658, SEGDIG / Ciberseguridad | urn:kora:kb:tde:regulacion:ley-21658:1.0.0 |
| Decreto Supremo 4, Procedimiento Digital | urn:kora:kb:tde:regulacion:decreto-4-procedimientos-electronicos:1.0.0 |
| **NORMAS TECNICAS** | |
| Dec.10, Documentos Expedientes | urn:kora:kb:tde:lineamientos-normas:decreto-10-documentos-expedientes-electronicos:1.0.0 |
| Dec.12, Interoperabilidad | urn:kora:kb:tde:lineamientos-normas:decreto-12-interoperabilidad:1.0.0 |
| Dec.8, Notificaciones | urn:kora:kb:tde:lineamientos-normas:decreto-8-norma-notificaciones:1.0.0 |
| Dec.7, Seguridad Ciberseguridad | urn:kora:kb:tde:lineamientos-normas:decreto-7-norma-seguridad-informacion:1.0.0 |
| Dec.9, Autenticacion | urn:kora:kb:tde:lineamientos-normas:decreto-9-norma-autenticacion:1.0.0 |
| Dec.11, Plataformas Procedimientos | urn:kora:kb:tde:lineamientos-normas:decreto-11-plataformas-electronicas:1.0.0 |
| **PLATAFORMAS** | |
| ClaveUnica, Integracion | urn:kora:kb:tde:plataformas-manuales:manual-integracion-claveunica:1.0.0 |
| ClaveUnica, Boton Implementacion | urn:kora:kb:tde:plataformas-manuales:manual-uso-boton-claveunica:1.0.0 |
| Notificaciones, Onboarding | urn:kora:kb:tde:plataformas-manuales:manual-inicio-notificaciones-electronicas:1.0.0 |
| Notificaciones, Integracion Tecnica | urn:kora:kb:tde:plataformas-manuales:manual-integracion-notificaciones:1.0.0 |
| Notificaciones, Uso institucional | urn:kora:kb:tde:plataformas-manuales:manual-usuario-institucional-notificaciones:1.0.0 |
| Notificaciones, Atencion ciudadana | urn:kora:kb:tde:plataformas-manuales:manual-atencion-ciudadana-notificaciones:1.0.0 |
| SIMPLE | urn:kora:kb:tde:plataformas-manuales:manual-uso-simple-saas:1.0.0 |
| SIMPLE, Glosario | urn:kora:kb:tde:plataformas-manuales:glosario-plataforma-simple:1.0.0 |
| DocDigital, Coordinacion TDE | urn:kora:kb:tde:plataformas-manuales:manual-coordinadora-transformacion-digital:1.0.0 |
| ClaveUnica, terminos y condiciones | urn:kora:kb:tde:plataformas-terminos:terminos-condiciones-claveunica:1.0.0 |
| **ESTRATEGIAS** | |
| Estrategia Datos | urn:kora:kb:tde:estrategias:estrategia-datos-administracion-estado:1.0.0 |
| Identidad Digital | urn:kora:kb:tde:estrategias:estrategia-identidad-digital:1.0.0 |
| Gobierno Digital 2030 | urn:kora:kb:tde:estrategias:estrategia-gobierno-digital-2030:1.0.0 |
| Capacitaciones TDE | urn:kora:kb:tde:estrategias:estrategia-capacitaciones-transformacion-digital:1.0.0 |
| Sistema TDE 2025 | urn:kora:kb:tde:lineamientos-guias:guia-metodologica-sistema-transformacion-digital-2025:1.0.0 |
| **GUIAS** | |
| CPAT, Guia Rapida | urn:kora:kb:tde:lineamientos-guias:guia-rapida-cpat:1.0.0 |
| MGDE, Marco Gestion Datos | urn:kora:kb:tde:lineamientos-guias:guia-tecnica-marco-gestion-datos:1.0.0 |
| Cloud Publica | urn:kora:kb:tde:lineamientos-guias:recomendaciones-tecnicas-cloud-publica:1.0.0 |
| Estandares de datos abiertos | urn:kora:kb:tde:lineamientos-estandares:estandares-apertura-reutilizacion-datos-abiertos:1.0.0 |
| Metadatos Documentos | urn:kora:kb:tde:lineamientos-guias:guia-tecnica-metadatos-documentos-expedientes:1.0.0 |
| EVALTIC | urn:kora:kb:tde:lineamientos-guias:guia-tecnica-evaltic-inversiones-gobierno-digital:1.0.0 |
| Calidad Web | urn:kora:kb:tde:lineamientos-guias:guia-calidad-web:1.0.0 |
| Diseno Servicios | urn:kora:kb:tde:plataformas-manuales:recomendaciones-diseno-servicios-estado:1.0.0 |
| Anonimizacion Datos | urn:kora:kb:tde:lineamientos-guias:guia-introductoria-anonimizacion-datos:1.0.0 |
| Gestion TIC, Orientaciones | urn:kora:kb:tde:lineamientos-guias:orientaciones-basicas-gestion-tic:1.0.0 |
| Seguridad Ciberseguridad, Guia | urn:kora:kb:tde:lineamientos-guias:guia-tecnica-seguridad-informacion-ciberseguridad:1.0.0 |
| Registro Tratamiento Datos, RAT | urn:kora:kb:tde:proteccion-datos:registro-actividades-tratamiento:1.0.0 |
| Metodologia Proyectos TIC | urn:kora:kb:tde:lineamientos-guias:metodologia-gestion-proyectos:1.0.0 |
| Voz y tono institucional | urn:kora:kb:tde:plataformas-manuales:guia-voz-y-tono:1.0.0 |
