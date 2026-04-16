# Auditoría de configuración y capacidades — Gateway hetzner2897261
**Fecha:** 2026-04-10 01:35 CLT (04:35 UTC)

## Resumen

| Capa | CRIT | WARN | INFO |
|------|------|------|------|
| Gateway | 0 | 0 | 0 |
| Telegram | 0 | 0 | 0 |
| Config | 0 | 3 | 2 |
| Seguridad | 0 | 3 | 1 |
| Agentes | 0 | 2 | 1 |

**Veredicto: PASS-CON-WARNINGS**

---

## Estado por agente

### main (Clawforge) ⚒️

| Dimensión | Estado |
|---|---|
| **Modelo** | `openai-codex/gpt-5.4` + fallbacks `minimax → opus → glm-5.1` |
| **Heartbeat** | ✅ 15min, 07:00–23:00 CLT |
| **Telegram** | ✅ default account, polling |
| **Sandbox** | `off` |
| **Tools** | Full: exec `security:full`, elevated `on`, `gateway`, `sessions_spawn` |
| **Skills** | ~15 compartidas (stack-auditor, config-patcher, operator, etc.) |
| **Workspace** | `~/.openclaw/workspace` — completo (AGENTS, SOUL, IDENTITY, USER, TOOLS, MEMORY, HEARTBEAT) |
| **Sesiones** | 11 activas |

### mente-omega (Korpensulo) Ω

| Dimensión | Estado |
|---|---|
| **Modelo** | hereda default `gpt-5.4` + fallbacks |
| **Heartbeat** | ✅ 30min, 07:00–22:00 CLT |
| **Telegram** | ✅ mente-omega account, polling |
| **Sandbox** | `off` (binds externos removidos 2026-04-08) |
| **Tools** | Restringido: **sin `exec`, `gateway`, `sessions_spawn`, `apply_patch`**. Sin elevated. |
| **Skills** | 11: academic-deep-research, analyst, arquitecto-categorico, intent-omega, marp-cli, pandas-skill, OPM, DB designers |
| **Workspace** | `workspace-mente-omega` — con symlinks a `hdos-app`, `hdos`, `normativa` |
| **Sesiones** | 11 |

### salubrista (Vector) 🏥

| Dimensión | Estado |
|---|---|
| **Modelo** | hereda default |
| **Heartbeat** | ✅ 30min, 07:00–22:00 CLT |
| **Telegram** | ✅ salubrista account, polling |
| **Sandbox** | hereda default (`off`) |
| **Tools** | Restringido: sin `exec`, `gateway`, `sessions_spawn`, `apply_patch`. Sin elevated. |
| **Skills** | 13: epi-analyst, epi-vigilance, hah-specialist, hospital-system-analyst, intent-hospitalization, intent-salubrista, network-analyst, OPM, product-builder, quality-auditor, report-builder, clarifier, implementation-planner |
| **Workspace** | `workspace-salubrista` — con symlink a `KNOWLEDGE`, `projects` |
| **Sesiones** | 4 |

### steipete ⚡

| Dimensión | Estado |
|---|---|
| **Modelo** | explícito `gpt-5.4` + fallbacks completos (`minimax → opus → glm-5.1`) |
| **Heartbeat** | ✅ 30min, 07:00–23:00 CLT |
| **Telegram** | ✅ steipete account, polling |
| **Sandbox** | hereda default (`off`) |
| **Tools** | **Full**: profile `coding`, exec `security:full`, elevated `on`, `gateway`, `sessions_spawn` |
| **Skills** | 24: blast-radius-estimator, brutal-loop-closure, context-hygiene, steinberg-* (7 skills propias), loop-closer, repo-architect, tooling-craftsman, triada, OPM, DB designers, frontend, architect |
| **Workspace** | `workspace-steipete` — con `artifacts`, `docs`, `reference`, `src` |
| **Sesiones** | 6 |
| **humanDelay** | `off` (responde inmediato) |

### gtd-integral (David) 🔭

| Dimensión | Estado |
|---|---|
| **Modelo** | hereda default |
| **Heartbeat** | ✅ 30min, 07:00–22:00 CLT |
| **Telegram** | ✅ gtd-integral account, polling |
| **Sandbox** | hereda default (`off`) |
| **Tools** | Restringido: sin `exec`, `gateway`, `sessions_spawn`, `apply_patch`. Sin elevated. |
| **Skills** | 11: capture-inbox, clarify-triage, delegation-governor, engage-decide, natural-planning, organize-buckets, regeneration, review-rhythm, state-recovery, vision-alignment, OPM |
| **Workspace** | `workspace-gtd-integral` — rico: `INBOX.md`, `NEXT_ACTIONS.md`, `PROJECTS.md`, `SOMEDAY_MAYBE.md`, `WAITING_FOR.md`, `REGULATION.md` |
| **Sesiones** | 3 |
| **Nota** | Heartbeat sin `prompt` explícito (hereda default del agent) |

### allan-kelly 🏗️

