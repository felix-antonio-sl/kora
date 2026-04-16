---
name: intent-contract
description: Create and refine intent contracts — the agentic evolution of user stories. Use when work needs to be specified with beneficiary, acceptance criteria, eval requirements, autonomy limits, and rollback plans before delegation to agents or teams.
---

# Intent Contract

Crear y refinar contratos de intencion para trabajo humano-agente.

## Cuando activar

- El usuario tiene trabajo que delegar a agentes o celulas.
- Necesita especificar una pieza de trabajo con criterios testables.
- Quiere convertir una historia de usuario o ticket en contrato de intencion.
- Pide ayuda para definir limites de autonomia para una tarea.

## Procedimiento

1. **Identificar beneficiario.** Quien se beneficia del resultado.
2. **Definir cambio deseado.** Que cambia concretamente.
3. **Explicitar beneficio esperado.** Por que importa.
4. **Redactar criterios de aceptacion.** Lista testable y verificable.
5. **Disenar evals minimos.** Que se evalua automaticamente y con que datos.
6. **Delimitar autonomia.** Que puede hacer el ejecutor sin preguntar, que requiere aprobacion.
7. **Identificar aprobacion humana.** Para que pasos es irreductible.
8. **Mapear riesgo y rollback.** Que puede salir mal y como se revierte.
9. **Validar completitud.** El contrato es ejecutable sin ambiguedad?

## Formato de salida

```
## Intent Contract: {titulo}
- Beneficiario: {quien}
- Cambio deseado: {que}
- Beneficio esperado: {por que}
- Criterios de aceptacion:
  - [ ] {criterio 1 — testable}
  - [ ] {criterio 2 — testable}
  - [ ] ...
- Evals minimos: {que se evalua, con que datos}
- Autonomia permitida: {acciones libres del ejecutor}
- Aprobacion requerida: {pasos que necesitan humano}
- Riesgo: {que puede fallar}
- Rollback: {como se revierte}
- Owner: {humano responsable del outcome}
- Ejecutor: {agente o celula asignada}
```

## Gotchas

- Si no tiene eval, no es un contrato; es un deseo.
- "Hazlo bien" no es criterio de aceptacion. "El test X pasa con datos Y" si lo es.
- El contrato no reemplaza la conversacion. La endurece y la hace verificable.
- Autonomia "total" es un anti-patron. Siempre hay algo que requiere humano.
