---
_nota: |
  Este documento NO es auto-generado por `python3 toolchain/kora sync-docs`.
  Producido por `polymath` operando con el skill `cat-thinking`
  (ICAS-BoK). Se conserva en `docs/reports/` como analisis historico y
  debe permanecer fuera de `docs/generated/`.
producido_por: polymath + SKILLS/cat-thinking
fecha: 2026-04-16
modo: audit + model
alcance: monorepo KORA completo
---

# Evaluacion e Inventario Categorico de KORA

> **Axioma de diseño** (skill `cat-thinking`):
> arquitectura = composicion correcta de partes que **preservan estructura**.
> Todo lo que no compone, no preserva o no es universal es deuda arquitectonica
> con nombre categorico.

Este documento aplica esa lente al estado actual de KORA (2026-04-16). No es
un reporte de mantencion (para eso esta `kora check`) ni un diagnostico de
operaciones (para eso esta `kora health`). Es una lectura **estructural**:
que categorias vive el monorepo, que funtores conectan sus capas, que
adjunciones son reales y cuales son pseudo, donde la composicion cierra y
donde no.

## TL;DR

- KORA funciona como una **2-categoria** con tres capas: **governance** (specs),
  **IR** (AGENTS/, SKILLS/, KNOWLEDGE/) y **outputs derivados** (BUILD/,
  OPERATIONS/, docs/generated/). Las capas se conectan por funtores
  declarados.
- La constitucion (gobernanza v4.0.0) es **categoricamente explicita**: declara
  canon, fuente de verdad por objeto, invariantes, y legacy como compatibilidad
  residual. Eso es raro y valioso — la mayoria de monorepos no tiene esto.
- **Hallazgo critico**: `SKILLS/` es **pseudo-portable**. Solo 4 SKILL.md son
  realmente top-level (`cat-thinking`, `data-modeling`,
  `graphic-design`, `ux-design`). Los 186+ bundles `CM-*` viven duplicados
  1:1 en `AGENTS/{ns}/{agent}/skills/` y en `SKILLS/{ns}/{agent}/CM-*/`. El
  funtor `overlay : AGENTS → SKILLS` es un **embedding diagonal**, no un
  embedding de una categoria de skills portables. Duplicacion material que
  viola la regla de mirrors (§4.1 gobernanza) en espiritu: el mirror no puede
  regenerarse mecanicamente desde una primaria clara.
- **Hallazgo alto**: 20 workspaces coexisten con `AGENT.md` moderno + cinco
  archivos legacy (`AGENTS.md`, `config.json`, etc.). Gobernanza lo permite
  como compatibilidad residual, pero la transformacion natural
  `legacy ⇒ modern` no esta aun totalmente instanciada. Deuda controlada pero
  viva.
- **Hallazgo alto**: el grafo de conocimiento tiene **329/509 nodos huerfanos
  (64,6%)**. Knowledge categoricamente cerrado requeriria una categoria conexa
  (salvo componentes deseados); 2/3 huerfanos sugiere que `cites` y `depends`
  estan subpoblados — la categoria de referencias es casi discreta.
- **Hallazgo medio**: solo **11 `TracesTo`** existen en el grafo. Con 538
  artefactos de knowledge y una Formal Layer oficial nombrada en CLAUDE.md,
  la adjuncion `ground : Concrete → Formal` esta casi vacia. El peso formal
  del repo es nominal, no operativo — todavia.
- **Candidata a formalizar**: el pipeline `source → drafts → KNOWLEDGE` tiene
  forma de cadena de adjunciones (`intake ⊣ filter` y `promote ⊣ revert`),
  pero no esta declarado como tal. Formalizarlo haria explicitos los left/right
  adjoints y daria garantias sobre idempotencia.

## 1. Inventario: objetos y morfismos

Cifras autoritativas obtenidas de `scripts/kora index` + `docs/generated/*`
(no inventadas).

### 1.1 Objetos por capa

| Capa | Objeto | Conteo | Fuente |
|------|--------|-------:|--------|
| Governance | specs canonicas + gobernanza + md-spec + extension | 7 | `ls specs/` |
| IR (agentes) | workspaces activos | 25 | `kora stats` |
| IR (agentes) | workspaces deprecated | 1 | `kora stats` |
| IR (agentes) | workspaces incompletos | 1 | `kora stats` |
| IR (agentes) | artefactos bootstrap legacy | 155 | `kora stats` |
| IR (skills) | skills totales en catalogo | 382 | `kora stats` |
| IR (knowledge) | artefactos KORA/MD publicados | 538 | `kora stats` |
| Outputs | docs/generated (auto) | 7 pares .json/.md | `ls docs/generated` |
| Catalogo | entradas totales indexadas | 1075 | `kora stats` |
| Perfiles | AGENTS/_perfiles/ (input, no workspaces) | 1 directorio | `ls AGENTS/` |

