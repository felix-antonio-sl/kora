---
_manifest:
  urn: "urn:tde:kb:guia-gestion-tic"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/guias/orientaciones-TIC"
version: 1.0.0
status: published
tags: [tic, gestion-tic, institucionalidad, gobierno-digital, tde, guia]
lang: es
---

# Orientaciones básicas para la gestión de TIC

## Objetivo

Guía sobre gestión de sistemas de información y datos para facilitar implementación e inicio de funcionamiento de nuevas instituciones públicas.

## Desafíos TIC de nuevas instituciones

- Tecnología que agregue valor a objetivos estratégicos institucionales
- Facilitar entrega de servicios a personas usuarias
- Cumplimiento normativo y estándares técnicos
- Estrategia TIC alineada con objetivos estratégicos
- Infraestructura tecnológica adecuada (on-premise o nube)
- Gestión de datos con políticas y gobernanza claras
- Personal calificado
- Interoperabilidad con otras entidades del Estado

## Marco institucional para gobierno digital

### Institucionalidad

Ley N° 21.658 crea Secretaría de Gobierno Digital (SGD) en Subsecretaría de Hacienda — órgano rector de TDE desde 01/03/2024. Continuadora legal de ex División de Gobierno Digital de SEGPRES.

**Funciones SGD**:
- Proponer Estrategia de Gobierno Digital al Ministro de Hacienda
- Coordinar implementación de Estrategia con enfoque integrado
- Coordinar, asesorar y apoyar intersectorialmente uso estratégico de tecnologías digitales, datos e información pública
- Desarrollar y operar plataformas y servicios compartidos (interoperabilidad, identidad digital)

**Reglamento regulará**: mecanismos e instrumentos de implementación, monitoreo/seguimiento/evaluación, solicitud de información, otras materias.

### Ley de Transformación Digital del Estado

Ley N° 21.180 (LTDE) — obliga OAE (excepto empresas públicas) a interoperar y gestionar trámites electrónicos antes de diciembre 2027. Régimen gradual de 7 fases (DFL N° 1 de 2020) según madurez digital.

- Reglamento: DS N° 4 de 2020, SEGPRES — tramitación electrónica de procedimientos administrativos
- 6 normas técnicas: interoperabilidad, seguridad, documentos electrónicos, notificaciones, calidad, autenticación

## Estrategia TIC

Elementos esenciales:
1. **Objetivos estratégicos TIC**: largo plazo, relación con objetivos institucionales, contribución de proyectos
2. **Modelo de arquitectura institucional**: arquitectura de referencia, CMDB, estructura hardware/software/redes (on-premise, cloud, IaaS, PaaS, SaaS)
3. **Modelo de planificación TIC**: identificación, priorización y gestión de proyectos TIC. Comité TIC (existencia, composición, funcionamiento)
4. **Evaluación de servicios TIC**: KPIs de servicios, proceso de mejora continua

## Estructura organizacional

Roles y equipos proporcionales al tamaño y complejidad del OAE:

