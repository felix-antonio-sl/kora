---
_manifest:
  urn: "urn:fxsl:skill:tester-test-executor:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-TEST-EXECUTOR

## Proposito
Ejecuta la suite completa de tests (aceptacion + integracion + unitarios existentes) en entorno sandboxed. Reporta resultados con evidencia: pass/fail por test, tiempo de ejecucion, stack traces de fallos.

## Input/Output
- **Input:** Suite a ejecutar: {suite: acceptance|integration|unit|all, filter?: string}
- **Output:** Resultados: {resultados: [{test_name, tipo, status, tiempo_ms, error?, stack_trace?}], resumen: {total, passed, failed, skipped, tiempo_total_ms}}

## Procedimiento

### Paso 1: Preparar entorno
- Verificar que el entorno de ejecucion es sandboxed (no produccion).
- Verificar que las dependencias de test estan instaladas (vitest, pytest).
- Verificar que los fixtures/seeds estan disponibles.
- Limpiar estado residual de ejecuciones previas.

### Paso 2: Descubrir tests
- Escanear directorio de tests segun suite:
  - `acceptance`: tests con patron `*.acceptance.test.*` o marcados como acceptance.
  - `integration`: tests con patron `*.integration.test.*` o marcados como integration.
  - `unit`: tests con patron `*.test.*` excluyendo acceptance e integration.
  - `all`: todos los anteriores.
- Aplicar filtro si se proporciona (por nombre, por historia, por componente).
- Reportar cantidad de tests descubiertos por tipo.

### Paso 3: Ejecutar suite
- Ejecutar tests en orden: unit → acceptance → integration (de mas rapido a mas lento).
- Por cada test:
  1. Ejecutar test.
  2. Capturar: nombre, status (pass|fail|skip|error), tiempo de ejecucion.
  3. Si falla: capturar error message + stack trace completo.
  4. Si timeout: marcar como fail con nota "timeout exceeded".
- No detener suite por fallos individuales (ejecutar todo, reportar al final).

### Paso 4: Generar reporte de resultados
- Tabla de resultados agrupada por tipo:

```
## Unitarios
| Test | Status | Tiempo |
|------|--------|--------|

## Aceptacion
| Test | Status | Tiempo | AC |
|------|--------|--------|----|

## Integracion
| Test | Status | Tiempo | Boundary |
|------|--------|--------|----------|
```

- Resumen: total, passed, failed, skipped, pass rate (%), tiempo total.
- Para cada fallo: error message + stack trace en bloque de codigo.

### Paso 5: Clasificar fallos
- **Fallo de test:** el test detecta un defecto → derivar a fxsl/coder para fix.
- **Fallo de entorno:** dependencia faltante, config incorrecta → reportar al Operador.
- **Fallo de test fragil:** test no deterministico → marcar para reescritura.
- **Timeout:** test excede tiempo limite → investigar causa.

## Invariantes
- Ejecutar en entorno sandboxed. NUNCA en produccion.
- No detener por fallos individuales. Ejecutar toda la suite.
- Stack trace completo en cada fallo. Sin ocultar detalles.
- Tiempos de ejecucion registrados por test.
- Resultados agrupados por tipo (unit, acceptance, integration).

## Signature Output
```
## Resumen de Ejecucion
| Metrica       | Valor |
|---------------|-------|
| Total tests   | 42    |
| Passed        | 40    |
| Failed        | 2     |
| Skipped       | 0     |
| Pass rate     | 95.2% |
| Tiempo total  | 12.3s |

## Fallos
### test_story1_ac2_limpiar_filtro
- **Status:** FAIL
- **Error:** Expected [] but received [Product{id:1}]
- **Stack trace:**
[stack trace en bloque de codigo]
```