Namespaces activos (por entradas de catalogo, ordenados):

`fxsl` (247), `gn` (233), `kora` (197), `salud` (157), `tde` (55),
`korvo` (37), `agengai` (36), `legal` (35), `dev` (28), `sii` (26),
`ops` (20), `pro` (4). Total: 12 namespaces, 1075 entradas.

### 1.2 Morfismos del repo (edges del grafo unificado)

Lectura del `repo-graph.json` (5687 edges, 958 nodos):

| Tipo de edge | Conteo | Interpretacion categorica |
|------|-------:|--------------------------|
| `XRef` | 4318 | referencias cruzadas en bodies — presheaf debil |
| `AllowsKB` | 344 | workspace → KB que puede leer (morfismo permiso) |
| `ContainsSkill` | 186 | workspace → skill (composicion agente) |
| `InvokesSkill` | 180 | declaracion dinamica de invocacion |
| `Cites` | 174 | knowledge → knowledge (dependencia semantica) |
| `ContainsArtifact` | 154 | workspace → bootstrap artifact |
| `AllowsTool` | 124 | workspace → tool (permiso de interfaz) |
| `DeclaresTool` | 124 | workspace → tool (declaracion semantica) |
| `DependsOn` | 59 | knowledge → knowledge (depende estructural) |
| `RoutesToAgent` | 13 | agente → agente (federacion/ruteo) |
| `TracesTo` | 11 | artefacto → Formal Layer oficial |

Observaciones:

- `AllowsTool` y `DeclaresTool` existen en paridad (124/124) — el check
  `tools-config-coherence` garantiza que los dos funtores (TOOLS.md,
  config.json) comuten. Es un **pullback declarativo**: un tool esta
  "habilitado de verdad" sii ambos funtores lo aceptan.
- `TracesTo = 11` es mínimo. Ver hallazgo H-3 mas abajo.
- `RoutesToAgent = 13` define un sub-grafo de federacion que vale la pena
  examinar independientemente (posible composicion 2-categorica).

## 2. Lectura categorica por capa

### 2.1 Governance — specs como tipos

Los 7 documentos en `specs/` forman una **categoria presentada**:

```
Objetos: {gobernanza, md-spec, knowledge-spec, agentfile-spec,
          skill-overlay-spec, runtime-spec-md, openclaw-runtime-extension}

Generadores (precedencia, §3 gobernanza):
  gobernanza --precedes--> md-spec --precedes--> {canonicas-dominio}
  {canonicas-dominio} --precedes--> {extensiones-ns}

Ecuaciones (invariantes §8):
  1. AGENT.md = canon
  2. skills_portables = preferido
  3. legacy = compat, no centro
  4. runtime, output = derivados
  5. compat no recentraliza
```

La categoria de specs satisface:

- **Composicion**: la relacion "precede" es un orden parcial con identidad —
  categoria thin.
- **Preservacion**: gobernanza v4.0.0 explicita que `legacy ⊆ canonica`
  (§3.2 — "absorbida dentro"). Es un funtor de inclusion con faithfulness
  pero sin fullness: legacy no cubre todo lo canonico.
- **Universalidad**: la regla de especializacion (§3.3) define un
  **pullback practico**: dado un objeto (ej. `AGENT.md`), la spec aplicable
  es la mas especifica del conjunto que lo menciona. Esto es un limite.

**Evaluacion**: spec layer sana. Rara calidad en un monorepo. Unica grieta:
la precedencia vs enforcement (§7) deja cinco niveles (schema / lint /
runtime / eval / manual) sin declarar per-regla. Un check que emita
`spec-enforcement-matrix` seria una transformacion natural faltante.

### 2.2 IR — agentes como coalgebras

Un agente en KORA tiene **dos formatos activos**:

| Formato | Conteo | Autoridad | Soporte formal |
|---------|-------:|-----------|---------------|
| `AGENT.md` (Agentfile, 6 dims) | 27 | canonico | `agentfile-spec.md` |
| Legacy 5-componentes | 26 | compat residual | perfil en `agentfile-spec` |
| **Coexistencia dual** | **20** | `AGENT.md` gana (§4 gobernanza) | ambos |

