---
_manifest:
  urn: urn:kora:kb:knowledge-spec
  provenance:
    created_by: FS
    created_at: '2026-04-14'
    source: KORA categorical-foundations 00, 02, 04, 05; md-spec v6.3.0; spec-md v5.2.0;
      pipeline-ingesta v1.0.0; gobernanza v3.5.0; polymath + arquitecto-categorico
      analysis
version: 1.0.0
status: published
tags:
- spec
- knowledge
- categoria
- grafo
- pipeline
- namespace
- artefacto
lang: es
extensions: {}
relations:
  cites:
  - urn:kora:kb:md-spec
---


# KORA/Knowledge-Spec v1.0.0

## 1. Definicion

Esta especificacion define el sistema de conocimiento KORA como una categoria formal. Gobierna la estructura, relaciones, pipeline y gobernanza de todos los artefactos en `KNOWLEDGE/`. Complementa md-spec (formato de artefactos descriptivos) y spec-md (formato de artefactos prescriptivos) con la estructura relacional que los conecta.

### 1.1 Fundamento categorico

El conocimiento KORA forma una categoria KnowCat donde:

- **Objetos**: artefactos de conocimiento con `_manifest` valido
- **Morfismos**: relaciones tipadas entre artefactos (cites, depends, supersedes, refines)
- **Composicion**: transitividad de relaciones — si A depende de B y B depende de C, entonces A depende transitivamente de C
- **Identidad**: cada artefacto tiene el morfismo identidad `id_A : A -> A`

Las propiedades de la categoria garantizan:
- **Asociatividad**: las cadenas de relaciones componen sin ambiguedad
- **Completud local**: cada namespace es una subcategoria plena de KnowCat
- **Trazabilidad**: todo artefacto tiene una cadena finita de provenance hasta su fuente

Traces to: formal/00 §1 (Category) ; formal/02 §1 (The Two Categories)

### 1.2 Alcance

Esta especificacion gobierna:

1. Los tipos de artefacto admitidos en `KNOWLEDGE/`.
2. Las relaciones inter-artefacto (morfismos de KnowCat).
3. La gobernanza de namespaces.
4. El pipeline de ingesta como cadena de funtores.
5. El grafo de conocimiento como vista materializada de KnowCat.
6. Los atributos de calidad como categoria enriched.
7. La clasificacion de contenido crudo vs artefacto publicado.

Esta especificacion **NO** gobierna el formato interno de artefactos (gobernado por md-spec y spec-md), ni agentes (gobernado por agentfile-spec), ni skills (gobernado por skill-overlay-spec).

## 2. Definiciones

| Termino | Definicion |
|---------|-----------|
| KnowCat | Categoria de artefactos de conocimiento KORA — objetos son artefactos, morfismos son relaciones tipadas |
| Artefacto | Archivo Markdown con `_manifest` YAML valido y `status: published` en `KNOWLEDGE/` |
| Contenido crudo | Archivo sin `_manifest` que reside en zona de pipeline (`source/`, `inbox/`) o en zona de exclusion |
| Namespace | Subdirectorio de primer nivel bajo `KNOWLEDGE/` que agrupa artefactos por dominio |
| Subcategoria de namespace | Subcategoria plena de KnowCat formada por artefactos de un namespace |
| Morfismo | Relacion tipada dirigida entre artefactos: `cites`, `depends`, `supersedes`, `refines` |
| Grafo de conocimiento | Vista materializada de KnowCat como grafo dirigido (generada por `kora kb-graph`) |
| Pipeline | Cadena de funtores `extract . transform . promote` que lleva contenido crudo a artefacto publicado |
| Funtor F | Koraficacion: `DocHumano -> KORA/MD` (md-spec §6) |
| Funtor G | Cristalizacion: `Decisiones -> KORA/Spec-MD` (spec-md §1.2) |
| Zona | Directorio con semantica de pipeline: `inbox/`, `source/`, `drafts/`, `KNOWLEDGE/` |

## 3. Tipos de artefacto

### 3.1 Artefactos KORA (objetos de KnowCat)

Todo objeto de KnowCat **DEBE** cumplir:

1. Residir bajo `KNOWLEDGE/{namespace}/`.
2. Ser un archivo `.md` con YAML frontmatter que contiene `_manifest.urn`.
3. Tener `status: published` o `status: deprecated`.
4. Seguir el formato md-spec (descriptivo) o spec-md (prescriptivo).

Un archivo que reside en `KNOWLEDGE/` pero no cumple estas condiciones **NO** es un objeto de KnowCat. Su presencia viola el invariante de zona (§8.1).

