---
_manifest:
  urn: "urn:kora:kb:knowledge-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "KORA categorical-foundations 00, 02, 04, 05; md-spec v6.3.0; gobernanza v4.0.0"
version: "1.0.0"
status: published
tags: [spec, knowledge, categoria, grafo, pipeline, namespace, artefacto]
lang: es
extensions: {}
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
---

# KORA/Knowledge-Spec v1.0.0

## 1. Definicion

Esta spec define el sistema de conocimiento KORA como una categoria materializada
en artefactos Markdown con relaciones tipadas. Su objetivo es convertir
`KNOWLEDGE/` en un corpus gobernado, direccionable y componible por humanos,
agentes y tooling.

### 1.1 Fundamento categorico

El conocimiento KORA forma una categoria `KnowCat`:

- objetos: artefactos con `_manifest.urn`,
- morfismos: relaciones tipadas entre artefactos,
- composicion: clausura de cadenas de dependencia o refinamiento,
- identidad: cada artefacto preserva su URN como objeto estable.

### 1.2 Alcance

Gobierna:

1. tipos de artefacto admitidos en `KNOWLEDGE/`,
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
| Artefacto publicado | Nodo con `status: published`, recuperable por el ecosistema. |
| Crudo | Material sin normalizar que aun no debe consumirse como ley o conocimiento estable. |
| Grafo derivado | Vista materializada de `KnowCat` para consulta, auditoria y routing. |

## 3. Tipos de artefacto

Los tipos funcionales admitidos incluyen:

- spec
- guide
- glossary
- inventory
- FAQ
- catalog
- note tecnica

El tipo es semantico, no una carpeta obligatoria. Lo que vuelve valido a un
artefacto no es su nombre de archivo sino su conformidad con `md-spec` y su
perfil correspondiente, junto con su URN.

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

### 4.2 Reglas

1. Toda relacion **DEBE** apuntar a URNs resolubles.
2. `supersedes` **NO DEBE** usarse como sinonimo de "menciona".
3. `refines` **NO DEBE** contradecir el artefacto refinado; si lo reemplaza,
   corresponde `supersedes`.
4. La precedencia normativa entre specs **NO** se decide aqui; se decide solo en
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

El pipeline canonicamente es:

1. intake
2. normalize
3. enrich
4. publish
5. graph

Interpretacion:

- intake recibe material crudo,
- normalize lo lleva a `md-spec` y, si hace falta, a su perfil prescriptivo,
- enrich agrega relaciones, tags y provenance,
- publish cambia lifecycle y lo vuelve consumible,
- graph materializa los morfismos para consulta.

## 7. Grafo de conocimiento

El grafo derivado **DEBE** construirse a partir de frontmatter, no de scraping
heuristico del body.

Usos canonicos:

- resolver URNs,
- detectar huerfanos,
- calcular dependencias transitivas,
- alimentar `allowed_kb` y routing de agentes,
- auditar supersesion y drift editorial.

## 8. Invariantes

Los invariantes del sistema de conocimiento son:

1. todo nodo publicado tiene URN,
2. `relations` es tipado y resoluble,
3. la precedencia normativa no se autodeclara en cada artefacto,
4. un nodo no puede estar simultaneamente supersedido y fuente primaria del
   mismo contrato sin explicitar migracion,
5. lo crudo no se consume como ley publicada.

## 9. Validacion

Checks minimos:

| Check | Condicion | Enforcement |
| --- | --- | --- |
| URN valido | `_manifest.urn` presente y resoluble | lint |
| `relations` valido | shape correcto y URNs conocidos | lint |
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
- `agentfile-spec`, `skill-overlay-spec` y `runtime-spec` consumen conocimiento
  a traves de `allowed_kb`, routing o metadata de conocimiento.

## 12. Productores canonicos de familia

Algunas familias documentales de `md-spec §5.6` tienen un productor canonico.
El productor canonico es la herramienta autorizada para generar artefactos de
esa familia cumpliendo sus invariantes.

### 12.1 Principio

Una familia **PUEDE** declararse con productor canonico cuando la generacion
del artefacto se beneficia de determinismo mecanico. En ese caso:

1. El productor garantiza el cumplimiento de los invariantes de la familia
   (`md-spec §5.6`).
2. La autoria editorial se ejerce sobre el corpus fuente, no sobre el artefacto
   generado.
3. La regeneracion **PUEDE** hacerse bajo demanda sin alterar la identidad
   URN del artefacto.

### 12.2 Registro de productores

| Familia  | Productor canonico            | Output                                          | Namespace fijo |
| -------- | ----------------------------- | ----------------------------------------------- | -------------- |
| `atomic` | `urn:kora:skill:atomize:1.0.0` | `OPERATIONS/drafts/kora/atomic-{slug}.md`      | `kora`         |

### 12.3 Reglas operativas

1. Un artefacto de familia con productor canonico **DEBERIA** ser regenerable
   desde el corpus fuente declarado en
   `extensions.kora.{family}.source_corpus` (o campo equivalente).
2. Si el artefacto se edita a mano despues de generarse, **DEBE** declararse
   `extensions.kora.{family}.hand_edited: true` para que el productor no lo
   sobreescriba en la siguiente corrida.
3. El productor canonico **DEBE** emitir artefactos con `status: draft` en
   `OPERATIONS/drafts/{namespace}/`; la promocion a `KNOWLEDGE/` pasa por el
   pipeline normal (`kora promote`), sujeta al protocolo de auditoria de
   `gobernanza §10`.
4. El productor canonico **DEBE** declararse en su salida mediante
   `extensions.kora.{family}.producer: urn:...`.
5. Una familia con productor canonico **PUEDE** tambien aceptar edicion
   manual. En ese caso, el productor funciona como generador de baseline,
   no como unico emisor valido.

### 12.4 Aislamiento de responsabilidades

- `md-spec` define los invariantes de la familia.
- `knowledge-spec` declara el productor canonico y sus reglas operativas.
- El productor concreto (skill, script, pipeline) vive fuera de ambas specs
  y es consumidor de ellas.

Esta separacion garantiza que un cambio en el productor **NO** requiera bump
de las specs, y que un cambio en las specs **SI** requiera revisar al
productor.
