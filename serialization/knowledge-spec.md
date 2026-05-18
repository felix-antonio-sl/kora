---
_manifest:
  urn: "urn:kora:kb:knowledge-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "KORA categorical-foundations 00, 02, 04, 05; md-spec v7.1.0; gobernanza v4.3.0; v1.2 alinea con autoria-spec unificada; v1.3 agrega requirements trazables y productor canonico atomic; v2.0 absorbe reglas de pipeline (URN conceptual, lifecycle descriptivo, status por directorio, namespace-directory) desde md-spec §3.1 r7-10, formaliza la curacion como cadena de funtores adjuntos, y registra atomize en topologia productiva"
version: "2.0.0"
status: publicado
tags: [knowledge, categoria, grafo, pipeline, namespace, artefacto, curacion, lifecycle, urn]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
  cites:
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:qa-spec"
---

# KORA/Knowledge-Spec v2.0.0

## 1. Definicion

Esta spec define el **sistema de conocimiento KORA** como una categoria
materializada en artefactos Markdown con relaciones tipadas, y gobierna el
**pipeline de curacion** que produce versiones KORA publicables a partir de
material crudo.

Su objetivo es convertir `artifacts/knowledge/` en un corpus **gobernado**,
**direccionable** y **componible** por humanos, agentes y tooling.

### 1.1 Fundamento categorico

El conocimiento KORA forma una categoria `KnowCat`:

- **objetos**: artefactos con `_manifest.urn`,
- **morfismos**: relaciones tipadas entre artefactos (§6),
- **composicion**: clausura de cadenas de dependencia o refinamiento,
- **identidad**: cada artefacto preserva su URN como objeto estable durante
  todo su lifecycle.

El pipeline de curacion (§8) habita la misma categoria como una cadena de
funtores que llevan material crudo desde `_SCRIPTORIUM/INBOX/` hasta el
corpus productivo, preservando identidad URN una vez asignada.

### 1.2 Alcance

Esta spec gobierna:

1. **identidad URN** del regimen conceptual `urn:{ns}:kb:{id}` (§3),
2. **lifecycle conceptual** de artefactos KORA/MD (§4),
3. **familias documentales** admitidas en `artifacts/knowledge/` (§5),
4. **morfismos tipados** (`relations`) entre nodos de conocimiento (§6),
5. **namespaces** y responsabilidad editorial (§7),
6. **pipeline de curacion** `INBOX -> REVIEW -> productivo` (§8),
7. **productores canonicos de familia** (§9),
8. **grafo derivado de conocimiento** (§10),
9. **invariantes** y **validacion** (§11-§12),
10. **procedimientos operativos** CLI (§13).

`md-spec` es responsable del **formato** del envelope, gramatica estructural,
familias documentales y koraficacion (transformacion `DocHumano -> KORA/MD`).
`knowledge-spec` se monta sobre ese formato y agrega tejido relacional,
pipeline e identidad.

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Nodo de conocimiento | Artefacto KORA/MD publicado o en proceso con `_manifest.urn`. |
| Morfismo | Relacion tipada entre nodos (`cites`, `depends`, `supersedes`, `refines`, `traces_requirements`). |
| Namespace | Subcategoria editorial y semantica dentro del corpus; coincide con el primer subdirectorio bajo `artifacts/knowledge/`. |
| URN conceptual | Identidad bajo el regimen `urn:{ns}:kb:{id}` (`gobernanza §4.3`); aplica a todo artefacto KORA/MD descriptivo y a las specs. |
| Lifecycle conceptual | Maquina de estados `borrador -> publicado -> deprecado`; sin transiciones inversas. |
| Artefacto publicado | Nodo con `status: publicado`, residente en `artifacts/knowledge/{ns}/...`, recuperable por el ecosistema. |
| Artefacto en revision | Nodo con `status: borrador`, residente en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/{ns}/...`, con URN provisional. |
| Material crudo | Archivo pre-categorial sin URN asignado, residente en `artifacts/knowledge/_SCRIPTORIUM/INBOX/...`, no consumible como ley. |
| Requirement | Predicado, constraint u obligacion publicada como nodo direccionable por URN. |
| Productor canonico | Herramienta autorizada (skill, script, pipeline) para generar artefactos de una familia con garantia mecanica de sus invariantes (§9). |
| Grafo derivado | Vista materializada de `KnowCat` para consulta, auditoria y routing. |
| Cohorte | Subconjunto de borradores en `_SCRIPTORIUM/REVIEW/{ns}/` promovible en bloque, con invariante de cierre comun (`gobernanza §5.1`). |

## 3. Identidad URN conceptual

### 3.1 Regimen unico para conocimiento

Todo artefacto KORA/MD descriptivo (familias de §5 y specs gobernadas por
`md-spec`) **DEBE** usar el regimen conceptual:

```
urn:{namespace}:kb:{id}
```

Reglas:

1. La version **NO DEBE** incluirse en el URN; se declara en el campo
   `version` del frontmatter (`gobernanza §4.3`).
2. Referencias en `relations`, `cites` o body **DEBEN** usar la forma sin
   version; la resolucion de version corresponde al catalogo (`docs/generated/catalog.yml`).
3. Un mismo componente **NO DEBE** declarar URN en dos regimenes
   simultaneamente; la migracion entre regimenes obliga a emitir un
   `supersedes` explicito.

```text
Correcto:
  urn:kora:kb:harness-spec
  urn:kora:kb:md-spec
  urn:kora:kb:gobernanza

