---
_manifest:
  urn: "urn:fxsl:skill:coder-tdd-executor:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-TDD-EXECUTOR

## Proposito
Ejecuta el ciclo TDD estricto para cada tarea del plan de implementacion. Nucleo del coder.

## Procedimiento
Para cada tarea del plan aprobado, ejecutar en orden:

### Paso 1: Definir tipos (Type-first)
- Definir interfaces/tipos que la tarea necesita.
- TypeScript: `interface` + schema Zod para validacion.
- Python: `BaseModel` Pydantic.
- NUNCA `any`, `object`, `unknown` sin refinamiento.
- Verificar coherencia con SCHEMA.md.

### Paso 2: Escribir test (Red)
- Escribir test que verifica el comportamiento esperado.
- El test DEBE fallar antes de implementar (red).
- Test unitario: vitest (TypeScript) o pytest (Python).
- Si la tarea tiene AC asociado: derivar test de aceptacion del AC.
- Formato: Arrange-Act-Assert.

### Paso 3: Implementar codigo (Green)
- Escribir el codigo MINIMO necesario para que el test pase.
- Respetar CONVENTIONS.md: naming, estructura, patrones.
- Validar inputs con Zod/Pydantic en todo boundary.
- SQL parametrizado, nunca concatenacion.
- No sobre-ingeniar: si el test pasa, es suficiente.

### Paso 4: Refactorizar (Refactor)
- Con tests verdes, mejorar estructura sin cambiar comportamiento.
- Eliminar duplicacion.
- Mejorar nombres.
- Extraer funciones si mejora legibilidad.
- Verificar que tests siguen verdes.

### Modo Refactor (tareas verdes)
- Leer codigo existente.
- Si no hay tests: escribir tests de caracterizacion primero.
- Refactorizar con tests verdes como red de seguridad.
- NUNCA refactorizar sin tests.

## Invariantes
- Todo codigo tiene test. Sin excepciones.
- Tests escritos ANTES de implementacion. Sin excepciones.
- Tipos definidos ANTES de tests. Sin excepciones.
- El ciclo Red→Green→Refactor no se salta ni se reordena.

## Output
Por tarea: {tipos_definidos[], tests_escritos[], codigo_implementado[], tests_pasan: bool, archivos_modificados[]}.
