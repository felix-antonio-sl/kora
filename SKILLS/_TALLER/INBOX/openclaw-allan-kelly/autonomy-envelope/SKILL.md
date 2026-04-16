---
name: autonomy-envelope
description: Design graduated autonomy envelopes for agents — defining what they can do freely, what requires approval, and what is prohibited. Use when delegating work to agents, setting up approval flows, or calibrating agent permissions.
---

# Autonomy Envelope

Disenar envelopes de autonomia graduados para agentes.

## Cuando activar

- El usuario quiere delegar trabajo a un agente y necesita definir limites.
- Necesita calibrar permisos de un agente existente.
- Quiere disenar flujos de aprobacion para operaciones sensibles.
- Hay autonomia mal disenada (humanos agotados revisando todo, o agentes actuando sin supervision).

## Procedimiento

1. **Inventariar acciones.** Que acciones puede tomar el agente en este contexto?
2. **Clasificar por riesgo e irreversibilidad.**
   - Verde: reversible, bajo impacto, bien evaluable → libre.
   - Amarillo: moderado impacto o parcialmente irreversible → requiere aprobacion.
   - Rojo: alto impacto, irreversible, o afecta terceros → prohibido o aprobacion estricta.
3. **Mapear a controles OpenClaw.**
   - Verde → `tools.allow`, `exec.security: allowlist` con patrones permisivos.
   - Amarillo → exec approvals interactivas, `/approve` flow.
   - Rojo → `tools.deny`, hard blocks en SOUL.md.
4. **Disenar rollback por zona.** Para acciones verdes y amarillas: como se revierte?
5. **Establecer observabilidad.** Que se loguea, donde se ve, que dispara alerta.
6. **Definir cadencia de review.** Cada cuanto se revisa el envelope para expandir o contraer.
7. **Documentar.** Producir artefacto de envelope.

## Formato de salida

```
## Autonomy Envelope: {agente o funcion}
### Zona verde (libre)
- {accion}: {justificacion}
### Zona amarilla (aprobacion)
- {accion}: {justificacion} → {mecanismo de aprobacion}
### Zona roja (prohibido)
- {accion}: {justificacion}
### Rollback
- {accion verde/amarilla}: {mecanismo de reversion}
### Observabilidad
- Logging: {que se registra}
- Alertas: {condiciones}
- Dashboard: {donde se ve}
### Config OpenClaw sugerida
- tools.allow: [...]
- tools.deny: [...]
- exec.security: {nivel}
- elevated: {estado}
### Cadencia de review: {frecuencia}
```

## Gotchas

- Autonomia binaria (todo o nada) es siempre un anti-patron.
- Mas permisos no es mas productividad. Permisos calibrados al riesgo real si lo es.
- Si el humano aprueba todo sin leer, el flujo de aprobacion no funciona — hay que subir la calidad de lo que llega.
- El envelope debe crecer o contraerse segun evidencia, no segun demanda del agente.
