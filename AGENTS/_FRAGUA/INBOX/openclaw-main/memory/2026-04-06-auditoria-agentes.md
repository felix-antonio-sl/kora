# Auditoría de agentes — 2026-04-06

**Host:** hetzner2897261  
**Gateway:** OpenClaw 2026.4.5  
**Canal:** Telegram 6/6 OK  
**Estado general:** PASS-CON-WARNINGS

## Resumen global

| Capa | Estado | Evidencia |
|---|---|---|
| Host | OK | `openclaw status --deep` → gateway reachable, node 24.13.1 |
| Gateway | OK | `openclaw health --json` → `ok: true` |
| Canales | OK | Telegram 6/6 probes OK |
| Seguridad | WARN | `openclaw security audit --deep` |
| Skills | OK | `openclaw skills list --eligible` → 33/33 ready |
| Heartbeats | WARN | `mente-omega` sigue disabled |
| Sesiones | WARN | `steipete` con sesión larga y árbol sucio observado |

## Hallazgos globales

| Sev | Capa | Hallazgo | Evidencia | Acción |
|---|---|---|---|---|
| WARN | Seguridad | `gateway.trustedProxies` vacío | `openclaw security audit --deep` | Mantener UI local-only o configurar proxies confiables |
| WARN | Seguridad | `plugins.entries.acpx.config.permissionMode=approve-all` | `openclaw security audit --deep` | Mantener solo si el gateway sigue bajo boundary personal/trusted |
| WARN | Seguridad | `exec.security=full` en `main` y `steipete` | `openclaw security audit --deep` | Aceptado por ahora; son los 2 agentes break-glass |
| WARN | Operación | `mente-omega` sigue sin heartbeat | `openclaw status --deep` | Activar heartbeat 30m, según decisión operativa ya tomada |
| WARN | Operación | `steipete` mostró sobre-iteración en sesión larga | `sessions_history`, `session_status`, repo dirty | Cerrar/reconducir sesión y limpiar árbol |

---

## main (Clawforge)

**Veredicto:** VERDE

| Área | Estado |
|---|---|
| Runtime | OK |
| Heartbeat | 15m activo |
| Seguridad | `exec=full`, aceptado |
| Memoria | 17 archivos, ~93 KB |
| Bootstrap | sólido |
| Skills | completas |

**Notas:**
- Sigue siendo el único control-plane amplio correcto.
- Cron `Session cleanup diario` hoy aparece `ok` en `openclaw cron list`.
- Sesión principal usa `gpt-5.4` con alto cache hit.

## mente-omega

**Veredicto:** WARN

| Área | Estado |
|---|---|
| Runtime | OK |
| Heartbeat | **disabled** |
| Seguridad | mejorado, sin `exec=full` |
| Memoria | 9 archivos, ~48 KB |
| TOOLS.md | muy corto/genérico |
| Skills | presentes |

**Hallazgos:**
- La decisión operativa era llevar heartbeat 30m, pero aún no quedó aplicada en runtime.
- Sigue siendo usable, pero le falta pulso periódico y TOOLS más explícito.

## salubrista

**Veredicto:** VERDE-CON-WARN

| Área | Estado |
|---|---|
| Runtime | OK |
| Heartbeat | 30m activo |
| Seguridad | sin `exec=full` |
| Memoria | **0 archivos en `memory/`** |
| Bootstrap | mejorado |
| Skills | dominio presentes |

**Hallazgos:**
- Gran mejora respecto a baseline: heartbeat real, menos privilegio.
- Sigue débil en memoria operativa diaria: `memory/` vacío.

## steipete

**Veredicto:** WARN

| Área | Estado |
|---|---|
| Runtime | OK |
| Heartbeat | 30m activo |
| Seguridad | `exec=full`, aceptado |
| Memoria | 20 archivos, ~119 KB |
| Skills | fuertes; `arquitecto-categorico` ya instalado y elegible |
| Sesiones | actividad alta |

**Hallazgos:**
- No estaba caído: estaba enganchado en sesión larga.
- Se observó lock vivo, queue `collect`, y working tree sucio en `/home/felix/projects/opmodel`.
- Hubo commits útiles, pero después siguió iterando más de la cuenta.

**Acción sugerida:**
- cerrar/resumir la sesión activa y limpiar el repo antes de una nueva línea de trabajo.

## gtd-integral

**Veredicto:** VERDE-CON-WARN

| Área | Estado |
|---|---|
| Runtime | OK |
| Heartbeat | 30m activo |
| Seguridad | drift principal corregido |
| Bootstrap | ahora sí tiene `BOOTSTRAP.md` |
| Memoria | 0 archivos en `memory/` |
| Uso | bajo |

**Hallazgos:**
- El problema crítico de drift ya no aparece.
- Sigue flojo en material operativo vivo, porque `memory/` está vacío.
- Es funcional, pero aún no productivo.

## allan-kelly

**Veredicto:** VERDE-CON-WARN

| Área | Estado |
|---|---|
| Runtime | OK |
| Heartbeat | 60m activo |
| Seguridad | sin `exec=full` |
| Memoria | 3 archivos, ~11 KB |
| Bootstrap | bueno |
| Uso | bajo |

**Hallazgos:**
- Quedó bastante ordenado.
- Sigue con memoria muy liviana y uso bajo, pero no hay drift visible.

---

## Priorización operativa siguiente

1. **Activar heartbeat 30m en `mente-omega`**.
2. **Cerrar/reconducir sesión activa de `steipete` y limpiar árbol en `opmodel`**.
3. **Dar señal/memoria viva a `salubrista` y `gtd-integral`**.
4. Luego sí: dreaming, cache tuning y mejoras 2026.4.5.
