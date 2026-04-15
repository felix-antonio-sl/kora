---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 00-07, formal restoration of governed extended skills, RFC 2119"
version: "4.0.0"
status: published
tags: [gobernanza, constitucion, precedencia, identidad, enforcement]
lang: es
extensions: {}
---

# KORA/Gobernanza v4.0.0

## 1. Definicion

Este documento es la constitucion operativa de KORA. Gobierna unicamente cuatro materias:

1. Precedencia entre especificaciones.
2. Identidad de artefactos.
3. Extensiones del ecosistema.
4. Niveles de enforcement.

Todo lo demas pertenece a la especificacion del artefacto correspondiente.

Traces to: formal/05 §1.2 (Bounded Lattice)

## 2. Definiciones

| Termino                | Definicion                                                                                                      |
| ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| Artefacto conceptual   | Artefacto cuyo URN identifica el concepto, no el snapshot; describe conocimiento, reglas o referencias estables |
| Artefacto ejecutable   | Artefacto cuyo URN identifica un snapshot que participa en ejecucion, deployment o composicion operacional      |
| Regimen de identidad   | Esquema URN que gobierna como se identifica un artefacto: conceptual o ejecutable                               |
| Entrypoint ejecutable  | Archivo que porta la identidad y el `_manifest.type` efectivos de un artefacto ejecutable                       |
| Fibra adjunta          | Material subordinado a un artefacto ejecutable que no introduce identidad ni kind propios                       |
| Formal Layer           | Capa de justificacion categorial oficial de KORA                                                                |
| Extension de namespace | Artefacto KORA/Spec-MD que agrega restricciones sin relajar reglas base                                         |
| Enforcement            | Nivel de verificabilidad de una regla: schema, lint, runtime, eval o manual                                     |
| Lifecycle de artefacto | Ciclo `draft -> published -> deprecated` que gobierna artefactos conceptuales (`md-spec §3.1`)                   |
| Lifecycle de agente    | Ciclo `active -> deprecated -> retired` que gobierna workspaces ejecutables (`agent-spec §9`)                    |

## 3. Precedencia

Cuando dos reglas se contradicen, prevalece la capa mas alta de esta jerarquia:

1. `gobernanza.md`
2. `spec-md.md` y `md-spec.md`
3. `agent-spec-md.md`, `skill-spec-md.md`, `runtime-spec-md.md`, `swarm-spec-md.md`
4. Extensiones de namespace
5. Documentacion derivada, plantillas y README

Si un conflicto no puede resolverse por dominio, este documento **DEBE** actualizarse antes de aceptar la coexistencia de ambas reglas.

La ubicacion fisica de un artefacto **NO DEBE** alterar su capa de precedencia. Una extension de namespace materializada en `specs/` sigue perteneciendo a la capa 4 si declara explicitamente su caracter de extension.

## 4. Identidad

KORA reconoce tres clases de artefacto.

### 4.1 Artefactos conceptuales

- Regimen: `urn:{namespace}:{type}:{id}`
- Version: en el campo raiz `version`
- Tipos: `kb`, `doc`, `ref`, `core`, `domain`

Estos artefactos describen conocimiento, reglas o referencias estables. Su URN identifica el concepto, no el snapshot.

### 4.2 Artefactos ejecutables (legacy)

- Regimen: `urn:{namespace}:{type}:{id}:{version}`
- Tipos: `agent-bootstrap`, `skill`

Estos artefactos participan en ejecucion, deployment o composicion operacional. Su URN identifica un snapshot ejecutable. Este regimen aplica a los componentes bootstrap del formato legacy de 5 archivos y a Skills.

### 4.3 Artefactos agente (Agentfile)

- Regimen: `urn:{namespace}:agent:{id}`
- Version: en el campo raiz `version`
- Tipo unico: `agent`

Estos artefactos describen un agente completo en formato `AGENT.md` (agentfile-spec). Su URN identifica al agente conceptualmente; la version esta fuera del URN (igual que artefactos conceptuales). Un `AGENT.md` subsume los 5 componentes legacy (`agent-bootstrap`) en un archivo unico.

Cuando un workspace tiene tanto `AGENT.md` como archivos legacy, `AGENT.md` es autoritativo.

### 4.4 Reglas

