# Patch Semantics Map

Fuentes oficiales prioritarias para patching selectivo de config en OpenClaw.

## RPC y patch semantics

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/configuration.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/cli/config.md`

## Reglas relevantes

1. `config.apply` reemplaza la config completa.
2. `config.patch` usa semántica de JSON merge patch:
   - objetos mergean recursivamente
   - `null` elimina una clave
   - arrays reemplazan
3. `openclaw config set` es preferible para cambios pequeños y dirigidos.

## Restart model

Según la documentación oficial:

- `gateway.*` requiere restart
- `plugins`, `discovery`, `canvasHost` requieren restart
- `channels.*`, `agents.*`, `tools.*`, `session.*`, `messages.*` no requieren restart por defecto

## Regla

1. Preferir patch selectivo sobre replace total si no cambia topología estructural.
2. Para arrays, usar `replace`, no `merge` conceptual.
3. Para borrados, usar `remove` y traducir a `null` al materializar el patch.
