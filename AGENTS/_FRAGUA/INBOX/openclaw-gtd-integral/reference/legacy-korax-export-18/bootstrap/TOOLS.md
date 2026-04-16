# TOOLS.md — Semántica de Herramientas

*urn:korvo:agent-bootstrap:korax-tools:2.0.0*

---

## Comandos PCA

### /inbox
- **Firma:** inbox(texto: string) → Confirmación { item, timestamp }
- **Pre:** Ninguna. **Post:** Item en INBOX.md con timestamp.
- **Delegation:** No aplica.
- **Cuándo usar:** Captura rápida al buffer. Estado: S_CAPTURE.
- **Cuándo NO usar:** Fuera de captura. No agregar metadatos (INV-06).

### /triaje
- **Firma:** triaje() → SesiónTriaje { procesados, eliminados, incubados, comprometidos, waiting }
- **Pre:** INBOX.md tiene ≥1 item.
- **Delegation (none):** Presentar items, preguntar destino. NO sugerir (INV-02).
- **Delegation (⊇ triage):** PUEDE decidir destino. DEBE reportar.

### /plan
- **Firma:** plan() → PlanDiario { bloques_asignados, compromisos }
- **Pre:** NEXT.md tiene ≥1 compromiso pendiente.
- **Delegation (none):** Presentar bloques y compromisos. NO calcular prioridades (INV-03).
- **Delegation (⊇ plan):** PUEDE asignar bloques. DEBE reportar.

### /done
- **Firma:** done(item: string) → Confirmación
- **Side-effect:** Mover de NEXT.md a DONE.md con timestamp.

### /sync
- **Firma:** sync() → ReporteSinc
- **DEBE** requerir participación del operador incluso con delegation_scope: full.

### /estado
- **Firma:** estado() → Dashboard. Solo lectura. Sin restricciones.

### /emergencia
- **Firma:** emergencia() → ModoEmergencia. Siempre requiere confirmación.

### /caos
- **Firma:** caos(horas: number) → ModoCaos. Silencio total.

### /delegar
- **Firma:** delegar(scope) → Confirmación { scope_activo, expira }
- **Scopes:** triage, plan, maintenance, full. TTL: 7 días.

### /revocar
- **Firma:** revocar(scope?) → Confirmación { scope_activo }

---

## Herramientas de Dominio de Vida

### domain_route
- **Firma:** query: string → domain: string
- **Routing:**

| Pattern | Domain |
| --- | --- |
| bienestar, dormir, ejercicio, médico, estrés, energía | salud |
| dinero, ahorro, gasto, inversión, presupuesto | finanzas |
| meta, objetivo, proyecto vital, deadline personal | metas |
| aprender, curso, libro, skill, conocimiento | aprendizaje |
| contacto, networking, relación, reunión personal | relaciones |

### web_search (restringido)
- **Acceso:** Solo en S_ADVISE, S_SOLVE, S_IDLE.
- **Prohibido:** Durante estados PCA core (S_TRIAGE, S_PLAN, S_EXECUTE, S_SYNC).
- **Nota:** Nunca sustituir consejo profesional con resultados web.

---

## Herramientas de Plataforma

### 🌐 Acceso web

| Prioridad | Herramienta | Cuándo usar |
| --- | --- | --- |
| 1 | `web_fetch` | Ya tienes URL y quieres contenido rápido |
| 2 | `browser` | JS/login/interacción/screenshot |
| 3 | `web_search` | Solo para descubrir URLs |

### 🧭 Browser

- **Default (VPS):** Perfil `openclaw`, Playwright Chromium headless
- **Bajo demanda (Mac):** `browser` con `target="node"`

### 🔧 Gateway

```bash
systemctl --user status openclaw-gateway
systemctl --user restart openclaw-gateway
journalctl --user -u openclaw-gateway -f
curl -s http://localhost:18789/health
```

### 📧 gog (Google Workspace)

```bash
gog gmail messages search "in:inbox is:unread" --account koraxfx@gmail.com --limit 10
gog calendar list --account koraxfx@gmail.com --limit 10
```

### gog_gmail_search
- **Firma:** gog_gmail_search(query: string, limit?: number) → Email[] {from, subject, snippet, date}
- **Acceso:** Solo en S_CLOSE, S_ADVISE, S_SOLVE, S_IDLE.
- **Prohibido:** Durante estados PCA core (S_TRIAGE, S_PLAN, S_EXECUTE, S_SYNC, S_CAPTURE).
- **Implementación:** `gog gmail search "{query}" --account koraxfx@gmail.com --limit {limit|20}`
- **Skill asociada:** `email-clasificador` (clasificación batch por tiers)
- **Corpus:** `docs/activa/email-patterns.md` (reglas de dominio, ruido, heurísticas)

### 🧠 Nodo `air`

Antes de tareas en el Mac:
1. `nodes status`
2. Si connected → `nodes run`
3. Si desconectado → runbook en AGENTS.md §3.3

### 🤖 Modelos

| Alias | Modelo | Uso |
| --- | --- | --- |
| `sonnet` | claude-sonnet-4-6 | Default + heartbeat |
| `opus` | claude-opus-4-6 | Razonamiento complejo |
| `haiku` | claude-haiku-4-5 | Tareas ligeras |
| `gpt-5.2` | openai-codex/gpt-5.2 | Fallback 1 |
| `kimi` | moonshot/kimi-k2.5 | Fallback 2, 262K ctx |
| `glm5` | zai/glm-5 | Fallback 3, reasoning |

Referencia completa: `memory/models.md`

---

## Matriz de Acceso

| Herramienta | Acceso | Restricción |
|---|---|---|
| Lectura/escritura archivos (workspace) | Allow | Solo dentro del workspace |
| Lectura de calendario (gog) | Allow | Solo lectura |
| Búsqueda email (gog_gmail_search) | Allow | Solo S_CLOSE, S_ADVISE, S_SOLVE, S_IDLE |
| Envío de mensajes (Telegram) | Allow | Solo al operador |
| Búsqueda web | Allow | Solo en S_ADVISE, S_SOLVE, S_IDLE |
| Browser | Allow | Default VPS, nodo air bajo demanda |
| Ejecución shell | Allow | Como clawdbot, sudo denylist |
| Nodo air | Allow | Verificar status antes |
| Sub-agentes | Allow | Solo con aprobación explícita del operador |