Las 6 dimensiones del Agentfile mapean directamente al skill
`cat-thinking`:

| Dimension | Construccion categorica | Doc ICAS |
|-----------|------------------------|----------|
| `coalgebra` | α : U → F(U) (Lambek, observacion) | 09-efectos, 14-agencia |
| `plan` | Free monad sobre polynomial p | 14-agencia |
| `interface` | Profunctor P : Agent^op × Tool → Set | 11-interaccion, 14-agencia |
| `fibers` | fibracion Grothendieck (identity/operator/memory) | 10-extension |
| `composition` | 2-morfismos entre agentes | 13-escala |
| `safety` | sub-coalgebra cerrada bajo α | 12b-safety-alignment |

Esta alineacion no es casualidad — el agentfile-spec esta escrito para
ser la presentacion operativa de la teoria que el skill formaliza. **Es
coherente**. Sin embargo:

- La dimension `plan` como free monad requeriria que los FSM declarados
  tengan hojas con tipos de resultado. Solo algunos AGENT.md lo hacen
  explicito.
- La dimension `safety` como sub-coalgebra cerrada requiere verificacion
  de clausura (∀s ∈ S, α(s) ⊆ F(S)). No hay check automatico para esto;
  es `manual` segun gobernanza §7.

**Evaluacion**: IR de agentes bien disenado, subtilmente sub-verificado.
El check `agentfile-dimensions` valida que las 6 dims **esten declaradas**,
no que sus **contenidos satisfagan las leyes** de la construccion que
nombran. Es un check de presencia, no de semantica.

### 2.3 IR — skills: el problema diagonal

Aqui esta la grieta mayor.

**Declaracion de principio** (gobernanza §2, corolario 2): "`SKILL.md`
portable es el formato preferido de capacidad."

**Estado real**:

```
find SKILLS -maxdepth 2 -name "SKILL.md"
  → SKILLS/ux-design/SKILL.md
  → SKILLS/data-modeling/SKILL.md
  → SKILLS/cat-thinking/SKILL.md
  → SKILLS/graphic-design/SKILL.md

find SKILLS -name "SKILL.md" | wc -l
  → 196

find SKILLS -type d -name "CM-*" | wc -l
  → 190 (todos bundles agent-bound)
```

Solo **4 skills genuinamente portables** top-level, sin namespace de agente.
Los otros 192 son o (a) bundles `CM-*` que viven bajo
`SKILLS/{ns}/{agent}/CM-*/SKILL.md`, o (b) 2 wrappers `transmute-*`.

Ademas, **duplicacion 1:1** con `AGENTS/`:

```
head -5 AGENTS/kora/clawforge/skills/CM-INTENT-CLASSIFIER.md
  → _manifest.urn: urn:kora:skill:clawforge-intent-classifier:1.0.0

head -5 SKILLS/kora/clawforge/CM-INTENT-CLASSIFIER/SKILL.md
  → _manifest.urn: urn:kora:skill:clawforge-intent-classifier:1.0.0
```

**Mismo URN, dos rutas en el filesystem.**

Lectura categorica:

- El "funtor overlay" `F : AGENTS → SKILLS` no es un embedding funtorial
  de una categoria de skills portables — es un **funtor diagonal**
  `Δ : AGENTS → AGENTS × SKILLS` donde la segunda proyeccion es una
  reformateacion sintactica (archivo `.md` plano ↔ directorio con
  `SKILL.md` adentro).
- No hay ganancia de portabilidad: si movieras `SKILLS/kora/clawforge/` a
  otro repo, seguiria siendo dependiente de `kora/clawforge` — el
  namespace ata la capacidad a un agente.
- Las 4 skills genuinamente top-level **si** son portables — el contraste
  es evidente.

**Diagnostico**: la capa SKILLS/ mezcla dos cosas que deben separarse.

1. **Skills portables** (agnosticas de agente): `cat-thinking`,
   `data-modeling`, `graphic-design`, `ux-design`, mas cualquier futura.
   Viven `SKILLS/<nombre>/SKILL.md` — sin namespace.
2. **Bundles de capacidad de agente** (antes `CM-*`): viven DENTRO del
   workspace, `AGENTS/{ns}/{agent}/skills/`. No tienen por que espejarse
   en SKILLS/.