1. Un componente bootstrap de agente legacy **DEBE** usar `agent-bootstrap`.
2. Un agente en formato Agentfile **DEBE** usar `agent`.
3. Un Skill, degenerado o extendido, **DEBE** usar `skill`.
4. Un CM degenerado **ES** un Skill; **NO DEBE** usar identidad `agent-bootstrap` ni `agent`.
5. Ninguna especificacion subordinada **PUEDE** definir un cuarto regimen de identidad sin cambiar este documento.

### 4.5 Manifest kind

La identidad URN y `_manifest.type` son ortogonales.

1. La URN gobierna el regimen identitario (`agent-bootstrap`, `agent` o `skill`).
2. `_manifest.type` gobierna el kind estructural del artefacto ejecutable o agente.
3. Para bootstraps de agente, los kinds permitidos son `bootstrap_agents`, `bootstrap_soul`, `bootstrap_user`, `bootstrap_tools`, `bootstrap_config`.
4. Para todo Skill, degenerado (`skills/CM-*.md`) o extendido (`skills/CM-*/SKILL.md`), el kind permitido del entrypoint es `lazy_load_endofunctor`.
5. Los directorios adjuntos `scripts/`, `references/` y `assets/` de un Skill extendido son fibras del mismo Skill y **NO** introducen kind ni identidad propios.
6. Ninguna spec subordinada **PUEDE** introducir kinds adicionales sin declararlos primero aqui.

Traces to: formal/01 §5.2 (Substitutability) ; formal/05 §1.3 (Domain Disjointness)

### 4.6 Migracion de identidad

Cuando un artefacto cambia de namespace (e.g., `gnub` -> `gn`, `kora` -> `tde`), la operacion **DEBE** ejecutarse como migracion atomica:

1. **Renombrar URNs**: actualizar `_manifest.urn` en todos los artefactos migrados. Enforcement: lint.
2. **Mover archivos**: reubicar bajo el directorio del namespace destino.
3. **Actualizar refs cruzadas**: toda referencia al URN anterior en otros artefactos **DEBE** actualizarse. Enforcement: lint (`kora health --strict`).
4. **Actualizar `allowed_kb`**: todo `config.json` de agente que referencie URNs migradas **DEBE** actualizarse. Enforcement: lint.
5. **Re-indexar**: ejecutar `kora index` tras la migracion.
6. **Verificar**: `kora health --strict` **DEBE** pasar sin errores tras la migracion.

Una migracion parcial (archivos movidos sin actualizar URNs o refs) es invalida y **DEBE** completarse o revertirse antes de cualquier otra operacion.

## 5. Formal Layer

### 5.1 Capa oficial

La unica Formal Layer oficial de KORA es `KNOWLEDGE/kora/categorical-foundations/`.

`Traces to:` **DEBE** referenciar exclusivamente documentos de esa capa.

### 5.2 Corpus auxiliar

`KNOWLEDGE/fxsl/cat/` y cualquier otro corpus categorial adicional son auxiliares. Pueden informar diseno, auditoria o critica, pero **NO DEBEN** respaldar `Traces to:` directamente.

Si un concepto auxiliar pasa a justificar reglas operacionales, **DEBE** absorberse mediante un documento puente dentro de la Formal Layer oficial.

## 6. Extensiones

Una extension de namespace:

1. **PUEDE** agregar restricciones.
2. **NO PUEDE** relajar reglas base.
3. **DEBE** vivir en un artefacto KORA/Spec-MD propio.
4. **DEBE** declarar explicitamente que especificacion extiende.
5. **PUEDE** residir en `specs/` o en una coleccion equivalente del repo, pero su precedencia sigue siendo la de extension y **NO** la de spec fundacional por mera ubicacion.
6. **DEBE** declarar en su frontmatter, dentro de `extensions.{namespace}`, la spec base extendida y cualquier metadata minima necesaria para resolver su tier.

Las extensiones de metadata se expresan unicamente dentro del campo `extensions.{namespace}` del artefacto gobernado.

En Skills extendidos, la metadata del bundle **DEBE** vivir bajo `extensions.{namespace}.skill` del `SKILL.md` entrypoint. Los directorios adjuntos no son un canal alterno de metadata raiz.

## 7. Enforcement

Toda regla importante de KORA cae en uno de cinco niveles:

