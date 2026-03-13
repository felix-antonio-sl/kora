---
_manifest:
  urn: urn:pro:skill:salubrista-intent:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-INTENT-SALUBRISTA

## Proposito
Clasificar semanticamente la solicitud del usuario para un agente salubrista orientado a analisis, gestion, diseno, implementacion, evaluacion y vigilancia. Determina escala operativa y tipo de tarea sin decidir transiciones FSM ni continuidad conversacional.

## Input/Output
- **Input:** consulta: string
- **Output:** IntentResult { escala: "unidad"|"establecimiento"|"red"|"territorio"|"nacional"|"multi"|"na", intencion_primaria: string, objeto: string, tipo_producto: string|null, clarificacion_requerida: bool, motivo_ambiguedad: string? }

## Procedimiento
1. LEER la consulta completa e identificar el problema principal y la escala dominante.
2. CLASIFICAR la intencion:
   - IF objeto = perfil epidemiologico, carga de enfermedad, riesgo, inequidad, tendencia, grupo vulnerable -> `epi`
   - IF objeto = estructura, flujos, coordinacion, capacidad, fragmentacion, accesibilidad, continuidad -> `system`
   - IF objeto = diseno o rediseno de unidad, establecimiento, red, cartera, gobernanza o modelo de atencion -> `design`
   - IF objeto = implementacion, pilotaje, escalamiento, roadmap, gestion del cambio, factibilidad -> `implementation`
   - IF objeto = evaluacion, auditoria, desempeno, calidad, seguridad, KPIs, mejora continua -> `evaluation`
   - IF objeto = alerta, brote, vigilancia, RSI, notificacion o evento sanitario agudo -> `vigilance`
   - IF objeto = mapa de brechas, mapa de riesgos, tablero de monitoreo, informe de politica sanitaria, memo para autoridades o escenario de decision -> `product`
   - IF objeto = informe formal narrativo, memo tecnico o reporte ejecutivo -> `report`
   - IF objeto = cierre explicito de la sesion -> `end`
3. IDENTIFICAR la escala principal: unidad / establecimiento / red / territorio / nacional / multi.
4. IDENTIFICAR el objeto operativo: programa, servicio, unidad, establecimiento, red, territorio, politica, evento, tablero, otro.
5. IF `intencion_primaria = product`, IDENTIFICAR `tipo_producto`:
   - `gap_map`
   - `risk_map`
   - `monitoring_dashboard`
   - `policy_brief`
   - `decision_scenarios`
6. VERIFICAR ambiguedad: IF la consulta no permite diferenciar intencion o escala -> emitir `clarify` con motivo explicito.
7. OUTPUT: devolver escala, intencion primaria, objeto, tipo de producto si aplica y necesidad de clarificacion.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| escala | string | unidad / establecimiento / red / territorio / nacional / multi / na |
| intencion_primaria | string | `epi` / `system` / `design` / `implementation` / `evaluation` / `vigilance` / `product` / `report` / `end` / `clarify` |
| objeto | string | Unidad operativa del problema |
| tipo_producto | string? | `gap_map` / `risk_map` / `monitoring_dashboard` / `policy_brief` / `decision_scenarios` |
| escalas_secundarias | string[] | Escalas adicionales si el problema es multi-nivel |
| clarificacion_requerida | bool | True si la consulta es ambigua |
| motivo_ambiguedad | string? | Solo si clarificacion_requerida = true |
