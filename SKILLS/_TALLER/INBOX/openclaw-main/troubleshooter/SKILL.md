---
name: troubleshooter
description: Diagnosticar y reparar problemas en host y gateway con minima intervencion. Usar cuando un agente no responde, mensajes no llegan, skills no cargan, config tiene errores, performance degradada, o canales desconectados.
---

## Alcance

Diagnostico y reparacion de problemas en agentes OpenClaw desplegados en host.
Capas cubiertas: recursos del host, proceso gateway, config, canales, skills.

## Procedimiento

### 1. Observar sintomas

Recopilar datos antes de actuar:

```bash
openclaw doctor              # diagnostico global
openclaw status              # estado del gateway
openclaw health --json       # health detallado
openclaw logs --follow       # logs en tiempo real
```

### 2. Clasificar capa

| Capa | Sintomas tipicos |
|------|-----------------|
| Host | disco lleno, OOM, CPU 100%, proceso caido |
| Gateway | no responde, crash loop, port conflict |
| Config | agente no carga, schema errors, missing keys |
| Canales | mensajes no llegan, bot offline, webhook falla |
| Skills | skill no ejecuta, timeout, error en carga |

### 3. Diagnostico en cascada (de abajo hacia arriba)

Seguir este checklist en orden. Detenerse en la primera falla encontrada.

**Checklist de depuracion:**

- [ ] **Recursos host**: `df -h`, `free -m`, `top -bn1 | head -5`
- [ ] **Proceso gateway**: `pgrep -f openclaw`, `systemctl --user status openclaw-gateway`
- [ ] **Puerto disponible**: `ss -tlnp | grep 18789`
- [ ] **Health endpoint**: `curl -fsS http://127.0.0.1:18790/healthz`
- [ ] **Config valida**: `openclaw config validate`
- [ ] **Agentes cargados**: `openclaw agents list`
- [ ] **Canal conectado**: `openclaw channels status`
- [ ] **Skills cargados**: `openclaw skills list --eligible`
- [ ] **Logs de error**: `openclaw logs --level error`

### 4. Identificar causa raiz

- Correlacionar la capa que falla con el sintoma reportado.
- Buscar el error mas profundo (earliest/lowest layer).

### 5. Aplicar fix minimo

- Preferir `openclaw daemon reload` sobre `openclaw gateway restart`; restart sobre reinstall.
- Un solo cambio a la vez. Verificar despues de cada cambio.
- Si el fix requiere editar config: usar `gateway → config.patch` (valida antes de escribir).

### 6. Verificar

```bash
openclaw doctor
openclaw health --json
```

Confirmar que el sintoma original desaparecio y no hay efectos secundarios.

## Notas

- No reiniciar el gateway completo si solo un canal o skill falla.
- Guardar logs antes de cualquier accion destructiva.
- Si el problema es recurrente, buscar causa estructural, no solo parchar.
- Puerto gateway: 18789 (RPC), 18790 (health endpoint).
