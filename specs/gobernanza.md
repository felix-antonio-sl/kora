---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 00-07, RFC 2119"
version: "3.0.0"
status: published
tags: [gobernanza, constitucion, precedencia, identidad, enforcement]
lang: es
---

# KORA/Gobernanza v3.0.0

## 1. Definicion

Este documento es la constitucion operativa de KORA. Gobierna unicamente cuatro materias:

1. Precedencia entre especificaciones.
2. Identidad de artefactos.
3. Extensiones del ecosistema.
4. Niveles de enforcement.

Todo lo demas pertenece a la especificacion del artefacto correspondiente.

Traces to: formal/05 §1.2 (Bounded Lattice)

## 2. Precedencia

Cuando dos reglas se contradicen, prevalece la capa mas alta de esta jerarquia:

1. `gobernanza.md`
2. `spec-md.md` y `md-spec.md`
3. `agent-spec-md.md`, `skill-spec-md.md`, `runtime-spec-md.md`, `swarm-spec-md.md`
4. Extensiones de namespace
5. Documentacion derivada, plantillas y README

Si un conflicto no puede resolverse por dominio, este documento **DEBE** actualizarse antes de aceptar la coexistencia de ambas reglas.

## 3. Identidad

KORA reconoce dos clases de artefacto.

### 3.1 Artefactos conceptuales

- Regimen: `urn:{namespace}:{type}:{id}`
- Version: en el campo raiz `version`
- Tipos: `kb`, `doc`, `ref`, `core`, `domain`

Estos artefactos describen conocimiento, reglas o referencias estables. Su URN identifica el concepto, no el snapshot.

### 3.2 Artefactos ejecutables

- Regimen: `urn:{namespace}:{type}:{id}:{version}`
- Tipos: `agent-bootstrap`, `skill`

Estos artefactos participan en ejecucion, deployment o composicion operacional. Su URN identifica un snapshot ejecutable.

### 3.3 Reglas

1. Un componente bootstrap de agente **DEBE** usar `agent-bootstrap`.
2. Un Skill, degenerado o extendido, **DEBE** usar `skill`.
3. Un CM degenerado **ES** un Skill; **NO DEBE** usar identidad `agent-bootstrap`.
4. Ninguna especificacion subordinada **PUEDE** definir un tercer regimen de identidad sin cambiar este documento.

### 3.4 Manifest kind

La identidad URN y `_manifest.type` son ortogonales.

1. La URN gobierna el regimen identitario (`agent-bootstrap` o `skill`).
2. `_manifest.type` gobierna el kind estructural del artefacto ejecutable.
3. Para bootstraps de agente, los kinds permitidos son `bootstrap_agents`, `bootstrap_soul`, `bootstrap_user`, `bootstrap_tools`, `bootstrap_config`.
4. Para Skills degenerados, el kind permitido es `lazy_load_endofunctor`.
5. Ninguna spec subordinada **PUEDE** introducir kinds adicionales sin declararlos primero aqui.

Traces to: formal/01 §5.2 (Substitutability) ; formal/05 §1.3 (Domain Disjointness)

## 4. Formal Layer

### 4.1 Capa oficial

La unica Formal Layer oficial de KORA es `knowledge/kora/categorical-foundations/`.

`Traces to:` **DEBE** referenciar exclusivamente documentos de esa capa.

### 4.2 Corpus auxiliar

`knowledge/fxsl/cat/` y cualquier otro corpus categorial adicional son auxiliares. Pueden informar diseño, auditoría o crítica, pero **NO DEBEN** respaldar `Traces to:` directamente.

Si un concepto auxiliar pasa a justificar reglas operacionales, **DEBE** absorberse mediante un documento puente dentro de la Formal Layer oficial.

## 5. Extensiones

Una extension de namespace:

1. **PUEDE** agregar restricciones.
2. **NO PUEDE** relajar reglas base.
3. **DEBE** vivir en un artefacto KORA/Spec-MD propio.
4. **DEBE** declarar explicitamente que especificacion extiende.

Las extensiones de metadata se expresan unicamente dentro del campo `extensions.{namespace}` del artefacto gobernado.

## 6. Enforcement

Toda regla importante de KORA cae en uno de cuatro niveles:

| Nivel | Semantica |
| --- | --- |
| `schema` | Verificable por parseo o validacion estructural |
| `lint` | Verificable por inspeccion estatica del repo |
| `runtime` | Verificable solo durante ejecucion u orquestacion |
| `manual` | Requiere juicio humano |

Reglas fundacionales que no admiten enforcement razonable **DEBERIAN** expresarse como `DEBERIA`, salvo invariantes identitarios, de seguridad o de trazabilidad.

## 7. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Precedencia consistente | Ninguna spec subordinada contradice una capa superior | manual | Reescribir regla o actualizar gobernanza |
| Identidad consistente | Solo existen los dos regímenes de identidad definidos en §3 | lint | Migrar URNs |
| Traces oficiales | Toda línea `Traces to:` apunta a la Formal Layer oficial | lint | Corregir o degradar a `Rationale:` |
| Extensiones acotadas | No hay metadata ad hoc fuera de `extensions.{namespace}` | schema | Reubicar extension |
| Enforcement declarado | Las tablas nuevas o reescritas incluyen columna `Enforcement` | lint | Completar tabla |
