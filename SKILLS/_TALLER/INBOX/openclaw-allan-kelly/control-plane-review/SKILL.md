---
name: control-plane-review
description: Review and design control planes for agentic systems — dashboards, observability, logging, alerting, and metrics. Use when visibility over agent operations is insufficient, when designing monitoring for new cells, or when diagnosing governance gaps.
---

# Control Plane Review

Revisar y disenar control planes para sistemas agenticos.

## Cuando activar

- El usuario no tiene visibilidad sobre lo que sus agentes hacen.
- Necesita disenar monitoring para una celula nueva.
- Quiere auditar si su observabilidad es suficiente para gobernar.
- Diagnostica gobernanza insuficiente o excesiva.

## Procedimiento

1. **Inventariar visibilidad actual.** Que se loguea? Donde se ve? Quien mira? Con que frecuencia?
2. **Mapear puntos ciegos.** Que operaciones de agentes no tienen logging ni metricas?
3. **Evaluar metricas existentes.**
   - Lead time to validated value
   - Tasa de aceptacion al primer intento
   - Intervencion humana por unidad de valor
   - Tiempo de recuperacion
   - Coste por outcome validado
   - Edad del contexto activo
4. **Disenar metricas faltantes.** Que se necesita medir que hoy no se mide?
5. **Disenar alertas.** Que condiciones requieren intervencion humana?
6. **Mapear a herramientas OpenClaw.**
   - `openclaw logs` para logging de gateway.
   - `openclaw health` / `openclaw doctor` para estado.
   - Session transcripts en `~/.openclaw/agents/<id>/sessions/`.
   - Cron runs en `~/.openclaw/cron/runs/`.
   - `/context detail` para uso de tokens.
   - `/usage cost` para costes.
7. **Documentar.** Producir artefacto de control plane.

## Formato de salida

```
## Control Plane: {scope}
### Visibilidad actual
- {fuente}: {que se ve} — {frecuencia de revision}
### Puntos ciegos
- {operacion sin visibilidad}: {riesgo}
### Metricas activas
| Metrica | Fuente | Frecuencia | Umbral alerta |
|---|---|---|---|
| {nombre} | {de donde sale} | {cadencia} | {cuando escalar} |
### Metricas a implementar
| Metrica | Propuesta de fuente | Prioridad |
|---|---|---|
| {nombre} | {como obtenerla} | {H/M/L} |
### Alertas
| Condicion | Canal | Destinatario |
|---|---|---|
| {que dispara} | {donde se alerta} | {quien actua} |
### Gobernanza
- Cadencia de revision del control plane: {frecuencia}
- Owner del control plane: {quien}
```

## Gotchas

- Un dashboard que nadie mira no es control plane; es decoracion.
- Metricas de vanidad (mensajes enviados, tokens consumidos) no son metricas de valor.
- Si no se ve, no se puede gobernar. Pero ver todo sin filtrar es ruido, no gobierno.
- El control plane debe ser tan barato de mantener como la informacion que produce.
