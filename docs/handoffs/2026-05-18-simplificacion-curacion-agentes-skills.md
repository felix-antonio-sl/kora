---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-18-simplificacion-curacion-agentes-skills"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-18"
    source: "Refactor pragmatico de la curacion de agentes y skills KORA, equivalente al refactor de conocimiento del 2026-05-17: agent-skill-construction-spec v1.1.0 declara explicitamente lo que NO gobierna y reapunta a autoria-spec donde duplica, autoria-conformance endurecido con status/version en root + status-por-directorio + namespace-directorio, 13 artefactos productivos con shape mixto normalizados, 4 skills promovidos de _TALLER/REVIEW a productivo."
version: "1.0.0"
status: publicado
tags: [handoff, agent-skill-construction-spec, autoria-conformance, autoria-spec, normalizacion-agentes-skills]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:agent-skill-construction-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:handoff-2026-05-17-simplificacion-curacion-knowledge"
---

# Handoff sesion 2026-05-18 — Simplificacion de la curacion de agentes y skills

## Resumen ejecutivo

Esta sesion aplica al dominio de **agentes y skills** la misma operacion
que la sesion anterior (`handoff-2026-05-17-simplificacion-curacion-knowledge`)
aplico a **conocimiento**: separar responsabilidades, endurecer enforcement
sin tocar lo congelado y normalizar deuda silenciosa.

Respetando el freeze formal de `harness-spec`, `autoria-spec` y
`transmutation-spec` (gobernanza §8.3), el refactor opera en:

1. **`agent-skill-construction-spec` v1.1.0** — explicita que NO gobierna
   shape ni lifecycle ni regimen URN, reemplaza tablas duplicadas por
   punteros a `autoria-spec` y separa los checks de construccion de los
   de shape final.
2. **`autoria-conformance`** y su validador funcional — agrega cuatro
   reglas universales que cierran un gap real (la spec ya exigia
   `status`/`version` en root, pero el validador silenciosamente aceptaba
   el shape mixto) mas dos invariantes de ubicacion (status-por-directorio
   y namespace-directorio) analogos a los de `knowledge-zone`.
3. **Normalizacion** — 13 artefactos productivos con shape mixto
   corregidos (10 skills + 2 AGENT.md + 1 skill con doble drift),
   4 skills promovidos a productivo (`transmute-claude-code`,
   `transmute-openclaw`, `graphic-design`, `hu-progress-auditor`), fix de
   URN broken en `transmute-openclaw`, invariantes minimas agregadas a
   `transmute-claude-code` y `transmute-openclaw`.

## Alcance

### Capa serializacion

- **`serialization/agent-skill-construction-spec.md` v1.1.0** (cambios
  aditivos, sin quiebres).

### Capa toolchain

- **`toolchain/kora_lib/autoria_validate.py`** — `UNIVERSAL_RULES` extendido
  con 4 reglas nuevas:
  - `envelope-status-requerido` (require `status` en root).
  - `envelope-version-requerido` (require `version` en root).
  - `envelope-status-fuera-de-lugar` (forbid `_manifest.status`).
  - `envelope-version-fuera-de-lugar` (forbid `_manifest.version`).
- **`toolchain/kora_lib/checks.py::_check_autoria_conformance`** — agrega
  status-por-directorio (autoria-spec §11) y namespace-directorio
  (autoria-spec §10.1) a la iteracion sobre artefactos productivos.

### Artefactos normalizados

- **13 artefactos con shape mixto** (`status`/`version` dentro de
  `_manifest` en lugar de root):
  - `artifacts/skills/dev/lineas-paralelas/` (status + version, doble drift)
  - `artifacts/skills/dev/steve-jobs-agentic-designer/`
  - `artifacts/skills/salud/jobs-healthcare-ux/`
  - `artifacts/skills/salud/constructor-tableros/`
  - `artifacts/skills/salud/asistencial-hospital/`
  - `artifacts/skills/salud/seguridad-informacion-salud/`
  - `artifacts/skills/salud/analista-redes/`
  - `artifacts/skills/salud/asistencial-hodom/`
  - `artifacts/skills/salud/interoperabilidad-salud/`
  - `artifacts/skills/salud/vigilancia-epidemiologica/`
  - `artifacts/skills/salud/auditor-calidad-hospitalizacion/`
  - `artifacts/agents/salud/gtd-integral/` (version duplicada)
  - `artifacts/agents/salud/medico-hospitalista/` (version duplicada)