| Nivel     | Semantica                                                            |
| --------- | -------------------------------------------------------------------- |
| `schema`  | Verificable por parseo o validacion estructural                      |
| `lint`    | Verificable por inspeccion estatica del repo                         |
| `runtime` | Verificable solo durante ejecucion u orquestacion                    |
| `eval`    | Verificable mediante evaluacion funcional con inputs representativos |
| `manual`  | Requiere juicio humano                                               |

Reglas fundacionales que no admiten enforcement razonable **DEBERIAN** expresarse como `DEBERIA`, salvo invariantes identitarios, de seguridad o de trazabilidad.

Una regla admite enforcement razonable si cumple al menos una de estas condiciones:

1. Es verificable por parseo o inspeccion estatica (`schema` o `lint`).
2. Es verificable mediante test suite o inputs representativos (`eval`).
3. Es verificable durante ejecucion u orquestacion (`runtime`).

Si ninguna de las tres condiciones se satisface, la regla es `manual`. Una regla `manual` que no toque invariantes identitarios, de seguridad ni de trazabilidad **DEBERIA** expresarse como `DEBERIA` en lugar de `DEBE`.

### 7.1 Binding enforcement-toolchain

Cada nivel de enforcement **DEBE** tener al menos un mecanismo de verificacion concreto:

| Nivel     | Mecanismo de verificacion                                   |
| --------- | ----------------------------------------------------------- |
| `schema`  | `python3 scripts/kora validate --profile strict`            |
| `lint`    | `python3 scripts/kora health --strict` + `kora validate`    |
| `runtime` | Evaluacion durante deployment o ejecucion del agente        |
| `eval`    | Test suite (`python3 -m unittest discover -s tests`) + inputs representativos |
| `manual`  | Documentado en reporte de auditoria con evidencia explicita |

Los checks `schema` y `lint` de las tablas de validacion de cada spec **DEBEN** tener cobertura en el toolchain. Si un check declarado como `lint` no tiene implementacion, **DEBE** documentarse como `manual` o implementarse.

## 8. Invariantes

1. La jerarquia de precedencia **NO DEBE** alterarse por una spec subordinada sin actualizar este documento.
2. Solo existen los regimenes de identidad definidos en §4.
3. Toda linea `Traces to:` **DEBE** apuntar a la Formal Layer oficial.
4. Ninguna extension **PUEDE** relajar reglas base.
5. Una fibra adjunta de Skill extendido **NO PUEDE** introducir identidad, kind ni precedencia paralelos al entrypoint que la gobierna.
6. Los directorios raiz del monorepo **DEBEN** usar casing canonico en mayusculas: `AGENTS/`, `KNOWLEDGE/`, `OPERATIONS/`. El toolchain **DEBE** usar constantes (`AGENTS_ROOT`, `KNOWLEDGE_ROOT`) y no paths hardcodeados.

## 9. Validacion

| Check                   | Criterio                                                      | Enforcement | Accion si falla                          |
| ----------------------- | ------------------------------------------------------------- | ----------- | ---------------------------------------- |
| Precedencia consistente | Ninguna spec subordinada contradice una capa superior         | manual      | Reescribir regla o actualizar gobernanza |
| Identidad consistente   | Solo existen los tres regimenes de identidad definidos en §4  | lint        | Migrar URNs                              |
| Kind de Skill consistente | Todo entrypoint de Skill usa `lazy_load_endofunctor` y las fibras adjuntas no crean kinds nuevos | lint/manual | Corregir entrypoint o bundle             |
| Traces oficiales        | Toda linea `Traces to:` apunta a la Formal Layer oficial      | lint        | Corregir o degradar a `Rationale:`       |
| Extensiones acotadas    | No hay metadata ad hoc fuera de `extensions.{namespace}`      | schema      | Reubicar extension                       |
| Enforcement declarado   | Las tablas nuevas o reescritas incluyen columna `Enforcement` | lint        | Completar tabla                          |
| Casing canonico         | Directorios raiz usan mayusculas (`AGENTS/`, `KNOWLEDGE/`, `OPERATIONS/`) | lint | Renombrar directorio                     |
| Migracion atomica       | No existen migraciones parciales (URNs sin mover o refs sin actualizar) | lint | Completar o revertir migracion           |

## 10. Protocolo de auditoria

Toda auditoria de artefactos KORA (workspaces, artefactos KORA/MD, specs) **DEBE** seguir este protocolo antes de declarar resultado.

### 10.1 Severidades

