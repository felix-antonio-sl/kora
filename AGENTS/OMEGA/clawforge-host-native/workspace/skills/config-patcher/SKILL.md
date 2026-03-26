---
name: config-patcher
description: Plan and apply incremental patches to live OpenClaw config without full rebuild. Use when the user wants to change a config value, add a channel, modify tool policy, or adjust model on a running gateway.
---

## Proposito

Modificar la configuracion de un agente OpenClaw en operacion mediante cambios incrementales, sin reconstruir desde cero.

## Cuando se activa

- El usuario quiere cambiar un valor de config en un agente que ya esta corriendo.
- Se necesita agregar o quitar un canal, ajustar tools policy, cambiar modelo.
- Hay que aplicar un parche sin downtime ni perdida de sessions.

## Procedimiento

1. **Leer config actual.** Obtener el `openclaw.json` vigente y el estado del gateway.
2. **Planificar el parche.** Definir que cambia y que permanece. Documentar el delta.
3. **Dry-run.** Validar el parche contra el schema antes de aplicar.
4. **Aplicar.** Usar `openclaw config set <key> <value>` para cambios puntuales o editar el archivo directamente para cambios complejos.
5. **Verificar.** Ejecutar `openclaw doctor` y `openclaw health` para confirmar que el gateway acepto el cambio.
6. **Documentar.** Registrar que se cambio, cuando, y por que.

## Reglas

- **Patch, no rebuild.** Siempre privilegiar el cambio minimo necesario.
- **Dry-run obligatorio.** Nunca aplicar sin validar primero.
- **Backup implicito.** Antes de editar el archivo, confirmar que hay forma de revertir.
- **Verificacion post-apply.** No declarar exito sin evidencia runtime.

## Formato de salida

```
**Estado actual:** <resumen de config relevante>
**Parche planificado:**
| Campo | Valor actual | Valor nuevo | Razon |
|-------|-------------|-------------|-------|
| ...   | ...         | ...         | ...   |

**Dry-run:** <PASS/FAIL + detalle>
**Aplicacion:** <comando(s) ejecutado(s)>
**Verificacion:** <resultado de doctor/health>
```
