# 2026-04-09 — skills de composicion Peter/steipete

## Decision

Para hacer operativa la aproximacion al vector Peter Steinberg, se agregaron skills locales de composicion que convierten rasgos identitarios en comportamiento reusable.

## Skills creadas

### 1. `steinberg-dispatch`

Uso:
- decidir topologia de ejecucion
- comprimir ambiguedad en siguiente paso ejecutable
- supervisar agentes sin caer en ceremonia
- mantener steerability y leverage

Paquete:
- `artifacts/skills/steinberg-dispatch.skill`

### 2. `steinberg-architecture-review`

Uso:
- review arquitectonico de alto leverage
- boundaries, dependencies, schema, naming, runtime split, repo shape, UX feel
- evitar review line-by-line cuando el problema es estructural

Paquete:
- `artifacts/skills/steinberg-architecture-review.skill`

### 3. `brutal-loop-closure`

Uso:
- cierre de loop despues de cambios
- validacion por blast radius
- evidencia de build/test/repo state/riesgo remanente

Paquete:
- `artifacts/skills/brutal-loop-closure.skill`

## Efecto buscado

Mover el agente desde identidad declarativa hacia composicion efectiva:
- mejor dispatch
- mejor criterio arquitectonico
- mejor cierre de loop
- menos deriva burocratica
- mas densidad operativa en respuestas y decisiones
