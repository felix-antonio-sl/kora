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
| Introduccion TDE, sistema TDE, panorama general | urn:tde:kb:guia-metodologica-sistema-transformacion-digital-2025 |
| Gobierno Digital 2030, Principios, Objetivos | urn:tde:kb:estrategia-gobierno-digital-2030 |
| Glosario, lenguaje institucional, terminos de plataforma | urn:tde:kb:glosario-plataforma-simple |
| **LEYES** | |
| Ley 21.180, TDE | urn:tde:kb:ley-21180-transformacion-digital-estado |
| Ley 19.880, LBPA, Procedimiento Administrativo | urn:tde:kb:ley-19880-bases-procedimientos-administrativos |
| Ley 21.658, SEGDIG / Ciberseguridad | urn:tde:kb:ley-21658 |
| Decreto Supremo 4, Procedimiento Digital | urn:tde:kb:decreto-4-procedimientos-electronicos |
| **NORMAS TECNICAS** | |
| Dec.10, Documentos Expedientes | urn:tde:kb:decreto-10-documentos-expedientes-electronicos |
| Dec.12, Interoperabilidad | urn:tde:kb:decreto-12-interoperabilidad |
| Dec.8, Notificaciones | urn:tde:kb:decreto-8-norma-notificaciones |
| Dec.7, Seguridad Ciberseguridad | urn:tde:kb:decreto-7-norma-seguridad-informacion |
| Dec.9, Autenticacion | urn:tde:kb:decreto-9-norma-autenticacion |
| Dec.11, Plataformas Procedimientos | urn:tde:kb:decreto-11-plataformas-electronicas |
| **PLATAFORMAS** | |
| ClaveUnica, Integracion | urn:tde:kb:manual-integracion-claveunica |
| ClaveUnica, Boton Implementacion | urn:tde:kb:manual-uso-boton-claveunica |
| Notificaciones, Onboarding | urn:tde:kb:manual-inicio-notificaciones-electronicas |
| Notificaciones, Integracion Tecnica | urn:tde:kb:manual-integracion-notificaciones |
| Notificaciones, Uso institucional | urn:tde:kb:manual-usuario-institucional-notificaciones |
| Notificaciones, Atencion ciudadana | urn:tde:kb:manual-atencion-ciudadana-notificaciones |
| SIMPLE | urn:tde:kb:manual-uso-simple-saas |
| SIMPLE, Glosario | urn:tde:kb:glosario-plataforma-simple |
| DocDigital, Coordinacion TDE | urn:tde:kb:manual-coordinadora-transformacion-digital |
| ClaveUnica, terminos y condiciones | urn:tde:kb:terminos-condiciones-claveunica |
| **ESTRATEGIAS** | |
| Estrategia Datos | urn:tde:kb:estrategia-datos-administracion-estado |
| Identidad Digital | urn:tde:kb:estrategia-identidad-digital |
| Gobierno Digital 2030 | urn:tde:kb:estrategia-gobierno-digital-2030 |
| Capacitaciones TDE | urn:tde:kb:estrategia-capacitaciones-transformacion-digital |
| Sistema TDE 2025 | urn:tde:kb:guia-metodologica-sistema-transformacion-digital-2025 |
| **GUIAS** | |
| CPAT, Guia Rapida | urn:tde:kb:guia-rapida-cpat |
| MGDE, Marco Gestion Datos | urn:tde:kb:guia-tecnica-marco-gestion-datos |
| Cloud Publica | urn:tde:kb:recomendaciones-tecnicas-cloud-publica |
| Estandares de datos abiertos | urn:tde:kb:estandares-apertura-reutilizacion-datos-abiertos |
| Metadatos Documentos | urn:tde:kb:guia-tecnica-metadatos-documentos-expedientes |
| EVALTIC | urn:tde:kb:guia-tecnica-evaltic-inversiones-gobierno-digital |
| Calidad Web | urn:tde:kb:guia-calidad-web |
| Diseno Servicios | urn:tde:kb:recomendaciones-diseno-servicios-estado |
| Anonimizacion Datos | urn:tde:kb:guia-introductoria-anonimizacion-datos |
| Gestion TIC, Orientaciones | urn:tde:kb:orientaciones-basicas-gestion-tic |
| Seguridad Ciberseguridad, Guia | urn:tde:kb:guia-tecnica-seguridad-informacion-ciberseguridad |
| Registro Tratamiento Datos, RAT | urn:tde:kb:registro-actividades-tratamiento |
| Metodologia Proyectos TIC | urn:tde:kb:metodologia-gestion-proyectos |
| Voz y tono institucional | urn:tde:kb:guia-voz-y-tono |
