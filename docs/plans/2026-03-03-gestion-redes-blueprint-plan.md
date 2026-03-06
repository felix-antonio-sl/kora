# Transformación del Blueprint de Gestión de Redes Asistenciales — Plan de Implementación

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transformar el cheatsheet monolítico (1.740 líneas, calidad 2.9/5) en un corpus multi-archivo KORA/MD de alta calidad (~5.500 líneas, 6 archivos) con profundidad uniforme, KPIs benchmarkeados, tablas IF/THEN, referencias normativas y estructura RAG-optimizada.

**Architecture:** 6 archivos en `knowledge/pro/gestion-redes/` con numeración continua de capítulos (1-36). Cada archivo tiene frontmatter KORA, cada `##` es chunk RAG autosuficiente. PARTE I define marcos genéricos; PARTE III y IV referencian vía URN + deltas.

**Tech Stack:** Markdown (KORA/MD v3.0.0), YAML frontmatter, Python (`scripts/kora index` para catalogar).

**Design doc:** `docs/plans/2026-03-03-gestion-redes-blueprint-design.md`

**Fuente primaria:** `/Users/felixsanhueza/fx_conocimientando/presentacion-suicidio/zz_fuentes/fx_cheat sheet/manual_gestion_redes_cheatsheet.md`

---

## Convenciones de calidad (aplicar en TODOS los tasks)

Cada subsección `###` del blueprint transformado DEBE seguir esta estructura:

```markdown
### N.M Título telegráfico

Párrafo telegráfico de propósito (1-2 líneas máximo, sin prosa introductoria).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| ... | ... |

**Decisiones (IF/THEN):**

| Condición | Acción | Base |
|-----------|--------|------|
| ... | ... | ... |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| ... | ... | ... | ... | ... | ... |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| ... | ... |

Ref: [Norma chilena]; [Guía internacional con año]; [Estándar acreditación].
```

No todas las subsecciones requieren TODOS los bloques — usar los que apliquen. Pero KPI (tabla 6 col) y Ref son obligatorios en toda subsección.

---

## Task 1: Crear directorio y estructura base

**Files:**
- Create: `knowledge/pro/gestion-redes/` (directorio)

**Step 1: Crear directorio**

```bash
mkdir -p /Users/felixsanhueza/Developer/kora/knowledge/pro/gestion-redes
```

**Step 2: Verificar que el directorio knowledge/pro/ existe**

```bash
ls -la /Users/felixsanhueza/Developer/kora/knowledge/pro/
```

Expected: directorio `gestion-redes/` visible.

**Step 3: Commit**

```bash
git add knowledge/pro/gestion-redes
git commit -m "feat(pro): crear directorio knowledge/pro/gestion-redes para blueprint asistencial"
```

---

## Task 2: Escribir 00-indice.md (Mapa + glosario + normativa)

**Files:**
- Create: `knowledge/pro/gestion-redes/00-indice.md`
- Read: fuente primaria (líneas 1-76 del cheatsheet original para front matter, glosario, leyenda)

**Step 1: Escribir el archivo**

El archivo DEBE contener estas 7 secciones `##`:

```
## 1. Propósito y alcance
```
- Qué es el corpus (blueprint operativo de gestión de redes asistenciales)
- Qué NO es (no es manual de procedimientos, no es normativa, no reemplaza guías clínicas)
- Audiencia: alta dirección, jefaturas de unidad, PMO, equipos clínico-operativos, TI
- Principio guía: Cuádruple Meta (experiencia paciente, salud poblacional, costos, bienestar equipo)

```
## 2. Mapa del corpus
```
Tabla con columnas: `Archivo | URN | Capítulos | Dominio | Audiencia primaria`

| Archivo | URN | Capítulos | Dominio |
|---------|-----|-----------|---------|
| 01-gestion-redes-general.md | urn:pro:kb:gestion-redes-general | 1-14 | Framework general: gobernanza, procesos, calidad, digital, finanzas, cambio |
| 02-unidades-asistenciales.md | urn:pro:kb:gestion-redes-unidades | 15-17 | Gestión por tipo de unidad: ambulatorias, hospitalarias, HaH |
| 03-urgencias.md | urn:pro:kb:gestion-redes-urgencias | 18-26 | Red de urgencias: EMS, SUH, protocolos tiempo-dependientes, desastres |
| 04-salud-mental.md | urn:pro:kb:gestion-redes-salud-mental | 27-36 | Red de salud mental: continuidad, crisis, TUS, derechos |
| 05-herramientas-anexos.md | urn:pro:kb:gestion-redes-herramientas | Anexos A-K | KPIs, BPMN, plantillas, FHIR, simulación, modelo de madurez |

