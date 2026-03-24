---
_manifest:
  urn: urn:kora:skill:forgemaster-openclaw-adapter:1.2.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - workspace_read
        - catalog_resolve
      requires: []
      references:
        - references/openclaw-platform-model.md
      assets:
        - assets/openclaw-workspace-template.md
        - assets/openclaw-json5-template.json5
        - assets/docker-compose-template.yml
        - assets/env-template
        - assets/init-volume.sh
---

# CM-OPENCLAW-ADAPTER

## Proposito

Mapea un workspace KORA normalizado al formato nativo de OpenClaw, generando workspace adaptado + config completo + skills adaptados + deployment hints. Produce artefactos y metadata listos para `CM-ARTIFACT-EMITTER`; el adapter no escribe a disco ni genera `_transmutation.yml`. Los artefactos finales se emiten a staging (R-TRANSMUTE-6) y el deploy a produccion sigue siendo responsabilidad exclusiva de ops/clawstack.

## Input/Output

- **Input:** workspace KORA completo via `workspace_read(agent_path)`
- **Output:** AdapterTransmutationReport (artefactos OpenClaw + hints para manifest)

## Procedimiento

### Fase 1: Preparacion

1. Consultar `references/openclaw-platform-model.md` para reglas de mapeo vigentes de la plataforma OpenClaw.

2. Leer workspace fuente completo: `workspace_read(agent_path)` → obtener AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json, skills/.

### Fase 2: Validar token budget

3. **Medir chars de cada componente fuente** (sin frontmatter):
   - Por cada archivo .md: contar chars del contenido operacional (post-strip).
   - WARNING si cualquier archivo > 17K chars (margen de seguridad, limite OpenClaw: 20K).
   - FAIL si cualquier archivo > 20K chars (truncamiento silencioso garantizado).
   - WARNING si total bootstrap > 100K chars (limite OpenClaw: 150K).
   - Si excede: recomendar compresion — remover notacion formal, compactar tablas, mover detalles a skills lazy-load.

### Fase 3: Detectar requisitos de deployment

4. **Detectar necesidad de sidecar** (principios-transmutacion P10):
   - Analizar TOOLS.md: buscar bindings a servicios HTTP externos, APIs con estado, bases de datos.
   - Si detecta endpoints HTTP, URLs de servicio, o referencias a DB → emitir `requires_sidecar: true` con razon.
   - Si solo usa tools nativos de OpenClaw (filesystem, code_execution, web_search, browser) → `requires_sidecar: false`.

5. **Resolver KB mounts** (principios-transmutacion P8):
   - Leer config.json.allowed_kb.
   - Para cada URN: resolver path via `catalog_resolve`.
   - Producir lista de mounts RO: `{urn, source_path, mount_path: "/home/node/knowledge/{ns}/{file}", mode: "ro"}`.
   - Nota: KBs NO van en bootstrap — van como archivos montados que el agente lee on-demand.

### Fase 4: Mapear componentes

6. **MAPEAR AGENTS.md:**
   - Eliminar frontmatter YAML KORA.
   - Preservar FSM completa como instrucciones operativas.
   - Preservar reglas duras y co-induccion como instrucciones.
   - Formato: Markdown plano sin `_manifest`.
   - Verificar: resultado < 17K chars (WARNING) / < 20K chars (FAIL).

7. **MAPEAR SOUL.md:**
   - Eliminar frontmatter YAML KORA.
   - Preservar identidad, paradigma, tono (secciones canonicas unicamente).
   - Extraer identidad visual → generar IDENTITY.md separado:
     ```markdown
     name: {nombre del agente}
     emoji: {emoji representativo derivado de identidad}
     theme: {tema derivado de dominio}
     ```

8. **MAPEAR USER.md:**
   - Eliminar frontmatter YAML KORA.
   - Preservar perfil, rutinas, preferencias.

9. **MAPEAR TOOLS.md:**
   - Eliminar frontmatter YAML KORA.
   - Convertir a notas sobre herramientas (OpenClaw no usa TOOLS.md para control, solo como notas).
   - Control real de tools → config.

10. **MAPEAR config.json → config-snippet.json5:**
    ```json5
    {
      id: "{namespace}-{nombre}",
      name: "{nombre legible}",
      workspace: "/home/node/.openclaw/workspace",
      model: { primary: "{model_routing.tier_default}" },
      identity: { name: "{nombre}", emoji: "{emoji}", theme: "{tema}" },
      sandbox: { mode: "{mapping de sandbox.mode}" },
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

11. **MAPEAR Skills:**
    - Para cada CM-* degenerado (skills/CM-*.md):
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
    - Para cada CM-* extendido (skills/CM-*/SKILL.md):
      - Misma adaptacion de SKILL.md.
      - Copiar fibras adjuntas (scripts/, references/, assets/) al directorio del skill OpenClaw.

### Fase 5: Preparar metadata para `CM-ARTIFACT-EMITTER`

12. **Preparar `manifest_overrides`** con campos extendidos:
    - `platform: openclaw`
    - Exclusiones: config.json (informa config plataforma, no se copia).
    - Token budget: chars medidos por archivo + total + within_limit.
    - Deployment hints:
      ```yaml
      deployment_hints:
        requires_sidecar: {boolean}
        sidecar_reason: "{razon si true}"
        kb_mounts:
          - urn: "{urn}"
            source: "{path relativo en repo KORA}"
            mount: "/home/node/knowledge/{ns}/{file}"
            mode: "ro"
        estimated_bootstrap_chars: {total}
        bootstrap_within_limit: {boolean}
        architecture: "caso-a" | "caso-b"
      ```
    - `CM-ARTIFACT-EMITTER` usa esta metadata para generar el `_transmutation.yml` final.

### Fase 6: Retornar artefactos compilados

13. Usar `assets/openclaw-workspace-template.md` como referencia de estructura output.

14. Referenciar templates de deploy en warnings del output:
    - `assets/openclaw-json5-template.json5` → template de config completo.
    - `assets/docker-compose-template.yml` → compose Caso A y Caso B.
    - `assets/env-template` → variables de entorno.
    - `assets/init-volume.sh` → script de inicializacion de volume.
    - Nota: estos templates son para el operador humano, no se incluyen en los artefactos transmutados.

15. Verificar que artefactos generados cumplen runtime-spec §9 pipeline canonico.

16. Retornar `artifacts[]`, `deployment_hints` y `manifest_overrides` a `CM-ARTIFACT-EMITTER`, que sera el unico responsable de escribir a disco y generar `_transmutation.yml`.

17. **Handoff a ops/clawstack**: Una vez que `CM-ARTIFACT-EMITTER` haya emitido los artefactos, comunicar al operador: "Transmutacion completa. Artefactos en {output_dir}. Para desplegar en produccion, encarnar ops/clawstack y ejecutar S-DEPLOY con transmutation_path={output_dir}/_transmutation.yml." No ejecutar Docker commands, no escribir a /srv/kora/, no inicializar volumes, no correr openclaw doctor. Esas operaciones son de clawstack.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artifacts | TransmutedArtifact[] | Lista de artefactos: {path, content, type} |
| mappings | MappingEntry[] | Tabla componente_kora → artefacto_openclaw |
| deployment_hints | DeploymentHints | Sidecar detection, KB mounts, token budget, architecture |
| manifest_overrides | object | Metadata target-specific para que `CM-ARTIFACT-EMITTER` emita `_transmutation.yml` |
| warnings | string[] | Limitaciones de mapeo + referencias a templates de deploy |
