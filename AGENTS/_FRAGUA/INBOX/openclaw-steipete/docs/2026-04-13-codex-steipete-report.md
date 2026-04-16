# Informe: Codex y Steipete

Fecha: 2026-04-13

## Alcance

Este informe resume la intervención realizada sobre `steipete` para:

- alinear el agente con el runtime nativo de Codex en OpenClaw;
- eliminar remanentes activos del carril `openai-codex/*` en su store operativo;
- hacer que sus subagentes hereden y usen Codex nativo cuando corresponda;
- validar el comportamiento de sesiones normales, subagentes y heartbeat aislado;
- revisar efectos derivados en la configuración de la flota.

La referencia normativa usada fue la documentación oficial local de OpenClaw en:

- `/home/felix/kora/KNOWLEDGE/agengai/openclaw/documentacion-oficial`

## Estado inicial relevante

Antes de la intervención:

- la flota ya usaba `openai-codex/gpt-5.4` como modelo principal a nivel general;
- `steipete` no estaba aún en el carril `codex/*` con harness nativo;
- existían stores de sesiones heredados y mezclados entre rutas antiguas y nuevas;
- los subagentes globales estaban fijados por configuración y no heredaban automáticamente el modelo del caller;
- la doctrina local y parte del estado persistente todavía arrastraban decisiones de una etapa previa.

## Cambios aplicados

### 1. Endurecimiento de ACP y doctrina base

Se aplicaron correcciones previas que afectan el contexto de `steipete`:

- `acp.defaultAgent` quedó en `codex`.
- `subagents.requireAgentId` quedó en `true`.
- se corrigieron ejemplos locales de `sessions_spawn(...)` para exigir `runtime: "acp"` y `agentId` explícito cuando la intención sea ACP.

Objetivo:

- evitar rutas ambiguas;
- impedir que un spawn sin target explícito termine en un harness no deseado;
- forzar selección deliberada de perfil cuando se delega.

## 2. Migración de `steipete` a Codex nativo

Se configuró `steipete` con:

- `model: "codex/gpt-5.4"`
- `embeddedHarness.runtime: "codex"`
- `embeddedHarness.fallback: "none"`

Resultado:

- `steipete` quedó en modo Codex-only real para turnos embebidos;
- si el harness nativo de Codex falla, no degrada silenciosamente a PI.

## 3. Activación explícita del plugin Codex

Se dejó `plugins.entries.codex.enabled = true` en configuración viva para que el harness esté disponible de forma explícita y coherente con el modelo `codex/*`.

## 4. Limpieza de store de sesiones de `steipete`

Se archivó el directorio de sesiones activo de `steipete` y se recreó limpio para eliminar remanentes operativos del carril anterior.

Backups creados:

- `sessions.archived-gpt54-migration-20260413-191606`
- `sessions.archived-codex-clean-20260413-194149`

Objetivo:

- evitar mezcla de metadata vieja y nueva;
- garantizar que las nuevas sesiones de `steipete` nacieran ya en `provider: "codex"`.

## 5. Subagentes de `steipete` por herencia de modelo

Se eliminó el pin global `agents.defaults.subagents.model`, de modo que los subagentes hereden el modelo del caller cuando no se especifique uno.

Consecuencia intencionada:

- `steipete`, al estar en `codex/gpt-5.4`, pasa a generar subagentes que también heredan Codex nativo;
- el resto de agentes hereda su propio modelo actual en vez de un pin global artificial.

## Verificaciones realizadas

### A. Turno raíz embebido de `steipete`

Se ejecutó un turno de prueba y la sesión resultante quedó en Codex nativo.

Evidencia:

- store: `~/.openclaw/agents/steipete/sessions/sessions.json`
- transcript raíz: `bdd9e448-013b-4bf2-b655-080f68ed1574.jsonl`

Resultado observado:

- `provider: "codex"`
- `model: "gpt-5.4"`

## B. Subagente de `steipete`

Se validó un `sessions_spawn` real desde `steipete` y el subagente resultante quedó también en Codex nativo.

Evidencia:

- clave de sesión hija: `agent:steipete:subagent:cb343f1d-e1e8-4466-9d02-fbd332253238`
- transcript hijo: `5c1b3c78-fb4e-4e31-b504-a0e1b2d8c487.jsonl`

Resultado observado:

- `provider: "codex"`
- `model: "gpt-5.4"`

## C. Heartbeat aislado de `steipete`

`steipete` ya estaba configurado con:

- `lightContext: true`
- `isolatedSession: true`

