---
_manifest:
  urn: "urn:kora:skill:guardian-improvement-generator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-IMPROVEMENT-GENERATOR

## Proposito

Generar propuestas de mejora coherentes para el ecosistema KORA identificando gaps y fricciones, estructuradas como RFC evaluable.

## Procedimiento

1. Identificar el area de mejora: gap de funcionalidad, friccion de uso, inconsistencia detectada, o necesidad emergente
2. Describir la solucion propuesta con precision tecnica: que cambia, como cambia, que queda igual
3. Analizar impacto en componentes del ecosistema: Spec, Agent, Hub, Life, Test, Federation
4. Verificar coherencia con P1-P7 antes de proponer
5. Estructurar como RFC minimo: Titulo | Problema | Solucion | Impacto | Compatibilidad-Atras | Criterios-Aceptacion
6. Escalar a S-EVALUATOR para veredicto formal

## Output

RFC estructurado: Titulo, Problema, Solucion propuesta, Impacto por componente, Compatibilidad hacia atras, Criterios de aceptacion.
