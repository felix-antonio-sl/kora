# Urgenciologo Walking Skeleton Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Encender la primera astilla vertical clinica de KORA con `salud/urgenciologo`, `me-dolor-toracico` y `claude-code`.

**Architecture:** Se implementa un consumer clinico productivo minimo, se cose el corpus `med-emergencia` en el tramo TOC -> `me-dolor-toracico`, y se cierra el tramo faltante de `transmute` para producir un bundle Claude Code deployable con trazabilidad visible. La salida funcional se verifica con un canario fijo y registro en `docs/generated/invocations.jsonl`.

**Tech Stack:** Python 3, unittest, YAML frontmatter KORA, runtime Claude Code markdown bundle.

---

### Task 1: Cubrir el skeleton con tests rojos

**Files:**
- Modify: `tests/test_cli_smoke.py`
- Modify: `tests/test_semantic_validation.py`
- Create: `tests/test_urgenciologo_skeleton.py`
- Reference: `artifacts/knowledge/salud/med-emergencia/dolor-toracico.md`

- [ ] **Step 1: Write the failing test for productive urgenciologo existence**

```python
def test_urgenciologo_productive_agent_exists(self):
    agent_path = ROOT / "artifacts" / "agents" / "salud" / "urgenciologo" / "AGENT.md"
    self.assertTrue(agent_path.exists(), agent_path)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_urgenciologo_productive_agent_exists`
Expected: `FAIL` because `artifacts/agents/salud/urgenciologo/AGENT.md` does not exist yet.

- [ ] **Step 3: Write the failing test for TOC wiring**

```python
def test_med_emergencia_toc_cites_dolor_toracico(self):
    frontmatter, _ = load_markdown_parts(
        ROOT / "artifacts" / "knowledge" / "salud" / "med-emergencia" / "toc-body-of-knowledge.md"
    )
    cites = ((frontmatter.get("relations") or {}).get("cites") or [])
    self.assertIn("urn:salud:kb:me-dolor-toracico", cites)
```

- [ ] **Step 4: Run test to verify it fails**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_med_emergencia_toc_cites_dolor_toracico`
Expected: `FAIL` because `relations.cites` does not include `urn:salud:kb:me-dolor-toracico`.

- [ ] **Step 5: Write the failing test for Claude bundle output**

```python
def test_transmute_claude_code_emits_deployable_bundle(self):
    result = run_cli("transmute", "--target", "claude-code", "--agent", "salud/urgenciologo")
    target_dir = ROOT / "artifacts" / "agents" / "salud" / "urgenciologo" / "_BUILD" / "claude-code"
    bundle_path = target_dir / "urgenciologo.md"
    self.assertTrue(bundle_path.exists(), bundle_path)
    content = bundle_path.read_text(encoding="utf-8")
    self.assertIn("name:", content)
    self.assertIn("description:", content)
    self.assertIn("tools:", content)
```

- [ ] **Step 6: Run test to verify it fails**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_transmute_claude_code_emits_deployable_bundle`
Expected: `FAIL` because `transmute` does not emit `urgenciologo.md` yet.

- [ ] **Step 7: Write the failing test for invocation log helper**

```python
def test_invocation_log_appends_canary_record(self):
    log_path = ROOT / "docs" / "generated" / "invocations.jsonl"
    self.assertTrue(log_path.exists(), log_path)
```

- [ ] **Step 8: Run test to verify it fails**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_invocation_log_appends_canary_record`
Expected: `FAIL` because the log file/helper does not exist yet.

### Task 2: Implement corpus wiring and productive urgenciologo

**Files:**
- Modify: `artifacts/knowledge/salud/med-emergencia/toc-body-of-knowledge.md`
- Create: `artifacts/agents/salud/urgenciologo/AGENT.md`
- Reference: `artifacts/agents/_FRAGUA/INBOX/urgenciologo/AGENT.md`
- Test: `tests/test_urgenciologo_skeleton.py`

- [ ] **Step 1: Add explicit TOC relation to `me-dolor-toracico`**

```yaml
relations:
  depends:
    - urn:salud:kb:med-emergencia
  cites:
    - urn:salud:kb:me-dolor-toracico
