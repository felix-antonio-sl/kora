---
_manifest:
  urn: "urn:ops:skill:verificador-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar contexto multi-turno de la sesion de verificacion. Mantener estado acumulado (clasificaciones, capas ejecutadas, evidencia) y generar resumen de sesion en nodo terminal.

## Input/Output

- **Input:** session_history: {turns: Turn[], current_state: FSM_State, verifications: VerificationResult[]}
- **Output:** session_summary: {verifications_executed: number, verdicts: VerdictCount, layers_stats: LayerStats, diversity_providers: ProviderPair[], timeline: TimelineEntry[], recommendation: string}

## Procedimiento

1. **Agregar verificaciones ejecutadas**:
   - Contar verificaciones completas: aprobadas vs rechazadas
   - Agrupar por tipo de cambio: lectura, escritura, destructiva
   - Listar PRs verificados con verdict

2. **Compilar estadisticas de capas**:
   - Para cada capa: veces ejecutada, veces pass, veces fail
   - Identificar capa con mayor tasa de fallo
   - IF alguna capa falla consistentemente → recomendar investigacion

3. **Registrar diversidad de providers**:
   - Listar pares coder/reviewer usados
   - Verificar que diversidad se mantuvo en toda la sesion
   - IF algun par fue mismo provider → flag de alerta

4. **Compilar timeline**:
   - Secuencia cronologica: clasificacion → capa1 → capa2 → ... → verdict
   - Timestamps por accion
   - Duracion total de sesion

5. **Generar recomendacion**:
   - IF tasa rechazo > 50% → "Alta tasa de rechazo. Revisar calidad de generacion del enjambre."
   - IF capa diversidad falla frecuentemente → "Diversidad de providers insuficiente. Configurar providers alternativos."
   - IF capa seguridad acumula warnings → "Warnings de seguridad recurrentes. Revisar patrones."
   - IF todo ok → "Sesion de verificacion completada sin anomalias."

## Signature Output

```yaml
session_summary:
  verifications_executed: 4
  verdicts:
    aprobado: 3
    rechazado: 1
  by_change_type:
    lectura: 2
    escritura: 1
    destructiva: 1
  layers_stats:
    CI:
      executed: 4
      pass: 4
      fail: 0
    REGRESION:
      executed: 4
      pass: 3
      fail: 1
    DIVERSIDAD:
      executed: 3
      pass: 3
      fail: 0
    SEGURIDAD:
      executed: 2
      pass: 2
      fail: 0
    HUMANA:
      executed: 1
      pass: 1
      fail: 0
  diversity_providers:
    - coder: "Anthropic"
      reviewer: "OpenAI"
    - coder: "OpenAI"
      reviewer: "Anthropic"
  timeline:
    - timestamp: "2026-02-24T10:00:00Z"
      action: "VERIFICAR"
      detail: "PR #210 → lectura → APROBADO (3/3)"
    - timestamp: "2026-02-24T10:15:00Z"
      action: "VERIFICAR"
      detail: "PR #211 → escritura → APROBADO (4/4)"
    - timestamp: "2026-02-24T10:40:00Z"
      action: "VERIFICAR"
      detail: "PR #212 → destructiva → APROBADO (5/5)"
    - timestamp: "2026-02-24T11:00:00Z"
      action: "VERIFICAR"
      detail: "PR #213 → escritura → RECHAZADO (capa 2: regresion degradada)"
  recommendation: "Sesion completada. PR #213 requiere revision de regresion antes de re-submit."
```
