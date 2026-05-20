---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-20-kora-v9"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-20"
    source: "Directiva HITL del operador 2026-05-20: especificacion para documentos descriptivos y prescriptivos diferenciadas; skills y agents pueden ser lo mismo pero varian por el arnes."
version: "1.0.0"
status: publicado
tags: [handoff, kora-v9, separacion-md-spec, spec-md, arnes-discriminante, autoria-v2]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:spec-md"
    - "urn:kora:kb:autoria-spec"
---

# Handoff 2026-05-20 — KORA v9: separacion descriptivo/prescriptivo + arnes discriminante

## Resumen ejecutivo

Esta sesion implementa la directiva HITL del operador (2026-05-20):
dos cambios doctrinales coordinados.

### Cambio 1: Separacion descriptivo/prescriptivo

`md-spec v10 → v11`: reducida a regimen descriptivo puro (~700 lineas).
`spec-md v1.0.0` nueva en `serialization/spec-md.md`: perfil
prescriptivo extraido (~280 lineas).

### Cambio 2: Arnes como discriminante ontologico

`autoria-spec v1.2 → v2.0`: nueva §4.6 declara que skills y agents son
**el mismo objeto agentico** distinguidos por el arnes categorial; la
forma material es proyeccion operacional, no taxonomia ontologica.

Decision arquitectural en
`urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes`.

## Cambio 1 — Detalle: spec-md vuelve al canon

### Nueva spec-md v1.0.0

`serialization/spec-md.md` con 13 secciones:

| Seccion | Contenido | Origen en md-spec v10 |
|---------|-----------|------------------------|
| §1 Definicion | perfil prescriptivo del envelope | §5.6.1 intro |
| §2 Definiciones | keyword, regla, cristalizacion, etc. | (consolidadas) |
| §3 Cristalizacion | funtor C, propiedades | §5.6.1.1 |
| §4 Lenguaje RFC 2119 | 5 keywords + 4 reglas | §5.6.1.2 |
| §5 Convencion de trazabilidad | Traces to / Rationale | §5.6.1.3 |
| §6 Elementos retoricos | Correcto/Incorrecto, Rationale, Tabla | §5.6.1.4 |
| §7 Prosa explicativa admisible | 4 funciones validas | §5.6.1.5 |
| §8 Patron regla+ejemplo+traza | 3 pasos | §5.6.1.6 |
| §9 Invariantes prescriptivos | 6 invariantes (consistencia, auto-suficiencia, no-circularidad, idioma, enforcement, integridad) | §5.6.1.7 + §7.6 |
| §10 Template esqueleto | 7 secciones obligatorias | §5.6.1.8 |
| §11 Auto-declaracion precedencia | regla de especializacion | §5.6.1.9 |
| §12 Validacion | 9 checks | filas spec en §9 |
| §13 Migracion | v1.0 reactivacion | (nueva) |

URN `urn:kora:kb:spec-md` regresa al canon (estaba retirado desde
md-spec v8.0, 2026-04-16).

### md-spec v11.0.0 reducida

- §5.6.1 perfil spec eliminado entero (9 subsecciones de 173 lineas)
- §5.6.1 actualizada como **delegado**: la familia `spec` declara que
  sus invariantes prescriptivos viven en spec-md
- §7.6 integridad perfil prescriptivo eliminada
- §9 tabla validacion: 9 filas spec eliminadas
- §1 Definicion reformulada: md-spec gobierna solo descriptivo;
  spec-md cubre prescriptivo
- §10.0 Contrato vigente v11 documenta los cambios

## Cambio 2 — Detalle: arnes como discriminante

### autoria-spec v2.0.0

Nueva §4.6 "Arnes como discriminante ontologico":

> Skills y agents NO son ontologicamente categorias distintas. Son
> proyecciones operacionales del mismo objeto agentico, distinguidas
> por el arnes categorial que ocupan en el espacio PMI × LFS.

Cuatro reglas:

1. **Identidad ontologica** = `(arnes_categorico, vector_ontologico)`.
2. **Forma material es derivada operacional**, no discriminante.
3. **Topologia fisica preservada** (`artifacts/skills/` y
   `artifacts/agents/`) por conveniencia operacional, no taxonomia.
4. **Promocion entre formas** preserva arnes.

Tabla de correspondencia arnes → forma material tipica:

| Arnes | Tipica | Alternativa |
|-------|--------|-------------|
| utilidad | habilidad | subagente |
| disciplina | habilidad | subagente |
| delegado | subagente | habilidad |
| persona | agente-propiamente-tal | subagente |
| orquestador | agente-propiamente-tal | agente-plataforma |
| servicio | agente-plataforma | --- |
| arquetipo | meta | --- |

