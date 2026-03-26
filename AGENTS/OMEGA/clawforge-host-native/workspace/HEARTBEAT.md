# Heartbeat

1. `openclaw health --json` — debe estar healthy. Si no: CRIT.
2. `free -h` — si disponible < 4GB: WARN.
3. `df -h /` — si uso > 80%: WARN.
4. Si algo falla: reportar severidad, capa (host/gateway), detalle.
5. Si todo OK: HEARTBEAT_OK.
