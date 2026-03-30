# HODOM - Base de Datos Ideal

## Idea central
La base ideal no debe copiar la lógica de la planilla por pestañas mensuales. Debe modelar la operación real:

- una unidad o servicio,
- un día operativo,
- ingresos y egresos,
- capacidad de camas,
- resumen mensual derivado,
- y trazabilidad de importación y conflictos.

La regla más importante es esta:

- si existe desglose por tipo, ese es el dato más rico y manda;
- si no existe desglose, el sistema acepta `total informado`;
- el resumen mensual nunca se edita a mano;
- siempre se deriva desde el dato diario.

## Qué corrige respecto de la planilla
La planilla vieja mezcla varias cosas en el mismo lugar:

- dato de entrada,
- fórmulas,
- resumen mensual,
- ajustes manuales,
- y errores históricos.

La base nueva separa esas responsabilidades:

1. `daily_report` guarda el estado diario mínimo confiable.
2. `daily_admission_count` y `daily_discharge_count` guardan desglose por tipo cuando exista.
3. `v_daily_report_resolved` resuelve automáticamente si usar desglose o total informado.
4. `v_monthly_summary` consolida el mes sin intervención manual.
5. `import_batch` e `import_issue` dejan trazabilidad de migración, validación y anomalías.

## Decisiones de diseño
### 1. El eje del sistema es el día, no el mes
Cada fila real del sistema es una fecha. El mes es una vista de agrupación, no la unidad básica del dato.

### 2. Hay dos niveles válidos de granularidad
El modelo acepta:

- detalle por tipo de ingreso/egreso,
- o solo total diario informado.

Eso evita forzar desglose falso cuando hoy no existe.

### 3. La capacidad de camas no debe quedar fija para siempre
Se modela en `bed_capacity_period`, porque en los datos ya se ve que la capacidad cambia entre períodos.

### 4. El resumen mensual no es tabla fuente
El resumen mensual debe salir de la vista `v_monthly_summary`. Si alguna vez se necesita un cierre formal, eso debería ser otro objeto de negocio, no una sobreescritura del cálculo.

### 5. La migración debe ser auditable
No basta con “importar”. Hay que dejar registro de:

- de qué archivo vino el dato,
- qué conflicto se detectó,
- qué día quedó dudoso,
- y qué quedó migrado solo como total informado.

## Tablas principales
### `service_unit`
Maestro del servicio o unidad operativa.

### `reporting_period`
Mes operativo de trabajo, con estado: abierto, importado, validado o cerrado.

### `bed_capacity_period`
Historial de capacidad de camas por rango de fechas.

### `daily_report`
Hecho diario principal.

Campos clave:

- `opening_census`
- `admissions_total_reported`
- `discharges_total_reported`
- `same_day_inout_total`
- `beds_available_reported`
- `patient_stay_days_total`
- `patient_stay_days_beneficiary`

### `daily_admission_count`
Desglose de ingresos por categoría.

### `daily_discharge_count`
Desglose de egresos por categoría.

### `import_batch`
Registro de cada carga o migración.

### `import_issue`
Registro de conflictos, advertencias y observaciones de importación.

## Vistas principales
### `v_daily_report_resolved`
Resuelve el día real:

- usa desglose si existe;
- si no, usa total informado;
- calcula camas disponibles resueltas;
- calcula censo final resuelto;
- y explicita de dónde salió cada total.

### `v_monthly_summary`
Entrega el resumen mensual correcto:

- ingresos,
- egresos,
- días cama,
- días de estada,
- índice ocupacional,
- promedio de estada,
- censo inicial y final.

## Criterio de operación futura
La base ideal permite tres escenarios sin romperse:

1. hoy solo tenemos totales diarios,
2. mañana empezamos a cargar algunos desgloses,
3. más adelante cargamos todo atomizado.

El modelo no obliga a rediseñarse cada vez. Simplemente mejora la resolución cuando entra mejor dato.
