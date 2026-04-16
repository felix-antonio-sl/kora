# HODOM HSC
# Validación con Casos Reales — Fase I

Versión: 2.4
Fecha: 2026-04-09
Estado: protocolo inicial de validación

Base:
- `opm-hodom-hsc-fase1-plan-tactico-v1.5.md`
- `opm-hodom-hsc-especificacion-funcional-fase1-v2.0.md`
- `opm-hodom-hsc-arquitectura-implementacion-fase1-v2.3.md`

Objetivo: definir cómo aceptar o rechazar Fase I usando episodios reales, no solo revisión abstracta.

---

## 1. Principio de validación

Fase I no se valida preguntando si “la funcionalidad existe”.

Se valida preguntando si, frente a un episodio real, el sistema permite responder con claridad y coherencia a estas tres preguntas:

1. ¿Cuál es el plan vigente?
2. ¿En qué estado está realmente el episodio?
3. ¿Qué prioridad clínica-operacional tiene hoy?

Si el sistema no responde bien eso en casos reales, Fase I no está cerrada.

---

## 2. Set recomendado de casos

Seleccionar al menos 5 episodios activos o recientemente egresados, distintos entre sí.

### Caso A — Episodio simple y estable
Propósito: probar legibilidad básica.

### Caso B — Episodio con alta carga de enfermería
Propósito: probar riqueza del plan y frecuencia.

### Caso C — Episodio con deterioro o riesgo relevante
Propósito: probar riesgo y escalamiento.

### Caso D — Episodio con llamada/regulación importante
Propósito: probar articulación entre clínica y resolución remota.

### Caso E — Episodio de egreso complejo o reingreso
Propósito: probar estado, cierre y coherencia de flujo.

---

## 3. Participantes mínimos de validación

- 1 referente clínico
- 1 referente de coordinación
- 1 referente funcional/producto
- opcional: Dirección Técnica en cierre

---

## 4. Criterios de validación por dimensión

# 4.1 Validación del Plan de Atención

Para cada caso, revisar:

### Preguntas
- ¿Se identifica fácilmente el objetivo clínico principal?
- ¿Se entiende qué disciplinas o prestaciones están activas?
- ¿Se puede inferir la frecuencia o intensidad esperada de atención?
- ¿Se entiende cuándo debería ajustarse o cerrarse el plan?

### Resultado esperado
- sí, sin abrir una cantidad excesiva de registros narrativos

### Señal de falla
- el evaluador necesita reconstruir el plan manualmente desde múltiples notas

---

# 4.2 Validación del Estado del Episodio

Para cada caso, revisar:

### Preguntas
- ¿El estado del episodio es visible?
- ¿El estado parece coherente con lo que se observa en ficha, admisión o egreso?
- ¿Hay contradicción entre pantallas?
- ¿Se diferencia bien entre estado del episodio y tipo de egreso?

### Resultado esperado
- el estado es legible, estable y no contradictorio

### Señal de falla
- el mismo caso “parece” estar en más de un estado a la vez

---

# 4.3 Validación del Riesgo Clínico Operacional

Para cada caso, revisar:

### Preguntas
- ¿El riesgo está visible?
- ¿La categoría parece razonable para el caso?
- ¿La coordinación podría usar esa señal para priorizar?
- ¿Existe una acción asociada plausible a esa categoría?

### Resultado esperado
- el riesgo no es decorativo; ayuda a decidir

### Señal de falla
- el evaluador dice “veo el badge, pero no me cambia nada”

---

## 5. Matriz de evaluación sugerida

| Caso | Plan claro | Estado claro | Riesgo útil | Coherencia entre pantallas | Observaciones |
|------|------------|--------------|-------------|----------------------------|---------------|
| A | Sí/No | Sí/No | Sí/No | Sí/No | |
| B | Sí/No | Sí/No | Sí/No | Sí/No | |
| C | Sí/No | Sí/No | Sí/No | Sí/No | |
| D | Sí/No | Sí/No | Sí/No | Sí/No | |
| E | Sí/No | Sí/No | Sí/No | Sí/No | |

---

## 6. Umbral de aceptación recomendado

Fase I puede considerarse aceptable si:

1. al menos 4 de 5 casos pasan en “plan claro”
2. al menos 5 de 5 casos pasan en “estado claro” o, como mínimo, no presentan contradicción crítica
3. al menos 4 de 5 casos pasan en “riesgo útil”
4. no hay contradicciones graves entre ficha, censo, admisión y egreso

Si no se cumple eso, Fase I debe considerarse incompleta, aunque técnicamente ya esté desplegada.

---

## 7. Preguntas de cierre de validación

Después de revisar los casos, hacer estas 5 preguntas al grupo:

1. ¿Explicar un episodio es ahora más fácil que antes?
2. ¿Coordinar una decisión cotidiana requiere menos reconstrucción mental?
3. ¿Hay algo importante del episodio que siga quedando invisible?
4. ¿El riesgo ayuda de verdad a priorizar?
5. ¿Qué pieza sigue sintiéndose artificial o no confiable?

---

## 8. Criterios de rechazo

Fase I debe rechazarse o reabrirse si ocurre cualquiera de estas situaciones:

- el plan sigue siendo básicamente implícito
- el estado del episodio se contradice entre módulos
- el riesgo no tiene consecuencia operativa ni credibilidad clínica
- los casos complejos no logran representarse mejor que antes
- el equipo considera que el sistema “agregó etiquetas” pero no mejoró entendimiento real

---

## 9. Recomendación práctica de ejecución

La validación no debería hacerse solo como demo técnica.

Formato recomendado:
1. abrir caso real
2. revisar ficha
3. revisar censo
4. revisar admisión o egreso si aplica
5. responder la matriz en vivo
6. registrar observaciones
7. consolidar ajustes

Duración sugerida:
- 20 a 30 minutos por caso
- 2 sesiones de validación si es necesario

---

## 10. Veredicto

La validación con casos reales es la frontera entre “tenemos una idea interesante” y “tenemos una columna vertebral realmente utilizable”.

Si Fase I no mejora la inteligibilidad de casos reales, todavía no está lista.
