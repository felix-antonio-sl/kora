---
_manifest:
  urn: "urn:tde:kb:decreto-8-norma-notificaciones"
  provenance:
    source: "https://wikiguias.digital.gob.cl/Normas/Decreto8"
version: 1.0.0
status: published
tags: [tde, lineamientos-normas, decreto, norma-tecnica, notificaciones, casilla-unica, domicilio-digital-unico]
lang: es
---

# Decreto 8 — Norma Técnica de Notificaciones

> Promulgación: 19-MAY-2023 | Publicación: 17-AGO-2023 | Versión: Única

## Encabezado

**Bases legales:**

| Instrumento | Materia |
|-------------|---------|
| DS Nº 100/2005 SEGPRES (CPR arts. 32 Nº6 y 35) | Constitución Política |
| Ley Nº 19.880 | Bases procedimientos administrativos |
| Ley Nº 18.993 | Crea MINSEGPRES |
| Ley Nº 19.477 | Ley Orgánica del Servicio de Registro Civil e Identificación |
| Ley Nº 19.628 | Protección de la vida privada |
| Ley Nº 21.180 | Transformación Digital del Estado |
| DFL Nº 1/2020 MINSEGPRES | Gradualidad implementación ley 21.180 |
| DFL Nº 1/2000 Ministerio de Justicia | — |
| DS Nº 4/2020 MINSEGPRES | Reglamento medios electrónicos (en adelante "el Reglamento") |
| Resolución Nº 7/2019 CGR | Exención toma de razón |

**Considerando (síntesis):** Ley 21.180 obliga a practicar notificaciones por medios electrónicos en base a un registro. Mesa Técnica de Notificaciones con participación de SRCeI, SII, Tesorería, Hacienda y Gobierno Digital. Consulta ciudadana dic. 2021. DS anterior retirado en abr. 2022 para revisión. [→ Artículos 1, 22]

---

## Disposiciones generales

### Artículo 1 — Objeto

Detallar el funcionamiento de la **Plataforma de Notificaciones** y establecer la forma en que los órganos de la Administración del Estado practicarán notificaciones electrónicas, en base a la información del **Registro de Domicilios Digitales Únicos (DDU)**, dependiente del Servicio de Registro Civil e Identificación (art. 46 ley Nº 19.880).

### Artículo 2 — Definiciones

| Término | Definición |
|---------|-----------|
| **Domicilio Digital Único (DDU)** | Medio electrónico determinado por una persona para recibir notificaciones electrónicas: puede ser la Casilla Única o un correo electrónico. |
| **Plataforma de Notificaciones** | Plataforma electrónica a través de la cual se practican las notificaciones electrónicas de los órganos del Estado. |
| **Reglamento** | DS Nº 4/2020 MINSEGPRES. |
| **Servicios Web** | Servicios informáticos automatizados con estándares y protocolos que permiten interoperabilidad de datos. |
| **Usuarios(as)** | Interesados(as) en un procedimiento administrativo y funcionarios(as) que acceden a plataformas que lo soportan. |

---

## Registro de Domicilios Digitales Únicos

### Artículo 3 — Registro de Domicilios Digitales Únicos

El **Registro de DDU** (dependiente del SRCeI, art. 46 ley Nº 19.880 y art. 20 del Reglamento) contendrá al menos:

1. Tipo de persona (natural o jurídica) y su RUN o RUT.
2. DDU vigente determinado por la persona.
3. Historial de cambios de DDU, con fecha y detalle.
4. Constancia de excepción a notificación electrónica, cuando corresponda (arts. 28 y ss. del Reglamento), mediante el módulo institucional o directamente ante el SRCeI.

---

## Componentes de la Plataforma de Notificaciones

### Artículo 4 — Componentes de la Plataforma de Notificaciones

