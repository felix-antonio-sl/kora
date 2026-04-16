# HODOM HSC
# Arquitectura de Implementación — Fase I

Versión: 2.3
Fecha: 2026-04-09
Estado: propuesta técnica inicial

Base:
- `opm-hodom-hsc-backlog-producto-fase1-v2.1.md`
- `opm-hodom-hsc-esquema-datos-minimo-fase1-v2.2.md`
- lectura directa de módulos `admision`, `censo`, `ficha/[stayId]`, `egreso`, `agenda`, `rem`, `llamadas`

Objetivo: proponer cómo implementar Fase I en `hdos-app` y sobre la BD existente con la menor fricción posible.

---

## 1. Principio técnico rector

Fase I no debería arrancar con refactor mayor de toda la BD ni de toda la app.

La estrategia correcta parece ser:
1. introducir una capa semántica nueva y mínima,
2. exponerla primero en superficies de alto valor,
3. luego endurecer persistencia e integración.

En otras palabras:
**primero consolidar, después profundizar.**

---

## 2. Superficies prioritarias a tocar

## 2.1 Ficha del episodio
Ruta:
- `src/app/(app)/ficha/[stayId]/page.tsx`

### Por qué primero
Es la superficie donde ya convergen:
- episodio,
- signos vitales,
- alertas,
- notas,
- visitas,
- llamadas,
- contexto de cuidador/domicilio.

### Qué agregar en Fase I
1. bloque **Plan actual**
2. badge **Estado del episodio**
3. badge **Riesgo clínico operacional**

### Valor
Máximo. Es la mejor pantalla para probar la nueva semántica sin rediseñar todo.

---

## 2.2 Censo
Ruta:
- `src/app/(app)/censo/page.tsx`

### Por qué segundo
Es la superficie de coordinación con más impacto operativo.

### Qué agregar en Fase I
1. columna o badge de **Estado canónico**
2. columna o badge de **Riesgo**
3. filtro básico por estado/riesgo si es viable

### Valor
Muy alto para coordinación y futura capa directiva.

---

## 2.3 Admisión
Ruta:
- `src/app/(app)/admision/page.tsx`

### Qué agregar en Fase I
1. normalizar lectura de estado hacia estado canónico
2. dejar visible transición de postulaciones a episodio admitido/activo

### Valor
Asegura coherencia de entrada del episodio.

---

## 2.4 Egreso
Ruta:
- `src/app/(app)/egreso/page.tsx`

### Qué agregar en Fase I
1. estado canónico visible
2. validación de transición a egresado/cerrado más clara

### Valor
Cierra coherencia end-to-end.

---

## 2.5 Agenda
Ruta:
- `src/app/(app)/agenda/page.tsx`

### Qué tocar en Fase I
Solo consumo mínimo si ya existe señal disponible:
- riesgo resumido o prioridad futura
- no sobrecargar en esta fase

### Valor
Importante, pero no conviene meter demasiada semántica nueva aquí antes de consolidarla en ficha/censo.

---

## 3. Capa de datos recomendada

## 3.1 Estado del episodio

### Recomendación
Implementar primero una vista canónica.

### Nombre sugerido
`clinical.v_estado_episodio_canonico`

### Fuente probable
- `clinical.estadia.estado`
- `clinical.estadia.tipo_egreso`
- datos de postulaciones si el pipeline ya vive antes de admisión plena

### Consumo inicial
- ficha
- censo
- admisión
- egreso

### Motivo técnico
Es lo más barato y de mayor retorno: no exige rediseño total, pero unifica semántica inmediatamente.

---

## 3.2 Riesgo clínico operacional

### Recomendación
Crear estructura liviana con una fila vigente por episodio.

### Nombre sugerido
`clinical.riesgo_operacional_episodio`

### Consumo inicial
- ficha
- censo

### Motivo técnico
El riesgo necesita responsable, motivo y actualización. Una vista pura puede quedar demasiado débil si queremos trazabilidad mínima.

---

## 3.3 Plan de Atención

### Recomendación
Partir con vista consolidada o estructura híbrida antes de una tabla rica.

