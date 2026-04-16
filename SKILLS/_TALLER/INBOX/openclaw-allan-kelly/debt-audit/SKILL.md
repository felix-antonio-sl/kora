---
name: debt-audit
description: Audit agentic debt across four dimensions — eval debt, context debt, autonomy debt, and observability debt. Use when diagnosing why an agentic system underperforms, produces regressions, or costs more than expected for the value delivered.
---

# Debt Audit

Auditar deuda agentica en cuatro dimensiones.

## Cuando activar

- El usuario sospecha que su sistema agentico no rinde como deberia.
- Hay regresiones pese a tests verdes.
- Los costes suben pero el valor no.
- Los agentes producen mucho pero el impacto real es bajo.
- Necesita un diagnostico estructurado antes de tomar decisiones.

## Procedimiento

1. **Recoger sintomas.** Que observa el usuario? Desde cuando? Que ha cambiado?
2. **Auditar eval debt.** Evaluacion fragil, incompleta, dependiente del autor, datasets obsoletos.
3. **Auditar context debt.** Contexto pobre, obsoleto, ambiguo, excesivo, no versionado.
4. **Auditar autonomy debt.** Delegacion sin limites, aprobacion sin lectura, permisos inflados.
5. **Auditar observability debt.** Ejecucion sin logging, sin dashboard, sin alertas, sin metricas.
6. **Cruzar deudas.** La combinacion es peor que la suma: eval debt + autonomy debt = riesgo critico.
7. **Priorizar.** Severidad × probabilidad de impacto × facilidad de correccion.
8. **Recomendar.** Acciones concretas por deuda, con owner sugerido y timeline.

## Formato de salida

```
## Debt Audit: {scope}
- Fecha: {YYYY-MM-DD}
- Sintomas reportados: {lista}

| Tipo | Hallazgo | Severidad | Cruce | Accion sugerida | Owner sugerido |
|---|---|---|---|---|---|
| eval | {desc} | H/M/L | {con que otra deuda interactua} | {recomendacion} | {rol} |
| context | ... | ... | ... | ... | ... |
| autonomy | ... | ... | ... | ... | ... |
| observability | ... | ... | ... | ... | ... |

### Riesgos compuestos
- {deuda A} + {deuda B} = {riesgo compuesto y consecuencia}

### Recomendaciones priorizadas
1. {accion mas urgente}
2. {siguiente}
3. ...
```

## Gotchas

- Las deudas se esconden detras de metricas verdes. Verde no es sano si los evals son fragiles.
- Context debt es la mas silenciosa: degrada gradualmente sin evento visible.
- Autonomy debt solo explota cuando algo sale muy mal. No esperar al incidente.
- Si todas las deudas son "bajas", probablemente la auditoria fue superficial.
