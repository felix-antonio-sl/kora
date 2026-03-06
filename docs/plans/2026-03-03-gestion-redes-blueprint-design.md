# Design: Transformación del Blueprint de Gestión de Redes Asistenciales

**Fecha:** 2026-03-03
**Autor:** FS + Claude
**Estado:** Aprobado
**URN base:** `urn:pro:kb:gestion-redes-*`

---

## 1. Contexto y problema

El archivo `manual_gestion_redes_cheatsheet.md` (~1.740 líneas, 62 KB) es un índice temático exhaustivo de gestión de redes asistenciales que cubre 4 dominios: gestión general, unidades asistenciales (incl. HaH), urgencias y salud mental. Fue evaluado con puntaje 2.9/5 por las siguientes deficiencias:

| Deficiencia | Impacto |
|-------------|---------|
| Profundidad superficial y uniforme (~4 bullets/sección) | No ejecutable; solo declarativo |
| KPIs sin benchmarks, metas ni fuentes | No permiten medir ni comparar |
| Ausencia de referencias normativas concretas | Sin trazabilidad regulatoria |
| Redundancia entre PARTE I, III y IV | Inflación sin valor; inconsistencia potencial |
| Sin frontmatter ni estructura RAG-friendly | No ingestable en KORA; recuperación pobre |
| Plantillas incompletas (solo estructuras vacías) | No operativas |
| Audiencia demasiado amplia sin diferenciación | No sirve bien a ningún rol |

## 2. Decisiones de diseño

| Decisión | Valor | Razón |
|----------|-------|-------|
| Formato | Blueprint operativo híbrido KORA/MD | Ni spec pura ni KB pura; cumple estándares de calidad KORA |
| Namespace | `pro` (profesional regulado) | Dominio de salud regulado, junto a medico-urgencias |
| Estructura | Multi-archivo por PARTE (6 archivos) | RAG-optimizado, versionable, ~800-1200 líneas/archivo |
| Profundidad | Uniforme profundizada + calidad lógica/técnica/referencial | Todas las ~170 subsecciones al mismo nivel de detalle |
| Consumidor | Knowledge standalone | Accesible por cualquier agente o humano vía RAG |

## 3. Arquitectura de archivos

```
knowledge/pro/gestion-redes/
├── 00-indice.md                     urn:pro:kb:gestion-redes-indice
├── 01-gestion-redes-general.md      urn:pro:kb:gestion-redes-general
├── 02-unidades-asistenciales.md     urn:pro:kb:gestion-redes-unidades
├── 03-urgencias.md                  urn:pro:kb:gestion-redes-urgencias
├── 04-salud-mental.md               urn:pro:kb:gestion-redes-salud-mental
└── 05-herramientas-anexos.md        urn:pro:kb:gestion-redes-herramientas
```

### 3.1 Frontmatter estándar (cada archivo)

```yaml
---
_manifest:
  urn: "urn:pro:kb:gestion-redes-{parte}"
  provenance:
    created_by: "FS"
    created_at: "2026-03-03"
    source: "Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane, NotebookLM 46 fuentes HaH"
version: "2.0.0"
status: draft
tags: [gestion-redes, asistencial, {tags-específicos-por-parte}]
lang: es
---
```

## 4. Contenido por archivo

### 4.1 — 00-indice.md (Mapa + glosario + normativa)

| Sección | Contenido |
|---------|-----------|
| `## 1. Propósito y alcance` | Qué es, qué NO es, audiencia, principio guía (Cuádruple Meta) |
| `## 2. Mapa del corpus` | Tabla: Archivo → URN → Capítulos → Dominio → Audiencia primaria |
| `## 3. Leyenda de formato` | Convenciones: KPI (tabla 6 col), IF/THEN, Ref, Riesgos (tabla) |
| `## 4. Glosario y acrónimos` | ~80-100 términos con definición telegráfica. SSOT: toda definición aquí |
| `## 5. Marco normativo` | Tabla maestra: Norma → Tipo → Capítulos → Vigencia. Centralizado |
| `## 6. Contextualización local` | Plantilla rellenable para alinear con normativa territorial |
| `## 7. Control de versiones` | Tabla SemVer + historial del corpus |

### 4.2 — 01-gestion-redes-general.md (PARTE I)

Reorganización: 18 → 14 capítulos por fusión de redundancias.

