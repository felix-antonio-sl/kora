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
3. **Validar campos.** Verificar que cada campo existe en el schema actual con `openclaw config validate`.
   Si hay dudas sobre un campo: consultar `openclaw config schema` o la documentacion oficial — nunca inventar.
4. **Aplicar — via nativa obligatoria:**
   - **Campos individuales**: `openclaw config set <key> <value>` (valida antes de escribir)
   - **Cambios complejos (multiples campos)**: usar la herramienta `gateway` → `config.patch` con el fragmento JSON5 del delta.
     `config.patch` valida en memoria antes de escribir al disco. Si el campo no existe en el schema, el gateway rechaza el patch sin modificar el archivo.
   - **NUNCA** usar `write` o `edit` directamente sobre `~/.openclaw/openclaw.json` para cambios de config.
     Esas herramientas no tienen checkpoint de validacion: escriben primero, el gateway valida despues — si hay un campo invalido, el gateway muere antes de poder corregirlo.
5. **Verificar.** Ejecutar `openclaw config validate`, `openclaw doctor` y `openclaw health` para confirmar que el gateway acepto el cambio.
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