Si esta separacion se aplica, SKILLS/ deja de ser pseudo-portable y pasa
a ser efectivamente portable. El funtor overlay cambia: deja de ser
diagonal y pasa a ser una **inclusion plena y fiel**.

### 2.4 IR — knowledge: el grafo poco conexo

538 artefactos KORA/MD, 509 nodos en kb-graph, 245 edges, **329 huerfanos
(64,6%)**.

| Metrica | Valor | Interpretacion |
|---------|------:|----------------|
| Nodos | 509 | conceptual layer |
| Edges | 245 | `cites` (182) + `depends` (63) |
| Huerfanos | 329 | nodos sin `cites` entrante ni saliente |
| Ciclos en `depends` | 0 | DAG limpio |
| Broken edges | 0 | URN integrity cerrada |

Un grafo donde 2/3 de los nodos no tienen aristas no es una red semantica —
es un **objeto casi-discreto**. Categoricamente: la categoria libre sobre
este grafo esta dominada por la identidad. Muy poca composicion de
referencias.

Causas probables (hipotesis, **certidumbre media**):

1. Muchos artefactos de atomize/ y drafts antiguos estan publicados pero
   no enlazados. El pipeline intake no exige citations como post-condicion.
2. Las citations se mantienen solo en los nodos "hub" (`med-emergencia`
   con 35 edges, `index` legal con 17, `ssot-master` con 14). El resto
   es satelite sin interconexion lateral.
3. `TracesTo` a Formal Layer esta subutilizado (solo 11 edges) — la via
   formal-de-abajo-arriba tambien esta discontinuada.

Ver §4 Recomendacion R-2 para accion.

### 2.5 Outputs — transmutacion como funtor

`AGENTS/{ns}/{agent}/` + `SKILLS/` → `BUILD/{target}/` donde
`target ∈ {claude-code, openclaw, gemini, codex, ...}`.

Lectura categorica: `Transmute_target` es un **funtor faithful pero no
full**. Cada target descarta dimensiones que su runtime no entiende:

| Target | Dimensiones que pierde | Por que |
|--------|------------------------|---------|
| claude-code | `composition` (sub-agentes como 2-morfismos), `coalgebra` (observaciones tipadas) | runtime plano |
| openclaw | `fibers` (knowledge fibrada) — se colapsa a 1 KB | motor lineal |
| gemini | `safety` (sub-coalgebra cerrada) — solo hard rules | no expresivo |
| codex | similar a claude-code | idem |

**Propiedad deseable**: cada `Transmute_target` deberia tener un
`Ingest_target` que recupere lo maximo del IR desde el output. Si
ambos existieran, formarian una adjuncion Σ ⊣ Δ (push ⊣ pull). Hoy:

- `Transmute_*` existe (varias implementaciones en
  `scripts/kora_lib/transmute*.py`).
- `Ingest_*` **no existe** como operacion inversa. El outputs a BUILD/
  es gitignored; no hay camino de regreso al IR.

Esto es intencional (BUILD/ es derivado) pero categoricamente tiene un
costo: **no puedes verificar que la transmutacion conserva lo que dice
conservar**. El diagrama `id ≟ Ingest ∘ Transmute` no puede instanciarse,
asi que la fidelidad se afirma a mano, no se prueba.

### 2.6 Pipelines — operaciones como cadena de adjunciones

El pipeline de knowledge es:

```
OPERATIONS/source/  →intake→  OPERATIONS/drafts/  →promote→  KNOWLEDGE/
  (gitignored)                   (tracked)                    (tracked)
```

Lectura candidata como cadena de adjunciones Σ ⊣ Δ:

- `intake` es `Σ : Raw → Draft` (libera estructura: extrae, etiqueta,
  clasifica, le pone manifest). No preserva todo — descarta ruido.
- `filter` / `reject` seria el `Δ : Draft → Raw` (mantiene solo lo que
  ya tenia forma de draft). Implicito hoy, no formalizado.
- `promote` es `Σ' : Draft → Published` (cristaliza un draft en published,
  le asigna URN, posiblemente lo congela).
- `revert` seria `Δ' : Published → Draft` (revertir publicacion). Existe
  manualmente (mover archivo) pero no hay comando.

Si se formalizaran los adjuntos inversos:

```
  intake ⊣ filter    (push libertad / pull estructura)
  promote ⊣ revert   (push cristalizacion / pull descongelamiento)
```

