---
_manifest:
  urn: "urn:kora:kb:knowledge-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "KORA categorical-foundations 00, 02, 04, 05; md-spec v7.1.0; gobernanza v4.3.0; v1.2 alinea con autoria-spec unificada; v1.3 agrega requirements trazables y productor canonico atomic"
version: "1.3.0"
status: publicado
tags: [knowledge, categoria, grafo, pipeline, namespace, artefacto]
lang: es
extensions: {}
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
---

# KORA/Knowledge-Spec v1.3.0

## 1. Definicion

Esta spec define el sistema de conocimiento KORA como una categoria materializada
en artefactos Markdown con relaciones tipadas. Su objetivo es convertir
`artifacts/knowledge/` en un corpus gobernado, direccionable y componible por humanos,
agentes y tooling.

### 1.1 Fundamento categorico

El conocimiento KORA forma una categoria `KnowCat`:

- objetos: artefactos con `_manifest.urn`,
- morfismos: relaciones tipadas entre artefactos,
- composicion: clausura de cadenas de dependencia o refinamiento,
- identidad: cada artefacto preserva su URN como objeto estable.

### 1.2 Alcance

Gobierna:

1. tipos de artefacto admitidos en `artifacts/knowledge/`,
2. el campo raiz `relations`,
3. namespaces y responsabilidad editorial,
4. pipeline de ingesta y publicacion,
5. el grafo derivado de conocimiento.

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Nodo de conocimiento | Artefacto publicado o en proceso con `_manifest.urn`. |
| Morfismo | Relacion tipada entre nodos. |
| Namespace | Subcategoria editorial y semantica dentro del corpus. |
| Artefacto publicado | Nodo con `status: publicado`, recuperable por el ecosistema. |
| Requirement | Predicado, constraint u obligacion que un sistema o artefacto debe satisfacer; en KORA se publica como nodo direccionable por URN, no como texto flotante. |
| Crudo | Material sin normalizar que aun no debe consumirse como ley o conocimiento estable. |
| Grafo derivado | Vista materializada de `KnowCat` para consulta, auditoria y routing. |

## 3. Tipos de artefacto

Los tipos funcionales admitidos en `artifacts/knowledge/` son las **familias
documentales** declaradas por `md-spec §5.6` — fuente unica y autoritativa
de la taxonomia. Esta spec no duplica la lista; si necesitas el catalogo
operativo de familias, lee `md-spec §5.6`.

Reglas:

1. La clasificacion por familia es semantica, no una carpeta obligatoria.
2. Lo que vuelve valido a un artefacto es su conformidad con `md-spec` y
   con los invariantes de la familia correspondiente, junto con su URN.
3. Un artefacto **PUEDE** declarar su familia via
   `extensions.{namespace}.family` o delegar la clasificacion a los
   mecanismos de `md-spec §5.6` (convencion de directorio, curaduria
   manual, productor canonico).
4. La familia `spec` vive exclusivamente en `specs/` y no en `artifacts/knowledge/`;
   las demas familias **PUEDEN** residir en `artifacts/knowledge/` segun su ciclo
   de publicacion.

## 4. Morfismos de KnowCat

Las relaciones se declaran en el campo raiz `relations` reservado por
`md-spec §3.2`.

### 4.1 Tipos permitidos

| Relacion | Significado |
| --- | --- |
| `cites` | Usa o menciona otro artefacto como soporte. |
| `depends` | Necesita que otro artefacto exista para interpretarse correctamente. |
| `supersedes` | Reemplaza semanticamente a otro artefacto. |
| `refines` | Especializa o precisa otro artefacto sin reemplazarlo. |
| `traces_requirements` | Declara que el artefacto implementa, satisface, verifica o realiza requirements publicados. En el grafo derivado se materializa como edge `TracesRequirement`. |

### 4.2 Reglas

1. Toda relacion **DEBE** apuntar a URNs resolubles.
2. `supersedes` **NO DEBE** usarse como sinonimo de "menciona".
3. `refines` **NO DEBE** contradecir el artefacto refinado; si lo reemplaza,
   corresponde `supersedes`.
