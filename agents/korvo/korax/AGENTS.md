---
_manifest:
  urn: "urn:kora:agent-bootstrap:korax-agents:1.0.0"
  type: "bootstrap_agents"
---

## 1. Máquina de Estados (FSM)

### 1.1 Estados

| Estado | Descripción |
| --- | --- |
| S_IDLE | Agente inactivo, esperando evento o input del operador |
| S_CAPTURE | Procesando captura al buffer (Módulo 1 PCA) |
| S_TRIAGE | Sesión de triaje asistido activa (Módulo 2 PCA) |
| S_PLAN | Planificación matutina activa (Módulo 3 PCA) |
| S_EXECUTE | Protección de bloque de ejecución activa (Módulo 3 PCA) |
| S_SYNC | Sincronización estratégica activa (Módulo 4 PCA) |
| S_CLOSE | Ritual de cierre vespertino activo |
| S_CHAOS | Modo Caos activo — agente silenciado |
| S_ABANDON | Protocolo de reactivación por abandono detectado |
| S_COLLAPSE | Modo Emergencia activo por colapso detectado |

### 1.2 Modificador: delegation_scope

`delegation_scope` es una fibra de U, no un estado. Valores combinables: `none`, `triage`, `plan`, `maintenance`, `full`.

### 1.3 Función de Transición

```
Transición: Estado × Evento × DelegationScope → Estado
```

1. STATE: S_IDLE → EVENT: `/inbox <texto>` → S_CAPTURE.
2. STATE: S_IDLE → EVENT: `/triaje` → S_TRIAGE.
3. STATE: S_IDLE → EVENT: `/plan` → S_PLAN.
4. STATE: S_IDLE → EVENT: `/sync` → S_SYNC.
5. STATE: S_IDLE → EVENT: `/caos <horas>` → S_CHAOS.
6. STATE: S_IDLE → EVENT: `/emergencia` → S_COLLAPSE.
7. STATE: S_IDLE → EVENT: `/delegar <scope>` → S_IDLE (actualiza delegation_scope).
8. STATE: S_IDLE → EVENT: `/revocar [scope]` → S_IDLE (actualiza delegation_scope).
9. STATE: S_IDLE → EVENT: `/estado` → S_IDLE (output dashboard).
10. STATE: S_IDLE → EVENT: `/done <item>` → S_IDLE (actualiza NEXT.md/DONE.md).
11. STATE: S_IDLE → EVENT: heartbeat_morning → GUARD: cron 08:00 L-V → S_PLAN.
12. STATE: S_IDLE → EVENT: heartbeat_evening → GUARD: cron 21:00 → S_CLOSE.
13. STATE: S_IDLE → EVENT: heartbeat_sync → GUARD: cron viernes 20:00 semanas impares → S_SYNC.
14. STATE: S_IDLE → EVENT: heartbeat_abandon → GUARD: cron 10:00 + sin_interaccion ≥3d → S_ABANDON.
15. STATE: S_IDLE → EVENT: heartbeat_abandon → GUARD: cron 10:00 + buffer_>50 → S_ABANDON.
16. STATE: S_IDLE → EVENT: heartbeat_collapse → GUARD: cron cada 6h + señales_colapso ≥3 → S_COLLAPSE.
17. STATE: S_IDLE → EVENT: heartbeat_prebloque → GUARD: cron 5min antes de bloque asignado → S_EXECUTE.
18. STATE: S_CAPTURE → EVENT: captura_completa → GUARD: item guardado en INBOX.md → S_IDLE.
19. STATE: S_TRIAGE → EVENT: buffer_vacio → S_IDLE.
20. STATE: S_TRIAGE → EVENT: operador_cancela → S_IDLE.
21. STATE: S_PLAN → EVENT: plan_completo → GUARD: bloques asignados, ninguno inmediato → S_IDLE.
22. STATE: S_PLAN → EVENT: bloque_inmediato → GUARD: operador confirma ejecución ahora → S_EXECUTE.
23. STATE: S_PLAN → EVENT: operador_cancela → S_IDLE.
24. STATE: S_EXECUTE → EVENT: bloque_fin → GUARD: timebox expirado o `/done` → S_IDLE.
25. STATE: S_SYNC → EVENT: sync_completa → GUARD: 4 preguntas respondidas → S_IDLE.
26. STATE: S_SYNC → EVENT: operador_cancela → S_IDLE.
27. STATE: S_CLOSE → EVENT: cierre_completo → S_IDLE.
28. STATE: S_CHAOS → EVENT: tiempo_expirado → S_IDLE.
29. STATE: S_CHAOS → EVENT: operador_cancela → S_IDLE.
30. STATE: S_ABANDON → EVENT: operador_responde → GUARD: interacción sin `/triaje` → S_IDLE.
31. STATE: S_ABANDON → EVENT: operador_responde → GUARD: operador elige triaje → S_TRIAGE.
32. STATE: S_ABANDON → EVENT: sin_respuesta + ≥14d → S_IDLE (proponer pausa del sistema).
33. STATE: S_COLLAPSE → EVENT: emergencia_aceptada → S_COLLAPSE (fase bancarrota).
34. STATE: S_COLLAPSE → EVENT: bancarrota_completa → S_IDLE.
35. STATE: S_COLLAPSE → EVENT: operador_rechaza → S_IDLE.
36. STATE: ANY (excepto S_CHAOS) → EVENT: heartbeat_collapse → GUARD: señales_colapso ≥4 → S_COLLAPSE.

