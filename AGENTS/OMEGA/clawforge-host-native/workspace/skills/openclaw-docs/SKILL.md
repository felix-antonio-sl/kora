---
name: openclaw-docs
description: Navigate and resolve queries against OpenClaw official documentation. Use when the user asks about OpenClaw features, config options, runtime behavior, channels, tools, plugins, or any platform capability.
---

## Proposito

Resolver consultas sobre OpenClaw usando exclusivamente la documentacion oficial como fuente primaria.

## Cuando se activa

- El usuario pregunta sobre una feature, opcion de config, o comportamiento de OpenClaw.
- Se necesita verificar un hecho de plataforma antes de configurar o desplegar.
- Hay ambiguedad sobre como funciona un canal, tool, plugin o skill.

## Procedimiento

1. **Identificar el tema.** Clasificar la consulta: config, gateway, canales, tools, skills, plugins, seguridad, sandboxing, sessions, modelos.
2. **Buscar en docs.** Localizar la seccion relevante en la documentacion oficial de OpenClaw. Usar `{baseDir}` si hay docs locales disponibles.
3. **Extraer la respuesta.** Citar la fuente con la ruta o seccion exacta del documento.
4. **Responder con evidencia.** Entregar la respuesta acompanada de la cita. Si la documentacion no cubre el caso, declararlo explicitamente.

## Reglas

- **No inferir.** Si la documentacion no dice algo, no asumirlo.
- **Citar siempre.** Toda afirmacion de plataforma debe tener referencia a la seccion de docs.
- **Distinguir versiones.** Si el comportamiento cambio entre versiones, indicarlo.
- **Sin opiniones.** Hechos verificables, no interpretaciones.

## Formato de salida

```
**Tema:** <tema identificado>
**Fuente:** <ruta o seccion de docs>
**Respuesta:** <respuesta con evidencia>
**Notas:** <advertencias, limitaciones o versiones relevantes>
```
