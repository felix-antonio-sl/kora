---
_manifest:
  urn: "urn:ops:skill:verificador-ci-layer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar la capa 1 de verificacion: CI verde (lint + type check + tests unitarios). Resultado binario pass/fail. CI verde es condicion minima pero radicalmente insuficiente por si sola (Swarm::Ops Axioma 4).

## Input/Output

- **Input:** changeset: {files: string[], pr_metadata: PRInfo, test_config?: TestConfig}
- **Output:** ci_result: {status: pass|fail, lint: {status: pass|fail, errors: string[]}, types: {status: pass|fail, errors: string[]}, tests: {status: pass|fail, total: number, passed: number, failed: number, skipped: number, failures: TestFailure[]}, duration_ms: number}

## Procedimiento

1. **Ejecutar lint**:
   - Correr linter configurado del proyecto
   - Registrar errores/warnings
   - IF errores → lint.status = fail

2. **Ejecutar type check**:
   - Correr type checker (mypy, tsc, etc.)
   - Registrar errores de tipo
   - IF errores → types.status = fail

3. **Ejecutar tests unitarios**:
   - Correr suite de tests configurada
   - Registrar total, passed, failed, skipped
   - IF failed > 0 → tests.status = fail
   - Capturar detalle de cada test fallido: nombre, assertion, output esperado vs actual

4. **Compilar resultado**: IF ANY componente fail → ci_result.status = fail. Todos deben pasar para status = pass.

5. **Registrar duracion**: Medir tiempo total de ejecucion de la capa.

## Signature Output

```yaml
ci_result:
  status: "pass"
  lint:
    status: "pass"
    errors: []
  types:
    status: "pass"
    errors: []
  tests:
    status: "pass"
    total: 142
    passed: 142
    failed: 0
    skipped: 0
    failures: []
  duration_ms: 34200
```