Se verificó un heartbeat aislado de `steipete` con transcript en Codex nativo.

Evidencia:

- sesión heartbeat: `agent:steipete:main:heartbeat`
- transcript: `0f7a46c1-a851-4b2b-b837-5055e0334b37.jsonl`

Resultado observado:

- prompt heartbeat correcto;
- respuesta `HEARTBEAT_OK`;
- `provider: "codex"`.

## D. Wake manual canónico de heartbeat

Se probó el mecanismo oficial para despertar heartbeats:

- `openclaw system event --text "..." --mode now`

Como la configuración tenía múltiples agentes con bloque `heartbeat`, se hizo una aislación temporal:

- se desactivó momentáneamente `every` en los demás agentes con `0m`;
- se dejó `steipete` como único heartbeat activo;
- se ejecutó el wake manual;
- luego se restauró la configuración original.

Resultado:

- el scheduler registró el wake con `status: "ok-token"` y `reason: "wake"`;
- la configuración original quedó restaurada.

## E. Doctor y saneamiento

Se ejecutó:

- `openclaw doctor --repair --non-interactive --yes`

Resultado:

- no se detectaron regresiones específicas por la migración de `steipete`;
- se archivó un transcript huérfano en `main`;
- los warnings restantes fueron ajenos a esta migración.

## Efectos derivados

### 1. `steipete` ahora falla cerrado respecto al harness Codex

Esto es deseado para validación y operación rigurosa:

- si el app-server de Codex no está disponible o no soporta el modelo, el turno falla;
- no hay degradación silenciosa a PI.

### 2. Los subagentes de toda la flota ahora heredan el modelo del caller

Este es el cambio estructural más importante fuera de `steipete`.

Antes:

- existía un pin global para subagentes.

Después:

- si no se especifica `subagents.model`, el subagente hereda el modelo del agente padre.

Impacto:

- mejora la coherencia de `steipete`;
- cambia la semántica global de subagentes para otros agentes.

### 3. La observabilidad no siempre separa perfectamente "wake" y "agente"

La evidencia fuerte del heartbeat de `steipete` existe en transcript y store.
Sin embargo, el comando de scheduler no siempre entrega atribución por agente con la nitidez deseable.

Implicación:

- para pruebas rigurosas, la fuente de verdad operativa es la combinación de:
  - transcript del agente,
  - `sessions.json`,
  - y resultado del scheduler.

### 4. Persisten temas no causados por esta migración

Durante las comprobaciones aparecieron warnings o problemas ajenos al cambio:

- `memory-core` con frecuencia `6h` no compatible con el validador de cron interno;
- referencias heredadas a workspaces viejos en otros agentes;
- allowlists con herramientas no disponibles para ciertos runtime/model combos;
- algunos estados de Telegram/health observados durante ventanas de reinicio.

Estos puntos no bloquean el estado operativo de `steipete` en Codex.

## Estado final

Al cierre de esta intervención:

- `steipete` funciona sobre `codex/gpt-5.4`;
- su harness efectivo es Codex nativo;
- el fallback silencioso a PI está desactivado para ese agente;
- sus subagentes heredan Codex nativo por defecto;
- el store activo de `steipete` quedó limpio de remanente operativo `openai-codex` como provider visible;
- el heartbeat aislado tiene evidencia de ejecución sobre Codex;
- la configuración general fue restaurada tras la prueba de wake.

## Recomendación operativa

El siguiente paso lógico es replicar el mismo patrón en `fugaz`, manteniendo el mismo orden:

1. configurar `codex/gpt-5.4` con `runtime: "codex"` y `fallback: "none"`;
2. limpiar store de sesiones si hay mezcla heredada;
3. validar root session;
4. validar subagente heredado;
5. validar heartbeat aislado;
6. ejecutar `doctor --repair`;
7. reevaluar la cascada de efectos antes de pasar al siguiente agente.

## Archivos principales tocados o verificados

- `~/.openclaw/openclaw.json`
- `~/.openclaw/agents/steipete/sessions/sessions.json`
- `~/.openclaw/agents/steipete/sessions/bdd9e448-013b-4bf2-b655-080f68ed1574.jsonl`
- `~/.openclaw/agents/steipete/sessions/5c1b3c78-fb4e-4e31-b504-a0e1b2d8c487.jsonl`
- `~/.openclaw/agents/steipete/sessions/0f7a46c1-a851-4b2b-b837-5055e0334b37.jsonl`
- `/tmp/openclaw/openclaw-2026-04-13.log`