Incorrecto:
  urn:kora:kb:harness-spec:1.0.0   # version embebida
  urn:kora:harness-spec            # sin tipo
```

Rationale: el regimen artefacto agentico `urn:{ns}:artefacto:{id}` es
exclusivo de `autoria-spec`. Mezclarlos rompe la disciplina de fuente
primaria de `gobernanza §4`.

### 3.2 Coherencia namespace-directorio

Cuando el artefacto reside bajo `artifacts/knowledge/`, el namespace en el
URN **DEBE** coincidir con el primer subdirectorio bajo
`artifacts/knowledge/`.

```text
Correcto:
  artifacts/knowledge/kora/harness-spec.md   -> urn:kora:kb:<id>
  artifacts/knowledge/salud/hodom/glosario.md -> urn:salud:kb:<id>

Incorrecto:
  artifacts/knowledge/kora/file.md           -> urn:salud:kb:<id>
```

Enforcement: lint (`knowledge-zone` y `lint-md`).

Excepcion: artefactos KORA/MD que viven fuera de `artifacts/knowledge/`
(specs en `governance/`, `ontology/`, `serialization/`, `runtime/`)
derivan su namespace de la topologia de la spec canonica que los gobierna;
para ellos esta regla no aplica. La regla equivalente para `artifacts/agents/`
y `artifacts/skills/` la fija `autoria-spec`.

## 4. Lifecycle conceptual

### 4.1 Cadena de estados

Artefactos KORA/MD descriptivos siguen la cadena:

```
borrador  ->  publicado  ->  deprecado
```

Reglas:

1. Las transiciones inversas son **invalidas**. Un artefacto deprecado no es
   reactivable: si su funcion debe restaurarse, se emite uno nuevo con
   `supersedes` apuntando al deprecado.
2. La transicion `borrador -> publicado` **DEBE** pasar por `kora promote`
   (§13) o procedimiento equivalente que verifique:
   - verificacion mecanica de envelope (`md-spec §6.10`),
   - verificacion de fidelidad (`md-spec §6.11`),
   - coherencia namespace-directorio (§3.2),
   - resolubilidad de `relations` (§6).
3. La transicion `publicado -> deprecado` **DEBE** pasar por `kora deprecate`
   (§13), que detecta dependientes reversos y exige `--force` si los hay.

Correcto: `kora promote artifacts/knowledge/_SCRIPTORIUM/REVIEW/salud/hodom/glosario.md`.

Incorrecto: editar a mano `status: borrador -> publicado` y mover el archivo
sin pasar por `kora promote`.

Rationale: las transiciones via CLI son funtoriales y trazables; las
transiciones manuales rompen la auditoria del pipeline.

### 4.2 Status por directorio

La residencia fisica del artefacto **DEBE** ser coherente con su `status`:

| Status | Ubicacion valida |
| --- | --- |
| `borrador` | `artifacts/knowledge/_SCRIPTORIUM/INBOX/` (material crudo, sin URN) o `_SCRIPTORIUM/REVIEW/{ns}/...` (con URN provisional) |
| `publicado` | `artifacts/knowledge/{ns}/...` |
| `deprecado` | `artifacts/knowledge/{ns}/...` (permanece in-place; el lifecycle es estado, no movimiento) |

Reglas:

1. Un artefacto con `status: publicado` o `status: deprecado` **NO PUEDE**
   residir en `_SCRIPTORIUM/`.
2. Un artefacto con `status: borrador` **NO PUEDE** residir en
   `artifacts/knowledge/{ns}/` productivo.
3. Material en `_SCRIPTORIUM/INBOX/` **PUEDE** carecer de `_manifest` y URN;
   es pre-categorial.

Enforcement: schema + lint (`knowledge-zone`).

### 4.3 Distincion con lifecycle agentico

`autoria-spec §11` define un lifecycle distinto para artefactos agenticos
productivos (`borrador -> activo -> deprecado -> retirado`). Esa cadena
**NO** aplica a artefactos KORA/MD descriptivos y nunca debe confundirse
con la de §4.1.

## 5. Familias documentales

Las **familias documentales** son perfiles del formato KORA/MD declarados
por `md-spec §5.6`. Esta spec **NO** duplica el catalogo de familias: si
necesitas el listado autoritativo de invariantes por familia, lee
`md-spec §5.6`.

Reglas operativas:

1. La clasificacion por familia es semantica, no una carpeta obligatoria.
2. Lo que vuelve valido a un artefacto es su conformidad con `md-spec` y
   con los invariantes de la familia correspondiente, junto con su URN
   conceptual (§3).
3. Un artefacto **PUEDE** declarar su familia via
   `extensions.{namespace}.family` o delegar la clasificacion a los
   mecanismos de `md-spec §5.6` (convencion de directorio, curaduria
   manual, productor canonico).
4. La familia `spec` vive exclusivamente en las capas normativas
   (`governance/`, `ontology/`, `serialization/`, `runtime/`) y no en
   `artifacts/knowledge/`; las demas familias **PUEDEN** residir en
   `artifacts/knowledge/` segun su ciclo de publicacion.

## 6. Morfismos de KnowCat

Las relaciones se declaran en el campo raiz `relations` reservado por
`md-spec §3.2`.

### 6.1 Tipos permitidos

| Relacion | Significado |
| --- | --- |
| `cites` | Usa o menciona otro artefacto como soporte. |
| `depends` | Necesita que otro artefacto exista para interpretarse correctamente. |
| `supersedes` | Reemplaza semanticamente a otro artefacto. |
| `refines` | Especializa o precisa otro artefacto sin reemplazarlo. |
| `traces_requirements` | Declara que el artefacto implementa, satisface, verifica o realiza requirements publicados. En el grafo derivado se materializa como edge `TracesRequirement`. |

### 6.2 Reglas

1. Toda relacion **DEBE** apuntar a URNs **resolubles** en el catalogo
   (`docs/generated/catalog.yml`). Composicion de morfismos preserva
   resolubilidad: si `A --cites--> B` y `B --refines--> C`, las dos aristas
   deben ser resolubles independientemente.
2. `supersedes` **NO DEBE** usarse como sinonimo de "menciona". Su target
   **DEBE** quedar en `status: deprecado` o `status: retirado`.
3. `refines` **NO DEBE** contradecir el artefacto refinado; si lo
   reemplaza, corresponde `supersedes`.
4. `traces_requirements` **DEBE** apuntar a nodos cuyo cuerpo o metadatos
   explicitan que son requirements, obligations, constraints o predicates
   normativos equivalentes.
5. La precedencia normativa entre specs **NO** se decide aqui; se decide
   solo en `gobernanza`.

### 6.3 Leyes algebraicas por tipo de relacion

Cada tipo de relacion define una **subcategoria** de `KnowCat` con leyes
algebraicas propias. La unica relacion sin estructura de orden es `cites`
(que admite ciclos y simetria); las demas son ordenes parciales o DAGs
con propiedades verificables.

| Relacion | Estructura categorial | Aciclica | Transitiva en clausura | Antisimetrica | Enforcement |
| --- | --- | --- | --- | --- | --- |
| `cites` | relacion binaria libre | no | no | no | `urn-integrity` |
| `depends` | DAG estricto | **si** | si (clausura) | no aplica (irreflexiva) | `kb-graph-cycles` |
| `supersedes` | poset estricto | **si** | si (clausura) | **si** | `relations-laws` |
| `refines` | preorder estricto | **si** | si (clausura) | no exigida | `relations-laws` |
| `traces_requirements` | relacion many-to-many | no | no | no | `traces-requirements-semantics` |

Reglas algebraicas:

1. **Aciclicidad de `supersedes`**: ningun ciclo `A --supersedes--> ... --supersedes--> A`.
   Rationale: un artefacto no se reemplaza a si mismo; la cadena debe
   terminar en un nodo `deprecado` o `retirado` que no supersede a nada.
2. **Antisimetria de `supersedes`**: si `A --supersedes--> B`, entonces
   `B --supersedes--> A` es **invalido**. Rationale: la sucesion es
   orientada en el tiempo; bidireccionalidad rompe el lifecycle.
3. **Aciclicidad de `refines`**: ningun ciclo
   `A --refines--> ... --refines--> A`. Rationale: refinar es especializar;
   un nodo no se especializa a si mismo via cadena cerrada.
4. **Composicion de `depends` preserva aciclicidad** (corolario):
   si `A --depends--> B` y `B --depends--> C`, entonces `C --depends--> A`
   es invalido. Verificado mecanicamente por `kb-graph-cycles`.
5. **`cites` y `traces_requirements`** no tienen restricciones de orden;
   solo se verifica resolubilidad del target (regla 1 de §6.2).

Enforcement: lint via `relations-laws` (aciclicidad y antisimetria), graph
via `kb-graph-cycles` (DAG de `depends`).

### 6.4 Composicion y functorialidad

`relations` define el grafo dirigido subyacente a `KnowCat`. El catalogo
materializado por `kora index` actua como **functor** que preserva:

- **identidad**: todo URN existente en el filesystem aparece en el
  catalogo con la misma identidad.
- **composicion**: cadenas de relaciones (`A --depends--> B --depends--> C`)
  son traversables sin perdida.

`kb-graph --orphans` detecta violaciones de functorialidad: nodos sin
edges de entrada o salida que sugieren ruptura del tejido relacional.

## 7. Namespaces

Un namespace define **contorno editorial** y **ownership semantico**. Sus
funciones son:

- agrupar dominio,
- reducir ambiguedad de routing,
- facilitar stewardship.

Reglas:

1. Un namespace **DEBERIA** mantener terminos y URNs estables.
2. El naming **DEBERIA** tender a kebab-case para artefactos nuevos.
3. Los namespaces pueden coexistir aunque sus corpus se citen mutuamente.
4. La coherencia namespace-directorio es obligatoria (§3.2).

## 8. Pipeline de curacion

### 8.1 Topologia canonica

El pipeline vive **dentro de `artifacts/knowledge/`** en el staging area
dedicado `_SCRIPTORIUM/`. No existe pipeline centralizado fuera de
`artifacts/knowledge/`.

```
artifacts/knowledge/_SCRIPTORIUM/INBOX/   <- material crudo, pre-categorial, sin URN asignado
artifacts/knowledge/_SCRIPTORIUM/REVIEW/  <- borradores con URN provisional, status: borrador
artifacts/knowledge/{ns}/...              <- productivo, status: publicado o deprecado
```

### 8.2 Cadena de funtores

El pipeline es una composicion de funtores que progresivamente comprime
material crudo en conocimiento direccionable, preservando verdad y dotando
identidad:

```
Intake     : Crudo               -> _SCRIPTORIUM/INBOX/...
Normalize  : _SCRIPTORIUM/INBOX/ -> _SCRIPTORIUM/REVIEW/{ns}/... (asigna URN provisional)
Enrich     : _SCRIPTORIUM/REVIEW/ -> _SCRIPTORIUM/REVIEW/ (agrega relations, tags, provenance)
Publish    : _SCRIPTORIUM/REVIEW/ -> artifacts/knowledge/{ns}/... (kora promote)
Graph      : artifacts/knowledge/ -> docs/generated/catalog.yml + kb-graph (kora index, kora kb-graph)
```

Reglas:

1. **Intake**: material crudo (texto, OCR, exports humanos) entra a
   `_SCRIPTORIUM/INBOX/`. Los subdirectorios de `INBOX/` son **opacos al
   toolchain**: no representan namespace KORA. El namespace solo se asigna
   en `Normalize`.
2. **Normalize**: el curador (humano o productor canonico) convierte el
   crudo a artefacto KORA/MD conforme a `md-spec §6`; el resultado pasa a
   `_SCRIPTORIUM/REVIEW/{ns}/...` con `status: borrador` y URN provisional
   `urn:{ns}:kb:{id}`.
3. **Enrich**: se agregan `relations`, `tags` y `provenance`. La
   identidad URN del nodo no cambia.
4. **Publish**: `kora promote` mueve de `REVIEW/` a `artifacts/knowledge/{ns}/...`
   cambiando `status: borrador -> publicado`. La identidad URN del nodo
   **DEBE** preservarse byte-identical durante esta transicion.
5. **Graph**: `kora index` y `kora kb-graph` materializan los morfismos
   derivados como vista catalogo + grafo.

### 8.3 Composicion preserva identidad

La composicion `Publish ∘ Enrich ∘ Normalize` es la curacion completa de
un artefacto. Aunque cada paso es discrecional (puede iterarse), la
**identidad URN asignada en `Normalize` no cambia** en ninguno de los
pasos posteriores. Esta es la invariante functorial central del pipeline.

```text
Correcto:
  borrador  : _SCRIPTORIUM/REVIEW/salud/hodom/glosario.md     urn:salud:kb:<id>
  publicado : artifacts/knowledge/salud/hodom/glosario.md     urn:salud:kb:<id>   (mismo URN)
