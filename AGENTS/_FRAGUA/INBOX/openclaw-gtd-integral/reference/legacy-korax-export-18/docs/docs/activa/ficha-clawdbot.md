# Ficha Técnica — Instancia Clawdbot

**Generado:** 2026-01-30 05:28 UTC  
**Versión Clawdbot:** 2026.1.25  
**Hash de Config:** `35149479c93a...`

---

## 1. Identidad del Agente

| Atributo | Valor |
|----------|-------|
| **Nombre** | Korax |
| **Rol** | Extensión cognitiva y actuador digital de Korvo |
| **Emoji** | 🪶 |
| **Vibe** | Directo, semiformal, funcional |
| **Workspace** | `/home/clawdbot/clawd` |
| **Agent ID** | `main` |
| **Sesión Actual** | `agent:main:main` |

---

## 2. Runtime del Sistema

| Atributo | Valor |
|----------|-------|
| **Host** | `1c39b2f7ee94` |
| **OS** | Linux 6.8.0-85-generic (x64) |
| **Node.js** | v22.22.0 |
| **Repo** | `/home/clawdbot/clawd` |
| **Gateway Mode** | `local` |

---

## 3. Configuración de Modelos

### 3.1 Modelo Primario
| Atributo | Valor |
|----------|-------|
| **Default** | `anthropic/claude-opus-4-5` |
| **Alias** | `opus` |
| **Auth** | OAuth (claude-cli) |

### 3.2 Modelos de Fallback (ordenados)
| Prioridad | Modelo | Alias |
|-----------|--------|-------|
| 1 | `openai-codex/gpt-5.2` | `gpt5` |
| 2 | `moonshot/kimi-k2.5` | `kimi` |

### 3.3 Modelos Configurados
| Modelo | Alias | Contexto | Max Tokens | Reasoning |
|--------|-------|----------|------------|-----------|
| `anthropic/claude-opus-4-5` | `opus` | - | - | No |
| `anthropic/claude-sonnet-4-5` | `sonnet` | - | - | No |
| `anthropic/claude-haiku-4-5` | `haiku` | 200K | - | No |
| `openai-codex/gpt-5.2` | `gpt5` | - | - | No |
| `moonshot/kimi-k2.5` | `kimi` | 262K | 32K | No |

### 3.4 Cooldowns de Billing
- **Backoff inicial:** 0.5h
- **Backoff máximo:** 2h
- **Ventana de fallos:** 0.0833h (5 min)

---

## 4. Canales de Comunicación

### 4.1 Telegram (Principal)
| Atributo | Valor |
|----------|-------|
| **Estado** | ✅ Habilitado |
| **Plugin** | `telegram` |
| **DM Policy** | `allowlist` |
| **Group Policy** | `allowlist` |
| **Stream Mode** | `partial` |
| **Allowlist** | `7192195698` (Korvo/Félix) |
| **Bot Token** | `8524...FgP4` (mascarado) |

### 4.2 Webhooks
| Atributo | Valor |
|----------|-------|
| **Estado** | ✅ Habilitados |
| **Path** | `/hooks` |
| **Token** | `237a2...1b64` (mascarado) |
| **Presets** | `gmail` |

#### Mapeo Gmail
| Campo | Valor |
|-------|-------|
| **Account** | `koraxfx@gmail.com` |
| **Modelo** | `haiku` |
| **Action** | `agent` |
| **Wake Mode** | `now` |
| **Delivery** | `true` → Telegram:7192195698 |
| **Template** | `📧 Nuevo email de {{from}}\nAsunto: {{subject}}\n\n{{snippet}}` |

---

## 5. Sesiones Activas (Resumen)

| Tipo | Cantidad |
|------|----------|
| **Sesión principal** | 1 (webchat → Telegram) |
| **Sesiones hook** | 19 (Gmail triggers) |
| **Total** | 20 sesiones |

