---
_manifest:
  urn: "urn:kora:skill:guardian-proposal-evaluator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-PROPOSAL-EVALUATOR

## Proposito

Evaluar propuestas de cambio al ecosistema KORA contra principios P1-P7 para emitir un veredicto fundamentado.

## Procedimiento

1. Recibir propuesta de cambio (RFC, sugerencia, idea)
2. Verificar coherencia con principios P1-P7: encapsulacion, abstraccion, federacion, minimalismo, trazabilidad, separacion de concerns, evolucion controlada
3. Evaluar compatibilidad hacia atras: ¿rompe artefactos existentes?
4. Analizar balance beneficio vs complejidad añadida
5. Contrastar con vision del ecosistema: ¿alinea con direccion KORA?
6. Emitir veredicto: APPROVE | APPROVE_WITH_MODIFICATIONS | DEFER | REJECT
7. Fundamentar veredicto con referencia explícita a principios violados o respetados
8. Si APPROVE_WITH_MODIFICATIONS: detallar modificaciones requeridas

## Output

Veredicto (APPROVE | APPROVE_WITH_MODIFICATIONS | DEFER | REJECT) + justificacion con referencias a principios P1-P7 + alternativas si aplica.
