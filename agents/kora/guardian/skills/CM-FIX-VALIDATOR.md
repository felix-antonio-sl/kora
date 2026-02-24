---
_manifest:
  urn: "urn:kora:skill:guardian-fix-validator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-FIX-VALIDATOR

## Proposito

Validar que una correccion propuesta resuelve efectivamente el issue detectado por CM-drift-analyzer sin introducir riesgos residuales.

## Procedimiento

1. Recibir fix propuesto y el issue original que lo motiva
2. Verificar que el fix aborda directamente la causa raiz identificada (no solo el sintoma)
3. Re-ejecutar logicamente el chequeo que detecto el issue contra el fix aplicado
4. Evaluar riesgo residual: ¿el fix introduce nuevos problemas o dependencias?
5. Verificar que el fix respeta principios P1-P7 (no genera nueva deuda tecnica)
6. Clasificar resultado: RESOLVED | PARTIAL (con pendientes) | INSUFFICIENT (requiere otro enfoque)
7. Si PARTIAL o INSUFFICIENT: detallar que queda por resolver

## Output

Clasificacion del fix (RESOLVED | PARTIAL | INSUFFICIENT) + evidencia del chequeo re-ejecutado + riesgo residual si aplica + proximos pasos.
