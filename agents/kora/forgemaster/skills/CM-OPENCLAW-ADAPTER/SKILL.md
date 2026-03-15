---
_manifest:
  urn: urn:kora:skill:forgemaster-openclaw-adapter:1.0.0
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
        - references/openclaw-platform-model.md
      assets:
        - assets/openclaw-workspace-template.md
---

# CM-OPENCLAW-ADAPTER

## Proposito
Mapea un workspace KORA normalizado al formato nativo de OpenClaw, generando workspace adaptado + config snippet + skills adaptados.

## Input/Output
- **Input:** source: WorkspaceAnalysis (output de CM-WORKSPACE-ANALYZER)
- **Output:** TransmutedArtifact[] (artefactos listos para CM-ARTIFACT-EMITTER)

## Procedimiento
1. Consultar `references/openclaw-platform-model.md` para reglas de mapeo vigentes.
2. MAPEAR AGENTS.md:
   - Eliminar frontmatter YAML KORA.
   - Preservar FSM completa como instrucciones operativas.
   - Preservar reglas duras y co-induccion como instrucciones.
   - Adaptar formato: OpenClaw espera Markdown plano sin `_manifest`.
   - Limite: max 20,000 chars por archivo (constraint OpenClaw).
3. MAPEAR SOUL.md:
   - Eliminar frontmatter YAML KORA.
   - Preservar identidad, paradigma, tono.
   - Extraer identidad visual → generar IDENTITY.md separado:
     ```markdown
     name: {nombre del agente}
     emoji: {emoji representativo derivado de identidad}
     theme: {tema derivado de dominio}
     ```
4. MAPEAR USER.md:
   - Eliminar frontmatter YAML KORA.
   - Preservar perfil, rutinas, preferencias.
5. MAPEAR TOOLS.md:
   - Eliminar frontmatter YAML KORA.
   - Convertir a notas sobre herramientas (OpenClaw no usa TOOLS.md para control, solo como notas).
   - Control real de tools → config-snippet.json5.
6. MAPEAR config.json → config-snippet.json5:
   ```json5
   {
     id: "{namespace}-{nombre}",
     name: "{nombre legible}",
     workspace: "~/.openclaw/workspace-{namespace}-{nombre}",
     model: "anthropic/claude-sonnet-4-5",  // default, ajustable
     identity: { name: "{nombre}", emoji: "{emoji}" },
     sandbox: { mode: "{sandbox.mode}" },
     tools: {
       allow: [{tools.allow mapeados a tools OpenClaw}],
       deny: [{tools.deny}]
     },
     subagents: {
       maxSpawnDepth: {sub_agents.max_depth},
       maxChildrenPerAgent: {sub_agents.max_concurrent}
     }
   }
   ```
7. MAPEAR Skills:
   - Para cada CM-* KORA:
     - Eliminar frontmatter KORA.
     - Generar SKILL.md con frontmatter OpenClaw:
       ```yaml
       ---
       name: {id-kebab-case}
       description: {proposito del skill}
       user-invocable: false
       ---
       ```
     - Preservar CM Core (Proposito, Input/Output, Procedimiento, Signature Output).
   - Para skills extendidos: copiar fibras adjuntas (scripts/, references/, assets/).
8. Usar `assets/openclaw-workspace-template.md` como referencia de estructura output.
9. Retornar lista de TransmutedArtifact[] con ruta relativa y contenido de cada artefacto.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artifacts | TransmutedArtifact[] | Lista de artefactos: {path, content, type} |
| mappings | MappingEntry[] | Tabla componente_kora → artefacto_openclaw |
| warnings | string[] | Limitaciones de mapeo documentadas |
