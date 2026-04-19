---
_manifest:
  urn: "urn:kora:kb:requirement-traceability-model"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-19"
    source: "Cierre H9: formaliza requirement como nodo direccionable y el edge TracesRequirement dentro de KnowCat."
version: "1.0.0"
status: publicado
tags: [requirement, traceability, knowledge, graph, kora]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:procesos-spec"
    - "urn:kora:kb:cat-governance-lattice"
  refines:
    - "urn:kora:kb:knowledge-spec"
  traces_requirements:
    - "urn:kora:kb:req-knowledge-graph-must-materialize-traces"
---

# Modelo de trazabilidad de requirements en KORA

## 1. Problema

KORA ya modelaba relaciones tipadas entre artefactos (`cites`, `depends`,
`supersedes`, `refines`), pero le faltaba una traza vertical explicita entre
un **requirement** y el artefacto que lo realiza, verifica o satisface. Eso
dejaba incompleta la composicion entre `requirements -> design -> construction
-> verification` descrita en el corpus categorial.

## 2. Decision canonica

KORA introduce el edge:

- `relations.traces_requirements`

que en el grafo derivado se materializa como:

- `TracesRequirement`

Su lectura es:

> este artefacto traza requirements publicados que declara implementar,
> satisfacer, verificar o realizar.

## 3. Que cuenta como requirement

En KORA, un requirement no es texto flotante. Es un nodo direccionable por URN
que expresa alguno de estos papeles:

- obligacion
- constraint
- predicate de aceptabilidad
- requirement explicito derivado de una spec, contrato o artefacto normativo

Operativamente, un requirement puede vivir como artefacto publicado propio o
como familia documental cuyos metadatos y cuerpo lo tipan sin ambiguedad.

## 4. Semantica categorial

Categoricamente, un requirement es un subobjeto o predicado sobre el espacio de
comportamientos aceptables. `TracesRequirement` no reemplaza `depends` ni
`cites`: agrega la flecha vertical que conecta un requirement con su
realizacion o verificacion.

Distincion:

- `cites`: usa como soporte
- `depends`: necesita para interpretar
- `refines`: precisa sin reemplazar
- `traces_requirements`: declara realizacion o satisfaccion de requirement

## 5. Regla de uso

Un artefacto DEBE usar `traces_requirements` cuando:

- el requirement es parte del contrato que implementa o verifica
- la traza debe sobrevivir como edge en el grafo

NO DEBE usarse solo para mencionar requirements de contexto. En ese caso,
corresponde `cites`.

## 6. Ejemplo minimo

```yaml
relations:
  cites:
    - "urn:kora:kb:knowledge-spec"
  traces_requirements:
    - "urn:kora:kb:req-demo"
```

Lectura:

- el artefacto cita `knowledge-spec` como soporte
- y traza `req-demo` como requirement que realiza o verifica
