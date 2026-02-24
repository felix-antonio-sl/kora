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
| Principios, Objetivos | urn:tde:kb:principios-objetivos |
| Glosario, Lexicon | urn:gov:kb:lexicon-wikiguias |
| **LEYES** | |
| Ley 21.180, TDE | urn:tde:kb:ley-21180 |
| Ley 19.880, LBPA | urn:tde:kb:ley-19880 |
| Ley 21.658, SEGDIG | urn:legal:kb:ley-21658-segdig |
| Ley 21.719, Datos Personales | urn:legal:kb:ley-21719-datos-personales |
| IA, Legislacion | urn:legal:kb:legislacion-ia-chile |
| **NORMAS TECNICAS** | |
| Dec.10, Documentos Expedientes | urn:tde:kb:nt-documentos-expedientes |
| Dec.12, Interoperabilidad | urn:tde:kb:nt-interoperabilidad |
| Dec.8, Notificaciones | urn:tde:kb:nt-notificaciones |
| Dec.7, Seguridad Ciberseguridad | urn:tde:kb:nt-seguridad-ciberseguridad |
| Dec.9, Autenticacion | urn:tde:kb:nt-autenticacion |
| Dec.11, Calidad Plataformas | urn:tde:kb:nt-calidad-plataformas |
| **PLATAFORMAS** | |
| ClaveUnica | urn:tde:kb:claveunica |
| Notificaciones | urn:gov:kb:notificaciones |
| SIMPLE | urn:tde:kb:simple-saas |
| DocDigital | urn:tde:kb:docdigital |
| PISEE | urn:tde:kb:pisee |
| Datos.gob | urn:gov:kb:datosgob |
| **ESTRATEGIAS** | |
| Datos Administracion Estado | urn:gov:kb:datos-administracion-estado |
| Identidad Digital | urn:gov:kb:identidad-digital |
| Gobierno Digital 2030 | urn:tde:kb:gobierno-digital-2030 |
| Capacitaciones TDE | urn:gov:kb:capacitaciones-tde |
| **GUIAS** | |
| CPAT | urn:tde:kb:cpat-completa |
| MGDE | urn:tde:kb:mgde |
| Cloud Publica | urn:gov:kb:cloud-publica |
| Metadatos Documentos | urn:tde:kb:metadatos-documentos |
| EVALTIC | urn:tde:kb:evaltic |
| Calidad Web | urn:tde:kb:calidad-web |
| Diseno Servicios | urn:tde:kb:diseno-servicios |
| Anonimizacion Datos | urn:tde:kb:anonimizacion-datos |
