---
_manifest:
  urn: "urn:ops:skill:integrador-conflict-resolver:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar conflictos de merge en trivial vs substantivo, resolver triviales autonomamente y preparar escalacion diagnostica completa para substantivos.

## I/O

- **Input:** conflict: {files: string[], diff_a: string, diff_b: string, conflict_markers: string[], pr_a: PRInfo, pr_b: PRInfo}
- **Output:** resolution: {classification: trivial|substantivo, status: resolved|escalated, resolved_diff?: string, escalation?: {reason: string, options: string[], impact: string, evidence: string[]}}

## Procedimiento

1. **Clasificar conflicto**:
   - Analizar naturaleza del conflicto en cada archivo afectado
   - Criterios trivial:
     - Import order diferente → trivial (reordenar segun convencion)
     - Whitespace/indentacion → trivial (aplicar formatter)
     - Formateo diferente → trivial (aplicar linter)
     - Funciones en orden diferente → trivial (ordenar alfabetico o por dependencia)
   - Criterios substantivo:
     - Logica conflictuante (IF diferentes para mismo caso) → substantivo
     - Implementaciones competidoras (dos soluciones para mismo problema) → substantivo
     - Contracts rotos (signature cambiada, interfaz incompatible) → substantivo
     - Cambios de tipo incompatibles → substantivo
     - Eliminacion vs modificacion del mismo codigo → substantivo

2. **IF trivial → resolver autonomamente**:
   - Aplicar convencion del proyecto (import order rules, formatting rules)
   - Generar diff resuelto
   - Verificar que resolucion preserva funcionalidad de ambos PRs
   - IF resolucion introduce nuevo conflicto → reclasificar como substantivo

3. **IF substantivo → preparar escalacion**:
   - Diagnostico completo: que conflictua, por que, donde
   - Listar opciones: adoptar PR-A, adoptar PR-B, combinar (si posible), reescribir
   - Evaluar impacto de cada opcion en el codebase
   - Registrar evidencia: archivos, lineas, diffs

4. **Registrar resultado**: clasificacion, resolucion o escalacion, evidencia.

## Signature Output

```yaml
resolution:
  classification: "trivial"
  status: "resolved"
  conflict_files: ["src/services/orders/__init__.py"]
  detail: "Import order: PR #206 agrega import A antes de B, PR #207 agrega import C antes de A"
  resolved_diff: |
    import A
    import B
    import C
  resolution_method: "Reorden alfabetico segun convencion del proyecto"
```

```yaml
resolution:
  classification: "substantivo"
  status: "escalated"
  conflict_files: ["src/services/orders/cache.py"]
  escalation:
    reason: "Implementaciones competidoras de cache para OrderService"
    options:
      - "Adoptar PR #208 (LRU cache): mejor para read-heavy workloads"
      - "Adoptar PR #209 (TTL cache): mejor para data freshness requirements"
      - "Combinar: LRU con TTL expiration (requiere reescritura)"
    impact: "Arquitectura de caching define patron para todos los servicios"
    evidence:
      - "PR #208: src/services/orders/cache.py implementa LRUCache(maxsize=1000)"
      - "PR #209: src/services/orders/cache.py implementa TTLCache(ttl=300)"
```
