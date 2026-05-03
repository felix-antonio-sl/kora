---
_manifest:
  urn: urn:ops:kb:principios-transmutacion-kora-openclaw-p02
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
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:ops:kb:principios-transmutacion-kora-openclaw
relations:
  cites:
  - urn:kora:kb:autoria-spec
  - urn:ops:kb:deploy-agente-kora-en-openclaw
  - urn:ops:kb:federacion-kora-v2
  - urn:ops:kb:ux-telegram-openclaw
---


# Principios de transmutacion KORA → OpenClaw - Parte 02

## P11 — El agente auto-modifica su workspace

OpenClaw permite que el agente escriba en su propio workspace en runtime. Esto genera **drift** — el workspace desplegado diverge del repo KORA.

Tipos de drift:

| Tipo | Ejemplo | Evaluacion |
|------|---------|-----------|
| Regla emergente | Agente agrega ANTI-04 a su AGENTS.md | Evaluar y backportear al repo si es valiosa |
| Artefacto residual | Screenshot de test en workspace | Limpiar |
| Memory | Archivos en `memory/` | Normal — es el proposito del directorio |
| HEARTBEAT.md | OpenClaw lo crea/modifica | Normal — es config de runtime |

**Patron de gestion del drift:**

1. Auditar periodicamente: `diff <(strip_fm repo/file) workspace/file`
2. Si el drift es una mejora, backportear al repo
3. Si es residuo, limpiar
4. Nunca sobreescribir el workspace desplegado sin verificar drift — puede destruir reglas que el agente aprendio

---

## P12 — Auth y secrets son state de runtime, no config declarativa

Los tokens OAuth, API keys, y gateway tokens son state que OpenClaw gestiona en runtime. No pertenecen al `openclaw.json5` del host.

```
Host (declarativo) Runtime (state)
────────────────── ───────────────
openclaw.json5 auth.profiles (generado por setup-token)
.env (TELEGRAM_BOT_TOKEN, etc.) gateway.auth.token (auto-generado)
 meta.lastTouchedVersion
 commands (auto-detectado)
```

Consecuencias:

- Nunca commitear tokens en repos
- `.env` tiene chmod 600, cada compose dir tiene el suyo
- El script de sync preserva las keys de runtime (P6)
- Si re-deployeas desde cero, necesitas re-ejecutar `setup-token`

---

## P13 — Validar antes de desplegar, diagnosticar antes de actuar

Dos principios operacionales que se aplican en cascada:

**Pre-deploy:**
```bash
kora validate --profile strict # ¿Workspace KORA valido?
docker compose config --quiet # ¿Compose YAML valido?
openclaw doctor # ¿Config OpenClaw valido?
```

**Post-deploy:**
```bash
docker compose ps # ¿Containers healthy?
docker compose logs # ¿Gateway arrancó?
# Test end-to-end via Telegram # ¿Cadena completa funciona?
```

Nunca hacer `docker compose up -d` sin haber pasado por `openclaw doctor` primero. Doctor detecta schema migrations, keys invalidos, permisos de filesystem, y conflictos de seguridad que un `up` convierte en crashloop silencioso.

---

## P14 — Federation cross-gateway via hooks nativos

OpenClaw no tiene federación nativa entre gateways. La comunicación cross-gateway se construye sobre `POST /hooks/agent` (endpoint HTTP que cada gateway expone) + DNS de Docker bridge (`kora-federation`). Cada agente usa `web_fetch` para derivar casos a otros gateways.

Requisitos: `hooks.enabled: true` + token literal en `openclaw.json5` (no interpola `${ENV_VAR}`). Mismo token para todos los gateways simplifica derivaciones. Cada agente necesita instrucciones de derivación en su TOOLS.md + acceso al directorio de federación (`/home/node/shared/federation/directorio-agentes.md`).

Referencia completa: `urn:ops:kb:federacion-kora-v2`.

---

## P15 — bind=lan para containers Docker en bridge

`gateway.bind: "loopback"` (default) escucha en `127.0.0.1` dentro del container. Otros containers en la misma bridge Docker no pueden alcanzarlo — el tráfico llega por `eth0`, no por loopback. Usar `"lan"` para escuchar en `0.0.0.0` dentro del container.

La seguridad del host la da el port mapping Docker (`127.0.0.1:{port}:{port}` — solo accesible desde localhost en el host). No expone el gateway a internet.

Necesario para: hooks cross-gateway (P14), panel web que consulta gateways desde kora-federation, cualquier comunicación inter-container.

---

## P16 — Config UX de canal como parte del deploy

La configuración del canal de mensajería (Telegram, Discord, etc.) tiene impacto directo en la experiencia del usuario. Defaults de OpenClaw son subóptimos para Telegram:

- `chunkMode: "newline"` fragmenta respuestas en muchas burbujas → cambiar a `"length"`
- `markdown.tables: "code"` renderiza tablas ilegibles en móvil → cambiar a `"bullets"`
- `replyToMode: "off"` sin threading visual → cambiar a `"first"`

La config UX no es cosmética — afecta si el usuario puede consumir las respuestas del agente. Debe ser parte del checklist de deploy, no un ajuste posterior.

Referencia completa: `urn:ops:kb:ux-telegram-openclaw`.

---

## Mapa de decisiones

```
¿El agente KORA tiene AGENTS.md + SOUL.md + TOOLS.md?
 NO → no es un agente valido, no se puede transmutar
 SI ↓

¿Necesita servicio externo con estado persistente?
 SI → sidecar HTTP (P10)
 NO → gateway solo

¿Las KBs caben en 150K de bootstrap?
 SI → copiar al workspace
 NO → mount RO separado (P8)

¿El agente necesita escribir codigo?
 SI → mount RW del proyecto target + code_execution (P4)
 NO → mount RO de referencia o sin mount

¿Necesita canal de mensajeria?
 SI → configurar channel en openclaw.json5 + bot token + UX config (P16)
 NO → gateway solo HTTP (para automatizacion sin humano)

¿Necesita proactividad autonoma?
 SI → heartbeat + cron jobs (P9 del tutorial)
 NO → solo reactivo (responde cuando le hablan)

¿Necesita comunicarse con otros agentes?
 SI → hooks cross-gateway (P14) + bind=lan (P15) + directorio federation
 NO → gateway aislado
```

---

## Referencias

- Tutorial paso a paso: `urn:ops:kb:deploy-agente-kora-en-openclaw`
- Federación cross-gateway: `urn:ops:kb:federacion-kora-v2`
- Config UX Telegram: `urn:ops:kb:ux-telegram-openclaw`
- Documentacion oficial OpenClaw: `
- Spec de agentes KORA: `urn:kora:kb:autoria-spec`
