---
_manifest:
  urn: urn:fxsl:skill:neriomath-clasificador:1.1.0
  type: lazy_load_endofunctor
---

## Proposito
Clasificar cada solicitud por scope, continuidad con trabajo previo y clase de activacion cognitiva para determinar el esfuerzo, ruta FSM y señal de multiplicacion apropiados.

## Input/Output
- **Input:** Solicitud del usuario, contexto de sesion activo
- **Output:** Clasificacion: {scope: in|out, continuidad: nueva|previa, clase: 1|2|3|4, ruta_fsm: estado_destino, multiplicar: si|no}

## Procedimiento
1. Evaluar SCOPE: la solicitud requiere analisis riguroso, exploracion dialectica, critica o produccion cognitiva? Si no -> S-REJECT.
2. Evaluar CONTINUIDAD: es continuacion de trabajo previo en la sesion? Si si -> S-OPERACION con contexto retenido.
3. Clasificar CLASE DE ACTIVACION:
   - CLASE-1 RESPUESTA DIRECTA (esfuerzo bajo): pregunta factual, pedido de formato, tarea mecanica, consulta de definicion, correccion puntual. Umbral: respuesta correcta en <3 oraciones. Ruta: S-PRODUCCION directo. Multiplicar: no.
   - CLASE-2 ANALISIS FOCALIZADO (esfuerzo medio): problema con estructura reconocible, evaluacion, comparacion, diagnostico acotado, propuesta con restricciones claras. Umbral: estructura identificable, restricciones mayormente declaradas. Ruta: S-POSICIONAMIENTO (compacto). Multiplicar: si hay patron transferible.
   - CLASE-3 ANALISIS PROFUNDO (esfuerzo alto): problema ambiguo, multiescalar, restricciones ocultas, alto impacto decisional, planteo aparentemente incorrecto. Umbral: costo alto de error O formulacion incorrecta O conflicto entre lo pedido y lo necesitado. Ruta: S-POSICIONAMIENTO (completo). Multiplicar: si, transferencia explicita.
   - CLASE-4 INSUFICIENCIA (sin esfuerzo productivo posible): informacion insuficiente para cualquier conclusion responsable. Ruta: S-CLARIFY declarando que falta, por que importa y como obtenerlo. Multiplicar: no.
4. Regla de escalamiento: empezar siempre por la clase mas baja compatible. Escalar si durante procesamiento aparecen senales de complejidad oculta. Nunca CLASE-3 por defecto.

## Signature Output
Clasificacion: scope [in|out], continuidad [nueva|previa], clase [1|2|3|4], ruta [estado FSM destino], multiplicar [si|no]. Justificacion en 1 oracion si clase >= 2.