### Nombre sugerido
`clinical.v_plan_atencion_actual`

### Posible evolución
Si la vista se vuelve demasiado artificial o incompleta, pasar a tabla `clinical.plan_atencion`.

### Consumo inicial
- ficha
- luego censo o agenda, solo parcialmente

### Motivo técnico
No conviene apresurarse a normalizar un objeto cuyo significado aún está cerrándose con casos reales.

---

## 4. Orden técnico recomendado

## Etapa T1 — Semántica de solo lectura

### Entregables
- vista `v_estado_episodio_canonico`
- vista `v_plan_atencion_actual` o equivalente provisional
- tabla/vista `riesgo_operacional_episodio` mínima

### UI
- ficha consume las 3 piezas
- censo consume estado y riesgo

### Beneficio
Máxima legibilidad con mínima invasión.

---

## Etapa T2 — Coherencia transversal

### Entregables
- admisión consume estado canónico
- egreso consume estado canónico
- validaciones mínimas de consistencia

### Beneficio
La semántica deja de ser local a una sola pantalla.

---

## Etapa T3 — Integración operacional ligera

### Entregables
- exposición mínima del plan hacia agenda
- riesgo disponible para coordinación ampliada
- reglas de detección de “faltantes”

### Beneficio
Empieza a impactar operación real sin sobrediseño.

---

## 5. Cambios de software concretos sugeridos

## 5.1 En `ficha/[stayId]/page.tsx`

### Agregar nuevas consultas
- `estadoCanónico`
- `planActual`
- `riesgoActual`

### Agregar nuevos bloques visuales
- tarjeta resumen de plan
- badge de estado
- badge de riesgo

### Cuidado
No mezclar esto con el timeline ni enterrarlo demasiado abajo. Debe estar alto en la pantalla.

---

## 5.2 En `censo/page.tsx`

### Agregar al query base
- `estado_canonico`
- `categoria_riesgo`

### Agregar visualización
- badge o columna breve
- colorimetría clara

### Cuidado
No sobrecargar tabla. Mantener legibilidad.

---

## 5.3 En `admision/page.tsx`

### Agregar
- mapeo de estado hacia canon
- si aplica, mostrar diferencia entre postulado / elegible / admitido

### Cuidado
No crear estados alternativos en frontend sin fuente única.

---

## 5.4 En `egreso/page.tsx`

### Agregar
- estado canónico del episodio
- coherencia con causal de egreso

### Cuidado
Separar visualmente estado del episodio y tipo de egreso.

---

## 6. Riesgos técnicos a evitar

## 6.1 Lógica semántica enterrada solo en frontend
No conviene calcular el canon completo en cada página. Debe existir capa compartida o vista canónica.

## 6.2 Multiplicar fuentes de verdad
Un error sería que:
- ficha calcule una cosa,
- censo otra,
- admisión otra.

## 6.3 Hacer tabla rica del plan demasiado pronto
Primero comprobar si la vista consolidada ya entrega valor suficiente.

## 6.4 Meter demasiado a agenda en Fase I
Agenda es crítica, pero debe recibir semántica ya estabilizada, no convertirse en laboratorio prematuro.

---

## 7. Paquete mínimo de implementación recomendado

### Sprint técnico mínimo razonable
1. crear vista `v_estado_episodio_canonico`
2. crear estructura mínima para riesgo
3. crear vista/estructura provisional para plan
4. integrar ficha
5. integrar censo
6. integrar admisión y egreso
7. ejecutar revisión con 5 casos reales

---

## 8. Señales de buena implementación

- la ficha se vuelve más legible sin volverse más pesada
- el censo gana poder de coordinación inmediatamente
- admisión y egreso dejan de hablar dialectos distintos
- el equipo usa las nuevas piezas al explicar un caso

---

## 9. Veredicto técnico

La implementación de Fase I no requiere una revolución técnica.

Requiere una capa semántica nueva, pequeña y bien puesta, consumida primero por las pantallas correctas.

La mejor jugada parece ser:
**vistas canónicas + estructura liviana + exposición en ficha/censo + validación con casos reales.**
