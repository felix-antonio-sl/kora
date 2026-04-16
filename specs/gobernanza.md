---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "refactor modern-first: AGENT.md canonico, capacidades portables, legacy como compatibilidad; v4.1 formaliza regimenes URN en §4.3"
version: "4.1.0"
status: published
tags: [gobernanza, constitucion, precedencia, identidad, enforcement]
lang: es
extensions: {}
relations:
  cites:
    - "urn:kora:kb:md-spec"
---

# KORA/Gobernanza v4.1.0

## 1. Definicion

Esta es la constitucion operativa de KORA. Su objetivo es mantener un sistema
pequeño, moderno y composable. La gobernanza no intenta describir todos los
artefactos: fija el canon, define precedencia, decide identidad y disciplina el
uso de extensiones.

Principio rector:

> KORA es `AGENT.md` + capacidades portables + transmutacion.

Todo lo legacy existe solo como compatibilidad residual.

## 2. Canon de diseno

KORA **DEBE** operar con estas prioridades:

1. una sola fuente de verdad por objeto,
2. semantica concentrada en el IR canonico,
3. capacidades reutilizables y portables por defecto,
4. runtime y outputs siempre derivados,
5. legado confinado a importacion, mirror o bootstrap residual.

Corolarios:

1. `AGENT.md` es el centro del sistema.
2. `SKILL.md` portable es el formato preferido de capacidad.
3. Los outputs de transmutacion (`_BUILD/` por workspace) y los workspaces runtime son derivados.
4. El formato legacy de 5 archivos y los `CM-*` no son el futuro del sistema;
   son perfiles de compatibilidad mientras existan consumidores.

## 3. Taxonomia de specs y precedencia

Cuando dos reglas parezcan contradecirse, prevalece esta jerarquia:

1. `gobernanza.md`
2. `md-spec.md`
3. specs canonicas de dominio
4. extensiones de namespace
5. README, plantillas, artefactos generados

### 3.1 Specs canonicas de dominio

Las specs canonicas son:

- `knowledge-spec.md`
- `agentfile-spec.md`
- `skill-overlay-spec.md`
- `runtime-spec-md.md`

### 3.2 Perfiles de compatibilidad legacy

La compatibilidad legacy sigue existiendo, pero ya no como centro del mapa
normativo. Vive absorbida dentro de las specs canonicas:

- compatibilidad de workspace legacy dentro de `agentfile-spec`
- compatibilidad de skills `CM-*` dentro de `skill-overlay-spec`
- compatibilidad de outputs antiguos dentro de `runtime-spec`

Si una regla legacy choca con una regla canonica, la regla canonica prevalece.

### 3.3 Regla de especializacion

Entre specs del mismo nivel prevalece la más especifica para el objeto que
gobierna:

- `agentfile-spec` para `AGENT.md`
- `skill-overlay-spec` para capacidades portables
- `runtime-spec` para invariantes runtime y compilacion del IR
- los perfiles legacy solo para interpretar mirrors o imports residuales

## 4. Identidad y fuente de verdad

Todo objeto KORA **DEBE** tener una fuente primaria:

- agente moderno: `AGENT.md`
- capacidad portable: `SKILL.md`
- output target: artefacto derivado en `{workspace}/_BUILD/{target}/`
- artefacto legacy: entrypoint legacy solo cuando no existe equivalente moderno

### 4.1 Regla de mirrors

Un mirror **PUEDE** existir solo si:

1. la fuente primaria está clara,
2. el mirror no contradice la primaria,
3. el mirror puede regenerarse o reconciliarse.

Si conviven `AGENT.md` y archivos legacy, `AGENT.md` es la autoridad.

### 4.2 Manifest kind

`_manifest.type` expresa el kind estructural del componente. Los kinds
reservados siguen siendo:

- `bootstrap_agents`
- `bootstrap_soul`
- `bootstrap_user`
- `bootstrap_tools`
- `bootstrap_config`
- `lazy_load_endofunctor`
- `runtime_extension`
- `transmutation_record`

### 4.3 Regimenes de URN

