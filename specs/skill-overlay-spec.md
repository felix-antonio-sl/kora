---
_manifest:
  urn: "urn:kora:kb:skill-overlay-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "capability profile portable canonico; v1.1 alinea lifecycle con gobernanza §5 (agrega retired)"
version: "1.1.0"
status: published
tags: [spec, skill, overlay, portable, capability]
lang: es
extensions: {}
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
---

# KORA/Skill-Overlay-Spec v1.1.0

## 1. Definicion

El skill moderno de KORA es un perfil portable `SKILL.md` compatible con
runtimes tipo agentskills.io y enriquecido con overlay KORA. Este es el formato preferido de capacidad.

## 2. Contrato minimo portable

Todo skill portable **DEBERIA** declarar:

- `name`
- `description`
- `allowed-tools`

Overlay KORA recomendado:

- `metadata.kora.urn`
- `metadata.kora.lifecycle`
- `metadata.kora.tools`
- `metadata.kora.knowledge`
- `metadata.kora.domain`
- `metadata.kora.composable_with`

## 3. Principios

1. Portabilidad primero.
2. Overlay sin colision.
3. Capacidad pequeña y componible.
4. Dependencias explicitas.

El overlay agrega trazabilidad y gobierno; no debe romper la utilidad del skill
si un runtime ignora `metadata.kora.*`.

## 4. Ubicacion y topologia

Ubicaciones validas:

- `SKILLS/{name}/SKILL.md`
- `SKILLS/{namespace}/{name}/SKILL.md`

No todo lo que vive bajo `SKILLS/` reclama esta spec. El catalogo puede mezclar
perfiles portables con bundles legacy o artefactos auxiliares.

## 5. Composicion y alias

Un skill portable **PUEDE**:

- componerse con otros,
- declarar conocimiento requerido,
- tiene alias o espejo `CM-*` por compatibilidad.

Pero:

1. no expande el dominio del agente por si mismo,
2. no suplanta `safety`,
3. no necesita un alias CM para ser valido.

## 6. Lifecycle

Los skills son artefactos ejecutables. Su lifecycle se alinea con
`gobernanza §5`:

- `draft` — aun no se carga en runtime
- `active` — productivo, resolvible por agentes
- `deprecated` — se conserva pero nuevos agentes no deben invocarlo
- `retired` — no debe cargarse; se mantiene por trazabilidad historica,
  su `_manifest.urn` no resuelve en runtime

Las transiciones inversas son invalidas. Un skill `retired` **NO PUEDE**
reactivarse; debe emitirse uno nuevo con `supersedes` hacia el retirado.

## 7. Validacion

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Portabilidad base | `name`, `description`, `allowed-tools` validos | lint |
| Overlay limpio | `metadata.kora.*` no contradice la capa portable | lint/manual |
| Topologia valida | El skill vive en topologia admitida | lint |
| Alias trazable | Si tiene espejo CM, el vinculo es explicito | manual/lint |

## 8. Migracion

Contrato vigente v1:

- el skill portable pasa a ser la forma canonica,
- `CM-*` queda absorbido como perfil de compatibilidad dentro de esta spec,
- el sistema moderno modela capacidades como perfiles pequeños, no como bundles
  estructuralmente centrales.
