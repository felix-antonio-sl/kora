---
name: openclaw-docs
description: Navigate and resolve queries against OpenClaw official documentation. Use when the user asks about OpenClaw features, config options, runtime behavior, channels, tools, plugins, or any platform capability. Also use BEFORE any operation that touches gateway config, channels, tools, sessions, skills, plugins, or sandbox to verify the approach is canonical. Triggers on words like canonical, native, official, nativo, canonico, or any reference to how something works or should be done in OpenClaw.
---

## Proposito

Resolver consultas sobre OpenClaw usando exclusivamente la documentacion oficial como fuente primaria.

## Cuando se activa

- El usuario pregunta sobre una feature, opcion de config, o comportamiento de OpenClaw.
- Se necesita verificar un hecho de plataforma antes de configurar o desplegar.
- Hay ambiguedad sobre como funciona un canal, tool, plugin o skill.
- El usuario pide algo "canonico", "nativo", "oficial", "de OpenClaw", o pregunta "como se hace en OpenClaw".
- El agente va a ejecutar cualquier operacion sobre el gateway, config, canales, tools, sessions, skills, plugins o sandbox — antes de actuar, verificar contra docs que el approach es correcto.
- Se menciona o se va a escribir un campo de config en `openclaw.json` — verificar que existe en el schema actual.

## Procedimiento

- 1. Identificar el tema. Clasificar la consulta: config, gateway, canales, tools, skills, plugins, seguridad, sandboxing, sessions, modelos.
- 2. Buscar en fuentes canónicas primarias. Revisar primero, de forma prioritaria, estas fuentes locales de mayor jerarquía:
  - /home/felix/kora/KNOWLEDGE/OMEGA/manual-integral-skills-openclaw.md
  - /home/felix/kora/KNOWLEDGE/OMEGA/openclaw-manual-integral.md
- 3. Evaluar suficiencia y contundencia. Determinar si esas fuentes contienen información suficiente, explícita y concluyente para responder. Si la cobertura es incompleta, ambigua, indirecta o no suficientemente contundente, no detenerse ahí.
- 4. Escalar a la documentación oficial base. Solo si las fuentes canónicas primarias no bastan, complementar o contrastar con:
  - /home/felix/kora/KNOWLEDGE/agengai/openclaw/documentacion-oficial
- 5. Extraer la respuesta. Recuperar la respuesta desde la fuente más autoritativa y pertinente disponible, indicando con precisión la ruta, sección o ubicación exacta del documento.
- 6. Responder con evidencia y jerarquía de fuentes. Entregar la respuesta acompañada de su sustento documental, dejando explícito:
  - si la respuesta quedó resuelta completamente en las fuentes OMEGA;
  - si fue necesario descender a la documentación oficial base;
  - y si, aun así, la documentación no cubre el caso de manera suficiente.
- 7. Resolver conflictos entre fuentes. Si hubiera tensiones, diferencias o aparentes contradicciones, priorizar la interpretación más canónica según la jerarquía definida: primero OMEGA, luego documentación oficial base, dejando constancia explícita de ello.

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