### 3.2 Contenido no-artefacto

Los siguientes tipos de contenido **NO DEBEN** residir directamente en `KNOWLEDGE/`:

| Tipo | Ejemplo | Destino correcto |
|------|---------|-----------------|
| Contenido crudo sin `_manifest` | PDFs, markdown sin frontmatter | `OPERATIONS/source/` |
| Datos tabulares | CSV, TSV, XLSX | `OPERATIONS/source/{ns}/data/` |
| Ontologias nativas | RDF/OWL, TTL | `OPERATIONS/source/{ns}/onto/` |
| Mirrors de documentacion externa | Copias verbatim de docs ajenos | `OPERATIONS/source/{ns}/mirror/` |
| Extracciones atomizadas sin curar | Proposiciones /atomize raw | `OPERATIONS/source/{ns}/` |

**Correcto:** `KNOWLEDGE/gn/kb/intro-gores-nuble.md` con `_manifest` y `status: published`.
**Incorrecto:** `KNOWLEDGE/gn/data/convenios.csv` (dato tabular, no artefacto KORA).
**Incorrecto:** `KNOWLEDGE/hi/ia-med.md` sin `_manifest` (contenido crudo, no artefacto).

### 3.3 Datos auxiliares

Si un artefacto KORA necesita referenciar datos tabulares, ontologias o recursos no-Markdown:

1. El recurso **DEBERIA** residir en `OPERATIONS/source/{ns}/` con la trazabilidad correspondiente.
2. El artefacto KORA **DEBERIA** referenciar el recurso via `_manifest.provenance.source` o en el cuerpo como enlace relativo.
3. El artefacto KORA **DEBE** ser autocontenido para RAG: el recurso externo es suplementario, no necesario para la comprension del artefacto.

## 4. Morfismos de KnowCat

### 4.1 Tipos de relacion

KnowCat tiene 4 tipos de morfismos. Cada uno tiene semantica precisa y reglas de composicion.

| Tipo | Direccion | Semantica | Composicion |
|------|-----------|-----------|-------------|
| `cites` | A cites B | A referencia a B como fuente o evidencia | Transitiva: A cites B cites C implica A cites-transitivamente C |
| `depends` | A depends B | A requiere B como prerequisito para comprension | Transitiva y aciclica (DAG): no **DEBEN** existir ciclos de dependencia |
| `supersedes` | A supersedes B | A reemplaza a B como version actualizada del mismo conocimiento | Lineal: B **DEBE** tener `status: deprecated` si A lo supersede |
| `refines` | A refines B | A es mas detallado que B sobre el mismo tema | No necesariamente transitiva |

Traces to: formal/00 §2 (Functor) ; formal/05 §2 (Transformation Functors)

### 4.2 Declaracion en frontmatter

Las relaciones se declaran en el campo `relations` del frontmatter YAML:

```yaml
---
_manifest:
  urn: "urn:{ns}:kb:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencia}"
relations:
  cites:
    - "urn:{ns}:kb:{id-citado}"
  depends:
    - "urn:{ns}:kb:{id-prerequisito}"
  supersedes:
    - "urn:{ns}:kb:{id-reemplazado}"
  refines:
    - "urn:{ns}:kb:{id-generalizado}"
version: "{semver}"
status: published
tags: [{tags}]
lang: "{iso}"
extensions: {}
---
```

Reglas:

1. El campo `relations` es **OPCIONAL**. Un artefacto sin relaciones explicitas es un objeto aislado en KnowCat (sin morfismos salientes).
2. Los valores de cada tipo **DEBEN** ser URNs resolubles a artefactos existentes en `KNOWLEDGE/`.
3. Las relaciones **DEBEN** ser verificables: `kora health --strict` reporta relaciones rotas como broken URNs.
4. El campo `relations` reside al mismo nivel que `_manifest`, no dentro de el.
5. Cada lista de URNs **DEBERIA** tener como maximo 10 entradas por tipo. Si un artefacto cita mas de 10 fuentes, considerar si el artefacto es demasiado amplio.

### 4.3 Invariantes de morfismos

1. **Aciclicidad de `depends`**: El grafo de dependencias **DEBE** ser un DAG. Enforcement: `kora kb-graph --check-cycles`.
2. **Consistencia de `supersedes`**: Si A supersede B, entonces B **DEBE** tener `status: deprecated`. Enforcement: lint.
3. **Resolvibilidad**: Todo URN en `relations` **DEBE** ser resolvible via `kora resolve`. Enforcement: health.
4. **Coherencia de namespace**: Las relaciones `cites` y `depends` **PUEDEN** cruzar namespaces. Las relaciones `supersedes` y `refines` **DEBERIAN** permanecer dentro del mismo namespace o namespace-familia.

