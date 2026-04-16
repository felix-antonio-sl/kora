---
name: cell-design
description: Design socio-technical cells for human-agent organizations. Use when the user needs to structure a team, define agent roles, assign ownership, or architect a delivery unit combining humans and agents with shared accountability.
---

# Cell Design

Disenar celulas socio-tecnicas estables para organizaciones humano-agente.

## Cuando activar

- El usuario quiere estructurar un equipo o celula.
- Necesita definir roles humanos y agenticos.
- Quiere disenar ownership, memoria y observabilidad de una unidad de delivery.
- Pide ayuda para organizar agentes en torno a un proposito.

## Procedimiento

1. **Identificar proposito.** Que valor produce esta celula? Para quien?
2. **Mapear humanos.** Roles: arquitecto de intencion, curador de autonomia, ingeniero de evaluacion, stakeholder experto. Un individuo puede portar varios.
3. **Mapear agentes.** Capacidades requeridas: ejecucion, analisis, verificacion, orquestacion. Cada agente con ownership claro.
4. **Disenar memoria.** Que persiste, donde (workspace, MEMORY.md, logs), con que cadencia se poda.
5. **Disenar evals.** Que se testea, quien evalua (humano vs agente vs ambos), con que datos, con que frecuencia.
6. **Disenar control plane.** Que se ve, donde (dashboard, canal, logs), con que frecuencia se revisa.
7. **Disenar rollback.** Para cada flujo autonomo: como se revierte si falla.
8. **Auditar agent sprawl.** Cada agente en la celula se justifica? Cual podria eliminarse o fusionarse?
9. **Documentar.** Producir artefacto de celula con el formato estandar.

## Formato de salida

```
## Celula: {nombre}
- Proposito: {outcome esperado}
- Beneficiario: {quien recibe valor}
- Humanos: {roles × personas}
- Agentes: {nombre × capacidad × limites}
- Memoria: {que × donde × cadencia}
- Evals: {que × quien × datos × frecuencia}
- Control plane: {que × donde × frecuencia}
- Rollback: {flujo × mecanismo}
- Deuda conocida: {eval/context/autonomy/observability}
- Cadencia de recalibracion: {frecuencia}
```

## Gotchas

- La celula no es un organigrama. Es una unidad de responsabilidad de valor.
- Un agente sin eval no es miembro de la celula; es un riesgo no gestionado.
- Mas agentes no es mejor. Menos agentes con ownership claro siempre gana.
- Si ningun humano tiene autoridad sobre la celula, la celula no existe; es un enjambre suelto.
