---
_manifest:
  urn: urn:kora:skill:forgemaster-anthropic-adapter:1.0.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - workspace_read
      requires: []
      references:
        - references/anthropic-skills-format.md
      assets:
        - assets/anthropic-skill-template.md
---

# CM-ANTHROPIC-ADAPTER

## Proposito
Mapea un workspace KORA normalizado al formato Anthropic Skill, compilando el agente completo en un SKILL.md unico con tags `<kora_bootstrap>` estructurados y referencias lazy-load a los skills derivados que luego emitira `CM-ARTIFACT-EMITTER`.

## Input/Output
- **Input:** workspace KORA completo via `workspace_read(agent_path)`
- **Output:** AdapterTransmutationReport (artefactos compilados + metadata de manifest para `CM-ARTIFACT-EMITTER`)

## Procedimiento
1. Consultar `references/anthropic-skills-format.md` para reglas de formato vigentes.
2. GENERAR FRONTMATTER Anthropic:
   ```yaml
   ---
   name: {namespace}-{nombre}
   description: {descripcion derivada de SOUL.md identidad + proposito. Incluir triggers de activacion.}
   ---
   ```
   - description DEBE incluir QUE hace + CUANDO usarla.
   - Max 1024 chars en description.
   - Sin caracteres `<>` en frontmatter (restriccion Anthropic).
   - Sin "claude" ni "anthropic" en name (palabras reservadas).
3. COMPILAR INSTRUCCIONES INICIALES:
   - Parrafo introductorio: "Al activar esta skill, adoptas la identidad y comportamiento de {namespace}/{nombre}."
   - Referencia a specs si aplica.
   - Instruccion de lazy-load: "Los skills derivados se cargan on-demand desde el paquete Anthropic emitido para `{namespace}/{nombre}`."
4. COMPILAR AGENTS.md → `<kora_bootstrap component="agents">`:
   - Incluir FSM completa con estados, transiciones, prioridades.
   - Incluir reglas duras.
   - Incluir co-induccion (checklist + protocolo correccion).
   - Incluir contexto multi-turno.
   - Incluir wiring.
   - Eliminar frontmatter KORA.
5. COMPILAR SOUL.md → `<kora_bootstrap component="soul">`:
   - Incluir identidad dialectica, paradigma cognitivo y tono.
   - Eliminar frontmatter KORA.
6. COMPILAR TOOLS.md → `<kora_bootstrap component="tools">`:
   - Incluir herramientas con firmas, cuando usar, routing map.
   - Eliminar frontmatter KORA.
7. COMPILAR `AGENTS.md` §6 si existe:
   - Extraer `Comportamiento Operativo` (saludo, estilo, ejemplos) desde `AGENTS.md`, no desde `SOUL.md`.
   - Incluirlo como bloque operativo separado dentro del skill compilado.
8. COMPILAR SECCION SKILLS:
   - Tabla de skills con CM, archivo, estado FSM asociado.
   - Instruccion: "Cuando entres en un estado FSM, lee el skill correspondiente para obtener el procedimiento detallado."
   - NO inlinear contenido de skills (lazy-load preservado).
9. COMPILAR SECCION INICIO:
   - Saludo del agente (de `AGENTS.md` §6 si existe; fallback: identidad + S-DISPATCHER).
   - Estado inicial: S-DISPATCHER.
10. Usar `assets/anthropic-skill-template.md` como esqueleto de referencia.
11. Preparar `manifest_overrides` para `CM-ARTIFACT-EMITTER` con `platform: anthropic`, warnings y exclusiones si aplica. El adapter NO genera `_transmutation.yml`.
12. Verificar que artefactos generados cumplen runtime-spec §9 pipeline canonico (skill-spec §6 inv.7).
13. Retornar AdapterTransmutationReport con el SKILL.md compilado y `manifest_overrides`.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artifacts | TransmutedArtifact[] | SKILL.md compilado + fibras opcionales |
| mappings | MappingEntry[] | Tabla componente_kora → seccion_skill |
| manifest_overrides | object | Metadata target-specific para que `CM-ARTIFACT-EMITTER` genere `_transmutation.yml` |
| warnings | string[] | Limitaciones de mapeo documentadas |
| estimated_tokens | number | Estimacion de tokens del skill compilado |
