---
name: sandbox-architect
description: Disenar la arquitectura de sandbox y politicas de herramientas para agentes OpenClaw. Usar cuando el usuario quiere configurar sandboxing, definir politicas allow/deny de tools, configurar exec security, o habilitar modo elevado.
---

## Alcance

Arquitectura de sandbox y politicas de herramientas para agentes OpenClaw.
Cubre: modo sandbox, scope, politicas exec, seguridad de tools y modo elevado.

## Procedimiento

### 1. Evaluar perfil de riesgo

Preguntas clave:
- El agente ejecuta comandos? (bash, scripts, etc.)
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

### 4. Definir politica de exec

```json
{
  "tools": {
    "exec": {
      "security": "allowlist",
      "ask": "on-miss"
    },
    "allow": ["read", "write", "glob", "grep"],
    "deny": ["web_search"]
  }
}
```

- `exec.security`: `"deny"` (bloquear todo exec) | `"allowlist"` (solo comandos en lista) | `"full"` (sin restriccion)
- `exec.ask`: `"off"` (nunca pedir) | `"on-miss"` (pedir si no esta en allowlist) | `"always"` (siempre pedir)
- `allow`: lista de tools permitidos.
- `deny`: tools bloqueados (tiene precedencia sobre allow).

### 5. Configurar modo elevado (opcional)

Para operaciones administrativas que necesitan permisos adicionales:

```json
{
  "tools": {
    "elevated": {
      "enabled": true,
      "allowFrom": ["admin"]
    }
  }
}
```

### 6. Aplicar y verificar

Aplicar via `gateway → config.patch` con el fragmento construido.

```bash
openclaw config validate
openclaw sandbox explain --agent <name>   # politica efectiva resuelta
openclaw daemon reload
```

`sandbox explain` muestra la politica efectiva resuelta, incluyendo herencias.

## Notas

- Principio de minimo privilegio: empezar restrictivo, abrir segun necesidad.
- `deny` siempre gana sobre `allow`.
- Para agentes expuestos a usuarios externos, usar `exec.security: "allowlist"` + `exec.ask: "always"`.
- Revisar politica efectiva con `sandbox explain` despues de cada cambio.
