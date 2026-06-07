# Alineacion de claims NxN — meta-evaluacion de 8 auditorias categoriales de las specs KORA

Fecha: 2026-06-08
Insumo: 8 reportes de auditoria categorial de las specs KORA, cada uno con sus
`atomic_claims` ya extraidos. Este documento es la **comparacion a nivel de
contenido**: alinea los claims a traves de los 8 functores de auditoria
`F_i: Specs -> Cat`, identifica donde coinciden (consenso / transformacion
natural), donde divergen (contradiccion / ruptura de naturalidad) y donde un
solo auditor vio algo correcto que nadie mas vio (claim unico valioso).

Los 8 reportes, por slug:

| slug | scope | veredicto | score | metodo declarado |
|------|-------|-----------|-------|------------------|
| `borrador-claude` | specs | solido (34) | Claude (Sonnet) + cat-thinking |
| `report-b1e84abd` | specs | solido (39) | opencode qwen3.7-plus + cat-thinking |
| `report-a3f7c2e1` | specs | solido (35) | opencode mimo-v2.5-pro + cat-thinking |
| `deep` | specs | **ejemplar (44)** | Claude + cat-thinking + falsos-amigos |
| `gemini` | **sistema** | **deficiente (14)** | Gemini + cat-thinking |
| `v6` | specs | solido (33) | opencode glm-5.1 + cat-thinking |
| `v7-0607` | specs | solido (32) | opencode kimi-k2.6 + cat-thinking |
| `v7-0608` | specs | solido (32) | (cat-thinking, modelo no declarado) |

Todo lo afirmado abajo como "verificado contra fuente" fue comprobado por mi
contra las specs vivas, el toolchain (`kora check --list`, `kora graph`,
`kora kb-graph`) y el corpus ICAS-BoK durante esta meta-evaluacion. Cito el
hecho de fondo, no recito el codigo.

---

## 0. Sesgo de metodo (leer ANTES que el consenso)

**7 de 8 reportes corren la misma skill `cat-thinking` anclada al mismo corpus
ICAS-BoK.** Solo varia el modelo subyacente (Claude, qwen, mimo, glm, kimi,
gemini). Esto tiene una consecuencia dura para leer el consenso:

> Cuando N reportes que comparten skill+corpus afirman lo mismo, eso es
> **correlacion de metodo**, no N confirmaciones independientes. La skill
> cat-thinking ES un instrumento con un prior fuerte: "busca la lectura
> categorial mas debil que cumple, distingue formal/heuristico/metaforico,
> ancla a URN, no cometas falsos-amigos". Reportes que ejecutan bien esa skill
> *convergeran por construccion* en los mismos hallazgos canonicos, aunque el
> hallazgo sea trivial o aunque todos hereden el mismo punto ciego.

Implicaciones concretas:

1. **El hallazgo "leyes functoriales declaradas pero no verificadas
   mecanicamente"** lo dicen 6 de 8. Es verdadero (lo verifique: la matriz de
   `_transmutation.yml` marca `xi_naturality`, `safety_closure`,
   `kleisli_composition` con `status: declared`). Pero su unanimidad es en gran
   parte un artefacto del corpus: `icas-preservacion` literalmente entrena al
   lector a decir "functor sin verificacion mecanica = funcion con intencion, no
   functor". El consenso aqui es **consenso-por-correlacion-de-metodo que
   ademas resulta verdadero**, no consenso-por-verdad-independiente. Su valor
   probatorio real viene de la verificacion contra `_transmutation.yml`, no del
   numero de auditores.

2. **El punto ciego compartido es igual de real.** 5 reportes que tocan la
   adjuncion `Lift_R ⊣ T_R` la leen como "adjuncion (lax) declarada-no-
   verificada". Solo `deep` —que usa la *misma* skill— rompe el patron y la
   diagnostica correctamente como **conexion de Galois sobre el reticulo, no
   adjuncion 1-categorial**. El hecho de que la mayoria coincida en la lectura
   mas debil-pero-imprecisa NO la vuelve correcta; un solo functor vio la
   estructura fina.

