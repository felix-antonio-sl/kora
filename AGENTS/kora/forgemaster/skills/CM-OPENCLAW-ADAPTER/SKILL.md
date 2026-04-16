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
        - spec_consult
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

Mapea un workspace KORA normalizado al formato nativo de OpenClaw, generando workspace adaptado + proyeccion nativa de config + plan de installs gestionados + hints de deployment. Produce artefactos y metadata listos para `CM-ARTIFACT-EMITTER`; el adapter no escribe a disco ni genera `_transmutation.yml`. Los artefactos finales se emiten a staging (R-TRANSMUTE-6) y el deploy a produccion sigue siendo responsabilidad exclusiva de `kora/clawforge`.

## Input/Output

- **Input:** workspace KORA completo via `workspace_read(agent_path)`
- **Output:** AdapterTransmutationReport (artefactos OpenClaw + hints para manifest)

## Procedimiento

### Fase 1: Preparacion

1. Consultar `references/openclaw-platform-model.md` y contrastar con `runtime-spec-md` + `openclaw-runtime-extension` para reglas vigentes de mapeo y contrato native-first.

2. Leer workspace fuente completo: `workspace_read(agent_path)` → obtener AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json, skills/.

### Fase 2: Validar token budget

3. **Medir chars de cada componente fuente** (sin frontmatter):
   - Por cada archivo .md: contar chars del contenido operacional (post-strip).
   - WARNING si cualquier archivo > 17K chars (margen de seguridad, limite OpenClaw: 20K).
   - FAIL si cualquier archivo > 20K chars (truncamiento silencioso garantizado).
   - WARNING si total bootstrap > 100K chars (limite OpenClaw: 150K).
   - Si excede: recomendar compresion — remover notacion formal, compactar tablas, mover detalles a skills lazy-load.

### Fase 3: Detectar requisitos de runtime y deployment

4. **Detectar requisitos estructurados de sidecar / servicio externo**:
   - Analizar evidencia estructurada del workspace: tools declaradas, config, skills y referencias explicitamente operativas.
   - Si la dependencia externa es explicitamente resoluble → emitir `requires_sidecar: true` con razon.
   - Si la evidencia aparece solo como texto libre ambiguo en `TOOLS.md` o `AGENTS.md` → **NO** fijar el hecho como contrato duro; emitir `manual_inputs_required`.
   - Si solo usa capacidades nativas OpenClaw → `requires_sidecar: false`.

5. **Resolver KB mounts** (principios-transmutacion P8):
   - Leer config.json.allowed_kb.
   - Para cada URN: resolver path via `catalog_resolve`.
   - Producir lista de mounts RO: `{urn, source_path, mount_path: "/home/node/knowledge/{ns}/{file}", mode: "ro"}`.
   - Nota: KBs NO van en bootstrap — van como archivos montados que el agente lee on-demand.

6. **Inicializar `managed_installs` vacio por default**:
   - `skills`: solo entradas registry-native si el source lo declara explicitamente.
   - `plugins`: idem.
   - `bundles`: idem.
   - Lo no deducible estructuradamente **NO DEBE** inferirse desde texto libre; se declara como `manual_inputs_required`.

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
   - Nunca delegar a `TOOLS.md` el dato autoritativo de mounts, plugins, ACLs, federation o deploy.

10. **MAPEAR config.json → `config_projection` nativa OpenClaw:**
    ```json5
    {
      id: "{namespace}-{nombre}",
      name: "{nombre legible}",
      workspace: "/home/node/.openclaw/workspace",
      model: { primary: "{model_routing.tier_default}" },
      thinkingDefault: "{si existe}",
      reasoningDefault: "{si existe}",
      fastModeDefault: "{si existe}",
      identity: { name: "{nombre}", emoji: "{emoji}", theme: "{tema}" },
      sandbox: { mode: "{mapping de sandbox.mode}" },
      tools: {
        profile: "{perfil nativo si aplica}",
        allow: [{tools.allow mapeados a tools OpenClaw}],
        deny: [{tools.deny}]
      },
      subagents: {
        maxSpawnDepth: {sub_agents.max_depth},
        maxChildrenPerAgent: {sub_agents.max_concurrent}
      }
    }
    ```
    - Preferir `tools.profile` + delta `allow/deny` cuando el set mapeado coincida con una superficie nativa de OpenClaw.
    - Proyectar solo config nativa; no copiar `config.json`.

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
    - `platform_contract`:
      ```yaml
      platform_contract:
        workspace_target:
          root: "workspace/"
        config_projection:
          path: "config-snippet.json5"
          native_surfaces:
            - "agents.list[]"
            - "agents.defaults"
            - "tools.*"
            - "sandbox.*"
            - "channels.*"
        managed_installs:
          skills: []
          plugins: []
          bundles: []
        deployment_hints:
          requires_sidecar: {boolean}
          sidecar_reason: "{razon si true}"
          kb_mounts:
            - urn: "{urn}"
              source: "{path relativo en repo KORA}"
              mount: "/home/node/knowledge/{ns}/{file}"
              mode: "ro"
          bind_mounts: []
          topology:
            recommended: "single-gateway-multi-agent" | "isolated-gateway"
            reason: "{si aplica}"
          manual_inputs_required: []
          estimated_bootstrap_chars: {total}
          bootstrap_within_limit: {boolean}
          architecture: "caso-a" | "caso-b"
        runtime_exclusions:
          - "auth-profiles.json"
          - "sessions/"
          - "pairing-store"
          - "credentials/"
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

16. Retornar `artifacts[]`, `platform_contract` y `manifest_overrides` a `CM-ARTIFACT-EMITTER`, que sera el unico responsable de escribir a disco y generar `_transmutation.yml`.

17. **Handoff a kora/clawforge**: Una vez que `CM-ARTIFACT-EMITTER` haya emitido los artefactos, comunicar al operador: "Transmutacion completa. Artefactos en {output_dir}. Para desplegar en produccion, encarnar kora/clawforge y ejecutar S-HANDOFF/S-DEPLOY con transmutation_path={output_dir}/_transmutation.yml; consumir `platform_contract` como fuente autoritativa de config/deploy." No ejecutar Docker commands, no escribir a /srv/kora/, no inicializar volumes, no correr openclaw doctor. Esas operaciones son de clawforge.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artifacts | TransmutedArtifact[] | Lista de artefactos: {path, content, type} |
| mappings | MappingEntry[] | Tabla componente_kora → artefacto_openclaw |
| platform_contract | object | Contrato estructurado OpenClaw: config_projection, managed_installs, deployment_hints, runtime_exclusions |
| manifest_overrides | object | Metadata target-specific para que `CM-ARTIFACT-EMITTER` emita `_transmutation.yml` |
| warnings | string[] | Limitaciones de mapeo + referencias a templates de deploy |
