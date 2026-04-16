# Paquete de Migración — Korax v3.4.0

**Fecha de exportación:** 2026-04-05
**Operador:** Félix Sanhueza (Korvo)
**URN base:** `urn:korvo:agent-bootstrap:korax-config:3.4.0`

---

## 1. Identidad

| Campo | Valor |
|---|---|
| **Nombre** | Korax |
| **Emoji** | 🦴 |
| **Vibe** | Exoesqueleto cognitivo de productividad y bienestar. Propone, no decide. Acompaña sin invadir. |
| **Canal primario** | Telegram |
| **Idioma** | es-CL |

## 2. Arquitectura

### 2.1 Rol

Agente de productividad y bienestar personal. Gestiona el sistema PCA v4.1 (captura → triaje → planificación → ejecución → sincronización → cierre). Acompaña en regulación emocional, rescate y desarrollo personal (Manual de Vida).

### 2.2 Modelo operativo

- **Co-agencia fija:** Korax propone, operador decide. Siempre (INV-12).
- **FSM de 11 estados** con transiciones explícitas (S-IDLE ↔ S-CAPTURE ↔ S-TRIAGE ↔ S-PLAN ↔ S-EXECUTE ↔ S-SYNC ↔ S-CLOSE ↔ S-CHAOS ↔ S-COLLAPSE ↔ S-ABANDON)
- **Entidades tipadas:** Candidato, UT, Proyecto, Objetivo (PROPOSITO|RESULTADO), Contribución
- **Computos derivados:** P (prioridad), U (urgencia), completitud(), PxU
- **Heartbeats:** 5 crons inyectan eventos externos al FSM

### 2.3 Principios

| ID | Principio |
|---|---|
| P1 | La atención es el recurso soberano (<10% tiempo del operador) |
| P2 | Separación de concerns (captura ≠ triaje) |
| P3 | Navegación por estado, no algoritmo |
| P4 | Start simple, scale only when needed |

## 3. Dependencias

### 3.1 PCA Sidecar (requerido)

- **Servicio:** kora-pca
- **Endpoint:** `http://kora-pca:8100/api`
- **Tipo:** HTTP API (JSON)
- **Función:** Persistencia de entidades PCA v4.1 en SQLite + computos derivados
- **Debe existir** antes de iniciar Korax

### 3.2 Federación kora (requerido)

- **Red:** kora-federation (Docker)
- **Directorio:** `/home/node/shared/federation/directorio-agentes.md`
- **Agentes pares:** steipete (dev), salubrista-hah (salud), clawforge (ops)
- **Protocolo:** Derivación via HTTP hooks con Bearer token compartido

### 3.3 Canal

- **Telegram** como canal primario
- Chat ID operador: `7192195698`

### 3.4 Runtime

- OpenClaw como runtime de agente
- Docker container
- Node.js v24+
- `code_execution` habilitado

## 4. Archivos de Workspace

### 4.1 Archivos core (obligatorios)

| Archivo | Función |
|---|---|
| `AGENTS.md` | FSM completo, modelo de datos, reglas duras, invariantes, señales, integridad, co-inducción |
| `SOUL.md` | Identidad, paradigma cognitivo, tono, axiomas |
| `TOOLS.md` | Binding completo de PCA API (HTTP) + herramientas conversacionales |
| `USER.md` | Perfil del operador, rutinas, umbrales de salud, preferencias de output |
| `MEMORY.md` | Decisiones, hallazgos, coordinación, notas |
| `HEARTBEAT.md` | Checklist para heartbeats |
| `BOOT.md` | Procedimiento de inicio |
| `BOOTSTRAP.md` | Pre-requisitos y post-recovery |
| `IDENTITY.md` | Nombre, emoji, vibe |
| `config.json` | Configuración operativa (sandbox, PCA binding, tools, crons, capacidades) |

### 4.2 Skills (12 módulos cognitivos)

Directorio `skills/`:

| Skill | Estado FSM | Función |
|---|---|---|
| `CM-CAPTURA.md` | S-CAPTURE | Captura rápida al buffer |
| `CM-TRIAJE.md` | S-TRIAGE | Arbol N1/N2/N3 de decisión |
| `CM-PLANIFICACION.md` | S-PLAN | Planificación matutina con bloques |
| `CM-SINCRONIZACION.md` | S-SYNC | 4 preguntas estratégicas quincenal |
| `CM-CLOSE.md` | S-CLOSE | Cierre nocturno con micro-check |
| `CM-BANCARROTA.md` | S-COLLAPSE | Protocolo de bancarrota + gracia 48h |
| `CM-DETECCION-ABANDONO.md` | S-ABANDON | Escalamiento 3d→7d→14d |
| `CM-DETECCION-COLAPSO.md` | S-COLLAPSE | Evaluación de 5 señales |
| `CM-RESCATE.md` | S-COLLAPSE/S-ABANDON | Estabilización (TIP→detectar→regular→reconectar) |
| `CM-REGULACION-EMOCIONAL.md` | S-PLAN/S-EXECUTE | 8 firmas corporales → calibración → acción opuesta |
| `CM-CATALIZADOR.md` | S-SYNC | HUMAN 3.0 + LWLG + anti-vision |
| `CM-REFLEXION.md` | S-CLOSE | 3-2-1 diario + revisiones periódicas |

### 4.3 Memoria adicional

Directorio `memory/`:

| Archivo | Contenido |
|---|---|
| `hodom-hsc-contexto-2026-03-25.md` | Contexto HODOM Hospital San Carlos (derivación salubrista) |
| `opmodel-contexto.md` | Contexto Open Model / OPM (derivación steipete) |

## 5. Estado Actual del Sistema

### 5.1 Datos PCA

| Métrica | Valor |
|---|---|
| Candidatos en buffer | 2 |
| UTs pendientes | 1 |
| Proyectos activos | 0 |
| Objetivos | 0 |
| Alertas | 0 |
| Señales activas | 0 |

### 5.2 Buffer de candidatos

| ID | Texto | Fecha |
|---|---|---|
| C-20260326002532245297 | Memory search: evaluar migrar de Gemini embeddings a LanceDB | 2026-03-26 |
| C-20260326013006802000 | Migrar hoy a un solo gateway en host | 2026-03-26 |

### 5.3 UTs activas

| ID | Título | Modo | P | U | PxU |
|---|---|---|---|---|---|
| U-20260326002316163612 | Materializar agente Nerion Polymat | MK | 0.2 | 0.0 | 0.0 |

### 5.4 Crons configurados

| Job | Horario | Estado |
|---|---|---|
| morning-plan | L-V 08:00 CLT | Activo (último run: timeout) |
| evening-close | Diario 21:00 CLT | Activo (último run: error API key) |
| biweekly-sync | Viernes 20:00 CLT | Activo (último run: timeout) |
| abandonment-check | Diario 10:00 CLT | Activo (último run: error API key) |
| collapse-monitor | Cada 6h | Activo (último run: error API key) |

> **Nota:** Los crons están registrados pero con errores recientes por issues de API key (Anthropic) y timeouts. Requieren configuración de model/créditos en el nuevo entorno.

## 6. Decisiones Consolidadas

| Fecha | Decisión |
|---|---|
| 2026-03-25 | Gestión de rutas: sistema dinámico y reordenable con salida compartible + versión reporte |
| 2026-03-25 | Reducir sobreingeniería; preferir skills nativas OpenClaw |
| 2026-03-25 | `kora kb` como skill, no subsistema |
| 2026-03-25 | Separar `kora` en conocimiento + agentes (provisional) |
| 2026-03-25 | Agentes genéricos con transmutaciones para OpenClaw/Claude Code/Codex |
| 2026-03-25 | PCA con Korax + skills como base operativa |
| 2026-03-25 | HSC con enfoque + skills |
| 2026-03-25 | Privilegiar agentes OpenClaw con skills sobre PSA actual |
| 2026-03-25 | Bootstraps más livianos, misma expresividad |

## 7. Procedimiento de Reconstrucción

### 7.1 Pre-requisitos

1. **OpenClaw** instalado y funcionando en el host destino
2. **Docker** disponible
3. **Red kora-federation** creada
4. **PCA sidecar** (kora-pca) deployado y accesible
5. **Bot de Telegram** configurado con token propio
6. **Modelo LLM** configurado en OpenClaw con créditos/API key válida
7. **Channel Telegram** configurado en OpenClaw

### 7.2 Paso a paso

#### Paso 1: Preparar el entorno Docker

```bash
# Crear red de federación
docker network create kora-federation

# Deployar PCA sidecar (imagen/container correspondiente)
# El PCA debe exponer puerto 8100 y estar en la red kora-federation
# Asegurar que el volumen de datos PCA persiste
```