| # | Rol | Función |
|---|-----|---------|
| 1 | Comité TIC | Gestión TIC estratégica por alta dirección. En instituciones pequeñas → Comité de Calidad, Experiencia Usuaria y TDE ([Guía PMG TDE](https://digital.gob.cl/transformacion-digital/estandares-y-guias/guia-metodologica-del-sistema-de-transformacion-digital/)) |
| 2 | Coordinador/a de TDE (CTD) | Enlace con SGD, lidera TDE. Nombrado por máxima autoridad. Registro en https://gobdigital.cerofilas.gob.cl/ |
| 3 | Jefatura TIC | Lidera estrategias y proyectos tecnológicos. Perfil: ingeniería/informática, gestión de proyectos, arquitectura de información, nube |
| 4 | Equipo TIC | Según estrategia: infraestructura (ingenieros nube, operaciones, redes, seguridad), desarrollo (desarrolladores, DBA, UX/UI, QA), analítica (analistas, científicos, ingenieros de datos, SIG) |
| 5 | Oficial de Seguridad | Define políticas, gestiona riesgos, atiende incidentes, cumple regulaciones. Coordina con ANCI |
| 6 | DPO (Encargado/a Protección de Datos) | Cumplimiento normativo, asesoría, capacitación, supervisión, enlace con autoridades |
| 7 | Otras contrapartes | Abogado/a en datos personales/tecnología/TDE + especialista en compras TIC |

## Infraestructura digital básica

| # | Componente | Detalle |
|---|-----------|---------|
| 1 | Nube | Almacenamiento, procesamiento, otros servicios + SIEM |
| 2 | Ofimática | Google Workspace o Microsoft 365 |
| 3 | Gestión documental | SaaS o soluciones públicas — consultar [Pauta de evaluación de gestión documental](https://digital.gob.cl/transformacion-digital/estandares-y-guias/pauta-de-evaluacion-de-sistemas-de-gestion-documental-y-de-expedientes-electronicos-en-el-estado/) |
| 4 | Sistema RRHH | Gestión transaccional de personas (SaaS): remuneraciones, asistencia, permisos, viáticos, vacaciones |
| 5 | Normativa | Servicios BCN, Ley Chile: https://www.bibliotecanacionaldigital.gob.cl/bnd/612/w3-propertyvalue-761831.html |
| 6 | Gestor de proyectos | Asana, Jira, Redmine |
| 7 | Servicios digitales | Seguir [Guía de calidad web](/guias/Guia_Web) para desarrollo/contratación SI |
| 8 | CRM | Cumplimiento SIAC |

## Integración con plataformas transversales SGD

| # | Acción | Detalle |
|---|--------|---------|
| 1 | CPAT | Completar catálogo de procedimientos administrativos en https://cpat.gob.cl/ |
| 2 | Plataformas SGD | **ClaveÚnica**: verificación identidad digital. **FirmaGob**: firma electrónica avanzada funcionarios. **DocDigital**: comunicaciones oficiales, oficinas de partes. **SIMPLE**: digitalización procesos orientados a personas. **PISEE**: interoperabilidad datos/documentos entre OAE. **Notificador**: notificaciones a domicilio digital único |
| 3 | Mesa de Servicios SGD | https://gobdigitalcl.freshdesk.com/support/home |

## Gestión de proyectos TIC

- SGD asesora formulación de proyectos para EVALTIC: https://wikiguias.digital.gob.cl/guias/guias/guia_evaltic
- Guía de gestión de proyectos TIC: https://wikiguias.digital.gob.cl/es/guias/Gestion_de_proyectos_TIC

## Gestión TIC avanzada

1. **Estrategia de datos**: modelo, infraestructura, tecnología, estructura organizacional, datos críticos, datos maestros, interoperabilidad, calidad. Seguir [marco de referencia SGD para gestión de datos](/guias/Gu%C3%ADa_MGDE). Anonimización: [guía introductoria](/guias/Guia_anonimizacion)
2. **Analítica/Big Data/BI**: usar [repositorio de algoritmos públicos](https://www.algoritmospublicos.cl/repositorio) para análisis de línea base
3. **IA**: en marco de [política nacional de IA](https://www.minciencia.gob.cl/areas/inteligencia-artificial/politica-nacional-de-inteligencia-artificial/) — ejes: factores habilitantes, desarrollo y adopción, gobernanza y ética
4. **Datos abiertos**: portal datos.gob.cl para datos requeridos por transparencia. Reduce solicitudes Ley de Transparencia
5. **BCP y DRP**: plan de continuidad operacional + plan de recuperación de desastres
6. **Dashboards**: paneles interactivos con indicadores clave

## Ruta de implementación y priorización

**Criterios de priorización**:
- **Cumplimiento legal primero**: Ley 21.180 y normativas obligatorias
- **Seguridad y ciberseguridad**: continuidad operacional y protección de datos
- **Riesgos operativos**: brechas que ponen en riesgo continuidad de servicios
- **Capacidades internas**: avanzar según disponibilidad y competencias, apoyo externo cuando necesario
- **Flexibilidad**: adaptar ruta según contexto, urgencia y necesidades