```
## 3. Leyenda de formato
```
Explicar las convenciones usadas en todo el corpus:
- Estructura de subsección (propósito telegráfico + tablas)
- Tabla KPI (6 columnas: Indicador/Fórmula/Meta/Benchmark/Fuente/Periodicidad)
- Tabla IF/THEN (Condición → Acción → Base)
- Tabla Riesgos (Riesgo → Mitigación)
- Bloque `Ref:` (normativa chilena + guía internacional + estándar)
- Notación URN para referencias cruzadas entre archivos

```
## 4. Glosario y acrónimos
```
Tabla alfabética con ~80-100 términos. Columnas: `Término | Definición telegráfica`

Incluir al menos: ACLS, APS, ATLS, BCP, BIA, BPMN, BSC, CESFAM, COSAM, CRS, DRG/GRD, DRP, EDIS, EHR/HCE, EMPI, EMS, ESI, FHIR, GES, HaH, HCAHPS, HICS, HL7, HoNOS, IAAS, ICS, IPC, KPI, LIS, LWBS, MCI, METS, NAC, NOC, OKR, PACS, PDSA, PHQ-9, PREM, PROM, RCA, RIS, RPM, RTO/RPO, SAPU, SAR, SLA, SNOMED, SUH, TAT, TUS, UCI, UOCS, VSM.

Cada definición: máximo 1 línea telegráfica.

```
## 5. Marco normativo de referencia
```
Tabla maestra con columnas: `Norma | Tipo | Capítulos impactados | Vigencia | Fuente`

Incluir al menos:
- Ley 19.937 (Autoridad Sanitaria)
- Ley 20.584 (Derechos y deberes de los pacientes)
- Ley 21.331 (Reconocimiento y protección de derechos personas con enfermedad mental)
- DS 4/2009 (Reglamento de prestadores institucionales)
- DS 38/2005 (Reglamento sobre derechos de los pacientes)
- Norma General Técnica sobre Sistema de Acreditación (Superintendencia de Salud)
- Garantías Explícitas en Salud (GES/AUGE)
- Guías clínicas MINSAL relevantes (IAM, ACV, depresión, etc.)
- Resoluciones exentas MINSAL sobre telemedicina, HCE, interoperabilidad

```
## 6. Contextualización local
```
Plantilla rellenable: tabla con columnas `Instrumento local | Tipo | Estado | Responsable | Observaciones`

Incluir filas ejemplo para: convenios de red, SLA regionales, resoluciones del Servicio de Salud, acuerdos COMGES.

```
## 7. Control de versiones
```
Tabla SemVer: `Versión | Fecha | Cambios | Autor`
- v1.0.0: 2025-09-25 — Cheatsheet original monolítico
- v2.0.0: 2026-03-03 — Transformación KORA/MD: multi-archivo, profundización uniforme, estructura RAG

**Step 2: Verificar frontmatter**

```bash
head -18 knowledge/pro/gestion-redes/00-indice.md
```

Expected: frontmatter YAML válido con `urn: "urn:pro:kb:gestion-redes-indice"`

**Step 3: Verificar estructura de headings**

```bash
grep "^## " knowledge/pro/gestion-redes/00-indice.md
```

Expected: 7 secciones `##` numeradas 1-7.

**Step 4: Commit**

```bash
git add knowledge/pro/gestion-redes/00-indice.md
git commit -m "feat(pro): crear 00-indice.md — mapa, glosario y marco normativo del corpus de redes asistenciales"
```

---

## Task 3: Escribir 01-gestion-redes-general.md (PARTE I — cap 1-14)

**Files:**
- Create: `knowledge/pro/gestion-redes/01-gestion-redes-general.md`
- Read: fuente primaria (líneas 79-746 del cheatsheet original)

**Step 1: Escribir el archivo**

