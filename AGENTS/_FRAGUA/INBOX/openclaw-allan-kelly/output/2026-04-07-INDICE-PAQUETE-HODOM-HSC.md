# Paquete de Diseño — Sistema Operativo HODOM HSC

**Fecha:** 2026-04-07
**Autor:** Allan Kelly
**Versión:** 1.0

---

## Contenido del paquete

| # | Documento | Archivo | Tamaño aprox. |
|---|-----------|---------|---------------|
| 0 | **Este índice** | `2026-04-07-INDICE-PAQUETE-HODOM-HSC.md` | — |
| 1 | Identificación de usuarios del sistema (17 usuarios) | `2026-04-07-usuarios-sistema-hodom-hsc.md` | ~16 KB |
| 2 | Historias de usuario núcleo (31 HU, 11 módulos) | `2026-04-07-historias-usuario-hodom-hsc.md` | ~24 KB |
| 3 | Arquitectura de información (modelo de datos, FHIR, flujos, permisos, integraciones) | `2026-04-07-arquitectura-informacion-hodom-hsc.md` | ~19 KB |
| 4 | Wireframes y flujos P0 (16 pantallas) | `2026-04-07-wireframes-flujos-p0-hodom-hsc.md` | ~45 KB |

**Total:** ~104 KB en 5 documentos markdown.

---

## Resumen ejecutivo

Este paquete contiene la especificación completa para construir el sistema operativo de hospitalización domiciliaria del Hospital de San Carlos Dr. Benicio Arzola Medina.

### Cifras clave

- **17 usuarios** identificados (6 clínicos + 3 gestión + 3 red + 3 supervisión + 2 no profesionales)
- **31 historias de usuario** (15 P0 + 12 P1 + 4 P2)
- **11 módulos funcionales**
- **16 pantallas P0** con wireframes textuales detallados
- **43 tablas** del modelo de datos (ERD integrado, 4 capas)
- **25 recursos FHIR R4** mapeados
- **12 variables de ciclo vital** (formulario real HSC)
- **6 tipos de egreso** (coproducto OPM SD1.6)
- **13 estados de visita**
- **5 integraciones externas** (REM/DEIS, APS, gestión de camas, DAU/SGH, laboratorio)
- **12 path equations** implementables como constraints

### Fuentes integradas

- ERD Modelo Integrado HODOM (43 tablas, 4 capas, 87 índices, 6 triggers)
- FHIR R4 Resource References (37 recursos)
- Modelo OPM v2.5 (SD–SD1.6+, 11 hallazgos de auditoría v2.5)
- Modelo Categorial v4.1 (6 categorías, 27 fuentes, datos empíricos HSC 2023-2025)
- DS 1/2022 — Reglamento HODOM
- Decreto Exento 31/2024 — Aprueba Norma Técnica
- Norma Técnica HODOM 2024
- Manual REM 2026 (DEIS/MINSAL)
- Formularios reales HSC (Ingreso Enfermería, Ciclo Vital, Curaciones, Kinesiología, CI 2026, Postulación)
- Datos empíricos HSC 2023-2025 (1698 episodios, 1231 pacientes)

### Secuencia de implementación recomendada

1. **Fase 1 (P0):** 15 HU → episodio completo punta a punta + REM automático
2. **Fase 2 (P1):** 12 HU → operación diaria real
3. **Fase 3 (P2):** 4 HU → complementos

---

## Cómo usar este paquete

1. Empezar por el **índice** (este documento)
2. Revisar **usuarios** para entender a quién sirve el sistema
3. Revisar **historias de usuario** para entender qué debe hacer
4. Revisar **arquitectura** para entender cómo se estructura
5. Revisar **wireframes** para entender cómo se ve y se navega
6. Pasar a **implementación** sobre el ERD integrado existente
