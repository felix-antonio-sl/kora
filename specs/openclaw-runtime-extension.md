---
_manifest:
  urn: "urn:agengai:kb:openclaw-runtime-extension"
  provenance:
    created_by: "OpenAI"
    created_at: "2026-03-23"
    source: "KORA runtime-spec v3.6.0, OpenClaw official docs baseline 2026.3.22, repair of native OpenClaw transmutation/deploy contract"
version: "1.0.0"
status: published
tags: [spec, runtime, openclaw, extension, transmutacion, deploy]
lang: es
extensions:
  agengai:
    extends:
      - "urn:kora:kb:runtime-spec-md"
    precedence_tier: 4
    platform: "openclaw"
    baseline_docs_release: "2026.3.22"
---

# AGENGAI/OpenClaw-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension de namespace extiende `runtime-spec-md` para el target OpenClaw. Su funcion es fijar el contrato nativo de transmutacion, configuracion y despliegue sin convertir detalles efimeros de la plataforma en reglas fundacionales de KORA.

Esta extension **NO** reemplaza `runtime-spec-md`; agrega restricciones OpenClaw-specific sobre superficies nativas, contrato estructurado, instalaciones gestionadas, topologia y fronteras de estado operativo.

Traces to: formal/05 §1.2 (Bounded Lattice) ; formal/07 §4.2 (Compositional Preservation)

### 1.1 Alcance

Esta extension gobierna:

1. el principio `native-first` para OpenClaw
2. el contrato estructurado minimo que una transmutacion KORA -> OpenClaw **DEBE** emitir
3. la separacion entre workspace target, config nativa, instalaciones gestionadas y estado operativo
4. las topologias canonicas de deploy OpenClaw relevantes para agentes KORA
5. el uso de surfaces nativas de Skills, plugins, bundles, sandboxes y canales

## 2. Precedencia

1. Esta extension pertenece a la capa 4 de `gobernanza §3` aunque resida en `specs/`.
2. Si una regla de esta extension contradice `runtime-spec-md`, prevalece `runtime-spec-md` hasta que la contradiccion se resuelva explicitamente.
3. Release notes, docs oficiales o tutoriales de OpenClaw **NO DEBEN** alterar por si solos esta extension; pueden motivar su actualizacion.
4. Cuando OpenClaw cambie una superficie nativa relevante, esta extension **DEBE** actualizarse o declarar deprecacion explicita de la regla afectada.

## 3. Native-First

Para OpenClaw, el adapter **DEBE** preferir superficies nativas y estructuradas antes que emulaciones textuales.

### 3.1 Reglas

