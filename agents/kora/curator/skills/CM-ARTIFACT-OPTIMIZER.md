---
_manifest:
  urn: "urn:kora:skill:curator-artifact-optimizer:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-ARTIFACT-OPTIMIZER

## Proposito
Analiza artefactos existentes y propone mejoras de calidad: telegrafizacion, estructura RAG, deduplicacion, referencias, densidad semantica.

## I/O

- **Input:** artefacto: path | URN (artefacto existente a optimizar)
- **Output:** OptimizationReport (ver Signature Output)

## Procedimiento
1. LEER artefacto completo. Clasificar tipo.
2. EVALUAR calidad en ejes:

| Eje | Evaluacion | Objetivo |
|-----|-----------|----------|
| Telegrafizacion | ¿Hay prosa que puede comprimirse mas? ¿Hay grasa residual? | Maxima densidad, cero grasa |
| Estructura RAG | ¿Cada ## es chunk autosuficiente? ¿Headings telegraficos? ¿Profundidad <= ####? | Independencia chunk total |
| SSOT | ¿Hay informacion duplicada entre secciones? | Un hecho, un lugar |
| Promocion | ¿Hay prosa comparativa/condicional que deberia ser tabla/lista? | Siempre prosa→estructura |
| Referencias | ¿URNs validos? ¿Referencias internas correctas? ¿Sin version en URN? | Resolucion completa |
| Frontmatter | ¿Tags suficientes y semanticos? ¿Source trazable? ¿Version coherente? | Metadata completa |
| Idioma | ¿Consistente? ¿Anglicismos controlados? | Coherencia linguistica |

3. PROPONER mejoras con prioridad:
   - P0: Perdida de fidelidad, SSOT violado.
   - P1: Grasa, independencia chunk rota, prosa sin promover.
   - P2: Tags, formato, anglicismos.
4. PRESENTAR propuestas al usuario con tabla {prioridad, eje, hallazgo, mejora_propuesta}.
5. IMPLEMENTAR mejoras aprobadas.
6. Bump version segun impacto.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artefacto_optimizado | string | Artefacto con mejoras aplicadas |
| mejoras_propuestas | {prioridad, eje, hallazgo, propuesta}[] | Mejoras identificadas |
| mejoras_aplicadas | string[] | Mejoras implementadas (aprobadas por usuario) |
| version_anterior | string | Version antes de optimizacion |
| version_nueva | string | Version despues de optimizacion |
| metricas_antes | {FS: number, CR: number} | Metricas pre-optimizacion |
| metricas_despues | {FS: number, CR: number} | Metricas post-optimizacion |
