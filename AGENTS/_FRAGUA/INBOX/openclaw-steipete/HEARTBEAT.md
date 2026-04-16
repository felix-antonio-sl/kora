# Heartbeat

## Checks (en orden, detener al primer CRITICO)

1. `session_status` — verificar modelo activo y contexto disponible
2. `df -h /home/felix` — disco. WARN > 85%, CRITICO > 95%
3. `free -h` — RAM disponible. WARN si < 2GB
4. Verificar repos activos en `/home/felix/projects/` sin conflictos de merge pendientes
5. Verificar skills de composicion cargan: `steinberg-dispatch`, `brutal-loop-closure`, `context-hygiene`

6. Verificar KORA accesible: `ls /home/felix/kora/KNOWLEDGE/fxsl/opm/` — si falla: WARN

## Severidad

- CRITICO: modelo no responde, disco > 95%, repos con conflictos bloqueantes
- WARN: disco > 85%, RAM < 2GB, skills no cargan, KORA inaccesible
- OK: todo normal

## Regla

Si no hay nada que reportar, responde solo: HEARTBEAT_OK
