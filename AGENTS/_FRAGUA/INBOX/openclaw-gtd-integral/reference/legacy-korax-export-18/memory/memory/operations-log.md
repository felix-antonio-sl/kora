# Operations Log — Alertas y Eventos del Sistema

*Log de eventos operacionales, alertas activas y cambios de estado.*

---

## Alertas Activas

*(ninguna al 2026-02-20)*

---

## Estado de Recursos

### 2026-02-20
- **Gateway:** OpenClaw v2026.2.20 (nativo, systemd) — activo
- **Containers:** 1 corriendo (browser sandbox solamente)
- **Servicios:**
  - `openclaw-gateway.service` — ✅ activo
  - `gog-gmail-watch.service` — ✅ activo
  - Gmail watch — renovado 2026-02-19, expira 2026-02-26
  - Browser sandbox Docker — ✅ corriendo, CDP bloqueado via iptables

---

## Hitos de Korax

| Fecha | Evento |
|-------|--------|
| 2026-01-26 | Nacimiento como Clawdbot. Primer workspace, repos de Korvo clonados |
| 2026-01-27 | Migración gateway Docker → nativo (systemd) |
| 2026-01-30 | Rebranding: Clawdbot → Korax. Identidad definida |
| 2026-01-31 | Balance de implementación: seguridad 3→8/10, operabilidad 4→9/10 |
| 2026-02-02 | Brave Search API activada. Korvo viaja a México (2-16 feb); Korax opera autónomo |
| 2026-02-14 | Ariel (hermano de Korvo) agregado temporalmente al allowlist Telegram |

---

## Cambios Recientes

| Fecha | Cambio | Detalles |
|-------|--------|----------|
| 2026-02-20 | **Fallback chain actualizada** | gpt-5.2 insertado como fallback #1. Cadena: sonnet → gpt-5.2 → kimi → glm5. Hot-reload |
| 2026-02-20 | **Fallback chain simplificada** | Korvo decidió: sonnet → kimi → glm5 (simplificación de la cadena de 7 modelos) |
| 2026-02-20 | **KODA deep review** | 47 agentes, 216KB artifacts, 6 namespaces. Tiers 1/2 diseñados |
| 2026-02-20 | **Refactorización de memoria** | MEMORY.md podada de 22KB a ~6KB. Contenido movido a memory/*.md y cabinet/docs/ |
| 2026-02-19 | **Auditoría de seguridad** | 3 críticos, 4 importantes, 7 mejoras. Ejecutada con rol INGENIERO-OPENCLAW-COMPOSICIONAL |
| 2026-02-19 | **C1: Gateway bind loopback** | Era lan, expuesto en IP pública → corregido a loopback |
| 2026-02-19 | **C2: API keys a .env** | Movidas de openclaw.json a .openclaw/.env con ${VAR} |
| 2026-02-19 | **C3: Fallback corregido** | gpt-5.2 (inexistente como fallback) → claude-sonnet-4-6 |
| 2026-02-19 | **CDP Docker bloqueado** | iptables DOCKER-USER -i eth0 DROP. CDP 1026 ya no accesible desde internet |
| 2026-02-19 | **Secrets .bak eliminados** | 7 archivos .bak con API keys en cleartext eliminados |
| 2026-02-19 | **Permisos hardened** | .claude/ .gemini/ → chmod 700/600. CUPS maskeado |
| 2026-02-19 | **Gmail pipeline restaurado** | OAuth re-auth + watch renovado + 2 bugs en gog-gmail-watch corregidos |
| 2026-02-19 | **Memory search optimizado** | MMR activado, temporal decay (30d), cabinet/docs indexado |
| 2026-02-19 | **Workspace reestructurado** | cabinet/ creado (inbox/, docs/, archive/). Ariel removido de allowlist |
| 2026-02-13 | **OpenClaw v2026.2.6-3 → v2026.2.13** | 449 commits, security fixes, heartbeat stall prevention |
| 2026-02-13 | **Heartbeat migrado a Haiku** | `anthropic/claude-haiku-4-5`, activeHours 08-23 Chile |
| 2026-02-09 | OpenClaw v2026.2.1 → v2026.2.6-3 | Actualización previa |
| 2026-02-04 | Stack dev instalado | jq, yq, ripgrep, fzf, bat, lazygit, httpie, sqlite3 |
| 2026-02-03 | Migración Docker → nativo | Gateway como servicio systemd |
| 2026-02-03 | Restricciones sudo implementadas | Denylist en /etc/sudoers.d/clawdbot |
| 2026-02-02 | Brave Search API activado | Web search funcional |

---

## Cron Jobs

| Job | ID | Horario | Estado |
|-----|-----|---------|--------|
| GTD Weekly Review | eeb633ab... | Dom 20:00 Chile | ✅ Activo |
| Recordatorio Gobernador | a072508c... | one-time (26 ene) | ⬜ Deshabilitado |
| Recordatorio Reunión | 6266a3ea... | one-time (26 ene) | ⬜ Deshabilitado |

---

## Problemas Resueltos

| Fecha | Problema | Resolución |
|-------|----------|------------|
| 2026-02-19 | CDP 1026 público desde internet | iptables DOCKER-USER -i eth0 DROP (persistente via netfilter-persistent) |
| 2026-02-19 | Token gog OAuth expirado | Re-auth manual via curl + `gog auth tokens import` |
| 2026-02-19 | gog-gmail-watch enviaba token vacío | Corregida variable env + migrado a `--hook-token` Bearer |
| 2026-02-19 | Gateway rechazaba webhooks Gmail (400) | Token en header requerido desde versión actual |
| 2026-02-13 | Heartbeats fallando (Kimi + rate limits) | Migrado a Haiku con activeHours |
| 2026-02-04 | Gateway Docker caído | Migrado a ejecución nativa (systemd) |
| 2026-02-03 | Cron job `c5e98d5d` obsoleto | Eliminado |
| 2026-01-31 | Browser no conectaba | Configurado CDP URL sandbox |
| 2026-01-30 | Rebrand Clawdbot → OpenClaw | Gateway recreado |

---

*Última actualización: 2026-02-20 UTC*