| Cap | Título | Origen |
|-----|--------|--------|
| 1 | Fundamentos y marco conceptual | Cap 1 original |
| 2 | Gobernanza y arquitectura decisional | Cap 2 |
| 3 | Planificación estratégica de la red | Cap 4 |
| 4 | Integración clínica y continuidad | Cap 5 |
| 5 | Gestión por procesos y mejora | Cap 6 |
| 6 | Acceso, demanda y listas de espera | Cap 7 |
| 7 | Capacidad, recursos y programación | Cap 8 |
| 8 | Operación y coordinación en tiempo real | Cap 9 |
| 9 | Personas, liderazgo y cultura | Cap 10 |
| 10 | Calidad, seguridad y gestión de riesgos | Cap 11 + 16 (riesgos/BCP fusionados) |
| 11 | Salud digital e interoperabilidad | Cap 12 |
| 12 | Datos, indicadores, desempeño y madurez | Cap 13 + 17 (evaluación/madurez fusionados) |
| 13 | Finanzas y cadena de suministro | Cap 14 |
| 14 | Gestión del cambio e implementación | Cap 15 + 18 (cambio + implementación fusionados) |

**Capítulo eliminado:** Cap 3 (marco normativo) → centralizado en 00-indice.md §5.

### 4.3 — 02-unidades-asistenciales.md (PARTE II)

| Cap | Título | Subsecciones |
|-----|--------|-------------|
| 15 | Unidades ambulatorias y de apoyo | 15.1-15.14 (antes 19.x) |
| 16 | Unidades hospitalarias | 16.1-16.7 (antes 20.x) |
| 17 | Hospitalización domiciliaria (Hospital at Home) | 17.1-17.10 (antes 21.x) |

Mejora: todas las unidades recibirán plantilla completa (Objetivo · Alcance · Cartera · Modelo operativo · Infraestructura · Dotación · Equipamiento · Procesos · Interfaces/SLA · KPI tabla · Riesgos tabla · Digital · Normativa).

### 4.4 — 03-urgencias.md (PARTE III)

| Cap | Título | Origen |
|-----|--------|--------|
| 18 | Arquitectura de la red de urgencias | Cap 22 |
| 19 | Prehospitalario (EMS) | Cap 23 |
| 20 | Flujo intrahospitalario en SUH | Cap 24 |
| 21 | Capacidad y flujo en urgencias | Cap 25 |
| 22 | Protocolos críticos y rutas tiempo-dependientes | Cap 26 |
| 23 | Calidad, seguridad y experiencia en urgencias | Cap 27 (delta sobre cap 10 general) |
| 24 | Tecnología y datos para urgencias | Cap 28 (delta sobre cap 11 general) |
| 25 | Desastres y MCI | Cap 29 |
| 26 | Talento en urgencias | Cap 30 (delta sobre cap 9 general) |

Mejoras: tablas de tiempos por código, diagramas de flujo textual, deltas sobre PARTE I en vez de redundancia.

### 4.5 — 04-salud-mental.md (PARTE IV)

| Cap | Título | Origen |
|-----|--------|--------|
| 27 | Arquitectura de la red de salud mental | Cap 31 |
| 28 | Modelos de atención y continuidad | Cap 32 |
| 29 | Cartera por ciclo vital y poblaciones | Cap 33 |
| 30 | Crisis y urgencias psiquiátricas | Cap 34 |
| 31 | Trastornos por uso de sustancias (TUS) | Cap 35 |
| 32 | Tecnología, datos y privacidad en SM | Cap 36 (delta sobre cap 11) |
| 33 | Calidad, seguridad y derechos en SM | Cap 37 (delta sobre cap 10 + Ley 21.331) |
| 34 | Indicadores y desempeño en SM | Cap 38 (delta sobre cap 12) |
| 35 | Recursos humanos en SM | Cap 39 (delta sobre cap 9) |
| 36 | Financiamiento y sostenibilidad en SM | Cap 40 |

Mejoras: marco de derechos (Ley 21.331), prevención del suicidio profundizada (C-SSRS, safety planning, IF/THEN por nivel de riesgo), tabla de PROMs estandarizados.

### 4.6 — 05-herramientas-anexos.md (PARTE V)

| Anexo | Contenido | Mejora |
|-------|-----------|--------|
| A | Catálogo de KPI (~80-100) | Tabla 6 columnas: Indicador/Fórmula/Meta/Benchmark/Fuente/Periodicidad |
| B | Mapas de procesos (BPMN) | 4-5 flujos textuales: SUH, ref/contraref, alta segura, crisis SM, admisión HaH |
| C | Plantillas operativas | SLA, RACI, checklists, SOP completados (no solo estructura) |
| D | Salud digital | Perfiles FHIR, integración, terminologías, ciberseguridad |
| E | Simulación y analítica | Modelos de demanda/colas, simulación SUH, estratificación SM |
| F | Infraestructura y diseño funcional | Criterios SUH, SM, HaH; señalética; biocontención |
| G | Cadena de suministro | Listados mínimos, stock crítico, mantenimiento |
| H | Marco normativo (adaptación local) | Mapeo leyes, habilitación, convenios — referencia a 00-indice §5 |
| I | Referencias clave | Expandida: ~30-40 referencias concretas con año |
| J | Índice analítico | Palabras clave → URN + sección |
| **K (NUEVO)** | **Modelo de madurez** | Rúbrica 1-5 por dominio con descriptores por nivel |

