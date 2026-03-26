---
name: troubleshooter
description: >-
  Diagnose and fix problems across host and gateway layers with minimum intervention.
  Use when an agent is unhealthy, messages are not arriving, skills fail to load,
  config has errors, performance is degraded, or channels are disconnected.
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
openclaw agent status <name> # estado del agente especifico
openclaw agent logs <name> --tail 100
```

### 2. Clasificar capa

| Capa | Sintomas tipicos |
|------|-----------------|
| Host | disco lleno, OOM, CPU 100%, proceso caido |
| Gateway | no responde, crash loop, port conflict |
| Config | agent no carga, schema errors, missing keys |
| Canales | mensajes no llegan, bot offline, webhook falla |
| Skills | skill no ejecuta, timeout, error en carga |

### 3. Diagnostico en cascada (de abajo hacia arriba)

Seguir este checklist en orden. Detenerse en la primera falla encontrada.

**Checklist de depuracion:**

- [ ] **Recursos host**: `df -h`, `free -m`, `top -bn1 | head -5`
- [ ] **Proceso gateway**: `pgrep -f openclaw`, `systemctl status openclaw`
- [ ] **Puerto disponible**: `ss -tlnp | grep 3000`
- [ ] **Health endpoint**: `curl -s localhost:3000/health`
- [ ] **Config valida**: `openclaw config validate`
- [ ] **Agente cargado**: `openclaw agent list`
- [ ] **Canal conectado**: `openclaw channel status --agent <name>`
- [ ] **Skills cargados**: `openclaw agent inspect <name>` (verificar skills section)
- [ ] **Logs de error**: `openclaw agent logs <name> --level error --tail 20`

### 4. Identificar causa raiz

- Correlacionar la capa que falla con el sintoma reportado.
- Buscar el error mas profundo (earliest/lowest layer).

### 5. Aplicar fix minimo

- Preferir reload sobre restart; restart sobre reinstall.
- Un solo cambio a la vez. Verificar despues de cada cambio.
- Si el fix requiere editar config: validar con `openclaw config validate` antes de aplicar.

### 6. Verificar

```bash
openclaw doctor
openclaw agent status <name>
```

Confirmar que el sintoma original desaparecio y no hay efectos secundarios.

## Notas

- No reiniciar el gateway completo si solo un agente falla.
- Guardar logs antes de cualquier accion destructiva.
- Si el problema es recurrente, buscar causa estructural, no solo parchar.