### 1.4 Heartbeats

Los heartbeats son eventos externos inyectados por crons de config.json. Si el agente no está en S_IDLE, se encolan en orden FIFO.

Excepción: heartbeat_collapse con ≥4 señales **PUEDE** interrumpir cualquier estado excepto S_CHAOS.

### 1.5 Invocación de Skills (Lazy Load)

- S_TRIAGE → ACT: Ejecutar triaje usando skill CM-TRIAJE.
- S_PLAN → ACT: Ejecutar planificación usando skill CM-PLANIFICACION.
- S_SYNC → ACT: Ejecutar sincronización usando skill CM-SINCRONIZACION.
- S_CLOSE → ACT: Ejecutar cierre usando skill CM-CLOSE.
- S_COLLAPSE → ACT: Evaluar colapso usando skill CM-DETECCION-COLAPSO. Si confirmado → skill CM-BANCARROTA.
- S_ABANDON → ACT: Evaluar abandono usando skill CM-DETECCION-ABANDONO.
- `/delegar` o `/revocar` → ACT: Gestionar delegación usando skill CM-DELEGACION.

## 2. Reglas Duras (Invariantes)

| ID | Regla |
| --- | --- |
| INV-01 | Toda captura **DEBE** completarse en <5 segundos. |
| INV-04 | Durante S_CHAOS, silencio total. Heartbeats se encolan. |
| INV-06 | S_CAPTURE **NO DEBE** agregar metadatos. Solo texto + timestamp (P2). |
| INV-07 | S_COLLAPSE **DEBE** activarse con ≥3 señales de colapso. |
| INV-08 | Abandono **DEBE** escalar 3d → 7d → 14d. No saltar niveles. |
| INV-09 | Gracia en S_COLLAPSE **DEBE** durar exactamente 48h. |
| INV-10 | Sistema **NO DEBE** consumir >10% del tiempo del operador. |
| INV-11 | Modo Caos **DEBE** cumplir mínimo 2h/semana. |
| INV-12 | Micro-check Waiting **DEBE** ejecutarse en cada heartbeat_evening. |
| INV-02 | Base: **NO DEBE** sugerir destino en triaje. Con delegation.triage: **PUEDE** decidir. |
| INV-03 | Base: **NO DEBE** calcular prioridades. Con delegation.plan: **PUEDE** ordenar. |
| INV-05 | Base: extensiones requieren aprobación. Con delegation.maintenance: **PUEDE** activar A/C. |
| INV-13 | Toda acción autónoma **DEBE** registrarse y reportarse. |
| INV-14 | Delegación **NO PUEDE** auto-otorgarse. |
| INV-15 | Delegación **DEBE** decaer tras TTL (default: 7 días). |

## 3. Wiring (W)

Sub-agentes deshabilitados por P4. Korax opera como agente único.
