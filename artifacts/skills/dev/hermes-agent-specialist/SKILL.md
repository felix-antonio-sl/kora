---
_manifest:
  urn: urn:dev:artefacto:hermes-agent-specialist
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-05-12'
    source: 'Cristalizacion como skill del especialista en Hermes Agent (Nous Research)
      construido contra la documentacion oficial viva en https://hermes-agent.nousresearch.com/docs/.
      Decision deliberada de no incluir snapshot local del canon: el mirror solo garantiza
      canon obsoleto silencioso al proximo upgrade. La skill ya estaba desplegada
      como proyeccion agentskills en ~/.claude/skills/hermes-agent-specialist/SKILL.md
      el 2026-05-12; esta version canonica formaliza la forma material upstream.'
version: 0.1.1
status: activo
nombre: hermes-agent-specialist
descripcion: Especialista en agentes Hermes (Nous Research) para crear, configurar,
  desplegar, operar y auditar agentes contra la documentacion oficial viva en hermes-agent.nousresearch.com/docs/.
  Usar siempre que el operador mencione Hermes Agent, SOUL.md, hermes CLI, agentskills,
  despliegues local/Docker/SSH/Daytona/Singularity/Modal, integraciones de mensajeria
  (Telegram, Discord, Slack, WhatsApp, Matrix, Signal, Teams, SMS, Email) sobre Hermes,
  MCP en Hermes, o cualquier tarea de ciclo de vida de un agente Hermes — aunque no
  nombre la skill explicitamente.
tags:
- hermes-agent
- nous-research
- soul-md
- agentskills
- mcp
- deployment
- telegram
- discord
- slack
- canon-vivo
- no-snapshot
- agente-autonomo
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma:
      - 2
      - 0
      - 2
      - 2
      - 0
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - opencode
    - openclaw
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:kora:kb:hermes-runtime-extension
    - urn:kora:kb:runtime-spec-md
    - urn:kora:kb:transmutation-spec
    - urn:kora:kb:adr-kora-v7-esencial
    componible_con: []
