---
_manifest:
  urn: "urn:kora:kb:skill-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 02, 04, KORA/Agent-Spec v8.1.0, descoping of non-enforced extended skills"
version: "3.3.0"
status: published
tags: [spec, skill, cm, degenerate, lazy-load]
lang: es
---

# KORA/Skill-Spec v3.3.0

## 1. Definicion

Un Skill es una capacidad lazy-load invocable por la FSM de un agente.

En el baseline vigente del repo, la unica forma soportada, auditada y gobernada automaticamente es:

1. Skill degenerado: archivo `CM-*.md` dentro de `skills/`

### 1.1 Alcance

Esta especificacion gobierna:

1. la forma degenerada del Skill
2. el CM Core minimo exigido por el repo
3. la integracion con `agent-spec-md`, `TOOLS.md` y `config.json`
4. el hecho de que cualquier superficie extendida queda reservada y fuera de enforcement automatico base

## 2. Definiciones

| Termino          | Definicion                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| Skill            | Unidad de capacidad cognitiva invocable por un agente                                          |
| CM Core          | Las 4 secciones obligatorias: `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output` |
| Skill degenerado | Archivo `CM-*.md` que ya es un Skill valido                                                    |
| Skill extendido  | Superficie reservada para una futura expansion, no soportada por el validator base             |
| Lazy-load        | El Skill se activa bajo demanda, no inline en el bootstrap                                     |

## 3. Anatomia del Skill

Un Skill degenerado **DEBE** vivir en `skills/` y **DEBE** conservar el CM Core:

1. `## Proposito`
2. `## Input/Output`
3. `## Procedimiento`
4. `## Signature Output`

Reglas:

1. Usa identidad `skill`, nunca `agent-bootstrap`.
2. Usa `_manifest.type = lazy_load_endofunctor`.
3. No mezcla FSM, tono, security ni wiring.
4. Puede ser invocado por la FSM, pero no contiene control conversacional ni transiciones.

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

La URN identitaria `skill` y el kind `_manifest.type = lazy_load_endofunctor` son ortogonales: la primera gobierna identidad ejecutable; la segunda gobierna la forma estructural del Skill degenerado.

Un Skill **PUEDE** producir o evaluar contenido sobre behavior, interface, security o wiring cuando su dominio es de diseno, auditoria o transformacion de artefactos. Lo que **NO DEBE** hacer es ejercer control conversacional, routing efectivo, politica operativa o seguridad runtime del agente durante la ejecucion.

## 4. Integracion con agent-spec-md

| Relacion   | Regla                                                                        |
| ---------- | ---------------------------------------------------------------------------- |
| Grammar CM | Hereda el CM Core exigido por `agent-spec-md`                                |
| Interface  | Toda invocacion de tool desde un CM debe estar respaldada por `TOOLS.md`     |
| Security   | Todo Skill se ejecuta dentro del envelope de `config.json`                   |
| Discovery  | El baseline gobierna discovery de Skills degenerados, no surfaces extendidas |

Regla de precedencia:

`agent-spec-md` gobierna la topologia del agente; `skill-spec-md` gobierna la forma degenerada del Skill.

## 5. Descope explicito de Skills extendidos

Las siguientes superficies quedan fuera del soporte efectivo del repo en esta fase:

1. directorios locales con `SKILL.md`
2. `scripts/`, `references/` y `assets/` como contrato runtime gobernado
3. progressive disclosure `Discover -> Activate -> Execute` como enforcement automatico
4. `Wrap` / `Extract` como ley operativa vigente

Si una de esas superficies reaparece en el futuro, requiere:

1. spec propia restaurada
2. validator compatible
3. tests repo-wide
4. alineacion explicita con `forgemaster`

## 6. Invariantes

1. Todo `CM-*.md` valido **DEBE** ser un Skill degenerado valido.
2. El CM Core **NO DEBE** contener FSM, tono, wiring ni security.
3. El bootstrap del agente **NO DEBE** inyectar Skills inline.
4. El validator base **DEBE** juzgar conformidad solo sobre Skill degenerado.
5. Ninguna spec o agente **DEBE** presentar Skills extendidos como capacidad vigente si el repo no los gobierna realmente.
6. Un Skill **NO DEBE** relajar, condicionar ni reinterpretar reglas duras declaradas en `AGENTS.md` o en las specs superiores. Si un Skill necesita flexibilidad que contradice una regla dura, la regla dura **DEBE** modificarse primero en su fuente.

Traces to: formal/02 §2.3 (Unit eta) ; formal/04 §2.4 (Filtered Discovery)

## 7. Validacion

| Check            | Criterio                                                          | Enforcement | Accion si falla                 |
| ---------------- | ----------------------------------------------------------------- | ----------- | ------------------------------- |
| Identidad skill  | Todo Skill usa URN `skill`                                        | lint        | Migrar URN                      |
| Grammar canonica | El CM Core tiene las 4 secciones obligatorias                     | lint        | Normalizar headings             |
| Lazy-load        | El bootstrap no contiene Skills inline                            | lint        | Extraer a `skills/`             |
| Purity           | El Skill no contiene FSM ni control conversacional segun tabla §3 | lint        | Extraer leakage                 |
| Tool envelope    | Toda tool usada por el Skill esta declarada semanticamente        | lint        | Alinear TOOLS.md                |
| No-relajacion    | Ningun CM redefine, relaja o condiciona reglas duras de AGENTS.md | manual      | Mover regla al bootstrap o spec |
| Scope baseline   | El repo no afirma soporte efectivo de Skills extendidos           | lint/manual | Corregir spec o agente          |
