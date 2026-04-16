# HODOM HSC
# Backlog de Producto — Fase I

Versión: 2.1
Fecha: 2026-04-09
Estado: backlog inicial de producto

Base:
- `opm-hodom-hsc-especificacion-funcional-fase1-v2.0.md`
- `opm-hodom-hsc-fase1-plan-tactico-v1.5.md`
- `opm-hodom-hsc-fase1-paquetes-trabajo-v1.6.md`

Propósito: traducir Fase I a un backlog de producto más cercano a implementación.

---

## 1. Épicas de producto

### EP-01 — Plan de Atención
### EP-02 — Estados del Episodio
### EP-03 — Riesgo Clínico Operacional
### EP-00 — Soporte transversal de validación y consistencia

---

# 2. EP-00 — Soporte transversal

## HU-0001 — Glosario operativo visible para el equipo
Como equipo HODOM,
quiero un glosario mínimo de términos clave,
para usar el mismo lenguaje en clínica, coordinación y sistema.

### Criterios de aceptación
- documento breve disponible
- incluye episodio, plan, estado, riesgo
- validado por núcleo decisor

## HU-0002 — Set de casos de validación
Como equipo funcional,
quiero un set de episodios reales de referencia,
para validar que Fase I no quede desacoplada de la operación.

### Criterios de aceptación
- al menos 5 casos seleccionados
- cubren diversidad clínica y operativa

---

# 3. EP-01 — Plan de Atención

## HU-0101 — Definir estructura funcional del Plan de Atención
Como equipo funcional,
quiero definir la estructura mínima del Plan de Atención,
para que el sistema tenga un objeto canónico visible y útil.

### Criterios de aceptación
- campos mínimos definidos
- relación con episodio explícita
- validación sobre casos reales

## HU-0102 — Persistir o consolidar el Plan de Atención
Como sistema,
quiero contar con una fuente de verdad del Plan de Atención,
para mostrarlo consistentemente en las superficies críticas.

### Criterios de aceptación
- decisión de persistencia tomada
- modelo de datos o vista definido
- puede recuperarse por `stay_id`

## HU-0103 — Mostrar Plan de Atención en ficha
Como profesional,
quiero ver el Plan de Atención actual en la ficha,
para entender rápidamente la intención clínica vigente.

### Criterios de aceptación
- bloque visible en ficha
- incluye contenido mínimo acordado
- muestra última actualización o vigencia

## HU-0104 — Usar Plan de Atención en coordinación
Como coordinación,
quiero leer desde el plan señales útiles para programación,
para no coordinar solo por intuición o narrativas dispersas.

### Criterios de aceptación
- el plan muestra al menos frecuencia o prioridad útil
- coordinación reconoce su utilidad práctica

## HU-0105 — Detectar episodios sin Plan de Atención suficiente
Como Dirección Técnica o coordinación,
quiero identificar episodios con plan ausente o insuficiente,
para reducir opacidad asistencial.

### Criterios de aceptación
- existe regla mínima para “plan incompleto”
- pueden listarse episodios afectados

---

# 4. EP-02 — Estados del Episodio

## HU-0201 — Definir estados canónicos del episodio
Como equipo funcional,
quiero definir los estados canónicos del episodio,
para unificar la lectura del flujo asistencial-operativo.

### Criterios de aceptación
- estados definidos y documentados
- eventos de transición principales definidos

## HU-0202 — Mapear estado canónico con datos actuales
Como referente de datos,
quiero mapear los estados actuales al canon del episodio,
para reducir contradicciones entre módulos.

### Criterios de aceptación
- matriz de mapeo publicada
- casos ambiguos identificados

## HU-0203 — Mostrar estado canónico en admisión
Como usuario de admisión,
quiero ver el estado canónico del episodio,
para saber en qué punto exacto del flujo está.

### Criterios de aceptación
- estado visible en admisión
- naming consistente con el canon

