# KORA Usina Productiva Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** dejar KORA operable como usina productiva para ingerir, curar, catalogar y exponer conocimiento, y para modelar, gestionar, componer y transmutar artefactos agenticos portables a múltiples runtimes.

**Architecture:** primero se repara la capa de verdad del sistema para eliminar verdes falsos y taxonomías rotas. Luego se consolida un modelo intermedio único para knowledge y artefactos agenticos, se endurecen los pipelines de staging/promoción y recién después se cierra la proyección a runtimes como Claude Code, Codex, Gemini, OpenClaw y Hermes.

**Tech Stack:** Python 3, `toolchain/kora`, `toolchain/kora_lib/*`, KORA/MD, JSON Schema, unittest, docs derivadas en `docs/generated/`.

---

## Intent Contract

- **Beneficiario:** el operador que quiere usar KORA como fábrica continua de conocimiento y artefactos agenticos desplegables.
- **Cambio deseado:** convertir KORA en una cadena confiable de authoring -> validación -> catalogación -> composición -> transmutación.
- **Beneficio esperado:** poder meter documentos y componentes al sistema sin perder trazabilidad, y sacar knowledge curado y agentes/skills listos para runtime sin ritual manual excesivo.
- **Criterio mínimo de éxito:** un documento bruto puede atravesar `_SCRIPTORIUM` hasta quedar publicado y resoluble por URN; un artefacto compartido puede atravesar `artifacts/skills|agents` hasta transmutar correctamente a al menos Claude Code, Codex y OpenClaw.
- **Minimum eval:** `python3 toolchain/kora index`, `python3 toolchain/kora check --strict`, `python3 toolchain/kora validate --profile strict`, `python3 -m unittest discover -s tests`, y una prueba de transmutación real por target.
- **Autonomy limit:** la implementación puede decidir detalle de módulos, nombres internos y checks; no debe inventar nuevas capas doctrinales ni ampliar el IR sin confirmación humana.
- **Main risk:** seguir construyendo encima de validación/reporting legacy y terminar con una usina que “parece verde” pero no gobierna la realidad del repo.

## File Map

### Truth and gating

- Modify: `toolchain/kora_lib/validation.py`
- Modify: `toolchain/kora_lib/checks.py`
- Modify: `tests/test_semantic_validation.py`
- Modify: `tests/test_cli_smoke.py`
- Modify: `tests/test_autoria_validate.py`

### Catalog and derived reporting

- Modify: `toolchain/kora_lib/catalog.py`
- Modify: `toolchain/kora_lib/reports.py`
- Modify: `toolchain/kora_lib/agent_audit.py`
- Modify: `toolchain/kora_lib/cli.py`
- Modify: `toolchain/README.md`
- Modify: `docs/generated/*` only when explicitly regenerating after code changes

### Knowledge factory

- Modify: `toolchain/kora_lib/intake.py`
- Modify: `toolchain/kora_lib/promote.py`
- Modify: `toolchain/kora_lib/kb_graph.py`
- Modify: `serialization/knowledge-spec.md`
- Modify: `docs/plans/source-mapping.yml` only if intake mapping shape needs extension

### Agentic artifact factory

- Modify: `serialization/autoria-spec.md`
- Modify: `ontology/harness-spec.md`
- Modify: `runtime/transmutation-spec.md`
- Modify: `toolchain/kora_lib/transmute.py`
- Modify: `toolchain/kora_lib/graph.py`

### Runtime projections

- Modify: `runtime/claude-code-runtime-extension.md`
- Modify: `runtime/codex-runtime-extension.md`
- Modify: `runtime/gemini-runtime-extension.md`
- Modify: `runtime/openclaw-runtime-extension.md`
- Create: `runtime/hermes-runtime-extension.md` only when the first four targets are proven stable

## Phase 0: Stop Lying

### Task 1: Repair strict validation so green means something

**Files:**
- Modify: `toolchain/kora_lib/validation.py`
- Modify: `tests/test_semantic_validation.py`
- Test: `tests/test_cli_smoke.py`

- [ ] **Step 1: Fix the schema path used by strict validation**

Change validation to load `serialization/schemas/kora-artefacto.json` from config-backed paths instead of probing the removed legacy root `schemas/`.

- [ ] **Step 2: Fail hard if the universal schema is missing in the real repo**

Do not silently continue with `autoria_schema = None` when validating `AGENT.md` in strict mode. Emit a global failure.

- [ ] **Step 3: Add a regression test against real repo topology**

