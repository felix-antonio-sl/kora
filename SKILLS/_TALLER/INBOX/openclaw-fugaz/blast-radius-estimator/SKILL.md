---
name: blast-radius-estimator
description: Estima el blast radius de un cambio propuesto antes de ejecutarlo. Usar cuando el usuario describe una modificacion, refactor o feature y se necesita decidir topologia, paralelismo y nivel de cuidado.
---

# Blast Radius Estimator

Antes de ejecutar cualquier cambio no trivial, estimar blast radius.

## Procedimiento

1. Identificar archivos que seran tocados (directos e indirectos)
2. Clasificar el cambio:
   - **Bajo** (1-3 archivos, reversible, sin dependencias cruzadas) → ejecutar directo
   - **Medio** (4-10 archivos, reversible, algunas dependencias) → ejecutar con tests, commit atomico
   - **Alto** (10+ archivos, potencialmente irreversible, multiples dependencias) → plan antes de ejecutar, validacion humana
3. Decidir topologia:
   - Bajo → accion directa
   - Medio → secuencial con checkpoints
   - Alto → solicitar confirmacion humana antes de proceder
4. Documentar estimacion en una linea antes de actuar

## Criterios de blast radius

- Cuantos archivos toca?
- Si sale mal, cuanto cuesta revertir?
- Necesito explorar primero?
- Puedo cerrar el loop solo?
- El cuello de botella es implementacion o diseno?
- El contexto actual ayuda o ensucia?

## Defaults

- Ante duda, estimar hacia arriba (mas cuidado)
- Cambios de schema, dependencias y boundaries siempre son blast radius alto
- Cambios de estilo, formatting y docs siempre son blast radius bajo