### 5.1 Sesión Principal
| Atributo | Valor |
|----------|-------|
| **Key** | `agent:main:main` |
| **Channel** | webchat |
| **To** | `telegram:7192195698` |
| **Display** | Ominono id:7192195698 |
| **Session ID** | `85e71314-ab12-4f80-8f00-4e773064037e` |
| **Modelo Actual** | `kimi-k2.5` |
| **Context Tokens** | 262,144 |
| **Total Tokens Usados** | 12,902 |
| **Transcript** | `85e71314-ab12-4f80-8f00-4e773064037e.jsonl` |

---

## 6. Tareas Programadas (Cron)

| ID | Nombre | Estado | Schedule | Tipo |
|----|--------|--------|----------|------|
| `eeb633ab-...` | GTD Weekly Review | ✅ Activo | `0 20 * * 0` (domingos 20:00 CL) | Recurrente |
| `a072508c-...` | Recordatorio: Presentación Gobernador | ⏸️ Inactivo | One-shot (ejecutado) | Una vez |
| `6266a3ea-...` | Recordatorio: Reunión equipo | ⏸️ Inactivo | One-shot (ejecutado) | Una vez |

### 6.1 GTD Weekly Review (Detalle)
- **Frecuencia:** Domingos 20:00 (America/Santiago)
- **Target:** `isolated` session
- **Acción:** AgentTurn con prompt de revisión GTD
- **Entrega:** Telegram a Korvo
- **Próxima ejecución:** 2026-01-31 20:00 CL

---

## 7. Plugins Habilitados

| Plugin | Estado | Notas |
|--------|--------|-------|
| `telegram` | ✅ | Canal principal |
| `google-antigravity-auth` | ✅ | Auth Google Workspace |

---

## 8. Configuración de Herramientas

### 8.1 Sandbox
| Atributo | Valor |
|----------|-------|
| **Browser auto-start** | ✅ Sí |
| **Host control** | ✅ Permitido |
| **Docker network** | `clawdbot_default` |

### 8.2 Browser
| Atributo | Valor |
|----------|-------|
| **Estado** | ✅ Habilitado |
| **Perfil default** | `sandbox` |
| **CDP URL** | `http://172.18.0.3:9222` |

### 8.3 Tools Policy
| Tipo | Configuración |
|------|---------------|
| **Allow** | `*` (todas) |
| **Deny** | Ninguna |

---

## 9. Límites y Concurrencia

| Recurso | Límite |
|---------|--------|
| **Agentes concurrentes** | 3 |
| **Subagentes concurrentes** | 6 |
| **Context pruning** | Cache TTL 1h |
| **Compaction** | `safeguard` mode |

---

## 10. Seguridad y Red

### 10.1 Trusted Proxies
- `100.64.0.0/10` (Tailscale)
- `127.0.0.1` (localhost)

### 10.2 API Keys (Variables de Entorno)
| Variable | Estado |
|----------|--------|
| `MOONSHOT_API_KEY` | ✅ Configurada |

---

## 11. Nodos Emparejados

**Estado:** Ningún nodo emparejado actualmente.

---

## 12. Comandos Nativos

| Configuración | Valor |
|---------------|-------|
| **Native commands** | `auto` |
| **Native skills** | `auto` |
| **Ack reaction scope** | `group-mentions` |

---

## 13. Historial de Configuración

| Evento | Fecha |
|--------|-------|
| **Última modificación** | 2026-01-26 21:39:41 UTC |
| **Versión en último touch** | 2026.1.25 |

---

## 14. Información del Propietario

| Atributo | Valor |
|----------|-------|
| **Nombre** | Félix (Korvo) |
| **Número permitido** | `7192195698` |
| **Timezone** | Chile (UTC-3/UTC-4) |
| **Email principal** | `felixsanhuezaluna@gmail.com` |
| **Email secundario** | `koraxfx@gmail.com` (hooks) |

---

*Ficha generada automáticamente por Korax* 🪶