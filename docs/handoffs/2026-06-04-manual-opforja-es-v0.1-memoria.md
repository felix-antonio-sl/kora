# Memoria: manual-opforja-es v0.1.0 — Sesión 2026-06-04

## Resumen

Sesión de consolidación post-publicación del corpus Forja. Se creó el manual operativo `manual-opforja-es` v0.1.0 como artefacto KORA productivo, se actualizó el README del corpus, y se regeneraron runtimes para `modelamiento-opm` v1.5.0 y `dov-dori` v1.2.0.

## Artefactos creados/modificados

### KORA (`/home/felix/kora`)

| Archivo | Cambio | URN |
|---|---|---|
| `artifacts/knowledge/fxsl/opm/opm-ssot-es/manual-opforja-es.md` | Nuevo (shard 1 de 2) | `urn:fxsl:kb:manual-opforja-es` |
| `artifacts/knowledge/fxsl/opm/opm-ssot-es/manual-opforja-es--p02.md` | Nuevo (shard 2 de 2) | `urn:fxsl:kb:manual-opforja-es-p02` |
| `artifacts/knowledge/fxsl/opm/opm-ssot-es/README.md` | Modificado: tabla familia Forja, precedencia, mapa de uso | — |

### Runtimes (sin repo git)

| Runtime | Artefacto | Estado |
|---|---|---|
| Claude Code | `~/.claude/agents/dov-dori.md` | Regenerado |
| Claude Code | `~/.claude/skills/modelamiento-opm/` | Regenerado |
| Codex | `~/.codex/skills/dov-dori/SKILL.md` | Regenerado |
| Codex | `~/.codex/skills/modelamiento-opm/` | Regenerado |
| OpenCode | `~/.config/opencode/agents/dov-dori.md` | Regenerado |
| OpenCode | `~/.config/opencode/skills/modelamiento-opm/` | Regenerado |

### OpenClaw fleet (`/home/felix/openclaw-fleet`)

| Workspace | Cambio |
|---|---|
| `dov-dori/` | Nuevo workspace |
| `allan-kelly/`, `fugaz/`, `gtd-integral/`, `salubrista/`, `steipete/` | `opm-modeler` → `modelamiento-opm` (skill reemplazada) |
| `main/skills/modelamiento-opm/` | Skill agregada |
| Varios workspaces | AGENTS.md, BOOT.md, IDENTITY.md regenerados |

## Decisiones

1. **Manual híbrido, no spec duplicada**: el manual enseña flujo y criterio; cita specs para autoridad; no reescribe reglas duras.
2. **Estabilidad por sección**: capítulos 0-2, 4-5, 6-7, 8 son estables (basados en corpus); capítulo 3 (UI) es vivo; capítulo 10 (ejemplo end-to-end) es reservado.
3. **Precedencia Forja asentada**: `reglas-opm-estrictas-es` como SSOT primaria prescriptiva; specs Forja como realizaciones modales; manual como orientación sin legislar.
4. **No se tocó `artifacts/knowledge/salud/ciberseguridad-minsal/`**: cambio no relacionado, permanece untracked.

## Validación

- `python3 toolchain/kora check --strict`: 34/34 OK
- `python3 toolchain/kora lint-md`: 0 issues
- `deploy-status`: `dov-dori` OK en 4 runtimes
- `deploy-status`: `modelamiento-opm` OK en 4 runtimes

## Pendientes

- Expandir capítulos 4 (construir modelo), 6-7 (cheatsheets OPD/OPL), 10 (ejemplo end-to-end)
- Sincronizar capítulo 3 con UI real de deep-opm-pro cuando el código se asiente
- Completar fichas de patrones (capítulo 9)
- `_BUILD/agentskills` regenerado pero no desplegado (agentskills está pausado)

## Commits esperados

1. **KORA**: `feat(knowledge): publicar manual-opforja-es v0.1.0 — manual operativo Forja`
2. **OpenClaw fleet**: `chore(fleet): regenerar modelamiento-opm v1.5.0 + dov-dori v1.2.0`
