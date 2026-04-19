# Plan operativo — Usina agentica kora

**Fecha**: 2026-04-19
**Autor**: steipete (auditoria inicial + plan)
**Horizonte**: 4 fases, ~10-12 sesiones efectivas
**Premisa de cierre**: un agente promovido, citando knowledge productivo recien curado, ejecutando tarea real en runtime vivo, trazable al hash IR en kora. Sin ese loop, todo lo demas es teatro.

## Contexto

kora es usina agentica de 3 caras operando sobre el mismo filesystem:

1. **Hub de knowledge** — corpus curado que agentes consumen.
2. **Hub de IR de agentes/skills** — modelo intermedio agnostico, source of truth.
3. **Hub de arneses** — composicion + transmute a runtimes (claude-code, codex, gemini, openclaw, mastra, agentskills; hermes por confirmar).

Auditoria inicial: strict 17/17 verde, 302 tests OK, 525 nodos KB sin huerfanos. Deuda nominal relevante: 82 strings legacy en toolchain, pseudo-churn diario en docs/generated, 221 MB en `_SCRIPTORIUM/INBOX`, toolchain/ con one-shots residuales, `_perfiles/` sin status ontologico claro.

## Fase 0 — Saneamiento y freeze

**Objetivo**: eliminar deuda nominal y congelar el framework antes de producir.

| # | Tarea | Comando / criterio cierre |
|---|-------|---------------------------|
| 0.1 | Freeze formal | Seccion "freeze activo" en `governance/gobernanza.md` con alcance: no modificar harness-spec, autoria-spec, transmutation-spec hasta cerrar fase 3 |
| 0.2 | Fix strings legacy | Find/replace en `toolchain/kora_lib/*.py`: `KNOWLEDGE/`→`artifacts/knowledge/`, `SKILLS/`→`artifacts/skills/`, `AGENTS/`→`artifacts/agents/`, `scripts/kora`→`toolchain/kora`. Tests verdes + strict 17/17 |
| 0.3 | Purgar toolchain/ | Mover one-shots (`kora_transmuter.py`, `source_mapper.py`, `check_counts.py`, `generate_hodom_template.py`, `telegraph_audit_repair.py`, `koraficate_sii_faq.py`, `migrate_coalgebra.py`) a `toolchain/legacy_migration/`. Reescribir `toolchain/README.md` en 15 lineas honestas o borrarlo |
| 0.4 | Decidir _perfiles | Opcion A: elevar a regimen formal en `autoria-spec`. Opcion B: mover a `_FRAGUA/INBOX/` como drafts. Decision explicita, no codigo |
| 0.5 | Clarificar Hermes | Confirmar si es runtime target nuevo o alias. Si es nuevo: ticket aparte, fuera de fase 3 |
| 0.6 | Desdeterminizar sync-docs | Quitar `Fecha:` variable del output, o mover 3 archivos drift-diario a `.gitignore` con CI |

**Duracion estimada**: 1 sesion.
**Blast radius**: bajo. Todo reversible.
**Cierre binario**: commit atomico + strict verde + git status limpio al dia siguiente sin regenerar.

---

## Fase 1 — Usina de knowledge operativa

**Objetivo**: pipeline `_SCRIPTORIUM/INBOX/` → productivo con throughput medido y copiloto agente.

| # | Tarea | Criterio cierre |
|---|-------|-----------------|
| 1.1 | Validar `atomize` | `python3 toolchain/kora atomize --help` + corrida seca contra 1 doc de `_SCRIPTORIUM/INBOX/`. Output no apunta a `OPERATIONS/` |
| 1.2 | Disciplinar `_SCRIPTORIUM` | Una politica: INBOX bruto sin ns, STAGED por ns. Documentar en `serialization/knowledge-spec.md`. Migrar contenido actual a la forma elegida |
| 1.3 | Promover `kora/curator` a copiloto | AGENT.md maduro con skills `atomize`, `intake`, `lifecycle-orchestrator` referenciadas. Transmute a claude-code o OpenClaw, probar con 1 doc real |
| 1.4 | Instrumentar tasa | Script de 20 lineas que imprime: nodos KB productivos, MB en `_SCRIPTORIUM`, skills productivas, agentes productivos. Guardar snapshot pre/post sesion |

**Duracion estimada**: 2 sesiones.
**Cierre binario**: 10 nodos knowledge promovidos via copiloto en una sesion, humano revisa no escribe. Tasa ≥ 5 nodos/hora.

---

## Fase 2 — Usina de IR agentes/skills

