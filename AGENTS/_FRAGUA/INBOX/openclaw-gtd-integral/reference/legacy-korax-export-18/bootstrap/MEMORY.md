# MEMORY.md — Korax Long-Term Memory

*Actualizado: 2026-03-05T19:00Z*

---

## Korvo

- Félix. GORE Ñuble (gestión/sistemas) + Urgencias HSC. Jefatura HODOM desde 2-mar-2026.
- Español neutro, directo, sin relleno. Quiere contraargumentos, no complacencia.
- **Timezone: America/Santiago (UTC-3 invierno / UTC-4 verano). Siempre interpretar horas como hora Chile salvo indicación explícita.**

## Proyectos activos

- **GoreOS** — modelo operativo institucional GORE
- **Sanixai** — servicios automatización/IA
- **Escuderos** — agentes por rol
- **Korvo–Korax** — asistente 24/7
- **Gateway jurídico** — consultores admin+laboral, servidor dedicado Hetzner
- **OpenOPD** — clon open-source de OPCloud (ISO/PAS 19450 OPM). Repo: `~/projects/opcloud-oss/`, puerto 3838
  - Stack: Next.js 16 + @xyflow/react + SQLite/Drizzle + Zustand + shadcn/ui
  - **26 commits, 7 fases completadas** (2026-03-03)
  - DB: unified graph model (`opm_nodes`/`opm_edges`/`opm_visual`). States y triangles = nodos first-class.
  - Fases: MVP → UX → ISO links → OPL+examples → ISO constraints → Graph refactor+undo/redo → Zoom/unfolding
  - Refs: `OPM-ISO19450.md`, `OPM-CONSTRAINTS.md`, `GAP-ANALYSIS-V2.md`, `DIAGNOSTIC.md`, `docs/opcloud-reference/`
  - OPCloud reference: `OPCLOUD-FULL-SPEC.md` (parcial, Gemini extraction), `context_menu_*.txt`
  - Pendiente: properties panel, OPL interactivo, copy/paste, auto-layout, dark theme

## Repos GitHub

- `felix-antonio-sl/kora` — specs agentes LLM, 683 artifacts, 43 agentes. Scripts portabilizados 2026-03-03. Activo
- `felix-antonio-sl/gore_os` — 820 US, 141 entidades, 71 tablas PG. Transición a LLM
- `felix-antonio-sl/leychile-sdk` — SDK Python BCN. Base gateway jurídico

## Frameworks

- **KORA** — Agent-Spec v5.0.0, F-coalgebras. KODA purgado 2026-02-24
- **ORKO** — transformación digital organizacional
- **PCA/GTD** — v1.0.0 implementado 2026-02-24 (10 estados, 32 transiciones, 15 invariantes, 8 skills)

## Kilo Gateway (2026-02-24)

Proveedor: `api.kilo.ai/api/gateway`. Modelos free: kimi (262K), glm5 (200K), minimax-kilo (200K).
Fallback: sonnet → gpt-5.2 → kimi → glm5. Detalle: `memory/models.md`, `memory/model-router-proposal.md`

## Servidor dedicado (legal-ai)

i7-7700, 64GB, 2×512GB NVMe. Ubuntu 24.04, Docker. Pendiente: Tailscale, hardening, KB legal.

## Stack dev

Detalle: `memory/dev-stack.md`. Resumen: Next.js+TS+Tailwind | FastAPI/Hono | PG+pgvector+Drizzle | OpenClaw+MCP | Langfuse | Claude Code+Gemini+Codex

---

## Regla idioma (ABSOLUTA)

**Siempre español (es-CL).** Sin excepciones. Todos los estados/roles/sesiones.

---

## Agentes especializados

| Agente | ID | Workspace | Bot Telegram | Modelo |
|---|---|---|---|---|
| Urgencista | `urgencista` | `~/agents/medico-urgencias/` | @klinikurgo_bot | Opus 4.6 |
| Salubrista HaH | `salubrista` | `~/agents/salubrista-hah/` | @SaluristaHahBot | Opus 4.6 |
| Clawmaster | `clawmaster` | `~/agents/clawmaster/` | Korax (subagent) | Opus 4.6 |

