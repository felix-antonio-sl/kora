---
_manifest:
  urn: "urn:kora:skill:curator-artifact-optimizer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-ARTIFACT-OPTIMIZER

## Proposito
Analiza artefactos existentes y propone mejoras de calidad: telegrafizacion, estructura RAG, deduplicacion, referencias, densidad semantica.

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

## Output
Artefacto optimizado. Reporte: {mejoras_propuestas: [{prioridad, eje, hallazgo, propuesta}], mejoras_aplicadas[], version_anterior, version_nueva, metricas_antes: {FS, CR}, metricas_despues: {FS, CR}}.
