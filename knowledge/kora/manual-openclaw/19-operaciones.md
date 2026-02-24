---
_manifest:
  urn: urn:kora:kb:19-operaciones
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '19'
- operaciones
lang: es
---

# Capítulo 19 — Operaciones

> **Propósito:** Referencia práctica para el día a día operativo: diagnosticar, monitorear, respaldar y recuperar. No es teoría — es el runbook.

- ---


## 19.1 Diagnóstico Rápido

### openclaw status

```bash
openclaw status          # resumen general
openclaw status --all    # detallado (safe to share, secrets redacted)
```

- Muestra: gateway version, uptime, canales conectados, agentes, modelos, sesiones activas, cron jobs, heartbeat state.


### openclaw doctor

```bash
openclaw doctor                    # diagnóstico + recomendaciones
openclaw doctor --fix              # aplicar fixes automáticos
openclaw doctor --generate-gateway-token   # generar token seguro
```

- Diagnostica: config obsoleta, permisos, migraciones pendientes, token faltante.


### openclaw security audit

```bash
openclaw security audit            # quick
openclaw security audit --deep     # + live probe
openclaw security audit --fix      # auto-fix
```

### openclaw sessions

```bash
openclaw sessions                  # listar todas
openclaw sessions --active 60      # activas última hora
openclaw sessions --json           # parseable
openclaw sessions --agent work     # filtrar por agente
```

### openclaw sandbox explain

```bash
openclaw sandbox explain                          # default agent
openclaw sandbox explain --agent work             # agente específico
openclaw sandbox explain --session agent:work:main  # sesión específica
openclaw sandbox explain --json                   # parseable
```

- ---


## 19.2 Gateway (systemd)

### Comandos esenciales

```bash
# Estado
sudo systemctl status openclaw-gateway

# Reiniciar (recarga config)
sudo systemctl restart openclaw-gateway

# Logs en vivo
sudo journalctl -u openclaw-gateway -f

# Logs últimas 200 líneas
sudo journalctl -u openclaw-gateway --tail 200

# Ver puerto
ss -ltnp | grep 18789

# Health check
curl -s http://localhost:18789/health
```

### Hot reload

- Algunos cambios de config se aplican sin restart:

- Model aliases y fallbacks
- Tool policy changes
- Session config (dmScope, reset)

- Cambios que requieren restart:

- Channel connections (nuevos bots, cuentas)
- Gateway port/bind/auth
- Plugin changes
- Hook changes

### Restart seguro

```bash
# 1. Verificar que no hay runs activos críticos
openclaw sessions --active 5

# 2. Restart
sudo systemctl restart openclaw-gateway

# 3. Verificar
openclaw status
curl -s http://localhost:18789/health
```

- ---


## 19.3 Logging

### Ubicación

```
Default:    /tmp/openclaw/openclaw-YYYY-MM-DD.log
Custom:     logging.file en openclaw.json
Systemd:    journalctl -u openclaw-gateway
```

### Redaction

```json5
{
  logging: {
    redactSensitive: "tools",      // default: redacta tool summaries
    redactPatterns: [
      "sk-ant-[a-zA-Z0-9]+",       // Anthropic keys
      "Bearer [a-zA-Z0-9]+"         // Bearer tokens
    ]
  }
}
```

### Filtrar logs útiles

```bash
# Errores
journalctl -u openclaw-gateway | grep -i error

# Routing de agentes
journalctl -u openclaw-gateway | grep routing

# Tool calls
journalctl -u openclaw-gateway | grep "tool_call"

# Heartbeats
journalctl -u openclaw-gateway | grep heartbeat

# Cron
journalctl -u openclaw-gateway | grep cron
```

### Retention

- Los logs no se auto-rotan.
- Configurar logrotate o limpiar manualmente:


```bash
# Limpiar logs >7 días
find /tmp/openclaw/ -name 'openclaw-*.log' -mtime +7 -delete
```

- ---


## 19.4 Backup Strategy

### Qué respaldar