- **Korax NO encarna rol médico ni salubrista** — derivar al agente correspondiente
- DAU/SGH/clínica → urgencista. HODOM/normativa/gestión HD → salubrista
- Docs clínicos (DAU, SGH, endpoints) viven en workspace urgencista
- Docs HODOM/normativa viven en workspace salubrista

---

## Decisiones operativas

### Browser
Default: Playwright headless VPS (`profile=openclaw`). Bajo demanda: air (`target=node`). Docker eliminado.

### Nodo air
Mac móvil, cualquier red. Verificar `nodes status` antes de tareas. LaunchAgent `ai.openclaw.node.plist`.
- `oc-update`: `openclaw update --no-restart && openclaw node restart`
- Post-update: siempre `openclaw node restart` (LaunchAgent queda not-loaded tras updates)
- Capacidades: `system.run`, `system.which`, `browser.proxy`
- Obsidian: `~/fx`
- **korax-switch v5** (`~/.korax-switch.sh`, source desde `~/.zshrc`): `korax minsal`/`normal`/`status`
  - MINSAL: **Named Tunnel `gw.sanixai.com`** (URL fija permanente). `openclaw node install --force` (canónico).
  - Normal: Tailscale directo (`clawdbot-hetzner.tail84b159.ts.net`).
  - Actualizar script: `curl -sf https://gw.sanixai.com/korax-switch > ~/.korax-switch.sh`
  - **Fortinet bloquea:** Hetzner IPs, GitHub, Tailscale control plane, SSH. **Permite:** Cloudflare, Google, MINSAL.
  - VPS: `cloudflared tunnel run korax-gw` + Caddy (:18790) como servicios systemd.
  - **Dominio:** `sanixai.com` en Cloudflare (nameservers: carmelo/ollie). Tunnel ID: `6cda580a-b944-47fe-b0e1-5bbc5832a74b`.
  - Detalle: ver clawmaster `memory/2026-03-04-fortinet-cloudflare.md`
- Watchdog: cron `node-air-watchdog` (deshabilitado)

### PC HODOM — Gateway red MINSAL (2026-03-05)
PC Windows hospital (SSÑuble), Tailscale IP `100.77.30.26`, TightVNC. `netsh portproxy` expone 8 servicios clínicos:

| Puerto | Servicio | Destino interno |
|---|---|---|
| :8080 | DAU | 10.6.85.218:80 |
| :8085 | SGH | 10.6.85.228:8085 |
| :8081 | OSIRIS | 10.6.85.123:8085 |
| :8082 | Autoconsulta | 10.7.195.176:80 |
| :8083 | Biblioteca | 10.5.210.202:8081 |
| :8084 | WEB San Carlos | 10.5.211.210:80 |
| :8086 | Admin | 10.6.85.214:8081 |
| :8443 | SSNUBLE Webview | 10.5.210.140:443 |

- **VPS alcanza directamente** todos los servicios vía Tailscale → **Mac ya no es requisito** para acceso clínico
- `dau-sgh.sh --proxy-hodomito` o `DAU_SGH_MODE=proxy-hodomito` → rutea vía PC HODOM
- **Pendientes hardening:** key expiry Tailscale, `--unattended`, restaurar auth VNC, ACLs, script restore-portproxy.ps1

### Tres modos acceso red MINSAL

| Modo | Ruta | Requiere Mac en hospital |
|---|---|---|
| Directo | Mac WiFi hospital → 10.6.x.x | Sí |
| Named Tunnel | Mac → gw.sanixai.com → VPS → air → curl | Sí |
| **proxy-hodomito** 🆕 | VPS/Mac → Tailscale → PC HODOM → 10.6.x.x | **No** |

### Seguridad
sandbox.mode=off. Mitigaciones: sudo denylist, allowlist Telegram, token gateway, loopback+Tailscale.
SSH: puerto 22 bloqueado UFW, solo Tailscale (100.99.32.96). Usuario `korvo` con sudo+key.

