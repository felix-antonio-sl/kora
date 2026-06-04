---
_manifest:
  urn: urn:kora:artefacto:kora-agentic-lifecycle
  type: artefacto
  provenance:
    created_by: OpenAI Codex
    created_at: '2026-06-03'
    source: Construccion fresca solicitada por el operador para cubrir el ciclo
      de vida conjunto de skills KORA y agents KORA. Parte de gobernanza,
      harness-spec, autoria-spec y runtime specs vigentes; no deriva del stack
      meta-KORA historico ni de lifecycle-orchestrator archivado. v1.0.1 alinea
      entornos_objetivo y conocimiento permitido con la reactivacion canonica
      de OpenCode en gobernanza v6.2.
version: 1.0.1
status: activo
nombre: kora-agentic-lifecycle
descripcion: "Gestiona el ciclo de vida completo de agentes y skills KORA:
  descubrir, crear, editar, mantener, auditar, promover, versionar, transmutar,
  deployar, deprecar y retirar artefactos agenticos sin tratar outputs runtime
  como fuente."
tags:
- kora
- ciclo-vida
- agentes
- skills
- autoria
- mantenimiento
- transmutacion
- deploy
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
      - 1
      - 3
      - 3
      - 1
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - openclaw
    - opencode
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:kora:kb:gobernanza
    - urn:kora:kb:host-roles
    - urn:kora:kb:harness-spec
    - urn:kora:kb:autoria-spec
    - urn:kora:kb:md-spec
    - urn:kora:kb:knowledge-spec
    - urn:kora:kb:qa-spec
    - urn:kora:kb:risk-register-spec
    - urn:kora:kb:runtime-spec-md
    - urn:kora:kb:multiagente-spec
    - urn:kora:kb:transmutation-spec
    - urn:kora:kb:claude-code-runtime-extension
    - urn:kora:kb:codex-runtime-extension
    - urn:agengai:kb:openclaw-runtime-extension
    - urn:kora:kb:opencode-runtime-extension
    - urn:kora:kb:hermes-runtime-extension
    - urn:kora:kb:meta-kora-rebuild-directive
    componible_con:
    - urn:kora:artefacto:kora-agents
    - urn:kora:artefacto:kora-skills
    - urn:kora:artefacto:custodio-kora
    - urn:kora:artefacto:transmute-claude-code
    - urn:kora:artefacto:transmute-openclaw
    - urn:kora:artefacto:cat-thinking
artefacto:
  perfil:
    dominio:
    - kora
    - agentes
    - skills
    - lifecycle
    - autoria
    - transmutacion
    - deploy
    disparadores:
    - el operador pregunta si existe capacidad KORA para construir o mantener agents y skills
    - hay que crear, editar, promover, transmutar o retirar un AGENT.md o SKILL.md
    - un artefacto agentico productivo tiene drift entre fuente, catalogo, build o runtime instalado
    - hay que decidir si una capacidad debe ser habilidad, subagente, agente o plataforma
    - hay que limpiar targets pausados, outputs derivados obsoletos o deuda de staging
    salidas:
    - diagnostico de cobertura con fuente, status, version, targets, builds e instalaciones locales
    - plan de lifecycle con accion, owner, gates, rollback y deuda residual
    - patch minimo sobre AGENT.md, SKILL.md, fibras auxiliares, tests o docs de soporte
    - transmutaciones regeneradas en _BUILD para targets canonicos activos
    - resultado de gates y decision final ready, active, needs_repair, blocked, deprecated o retired
  plan:
    estado_inicial: triaje-lifecycle
    estado_terminal: cierre-verificado
    estados:
    - triaje-lifecycle
    - cargar-canon
    - inventariar-artefacto
    - clasificar-forma-material
    - disenar-cambio
    - aplicar-cambio
    - verificar-gates
    - transmutar-deployar
    - cierre-verificado
  interfaz:
    herramientas:
    - Read
    - Grep
    - Glob
    - Bash
    - Write
    permisos: Lectura del canon KORA y escritura acotada a artifacts/agents/,
      artifacts/skills/, tests, docs auxiliares y outputs _BUILD derivados cuando
      el operador pide mantenimiento agentico. Deploy local solo con comando
      explicito o cuando el objetivo lo requiere; no pushea por si misma.
    protocolos:
      entrada: solicitud de ciclo de vida, path, URN, nombre de agente/skill o requerimientos
      salida: inventario, patch, transmutacion, deploy dry-run/apply, gates y cierre operativo
  invariantes:
    reglas_duras:
    - Resolver y leer las URNs canonicas relevantes antes de cambiar un artefacto agentico.
    - Aplicar precedencia estricta; gobernanza y autoria-spec mandan sobre artefactos y builds.
    - No usar lifecycle-orchestrator, kora-agents legacy, kora-skills legacy ni otros meta-KORA historicos como fuente de diseno.
    - Mantener fuente primaria en AGENT.md o SKILL.md; _BUILD y runtimes instalados son derivados regenerables.
    - Clasificar forma material antes de editar; una habilidad no debe esconder workspace, memoria ambiental ni servicio.
    - No declarar runtimes pausados en entornos_objetivo; agentskills solo se usa como compatibilidad o con --force-paused e HITL.
    - Versionar cuando cambia contrato, interfaz, targets o comportamiento observable; no bumpear por regenerar builds identicos.
    - Promocion, deprecacion y retiro deben dejar status, ubicacion, catalogo y builds coherentes.
    - Ejecutar gates proporcionales y reportar comandos; si fallan, cerrar como needs_repair o blocked.
    - Deploy local debe distinguir dry-run de apply y declarar destino runtime.
    compromisos_eticos:
      transparencia: Separar hecho verificado, inferencia y recomendacion de cambio.
      responsabilidad: Declarar impacto, rollback y deuda residual antes de promocion o deploy.