### Promociones a productivo (`_TALLER/REVIEW/` -> `artifacts/skills/`)

| URN | Origen | Destino productivo |
|-----|--------|---------------------|
| `urn:kora:artefacto:transmute-claude-code` | `_TALLER/REVIEW/transmute-claude-code/` | `artifacts/skills/kora/transmute-claude-code/` |
| `urn:kora:artefacto:transmute-openclaw` | `_TALLER/REVIEW/transmute-openclaw/` | `artifacts/skills/kora/transmute-openclaw/` |
| `urn:kora:artefacto:graphic-design` | `_TALLER/REVIEW/graphic-design/` | `artifacts/skills/kora/graphic-design/` |
| `urn:dev:artefacto:hu-progress-auditor` | `_TALLER/REVIEW/hu-progress-auditor/` | `artifacts/skills/dev/hu-progress-auditor/` |

### Otros fixes

- **`transmute-openclaw/SKILL.md`** — URN broken (`urn:kora:kb:openclaw-runtime-extension`
  cambiado a `urn:agengai:kb:openclaw-runtime-extension` que es el
  canonico segun el catalogo).
- **`transmute-claude-code/SKILL.md`** y **`transmute-openclaw/SKILL.md`** —
  agregadas `artefacto.invariantes.reglas_duras` minimas (preservacion
  de URN, registro de perdidas en `_transmutation.yml`, abort si vector
  fuera de dominio, prohibicion de paths absolutos en output OpenClaw).
  El check `construction-risk-declared` ahora pasa para ambos.

## Decisiones doctrinales

### agent-skill-construction-spec v1.0.0 -> v1.1.0

**v1.1 NO duplica shape**. La regla central de la version es: **si una
regla aparece tanto aqui como en `autoria-spec`, prevalece
`autoria-spec`**. Esto cierra una zona gris previa donde algunas tablas
podian leerse como autoridad alternativa.

Cambios concretos:

- **§1.2 (nueva)** — declara explicitamente lo que NO gobierna esta
  spec: shape de frontmatter/body, lifecycle agentico, regimen URN,
  validacion estructural completa.
- **§3.3 (Fase C decision de forma material)** — la matriz de
  "usar cuando / evitar cuando" queda como **resumen operativo**, con
  regla explicita de que el dominio de proyeccion autoritativo vive en
  `autoria-spec §5` y la promocion entre formas en `autoria-spec §8`.
- **§3.8 (Fase H materializacion)** — topologia con punteros a las
  subsecciones especificas de `autoria-spec §5.1-§5.4`. Agrega regla de
  namespace-directorio enforced por `autoria-conformance`.
- **§5.2 (tabla de checks)** — separa los **checks de construccion**
  (que esta spec gobierna) de los **checks de shape final** (gobernados
  por `autoria-spec §14`). Declara `Spec ref` por check. Registra que
  `autoria-conformance` v1.1 enforza status/version-en-root +
  status-por-directorio + namespace-directorio.
- **§7.1 (nueva)** — declara el contrato vigente v1.1.

### Endurecimiento de `autoria-conformance`

El validador ya tenia el catalogo de reglas correctas, pero el shape
mixto (`status` dentro de `_manifest`) **silenciaba el check**: `path("status")`
retornaba `None`, y `in_set(None, ...)` se interpretaba como "no aplica".
Esto permitia que 13 artefactos productivos pasaran sin diagnostico.

El fix:

- `require(path("status"))` + `require(path("version"))` exigen presencia
  en root.
- `forbid(path("_manifest", "status"))` + `forbid(path("_manifest", "version"))`
  exigen ausencia dentro de `_manifest`.