```

Incorrecto: cambiar el URN al promover ("ya esta publicado, le pongo otro
slug"). Eso es emitir un nodo distinto, no promover el existente. Si el
URN debe cambiar, hay que deprecar el anterior y emitir uno nuevo con
`supersedes`.

### 8.4 Cohortes

Una **cohorte** es un subconjunto de borradores en `_SCRIPTORIUM/REVIEW/{ns}/`
que se promueven en bloque (`kora promote-cohort {ns}`). Util cuando varios
nodos comparten dependencias o requieren cierre conjunto.

El comando `kora promote-cohort` aborta al primer fallo para preservar
composicion: no permite promociones parciales que dejen el grafo en estado
inconsistente.

## 9. Productores canonicos de familia

Algunas familias documentales tienen **productor canonico**: herramienta
autorizada para generar artefactos de esa familia cumpliendo sus
invariantes.

### 9.1 Principio

Una familia **PUEDE** declararse con productor canonico cuando la
generacion del artefacto se beneficia de un workflow gobernado,
regenerable y verificable. En ese caso:

1. El productor garantiza el cumplimiento de los invariantes de la familia
   (`md-spec §5.6`) y constituye la **unica ruta soportada** de emision
   para esa familia.
2. La autoria editorial se ejerce sobre el corpus fuente, no sobre el
   artefacto generado.
3. La regeneracion **PUEDE** hacerse bajo demanda sin alterar la identidad
   URN del artefacto (§8.3).

### 9.2 Registro de productores

| Familia | Productor canonico | URN del productor | Output |
| --- | --- | --- | --- |
| `atomic` | `artifacts/skills/kora/atomize/SKILL.md` | `urn:kora:artefacto:atomize` | `artifacts/knowledge/_SCRIPTORIUM/REVIEW/{ns}/atomic/atomic-{slug}.md` |

### 9.3 Reglas operativas

1. Un artefacto de familia con productor canonico **DEBERIA** ser
   regenerable desde el corpus fuente declarado en
   `extensions.kora.{family}.source_corpus` (o campo equivalente),
   siempre que la regeneracion siga cumpliendo `md-spec §6.11` y `FS=100%`.
2. Si el artefacto se edita a mano despues de generarse, **DEBE**
   declararse `extensions.kora.{family}.hand_edited: true` para que el
   productor no lo sobreescriba en la siguiente corrida.
3. El productor canonico **DEBE** emitir artefactos con `status: borrador`
   en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/`; la promocion pasa por
   `kora promote` y verifica los checks de `md-spec §6.10` y `§6.11` mas
   la coherencia de namespace (§3.2).
