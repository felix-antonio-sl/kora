---
_manifest:
  urn: "urn:kora:kb:handoff-2026-06-11-dov-dori-dual-mode-realineacion"
  provenance:
    created_by: "Claude"
    created_at: "2026-06-11"
    source: "Sesion 2026-06-10: investigacion de configuracion dov-dori x modelamiento-opm, cierre de deuda 1 (drift de version v1.5.1->v1.8.0) y deuda 2 (forma persona no materializada -> doctrina dual-mode). Claude Fable 5 sobre repo kora, host primary."
  version: "1.0.0"
  status: publicado
  tags: [handoff, dov-dori, modelamiento-opm, dual-mode, runtime-extension, claude-code, transmutacion]
  lang: es
extensions:
  kora:
    family: note
---

# Handoff — dov-dori dual-mode + realineacion con modelamiento-opm (2026-06-11)

## Estado actual

Las dos deudas detectadas por la investigacion de configuracion
dov-dori x modelamiento-opm estan **cerradas**. Todo pusheado a
`origin/master` (master == origin, working tree limpio):

| Commit | Que |
|--------|-----|
| `17f8c43` | `dov-dori` v1.3.0 — re-alineacion con `modelamiento-opm` vigente (v1.6.0–v1.8.0): desanclaje de version en prosa (9 sitios fijaban v1.5.1), cierre visual obligatorio (`revisar-visual`), camino primario con sello (M2), anclas normativa/meta + W6.0, `generic-view` ≠ refinamiento |
| `6440e408` | `claude-code-runtime-extension` v1.2.0 (§2.1 dual-mode) + `dov-dori` v1.4.0 (doctrina de modos + auto-conciencia) |

Gates al cierre: `check --strict` **37/37** (x2), suite **383 OK** (x2).
Re-transmutado a 4 targets y re-deployado via `kora deploy-builds --apply
--overwrite` a claude-code, codex y opencode (hash de procedencia verificado).
openclaw solo `_BUILD` (sin deploy vivo: dov-dori no es bot de la fleet).

## Decisiones

1. **Dictamen de configuracion** (origen de la sesion): para crear modelos OPM
   desde un dominio, la mejor configuracion es **Dori encarnado como persona en
   el hilo principal invocando el la skill** — unica donde "Dori conduce →
   skill ejecuta → operador valida" se materializa sin perdida. Evidencia: la
   skill es HITL-dialectica (estado `aclarar` bloquea esperando al operador);
   el subagente no tiene Skill tool ni Bash **por diseno**; el vector Μ=2
   deriva modo persona (runtime-extension §4.1). Subagente = solo dictamenes
   batch; skill sola = mecanica acotada.
2. **Desanclaje de version en prosa normativa**: el pinning "v1.5.1" en 9
   sitios del AGENT.md era la causa raiz del drift. La referencia canonica
   entre artefactos es el URN sin version embebida (mismo principio que
   `autoria-spec` manda para `_manifest.urn`); la alineacion puntual se declara
   en `provenance.update_reason`.
3. **Dual-mode sin segunda forma material**: la deuda "forma persona no
   materializada" se cerro precisando la spec, no extendiendo la toolchain.
   `T_{claude-code}` emite UN artefacto que sirve dos modos: subagente Task
   (registro nativo) y fuente de encarnacion (persona del hilo principal).
   Las perdidas se declaran **por modo de invocacion**, no por forma emitida.
4. **DEBERIA, no DEBE**, para la doctrina de modos en el body de agentes
   persona: evita retro-obligacion inmediata sobre `steipete` y `allan-kelly`
   (mismo arnes, mismo riesgo latente) sin un check que lo enforce.
5. **Excepcion consciente a la politica de handoffs** (1/semana, ya existia el
   del 2026-06-09): este handoff se emite por instruccion directa del operador
   y documenta dos decisiones de infraestructura (spec v1.2.0 + patron de
   desanclaje).

## Artefactos relevantes

- Agente: `artifacts/agents/fxsl/dov-dori/AGENT.md` (v1.4.0) — seccion nueva
  "Modos de Invocacion (dual-mode)" + regla dura de auto-conciencia de modo.
- Spec runtime: `runtime/claude-code-runtime-extension.md` (v1.2.0) — §2.1
  "Realizacion del modo persona (dual-mode)", §7 fila Conversacion persona.
- Proyecciones: `artifacts/agents/fxsl/dov-dori/_BUILD/{claude-code,codex,opencode,openclaw}/`
  (gitignored) con `_transmutation.yml` `source_version: 1.4.0`.
- Deploys vivos: `~/.claude/agents/dov-dori.md`, `~/.codex/skills/dov-dori/`,
  `~/.config/opencode/agents/dov-dori.md`.
- Contraparte skill: `artifacts/skills/kora/modelamiento-opm/SKILL.md` v1.8.0
  (commits `eb92c5c` + `2320bca`, sesion hermana del 2026-06-10).

## Pendientes

- **Opcional, no bloqueante**: anadir la doctrina dual-mode al body de
  `steipete` y `allan-kelly` cuando se toquen por otra razon (la regla DEBERIA
  de la extension v1.2.0 ya los cubre normativamente).
- Ninguna deuda abierta de esta linea.

## Supuestos

- `modelamiento-opm` v1.8.0 es la vigente; el desanclaje hace que bumps futuros
  de la skill NO exijan tocar a Dori salvo cambio de contrato semantico
  (handoff, especies de ancla, estados nuevos que Dori deba exigir).
- `kora deploy-builds` es el camino canonico de deploy (no `cp` manual).
- Claude Code lee `~/.claude/agents/` solo al iniciar sesion (runtime-extension
  §12.1): el dov-dori v1.4.0 deployado aplica en sesiones nuevas.

## Riesgos

- **Drift de contrato** (no de version): si la skill cambia la semantica del
  handoff (p. ej. nueva especie de ancla, nuevo estado obligatorio), Dori debe
  absorberlo conceptualmente; el desanclaje elimina el sintoma de version pero
  no sustituye la revision de contrato. Senal: update_reason de la skill.
- **Encarnacion no enforzada**: el modo persona depende de que el operador (o
  un prompt de arranque) cargue las instrucciones; no hay mecanismo runtime que
  lo haga automatico. Mitigacion: la auto-conciencia de modo hace que el
  subagente devuelva handoff en vez de fingir la sesion.

## Prompt de continuacion

> El frente dov-dori x modelamiento-opm esta cerrado (ver
> `docs/handoffs/2026-06-11-dov-dori-dual-mode-realineacion.md`). Para modelar
> OPM desde un dominio: encarnar a dov-dori en el hilo principal
> (`~/.claude/agents/dov-dori.md`) y dejar que el invoque la skill
> `modelamiento-opm`; despachar el subagente dov-dori solo para dictamenes
> batch. Si se retoma: verificar version vigente de la skill
> (`artifacts/skills/kora/modelamiento-opm/SKILL.md`) y revisar si su
> update_reason introduce cambios de contrato que Dori deba absorber. Mejora
> opcional pendiente: doctrina dual-mode en steipete/allan-kelly. Antes de
> editar: `check --strict` + suite. Commits selectivos.
