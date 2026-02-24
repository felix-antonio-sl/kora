---
_manifest:
  urn: "urn:kora:skill:orquestador-generico-protocol-selector:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-PROTOCOL-SELECTOR

## Proposito

Seleccionar el protocolo de orquestacion optimo para un conjunto de participantes y objetivo dado, basandose en las dependencias entre tareas.

## Procedimiento

1. Recibir objetivo de la orquestacion y lista de participantes con sus capacidades
2. Analizar dependencias entre las tareas que deben ejecutar los participantes
3. Aplicar criterio de seleccion:
   - Dependencias lineales (B requiere output de A): SECUENCIAL
   - Tareas independientes (pueden ejecutarse simultaneamente): PARALELO
   - Siguiente tarea depende de resultado previo (ramificacion dinamica): DINAMICO
   - Multiples perspectivas que deben converger en consenso: CONSENSO
4. Verificar que el protocolo seleccionado es viable con los participantes disponibles
5. Si ambiguo: recomendar protocolo mas simple primero (SECUENCIAL > PARALELO > DINAMICO > CONSENSO)

## Output

Protocolo seleccionado (SECUENCIAL | PARALELO | DINAMICO | CONSENSO) + justificacion basada en dependencias + orden de ejecucion propuesto para los participantes.
