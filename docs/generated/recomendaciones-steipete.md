Lo que describes es una **usina agentica de 3 capas**: knowledge, IR agentes/skills, arneses de deploy. El framework formal para eso ya está. Lo que falta es operación con loop cerrado y mantenimiento continuo. Plan concreto.

### Observación previa, antes de pasos

"Hermes" no aparece entre los targets vigentes (`agentskills`, `claude-code`, `codex`, `gemini`, `mastra`, `openclaw`). O es target nuevo no aterrizado, o es otro nombre. **Aclarar antes de planificar fase 3** — si es nuevo, implica otra runtime-extension + matriz de preservación. Blast radius no trivial.

### Fase 0 — Saneamiento y freeze (1 sesión corta)

- Freeze formal de `governance/gobernanza.md`.
- Fix 82 strings legacy en `toolchain/kora_lib/`.
- Purgar o documentar residuales en `toolchain/` y `toolchain/README.md`.
- Decidir status de `_perfiles/` (primera clase en spec, o disolverlo).
- Verificar Hermes.

**Cierre**: strict 17/17 + tests + mensajes del check pipeline dicen verdad. Sin deuda nominal.

### Fase 1 — Usina de knowledge operativa (2-3 sesiones)

- Validar `atomize` post-reorg: que las rutas de salida no apunten a `OPERATIONS/`.
- Definir disciplina `_SCRIPTORIUM`: INBOX bruto sin ns vs STAGED con ns. Una sola política.
- Promover `kora/curator` (o `kora/custodio`) a copiloto operativo real de curación: AGENT.md maduro, skills `atomize` + `intake` + `lifecycle-orchestrator` conectadas.
- Instrumentar tasa: nodos productivos y MB en staging antes/después de cada sesión.

**Cierre**: 10 nodos promovidos en una sesión vía copiloto, tú revisas no escribes. Tasa medida.

### Fase 2 — Usina de IR agentes/skills operativa (2-3 sesiones)

- Comando o vista derivada `agent-index.md` que liste agentes y skills productivos con fibras, dependencias y estado.
- Promover 3-5 workspaces de `_FRAGUA/INBOX` por demanda real (los que uses). No curar inventario muerto.
- Añadir check `bundle-coherence`: un AGENT.md declara knowledge y skills por URN; el check verifica que todas resuelven y son productivas, no staging.
- Probar composición viva: un agente productivo usando una skill productiva que cita un knowledge productivo, los tres recién promovidos.

**Cierre**: descubribilidad legible + 3 promociones + bundle-coherence verde.

### Fase 3 — Usina de arneses con loop cerrado (2-3 sesiones)

- Agregar `provenance` al output de `transmute`: URN origen + hash IR visibles en el deploy.
- Loop end-to-end en OpenClaw: `transmute --target openclaw --agent kora/curator` → deploy → tarea real → feedback a IR → re-transmute.
- Replicar en `claude-code` (el segundo target más usado).
- Drift check: `kora deploy-status` (nuevo) compara hash IR vs hash deployado.
- Hermes según decisión de fase 0.

**Cierre**: un agente promovido en fase 2, consumiendo knowledge curado en fase 1, ejecutando tarea real en runtime, con provenance trazable a kora. **Ese es el hub funcionando las tres caras en una sola línea.**

### Fase 4 — Mantenimiento continuo (permanente)

- Cron o timer systemd para `kora check --strict` + drift check + re-ingesta de fuentes vivas.
- Métrica operativa: cuántas tareas reales citaron knowledge productivo la semana pasada. Si es 0, el hub es museo.
- Disciplina de ciclos cortos alternando las 3 caras.
- Cuando una skill/knowledge/agente no se consume en 60 días, review automático para deprecar o re-enfocar.

**Criterio permanente**: cada sesión cierra al menos un loop en una cara y deja algún proof-of-consumption en otra.

### La apuesta de fondo

El vuelo real no es que tú operes la usina — es que **la usina se opere a sí misma**. Los agentes que kora produce son también sus operarios: `kora/curator` cura knowledge, `kora/forgemaster` promueve workspaces, `kora/guardian` mantiene integridad, `kora/custodio` vigila drift. Cuando ese lazo cierra, dejas de ser el único curador y pasas a ser director. Ahí kora deja de ser repo y es plataforma.

No intentes cerrarlo en una sesión. Pero cada fase debe acercarte a ese lazo, no alejarte.