---
_manifest:
  urn: "urn:ops:skill:integrador-coherence-verifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analisis cross-PR cuando multiples PRs target la misma zona del codebase. Verificar que los cambios combinados de todos los PRs no introducen contradicciones, duplicaciones o asunciones mutuamente excluyentes.

## Input/Output

- **Input:** prs: {pr_id: string, diff: string, target_zone: string, files: string[]}[], codebase_state: {architecture: ArchInfo, active_prs: PRInfo[]}
- **Output:** coherence_result: {status: coherent|contradictory|duplicate, conflicts: CrossPRConflict[], prs_analyzed: number, zones_checked: string[], recommendation: string}

## Procedimiento

1. **Agrupar PRs por zona**:
   - Identificar zonas del codebase que reciben cambios de multiples PRs
   - Mapear archivos modificados a zonas arquitectonicas (modulo, servicio, layer)
   - IF multiples PRs modifican misma zona → analisis profundo requerido

2. **Detectar patrones contradictorios**:
   - Comparar patrones introducidos por cada PR en la misma zona
   - IF PR-A introduce patron X y PR-B introduce patron Y para mismo caso → contradictory
   - Ejemplo: PR-A usa middleware pattern, PR-B usa decorator pattern para mismo concern

3. **Detectar implementaciones duplicadas**:
   - Comparar funcionalidad neta de cada PR
   - IF PR-A y PR-B implementan misma feature con diferentes approaches → duplicate
   - Ejemplo: PR-A y PR-B ambos implementan cache para OrderService

4. **Verificar asunciones mutuas**:
   - Extraer asunciones implicitas de cada PR (estado esperado de dependencias, interfaces consumidas)
   - IF PR-A asume estado X y PR-B modifica X → asuncion rota
   - Ejemplo: PR-A asume schema v2, PR-B migra a schema v3

5. **Verificar consistencia de interfaces**:
   - Si multiples PRs modifican interfaces en misma zona, verificar que las modificaciones son compatibles
   - IF interface modifications conflictuan → contradictory

6. **Compilar resultado**: listar conflictos cross-PR con evidencia, emitir recomendacion (merge en orden, hold, escalar).

## Signature Output

```yaml
coherence_result:
  status: "contradictory"
  prs_analyzed: 3
  zones_checked: ["src/services/orders/", "src/api/v2/"]
  conflicts:
    - type: "competing_implementations"
      prs: ["#208", "#209"]
      zone: "src/services/orders/cache.py"
      detail: "PR #208 implementa LRU cache, PR #209 implementa TTL cache para OrderService"
      severity: "high"
      recommendation: "Escalar a Operador: decision arquitectonica requerida"
  recommendation: "HOLD PRs #208 y #209. Merge PR #210 (sin overlap). Escalar conflicto cache a Operador."
```
