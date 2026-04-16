---
name: delegation-governor
description: Diseñar delegaciones seguras con contrato completo. Usar cuando el usuario quiere delegar trabajo a personas o agentes, o cuando una delegacion existente necesita auditoria.
---

# Delegation Governor

## Cuando activar

- El usuario quiere delegar algo.
- Una delegacion existente no tiene contrato completo.
- Auditoria de waiting fors revela delegaciones defectuosas.

## Contrato de delegacion

Toda delegacion valida debe explicitar estos 6 campos:

| Campo | Pregunta |
|---|---|
| `outcome` | que resultado se espera? |
| `owner` | quien ejecuta? |
| `limites` | que NO hacer? |
| `review` | cuando y como verificar? |
| `deadline` | fecha o condicion de retorno? |
| `failure mode` | que pasa si falla? |

Si falta un campo, la delegacion esta incompleta. Completar antes de formalizar.

## Procedimiento

1. **Identificar que se delega.** Describir la tarea.
2. **Determinar owner.** Humano o agente?
3. **Construir contrato.** Completar los 6 campos.
4. **Clasificar bucket.** `waiting for humans` o `waiting for agents`.
5. **Definir cadencia de review.** Diaria, semanal, por evento?
6. **Registrar** en bucket y memoria.

## Distincion humano vs agente

| Tipo | Requiere |
|---|---|
| Delegacion a humano | compromiso, seguimiento, contexto suficiente |
| Delegacion a agente | gating tecnico, limites explicitos, auditoria |

## Regla de oro

Delegar accion no es delegar criterio. Si la delegacion incluye juicio de significado, es incompleta.

## Gotchas

- "Que lo haga la IA" no es una delegacion. Es un deseo sin contrato.
- Delegacion sin review es abandono.
- Revisar waiting fors es parte de la Weekly Review, no un extra opcional.
