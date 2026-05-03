---
_manifest:
  urn: urn:kora:skill:clawforge-stack-optimizer:1.0.0
  type: lazy_load_endofunctor
---

# CM-STACK-OPTIMIZER

## Proposito
Optimizacion full-stack evaluando ejes en las 3 capas con impacto estimado. Propone mejoras y ejecuta las aprobadas.

## Input/Output
- **Input:** capas: string[] (host|docker|openclaw), metricas_actuales: Metrics | null
- **Output:** OptimizationReport (ver Signature Output)

## Procedimiento
1. EVALUAR CAPA HOST:
   - RAM/CPU disponible vs uso actual
   - Swap configurado adecuadamente
   - Servicios innecesarios consumiendo recursos
   - Kernel parameters (vm.swappiness, net.core.somaxconn)
2. EVALUAR CAPA DOCKER:
   - Container resource limits vs uso real
   - Image sizes (multi-stage builds?)
   - Layer cache efficiency
   - Volume driver performance
   - Container count vs necesidad
3. EVALUAR CAPA OPENCLAW:
   - Token economy: tokens/respuesta promedio (>4K warning, >8K critical)
   - Context window: % utilizado en sesiones activas (>70% warning, >90% critical)
   - Model selection: modelo vs use case (opus en chat trivial = desperdicio)
   - Bootstrap size: chars totales AGENTS+SOUL+USER+TOOLS+IDENTITY (>15K warning, >25K critical)
   - Session management: sesiones idle (>50 warning, >100 critical)
   - Memory DB: tamano sqlite-vec (>500MB warning sin QMD)
   - Compaction: auto-compaction habilitado y configurado
   - Sandbox overhead: modo sandbox vs tools peligrosos reales
4. PROPONER MEJORAS con impacto estimado: delta tokens, delta latencia, delta recursos.
5. IMPLEMENTAR aprobadas con verificacion post-cambio.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| ejes_evaluados | EvalEntry[] | Eje, capa, metrica actual, threshold, estado |
| bottlenecks | string[] | Cuellos de botella identificados |
| mejoras_propuestas | Improvement[] | Mejora, impacto estimado, esfuerzo |
| mejoras_aplicadas | string[] | Las implementadas |
| metricas_post | Metrics | Metricas post-optimizacion |