```

- [ ] **Step 2: Run the TOC wiring test**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_med_emergencia_toc_cites_dolor_toracico`
Expected: `PASS`

- [ ] **Step 3: Create minimal productive `salud/urgenciologo/AGENT.md`**

```yaml
---
_manifest:
  urn: "urn:salud:artefacto:urgenciologo"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-20"
    source: "artifacts/agents/_FRAGUA/INBOX/urgenciologo/AGENT.md"
version: "1.0.0"
status: activo
nombre: urgenciologo
descripcion: "Copiloto clinico de medicina de emergencia para pacientes agudos indiferenciados."
tags: [urgencias, emergencias, medicina-emergencia, salud]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 1
      xi: 2
      lambda: 0
      phi: 1
      sigma: [2,1,2,1,1]
    presentacion: estado-primario
    atlas:
      arnes_categorico: persona
      forma_material: agente-propiamente-tal
      metafora_relacional: centro-de-control
    entornos_objetivo: [claude-code]
    conocimiento_permitido:
      - "urn:salud:kb:med-emergencia"
      - "urn:salud:kb:me-toc-body-of-knowledge"
      - "urn:salud:kb:me-razonamiento-clinico"
      - "urn:salud:kb:me-evaluacion-primaria"
      - "urn:salud:kb:me-dolor-toracico"
    componible_con: []
  claude_code:
    model: opus
    color: red
    max_turns: 12
artefacto:
  perfil:
    dominio: [medicina-emergencia, urgencias, razonamiento-clinico]
    disparadores: [consulta-clinica-aguda, dolor-toracico]
    salidas: [analisis, priorizacion, resumen]
  plan:
    estado_inicial: S-DISPATCHER
    estado_terminal: S-END
    estados:
      - id: S-DISPATCHER
        accion: "Clasificar consulta clinica de urgencia y fijar foco sobre el KB permitido."
      - id: S-END
        accion: "Emitir respuesta clinica acotada al corpus permitido."
  interfaz:
    herramientas: [Read, Grep, Glob]
    permisos: lectura-corpus
  contexto:
    memoria_config:
      mode: session
  invariantes:
    reglas_duras:
      - "No prescribir directamente"
      - "No salir del corpus permitido cuando la pregunta se responda con KB local"
      - "Explicitar incertidumbre cuando el nodo no cubra la consulta"
---
```

- [ ] **Step 4: Run the productive agent existence test**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_urgenciologo_productive_agent_exists`
Expected: `PASS`

- [ ] **Step 5: Run focused validation**

Run: `python3 toolchain/kora validate --profile strict`
Expected: `Validation complete! Workspaces valid:` with `salud/urgenciologo` included and no new invalid workspaces.

### Task 3: Implement deployable Claude Code bundle output

**Files:**
- Modify: `toolchain/kora_lib/transmute.py`
- Modify: `tests/test_cli_smoke.py`
- Modify: `tests/test_urgenciologo_skeleton.py`
- Reference: `runtime/claude-code-runtime-extension.md`

- [ ] **Step 1: Add failing smoke assertions for bundle shape**

```python
def test_transmute_claude_code_emits_bundle_file(self):
    result = run_cli("transmute", "--target", "claude-code", "--agent", "salud/urgenciologo")
    self.assertIn("Bundle:", result.stdout)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_cli_smoke.KoraCliSmokeTests.test_transmute_claude_code_emits_bundle_file`
Expected: `FAIL` because `transmute` does not print `Bundle:` yet.

- [ ] **Step 3: Implement minimal Claude bundle emitter**

```python
def _emit_claude_code_bundle(target_dir: Path, frontmatter: dict, body: str, transmutation_path: Path) -> Path:
    claude_ext = (frontmatter.get("extensions") or {}).get("claude_code") or {}
    bundle_path = target_dir / f"{frontmatter['nombre']}.md"
    lines = [
        "---",
        f"name: {frontmatter['nombre']}",
        f"description: {frontmatter['descripcion']}",
        "tools: Read, Grep, Glob",
        f"model: {claude_ext.get('model', 'opus')}",
        f"color: {claude_ext.get('color', 'gray')}",
        f"max_turns: {claude_ext.get('max_turns', 12)}",
        "---",
        "",
        f"Source URN: {frontmatter['_manifest']['urn']}",
        f"Transmutation manifest: {transmutation_path.name}",
        "",
        body.strip(),
        "",
    ]
    bundle_path.write_text("\n".join(lines), encoding="utf-8")
    return bundle_path
