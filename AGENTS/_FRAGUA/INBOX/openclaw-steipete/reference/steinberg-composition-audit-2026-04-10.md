# Steinberg composition audit — 2026-04-10

## Estado

La composicion local ya cubre las capacidades nucleares del vector Peter Steinberg:

- framing
- routing
- dispatch
- architecture review
- repo shaping
- multi-agent foreman
- loop closure
- taste review

## Solapamientos detectados

### `steinberg-dispatch` vs `steinberg-agent-foreman`

Solapan en coordinacion, pero la separacion correcta es:
- `dispatch` elige topologia y siguiente paso
- `agent-foreman` supervisa workers una vez decidida la topologia multi-agente

### `steinberg-architecture-review` vs `steinberg-repo-shaping`

Solapan en repo shape, pero la separacion correcta es:
- `architecture-review` mira forma del sistema
- `repo-shaping` mira forma del repositorio como contexto operable

### `steinberg-architecture-review` vs `steinberg-taste-review`

Solapan en naming y feel, pero la separacion correcta es:
- `architecture-review` cuando naming o feel afectan estructura
- `taste-review` cuando el problema es friccion, polish o coherencia de producto

## Gap que faltaba y ya se cubrio

- `steinberg-intent-framing` cubre el hueco previo entre solicitud borrosa y dispatch.

## Juicio actual

No se detecta otra capacidad nuclear faltante que justifique crear otra skill troncal ahora mismo.

Crear mas skills en este punto arriesga:
- redundancia
- drift burocratico
- costo de contexto innecesario
- fragmentacion doctrinal

## Recomendacion

Fase siguiente:
1. consolidar uso real de las 8 skills troncales
2. iterarlas con casos reales
3. podar cualquier redundancia que aparezca en practica
4. crear nuevas skills solo si aparece un gap repetido y no cubierto

## Regla

A partir de este punto, mejorar por integracion y uso real vale mas que seguir expandiendo catalogo.
