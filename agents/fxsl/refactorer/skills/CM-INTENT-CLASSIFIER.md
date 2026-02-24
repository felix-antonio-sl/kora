---
_manifest:
  urn: "urn:fxsl:skill:refactorer-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en la FSM WF-REFACTORER, determinando la capacidad de mejora continua requerida.

## Procedimiento
1. Analizar mensaje: palabras clave, artefactos mencionados (archivos, zonas, dependencias, metricas), contexto previo.
2. Clasificar capacidad: ANALIZAR(complejidad, duplicacion, metricas, evaluar), REFACTORIZAR(extraer, renombrar, simplificar, limpiar, verde, duplicacion), MODERNIZAR(dependencias, deprecado, actualizar, migrar, patron), DEUDA(catalogo, tendencia, reporte, retrospectiva), END(terminar).
3. Si el mensaje menciona metricas, complejidad o evaluacion de zona → ANALIZAR.
4. Si el mensaje pide mejora de codigo existente sin cambio de comportamiento → REFACTORIZAR.
5. Si el mensaje menciona dependencias outdated, patrones deprecados o migracion → MODERNIZAR.
6. Si el mensaje pide catalogo, reporte o tendencia de deuda → DEUDA.
7. Si el mensaje pide implementar feature nueva → RECHAZAR("Fuera de scope. Para features→fxsl/coder.").
8. Emitir clasificacion: {capacidad, confianza}.

## Output
Clasificacion: `capacidad` (enum), `confianza` (alta|media|baja). Si confianza=baja, preguntar.