```

- [ ] **Step 4: Call the emitter from `cmd_transmute` for `claude-code`**

```python
bundle_path = None
if target == "claude-code":
    bundle_path = _emit_claude_code_bundle(target_dir, frontmatter, body, yml_path)
    print(f"  Bundle: {bundle_path.relative_to(KORA_ROOT)}")
```

- [ ] **Step 5: Run focused transmute tests**

Run: `python3 -m unittest tests.test_cli_smoke tests.test_urgenciologo_skeleton -v`
Expected: `PASS` for the new bundle assertions.

### Task 4: Implement canary logging support

**Files:**
- Modify: `toolchain/kora_lib/transmute.py`
- Create: `docs/generated/invocations.jsonl` (through code path or fixture-safe writer)
- Modify: `tests/test_urgenciologo_skeleton.py`

- [ ] **Step 1: Write the failing helper test**

```python
def test_append_invocation_record_writes_jsonl(self):
    target = ROOT / "docs" / "generated" / "invocations.jsonl"
    append_invocation_record(
        {
            "agent_urn": "urn:salud:artefacto:urgenciologo",
            "input_hash": "sha256:in",
            "output_hash": "sha256:out",
            "eval_result": "baseline",
        },
        path=target,
    )
    content = target.read_text(encoding="utf-8")
    self.assertIn('"agent_urn": "urn:salud:artefacto:urgenciologo"', content)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_append_invocation_record_writes_jsonl`
Expected: `FAIL` because `append_invocation_record` does not exist yet.

- [ ] **Step 3: Implement the minimal JSONL appender**

```python
def append_invocation_record(record: dict, path: Path | None = None) -> Path:
    import json
    from datetime import datetime, timezone

    target = path or (KORA_ROOT / "docs" / "generated" / "invocations.jsonl")
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts": datetime.now(timezone.utc).isoformat(),
        **record,
    }
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return target
```

- [ ] **Step 4: Run focused logging tests**

Run: `python3 -m unittest tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_append_invocation_record_writes_jsonl`
Expected: `PASS`

### Task 5: Verify the repository and prepare manual canary execution

**Files:**
- Modify: `tests/test_urgenciologo_skeleton.py`
- Verify: `artifacts/agents/salud/urgenciologo/_BUILD/claude-code/`
- Verify: `docs/generated/invocations.jsonl`

- [ ] **Step 1: Run repository verification**

Run: `python3 toolchain/kora check --strict`
Expected: `Passed: 17` and `Failed: 0`

- [ ] **Step 2: Run full test suite**

Run: `python3 -m unittest discover -s tests`
Expected: `OK`

- [ ] **Step 3: Generate fresh bundle**

Run: `python3 toolchain/kora transmute --target claude-code --agent salud/urgenciologo`
Expected: stdout includes `Manifest:` and `Bundle:`

- [ ] **Step 4: Record manual canary baseline**

```python
append_invocation_record(
    {
        "agent_urn": "urn:salud:artefacto:urgenciologo",
        "input_hash": "sha256:<hash-pregunta-canario>",
        "output_hash": "sha256:<hash-respuesta-baseline>",
        "eval_result": "baseline",
    }
)
```

- [ ] **Step 5: Commit implementation**

```bash
git add artifacts/knowledge/salud/med-emergencia/toc-body-of-knowledge.md \
  artifacts/agents/salud/urgenciologo/AGENT.md \
  toolchain/kora_lib/transmute.py \
  tests/test_cli_smoke.py \
  tests/test_semantic_validation.py \
  tests/test_urgenciologo_skeleton.py \
  docs/generated/invocations.jsonl \
  docs/superpowers/plans/2026-04-20-urgenciologo-walking-skeleton.md
git commit -m "feat(salud): enciende skeleton de urgenciologo"
```
