---
_manifest:
  urn: "urn:kora:kb:plan-normalizacion-recuperacion-kora-2026-05-26"
  provenance:
    created_by: "Codex"
    created_at: "2026-05-26"
    source: "Solicitud HITL: normalizar/recuperar agentes, skills y artefactos de conocimiento KORA, y recuperar versiones locales desde Codex, Claude y OpenClaw."
version: "0.1.0"
status: borrador
tags: [plan, recuperacion, normalizacion, agents, skills, knowledge, codex, claude-code, openclaw]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:transmutation-spec"
---

# Plan operativo — normalizacion y recuperacion KORA

## Regla de ejecucion

La direccion de verdad es:

```text
fuentes originales -> KORA IR -> runtime outputs
runtime outputs mejores -> REVIEW -> KORA IR -> runtime outputs
```

Los outputs runtime de Codex, Claude y OpenClaw no pisan KORA directamente.
Todo item externo recuperable entra como candidato trazado, se normaliza contra
`autoria-spec` o KORA/MD, y se promueve solo despues de gates.

## Estado de inventario

Inventario reproducible:

```bash
python3 toolchain/kora recovery-inventory --json --output docs/generated/recovery-inventory.json
python3 toolchain/kora recovery-inventory --output docs/generated/recovery-inventory.md
```

Snapshot inicial:

| Area | Conteo | Observacion |
|------|--------|-------------|
| Agents KORA productivos | 6 | Todos tienen mapping externo Claude/OpenClaw o proyeccion Codex. |
| Skills KORA productivos root | 32 | El catalogo registra 35 entradas por incluir skills anidados y retirados. |
| Knowledge KORA productivo escaneado | 575 | 56 gaps de `provenance.source`. |
| Knowledge INBOX | 97 | Pre-categorial; requiere source-map antes de promocion. |
| Knowledge REVIEW | 162 | Cola primaria para normalizacion KORA/MD. |
| Codex skills externos | 38 | 32 mapeados, 6 huerfanos; 5 son `.system`. |
| Claude skills externos | 30 | 28 mapeados, 2 huerfanos. |
| Claude agents externos | 13 | 7 mapeados, 6 huerfanos. |
| OpenClaw workspaces | 9 | 7 mapeados, 2 huerfanos (`fugaz`, `main`). |

Snapshot tras primera normalizacion:

| Area | Resultado |
|------|-----------|
| `docs/generated/recovery-inventory.*` | Generado por `python3 toolchain/kora recovery-inventory`; ahora distingue productivo de staging. |
| `tde` metadata | 55 archivos normalizados de `_manifest.provenance: <url>` a `_manifest.provenance.source`. |
| Gaps `provenance.source` | Bajaron de 56 a 0; `urn:salud:kb:me-body-of-knowledge-diferencial` conserva `sources` y ahora expone `provenance.source`. |
| Gate `tde` | `python3 toolchain/kora check --strict --path artifacts/knowledge/tde` paso 34/34. |
| `jobs-web-ux` | Ingerido y refinado en `_TALLER/INBOX/jobs-web-ux`; gate acotado paso 34/34. |
| `database-designer` | Ingerido y refinado en `_TALLER/INBOX/database-designer`; gate acotado paso 34/34. |
| `agent-architect` | Ingerido y refinado en `_FRAGUA/INBOX/agent-architect`; gate acotado paso 34/34. |
| `polymath` | Ingerido y refinado en `_FRAGUA/INBOX/polymath`; gate acotado paso 34/34. |
| `_FRAGUA/_archivo` | Ajustado el gate de construccion para no tratar archivos historicos como fuentes vigentes bajo `--path artifacts/agents`; test agregado. |

## Cola A — recuperacion agentica externa

