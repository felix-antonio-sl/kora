---
_manifest:
  urn: "urn:tde:kb:nt-notificaciones"
  provenance:
    created_by: "FS"
    created_at: "2026-02-24"
    source: "wikiguias.digital.gob.cl"
version: "2.0.0"
status: published
tags: [transformacion-digital, norma-tecnica, notificaciones, ddu, casilla-unica, chile]
lang: es
---

# Norma Técnica de Notificaciones (Decreto 8)

## Objeto y Definiciones
Detalla el funcionamiento de la **Plataforma de Notificaciones** y la obligatoriedad de practicar notificaciones electrónicas para los Órganos de la Administración del Estado (OAE).
- **Domicilio Digital Único (DDU)**: medio electrónico determinado por el usuario para recibir notificaciones (Casilla Única o correo electrónico).
- **Plataforma de Notificaciones**: sistema centralizado administrado por la DGD para la emisión y registro de notificaciones.
- **API de Notificaciones**: servicio web para la integración automática de plataformas institucionales con el sistema de envío nacional.

## Registro de Domicilios Digitales Únicos (DDU)
Administrado por el Servicio de Registro Civil e Identificación.
- **Contenido**: RUT/RUN, DDU vigente, histórico de cambios y situación de excepción legal a la notificación electrónica.
- **Configuración**: los usuarios definen su DDU en el portal oficial autenticándose con ClaveÚnica. El último medio registrado se considera el vigente.

## Componentes del Sistema
- **Casilla Única**: bandeja de mensajes centralizada para ciudadanos y empresas.
- **Módulo Institucional**: interfaz para que funcionarios envíen notificaciones, consulten estados y registren excepciones.
- **Componente de Envío**: motor que despacha los mensajes al DDU correspondiente.
- **Módulo de Administración DDU**: herramienta del Registro Civil para gestión de la identidad digital vinculada al domicilio.

## Proceso de Notificación
Los OAEs deben proporcionar datos mínimos para cada envío:
- Código de institución (Gestor de Códigos).
- RUN/RUT del destinatario.
- Identificador de expediente (IUIe) y del procedimiento.
- Documentos adjuntos o enlaces (URI) persistentes.
- **Resultado**: la plataforma asigna un código de transacción e informa estados (Enviado, Exceptuado, Sin DDU, Error).

## Validez y Trazabilidad
- **Práctica**: se entiende realizada transcurridos 3 días hábiles desde su envío al DDU.
- **Certificación**: el sistema genera automáticamente un certificado digital con fecha/hora de envío y recepción, asegurando integridad.
- **Avisos**: se pueden configurar correos informativos, pero su ausencia no invalida la notificación legal.
- **Leyes Especiales**: en procedimientos con reglas propias, se debe enviar copia al DDU sin sustituir la forma principal legalmente establecida.

## Indisponibilidad y Fallas
- **Contingencia**: ante caídas del sistema, la plataforma emite certificados de incidencia.
- **Regularización**: las notificaciones no enviadas durante la falla deben remitirse inmediatamente tras el restablecimiento del servicio, registrando la nueva fecha/hora.

## Disposiciones Finales
- **Administrador Institucional**: cada OAE debe designar un responsable para gestionar perfiles y permisos de la plataforma.
- **Actualización**: revisión obligatoria de la norma cada 2 años.
- **Gradualidad**: sujeta a las fases del DFL 1/2020 para la Transformación Digital.