Este es el archivo más grande (~1.400 líneas). Contiene 14 capítulos con ~70 subsecciones.

**Mapping de capítulos:**

| Cap nuevo | Título | Origen en cheatsheet | Subsecciones |
|-----------|--------|---------------------|-------------|
| 1 | Fundamentos y marco conceptual | Cap 1 (líneas 81-117) | 1.1-1.5 |
| 2 | Gobernanza y arquitectura decisional | Cap 2 (líneas 119-154) | 2.1-2.5 |
| 3 | Planificación estratégica de la red | Cap 4 (líneas 193-228) | 3.1-3.5 |
| 4 | Integración clínica y continuidad | Cap 5 (líneas 230-265) | 4.1-4.5 |
| 5 | Gestión por procesos y mejora | Cap 6 (líneas 267-302) | 5.1-5.5 |
| 6 | Acceso, demanda y listas de espera | Cap 7 (líneas 304-339) | 6.1-6.5 |
| 7 | Capacidad, recursos y programación | Cap 8 (líneas 341-376) | 7.1-7.5 |
| 8 | Operación y coordinación en tiempo real | Cap 9 (líneas 378-413) | 8.1-8.5 |
| 9 | Personas, liderazgo y cultura | Cap 10 (líneas 415-450) | 9.1-9.5 |
| 10 | Calidad, seguridad y gestión de riesgos | Cap 11 (líneas 452-487) + Cap 16 (líneas 637-672) | 10.1-10.10 (fusión) |
| 11 | Salud digital e interoperabilidad | Cap 12 (líneas 489-524) | 11.1-11.5 |
| 12 | Datos, indicadores, desempeño y madurez | Cap 13 (líneas 526-561) + Cap 17 (líneas 674-709) | 12.1-12.10 (fusión) |
| 13 | Finanzas y cadena de suministro | Cap 14 (líneas 563-598) | 13.1-13.5 |
| 14 | Gestión del cambio e implementación | Cap 15 (líneas 600-635) + Cap 18 (líneas 711-746) | 14.1-14.10 (fusión) |

**Instrucciones de transformación por sección:**

Para CADA una de las ~70 subsecciones:

1. Leer el contenido telegráfico original (Objetivo/Cómo/Entregables/KPI/Riesgos)
2. Expandir a la estructura de calidad definida en las convenciones del plan:
   - Párrafo telegráfico de propósito
   - Tabla de componentes con detalle operativo
   - Tabla IF/THEN donde haya decisiones
   - Tabla KPI con 6 columnas (agregar benchmarks internacionales y metas sugeridas)
   - Tabla de riesgos (Riesgo/Mitigación)
   - Bloque `Ref:` con normativa + guía internacional
3. Para capítulos fusionados (10, 12, 14): integrar orgánicamente el contenido de ambos capítulos originales; no yuxtaponer

**Capítulos que requieren atención especial:**

- **Cap 4 (Integración clínica):** §4.3 Gestión de transiciones (alta segura) — tabla IF/THEN por tipo de alta (médica, SUH, HaH, psiquiátrica). Referenciar HaH vía URN a `urn:pro:kb:gestion-redes-unidades`.
- **Cap 10 (Calidad + riesgos):** Fusionar calidad del paciente (PDSA, seguridad medicamento, EA, PROMs) con gestión de riesgos (BIA, BCP/DRP, HICS, simulacros). Este capítulo es el marco genérico que PARTE III y IV referenciarán.
- **Cap 11 (Salud digital):** Marco genérico de HIS/EHR, FHIR, telemedicina, IA, gobierno de datos. Las PARTEs III y IV solo agregarán deltas (EDIS, telepsiquiatría, etc.).
- **Cap 14 (Cambio + implementación):** Fusionar metodologías de cambio (ADKAR, Lean-Agile) con implementación por etapas (30-60-90, MVP, hitos). Resultado: un capítulo cohesivo de "cómo llegar de aquí a allá".

**Step 2: Verificar estructura**

```bash
grep "^## \|^### " knowledge/pro/gestion-redes/01-gestion-redes-general.md | wc -l
```

Expected: ~84 headings (14 `##` + ~70 `###`).

```bash
grep "^## " knowledge/pro/gestion-redes/01-gestion-redes-general.md
```

Expected: 14 capítulos numerados 1-14.

