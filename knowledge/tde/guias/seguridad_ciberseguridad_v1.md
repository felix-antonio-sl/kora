---
_manifest:
  urn: urn:tde:kb:seguridad-ciberseguridad
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- seguridad-informacion
- ciberseguridad
- gestion-riesgos
- chile
- tde
lang: es
---

# Guía Técnica de Seguridad de la Información y Ciberseguridad

## Contexto y Alcance
- Apoyo a la Norma Técnica de Seguridad de la Información y Ciberseguridad (Decreto N° 7, 2023) y la Ley 21.180.
- Basada en normas ISO 27000 y el marco NIST.
- Aplica a todos los órganos de la administración del Estado (OAE) para resguardar confidencialidad, integridad y disponibilidad de información y plataformas.


## Política Institucional
- Cada OAE debe aprobar una Política de Seguridad (revisión anual).

- **Diagnóstico**: establecer línea base de activos y riesgos.
- **Clasificación**: categorizar información como Pública, Reservada o Secreta (DS 83/2015).
- **Roles**: definir Dueño del Activo (inventario y clasificación) y Custodio (gestión de accesos).
- **Continuidad**: fijar lineamientos para respaldos, criptografía y eliminación segura.

## Gestión de Riesgos
- Proceso sistemático de identificación, análisis y tratamiento.

- **Apetito al riesgo**: cantidad de riesgo que la institución está dispuesta a asumir.
- **Identificación**: mapear activos, amenazas y consecuencias (incluyendo servicios de terceros).
- **Tratamiento**: Aceptar (dentro de umbral), Mitigar (controles), Transferir (terceros) o Evitar (eliminar fuente).
- **Registro**: bitácora actualizada de riesgos y monitoreo continuo de efectividad.

## Función: Identificación y Gobernanza
- **Inventario**: plataformas, bases de datos y sistemas etiquetados y priorizados.
- **Flujo de datos**: monitorear comunicación entre emisores y receptores.
- **Gobernanza**: coordinar políticas y supervisar cumplimiento legal y regulatorio.

## Función: Protección
- Medidas técnicas y organizativas para la entrega segura de servicios.

- **Servidores**: administración por roles; separación de entornos (dev/prod); sincronización con hora oficial.
- **Redes**: segmentación; uso obligatorio de VPN para acceso externo; MFA para administradores.
- **Credenciales**: modelo de mínimos privilegios; almacenamiento de claves con hash unidireccional.
- **Desarrollo Seguro**: incorporación de seguridad en ciclo de vida (S-SDLC); pautas OWASP; análisis de vulnerabilidades previo a producción.
- **Criptografía**: uso de estándares robustos (AES, RSA, SHA-2/3) para datos en tránsito y reposo.

## Función: Detección y Respuesta
- **Monitoreo**: registro de logs de administradores y eventos de seguridad (retención mínima 12 meses).
- **Detección**: análisis sistemático de anomalías y código malicioso.
- **Respuesta**: planes inmediatos de mitigación y notificación obligatoria a la ANCI/CSIRT de Gobierno.
- **Análisis Forense**: resguardo de evidencia con cadena de custodia para resolución de causa raíz.
- **Recuperación**: planes BCP/DRP para restablecer servicios críticos tras una disrupción.

## Relación con Proveedores
- **SLA**: incluir requisitos de seguridad en contratos de diseño y operación.
- **Cloud**: definir modelo de responsabilidad compartida; asegurar recuperación de datos al término del contrato.
- **Cadena de Suministro**: evaluar riesgos de ciberseguridad en adquisiciones tecnológicas.