4. El productor canonico **DEBE** declararse en su salida mediante
   `extensions.kora.{family}.producer: urn:...`.
5. Una familia con productor canonico **PUEDE** aceptar reparacion manual
   posterior sobre artefactos ya emitidos. Esa reparacion es excepcional
   y verificable; **NO** constituye una ruta alternativa de generacion.
6. En la familia `atomic`, `atomize` es la unica ruta soportada para
   emitir nuevos artefactos. Ningun scaffold mecanico, wrapper auxiliar o
   segmentacion automatica fuera de `atomize` **PUEDE** tratarse como
   opcion equivalente.
7. En la familia `atomic`, una corrida de `atomize` que colapsa, omite o
   mezcla hechos del cuerpo sustantivo del documento **NO** satisface la
   spec aunque el archivo lintee.

### 9.4 Aislamiento de responsabilidades

- `md-spec` define los invariantes de la familia.
- `knowledge-spec` declara el productor canonico y sus reglas operativas.
- El productor concreto (skill, script, pipeline) vive en
  `artifacts/skills/` o `artifacts/agents/` como artefacto productivo y es
  consumidor de las dos specs anteriores.

Esta separacion garantiza que un cambio en el productor **NO** requiera
bump de las specs, y que un cambio en las specs **SI** requiera revisar
al productor.

