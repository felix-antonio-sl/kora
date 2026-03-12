---
_manifest:
  urn: "urn:kora:kb:skill-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 02, 04, 06, 07, KORA/Agent-Spec v8.4.0, restoration of governed extended skills"
version: "4.0.0"
status: published
tags: [spec, skill, cm, degenerate, lazy-load]
lang: es
---

# KORA/Skill-Spec v4.0.0

## 1. Definicion

Un Skill es una capacidad lazy-load invocable por la FSM de un agente.

En el baseline vigente del repo existen dos materializaciones gobernadas del mismo objeto `skill`:

1. Skill degenerado: archivo `skills/CM-*.md`
2. Skill extendido: directorio `skills/CM-*/` con entrypoint `SKILL.md`

### 1.1 Alcance

Esta especificacion gobierna:

1. la forma degenerada y extendida del Skill
2. el CM Core minimo exigido por el repo
3. la relacion `Free ⊣ Forget` entre CM y Skill
4. la integracion con `agent-spec-md`, `TOOLS.md`, `config.json` y `runtime-spec-md`
5. discovery, activation y ejecucion de Skills extendidos sin drift de interfaz

## 2. Definiciones

| Termino          | Definicion                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| Skill            | Unidad de capacidad cognitiva invocable por un agente                                          |
| CM Core          | Las 4 secciones obligatorias: `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output` |
| Skill degenerado | Archivo `CM-*.md` que ya es un Skill valido                                                    |
| Skill extendido  | Directorio `skills/CM-*/` con entrypoint `SKILL.md` y fibras adjuntas opcionales               |
| Forget           | Proyeccion que extrae el `CM Core` de un Skill                                                 |
| Free             | Construccion que envuelve un `CM Core` como Skill degenerado                                   |
| Promote          | Operacion que agrega `scripts/`, `references/` o `assets/` preservando el `CM Core`           |
| Lazy-load        | El Skill se activa bajo demanda, no inline en el bootstrap                                     |

## 3. Anatomia del Skill

Todo Skill KORA, degenerado o extendido, **DEBE** preservar el mismo `CM Core`:

1. `## Proposito`
2. `## Input/Output`
3. `## Procedimiento`
4. `## Signature Output`

### 3.1 Skill degenerado

Un Skill degenerado **DEBE** materializarse como `skills/CM-*.md`.

Reglas:

1. Usa identidad `skill`, nunca `agent-bootstrap`.
2. Usa `_manifest.type = lazy_load_endofunctor`.
3. No mezcla FSM, tono, security ni wiring.
4. Puede ser invocado por la FSM, pero no contiene control conversacional ni transiciones.

### 3.2 Skill extendido

Un Skill extendido **DEBE** materializarse como:

```text
skills/
  CM-NOMBRE/
    SKILL.md
    scripts/        # opcional
    references/     # opcional
    assets/         # opcional
```

Reglas:

1. El entrypoint `SKILL.md` **DEBE** usar identidad `skill` y `_manifest.type = lazy_load_endofunctor`.
2. El nombre del directorio `CM-NOMBRE/` **DEBE** ser el identificador simbolico del Skill activable por la FSM.
3. `SKILL.md` **DEBE** contener el mismo `CM Core` obligatorio definido en esta spec.
4. `scripts/`, `references/` y `assets/` son fibras adjuntas opcionales del mismo Skill; **NO DEBEN** portar identidad ni kind propios.
5. La metadata del bundle **DEBE** vivir bajo `extensions.{namespace}.skill` del `SKILL.md` entrypoint.
6. Un Skill extendido **NO DEBE** duplicar su identidad en un `CM-*.md` paralelo persistido; la proyeccion degenerada se obtiene via `Forget(SKILL)`.

### 3.3 Algebra operativa

Reglas normativas:

1. `Free(CM)` **DEBE** producir un Skill degenerado que preserve exactamente las cuatro secciones del `CM Core`.
2. `Forget(Skill)` **DEBE** extraer exactamente esas cuatro secciones, sin reescritura semantica.
3. `Promote` **PUEDE** agregar `scripts/`, `references/`, `assets/` y metadata extendida, pero **NO DEBE** alterar el `CM Core`.
4. La unidad `η: CM -> Forget(Free(CM))` **DEBE** preservarse como identidad observacional sobre el `CM Core`.
5. La counidad `ε: Free(Forget(Skill)) -> Skill` **DEBE** ser identidad sobre el `CM Core` e inclusion solo sobre las fibras adjuntas.

Patrones prohibidos en un Skill degenerado (definicion operativa de "control conversacional" y "mezcla de FSM"):

| Patron prohibido                         | Ejemplo de violacion                                                            | Regla vulnerada |
| ---------------------------------------- | ------------------------------------------------------------------------------- | --------------- |
| Variables de estado FSM                  | `estado_actual: FSMState`, `current_state`                                      | Regla 3         |
| Clasificaciones de transicion            | `END`, `DISPATCH`, `NEXT_STATE` como outputs de clasificacion                   | Regla 4         |
| Instrucciones de continuidad multi-turno | "la FSM debe volver a despachar", "en el siguiente turno"                       | Regla 4         |
| Orquestacion de fases del agente         | "Fase 1... Fase 2... Fase 3..." como control secuencial de ejecucion del agente | Regla 3         |
| Composicion inter-componente operativa   | Wiring o routing efectivo a otros agentes o skills desde dentro del CM          | Regla 3         |
| Logica de seguridad                      | Permisos, sandbox, filtrado de tools                                            | Regla 3         |
| Relajacion de reglas duras               | Condicionar o reinterpretar umbrales o restricciones del bootstrap              | §6 invariante 6 |