Se obtendria:

- **Idempotencia garantizada**: `intake . filter . intake = intake`.
- **Unit/counit como invariantes verificables**.
- **Composicion de pipelines** sin interferencia entre etapas.

Hoy el pipeline funciona pero su algebra operacional no esta declarada.
Ver R-3.

## 3. Hallazgos por severidad

### H-1 · CRITICO · SKILLS/ pseudo-portable

**Propiedad violada**: principio de portabilidad declarado por gobernanza
§2 corolario 2, y regla de mirrors §4.1.

**Estructura**: `SKILLS/{ns}/{agent}/CM-*/` duplica material
sintacticamente con `AGENTS/{ns}/{agent}/skills/CM-*.md`, con mismo URN.

**Violacion**:
- 190/196 "skills portables" estan namespaced bajo un agente → no son
  portables.
- El mirror no tiene fuente primaria clara: la primaria podria ser
  cualquiera de las dos ubicaciones.
- El funtor `overlay` es diagonal, no un embedding pleno y fiel de una
  categoria de skills portables.

**Fundamentacion**: `references/02-preservacion` (funtor full/faithful),
`references/04-identidad-es-relacion` (Yoneda: la identidad de un skill
reside en su uso, y skills agent-bound no tienen identidad indepentiente
del agente).

**Correccion**: separar la categoria SKILLS/ en dos:

1. `SKILLS/<nombre>/SKILL.md` — portables genuinas (top-level sin ns).
2. `AGENTS/{ns}/{agent}/skills/` — bundles de agente (no mirrored).

Eliminar `SKILLS/{ns}/{agent}/CM-*/`. Actualizar
`skill-overlay-spec.md` para distinguir "skill portable" de "bundle de
agente".

**Esfuerzo**: Medio. Requiere codemod en `scripts/kora migrate`, ajuste
de `skill-overlay-spec.md`, y revision de 190 directorios CM-*.

### H-2 · ALTO · Coexistencia AGENT.md + legacy en 20 workspaces