## 5. Namespaces

### 5.1 Definicion

Un namespace es un subdirectorio de primer nivel bajo `KNOWLEDGE/` que agrupa artefactos por dominio. Cada namespace forma una subcategoria plena de KnowCat.

Traces to: formal/03 §1 (Definition of Eco)

### 5.2 Namespaces registrados

| Namespace | Dominio | Familia |
|-----------|---------|---------|
| `kora` | Meta-sistema KORA (specs, formal layer, sys) | meta |
| `fxsl` | Felix S.L. — metodologias, teoria de categorias, OPM | personal |
| `gn` | Gobierno Regional de Nuble | institucional |
| `salud` | Salud publica, hospitalizacion domiciliaria, epidemiologia | dominio |
| `tde` | Transformacion digital del Estado | dominio |
| `sii` | Servicio de Impuestos Internos | dominio |
| `legal` | Marco juridico (sociedades, trabajo medico) | dominio |
| `agengai` | IA agentica (OpenClaw, Claude Code, plataformas) | tecnologia |
| `ops` | Operaciones y deployment del ecosistema | operacional |
| `korvo` | Agente personal korvo — filosofia y manual de vida | personal |
| `dev` | Desarrollo de software (IFML, patrones) | tecnologia |
| `pro` | Productividad y gestion personal | personal |
| `hi` | Health informatics — informatica en salud | dominio |
| `omega` | Legacy: especificaciones OpenClaw pre-KORA | legacy |

### 5.3 Reglas de namespace

1. Los nombres de namespace **DEBEN** ser lowercase. `OMEGA` **DEBE** migrar a `omega`.
2. Un namespace nuevo **DEBE** registrarse en esta tabla antes de crear artefactos en el.
3. Todo artefacto en `KNOWLEDGE/{ns}/` **DEBE** tener `urn:{ns}:kb:{id}` como URN — el namespace del URN **DEBE** coincidir con el directorio fisico. Enforcement: lint (ya en md-spec §3.1.7).
4. Los namespaces `meta` y `operacional` **NO DEBEN** contener conocimiento de dominio.
5. Un namespace sin artefactos validos (0 objetos en KnowCat) **DEBERIA** eliminarse o consolidarse.

### 5.4 Familias de namespace

Las familias agrupan namespaces con afinidad tematica:

| Familia | Namespaces | Descripcion |
|---------|-----------|-------------|
| meta | kora | Gobernanza y estructura del ecosistema |
| personal | fxsl, korvo, pro | Conocimiento personal de Felix |
| institucional | gn | Conocimiento organizacional GORE Nuble |
| dominio | salud, tde, sii, legal, hi | Conocimiento por area tematica |
| tecnologia | agengai, dev | Conocimiento tecnologico |
| operacional | ops | Operaciones del ecosistema |
| legacy | omega | Contenido pre-KORA en transicion |

Las familias **NO** tienen enforcement directo — son indicativas para consulta y auditoria. `kora stats` **DEBERIA** reportar conteos por familia.

## 6. Pipeline como cadena de funtores

### 6.1 Modelo categorico del pipeline

El pipeline de ingesta es una cadena composicional de funtores entre categorias zonales:

```
RawCat  --extract-->  CuratedCat  --transform-->  WIPCat  --promote-->  KnowCat
(inbox)               (source)                    (drafts)              (KNOWLEDGE)
```

Cada zona es una categoria cuyos objetos son archivos y cuyos morfismos son transformaciones de contenido. Los funtores preservan trazabilidad:

- **extract**: identifica el namespace destino, cura el contenido (elimina ruido, formatea markdown), deposita en `source/`. No agrega `_manifest`.
- **transform**: aplica funtor F (koraficacion) o G (cristalizacion), agrega `_manifest` con `status: draft`, deposita en `drafts/`.
- **promote**: verifica lint y schema, cambia `status: draft -> published`, mueve a `KNOWLEDGE/`, ejecuta `kora index`.

La composicion `promote . transform . extract = ingest` es el pipeline completo.

Traces to: formal/00 §2 (Functor) ; formal/02 §3 (Progressive Disclosure as Categorical Operation)

### 6.2 Propiedades de los funtores

| Funtor | Preserva | Pierde | Fidelidad |
|--------|----------|--------|-----------|
| extract | Contenido factual, estructura logica | Formato original (PDF, HTML), ruido editorial | Faithful (inyectivo en hechos) |
| transform (F) | Verdad factual, estructura, metadata | Retorica, hedging, redundancia | Faithful + full en hechos |
| transform (G) | Reglas, obligaciones, enforcement | Vaguedad, opcionalidad implicita | Faithful + full en reglas |
| promote | Todo (identidad en contenido) | Nada (solo cambia status + zona) | Isomorfismo |

