---
_manifest:
  urn: "urn:kora:kb:agentfile-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "IR canonico del agente KORA; v1.1 agrega §13 Compatibilidad legacy para materializar la absorcion declarada en gobernanza §3.2"
version: "1.1.0"
status: published
tags: [spec, agente, agentfile, canon, ir]
lang: es
extensions: {}
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:skill-overlay-spec"
  cites:
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:runtime-spec-md"
---

# KORA/Agentfile-Spec v1.1.0

## 1. Definicion

`AGENT.md` es la representacion intermedia canonica del agente KORA. Todo el
sistema moderno gira en torno a este artefacto.

El `AGENT.md` concentra la semantica del agente en 6 dimensiones:

1. `coalgebra`
2. `plan`
3. `interface`
4. `fibers`
5. `composition`
6. `safety`

## 2. Fuente de verdad

Reglas:

1. `AGENT.md` es la unica fuente de verdad normativa del agente.
2. Todo mirror legacy es subordinado.
3. Todo artefacto runtime o target es derivado.

## 3. Envelope y shape

Todo `AGENT.md` **DEBE** portar:

- `_manifest`
- `version`
- `name`
- `status`
- `tags`
- `lang`
- `extensions`
- `agent`

`agent` **DEBE** declarar las 6 dimensiones, aunque alguna sea minima.

## 4. Las 6 dimensiones

### 4.1 Coalgebra

Describe que agente es:

- `description`
- `domain`
- `triggers`
- `outputs`
- `invariants`

### 4.2 Plan

Describe la maquina de estados:

- `initial_state`
- `terminal_state`
- `states`

El plan **DEBE** ser determinista o declarar su precedencia.

### 4.3 Interface

Describe tools y permissions de forma semantica, no como plumbing crudo.

### 4.4 Fibers

Las fibras del agente son:

- `identity`
- `operator`
- `memory`
- `runtime`
- `knowledge`

### 4.5 Composition

Describe subagentes, roles, delegacion y disipacion.

La composicion moderna tambien absorbe la antigua semantica de swarm:

- golden paths
- circuit breakers
- backpressure
- event routing
- sentinel pattern

### 4.6 Safety

Contiene:

- `hard_rules`
- `co_induction`
- `guardrails`
- `alignment`

## 5. Capability references

`agent.skills` declara dependencias de capacidad.

Reglas:

1. Toda capacidad nueva **DEBERIA** resolverse como skill portable.
2. Un `CM-*` solo se justifica como compatibilidad.
3. Ninguna capacidad puede relajar `safety` del agente.

## 6. Body canonico

El body existe para refinamiento legible. Secciones tipicas:

- `## Behavior`
- `## Context`
- `## Style`

Reglas:

1. el body expande pero no gobierna contra el frontmatter,
2. si hay conflicto, prevalece el frontmatter.

## 7. Topologia minima

Topologia moderna:

```text
AGENT.md
```

Todo lo demás es opcional o derivado.

## 8. Complejidad

Los niveles `L0-L4` son una escala de densidad y articulacion, no especies de
agente. Un agente minimo sigue siendo válido si las 6 dimensiones existen.

## 9. Subsumision

Las dependencias de capacidad son subordinadas al agente:

1. `hard_rules` prevalece sobre cualquier skill,
2. `co_induction` prevalece sobre shortcuts locales,
3. el agente conserva dominio, routing y cierre de safety.

## 10. Composition avanzada

Cuando el agente compone otros agentes o actua como coordinador, `composition`
**DEBE** poder expresar:

1. golden path nominal,
2. puntos de corte o circuit breakers,
3. reglas de backpressure,
4. routing de eventos o delegaciones,
5. sentinel u observabilidad de composicion.

Esto reemplaza la necesidad de una spec swarm separada para el regimen canonico.

## 11. Validacion

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Envelope valido | Frontmatter completo | schema/lint |
| IR completo | Las 6 dimensiones existen | schema/lint |
| Plan cerrado | Estados y prioridades coherentes | lint/manual |
| Capacidades resolubles | `agent.skills` resuelve sin ambiguedad | lint |
| Body subordinado | El body no contradice el frontmatter | lint/manual |
| Composition visible | La composicion avanzada no queda oculta fuera del IR | lint/manual |

## 12. Migracion

Contrato vigente v1:

- `AGENT.md` es el centro del sistema.
- Los workspaces nuevos no requieren scaffold legacy.
- La migracion correcta absorbe legado en el IR y deja lo viejo como mirror
  temporal o lo elimina.

Cambios v1.1:

- §13 materializa la compatibilidad de workspace legacy declarada en
  `gobernanza §3.2` como absorcion dentro de `agentfile-spec`.

## 13. Compatibilidad con workspace legacy

El **scaffold legacy** de un workspace consiste en los archivos
`AGENTS.md`, `config.json`, `IDENTITY.md`, `SOUL.md`, `USER.md`, `TOOLS.md`
y un directorio `skills/` con bundles `CM-*`. Este perfil preserva la
semantica pre-Agentfile para consumidores que aun no soportan el IR
moderno.

### 13.1 Regla de coexistencia

Reglas:

1. Si `AGENT.md` y scaffold legacy coexisten en un mismo workspace,
   `AGENT.md` es la autoridad normativa (`gobernanza §4`).
2. Los archivos legacy son **mirrors subordinados**: sirven como
   importacion o interoperabilidad mientras se completa la absorcion.
3. Un conflicto entre `AGENT.md` y un archivo legacy se resuelve a favor
   de `AGENT.md` sin excepciones.
4. La coexistencia prolongada (mas alla del ciclo de absorcion
   declarado) es **deuda declarada** y **DEBE** registrarse en
   `extensions.kora.legacy_coexistence: <motivo>`.

### 13.2 Regimen URN de los archivos legacy

Los archivos legacy usan el regimen ejecutable legacy
(`gobernanza §4.3`):

| Archivo       | URN                                                  |
| ------------- | ---------------------------------------------------- |
| `AGENTS.md`   | `urn:{ns}:agent-bootstrap:{id}-agents:{version}`     |
| `config.json` | `urn:{ns}:agent-bootstrap:{id}-config:{version}`     |
| `IDENTITY.md` | `urn:{ns}:agent-bootstrap:{id}-identity:{version}`   |
| `SOUL.md`     | `urn:{ns}:agent-bootstrap:{id}-soul:{version}`       |
| `USER.md`     | `urn:{ns}:agent-bootstrap:{id}-user:{version}`       |
| `TOOLS.md`    | `urn:{ns}:agent-bootstrap:{id}-tools:{version}`      |

Un `AGENT.md` que absorbe uno de estos archivos **NO DEBE** heredar su URN;
mantiene el regimen Agentfile (`urn:{ns}:agent:{id}`) y **PUEDE** declarar
`supersedes` hacia los URN legacy.

### 13.3 Disipacion

La disipacion del scaffold legacy procede en tres pasos:

1. **Absorcion**: el contenido legacy relevante se traduce a una dimension
   de `AGENT.md`.
2. **Mirror**: los archivos legacy se conservan como mirror subordinado
   (`gobernanza §4.1`) mientras algun consumidor los requiera.
3. **Eliminacion**: al cesar la dependencia externa, los archivos legacy
   se eliminan y el workspace queda unicamente con `AGENT.md`.

### 13.4 Prohibiciones

1. Nuevos workspaces **NO DEBEN** nacer en scaffold legacy.
2. Nuevas capacidades **NO DEBEN** agregarse al legacy en lugar de al IR.
3. Ningun archivo legacy puede reclamar autoridad sobre `hard_rules` o
   `safety` declarados en `AGENT.md`.