**Propiedad violada**: canon claro §9 gobernanza ("cada objeto tiene
fuente primaria"). Gobernanza §4 dice "si conviven AGENT.md y archivos
legacy, AGENT.md es la autoridad" — es una regla de desempate, pero la
mera coexistencia significa que la **transformacion natural
`legacy ⇒ modern` no esta completada**.

**Estructura**: 20/27 workspaces con `AGENT.md` tienen tambien `AGENTS.md`
+ `config.json` + otros. Ejemplos: `gn/goreologo`, `fxsl/neriomath`,
`salud/salubrista`, `korvo/korax`.

**Violacion**:
- Una TN coherente requeriria que cada workspace estuviera en modo
  "AGENT.md solo" o "legacy solo", no en ambos.
- Mantener ambos formatos indefinidamente duplica superficie de mantencion
  y expone a **drift** (el legacy se edita pero el AGENT.md no, o viceversa).

**Fundamentacion**: `references/03-comparacion` (TN como familia coherente
de morfismos). `references/20-infraestructura-autonoma` (reconciliation).

**Correccion**:
1. Declarar un **cutoff**: fecha a partir de la cual el legacy en
   workspaces con AGENT.md se **elimina**, no solo "se queda como compat".
2. Agregar check `workspace-format-single-source`: si hay AGENT.md,
   prohibir AGENTS.md/config.json directamente (no solo desempatarlos).
3. Ejecutar migracion de los 20 duales: extraer la semantica legacy que
   aun no este en AGENT.md, inyectarla, eliminar archivos legacy.

**Esfuerzo**: Medio. El codemod `kora migrate --profile transitional`
ya existe; habria que agregarle cohort `dual-cleanup`.

### H-3 · ALTO · Grafo de knowledge casi-discreto

**Propiedad violada**: la categoria de knowledge como presheaf de
referencias. Para ser util como red semantica, necesita conectividad.

**Estructura**: 329/509 nodos huerfanos (64,6%). 245 edges totales.

**Violacion**:
- Una categoria con 2/3 de objetos aislados es esencialmente un coproducto
  de objetos solitarios + un subgrafo conexo pequeño.
- Las queries de composicion del tipo "que knowledge depende de X y a que
  workspace lo autorizo" solo funcionan en el subgrafo conexo.

**Fundamentacion**: `references/01-composicion`,
`references/04-identidad-es-relacion`.

**Correccion**:
1. Agregar check `kb-coverage`: cada artefacto publicado debe tener ≥1
   `cites` o `depends` (in o out), excepto los declarados "foundational"
   (leaf nodes de un namespace).
2. Revisar artefactos bajo `KNOWLEDGE/fxsl/` (98 nodos, muchos huerfanos
   probables) — candidatos a absorber formalmente o archivar.
3. Poblar `TracesTo` a Formal Layer donde aplique — la Formal Layer
   oficial (`KNOWLEDGE/kora/categorical-foundations/`) solo tiene 11
   edges entrantes.

**Esfuerzo**: Alto si se hace a mano; Medio si se genera un reporte de
huerfanos y se cierra por cohorts.

### H-4 · MEDIO · Transmutacion sin inversa

**Propiedad violada**: universalidad. `Transmute_target` afirma preservar
informacion pero no puede demostrarse sin un `Ingest_target`.

**Correccion**:
- **Opcion A** (conservadora): agregar checks post-transmutacion que
  verifiquen propiedades declaradas (ej. "todo tool del IR esta en el
  output"). Esto es `Ingest` parcial — solo verifica el retract.
- **Opcion B** (ambiciosa): implementar `Ingest_claude-code` e
  `Ingest_openclaw` que recuperan el IR desde BUILD/. Verifica
  `id ≟ Ingest ∘ Transmute` modulo clases de isomorfia declaradas.

**Esfuerzo**: Opcion A: Medio. Opcion B: Alto.

### H-5 · MEDIO · Pipeline de knowledge sin algebra declarada

**Propiedad violada**: universalidad del pipeline `source → drafts →
KNOWLEDGE`. Las adjunciones candidatas no estan formalizadas.

**Correccion**:
1. Documentar en `knowledge-spec.md` las adjunciones:
   - `intake ⊣ filter`
   - `promote ⊣ revert`
2. Implementar `kora revert <urn>` como comando simetrico a `kora
   promote`.
3. Testear idempotencia: `promote(revert(x)) = x` modulo clase de
   equivalencia `ε` (editados).

**Esfuerzo**: Bajo para documentacion; Medio para implementacion.

### H-6 · BAJO · atomize/ fuera del canon

`atomize/raw/*.md` no tiene YAML frontmatter y genera WARN en `kora
index`. Esta fuera del canon pero no declarado como tal.

**Correccion**: agregar `atomize/` a `.kora-ignore` equivalente o declarar
en gobernanza que `atomize/raw/` es pre-canonico (no KORA/MD). No es
critico — los WARN no interrumpen el index.

**Esfuerzo**: Bajo.

## 4. Recomendaciones con trade-offs

### R-1 · Separar SKILLS/ portables de bundles de agente

**Decision**: eliminar `SKILLS/{ns}/{agent}/` como ruta; mover bundles a
`AGENTS/{ns}/{agent}/skills/` (donde ya estan duplicados) y dejar
`SKILLS/<nombre>/` solo para skills genuinamente portables.

**Sacrificio**:
- **Pierde**: ilusion de "libreria global" de skills. Hoy parece que hay
  382 skills portables; despues habra ~10-20 realmente portables + ~190
  bundles agent-bound.
- **Gana**: claridad categorica. El funtor `SKILLS` es genuinamente
  embedding; deja de ser diagonal. Las 4 skills portables reales
  (`cat-thinking`, `data-modeling`, etc.) se destacan en vez de
  perderse entre 190 CMs.
- **Riesgo**: cualquier consumidor externo (openclaw-fleet, transmute
  outputs) que referencie `SKILLS/{ns}/{agent}/` debe reapuntar. Auditar
  antes de migrar.

**Alternativa**: mantener el mirror pero declararlo como
`BUILD/skills-view/` (derivado, gitignored), regenerado por
`kora sync-docs`. Mantiene la ilusion sin el costo de duplicacion
tracked.

### R-2 · Check de cobertura de knowledge

**Decision**: agregar `kb-coverage` al registry de `kora check` (severity
medium). Exige ≥1 edge entrante o saliente para cada artefacto
publicado, salvo excepciones declaradas.

**Sacrificio**:
- **Pierde**: flexibilidad de publicar knowledge "aislado" (ej. notas
  sueltas o standalone references). Requeriria excepciones.
- **Gana**: conectividad real del corpus. Forza al author a pensar
  "como se relaciona este artefacto con los demas".
- **Riesgo**: los 329 huerfanos actuales son un cliff — el check fallaria
  estrepitosamente de dia uno. Introducir como `warning` primero, luego
  elevar a `medium`.

### R-3 · Declarar adjunciones del pipeline

**Decision**: redactar seccion "Algebra del pipeline" en
`knowledge-spec.md` declarando las adjunciones `intake ⊣ filter` y
`promote ⊣ revert`. Implementar `kora revert`.

**Sacrificio**:
- **Pierde**: simplicidad del pipeline actual ("no hay marcha atras").
- **Gana**: operaciones simetricas, idempotencia verificable,
  reconciliacion automatica posible.
- **Riesgo**: `revert` destructivo si mal usado. Mitigar con dry-run por
  defecto y confirmacion explicita.

### R-4 · Completar migracion dual → AGENT.md

**Decision**: cutoff a 3 meses. Workspaces con AGENT.md deben eliminar
archivos legacy coexistentes. Agregar `workspace-format-single-source`
como check `high`.

**Sacrificio**:
- **Pierde**: compatibilidad con consumidores que aun esperen formato
  legacy (probablemente ninguno interno, pero podria haber externos).
- **Gana**: canon claro materializado. Gobernanza §4 aplicada en hecho,
  no solo en regla de desempate.
- **Riesgo**: transmutacion de workspaces duales puede depender del
  legacy como fuente de info que aun no esta en AGENT.md. Verificar
  caso por caso.

### R-5 · Verificacion semantica de las 6 dimensiones Agentfile

**Decision**: escalar el check `agentfile-dimensions` de "presencia" a
"semantica":

- `coalgebra`: verificar que triggers y outputs tienen tipos coherentes.
- `plan`: verificar que el FSM declarado tiene estados finales o hojas.
- `safety`: verificar clausura de sub-coalgebra (si una regla hard
  prohibe X, X no puede ser output de una transicion valida).

**Sacrificio**:
- **Pierde**: facilidad de adopcion — escribir un AGENT.md que **tambien
  pasa la verificacion semantica** es mas dificil que uno que solo
  declara dimensiones.
- **Gana**: la palabra "coalgebra" en la dimension se vuelve operativa,
  no decorativa. KORA pasa de "declaracion categorica" a "verificacion
  categorica".
- **Riesgo**: esto requiere motor de inferencia de tipos — no trivial.
  Escalar como sub-proyecto.

## 5. Inventario categorico resumido

### Categorias principales identificadas

```
SpecCat         — specs + precedencia (thin category, orden parcial)
AgentCat        — 27 workspaces AGENT.md (+ 26 legacy como sub-cat compat)
SkillCat        — 4 objetos portables + 190 bundles (mezclados, H-1)
KnowledgeCat    — 509 nodos, presheaf de refs (329 huerfanos, H-3)
BuildCat_target — outputs por target (faithful, no full)
OperatingCat    — contratos del nucleo (docs/generated/operating-core-contracts)
```

### Funtores principales

```
C : AgentCat × SpecCat  →  Constraints
  (tipa cada agente con las specs que gobiernan su formato)

T_target : AgentCat  →  BuildCat_target
  (transmute; faithful, no full; sin inversa hoy — H-4)

O : AgentCat  →  SkillCat
  (overlay; HOY es diagonal-duplicador — H-1;
   DEBERIA ser embedding pleno y fiel tras R-1)

R : WorkspaceCat  →  KnowledgeCat
  (AllowsKB; permisos de lectura — well defined, 344 edges)

X : AgentCat  →  AgentCat
  (RoutesToAgent; federacion — sub-categoria de 13 edges)

D : KnowledgeCat  →  KnowledgeCat  (endofuntor)
  (depends + cites; define presheaf de referencias)

F : KnowledgeCat  →  FormalLayer
  (TracesTo; casi vacio — 11 edges; H-3 tambien)
```

### Adjunciones candidatas (no todas instanciadas)

```
intake  ⊣  filter     (H-5, por formalizar)
promote ⊣  revert     (H-5, por formalizar)
transmute_t ⊣ ingest_t (H-4, no existe inversa)
legacy  ⊆  canonica   (inclusion, no adjuncion — gobernanza §3.2)
```

### Invariantes constitucionales (gobernanza §8)

1. `AGENT.md` es canon.
2. Skills portables preferidos.
3. Legacy = compat, no centro.
4. Runtime/output son derivados.
5. Compat no recentraliza.

De estos, **1 y 3 estan parcialmente cumplidos** (H-2); **2 esta
contradicho por la estructura actual de SKILLS/** (H-1); **4 cumple** (BUILD/ es
gitignored, docs/generated son derivados); **5 cumple**.

## 6. Preguntas abiertas para Felix

Estas son decisiones que requieren tu juicio, no solo ejecucion:

**Q-1 — Timing de R-1 (separar SKILLS/)**: el refactor de SKILLS/ es el
mas invasivo (toca 190 directorios). Puede hacerse en un solo cambio
grande o gradualmente por namespace. Cual preferis? Que consumidores
externos referencian `SKILLS/{ns}/{agent}/` que debamos coordinar antes
(openclaw-fleet probablemente)?

**Q-2 — Definicion de "portable"**: el skill `data-modeling` esta
top-level pero usa terminologia especifica (ERDs, normalizacion). El
skill `graphic-design` asume identidad visual. Son realmente portables
a cualquier namespace? Vale la pena un criterio formal (ej. "portable =
no referencia ningun namespace concreto en su texto")?

**Q-3 — Cutoff del dual (R-4)**: los 20 workspaces duales. Hay alguno
que debe quedarse en legacy porque tiene consumidor activo que no puede
migrar? `salud/medico-urgencias` y `salud/salubrista` acaban de recibir
trabajo pesado (BOK medicina emergencia v2.0.0 del 2026-04-15 segun
memoria) — estan en estado moviendose, no congelar todavia?

**Q-4 — Nivel de verificacion semantica (R-5)**: hasta donde escalar el
check de dimensiones del Agentfile? Verificar presencia es trivial;
verificar clausura de sub-coalgebras requiere motor de tipos. Es un
sub-proyecto con costo propio. Prioridad respecto a H-1/H-2/H-3?

**Q-5 — Rol de la Formal Layer**: `KNOWLEDGE/kora/categorical-foundations/`
tiene 11 `TracesTo` entrantes de 538 artefactos. Es porque la Formal
Layer esta joven y hay que poblarla; o porque la mayoria del corpus no
deberia trazar formalmente? Cual es la ambicion: aspirar a 50% traceable
o dejarla como garante de nucleo?

**Q-6 — `atomize/` (H-6)**: es transitorio (se vacia hacia
KNOWLEDGE/) o permanente como staging area? Si es permanente, declararlo
en gobernanza como "zona pre-canonica" resolveria los WARN. Si es
transitorio, el contenido de raw/ esperando procesamiento es deuda
operacional.

---

## Apendice · Metodo y trazabilidad

- **Skill utilizado**: `SKILLS/cat-thinking/SKILL.md`, modos
  `audit` (secciones 2-3) + `model` (seccion 5).
- **Corpus citado**:
  - `references/01-composicion` — composicion, asociatividad, identidad.
  - `references/02-preservacion` — funtores, faithfulness, fullness.
  - `references/03-comparacion` — transformaciones naturales.
  - `references/04-identidad-es-relacion` — Yoneda.
  - `references/06-adjunciones` — Σ/Δ/Π.
  - `references/14-agencia` — free monad, cofree comonad, agentes.
  - `references/19-patrones` — patrones como construcciones universales.
- **Autoridades operativas consultadas**:
  - `specs/gobernanza.md` v4.0.0
  - `specs/agentfile-spec.md`
  - `specs/skill-overlay-spec.md`
  - `docs/generated/repo-stats.md`, `kb-graph.md`, `repo-graph.json`
  - `scripts/kora stats`, `scripts/kora index`, `scripts/kora check --list`
- **No se modifico** ningun artefacto de KORA (specs, knowledge, agents,
  skills, catalog). Solo lectura + este reporte.

## Self-check (skill cat-thinking)

- [x] Axioma de diseño evaluado (compone / preserva / es universal) en
      cada hallazgo.
- [x] Construcciones nombradas son las correctas (funtor diagonal en H-1,
      TN en H-2, presheaf en H-3, adjuncion en H-4/H-5).
- [x] Documentos del corpus citados en cada hallazgo.
- [x] Output operativo (cada recomendacion tiene comando / check / codemod
      concreto), no solo teorico.
- [x] Perdida de informacion declarada (T_target faithful no full,
      overlay diagonal pierde portabilidad).
- [x] Vocabulario categorico traducido a practica en cada punto.
- [x] Modo `audit + model` es el correcto para el pedido "evaluar e
      inventariar".