Extend the validation tests so one case uses the actual repo layout and asserts that strict validation loads the schema from `serialization/schemas/`.

- [ ] **Step 4: Verify the CLI exposes the repaired guarantee**

Run:

```bash
python3 toolchain/kora validate --profile strict
python3 -m unittest tests.test_semantic_validation tests.test_cli_smoke
```

Expected:
- `validate` still completes
- bootstrap/schema counters are coherent
- tests pass

- [ ] **Step 5: Commit**

```bash
git add toolchain/kora_lib/validation.py tests/test_semantic_validation.py tests/test_cli_smoke.py
git commit -m "fix: enforce strict autoria schema loading"
```

**Exit criteria:** strict validation can no longer pass while skipping the universal schema.

### Task 2: Decommission false-green reporting surfaces

**Files:**
- Modify: `toolchain/kora_lib/agent_audit.py`
- Modify: `tests/test_cli_smoke.py`
- Modify: `docs/generated/agent-audit.json`
- Modify: `docs/generated/agent-audit.md`

- [ ] **Step 1: Remove legacy baseline references from the audit generator**

Replace retired `specs/*`, `agentfile-spec`, and `skill-overlay-spec` baselines with the v5 spec roots: governance, ontology, serialization, runtime.

- [ ] **Step 2: Change the report contract**

If the generator only audits a subset of the fleet, make that explicit in payload and markdown. It must stop implying full-fleet health.

- [ ] **Step 3: If full v5 audit is not ready, mark the report as limited**

Expose a field such as `coverage_mode: partial` and a visible warning in markdown.

- [ ] **Step 4: Regenerate and verify**

Run:

```bash
python3 toolchain/kora sync-docs
python3 -m unittest tests.test_cli_smoke tests.test_agent_audit
```

Expected:
- report renders
- baseline paths are real
- no retired spec path survives

- [ ] **Step 5: Commit**

```bash
git add toolchain/kora_lib/agent_audit.py tests/test_cli_smoke.py docs/generated/agent-audit.json docs/generated/agent-audit.md
git commit -m "fix: make agent audit honest under v5"
```

**Exit criteria:** `agent-audit` no longer presents itself as authoritative when it is not.

## Phase 1: Make the Catalog Speak v5

### Task 3: Reclassify catalog entries around `artefacto`

**Files:**
- Modify: `toolchain/kora_lib/catalog.py`
- Modify: `toolchain/kora_lib/reports.py`
- Modify: `tests/test_cli_smoke.py`
- Modify: `docs/generated/catalog.yml`
- Modify: `docs/generated/repo-stats.json`
- Modify: `docs/generated/repo-stats.md`

- [ ] **Step 1: Define the v5 category model**

Use URN regime + `extensions.kora.atlas.forma_material` to classify entries into meaningful buckets. At minimum:
- `ArtefactosAgenticos`
- `Knowledge`
- `Documents`
- `Other`

- [ ] **Step 2: Preserve legacy compatibility only as adapter logic**

Legacy `agent` and `skill` URNs may still map, but `urn:*:artefacto:*` must become first-class.

- [ ] **Step 3: Repair stats semantics**

Stop using `Catalog.Agents` as `agent_bootstrap_artifacts`. Replace with a metric that matches the current model or remove it.

- [ ] **Step 4: Regenerate and inspect**

Run:

```bash
python3 toolchain/kora index
python3 toolchain/kora stats --json
python3 toolchain/kora resolve urn:kora:artefacto:forgemaster
```

Expected:
- `forgemaster` no longer resolves as `[Other]`
- stats stop saying `Agents: 0` while there are productive workspaces

- [ ] **Step 5: Commit**

```bash
git add toolchain/kora_lib/catalog.py toolchain/kora_lib/reports.py tests/test_cli_smoke.py docs/generated/catalog.yml docs/generated/repo-stats.json docs/generated/repo-stats.md
git commit -m "feat: align catalog taxonomy with autoria v5"
```

**Exit criteria:** derived reports and the catalog express the same ontology as the repo.

### Task 4: Remove operational drift from the public interface

**Files:**
- Modify: `toolchain/kora_lib/reports.py`
- Modify: `toolchain/kora_lib/checks.py`
- Modify: `toolchain/README.md`
- Modify: `toolchain/kora_lib/cli.py`
- Search/update: repo-wide `scripts/kora`, `scripts/kora_lib`

- [ ] **Step 1: Normalize all supported command references**

Replace every live operator hint `scripts/kora` with `python3 toolchain/kora`.