| Qué | Ubicación | Frecuencia | Criticidad |
|-----|-----------|------------|-----------|
| Config | `~/.openclaw/openclaw.json` | Después de cambios | Alta |
| Secrets/env | `~/.openclaw/.env` | Después de cambios | Alta |
| Auth profiles | `~/.openclaw/agents/*/agent/auth-profiles.json` | Después de re-auth | Alta |
| Channel creds | `~/.openclaw/credentials/` | Después de cambios | Alta |
| Workspace | `~/clawd/` (o custom) | Semanal | Media |
| Memoria | `~/clawd/memory/` | Diario (auto via git) | Alta |
| Sessions | `~/.openclaw/agents/*/sessions/` | Opcional | Baja |
| Cron jobs | `~/.openclaw/cron/jobs.json` | Después de cambios | Media |

### Script de backup

```bash
#!/bin/bash
BACKUP_DIR=~/backups
DATE=$(date +%Y%m%d)

tar -czvf "$BACKUP_DIR/openclaw-$DATE.tar.gz" \
  ~/.openclaw/openclaw.json \
  ~/.openclaw/.env \
  ~/.openclaw/agents/*/agent/auth-profiles.json \
  ~/.openclaw/credentials/ \
  ~/.openclaw/cron/jobs.json \
  ~/clawd/

echo "Backup: $BACKUP_DIR/openclaw-$DATE.tar.gz"
```

### Recuperación

```bash
# 1. Detener gateway
sudo systemctl stop openclaw-gateway

# 2. Restaurar
tar -xzvf ~/backups/openclaw-20260220.tar.gz -C /

# 3. Verificar permisos
chmod 700 ~/.openclaw
chmod 600 ~/.openclaw/openclaw.json
chmod 600 ~/.openclaw/.env

# 4. Reiniciar
sudo systemctl start openclaw-gateway
openclaw status
```

- ---


## 19.5 Monitoreo

### Health check periódico (cron del OS)

```bash
# /etc/cron.d/openclaw-health
*/5 * * * * clawdbot curl -sf http://localhost:18789/health || systemctl restart openclaw-gateway
```

### Alertas por espacio en disco

```bash
# Sessions y logs pueden crecer
du -sh ~/.openclaw/agents/*/sessions/
du -sh /tmp/openclaw/
```

### Métricas de sesión

```bash
# Sesiones activas
openclaw sessions --active 60 --json | jq length

# Tokens consumidos (de sessions.json)
cat ~/.openclaw/agents/main/sessions/sessions.json | jq '[.[].totalTokens] | add'
```

- ---


## 19.6 Mantenimiento Periódico

### Semanal

- [ ] `openclaw security audit`
- [ ] Verificar espacio en disco
- [ ] Limpiar sessions viejas si necesario
- [ ] Verificar que cron jobs corren correctamente (`openclaw cron runs`)

### Mensual

- [ ] `openclaw security audit --deep`
- [ ] Backup completo
- [ ] Revisar y podar MEMORY.md
- [ ] Verificar créditos de providers (billing)
- [ ] Actualizar OpenClaw si hay nueva versión

### Post-cambio de config

- [ ] `openclaw doctor`
- [ ] `openclaw security audit`
- [ ] Verificar routing: `openclaw agents list --bindings`
- [ ] Verificar tools: `openclaw sandbox explain`
- [ ] Backup de config

- ---


## Resumen del Capítulo

| Tarea | Herramienta |
|-------|-------------|
| Diagnóstico general | `openclaw status --all` |
| Fix automáticos | `openclaw doctor --fix` |
| Auditoría de seguridad | `openclaw security audit --deep` |
| Ver sesiones | `openclaw sessions --active 60` |
| Ver tools resueltos | `openclaw sandbox explain --agent <id>` |
| Logs en vivo | `journalctl -u openclaw-gateway -f` |
| Backup | Script tar.gz de config + workspace + credentials |
| Health monitoring | Cron del OS + curl health endpoint |
| Incident response | Stop → Rotate → Audit → Report |

- ---


- *Siguiente: [Capítulo 20 — Patrones de Diseño](20-patrones-diseno.md) (Parte VI)*

