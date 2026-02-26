---
_manifest:
  urn: "urn:tde:kb:guia-metadatos-documentos"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/guias/Metadatos_Expediente_Electr%C3%B3nico"
version: 1.0.0
status: published
tags: [tde, guia, metadatos, expediente-electronico, documento-electronico, gestion-documental, norma-tecnica]
lang: es
---

# Guía Técnica de Metadatos para Documentos y Expedientes Electrónicos

Estado: BORRADOR.
Base legal: Ley N° 21.180 (TDE) > DS N° 4/2020 (MINSEGPRES) > DS N° 10/2023 (Norma Técnica de Documentos y Expedientes Electrónicos).
Estándares base: ISO 15.489 (gestión de documentos), ISO 23.081 (metadatos para gestión de documentos).
Referencias adicionales: Australian Government Recordkeeping Metadata Standard, e-EMGDE (España).

---

## 1. Fundamentos

Los metadatos describen estructura, contenido y contexto de documentos/expedientes electrónicos. Garantizan: disponibilidad, recuperación, accesibilidad, conservación e interoperabilidad.

Se incorporan progresivamente durante el ciclo de gestión documental: creación > gestión > resguardo/preservación > transferencia al Archivo Nacional.

### Modelo entidad-relación

Entidades: Documento, Expediente, Actor (institución/persona responsable o involucrada), Relación (asociación entre entidades).

### Tipos de metadatos

| Tipo | Descripción |
|------|-------------|
| Obligatorio | Esenciales; deben incorporarse siempre |
| Condicional | Según tipo de documento/expediente y contexto |
| Sugerido | Para descripción más detallada, a criterio del OAE |

Marcas especiales:
- **AN**: requerido por Archivo Nacional para transferencia digital.
- **MU**: campo múltiple (múltiples registros).

Los metadatos son de registro permanente mientras exista el documento/expediente. No deben sobrescribirse.

## 2. Esquema de metadatos — Resumen

| Entidad | Total elementos | Obligatorios | Condicionales | Sugeridos |
|---------|----------------|-------------|---------------|-----------|
| Expediente | 29 | 18 | 5 | 6 |
| Documento | 46 | 12 | 16 | 18 |

## 3. Metadatos para expedientes electrónicos

8 grupos:

### Grupo 1 — Identificación

| N° | Código | Rótulo | Tipo | Oblig. | AN | MU |
|----|--------|--------|------|--------|----|----|
| 1 | MGDEE1_1 | Identificador de expediente | Alfanumérico, automático | Oblig. | SI | - |
| 2 | MGDEE1_2 | Código serie | Alfanumérico, automático | Sugerido | - | - |
| 3 | MGDEE1_3 | Número del expediente | Alfanumérico, automático | Sugerido | - | - |
| 4 | MGDEE1_4 | Estado | Alfanumérico, auto/manual | Sugerido | - | - |
| 5 | MGDEE1_5 | Título del expediente | Texto, manual | Oblig. | SI | - |

### Grupo 2 — Descripción

| N° | Código | Rótulo | Tipo | Oblig. | AN | MU |
|----|--------|--------|------|--------|----|----|
| 6 | MGDEE2_1 | Resumen | Texto, manual | Sugerido | - | - |
| 7 | MGDEE2_2 | Asunto del expediente | Texto, manual | Oblig. | SI | - |

### Grupo 3 — Temporalidad

| N° | Código | Rótulo | Formato | Oblig. | AN |
|----|--------|--------|---------|--------|-----|
| 8 | MGDEE3_1 | Fecha de creación | ISO 8601 (aaaa-mm-dd hh:mm:ss) | Oblig. | SI |
| 9 | MGDEE3_2 | Fecha de finalización | ISO 8601 | Oblig. | SI |

### Grupo 4 — Caracterización documental

| N° | Código | Rótulo | Oblig. |
|----|--------|--------|--------|
| 10 | MGDEE4_1 | Mecanismo de incorporación | Oblig. |
| 11 | MGDEE4_2 | URI de expediente | Oblig. |

### Grupo 5 — Relaciones

**5.1 OAE asociado:**

