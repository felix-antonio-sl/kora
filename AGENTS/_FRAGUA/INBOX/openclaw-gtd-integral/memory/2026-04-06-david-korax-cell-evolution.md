# David cell evolution after Korax absorption

## Idea fuerza

La evolucion correcta no es fusionar workspaces completos. Es conservar la esencia de David y absorber de Korax solo las piezas que mejoran su capacidad de cell:

- mejor deteccion de colapso o abandono
- mejor rescate y reentrada
- mejor separacion captura vs triaje
- mejor ritmo de cierre y sincronizacion
- mejor co-agencia explicita

## Decision operativa

- legacy completo preservado en `reference/legacy-korax/`
- runtime OpenClaw actual manda
- no se importan sidecars, hooks ni `config.json`
- skills actuales de David siguen siendo la superficie nativa
- el legado se usa como referencia y linaje, no como runtime paralelo

## Criterio canonico

Un cell OpenClaw perfecto:
- usa archivos de workspace canonicos
- no inventa herramientas ni runtimes paralelos
- no depende de Docker doctrine si el gateway vive nativamente en host
- metaboliza legado en `SOUL.md`, `AGENTS.md`, `MEMORY.md`, `memory/`, `reference/` y skills nativas
