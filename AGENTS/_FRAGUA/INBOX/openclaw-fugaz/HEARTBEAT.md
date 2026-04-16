# Heartbeat

## Checks (en orden, detener al primer CRITICO)

1. `session_status` — verificar modelo activo, contexto disponible, y cache hit rate
2. Verificar que los repos de trabajo en `/home/felix/projects/` existen y no tienen conflictos de merge pendientes
3. Revisar si `memory/` tiene notas del dia actual. Si no, considerar si hubo sesion activa reciente que deberia haber generado memoria
4. Verificar que skills de dominio cargan: `blast-radius-estimator`, `repo-architect`, `loop-closer`, `context-hygiene`
5. Verificar espacio en disco (`df -h /home/felix`) — WARN si > 85%

6. Verificar KORA accesible: `ls /home/felix/kora/KNOWLEDGE/fxsl/opm/` — si falla: WARN

## Severidad

- CRITICO: modelo no responde, disco > 95%, repos con conflictos bloqueantes
- WARN: sin memoria del dia con sesion activa, disco > 85%, skills no cargan, KORA inaccesible
- OK: todo normal

## Regla

Si no hay nada que reportar, responde solo: HEARTBEAT_OK
