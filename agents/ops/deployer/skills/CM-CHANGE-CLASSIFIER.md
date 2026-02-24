---
_manifest:
  urn: "urn:ops:agent-bootstrap:deployer-cm-change-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar el riesgo de un PR o changeset para determinar la estrategia de deploy. Asignar uno de tres niveles: lectura, escritura, destructiva.

## Input/Output

- **Input:** changeset: {files: string[], pr_metadata: PRInfo, diff_summary: string, labels: string[]}
- **Output:** classification: {risk: lectura|escritura|destructiva, reason: string, affected_systems: string[], dod_status: {passed: number, total: 9, missing: string[]}}

## Procedimiento

1. **Verificar DoD** (9-step pipeline Xanpan §9.3):
   - IF alguno de los 9 pasos falta → classification.dod_status.missing = pasos faltantes
   - IF DoD incompleto → deploy NO procede. Retornar con missing steps.

2. **Analizar diff** por tipo de archivo:
   - .md, .yml (config), .env.example, docs/ → peso lectura
   - .py, .js, .ts (endpoints, handlers, models) → peso escritura
   - migrations/, schema/, auth/, .sql (DDL) → peso destructiva
   - Eliminar archivos con datos → peso destructiva

3. **Evaluar patrones destructivos**:
   - DROP TABLE, ALTER TABLE, DELETE FROM → destructiva
   - Cambio en auth/permissions/roles → destructiva
   - Eliminacion masiva de datos → destructiva
   - Cambio de schema irreversible → destructiva

4. **Evaluar patrones escritura**:
   - Nuevos endpoints API → escritura
   - Mutacion de datos (INSERT, UPDATE) → escritura
   - Nuevas features con logica de negocio → escritura
   - Cambios en servicios activos → escritura

5. **Clasificar**: tomar el nivel MAS ALTO detectado. IF cualquier archivo destructivo → toda la clasificacion es destructiva. Principio conservador.

6. **Registrar** reason con evidencia: archivos que determinaron clasificacion.

## Signature Output

```yaml
classification:
  risk: "escritura"
  reason: "Nuevo endpoint API /api/v2/orders con mutacion de datos"
  affected_systems: ["api-gateway", "orders-service"]
  dod_status:
    passed: 9
    total: 9
    missing: []
  files_analyzed: 12
  determining_files:
    - "src/api/orders.py → new endpoint (escritura)"
    - "src/models/order.py → new model field (escritura)"
```