#### Paso 2: Verificar PCA

```bash
curl http://kora-pca:8100/api/estado
# Debe responder JSON con candidatos_buffer, uts, proyectos, objetivos, alertas
```

#### Paso 3: Crear workspace del agente

```bash
mkdir -p ~/.openclaw/workspace/{skills,memory,inbox,output,sources}
```

#### Paso 4: Copiar archivos de workspace

Copiar al workspace del agente los siguientes archivos **en orden**:

**Core (obligatorios):**
- `IDENTITY.md`
- `SOUL.md`
- `AGENTS.md`
- `TOOLS.md`
- `USER.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `BOOT.md`
- `BOOTSTRAP.md`
- `config.json`

**Skills (directorio skills/):**
- `CM-CAPTURA.md`
- `CM-TRIAJE.md`
- `CM-PLANIFICACION.md`
- `CM-SINCRONIZACION.md`
- `CM-CLOSE.md`
- `CM-BANCARROTA.md`
- `CM-DETECCION-ABANDONO.md`
- `CM-DETECCION-COLAPSO.md`
- `CM-RESCATE.md`
- `CM-REGULACION-EMOCIONAL.md`
- `CM-CATALIZADOR.md`
- `CM-REFLEXION.md`

**Memoria (directorio memory/):**
- `hodom-hsc-contexto-2026-03-25.md`
- `opmodel-contexto.md`

#### Paso 5: Configurar OpenClaw

En la config de OpenClaw para el agente:

1. **Channel Telegram:** configurar bot token + chat ID `7192195698`
2. **Modelo:** configurar provider/model deseado (actualmente `zai/glm-5.1`)
3. **Sandbox:** `permissive` (requiere `code_execution` para curl al PCA)
4. **Cron jobs:** registrar los 5 crons (ver sección 5.4)
5. **Authorized senders:** `7192195698`

#### Paso 6: Configurar crons

Recrear los 5 cron jobs en OpenClaw:

| Nombre | Cron (CLT) | Payload |
|---|---|---|
| morning-plan | `0 8 * * 1-5` | agentTurn: flujo S-PLAN |
| evening-close | `0 21 * * *` | agentTurn: flujo S-CLOSE |
| biweekly-sync | `0 20 * * 5` | agentTurn: flujo S-SYNC |
| abandonment-check | `0 10 * * *` | agentTurn: señales abandono |
| collapse-monitor | `0 */6 * * *` | agentTurn: señales colapso |

Todos con `sessionTarget: "isolated"`, `delivery.mode: "announce"`, `channel: "telegram"`, `to: "7192195698"`.

#### Paso 7: Configurar federación

```bash
mkdir -p /home/node/shared/federation/
# Copiar directorio-agentes.md al directorio compartido
```

Verificar conectividad con agentes pares via hooks.

#### Paso 8: Inicializar PCA (si es DB nueva)

```bash
curl -X POST http://kora-pca:8100/api/init
```

Si se migra DB existente, copiar el archivo SQLite del volumen PCA.

#### Paso 9: Verificar funcionamiento

```bash
# 1. Boot check
curl http://kora-pca:8100/api/estado

# 2. Enviar mensaje de prueba via Telegram

# 3. Verificar que crons ejecutan sin error

# 4. Verificar hooks de federación
curl http://kora-personal:18789/hooks/agent
```

### 7.3 Checklist de validación

- [ ] PCA responde en puerto 8100
- [ ] `/estado` devuelve JSON válido
- [ ] Bot de Telegram responde
- [ ] `/captura <texto>` funciona
- [ ] `/estado` genera dashboard
- [ ] Crons ejecutan sin error
- [ ] Hooks de federación responden
- [ ] MEMORY.md accesible por memory_search
- [ ] 12 skills presentes y cargables

## 8. Notas de migración

- **DB PCA:** Si se migra con datos existentes, copiar el volumen SQLite. Si se inicia limpio, solo ejecutar `pca_init`.
- **API keys:** Los crons actuales fallan por crédito Anthropic agotado. En el nuevo entorno, configurar provider con créditos válidos.
- **Modelo:** El modelo actual (`zai/glm-5.1`) es configurable. Cualquier modelo razonablemente capaz funciona.
- **Federación:** Los hooks de derivación requieren que los agentes pares estén operativos. Sin ellos, Korax funciona independientemente pero no puede derivar.
- **TZ:** America/Santiago (UTC-3/UTC-4 con horario de verano).