**Step 3: Verificar que no hay prosa introductoria (grasa KORA/MD)**

```bash
grep -i "en esta sección\|a continuación\|como se mencionó\|cabe destacar\|es importante" knowledge/pro/gestion-redes/01-gestion-redes-general.md
```

Expected: 0 resultados.

**Step 4: Verificar KPIs con benchmarks**

```bash
grep -c "| Indicador |" knowledge/pro/gestion-redes/01-gestion-redes-general.md
```

Expected: ≥14 tablas KPI (al menos 1 por capítulo).

**Step 5: Commit**

```bash
git add knowledge/pro/gestion-redes/01-gestion-redes-general.md
git commit -m "feat(pro): crear 01-gestion-redes-general.md — PARTE I con 14 capítulos profundizados"
```

---

## Task 4: Escribir 05-herramientas-anexos.md (PARTE V — Anexos A-K)

**Files:**
- Create: `knowledge/pro/gestion-redes/05-herramientas-anexos.md`
- Read: fuente primaria (líneas 1524-1740 del cheatsheet original)

**Razón del orden:** Este archivo se escribe ANTES que 02, 03 y 04 porque contiene los KPIs centralizados y plantillas que esas partes referencian.

**Step 1: Escribir el archivo**

11 anexos con el siguiente contenido:

**Anexo A — Catálogo de KPI:**
- A.1 KPI de red general (~20 KPIs)
- A.2 KPI de urgencias (~20 KPIs)
- A.3 KPI de salud mental (~15 KPIs)
- A.4 KPI de hospitalización domiciliaria (~10 KPIs)
- A.5 KPI transversales (calidad, digital, finanzas) (~15 KPIs)

Cada KPI en tabla de 6 columnas: `Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad`

**Anexo B — Mapas de procesos (BPMN textual):**
5 diagramas de flujo en formato textual con swimlanes por rol:
1. Flujo completo SUH (pre-arribo → triaje → circuitos → destino)
2. Referencia / contrarreferencia (APS ↔ especialidad ↔ hospital)
3. Alta segura (planificación → educación → seguimiento)
4. Crisis de salud mental (detección → intervención → estabilización → seguimiento)
5. Admisión HaH (screening → admisión → tratamiento → egreso)

Formato textual por swimlane:
```
[ROL] Acción → Decisión? → Sí: Acción A / No: Acción B → Siguiente
```

**Anexo C — Plantillas operativas:**
- C.1 SLA inter-nodos: 2 plantillas YAML completadas (ACV + HaH, ya existentes; agregar 1 más: derivación SM)
- C.2 Matriz RACI: tabla CSV con ~10 actividades clave
- C.3 Checklist de apertura de servicios: expandido a ~15 ítems con categorización
- C.4 Estructura SOP/WI: plantilla con campos completados como ejemplo

**Anexo D — Salud digital:**
- Perfiles FHIR recomendados (tabla: Recurso → Uso → Perfil)
- Patrón de integración (eventos clínicos → cola → consumidores)
- Terminologías (tabla: Dominio → Estándar → Ejemplo)
- Ciberseguridad (checklist de 10 controles mínimos)

**Anexo E — Simulación y analítica:**
- Modelado de demanda y colas: parámetros λ, μ, s; fórmulas Wq y ρ
- Simulación SUH: escenarios tipo con parámetros
- Estratificación de riesgo en SM: variables y modelo de priorización

**Anexo F — Infraestructura y diseño funcional:**
- Criterios de superficie/flujo: tabla por tipo de unidad (SUH, SM, HaH)
- Señalética y accesibilidad
- Biocontención y decontaminación

**Anexo G — Cadena de suministro:**
- Listados mínimos por dispositivo: tablas para SUH/EMS, SM, HaH
- Stock crítico: parámetros min/max, FEFO, alarmas
- Mantenimiento: plan PM, KPIs de uptime y MTBF

**Anexo H — Marco normativo (adaptación local):**
- Referencia a 00-indice.md §5 vía URN
- Plantilla de adaptación territorial con filas ejemplo

**Anexo I — Referencias clave:**
- ~30-40 referencias concretas organizadas por dominio
- Formato: `Organización. Título. Año. [URL o identificador]`

**Anexo J — Índice analítico:**
- Tabla: `Palabra clave | Archivo | Sección(es)`

