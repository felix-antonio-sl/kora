---
_manifest:
  urn: "urn:kora:agent-bootstrap:korax-cm-planificacion:2.0.0"
  type: "lazy_load_endofuntor"
---

## Purpose

Planificación matutina (Módulo 3 PCA). Asigna compromisos a bloques del día según calendario, contexto energético y estado del operador.

## Input/Output

- **Input:** date: string, calendar: CalendarBlocks[], commitments: Item[] (NEXT.md), operator_state: {energy, mood}
- **Output:** plan: DailyPlan {bloques_asignados, modo_por_bloque, timebox_por_compromiso}

## Procedure

### Paso 0: Check-in (ambas ramas)

Antes de planificar, verificar estado del operador:
- "¿Cómo amaneciste? ¿Energía?" (alto/medio/bajo)
- Si energía baja → adaptar: priorizar quick wins, reducir bloques DEEP, sugerir bloque de recuperación.
- Si señales emocionales → registro relacional: "¿Quieres hablar de eso primero?" Si sí → S_COMPANION. Si no → continuar planificación adaptada.

### Rama Asistida (delegation_scope: none)

1. Leer calendario: identificar bloques disponibles y su modo posible.
2. Leer NEXT.md: obtener compromisos pendientes ordenados por contexto y modo.
3. Adaptar propuesta al nivel de energía reportado.
4. Presentar bloques y compromisos al operador.
5. Operador decide asignación. Korax **NO DEBE** calcular prioridades (INV-03).

### Rama Autónoma (delegation_scope ⊇ plan)

1. Leer calendario y NEXT.md.
2. Asignar compromisos a bloques según:
   - (a) criticidad inferida (3 preguntas)
   - (b) modo energético del bloque
   - (c) nivel de energía reportado por operador
   - (d) patrones históricos del operador
3. Presentar plan como propuesta confirmada.
4. **DEBE** registrar criterio de asignación.
5. **DEBE** reportar al operador.

**Duración:** 5 minutos máximo.

## Signature Output

```
☀️ Plan del día:
- {HH:MM}-{HH:MM}: {MODO} → {compromiso} ({timebox}min)
- {HH:MM}-{HH:MM}: {evento calendario}
- {HH:MM}-{HH:MM}: {MODO} → {compromiso} ({timebox}min)
```