| N° | Código | Rótulo | Oblig. | AN | MU |
|----|--------|--------|--------|----|----|
| 12 | MGDEE51_1 | Código de OAE productor | Oblig. (GESCODE) | SI | - |
| 13 | MGDEE51_2 | Nombre OAE productor | Condicional | SI | - |
| 14 | MGDEE51_3 | Tipo relación OAE | Oblig. | - | SI |
| 15 | MGDEE51_4 | Código de OAE relacionado | Oblig. (GESCODE) | - | SI |
| 16 | MGDEE51_5 | Nombre OAE relacionado | Condicional | - | SI |

**5.2 Otros actores:**

| N° | Código | Rótulo | Oblig. | MU |
|----|--------|--------|--------|----|
| 17 | MGDEE52_1 | Tipo relación con otros actores | Oblig. | SI |
| 18 | MGDEE52_2 | Tipo de actor relacionado | Oblig. | SI |
| 19 | MGDEE52_3 | RUN/RUT relacionado | Condicional | SI |
| 20 | MGDEE52_4 | Nombre del actor relacionado | Condicional | SI |

**5.3 Indice de documentos asociados:**

| N° | Código | Rótulo | Oblig. | AN | MU |
|----|--------|--------|--------|----|----|
| 21 | MGDEE53_1 | Identificador expediente/documento vinculado | Oblig. | SI | SI |
| 22 | MGDEE53_2 | Fecha de incorporación | Oblig. (ISO 8601) | SI | SI |

### Grupo 6 — Seguridad

| N° | Código | Rótulo | Oblig. | AN |
|----|--------|--------|--------|-----|
| 23 | MGDEE6_1 | Nivel de acceso | Oblig. (GESCODE) | SI |
| 24 | MGDEE6_2 | Fecha fin restricción | Sugerido | - |
| 25 | MGDEE6_3 | Texto advertencia | Sugerido | - |
| 26 | MGDEE6_4 | Información sensible/privada | Oblig. (SI/NO) | - |

### Grupo 7 — Procedimiento administrativo

| N° | Código | Rótulo | Oblig. |
|----|--------|--------|--------|
| 27 | MGDEE7_1 | Código CPAT asociado | Oblig. |
| 28 | MGDEE7_2 | Nombre PA asociado | Condicional |

### Grupo 8 — Versión

| N° | Código | Rótulo | Oblig. |
|----|--------|--------|--------|
| 29 | MGDEE8_1 | Versión MGDEE | Oblig. |

## 4. Metadatos para documentos electrónicos

10 grupos:

### Grupo 1 — Identificación

| N° | Código | Rótulo | Oblig. | AN |
|----|--------|--------|--------|-----|
| 1 | MGDDE1_1 | Identificador | Oblig. | SI |
| 2 | MGDDE1_2 | Código serie | Condicional | SI |
| 3 | MGDDE1_3 | Número del documento | Sugerido | - |
| 4 | MGDDE1_4 | Estado | Sugerido | - |
| 5 | MGDDE1_5 | Versión | Sugerido | - |
| 6 | MGDDE1_6 | Título del documento | Oblig. | SI |
| 7 | MGDDE1_7 | Resolución de captura | Condicional (microforma) | SI |
| 8 | MGDDE1_8 | Nombre archivo asociado | Sugerido | - |

### Grupo 2 — Características técnicas

| N° | Código | Rótulo | Oblig. | AN |
|----|--------|--------|--------|-----|
| 9 | MGDDE2_1 | Tamaño (Kb) | Sugerido | - |
| 10 | MGDDE2_2 | Cantidad de páginas/extensión | Condicional (microforma) | SI |
| 11 | MGDDE2_3 | Formato | Sugerido | - |
| 12 | MGDDE2_4 | Nombre y versión del software | Sugerido | - |

### Grupo 3 — Descripción

| N° | Código | Rótulo | Oblig. | AN |
|----|--------|--------|--------|-----|
| 13 | MGDDE3_1 | Resumen | Sugerido | - |
| 14 | MGDDE3_2 | Palabras claves | Oblig. | SI |
| 15 | MGDDE3_3 | Idioma | Sugerido | - |
| 16 | MGDDE3_4 | Comunas | Sugerido | - |

### Grupo 4 — Temporalidad

