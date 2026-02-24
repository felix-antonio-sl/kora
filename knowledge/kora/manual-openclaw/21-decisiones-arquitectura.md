---
_manifest:
  urn: urn:kora:kb:21-decisiones-arquitectura
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '21'
- decisiones
- arquitectura
lang: es
---

# Capítulo 21 — Decisiones de Arquitectura (Decision Records)

> **Propósito:** Framework para las decisiones arquitectónicas más comunes. Cada sección plantea la pregunta, los criterios de decisión, las opciones con trade-offs, y una recomendación. Úsalo como checklist al diseñar tu setup.

- ---


## 21.1 ¿Cuántos agentes necesito?

### Criterios de split

| Factor | 1 agente suficiente | Múltiples agentes necesarios |
|--------|---------------------|------------------------------|
| **Personas** | Solo tú | Múltiples usuarios con diferente trust/contexto |
| **Personalidad** | Misma voz en todos los canales | Diferentes tonos/idiomas por contexto |
| **Tools** | Mismos tools en todo contexto | Diferentes niveles de acceso (full vs read-only) |
| **Modelo** | Mismo modelo para todo | Opus para trabajo, Haiku para familia |
| **Memoria** | Una memoria para todo | Memorias aisladas por dominio/persona |
| **Sandbox** | Misma postura de seguridad | Host para DMs, Docker para grupos |

- **Recomendación:** Empieza con 1 agente.
- Agrega cuando la separación sea **necesaria**, no cuando sea "nice to have".
- Cada agente es mantenimiento (workspace, auth, memoria).


- ---


## 21.2 ¿Sandbox on/off?

| Situación | Recomendación | Justificación |
|-----------|--------------|---------------|
| Solo tú, DMs, input controlado | `off` | Acceso nativo a tools del host (gog, scripts) |
| Solo tú, pero procesas contenido externo | `non-main` | Grupos y cron en sandbox; DMs en host |
| Múltiples personas | `all` (para agentes no-personales) | Blast radius limitado |
| Bot público | `all` + `workspaceAccess: "none"` | Mínimo blast radius |

- **Si dudas:** `non-main` es el sweet spot.
- DMs de confianza en host, todo lo demás en sandbox.


- ---


## 21.3 ¿Sub-agentes vs cron aislado?

| Criterio | Sub-agente | Cron aislado |
|----------|-----------|-------------|
| **Trigger** | Conversación (on-demand) | Schedule (programado) |
| **Resultado** | Announce a la sesión parent | Announce a canal o webhook |
| **Contexto** | Recibe task del parent | Recibe message fijo del job |
| **Model** | Override per-spawn | Override per-job |
| **Interacción** | Steer/kill desde parent | Manual run/edit |
| **Cleanup** | Auto-archive | Job persiste (recurring) o auto-delete (one-shot) |

- **Recomendación:** Si la tarea es **reactiva** (el usuario la pide) → sub-agente.
- Si es **proactiva** (schedule fijo) → cron.


- ---


## 21.4 ¿Un gateway o múltiples?

| Criterio | Un gateway | Múltiples gateways |
|----------|-----------|-------------------|
| **Complejidad** | Baja | Alta (puertos, configs, servicios separados) |
| **Aislamiento** | Via multi-agent (process compartido) | Process separados |
| **Rescue** | Si cae, todo cae | Rescue bot sobrevive |
| **Versiones** | Una versión | Diferentes versiones posibles |
| **Recursos** | Un proceso | Múltiples procesos |

- **Recomendación:** Un gateway para 99% de los setups.
- Agregar un rescue bot solo si dependes críticamente del agente y necesitas un failsafe.


- ---


## 21.5 ¿Heartbeat vs cron?

- **Resumen ejecutivo del Cap.
- 14:**


```
Checks periódicos simples que se batchean → Heartbeat
Timing exacto, model override, aislamiento → Cron
Ambos → Sí, se complementan
```

- ---


## 21.6 ¿Modelo por agente o fallback chain compartida?

| Enfoque | Pros | Contras |
|---------|------|---------|
| **Modelo por agente** | Optimizado por caso de uso (opus=deep, haiku=cheap) | Más auth profiles que configurar |
| **Fallback chain compartida** | Una config, mantenimiento simple | Todos los agentes usan la misma cadena |
| **Modelo por agente + fallback compartido** | Best of both: primary per-agent, fallbacks heredados | Config ligeramente más compleja |

- **Recomendación:** Primary per-agent (cada agente con el modelo que mejor sirve su propósito), fallbacks en `agents.defaults.model.fallbacks` (compartidos, diversidad de provider).


- ---


## 21.7 ¿tools.elevated: cuándo y para quién?

| Situación | Elevated |
|-----------|---------|
| Agente sin sandbox | No necesario (ya en host) |
| Agente sandboxed, necesita instalar en host | `on` con allowFrom tight |
| Debugging de host desde agente sandboxed | `full` temporalmente |
| Operación rutinaria que necesita path del host | No — usar bind mount |
| Agente público o untrusted | **Nunca** |

- **Recomendación:** `enabled: false` por default.
- Habilitar solo cuando no hay alternativa (bind mount suele ser mejor).


- ---


## 21.8 Memory architecture

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué va en MEMORY.md? | Hechos durables que el agente necesita en TODA interacción |
| ¿Qué va en memory/*.md? | Todo lo demás: daily logs, notas, detalles |
| ¿Cuánto puede crecer MEMORY.md? | <10KB (~2,500 tokens). Más → truncation o compaction loops |
| ¿Embeddings: OpenAI o local? | OpenAI si tienes key (mejor calidad). Local si quieres zero-cost |
| ¿MMR? | Sí si tienes >50 daily logs con contenido repetitivo |
| ¿Temporal decay? | Sí si tienes >3 meses de historial |
| ¿Session memory search? | Solo si no documentas consistentemente en daily logs |
| ¿QMD? | Solo para corpus grandes (>10K chunks) o si necesitas reranking |

- ---


## 21.9 Checklist Pre-Deployment

```
Identity
  [ ] ¿Quién puede enviar DMs? (dmPolicy + allowFrom)
  [ ] ¿Quién puede trigger en grupos? (groupPolicy + requireMention)
  [ ] ¿dmScope apropiado para el número de usuarios?

Scope
  [ ] ¿Tool policy apropiada por agente?
  [ ] ¿Sandbox mode apropiado? (off/non-main/all)
  [ ] ¿Control plane tools (gateway, cron) denied para untrusted?
  [ ] ¿Elevated disabled o con allowFrom tight?

Network
  [ ] Gateway en loopback?
  [ ] Auth token configurado y largo?
  [ ] ¿Funnel/Serve necesario? Si no, desactivado
  [ ] Webhook token separado del gateway token?

Modelo
  [ ] ¿Primary model apropiado para el nivel de trust?
  [ ] ¿Fallbacks configurados con diversidad de provider?
  [ ] ¿Heartbeat usando modelo barato?

Memoria
  [ ] MEMORY.md <10KB?
  [ ] Embedding provider configurado?
  [ ] MMR/decay habilitados si aplica?

Operaciones
  [ ] Backup strategy definida?
  [ ] Health check periódico configurado?
  [ ] `openclaw security audit` limpio?

Permisos
  [ ] ~/.openclaw/ = 700
  [ ] openclaw.json = 600
  [ ] .env = 600
```

- ---


- *Siguiente: [Apéndices](apendices.md)*

