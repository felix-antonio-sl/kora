---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-21-jointjs-skill-y-transmutacion-claude"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-21"
    source: "Cierre operativo de la skill jointjs-open-source y de la capacidad skill -> claude-code en KORA."
version: "1.0.0"
status: publicado
tags: [handoff, jointjs, skill, claude-code, transmutacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:operational-memory-2026-04-21-jointjs-skill-y-transmutacion-claude"
    - "urn:kora:kb:next-session-prompt-2026-04-21-jointjs-skill-y-transmutacion-claude"
  refines:
    - "urn:kora:kb:handoff-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
---

# Handoff explícito — JointJS skill y transmutación skill -> Claude Code

## Resumen ejecutivo

Al cierre del **21 de abril de 2026**, KORA suma dos capacidades nuevas:

1. **Skill productiva `jointjs-open-source`** bajo `artifacts/skills/kora/`
2. **Transmutación de skill KORA a Claude Code skill bundle**

Esto cierra el gap que existía entre:

- skills KORA productivas
- y su proyección al runtime `claude-code`

Hasta antes de esta sesión:

- `agentskills` sí soportaba `skill -> runtime`
- `claude-code` solo soportaba `agent -> runtime`

Ahora `claude-code` también acepta skills productivas.

## Artefactos relevantes

### Skill fuente

- [artifacts/skills/kora/jointjs-open-source/SKILL.md](/Users/felixsanhueza/Developer/kora/artifacts/skills/kora/jointjs-open-source/SKILL.md)

Características:

- scope explícito: **JointJS open-source**
- consulta obligatoria a la docs oficial viva
- separación explícita OSS vs JointJS+
- sin corpus local ni mirrors de la documentación

### Bundle Claude generado

- [artifacts/skills/kora/jointjs-open-source/_BUILD/claude-code/jointjs-open-source/SKILL.md](/Users/felixsanhueza/Developer/kora/artifacts/skills/kora/jointjs-open-source/_BUILD/claude-code/jointjs-open-source/SKILL.md)
- [artifacts/skills/kora/jointjs-open-source/_BUILD/claude-code/_transmutation.yml](/Users/felixsanhueza/Developer/kora/artifacts/skills/kora/jointjs-open-source/_BUILD/claude-code/_transmutation.yml)

La shape final del target sigue la documentación oficial actual de Claude Code
Skills:

- layout `.../claude-code/<skill-name>/SKILL.md`
- frontmatter mínimo `name`, `description`

### Plan y spec

- [docs/superpowers/specs/2026-04-20-jointjs-open-source-skill-design.md](/Users/felixsanhueza/Developer/kora/docs/superpowers/specs/2026-04-20-jointjs-open-source-skill-design.md)
- [docs/superpowers/plans/2026-04-20-jointjs-open-source-skill.md](/Users/felixsanhueza/Developer/kora/docs/superpowers/plans/2026-04-20-jointjs-open-source-skill.md)

## Decisiones tomadas

### 1. Shape de la skill

No se usó el scaffold externo final del `skill-creator` porque chocaba con las
invariantes del repo:

- en `artifacts/skills/` KORA exige `autoria-spec`
- `agents/openai.yaml` no es subdir canónico para habilidades productivas del repo

La skill quedó como artefacto KORA productivo real, no como bundle híbrido.

### 2. Fuente de verdad

La skill `jointjs-open-source` es **live-docs puro**:

- la autoridad técnica vive en `https://docs.jointjs.com/`
- no se replica contenido técnico local
- el agente debe consultar la docs también para preguntas simples

### 3. Fidelidad del transmutador

La proyección `skill -> claude-code` se ajustó a la documentación oficial actual
de Claude Code skills, no a una reinterpretación libre basada en subagentes.

## Cambios funcionales en la toolchain

Archivo principal:

- [toolchain/kora_lib/transmute.py](/Users/felixsanhueza/Developer/kora/toolchain/kora_lib/transmute.py)

Cambios relevantes:

- `_build_claude_code_skill_target_path()`
- `_project_skill_frontmatter_to_claude_code()`
- `_emit_claude_code_skill_bundle()`
- `_transmute_skill_to_claude_code()`
- `cmd_transmute()` ahora intenta resolver skill productiva cuando el target es `claude-code`

## Tests agregados

- [tests/test_skill_transmute_claude.py](/Users/felixsanhueza/Developer/kora/tests/test_skill_transmute_claude.py)

Este test prueba que:

- `transmute --target claude-code --agent kora/jointjs-open-source` retorna exit 0
- emite `_transmutation.yml`
- emite bundle skill en `.../claude-code/jointjs-open-source/SKILL.md`

## Verificación fresca

Comandos corridos al cierre:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora transmute --target claude-code --agent kora/jointjs-open-source
```

Resultado:

- `check --strict` -> `18/18`
- `unittest` -> `Ran 321 tests`, `OK (skipped=2)`
- la transmutación skill -> Claude se ejecuta sin error y genera bundle

## Commits relevantes

Cadena reciente:

- `76eea2e` — spec skill JointJS
- `62e8af9` — skill `jointjs-open-source`
- `1b7352f` — alineación spec/plan a shape KORA
- `b4db0f1` — soporte `skill -> claude-code`

## Estado actual

### Lo que ya funciona

- skill productiva `jointjs-open-source`
- `skill -> claude-code` en toolchain
- bundle Claude generado correctamente

### Lo que todavía no está hecho

- deploy real del skill bundle a `~/.claude/skills/jointjs-open-source/`
- validación runtime real del uso del skill desde Claude Code
- equivalente `skill -> codex`
- equivalente `skill -> gemini`

## Supuestos vigentes

1. La documentación oficial relevante de Claude Code para skills sigue siendo
   consistente con el layout usado: `skills/<name>/SKILL.md`.
2. Para skills de Claude, basta frontmatter mínimo `name` + `description` en el
   bundle target.
3. El knowledge contract es vacío en esta skill porque su fuente de verdad es la
   docs web, no un corpus local KORA.

## Riesgos abiertos

1. **Drift de plataforma**:
   si Claude Code cambia la shape de skills, este transmutador requerirá ajuste.

2. **Paridad incompleta entre runtimes**:
   Claude ya soporta skill bundles; Codex/Gemini no necesariamente.

3. **Validación funcional aún offline**:
   hoy el éxito está verificado a nivel de bundle generado y tests del repo, no
   todavía por invocación real del skill bundle desde una sesión Claude.

## Pendientes concretos

1. Probar instalación real:

```bash
mkdir -p ~/.claude/skills/jointjs-open-source
cp artifacts/skills/kora/jointjs-open-source/_BUILD/claude-code/jointjs-open-source/SKILL.md ~/.claude/skills/jointjs-open-source/SKILL.md
```

2. Invocar Claude Code usando esa skill y verificar que:
   - consulta `docs.jointjs.com`
   - distingue OSS vs Plus
   - cita fuente oficial

3. Si eso funciona, cerrar el siguiente gap:
   - `skill -> codex`

## Handoff operativo

Si otra sesión retoma desde aquí:

1. leer este handoff
2. leer la memoria operativa compañera
3. verificar:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora transmute --target claude-code --agent kora/jointjs-open-source
```

Contrato esperado:

- `18/18`
- `321 OK (skipped=2)`
- bundle Claude presente en `_BUILD/claude-code/jointjs-open-source/SKILL.md`
