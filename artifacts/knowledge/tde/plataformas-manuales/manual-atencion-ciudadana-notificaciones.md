---
_manifest:
  urn: "urn:tde:kb:manual-atencion-ciudadana-notificaciones"
  provenance:
    source: "https://wikiguias.digital.gob.cl/Manuales/atencion-ciudadana-notificador"
version: 1.0.0
status: published
tags: [tde, plataformas-manuales, notificaciones, casilla-unica]
lang: es
---

# Manual de Atención Ciudadana — Plataforma de Notificaciones

Herramienta de consulta rápida para funcionarios de soporte de los OAE. No está dirigido a ciudadanos.

## Conceptos clave

| Término | Definición |
|---------|------------|
| **CasillaÚnica** | Sitio web oficial del Estado donde las personas reciben notificaciones electrónicas enviadas por los OAE. URL: https://casillaunica.gob.cl |
| **Domicilio Digital Único (DDU)** | Medio electrónico elegido por la persona para recibir notificaciones electrónicas. |
| **Ambiente institucional** | Plataforma donde las instituciones envían notificaciones (interfaz web o API). |
| **Ambiente ciudadano** | Interfaz donde la ciudadanía recibe, consulta y gestiona sus notificaciones. |
| **Marcha blanca** | Periodo de uso voluntario de la plataforma de notificaciones (año 2025). |

## Marco normativo

- Ley N° 21.180 de Transformación Digital del Estado
- Ley N° 19.880, sobre procedimientos administrativos
- Norma Técnica de Notificaciones Electrónicas (Decreto N° 8/2021)

## Flujo de atención en marcha blanca

1. El ciudadano o ciudadana solicita o inicia un procedimiento administrativo ante la institución.
2. La institución solicita autorización al ciudadano para enviar la respuesta a su CasillaÚnica. Comunicar de manera clara los beneficios. *Este paso no será necesario a partir de 2026.*
3. Si el ciudadano acepta: la respuesta se envía a CasillaÚnica. El ciudadano debe ingresar a su casilla para visualizar el mensaje.
4. Si el ciudadano no acepta: la institución notifica por el medio tradicional del procedimiento.

## Consideraciones del uso de CasillaÚnica

| Consideraciones generales | Consideraciones para el ciudadano/a |
|---------------------------|-------------------------------------|
| Plataforma en marcha blanca durante 2025; solo participan instituciones que manifiesten voluntad de incorporarse. | Debe activar su DDU en https://casillaunica.gob.cl |
| El uso de CasillaÚnica por la ciudadanía es voluntario y requiere consentimiento expreso ante la institución. | La falta de activación del DDU no impide que se practiquen las notificaciones. |
| Las notificaciones solo se practicarán cuando el ciudadano haya entregado consentimiento previo. | Al activar CasillaÚnica debe registrar un correo electrónico válido para avisos de nuevas notificaciones. |
| Una vez aceptada la notificación mediante esta plataforma, se entenderá practicada al cumplirse tres días hábiles administrativos desde su envío. | Los usuarios deben usar la plataforma de manera segura y responsable; se prohíbe el acceso no autorizado, alteración de información, propagación de malware y ataques cibernéticos. |
| | En caso de consultas o incidentes, contactar directamente a la institución que lleva el procedimiento a través de sus canales oficiales. |

## Ambientes de la plataforma

| Ambiente institucional (para OAE) | Ambiente ciudadano (para personas) |
|-----------------------------------|------------------------------------|
| Portal Web Institucional y API para integrar en plataformas propias. | Portal Web Ciudadano: www.casillaunica.gob.cl |
| Roles principales: Administrador Institucional y Administrador de Mensajes. | El destinatario activa su DDU para ver sus mensajes. |
| Permite enviar mensajes por interfaz web y API; módulo de estadísticas y consulta. | Estado del DDU (excluyente): no configurado, casilla, correo, excepcionado. El SRCeI mantiene el registro de configuraciones. |

## Ambiente institucional

### Acceso

Ingresar a través del enlace "Acceso a instituciones" ubicado en el pie de página del sitio web, columna central.

### Consulta de configuración del DDU

Antes de enviar una notificación, consultar si el RUN del destinatario tiene DDU configurado:

1. Hacer clic en la sección de consulta DDU.
2. Ingresar hasta 50 RUN en la ventana desplegada.
3. El sistema muestra la configuración de cada RUN al momento de la consulta (puede cambiar en cualquier momento).

### Tipos de configuración del DDU

