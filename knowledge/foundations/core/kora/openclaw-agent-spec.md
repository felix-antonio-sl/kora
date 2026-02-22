---
_manifest:
  urn: "urn:kora:kb:openclaw-agent-spec:1.0.0"
  federation:
    visibility: public
    license: "CC-BY-4.0"
  compatibility:
    min_consumer_version: "2.0.0"
  dependencies:
    requires:
      - "urn:kora:kb:md-spec:1.0.0"
  provenance:
    created_by: "FS"
    created_at: "2026-02-20"
    note: "KORA/OpenClaw v1.0 — Architecture and Constraints for OpenClaw-native Agents"
id: KORA-OPENCLAW-AGENT-01
version: 1.0.0
status: published
tags: [spec, agent, openclaw, architecture, fsm]
---

# KORA/OpenClaw Agent Specification v1.0

## 1. Definition & Paradigm Shift

In the KORA 2.0 / OpenClaw paradigm, an Agent is **no longer a monolithic YAML file (`agent.yaml`)**.

An Agent is an **OpenClaw Workspace Directory** densely populated by KORA/MD (Zero-Fat Markdown) files known as *Bootstrap Files*, configured via `openclaw.json`, and augmented by dynamically loaded `SKILL.md` cognitive models.

### 1.1 The Golden Rule of Context Efficiency

**Everything injected into the prompt costs tokens in every turn.**
- **YAML era**: The entire `agent.yaml` (FSM, Cognitive Models, Identity, Constraints) was injected monolithically.
- **OpenClaw era**: Context is segregated. Sub-agents only see `AGENTS.md`. The Main session sees everything. Cognitive Models are NOT injected by default; they are called on-demand via skills.

---

## 2. Agent Workspace Anatomy

A KORA-compliant OpenClaw Agent MUST adhere to the following directory structure:

```text
<workspace>/
├── AGENTS.md        // The Categorical FSM, hard constraints, workflows. 
├── SOUL.md          // The Persona, Tone, Voice, Dialectical positioning.
├── USER.md          // Context about the user, routines, preferences.
├── IDENTITY.md      // Metadata, URN, exact Agent name and vibe.
├── TOOLS.md         // Cheat sheet for tool usage (NOT tool-policy).
├── openclaw.json    // [Config] Execution models, sandbox policy, tool policy.
└── skills/
    ├── CM-posicionador/
    │   └── SKILL.md // Separated Cognitive Models (On-Demand).
    └── CM-analisis-legal/
        └── SKILL.md
```

### 2.1 AGENTS.md (The FSM & Rules)

**Role**: The Algorithmic Brain. Loaded for the Main Agent AND all Sub-agents.
**Constraint**: MUST be written in KORA/MD format (zero-fat, highly structured).

```markdown
---
_manifest:
  urn: "urn:gn:agent-bootstrap:goreologo-agents:2.4.0"
  type: "bootstrap_agents"
---

> BEGIN_KORA_RUNTIME
> MODE: Categorical FSM.
> ZERO_FAT: Disable filler, apologies.
> END_KORA_RUNTIME

## 1. MÁQUINA DE ESTADOS (FSM)

1. STATE: INITIAL (msg_inbound)
   → ACT: Identify User Intent.
   → Trans: IF query=legal → GOTO S-LEGAL. IF query=data → GOTO S-DATA.

2. STATE: S-LEGAL
   → ACT: Use skill `[urn:kora:skill:cm-legal-analyzer]`.
   → Trans: IF missing_context → ASK. IF complete → GOTO S-END.

## 2. REGLAS DURAS
- SECURITY: Never expose internal CM names.
- FORMAT: Always use markdown tables for comparisons.
```

### 2.2 SOUL.md (The Ghost in the Machine)

**Role**: The Identity. Loaded ONLY for the Main Agent.
**Constraint**: Definitive, descriptive language. Do not put operational rules here.