### 6.3 Ciclo de vida del artefacto en pipeline

```
[inbox]          [source]         [drafts]           [KNOWLEDGE]
   |                |                |                    |
   | deposit        | extract        | transform(F|G)     | promote
   v                v                v                    v
 crudo           curado          WIP c/manifest       publicado
 (sin metadata)  (sin metadata)  (status: draft)     (status: published)
```

Las transiciones **DEBEN** ser estrictamente progresivas. Un artefacto **NO DEBE** retroceder de zona (e.g., KNOWLEDGE -> drafts) excepto para `supersedes` donde el nuevo artefacto inicia su propio pipeline.

### 6.4 Comandos CLI del pipeline

| Comando | Accion | Funtor |
|---------|--------|--------|
| `kora intake` | Reporta estado de source/ vs drafts/ vs KNOWLEDGE/ | Diagnostico |
| `kora promote {path}` | Verifica, cambia status, mueve a KNOWLEDGE/, indexa | promote |
| `kora kb-graph` | Materializa el grafo de relaciones de KnowCat | Vista |
| `kora lint-md --fix` | Auto-corrige issues de lint en artefactos | Mantenimiento |

El funtor `extract` y `transform` son manuales o ejecutados por agentes (e.g., curator). No se automatizan como comandos CLI porque requieren juicio semantico.

## 7. Grafo de conocimiento

### 7.1 Definicion

El grafo de conocimiento es una vista materializada de KnowCat como grafo dirigido, generada por `kora kb-graph`.

Los nodos son artefactos (con URN como identificador). Las aristas son relaciones tipadas extraidas de los campos `relations` del frontmatter.

### 7.2 Formato de salida

`kora kb-graph --json` produce un archivo en `docs/generated/kb-graph.json`:

```json
{
  "nodes": [
    {
      "urn": "urn:kora:kb:md-spec",
      "namespace": "kora",
      "status": "published",
      "version": "6.3.0",
      "tags": ["spec", "markdown"]
    }
  ],
  "edges": [
    {
      "from": "urn:kora:kb:knowledge-spec",
      "to": "urn:kora:kb:md-spec",
      "type": "depends"
    }
  ],
  "stats": {
    "total_nodes": 367,
    "total_edges": 0,
    "by_namespace": {},
    "by_relation_type": {},
    "orphan_nodes": 0,
    "cycles_in_depends": 0
  }
}
```

### 7.3 Invariantes del grafo

1. Todo nodo **DEBE** corresponder a un artefacto con `_manifest` valido en `KNOWLEDGE/`.
2. Toda arista **DEBE** conectar nodos existentes (no broken URNs).
3. El subgrafo de `depends` **DEBE** ser aciclico.
4. Nodos sin aristas entrantes ni salientes son "orphan nodes" — validos pero indicativos de baja integracion.

### 7.4 Metricas de calidad

El grafo materializa atributos de calidad como metricas:

| Metrica | Definicion | Target |
|---------|-----------|--------|
| Cobertura de manifest | % de archivos en KNOWLEDGE/ con `_manifest` valido | 100% |
| Densidad relacional | aristas / nodos | > 0.5 (cada artefacto tiene al menos una relacion promedio) |
| Orphan ratio | nodos sin aristas / total nodos | < 30% |
| Cycle count | ciclos en `depends` | 0 |
| Cross-namespace ratio | aristas inter-namespace / total aristas | Informativo |
| Lint pass rate | artefactos sin lint issues / total artefactos | > 95% |
| Supersedence coherence | artefactos con supersedes donde target tiene status: deprecated | 100% |

## 8. Invariantes

### 8.1 Segregacion de zonas

`KNOWLEDGE/` **DEBE** contener exclusivamente artefactos KORA validos (§3.1). Contenido no-artefacto **DEBE** residir en las zonas de pipeline correspondientes (§3.2).

Enforcement: `kora health --strict` **DEBERIA** reportar archivos sin `_manifest` en `KNOWLEDGE/` como violacion de zona.

### 8.2 Unicidad de URN

Todo URN en KnowCat **DEBE** ser unico. Dos artefactos distintos **NO DEBEN** compartir URN.

Enforcement: `kora index` detecta colisiones.

### 8.3 Coherencia de namespace fisico-logico

El namespace en el URN (`urn:{ns}:kb:{id}`) **DEBE** coincidir con el primer subdirectorio bajo `KNOWLEDGE/` donde reside el artefacto.

