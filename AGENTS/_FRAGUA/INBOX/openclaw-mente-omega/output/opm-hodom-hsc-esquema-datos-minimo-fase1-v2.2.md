# HODOM HSC
# Esquema de Datos Mínimo — Fase I

Versión: 2.2
Fecha: 2026-04-09
Estado: propuesta inicial de modelado de datos

Propósito: proponer una estructura mínima de datos para Fase I, centrada en:
- Plan de Atención
- Estado del Episodio
- Riesgo Clínico Operacional

No es DDL definitivo. Es una especificación semántica mínima para orientar diseño de datos y conversación técnica.

---

## 1. Principio general

La regla rectora es esta:

**no crear más estructura que la necesaria para volver explícita la columna vertebral del episodio.**

El objetivo no es rediseñar toda la BD.
El objetivo es introducir los mínimos objetos o vistas que permitan consolidar plan, estado y riesgo sin romper el sistema existente.

---

# 2. Objeto 1 — Plan de Atención

## 2.1 Opción semántica recomendada

Tratar el Plan de Atención como objeto principal del episodio.

### Nombre propuesto
`clinical.plan_atencion`

### Clave principal
- `plan_id`

### Clave funcional
- `stay_id`

## 2.2 Campos mínimos sugeridos

| Campo | Tipo lógico | Descripción |
|------|-------------|-------------|
| `plan_id` | UUID | identificador único |
| `stay_id` | UUID/text | episodio al que pertenece |
| `version` | integer | versión del plan |
| `estado` | enum/text | borrador / activo / actualizado / cerrado |
| `objetivo_clinico` | text | objetivo principal del episodio |
| `problema_principal` | text | diagnóstico/problema activo dominante |
| `prestaciones_activas` | json/text | resumen por disciplina |
| `frecuencia_objetivo` | text/json | frecuencia esperada de atención |
| `criterios_monitoreo` | text/json | qué vigilar y cómo |
| `criterios_ajuste` | text/json | cuándo modificar plan |
| `criterios_egreso` | text/json | condiciones de cierre |
| `actualizado_por` | provider_id/user_id | responsable de última actualización |
| `actualizado_en` | timestamp | fecha/hora última actualización |
| `fuente` | text | manual / consolidado / híbrido |

## 2.3 Observación importante

En una primera iteración, `prestaciones_activas`, `frecuencia_objetivo`, `criterios_monitoreo`, `criterios_ajuste` y `criterios_egreso` pueden vivir como JSON o texto estructurado. No hace falta normalizar todo de entrada.

## 2.4 Vista derivada sugerida

Si no se crea tabla inmediatamente, puede existir primero una vista consolidada:

`clinical.v_plan_atencion_actual`

con una fila vigente por `stay_id`.

---

# 3. Objeto 2 — Estado del Episodio

## 3.1 Opción semántica recomendada

No necesariamente crear tabla nueva primero.

Primero crear una capa canónica por vista o campo derivado, y luego decidir si se persiste directamente.

### Nombre sugerido de vista
`clinical.v_estado_episodio_canonico`

## 3.2 Estados sugeridos

- `postulado`
- `elegible`
- `admitido`
- `activo`
- `egresado`
- `cerrado`

## 3.3 Campos mínimos sugeridos

| Campo | Tipo lógico | Descripción |
|------|-------------|-------------|
| `stay_id` | UUID/text | episodio |
| `estado_canonico` | enum/text | estado actual del episodio |
| `estado_fuente` | text | estado original del sistema |
| `tipo_egreso` | text | causal de egreso, si existe |
| `fecha_transicion` | timestamp/date | última transición relevante |
| `origen_estado` | text | derivado / explícito |

## 3.4 Regla recomendada

La primera versión puede ser una vista derivada que mapee `clinical.estadia.estado` y `tipo_egreso` a estado canónico.

Solo si la vista queda corta, pasar a persistencia explícita o event sourcing básico.

---

# 4. Objeto 3 — Riesgo Clínico Operacional

## 4.1 Opción semántica recomendada

Crear una estructura liviana, ligada al episodio.

### Nombre propuesto
`clinical.riesgo_operacional_episodio`

### Clave principal
- `riesgo_id`

### Clave funcional
- `stay_id`

## 4.2 Categorías sugeridas

- `estable`
- `en_observacion`
- `inestable`

## 4.3 Campos mínimos sugeridos

| Campo | Tipo lógico | Descripción |
|------|-------------|-------------|
| `riesgo_id` | UUID | identificador |
| `stay_id` | UUID/text | episodio |
| `categoria_riesgo` | enum/text | categoría vigente |
| `motivo_riesgo` | text | explicación breve |
| `fuente_riesgo` | text | manual / regla / híbrido |
| `actualizado_por` | provider_id/user_id | responsable |
| `actualizado_en` | timestamp | actualización |
| `activo` | boolean | si es el riesgo vigente |

## 4.4 Vista sugerida

`clinical.v_riesgo_episodio_actual`

una fila vigente por `stay_id`.

---

# 5. Relación entre los tres objetos

## Relación principal
Todos cuelgan de:
- `stay_id`

## Lectura estructural
- **Plan de Atención** = intención vigente
- **Estado del Episodio** = situación de proceso vigente
- **Riesgo Clínico Operacional** = prioridad operativa vigente

Juntos forman la columna vertebral mínima del episodio.

---

# 6. Superficies que deberían consumirlos

## Ficha
- plan actual
- estado canónico
- riesgo actual

## Censo
- estado canónico
- riesgo actual
- eventualmente resumen del plan

## Admisión
- estado canónico

## Egreso
- estado canónico
- referencia al plan/riesgo cuando aplique

## Agenda
- señal de plan/riesgo a mediano plazo

## Cockpit futuro
- estado + riesgo + capacidad + continuidad

---

# 7. Estrategia técnica recomendada

## 7.1 No partir con gran refactor BD

Secuencia recomendada:
1. vista canónica de estado
2. vista o tabla liviana de plan actual
3. tabla/vista liviana de riesgo actual
4. después endurecer persistencia según aprendizaje

## 7.2 Principio de mínima invasión

- reutilizar `stay_id`
- no romper tablas clínicas existentes
- preferir consolidación primero, normalización profunda después

## 7.3 Principio de trazabilidad

Toda consolidación nueva debe mantener:
- fuente,
- responsable,
- timestamp,
- versión o vigencia cuando aplique

---

# 8. Riesgos de diseño de datos

## Riesgo 1
Crear demasiada estructura nueva y duplicar el sistema actual.

## Riesgo 2
No crear suficiente estructura y dejar que plan/estado/riesgo sigan implícitos.

## Riesgo 3
Confundir objeto canónico con tabla definitiva.

## Riesgo 4
Perder trazabilidad del origen de la información consolidada.

---

# 9. Recomendación final

La mejor jugada para Fase I parece ser esta:

- **Estado del episodio**: empezar por vista canónica
- **Plan de atención**: empezar por vista consolidada o tabla liviana si hace falta persistencia temprana
- **Riesgo**: empezar por tabla liviana o vista actual simple

Eso permite avanzar rápido, aprender con casos reales y evitar refactor masivo prematuro.

---

# 10. Veredicto

El esquema mínimo de Fase I no debe buscar perfección relacional.
Debe buscar una cosa más importante:

**hacer explícita la semántica que hoy existe de forma dispersa, para que el sistema se vuelva más inteligible y gobernable.**
