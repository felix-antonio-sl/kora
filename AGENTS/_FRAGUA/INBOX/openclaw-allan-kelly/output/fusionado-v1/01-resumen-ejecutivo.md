# Resumen Ejecutivo — Sistema Operativo HODOM HSC

Hospital de San Carlos Dr. Benicio Arzola Medina | Abril 2026

---

## El problema

La Unidad de Hospitalización Domiciliaria del HSC opera con 20-25 cupos diarios, atiende ~600-850 pacientes/año y genera más de 10.000 visitas anuales. Toda esta operación se sostiene con:

- 8-10 planillas Excel para programación, rutas, llamadas, turnos y estadística
- formularios Google para postulación e ingreso
- registros en papel para ficha clínica, enfermería, kinesiología y curaciones
- redigitación manual del REM A21 cada mes
- sin registro formal de teleatención ni regulación médica a distancia

Esto genera riesgo de pérdida de información clínica, imposibilidad de trazabilidad regulatoria completa, 2-3 días mensuales dedicados a consolidar REM, y dificultad para coordinar 8+ profesionales y 3 móviles diarios.

---

## La propuesta

Un **sistema operativo de hospitalización domiciliaria** que integre en una sola plataforma:

1. Admisión y elegibilidad normativa (DS 1/2022)
2. Ficha clínica electrónica del episodio HODOM
3. Programación y rutas dinámicas
4. Teleatención y regulación con trazabilidad
5. Generación automática de REM A21
6. Registro offline-first para terreno rural

---

## Usuarios identificados: 19

| Grupo | Roles | Cantidad |
|---|---|---|
| Clínico-operativo | Médico AD, médico regulador, enfermeras, TENS, kinesiólogo, fonoaudiólogo, trabajo social, otros | ~12-15 |
| Administrativo-logístico | Coordinación, administrativo, gestor rutas, bodega, conductor, estadístico | ~5-6 |
| Institucional | Dirección Técnica, derivadores hospitalarios, APS/CESFAM | ~10+ |
| Beneficiarios | Pacientes y cuidadores | ~20-30 activos |

---

## MVP: qué reemplaza

| Hoy (manual) | MVP (sistema) |
|---|---|
| Planilla programación mensual | Tablero coordinación en tiempo real |
| Google Form postulación | Módulo admisión con checklist normativo |
| Registros en papel | Ficha clínica electrónica con registro móvil offline |
| Planilla rutas diarias | Agenda con asignación profesional + móvil + ruta |
| Planilla llamadas | Bandeja comunicaciones trazable |
| Redigitación REM mensual | Generación automática desde datos operacionales |
| Sin registro teleatención | Módulo teleatención con trazabilidad clínica |

---

## Métricas de éxito

| Indicador | Hoy | Meta MVP |
|---|---|---|
| Tiempo generación REM | 2-3 días | < 1 hora |
| Registros clínicos en papel | ~80% | < 20% |
| Planillas Excel activas | 8-10 | 0 |
| Trazabilidad de llamadas | parcial | 100% |
| Visitas sin registro formal | ~10-15% | < 2% |
| Tiempo admisión (postulación → episodio) | sin medición | medido y < 12h |

---

## Entregables del paquete

- Diseño de 19 usuarios con necesidades
- 35 historias de usuario priorizadas (P0/P1/P2) con trazabilidad normativa y FHIR
- Matriz RBAC de 14 roles × 7 módulos con CRUD+X
- 16 wireframes de pantallas P0 + formulario visita móvil offline
- Modelo de datos MVP PostgreSQL ejecutable (14 tablas + vistas + funciones REM)
- Arquitectura de información sobre ERD completo (43 tablas)
- Diseño de teleatención con tipos, reglas y escalamiento
- Backlog en 3 fases con métricas de cierre

---

## Siguiente paso

1. Validar con equipo clínico real (coordinadora + médico + enfermera terreno)
2. Decidir stack tecnológico y hosting
3. Construir MVP Fase 1 (estimación: 6-8 semanas con equipo dedicado)