| Componente | Descripción |
|-----------|------------|
| **1. Casilla Única** | DDU opcional; permite acceder a notificaciones en bandeja centralizada (→ Artículo 6). |
| **2. Módulo institucional** | Permite a cada órgano: (i) enviar notificaciones, (ii) consultar estados, (iii) registrar solicitudes de notificación no electrónica y su resolución. Disponible para todos los órganos. |
| **3. Componente de envío de mensajes** | Envía notificaciones al DDU determinado. |
| **4. API de notificaciones** | Servicio web para integración automática de plataformas institucionales. |
| **5. Módulo de administración del DDU** | Permite a las personas configurar y modificar su DDU; dispuesto por el SRCeI, conectado vía servicio web. |

> El componente Nº 5 es administrado por el SRCeI. Los componentes 1–4 son administrados por la División de Gobierno Digital del MINSEGPRES.

---

## Configuración y funcionamiento del DDU

### Artículo 5 — Configuración del DDU

- El DDU puede ser **Casilla Única** o **correo electrónico**, a elección del(la) interesado(a).
- La configuración se realiza en el portal web de la Plataforma de Notificaciones, accediendo mediante el mecanismo oficial de autenticación (→ Norma Técnica de Autenticación, art. 57 Reglamento).
- Solo una vez activada la Casilla Única el(la) interesado(a) puede acceder a las notificaciones.
- Para personas jurídicas: al activar la Casilla Única se deben indicar la(s) persona(s) natural(es) autorizadas para acceder a ella.
- El **último DDU determinado** es el vigente.

### Artículo 6 — Bandeja de mensajes de la Casilla Única

Al configurar la Casilla Única como DDU se habilita una bandeja que contiene todas las notificaciones de los procedimientos en que se figure como interesado(a), apoderado(a) o representante, ordenadas por fecha y órgano remitente.

### Artículo 7 — Aviso de notificación

- Con DDU = Casilla Única: el(la) interesado(a) puede configurar un medio electrónico adicional para recibir **avisos** de cada nueva notificación (medios disponibles según guía técnica → Artículo 22).
- Para personas jurídicas: los avisos se envían al correo del representante y/o de los autorizados.
- El aviso es meramente informativo. **No constituye notificación.** Su no recepción no invalida la notificación.

### Artículo 8 — Excepciones a la notificación por medios electrónicos

La solicitud de excepción se realiza por el(la) interesado(a) al órgano correspondiente o directamente al SRCeI, según el Párrafo 2º del Título V del Reglamento. Los órganos que acojan la excepción deben comunicarla al SRCeI mediante el módulo institucional, para actualizar el Registro de DDU.

### Artículo 9 — Notificaciones por medios electrónicos en virtud de leyes especiales

En procedimientos de leyes especiales que normen expresamente notificaciones (art. 3 Nº2 DFL Nº 1/2020 MINSEGPRES): se deberá **enviar copia** de la notificación al DDU. Dicha copia **no sustituye** la forma de notificación de la ley especial. Aplica solo a actos de efecto particular (excluye actos que deban publicarse).

### Artículo 10 — Reconfiguración del DDU

Para cambiar el DDU de Casilla Única a correo electrónico: acceder al módulo de administración del DDU, indicar la dirección de correo y validarla según lo que disponga la guía técnica (→ Artículo 22).

---

## De las notificaciones a través de la Plataforma de Notificaciones

### Artículo 11 — Designación de administrador(a) institucional de la Plataforma de Notificaciones

El(La) Jefe(a) Superior de Servicio (o quien delegue) designará un(a) **administrador(a)** a cargo de gestionar permisos y perfiles para la gestión de notificaciones electrónicas del órgano.

### Artículo 12 — Formas de envío de notificaciones

Los órganos enviarán sus notificaciones electrónicas a la Plataforma mediante alguna de estas formas:

1. **Portal web** del módulo institucional (funcionarios autorizados según art. 11).
2. **API de notificaciones** para envío automático integrado.

### Artículo 13 — Datos para el envío de una notificación

El órgano deberá proporcionar al menos:

1. Código del órgano (del Gestor de Códigos del Estado, → Norma Técnica de Interoperabilidad, art. 57 Reglamento).
2. RUN o RUT del(de la) destinatario(a) (identifica además su DDU).
3. Identificador del expediente electrónico, si corresponde (→ Norma Técnica de Documentos y Expedientes, art. 57 Reglamento).
4. Identificación del procedimiento administrativo (→ Norma Técnica de Interoperabilidad).
5. Tipo de notificación (según guía técnica → Artículo 22).
6. Asunto y descripción de la notificación.
7. Documentos adjuntos o URI persistente (con estándares de la Norma Técnica de Documentos y Expedientes), si corresponde.

### Artículo 14 — Envío de notificaciones

Las notificaciones se envían al DDU del(de la) interesado(a), su apoderado(a) o representante, en base al Registro de DDU y a la información del órgano (→ Artículo 13).

### Artículo 15 — Resultado del envío de la notificación

Cada notificación recibe un **código identificador de transacción** generado por la Plataforma. Los estados posibles son:

1. Notificación enviada exitosamente.
2. Persona exceptuada de notificación electrónica → el órgano debe notificar según arts. 46 incs. 2° y 3° ley Nº 19.880.
3. Persona sin DDU registrado → el órgano notifica según art. 25 inc. 2° del Reglamento.
4. Envío no exitoso → el órgano debe **reenviar** hasta obtener éxito. Si el error es persistente por falla de la Plataforma, debe alertar a la División de Gobierno Digital mediante la Mesa de Ayuda.

### Artículo 16 — Constancia de la fecha y hora de envío y recepción

La Plataforma dejará constancia de: (a) fecha y hora del envío al DDU, (b) fecha y hora de recepción por el(la) destinatario(a), y (c) código identificador de transacción. Esta información se incorpora al certificado digital (art. 26 inc. final del Reglamento). Si el DDU es correo electrónico, se registra solo la fecha y hora de envío (→ Artículo 20).

### Artículo 17 — Datos de trazabilidad de las notificaciones

La Plataforma deberá registrar (art. 26 Reglamento):

1. Información entregada por el órgano para el envío (→ Artículo 13).
2. Estado de las notificaciones (→ Artículo 15).
3. Datos registrados según el artículo precedente.
4. Todos los datos derivados de su operación.

### Artículo 18 — Consulta de estado de envío de notificaciones

Cada órgano debe verificar el estado de envío de sus notificaciones mediante el código identificador de transacción (→ Artículo 15), en cumplimiento del art. 26 del Reglamento.

### Artículo 19 — Constancia de las notificaciones realizadas en dependencias de la Administración

Si la notificación se realiza presencialmente en las dependencias del órgano (art. 23 Reglamento), el(la) funcionario(a) deberá registrar la fecha y hora de la notificación en la Plataforma de Notificaciones.

### Artículo 20 — Correo electrónico como DDU

Cuando el DDU sea un correo electrónico, el(la) interesado(a) debe:

1. Mantener la cuenta habilitada y con capacidad para recibir notificaciones.
2. Revisar la bandeja de correo no deseado.
3. Verificar el remitente mediante el código identificador de transacción.

El(La) interesado(a) recibirá en su correo todas las notificaciones de los procedimientos en que figure como tal.

### Artículo 21 — Interrupción del servicio

En caso de **indisponibilidad** de la Plataforma: emitirá certificado de dicha situación (arts. 47 y 7 finales del Reglamento). Las **mantenciones programadas** se informarán con anterioridad indicando horas o fechas. Las notificaciones no enviadas en el período de incidencia se remitirán al reestablecerse el servicio, registrando fecha y hora de envío.

---

## Disposiciones finales

### Artículo 22 — Guía técnica

La División de Gobierno Digital del MINSEGPRES dictará una o más guías técnicas con los aspectos operativos y procesos de implementación.

### Artículo 23 — Gradualidad

La aplicación es acorde a la gradualidad del DFL Nº 1/2020 MINSEGPRES. La División de Gobierno Digital definirá los lineamientos y formato de cumplimiento para los órganos obligados.

### Artículo 24 — Revisión y actualización de la norma

Revisión y actualización **al menos cada dos años**, contados desde la entrada en vigencia. Las actualizaciones considerarán aprendizajes y dificultades reportados por los órganos, impulsando buenas prácticas y minimizando efectos de prácticas incorrectas.
