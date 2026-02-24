---
_manifest:
  urn: urn:tde:kb:simple-saas-oae
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- simple
- saas
- procesos-digitales
- oae
- chile
- tde
lang: es
---

# Guía de Uso de SIMPLE (SaaS) para Órganos del Estado

## Definición y Funcionalidades
- SIMPLE (Sistema de Implementación de Procesos Ligeramente Estandarizados) es un modelador de procesos (BPMS) del Estado para digitalizar trámites de baja complejidad.

- **Capacidades**: modelamiento gráfico, reglas de negocio, diseño de formularios, generación de documentos, firma electrónica (FirmaGob), autenticación (ClaveÚnica) e integración con APIs externas.
- **Objetivo**: facilitar la transición progresiva a procedimientos administrativos electrónicos (Ley 21.180).

## Gobernanza de Ambientes
- **Desarrollo**: entorno para creación, pruebas y aprendizaje. Limpieza anual obligatoria (último día hábil de enero).
- **Producción**: exclusivo para procesos validados y certificados. Prohibido usar para testeo.
- **Migración**: todo paso a producción requiere aprobación previa del equipo de Gobierno Digital.
- **Responsabilidad**: el encargado institucional administra usuarios y resuelve solicitudes internas/externas.

## Almacenamiento y Disponibilidad
- **Archivos (File Transfer)**: borrado automático a los 30 días corridos del ingreso. No hay recuperación tras eliminación.
- **Disponibilidad**: ininterrumpida, salvo mantenciones programadas (aviso previo de 48h a contrapartes técnicas).
- **Caídas Externas**: Gobierno Digital no responde por fallas en servicios de terceros (redes, APIs externas, RCE).

## Uso de la API y Reportería
- **API Compartida**: prohibido generar sobreconsumos que afecten a otros OAEs. No usar acciones REST desde procesos internos para consultar la propia API.
- **Masivos**: consumos de alto volumen sugeridos en horario 00:00 a 05:00 hrs.
- **Reportería**: consultas en backend limitadas a periodos de 6 meses para evitar caídas por volumen. Para históricos, usar API y base de datos propia.

## Procedimientos de Publicación
- **Lanzamiento**: informar a Gobierno Digital con 2 semanas de anticipación vía formulario oficial.
- **Certificación**: obligatoria para garantizar soporte técnico. Procesos no visados son de absoluta responsabilidad del OAE.
- **Modificaciones**: cambios menores requieren actualizar documentación; cambios mayores se consideran procesos nuevos.
- **Correo**: configuración obligatoria de remitente `no-reply@digital.gob.cl` en equipos de TI para evitar SPAM.

## Monitoreo y Soporte
- **Escenarios de Consumo**: si el tráfico afecta la estabilidad, la SGD puede bloquear la URL de la cuenta institucional hasta que se realicen ajustes.
- **Mesa de Ayuda**: canal único de soporte técnico vía digital.gob.cl (Lunes a Viernes, horario hábil).
- **Proveedores**: no existe relación directa SGD-Proveedor. Toda solicitud debe ser emitida por el OAE con correo institucional.
- **Aceptación**: el uso de la cuenta implica la aceptación total de estos términos operativos.
