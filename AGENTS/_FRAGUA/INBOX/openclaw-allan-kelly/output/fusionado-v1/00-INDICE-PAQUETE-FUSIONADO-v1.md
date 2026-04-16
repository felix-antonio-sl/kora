# Paquete Fusionado v1.0 — Sistema Operativo HODOM HSC

Hospital de San Carlos Dr. Benicio Arzola Medina
Fecha: 2026-04-07
Autores: Allan Kelly (diseño, rigor, trazabilidad) + Ingeniero Fugaz (ejecutabilidad, realismo, RBAC)

---

## Contenido

| # | Archivo | Descripción | Origen |
|---|---------|-------------|--------|
| 00 | `00-INDICE-PAQUETE-FUSIONADO-v1.md` | Este índice | Nuevo |
| 01 | `01-resumen-ejecutivo.md` | Resumen de una página para dirección | IF + AK |
| 02 | `02-usuarios-sistema.md` | 19 usuarios identificados con necesidades | AK + granularidad IF |
| 03 | `03-historias-usuario.md` | 35 HU con CA, FHIR, normativa y prioridad | AK + HU teleatención IF |
| 04 | `04-roles-permisos-rbac.md` | 14 roles × 7 módulos CRUD+X + segregación | IF (superior) |
| 05 | `05-arquitectura-informacion.md` | Modelo datos, FHIR, flujos estado, integraciones | AK + DDL IF |
| 06 | `06-wireframes-flujos-p0.md` | 16 pantallas P0 + formulario visita móvil offline | AK + realismo IF |
| 07 | `07-backlog-mvp.md` | Backlog MoSCoW 3 fases + métricas de éxito | IF + trazabilidad AK |
| 08 | `08-modelo-datos-mvp.sql` | DDL PostgreSQL ejecutable (14 tablas + vistas + funciones REM) | IF |
| 09 | `09-diseno-teleatención.md` | Tipos, reglas, escalamiento, registro | IF |
| 10 | `10-auditoria-comparativa.md` | Cómo se fusionaron ambos paquetes | AK |

## Cifras clave del paquete fusionado

- **19 usuarios** (6 clínicos + 4 gestión + 3 red + 3 supervisión + 3 no profesionales)
- **35 historias de usuario** (17 P0 + 13 P1 + 5 P2)
- **11 módulos funcionales** (agrupables en 7 bounded domains para MVP)
- **16 pantallas P0** + formulario visita móvil offline-first
- **14 tablas MVP** ejecutables + referencia a 43 tablas ERD completo
- **25 recursos FHIR R4** mapeados
- **14 roles RBAC** con CRUD+X + segregación de datos sensibles
- **12 path equations** implementables
- **5 integraciones externas**
- **6 métricas de éxito** con línea base y meta

## Fuentes integradas

- ERD Modelo Integrado HODOM (43 tablas, 4 capas)
- FHIR R4 Resource References (37 recursos)
- Modelo OPM v2.5 (SD–SD1.6+)
- Modelo Categorial v4.1 (6 categorías, 27 fuentes)
- DS 1/2022, Decreto Exento 31/2024, NT 2024
- Manual REM 2026 (DEIS/MINSAL)
- Formularios reales HSC
- Datos empíricos HSC 2023-2025
- Documentación legacy Drive HODOM HSC

## Secuencia de implementación

1. **Fase 1 (P0):** 17 HU → episodio completo punta a punta + REM automático
2. **Fase 2 (P1):** 13 HU → operación diaria real + teleatención + logística
3. **Fase 3 (P2):** 5 HU → analítica + interoperabilidad + optimización
