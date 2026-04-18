---
_manifest:
  urn: "urn:kora:kb:procesos-spec"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Cierra H2 del backlog post-olas: explicita los 9 procesos del toolchain KORA como funtores con dominio, codominio, preservacion y perdida declarada."
version: "1.0.0"
status: publicado
tags: [spec, procesos, toolchain, functor, invariantes, lifecycle]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:cat-foundations"
    - "urn:kora:kb:cat-governance-lattice"
    - "urn:kora:kb:cat-audit-invariants"
    - "urn:kora:kb:cat-behavioral-preservation"
    - "urn:fxsl:kb:icas-procesos"
---

# KORA/Procesos-Spec v1.0.0

## 1. Definicion

`procesos-spec` gobierna la lectura **functorial** de los procesos del
toolchain KORA. Su objetivo es eliminar la ambiguedad operacional: cada
subcomando deja de ser “algo que hace cosas” y pasa a ser una transformacion
con dominio, codominio, invariantes y perdida declarada.

Principio rector:

> Todo proceso KORA **DEBE** declarar que estructura preserva, que estructura
> pierde y bajo que condiciones deja de estar definido.

Rationale: en ICAS-BoK los procesos de ingenieria son funtores entre categorias
de artefactos. Lo importante no es el shell command en si, sino el contrato de
preservacion que encarna.

## 2. Categorias operativas

Esta spec usa las siguientes categorias de trabajo:

| Simbolo | Categoria | Objetos |
|---------|-----------|---------|
| `Legacy` | Shapes retirados | artefactos previos a `autoria-spec` o topologias obsoletas |
| `IR` | Artefactos canonicos | documentos y workspaces conformes al canon vigente |
| `Diag` | Diagnosticos | conjuntos/listas de findings ordenados por severidad |
| `Prod` | Artefactos publicados/activos | objetos promovidos al corpus o fleet productivo |
| `Stage` | Artefactos en staging | `_FRAGUA/`, `_TALLER/`, `_SCRIPTORIUM/` |
| `Runtime_R` | Artefactos proyectados | wrappers, bundles o blueprints para un runtime `R` |
| `Graph` | Vistas graficas | grafo de referencias y relaciones |
| `Catalog` | Vista indexada | URNs, paths, versiones, relaciones y metadatos resolubles |

## 3. Los 9 procesos como funtores

### 3.1 Tabla canonica

| Proceso | Funtor | Dominio | Codominio |
|---------|--------|---------|-----------|
| `migrate` | `Migrate` | `Legacy` | `IR` |
| `validate` | `Validate` | `IR` | `Diag` |
| `check` | `Check` | `RepoState` | `Diag` |
| `promote` | `Promote` | `Stage` | `Prod` |
| `deprecate` | `Deprecate` | `Prod` | `Prod_deprecated` |
| `transmute` | `T_R` | `IR` | `Runtime_R` |
| `ingest` | `Lift_R` | `Runtime_R` | `Stage` |
| `kb-graph` | `KG` | `Corpus` | `Graph` |
| `index` | `Idx` | `RepoState` | `Catalog` |

### 3.2 `migrate`

`Migrate: Legacy -> IR`

Preserva:

1. identidad semantica del artefacto,
2. contenido normativo y relaciones que siguen siendo representables,
3. procedencia del origen.

Pierde:

1. scaffolds legacy retirados,
2. sinonimos de campos absorbidos por el canon,
3. convenciones de path que ya no pertenecen a la topologia vigente.

Invariantes:

1. `migrate` **DEBE** ser idempotente una vez alcanzado el shape canonico.
2. `migrate` **NO DEBE** inventar capacidad no sustentada por el origen.
3. Si la derivacion de un vector no es concluyente, **DEBE** dejar huella
   revisable y no simular certeza.

### 3.3 `validate`

`Validate: IR -> Diag`

Preserva:

1. el artefacto como objeto auditado,
2. la tipificacion de sus campos,
3. el regimen de severidad de los hallazgos.

Pierde:

1. ninguna estructura del artefacto; es una lectura, no una mutacion.

Invariantes:

1. `validate` **DEBE** ser puro respecto del objeto inspeccionado.
2. `validate` **DEBERIA** ser monotono: agregar informacion estructural no
   deberia ocultar un fallo ya detectado sin explicacion.

### 3.4 `check`

`Check: RepoState -> Diag`

`check` es el pliegue del registro de checks sobre el repo.

Preserva:

1. trazabilidad entre hallazgo y regla,
2. orden topologico de dependencias entre checks,
3. severidad y fase de cada finding.

Pierde:

1. detalle irrelevante del repo que no participa en ningun check.

Invariantes:

1. `check` **DEBE** componer checks via el monoide libre de diagnosticos.
2. `check` **NO DEBE** reinterpretar una regla como si fuera otra.
3. `check --strict` **DEBE** fallar si cualquier check falla.

### 3.5 `promote`

`Promote: Stage -> Prod`

Preserva:

1. URN, version y contenido aprobado,
2. procedencia del staging,
3. relaciones declaradas.

Pierde:

1. la condicion de provisionalidad del objeto en staging.

Invariantes:

1. `promote` **DEBE** ser monotono en lifecycle.
2. `promote` **NO DEBE** alterar el contenido aprobado fuera de las
   normalizaciones canonicas necesarias para publicar.
3. `promote` **DEBE** rechazar artefactos que no pasen validacion/checks
   requeridos.

### 3.6 `deprecate`

`Deprecate: Prod -> Prod_deprecated`

Preserva:

1. identidad historica del objeto,
2. resolucion del URN,
3. accesibilidad para auditoria y trazabilidad.

Pierde:

1. elegibilidad como camino vigente por defecto.

Invariantes:

1. `deprecate` **DEBE** ser absorbente: un objeto deprecado no vuelve a activo
   por mutacion interna.
2. `deprecate` **DEBERIA** declarar `supersedes` cuando exista sucesor canonico.

### 3.7 `transmute`

`T_R: IR -> Runtime_R`

Preserva:

1. composicion e identidad del IR,
2. monotonia por eje,
3. safety closure y `qa_budget` dentro del dominio soportado.

Pierde:

1. capacidades fuera del dominio del runtime,
2. distinciones que la runtime-extension autorice colapsar,
3. detalle IR que no tenga superficie en el target.

Invariantes:

1. toda perdida **DEBE** declararse en `_transmutation.yml`,
2. toda violacion estructural **DEBE** abortar la transmutacion,
3. el target nunca se vuelve fuente de verdad.

### 3.8 `ingest`

`Lift_R: Runtime_R -> Stage`

Preserva:

1. comportamiento observable representable,
2. procedencia del runtime de origen,
3. evidencia de que el objeto no nacio en el canon KORA.

Pierde:

1. detalles privados del target sin equivalencia en staging,
2. estado operativo efimero no apto para versionado.

Invariantes:

1. `ingest` **NO DEBE** inventar claims de equivalencia que el runtime no
   respalde.
2. `ingest` **DEBE** dejar el objeto en `Stage`, no promocionarlo
   implicitamente.

### 3.9 `kb-graph`

`KG: Corpus -> Graph`

Preserva:

1. nodos conceptuales (`urn:{ns}:kb:{id}`),
2. relaciones declaradas en frontmatter,
3. clasificacion de orfandad y ciclos.

Pierde:

1. prosa del body que no este materializada como relacion,
2. relaciones implicitas no declaradas.

Invariantes:

1. `kb-graph` **DEBE** ser fiel a manifests y relations declaradas.
2. `kb-graph` **NO DEBE** inferir aristas semanticas invisibles como si fueran
   relaciones normativas.

### 3.10 `index`

`Idx: RepoState -> Catalog`

Preserva:

1. resolucion de URN,
2. path canonico,
3. version, status y metadata base.

Pierde:

1. narrativa del body,
2. interpretacion de alto orden que no viva en metadata resoluble.

Invariantes:

1. `index` **DEBE** ser idempotente.
2. `index` **DEBE** fallar o advertir ante fuentes publicadas cuyo source ya no
   exista.

## 4. Composiciones canonicas

Las siguientes composiciones son de primer orden en KORA:

1. `migrate ; validate ; check ; promote`
2. `ingest ; validate ; promote`
3. `index ; kb-graph`
4. `validate ; transmute`

Reglas:

1. `promote` **NO DEBE** ejecutarse antes de `validate/check` cuando estos
   apliquen.
2. `transmute` **DEBERIA** operar sobre `IR` ya validado.
3. `kb-graph` e `index` **DEBERIAN** leerse como vistas materializadas del repo;
   son compatibles pero no equivalentes.

## 5. Invariantes coinductivas

Estos procesos forman una dinamica repetida sobre el repo. Las siguientes
propiedades **DEBEN** mantenerse en el limite:

1. aplicar `index` o `kb-graph` repetidamente sobre un repo estable converge al
   mismo objeto materializado,
2. repetir `check` sobre un repo sin cambios no introduce hallazgos nuevos,
3. toda cadena `promote ; deprecate` preserva la historia de identidad,
4. toda cadena `transmute ; ingest` solo puede reclamar equivalencia modulo
   perdida declarada.

## 6. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| `migrate-idempotente` | Reaplicar `migrate` sobre canon no cambia paths | manual |
| `validate-puro` | `validate` no muta el artefacto inspeccionado | manual |
| `check-topologico` | El DAG de dependencias de checks no contiene ciclos | lint |
| `promote-monotono` | `promote` no revierte lifecycle ni baja status | manual |
| `transmute-proof-carrying` | Todo target emitido deja `_transmutation.yml` | lint |
| `ingest-provenance` | Toda ingesta declara runtime fuente y referencia original | manual |
| `kb-graph-fiel` | El grafo solo usa relations declaradas | lint |
| `index-idempotente` | `index` sobre repo estable no cambia el catalogo | lint |

## 7. Migracion

`procesos-spec v1.0.0` es declarativa y no introduce nuevos subcomandos.

Reglas de migracion:

1. los comandos existentes **NO REQUIEREN** renombrarse;
2. su interpretacion formal pasa a estar gobernada por esta spec;
3. nuevas automatizaciones **DEBERIAN** declarar a cual de estos funtores
   refinan, componen o especializan.
