---
_manifest:
  urn: "urn:ops:skill:verificador-regression-layer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar la capa 2 de verificacion: eval de regresion con dataset parcialmente humano. Verificar que el cambio no rompe outputs existentes. Si golden dataset disponible, usar como anchor de referencia.

## Input/Output

- **Input:** changeset: Changeset, dataset: {golden?: GoldenDataset, regression: RegressionDataset}
- **Output:** regression_result: {status: pass|degraded|warn, cases_total: number, cases_matched: number, cases_degraded: number, degradations: Degradation[], golden_anchor_used: boolean, delta: DeltaReport}

## Procedimiento

1. **Verificar disponibilidad de dataset**:
   - IF regression dataset disponible → proceder
   - IF no hay dataset → status = warn, registrar "Sin dataset de regresion. Pass condicional. ACCION REQUERIDA: crear dataset."
   - IF golden dataset disponible → usarlo como anchor de referencia

2. **Ejecutar cases de regresion**:
   - Para cada case en el dataset: ejecutar input → obtener output actual
   - Comparar output actual vs output esperado
   - Registrar match/mismatch por case

3. **Evaluar con golden dataset** (si disponible):
   - Los golden cases tienen mayor peso
   - IF golden case falla → degradation critica
   - Golden cases representan outputs validados por humanos

4. **Calcular delta**:
   - cases_matched / cases_total = tasa de match
   - Identificar cases degradados: output cambio de forma que no corresponde
   - Clasificar degradaciones: critica (golden case fallo), alta (output incorrecto), media (output diferente pero aceptable)

5. **Determinar status**:
   - IF cases_degraded == 0 → pass
   - IF degradaciones criticas > 0 → degraded (fail)
   - IF degradaciones alta > 0 → degraded (fail)
   - IF solo degradaciones media → pass con warnings

## Signature Output

```yaml
regression_result:
  status: "pass"
  cases_total: 89
  cases_matched: 89
  cases_degraded: 0
  degradations: []
  golden_anchor_used: true
  golden_cases: 12
  golden_matched: 12
  delta:
    match_rate: "100%"
    critical_degradations: 0
    high_degradations: 0
    medium_degradations: 0
```