Enforcement: lint (ya en md-spec).

### 8.4 Completud del frontmatter

Todo artefacto en `KNOWLEDGE/` **DEBE** tener frontmatter YAML con al menos: `_manifest.urn`, `_manifest.provenance`, `version`, `status`, `tags`, `lang`.

El campo `relations` es opcional pero **DEBERIA** existir cuando el artefacto tiene dependencias o citas conocidas.

### 8.5 Naming convention

1. Los archivos **DEBEN** usar kebab-case: `nombre-descriptivo.md`.
2. Los prefijos legacy (`kb_gn_XXX_`) **DEBERIAN** migrar a kebab-case gradualmente.
3. Los namespaces **DEBEN** ser lowercase.
4. Los subdirectorios dentro de un namespace **DEBERIAN** ser tematicos, no numericos.

## 9. Validacion

| Check | Criterio | Enforcement | Comando |
|-------|----------|-------------|---------|
| Manifest presente | Todo .md en KNOWLEDGE/ tiene `_manifest` | health | `kora health --strict` |
| URN unico | No hay colisiones de URN | index | `kora index` |
| NS fisico = NS logico | URN ns coincide con directorio | lint | `kora lint-md` |
| Relaciones resolubles | URNs en `relations` existen | health | `kora health --strict` |
| DAG de depends | Sin ciclos en relaciones `depends` | kb-graph | `kora kb-graph --check-cycles` |
| Supersedence coherente | Target de supersedes tiene status: deprecated | lint | `kora lint-md` |
| Lint clean | 0 issues de lint | lint | `kora lint-md` |
| Zona segregada | Sin contenido no-artefacto en KNOWLEDGE/ | health | `kora health --strict` |

## 10. Migracion desde estado actual

### 10.1 Estado diagnosticado

Al momento de creacion de esta spec:

- 819 archivos .md en KNOWLEDGE/, solo 367 en catalogo
- 452 archivos sin `_manifest` (55%) — contenido crudo mezclado con artefactos
- 890 issues de lint (758 html_raw, 109 oversized_chunk, 13 empty_wrapper, 10 meta_heading)
- Namespace `OMEGA` en mayusculas (debe ser `omega`)
- `agengai/openclaw/documentacion-oficial/` contiene 427 archivos de mirror crudo
- `gn/data/` contiene CSVs, `gn/onto_gorenuble/` contiene RDF/OWL
- `hi/`, `fxsl/cat/corpus-categorico*/` y otros contienen contenido crudo sin koraficar

### 10.2 Plan de migracion

| Fase | Accion | Resultado |
|------|--------|-----------|
| 1 | Mover contenido no-artefacto de KNOWLEDGE/ a OPERATIONS/source/ | Solo artefactos validos en KNOWLEDGE/ |
| 2 | Renombrar OMEGA → omega | Namespace normalizado |
| 3 | Remediar lint issues (html_raw, oversized chunks) | < 50 lint issues residuales |
| 4 | Agregar campo `relations` a artefactos con dependencias conocidas | Morfismos de KnowCat materializados |
| 5 | Implementar `kora kb-graph` | Grafo de conocimiento materializable |
| 6 | Implementar `kora promote` | Pipeline de promocion funcional |
| 7 | Migrar naming legacy (kb_gn_XXX) a kebab-case | Gradual, no-blocking |

### 10.3 Retrocompatibilidad

- El campo `relations` es opcional — artefactos existentes sin el siguen siendo validos.
- El comando `kora kb-graph` produce output aunque no haya relaciones declaradas (grafo de nodos sin aristas).
- La migracion de naming es gradual y no rompe URNs (el URN es el identificador estable).
- Los artefactos movidos de KNOWLEDGE/ a source/ mantienen su contenido intacto para futuro koraficacion.

## 11. Relacion con otras specs

| Spec | Relacion |
|------|----------|
| gobernanza.md | Precedencia: gobernanza > esta spec > md-spec/spec-md en materia de Knowledge |
| md-spec.md | Define formato de artefactos descriptivos — esta spec define su organizacion y relaciones |
| spec-md.md | Define formato de artefactos prescriptivos — esta spec los incluye como objetos de KnowCat |
| pipeline-ingesta (KB) | Formalizado y subsumido por §6 de esta spec |
| agentfile-spec.md | Los agentes consumen Knowledge via `fibers.knowledge.allowed_kb` — esta spec define la oferta |
| skill-overlay-spec.md | Skills referencian Knowledge via `metadata.kora.knowledge` — esta spec define que pueden referenciar |
