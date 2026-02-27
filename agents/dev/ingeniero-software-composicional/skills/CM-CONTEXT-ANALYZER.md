---
_manifest:
  urn: "urn:dev:skill:ingeniero-software-composicional-context-analyzer:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar condiciones de trabajo del proyecto usando Lente MBT (C1-C5) para informar decisiones de arquitectura y diseno.

## I/O

- **Input:** Descripcion del proyecto o contexto desde S-OPPORTUNITY
- **Output:** Perfil de Contexto con 5 dimensiones evaluadas

## Procedimiento

1. Evaluar C1-RECURSOS: restricciones de tiempo, equipo, presupuesto
2. Evaluar C2-PROPOSITO: MVP exploratorio o sistema critico, tolerancia a fallos
3. Evaluar C3-DOMINIO: conocido/estable o novedoso/volatil, complejidad intrinseca
4. Evaluar C4-CULTURA: agil/informal o estricto/formal, nivel de documentacion requerido
5. Evaluar C5-LEGADO: codigo heredado, deuda tecnica existente, integraciones necesarias
6. Sintetizar perfil con impacto en decisiones de arquitectura

## Signature Output

```
## Perfil de Contexto
| Dimension | Evaluacion | Impacto Arquitectonico |
|-----------|-----------|----------------------|
| C1-RECURSOS | {evaluacion} | {impacto} |
| C2-PROPOSITO | {evaluacion} | {impacto} |
| C3-DOMINIO | {evaluacion} | {impacto} |
| C4-CULTURA | {evaluacion} | {impacto} |
| C5-LEGADO | {evaluacion} | {impacto} |
```
