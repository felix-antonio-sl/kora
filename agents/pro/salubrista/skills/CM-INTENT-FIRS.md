---
_manifest:
  urn: "urn:pro:skill:salubrista-intent-firs:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-FIRS

## Propósito
Clasificar la intención del usuario y posicionar el problema en la dimensión FIRS correcta (I/II/III), determinando el estado FSM destino. Previene errores de nivel antes de activar razonamiento.

## I/O

- **Input:** consulta: string (texto libre del usuario)
- **Output:** IntentResult { dimension: "I"|"II"|"III"|"multi", estado_destino: string, nivel_analisis: string, clarificacion_requerida: bool }

## Procedimiento

1. LEER consulta completa. Identificar objeto principal: ¿es un individuo/paciente? ¿es una población/grupo? ¿es una red/sistema/organización?
2. POSICIONAR en FIRS:
   - IF objeto = individuo + razonamiento clínico/diagnóstico/terapéutico → Dim I → S-CLINICAL
   - IF objeto = población + inferencia causal/brote/dinámica transmisión → Dim II → S-EPI
   - IF objeto = red/sistema/establecimiento/gestión → Dim III → S-NETWORK
   - IF objeto = evaluación/calidad/auditoría/GPC/mejora continua → S-AUDIT
   - IF objeto = alerta/brote activo/vigilancia/RSI → S-VIGILANCE
   - IF objeto = informe/reporte formal/BSC/KPIs → S-REPORT
   - IF multi-dimensión → identificar Dim primaria + notar Dims secundarias para puentes posteriores
3. IDENTIFICAR nivel de análisis explícito: individuo / equipo / servicio / red / población
4. VERIFICAR: ¿la consulta es ambigua? IF ambigua → formular pregunta de clarificación mínima (una sola pregunta)
5. OUTPUT: declarar Dim FIRS + estado destino + nivel de análisis + si requiere clarificación

## Signature Output

| Campo | Tipo | Descripción |
|-------|------|-------------|
| dimension | string | "I" / "II" / "III" / "multi" |
| estado_destino | string | S-CLINICAL / S-EPI / S-NETWORK / S-AUDIT / S-VIGILANCE / S-REPORT |
| nivel_analisis | string | individuo / equipo / servicio / red / población |
| dims_secundarias | string[] | Dimensiones FIRS adicionales si multi-nivel |
| clarificacion_requerida | bool | True si consulta ambigua |
| pregunta_clarificacion | string? | Solo si clarificacion_requerida = true |
