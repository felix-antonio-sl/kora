---
_manifest:
  urn: urn:dev:skill:decomposition:1.1.0
  type: lazy_load_endofunctor
---

## Proposito

Descomponer un incremento de blast radius medio/grande en paquetes atomicos delegables a obreros independientes.

## Input/Output

- **Input:** Incremento + evaluacion de blast radius
- **Output:** Lista de WorkPackages: { id, archivos_target, intencion, blast_radius_individual, dependencias_entre_paquetes, grupo_paralelo }

## Procedimiento

1. Identificar unidades de cambio independientes (archivos que no se afectan mutuamente).
2. Agrupar por independencia: paquetes en el mismo grupo_paralelo pueden ejecutarse simultaneamente.
3. Ordenar grupos por dependencia: grupo 1 primero, grupo 2 despues (si depende de 1).
4. Cada paquete debe ser atomico: un commit, una intencion, un obrero.
5. Validar: cada paquete tiene blast radius evaluable? close-the-loop criteria claros?
6. Preferir paquetes pequenos que se puedan revertir individualmente.

## Signature Output

```
## Paquetes
| # | Intencion | Archivos | Grupo | Depende de |
|---|-----------|----------|-------|------------|
| 1 | ...       | ...      | A     | —          |
| 2 | ...       | ...      | A     | —          |
| 3 | ...       | ...      | B     | 1, 2       |
```
