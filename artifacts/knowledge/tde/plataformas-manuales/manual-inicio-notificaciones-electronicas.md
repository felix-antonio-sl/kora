---
_manifest:
  urn: "urn:tde:kb:manual-inicio-notificaciones-electronicas"
  provenance:
    source: "https://wikiguias.digital.gob.cl/Manuales/manual-de-inicio-notificaciones"
version: 1.0.0
status: published
tags: [tde, plataformas-manuales, notificaciones, plataforma, manuales]
lang: es
---

# Manual de Inicio — Plataforma de Notificaciones Electrónicas del Estado

Dirigido a funcionarios de los OAE encargados de implementar la Ley de Transformación Digital y a Coordinadores de Transformación Digital.

## Qué es la plataforma

Plataforma electrónica centralizada a través de la cual los OAE envían notificaciones electrónicas a los ciudadanos en sus procedimientos administrativos, a la CasillaÚnica (https://casillaunica.gob.cl).

La Ley N° 21.180 de Transformación Digital del Estado obliga a que todos los procedimientos administrativos sean electrónicos para el año 2027.

**Recursos relacionados:**
- [Resumen sobre la Ley de Transformación Digital del Estado](https://digital.gob.cl/transformacion-digital/estandares-y-guias/guia-resumen-sobre-la-ley-de-transformacion-digital-del-estado/)
- [Norma técnica de Notificaciones](https://www.bcn.cl/leychile/navegar?idNorma=1195121)
- [Manual de Integración](https://docs.google.com/document/d/1YS3ZtH2X2tuQD1lrnaEqRffBjITWjpLGE5Gk6kh-fC8/edit?tab=t.0)

## Límites técnicos de la plataforma

- Archivos adjuntos: hasta 20 MB (un archivo o varios en conjunto).
- Envío por interfaz web: hasta 250 destinatarios por envío.
- Envío por API: hasta 250 destinatarios; límite de transacciones por segundo (TPS) descrito en la [Guía de Integración](https://docs.google.com/document/d/1YS3ZtH2X2tuQD1lrnaEqRffBjITWjpLGE5Gk6kh-fC8/edit?usp=sharing).
- Formatos de archivo adjunto permitidos: PDF (con firma electrónica avanzada y simple), PNG, JPG, JPEG, DOC, DOCX, XLS, XLSX.
- Si se adjuntan PDF firmados electrónicamente, la plataforma valida que las firmas sean válidas.

## Antes de comenzar

### 1. Designar Coordinador/a de Transformación Digital

Toda institución debe tener un Coordinador/a de Transformación Digital oficialmente designado.

**Si la institución aún no ha designado un Coordinador/a:**

1. Tramitar un Oficio dirigido al Director de la Secretaría de Gobierno Digital (Ministerio de Hacienda) indicando a la persona nombrada y su subrogante. Incluir: nombre completo, RUT, email, teléfono de contacto y cargo.
2. Enviar el oficio a través de DocDigital. Si no están habilitados en DocDigital, enviar a: officinapartes@hacienda.gov.cl
3. El Coordinador/a y el/la Subrogante deben registrarse en la Red de Coordinadores adjuntando el oficio de designación: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2643

### 2. Obtener ClaveÚnica

Los funcionarios que utilizarán la plataforma deben contar con ClaveÚnica activa. Activar en el Servicio de Registro Civil e Identificación; sucursales: https://claveunica.cl/sucursales

### 3. Seleccionar procedimientos administrativos a notificar

El procedimiento administrativo debe estar cargado en CPAT (https://cpat.gob.cl/).

**Filtros a aplicar en el CPAT:**

| Campo | Valor requerido |
|-------|-----------------|
| Estado registro | Completado |
| Tipo de usuario/a | Persona natural y jurídica (ambos tipos) |
| Nivel de digitalización | Nivel 3 (recomendado para marcha blanca) |
| Firma electrónica avanzada* | Utiliza FEA provista por externo / FirmaGob / ambas |
| Notificación(es) practicada(s) | Sí |

\* Aplicar criterio de firma solo si la notificación contempla documentos adjuntos firmados electrónicamente.

## Proceso de integración — Paso a paso

1. Designar equipo de contacto institucional: contacto técnico, contacto de negocio y administrador institucional.
2. Solicitar habilitación de la institución en CeroFilas: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2988
3. La SGD habilita a la institución en ambiente demo.
4. La institución realiza configuraciones en ambiente demo según el medio de envío elegido:

| Vía web | Vía API |
|---------|---------|
| Habilitar OAE | Habilitar OAE y recibir credenciales para integración vía API-Certificación y nodo PISEE |

5. Si la SGD tiene observaciones sobre las actividades en ambiente demo, la institución debe realizar las correcciones indicadas.
6. La SGD habilita a la institución en producción.
7. La institución puede comenzar a preparar y enviar notificaciones a la ciudadanía.

## Capacitaciones

Inscripción en capacitaciones de la Plataforma de Notificaciones: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785

## Recursos adicionales

- [Manual del Coordinador/a de Transformación Digital](https://digital.gob.cl/transformacion-digital/estandares-y-guias/manual-para-coordinadores-de-transformacion-digital/)
- [Kit de recursos informativos](https://participacion.digital.gob.cl/es-CL/projects/cmtd-kit-recursos-informativos)
