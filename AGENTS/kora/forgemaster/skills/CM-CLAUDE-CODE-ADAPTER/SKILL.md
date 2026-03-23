---
_manifest:
  urn: "urn:kora:skill:forgemaster-claude-code-adapter:1.0.0"
  type: "lazy_load_endofunctor"
  version: "1.0.0"
  status: "published"
  language: "es"
  form: "extended"
  allowed_tools:
    - workspace_read
    - artifact_write
---

## Proposito

Mapear un workspace KORA normalizado al formato nativo Claude Code (subagent + skills), compilando los 5 componentes + skills en artefactos con enforcement server-side via frontmatter. Reemplaza al approach monolitico de CM-ANTHROPIC-ADAPTER para el target CC nativo, preservando equivalencia funcional (runtime-spec §6.1) con enforcement mecanico de config.json (runtime-spec §3.2).

## Input/Output

- **Input:** workspace KORA completo (5 componentes + skills/) + namespace + nombre del agente
- **Output:** TransmutedArtifact[] = subagent (.claude/agents/{ns}--{name}.md) + skills (.claude/skills/{ns}--{name}--{cm}/SKILL.md) + manifest (_transmutation/{ns}--{name}.yml)

## Procedimiento

### Fase 1: Preparacion

1. **Consultar referencias de formato**: Leer `references/cc-subagent-format.md` y `references/cc-skill-format.md` para reglas vigentes de la plataforma CC.

2. **Leer workspace fuente**: `workspace_read(agent_path)` → obtener AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json, skills/.

3. **Consultar mapping**: Leer `references/mapping-table.md` para tabla de correspondencia KORA → CC con justificaciones spec.

### Fase 2: Compilar frontmatter (config.json → server-side)

4. **Generar frontmatter del subagent** desde config.json:

   - `name`: `{namespace}--{nombre}` (doble guion como separador de namespace; M5).
   - `description`: Derivar de SOUL.md §Identidad Dialectica + triggers de activacion de la FSM. Maximo 200 chars. Sin caracteres `<>`.
   - `model`: `config.json.model_routing.tier_default` → `opus` | `sonnet` | `haiku`. Si ausente, omitir (hereda del padre).
   - `effort`: Derivar de `config.json.limits`. Si ausente, omitir.
   - `maxTurns`: Derivar de `config.json.limits`. Default CC: 50.
   - `permissionMode`: Mapping de `config.json.sandbox.mode`:

     | KORA sandbox.mode | CC permissionMode |
     |-------------------|-------------------|
     | strict            | plan              |
     | isolated          | acceptEdits       |
     | permissive        | default           |
     | off               | bypassPermissions |

   - `tools`: Mapear `config.json.tools.allow` a sintaxis CC. Herramientas semanticas KORA se mapean a tools CC disponibles (Read, Grep, Glob, Bash, Write, Edit, Agent, WebFetch, WebSearch, etc.). Tools sin equivalente CC directo → documentar como limitacion en warnings.
   - `disallowedTools`: `config.json.tools.deny` mapeado a nombres CC.
   - `skills`: Lista de `{ns}--{name}--{cm}` para cada CM-* declarado en skills/.
   - `hooks.Stop`: Hook de co-induccion tipo prompt:

     ```yaml
     hooks:
       Stop:
         - hooks:
             - type: prompt
               prompt: "Co-induccion {name}: (1) SCOPE_COMPLIANCE—output dentro del dominio declarado (2) STATE_AWARENESS—coherente con estado FSM activo (3) INTERFACE_DISCIPLINE—solo tools declarados usados. Si alguno falla, indica cual y sugiere correccion. $ARGUMENTS"
               model: {co_induction_model}
     ```

     Modelo del hook: `haiku` si FSM tiene <= 8 estados; `sonnet` si FSM tiene > 8 estados (M3).

5. **Absorber runtime_capabilities** (M6): Mapear `config.json.runtime_capabilities.allow` y `.deny` a `permissionMode` + `disallowedTools` segun corresponda. Capabilities sin mapping directo (e.g., deploy, filesystem_write) → documentar en `enforcement_gaps` del manifest.

### Fase 3: Compilar body del subagent

6. **Compilar SOUL.md** (seccion superior del body):
   - Strip frontmatter YAML (R-TRANSMUTE-2).
   - Incluir SOLO secciones canonicas: Identidad Dialectica, Paradigma Cognitivo, Tono.
   - Secciones de behavior (Saludo, Estilo, Ejemplos) NO van aqui — van en la seccion AGENTS.md.
   - Cerrar con separador `---`.

7. **Compilar AGENTS.md** (seccion principal del body):
   - Strip frontmatter YAML.
   - Incluir en orden: FSM, Reglas Duras, Co-induccion, Contexto Multi-turno, Wiring, Comportamiento Operativo.
   - Preservar numeracion de estados, prioridades de transicion y texto de reglas duras intacto.
   - Cerrar con separador `---`.

