---
_manifest:
  urn: "urn:kora:kb:handoff-2026-06-04-koraficacion-knowledge"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Cierre operativo solicitado por HITL: recuperar la capacidad legacy KODA de curacion/deshidratacion documental como skill KORA/MD nativa."
version: "1.0.0"
status: publicado
tags: [handoff, koraficacion, knowledge, kora-md, curacion, skills]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-06-04 - koraficacion knowledge

## Estado actual

KORA recupero la capacidad de transformar documentos humanos en artefactos de
conocimiento KORA/MD de alta fidelidad mediante la skill productiva
`koraficacion-knowledge`.

La capacidad se materializo como skill, no como agente: opera como metodo
portable sin memoria persistente ni workspace propio. El agente anfitrion puede
ser Claude Code, Codex, OpenCode u OpenClaw.

## Decision

No se reactivo YAML KODA, `atomize`, la familia retirada `atomic` ni el agente
legacy `agent_koda_transformer` como blueprint runtime.

Se absorbio solo el nucleo operacional probado del stack legacy:

- inventario `skeleton/meat/fat`.
- telegrafizacion como compresion semantica.
- deduplicacion SSOT.
- auditoria original vs salida.
- FS como obligacion de fidelidad.
- CR como dato observado, no como gate universal.

Despues de una correccion HITL posterior, la metrica de eficiencia quedo como
`IDC` (Indice de Deshidratacion Contextual):

```text
CR  = len(fuente) / len(salida)
IDC = CR observado / CR esperado para el perfil documental
```

Perfiles iniciales:

| Perfil | CR esperado |
| --- | ---: |
| `prosa-redundante` | 1.70 |
| `mixto` | 1.40 |
| `denso-estructurado` | 1.15 |
| `fuente-ya-densa` | 1.00 |

Lectura categorica aplicada:

- `DocHumano -> KORA/MD` debe comportarse como funtor fiel sobre hechos
  relevantes: preserva skeleton/meat y olvida solo fat declarado
  (`urn:fxsl:kb:icas-preservacion`).
- La auditoria original/salida es una heuristica tipo adjuncion, no garantia
  formal (`urn:fxsl:kb:icas-adjunciones`).

## Piezas Tocadas

Fuente productiva:

- `artifacts/skills/kora/koraficacion-knowledge/SKILL.md`
- `artifacts/skills/kora/koraficacion-knowledge/referencias/playbook-koraficacion.md`
- `artifacts/skills/kora/koraficacion-knowledge/referencias/auditoria-fidelidad.md`
- `artifacts/skills/kora/koraficacion-knowledge/referencias/legacy-koda-bridge.md`
- `artifacts/skills/kora/koraficacion-knowledge/scripts/audit_korafication.py`

Cobertura ejecutable:

- `tests/test_artifacts.py`

Memoria operativa:

- `docs/handoffs/2026-06-04-koraficacion-knowledge-memoria.md`

## Despliegue

La skill fue transmutada y desplegada a:

- Claude Code: `/home/felix/.claude/skills/koraficacion-knowledge/`
- Codex: `/home/felix/.codex/skills/koraficacion-knowledge/`
- OpenCode: `/home/felix/.config/opencode/skills/koraficacion-knowledge/`
- OpenClaw main: `/home/felix/openclaw-fleet/workspaces/main/skills/koraficacion-knowledge/`

Los `_BUILD/` generados son derivados e ignorados por git.

## Validacion ejecutada

- `python3 toolchain/kora host`: host primary `hetzner2897261`.
- `python3 toolchain/kora index`: 657 artefactos indexados.
- `python3 toolchain/kora lint-md docs/handoffs/2026-06-04-koraficacion-knowledge.md docs/handoffs/2026-06-04-koraficacion-knowledge-memoria.md artifacts/skills/kora/koraficacion-knowledge/SKILL.md artifacts/skills/kora/koraficacion-knowledge/referencias/playbook-koraficacion.md artifacts/skills/kora/koraficacion-knowledge/referencias/auditoria-fidelidad.md artifacts/skills/kora/koraficacion-knowledge/referencias/legacy-koda-bridge.md`: 0 issues.
- `python3 toolchain/kora check --strict --path artifacts/skills/kora/koraficacion-knowledge`: 34/34 OK.
- `python3 toolchain/kora check --strict --path docs/handoffs/2026-06-04-koraficacion-knowledge.md`: 34/34 OK.
- `python3 toolchain/kora check --strict --path docs/handoffs/2026-06-04-koraficacion-knowledge-memoria.md`: 34/34 OK.
- `python3 toolchain/kora transmute --target {claude-code,codex,opencode,openclaw} --agent kora/koraficacion-knowledge`: OK.
- `python3 toolchain/kora deploy-builds --skill kora/koraficacion-knowledge --target {claude-code,codex,opencode,openclaw} --openclaw-workspace main --apply --overwrite`: 4 outputs desplegados.
- `python3 toolchain/kora check --strict`: 34/34 OK.
- `python3 toolchain/kora validate --profile strict`: 16 workspaces validos, 0 invalidos.
- `python3 -m unittest tests.test_artifacts`: 47 tests OK.
- `python3 -m unittest discover -s tests`: 339 tests OK.
- `git diff --check`: OK.

## Riesgos y pendientes

- `audit_korafication.py` no prueba FS semantico completo; solo detecta
  perdidas mecanicas baratas. El cierre real exige ledger semantico.
- El clasificador automatico de perfil IDC es heuristico; puede requerir
  override manual con `--profile`.
- Si en el futuro se quiere monopolio de emision para una familia documental,
  corresponde ADR HITL y actualizacion de `knowledge-spec §9`. Este cierre no
  registra productor canonico.
