---
_manifest:
  urn: urn:dev:skill:blast-radius:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Evaluar el alcance de un cambio antes de ejecutarlo. Determinar cuántos archivos se afectan, qué dependencias se tocan, cuál es el riesgo, y cuántos obreros paralelos asignar.

## Input/Output

- **Input:** Descripción del incremento + contexto del codebase (archivos relevantes leídos)
- **Output:** Evaluación: { nivel: small|medium|large, archivos_estimados, dependencias, riesgo, reversibilidad, parallelism_recomendado }

## Procedimiento

1. Identificar archivos directamente afectados por el cambio.
2. Trazar dependencias: qué otros archivos importan/usan los afectados?
3. Evaluar riesgo: toca estado compartido? APIs públicas? migraciones de datos?
4. Evaluar reversibilidad: se puede revertir con un `git revert`?
5. Clasificar:
   - **Small** (< 3 archivos, sin deps complejas): 1 obrero, skip planning
   - **Medium** (3-10 archivos, deps lineales): 1-2 obreros, planning ligero
   - **Large** (10+ archivos, deps cruzadas, estado compartido): 2-4 obreros, planning completo + descomposición
6. Recomendar parallelism: cuántos obreros independientes pueden trabajar sin conflictos de merge.

## Signature Output

```
## Blast Radius
- Nivel: [small|medium|large]
- Archivos estimados: [N]
- Dependencias: [lista]
- Riesgo: [bajo|medio|alto] — [razón]
- Reversibilidad: [alta|media|baja]
- Obreros recomendados: [N] en [paralelo|serie]
```
