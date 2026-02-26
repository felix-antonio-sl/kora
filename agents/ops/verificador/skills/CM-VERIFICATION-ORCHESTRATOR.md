---
_manifest:
  urn: "urn:ops:skill:verificador-verification-orchestrator:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Orquestar la ejecucion secuencial de las 5 capas de verificacion adaptadas al tipo de cambio. Determinar capas requeridas segun riesgo. Ejecutar en orden fijo. Fail-fast si alguna capa falla.

## I/O

- **Input:** changeset: {files: string[], pr_metadata: PRInfo, diff_summary: string, coder_info: {provider: string, model: string}}
- **Output:** orchestration_result: {change_type: lectura|escritura|destructiva, layers_required: number[], layers_executed: LayerResult[], verdict: APROBADO|RECHAZADO, failed_layer?: string, evidence: Evidence[]}

## Procedimiento

1. **Clasificar tipo de cambio**:
   - Analizar archivos modificados y diff summary
   - .md, .yml (config), .env.example, docs/ → lectura
   - .py, .js, .ts (endpoints, handlers, models) → escritura
   - migrations/, schema/, auth/, .sql (DDL), DELETE/DROP → destructiva
   - Tomar nivel MAS ALTO detectado. Principio conservador.

2. **Determinar capas requeridas**:
   - lectura → capas [1, 2, 3] (CI + Regresion + Diversidad)
   - escritura → capas [1, 2, 3, 4] (+ Seguridad)
   - destructiva → capas [1, 2, 3, 4, 5] (+ Humana)

3. **Ejecutar capas en orden fijo**:
   - Capa 1: CI → ci_execute
   - Capa 2: Regresion → regression_run
   - Capa 3: Diversidad → diversity_check
   - Capa 4: Seguridad → security_scan (si requerida)
   - Capa 5: Humana → human_gate (si requerida)

4. **Fail-fast**: Si alguna capa retorna fail → detener ejecucion. NO ejecutar capas posteriores. Registrar capa fallida con evidencia.

5. **Compilar verdict**: IF todas capas requeridas pass → APROBADO. IF alguna fail → RECHAZADO con capa fallida y razon.

## Signature Output

```yaml
orchestration_result:
  change_type: "escritura"
  layers_required: [1, 2, 3, 4]
  layers_executed:
    - layer: 1
      name: "CI"
      status: "pass"
      detail: "lint OK, types OK, tests 142/142 pass"
    - layer: 2
      name: "REGRESION"
      status: "pass"
      detail: "dataset 89 cases, 0 degradations"
    - layer: 3
      name: "DIVERSIDAD"
      status: "pass"
      detail: "coder=Claude, reviewer=GPT-4, cross-eval positivo"
    - layer: 4
      name: "SEGURIDAD"
      status: "pass"
      detail: "SAST 0 criticos, DAST OK, privilegios OK"
  verdict: "APROBADO"
  failed_layer: null
  evidence:
    - "CI: 142 tests pass, 0 fail, 0 skip"
    - "Regresion: 89/89 outputs match expected"
    - "Diversidad: Claude != GPT-4 (verified)"
    - "Seguridad: 0 criticos, 2 low (informational)"
```