| Dimensión | Estado |
|---|---|
| **Modelo** | hereda default |
| **Heartbeat** | ✅ 60min, 08:00–21:00 CLT (ventana más estrecha) |
| **Telegram** | ✅ allan-kelly account, polling |
| **Sandbox** | hereda default (`off`) |
| **Tools** | Restringido: sin `exec`, `gateway`, `sessions_spawn`, `apply_patch`. Sin elevated. |
| **Skills** | 9: autonomy-envelope, cell-design, control-plane-review, debt-audit, eval-architecture, intent-contract, OPM, recalibration, triad-coordination |
| **Workspace** | `workspace-allan-kelly` — con `output`, `memory` |
| **Sesiones** | 3 |

### fugaz ⚡

| Dimensión | Estado |
|---|---|
| **Modelo** | explícito `gpt-5.4` + fallbacks completos |
| **Heartbeat** | ✅ 30min, 07:00–23:00 CLT |
| **Telegram** | ✅ fugaz account, polling |
| **Sandbox** | hereda default (`off`) |
| **Tools** | **Full**: profile `coding`, exec `security:full`, elevated `on`, `gateway`, `sessions_spawn` |
| **Skills** | 15: arquitecto-categorico, blast-radius-estimator, context-hygiene, DB designers, frontend, architect, legacy-continuity, loop-closer, OPM, repo-architect, tooling-craftsman, triad-coordination |
| **Workspace** | `workspace-fugaz` — con `docs`, `reference`, `reference-data` |
| **Sesiones** | 4 |
| **humanDelay** | `off` |

---

## Hallazgos

| # | Sev | Capa | Hallazgo | Acción |
|---|-----|------|----------|--------|
| 1 | WARN | Seguridad | `exec security=full` en 3 agentes (main, steipete, fugaz) | Migrar a `allowlist` cuando el workflow lo permita |
| 2 | WARN | Seguridad | `acpx.permissionMode=approve-all` | Desactivar cuando no se use ACP activamente |
| 3 | WARN | Seguridad | `trustedProxies` vacío | Configurar si se expone control UI vía reverse proxy |
| 4 | WARN | Config | `gtd-integral` heartbeat sin `prompt` propio | Hereda default genérico; debería tener `HEARTBEAT.md` propio |
| 5 | WARN | Config | Workspaces ACP vacíos (`claude`, `codex`, `gemini`, `opencode`) son scaffolds genéricos sin personalidad | Limpiar si no se usan como agentes reales |
| 6 | INFO | Config | `steipete` y `fugaz` son gemelos funcionales (mismo modelo, tools profile `coding`, mismo sandbox, skills casi idénticas) | Intencional para distribución de carga |
| 7 | INFO | Config | `mente-omega` tiene symlinks a `hdos-app` y `hdos` en su workspace | Verificar que sigue siendo necesario |
| 8 | INFO | Seguridad | Superficie de ataque: 0 groups abiertos, 1 allowlist, elevated habilitado para 3 agentes, browser control on | Consistente con modelo single-operator |

---

## Taxonomía de capacidades

| Agente | Rol | Poder | Skills | Observación |
|--------|-----|-------|--------|-------------|
| **Clawforge** | Operador del stack | 🔴 Full + elevated | 15 compartidas | SSOT del gateway |
| **steipete** | Ingeniero agentico productor | 🔴 Full + elevated | 24 (7 propias steinberg-*) | Motor de producción principal |
| **fugaz** | Ingeniero agentico productor | 🔴 Full + elevated | 15 | Gemelo de steipete para paralelismo |
| **mente-omega** | Arquitecto cognitivo / analista | 🟡 Medio (sin exec/spawn) | 11 | Sin capacidad de ejecución directa |
| **salubrista** | Copiloto sanitario | 🟡 Medio (sin exec/spawn) | 13 (domain-heavy) | Especializado HODOM |
| **gtd-integral** | Operador GTD / claridad | 🟡 Medio (sin exec/spawn) | 11 (GTD nativo) | Sistema integral de productividad |
| **allan-kelly** | Pensador producto/organización | 🟡 Medio (sin exec/spawn) | 9 (org-design) | Ventana heartbeat más estrecha |

---

## Config global relevante

- **OpenClaw:** 2026.4.5 (2026.4.7 disponible)
- **Node.js:** v24.x (`/usr/local/bin/node`)
- **Modelo default:** `openai-codex/gpt-5.4`
- **Fallbacks:** `minimax/MiniMax-M2.7` → `anthropic/claude-opus-4-6` → `zai/glm-5.1`
- **Compaction model:** `minimax/MiniMax-M2.7`
- **Subagent model:** `minimax/MiniMax-M2.7`
- **Memory search:** `openai/text-embedding-3-small` (1536d), hybrid (0.7 vector + 0.3 text), MMR enabled
- **Heartbeat default:** 15min, 07:00–23:00 CLT
- **Subagentes:** max 8 concurrentes, max depth 2, timeout 3600s
- **Sandbox default:** `off`

---

*Generado por Clawforge ⚒️ — 2026-04-10*
