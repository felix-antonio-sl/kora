---
name: sandbox-architect
description: >-
  Design sandbox architecture and tool policies for OpenClaw agents.
  Use when the user wants to configure sandboxing, define tool allow or deny
  policies, set up exec approvals, or configure elevated mode.
---

## Alcance

Arquitectura de sandbox y politicas de herramientas para agentes OpenClaw.
Cubre: modo sandbox, scope, politicas allow/deny, aprobaciones exec y modo elevado.

## Procedimiento

### 1. Evaluar perfil de riesgo

Preguntas clave:
- El agente ejecuta codigo? (bash, scripts, etc.)
- Tiene acceso a datos sensibles?
- Opera en entorno compartido o dedicado?
- Quien interactua con el? (admin, usuarios externos, automatizaciones)

### 2. Elegir modo sandbox

| Modo | Comportamiento | Cuando usar |
|------|---------------|-------------|
| `off` | Sin sandbox | Solo desarrollo local o agentes sin exec |
| `non-main` | Sandbox en sub-agentes | Agente principal confiable, sub-agentes no |
| `all` | Todo sandboxed | Produccion, agentes expuestos a usuarios externos |

### 3. Elegir scope

| Scope | Comportamiento |
|-------|---------------|
| `session` | Sandbox aislado por sesion, se destruye al terminar |
| `agent` | Sandbox persistente por agente, compartido entre sesiones |
| `shared` | Sandbox compartido entre agentes (usar con precaucion) |

### 4. Definir politica de herramientas

```json
{
  "sandbox": {
    "mode": "all",
    "scope": "session"
  },
  "tools": {
    "allow": ["read", "write", "glob", "grep", "bash"],
    "deny": ["web_search"],
    "requireApproval": ["bash"]
  }
}
```

- `allow`: lista explicita de tools permitidos.
- `deny`: tools bloqueados (tiene precedencia sobre allow).
- `requireApproval`: tools que requieren confirmacion del usuario antes de ejecutar.

### 5. Configurar modo elevado (opcional)

Para operaciones administrativas que necesitan salir del sandbox temporalmente:

```json
{
  "elevated": {
    "enabled": true,
    "requireApproval": true,
    "timeout": 300
  }
}
```

### 6. Aplicar y verificar

```bash
openclaw config set sandbox --from-json fragment.json
openclaw config validate
openclaw sandbox explain --agent <name>
openclaw agent reload <name>
```

`sandbox explain` muestra la politica efectiva resuelta, incluyendo herencias.

## Notas

- Principio de minimo privilegio: empezar restrictivo, abrir segun necesidad.
- `deny` siempre gana sobre `allow`.
- `requireApproval` en `bash` es recomendado para agentes expuestos a usuarios externos.
- Revisar politica efectiva con `sandbox explain` despues de cada cambio.