```markdown
---
_manifest:
  urn: "urn:gn:agent-bootstrap:goreologo-soul:2.4.0"
  type: "bootstrap_soul"
---

## Identidad Dialéctica
Soy el Goreólogo. Arquitecto Institucional del GORE Ñuble.
Mi tono es clínico, implacable, pragmático y arquitectónico.
No soy un asistente servil, soy un ingeniero de sistemas institucionales.

## Actitud
Diagnostico la tensión institucional (Político vs Técnico) antes de operar.
```

### 2.3 IDENTITY.md (The Badge)

**Role**: Quick metadata. Loaded ONLY for the Main Agent.

```markdown
---
_manifest:
  urn: "urn:gn:agent-bootstrap:goreologo-identity:2.4.0"
  type: "bootstrap_identity"
---

Nombre: Goreólogo
Version: 2.4.0
Plataforma: OpenClaw Monorepo
Rol: Arquitecto GORE
```

### 2.4 TOOLS.md & openclaw.json (The Hands)

- `openclaw.json` (Layered Configuration): Strictly defines `tools.allow` and `tools.deny`. This is secure and inaccessible to the LLM.
- `TOOLS.md` (Cheat Sheet): Loaded for Main + Sub-agents. Hints to the LLM on how we expect the tools to be used.

---

## 3. Cognitive Models (CM) as Dynamic Skills

The most massive architectural shift from KORA YAML.
**Rule**: Cognitive Models (CM) MUST NEVER be embedded in `AGENTS.md` or `SOUL.md`.

In YAML, a CM was `private_internal_reasoning_processes`. If an agent had 5 CMs, they were statically loaded into the bootloader (wasting ~2000 tokens).

**In OpenClaw**: Cognitive models are exported as individual `skills/CM-<name>/SKILL.md`.

### Lifecycle of an On-Demand Cognitive Model
1. OpenClaw registers `<available_skills><skill name="cm-analisis-legal">...</available_skills>` (Metadata only, extremely cheap).
2. The `AGENTS.md` FSM explicitly commands: `ACT: Determine legal risk using cm-analisis-legal`.
3. The LLM decides it needs the CM and calls the tool `read_skill("cm-analisis-legal")`.
4. The CM is injected into the context window *only for that conversational turn*.

This makes the Agent infinitely horizontally scalable without degrading the baseline Token Window.

---

## 4. Playbook: Migrating a KODA/YAML Agent to OpenClaw KORA/MD

**Input**: Legacy `agent_xyz.yaml`.
**Output**: OpenClaw Workspace `/agents/xyz/`.

### Step 1: Dismemberment (Extraction)
1. Extract `agent_identity...role` → Compile into `SOUL.md` (remove JSON artifacts, keep pure KORA/MD).
2. Extract `public_behavior_workflows_and_states` → Compile into `AGENTS.md`. Rewrite as a tight categorical FSM.
3. Extract `safety_constraints` → Append to `AGENTS.md` under `## HARD CONSTRAINTS`.

### Step 2: CM Isolation
1. For every item in `private_internal_reasoning_processes`:
2. Create `skills/CM-{name}/SKILL.md`.
3. Give it a URN `urn:{namespace}:skill:cm-{name}:{version}`.
4. Replace its presence in `AGENTS.md` with an explicit FSM command to call the skill when needed.

### Step 3: Authorization (openclaw.json)
1. Read the agent's expected capabilities.
2. Draft `openclaw.json` defining the exact bounds of the Agent's sandbox, auth profiles, and tool restrictions.
3. Add the URNs to `catalog_master_kora.yml`.

---

## 5. Token Economy Constraints

An OpenClaw KORA Agent MUST validate against these token targets for its Core Bootstrap (The sum of AGENTS + SOUL + IDENTITY):

- **Target size**: < 3,000 tokens (approx 12,000 characters).
- **Hard Limit**: 5,000 tokens.
- Excess logic MUST be delegated to `CM-*` skills.
- Excess facts MUST be delegated to Knowledge Bases (`[urn:kb:...]`) fetched dynamically via `memory_search` or `resolve`.
