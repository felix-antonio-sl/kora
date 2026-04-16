# Análisis de Riesgo: Actualización OpenClaw 2026.2.26

*Timestamp: 2026-02-27T00:55Z*
*Analista: Korax*
*Sesión afectada: agent:main:telegram:direct:7192195698*

---

## Resumen Ejecutivo

| Aspecto | Valoración |
|---------|------------|
| **Riesgo general** | MEDIO-ALTO |
| **Sesiones activas** | 1 (la nuestra) |
| **Subagentes activos** | 0 |
| **Cambios críticos** | 2 (ACP/Threads, Codex/WebSocket) |
| **Rollback disponible** | Sí (backup en ~/.npm-global) |

---

## Cambios de Alto Impacto

### 1. ACP/Thread-bound Agents (Riesgo: ALTO)

**Cambio:** Los agentes ACP ahora son runtimes first-class para sesiones thread-bound.

**Impacto:**
- `sessions_spawn` con `runtime="acp"` ahora integra con backend acpx
- Lifecycle controls nuevos (startup reconciliation, runtime cleanup)
- Coalesced thread replies (puede cambiar comportamiento de respuestas)

**Estado actual:**
- Tenemos configurado `openai-codex:default` en auth profiles
- Fallback chain incluye `openai-codex/gpt-5.2`
- Sin subagentes ACP activos al momento del upgrade

**Riesgo concreto:**
- Si hay código usando `sessions_spawn` con ACP, el comportamiento de threading cambia
- Posible degradación si el bridge acpx falla

**Mitigación:**
- ✅ No hay subagentes activos
- ✅ Nuestra sesión principal usa modelo kimi (no ACP)
- ⚠️ Monitorear próximos spawns con ACP

---

### 2. Codex/WebSocket Transport (Riesgo: MEDIO-ALTO)

**Cambio:** Transporte por defecto cambia de SSE a WebSocket (`transport: "auto"` con fallback SSE).

**Impacto:**
- Conexiones a OpenAI Codex ahora intentan WebSocket primero
- Fallback automático a SSE si WebSocket falla
- Latencia potencialmente menor, pero nuevo código de conexión

**Estado actual:**
- Tenemos `openai-codex:default` en auth profiles
- Codex está en fallback chain: `gpt-5.2`, `kimi`, `glm5`
- Configuración actual no especifica transport override

**Riesgo concreto:**
- Primera conexión Codex post-upgrade podría fallar o tener latencia extra
- Si WebSocket tiene problemas, el fallback a SSE puede causar delay perceptible
- Provider directo `minimax-portal` tiene trial vencido (2026-02-26) — ya migrado a Kilo

**Mitigación:**
- ✅ Tenemos fallback chain robusta (kimi, glm5)
- ⚠️ Si Codex falla, el sistema debería fallback a kimi automáticamente
- ⚠️ Monitorear `/status` o primer uso de Codex

---

## Cambios de Medio Impacto

### 3. Telegram/DM Allowlist Fix (Riesgo: MEDIO)

**Cambio:** Fix para herencia de `dmPolicy: "allowlist"` y `allowFrom`.

**Impacto:**
- Antes: DM traffic podía ser silenciosamente descartado
- Ahora: Enforcement correcto usando effective account-plus-parent config

**Estado actual:**
- Telegram configurado con `dmPolicy: "allowlist"`, `allowFrom: ["7192195698"]`
- Tenemos `replyToMode: "first"` y `chunkMode: "length"`

**Riesgo concreto:**
- Teóricamente LOW (es un fix, debería mejorar)
- Si hay bug en el fix, podríamos perder mensajes
- Doctor checks ahora alineados — podría reportar "issues" nuevos

**Mitigación:**
- ✅ Configuración simple y estándar
- ⚠️ Verificar recepción de mensajes en próximos minutos

---

## Cambios de Bajo Impacto

### 4. External Secrets Management (Riesgo: BAJO)

**Cambio:** Nuevo workflow `openclaw secrets` (audit, configure, apply, reload).

**Impacto:** Feature nuevo, no afecta configuración existente.

**Estado actual:** No usamos secrets aún.

---

### 5. Agents/Routing CLI (Riesgo: BAJO)

**Cambio:** Nuevos comandos `openclaw agents bindings/bind/unbind`.

**Impacto:** Feature nuevo para account-scoped routing.

**Estado actual:** No usamos routing complejo aún.

---

## Verificación Post-Upgrade Inmediata

### Checklist (ejecutar ahora):

```bash
# 1. Versión correcta
openclaw --version  # Esperado: 2026.2.26

# 2. Healthcheck gateway
curl -s http://localhost:18789/health

# 3. Doctor checks
openclaw doctor --non-interactive

# 4. Config válida
openclaw config validate
```

### Checklist (monitorear en próximas 24h):

- [ ] Recepción mensajes Telegram normal
- [ ] Fallback de modelos funciona (testear `/model gpt-5.2`)
- [ ] sessions_spawn con ACP funciona (si se usa)
- [ ] Subagentes terminan sin errores
- [ ] No hay mensajes perdidos en Telegram

---

## Procedimiento de Rollback (si es necesario)

```bash
# 1. Detener gateway
systemctl --user stop openclaw-gateway

# 2. Restaurar versión anterior
rm -rf ~/.npm-global/lib/node_modules/openclaw
npm install --prefix ~/.npm-global openclaw@2026.2.25

# 3. Reiniciar
systemctl --user start openclaw-gateway
```

**Nota:** Backup de 2026.2.25 no existe compilado, habría que reinstalar desde NPM.

---

## Recomendaciones

1. **INMEDIATO:** Ejecutar healthcheck y doctor
2. **CORTO PLAZO:** Testear fallback a Codex con `/model gpt-5.2`
3. **MONITOREO:** Observar comportamiento de subagentes ACP en próximas 48h
4. **CONTINGENCIA:** Si hay problemas, rollback a 2026.2.25 vía NPM

---

## Conclusión

La actualización es **aplicable** pero requiere vigilancia. Los cambios ACP/Thread y Codex/WebSocket son arquitectónicos significativos. Sin sesiones críticas activas ni subagentes en ejecución, el riesgo de pérdida de datos es mínimo. El principal riesgo es degradación de servicio si los nuevos transportes/runtimes fallan.

**Decisión recomendada:** Proceder con monitoreo activo, tener rollback listo.

---

*Análisis generado por Korax para Korvo*