## 10. Grafo derivado de conocimiento

El grafo derivado **DEBE** construirse a partir de frontmatter, no de
scraping heuristico del body.

Usos canonicos:

- resolver URNs,
- detectar huerfanos,
- calcular dependencias transitivas,
- alimentar `allowed_kb` y routing de agentes,
- materializar trazabilidad vertical requirement -> implementacion/verificacion,
- auditar supersesion y drift editorial.

Materializacion: `kora index` + `kora kb-graph --json --orphans`.

## 11. Invariantes

Los invariantes del sistema de conocimiento son:

1. **URN como identidad estable**: todo nodo publicado tiene URN
   conceptual; el URN preserva la identidad del nodo durante todo el
   lifecycle (§4) y todo el pipeline (§8.3).
2. **Relations resolubles**: `relations` es tipado y todos sus targets
   resuelven en el catalogo (§6.2 r1).
3. **Precedencia normativa centralizada**: la precedencia entre specs no
   se autodeclara en cada artefacto; vive solo en `gobernanza`.
4. **Coherencia supersesion-status**: un nodo no puede estar
   simultaneamente supersedido y `status: publicado`; quien es
   supersedido pasa a `deprecado` o `retirado`.
5. **Crudo no consumible**: material en `_SCRIPTORIUM/INBOX/` no se
   consume como ley publicada; la zona productiva solo contiene
   artefactos con `_manifest` completo y `status` valido.
