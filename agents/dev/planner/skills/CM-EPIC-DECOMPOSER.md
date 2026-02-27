---
_manifest:
  urn: "urn:dev:skill:planner-epic-decomposer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-EPIC-DECOMPOSER

## Proposito
Descompone una epica en historias de usuario con anatomia completa segun Xanpan::Agents §5.

## Procedimiento
1. Leer epica y KR asociado. Entender el valor de negocio que la epica debe entregar.
2. Identificar actores (Who), funcionalidades (What), beneficios (Why).
3. Descomponer en 4-8 historias independientes. Cada historia DEBE:
   - Entregar valor de negocio independiente (no ser solo una tarea tecnica).
   - Ser consumible por un agente en minutos a horas, no dias.
   - Tener los 5 elementos: Who/What/Why, ACs, valor, complejidad, riesgo.
4. Para cada historia:
   - Who/What/Why: "Como [usuario], quiero [funcionalidad], para [beneficio]".
   - Criterios de aceptacion: 3-7 condiciones testables, numeradas.
   - Valor de negocio: 1-5 (estimacion abstracta del PO).
   - Senal de complejidad: simple|estandar|complejo|critico.
   - Clasificacion de riesgo: lectura|escritura|destructiva.
5. Verificar que las historias cubren la epica completa sin gaps ni overlap.
6. Presentar historias en tabla para aprobacion del PO.

## Output
Lista de historias: tabla con {id, who_what_why, num_acs, valor, complejidad, riesgo}. Detalle expandible por historia.