4. `traces_requirements` **DEBE** apuntar a nodos cuyo cuerpo o metadatos explicitan
   que son requirements, obligations, constraints o predicates normativos equivalentes.
5. La precedencia normativa entre specs **NO** se decide aqui; se decide solo en
   `gobernanza`.

## 5. Namespaces

Un namespace define contorno editorial y ownership semantico. Sus funciones son:

- agrupar dominio,
- reducir ambiguedad de routing,
- facilitar stewardship.

Reglas:

1. Un namespace **DEBERIA** mantener terminos y URNs estables.
2. El naming **DEBERIA** tender a kebab-case para artefactos nuevos.
3. Los namespaces pueden coexistir aunque sus corpus se citen mutuamente.

## 6. Pipeline como cadena de funtores

El pipeline de conocimiento vive **dentro de `artifacts/knowledge/`** en el staging area
dedicado `_SCRIPTORIUM/`. No existe pipeline centralizado fuera de
`artifacts/knowledge/`.

Topologia canonica:

```
artifacts/knowledge/_SCRIPTORIUM/INBOX/   <- material crudo, pre-categorial, sin URN asignado
artifacts/knowledge/_SCRIPTORIUM/REVIEW/  <- borradores con URN provisional, status: borrador, listos para auditar
artifacts/knowledge/{ns}/...              <- productivo con status: publicado o deprecado
```

El pipeline canonicamente es:

1. **intake** — material crudo llega a `_SCRIPTORIUM/INBOX/`. Los
   subdirectorios de `INBOX/` son opacos al toolchain (no representan
   namespace KORA).
2. **normalize** — el curador (humano o skill canonico) convierte el crudo
   a artefacto KORA/MD conforme a `md-spec`; el resultado pasa a
   `_SCRIPTORIUM/REVIEW/` con `status: borrador` y URN provisional.
3. **enrich** — se agregan `relations`, `tags` y `provenance`.
4. **publish** — `kora promote` mueve de `REVIEW/` a `artifacts/knowledge/{ns}/...`
   cambiando `status: borrador -> publicado`.
5. **graph** — `kora index` + `kora kb-graph` materializan los morfismos
   derivados.

Reglas:

1. Un artefacto con `status: publicado` o `status: deprecado` **NO PUEDE**
   residir en `_SCRIPTORIUM/`.
2. Un artefacto con `status: borrador` **NO PUEDE** residir en
   `artifacts/knowledge/{ns}/...` productivo.
3. Los subdirectorios de `INBOX/` son **pre-categoriales**: no implican
   namespace KORA. El namespace se asigna en `REVIEW/` como URN
   provisional y se confirma al promover a productivo.

## 7. Grafo de conocimiento

El grafo derivado **DEBE** construirse a partir de frontmatter, no de scraping
heuristico del body.

Usos canonicos:

- resolver URNs,
- detectar huerfanos,
- calcular dependencias transitivas,
- alimentar `allowed_kb` y routing de agentes,
- materializar trazabilidad vertical requirement -> implementacion/verificacion,
- auditar supersesion y drift editorial.

## 8. Invariantes

Los invariantes del sistema de conocimiento son:

1. todo nodo publicado tiene URN,
2. `relations` es tipado y resoluble,
3. la precedencia normativa no se autodeclara en cada artefacto,
4. un nodo no puede estar simultaneamente supersedido y fuente primaria del
   mismo contrato sin explicitar migracion,
5. lo crudo no se consume como ley publicada,
6. toda `TracesRequirement` del grafo debe provenir de `relations.traces_requirements`
   y apuntar a requirements direccionables.

## 9. Validacion

Checks minimos:

| Check | Condicion | Enforcement |
| --- | --- | --- |
| URN valido | `_manifest.urn` presente y resoluble | lint |
| `relations` valido | shape correcto y URNs conocidos | lint |
| `TracesRequirement` valido | targets resolubles y semanticamente requirement | lint/graph |
| Lifecycle coherente | `status` consistente con estado del pipeline | lint/manual |
| Huerfano critico | artefacto esperado sin relaciones de entrada o salida | graph/manual |
| Supersesion limpia | `supersedes` sin loops absurdos | graph |

