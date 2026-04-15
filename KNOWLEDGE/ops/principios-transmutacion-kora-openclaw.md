---
_manifest:
  urn: urn:ops:kb:principios-transmutacion-kora-openclaw
  provenance:
    created_by: ops/clawstack
    created_at: '2026-03-22'
    source: Experiencia operacional desplegando korax v3.4.0, steipete v1.5.1 y salubrista-hah
      v1.0.0 en Hetzner
    updated_at: '2026-03-23'
version: 1.1.0
status: published
tags:
- principios
- transmutacion
- openclaw
- docker
- arquitectura
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:ops:kb:principios-transmutacion-kora-openclaw
relations:
  cites:
  - urn:ops:kb:deploy-agente-kora-en-openclaw
---


# Principios de transmutacion KORA → OpenClaw


Este documento captura los principios generales para tomar un agente especificado en el ecosistema KORA y encarnarlo como servicio OpenClaw corriendo en Docker sobre un servidor Unix remoto. No es un paso-a-paso (eso esta en `urn:ops:kb:deploy-agente-kora-en-openclaw`) sino el marco conceptual que guia las decisiones.

---

## P1 — Especificacion y runtime son capas distintas

KORA especifica **que** es un agente. OpenClaw le da **donde** vivir.

```
KORA OpenClaw
──── ────────
Que piensa (SOUL.md) Como se conecta (gateway, canales)
Que hace (AGENTS.md, FSM) Con que modelo razona (provider, auth)
Con que opera (TOOLS.md) Donde persiste (sessions, memory)
Para quien (USER.md) Como escala (containers, cron, heartbeat)
Que sabe (skills/, KBs) Como se protege (sandbox, allowlist)
```

La transmutacion no modifica la especificacion — la viste con un runtime. Un agente KORA bien especificado deberia poder correr en OpenClaw, en otro gateway, o como prompt manual sin cambiar su AGENTS.md.

**Corolario:** si un cambio al deploy requiere modificar AGENTS.md, la especificacion tenia una dependencia implicita del runtime. Eso es un defecto de la spec, no del deploy.

---

## P2 — Strip, no transform

Los archivos KORA tienen frontmatter YAML (`---\n_manifest:\n...\n---`) que es metadata de gobernanza. OpenClaw no lo entiende y no lo necesita. La operacion es **strip** (remover el envoltorio) — nunca **transform** (cambiar el contenido).

```
KORA file = frontmatter + contenido operacional
OpenClaw file = contenido operacional (identico)
```

Si te encuentras reescribiendo contenido durante el deploy, algo esta mal. El contenido operacional debe ser identico bit-a-bit despues de strip. Las unicas excepciones validas:

- `config.json`: es metadata KORA, no se copia al workspace OpenClaw
- `IDENTITY.md`: puede no existir en KORA y necesitar creacion (OpenClaw lo requiere)
- Paths hardcodeados de entorno local (macOS → Linux): se corrigen en el workspace, no en el repo

---

## P3 — El config.json de KORA no es el openclaw.json

Son dos documentos con propositos distintos:

| | config.json (KORA) | openclaw.json (OpenClaw) |
|-|-------------------|------------------------|
| **Proposito** | Gobernanza: que tools se permiten, que KBs se acceden, que sandbox aplica | Runtime: modelo, canales, gateway, heartbeat, cron |
| **Quien lo lee** | Validador KORA (`kora validate`) | OpenClaw gateway |
| **Donde vive** | Repo KORA, con frontmatter | Named volume del container |
| **Se copia al workspace?** | No (o solo como referencia informativa) | N/A — es la config del gateway |

La informacion de `config.json` informa el diseño del `openclaw.json`, pero no se traduce mecanicamente. Los `tools.allow` de KORA son declaraciones semanticas; las tools de OpenClaw son capacidades concretas del runtime (exec, browser, web_search, etc.).

---

## P4 — El container es el boundary de aislamiento

Cada agente OpenClaw corre en su propio container Docker. Esto impone:

- **Filesystem aislado**: el agente no ve el host. Acceso explicito via bind mounts.
- **Red aislada**: containers se ven entre si solo via redes Docker explicitas.
- **Identidad separada**: cada agente tiene su propio bot Telegram, su propio puerto gateway, su propio volume de state.

**Principio de mount:** montar solo lo necesario, con el permiso minimo.

| Tipo de recurso | Mount | Permiso |
|----------------|-------|---------|
| Workspace del agente | bind mount | RW (el agente escribe memory, logs) |
| Knowledge bases | bind mount | RO |
| Repos de referencia (consulta) | bind mount | RO |
| Proyectos de desarrollo (codigo) | bind mount | RW (solo los que el agente debe modificar) |
| Config OpenClaw | named volume + copy | RW (OpenClaw escribe auth, tokens en runtime) |
| Datos persistentes (DB, sessions) | named volume | RW |

**Antipatron:** montar todo `/home/felix/projects/` como RW. Un agente de productividad (korax) no necesita escribir en repos de codigo. Un coordinador de desarrollo (steipete) necesita escribir solo en los proyectos que coordina.

---

## P5 — Separar repos de gobernanza de proyectos de desarrollo

```
/home/felix/
├── kora/ ← Gobernanza (specs, agents, KBs) — NUNCA un proyecto de desarrollo
└── projects/ ← Proyectos de desarrollo
 ├── openclaw/
 ├── pca/
 └── opmodel/
```