- [ ] **Step 2: Add a drift check**

Teach `check --strict` to flag supported docs or fix hints that still reference removed operational paths.

- [ ] **Step 3: Verify**

Run:

```bash
rg -n "scripts/kora|scripts/kora_lib" /Users/felixsanhueza/Developer/kora
python3 toolchain/kora check --strict
```

Expected:
- only intentionally historical references remain
- strict check passes

- [ ] **Step 4: Commit**

```bash
git add toolchain/kora_lib/reports.py toolchain/kora_lib/checks.py toolchain/README.md toolchain/kora_lib/cli.py
git commit -m "fix: remove legacy scripts path from operator surface"
```

**Exit criteria:** the repo has one live operational entrypoint and teaches only that one.

## Phase 2: Build the Knowledge Factory

### Task 5: Define and harden the document pipeline end-to-end

**Files:**
- Modify: `serialization/knowledge-spec.md`
- Modify: `toolchain/kora_lib/intake.py`
- Modify: `toolchain/kora_lib/promote.py`
- Modify: `toolchain/kora_lib/kb_graph.py`
- Test: `tests/test_check_pipeline.py`

- [ ] **Step 1: Freeze the pipeline contract**

State clearly what each stage means:
- `_SCRIPTORIUM/INBOX` = bruto ingresado
- `_SCRIPTORIUM/REVIEW` = curado y validable
- `artifacts/knowledge/{ns}` = publicado y resoluble

- [ ] **Step 2: Make intake produce invariant minimum metadata**

Every ingested document must carry stable provenance, source identity, and enough normalization to be promotable later.

- [ ] **Step 3: Make promote enforce publication gates**

Promotion must require catalog/index health, resolvable references, and md-spec / knowledge-spec compliance.

- [ ] **Step 4: Verify with a fixture path**