**Anexo K (NUEVO) — Modelo de madurez:**
- Rúbrica por dominio con 5 niveles
- Dominios: gobernanza, integración clínica, calidad, digital, urgencias, salud mental, HaH
- Tabla: `Dominio | Nivel 1 (Inicial) | Nivel 2 (Definido) | Nivel 3 (Estandarizado) | Nivel 4 (Gestionado) | Nivel 5 (Optimizado)`

**Step 2: Verificar conteo de KPIs**

```bash
grep -c "^|" knowledge/pro/gestion-redes/05-herramientas-anexos.md
```

Expected: >200 filas de tabla (KPIs + otras tablas).

**Step 3: Commit**

```bash
git add knowledge/pro/gestion-redes/05-herramientas-anexos.md
git commit -m "feat(pro): crear 05-herramientas-anexos.md — catálogo KPI, BPMN, plantillas, modelo de madurez"
```

---

## Task 5: Escribir 02-unidades-asistenciales.md (PARTE II — cap 15-17)

**Files:**
- Create: `knowledge/pro/gestion-redes/02-unidades-asistenciales.md`
- Read: fuente primaria (líneas 750-995 del cheatsheet, incluyendo HaH)

**Step 1: Escribir el archivo**

3 capítulos con ~31 subsecciones.

**Cap 15 (Unidades ambulatorias y de apoyo) — 14 subsecciones:**

Cada unidad (15.1-15.14) recibe la plantilla completa declarada en el design:

| Sub | Unidad | Detalle especial a profundizar |
|-----|--------|-------------------------------|
| 15.1 | APS/CESFAM/Clínicas comunitarias | Modelo de atención integral, MAIS, cartera APS |
| 15.2 | Centros de especialidad/CRS | Gestión de interconsultas, productividad de box |
| 15.3 | Hospital de día médico/quirúrgico | Selección de casos, criterios ambulatorización |
| 15.4 | Imagenología | RIS/PACS, tiempos de informe, teleradiología |
| 15.5 | Laboratorio clínico y bancos de sangre | TAT, calidad pre-analítica, hemovigilancia |
| 15.6 | Farmacia clínica | Conciliación, alto riesgo, trazabilidad |
| 15.7 | Esterilización (CME) | Flujos sucio-limpio, trazabilidad |
| 15.8 | Rehabilitación/Kinesiología | PROMs funcionales, adherencia |
| 15.9 | Odontología | GES dental, control IPC |
| 15.10 | Atención domiciliaria y paliativos | Distinguir explícitamente de HaH (cap 17) |
| 15.11 | Admisión y OIRS | Identificación, OIRS, reclamos |
| 15.12 | Transporte sanitario programado | Programación, seguridad |
| 15.13 | Docencia e investigación clínica | Ética, campos clínicos |
| 15.14 | Servicios generales | IPC, alimentación, residuos |

**Cap 16 (Unidades hospitalarias) — 7 subsecciones:**

| Sub | Unidad | Detalle especial |
|-----|--------|-----------------|
| 16.1 | Hospitalización médico-quirúrgica | Plan de cuidados, gestión de camas, LOS |
| 16.2 | UCI/UTI/UPC | Ratios, bundles (CVC, VAP, CAUTI), mortalidad ajustada |
| 16.3 | Pabellones/quirófanos | Utilización de sala, cancelaciones, tiempos intraOP |
| 16.4 | Obstetricia y Neonatología | Parto seguro, morbilidad materna severa |
| 16.5 | Pediatría | Seguridad medicamento pediátrico, dosificación |
| 16.6 | Oncología integral | Tiempos sospecha→tratamiento, quimio segura |
| 16.7 | Gestión de camas | Asignación, boarding, altas AM. Vincular con HaH (cap 17) como estrategia de liberación de camas |

**Cap 17 (Hospitalización domiciliaria — HaH) — 10 subsecciones:**

Ya tiene buena profundidad. Aplicar las mismas mejoras de calidad:
- Agregar tablas IF/THEN donde faltan (especialmente en 17.2 elegibilidad y 17.5 vías clínicas)
- Completar benchmarks en KPIs
- Agregar bloques `Ref:` con fuentes concretas (Cochrane 2024, Levine 2019, CMS AHCAH)
- Asegurar que cada `###` es chunk RAG autosuficiente