| N° | Código | Rótulo | Formato | Oblig. | AN |
|----|--------|--------|---------|--------|-----|
| 17 | MGDDE4_1 | Fecha de creación | ISO 8601 | Oblig. | SI |
| 18 | MGDDE4_2 | Fecha de modificación | ISO 8601 | Oblig. | - |
| 19 | MGDDE4_3 | Fecha de captura | ISO 8601 | Condicional (microforma) | SI |
| 20 | MGDDE4_4 | Cobertura temporal | Fecha | Sugerido | - |

### Grupo 5 — Caracterización documental

| N° | Código | Rótulo | Oblig. | AN |
|----|--------|--------|--------|-----|
| 21 | MGDDE5_1 | Tipo documental | Condicional (GESCODE) | - |
| 22 | MGDDE5_2 | Origen del documento | Condicional (microforma) | SI |
| 23 | MGDDE5_3 | Mecanismo de incorporación | Oblig. (GESCODE) | - |
| 24 | MGDDE5_4 | URI documento externo | Condicional | SI |
| 25 | MGDDE5_5 | Ubicación física referenciado | Condicional | - |
| 26 | MGDDE5_6 | Estado conservación microforma | Condicional (GESCODE) | SI |
| 27 | MGDDE5_7 | Disposición | Sugerido | - |

### Grupo 6 — Relaciones

**6.1 OAE asociada:**

| N° | Código | Rótulo | Oblig. | AN | MU |
|----|--------|--------|--------|----|----|
| 28 | MGDDE61_1 | Código OAE | Oblig. | SI | SI |
| 29 | MGDDE61_2 | Nombre OAE | Condicional | SI | SI |
| 30 | MGDDE61_3 | Tipo relación documento-OAE | Oblig. | SI | SI |

**6.2 Otros actores:**

| N° | Código | Rótulo | Oblig. | AN | MU |
|----|--------|--------|--------|----|----|
| 31 | MGDDE62_1 | Tipo relación con otros actores | Oblig. | SI | SI |
| 32 | MGDDE62_2 | Tipo de actor relacionado | Condicional | - | SI |
| 33 | MGDDE62_3 | Identificación actor (RUN/RUT) | Oblig. | SI | SI |
| 34 | MGDDE62_4 | Nombre del actor relacionado | Condicional | - | SI |

### Grupo 7 — Seguridad

| N° | Código | Rótulo | Oblig. | AN |
|----|--------|--------|--------|-----|
| 35 | MGDDE7_1 | Nivel de acceso | Oblig. | SI |
| 36 | MGDDE7_2 | Fecha fin restricción | Sugerido | - |
| 37 | MGDDE7_3 | Texto advertencia | Sugerido | - |
| 38 | MGDDE7_4 | Información sensible | Sugerido | - |

### Grupo 8 — Firma

| N° | Código | Rótulo | Oblig. | MU |
|----|--------|--------|--------|----|
| 39 | MGDDE8_1 | Tipo firma | Condicional | SI |
| 40 | MGDDE8_2 | Proveedor | Condicional | SI |
| 41 | MGDDE8_3 | Firma electrónica avanzada | Condicional | - |
| 42 | MGDDE84_1 | Nombre/Cargo representación | Condicional | SI |
| 43 | MGDDE84_2 | RUN firmante | Condicional | SI |

### Grupo 9 — Procedimiento administrativo

| N° | Código | Rótulo | Oblig. |
|----|--------|--------|--------|
| 44 | MGDDE9_1 | Código PA asociado (CPAT) | Condicional |
| 45 | MGDDE9_2 | Nombre PA asociado | Condicional |

### Grupo 10 — Versión

| N° | Código | Rótulo | Oblig. |
|----|--------|--------|--------|
| 46 | MGDDE10_1 | Versión MGDDE | Oblig. |

## 5. Codificadores de referencia (GESCODE)

Listas controladas gestionadas por Gestor de Códigos del Estado:
1. Tipo documental
2. Mecanismo de incorporación de documentos
3. Estado de conservación microforma
4. Tipo relación OAE (custodia, autor institucional, gestionador)
5. Tipo relación otros actores (responsable, interesado, autor, destinatario)
6. Tipo actor (ciudadano, empresa, funcionario, otro)
7. Nivel de acceso (público, restringido, reservado, secreto)
8. Origen del documento (repositorio externo, generado internamente, digitalizado)
