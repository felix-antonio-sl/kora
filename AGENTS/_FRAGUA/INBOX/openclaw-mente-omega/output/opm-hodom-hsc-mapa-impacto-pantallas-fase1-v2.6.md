# HODOM HSC
# Mapa de Impacto por Pantalla — Fase I

Versión: 2.6
Fecha: 2026-04-09
Estado: propuesta de impacto UI inicial

Propósito: aterrizar Fase I en cambios concretos por pantalla dentro de `hdos-app`.

Pantallas consideradas:
- admisión
- ficha
- censo
- egreso
- agenda

---

## 1. Principio de intervención

Fase I no debe rediseñar todas las pantallas.
Debe insertar tres nuevas capas semánticas con mínima fricción visual:
- plan
- estado
- riesgo

La regla es:
**agregar claridad, no ruido.**

---

# 2. Pantalla: Ficha del episodio

Ruta:
- `src/app/(app)/ficha/[stayId]/page.tsx`

## 2.1 Cambio propuesto
Agregar un bloque de resumen operativo alto en la pantalla, antes o cerca del contenido longitudinal principal.

## 2.2 Elementos nuevos
1. **Estado del episodio**
2. **Riesgo clínico operacional**
3. **Plan actual**

## 2.3 Diseño funcional sugerido

### Banda superior de contexto
- estado del episodio (badge)
- riesgo (badge con color)
- días de estadía

### Tarjeta “Plan actual”
- objetivo clínico
- problema principal
- prestaciones activas
- frecuencia objetivo
- actualización más reciente

## 2.4 Beneficio esperado
- lectura clínica y operativa más rápida
- menos necesidad de reconstrucción desde timeline/notas

## 2.5 Riesgo de mala implementación
- enterrar el bloque muy abajo
- sobrecargarlo con demasiado detalle
- duplicar información ya visible sin jerarquía

---

# 3. Pantalla: Censo

Ruta:
- `src/app/(app)/censo/page.tsx`

## 3.1 Cambio propuesto
Convertir el censo en mejor superficie de coordinación agregando estado canónico y riesgo.

## 3.2 Elementos nuevos
1. columna o badge de **Estado del episodio**
2. columna o badge de **Riesgo**
3. filtro opcional por estado/riesgo

## 3.3 Diseño funcional sugerido

### En fila de paciente
- nombre
- días
- alertas
- estado canónico
- riesgo

### En filtros
- estado: activo / egresado / admitido / etc.
- riesgo: estable / observación / inestable

## 3.4 Beneficio esperado
- mejor priorización diaria
- mejor coordinación de carga y continuidad

## 3.5 Riesgo de mala implementación
- volver la tabla ilegible
- usar demasiados colores o badges
- no cuidar consistencia con ficha

---

# 4. Pantalla: Admisión

Ruta:
- `src/app/(app)/admision/page.tsx`

## 4.1 Cambio propuesto
Hacer visible el estado canónico del episodio en el pipeline de entrada.

## 4.2 Elementos nuevos
1. lectura canónica del estado
2. si aplica, diferencia más clara entre:
- postulado
- elegible
- admitido

## 4.3 Diseño funcional sugerido
- mantener checklist de elegibilidad
- agregar badge de estado canónico por fila
- eventualmente señal de “listo para activar episodio”

## 4.4 Beneficio esperado
- menos ambigüedad entre postulación y admisión efectiva

## 4.5 Riesgo de mala implementación
- duplicar estados viejos y nuevos al mismo tiempo sin jerarquía

---

# 5. Pantalla: Egreso

Ruta:
- `src/app/(app)/egreso/page.tsx`

## 5.1 Cambio propuesto
Asegurar que el egreso consuma y exprese estado canónico de manera limpia.

## 5.2 Elementos nuevos
1. estado actual del episodio
2. transición esperada al egresar
3. eventual referencia breve a plan o riesgo si ayuda a cierre

## 5.3 Diseño funcional sugerido
- badge de estado actual
- tipo de egreso visible y claramente separado
- confirmación conceptual del cierre del episodio

## 5.4 Beneficio esperado
- cierre semántico más robusto
- menos contradicción entre causal y estado

## 5.5 Riesgo de mala implementación
- mezclar tipo de egreso y estado del episodio en un solo rótulo

---

# 6. Pantalla: Agenda

Ruta:
- `src/app/(app)/agenda/page.tsx`

## 6.1 Cambio propuesto
Intervención mínima en Fase I.

## 6.2 Elementos nuevos opcionales
1. riesgo resumido por visita/episodio
2. señal ligera de prioridad derivada del plan

## 6.3 Diseño funcional sugerido
No agregar mucho al listado principal en Fase I.

Si se agrega algo, que sea:
- un ícono o tag breve de prioridad/riesgo
- siempre que la semántica ya esté consolidada en ficha/censo

## 6.4 Beneficio esperado
- alinear territorio con prioridad clínica sin sobrecargar agenda

## 6.5 Riesgo de mala implementación
- convertir agenda en el lugar donde se experimenta semántica no estabilizada

---

# 7. Orden sugerido de cambios UI

## Orden recomendado
1. ficha
2. censo
3. admisión
4. egreso
5. agenda

## Razón
- ficha: máxima densidad clínica
- censo: máximo valor coordinativo
- admisión/egreso: consistencia de frontera
- agenda: consumo posterior de semántica ya validada

---

# 8. Cambios mínimos por pantalla

| Pantalla | Cambio mínimo imprescindible |
|----------|------------------------------|
| Ficha | plan + estado + riesgo |
| Censo | estado + riesgo |
| Admisión | estado canónico |
| Egreso | estado canónico coherente con causal |
| Agenda | opcional, solo si no agrega ruido |

---

# 9. Criterio de aceptación UI de Fase I

Fase I está bien impactada en UI si ocurre esto:
- un clínico entiende mejor el episodio en ficha
- coordinación prioriza mejor desde censo
- admisión y egreso dejan de sentirse semánticamente desconectados
- agenda no se vuelve más confusa

---

# 10. Veredicto

El mapa de impacto por pantalla muestra algo útil:

Fase I no necesita una gran transformación visual.
Necesita pequeñas inserciones muy bien ubicadas en las superficies correctas.

Eso baja riesgo y acelera aprendizaje.
