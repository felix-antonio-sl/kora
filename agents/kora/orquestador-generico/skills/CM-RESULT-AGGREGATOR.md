---
_manifest:
  urn: "urn:kora:skill:orquestador-generico-result-aggregator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-RESULT-AGGREGATOR

## Proposito

Agregar los resultados individuales de participantes en una respuesta integrada coherente, aplicando la estrategia de agregacion apropiada al objetivo de la orquestacion.

## Procedimiento

1. Recopilar todos los resultados de los participantes segun protocolo ejecutado
2. Identificar convergencias: puntos de acuerdo o conclusiones compartidas entre participantes
3. Identificar divergencias: contradicciones o perspectivas incompatibles entre participantes
4. Seleccionar estrategia de agregacion:
   - UNION: incluir todas las contribuciones complementarias sin exclusion
   - INTERSECTION: incluir solo lo que todos los participantes coinciden
   - WEIGHTED: ponderar contribuciones segun rol y relevancia al objetivo
   - HIERARCHICAL: jerarquizar segun autoridad del participante en el sub-dominio
5. Construir sintesis integrada sin exponer internos de los participantes
6. Atribuir contribuciones por participante de forma visible pero no verbosa

## Output

Respuesta integrada con: convergencias destacadas, divergencias explicadas, sintesis final atribuida por participante. Sin exposicion de prompts internos.