---

# kora-agentic-lifecycle

## Proposito

Gestionar el ciclo de vida completo de agentes y skills KORA. Esta skill coordina
descubrimiento, creacion, edicion, mantenimiento, auditoria, promocion,
versionado, transmutacion, deploy local, deprecacion y retiro de artefactos
agenticos, manteniendo la fuente en `AGENT.md` o `SKILL.md`.

No reemplaza a `kora-agents` ni `kora-skills`: las usa como capacidades
especializadas. Esta skill decide el flujo end-to-end y asegura que fuente,
catalogo, `_BUILD/` e instalaciones runtime no diverjan sin declararlo.

## Cuando Usar

- Preguntar si KORA ya tiene una capacidad para construir o mantener agents y skills.
- Crear, reconstruir, editar o reparar un `AGENT.md` o `SKILL.md`.
- Promover material desde `_FRAGUA/` o `_TALLER/` a productivo.
- Regenerar transmutaciones despues de un cambio de fuente.
- Revisar drift entre `entornos_objetivo`, `_BUILD/`, catalogo e instalaciones locales.
- Deprecar, retirar o reactivar un artefacto agentico.

## Cuando No Usar

- Editar knowledge KORA/MD puro: usar la ruta de knowledge y `custodio-kora`.
- Disenar contenido de dominio sin tocar lifecycle agentico: usar la skill de dominio.
- Saltar directo a un runtime externo sin fuente KORA canonica.
- Resucitar artefactos meta-KORA historicos como blueprint.

## Workflow

1. Clasificar el intent: `descubrir`, `crear`, `editar`, `mantener`,
   `promover`, `transmutar`, `deployar`, `deprecar`, `retirar` o `bloqueado`.
2. Cargar canon minimo: `gobernanza`, `harness-spec`, `autoria-spec`,
   `runtime-spec-md`, `transmutation-spec` y la runtime-extension aplicable.
3. Inventariar estado: fuente, status, version, URN, targets declarados,
   `_BUILD/`, catalogo, instalaciones locales y staging/archivo relacionado.
4. Clasificar forma material. Si `forma_material=habilidad`, delegar criterios
   de construccion a `kora-skills`; si es agente/subagente/plataforma, delegar a
   `kora-agents`.
5. Disenar cambio minimo: campos, versionado, transmutaciones, deploy, rollback
   y deuda residual.
6. Aplicar cambio sobre fuente primaria y fibras auxiliares, nunca sobre runtime
   como autoridad.
7. Ejecutar gates proporcionales:
   `python3 toolchain/kora check --strict --path <subtree>` cuando aplique,
   `python3 toolchain/kora check --strict`, `python3 toolchain/kora index` y
   tests relevantes si se toco toolchain o specs.
8. Transmutar targets activos con `python3 toolchain/kora transmute --target ...`.
   Usar `deploy-builds --dry-run` antes de `--apply` cuando el objetivo incluya
   instalacion local.
9. Cerrar con estado: `ready`, `active`, `needs_repair`, `blocked`,
   `deprecated`, `retired` o `rerouted`.

## Politica De Targets

Targets canonicos activos: `claude-code`, `codex`, `openclaw`, `hermes`,
`opencode`.
Mientras `hermes-runtime-extension` siga en stub, declararlo solo cuando la
runtime-extension sostenga el caso concreto. Targets pausados (`agentskills`,
`gemini`, `mastra`) no van en `entornos_objetivo`; agentskills
queda como compatibilidad estructural de habilidades y puede verificarse por
gate, no como runtime canonico.

## Reglas Duras

- `docs/generated/*` se regenera, no se edita como fuente.
- `_BUILD/` se puede borrar o regenerar; no justifica el contenido fuente.
- Un cambio de contrato observable exige version bump.
- Un deploy local debe declarar destino (`~/.codex`, `~/.claude`, workspace
  OpenClaw) y si fue dry-run o apply.
- Si el artefacto existente contradice gobernanza o autoria-spec, se corrige el
  artefacto o se declara deuda; no se relaja la spec por conveniencia.

## Salida Esperada

Un cierre operativo con inventario, cambios aplicados, transmutaciones
regeneradas, gates ejecutados, estado final y deuda residual.