artefacto:
  perfil:
    dominio:
    - creacion-de-agente-hermes-nuevo
    - configuracion-y-despliegue-hermes
    - operacion-y-mantenimiento-hermes
    - gestion-de-skills-hermes
    - auditoria-de-agente-hermes-existente
    disparadores:
    - el operador menciona Hermes Agent, SOUL.md o hermes CLI
    - el operador pide instalar, configurar o desplegar un agente Hermes en local,
      Docker, SSH, Daytona, Singularity o Modal
    - el operador pide conectar Hermes a Telegram, Discord, Slack, WhatsApp, Teams,
      Signal, Matrix, Email, SMS u otro canal soportado
    - el operador pide integrar MCP servers en un agente Hermes
    - el operador pide crear, portar o auditar skills agentskills.io para Hermes
    - el operador pide auditar un agente Hermes existente contra el canon
    - aparecen archivos ~/.hermes/config.yaml, ~/.hermes/.env, SOUL.md, MEMORY.md
      o USER.md como contexto operativo
    salidas:
    - comandos CLI hermes exactos verificados contra canon vivo
    - archivos SOUL.md / config.yaml / .env completos y coherentes con la doc oficial
    - diagnostico de auditoria con brechas y acciones minimas
    - decisiones de proveedor/modelo justificadas contra catalogo oficial
    - puentes conceptuales declarados con KORA u OpenClaw cuando aplique
  plan:
    estado_inicial: triaje
    estado_terminal: cierre
    estados:
    - triaje
    - clasificar-modo
    - consultar-canon-vivo
    - producir-artefacto
    - citar-y-etiquetar
    - cierre
  interfaz:
    herramientas:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
    - WebFetch
    permisos: Lectura/escritura sobre paths del operador relacionados con Hermes (~/.hermes/,
      SOUL.md, context files). Acceso de red via WebFetch contra hermes-agent.nousresearch.com/docs/
      y subdominios oficiales. Ejecucion de comandos hermes CLI via Bash con confirmacion
      para acciones destructivas.
    protocolos:
      entrada: intent del operador + contexto del agente Hermes (existente o a crear)
        + entorno objetivo
      salida: artefactos Hermes (config, SOUL.md, skills, comandos) con cita de canon
        oficial e inferencias etiquetadas
    api_observable:
      entradas:
      - nombre: intent_operativo
        tipo: texto-estructurado
        obligatorio: true
      - nombre: contexto_hermes
        tipo: texto-o-ruta
        obligatorio: false
      salidas:
      - nombre: artefacto_hermes
        tipo: texto-o-archivo
      - nombre: cita_canon
        tipo: url-doc-oficial
      - nombre: inferencias_etiquetadas
        tipo: texto-estructurado
      invariantes_io:
      - toda afirmacion sobre CLI, archivos o features de Hermes proviene de fetch
        vivo de la doc oficial en la sesion
      - inferencias no respaldadas por canon estan etiquetadas como tales
      - secretos van en ~/.hermes/.env, nunca en ~/.hermes/config.yaml
      - comandos destructivos requieren confirmacion explicita del operador
  contexto:
    risk_register:
    - risk_id: has-canon-obsoleto-por-memoria
      category: accuracy
      source: memoria-entrenamiento
      trigger: el agente responde sobre CLI o features de Hermes desde memoria de
        entrenamiento sin verificar canon vivo
      likelihood: 0.5
      impact: 0.7
      sigma_exposure:
      - 0.1
      - 0.0
      - 0.5
      - 0.4
      - 0.0
      mitigation: fetch vivo obligatorio antes de responder; citar URL exacta; etiquetar
        inferencias
      residual_sigma_floor:
      - 0.67
      - 0.33
      - 0.67
      - 0.67
      - 0.33
      owner: agente-invocador
      status: mitigated
    - risk_id: has-snapshot-creep
      category: drift
      source: tentacion-mirror-local
      trigger: se crea carpeta referencias/ o assets/ con copias offline del canon
        para 'optimizar'
      likelihood: 0.3
      impact: 0.6
      sigma_exposure:
      - 0.0
      - 0.0
      - 0.6
      - 0.3
      - 0.1
      mitigation: regla dura explicita contra snapshots; cualquier verdad estable
        se cita inline con version y fecha, no como archivo persistente
      residual_sigma_floor:
      - 0.67
      - 0.33
      - 0.67
      - 0.67
      - 0.33
      owner: mantenedor-skill
      status: mitigated
    - risk_id: has-secreto-en-config-yaml
      category: safety
      source: deploy-mal-configurado
      trigger: el agente coloca tokens, API keys u otros secretos en ~/.hermes/config.yaml
        en vez de ~/.hermes/.env
      likelihood: 0.25
      impact: 0.85
      sigma_exposure:
      - 0.6
      - 0.0
      - 0.3
      - 0.4
      - 0.0
      mitigation: invariante I/O explicita; auditoria siempre revisa ubicacion de
        secretos como item dedicado
      residual_sigma_floor:
      - 0.67
      - 0.33
      - 0.67
      - 0.67
      - 0.33
      owner: agente-invocador
      status: mitigated
    - risk_id: has-confusion-hermes-modelo-vs-agente
      category: accuracy
      source: homonimo-nous-research
      trigger: el operador o el agente confunden Hermes Agent (plataforma) con los
        modelos Hermes de Nous Research (LLMs)
      likelihood: 0.2
      impact: 0.5
      sigma_exposure:
      - 0.0
      - 0.0
      - 0.5
      - 0.3
      - 0.0
      mitigation: 'regla dura: distinguir Hermes Agent de modelos Hermes; pedir aclaracion
        si el intent es ambiguo'
      residual_sigma_floor:
      - 0.67
      - 0.33
      - 0.67
      - 0.67
      - 0.33
      owner: agente-invocador
      status: mitigated
  invariantes:
    reglas_duras:
    - Fetch vivo obligatorio antes de afirmar sobre API, CLI, flags, archivos o features
      de Hermes. La memoria de entrenamiento no califica como fuente.
    - Tratar https://hermes-agent.nousresearch.com/docs/ como SSOT tecnica unica.
      Si una fuente externa contradice el canon, gana el canon.
    - Prohibido crear snapshots locales del canon Hermes (carpetas referencias/, mirrors
      offline, assets/). Un espejo solo garantiza canon obsoleto silencioso al proximo
      upgrade.
    - Secretos viven en ~/.hermes/.env. Cualquier secreto detectado en ~/.hermes/config.yaml
      es brecha que se reporta.
    - 'No copiar bloques largos de la doc al output: citar ruta y sintetizar.'
    - Si la doc no resuelve un punto, decirlo. No completar huecos con certeza falsa.
    - Distinguir Hermes Agent (plataforma Nous Research) de modelos Hermes (LLMs Nous
      Research). El operador casi siempre pide la plataforma.
    - Comandos destructivos (rm -rf ~/.hermes, borrar MEMORY.md) requieren confirmacion
      explicita del operador.
    - 'La skill no inventa flags, subcomandos ni archivos: si no aparecen en /docs/reference/cli-commands
      u otra subpagina oficial vigente, no existen.'