1. Behavior identitario del agente **DEBE** residir en el workspace target (`AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `TOOLS.md`, `skills/`).
2. Enforcement, policy y config runtime **DEBEN** proyectarse a la config nativa de OpenClaw (`agents.defaults`, `agents.list[]`, `tools.*`, `sandbox.*`, `bindings[]`, `channels.*`, `gateway.*` y superficies equivalentes).
3. `TOOLS.md` en OpenClaw **NO DEBE** usarse como fuente autoritativa de policy, deploy, mounts o enforcement.
4. Un adapter **NO DEBE** pedir al deployer reinterpretar texto libre del workspace para datos criticos que puedan declararse estructuradamente.
5. Si la fuente KORA no contiene datos suficientes para completar un campo critico del contrato, el adapter **DEBE** emitir `manual_inputs_required` o equivalente, y **NO DEBE** inventarlo por heuristica debil.

## 4. Contrato Estructurado OpenClaw

Toda transmutacion KORA -> OpenClaw destinada a configuracion o deploy posterior **DEBE** emitir un contrato estructurado autosuficiente.

### 4.1 Bloques minimos

El contrato **DEBE** separar al menos estos bloques:

| Bloque | Contenido minimo |
| ------ | ---------------- |
| `workspace_target` | artefactos bootstrap y skills locales que viviran en el workspace OpenClaw |
| `config_projection` | patch o projection de config nativa OpenClaw derivada de `config.json` |
| `managed_installs` | skills, plugins o bundles que deben instalarse por vias nativas |
| `deployment_hints` | topologia recomendada, sidecars, mounts RO/RW, prerequisitos y datos manuales faltantes |
| `runtime_exclusions` | estado operativo que queda explicitamente fuera del wrapper |

### 4.2 Reglas

1. `config_projection` **DEBE** ser consumible sin reinterpretar `TOOLS.md` ni otros bootstraps textuales.
2. `managed_installs` **DEBE** distinguir installs nativos de OpenClaw de skills locales materializados en `workspace_target`.
3. `deployment_hints` **DEBE** declarar explicitamente cuando un dato sigue siendo manual o dependiente del operador.
4. El deploy posterior **NO DEBE** derivar mounts RW, plugins requeridos, politica de federation o ACLs durables desde notas textuales si el contrato ya puede cargarlos.

## 5. Projection Rules

### 5.1 Config nativa

1. `config.json` KORA **DEBE** proyectarse a surfaces nativas OpenClaw y **NO DEBE** copiarse como texto ni como pseudo-bootstrap.
2. Los defaults de thinking, reasoning y fast mode **DEBEN** mapearse a `agents.defaults.*` o `agents.list[].*` cuando existan.
3. La politica de tools **DEBE** mapearse usando `tools.profile`, `tools.allow`, `tools.deny`, `tools.byProvider`, `tools.elevated` y surfaces equivalentes antes que texto instruccional.
4. La politica de sandbox **DEBE** mapearse a `agents.defaults.sandbox` o `agents.list[].sandbox`.
5. La politica de sub-agentes **DEBE** mapearse a `subagents.allowAgents`, `tools.sessions_spawn`, `tools.subagents` o surfaces equivalentes de OpenClaw.

### 5.2 Topologia

1. La topologia canonica por defecto **DEBE** ser `single-gateway-multi-agent`.
2. Un gateway aislado por agente **SOLO DEBERIA** recomendarse cuando exista una razon estructural: frontera de confianza, rescate operacional, aislamiento de estado o incompatibilidad real de routing.
3. Si se requieren multiples gateways en un mismo host, el contrato **DEBE** preferir `--profile` / `OPENCLAW_STATE_DIR` / `OPENCLAW_CONFIG_PATH` antes que layouts ad hoc.
4. Si el gateway corre en Docker bridge y debe ser alcanzable fuera del loopback del contenedor, `gateway.bind` **NO DEBE** quedar en `loopback`; **DEBE** proyectarse a `lan` o `custom` segun la topologia.
5. Cuando existan multiples gateways, el contrato **DEBE** reservar espacio suficiente entre puertos base para derived ports.

### 5.3 Telegram y ACL durable

1. Para bots de un solo operador, el contrato **DEBERIA** preferir `dmPolicy: "allowlist"` con `allowFrom` numerico explicito.
2. Pairing **PUEDE** bootstrappear acceso, pero **NO DEBERIA** ser la unica ACL durable si la plataforma permite persistir la allowlist en config.
3. Si se usan multiples cuentas Telegram, el contrato **DEBE** hacer explicito el `defaultAccount` o equivalente.

## 6. Managed Installs

### 6.1 Skills

1. Un Skill local KORA que forma parte del agente **PUEDE** materializarse en `workspace_target/skills/`.
2. Un Skill que OpenClaw puede obtener de forma nativa desde registry **DEBERIA** declararse en `managed_installs.skills` antes que copiarse como bundle ad hoc.

### 6.2 Plugins y bundles

1. Plugins OpenClaw **DEBEN** instalarse por superficies nativas (`openclaw plugins install`, marketplace o locator equivalente), no por copia silenciosa al workspace.
2. Bundles compatibles (Codex, Claude, Cursor u otros soportados por OpenClaw) **DEBEN** declararse como install gestionado cuando la capacidad deseada viva en el bundle y no en el workspace local del agente.
3. Ningun pipeline **DEBE** asumir auto-load implicito de plugin code ubicado en el workspace.
4. Hooks, plugins o bundles que requieran enable/trust explicito **DEBEN** declararlo en el contrato.

## 7. Runtime State

1. `auth-profiles.json`, sesiones, pairing stores, caches, volumes, secretos resueltos, state dirs y demas `Runtime State` **NO DEBEN** materializarse dentro del wrapper.
2. El deployer **DEBE** crear o reconciliar ese estado via surfaces nativas de OpenClaw, del host o del orquestador.
3. Metadata operacional mutable (por ejemplo federation overlays, registros vivos, scratch del operador) **NO DEBE** mutar los bootstraps del workspace target como atajo.
4. Si un dato operacional necesita persistencia repo-wide, **DEBE** backportearse al repo canonico o vivir en storage operativo separado; no en drift local del workspace desplegado.

## 8. Baseline 2026.3.11 -> 2026.3.22 Absorbida

Las siguientes superficies recientes se consideran absorbidas por esta extension y **PUEDEN** usarse como base normativa operacional para OpenClaw:

1. installs nativos de Skills via ClawHub
2. ClawHub-first y marketplace/bundle installs para plugins
3. defaults por agente para thinking, reasoning y fast mode
4. `imageGenerationModel` nativo
5. backends de sandbox `ssh` y `openshell`
6. browser `existing-session` con `userDataDir`
7. `controlUi.allowedOrigins` y endurecimiento de `trusted-proxy`
8. `channels.telegram.silentErrorReplies` y ACL durable por `allowFrom`

## 9. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| ----- | -------- | ----------- | --------------- |
| Native-first | Config, policy e installs usan surfaces nativas OpenClaw cuando existen | runtime | Corregir adapter |
| Contrato autosuficiente | El deploy/config no depende de reinterpretacion textual del workspace | manual | Completar contract |
| Projection segregada | Workspace, config projection, managed installs y runtime state no se colapsan | lint | Re-segregar artefactos |
| Gateway topology explicita | La topologia recomendada y sus prerequisitos quedan declarados | manual | Declarar topology hints |
| ACL durable | Telegram owner-bot usa allowlist durable o excepcion documentada | runtime | Ajustar config projection |
| Managed installs nativos | Plugins y bundles no se copian como pseudo-workspace | manual | Mover a managed installs |
| Runtime state excluido | Credenciales, sesiones y stores quedan fuera del wrapper | lint | Excluir estado mutable |

## 10. Migracion

### Contrato vigente v1

- OpenClaw se trata como runtime con surfaces nativas, no como destino de wrappers textuales monoliticos.
- La transmutacion entrega contrato estructurado autosuficiente.
- La topologia por defecto es un gateway con multiples agentes.
- Plugins, bundles y hooks viven por install/enable nativo; no por copia implicita al workspace.
- El estado operativo queda fuera del wrapper y del repo fuente.