Conjuntamente, las 4 reglas forman una **categoria de discriminacion**
sobre el shape: cualquier artefacto con `status`/`version` fuera de root
produce diagnostico explicito.

Ademas, el check agrega dos verificaciones de ubicacion (analogas a
`knowledge-zone`):

- **Status-por-directorio**: artefactos en `artifacts/agents/{ns}/` y
  `artifacts/skills/{ns}/` solo aceptan `status ∈ {activo, deprecado,
  retirado}`; `borrador` queda restringido a `_FRAGUA/REVIEW` o
  `_TALLER/REVIEW`.
- **Namespace-directorio**: el namespace del URN
  (`urn:{ns}:artefacto:{id}`) coincide con el primer subdirectorio
  bajo `artifacts/agents/` o `artifacts/skills/`.

### Disciplina functorial implicita

- **Identidad** — la promocion via `kora promote` preserva el URN
  byte-identical (`autoria-spec §10` ya lo declara; el endurecimiento
  ahora lo enforza al rechazar drift de ubicacion).
- **Composicion** — `validate(art)` es composicion de reglas en la
  categoria Kleisli del monad `List[Diagnostic]`; agregar reglas es
  apilar morfismos.
- **Adjuncion Check ⊣ Fix** — las 4 reglas nuevas (status/version
  fuera-de-lugar) son **mecanicamente fixables** por el codemod
  `kora migrate --perfil a-autoria` (extension natural; ver deuda
  residual).

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 625 artefactos indexados (+4 vs baseline post-knowledge: las 4 promociones) |
| `python3 toolchain/kora check --strict` | 32/33 verdes; 1 LOW preexistente en hodom-v1.3.0 (WIP del operador) |
| `python3 -m unittest discover -s tests` | suite completa verde |

Tras el endurecimiento de `autoria-conformance`, el check detecto:

- 13 artefactos con shape mixto (todos normalizados).
- 1 URN broken en `transmute-openclaw` (fix aplicado).
- 2 skills sin invariantes con `sigma_transparency=3` (`transmute-*`),
  reglas duras minimas agregadas.

## Estado consolidado

### Que cerramos definitivamente

- `agent-skill-construction-spec` y `autoria-spec` ya no se solapan
  ambiguamente: la primera dice **como construir**, la segunda dice
  **cual es el shape**.
- `autoria-conformance` enforza efectivamente las reglas de envelope
  que la spec siempre prometia: `status`/`version` en root.
- `status-por-directorio` y `namespace-directorio` cierran el ciclo
  para agentes y skills, paralelo a lo que `knowledge-zone` hace para
  conocimiento.
- 4 skills clave promovidos: `transmute-claude-code`, `transmute-openclaw`,
  `graphic-design`, `hu-progress-auditor`.

### Que quedo como deuda real

1. **`_TALLER/INBOX/`** sigue con 8+ skills sin promover, varios bajo
   `_rebuild_required/2026-05-03/` (cohorte de meta-KORA en reconstruccion
   por `meta-kora-rebuild-directive`). No tocado en esta sesion: la
   doctrina explicita los marca como pre-categoriales.
2. **`_FRAGUA/`** no existe en el filesystem actualmente; cuando aparezca
   staging de agentes nuevo, el check `autoria-conformance` ya esta
   listo para enforzar.
3. **`autoria_validate` codemod** — las 4 reglas nuevas son trivialmente
   reparables (mover `status`/`version` a root), pero el codemod
   `migrate_to_autoria` aun no lo hace. Esta sesion lo hizo manualmente
   en los 13 archivos detectados; agregar el codemod al migrator es
   deuda menor.
4. **`construction-risk-declared`** sigue como MEDIUM y solo dispara para
   `forma_material ∈ {agente-propiamente-tal, agente-plataforma}` o
   `sigma_i >= 3`. Las dos transmute-* ahora pasan porque tienen
   `invariantes`. Si aparecen mas skills con sigma alto, el check los
   detectara.
5. **WIP del operador** en `artifacts/knowledge/salud/salubrista/hodom/`
   y `artifacts/skills/dev/hermes-agent-specialist/` queda intacto (no
   tocado).