**Objetivo**: descubribilidad, promocion por demanda, composicion viva verificable.

| # | Tarea | Criterio cierre |
|---|-------|-----------------|
| 2.1 | Comando/vista de catalogo | `python3 toolchain/kora agents --list --with-deps` o `docs/generated/agent-index.md` legible: nombre, URN, hash, skills usadas, knowledge citado, runtime targets soportados |
| 2.2 | Promover 3-5 workspaces | Por demanda real, desde `_FRAGUA/INBOX`. Candidatos: `polymath`, `opm-specialist`, `salubrista`, `steipete`, `forjador-openclaw`. No inventario muerto |
| 2.3 | Check `bundle-coherence` | Nuevo check: AGENT.md declara deps `knowledge:` y `skills:` por URN; el check verifica existencia + productivo (no staging). Sumar al strict |
| 2.4 | Test de composicion viva | Un agente promovido usando una skill promovida que cita un knowledge promovido. Los tres transitaron staging → productivo en fases 1-2 |

**Duracion estimada**: 2-3 sesiones.
**Cierre binario**: catalogo legible + 3 promociones + bundle-coherence verde + composicion viva probada.

---

## Fase 3 — Usina de arneses con loop cerrado

**Objetivo**: deploy trazable con provenance + loop feedback runtime ↔ IR.

| # | Tarea | Criterio cierre |
|---|-------|-----------------|
| 3.1 | Provenance en transmute | Output de `transmute` incluye `provenance.urn` + `provenance.hash` + `provenance.timestamp`. Backport a los 6 targets vigentes |
| 3.2 | Loop end-to-end OpenClaw | Transmute `kora/curator` → deploy `~/openclaw-fleet/workspaces/curator/` → tarea real por Telegram → feedback a IR kora → re-transmute → re-deploy |
| 3.3 | Replicar en Claude Code | Mismo loop, target `claude-code`, deploy a `~/.claude/agents/` |
| 3.4 | Drift check | `kora deploy-status` compara hash IR vs hash deployado en runtimes locales conocidos. Reporta stales |

**Duracion estimada**: 2-3 sesiones.
**Cierre binario**: `kora/curator` ejecuta 3 tareas reales en OpenClaw citando knowledge curado en fase 1, con provenance visible. Repetir en claude-code. Drift check detecta un deploy stale intencionalmente introducido.

---

## Fase 4 — Mantenimiento continuo (permanente)

**Regimen post-cierre.** No es una fase que termina; es la condicion de vida del hub.

- **Timer systemd user-level**: `kora check --strict` + `kora deploy-status` diario. Notifica si falla.
- **Metrica semanal operativa**: cuantas tareas reales citaron knowledge productivo. Si es 0, investigar antes de curar mas.
- **Ciclos alternantes**: medio dia knowledge, medio dia agentes. Nunca mas de 2 sesiones consecutivas en la misma cara.
- **Deprecacion proactiva**: si un artefacto productivo no se consume en 60 dias, review para deprecar, reenfocar o absorber.
- **Freeze se levanta** solo despues de fase 3 cerrada y con criterio explicito de que gap no cubierto justifica la proxima ola.

---

## Riesgos y reglas de parada

- **Si fase 0.2 introduce regresiones en tests**, parar y revisar: los strings legacy pueden estar cubriendo contratos reales. Investigar antes de persistir el fix.
- **Si el copiloto de curacion aluciona manifiestos en fase 1.3**, no escalar a volumen. Volver a reforzar la skill `intake` o `atomize`.
- **Si el provenance de transmute rompe runtimes existentes** (fase 3.1), aislarlo tras flag y probar por target antes de unificar.
- **Si al terminar fase 3 ningun agente deployado consume knowledge productivo espontaneamente**, el problema es de diseno del puente de consumo, no de volumen. Pausar fases y redisenar.

---

## Apuesta de fondo

El vuelo real no es que el humano opere la usina — es que **la usina se opere a si misma**. Los agentes que kora produce son tambien sus operarios: `kora/curator` cura knowledge, `kora/forgemaster` promueve workspaces, `kora/guardian` mantiene integridad, `kora/custodio` vigila drift. Cuando ese lazo cierra, el humano deja de ser el unico curador y pasa a ser director. Ahi kora deja de ser repo y es plataforma.

No intentar cerrarlo en una sesion. Pero cada fase debe acercar a ese lazo, no alejar.

---

## Orden de arranque inmediato

1. Leer este plan.
2. Confirmar/ajustar fase 0 en 5 minutos.
3. Abrir sesion dedicada a fase 0 completa. No mezclar con fase 1.
