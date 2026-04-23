# Curation Conductor Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear una skill KORA productiva que determine y acompañe el proceso de curación de artefactos de conocimiento KORA de comienzo a fin.

**Architecture:** La skill vivirá en `artifacts/skills/kora/curation-conductor/` con un `SKILL.md` compacto y dos referencias de soporte. No reemplaza `atomize`, `promote` ni `validation`; los orquesta explícitamente dentro del pipeline de knowledge y rerutea fuera de scope cuando el material corresponde a `spec`.

**Tech Stack:** Markdown KORA, `toolchain/kora`, specs KORA, referencias locales.

---

### Task 1: Abrir el ciclo rojo con tests del bundle

**Files:**
- Create: `tests/test_curation_conductor_skill.py`
- Reference: `artifacts/skills/kora/curation-conductor/`

- [ ] **Step 1: Write the failing test for skill existence**

```python
def test_curation_conductor_skill_exists(self):
    skill_path = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "SKILL.md"
    self.assertTrue(skill_path.exists(), skill_path)
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
python3 -m unittest tests.test_curation_conductor_skill.CurationConductorSkillTests.test_curation_conductor_skill_exists -v
```

Expected:
- `FAIL` because the skill does not exist yet.

- [ ] **Step 3: Write the failing test for references**

```python
def test_curation_conductor_references_exist(self):
    base = ROOT / "artifacts" / "skills" / "kora" / "curation-conductor" / "referencias"
    self.assertTrue((base / "process-map.md").exists())
    self.assertTrue((base / "family-decision-table.md").exists())
```

- [ ] **Step 4: Run test to verify it fails**

Run:

```bash
python3 -m unittest tests.test_curation_conductor_skill.CurationConductorSkillTests.test_curation_conductor_references_exist -v
```

Expected:
- `FAIL` because references do not exist yet.

### Task 2: Implement the skill bundle

**Files:**
- Create: `artifacts/skills/kora/curation-conductor/SKILL.md`
- Create: `artifacts/skills/kora/curation-conductor/referencias/process-map.md`
- Create: `artifacts/skills/kora/curation-conductor/referencias/family-decision-table.md`
- Test: `tests/test_curation_conductor_skill.py`

- [ ] **Step 1: Create the skill directory**

Run:

```bash
mkdir -p artifacts/skills/kora/curation-conductor/referencias
```

- [ ] **Step 2: Write `SKILL.md` in native KORA shape**

The file must include:

- `_manifest`
- `version`
- `status`
- `nombre`
- `descripcion`
- `extensions.kora.vector_ontologico`
- `extensions.kora.atlas.forma_material = habilidad`
- `conocimiento_permitido` with the KORA specs it depends on
- `## Proposito`
- `## Cuando Usar`
- `## Workflow`
- `## Reglas Duras`
- `## Recursos`
- explicit reroute for prescriptive/foundational material outside `artifacts/knowledge/`

- [ ] **Step 3: Write `referencias/process-map.md`**

Content must map:

- intake
- scope gate
- family selection
- `F` koraficación
- reroute to `spec`
- `atomic` -> `atomize`
- validation
- promote
- final states

- [ ] **Step 4: Write `referencias/family-decision-table.md`**

Content must include a decision table with at least:

- input shape
- descriptive vs prescriptive
- `atomic` yes/no
- target family or reroute verdict
- producer
- start zone
- publish gate

- [ ] **Step 5: Run the two new tests**

Run:

```bash
python3 -m unittest tests.test_curation_conductor_skill -v
```

Expected:
- `OK`

### Task 3: Validate the skill against the repo

**Files:**
- Verify: `artifacts/skills/kora/curation-conductor/`
- Verify: generated docs after indexing

- [ ] **Step 1: Reindex the repo**

Run:

```bash
python3 toolchain/kora index
```

Expected:
- catalog regenerated and includes the new skill

- [ ] **Step 2: Run strict checks**

Run:

```bash
python3 toolchain/kora check --strict
```

Expected:
- all checks pass

- [ ] **Step 3: Run full test suite**

Run:

```bash
python3 -m unittest discover -s tests
```

Expected:
- full suite passes

- [ ] **Step 4: Commit**

```bash
git add \
  docs/superpowers/specs/2026-04-23-curation-conductor-skill-design.md \
  docs/superpowers/plans/2026-04-23-curation-conductor-skill.md \
  artifacts/skills/kora/curation-conductor/SKILL.md \
  artifacts/skills/kora/curation-conductor/referencias/process-map.md \
  artifacts/skills/kora/curation-conductor/referencias/family-decision-table.md \
  tests/test_curation_conductor_skill.py \
  docs/generated/catalog.yml \
  docs/generated/repo-graph.json \
  docs/generated/repo-stats.json \
  docs/generated/repo-stats.md
git commit -m "feat(skills): agrega curation conductor"
```
