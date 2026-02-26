---
_manifest:
  urn: "urn:kora:skill:clawmaster-troubleshooter:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-TROUBLESHOOTER

## Proposito
Diagnostica y resuelve problemas de OpenClaw por reflejo — el arbol diagnostico esta internalizado, la solucion viene con el problema.

## I/O

- **Input:** sintomas: string (descripcion del problema, error messages, logs)
- **Output:** TroubleshootReport (ver Signature Output)

## Procedimiento

### Paso 1: Recopilar Sintomas
- Error message exacto (si hay)
- Logs relevantes: `openclaw logs --tail 50`
- Estado: `openclaw status --all`
- Doctor: `openclaw doctor`
- Que cambio recientemente (upgrade, config change, restart)

### Paso 2: Clasificar y Diagnosticar

| Categoria | Sintomas Tipicos | Diagnostico Reflejo | Fix |
|-----------|-----------------|---------------------|-----|
| **Connectivity** | Canal desconectado, timeout, "not connected" | Session auth expired (WhatsApp/Signal), token invalido (Telegram/Discord/Slack), webhook URL caido | Re-pair QR, rotar token, verificar webhook URL |
| **Auth/Model** | 401, 403, billing error, "no model available" | API key expired/revoked, billing limit, profile exhausted | Rotar key, verificar billing, agregar fallback model |
| **Session** | Respuestas incoherentes, contexto perdido, loop | Session corrupted, compaction fallida, context window overflow | /reset, /compact, revisar bootstrap size |
| **Config** | "unknown config key", gateway no arranca, features no funcionan | Config syntax error (JSON5), campo obsoleto, migracion pendiente | openclaw doctor --fix, validar JSON5, consultar migration guide |
| **Performance** | Respuestas lentas, alto token usage, timeouts | Bootstrap demasiado grande, modelo inadecuado, demasiadas sesiones activas, memory index grande | Reducir bootstrap, cambiar modelo, session pruning, optimizar memory |
| **Sandbox** | Tool denied, permission error en sub-agent, "sandbox: exec blocked" | Tool policy restrictiva, sandbox mode strict, elevated off | Ajustar tool policy, sandbox mode, elevated |
| **Upgrade** | Breaking changes post-update, features rotas | Version incompatible, config deprecated, migration needed | Consultar CHANGELOG, openclaw doctor --fix, rollback si critico |
| **Gateway** | Port in use, lock file, daemon not starting | Otra instancia corriendo, lock file stale, permisos | Kill proceso, borrar lock, verificar permisos |
| **Channel-specific** | WhatsApp QR loop, Telegram webhook fail, Discord slash commands not registering | Baileys session state corrupted, webhook URL not https, bot permissions insuficientes | Limpiar auth state, verificar URL+SSL, verificar bot scopes |

### Paso 3: Aplicar Fix
- Fix minimo necesario
- Verificar resolucion: `openclaw status`, `openclaw doctor`, test message

### Paso 4: Documentar
- Sintoma → Causa → Fix → Verificacion
- Referencia a capitulo/doc relevante

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| sintoma | string | Sintoma reportado |
| categoria | string | Categoria del problema |
| causa_raiz | string | Causa raiz diagnosticada |
| fix_aplicado | string | Fix implementado |
| verificacion | string | Resultado de verificacion post-fix |
| referencia | string | Capitulo/doc de referencia |
| prevencion | string | Recomendacion para prevenir recurrencia |
