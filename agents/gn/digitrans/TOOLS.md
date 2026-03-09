---
_manifest:
  urn: "urn:gn:agent-bootstrap:digitrans-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Parametros:** `urn` conceptual del artefacto TDE u ORKO a resolver.
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
| Introduccion TDE, sistema TDE, panorama general | urn:tde:kb:guia-sistema-tde-2025 |
| Gobierno Digital 2030, Principios, Objetivos | urn:tde:kb:gobierno-digital-2030 |
| Glosario, lenguaje institucional, terminos de plataforma | urn:tde:kb:glosario-simple |
| **LEYES** | |
| Ley 21.180, TDE | urn:tde:kb:ley-21180-tde |
| Ley 19.880, LBPA, Procedimiento Administrativo | urn:tde:kb:ley-19880-procedimiento-administrativo |
| Ley 21.658, SEGDIG / Ciberseguridad | urn:tde:kb:ley-21658-ciberseguridad |
| Ley 21.719, Datos Personales | urn:tde:kb:ley-21719-datos-personales |
| IA, Legislacion | urn:tde:kb:legislacion-ia-chile |
| Decreto Supremo 4, Procedimiento Digital | urn:tde:kb:decreto-4-procedimiento-digital |
| **NORMAS TECNICAS** | |
| Dec.10, Documentos Expedientes | urn:tde:kb:nt-documentos-expedientes |
| Dec.12, Interoperabilidad | urn:tde:kb:nt-interoperabilidad |
| Dec.8, Notificaciones | urn:tde:kb:nt-notificaciones |
| Dec.7, Seguridad Ciberseguridad | urn:tde:kb:nt-seguridad-ciberseguridad |
| Dec.9, Autenticacion | urn:tde:kb:nt-autenticacion |
| Dec.11, Plataformas Procedimientos | urn:tde:kb:nt-plataformas-procedimientos |
| **PLATAFORMAS** | |
| ClaveUnica, Integracion | urn:tde:kb:manual-integracion-claveunica |
| ClaveUnica, Boton Implementacion | urn:tde:kb:manual-claveunica-boton |
| Notificaciones, Onboarding | urn:tde:kb:manual-notificaciones-inicio |
| Notificaciones, Integracion Tecnica | urn:tde:kb:manual-integracion-notificaciones |
| Notificaciones, Uso institucional | urn:tde:kb:manual-notificaciones-institucional |
| Notificaciones, Atencion ciudadana | urn:tde:kb:manual-notificaciones-atencion-ciudadana |
| SIMPLE | urn:tde:kb:manual-simple-saas |
| SIMPLE, Glosario | urn:tde:kb:glosario-simple |
| DocDigital | urn:tde:kb:manual-coordinadora-tde |
| PISEE, Red de Interoperabilidad del Estado | urn:tde:kb:manual-coordinadora-tde |
| ClaveUnica, terminos y condiciones | urn:tde:kb:claveunica-tyc |
| Coordinacion institucional TDE | urn:tde:kb:manual-coordinadora-tde |
| **ESTRATEGIAS** | |
| Estrategia Datos | urn:tde:kb:estrategia-datos |
| Identidad Digital | urn:tde:kb:estrategia-identidad-digital |
| Gobierno Digital 2030 | urn:tde:kb:gobierno-digital-2030 |
| Capacitaciones TDE | urn:tde:kb:estrategia-capacitaciones-tde |
| Sistema TDE 2025 | urn:tde:kb:guia-sistema-tde-2025 |
| **GUIAS** | |
| CPAT, Guia Rapida | urn:tde:kb:guia-rapida-cpat |
| MGDE, Marco Gestion Datos | urn:tde:kb:guia-marco-gestion-datos |
| Cloud Publica | urn:tde:kb:guia-cloud-publica |
| Estandares de datos abiertos | urn:tde:kb:guia-estandares-datos-abiertos |
| Metadatos Documentos | urn:tde:kb:guia-metadatos-documentos |
| EVALTIC | urn:tde:kb:guia-evaltic |
| Calidad Web | urn:tde:kb:guia-calidad-web |
| Diseno Servicios | urn:tde:kb:guia-diseno-servicios |
| Anonimizacion Datos | urn:tde:kb:guia-anonimizacion-datos |
| Gestion TIC, Orientaciones | urn:tde:kb:guia-gestion-tic |
| Seguridad Ciberseguridad, Guia | urn:tde:kb:guia-seguridad-ciberseguridad |
| Registro Tratamiento Datos, RAT | urn:tde:kb:guia-registro-tratamiento-datos |
| Metodologia Proyectos TIC | urn:tde:kb:guia-metodologia-proyectos |
| Voz y tono institucional | urn:tde:kb:guia-voz-tono |
| **ORKO BRIDGE** | |
| ORKO, Metodologia WSLC | urn:orko:kb:orko-metodologia |
| ORKO, Fases WSLC | urn:orko:kb:orko-fases |
| ORKO, Fundamentos y H_org | urn:orko:kb:orko-fundamentos |