**Step 2: Verificar que 15.10 distingue explícitamente de HaH**

```bash
grep -A5 "15.10" knowledge/pro/gestion-redes/02-unidades-asistenciales.md | head -6
```

Expected: mención explícita de que atención domiciliaria de baja complejidad ≠ HaH (cap 17).

**Step 3: Commit**

```bash
git add knowledge/pro/gestion-redes/02-unidades-asistenciales.md
git commit -m "feat(pro): crear 02-unidades-asistenciales.md — ambulatorias, hospitalarias y HaH profundizados"
```

---

## Task 6: Escribir 03-urgencias.md (PARTE III — cap 18-26)

**Files:**
- Create: `knowledge/pro/gestion-redes/03-urgencias.md`
- Read: fuente primaria (líneas 1000-1280 del cheatsheet renumerado)

**Step 1: Escribir el archivo**

9 capítulos con ~45 subsecciones.

**Instrucciones especiales:**

1. **Cap 22 (Protocolos críticos):** Cada código tiempo-dependiente recibe tabla de hitos completa:

Para ACV (22.1):
```
| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Door-to-CT | ≤20 min | AHA/ASA 2024: ≤25 min | Enfermería triaje + radiólogo |
| Door-to-needle (IVT) | ≤60 min | AHA: ≤45 min | Neurólogo/médico SUH |
| Door-in-door-out (transferencia) | ≤45 min | AHA 2024 | Equipo SUH |
```

Similar para IAM (22.2), Sepsis (22.3), Trauma (22.4), Paro (22.5), Tóxicos (22.6), Obstétricas/pediátricas (22.7), Crisis SM (22.8).

2. **Cap 20 (Flujo intrahospitalario SUH):** Incluir diagrama de flujo textual completo (pre-arribo → triaje → circuitos → diagnóstico → interconsulta → UOCS → destino). Referenciar BPMN detallado en Anexo B vía URN.

3. **Secciones delta (cap 23, 24, 26):** Estas secciones tratan calidad, tecnología y talento en urgencias. DEBEN:
   - Abrir con referencia explícita al marco genérico de PARTE I: `Marco base: ver [Calidad y seguridad](urn:pro:kb:gestion-redes-general) cap 10. Esta sección agrega los deltas específicos de urgencias.`
   - Solo incluir contenido que sea DIFERENTE o ADICIONAL al marco genérico
   - No repetir lo que ya está en PARTE I

**Step 2: Verificar tablas de tiempos**

```bash
grep -c "Door-to\|FMC-to\|bundle\|≤.*min" knowledge/pro/gestion-redes/03-urgencias.md
```

Expected: ≥15 menciones de hitos tiempo-dependientes.

**Step 3: Verificar referencias delta a PARTE I**

```bash
grep -c "urn:pro:kb:gestion-redes-general" knowledge/pro/gestion-redes/03-urgencias.md
```

Expected: ≥3 referencias URN a PARTE I (en cap 23, 24, 26).

**Step 4: Commit**

```bash
git add knowledge/pro/gestion-redes/03-urgencias.md
git commit -m "feat(pro): crear 03-urgencias.md — protocolos tiempo-dependientes, flujo SUH, desastres"
```

---

## Task 7: Escribir 04-salud-mental.md (PARTE IV — cap 27-36)

**Files:**
- Create: `knowledge/pro/gestion-redes/04-salud-mental.md`
- Read: fuente primaria (líneas 1283-1520 del cheatsheet renumerado)

**Step 1: Escribir el archivo**

10 capítulos con ~40 subsecciones.

**Instrucciones especiales:**

1. **Cap 27 (Arquitectura):** Abrir §27.1 con tabla de principios rectores + base normativa:

```
| Principio | Descripción | Base normativa |
|-----------|-------------|----------------|
| Recuperación | Orientación a la recuperación funcional y personal | Ley 21.331 art. 5 |
| Mínima coerción | Contenciones solo como último recurso, proporcionales y documentadas | Ley 21.331 art. 12 |
| Derechos | Consentimiento informado, dignidad, participación | Ley 20.584 + Ley 21.331 |
| Comunitario | Atención lo más cercana posible al entorno habitual | Plan Nacional SM, OMS mhGAP |
```