| Prioridad | Item | Fuente | Decision |
|-----------|------|--------|----------|
| P0 | `jobs-web-ux` | `/home/felix/.codex/skills/jobs-web-ux/SKILL.md` y `/home/felix/.claude/skills/jobs-web-ux/SKILL.md` | Recuperar como skill KORA en REVIEW bajo namespace `dev`. |
| P1 | `database-designer` | `/home/felix/.claude/skills/database-designer/SKILL.md` | Recuperado como borrador `dev`; requiere decision de promocion y posible knowledge complementario. |
| P1 | `agent-architect` | `/home/felix/.claude/agents/agent-architect.md` | Ingerido como candidato `dev`; requiere verificacion viva de spec Claude antes de promocion. |
| P1 | `forjador-openclaw` | `/home/felix/.claude/agents/forjador-openclaw.md` | Rehacer desde specs KORA + knowledge OpenClaw vigente; no usar paths legacy `KNOWLEDGE/...`. |
| P2 | `ifml-architect` | `/home/felix/.claude/agents/ifml-architect.md` | Probable convergencia con `urn:kora:artefacto:ifml`; comparar antes de crear nuevo agente. |
| P2 | `opm-specialist` | `/home/felix/.claude/agents/opm-specialist.md` | Probable convergencia con `urn:kora:artefacto:modelamiento-opm`; comparar antes de crear nuevo agente. |
| P2 | `polymath` | `/home/felix/.claude/agents/polymath.md` | Candidato a persona/skill general; requiere decision de namespace y fuente. |
| P2 | `ux-research-design-ai` | `/home/felix/.claude/agents/ux-research-design-ai.md` | Probable convergencia con `urn:kora:artefacto:ux-design`; comparar antes de crear nuevo agente. |
| P3 | Codex `.system` skills | `/home/felix/.codex/skills/.system/*` | Excluir de KORA: son capacidades del runtime, no artefactos KORA. |

## Cola B — OpenClaw

| Prioridad | Workspace | Decision |
|-----------|-----------|----------|
| P0 | `main` | No ingerir `MEMORY.md` completo: contiene estado runtime, politicas de flota y datos locales sensibles. Extraer solo decisiones canonicas no sensibles hacia knowledge `ops` si faltan. |
| P0 | `fugaz` | No ingerir memoria completa: contiene datos personales/clinicos y continuidad runtime. Si se preserva, crear agente KORA fresco como clon operacional de `steipete` con memoria redactada. |
| P1 | workspaces mapeados | Tratar `SOUL.md`/`TOOLS.md`/`USER.md` como outputs runtime; solo recuperar deltas doctrinales si mejoran el IR KORA. |

Riesgos verificados por inventario OpenClaw:

- Memorias runtime de `steipete`, `fugaz`, `hospitalista`, `urgenciologo` y `main`
  contienen PII clinica, identificadores o resúmenes asistenciales; no se
  promueven crudas.
- Hay tokens Bearer, DSN/URLs con credenciales y Telegram IDs en material legacy
  bajo `reference/` y memorias runtime; cualquier ingesta debe ser redactada.
- `hospitalista` como workspace OpenClaw mapea al agente
  `urn:salud:artefacto:medico-hospitalista`, no a la skill
  `urn:salud:artefacto:hospitalista`.

## Cola C — knowledge desde fuentes originales

Orden de recuracion por valor/riesgo:

1. `tde`: metadata normalizada; siguiente paso es recurar contra Wikiguias/leyes
   oficiales si se requiere contenido, no solo frontmatter.
2. `salud`: alto uso por agentes clinicos; revisar fuente y PII antes de tocar.
3. `gn`: recurar desde `_SCRIPTORIUM/INBOX/gn/gorenuble_koda`.
4. `legal`: alto riesgo normativo; recurar desde fuentes oficiales.
5. `sii`: normalizar metadata desde `questions.json`/`documents.json`.
6. `fxsl`: separar SSOT primaria de consolidaciones OPM/IFML/GIST.
7. `agengai`, `ops`, `kora`, `korvo`, `pro`, `dev`: recurar solo por cambios
   operativos o gaps concretos.

Comandos por lote:

```bash
python3 toolchain/kora lint-md artifacts/knowledge/<namespace>
python3 toolchain/kora check --strict --path artifacts/knowledge/<namespace>
python3 toolchain/kora kb-graph --json --orphans
```

## Gates de cierre

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```