KORA es infraestructura de gobernanza que define a los agentes. No es un proyecto que los agentes desarrollan. Mezclarlo en `projects/` genera confusion sobre quien tiene autoridad sobre que.

Dentro de los containers, esta separacion se refleja en paths distintos:

```
/home/node/repos/kora ← referencia (RO) — el agente puede consultar specs
/home/node/projects/opmodel ← desarrollo (RW) — el agente puede escribir codigo
```

---

## P6 — El config del gateway vive en un named volume, no en un bind mount

OpenClaw escribe en su propio config (`openclaw.json`) durante runtime — auth profiles, gateway tokens, metadata de version, estado de commands. Un bind mount de archivo individual causa `EBUSY` porque OpenClaw usa atomic rename (write-to-tmp + rename) que falla sobre mount points.

**Patron correcto:**

1. Mantener `openclaw.json5` en el host como source of truth para la config controlada por el operador
2. Named volume en `/home/node/.openclaw/` para todo el state del gateway
3. Script de **merge** (no copy) para sincronizar cambios del host sin destruir state de runtime

```bash
# MAL: copia ciega que destruye auth profiles y tokens
cp host.json5 container:/home/node/.openclaw/openclaw.json

# BIEN: merge que preserva keys de runtime
sync-config.sh <compose-dir> <service> <host-config.json5>
```

Keys que el host controla: `agents`, `session`, `gateway`, `channels`, `browser`, `cron`.
Keys que el runtime controla: `meta`, `auth`, `commands`, `gateway.auth.token`.

---

## P7 — Port spacing y aislamiento de red

Cada gateway OpenClaw usa un puerto base y deriva puertos adicionales:

```
base → gateway WebSocket
base + 2 → browser control
base + 9.. → browser CDP
```

Dos gateways en puertos consecutivos (18789, 18790) pueden colisionar en puertos derivados. Minimo 20 puertos de separacion entre bases.

```
korax: 18789 (browser: 18791, CDP: 18798+)
steipete: 18810 (browser: 18812, CDP: 18819+)
salubrista: 18830 (browser: 18832, CDP: 18839+)
siguiente: 18850
```

Red compartida `kora-federation` (bridge) conecta los containers del stack. El gateway que la crea la define con `driver: bridge, name: kora-federation`. Los demas la referencian con `external: true`.

---

## P8 — Knowledge como volumen compartido read-only

Las KBs se montan como volumen RO compartido por todos los gateways. **No van en el bootstrap** — serian decenas de KB de chars que se inyectan en cada turno, quemando tokens sin necesidad.

```
/srv/kora/knowledge/ ← directorio compartido
├── korvo/ ← KBs de korax (manual-de-vida, filosofia)
├── dev/ ← KBs de steipete (praxis, tooling)
└── agengai/openclaw/ ← corpus OpenClaw (19M, sin frontmatter KORA)
```

Montado como `/home/node/ en cada container. El agente lee las KBs bajo demanda via filesystem, no las carga en cada turno.

**Excepcion:** un agente puede tener KBs criticas que SI necesitan estar en bootstrap (ej: un agente de emergencia medica que debe tener el protocolo disponible sin latencia de lectura). Pero eso es la excepcion, no la regla.

---

## P9 — Token budget como restriccion de diseno

OpenClaw trunca archivos bootstrap a 20,000 chars por archivo y 150,000 chars en total. Esto no es un bug — es una restriccion de la ventana de contexto del modelo.

| Recurso | Limite | Consecuencia de excederlo |
|---------|--------|---------------------------|
| Archivo individual | 20K chars | Truncamiento silencioso |
| Bootstrap total | 150K chars | Truncamiento silencioso |
| Skills | Sin limite fijo | Lazy-load: se cargan solo cuando se invocan |

**Implicaciones para el diseno del agente:**

- AGENTS.md < 17K chars (margen de seguridad)
- Todo lo que sea "procedimiento especializado" va a skills/ (lazy-load)
- KBs van como archivos de referencia, no en bootstrap
- La notacion formal (coalgebras, fibraciones) se remueve — el LLM no la necesita para operar

Si un agente no cabe en 150K de bootstrap, la especificacion es demasiado grande. Comprimir, particionar en skills, o repensar el alcance.

---

## P10 — Sidecar cuando hay runtime externo, no cuando no

No todo agente necesita un sidecar. La decision:

| El agente necesita... | Solucion |
|----------------------|----------|
| Solo conversar | Gateway solo, sin sidecar |
| Ejecutar codigo (CLI, scripts) | `code_execution` nativo de OpenClaw |
| Persistir estado en base de datos | Sidecar HTTP (Python, Go, etc.) |
| Acceder a API externa | `web_fetch` o `exec curl` — no necesita sidecar |
| Navegar web | Browser headless integrado en OpenClaw |

**Korax** necesita sidecar (PCA con SQLite). **Steipete** no — es puramente conversacional + exec de obreros.

Un sidecar agrega complejidad: segundo container, healthcheck, networking interno, backup de datos. Solo justificado cuando el agente necesita un runtime que no existe dentro de OpenClaw (ej: SQLite con 22 endpoints custom, procesamiento de imagenes, etc.).

---
