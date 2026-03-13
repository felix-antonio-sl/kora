---
_manifest:
  urn: urn:pro:skill:salubrista-intent-firs:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-INTENT-FIRS

## Proposito
Clasificar semánticamente la intención del usuario y posicionar el problema en la dimensión FIRS correcta (I/II/III), detectando continuidad conversacional y necesidad de aclaración mínima. Produce una señal neutral para despacho; no decide transiciones FSM.

## Input/Output
- **Input:** consulta: string (texto libre del usuario)
- **Output:** IntentResult { dimension: "I"|"II"|"III"|"multi"|"na", intencion_primaria: string, nivel_analisis: string, continuidad: string, clarificacion_requerida: bool }

## Procedimiento
1. LEER consulta completa. Identificar objeto principal y continuidad: ¿es un caso nuevo, continuación, cambio de dimensión o cambio radical de tema?
2. POSICIONAR en FIRS y etiquetar intención dominante:
   - IF objeto = individuo + razonamiento clínico/diagnóstico/terapéutico → dimension "I" + intención `clinical`
   - IF objeto = población + inferencia causal/brote/dinámica transmisión → dimension "II" + intención `epi`
   - IF objeto = red/sistema/establecimiento/gestión → dimension "III" + intención `network`
   - IF objeto = evaluación/calidad/auditoría/GPC/mejora continua → conservar dimensión del objeto auditado si es inferible; en caso contrario `multi` + intención `audit`
   - IF objeto = alerta/brote activo/vigilancia/RSI → dimension "II" o `multi` según alcance + intención `vigilance`
   - IF objeto = informe/reporte formal/BSC/KPIs → conservar dimensión dominante si ya es inferible; en caso contrario `multi` + intención `report`
   - IF objeto = cierre explícito de la sesión → dimension `na` + intención `end`
   - IF multi-dimensión → identificar dimensión primaria + notar dimensiones secundarias para puentes posteriores
3. IDENTIFICAR nivel de análisis explícito: individuo / equipo / servicio / red / población / no_aplica.
4. VERIFICAR: ¿la consulta es ambigua? IF ambigua → formular una sola pregunta de clarificación y emitir intención `clarify` con dimension `na`.
5. OUTPUT: declarar dimensión FIRS + intención primaria + nivel de análisis + continuidad + si requiere clarificación.

## Signature Output
| Campo | Tipo | Descripción |
|-------|------|-------------|
| dimension | string | "I" / "II" / "III" / "multi" / "na" |
| intencion_primaria | string | `clinical` / `epi` / `network` / `audit` / `vigilance` / `report` / `end` / `clarify` |
| nivel_analisis | string | individuo / equipo / servicio / red / población / no_aplica |
| continuidad | string | nueva / continuacion / cambio_dimension / cambio_radical |
| dims_secundarias | string[] | Dimensiones FIRS adicionales si multi-nivel |
| clarificacion_requerida | bool | True si consulta ambigua |
| pregunta_clarificacion | string? | Solo si clarificacion_requerida = true |