3. **Sobre-formalizacion compartida.** `v6`, `v7-0608` y `gemini` marcan la
   adjuncion `F ⊣ U` (free/forgetful entre IR y serializacion) como "Formal",
   **contra la advertencia explicita del propio corpus que citan**
   (`icas-adjunciones`: los pares free/forgetful aplicados son "rara vez una
   adjuncion exacta", "no debe leerse como teorema sin mas"). Tres reportes
   cometiendo el mismo error citando la misma fuente que lo prohibe es el
   ejemplo perfecto de correlacion-de-metodo-erronea: el corpus advierte, la
   skill no fuerza el chequeo, y varios modelos resbalan igual.

4. **`gemini` esta fuera del cluster de metodo** en la practica: aunque declara
   cat-thinking, NO ejecuta su disciplina (cero formal/heuristico, cero
   hallazgos, audita el sistema en vez de las specs). Sirve como **control
   negativo**: muestra que invocar la skill no garantiza ejecutarla, y que sin
   la disciplina el resultado degenera al functor constante "todo correcto".

Regla operativa para el resto del documento: **el peso de un cluster lo da la
verificacion contra fuente, no el conteo de afirmantes.** Marco `unanime` y
`mayoria` para describir la topologia del acuerdo, pero la columna que decide
verdad es "verificado contra fuente".

---

## 1. Clusters tematicos

Agrupo los ~120 atomic_claims en clusters por objeto categorial auditado.

### Cluster A — Matriz de preservacion de transmutation (`preserved` vs `declared`)

**Statement canonico (verificado):** El ejemplo canonico de `_transmutation.yml`
en `transmutation-spec` declara **5 leyes `preserved`** (composition, identity,
pi_monotonicity, mu_monotonicity, xi_monotonicity) y **3 `declared`**
(xi_naturality, safety_closure, kleisli_composition). El gap real es: las 3
`declared` son deuda de verificacion mecanica, no de diseno.

- Afirman el gap correctamente con la cifra exacta: `report-b1e84abd` (C1),
  `report-a3f7c2e1` (H7), `deep` (C6, C14).
- Afirman el gap pero con **cifra falsa**: `borrador-claude` (ac1: "2/8
  preserved, 6 declared"), `v7-0608` (c7: "5 declared, solo 3 preserved" —
  cifra invertida).
- `v6` y `v7-0607` mencionan la matriz sin comprometerse a una cifra
  (correcto-por-prudencia).

**Status: en-conflicto** sobre la cifra; **unanime** sobre la direccion (existe
deuda de verificacion). Ver contradiccion #1.

### Cluster B — Naturalidad de Xi como deuda critica

**Statement canonico (verificado):** `xi_naturality` esta declarada como ley
functorial obligatoria pero `_transmutation.yml` la marca `status: declared,
evidence: requires runtime review`; ningun check mecanico la verifica. T_R
esta definido sobre objetos (matriz de proyeccion) pero no verificado sobre
morfismos.

- Afirmado por: `report-b1e84abd` (C1), `report-a3f7c2e1` (H7), `deep` (C6),
  `borrador-claude` (implicito en ac1/ac3), `v7-0608` (c7), `v6` (A3 lo
  reconoce como el functor correcto pero con la deuda).
- Contradicho por: nadie. `gemini` lo **ignora** (afirma transmute como functor
  pleno que conmuta, lo que es menos honesto que la propia spec).

**Status: unanime** (entre los que auditan specs). Verdadero. Es el hallazgo
central de la cosecha, pero ver sesgo de metodo punto 1.

### Cluster C — Adjuncion Lift_R ⊣ T_R: ¿adjuncion o conexion de Galois?

**Statement canonico (verificado):** La spec declara `T_R ∘ Lift_R = id (modulo
perdida)` y `Lift_R ∘ T_R ≤ id (modulo atlas)`, con el hedge "cuando es
construible". Como los hom-sets del reticulo PMI x LFS tienen a lo sumo un
elemento, **la estructura real es una conexion de Galois sobre el reticulo, no
una adjuncion 1-categorial**; llamarla "adjuncion" sin mas es un falso-amigo
(en un poset las identidades triangulares son automaticas si se cumple Galois).

- Lectura correcta y fina (Galois): **solo `deep`** (C8). Verificado contra
  `icas-adjunciones` + `transmutation-spec` linea 96.
- Lectura "adjuncion lax declarada-no-verificada" (correcta de fondo, imprecisa
  en el tipo): `report-b1e84abd` (C6, D2), `report-a3f7c2e1` (H9),
  `borrador-claude` (ac3).
- **Sobre-formalizada como "Formal/teorema"** (error): `v6` (A14/c14),
  `v7-0608` (c15/R-F5), `gemini` (Instantiate ⊣ Observe como cumplida).

**Status: en-conflicto.** `deep` tiene razon; los que la marcan "Formal" estan
mal contra el corpus que citan. Ver contradiccion #2 y claim unico valioso #1.

### Cluster D — Espacio PMI x LFS: ¿poset/reticulo o categoria rica?

**Statement canonico (verificado):** Cada eje es un reticulo finito de orden
total (join=max, meet=min); el producto es un reticulo; el espacio valido es un
**sub-poset** definido por las 5 restricciones inter-eje (`harness-spec §4.1`),
que son implicaciones decidibles sobre dominio finito verificadas por el check
`vector-laws`. Es poset (a lo sumo un morfismo entre objetos), no categoria con
morfismos ricos.

- Afirmado por: `report-b1e84abd` (C8), `deep` (C3, C4, C5), `v6` (c6),
  `v7-0608` (c1, c2), `report-a3f7c2e1` (H1 lo toca via reticulo Sigma).
- Matiz adicional correcto: `v6` (A1/c1) y `report-a3f7c2e1` (S31) leen las
  4 capas como fibration/functores; plausible, no verificado formalmente.

**Status: unanime** entre quienes lo tocan. Verdadero. Sin contradicciones.
Buen ejemplo de consenso robusto que ademas es verdad simple.

### Cluster E — Producto semidirecto `⋉` sin accion definida

**Statement canonico (verificado):** `harness-spec` usa el operador
`(m_p x c_q x Xi) ⋉ Contexto` ("producto semidirecto") sin definir el grupo G ni
la accion phi: G -> Aut(A). Es lenguaje **heuristico**, no construccion formal:
no hay accion de los ejes LFS sobre los PMI; es producto de reticulos con
restricciones de compatibilidad.

- Afirmado por: `deep` (C2, C5), `report-a3f7c2e1` (H3), `v7-0607` (AC1),
  `v7-0608` (c1 lo lista como formal pero el cuerpo lo matiza).

**Status: mayoria** entre quienes lo tocan. Verdadero. `deep` y `v7-0607` lo
clasifican explicitamente como heuristico, que es la lectura correcta.

### Cluster F — Axioma de agencia: Pi=free monad, Mu=cofree comonad, Xi=ley

**Statement canonico (verificado):** El axioma `Artefacto = (m_p x c_q x Xi)`
identifica Pi con la free monad m_p, Mu con la cofree comonad c_q y Xi con la
ley de interaccion `m_p ⊗ c_q -> m_{p⊗q}`, fiel a `icas-agencia` (Libkind-
Spivak, "pattern runs on matter"). Es la pieza **formal** mas solida de la
ontologia.

- Afirmado por: `deep` (C1), `v7-0608` (c3/O-F3), `v7-0607` (AC2), `gemini`
  (C5 — su unico claim plenamente verificado), `report-b1e84abd` (C3 via
  coalgebra).

**Status: unanime.** Verdadero. Notable: es el unico claim donde `gemini`
acierta de lleno, porque es re-narracion fiel del corpus, no auditoria.

### Cluster G — Coreografia multiagente como sheaf (falta el sitio)

**Statement canonico (verificado):** `multiagente-spec` modela la coreografia
como sheaf `Ch = (Roles, Fases, Cover, Sec, Glue)` y distingue coreografia
(sheaf) de orquestacion (operad/wiring). Es heuristico de alta calidad: declara
Cover/Sec/Glue pero **no establece el sitio (C, J)** (la topologia de
Grothendieck) que lo haria verificable.

- Afirmado por: `deep` (C10), `borrador-claude` (ac5), `report-b1e84abd` (C2 via
  topos/Omega), `v7-0607` (AC9), `v7-0608` (implicito).
- Matiz de anclaje: `v7-0607` atribuye "coreografia=sheaf" a `icas-protocolos §2`
  donde el corpus primario la define como **profunctor** (el sheaf aparece
  despues, para consenso). Fiel a la spec, impreciso respecto al corpus.

**Status: mayoria.** Verdadero. La falta del sitio es real.

### Cluster H — Yoneda / api_observable

**Statement canonico (verificado):** `autoria-spec §3.5.1` declara
`api_observable` como "Yoneda operativo". El claim correcto: api_observable es
condicion **necesaria pero no suficiente**; es un representante, no el
isomorfismo natural `Hom(A,-) ≅ Hom(B,-)`; la igualdad deberia ser de
representables, no de objetos. `icas-identidad-es-relacion` define representable
como `F ≅ Hom(A,-)`.

- Lectura fina correcta: `report-a3f7c2e1` (H6), `borrador-claude` (ac4),
  `report-b1e84abd` (D4 lo usa bien para topos).
- Lectura "espiritu Yoneda, no construccion formal": `deep` (C13),
  `report-a3f7c2e1` reconoce el matiz.
- `gemini` no lo toca.

**Status: mayoria.** Verdadero. Convergencia genuina y bien anclada.

### Cluster I — Koraficacion (Functor K): ¿faithful? ¿monada idempotente?

**Statement canonico (verificado):** `md-spec` declara la koraficacion como
"functor fiel" con FS=100% sin exhibir leyes functoriales (no se verifica
`K(g∘f)=K(g)∘K(f)`); "fiel" se usa como falso-amigo de *faithful*. El corpus
`02-preservacion` linea 106 define faithful como **inyectividad sobre hom-sets**
(no colapsar flechas), que es distinto de "preservar todos los monomorfismos".

- Diagnostico correcto (metaforico, falta verificar sobre morfismos): `deep`
  (C11), `report-b1e84abd` (C5), `v7-0607` (AC12), `v7-0608` (c14/S-D2).
- **Falso-amigo cometido**: `v6` (A13/c16: "FS=100% = K faithful = preserva
  todos los monomorfismos"). Confunde faithful con mono-preservation.

**Status: en-conflicto** en el detalle (v6 introduce un error que los demas no
cometen); **mayoria** en que K no esta verificado como functor. Ver
contradiccion #3.

### Cluster J — Lifecycle / olas (`Ola_k` como functor)

**Statement canonico (verificado):** `gobernanza §5.1` describe la transicion
`Ola_k -> Ola_{k+1}` como functor, pero la spec misma alterna entre "functor"
(una linea) y "morfismo" (otra), con confusion de niveles. Es metaforico.

- Afirmado por: `deep` (C12 — nota la auto-contradiccion de la spec),
  `report-a3f7c2e1` (H10), `v6` (c10 via dos posets + functor testigo).
- Las dos cadenas de lifecycle como posets distintos irreversibles: `v6` (A10),
  `v7-0607` (AC8 via promocion = inclusiones sin inversa).

**Status: mayoria.** Verdadero. `deep` aporta el detalle mas duro (la spec se
contradice a si misma).

### Cluster K — Precedencia de specs: ¿orden total o preorden?

**Statement canonico (verificado):** La precedencia de `gobernanza §3` es un
**preorden** (hay pares incomparables del mismo nivel sin regla de
especializacion), no un orden total. La regla "prevalece la mas especifica" es
un morfismo en ese poset.

- Afirmado por: `v6` (A11/c11 — verificado), `report-a3f7c2e1` (H11 via regla de
  especializacion), `report-b1e84abd` (C12 via coproducto de regimenes URN).

**Status: mayoria.** Verdadero, poco contestado.

### Cluster L — Matriz de validacion organizada por forma_material vs doctrina arnes-discriminante

**Statement canonico (verificado):** `autoria-spec v2.0` declara el **arnes como
discriminante ontologico** (§4.6) pero la matriz de realizabilidad §6/§12 esta
organizada **por forma_material**. Hay desalineacion doctrina/enforcement real.

- Hallazgo HIGH correcto: `v6` (A15/c15 — su hallazgo mas fuerte, lo admite el
  propio §4.6).
- Capturado pero **sub-dimensionado** (graduado BAJA, error de severidad):
  `v7-0607` (AC13 lo reconoce como perdida del propio reporte).
- Tension relacionada (atlas "ortogonales" §4.5 vs discriminante §4.6): `v6`
  (A7), no enganchada por `v7-0607`.

**Status: minoria** (solo v6 lo eleva correctamente). Verdadero y valioso. Ver
claim unico valioso #2.

### Cluster M — Atlas "ortogonales": error de atribucion de fuente

**Statement canonico (verificado):** El termino "ortogonales/independientes"
para los tres atlas vive **solo en `autoria-spec §4.5`** (linea: "Tres atlas
ortogonales"). `harness-spec §5` dice lo contrario: "Tres atlas
**complementarios**... proyecciones semanticas, no clasificaciones disjuntas".

- `v6` (A7/c17) afirma que "harness-spec §5 declara los atlas ortogonales" — eso
  es **error de atribucion factual** (verificado: harness §5 dice
  complementarios). El hallazgo de fondo (la ortogonalidad es imprecisa por las
  restricciones cruzadas arnes-forma) es correcto; la cita esta mal.

**Status: aislado.** El hallazgo de fondo es plausible; la atribucion es falsa.

### Cluster N — Cites: ciclos, orden, y que hace el toolchain

**Statement canonico (verificado):**
- En el frontmatter de las specs hay relaciones `cites` que forman ciclos
  (autoria<->qa, md->knowledge->autoria->md). Verdadero.
- El agregado "21 ciclos" NO es verificable y tiene aire de precision fabricada.
- El check `relations-laws` verifica `supersedes/refines acyclic` (NO cites;
  cites admite ciclos por diseno, declarado en `knowledge-spec §6.3`).
- En el grafo de desarrollo (`kora graph`), las aristas spec->spec son **todas
  de kind `XRef`** (67); hay **cero `DependsOn` y cero `Cites` spec->spec**. El
  toolchain NO conflaciona cites con depends.
- En el `kb-graph` (689 nodos, usado para orphans/cycles), las specs de
  governance/ontology/serialization/runtime **no son nodos** (viven fuera de
  `artifacts/knowledge/`). Las specs no se auditan a si mismas via kb-graph.

- `borrador-claude` (ac6) afirma los ciclos reales: **verdadero**.
- `borrador-claude` (ac7: "21 ciclos"): **dudoso/fabricado**.
- `borrador-claude` (ac8: "el toolchain trata cites como depends y eso produce
  ruido"): **falso** (el toolchain emite XRef, no DependsOn).
- `borrador-claude` (ac9: "kb-graph no incluye las specs como nodos de primera
  clase"): **verdadero**.
- ac8 y ac9 son **mutuamente inconsistentes** dentro del mismo reporte: si las
  specs no estan en kb-graph (ac9), el toolchain no puede estar conflando sus
  cites a depends ahi (ac8). Ver contradiccion #4.
- `knowledge-spec §6.3` ya declara que cites no implica orden/aciclicidad:
  `v7-0607` (AC6/T6) recomienda agregar esa nota = **hallazgo fantasma**
  (la spec ya lo dice). `report-b1e84abd` (C7) y este mismo reporte afirman un
  check `refines-acyclic` faltante = **falso positivo** (relations-laws ya lo
  cubre).

**Status: en-conflicto** (errores internos y entre reportes). Ver
contradicciones #4 y #5.

### Cluster O — Cambio de base Sigma discreto -> enriquecido

**Statement canonico (verificado):** `qa-spec` (lineas 62, 125-133) declara la
inclusion monotona `ιΣ: {0,1,2,3}^5 -> [0,1]^5` con la receta explicita
ιΣ(0)=0, ιΣ(1)=1/3, ιΣ(2)=2/3, ιΣ(3)=1, y exige preservar monotonicidad. Una
aplicacion monotona entre posets-como-categorias **ES un functor**. El puente
existe y es functorial.

- Lectura correcta (el puente existe): `deep` (C9 — califica qa-spec como la
  spec mas solida), `v6` (C13 via enriquecimiento), `report-b1e84abd` (C13 nota
  la tension pero reconoce el cambio de base).
- **Reportado como gap inexistente**: `v7-0608` (c10/O-D2: "cambio de base no
  functorial / gap de spec"). Error: el reporte no leyo qa-spec (la lista como
  no auditada).

**Status: en-conflicto.** El puente existe; v7-0608 esta mal. Ver
contradiccion #6.

### Cluster P — Objetos zombie: specs deprecadas-no-retiradas

**Statement canonico (verificado):** `canario-spec` y `procesos-spec` siguen
fisicamente en `ontology/` con `status: deprecado` en el frontmatter. Son
objetos zombie (deprecadas pero no retiradas), tension con SSOT.

- Afirmado por: **solo `v7-0608`** (c11/G-D1). Verificado: ambos archivos
  presentes con status deprecado.

**Status: aislado.** Verdadero. Ningun otro reporte lo vio. Ver claim unico
valioso #3.

### Cluster Q — hermes-runtime-extension es un stub

**Statement canonico (verificado):** `hermes-runtime-extension` esta en v0.1.0
stub; su matriz de preservacion pi/mu/xi esta en `status: pending`; sin Lift_R.
`hermes` es canonico (gobernanza §8.2) pero sus transmutaciones son
experimentales.

- Afirmado por: **solo `v7-0608`** (c9/R-D3).

**Status: aislado.** Verdadero. Ver claim unico valioso #3.

### Cluster R — Runtimes canonicos vs archivados (enumeracion)

**Statement canonico (verificado):** Runtimes **canonicos** = {claude-code,
codex, openclaw, hermes, opencode} (gobernanza §8.2/§8.2.1, opencode reactivado
2026-06-04). Runtimes **archivados** = {gemini, mastra, agentskills}
(gobernanza §8.4).

- `v7-0608` (c8/R-D2) cuenta **gemini y mastra como canonicos** (estan
  archivados) y omite opencode/hermes. El numero "4/5" sale por azar pero el
  conjunto de miembros esta mal. **Error.**
- `borrador-claude` (ac14) nota que el cambio de runtime canonico se hizo como
  punto en gobernanza, no como ADR archivado — plausible, distinto tema.

**Status: aislado-erroneo** (solo v7-0608 enumera, y mal).

### Cluster S — Higher-categories: 2-categoria de coreografia, operads sin axiomas

**Statement canonico (verificado):**
- `harness-spec §3.1` menciona el operad `Org^#_m` para Xi=4 sin verificar
  axiomas de operad: `report-b1e84abd` (C10) — plausible/verificado.
- `harness-spec §6` menciona fibracion de Grothendieck para Lambda sin construir
  el functor de indice: `report-b1e84abd` (C11) — verificado.
- 2-categoria de coreografia / coreografia como 2-categoria: `borrador-claude`
  (H7 en prosa). Plausible.

**Status: minoria.** Estos son hallazgos de "falta el nombre/construccion
categorial", de bajo poweroperacional pero correctos.

### Cluster T — autoria-spec §16.1: staleness del ejemplo (atomize/atomic + runtimes archivados)

**Statement canonico (verificado):** El ejemplo `atomizar` de `autoria-spec
§16.1` invoca `entornos_objetivo` con gemini/mastra (archivados) Y la familia
`atomic` (eliminada en md-spec v10) Y el productor `atomize` (retirado,
knowledge-spec v3).

- `v7-0607` (AC3 + AC4) captura ambos niveles: AC3 (runtimes archivados,
  verificado) y AC4 (reconoce que la staleness es mayor: atomic+atomize, no solo
  dos runtimes). Severidad real alta-editorial, el reporte la cuenta media.

**Status: aislado.** Verdadero. Solo v7-0607 lo vio (con auto-correccion de
severidad). Ver claim unico valioso #4.

### Cluster U — Gemini: estructura fabricada y functor constante

**Statement canonico (verificado):** `gemini` inventa el carrier
`U = U_phen x U_ctx x U_epi x U_sta` y un "Principio de Segregacion" y los
atribuye a `icas-efectos`. **No existen** en el corpus ni en harness/autoria
(verificado: 0 hits en todo el corpus + ontology + serialization). harness-spec
descompone el agente en 6 ejes PMI x LFS, no en un producto fibrado de 4
estados.

- `gemini` (C4) lo afirma como verificado. **Erroneo: estructura fabricada.**
- `gemini` ademas afirma transmute como functor pleno que conmuta (C7), la
  adjuncion Instantiate ⊣ Observe como garantia de seguridad (C6), y el veredicto
  global "correctness-by-construction, cero defectos" (C10). Todos son el
  **functor constante hacia "todo correcto"**, mas optimistas y menos honestos
  que las propias specs.

**Status: aislado-erroneo.** `gemini` es el control negativo de la cosecha.

---

## 2. Consenso robusto (el LIMITE de los functores)

Lo que casi todos los auditores-de-specs afirman Y resiste verificacion contra
fuente. Esto mapea a `icas-universales`: el limite es el objeto que se proyecta
consistentemente a todos los functores.

1. **Existe deuda de verificacion mecanica, no de diseno.** Las leyes
   functoriales criticas (xi_naturality, safety_closure, kleisli_composition)
   estan `declared` no `preserved` en `_transmutation.yml`; ningun check las
   verifica. (6/8; verificado.)
2. **T_R esta definido sobre objetos, no verificado sobre morfismos
   (naturalidad de Xi).** (unanime entre specs-auditors; verificado.)
3. **El espacio PMI x LFS es un poset/reticulo finito (sub-poset con
   restricciones inter-eje), no una categoria con morfismos ricos**, y las 5
   leyes inter-eje son decidibles y verificadas por `vector-laws`. (unanime;
   verificado.)
4. **El axioma de agencia (Pi=free monad, Mu=cofree comonad, Xi=ley de
   interaccion) es formal y fiel a icas-agencia.** (unanime; verificado.)
5. **La distincion `preserved`/`declared` de `_transmutation.yml` es el activo
   de integridad intelectual del sistema y deberia extenderse a todas las
   specs.** (deep C14, report-a3f7c2e1, report-b1e84abd; verificado como
   recomendacion sana.)
6. **El sistema NO comete falsos-amigos groseros en las specs mismas**:
   functor/monada/coalgebra/sheaf/bisimulacion se usan donde hay (o casi hay)
   leyes correspondientes. (report-b1e84abd C14, deep, v7-0607; plausible —
   los falsos-amigos aparecen en *algunos auditores*, no en las specs.)

Estos 6 son el consenso robusto. Notese que 4 de 6 son verdades estructurales
relativamente simples; su unanimidad es tanto correlacion-de-metodo como
verdad. El #1 y #2 cargan el verdadero peso diagnostico.

---

## 3. Cobertura union (el COLIMITE: todo tema tocado por al menos uno)

El colimite reune todo objeto auditado por algun functor. Temas cubiertos:

- transmutation: matriz preserved/declared, naturalidad Xi, adjuncion/Galois
  Lift⊣T, bisimulacion modulo perdida, composicion de functores (no
  conmutatividad), orden ≤ del reticulo.
- harness: espacio PMI x LFS como poset, 5 leyes inter-eje, producto semidirecto
  ⋉, axioma de agencia (free/cofree/Xi), operad Org^#_m, fibracion de Grothendieck
  para Lambda, Sigma como reticulo, meta-dimension de presentacion (ana/cata).
- autoria: api_observable/Yoneda, arnes como discriminante vs matriz por
  forma_material, atlas "ortogonales"/complementarios, shape coalgebraico (FSM),
  promocion como inclusiones de subcategorias, qa_budget como subobjeto de Sigma,
  staleness §16.1 (atomize/atomic).
- md: koraficacion (Functor K, faithful, monada idempotente), telegrafizacion
  FS/CR.
- knowledge: relations (depends=DAG, supersedes=poset, refines=preorden, cites
  ciclico), refines mutuo/antisimetrizacion, KnowCat Bool-enriquecida.
- gobernanza: 4 capas como functores/fibration, precedencia como preorden, regla
  de especializacion, olas/lifecycle, regimenes URN como coproducto, runtimes
  canonicos vs archivados, specs deprecadas-no-retiradas (zombies), ADR faltante
  para cambio de runtime.
- qa: V_QA monoidal enriquecida, inclusion monotona ιΣ (cambio de base).
- multiagente: coreografia como sheaf, falta del sitio (C,J), coreografia vs
  orquestacion (sheaf vs operad), 2-categoria de coreografia.
- runtime-extensions: hermes stub, fidelidad por runtime, namespace foraneo
  (salubrista-openclaw en agengai).
- toolchain (parcial, fuera de scope estricto): kb-graph no incluye specs,
  XRef vs DependsOn, monotonicidad decidible no ejecutada.

**Huecos del colimite** (ningun reporte de specs los cubre a fondo):
- Formal Layer oficial `categorical-foundations/` 02-04, 06-08 (06-audit-
  invariants y 07-behavioral-preservation son justo donde podria refutarse o
  confirmarse el hallazgo central de naturalidad/bisimulacion). `deep`,
  `report-b1e84abd` y `report-a3f7c2e1` declaran honestamente no haberlos
  abierto.
- `procesos-spec` y `risk-register-spec` como objetos auditados (solo v7-0608
  toca procesos via zombie).
- runtime-spec-md a fondo.

---

## 4. Contradicciones (mismo objeto, functores incompatibles)

### Contradiccion #1 — Cifra de la matriz de preservacion

- **Lado A** (`borrador-claude` ac1): "2/8 preserved, 6 declared".
- **Lado B** (`v7-0608` c7): "5 declared, solo 3 preserved" (invertido).
- **Lado C** (`report-b1e84abd`, `report-a3f7c2e1`, `deep`): la cifra correcta
  implicita es 5 preserved / 3 declared.
- **Quien tiene razon: el lado C.** Verificado contra `transmutation-spec`
  (ejemplo canonico de `_transmutation.yml`): 5 `preserved` (composition,
  identity, pi/mu/xi_monotonicity) + 3 `declared` (xi_naturality, safety_closure,
  kleisli_composition). `borrador-claude` confundio las 2 leyes basicas de §3.1
  con el total y genero "2/8". `v7-0608` invirtio la cifra. Ambos errores
  inflan el hallazgo bandera de su respectivo reporte. La direccion del hallazgo
  (existe deuda) es correcta en los tres; la cifra solo en C.

### Contradiccion #2 — Lift_R ⊣ T_R: ¿adjuncion Formal o conexion de Galois?

- **Lado A** (`v6` A14, `v7-0608` R-F5, `gemini`): adjuncion `F⊣U`/`Lift⊣T`
  marcada "Formal/teorema/cumplida".
- **Lado B** (`deep` C8): conexion de Galois sobre el reticulo, NO adjuncion
  1-categorial; "adjuncion" es falso-amigo.
- **Quien tiene razon: `deep`.** Verificado: en un poset (hom-sets <= 1 elemento)
  la estructura `Lift_R ∘ T_R ≤ id` es exactamente una conexion de Galois; el
  corpus `icas-adjunciones` que el lado A *cita* advierte que free/forgetful
  aplicado es "rara vez una adjuncion exacta" y "no debe leerse como teorema sin
  mas". El lado A se sobre-formaliza contra su propia fuente. (`report-b1e84abd`
  y `report-a3f7c2e1` ocupan terreno intermedio correcto-pero-impreciso:
  "adjuncion lax declarada-no-verificada".)

### Contradiccion #3 — Koraficacion faithful: ¿= preserva monos?

- **Lado A** (`v6` A13): "FS=100% = K faithful = preserva todos los
  monomorfismos".
- **Lado B** (`deep`, `report-b1e84abd`, `v7-0607`): K es metaforico; "fiel" es
  falso-amigo de faithful; falta verificar leyes functoriales sobre morfismos.
- **Quien tiene razon: el lado B.** Verificado contra `02-preservacion` linea
  106: faithful = inyectividad sobre hom-sets (no colapsar flechas), que es
  **distinto** de preservar monomorfismos. `v6` conflaciona dos propiedades y
  ademas se contradice internamente (su propio §6 lista el claim como
  Heuristico). El lado B es la lectura correcta.

### Contradiccion #4 — ¿El toolchain conflaciona cites con depends? (intra-reporte)

- **Lado A** (`borrador-claude` ac8): "el toolchain trata cites como depends y
  eso produce el ruido / 21 ciclos".
- **Lado B** (`borrador-claude` ac9, mismo reporte): "kb-graph no incluye las
  specs como nodos de primera clase; las specs no se auditan a si mismas".
- **Quien tiene razon: el lado B.** Verificado: (a) en `kora graph` las aristas
  spec->spec son TODAS `XRef` (67), con cero `DependsOn`/`Cites` — no hay
  conflacion; (b) el `kb-graph` (689 nodos) no contiene las specs como nodos
  (viven fuera de `artifacts/knowledge/`). ac8 y ac9 son mutuamente
  inconsistentes en el mismo reporte: si las specs no estan en kb-graph, su
  toolchain no puede estar conflando alli sus cites. ac8 es falso; ac9 es
  verdadero. El "21 ciclos" es fabricado (los ciclos reales en `depends` = 0; en
  `cites` del frontmatter existen pero el agregado 21 no se sostiene).

### Contradiccion #5 — ¿Falta un check `refines-acyclic`?

- **Lado A** (`report-b1e84abd` C7/D11, y el reporte ac8-adyacente de
  borrador): no hay check de aciclicidad de refines; posible gap; agregar
  `refines-acyclic`.
- **Lado B** (estado real del toolchain): el check `relations-laws` (HIGH,
  scope=artifact) verifica explicitamente "supersedes/refines acyclic;
  supersedes antisymmetric".
- **Quien tiene razon: el lado B (el toolchain).** Verificado contra
  `kora check --list`. La aciclicidad de refines SI esta enforced. El lado A es
  un falso positivo nacido de buscar el nombre literal `refines-acyclic`; ademas
  `report-b1e84abd` se contradice (su F1 cita `relations-laws` como verificador
  de las leyes de relaciones, refutando su propio D11). La recomendacion de
  agregar el check es redundante.

### Contradiccion #6 — ¿El cambio de base Sigma->enriquecido es functorial?

- **Lado A** (`v7-0608` c10/O-D2): "no functorial / gap de spec; declarar
  functor de cambio de base".
- **Lado B** (`deep` C9, `v6`, `report-b1e84abd`): el puente existe y es
  functorial.
- **Quien tiene razon: el lado B.** Verificado contra `qa-spec` lineas 62 y
  125-133: la inclusion monotona `ιΣ: {0,1,2,3}^5 -> [0,1]^5` esta declarada con
  receta explicita, y exige preservar monotonicidad. Una aplicacion monotona
  entre posets-como-categorias es un functor. `v7-0608` reporta como gap algo
  que la spec ya resuelve; el propio reporte admite no haber auditado qa-spec.

### Contradiccion #7 — Scope: ¿que es "auditar las specs"?

- **Lado A** (`gemini`): audita "la arquitectura/sistema/toolchain KORA"; no
  nombra una sola spec.
- **Lado B** (los otros 7): auditan las specs como objeto (la ley), nombrando
  archivos concretos.
- **Quien tiene razon: el lado B.** El encargo es auditar las specs (la ley que
  define artefacto valido), no el sistema. Verificado: `gemini` tiene 0
  menciones de archivos de spec; re-narra la auto-descripcion categorial del
  sistema como hallazgo y concluye cero defectos. Es scope-miss + functor
  constante.

### Contradiccion #8 (menor) — atlas "ortogonales": ¿en harness o en autoria?

- **Lado A** (`v6` A7): "harness-spec §5 declara los atlas ortogonales".
- **Lado B** (la fuente): `harness-spec §5` dice "complementarios... no
  clasificaciones disjuntas"; "ortogonales" vive solo en `autoria-spec §4.5`.
- **Quien tiene razon: el lado B (la fuente).** Error de atribucion factual de
  `v6`: el remedio apunta a la spec que no contiene el termino. El hallazgo de
  fondo (la ortogonalidad es imprecisa por restricciones cruzadas arnes-forma)
  es correcto; la cita esta mal.

---

## 5. Claims unicos valiosos (rompen la naturalidad, parecen correctos)

Hallazgos que **un solo functor** vio y que resisten verificacion: candidatos a
insight genuino. Son las rupturas de naturalidad que importan, porque muestran
que la mayoria comparte un punto ciego.

1. **`deep`: Lift_R ⊣ T_R es una conexion de Galois, no una adjuncion
   1-categorial.** El insight mas fino de toda la cosecha. Mientras 5 reportes
   (incl. los que sobre-formalizan a "Formal") tratan la estructura como
   adjuncion, `deep` identifica que en un poset los hom-sets tienen <= 1
   elemento, por lo que la estructura correcta es Galois (y las identidades
   triangulares son automaticas). Verificado contra corpus + spec. Valioso
   porque corrige el tipo categorial exacto y desactiva tanto la
   sobre-formalizacion como la critica "adjuncion no verificada".

2. **`v6`: la matriz de realizabilidad §6/§12 organizada por `forma_material`
   contradice la doctrina v2.0 de arnes-como-discriminante-ontologico (§4.6).**
   Desalineacion doctrina/enforcement estructural y accionable, que el propio
   §4.6 admite. `v7-0607` la vio pero la grado BAJA (sub-severo); `v6` la elevo
   a HIGH correctamente. Valioso porque es una tension interna de la spec mas
   reciente, no una deuda de verificacion generica.

3. **`v7-0608`: objetos zombie (canario-spec/procesos-spec deprecadas-no-
   retiradas) + hermes-runtime-extension stub.** Ningun otro reporte miro el
   estado de lifecycle de las specs como objetos del sistema. Verificado: ambos
   archivos presentes con `status: deprecado`; hermes con matriz pending. Valioso
   porque audita las specs como *artefactos con ciclo de vida*, no solo como
   texto categorial. (Lastima que el mismo reporte arruine su credibilidad con
   la cifra invertida y la enumeracion erronea de runtimes canonicos.)

4. **`v7-0607`: la staleness de `autoria-spec §16.1` es mas profunda que dos
   runtimes archivados — invoca la familia `atomic` (eliminada, md-spec v10) y el
   productor `atomize` (retirado, knowledge-spec v3).** Auto-correccion de
   severidad rara y honesta. Valioso porque detecta un ejemplo de spec que quedo
   anclado a tres conceptos retirados a la vez; es deuda editorial real que
   genera contradiccion interna del canon.

5. **`borrador-claude`: la runtime-extension `salubrista-openclaw` vive en el
   namespace `agengai` en vez de `runtime/`, sin ADR; y el sitio del sheaf en
   multiagente / la 2-categoria de coreografia.** El unico que recorrio
   namespaces foraneos y morfismos de coreografia de orden superior. Plausible y
   accionable, aunque su reporte pierde credibilidad por la cifra 2/8 y la
   contradiccion H1/H6.

6. **`report-b1e84abd`: enforcement levels como clasificador de subobjetos Omega
   del topos (Heyting/intuicionista).** Uso fiel y productivo de `icas-topoi`:
   identifica el candidato natural a Omega para el sheaf de multiagente, con el
   matiz intuicionista correcto. Valioso porque conecta dos specs (multiagente +
   gobernanza/permisos) via una construccion del corpus, en vez de auditarlas por
   separado.

---

## 6. Sintesis para el meta-evaluador

- **El funtor mas fiel y pleno es `deep`** (44/45): unico que rompe el punto
  ciego compartido (Galois), separa formal/heuristico/metaforico con disciplina,
  0 claims falsos verificados. Es el patron de oro de la cosecha.
- **`report-b1e84abd` (39) es el mejor sibling no-Claude**: cifra correcta,
  anclaje doble, pero arrastra una contradiccion interna (F1 vs D11 sobre
  refines-acyclic).
- **El consenso robusto (seccion 2) es real pero parcialmente inflado por
  correlacion-de-metodo**: 7/8 comparten skill+corpus. El peso probatorio viene
  de la verificacion contra `_transmutation.yml`, `qa-spec`, `kora check --list`
  y el corpus, no del conteo de afirmantes.
- **Los errores falsables se concentran en los hallazgos bandera**: las dos
  cifras de la matriz de preservacion (borrador 2/8; v7-0608 invertida), la
  conflacion cites/depends (borrador H1 vs H6), el check refines-acyclic
  fantasma (b1e84abd, borrador), el gap de cambio de base inexistente (v7-0608),
  la asociatividad fabricada (a3f7c2e1 H8), y la estructura fabricada de gemini
  (U_phen...). Patron: el claim mas ruidoso de cada reporte es el mas propenso a
  error, por presion de severidad (Goodhart inverso).
- **`gemini` es el control negativo**: invocar cat-thinking no es ejecutarla.
  Audita el sistema en vez de la ley, no halla un defecto, inventa estructura, y
  colapsa al functor constante "todo correcto" —menos honesto que las propias
  specs.