## 10. Migracion desde estado actual

Plan minimo:

1. mantener `relations` como opcional para retrocompatibilidad,
2. agregar relaciones solo donde la dependencia sea real,
3. mover naming legacy a naming estable sin romper URNs existentes salvo plan
   explicito,
4. distinguir crudo, draft y published con lifecycle claro.

## 11. Relacion con otras specs

- `md-spec` gobierna formato y perfiles; esta spec gobierna el tejido
  relacional.
- `gobernanza` decide precedencia; `knowledge-spec` **NO** la reescribe.
- `autoria-spec` y `runtime-spec` consumen conocimiento a traves de `conocimiento_permitido`, routing o metadata de conocimiento.

## 12. Productores canonicos de familia

Algunas familias documentales de `md-spec §5.6` tienen un productor canonico.
El productor canonico es la herramienta autorizada para generar artefactos de
esa familia cumpliendo sus invariantes.

### 12.1 Principio

Una familia **PUEDE** declararse con productor canonico cuando la generacion
del artefacto se beneficia de un workflow gobernado, regenerable y verificable.
En ese caso:

1. El productor garantiza el cumplimiento de los invariantes de la familia
   (`md-spec §5.6`) y constituye la unica ruta soportada de emision para esa
   familia.
2. La autoria editorial se ejerce sobre el corpus fuente, no sobre el artefacto
   generado.
3. La regeneracion **PUEDE** hacerse bajo demanda sin alterar la identidad
   URN del artefacto.

### 12.2 Registro de productores

| Familia  | Productor canonico            | Output                                          | Namespace fijo |
| -------- | ----------------------------- | ----------------------------------------------- | -------------- |
| `atomic` | `artifacts/skills/_TALLER/INBOX/atomize/SKILL.md` (staging, sin URN productivo vigente) | `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-{slug}.md` | `kora`         |

### 12.3 Reglas operativas

1. Un artefacto de familia con productor canonico **DEBERIA** ser regenerable
   desde el corpus fuente declarado en
   `extensions.kora.{family}.source_corpus` (o campo equivalente), pero solo
   si la regeneracion sigue cumpliendo `md-spec §6.11` y `FS=100%`.
2. Si el artefacto se edita a mano despues de generarse, **DEBE** declararse
   `extensions.kora.{family}.hand_edited: true` para que el productor no lo
   sobreescriba en la siguiente corrida.
3. El productor canonico **DEBE** emitir artefactos con `status: borrador` en
   `artifacts/knowledge/_SCRIPTORIUM/REVIEW/`; la promocion a `artifacts/knowledge/{ns}/...` pasa
   por `kora promote`, sujeta a los checks de `md-spec §6.10` y `§6.11` y a
   la coherencia de namespace (`md-spec §3.1` regla 7).
4. El productor canonico **DEBE** declararse en su salida mediante
   `extensions.kora.{family}.producer: urn:...`.
5. Una familia con productor canonico **PUEDE** aceptar reparacion manual
   posterior sobre artefactos ya emitidos por el productor. Esa reparacion es
   excepcional y verificable; **NO** constituye una ruta alternativa de
   generacion.
6. En la familia `atomic`, `atomize` es la unica ruta soportada para emitir
   nuevos artefactos de familia. Ningun scaffold mecanico, wrapper auxiliar o
   segmentacion automatica fuera de `atomize` **PUEDE** tratarse como opcion
   equivalente.
7. En la familia `atomic`, una corrida de `atomize` que colapsa, omite o mezcla
   hechos del cuerpo sustantivo del documento **NO** satisface la spec aunque el
   archivo lintee.

Nota operativa: publicar un `atomic` que actue como `scaffold semantico degradado`
viola esta spec aunque el archivo lintee.

### 12.4 Aislamiento de responsabilidades

- `md-spec` define los invariantes de la familia.
- `knowledge-spec` declara el productor canonico y sus reglas operativas.
- El productor concreto (skill, script, pipeline) vive fuera de ambas specs
  y es consumidor de ellas.

Esta separacion garantiza que un cambio en el productor **NO** requiera bump
de las specs, y que un cambio en las specs **SI** requiera revisar al
productor.
