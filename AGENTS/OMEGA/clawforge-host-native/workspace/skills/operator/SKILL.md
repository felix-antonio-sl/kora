---
name: operator
description: >-
  Maintain a running OpenClaw agent: restart, sync config, health monitoring,
  session management, memory hygiene, cron management, and optimization.
  Use when the user needs to operate, maintain, improve, or optimize a deployed agent.
---

## Alcance

Operacion continua de un agente OpenClaw desplegado en un host.
Cubre: restart, config sync, health check, sesiones, memoria, cron y optimizacion.

## Procedimiento

### 1. Verificar estado actual

```bash
openclaw status              # estado general del gateway
openclaw agent list          # agentes activos
openclaw doctor              # diagnostico completo
```

Confirmar que el agente existe y su estado (running/stopped/error).

### 2. Identificar operacion necesaria

| Operacion | Comando |
|-----------|---------|
| Reiniciar agente | `openclaw agent restart <name>` |
| Recargar config | `openclaw agent reload <name>` |
| Ver logs | `openclaw agent logs <name> --tail 50` |
| Listar sesiones | `openclaw session list --agent <name>` |
| Limpiar memoria | `openclaw memory clear --agent <name> --before <date>` |
| Ver cron jobs | `openclaw cron list --agent <name>` |
| Crear cron | `openclaw cron add --agent <name> --schedule "<cron>" --skill <id>` |
| Eliminar cron | `openclaw cron remove <cron-id>` |

### 3. Ejecutar con evidencia

- Ejecutar el comando correspondiente.
- Capturar salida completa como evidencia.
- Si hay error, no reintentar ciegamente: diagnosticar primero.

### 4. Optimizacion

- Revisar `openclaw agent inspect <name>` para metricas de uso.
- Ajustar `maxTurns`, `model`, `maxTokens` segun patrones de uso.
- Eliminar skills no utilizados del config.
- Consolidar cron jobs redundantes.
- Limpiar sesiones antiguas periodicamente.

### 5. Verificar post-operacion

```bash
openclaw agent status <name>   # confirmar estado esperado
openclaw doctor                # sin warnings nuevos
```

## Notas

- Siempre hacer `openclaw agent reload` despues de cambiar config, no restart completo.
- Antes de optimizar modelo o tokens, revisar logs para entender patrones reales.
- Documentar cada cambio de config con motivo en el commit o nota.
