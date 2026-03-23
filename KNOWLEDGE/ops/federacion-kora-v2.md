---
_manifest:
  urn: "urn:ops:kb:federacion-kora-v2"
  provenance:
    created_by: "ops/clawstack + kora/curator"
    created_at: "2026-03-23"
    source: "Diseño e implementación de federation v2 sobre 3 gateways OpenClaw en Docker"
version: "1.0.0"
status: published
tags: [federacion, hooks, shared-storage, cross-gateway, panel, arquitectura, openclaw, docker]
lang: es
---

# Federación KORA v2 — Comunicación cross-gateway y storage compartido

Arquitectura para comunicación entre agentes OpenClaw desplegados en gateways Docker separados sobre una bridge network compartida (`kora-federation`). OpenClaw no tiene federación nativa entre gateways — esta arquitectura usa hooks HTTP nativos + DNS de Docker como bridge.

---

## Restricción fundamental

OpenClaw soporta comunicación inter-agente solo **dentro del mismo gateway** (`agentToAgent`, `sessions_spawn`). Entre gateways separados no hay mecanismo nativo. La federación se construye sobre:

- `POST /hooks/agent` — endpoint HTTP que cada gateway expone
- DNS de Docker bridge — los containers se resuelven por nombre en `kora-federation`
- `web_fetch` — tool nativa de OpenClaw disponible para todos los agentes

---

## Hooks cross-gateway

### Habilitación

Cada `openclaw.json5` requiere:

```json5
hooks: {
  enabled: true,
  token: "{token-compartido-entre-gateways}",
}
```

Token literal en config (OpenClaw no interpola `${ENV_VAR}` en JSON). Mismo token para todos los gateways simplifica derivaciones.

### Requisito Docker: bind=lan

`gateway.bind` debe ser `"lan"` (no `"loopback"`). Razón: `loopback` escucha en `127.0.0.1` dentro del container — otros containers no pueden alcanzarlo por la IP de Docker bridge. `lan` escucha en `0.0.0.0` dentro del container. La seguridad la da el port mapping de Docker (`127.0.0.1:{port}:{port}` en el host — no expuesto al exterior).

Referencia: docs oficiales OpenClaw `docs/gateway/configuration-reference.md`:
> Docker note: the default loopback bind listens on 127.0.0.1 inside the container. With Docker bridge networking, traffic arrives on eth0, so the gateway is unreachable. Use bind: "lan" to listen on all interfaces.

### Flujo de derivación

```
agente-origen detecta caso fuera de su dominio
  → lee directorio-agentes.md (montado RO en /home/node/shared/federation/)
  → identifica agente destino + gateway URL
  → informa al usuario: "Derivo a {destino} en {bot telegram}. La respuesta aparecerá allá."
  → web_fetch POST http://{container}:{port}/hooks/agent
    Authorization: Bearer {hooks-token}
    { "message": "[Derivación de {origen}] {contexto}", "name": "derivacion-{origen}" }
  → gateway destino recibe hook, ejecuta turno, responde en su canal Telegram
```

La respuesta aparece en el **bot Telegram del destino**, no en el del origen. Mismo usuario (mismo `allowFrom` ID).

### Reglas anti-loop

- No derivar en cadena (si recibes derivación y no es tu dominio, responde al usuario sin re-derivar)
- No derivar sin informar al usuario a qué bot ir
- Un solo destino por derivación
- Contexto completo para que el destino no pregunte de vuelta

---

## Storage compartido

### Estructura

```
/srv/kora/shared/
├── federation/           ← RO para todos, nadie escribe en runtime
│   └── directorio-agentes.md  ← inventario: quién, dónde, dominio, hook URL
├── {agent-id}/           ← RW para el agente dueño
├── {agent-id}/           ← ...
└── {agent-id}/           ← ...
```

### Mounts Docker por gateway

Cada compose monta:
- `../shared/federation:/home/node/shared/federation:ro` — siempre
- `../shared/{mi-id}:/home/node/shared/{mi-id}` — RW propio, siempre

Visibilidad cruzada (leer directorio de otro agente) es configurable: se agrega mount `:ro` del directorio ajeno. Requiere recrear container.

### Visibilidad

Controlada por bind mounts en docker-compose.yml. Todos los containers corren como uid 1000 (node) — no se puede distinguir por permisos Unix. El enforcement es a nivel de mount Docker (`ro`, `rw`, o no montado).

---

## Directorio de agentes

Archivo central en `/srv/kora/shared/federation/directorio-agentes.md`. Contiene por agente:
- Dominio detallado (qué acepta, qué rechaza)
- Gateway: container name + port + hook URL
- Canal Telegram (bot username)

Cada agente tiene instrucciones de derivación en su TOOLS.md que referencian este directorio.

---

## Panel web (kora.sanixai.com)

Dashboard unificado para operar la federación. Source: `~/projects/kora-panel/`.

### Stack

Node.js + Express + React (Vite). Container en redes `web` (Traefik) + `kora-federation` (alcanza gateways). Docker socket montado RO para leer estado + restart containers. Auth: basic auth via Traefik middleware.

### APIs

| Endpoint | Función |
|---|---|
| `GET /api/health` | Health de todos los gateways (RPC a cada uno) |
| `GET /api/containers` | Estado containers Docker |
| `GET /api/registry` | Registry de agentes (fuente de verdad del panel) |
| `GET /api/visibility` | Matriz de visibilidad cruzada |
| `POST /api/visibility` | Toggle visibilidad (persiste en registry.json) |
| `POST /api/hooks/:agent` | Derivación cross-gateway via hook |
| `GET /api/containers/:name/logs` | Logs de container (últimas N líneas) |
| `POST /api/containers/:name/restart` | Restart container via Docker API |
| `GET /api/shared/:agent` | Listado de archivos en shared/ |

### Registry

`registry.json` es la fuente de verdad del panel. Contiene: agentes (gateway, compose path, config, telegram, namespace, shared dir), matriz de visibilidad, hooks token.

---

## Agregar un nuevo agente a la federación

1. Transmutación (forgemaster): KORA workspace → OpenClaw artefactos
2. Deploy (clawstack): compose, config, volume, auth, restart
3. Crear directorio shared: `/srv/kora/shared/{nuevo-id}/`
4. Agregar mount shared/ al compose del nuevo gateway
5. Actualizar `directorio-agentes.md` con el nuevo agente
6. Agregar hooks config al openclaw.json5 del nuevo gateway
7. Agregar sección federación al TOOLS.md del nuevo workspace
8. Registrar en panel (registry.json)
9. Opcionalmente: agregar mounts de visibilidad cruzada a composes existentes