La URN identitaria `skill` y el kind `_manifest.type = lazy_load_endofunctor` son ortogonales: la primera gobierna identidad ejecutable; la segunda gobierna la forma estructural del entrypoint del Skill, degenerado o extendido.

Un Skill **PUEDE** producir o evaluar contenido sobre behavior, interface, security o wiring cuando su dominio es de diseno, auditoria o transformacion de artefactos. Lo que **NO DEBE** hacer es ejercer control conversacional, routing efectivo, politica operativa o seguridad runtime del agente durante la ejecucion.

## 4. Integracion con agent-spec-md

| Relacion   | Regla                                                                        | Enforcement |
| ---------- | ---------------------------------------------------------------------------- | ----------- |
| Grammar CM | Hereda el CM Core exigido por `agent-spec-md`                                | lint        |
| Interface  | Toda invocacion de tool desde un CM debe estar respaldada por `TOOLS.md`     | lint        |
| Security   | Todo Skill se ejecuta dentro del envelope de `config.json`                   | runtime     |
| Discovery  | Discovery de Skills degenerados y extendidos se filtra por `config.json`     | runtime     |

Regla de precedencia:

`agent-spec-md` gobierna la topologia del agente; `skill-spec-md` gobierna la forma del Skill y la relacion entre su proyeccion degenerada y su forma extendida.

## 5. Progressive Disclosure y Skills extendidos

La activacion de un Skill extendido **DEBE** seguir el ciclo:

1. **Discover** — proyectar solo metadata minima del bundle
2. **Activate** — inyectar `Forget(SKILL)` = `CM Core`
3. **Execute** — montar fibras adjuntas solo si la activacion lo requiere

Reglas:

1. Discover **NO DEBE** bootstrappear `scripts/`, `references/` ni `assets/`.
2. Activate **DEBE** preservar lazy-load y exponer solo el `CM Core`.
3. Execute **PUEDE** montar el bundle completo, pero **NO DEBE** alterar `AGENTS.md`, `TOOLS.md` ni `config.json`.
4. `allowed_tools` declaradas en `extensions.{namespace}.skill` **DEBEN** satisfacer `allowed_tools ⊆ TOOLS.md`.
5. `requires` declarados en `extensions.{namespace}.skill` **DEBEN** ser compatibles con `config.json`.
6. Un wrapper o adapter **NO DEBE** colapsar el bundle dentro del bootstrap del agente.

## 6. Invariantes

1. Todo `CM-*.md` valido **DEBE** ser un Skill degenerado valido.
2. El CM Core **NO DEBE** contener FSM, tono, wiring ni security.
3. El bootstrap del agente **NO DEBE** inyectar Skills inline.
4. El validator base **DEBE** juzgar conformidad sobre `skills/CM-*.md` y sobre `skills/CM-*/SKILL.md` cuando existan.
5. Todo Skill extendido **DEBE** preservar el `CM Core` de su activacion via `Forget`.
6. Un Skill **NO DEBE** relajar, condicionar ni reinterpretar reglas duras declaradas en `AGENTS.md` o en las specs superiores. Si un Skill necesita flexibilidad que contradice una regla dura, la regla dura **DEBE** modificarse primero en su fuente.

Traces to: formal/02 §2.3 (Unit eta) ; formal/02 §2.4 (Counit epsilon) ; formal/02 §4.3 (Promotion preserves CMCore) ; formal/04 §2.4 (Filtered Discovery) ; formal/04 §5 (Progressive Disclosure)

## 7. Validacion

| Check            | Criterio                                                          | Enforcement | Accion si falla                 |
| ---------------- | ----------------------------------------------------------------- | ----------- | ------------------------------- |
| Identidad skill  | Todo Skill usa URN `skill`                                        | lint        | Migrar URN                      |
| Grammar canonica | Todo entrypoint de Skill conserva el `CM Core` con las 4 secciones obligatorias | lint        | Normalizar headings             |
| Materializacion resoluble | Todo `CM-*` referido resuelve a `skills/CM-*.md` o `skills/CM-*/SKILL.md` | lint        | Corregir path o referencia      |
| Bundle extendido | Si existe `SKILL.md`, el bundle vive solo bajo `scripts/`, `references/`, `assets/` y metadata en `extensions.{namespace}.skill` | lint/manual | Reubicar bundle o metadata      |
| Lazy-load        | El bootstrap no contiene Skills inline                            | lint        | Extraer a `skills/`             |
| Purity           | El Skill no contiene FSM ni control conversacional segun tabla §3 | lint        | Extraer leakage                 |
| Tool envelope    | Toda tool usada por el Skill esta declarada semanticamente        | lint        | Alinear TOOLS.md                |
| Monad compatibility | `requires` del Skill son compatibles con `config.json`         | runtime     | Ajustar bundle o envelope       |
| Progressive disclosure | Discover/Activate/Execute preservan lazy-load y `CM Core`   | runtime     | Corregir adapter o activacion   |
| No-relajacion    | Ningun CM redefine, relaja o condiciona reglas duras de AGENTS.md | manual      | Mover regla al bootstrap o spec |
