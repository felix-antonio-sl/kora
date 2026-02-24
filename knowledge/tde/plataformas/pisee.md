---
_manifest:
  urn: "urn:tde:kb:pisee"
  provenance:
    created_by: "FS"
    created_at: "2026-02-24"
    source: "wikiguias.digital.gob.cl"
version: "2.0.0"
status: published
tags: [transformacion-digital, pisee, interoperabilidad, plataforma-compartida, chile]
lang: es
---

# Red de Interoperabilidad PISEE

## Definición y Objetivo
PISEE es el servicio compartido que permite el intercambio seguro y trazable de datos, documentos y expedientes electrónicos entre Órganos de la Administración del Estado (OAE). Basada en nodos de interoperabilidad alojados en la infraestructura de cada órgano, elimina la necesidad de solicitar al ciudadano información que el Estado ya posee.

## Nodos de Interoperabilidad
- **Nodo de Desarrollo**: ambiente para pruebas y validación de integraciones técnicas. Solicitado vía CeroFilas por el Coordinador de Transformación Digital (CTD).
- **Nodo de Producción**: habilitado para el consumo y provisión de servicios reales. Requiere cumplimiento estricto de la Norma Técnica de Interoperabilidad (Decreto 12).
- **Funcionalidad**: permite el envío y recepción cifrada de mensajes entre instituciones conectadas a la red nacional.

## Estándares y Obligaciones
- **Integración Obligatoria**: los OAEs deben actuar como consumidores y/o proveedores según su mandato legal.
- **Vía Estándar**: PISEE es el canal oficial para todo intercambio sistemático de información interinstitucional.
- **EVALTIC**: es obligatorio evaluar el uso de PISEE al formular nuevos proyectos de inversión tecnológica.
- **Enfoque Integrado**: alinear las integraciones con la Estrategia de Datos y los marcos de seguridad/ciberseguridad vigentes.

## Gobernanza Operativa
- **Responsables**: el CTD debe formalizar a los administradores técnicos y de negocio ante la SGD.
- **Actualización**: deber de mantener vigentes los servicios publicados en el Catálogo de Servicios de Interoperabilidad y vinculados al CPAT.
- **Capacitación**: asistencia obligatoria a talleres técnicos de consumo y provisión de servicios de información.

## Articulación con el Modelo TDE
- **Plataformas**: PISEE actúa como canal base para otros servicios compartidos (ej. Notificaciones, DocDigital).
- **Trazabilidad**: todas las transacciones deben registrarse en el sistema centralizado de trazabilidad del Estado.
- **Datos Sensibles**: requiere integración con el Gestor de Autorizaciones para validar consentimientos ciudadanos vía ClaveÚnica.
- **Migración**: los OAEs deben transitar de versiones antiguas de PISEE a la nueva red de interoperabilidad según el cronograma del DFL 1/2020.
