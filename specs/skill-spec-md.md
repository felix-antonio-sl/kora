---
_manifest:
  urn: "urn:kora:kb:skill-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 02, 04, KORA/Agent-Spec v8.1.0, repair of lifecycle/protocol contract"
version: "3.1.0"
status: published
tags: [spec, skill, cm, progressive-disclosure, lazy-load, script-protocol]
lang: es
---

# KORA/Skill-Spec v3.1.0

## 1. Definicion

Un Skill es una capacidad ejecutable bajo evaluacion diferida. Puede existir como:

1. Skill degenerado: archivo `CM-*.md`
2. Skill extendido: directorio con `SKILL.md`

Ambas formas comparten la misma identidad semantica `skill`. La forma extendida agrega estructura ejecutable; la forma degenerada preserva el CM Core minimo.

### 1.1 Alcance

Esta especificacion gobierna:

1. la forma degenerada y la forma extendida de los Skills
2. la relacion `Wrap` / `Extract` entre CM y Skill
3. el ciclo de vida de progressive disclosure
4. el script protocol para codigo ejecutable dentro de Skills extendidos
5. la integracion con `agent-spec-md` y `config.json`

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Skill | Unidad de capacidad cognitiva invocable por un agente |
| CM Core | Las 4 secciones obligatorias: `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output` |
| Skill degenerado | Archivo `CM-*.md` que ya es un Skill valido |
| Skill extendido | Directorio con `SKILL.md` y opcionalmente `scripts/`, `references/`, `assets/` |
| Wrap | Proceso `CM -> Skill extendido` |
| Extract | Proceso `Skill -> CM Core` |
| Progressive Disclosure | Discover -> Activate -> Execute |
| Script Protocol | Convencion Python 3 + stdin/stdout JSON para scripts de Skills extendidos |

## 3. Anatomia del Skill

### 3.1 Forma degenerada

Un Skill degenerado **DEBE** vivir en `skills/` y **DEBE** conservar exactamente el CM Core:

1. `## Proposito`
2. `## Input/Output`
3. `## Procedimiento`
4. `## Signature Output`

Reglas:

1. Usa identidad `skill`, nunca `agent-bootstrap`.
2. Usa `_manifest.type = lazy_load_endofunctor`.
3. No mezcla FSM, tono, security ni wiring.
4. Puede ser invocado por la FSM, pero no contiene control conversacional ni transiciones.

### 3.2 Forma extendida

La forma extendida envuelve el mismo CM Core en un directorio:

```text
{skill}/
  SKILL.md
  scripts/
  references/
  assets/
```

`SKILL.md` **DEBE** preservar el mismo CM Core y **PUEDE** agregar secciones auxiliares como `## Scripts`, `## References` o `## Examples`.

Reglas:

1. El `name` del frontmatter **DEBE** coincidir con el nombre del directorio padre.
2. Todo `allowed-tools` **DEBE** ser subconjunto de la interfaz declarada en `TOOLS.md`.
3. Todo `requires` **DEBE** ser compatible con `config.json`.
4. La forma extendida agrega capacidad, no cambia la identidad semantica del Skill.

Traces to: formal/02 §5.3 (allowed-tools subset) ; formal/02 §5.4 (requires subset)

### 3.3 Script Protocol

Todo script ejecutable dentro de `scripts/` **DEBE** seguir este protocolo:

1. Python 3 como lingua franca.
2. Entrada por `stdin` en JSON.
3. Salida por `stdout` en JSON.
4. Documentacion del I/O en `SKILL.md`.
5. Rutas relativas dentro del Skill; nunca rutas absolutas del host.

La finalidad del protocolo es mantener interoperabilidad y portabilidad sin acoplar el Skill a un runtime especifico.

## 4. Relacion entre CM y Skill

### 4.1 Wrap y Extract

- `Wrap`: toma un CM y produce un Skill extendido.
- `Extract`: toma un Skill y extrae su CM Core.

El Extract de un Skill extendido **DEBE** seguir siendo un Skill degenerado valido.

Traces to: formal/02 §2.3 (Unit eta)

### 4.2 Propiedades

