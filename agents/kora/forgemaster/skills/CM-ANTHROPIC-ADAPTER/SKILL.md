---
_manifest:
  urn: urn:kora:skill:forgemaster-anthropic-adapter:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - workspace_read
        - artifact_write
      requires: []
      references:
        - references/anthropic-skills-format.md
      assets:
        - assets/anthropic-skill-template.md
---

# CM-ANTHROPIC-ADAPTER

## Proposito
Mapea un workspace KORA normalizado al formato Anthropic Skill (Claude Code), compilando el agente completo en un SKILL.md unico con tags `<kora_bootstrap>` estructurados y referencia lazy-load a skills del workspace fuente.

## Input/Output
- **Input:** source: WorkspaceAnalysis (output de CM-WORKSPACE-ANALYZER)
- **Output:** TransmutedArtifact[] (artefactos listos para CM-ARTIFACT-EMITTER)

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
   - Instruccion de lazy-load: "Los skills (CM-*.md) se encuentran en `AGENTS/{namespace}/{nombre}/skills/` y se cargan on-demand."
4. COMPILAR AGENTS.md → `<kora_bootstrap component="agents">`:
   - Incluir FSM completa con estados, transiciones, prioridades.
   - Incluir reglas duras.
   - Incluir co-induccion (checklist + protocolo correccion).
   - Incluir contexto multi-turno.
   - Incluir wiring.
   - Eliminar frontmatter KORA.
5. COMPILAR SOUL.md → `<kora_bootstrap component="soul">`:
   - Incluir identidad dialectica, paradigma cognitivo, tono, saludo, estilo, ejemplos.
   - Eliminar frontmatter KORA.
6. COMPILAR TOOLS.md → `<kora_bootstrap component="tools">`:
   - Incluir herramientas con firmas, cuando usar, routing map.
   - Eliminar frontmatter KORA.
7. COMPILAR SECCION SKILLS:
   - Tabla de skills con CM, archivo, estado FSM asociado.
   - Instruccion: "Cuando entres en un estado FSM, lee el skill correspondiente para obtener el procedimiento detallado."
   - NO inlinear contenido de skills (lazy-load preservado).
8. COMPILAR SECCION INICIO:
   - Saludo del agente (de SOUL.md).
   - Estado inicial: S-DISPATCHER.
9. Usar `assets/anthropic-skill-template.md` como esqueleto de referencia.
10. Retornar TransmutedArtifact[] con el SKILL.md compilado.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artifacts | TransmutedArtifact[] | SKILL.md compilado + fibras opcionales |
| mappings | MappingEntry[] | Tabla componente_kora → seccion_skill |
| warnings | string[] | Limitaciones de mapeo documentadas |
| estimated_tokens | number | Estimacion de tokens del skill compilado |