| Tipo | Descripción |
|------|-------------|
| **DDU no configurado** | Usuario no ha ingresado a la plataforma. |
| **DDU Casilla** | Configuración inicial tras el proceso de activación. |
| **DDU Correo** | Usuario cambió su configuración a correo electrónico. *(no disponible en marcha blanca)* |
| **DDU Excepcionado** | El interesado realizó solicitud al OAE conforme al art. 8 de la Norma Técnica y cumple condiciones de los arts. 28 y 29 del Reglamento. |

### Flujo de notificación según tipo de DDU

| Tipo DDU | Resultado para el ciudadano |
|----------|----------------------------|
| **DDU Casilla** | Recibe correo de aviso y mensaje en bandeja de CasillaÚnica. |
| **DDU Correo** *(no disponible en marcha blanca)* | Recibe mensaje en el correo configurado. |
| **DDU Excepcionado** | No puede ingresar a CasillaÚnica. |
| **DDU no configurado** | Visualiza el mensaje cuando ingrese a CasillaÚnica. |

### Envío de mensajes

- Ver lista de mensajes remitidos por la institución.
- Verificar si el mensaje fue enviado correctamente.
- Consultar la configuración de DDU del destinatario al momento del envío.

### Ver resumen del envío a destinatarios

Disponible en el detalle de un mensaje (opción "Mensajes enviados"): muestra resumen de mensajes enviados con la configuración de DDU por RUN.

### Información disponible en mensajes enviados

- Estado del envío.
- Descripción del estatus.
- Fecha y hora de entrega.
- Fecha y hora de lectura por el ciudadano.

Acceso: opción "Mensajes enviados" o "Mensajes a destinatarios" en el módulo de estadísticas.

## Ambiente ciudadano

### Acceso y activación de CasillaÚnica

URL: https://casillaunica.gob.cl

Pasos de activación:

1. Ingresar con ClaveÚnica.
2. Agregar un correo electrónico de aviso para nuevas notificaciones.
3. Confirmar el correo electrónico.
4. Leer y aceptar los términos y condiciones.
5. Confirmar la activación.
6. Ya es posible ver la CasillaÚnica y revisar notificaciones.

### Secciones de ayuda del sitio

- **¿Qué es DDU?** — https://casillaunica.gob.cl/que-es-ddu/ — información sobre el Domicilio Digital Único.
- **¿Cómo ver mis notificaciones?** — https://casillaunica.gob.cl/como-ver-mis-notificaciones/ — guía rápida para activar el DDU.
- **Ayuda** — https://casillaunica.gob.cl/ayuda/ — preguntas frecuentes para ciudadanía e instituciones.

### Ver mensajes recibidos

Autenticarse con ClaveÚnica en https://casillaunica.gob.cl para visualizar el listado de notificaciones de las instituciones del Estado.

### Menú de CasillaÚnica

- **Bandeja de mensajes:** bandeja principal con notificaciones recibidas, ordenadas de forma descendente por fecha y hora. También existen bandejas "Destacados" y "Archivados".
- **Búsqueda:** buscador y filtros por palabra en el asunto del mensaje.
- **Configuración:** permite cambiar el correo configurado como aviso de notificación.
- **Ayuda:** muestra la sección de preguntas frecuentes.

## Escalamiento de casos

### Consultas frecuentes

| Pregunta | Posibles causas | Respuesta |
|----------|-----------------|-----------|
| No puedo ingresar a CasillaÚnica. | No tiene ClaveÚnica / no recuerda la contraseña. | Solicitar o recuperar ClaveÚnica. |
| Ingresé por primera vez y no veo la bandeja inmediatamente. | Debe registrar correo válido y aceptar términos y condiciones (activar la casilla). | Ingresar a casillaunica.gob.cl y realizar el proceso de activación; solo se muestra una vez. |
| No encuentro un mensaje o veo la bandeja vacía. | No está en la bandeja correcta / fue marcado como archivado. | Cambiar de bandeja; buscar en "Archivados". |
| Configuré un correo en la activación y no veo la notificación con la resolución en ese correo. | El correo configurado recibe solo avisos de mensajes nuevos, no el contenido de la notificación. | Buscar el contenido de la notificación en la bandeja de CasillaÚnica; el correo solo recibe un aviso. |

## Buenas prácticas de atención

- Usar lenguaje claro; evitar tecnicismos.
- No improvisar interpretaciones legales; citar normativa vigente.
- Aclarar que el contenido de la notificación es responsabilidad de la institución emisora, no de la plataforma.
- Evitar frases ambiguas; crear respuestas modelo.
- Confirmar que el ciudadano entendió la acción a seguir.