KORA distingue tres regimenes de identidad URN. El regimen elegido determina
forma del URN y ubicacion de la version:

| Regimen            | Patron                                  | Version                      | Uso                                                      |
| ------------------ | --------------------------------------- | ---------------------------- | -------------------------------------------------------- |
| Conceptual         | `urn:{ns}:kb:{id}`                      | campo `version` fuera del URN | artefactos KORA/MD (knowledge, specs, meta)             |
| Agentfile          | `urn:{ns}:agent:{id}`                   | campo `version` fuera del URN | agentes modernos (`AGENT.md`)                           |
| Ejecutable legacy  | `urn:{ns}:{kind}:{id}:{version}`        | incorporada en el URN         | bootstrap artifacts y skills `CM-*` (compat)            |

`{kind}` en el regimen ejecutable legacy es uno de los `_manifest.type`
listados en §4.2 (p. ej. `agent-bootstrap`, `skill`, `lazy_load_endofunctor`).

Reglas:

1. El regimen conceptual es preferido para artefactos descriptivos nuevos.
2. El regimen Agentfile es canonico para agentes modernos.
3. El regimen ejecutable legacy **NO DEBE** usarse para componentes nuevos;
   solo persiste en componentes de compatibilidad explicitamente declarados.
4. Referencias a artefactos conceptuales y Agentfile en `relations`, `depends`,
   `cites` o body **DEBEN** usar la forma sin version; la resolucion de version
   es responsabilidad del catalogo y del runtime.
5. Un mismo componente **NO DEBE** declarar URN en dos regimenes
   simultaneamente; la migracion entre regimenes obliga a emitir un
   `supersedes` explicito.

## 5. Lifecycle y deprecacion

KORA distingue:

- artefactos conceptuales: `draft -> published -> deprecated`
- artefactos ejecutables: `draft -> active -> deprecated -> retired`

Reglas:

1. Lo legacy nuevo **NO DEBE** expandirse.
2. Toda nueva capacidad **DEBERIA** nacer portable.
3. Todo nuevo agente **DEBERIA** nacer en `AGENT.md`.
4. Si un artefacto legacy se mantiene, debe declararse compatibilidad, no
   canon.

## 6. Extensiones

Una extension de namespace agrega restricciones a un target o ecosistema
concreto.

Reglas:

1. Una extension **DEBE** depender de una spec base o canonica.
2. Una extension **PUEDE** estrechar reglas.
3. Una extension **NO DEBE** relajar el canon por omision.
4. La extension sigue siendo capa 6 aunque viva dentro de `specs/`.

## 7. Enforcement

Toda regla normativa cae en uno de estos niveles:

- `schema`
- `lint`
- `runtime`
- `eval`
- `manual`

Reglas:

1. Una regla sin enforcement explicito se interpreta como `manual`.
2. El repo **NO DEBE** prometer enforcement mecanico inexistente.
3. El canon **NO DEBE** degradarse para acomodar tooling atrasado.

## 8. Invariantes

Los invariantes constitucionales son:

1. `AGENT.md` es el canon del agente.
2. Las capacidades portables son la forma preferida de skill.
3. Legacy es compatibilidad, no centro.
4. Runtime y output siempre son derivados.
5. Ninguna spec de compatibilidad puede recentralizar el sistema.

## 9. Validacion

Checks minimos:

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Canon claro | Cada objeto tiene fuente primaria | lint/manual |
| Legacy acotado | No se expande lo legacy como camino por defecto | manual |
| Mirror limpio | Los mirrors no contradicen la fuente primaria | lint/manual |
| Extension monotona | Las extensiones no relajan el canon | manual |
| Kind valido | `_manifest.type` usa taxonomia reservada | lint |

## 10. Migracion

Contrato vigente v4:

- KORA se declara modern-first.
- `agentfile-spec`, `skill-overlay-spec` y `runtime-spec` son el centro.
- la compatibilidad legacy queda absorbida dentro de esas specs canonicas.
- La tarea de migracion ya no es "soportar ambos mundos igual", sino absorber
  el mundo legacy dentro del canon moderno y luego disiparlo.