6. **Coherencia namespace-directorio**: §3.2 r1.
7. **TracesRequirement bien fundada**: toda `TracesRequirement` del grafo
   proviene de `relations.traces_requirements` y apunta a requirements
   direccionables.
8. **Productor canonico monopoliza emision**: si una familia tiene
   productor declarado, no se admite generacion alternativa (§9.3 r6).

## 12. Validacion

Checks canonicos sobre artefactos de conocimiento:

| Check | Condicion | Severidad | Enforcement | Spec ref |
| --- | --- | --- | --- | --- |
| `urn-integrity` | Todo URN en relations resuelve | alta | lint | §6.2 r1 |
| `knowledge-zone` | Archivos en `artifacts/knowledge/{ns}/` tienen `_manifest` valido | alta | schema | §4.2, §8.1 |
| `kb-graph-cycles` | Grafo `depends` sin ciclos | alta | graph | §6.2, §10 |
| `traces-requirements-semantics` | Targets de `traces_requirements` son requirement-like | alta | graph | §6.2 r4, §11 inv7 |
| `supersedes-consistency` | Targets de `supersedes` estan `deprecado` o `retirado` | media | graph | §6.2 r2, §11 inv4 |
| `lint-md` | Artefactos cumplen formato `md-spec` (envelope, familia, gramatica) | baja | lint | `md-spec §9` |

