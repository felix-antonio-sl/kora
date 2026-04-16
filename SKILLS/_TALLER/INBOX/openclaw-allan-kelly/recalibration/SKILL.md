---
name: recalibration
description: Facilitate operational recalibration sessions for human-agent cells — combining human retrospective (sense, tension, authority, fatigue, decisions) with operational retrospective (metrics, evals, context windows, cost, failure modes). Use for periodic reviews, post-incident analysis, or when the cell needs to adjust its operating parameters.
---

# Recalibration

Facilitar sesiones de recalibracion operacional para celulas humano-agente.

## Cuando activar

- Es momento de review periodico (semanal, quincenal, mensual).
- Hubo un incidente o fallo significativo.
- La celula siente que algo no funciona pero no identifica que.
- Se necesita ajustar autonomia, topologia o limites.

## Procedimiento

### Fase 1: Retro humana (sentido, tension, autoridad)

1. **Estado del equipo.** Fatiga? Confusion? Perdida de confianza en el sistema?
2. **Tensiones.** Que fricciones aparecieron? Entre humanos? Entre humano y agente?
3. **Autoridad.** Alguien siente que perdio control? Alguien tiene demasiada carga de decision?
4. **Sentido.** El trabajo que se hace se conecta con el proposito de la celula?
5. **Decisiones pendientes.** Que se pospuso y por que?

### Fase 2: Retro operacional (metricas, evals, costes, fallos)

1. **Metricas clave.** Lead time, tasa de aceptacion, intervencion humana, coste, edad del contexto.
2. **Evals.** Que paso? Que fallo? Que eval falto?
3. **Contexto.** Deterioro? Actualizacion pendiente? Exceso?
4. **Costes.** Proporcionales al valor? Creciendo sin justificacion?
5. **Modos de fallo.** Que rompio o casi rompio? Se detecto a tiempo?

### Fase 3: Recalibracion

1. **Ajustar autonomia.** Expandir, contraer o mantener envelopes.
2. **Ajustar topologia.** Agentes a agregar, eliminar o fusionar.
3. **Ajustar memoria.** Podar obsoleto, agregar faltante, versionar contexto.
4. **Ajustar evals.** Nuevos evals necesarios? Evals obsoletos a retirar?
5. **Ajustar cadencias.** Frecuencia de review, heartbeat, cron.
6. **Comprometer acciones.** Cada ajuste tiene owner y deadline.

## Formato de salida

```
## Recalibration: {celula} — {fecha}

### Retro humana
- Estado: {resumen}
- Tensiones: {lista}
- Decisiones pendientes: {lista}

### Retro operacional
| Metrica | Valor actual | Tendencia | Diagnostico |
|---|---|---|---|
| {metrica} | {valor} | {sube/baja/estable} | {interpretacion} |

### Ajustes
| Dimension | Cambio | Owner | Deadline |
|---|---|---|---|
| Autonomia | {expandir/contraer X} | {quien} | {cuando} |
| Topologia | {agregar/eliminar agente X} | {quien} | {cuando} |
| Memoria | {podar/agregar X} | {quien} | {cuando} |
| Evals | {nuevo eval X / retirar Y} | {quien} | {cuando} |
| Cadencias | {ajustar X} | {quien} | {cuando} |

### Proxima recalibracion: {fecha}
```

## Gotchas

- La retro humana no es opcional. Sin ella, la recalibracion es ajuste tecnico sin direccion.
- Si todos los ajustes son "mantener", la recalibracion fue superficial.
- Recalibrar sin datos es opinar. Los datos vienen del control plane.
- No confundir recalibracion con escalamiento. A veces la respuesta correcta es reducir.
