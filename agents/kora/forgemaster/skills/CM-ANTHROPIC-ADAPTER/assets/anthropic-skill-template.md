---
title: Anthropic Skill Template
status: internal
lang: es
---

# Anthropic Skill Template

Esqueleto para la generacion de un Anthropic Skill compilado desde un workspace KORA.

## Template

````markdown
---
name: {namespace}-{nombre}
description: {descripcion con QUE hace y CUANDO usarla. Max 1024 chars. Sin <>.}
---

# {namespace}/{nombre} — {titulo descriptivo}

Al activar esta skill, adoptas la identidad y comportamiento de {namespace}/{nombre}. Sigue estrictamente la FSM, reglas y co-induccion definidas abajo. Los skills (CM-*.md) se encuentran en `AGENTS/{namespace}/{nombre}/skills/` y se cargan on-demand.

## Specs de referencia (consultar cuando sea necesario)

{lista de specs relevantes del agente}

## Workspace de agentes

{contexto sobre estructura de workspace si aplica}

---

<kora_bootstrap component="agents">

{CONTENIDO DE AGENTS.md SIN FRONTMATTER}

</kora_bootstrap>

<kora_bootstrap component="soul">

{CONTENIDO DE SOUL.md SIN FRONTMATTER}

</kora_bootstrap>

<kora_bootstrap component="tools">

{CONTENIDO DE TOOLS.md SIN FRONTMATTER}

</kora_bootstrap>

## Skills (Lazy Load)

Los skills se cargan on-demand. Para cargar un skill, lee el archivo correspondiente en `AGENTS/{namespace}/{nombre}/skills/`:

| CM | Archivo | Estado FSM |
|----|---------|-----------|
{tabla de skills con CM, archivo, estado FSM}

Cuando entres en un estado FSM, lee el skill correspondiente para obtener el procedimiento detallado.

## Inicio

Al activar esta skill, saluda al usuario con el saludo definido arriba y entra en S-DISPATCHER.
````