## Cambio 3 — gobernanza

`gobernanza.md` actualizada:

- §3 lista jerarquica: `md-spec` (descriptivo) + `spec-md` (prescriptivo).
- §3.2 capa serializacion: tabla incluye `spec-md`.
- §3.4 regla de especializacion: `spec-md` para perfil prescriptivo.

(Sin bump de version: cambios menores que no rompen contratos.)

## Lo que NO se toca

- **41 artefactos productivos** (6 agents + 35 skills): SKILL.md y
  AGENT.md preservados sin mover, sin renombrar.
- **Topologia fisica** `artifacts/skills/` y `artifacts/agents/`.
- **harness-spec**: sigue en freeze (es la ontologia PMI × LFS; el
  refactor de autoria no requiere tocarla).
- **toolchain**: el shape skill/agent permanece igual; el discriminante
  ontologico es declarativo, no requiere cambio en codigo.

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 643 artefactos indexados (+ADR v9 + spec-md nueva) |
| `python3 toolchain/kora check --strict` | 28/29 verdes; 1 HIGH preexistente WIP operador en `HANDOFF.md` |
| `python3 -m unittest discover -s tests` | resultado en commit (en background) |

## Estado consolidado

### Que cerramos

- spec-md v1.0 regresa al canon con perfil prescriptivo completo.
- md-spec v11 queda descriptivo puro.
- autoria-spec v2.0 declara arnes como discriminante ontologico.
- gobernanza ajustada para registrar spec-md en taxonomia.
- ADR v9 producido con alternativas, consecuencias, factorizacion.

### Que queda como deuda

1. **Refs cruzadas en `_TALLER/INBOX/_rebuild_required/`** que apuntan
   a `md-spec §5.6.2.X` (ahora `spec-md §X` o `md-spec §5.6.1.X`
   delegado). Quedan obsoletas pero son material pre-categorial; no se
   tocan.
2. **toolchain checks** que verifican specs prescriptivas usan ahora
   spec-md como `spec_ref`; algunos checks aun usan refs a md-spec
   §5.6.2 (deuda menor, no rompe operacion).
3. **Matriz §6 de autoria-spec**: doctrinalmente reconocida como
   parcialmente redundante con el arnes; refactor mecanico podria
   consolidar filas, pero no es urgente.

### Que NO debe asumirse

- No asumir que skill/agent siguen siendo categorias distintas: en
  autoria-spec v2.0 son **proyecciones operacionales** del mismo
  objeto.
- No asumir que el URN `urn:kora:kb:spec-md` sigue retirado: regresa
  al canon como nodo activo v1.0.0.
- No asumir que md-spec sigue gobernando regimen prescriptivo: solo
  descriptivo. El regimen prescriptivo vive en spec-md.

## Artefactos dejados versionados

### Specs
- `serialization/md-spec.md` v11.0.0 (descriptivo puro).
- `serialization/spec-md.md` v1.0.0 (nueva, prescriptivo).
- `serialization/autoria-spec.md` v2.0.0 (arnes como discriminante).
- `governance/gobernanza.md` (taxonomia actualizada, sin bump).

### Knowledge
- `artifacts/knowledge/kora/adr/adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes.md`
  (familia adr).

### Docs
- `docs/handoffs/2026-05-20-kora-v9-separacion-prescriptivo-y-arnes.md`
  (este).

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-20-kora-v9-separacion-prescriptivo-y-arnes.md`.

Contexto vigente:

- md-spec v11.0.0 cubre solo regimen descriptivo.
- spec-md v1.0.0 cubre regimen prescriptivo (RFC 2119, Traces to,
  cristalizacion, invariantes prescriptivos). URN urn:kora:kb:spec-md
  regresa al canon.
- autoria-spec v2.0.0 declara arnes como discriminante ontologico;
  skills y agents son el mismo objeto agentico variando por arnes.
- 41 artefactos productivos no se mueven; topologia fisica
  artifacts/skills/ y artifacts/agents/ preservada por conveniencia
  operacional.

Para Fase 2b (si se desea continuar):
1. Compactar md-spec v11 a ~600 lineas (poda redundancia descriptiva).
2. Consolidar matriz §6 de autoria-spec donde redundante con arnes.
3. Limpiar refs cruzadas en `_TALLER/INBOX/_rebuild_required/` si
   se reactivan esos skills.
4. Refactor checks toolchain para usar spec-md como spec_ref donde
   aplique.

Mantener disciplina: no mover artefactos productivos sin HITL + ADR.
```