1. `Extract(Wrap(CM)) = CM` para el CM Core.
2. `Wrap(Extract(Skill))` no preserva scripts, references ni assets; solo preserva el CM Core.
3. La compatibilidad hacia atras depende de que el CM Core no se altere durante la promocion a Skill extendido.

## 5. Progressive Disclosure Lifecycle

El ciclo de vida operativo de un Skill **DEBE** separarse en tres fases:

| Fase | Contenido visible | Funcion |
| --- | --- | --- |
| Discover | `name` + `description` | decidir si el Skill es relevante |
| Activate | CM Core | inyectar el proceso cognitivo |
| Execute | CM Core + extras bajo demanda | ejecutar scripts o consultar referencias |

Traces to: formal/02 §3.1 (Three Phases) ; formal/04 §5.1 (Four Phases)

### 5.1 Reglas de lifecycle

1. El bootstrap del agente **NO DEBE** inyectar todos los Skills completos.
2. Discover **DEBE** ser barato: solo metadata minima.
3. Activate **DEBE** inyectar solo el CM Core.
4. Execute **PUEDE** montar `scripts/`, `references/` o `assets/` bajo demanda.
5. El runtime **DEBE** tratar el Skill como capacidad lazy-load, no como prosa fija del bootstrap.

### 5.2 Token economy

1. El CM Core activado **NO DEBERIA** exceder ~5000 tokens.
2. Las secciones auxiliares de un `SKILL.md` **NO DEBEN** inyectarse en Activate.
3. Si el Skill necesita demasiado contexto para Activate, debe refactorizarse.

## 6. Topologia y coexistencia

| Forma | Ubicacion | Regla |
| --- | --- | --- |
| Degenerado | `agents/{ns}/{name}/skills/CM-*.md` | backward compatible |
| Extendido local | `agents/{ns}/{name}/skills/{skill}/SKILL.md` | mismo CM Core |
| Extendido federado | `skills/{namespace}/{skill}/SKILL.md` | reusable entre agentes |

Reglas:

1. Un Skill degenerado y un Skill extendido con el mismo identificador **NO DEBEN** coexistir en el mismo workspace.
2. La promocion local -> federado **DEBE** preservar el CM Core.
3. Toda referencia interna a `scripts/`, `references/` o `assets/` **DEBE** usar rutas relativas.

## 7. Integracion con agent-spec-md

| Relacion | Regla |
| --- | --- |
| Grammar CM | Hereda el CM Core exigido por `agent-spec-md` |
| Interface | `allowed-tools` es subconjunto de `TOOLS.md` |
| Security | `requires` es compatible con `config.json` |
| Discovery | Los Skills son objetos descubribles y filtrables |

Regla de precedencia:

`agent-spec-md` gobierna la topologia del agente; `skill-spec-md` gobierna la forma y lifecycle del Skill.

## 8. Invariantes

1. Todo `CM-*.md` valido **DEBE** seguir siendo un Skill degenerado valido.
2. El CM Core **NO DEBE** contener FSM, tono, wiring ni security.
3. El lifecycle **DEBE** preservar lazy-load.
4. `Extract(Wrap(CM))` **DEBE** preservar el CM Core.
5. Los Skills extendidos **PUEDE** existir por ley, pero el enforcement automatico base del repo sigue verificando principalmente Skill degenerado y preservacion del CM Core.

Traces to: formal/02 §2.3 (Unit eta) ; formal/07 §6.2 (Monotone Extension)

## 9. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Identidad skill | Todo Skill usa URN `skill` | lint | Migrar URN |
| Grammar canonica | El CM Core tiene las 4 secciones obligatorias | lint | Normalizar headings |
| Lazy-load | El bootstrap no contiene Skills inline | lint | Extraer a `skills/` |
| Progressive disclosure | Discover/Activate/Execute estan respetados por el runtime | runtime | Corregir adapter |
| Wrap/Extract | Un Skill extendido preserva CM Core valido | manual | Reescribir `SKILL.md` |
| Script Protocol | Scripts usan Python 3 + stdin/stdout JSON | manual | Reescribir scripts |
| allowed-tools | Subconjunto de `TOOLS.md` | lint | Ajustar declaracion |
| requires | Compatible con `config.json` | lint | Ajustar declaracion |