`md-spec §9` cubre los checks de **formato** (envelope, gramatica, family
invariants). Esta spec cubre los checks de **tejido relacional** y
**pipeline**.

Las severidades y enforcement coinciden con los del registry vivo
(`python3 toolchain/kora check --list`).

## 13. Procedimientos operativos

Comandos CLI vigentes para curacion de conocimiento (`python3 toolchain/kora`):

| Comando | Funtor | Uso |
| --- | --- | --- |
| `intake` | (status) | Reporta archivos fuente vs artefactos KORA/MD. |
| `atomize` | `Normalize` para familia `atomic` | Productor canonico (§9). Lee `artifacts/skills/kora/atomize`. |
| `lint-md` | check `Publish` | Lint estructural sobre artefactos publicados o REVIEW. |
| `promote` | `Publish` | Mueve un borrador de `_SCRIPTORIUM/REVIEW/{ns}/` a `artifacts/knowledge/{ns}/`. |
| `promote-cohort` | `Publish` batch | Promueve toda una cohorte (`{ns}`) con abort-on-first-failure. |
| `deprecate` | transicion lifecycle | Marca publicado como deprecado; detecta dependientes reversos. |
| `index` | `Graph` (catalogo) | Reconstruye `docs/generated/catalog.yml`. |
| `kb-graph` | `Graph` (grafo) | Materializa grafo derivado; flag `--orphans` para detectar huerfanos. |
| `resolve` | (lookup) | Resuelve un URN a path local. |
| `check --strict` | gate compuesto | Ejecuta los 33 checks del registry (incluye los de §12). |

`kora promote-cohort` se invoca como subcomando interno via
`kora promote` con un directorio como argumento (ver `cmd_promote_cohort`
en `toolchain/kora_lib/promote.py`).

## 14. Migracion

### 14.1 Que cambio v1.3 -> v2.0

Esta version absorbe del `md-spec §3.1` las reglas que **no** son formato
sino pipeline o identidad. Especificamente:

- **§3** (nueva): URN conceptual `urn:{ns}:kb:{id}` y coherencia
  namespace-directorio (antes en `md-spec §3.1 r7`).
- **§4** (nueva): lifecycle `borrador -> publicado -> deprecado`, status
  por directorio y transiciones via `kora promote` (antes en
  `md-spec §3.1 r8-10`).
- **§8** (renombrada y formalizada): pipeline antes `§6 Pipeline como
  cadena de funtores` ahora explicita la composicion functorial y la
  preservacion de identidad URN.
- **§9** (renumerada): productores canonicos (antes `§12`). El registro
  se actualiza: `atomize` queda en topologia productiva
  `artifacts/skills/kora/atomize/SKILL.md` con URN
  `urn:kora:artefacto:atomize`.
- **§11** (consolidada): invariantes ampliados a 8, integrando los del
  pipeline.
- **§12** (alineada): tabla de validacion declara `Spec ref` explicito.
- **§13** (nueva): catalogo de comandos CLI vigentes.

### 14.2 Que migrar

- Artefactos KORA/MD existentes **no requieren** cambios de frontmatter o
  URN; el regimen URN era ya conceptual desde v1.0.
- Referencias a `knowledge-spec §3` (tipos de artefacto) y `knowledge-spec §6`
  (pipeline) se reapuntan a esta version: `§5` y `§8` respectivamente.
- Referencias a `knowledge-spec §12` (productores) se reapuntan a `§9`.
- `atomize` queda promovido a `artifacts/skills/kora/atomize/`; cualquier
  referencia a `artifacts/skills/_TALLER/INBOX/atomize/` queda historica.

### 14.3 Que se depreca

- Nada del contrato semantico de v1.3 se depreca. Las reglas absorbidas
  desde `md-spec §3.1 r7-10` quedan en aquella spec con redireccion
  explicita a `knowledge-spec §3` y `§4` (ver `md-spec v9.0.0`).
- `md-spec §10` (en v8.1) describia pipeline; ese contenido queda como
  redireccion a `knowledge-spec §8`.
