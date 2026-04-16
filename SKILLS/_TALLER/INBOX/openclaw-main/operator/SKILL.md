---
name: operator
description: Mantener un agente OpenClaw en produccion — restart, sync config, health monitoring, gestion de sesiones, higiene de memoria, cron y optimizacion. Usar cuando el usuario necesita operar, mantener, o mejorar un agente desplegado.
---

## Alcance

Operacion continua de un agente OpenClaw desplegado en un host.
Cubre: restart, config sync, health check, sesiones, memoria, cron y optimizacion.

## Procedimiento

### 1. Verificar estado actual

```bash
openclaw status              # estado general del gateway
openclaw agents list         # agentes activos y su estado
openclaw doctor              # diagnostico completo
```

### 2. Identificar operacion necesaria

| Operacion | Comando |
|-----------|---------|
| Reiniciar gateway | `openclaw gateway restart` |
| Hot-reload config | `openclaw daemon reload` |
| Ver logs | `openclaw logs --follow` |
| Listar sesiones | `openclaw sessions` |
| Higiene de memoria | editar o limpiar archivos en `~/.openclaw/workspace*/` |
| Ver cron jobs | `openclaw cron list` |
| Crear cron | `openclaw cron add --schedule "<cron>" --skill <id>` |
| Eliminar cron | `openclaw cron remove <cron-id>` |
| Health check | `openclaw health --json` |
| Auditoria profunda | `openclaw status --deep` + `openclaw agents list` |

### 3. Ejecutar con evidencia

- Ejecutar el comando correspondiente.
- Capturar salida completa como evidencia.
- Si hay error, no reintentar ciegamente: diagnosticar primero.

### 4. Optimizacion

- Revisar `openclaw status --deep` para metricas de uso.
- Ajustar `maxTurns`, `model`, `maxTokens` segun patrones de uso via `config.patch`.
- Eliminar skills no utilizados del config.
- Consolidar cron jobs redundantes.
- Limpiar sesiones antiguas periodicamente.

### 5. Verificar post-operacion

```bash
openclaw health --json       # confirmar estado esperado
openclaw doctor              # sin warnings nuevos
```

## Notas

- Para hot-reload de config (sin reiniciar el proceso), usar `openclaw daemon reload`.
- Para reinicio completo del gateway, usar `openclaw gateway restart`.
- Antes de optimizar modelo o tokens, revisar logs para entender patrones reales.
- Documentar cada cambio de config con motivo en MEMORY.md o nota de sesion.
