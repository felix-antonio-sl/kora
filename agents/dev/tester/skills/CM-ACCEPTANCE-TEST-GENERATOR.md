---
_manifest:
  urn: "urn:dev:skill:tester-acceptance-test-generator:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-ACCEPTANCE-TEST-GENERATOR

## Proposito
Deriva tests de aceptacion ejecutables a partir de los criterios de aceptacion (ACs) de una historia. Cada AC produce al menos un test en formato DADO/CUANDO/ENTONCES.

## Input/Output
- **Input:** Historia con ACs parseados (output de ac_parse): {criterios_aceptacion: [{id, dado, cuando, entonces}]}
- **Output:** Tests ejecutables: {tests: [{ac_id, test_name, test_code, framework}]}

## Procedimiento

### Paso 1: Validar ACs
- Verificar que la historia tiene al menos un AC.
- Verificar que cada AC tiene: condicion previa (DADO), accion (CUANDO), resultado esperado (ENTONCES).
- Si AC incompleto → reportar: "AC [id] incompleto. Falta: [elemento]. Derivar a fxsl/planner."

### Paso 2: Derivar tests por AC
Para cada AC:
1. Mapear DADO → setup/arrange del test (precondiciones, datos, estado inicial).
2. Mapear CUANDO → act del test (accion que dispara el comportamiento).
3. Mapear ENTONCES → assert del test (verificacion del resultado esperado).
4. Nombrar test: `test_[historia_id]_ac[n]_[descripcion_corta]`.
5. Evaluar si el AC requiere multiples variantes (edge cases derivados del AC).

### Paso 3: Generar codigo de test
- Framework TypeScript: vitest con `describe`/`it`/`expect`.
- Framework Python: pytest con `def test_`/`assert`.
- Estructura por test:
  ```
  // DADO: [condicion previa]
  // CUANDO: [accion]
  // ENTONCES: [resultado esperado]
  ```
- Cada test DEBE ser independiente (no depender de estado de otro test).
- Cada test DEBE ser determinista (sin randomness, sin timestamps, sin external state mutable).

### Paso 4: Verificar cobertura de ACs
- Contar: ACs totales vs ACs con test.
- Si algun AC no tiene test → generar test faltante.
- Regla: 0 ACs sin test. Sin excepciones.

### Paso 5: Presentar para revision
- Tabla resumen: AC_ID | Test Name | Framework | Status (generado).
- Codigo de cada test en bloque con lenguaje especificado.
- Solicitar aprobacion del Operador antes de ejecutar.

## Invariantes
- Todo AC tiene al menos un test. Sin excepciones.
- Formato DADO/CUANDO/ENTONCES obligatorio.
- Tests independientes: ejecutables en cualquier orden.
- Tests deterministicos: mismo resultado en re-ejecucion.
- NO testear implementacion. Testear el comportamiento descrito en el AC.

## Signature Output
```
| AC  | Test                          | Framework | Status  |
|-----|-------------------------------|-----------|---------|
| AC1 | test_story1_ac1_filtro_cat    | vitest    | generado|
| AC2 | test_story1_ac2_limpiar_filtro| vitest    | generado|
```
[bloques de codigo por test]
