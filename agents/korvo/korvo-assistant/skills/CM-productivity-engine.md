---
_manifest:
  urn: "urn:korvo:agent-bootstrap:korvo-assistant-cm-productivity-engine:1.0.0"
  type: "lazy_load_endofuntor"
---

## Purpose

Motor de productividad que evalua el estado actual de Felix y propone tecnicas adaptadas al momento, energia y tipo de tareas pendientes.

## Input/Output

- **Input:** current_state: {tasks, blockers, energy_level, time_of_day}
- **Output:** productivity_plan: {assessment, technique, actions, celebration}

## Procedure

1. **Assessment** — Estado actual:
   - Listar tareas pendientes
   - Identificar bloqueos activos
   - Evaluar nivel de energia (alto/medio/bajo)
   - Tiempo disponible

2. **Technique Selection** — Seleccionar segun contexto:
   - Energia alta + tarea compleja → Bloques de focus (90 min deep work)
   - Energia media + varias tareas → Pomodoro adaptado (25/5)
   - Energia baja + inercia → Quick wins primero (tareas de 5 min)
   - Energia baja + agotamiento → Energy management (break, caminar, hidratacion)
   - Distraccion alta → Eliminacion de distracciones (modo avion, ambiente)

3. **Action Plan** — Pasos concretos:
   - Ordenar tareas por prioridad (Eisenhower)
   - Asignar tecnica a cada bloque
   - Definir checkpoints de progreso

4. **Celebration** — Refuerzo positivo:
   - Celebrar progreso, no solo completitud
   - Reconocer esfuerzo

## Signature Output

```markdown
### Estado
Energia: [nivel] | Tareas: [N pendientes] | Bloqueos: [si/no]

### Plan
1. [Tecnica] → [Tarea] (tiempo estimado)
2. ...

### Tip
[Consejo adaptado al momento]
```
