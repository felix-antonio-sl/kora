---
_manifest:
  urn: urn:tde:kb:nt-autenticacion
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- norma-tecnica
- autenticacion
- clave-unica
- clave-tributaria
- chile
- tde
lang: es
---

# Norma Técnica de Autenticación (Decreto 9)

## Objeto y Definiciones
- Establece cómo los Órganos de la Administración del Estado (OAE) deben implementar mecanismos oficiales de autenticación en sus plataformas para validar identidades con niveles de confianza determinados.

- **Autenticación**: proceso electrónico de validación de datos de identificación para acceso.
- **Factor de Autenticación**: dato reservado o inherente (contraseña, biometría) para establecer identidad.
- **Mecanismo Oficial**: método validado por el Ministerio SEGPRES que cumple esta norma.

## Mecanismos Oficiales Obligatorios
- Los OAEs deben usar mecanismos oficiales, salvo excepciones legales de tramitación electrónica.

- **ClaveÚnica**: para personas naturales. Administrada por SEGPRES/DGD; enrolamiento vía Registro Civil. Basada en OpenID Connect.
- **Clave Tributaria**: para personas jurídicas y agrupaciones sin personalidad jurídica. Administrada por el SII. Prohibido su uso para autenticar personas naturales fuera del SII.

## Estándares Técnicos
- **Protocolos**: OpenID Connect y OAuth 2.0 (o superiores).
- **Cifrado de Almacenamiento**: algoritmos Bcrypt, PBKDF2, SHA-3, Argon2.
- **Cifrado de Transmisión**: TLS v1.2 o superior.
- **Seguridad**: implementación de CAPTCHA, límites de intentos fallidos, bloqueo y desbloqueo seguro.
- **UX**: cumplimiento de lineamientos de marca y estándares de accesibilidad web (WCAG).

## Proceso de Integración
1. Solicitud formal del OAE al administrador del mecanismo (DGD o SII).
2. Aceptación de términos y condiciones por la Jefatura Superior de Servicio.
3. Integración técnica y entrega de credenciales.
4. Certificación y habilitación final.
- **Revocación**: el administrador puede suspender el servicio ante incumplimiento de la norma o fallas de seguridad.

## Obligaciones de los Órganos (OAE)
- **Trazabilidad**: registrar ID de usuario y fecha/hora (sincronizada con SHOA) de cada acceso. Conservar registros por al menos 12 meses.
- **Seguridad**: informar de inmediato al CSIRT de Gobierno ante riesgos o amenazas detectadas.
- **Privacidad**: asegurar cumplimiento de la Ley 19.628 (Protección de la Vida Privada) y derechos ARCO.
- **Niveles de Confianza**: evaluar factores adicionales (MFA) según la criticidad del trámite o sensibilidad de los datos.

## Nuevos Mecanismos
- Los OAEs pueden solicitar a la DGD la oficialización de nuevos métodos.
- Requisitos:

- Procesos de enrolamiento seguros (minimizar suplantación).
- Políticas de privacidad accesibles.
- Soporte técnico a usuarios y gestión de revocación de credenciales.
- Acciones de educación para el uso seguro.

## Disposiciones Finales
- **Actualización**: revisión obligatoria de la norma cada 2 años.
- **Gradualidad**: sujeta a los plazos del DFL 1/2020 para la Transformación Digital.
- **Guías Técnicas**: la DGD emitirá documentos operativos para facilitar la implementación y el uso de mecanismos no oficiales autorizados.
