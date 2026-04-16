# Architecture + memory notes heredadas del steipe antiguo

## 1. Memoria de agentes — ideas legadas útiles

### Hermes Agent analysis
El steipe antiguo evaluó Hermes (fork Python de OpenClaw) y rescató varias ideas útiles:
- memoria por capas (hot/cold)
- snapshot congelado de memoria para preservar coherencia de contexto
- búsqueda FTS de sesiones
- skills auto-mejorables
- separación cached vs ephemeral en el prompt assembly

### Supermemory analysis
También evaluó Supermemory como infraestructura de contexto y memoria:
- knowledge graph con relaciones tipo updates / extends / derives
- auto-recall antes de cada turno
- auto-capture después de cada turno
- perfiles estáticos y dinámicos
- olvido automático / filtrado de ruido

## 2. Qué heredar de eso en steipete actual
No heredar la plataforma ajena en sí, pero sí el criterio:
- privilegiar memoria útil sobre acumulación indiscriminada
- distinguir memoria caliente y memoria histórica
- usar búsqueda semántica sobre `MEMORY.md`, `memory/*.md` y sesiones cuando aplique
- destilar aprendizajes a skills o referencias del workspace, no dejarlos enterrados en transcripts

## 3. Propuesta Kora → OpenClaw
El steipe antiguo produjo una propuesta fuerte de simplificación arquitectónica:
- OpenClaw como plataforma principal
- agentes como unidad principal
- skills como mecanismo preferente de capacidades
- servicios externos como adapters opcionales
- bootstrap más liviano y legible

La idea central sigue siendo valiosa para el steipete actual:
- menos ceremony
- más operabilidad
- más skills, menos ontología pesada en bootstrap
- más claridad entre identidad, memoria y runtime

## 4. Regla de continuidad
Estas notas son parte del legado estratégico del steipe antiguo. El steipete actual puede usarlas como criterio de diseño, pero no debe asumirlas como verdad automática sin verificar el estado real del sistema y de OpenClaw.
