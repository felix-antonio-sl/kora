# JointJS Open-Source Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear una skill KORA productiva para Claude Code especializada en JointJS open-source, con consulta obligatoria a la documentación oficial viva antes de responder o implementar.

**Architecture:** La skill vivirá en `artifacts/skills/kora/jointjs-open-source/` como artefacto productivo KORA con un único `SKILL.md`. El contenido técnico de JointJS no se replica localmente; el `SKILL.md` solo codifica el workflow live-docs, las reglas duras OSS vs Plus y el contrato de salida.

**Tech Stack:** Markdown, YAML frontmatter KORA, `toolchain/kora`, `quick_validate.py` como referencia auxiliar.

---

### Task 1: Scaffold y validación base

**Files:**
- Create: `artifacts/skills/kora/jointjs-open-source/SKILL.md`
- Test: validar con `kora check --strict`

- [ ] **Step 1: Scaffold con el inicializador canónico**

Run:

```bash
python3 /Users/felixsanhueza/.codex/skills/.system/skill-creator/scripts/init_skill.py \
  jointjs-open-source \
  --path /Users/felixsanhueza/Developer/kora/artifacts/skills/kora \
  --interface display_name="JointJS OSS Specialist" \
  --interface short_description="Implementa y depura JointJS OSS con docs oficiales." \
  --interface default_prompt="Usa $jointjs-open-source para resolver esto con JointJS open-source consultando primero la documentación oficial viva."
```

Expected:
- Se crea `artifacts/skills/kora/jointjs-open-source/`
- Se crea `SKILL.md`

- [ ] **Step 2: Verificar el scaffold**

Run:

```bash
find artifacts/skills/kora/jointjs-open-source -maxdepth 3 -type f | sort
```

Expected:
- `artifacts/skills/kora/jointjs-open-source/SKILL.md`

- [ ] **Step 3: Validar formato base**

Run:

```bash
python3 /Users/felixsanhueza/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/felixsanhueza/Developer/kora/artifacts/skills/kora/jointjs-open-source
```

Expected:
- `Skill is valid!`

### Task 2: Escribir el `SKILL.md` live-docs puro

**Files:**
- Modify: `artifacts/skills/kora/jointjs-open-source/SKILL.md`
- Reference: `docs/superpowers/specs/2026-04-20-jointjs-open-source-skill-design.md`

- [ ] **Step 1: Reemplazar el template por frontmatter mínimo**

```yaml
---
name: jointjs-open-source
description: Usa esta skill cuando necesites implementar, integrar, depurar o explicar JointJS open-source en Claude Code consultando siempre la documentación oficial viva en docs.jointjs.com antes de responder.
---
```

- [ ] **Step 2: Escribir el cuerpo compacto del workflow**

Contenido mínimo esperado:

```md
# JointJS Open-Source

## Proposito

Especialista en JointJS open-source para Claude Code. Antes de responder sobre API, integración, implementación o debugging, consulta la documentación oficial viva en `https://docs.jointjs.com/`.

## Cuando Usar

- dudas de API de JointJS
- implementación de diagramas, graph, paper, links, ports o shapes
- integración con frameworks
- debugging de comportamiento o eventos
- preguntas de arquitectura o capacidades del OSS

## Workflow

1. Clasificar la consulta.
2. Ubicar la sección oficial más probable en `docs.jointjs.com`.
3. Leer la documentación oficial viva antes de responder.
4. Responder o implementar con base en esa fuente.
5. Citar la página o sección oficial consultada.
6. Marcar explícitamente cualquier inferencia.

## Reglas Duras

- No responder de memoria sobre JointJS si la docs oficial puede verificarse.
- Tratar `https://docs.jointjs.com/` como fuente de verdad.
- Si una feature parece de JointJS+, decirlo explícitamente y no presentarla como OSS.
- No copiar bloques extensos de documentación oficial al output.

## Politica OSS vs Plus

- Asumir OSS por defecto.
- Si la docs oficial sugiere plugin o paquete Plus, marcar la frontera explícitamente.

## Salida Esperada

- respuesta breve y accionable
- referencia a la sección oficial consultada
- código mínimo cuando se pida implementación
- inferencias etiquetadas como tales
```

- [ ] **Step 3: Ejecutar validación de formato**

Run:

```bash
python3 /Users/felixsanhueza/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/felixsanhueza/Developer/kora/artifacts/skills/kora/jointjs-open-source
```

Expected:
- `Skill is valid!`

### Task 3: Verificar la skill final en el repo

**Files:**
- Verify: `artifacts/skills/kora/jointjs-open-source/SKILL.md`
- Verify: `docs/generated/catalog.yml`

- [ ] **Step 1: Validar skill final**

Run:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
```

Expected:
- la nueva skill entra limpia al catálogo y el strict queda verde

- [ ] **Step 2: Verificar árbol final**

Run:

```bash
find artifacts/skills/kora/jointjs-open-source -maxdepth 3 -type f | sort
```

Expected:
- `artifacts/skills/kora/jointjs-open-source/SKILL.md`

- [ ] **Step 3: Commit**

```bash
git add \
  docs/superpowers/plans/2026-04-20-jointjs-open-source-skill.md \
  artifacts/skills/kora/jointjs-open-source/SKILL.md
git commit -m "feat(skills): agrega skill jointjs open-source"
```