Run:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora kb-graph --json --orphans
python3 -m unittest tests.test_check_pipeline
```

- [ ] **Step 5: Commit**

```bash
git add serialization/knowledge-spec.md toolchain/kora_lib/intake.py toolchain/kora_lib/promote.py toolchain/kora_lib/kb_graph.py tests/test_check_pipeline.py
git commit -m "feat: harden knowledge ingestion and promotion pipeline"
```

**Exit criteria:** a raw source can become curated published knowledge with traceability and no broken graph.

## Phase 3: Build the Agentic Artifact Factory

### Task 6: Treat skills, subagents, and agents as one authoring continuum

**Files:**
- Modify: `serialization/autoria-spec.md`
- Modify: `ontology/harness-spec.md`
- Modify: `toolchain/kora_lib/validation.py`
- Modify: `toolchain/kora_lib/graph.py`
- Test: `tests/test_autoria_validate.py`

- [ ] **Step 1: Freeze the minimum shared contract**

The shared authoring model must express:
- identity
- ontological vector
- allowed knowledge
- composability
- runtime intent

- [ ] **Step 2: Tighten conditional validation by `forma_material`**

Skills, subagents, agents, and platform agents should each have explicit required dimensions and disallowed ones.

- [ ] **Step 3: Surface composition explicitly in the graph**

Graph output should show which artifacts depend on which knowledge and which artifacts compose which others.

- [ ] **Step 4: Verify**

Run:

```bash
python3 toolchain/kora check --strict
python3 toolchain/kora graph --json
python3 -m unittest tests.test_autoria_validate tests.test_semantic_validation
```

- [ ] **Step 5: Commit**

```bash
git add serialization/autoria-spec.md ontology/harness-spec.md toolchain/kora_lib/validation.py toolchain/kora_lib/graph.py tests/test_autoria_validate.py
git commit -m "feat: unify artifact factory around autoria continuum"
```

**Exit criteria:** shared components are authored once and can evolve across forms without model drift.

### Task 7: Close composition between knowledge and artifacts

**Files:**
- Modify: `serialization/autoria-spec.md`
- Modify: `toolchain/kora_lib/checks.py`
- Modify: `toolchain/kora_lib/graph.py`
- Test: `tests/test_check_pipeline.py`

- [ ] **Step 1: Enforce `conocimiento_permitido` and `componible_con` as real contracts**

These fields must stop being decorative. References must resolve, and invalid cross-links must fail checks.

- [ ] **Step 2: Add policy checks**

At minimum:
- every published artifact that depends on knowledge must declare it
- every composition target must exist and be compatible enough to compose

- [ ] **Step 3: Verify**

Run:

```bash
python3 toolchain/kora check --strict
python3 toolchain/kora graph --json
python3 -m unittest tests.test_check_pipeline tests.test_cli_smoke
```

- [ ] **Step 4: Commit**

```bash
git add serialization/autoria-spec.md toolchain/kora_lib/checks.py toolchain/kora_lib/graph.py tests/test_check_pipeline.py
git commit -m "feat: enforce knowledge and artifact composition contracts"
```

**Exit criteria:** composition is explicit, resolvable, and governed by checks.

## Phase 4: Runtime Output You Can Actually Ship

### Task 8: Prove transmutation on real targets before adding Hermes

**Files:**
- Modify: `runtime/transmutation-spec.md`
- Modify: `toolchain/kora_lib/transmute.py`
- Modify: `runtime/claude-code-runtime-extension.md`
- Modify: `runtime/codex-runtime-extension.md`
- Modify: `runtime/gemini-runtime-extension.md`
- Modify: `runtime/openclaw-runtime-extension.md`
- Test: `tests/test_cli_smoke.py`

- [ ] **Step 1: Define a proof target set**

For short-term production, require verified projection for:
- Claude Code
- Codex
- Gemini
- OpenClaw

Hermes stays blocked until these are stable.

- [ ] **Step 2: Add one canonical artifact fixture per material form**

Use real productive artifacts where possible, not toy examples.

- [ ] **Step 3: Verify transmutation round-trip / output shape**

Run:

```bash
python3 toolchain/kora transmute --target claude-code --agent kora/curator --dry-run
python3 toolchain/kora transmute --target codex --agent kora/curator --dry-run
python3 toolchain/kora transmute --target gemini --agent kora/curator --dry-run
python3 toolchain/kora transmute --target openclaw --agent kora/curator --dry-run
python3 -m unittest tests.test_cli_smoke
```

- [ ] **Step 4: Commit**

```bash
git add runtime/transmutation-spec.md toolchain/kora_lib/transmute.py runtime/claude-code-runtime-extension.md runtime/codex-runtime-extension.md runtime/gemini-runtime-extension.md runtime/openclaw-runtime-extension.md tests/test_cli_smoke.py
git commit -m "feat: prove transmutation on primary runtimes"
```

**Exit criteria:** one canonical artifact can be projected consistently to the primary runtimes.

## Phase 5: Continuous Operation

### Task 9: Make maintenance continuous without adding theater

**Files:**
- Modify: `toolchain/kora_lib/checks.py`
- Modify: `toolchain/kora_lib/reports.py`
- Modify: `.github/workflows/*` if CI exists for these checks
- Modify: `docs/reports/*` only if a real operator handoff format needs update

- [ ] **Step 1: Define the production maintenance gate**

Required:
- `index`
- `check --strict`
- `validate --profile strict`
- `unittest`
- at least one transmute proof on touched artifact classes

- [ ] **Step 2: Separate truth from dashboards**

Generated docs may exist, but deployment or promotion decisions must key off checks, not prettified markdown.

- [ ] **Step 3: Verify**

Run:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict
python3 -m unittest discover -s tests
```

- [ ] **Step 4: Commit**

```bash
git add toolchain/kora_lib/checks.py toolchain/kora_lib/reports.py .github/workflows
git commit -m "feat: define production maintenance gate"
```

**Exit criteria:** KORA can be operated continuously without relying on human memory to know what “healthy” means.

## Final Production Bar

KORA is ready to work as the usina you want when all of these are true:

- strict validation uses the real v5 schema and fails loudly when it cannot
- the catalog models `artefacto` as first-class
- knowledge can move from bruto to curado to publicado with provenance intact
- shared agentic components are authored once in the intermediate model
- composition with knowledge and between artifacts is explicit and checked
- primary runtime projections are proven on real artifacts
- the maintenance gate is executable and trusted

## Non-Goals For This Wave

- do not add a new doctrine layer
- do not add Hermes before the first four runtimes are stable
- do not turn generated docs into the source of truth
- do not optimize for elegance before closing the truth loop

## Recommended Execution Order

1. Task 1
2. Task 2
3. Task 3
4. Task 4
5. Task 5
6. Task 6
7. Task 7
8. Task 8
9. Task 9

## Review Check Before Starting Execution

- If a task changes the truth model, run `check --strict` before touching docs.
- If a task changes docs only, verify it does not smuggle schema/runtime drift.
- If a task touches transmutation, verify on at least one real productive artifact.
- If a task touches validation, make one test fail first and then fix it.