## 5. Transformaciones transversales de calidad

### 5.1 Telegrafización KORA/MD §5.4

Cada subsección pasa de ~4 bullets declarativos a estructura completa:
- Párrafo telegráfico de propósito (1-2 líneas)
- Tabla de componentes/detalle
- Tabla IF/THEN para decisiones
- Tabla KPI (6 columnas con benchmarks)
- Tabla de riesgos (Riesgo/Mitigación)
- Bloque `Ref:` con normativa + guía internacional

### 5.2 KPIs con benchmarks

Todos los KPIs pasan a tabla: `Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad`

### 5.3 Tablas IF/THEN para lógica decisional

Toda decisión binaria/condicional: `Condición → Acción → Base/Fundamentación`

### 5.4 Eliminación de redundancia inter-PARTE

- PARTE I define marcos genéricos
- PARTE III y IV referencian vía URN + solo agregan deltas específicos
- Regla: si >50% overlap con PARTE I, reemplazar por referencia + delta

### 5.5 Referencias normativas concretas

Cada sección incluye bloque `Ref:` con:
- Norma chilena (Ley, DS, Resolución MINSAL, Norma Técnica)
- Guía internacional (con año y organización)
- Estándar de acreditación relevante

### 5.6 Coherencia interna

- Numeración continua cross-archivo (1-36 capítulos totales)
- Referencias cruzadas vía URN
- Glosario centralizado en 00-indice (SSOT)
- Terminología unificada (términos iguales en todo el corpus)

### 5.7 Cada `##` como chunk RAG autosuficiente

Cada sección `##` incluye contexto mínimo para ser recuperada aisladamente: sujeto explícito, alcance, no depende de secciones anteriores para ser entendida.

## 6. Estimación de tamaño

| Archivo | Líneas estimadas | Capítulos |
|---------|:---:|:---:|
| 00-indice | ~400 | — |
| 01-general | ~1.400 | 14 (×~5 subsecciones) |
| 02-unidades | ~900 | 3 (×~10 subsecciones) |
| 03-urgencias | ~1.100 | 9 (×~5 subsecciones) |
| 04-salud-mental | ~900 | 10 (×~4 subsecciones) |
| 05-herramientas | ~800 | 11 anexos |
| **Total** | **~5.500** | **36 cap + 11 anexos** |

Factor de expansión: ~3.2× respecto al original (1.740 → ~5.500 líneas).

## 7. Plan de ejecución (alto nivel)

| Fase | Descripción | Dependencia |
|------|------------|-------------|
| 1 | Crear directorio + 00-indice.md | Ninguna |
| 2 | Transformar 01-general (más grande, define marcos reusados) | Fase 1 |
| 3 | Transformar 05-herramientas (KPIs + plantillas reusadas) | Fase 2 |
| 4 | Transformar 02-unidades | Fases 2-3 |
| 5 | Transformar 03-urgencias | Fases 2-3 |
| 6 | Transformar 04-salud-mental | Fases 2-3 |
| 7 | Verificación cruzada: coherencia, URNs, glosario, numeración | Fases 1-6 |
| 8 | `scripts/kora index` + validación | Fase 7 |

Fases 4-5-6 son independientes entre sí y pueden ejecutarse en paralelo.

## 8. Fuentes del contenido

| Fuente | Alcance | Tipo |
|--------|---------|------|
| Blueprint original v1.0 (cheatsheet) | Estructura base, 40 capítulos, ~170 subsecciones | Primaria |
| NotebookLM (46 fuentes HaH) | Cap 17 (HaH): evidencia, modelos, RPM, vías clínicas, economía | Primaria |
| Investigación académica (Cochrane, Levine, Mount Sinai) | HaH: datos cuantitativos, benchmarks, programas internacionales | Secundaria |
| KORA/MD spec v3.0.0 | Estándares de formato y calidad | Normativa |
| Normativa MINSAL (por agregar durante transformación) | Referencias regulatorias chilenas | Complementaria |
| Guías internacionales (OPS, IHI, NICE, AHRQ, AHA, ESC) | Benchmarks y protocolos por dominio | Complementaria |
