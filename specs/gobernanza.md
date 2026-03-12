---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 00-07, formal restoration of governed extended skills, RFC 2119"
version: "3.2.0"
status: published
tags: [gobernanza, constitucion, precedencia, identidad, enforcement]
lang: es
---

# KORA/Gobernanza v3.2.0

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

## 3. Precedencia

Cuando dos reglas se contradicen, prevalece la capa mas alta de esta jerarquia:

1. `gobernanza.md`
2. `spec-md.md` y `md-spec.md`
3. `agent-spec-md.md`, `skill-spec-md.md`, `runtime-spec-md.md`, `swarm-spec-md.md`
4. Extensiones de namespace
5. Documentacion derivada, plantillas y README

Si un conflicto no puede resolverse por dominio, este documento **DEBE** actualizarse antes de aceptar la coexistencia de ambas reglas.

## 4. Identidad

KORA reconoce dos clases de artefacto.

### 4.1 Artefactos conceptuales

- Regimen: `urn:{namespace}:{type}:{id}`
- Version: en el campo raiz `version`
- Tipos: `kb`, `doc`, `ref`, `core`, `domain`

Estos artefactos describen conocimiento, reglas o referencias estables. Su URN identifica el concepto, no el snapshot.

### 4.2 Artefactos ejecutables

- Regimen: `urn:{namespace}:{type}:{id}:{version}`
- Tipos: `agent-bootstrap`, `skill`

Estos artefactos participan en ejecucion, deployment o composicion operacional. Su URN identifica un snapshot ejecutable.

### 4.3 Reglas

1. Un componente bootstrap de agente **DEBE** usar `agent-bootstrap`.
2. Un Skill, degenerado o extendido, **DEBE** usar `skill`.
3. Un CM degenerado **ES** un Skill; **NO DEBE** usar identidad `agent-bootstrap`.
4. Ninguna especificacion subordinada **PUEDE** definir un tercer regimen de identidad sin cambiar este documento.

### 4.4 Manifest kind

La identidad URN y `_manifest.type` son ortogonales.

1. La URN gobierna el regimen identitario (`agent-bootstrap` o `skill`).
2. `_manifest.type` gobierna el kind estructural del artefacto ejecutable.
3. Para bootstraps de agente, los kinds permitidos son `bootstrap_agents`, `bootstrap_soul`, `bootstrap_user`, `bootstrap_tools`, `bootstrap_config`.
4. Para todo Skill, degenerado (`skills/CM-*.md`) o extendido (`skills/CM-*/SKILL.md`), el kind permitido del entrypoint es `lazy_load_endofunctor`.
5. Los directorios adjuntos `scripts/`, `references/` y `assets/` de un Skill extendido son fibras del mismo Skill y **NO** introducen kind ni identidad propios.
6. Ninguna spec subordinada **PUEDE** introducir kinds adicionales sin declararlos primero aqui.

Traces to: formal/01 §5.2 (Substitutability) ; formal/05 §1.3 (Domain Disjointness)

## 5. Formal Layer

### 5.1 Capa oficial

La unica Formal Layer oficial de KORA es `knowledge/kora/categorical-foundations/`.

`Traces to:` **DEBE** referenciar exclusivamente documentos de esa capa.

### 5.2 Corpus auxiliar

`knowledge/fxsl/cat/` y cualquier otro corpus categorial adicional son auxiliares. Pueden informar diseno, auditoria o critica, pero **NO DEBEN** respaldar `Traces to:` directamente.

Si un concepto auxiliar pasa a justificar reglas operacionales, **DEBE** absorberse mediante un documento puente dentro de la Formal Layer oficial.

## 6. Extensiones

Una extension de namespace:

1. **PUEDE** agregar restricciones.
2. **NO PUEDE** relajar reglas base.
3. **DEBE** vivir en un artefacto KORA/Spec-MD propio.
4. **DEBE** declarar explicitamente que especificacion extiende.

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

## 8. Invariantes

1. La jerarquia de precedencia **NO DEBE** alterarse por una spec subordinada sin actualizar este documento.
2. Solo existen los regimenes de identidad definidos en §4.
3. Toda linea `Traces to:` **DEBE** apuntar a la Formal Layer oficial.
4. Ninguna extension **PUEDE** relajar reglas base.
5. Una fibra adjunta de Skill extendido **NO PUEDE** introducir identidad, kind ni precedencia paralelos al entrypoint que la gobierna.

## 9. Validacion

| Check                   | Criterio                                                      | Enforcement | Accion si falla                          |
| ----------------------- | ------------------------------------------------------------- | ----------- | ---------------------------------------- |
| Precedencia consistente | Ninguna spec subordinada contradice una capa superior         | manual      | Reescribir regla o actualizar gobernanza |
| Identidad consistente   | Solo existen los dos regimenes de identidad definidos en §4   | lint        | Migrar URNs                              |
| Kind de Skill consistente | Todo entrypoint de Skill usa `lazy_load_endofunctor` y las fibras adjuntas no crean kinds nuevos | lint/manual | Corregir entrypoint o bundle             |
| Traces oficiales        | Toda linea `Traces to:` apunta a la Formal Layer oficial      | lint        | Corregir o degradar a `Rationale:`       |
| Extensiones acotadas    | No hay metadata ad hoc fuera de `extensions.{namespace}`      | schema      | Reubicar extension                       |
| Enforcement declarado   | Las tablas nuevas o reescritas incluyen columna `Enforcement` | lint        | Completar tabla                          |
