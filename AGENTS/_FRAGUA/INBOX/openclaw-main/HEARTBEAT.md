# Heartbeat

## hetzner2897261 (local)
1. `zsh -ic 'openclaw health --json'` — debe estar healthy. Si no: CRIT.
2. `free -h` — si disponible < 4GB: WARN.
3. `df -h /` — si uso > 80%: WARN.

## clawdbot-hetzner (remoto)
4. `ssh clawdbot@157.180.121.173 'export PATH="$HOME/.npm-global/bin:$PATH" && openclaw health --json'` — debe estar healthy. Si no: CRIT.
5. `ssh clawdbot@157.180.121.173 'free -h'` — si disponible < 4GB: WARN.

## Conocimiento y memoria
6. Verificar que KORA es accesible: `ls /home/felix/kora/KNOWLEDGE/agengai/openclaw/documentacion-oficial/ > /dev/null` — si falla: WARN.
7. `openclaw memory status` — verificar que el indice de memoria esta sano y los extraPaths configurados estan indexados. Si hay errores: WARN.

## Cierre
- Si algo falla: reportar severidad, capa (host/gateway/kora/memoria), servidor, detalle.
- Si todo OK en ambos: HEARTBEAT_OK.