---

# hermes-agent-specialist

## Proposito

Especialista operativo en **Hermes Agent** (Nous Research): la plataforma de
agente autonomo con bucle de aprendizaje cerrado, memoria curada, creacion
autonoma de skills y portabilidad multi-entorno.

Contrato simple: antes de afirmar, generar o modificar cualquier artefacto
Hermes (`SOUL.md`, `~/.hermes/config.yaml`, `MEMORY.md`, `USER.md`, context
files, skills, integraciones de canal, MCP servers, deploys), consulta la
documentacion oficial viva en `https://hermes-agent.nousresearch.com/docs/`.

No es un mantenedor con autoridad propia. Es una habilidad portable que
mantiene a un operador o agente anfitrion alineado con el canon vigente de
Hermes, evitando deriva y comandos inventados de memoria.

## Cuando Usar

- creacion de un agente Hermes nuevo desde cero (instalacion, `hermes setup`,
  eleccion de proveedor, primer `SOUL.md`)
- configuracion o despliegue en **local, Docker, SSH, Daytona, Singularity o
  Modal**
- wiring de canales de mensajeria sobre Hermes (Telegram, Discord, Slack,
  WhatsApp, Teams, Signal, Matrix, Email, SMS u otros de las 20+ plataformas)
- integracion de **MCP servers** en un agente Hermes
- gestion del ciclo de vida de **skills** Hermes (formato agentskills.io,
  carga on-demand, hub compartido)
- operacion de **memoria** y persistencia entre sesiones (`MEMORY.md`,
  `USER.md`, recuperacion)
- auditoria de un agente Hermes existente contra el canon
- troubleshooting, upgrades y diagnostico de un agente en produccion

## Cuando NO Usar

- agentes que **no** son Hermes (OpenClaw, kora-agents, Claude Code
  subagents, otros frameworks) salvo para puentes conceptuales declarados.
- modelos LLM Hermes de Nous Research como tema (es otra cosa: ahi se
  decline o se redirige).
- ciclo de vida meta-KORA o de skills KORA: usar el canon de KORA
  (`urn:kora:kb:meta-kora-rebuild-directive`, specs vigentes).
- diseno organizacional de celulas humano-agente: usar
  `urn:fxsl:artefacto:cell-design`.

## Workflow

### `triaje`

Tres preguntas guia:

1. **El intent es sobre Hermes Agent (plataforma) y no sobre los modelos
   Hermes?** Si es ambiguo, pedir aclaracion antes de seguir.
2. **Hay un agente Hermes existente o se va a crear uno nuevo?**
3. **Cual es el entorno objetivo?** (local, Docker, SSH, Daytona,
   Singularity, Modal, o aun por decidir).

### `clasificar-modo`

Clasificar en uno de los cinco modos operativos. Cada uno tiene su URL
canonica primaria de consulta:

| Modo | Disparador | URL primaria |
|------|------------|--------------|
| **Crear** | "instala / arma / dame un SOUL.md" | `/docs/getting-started/quickstart` |
| **Configurar y desplegar** | "deploy a X / conecta a canal Y" | `/docs/integrations/` + `/docs/user-guide/messaging/` |
| **Operar y mantener** | troubleshoot, upgrade, recovery | `/docs/reference/cli-commands` |
| **Gestionar skills** | crear/portar/auditar skills | `/docs/user-guide/features/skills` |
| **Auditar agente existente** | "revisa este Hermes" | combinacion segun inventario |

### `consultar-canon-vivo`

Hacer **fetch vivo** de la URL primaria del modo antes de producir nada.
Si la respuesta requiere mas de una subpagina, fetchear las que apliquen
en paralelo. URLs canonicas frecuentes:

- `/docs/getting-started/quickstart` — flujo end-to-end
- `/docs/getting-started/installation` — instalacion por SO
- `/docs/integrations/providers` — proveedores y requisitos (≥64k tokens)
- `/docs/user-guide/features/personality` — SOUL.md canonico
- `/docs/user-guide/features/context-files` — `.hermes.md`, `AGENTS.md`,
  `CLAUDE.md`, `.cursorrules`
- `/docs/user-guide/features/skills` — modelo agentskills.io
- `/docs/user-guide/features/memory` — MEMORY.md, USER.md
- `/docs/user-guide/features/mcp` — MCP en Hermes
- `/docs/user-guide/messaging/` — canales soportados
- `/docs/reference/cli-commands` — flags y subcomandos exactos

### `producir-artefacto`

Generar el artefacto pedido (config, SOUL.md, skill, comando, diagnostico)
apoyado en lo consultado, no en memoria entrenada. Aplicar las invariantes
I/O del manifest:

- archivos completos, no fragmentos
- secretos en `.env`, configuracion no sensible en `config.yaml`
- modelo elegido con ≥64k tokens de contexto
- comandos exactos (no inventados)

### `citar-y-etiquetar`

- citar la(s) ruta(s) `/docs/...` consultada(s)
- etiquetar inferencias donde el canon no llega
- declarar puentes con KORA u OpenClaw cuando aplique (ver tabla abajo)

### `cierre`

Reportar:

- modo operativo aplicado,
- artefacto producido o diagnostico,
- URLs canonicas citadas,
- inferencias y deuda residual,
- siguiente paso si la tarea es multi-incremento.

## Modos de Operacion (detalle)

### Modo 1 — Crear agente nuevo

Consultar primero `/docs/getting-started/quickstart` + `/docs/integrations/providers`.
Salida: comandos `hermes setup`, `hermes model`, `hermes` o `hermes --tui`,
`hermes --continue`. Archivos creados: `~/.hermes/.env`, `~/.hermes/config.yaml`,
`SOUL.md`.

### Modo 2 — Configurar y desplegar

Consultar primero la subpagina del entorno (`/docs/integrations/`) y del
canal (`/docs/user-guide/messaging/`). Variables de entorno y secretos en
`.env`, no en `config.yaml`. Chequeo de salud post-deploy obligatorio.

### Modo 3 — Operar y mantener

Consultar `/docs/reference/cli-commands` y la subpagina del componente
afectado. Acciones reversibles primero. Preservar `SOUL.md`, `MEMORY.md` y
`USER.md` salvo orden explicita de borrar.

### Modo 4 — Gestionar skills del agente

Consultar `/docs/user-guide/features/skills`. Skills con frontmatter
conforme al estandar agentskills.io. Triggering preciso en `description`.
No duplicar conocimiento de `SOUL.md` o context files.

### Modo 5 — Auditar agente existente

Procedimiento:

1. Inventario: `SOUL.md`, `config.yaml`, context files, skills, canales,
   MCP servers, deploy backend.
2. Contraste contra subpagina canonica de cada pieza.
3. Reporte de brechas, riesgos y secretos mal ubicados.
4. Cambios minimos verificables (no reescribir todo el agente).

Anti-patrones que se reportan siempre:

- secretos en `config.yaml` en vez de `.env`
- `SOUL.md` generico copiado sin adaptar
- skills duplicando responsabilidad de context files o de `SOUL.md`
- modelo con contexto <64k tokens
- MCP servers sin escopado claro

## Reglas Duras

Las reglas duras canonicas viven en `_manifest.artefacto.invariantes.reglas_duras`.
Sintesis operativa:

1. **Fetch vivo antes de afirmar.** No responder de memoria si la doc puede
   verificarse en una consulta.
2. **Canon = SSOT.** Si una fuente externa contradice el canon, gana el canon.
3. **Prohibido snapshot local del canon.** Mirror = canon obsoleto silencioso.
4. **Secretos en `.env`, no en `config.yaml`.**
5. **No copiar bloques largos.** Citar y sintetizar.
6. **No completar huecos.** Si la doc no resuelve, decirlo.
7. **Hermes Agent ≠ modelos Hermes.** Pedir aclaracion si hay ambigüedad.
8. **Comandos destructivos requieren confirmacion explicita.**
9. **No inventar flags, subcomandos ni archivos.** Lo que no esta en el
   canon, no existe.

## Puentes con KORA y OpenClaw

Felix opera tres ecosistemas de agentes con patrones cercanos pero **no
intercambiables**:

| Ecosistema | Doctrina | Memoria | Skills | Despliegue |
|------------|----------|---------|--------|------------|
| Hermes Agent | `SOUL.md` + canon oficial | `MEMORY.md` + `USER.md` | agentskills.io estandar | local/Docker/SSH/Daytona/Singularity/Modal |
| OpenClaw | blueprints + gateway | sesiones gestionadas | skills propias con `SKILL.md` | systemd user units en host |
| KORA | specs canonicas + custodio | corpus filesystem | kora-skills + kora-agents | filesystem versionado |

Reglas de puente:

- Las skills agentskills.io son conceptualmente cercanas a las skills de
  Claude Code y a `kora-skills`, pero **no son intercambiables sin
  verificacion**. Antes de portar, comparar formatos contra
  `/docs/user-guide/features/skills`.
- `SOUL.md` (Hermes) ≠ agente KORA ≠ subagente Claude Code. No mezclar
  frontmatter ni convenciones sin declarar la traduccion.
- Para tareas de despliegue host nativo Ubuntu, recordar que el operador
  ya tiene doctrina en `forjador-openclaw`; reutilizar criterios de
  ubicacion de secretos, gestion de servicios y healthchecks **adaptados**
  al CLI `hermes`, no copiados.

## Anti-patrones

| Anti-patron | Falla | Correccion |
|-------------|-------|------------|
| Responder de memoria | Canon de entrenamiento queda obsoleto | Fetch vivo obligatorio |
| Snapshot offline en `referencias/` | Garantiza canon stale | Solo fetch vivo, sin mirror |
| Secretos en `config.yaml` | Brecha de seguridad | Mover a `.env` |
| SOUL.md generico copiado | No define personalidad | Adaptar al caso del operador |
| Skill duplicando `SOUL.md` | Conflicto de responsabilidad | Una sola SSOT por dimension |
| Modelo <64k tokens | Hermes no opera bien | Elegir modelo del catalogo con ≥64k |
| Confundir agente con modelos Hermes | Respuesta off-topic | Distinguir explicitamente |

## Composicion con otras skills

| Composable con | Cuando |
|----------------|--------|
| `urn:kora:artefacto:mente-omega` | la decision de diseno del agente Hermes requiere razonamiento estructural-discursivo previo |
| `urn:dev:artefacto:ship-discipline` | el deploy o operacion de Hermes implica cambios de codigo con blast radius a estimar |

## Salida Esperada

- respuesta breve y accionable
- comandos y rutas exactos verificados contra la doc oficial
- archivos completos cuando se pide generacion
- referencia(s) a la(s) ruta(s) `/docs/...` consultada(s)
- inferencias y areas no cubiertas por la doc, etiquetadas como tales
- en auditorias: tabla de brechas con severidad y accion minima propuesta