8. **Compilar TOOLS.md** (seccion inferior del body):
   - Strip frontmatter YAML.
   - Incluir routing maps (kb_route) y semantica de herramientas.
   - Cerrar con separador `---`.

9. **Agregar tabla de skills lazy-load**:

   ```markdown
   ## Skills (Lazy Load)

   Cuando entres en un estado FSM, invoca el skill correspondiente:

   | Estado | Skill | CM |
   |--------|-------|----|
   | {estado} | {ns}--{name}--{cm} | CM-{CM} |

   Para cargar un skill: invocalo como `/{ns}--{name}--{cm}` o consulta `AGENTS/{ns}/{name}/skills/CM-{CM}` directamente.
   ```

10. **Excluir USER.md** (H1): No incluir en el body. El contexto operador en CC es provisto nativamente por la conversacion. Documentar en manifest campo `exclusions` con justificacion citando runtime-spec §6.1.

11. **Excluir config.json del body** (runtime-spec §9.2): Su informacion ya esta en el frontmatter server-side. No copiar como texto.

### Fase 4: Verificar segregacion

12. **Check de segregacion logica** (H2): Verificar que:
    - Seccion SOUL no contiene FSM, reglas, wiring, ni policy.
    - Seccion AGENTS no contiene tono, paradigma, ni identidad (fuera de §6 Comportamiento Operativo).
    - Seccion TOOLS no contiene policy operativa ni behavior condicional.
    - Headers H1 (`#`) separan claramente cada seccion.
    - Separadores `---` delimitan transiciones entre componentes.
    Si falla → corregir antes de emitir.

### Fase 5: Compilar skills

13. **Para cada CM-* en skills/**:
    - Crear `.claude/skills/{ns}--{name}--{cm}/SKILL.md`.
    - Frontmatter CC:
      - `name`: `{ns}--{name}--{cm}`
      - `description`: Derivado de la seccion Proposito del CM. Maximo 200 chars.
    - Body: CM Core stripped (sin frontmatter KORA). Preservar las 4 secciones canonicas: Proposito, Input/Output, Procedimiento, Signature Output.
    - Copiar `scripts/`, `references/`, `assets/` como subdirectorios del skill CC si existen.
    - Verificar que CM Core preserva las 4 secciones (skill-spec §3).

### Fase 6: Generar manifest y verificar

14. **Verificar token budget** (runtime-spec §9.4): Body del subagent < 20K chars. Si excede → mover secciones extensas (routing maps, ejemplos) a skills adicionales lazy-load.

15. **Documentar enforcement_gaps** (H3): En manifest:
    - `allowed_kb`: original=server-side, efectivo=instruccional. Mitigacion: MCP kb-reader o hook pre-tool.
    - `runtime_capabilities` sin mapping: documentar absorcion parcial (M6).

16. **Generar _transmutation.yml**: Usar template de `assets/transmutation-manifest-template.yml`. Incluir:
    - SHA-256 de cada componente fuente.
    - Exclusiones (USER.md, config.json) con justificaciones.
    - Enforcement gaps con niveles original vs efectivo.
    - Segregation mode: logical, check: headers.
    - Timestamp ISO 8601.
    - Adapter: CM-CLAUDE-CODE-ADAPTER v1.0.0.

17. **Emitir artefactos**: `artifact_write` para cada archivo generado (subagent, skills, manifest).

### Fase 7: Verificacion de equivalencia (H4)

18. **Si es pilot o primera transmutacion**, ejecutar 3 inputs representativos:
    - **Input 1** (routing): Solicitud dentro de scope → verificar que el agente CC rutea al mismo estado que el agente KORA.
    - **Input 2** (rechazo): Solicitud fuera de scope → verificar que el rechazo se produce con el mismo mensaje.
    - **Input 3** (tool): Solicitud que activa tool → verificar que el tool esta disponible y se invoca.
    Documentar resultados en manifest campo `behavioral_equivalence`.

## Signature Output

```json
{
  "artifacts": [
    {"path": ".claude/agents/{ns}--{name}.md", "type": "subagent"},
    {"path": ".claude/skills/{ns}--{name}--{cm}/SKILL.md", "type": "skill"},
    {"path": "_transmutation/{ns}--{name}.yml", "type": "manifest"}
  ],
  "mappings": [
    {"kora_field": "sandbox.mode", "cc_field": "permissionMode", "type": "direct"},
    {"kora_field": "tools.allow", "cc_field": "tools", "type": "derived"},
    {"kora_field": "USER.md", "cc_field": null, "type": "excluded"}
  ],
  "enforcement_gaps": [
    {"constraint": "allowed_kb", "original": "server-side", "effective": "instruccional"}
  ],
  "exclusions": [
    {"component": "USER.md", "reason": "runtime-spec §6.1"}
  ],
  "warnings": [],
  "token_budget": {"body_chars": 0, "within_limit": true}
}
```