| Nivel    | Semantica                                                      | Efecto sobre PASS |
| -------- | -------------------------------------------------------------- | ----------------- |
| CRITICAL | Viola invariante de spec fundacional o rompe integridad repo   | Bloquea PASS      |
| HIGH     | Viola regla DEBE sin ser invariante                            | Bloquea PASS salvo excepcion documentada |
| MEDIUM   | Viola regla DEBERIA o afecta calidad sin romper invariante     | Debe documentarse |
| LOW      | Observacion informativa o mejora opcional                      | Informativa       |

### 10.2 Relacion con checks de specs subordinadas

Los checks de la tabla `## Validacion` de cada spec subordinada (agent-spec-md, skill-spec-md, runtime-spec-md, swarm-spec-md, md-spec, spec-md) son los checks concretos que **DEBEN** evaluarse durante la auditoria del artefacto gobernado por esa spec.

### 10.3 Condiciones para PASS

Un artefacto **DEBE** cumplir todas estas condiciones antes de declararse PASS:

1. Todos los checks con enforcement `schema` y `lint` de la spec gobernante **DEBEN** pasar sin fallo.
2. Los checks con enforcement `manual` **DEBEN** documentarse con evidencia explicita en el reporte.
3. El toolchain **DEBE** ejecutarse antes de declarar PASS: `kora health --strict` y `kora validate --profile strict`.
4. No **DEBE** existir ningun hallazgo CRITICAL ni HIGH sin resolver.

### 10.4 Condiciones para PASS de koraficacion

Ademas de §10.3, un artefacto koraficado **DEBE**:

1. Pasar verificacion mecanica (`md-spec §6.10`).
2. Pasar verificacion de fidelidad y calidad (`md-spec §6.11`).
3. Documentar `FS` y `CR` en el reporte.
4. Si `CR < 1.5`, documentar justificacion explicita en el reporte.
5. **NO DEBE** transitar a `status: published` sin cumplir las condiciones anteriores.

### 10.5 Cross-validacion

La verificacion de fidelidad (`FS`) **NO DEBERIA** ser auto-reportada por el mismo agente que ejecuto la transformacion. Cuando sea posible, la verificacion **DEBERIA** ejecutarse por un agente distinto o por toolchain mecanico.

Rationale: Agentes de baja capacidad tienden a inflar `FS` auto-reportado (evidencia operativa: FS declarado 100% vs mecanico 86-94%).

### 10.6 Convergencia

Si una auditoria requiere mas de 3 iteraciones sin alcanzar PASS, el artefacto **DEBERIA** re-evaluarse para rediseno en lugar de correccion incremental.

### 10.7 Reporte de auditoria

Todo reporte de auditoria **DEBERIA** registrarse en `docs/reports/` con formato `{fecha}-{scope}-{tipo}.md`.

## 11. Migracion

Esta seccion se establece a partir de v3.4.0. Los breaking changes de major bumps anteriores no fueron documentados en seccion dedicada.

### Contrato vigente v3

- Jerarquia de precedencia de 5 capas (§3).
- Dos regimenes de identidad: conceptual y ejecutable (§4).
- Dos lifecycles ortogonales: artefacto (`draft -> published -> deprecated`) y agente (`active -> deprecated -> retired`).
- Formal Layer unica en `KNOWLEDGE/kora/categorical-foundations/` (§5).
- Extensiones solo aditivas, nunca relajantes (§6).
- Cinco niveles de enforcement con binding a toolchain (§7).
- Protocolo de auditoria con severidades CRITICAL/HIGH/MEDIUM/LOW (§10).

### Transicion v3 -> v4

**Que cambio:**
- §4 pasa de 2 a 3 regimenes de identidad: se agrega `agent` para AGENT.md (§4.3).
- §4.4 (Reglas) renumerada a §4.4, §4.5 (Manifest kind) renumerada a §4.5, §4.6 (Migracion) renumerada a §4.6.

**Que migrar:**
- Los AGENT.md ya existentes usan `urn:{ns}:agent:{id}` — esta transicion formaliza lo que ya se estaba usando.
- Ningun cambio operativo necesario; solo se registra el regimen que ya estaba activo.

**Que se depreca:**
- Nada. Los componentes legacy (`agent-bootstrap`) siguen validos para workspaces que no migren a AGENT.md.

Toda futura transicion major **DEBE** documentar aqui: (1) que cambio, (2) que migrar, y (3) que se depreca.
