---
_manifest:
  urn: urn:tde:kb:catalogo-cpat-nuble
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: "Secretar\xEDa de Gobierno Digital"
version: 2.0.0
status: published
tags:
- transformacion-digital
- cpat
- nuble
- tramites
- madurez-digital
- chile
- tde
lang: es
---

# Catálogo CPAT Ñuble: Madurez de Trámites Digitales

## Resumen de Situación Regional
- Análisis de madurez digital para GORE Ñuble y 15 municipalidades (período 2024–2025).

- **Dominio de Objetos**: predominan *Solicitud/Permiso* y *Certificado/Constancia*.
- **Madurez Crítica**: alta concentración en Niveles 0–1 (presencial o informativo).
- **Brecha Digital**: disparidad entre disponibilidad de URL informativa y canal transaccional real.
- **Autenticación**: baja adopción de ClaveÚnica; uso extendido de mecanismos propios heterogéneos.
- **GORE Ñuble**: núcleo avanzado Nivel 5 (~21%) convive con 50% en Nivel 0.
- **Municipios**: promedio ~3,7% en Nivel 5; más de la mitad en Niveles 0–1. Buenas prácticas en Ninhue y Ñiquén.

## Acciones Inmediatas (Quick Wins)
- Llevar trámites priorizados a **Nivel 3** (formulario + expediente + notificación).
- Foco inicial: top 30–50 trámites de alto volumen/urgencia social.
- Estandarizar autenticación: **ClaveÚnica por defecto**.
- Eliminar/migrar mecanismos de autenticación propios.
- Convertir páginas informativas en flujos transaccionales completos.
- Implementar tablero regional con KPIs de madurez y calidad.

## Metodología de Clasificación
- Dimensiones de análisis para registros CPAT:

- **Objeto**: función central (Solicitud, Certificado, Pago, etc.).
- **Tipo CPAT**: función común o específica.
- **Nivel (0–5)**: grado de digitalización (0: presencial, 5: automatización avanzada).
- **Autenticación**: ClaveÚnica, Tributaria, Propia o Sin autenticación.
- **Canal y URL**: validación de existencia de canal digital y enlace de inicio.

## Tipología de Trámites
1. **Solicitud/Permiso**: autorizaciones, licencias, prórrogas.
2. **Certificado/Constancia**: documentos acreditativos, fe de hechos.
3. **Pago/Arancel**: derechos, cancelaciones, multas.
4. **Beneficio/Subsidio**: postulación a becas, aportes, bonos.
5. **Inscripción/Registro**: matrículas, padrones, actualizaciones.
6. **Reclamo/Transparencia**: OIRS, lobby, acceso a información pública.
7. **Compras/Licitaciones**: proveedores, Mercado Público.
8. **Atención/Orientación**: guías, asesoría sin acto administrativo.

## Implicancias de IA Responsable
- Requisitos para trámites Nivel >=3 con automatización:

- **Riesgo**: identificar decisiones que afecten derechos o elegibilidad.
- **Gobernanza**: exigir revisión humana, explicabilidad y bitácoras de decisión.
- **Transparencia**: rotulado de IA y canales de apelación para el usuario.
- **Calidad**: diccionarios de datos, linaje y pruebas de sesgo.
- **Ciberseguridad**: controles mínimos y gestión de incidentes en automatizaciones.

## Hoja de Ruta 12 Meses
- **0–90 días**: inventario de automatizaciones, matriz de riesgos, limpieza de URLs, estandarización ClaveÚnica.
- **90–180 días**: migración de top 30–50 trámites a Nivel 3; implementación de tablero regional de KPIs.
- **180–365 días**: escalamiento a Niveles 4–5 para trámites estratégicos; auditorías de IA y interoperabilidad avanzada.

## Arquitectura de Solución Objetivo
- **Experiencia**: formularios accesibles, multicanal, con seguimiento de folio.
- **Identidad**: ClaveÚnica y firma electrónica (simple/avanzada).
- **Procesos**: motor BPM con reglas, SLAs e integración a pagos/notificaciones.
- **Datos**: catálogo, diccionarios y tablero de control para auditoría.
- **Interoperabilidad**: validaciones automáticas con terceros y conciliación de pagos.
- **IA**: asistentes de orientación (bajo riesgo) y apoyo a decisión con revisión humana (alto riesgo).

## Riesgos y Mitigaciones
- **R1: Obsolescencia**: validación periódica y monitoreo de enlaces.
- **R2: Autenticación propia**: plan de migración progresiva a ClaveÚnica.
- **R3: Dependencias**: SLAs para servicios externos (pagos/interop).
- **R4: Automatización sin control**: revisión humana obligatoria y auditorías de algoritmos.
- **R5: Brecha municipal**: uso de plantillas regionales y mentoring entre comunas.
