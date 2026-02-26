---
_manifest:
  urn: "urn:tde:agent-bootstrap:digitrans-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| **CORE** | |
| Introduccion TDE | urn:gov:kb:intro-tde |
| Gobierno Digital 2030, Principios, Objetivos | urn:tde:kb:gobierno-digital-2030 |
| Glosario, Lexicon | urn:gov:kb:lexicon-wikiguias |
| **LEYES** | |
| Ley 21.180, TDE | urn:tde:kb:ley-21180-tde |
| Ley 19.880, LBPA, Procedimiento Administrativo | urn:tde:kb:ley-19880-procedimiento-administrativo |
| Ley 21.658, SEGDIG (perspectiva legal) | urn:legal:kb:ley-21658-segdig |
| Ley 21.658, Ciberseguridad (perspectiva TDE) | urn:tde:kb:ley-21658-ciberseguridad |
| Ley 21.719, Datos Personales (perspectiva legal) | urn:legal:kb:ley-21719-datos-personales |
| Ley 21.719, Datos Personales (perspectiva TDE) | urn:tde:kb:ley-21719-datos-personales |
| IA, Legislacion (perspectiva legal) | urn:legal:kb:legislacion-ia-chile |
| IA, Legislacion (perspectiva TDE) | urn:tde:kb:legislacion-ia-chile |
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
| Notificaciones (perspectiva gov) | urn:gov:kb:notificaciones |
| Notificaciones, Onboarding | urn:tde:kb:manual-notificaciones-inicio |
| Notificaciones, Integracion Tecnica | urn:tde:kb:manual-integracion-notificaciones |
| SIMPLE | urn:tde:kb:manual-simple-saas |
| SIMPLE, Glosario | urn:tde:kb:glosario-simple |
| Datos.gob | urn:gov:kb:datosgob |
| **ESTRATEGIAS** | |
| Datos Administracion Estado | urn:gov:kb:datos-administracion-estado |
| Estrategia Datos | urn:tde:kb:estrategia-datos |
| Identidad Digital (perspectiva gov) | urn:gov:kb:identidad-digital |
| Identidad Digital (perspectiva TDE) | urn:tde:kb:estrategia-identidad-digital |
| Gobierno Digital 2030 | urn:tde:kb:gobierno-digital-2030 |
| Capacitaciones TDE (perspectiva gov) | urn:gov:kb:capacitaciones-tde |
| Capacitaciones TDE (perspectiva TDE) | urn:tde:kb:estrategia-capacitaciones-tde |
| Sistema TDE 2025 | urn:tde:kb:guia-sistema-tde-2025 |
| **GUIAS** | |
| CPAT, Guia Rapida | urn:tde:kb:guia-rapida-cpat |
| MGDE, Marco Gestion Datos | urn:tde:kb:guia-marco-gestion-datos |
| Cloud Publica | urn:gov:kb:cloud-publica |
| Metadatos Documentos | urn:tde:kb:guia-metadatos-documentos |
| EVALTIC | urn:tde:kb:guia-evaltic |
| Calidad Web | urn:tde:kb:guia-calidad-web |
| Diseno Servicios | urn:tde:kb:guia-diseno-servicios |
| Anonimizacion Datos | urn:tde:kb:guia-anonimizacion-datos |
| Gestion TIC, Orientaciones | urn:tde:kb:guia-gestion-tic |
| Seguridad Ciberseguridad, Guia | urn:tde:kb:guia-seguridad-ciberseguridad |
| Registro Tratamiento Datos, RAT | urn:tde:kb:guia-registro-tratamiento-datos |
| Metodologia Proyectos TIC | urn:tde:kb:guia-metodologia-proyectos |
