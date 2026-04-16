# Memory — kora/korax

## Contexto Operador

_Registrar aquí preferencias, rutinas y contexto del operador._

## Decisiones

- **2026-03-25:** Para la gestión de rutas, Félix quiere un sistema donde cada actividad pueda moverse y adaptarse dinámicamente para organizarse; al final debe poder imprimirse una salida compartible para todos y otra versión para reporte. La dinámica y reordenabilidad son requisito de diseño.
- **2026-03-25:** Reducir la sobreingeniería. Para esta noche y hacia adelante, preferir usar las skills nativas de OpenClaw y soluciones más simples antes de agregar capas, automatizaciones o arquitectura extra.
- **2026-03-25:** `kora kb` podría materializarse como una skill, no necesariamente como un subsistema aparte. Evaluar esa vía primero para mantener simplicidad.
- **2026-03-25:** Separar `kora` en dos dominios: `kora conocimiento` y `kora agentes`. Tomarlo por ahora como decisión de arquitectura provisional.
- **2026-03-25:** Los agentes se diseñarán como genéricos en su forma más pura y formal, con transmutaciones/encarnaciones operativas para OpenClaw, Claude Code y Codex.
- **2026-03-25:** Volver a PCA con Korax + skills como base operativa; privilegiar esa arquitectura frente a variantes más complejas.
- **2026-03-25:** HSC también debe pensarse con enfoque `+ skills`.
- **2026-03-25:** Para colapsar la sobreingeniería actual, priorizar agentes OpenClaw con skills por sobre el servicio PSA actualmente en uso.
- **2026-03-25:** Simplificar los bootstraps: menos formalismo extremo y Markdown más liviano, manteniendo la misma expresividad.

## Hallazgos Pendientes

_Items abiertos que requieren seguimiento._

## Rutinas y Patrones

_Patrones recurrentes identificados._

## Coordinación

- Gateways pares habilitados con hooks en la federación: `clawforge`, `steipete`, `salubrista-hah`.
- Pueden derivar vía hook cuando necesiten apoyo de estructuración, priorización, síntesis, foco, realismo operativo o reducción de carga cognitiva para Félix.

## Notas

- **2026-03-25:** Recibida derivación de steipete con contexto estratégico de Open Model (opmodel). Plataforma OPM de modelamiento general. 961 tests green, base visual madura. Detalle en `memory/opmodel-contexto.md`.