### Que NO debe asumirse

- No asumir que `autoria-spec` cambio: esta en freeze. Solo el toolchain
  y `agent-skill-construction-spec` se actualizaron.
- No asumir que las refs a `agent-skill-construction-spec §3.3` o `§3.8`
  siguen apuntando a tablas autoritativas: en v1.1 son resumenes
  operativos que delegan a `autoria-spec §5` y `§8`.
- No asumir que un artefacto productivo con shape mixto pasa el check:
  el validador ahora discrimina.

## Artefactos dejados versionados

### Specs
- `serialization/agent-skill-construction-spec.md` — v1.1.0.

### Toolchain
- `toolchain/kora_lib/autoria_validate.py` — 4 reglas universales nuevas.
- `toolchain/kora_lib/checks.py::_check_autoria_conformance` — status-por-directorio
  + namespace-directorio.

### Artefactos normalizados (shape mixto fix)
- 11 SKILL.md (1 con doble drift) + 2 AGENT.md.

### Skills promovidos (`_TALLER/REVIEW/` -> productivo)
- `artifacts/skills/kora/transmute-claude-code/`
- `artifacts/skills/kora/transmute-openclaw/`
- `artifacts/skills/kora/graphic-design/`
- `artifacts/skills/dev/hu-progress-auditor/`

### Skills con invariantes nuevas
- `transmute-claude-code/SKILL.md`
- `transmute-openclaw/SKILL.md` (incluye fix de URN broken)

### Docs
- `docs/handoffs/2026-05-18-simplificacion-curacion-agentes-skills.md` (este).

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-18-simplificacion-curacion-agentes-skills.md`.

Contexto que debes asumir como vigente:

- `agent-skill-construction-spec v1.1.0` declara explicitamente que NO
  gobierna shape ni lifecycle ni regimen URN; eso vive en `autoria-spec`.
  La precedencia es `autoria-spec` > `agent-skill-construction-spec`
  cuando una regla aparezca en ambas.
- `autoria-conformance` enforza ahora: status/version en root,
  status-por-directorio (productivo solo activo/deprecado/retirado) y
  namespace-directorio (URN ns == subdir).
- 13 artefactos productivos con shape mixto ya fueron normalizados.
- 4 skills promovidos a productivo: `transmute-claude-code`,
  `transmute-openclaw`, `graphic-design`, `hu-progress-auditor`.

Para tareas tipicas:

1. Crear skill o agente nuevo: leer `agent-skill-construction-spec` para
   el metodo y `autoria-spec` para el shape. Materializar en
   `_TALLER/INBOX/{name}/SKILL.md` o `_FRAGUA/INBOX/{ns}/{name}/`. Mover
   a REVIEW cuando este lista para auditar. Promover con `kora promote`.
2. Normalizar un artefacto con drift: leer su frontmatter; si
   `status`/`version` esta dentro de `_manifest`, moverlos a root. El
   check `autoria-conformance` ahora lo detecta.
3. Antes de cualquier cambio mayor de doctrina, revisar `gobernanza §8.3`:
   `harness-spec`, `autoria-spec` y `transmutation-spec` siguen en
   freeze formal.

Posibles continuaciones (no urgentes):

A. **Extender `migrate_to_autoria` para fix automatico** — los 4 codes
   nuevos (`envelope-status-requerido`, `envelope-version-requerido`,
   `envelope-status-fuera-de-lugar`, `envelope-version-fuera-de-lugar`)
   son mecanicamente reparables.
B. **Drenar `_TALLER/INBOX/`** — varios skills (incluyendo el cohort
   `_rebuild_required/2026-05-03/`) sin promover.
C. **Auditar staging de agentes** — `_FRAGUA/` no existe actualmente;
   crearlo si aparece staging nuevo, con la disciplina ya enforced.
D. **Refactor de runtime-extensions** — analogo a lo que hicimos con
   construction-spec: simplificar duplicacion entre runtime-extensions
   sin tocar `transmutation-spec` (freeze).

Mantener commits acotados por linea. No tocar specs en freeze sin
justificacion HITL explicita.
```