### Memoria
MEMORY.md = curado. `memory/YYYY-MM-DD.md` = diario. Estilo telegráfico. Objetivo <15KB.

### OpenClaw (DEFINITIVO)
- Versión: **2026.3.2** en VPS (actualizado 2026-03-03), **2026.3.1** en nodo air
- Install: `~/.npm-global/lib/node_modules/openclaw/`. Bin: `~/.npm-global/bin/openclaw`
- **NUNCA** `sudo npm i -g openclaw` — duplica en `/usr/lib`
- Update: manual only (`gateway update.run`). Auto-update evaluado y descartado.
- Thinking: `adaptive` es default para Claude 4.6 desde 2026.3.1 (antes `off`)
- Streaming: block. Typing: instant.
- context1m: true (Opus+Sonnet). Header: `anthropic-beta: context-1m-2025-08-07`

### OpenClaw 2026.3.2 — Features clave
- **SecretRef (64 targets)**: credenciales gestionadas → migrar DAU/SGH de texto plano
- **PDF tool nativo**: análisis PDFs directo (normas, informes)
- **`sessions_spawn` attachments**: enviar archivos a subagents
- **`openclaw config validate`**: validar config antes de aplicar
- **BREAKING**: `tools.profile` default=`messaging` (nuevas installs), ACP dispatch default=enabled, Plugin SDK `registerHttpHandler` removed → `registerHttpRoute`
- **Cron HEARTBEAT_OK leak fix**: ya no aparece ruido heartbeat en chat

### OpenClaw 2026.3.1 — Features clave
- **Telegram DM Topics**: per-DM topic config. Potencial reemplazo del hack subagent para urgencista.
- **Heartbeat lightContext**: `agents.*.heartbeat.lightContext: true` → ahorro tokens.
- **Thinking `adaptive`**: default Claude 4.6.
- **BREAKING nodo air**: `system.run` usa canonical path (`realpath`).

### Automatización (2026-02-26)
- `projects/air-bridge/` — INBOX.md VPS → Obsidian via air
- `projects/downloads-scout/` — escanea Downloads en air → INBOX.md
- `projects/korax-briefing/` — brief matutino a Telegram, L-V 11:00 UTC

### Correo
- Flujo: iCloud/GORE → felixsanhuezaluna@gmail.com → forwarding a koraxfx@gmail.com
- gog `koraxfx`: token permanente (OAuth prod). Gmail webhook operativo.
- Korax envía SOLO a felixsanhuezaluna. Circuito completo NO verificado.

---

## Situación laboral (2026-03-02, actualizado 18:37 UTC)

Comisión servicio 22h (Ley 19.664) GORE desde oct-2023. **Finalizada 1° marzo 2026.**
Ord. 1A N°396 (12-feb, Dir. HSC Gatica): retorno HSC, dist. horaria con jefatura+SDM.
**Alejandro Aguilera** — contacto GORE para continuidad como colaborador externo (tardes, ~3-4h según HODOM).

### Nuevo equipo directivo HSC
- **René Goza** — subdirector médico (nuevo). Tono amable con Korvo.
- **Valentina** — segunda. **Gaete** — tercero.
- **Natalia** — directivo saliente, presionó reasignar Korvo fuera de Medicina sin coordinar con Calderón.

### HODOM (Hospitalización Domiciliaria) — CONFIRMADO
- Korvo asume dirección técnica HODOM 22h a partir de lun 2-mar ✅ (confirmado con Goza + informado a Aguilera)
- Carpeta proyecto (gestión + diseño + implementación): `projects/hodom/`
- **Mar 3**: presentación al equipo HODOM + definir horario 22h
- **Mar 3 tarde**: reunión Alejandro Aguilera (GORE) para negociar continuidad como colaborador externo. Depende del horario HODOM.
- Condiciones a confirmar: horario exacto (mañanas), asignación económica, dependencia orgánica SDM