2. **Cap 30 (Crisis psiquiátricas):** §30.2 evaluación de riesgo con tabla IF/THEN por nivel:

```
| Nivel de riesgo | Criterios | Acción | Plazo | Dispositivo |
|----------------|-----------|--------|-------|------------|
| Bajo | Ideación pasiva, sin plan, factores protectores presentes | Safety plan + seguimiento APS/COSAM | <7 días | Ambulatorio |
| Moderado | Ideación activa sin plan específico O antecedente de intento | Evaluación psiquiátrica + safety plan + seguimiento intensivo | <24h | COSAM/EMC |
| Alto | Plan definido + acceso a medios + intención declarada | Hospitalización breve o contención terapéutica + restricción de medios | Inmediato | SUH/Unidad SM |
| Inminente | Intento en curso o amenaza inmediata | Intervención de crisis + traslado seguro | Inmediato | EMS/SUH |
```

3. **Cap 33 (Calidad, seguridad y derechos en SM):** §33.2 Prevención del suicidio — profundización:
   - Screening tools: PHQ-9 ítem 9 (umbral ≥1), C-SSRS (niveles 1-5)
   - Safety planning (6 pasos del modelo Stanley-Brown)
   - Contacto post-alta <72h (evidence: reduce mortalidad 30%)
   - Restricción de medios letales
   - Tabla KPI con benchmarks internacionales

4. **Tabla de PROMs estandarizados** en §34:

```
| Instrumento | Dominio | Población | Corte clínico | Cambio significativo | Ref |
|-------------|---------|-----------|---------------|---------------------|-----|
| PHQ-9 | Depresión | Adultos | ≥10 moderada; ≥20 severa | ↓≥5 puntos | Kroenke 2001 |
| GAD-7 | Ansiedad | Adultos | ≥10 moderada | ↓≥4 puntos | Spitzer 2006 |
| HoNOS | Funcionamiento global | Adultos | Por ítem (0-4) | ↓≥2 total | Wing 1998 |
| SDQ | SM infanto-juvenil | 4-17 años | ≥17 anormal | — | Goodman 1997 |
| AUDIT | Consumo alcohol | Adultos | ≥8 riesgo; ≥20 dependencia | — | OMS |
| Zarit | Sobrecarga cuidador | Cuidadores | ≥47 sobrecarga | — | Zarit 1980 |
```

5. **Secciones delta (cap 32, 34, 35):** Mismo patrón que urgencias — referencia URN a PARTE I + solo deltas.

**Step 2: Verificar tabla de riesgo suicida**

```bash
grep -c "Bajo\|Moderado\|Alto\|Inminente" knowledge/pro/gestion-redes/04-salud-mental.md
```

Expected: ≥4 (niveles de riesgo en la tabla IF/THEN).

**Step 3: Verificar Ley 21.331**

```bash
grep -c "21.331" knowledge/pro/gestion-redes/04-salud-mental.md
```

Expected: ≥3 referencias a la ley de derechos de personas con enfermedad mental.

**Step 4: Commit**

```bash
git add knowledge/pro/gestion-redes/04-salud-mental.md
git commit -m "feat(pro): crear 04-salud-mental.md — crisis, suicidio, TUS, derechos con Ley 21.331"
```

---

## Task 8: Verificación cruzada de coherencia

**Files:**
- Read: todos los archivos en `knowledge/pro/gestion-redes/`

**Step 1: Verificar numeración continua de capítulos (1-36)**

```bash
grep "^## [0-9]" knowledge/pro/gestion-redes/0[1-4]*.md | sort -t: -k2 -V
```

Expected: secuencia continua 1, 2, 3, ..., 36 sin saltos ni duplicados.

**Step 2: Verificar que todas las URN internas resuelven**

```bash
grep -oh "urn:pro:kb:gestion-redes-[a-z-]*" knowledge/pro/gestion-redes/*.md | sort -u
```

Expected: solo URNs que correspondan a archivos existentes:
- urn:pro:kb:gestion-redes-indice
- urn:pro:kb:gestion-redes-general
- urn:pro:kb:gestion-redes-unidades
- urn:pro:kb:gestion-redes-urgencias
- urn:pro:kb:gestion-redes-salud-mental
- urn:pro:kb:gestion-redes-herramientas