## HU-0204 — Mostrar estado canónico en ficha y censo
Como profesional o coordinación,
quiero ver el estado canónico en ficha y censo,
para trabajar sobre una semántica compartida.

### Criterios de aceptación
- visible en ficha y censo
- no se contradice entre ambas superficies

## HU-0205 — Mostrar estado canónico en egreso
Como usuario de egreso,
quiero ver el estado canónico del episodio,
para cerrar coherentemente el caso.

### Criterios de aceptación
- visible en egreso
- coherente con causal de egreso

## HU-0206 — Detectar inconsistencias de estado
Como referente de datos o coordinación,
quiero identificar episodios con estados incoherentes,
para corregir errores de proceso o de datos.

### Criterios de aceptación
- existe listado o regla mínima de inconsistencia
- se pueden revisar casos afectados

---

# 5. EP-03 — Riesgo Clínico Operacional

## HU-0301 — Definir categorías de riesgo
Como equipo clínico y de coordinación,
quiero acordar categorías simples de riesgo,
para compartir una señal operacional útil.

### Criterios de aceptación
- categorías definidas: estable / en observación / inestable
- consecuencias operativas mínimas documentadas

## HU-0302 — Persistir o calcular riesgo por episodio
Como sistema,
quiero tener una fuente de verdad de riesgo por episodio,
para mostrarlo consistentemente en las superficies clave.

### Criterios de aceptación
- fuente de verdad definida
- recuperable por `stay_id`

## HU-0303 — Mostrar riesgo en censo
Como coordinación,
quiero ver el riesgo de cada episodio en el censo,
para priorizar trabajo diario.

### Criterios de aceptación
- riesgo visible en censo
- diferenciación visual clara

## HU-0304 — Mostrar riesgo en ficha
Como profesional,
quiero ver el riesgo en ficha,
para usar una lectura breve y compartida del episodio.

### Criterios de aceptación
- riesgo visible en ficha
- consistente con censo

## HU-0305 — Asociar riesgo a acción operativa
Como unidad,
quiero que cada categoría de riesgo tenga una consecuencia mínima de operación,
para que la señal no sea decorativa.

### Criterios de aceptación
- regla mínima por categoría definida
- coordinación y clínica saben cómo usarla

## HU-0306 — Detectar episodios sin riesgo asignado
Como coordinación o Dirección Técnica,
quiero identificar episodios sin riesgo visible,
para completar la columna vertebral operativa.

### Criterios de aceptación
- existe listado o alerta para episodios sin riesgo

---

# 6. Tareas técnicas sugeridas por historia

## Ejemplos para EP-01
- diseñar esquema o vista del plan
- mapear campos existentes que alimentan el plan
- construir componente UI “Plan actual”
- agregar timestamp/fuente de actualización

## Ejemplos para EP-02
- definir enumeración de estados
- mapear `clinical.estadia.estado`
- agregar helper de estado canónico
- propagar badge/label a admisión, ficha, censo y egreso

## Ejemplos para EP-03
- definir enumeración de riesgo
- decidir cálculo manual/automático/híbrido
- propagar badge/label a censo y ficha
- agregar regla de casos sin riesgo

---

# 7. Priorización sugerida dentro de Fase I

## P0
- HU-0001
- HU-0002
- HU-0101
- HU-0201
- HU-0301

## P1
- HU-0102
- HU-0202
- HU-0302
- HU-0103
- HU-0204
- HU-0303
- HU-0304

## P2
- HU-0104
- HU-0105
- HU-0203
- HU-0205
- HU-0206
- HU-0305
- HU-0306

---

# 8. Definición de éxito del backlog

Este backlog está bien ejecutado si, al final de Fase I:
- el plan ya no es implícito,
- el episodio ya no es semánticamente ambiguo,
- el riesgo ya no es invisible,
- y el sistema se vuelve más inteligible sin haberse vuelto más pesado.
