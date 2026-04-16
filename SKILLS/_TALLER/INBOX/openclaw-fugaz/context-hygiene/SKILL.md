---
name: context-hygiene
description: Gestiona el contexto de la sesion para mantenerlo limpio y productivo. Usar cuando la conversacion se extiende, el contexto se satura, o se detecta informacion irrelevante acumulada.
---

# Context Hygiene

El contexto del modelo es recurso caro. Cada token que entra compite por atencion.

## Senales de contexto degradado

- Respuestas que repiten informacion ya establecida
- Perdida de coherencia con decisiones anteriores
- Instrucciones que se ignoran o contradicen
- Latencia creciente sin aumento de complejidad

## Procedimiento

1. **Diagnosticar** — `/context detail` para ver tamano actual
2. **Podar** — Si hay tool results grandes ya procesados, su valor disminuye. Considerar `/compact` con instrucciones focalizadas.
3. **Resumir** — Antes de compactar, escribir decisiones clave a `memory/` para preservarlas.
4. **Prevenir** — En lecturas futuras, usar offsets y limites. No leer archivos completos.

## Reglas

- No cargar en contexto lo que puede consultarse bajo demanda
- Preferir lecturas parciales sobre lecturas completas
- Si un archivo supera 200 lineas, leer solo la seccion relevante
- Resultados de exec largos: capturar solo lo necesario
- Screenshots > descripciones textuales largas para contexto visual