**Recursos actuales HODOM:**
4 móviles + conductores | 44h médicas | 2 enfermeras 44h | kine 44h | fono 1 jornada | TENS | 1 admin completa

**Cobertura:** pacientes >18a, radio ~20km del hospital

**Flujos:** Medicina + Urgencia (consolidados) | Cirugía (curaciones, ATB EV) | Traumatología (ocasional) | APS dependencia severa (excepcional)

**Marco legal:**
- Norma BCN 1181901: "Reglamento de Establecimientos de Hospitalización Domiciliaria" (vía leychile-sdk)
- Art. 4: autorizacion SEREMI puede estar incluida en autorización general del hospital → verificar
- Art. 7-9: Director Técnico = médico cirujano, ≥22h semanales, informar jornada al SEREMI
- Art. 11: Coordinador requiere ≥5 años experiencia + gestión + curso IAAS 80h
- Art. 15-17: criterios ingreso/egreso/exclusión explícitos
- Art. 19: oficina debe tener telefonía 24h con grabación, TI, respaldo eléctrico
- Art. 21: registros obligatorios (consentimiento, carta derechos, formulario ingreso, etc.)
- Art. 25: plazo adecuación 6 meses desde publicación (para unidades existentes)

**Situación terreno (día 1, 3-mar-2026):**
- Hacinados, sin WiFi, ethernet super restringido
- Enfermera a cargo: **Anastasia**
- Documentación compartida vía Google Drive

**Brechas críticas (prioridades):**
1. Autorización sanitaria → verificar si aplica Art. 4 (puede estar en autorización general HSC)
2. Sin oxigenoterapia domiciliaria → rechazos de derivación
3. Protocolos desactualizados → riesgo médico-legal
4. Cartera de prestaciones restringida (fases complejas rechazadas)

**Informe abogado:** `docs/activa/informe-comision-servicio-2026-02-26.md`

## Turnos HSC

Calendar Google: "Turnos HSC". TFS=fin semana, TD=08-20h, TN=20-08h. 27 turnos hasta jun-2026.

## Sistemas clínicos SSÑ

→ Detalle completo en workspace urgencista (`~/agents/medico-urgencias/docs/`)
- LIS sin acceso programático (10.6.85.157, 10.6.85.214:8081)

## Lecciones técnicas

- Gateway: user-level systemd (`openclaw gateway install`)
- `nodes run` > `exec host=node` para shell wrappers en macOS
- Bootstrap files grandes se truncan → mantener breves
- DAU `obtener_anamnesis.php` = GET. `guarda_atencion_medica.php` = stateless.
- **GAP seguridad**: credenciales DAU/SGH en texto plano (urgencista workspace). Pendiente migrar a OpenClaw SecretRef (2026.3.2+).
- **Zustand**: NUNCA usar `get` property accessors (destruidos por `Object.assign`). Selectores con `.filter()` causan infinite re-render → usar `useShallow` de `zustand/react/shallow`.
- **Termius SFTP**: Korvo accede al VPS como `clawdbot` desde Mac (key `/Users/felixsanhueza/.ssh/id_ed25519`).
- **Gemini CLI**: `gemini --yolo -p "prompt"` para one-shot con auto-approve. Quota gemini-2.5-pro: 2M tokens input. Útil para análisis de bundles JS grandes.
- **KORA scripts portabilidad**: todos usan `Path(__file__).resolve().parent.parent` para detectar KORA_ROOT. Paths externos via env vars (`KORA_WIKIGUIAS_PATH`, `KORA_POSIBLES_PATH`). Commit `93d26e8`.
- **Nodo air `nodes run` falla** con breaking change 2026.3.1 (`realpath` en `system.run`). Update remoto imposible → requiere Terminal local en Mac.

---

## Índice

- `memory/infrastructure.md` | `memory/models.md` | `memory/operations-log.md`
- `memory/dev-stack.md`
- Clínica/DAU/SGH → `~/agents/medico-urgencias/docs/`
- HODOM/normativa → `~/agents/salubrista-hah/docs/`
