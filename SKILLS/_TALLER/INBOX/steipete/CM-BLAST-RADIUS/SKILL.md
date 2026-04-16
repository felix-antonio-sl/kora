---
_manifest:
  urn: urn:dev:skill:blast-radius:1.0.1
  type: lazy_load_endofunctor
---

## Proposito

Evaluar el alcance de un cambio antes de ejecutarlo. Determinar cuantos archivos se afectan, que dependencias se tocan, cual es el riesgo, y cuantos obreros paralelos asignar.

## Input/Output

- **Input:** Descripcion del incremento + contexto del codebase (archivos relevantes leidos)
- **Output:** Evaluacion: { nivel: small|medium|large, archivos_estimados, dependencias, riesgo, reversibilidad, parallelism_recomendado }

## Procedimiento

1. Identificar archivos directamente afectados por el cambio.
2. Trazar dependencias: que otros archivos importan/usan los afectados?
3. Evaluar riesgo: toca estado compartido? APIs publicas? migraciones de datos?
4. Evaluar reversibilidad: se puede revertir con un `git revert`?
5. Clasificar:
   - **Small** (< 3 archivos, sin deps complejas): 1 obrero, skip planning
   - **Medium** (3-10 archivos, deps lineales): 1-2 obreros, planning ligero
   - **Large** (10+ archivos, deps cruzadas, estado compartido): 2-4 obreros, planning completo + descomposicion
6. Recomendar parallelism: cuantos obreros independientes pueden trabajar sin conflictos de merge.

## Signature Output

```
## Blast Radius
- Nivel: [small|medium|large]
- Archivos estimados: [N]
- Dependencias: [lista]
- Riesgo: [bajo|medio|alto] — [razon]
- Reversibilidad: [alta|media|baja]
- Obreros recomendados: [N] en [paralelo|serie]
```
