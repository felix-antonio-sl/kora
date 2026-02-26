---
_manifest:
  urn: "urn:tde:kb:manual-notificaciones-inicio"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Manuales/manual-de-inicio-notificaciones"
version: 1.0.0
status: published
tags: [tde, plataforma, notificaciones, casilla-unica, inicio, marcha-blanca, oae, integracion]
lang: es
---

# Manual de inicio — Plataforma de Notificaciones Electronicas del Estado

Guia para OAE en proceso de marcha blanca de implementacion de la plataforma. Dirigida a funcionarios de OAE encargados de implementacion de Ley de Transformacion Digital y Coordinadores de Transformacion Digital.

## Antecedentes

Ley de Transformacion Digital: todos los PA deben ser electronicos para 2027. Plataforma de Notificaciones Electronicas: canal oficial para que OAE notifiquen a ciudadanos mediante CasillaUnica (https://casillaunica.gob.cl/). Integracion obligatoria para todos los OAE.

## Que es la plataforma

Plataforma electronica centralizada para envio de notificaciones electronicas de OAE en PA que lo requieran.

## Relacion con Ley de Transformacion Digital

Ley 21.180: obligatoriedad de medios electronicos para PA (excepto exclusiones legales).

DFL N1 del Ministerio Segpres y Ley N 21.464 establecen **3 grupos de implementacion** con cronograma por fases. Fase de Notificaciones electronicas: que instituciones notifiquen PA por medios electronicos basados en registro unico.

Recursos normativos:
- Resumen Ley TDE: https://digital.gob.cl/transformacion-digital/estandares-y-guias/guia-resumen-sobre-la-ley-de-transformacion-digital-del-estado/
- Norma Tecnica de Notificaciones: https://www.bcn.cl/leychile/navegar?idNorma=1195121

## Prerequisitos para notificar via CasillaUnica

### Antes de comenzar

1. **Coordinador/a de Transformacion Digital designado** oficialmente
   - Oficio dirigido al Director de SGD del Ministerio de Hacienda
   - Indicar: nombre completo, RUT, email, telefono, cargo (titular + subrogante)
   - Enviar via DocDigital o correo: oficinapartes@hacienda.gov.cl
   - Registrarse en Red de Coordinadores: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2643

2. **Funcionarios con ClaveUnica activa**
   - Activacion en Servicio de Registro Civil e Identificacion
   - Sucursales: https://claveunica.cl/sucursales

3. **Seleccionar PA a notificar** — requisitos:
   - PA cargado en CPAT (si no publicado, informar en proxima apertura)
   - Idealmente con disponibilidad en linea (portal web)
   - Consultar factibilidad con SGD si PA no esta en linea

### Filtros CPAT para seleccion de PA

| Criterio | Valor requerido |
|---|---|
| Estado registro | Completado |
| Tipo de usuario/a | Ambos (persona natural y juridica) o Persona natural |
| Nivel de digitalizacion | Nivel 3 (recomendado para marcha blanca) |
| Firma electronica avanzada* | Provista por externo / FirmaGob / Ambas |
| Notificaciones practicadas | Si |

*Aplicar solo si notificacion contempla documentos firmados electronicamente.

Acceso CPAT: https://cpat.gob.cl/ — descargar Excel y filtrar.

## Proceso de integracion

Dos medios de envio: **via web** y **via API**. En ambos casos: designar administrador institucional + configurar plataforma + pruebas en ambiente demo.

### Paso a paso

1. Designar equipo de contacto: tecnico + negocio + administrador institucional
2. Solicitar habilitacion en CeroFilas: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2988
3. SGD habilita institucion en ambiente demo
4. Configuraciones segun medio:

| Via web | Via API |
|---|---|
| Habilitar OAE | Habilitar OAE + credenciales API-Certificacion + nodo PISEE |

5. Corregir observaciones SGD (si aplica)
6. SGD habilita institucion en produccion
7. Institucion lista para enviar notificaciones

## Consideraciones de uso

- PA debe estar cargado en CPAT
- Adjuntos: hasta 20 MB (un archivo o conjunto)
- Via web: hasta 250 destinatarios por envio
- Via API: hasta 250 destinatarios; TPS y limites en Guia de Integracion
- PDF firmados electronicamente: validacion automatica de firmas
- Formatos adjuntos: PDF (con firma avanzada y simple), PNG, JPG, JPEG, DOC, DOCX, XLS, XLSX

## Capacitaciones

Inscripcion: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785

## Recursos adicionales

- Manual del Coordinador/a de TDE: https://digital.gob.cl/transformacion-digital/estandares-y-guias/manual-para-coordinadores-de-transformacion-digital/
- Kit de recursos informativos: https://participacion.digital.gob.cl/es-CL/projects/cmtd-kit-recursos-informativos