**Step 3: Verificar que no hay grasa KORA/MD en ningún archivo**

```bash
grep -ri "en esta sección\|a continuación\|como se mencionó\|cabe destacar\|es importante señalar\|por otro lado" knowledge/pro/gestion-redes/*.md
```

Expected: 0 resultados.

**Step 4: Verificar consistencia terminológica**

Verificar que términos clave se usan de forma consistente (no "SUH" en un archivo y "servicio de urgencia" en otro):

```bash
grep -c "SUH\|servicio de urgencia" knowledge/pro/gestion-redes/*.md
```

Expected: "SUH" domina; "servicio de urgencia" solo aparece como definición en glosario.

**Step 5: Contar KPIs totales**

```bash
grep -c "| Indicador |" knowledge/pro/gestion-redes/*.md
```

Expected: ≥40 tablas KPI distribuidas entre los 6 archivos.

**Step 6: Verificar conteo total de líneas**

```bash
wc -l knowledge/pro/gestion-redes/*.md
```

Expected: ~5.000-6.000 líneas totales.

**Step 7: Commit (si hubo correcciones)**

```bash
git add knowledge/pro/gestion-redes/
git commit -m "fix(pro): correcciones de coherencia cruzada en corpus de redes asistenciales"
```

---

## Task 9: Indexar en catálogo KORA y validar

**Step 1: Ejecutar indexador**

```bash
cd /Users/felixsanhueza/Developer/kora && python3 scripts/kora index
```

Expected: 6 nuevos artefactos indexados en `catalog/catalog_master_kora.yml` bajo la sección Knowledge.

**Step 2: Verificar que los URNs aparecen en el catálogo**

```bash
grep "gestion-redes" catalog/catalog_master_kora.yml
```

Expected: 6 entradas con URNs correctos.

**Step 3: Verificar salud del repo**

```bash
python3 scripts/kora health
```

Expected: 0 URNs rotas.

**Step 4: Commit del catálogo actualizado**

```bash
git add catalog/catalog_master_kora.yml
git commit -m "chore(catalog): indexar 6 artefactos de knowledge/pro/gestion-redes"
```

---

## Task 10: Commit final y limpieza

**Step 1: Verificar estado git**

```bash
git status
```

Expected: working tree clean (todo commiteado).

**Step 2: Verificar estadísticas del corpus**

```bash
python3 scripts/kora stats
```

Expected: namespace `pro` muestra incremento de Knowledge artifacts.

**Step 3: Log de commits de la sesión**

```bash
git log --oneline -10
```

Expected: ~6-8 commits limpios correspondientes a Tasks 1-9.

---

## Dependencias entre tasks

```
Task 1 (directorio) ──→ Task 2 (00-indice)
                    └──→ Task 3 (01-general) ──→ Task 4 (05-herramientas)
                                             └──→ Task 5 (02-unidades)  ──┐
                                             └──→ Task 6 (03-urgencias) ──├→ Task 8 (verificación) → Task 9 (indexar) → Task 10 (limpieza)
                                             └──→ Task 7 (04-salud-mental)┘
```

Tasks 5, 6, 7 son independientes entre sí y PUEDEN ejecutarse en paralelo.

---

## Estimación de esfuerzo

| Task | Archivo | Líneas estimadas | Complejidad |
|------|---------|:---:|:---:|
| 1 | directorio | — | Trivial |
| 2 | 00-indice | ~400 | Media (glosario ~100 términos, marco normativo) |
| 3 | 01-general | ~1.400 | Alta (14 capítulos, 70 subsecciones, 3 fusiones) |
| 4 | 05-herramientas | ~800 | Alta (~80 KPIs, 5 BPMN, modelo madurez) |
| 5 | 02-unidades | ~900 | Media-Alta (31 subsecciones, plantilla completa por unidad) |
| 6 | 03-urgencias | ~1.100 | Alta (protocolos tiempo-dependientes, tablas de hitos) |
| 7 | 04-salud-mental | ~900 | Alta (prevención suicidio, IF/THEN riesgo, PROMs, Ley 21.331) |
| 8 | verificación | — | Media (scripts de validación) |
| 9 | indexar | — | Trivial |
| 10 | limpieza | — | Trivial |
