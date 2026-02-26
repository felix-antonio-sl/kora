---
_manifest:
  urn: "urn:tde:kb:manual-notificaciones-atencion-ciudadana"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Manuales/atencion-ciudadana-notificador"
version: 1.0.0
status: published
tags: [tde, plataforma, notificaciones, casilla-unica, atencion-ciudadana, ddu, soporte]
lang: es
---

# Manual de atencion ciudadana — Plataforma de Notificaciones

Herramienta de consulta rapida para funcionarios de soporte de OAE. No es material para el ciudadano.

Cada OAE que utilice la plataforma debe responder consultas ciudadanas sobre:
- Funcionamiento basico de CasillaUnica
- Activacion y uso del DDU
- Problemas de acceso o visualizacion de mensajes
- Alcance de notificaciones electronicas segun la Ley
- Tramites y PA notificados por la institucion

## Conceptos clave

| Termino | Definicion |
|---|---|
| CasillaUnica | Plataforma/sitio web oficial del Estado para recibir notificaciones electronicas de OAE |
| DDU (Domicilio Digital Unico) | Medio electronico determinado por persona para recibir notificaciones electronicas |
| Ambiente institucional | Plataforma donde instituciones envian notificaciones (web o API) |
| Ambiente ciudadano | Interfaz donde ciudadania recibe, consulta y gestiona notificaciones |
| Marcha blanca | Periodo de uso voluntario de la plataforma (2025) |

## Marco normativo

- Ley N 21.180 de Transformacion Digital del Estado
- Ley N 19.880 sobre procedimientos administrativos
- Norma Tecnica de Notificaciones Electronicas (Decreto N 8/2021)

Objetivo: modernizar gestion del Estado, garantizar notificaciones seguras, accesibles y verificables.

## Flujo de atencion en marcha blanca

1. Ciudadano/a solicita o inicia PA ante institucion
2. Institucion solicita autorizacion al ciudadano para enviar respuesta a CasillaUnica (paso eliminado a partir de 2026)
3. Si acepta → envio por CasillaUnica. Si rechaza → notificacion por medio tradicional

## Consideraciones de uso

### Generales

- Plataforma en marcha blanca 2025: participacion voluntaria de instituciones
- Uso de CasillaUnica por ciudadania es voluntario (requiere consentimiento expreso)
- Notificaciones solo se practican con consentimiento previo del ciudadano
- Una vez aceptada la notificacion: se entiende practicada a los **3 dias habiles administrativos** desde envio a CasillaUnica

### Para el ciudadano/a

- Activar DDU en casillaunica.gob.cl
- Falta de activacion del DDU no impide notificaciones conforme a cada PA
- Registrar correo electronico valido al activar (usado para avisos de recepcion)
- Uso seguro y responsable; se prohibe: acceso no autorizado, alteracion de informacion, software malicioso, ataques ciberneticos
- Consultas y asistencia: contactar institucion emisora por canales oficiales

## Ambientes de la plataforma

| Aspecto | Ambiente institucional | Ambiente ciudadano |
|---|---|---|
| Destinado a | OAE e instituciones | Personas |
| Valor agregado | Notificar electronicamente | Recibir notificaciones de forma centralizada y segura; definir DDU |
| Medios de uso | Portal web institucional + API | Portal web: www.casillaunica.gob.cl |
| Roles | Adm. Institucional + Adm. Mensajes | Personas naturales y juridicas |
| Funciones principales | Enviar mensajes (web/API), estadisticas, consulta | Activar DDU, ver mensajes, organizar bandeja |

## Ambiente institucional

### Acceso

Enlace en pie de pagina del sitio web, columna central: "Acceso a instituciones".

### Consulta de configuracion DDU

Consultar hasta 50 RUN simultaneos. Muestra configuracion al momento de la consulta (puede cambiar en cualquier momento).

### Tipos de configuracion DDU

| Tipo | Descripcion |
|---|---|
| DDU no configurado | Usuario no ha ingresado a la plataforma |
| DDU Casilla | Estado inicial tras activacion |
| DDU Correo | Configuracion cambiada a correo electronico (no disponible en marcha blanca) |
| DDU Excepcionado | Solicitud aprobada ante OAE segun Norma Tecnica art. 8, Reglamento arts. 28-29 |

### Envio de mensajes segun DDU

| DDU | Correo aviso | Plataforma CasillaUnica |
|---|---|---|
| Casilla | Recibe correo de aviso | Recibe mensaje en bandeja |
| Correo (no disponible MB) | Recibe mensaje en correo configurado | — |
| Excepcionado | No puede ingresar a CasillaUnica | — |
| No configurado | — | Visualizara mensaje cuando ingrese |

### Mensajes enviados

Detalle disponible: estado del envio, descripcion del estatus, fecha/hora de entrega, fecha/hora de lectura. Visible en "Mensajes enviados" y "Mensajes a destinatarios" (estadisticas).

## Ambiente ciudadano

### Acceso y activacion

URL: https://casillaunica.gob.cl

Pasos de activacion:
1. Ingresar con ClaveUnica
2. Agregar correo electronico de contacto (avisos de nuevas notificaciones)
3. Confirmar correo electronico
4. Leer y aceptar terminos y condiciones
5. Confirmar activacion
6. CasillaUnica activa — revisar notificaciones

### Secciones de ayuda

- **Que es DDU**: seccion informativa sobre Domicilio Digital Unico
- **Como ver mis notificaciones**: guia rapida con pasos de activacion
- **Ayuda**: preguntas frecuentes (set ciudadania + set instituciones)

### Menu de CasillaUnica

**Bandejas**: Bandeja de mensajes (principal), Destacados, Archivados. Mensajes ordenados descendente por fecha/hora. Info por registro: fecha/hora, institucion, asunto, adjuntos.

**Busqueda**: buscador por palabra en asunto + filtros complementarios.

**Configuracion**: cambiar correo de aviso de notificacion.

**Ayuda**: seccion de ayuda del producto.

## Atencion y escalamiento de casos

### Consultas frecuentes

| Pregunta | Posibles causas | Respuesta |
|---|---|---|
| No puedo ingresar a CasillaUnica | No tiene ClaveUnica / No recuerda contrasena | Solicitar o recuperar ClaveUnica |
| Ingreso por primera vez y no veo bandeja | Debe activar casilla (registrar correo + aceptar T&C) | Ingresar a casillaunica.gob.cl y completar proceso de activacion (solo una vez) |
| No encuentro un mensaje / bandeja vacia | Bandeja incorrecta / mensaje archivado o destacado | Cambiar de bandeja (archivados, destacados) |
| No veo resolucion en correo configurado | El correo es solo para avisos; contenido esta en CasillaUnica | Buscar notificacion en bandeja de CasillaUnica |

## Buenas practicas de atencion

- Lenguaje claro, evitar tecnicismos
- No improvisar interpretaciones legales; citar normativa vigente
- Aclarar que el contenido de la notificacion es responsabilidad de la **institucion emisora**, no de la plataforma
- Evitar frases ambiguas; crear respuestas modelo
- Confirmar que el ciudadano entendio la accion a seguir
