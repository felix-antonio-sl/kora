---
_manifest:
  urn: "urn:kora:kb:auditoria-categorial-specs-borrador-claude"
  provenance:
    created_by: "chiquito"
    created_at: "2026-06-07"
    source: "Auditoria categorial de las 14 specs vigentes de KORA contra el corpus ICAS-BoK (24 URNs); reformulacion, hallazgos por spec, hallazgos transversales sobre la categoria Spec, tabla de salud categorial y 12 recomendaciones priorizadas con URN del corpus. Modelo de inference: Claude (Sonnet). Skill: cat-thinking v1.0.0."
version: "1.0.0"
status: publicado
tags: [audit, categorial, spec, gobernanza, harness, autoria, transmutation, multiagente, knowledge, md-spec, qa-spec, icas-bok, 2-categoria, adjuncion, funtor, sheaf, fibracion, drift, lifecycle]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:fxsl:kb:icas-sintesis"
    - "urn:fxsl:kb:icas-composicion"
    - "urn:fxsl:kb:icas-preservacion"
    - "urn:fxsl:kb:icas-comparacion"
    - "urn:fxsl:kb:icas-identidad-relacion"
    - "urn:fxsl:kb:icas-universales"
    - "urn:fxsl:kb:icas-adjunciones"
    - "urn:fxsl:kb:icas-composicion-estructura"
    - "urn:fxsl:kb:icas-enriquecimiento"
    - "urn:fxsl:kb:icas-higher-categories"
    - "urn:fxsl:kb:icas-efectos"
    - "urn:fxsl:kb:icas-extension"
    - "urn:fxsl:kb:icas-topoi"
    - "urn:fxsl:kb:icas-escala"
    - "urn:fxsl:kb:icas-agencia"
    - "urn:fxsl:kb:icas-protocolos"
    - "urn:fxsl:kb:icas-tiempo"
    - "urn:fxsl:kb:icas-lifecycle"
    - "urn:fxsl:kb:icas-procesos"
    - "urn:fxsl:kb:icas-calidad-riesgo"
    - "urn:fxsl:kb:icas-patrones"
    - "urn:fxsl:kb:icas-infraestructura"
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:risk-register-spec"
    - "urn:kora:kb:procesos-spec"
    - "urn:kora:kb:canario-spec"
    - "urn:kora:kb:host-roles"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:multiagente-spec"
    - "urn:kora:kb:agent-skill-construction-spec"
---

# Auditoria categorial de las specs de KORA

**Autor:** chiquito
**Modelo de inference:** Claude (Sonnet)
**Skill de soporte:** `cat-thinking` v1.0.0
**Fecha:** 2026-06-07
**URN:** `urn:kora:kb:auditoria-categorial-specs-borrador-claude`

> Workflow aplicado: `cat-thinking` v1.0.0. Toda conclusion va citada a su URN del corpus ICAS-BoK (24 piezas en `artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`) y, cuando aplica, a la URN KORA auditada.

---

## 0 - Triaje

**Que se audita**: el estrato **Spec** de KORA, 14 documentos con `family=spec` (o sufijos homologos) que declaran la ley de la casa:

| Capa | Specs |
|------|-------|
| Constitucion (governance) | `gobernanza` v6.2.0, `host-roles` v1.1.0 *(deprecada, absorbida)* |
| Ontologia (ontology) | `harness-spec`, `qa-spec`, `procesos-spec`, `canario-spec` *(deprecada)*, `risk-register-spec` |
| Serializacion | `autoria-spec` v2.0.0, `md-spec`, `knowledge-spec` v3.0.0, `agent-skill-construction-spec` |
| Runtime | `runtime-spec-md` v3.8.0, `transmutation-spec` v1.2.0, `multiagente-spec` v1.0.0, `salubrista-openclaw-spec` |

**Tensiones declaradas** (antes de leer): (1) el grafo de specs es aciclico por `depends` pero **ciclico por `cites`** - 21 ciclos; (2) varias specs se declaran a si mismas funtores/adjuntos/monadas, lo que exige verificar las leyes; (3) la "precedencia" de gobernanza §3 es un poset declarado pero no siempre un orden total realizable.

---

## 1 - Reformulacion categorial

| Fenomeno KORA | Lectura categorial |
|---|---|
| Las 14 specs como documentos relacionados | **Categoria `Spec`** con objetos = specs y morfismos = `depends` (morfismo de **inclusion estructural**), `cites` (morfismo **bibliografico**, mucho mas debil) y `supersedes` (morfismo de **reemplazo**, no invertible) |
| `gobernanza` citada por todas las demas | Objeto **terminal** en el sentido de autoridad (no topologico) - el **counit** del sistema, no el unit |
| `harness-spec` define el espacio IR (PMI x LFS) | **Categoria `IR`** producto de 6 ejes `Π x M x Ξ x Λ x Φ x Σ` con Σ enriquecido en `([0,1]^5, ≤, 1̄, ⊗)` |
| Vector ontologico con leyes inter-eje | **Subobjeto** de `IR` definido por un **sistema de restricciones** (sketch) - `harness-spec §4.1` lo da como axiomas de Π, M, Ξ |
| `autoria-spec` shape unificado | **Funtor de inclusion** `Sh: Artefacto -> IR` cuya imagen es exactamente la sub-categoria `Imagen(Sh)` de vectores realizables |
| Las 4 formas materiales con cadena de promocion | **Sub-categoria plena** `Forma` con morfismos `habilidad -> subagente -> agente-propiamente-tal -> agente-plataforma`; la demesion prohibida ⇒ la **direccion de los morfismos esta ordenada** (categoria **delgada** / thin category) |
| Las 3 atlas A x B x C ortogonales | **Producto de categorias** `AtlasA x AtlasB x AtlasC` (cada atlas es un **enum cerrado** = categoria discreta) ⇒ el espacio de artefactos vive en el pullback `IR ×_Spec (AtlasA x AtlasB x AtlasC)` |
| `transmutation-spec` `T_R: KORA_IR -> Runtime_R` | **Funtor de proyeccion** ya declarado por la spec - candidato a preservacion real (no nominal) |
| `Lift_R ⊣ T_R` (cuando existe) | **Adjunction** ya declarada - verificar si el round-trip cumple leyes de unit/counit |
| `_transmutation.yml` como prueba | **Seccion** en una **fibracion** sobre `KORA_IR` (proof-carrying via fibra) |
| `multiagente-spec` "seccion global desde locales" | **Sheaf** explicitamente declarado (la spec dice "sheaf operacional") |
| `qa-spec` Σ enriquecido en `[0,1]^5` | Categoria enriquecida: `IR_Σ = [0,1]^5` con `≤` y `⊗` monoidal - corresponde a `08-enriquecimiento` |
| `kora check --strict` | **Pullback** en `Spec`: un artefacto es valido si y solo si satisface el pullback de todas las specs que lo requieren |
| `kora resolve <urn>` | **Lookup estilo Yoneda**: el objeto queda determinado por su representable - el catalogo es un **presheaf** `Spec^op -> Set` |
| `kora transmute --target T` | **Computo de un funtor**: la CLI materializa `T_R(X)` |
| Forma material + lifecycle + composicion | **Coalgebra** sobre endofuntor `F(X) = Plan x Interfaz x Contexto x Invariantes` |
| `runtime-spec-md` "equivalencia funcional, no textual" | **Equivalencia observacional** = **bisimulacion** sobre la coalgebra de la spec |

---

## 2 - Corpus invocado y citas

| Pieza ICAS-BoK | URN | Rol en la auditoria |
|---|---|---|
| Composicion / leyes | `urn:fxsl:kb:icas-composicion` | leyes de `T_R` (composicion, identidad) y del shape unificado |
| Preservacion | `urn:fxsl:kb:icas-preservacion` | verificacion de funtorialidad y fidelidad |
| Comparacion | `urn:fxsl:kb:icas-comparacion` | equivalencia entre runtimes; naturalidad de `T_R` |
| Identidad / relacion | `urn:fxsl:kb:icas-identidad-relacion` | Yoneda operativo del shape; `api_observable` |
| Universales | `urn:fxsl:kb:icas-universales` | producto (vector), coproducto (atlas), pullback (check) |
| Adjunciones | `urn:fxsl:kb:icas-adjunciones` | `T_R ⊣ Lift_R`; free/forgetful en autoria |
| Composicion con estructura | `urn:fxsl:kb:icas-composicion-estructura` | categorias monoidales para multiagente |
| Enriquecimiento | `urn:fxsl:kb:icas-enriquecimiento` | `Σ` en `[0,1]^5` (qa-spec) |
| Efectos | `urn:fxsl:kb:icas-efectos` | monadas de plan, comonadas de materia, bisimulacion |
| Extension | `urn:fxsl:kb:icas-extension` | Kan extension de specs a namespaces |
| Topoi | `urn:fxsl:kb:icas-topoi` | sheaves (multiagente) y permisos ricos |
| Escala | `urn:fxsl:kb:icas-escala` | operad para la pila de 4 capas; megamodelo |
| Agencia | `urn:fxsl:kb:icas-agencia` | free monad (plan) y cofree comonad (materia) |
| Protocolos | `urn:fxsl:kb:icas-protocolos` | coreografia multiagente |
| Tiempo | `urn:fxsl:kb:icas-tiempo` | behavior types, FSM, contratos |
| Lifecycle | `urn:fxsl:kb:icas-lifecycle` | V-model, drift, deuda categorial |
| Procesos | `urn:fxsl:kb:icas-procesos` | requirements -> design -> testing (factorizacion) |
| Calidad/riesgo | `urn:fxsl:kb:icas-calidad-riesgo` | `qa-spec`, `risk-register-spec` |
| Patrones | `urn:fxsl:kb:icas-patrones` | anti-patrones, wrapper functors |
| Infraestructura | `urn:fxsl:kb:icas-infraestructura` | toolchain `kora` como 2-categoria |

---

## 3 - Auditoria por spec

### 3.1 `gobernanza` v6.2.0 - `urn:kora:kb:gobernanza`

- **Tipo categorial esperado**: constitucion = **objeto counit** del sistema; no un funtor, no una monada, sino el **functor constante** que provee el **ambiente legal**.
- **Hallazgo A - Precedencia declarada vs realizable**: `gobernanza §3` declara un orden total 1->2->3->4 sobre los rangos de specs. Pero la **precedencia operativa** (que spec "gana" en caso de conflicto) no es total: cuando `qa-spec` y `autoria-spec` se contradicen (p.ej., que campo prevalece en un artefacto), no hay regla de combinacion explicita; el toolchain debe implementar ese pullback. **Falta la operacion de combinacion** - es **union de subobjetos en un poset** sin supremo definido ⇒ no es reticolo, es solo **preorden**. *Patron aplicable: pasar `Spec` con `≤` a un **reticulo** o declarar `Spec` como **fibracion sobre gobernanza** con preferencia explicita.* -> `urn:fxsl:kb:icas-universales`.
- **Hallazgo B - `cites` vs `depends`**: gobernanza es citada por 13/14 specs; el morfismo `cites` la trata como un **grafo de precedencia bibliografica**, lo cual es legitimo, pero el riesgo es que la constitucion quede **invocada como autoridad** sin ser **invocada como counit**. Una spec que cita gobernanza no queda automaticamente en cumplimiento; necesita la **evaluacion** del pullback.
- **Hallazgo C - version de 6.1 -> 6.2**: el cambio (reactivar `opencode` como canonico) se hizo como **punto en gobernanza**, no como ADR archivado separado. Buena practica: cualquier promocion/deprecacion de runtime debe dejar **traza archivada en `decisiones-archivadas/`**, que es donde el sistema ya tiene el patron.

### 3.2 `harness-spec` - `urn:kora:kb:harness-spec`

- **Tipo**: **ley ontologica**. Define `IR = Π x M x Ξ x Λ x Φ x Σ` con sketch (leyes inter-eje) y Σ en `[0,1]^5`.
- **Hallazgo D - leyes inter-eje declaradas, no axiomatizadas**: §4.1 da las leyes como prosa. Conviene **promoverlas a axiomas formales** del sketch (texto declarativo pero con tabla `(Π,M,Ξ,Λ,Φ,Σ) ⊨ axioma` referenciable). Hoy un agente que escribe un vector fuera de ley lo descubre solo al pasar checks. *Patron: sketch presentable por una teoria de Lawvere con teorias asociadas.* -> `urn:fxsl:kb:icas-adjunciones`.
- **Hallazgo E - freeze formal vigente**: el freeze es sano, pero combinado con la **ausencia de axiomas formales** (Hallazgo D) hace que cualquier correccion menor requiera re-negociar el freeze. **Recomendacion**: el freeze protege semantica, no redaccion; separar el documento en dos: (1) **ontologia formal** (axiomas, dominios) en freeze estricto, (2) **comentarios y ejemplos** editables.

### 3.3 `autoria-spec` v2.0.0 - `urn:kora:kb:autoria-spec`

- **Tipo**: **funtor de serializacion** `Sh: ArtefactoAgentico -> IR`, parcial segun forma material.
- **Hallazgo F - arnes como discriminante ontologico** (v2.0, HITL 2026-05-20): se **unifica ontologicamente** "skill" y "agent" como el mismo objeto. Eso es **correcto desde la teoria** (es el arnes el que define el objeto, no la topologia fisica). Pero la spec mantiene **dos arboles de archivos** (`artifacts/skills/` y `artifacts/agents/`) por "conveniencia operacional". Esto es un **2-celda** entre la categoria ontologica (un solo objeto) y la categoria de filesystem (dos lugares). El riesgo: el check no puede saber, por **mera inspeccion del path**, que forma material es. La **discriminacion** esta bien hecha - solo en el frontmatter - pero la spec deberia **declarar explicitamente** el 2-morfismo y la **invariante**: "un path `artifacts/skills/X/` no implica `forma_material=habilidad`; solo el frontmatter decide". -> `urn:fxsl:kb:icas-higher-categories`.
- **Hallazgo G - `forma_material` y promocion**: la cadena es un **morfismo en una categoria delgada** con orden parcial. La **promocion preserva URN** y bumpea major; la **demesion esta prohibida** (correcto: seria **perdida de estructura no functorial**). Pero la spec no dice que pasa con la **monotonicidad**: si `forma_material` cambia, ¿los morfismos de composicion (`componible_con`) se preservan? **Riesgo**: la **adjuncion libre** que el autorship promete (un agente-propiamente-tal es "libre sobre" su plan) **no se preserva** al promover, porque `composicion` solo se permite en `Ξ=4` (orquestador). **Recomendacion**: declarar el **funtor de promocion** `P: Forma_habilidad -> Forma_agente-plataforma` y su **counit de perdida** explicito (lo que se gana, lo que se exige). -> `urn:fxsl:kb:icas-adjunciones`.
- **Hallazgo H - `api_observable` como Yoneda operativo** (§3.5.1): **excelente**. La spec dice "dos artefactos con el mismo `api_observable` son **indistinguibles por cualquier caller**". Eso es literalmente la **lemma de Yoneda** en una categoria de artefactos. Pero la spec **no cierra la otra direccion**: dos artefactos con api diferente pueden ser indistinguibles por un sub-caller. Conviene **declarar la sub-categoria de observacion** (que morfismos de `C(Artefacto, X)` son visibles para el caller) y **dejar la igualdad `api_observable` como igualdad de representables, no igualdad de objetos**. -> `urn:fxsl:kb:icas-identidad-relacion`.
- **Hallazgo I - `qa_budget` y Σ**: la spec dice "NO DEBE contradecir `vector_ontologico.sigma`; solo puede igualarlo o estrecharlo". Esto es un **morfismo de sub-objetos** en la categoria enriquecida `([0,1]^5, ≤)` ⇒ correcto, pero **el check no lo enuncia asi**. El check deberia ser `Σ_IR ∧ ¬(Σ_budget ≤ Σ_IR) ⇒ FAIL`. -> `urn:fxsl:kb:icas-enriquecimiento`.

### 3.4 `md-spec` y `knowledge-spec` - `urn:kora:kb:md-spec`, `urn:kora:kb:knowledge-spec`

- **Tipo**: **categoria de conocimiento** `KnowCat` con morfismos `cites/refines/traces/depends/supersedes`.
- **Hallazgo J - `KnowCat` es buena pero no declara la sub-categoria de artefactos "normativos"**: la spec describe el grafo pero no define que sub-grafo es **coherente** (consistencia interna). Una `citation` de A a B y de B a C no implica transitividad. Si la spec quiere **propagar restricciones**, debe declarar la sub-categoria **transitive-closure** explicitamente y la **ley de yoneda** sobre el grafo. -> `urn:fxsl:kb:icas-identidad-relacion`.
- **Hallazgo K - pipeline como cadena de funtores adjuntos**: §v2.0 introdujo la cadena `_SCRIPTORIUM/INBOX -> REVIEW -> {ns}/` con adjuncion `free ⊣ forgetful`. Es **categorialmente sano**. Pero la spec **no enuncia el funtor explicitamente** ni su counit (que se pierde al "olvidar" la staging). **Recomendacion**: declarar `F_ingest ⊣ G_publish` y la metrica de **drift categorial** entre staging y publicable (diferencia entre seccion y global, en el sentido sheaf). -> `urn:fxsl:kb:icas-topoi`.

### 3.5 `transmutation-spec` v1.2.0 - `urn:kora:kb:transmutation-spec`

- **Tipo**: **ley de funtores** sobre los `T_R: IR -> Runtime_R`. Esta es la spec con mayor **densidad categorial explicita** del repo.
- **Hallazgo L - la spec se llama a si misma "funtor" pero la verificacion de leyes es parcial**:
  - §3.1 declara **composicion e identidad** como obligatorias. Bien.
  - §3.2 declara 6 estructuras a preservar (Ξ-naturality, safety-closure, Kleisli-composition, Π/M/Ξ-monotonicity).
  - **Pero §6.1 (`_transmutation.yml`)** permite marcar `status: declared` para varias, distinguiendolas de `preserved`. **Esto rompe la pretension functorial**: si la **mayoria** de las leyes quedan como `declared` y no `preserved`, la transmutacion real no es un funtor - es un **funtor parcial con perdida documentada**. La spec deberia **distinguir dos modos**: `T_R` estricto (solo cuando todas las leyes son `preserved`) y `T_R` laxo (con `declared`). -> `urn:fxsl:kb:icas-preservacion`.
- **Hallazgo M - adjuncion `Lift_R ⊣ T_R` declarada pero no construida**: §2.3 y §9 declaran la adjuncion y el round-trip `ingest -> transmute -> ingest ≡ ingest`. **Ningun runtime la implementa verificadamente** hoy. La spec lo dice expresamente: "no todos los runtimes tienen `Lift_R`". Recomendacion: la adjuncion **deberia ser declarativa, no aspiracional** - definir el contrato que un runtime debe cumplir para que `Lift_R ⊣ T_R` sea adjuncion real (hom-natural-iso, unit/counit verificados). -> `urn:fxsl:kb:icas-adjunciones`.
- **Hallazgo N - `_transmutation.yml` como fibracion**: §6 lo llama "proof-carrying artifact". Eso lo identifica con la **fibra de un morfismo** en una fibracion sobre `IR`. Pero la spec **no declara la fibracion** ni la **base**. Hoy es solo metadata por-output, sin teoria. **Recomendacion**: modelar `_transmutation.yml` como seccion de un **presheaf sobre `KORA_IR`** con la proyeccion `p: Trans -> IR`. -> `urn:fxsl:kb:icas-extension`.
- **Hallazgo O - matriz de preservacion por runtime es funcion parcial, no funtor total**: §7.1 muestra como `claude-code.pi["3"]` se proyecta a `pi=2`. Esto significa que `T_R` **no es functor total** - es **funtor parcial** con un **dominio declarado**. La spec lo trata bien declarando `D_R`, pero **no declara la estructura de sub-categoria de `D_R`**: no se garantiza, p.ej., que la **composicion de morfismos en `D_R` se mantenga dentro de `D_R`**. Si la composicion sale, ¿falla? ¿proyecta con `fidelity: none`? **No queda claro.** -> `urn:fxsl:kb:icas-preservacion`.

### 3.6 `runtime-spec-md` v3.8.0 - `urn:kora:kb:runtime-spec-md`

- **Tipo**: **contrato runtime abstracto** (interfaz).
- **Hallazgo P - equivalencia funcional, no textual** (§6): bien enunciada, **bisimulacional** en espiritu. Pero la spec no define el **sistema de transiciones** sobre el cual se evalua equivalencia. Hoy es **declarativa**: "se evalua sobre routing, cierre de tools, enforcement, degradaciones". **Recomendacion**: declarar la **coalgebra de runtime** explicitamente: `α: RuntimeArtefacto -> F(RuntimeArtefacto)` con `F(X) = Routing x Tools x Safety x Degradaciones`, y la **bisimulacion** como la relacion de equivalencia estandar sobre esa coalgebra. -> `urn:fxsl:kb:icas-efectos`.
- **Hallazgo Q - drift audit**: §2.4 dice "posibilidad de auditar drift entre fuente y estado". El drift se define como diferencia entre **fuente** y **estado**. La spec no define la **metrica de drift**. **Recomendacion**: declarar el **functor de drift** `Drift: RuntimeEstado -> RuntimeFuente^op` y la **distancia categorial** (= que tan lejos del counit del pullback `fuente x_specs estado` se esta). -> `urn:fxsl:kb:icas-lifecycle`.

### 3.7 `multiagente-spec` v1.0.0 - `urn:kora:kb:multiagente-spec`

- **Tipo**: **ley sheaf**. La spec se declara a si misma un sheaf operacional.
- **Hallazgo R - sheaf declarado pero no validado contra el topos**: §3.1 declara `Ch = (Roles, Fases, Cover, Sec, Glue)`. La **condicion de pegado** (§3.2) esta enunciada, pero la spec **no declara el sitio** (topologia de Grothendieck sobre la cual `Sec` es presheaf y `Glue` lo convierte en sheaf). **Recomendacion**: declarar el **sitio de cobertura** explicitamente: `J = {cubrimientos por roles que comparten un solapamiento obligatorio}` y la **condicion de sheaf** sobre ese sitio. -> `urn:fxsl:kb:icas-topoi`.
- **Hallazgo S - coreografia vs orquestacion bien tipada** (categoria vs operad): §4 distingue **ley global** (sheaf) de **realizacion local** (operad / wiring diagram). Eso es un **2-categoria**: objetos = coreografias, 1-celdas = orquestaciones, 2-celdas = refinamientos. La spec lo da en prosa, no en el formalismo 2-categorial. **Recomendacion**: declarar la **2-categoria `Coreografia`** con `N(coro) = operad de orquestacion` como nerve, y **caracterizar OpenClaw/ACP como un functor `U: Coreografia -> Wiring^op`**. -> `urn:fxsl:kb:icas-higher-categories` + `urn:fxsl:kb:icas-escala`.
- **Hallazgo T - handoffs canonicos y el "ticket de procedencia"** (§5): bien hecho; es un **objeto minimo** (un **comonoide** en categoria de tipos). Podria declararse formalmente.

### 3.8 `qa-spec` - `urn:kora:kb:qa-spec`

- **Tipo**: **ley de enriquecimiento** (Cost-category / `Σ : IR -> [0,1]^5`).
- **Hallazgo U - `[0,1]^5` con `⊗` monoidal**: declarado. **Pero la asociatividad de `⊗` no se demuestra ni se axiomatiza** - la spec lo asume. Si `⊗` es la media geometrica o el minimo, no es asociativo puro; deberia declararse como **monoidal preorder**, no **monoidal category**, y enunciar la ley. -> `urn:fxsl:kb:icas-enriquecimiento` + `urn:fxsl:kb:icas-composicion-estructura`.
- **Hallazgo V - `qa_budget` como narrowing** (estrechar el `Σ`): bien enunciado. Es un **morfismo de sub-objetos** en la categoria enriquecida. **Correcto**.

### 3.9 `risk-register-spec` - `urn:kora:kb:risk-register-spec`

- **Tipo**: **ledger de riesgos tipados** = **presheaf sobre la categoria de riesgos** con `risk_id` como objeto.
- **Hallazgo W - bien anclado en Σ**; el `sigma_exposure` lo enlaza con la categoria enriquecida. Pero la spec **no declara la operacion de "consolidacion de riesgos"** cuando dos riesgos independientes se solapan. Enriquecido: si dos riesgos tienen `sigma_exposure` independientes, la **exposicion conjunta** es un **producto monoidal** (no el sup) y eso deberia declararse.

### 3.10 `host-roles` v1.1.0 (deprecada) y `canario-spec` (deprecada) y `procesos-spec`

- **`host-roles`**: deprecada, absorbida en gobernanza §12. **Bien**: el morfismo `supersedes` esta declarado. La spec sirve como **referencia historica con URN resoluble** - eso es el patron **correcto** de deprecacion. Pero **deberia** añadirse un **test automatizado** que verifique que toda `cites -> host-roles` se redirige a `gobernanza §12`.
- **`canario-spec`**: deprecada (gobernanza v5.0.0 §11). **Recomendacion**: igual que `host-roles`; documentar el redireccionamiento explicito.
- **`procesos-spec`**: vigente; ancla el V-model de ingenieria. **Hallazgo X - V-model como composicion de funtores**: el V puede leerse como un **adjunction `Spec ⊣ Test`** donde `Spec ⊣ Test`. La spec lo da en prosa; convendria axiomatizar el par adjuncion.

### 3.11 `agent-skill-construction-spec` - `urn:kora:kb:agent-skill-construction-spec`

- **Tipo**: **metodologia** pre-transmutacion. Buen candidato a **operad** sobre la categoria de artefactos.
- **Hallazgo Y - metodologia vs especificacion**: hay una tension: la spec define **como construir** un artefacto, no **que es**. En terminos categoriales, es un **endofuntor** `Build: IR -> IR` con leyes (idempotencia, monotonicidad). La spec no las enuncia. **Recomendacion**: axiomatizar `Build` y exigir **conmutatividad** con `Sh` (serializacion) y `T_R` (transmutacion) - deberia ser un **2-celda natural** `T_R ∘ Build ≅ T_R`.

### 3.12 `salubrista-openclaw-spec` - `urn:agengai:kb:salubrista-openclaw-spec`

- **Tipo**: **runtime-extension** especifica (caso).
- **Hallazgo Z - extension a namespace agengai**: las runtime-extensions canonicas viven en `runtime/`. Esta vive en otro namespace. El patron **deberia** ser uno solo: o todas las runtime-extensions viven en `runtime/` y los namespaces son meras proyecciones, o se admite namespace propio y se documenta. Hoy es ambiguo. **Recomendacion**: el principio rector v6.0 de KORA dice "runtimes canonicos reducidos a 5"; una extension que vive en otro namespace necesita ADR explicito.

---

## 4 - Hallazgos transversales (sobre la **categoria Spec**)

### H1 - Ciclos por `cites` (21 detectados)
El grafo de **depends** es aciclico (8 raices, profundidad 4 con `gobernanza` en el fondo). Pero el grafo de **depends + cites** tiene **21 ciclos**. Ejemplos: `autoria-spec ↔ qa-spec` (mutuo), `md-spec -> knowledge-spec -> autoria-spec -> md-spec` (3-ciclo), y ciclos de 5+ que cierran de vuelta a `gobernanza`.

**Diagnostico categorial**: `cites` no es morfismo de **precedencia** (como `depends`), sino morfismo de **uso** (bibliografico). En una **categoria con dos morfismos distinguidos**, conviene **declarar las leyes de cada uno**:
- `depends`: debe satisfacer **asociatividad, identidad, no-ciclicidad** (es el morfismo de precedencia).
- `cites`: **no requiere DAG** (puede haber circularidad referencial sin incoherencia), pero **debe respetar la transitividad de la autoridad** (si A cita B y B cita C, y C contradice a A, A no queda "ganador" por auto-citacion).

**Recomendacion**: tipar la relacion `cites` como **flecha en un `2-poset` con 2-celdas explicitas** (refinamiento de "que lado gana" en caso de contradiccion). -> `urn:fxsl:kb:icas-higher-categories`. Hoy el toolchain trata `cites` como si fuera `depends` y eso es lo que produce el ruido.

### H2 - Precedencia sin combinacion (sin supremo)
`gobernanza §3` declara orden total entre capas. Pero **dentro de una capa** (p.ej., `autoria-spec` vs `qa-spec`), no hay regla de combinacion. Si dos specs se contradicen en el mismo artefacto, **no hay counit explicito del pullback**. El check actual aborta con error en lugar de **elegir un ganador** segun la precedencia.

**Recomendacion**: declarar `Spec` como **fibracion sobre gobernanza** donde la fibra de cada capa es un **reticulo** (con supremo = la decision del toolchain). -> `urn:fxsl:kb:icas-universales`.

### H3 - La mayoria de las specs se declaran functor/adjunto/monada, pero la verificacion de leyes es declarativa, no mecanizada
`transmutation-spec` y `multiagente-spec` son los casos mas explicitos. La spec dice "transmutacion es funtor" pero admite `status: declared` para 6 de las 8 leyes. **Eso significa que el funtor real tiene 2 leyes verificadas y 6 declaradas** - no es un funtor, es un **funtor parcial con deuda categorial**.

**Recomendacion**: introducir el **perfil de cumplimiento categorial** por spec: una tabla `(ley, status: preserved|declared|absent)` visible en el frontmatter y en el catalogo. -> `urn:fxsl:kb:icas-preservacion` + `urn:fxsl:kb:icas-lifecycle`.

### H4 - Drift categorial sin metrica
`runtime-spec-md §2.4` obliga a poder auditar drift entre fuente y estado. Pero la spec **no define la metrica**. El toolchain detecta drift estructural (campo faltante) pero no drift **categorial** (el IR dice Π=2, el runtime lo realiza como Π=1 sin declararlo).

**Recomendacion**: introducir un **drift-score** que mida la **distancia de counit** en el pullback `fuente x_specs estado`. -> `urn:fxsl:kb:icas-lifecycle`.

### H5 - El shape unificado y el 2-morfismo filesystem ↔ ontologia
`autoria-spec` v2.0 declara "el arnes es el discriminante ontologico, el path es naming convention". Eso es **correcto**, pero crea un **2-morfismo** (cambio de "lenguaje") que **no se verifica automaticamente**: el check usa el path para decidir que schema aplicar antes de leer el frontmatter, lo cual **invierte la precedencia ontologica**.

**Recomendacion**: invertir el orden del check - primero leer el frontmatter, **decidir la forma material desde `atlas.forma_material`**, y solo despues aplicar el schema. Hoy el check `topologia-valida` cruza path ↔ forma con jerarquia confusa. -> `urn:fxsl:kb:icas-higher-categories`.

### H6 - KB-graph es nerve de `KnowCat`, no de `Spec`
El `kb-graph` actual cubre 689 nodos de conocimiento, agentes, skills. **No incluye las specs como nodos de primera clase con su grafo de `depends`/`cites`/`supersedes`**. Eso significa que **el catalogo de specs no se audita a si mismo** por la misma metrica que audita el resto. **Recomendacion**: tratar las 14 specs como **objetos de `Spec`** y graficar `Spec` con el mismo nervio. -> `urn:fxsl:kb:icas-extension`.

### H7 - Multiagente-spec se queda en 1-categoria siendo declaradamente 2-categoria
La spec distingue coreografia (ley global) de orquestacion (ejecutor local). Eso es exactamente la **distincion objeto/1-celda en una 2-categoria** (`N(coro) = operad`). La spec la da en prosa, no en el formalismo. -> `urn:fxsl:kb:icas-higher-categories` + `urn:fxsl:kb:icas-escala`.

### H8 - Forma material y la adjuncion libre
La cadena `habilidad -> subagente -> agente-propiamente-tal -> agente-plataforma` deberia ser una **adjuncion libre** (la promocion es libre sobre el arnes; el counit de la promocion es la capacidad ganada). Hoy esta declarada como **morfismo de una categoria delgada** sin estructura adjunta. -> `urn:fxsl:kb:icas-adjunciones`.

### H9 - `qa-spec` y la eleccion del monoidal
`Σ ∈ [0,1]^5` con `⊗` monoidal. **No se axiomatiza la asociatividad** de `⊗`. Si es minimo o media geometrica, no es monoidal categorico estandar. **Recomendacion**: o usar **`[0,∞]` con +** (Cost-category verdadera) o **`{0,1}` con ∧** (Bool-category) o **`[0,1]` con `max`** (tropical). Mezclar `[0,1]^5` con un `⊗` no declarado es **deuda categorial**. -> `urn:fxsl:kb:icas-enriquecimiento`.

### H10 - `_transmutation.yml` como fibracion no declarada
La spec lo llama "proof-carrying artifact" pero **no declara la fibracion**. Sin base de la fibracion ni fibras, el "proof" es un metadato aislado. -> `urn:fxsl:kb:icas-extension`.

---

## 5 - Tabla de salud categorial

| Spec | Funtorialidad | Adjuncion | Sheaf | Topos | Notas |
|---|---|---|---|---|---|
| `gobernanza` | n/a (counit) | n/a | n/a | parcial (Ω implicito) | sin supremo declarado |
| `harness-spec` | si (objeto IR) | n/a | n/a | n/a | axiomas en prosa |
| `autoria-spec` | **parcial** (Sh, no mecanizado) | **no** (cadena forma-material sin counit) | n/a | n/a | Yoneda operativo (✓) |
| `md-spec` / `knowledge-spec` | n/a | parcial (free⊣forgetful en pipeline) | n/a | n/a | grafo de conocimiento es nerve |
| `transmutation-spec` | **declarado, no verificado** (2/8 leyes) | **declarada, no construida** | n/a | n/a | fibracion no declarada |
| `runtime-spec-md` | n/a (interfaz) | n/a | n/a | n/a | bisimulacion en prosa |
| `multiagente-spec` | n/a | n/a | **declarado** | **sitio no declarado** | 2-cat implicita |
| `qa-spec` | n/a | n/a | n/a | parcial (enriquecido) | `⊗` no axiomatizado |
| `risk-register-spec` | n/a | n/a | n/a | parcial | composicion de riesgos no axiomatizada |
| `procesos-spec` | n/a (V-model) | **no axiomatizada** | n/a | n/a | deberia ser `Spec ⊣ Test` |
| `agent-skill-construction-spec` | **no axiomatizado** (Build endofuntor) | n/a | n/a | n/a | sin 2-celda con T_R |
| `host-roles` / `canario-spec` | n/a (deprecadas) | n/a | n/a | n/a | redireccionamiento sin test |

---

## 6 - Recomendaciones priorizadas (con cita categorial)

| # | Recomendacion | Categoria | URN |
|---|---|---|---|
| R1 | Declarar la **fibra de cumplimiento de leyes** en cada spec (perfil `(ley, status)`) | Drift | `urn:fxsl:kb:icas-lifecycle`, `urn:fxsl:kb:icas-preservacion` |
| R2 | Tipar `cites` como morfismo **de uso** y `depends` como morfismo **de precedencia**; exigir DAG a `depends`, admitir ciclos en `cites` con redireccionamiento explicito | Composicion | `urn:fxsl:kb:icas-composicion`, `urn:fxsl:kb:icas-higher-categories` |
| R3 | Tratar las 14 specs como **objetos de `Spec`** con su propio nerve y grafo en `kb-graph` | Extension | `urn:fxsl:kb:icas-extension` |
| R4 | Invertir el orden del check: frontmatter decide, path confirma | Higher | `urn:fxsl:kb:icas-higher-categories` |
| R5 | Declarar el **funtor de promocion** entre formas materiales y su counit (que se gana) | Adjunciones | `urn:fxsl:kb:icas-adjunciones` |
| R6 | Axiomatizar la **ley monoidal** de `⊗` en `qa-spec` o cambiar la categoria enriquecida | Enriquecimiento | `urn:fxsl:kb:icas-enriquecimiento` |
| R7 | Declarar el **sitio (J)** de la sheaf de coreografia en `multiagente-spec` | Topos | `urn:fxsl:kb:icas-topoi` |
| R8 | Modelar la **2-categoria `Coreografia`** (objetos=coreos, 1-celdas=orquestaciones, 2-celdas=refinamientos) | Higher + Escala | `urn:fxsl:kb:icas-higher-categories`, `urn:fxsl:kb:icas-escala` |
| R9 | Declarar la **fibracion** `p: Trans -> IR` y las fibras como `_transmutation.yml` | Extension | `urn:fxsl:kb:icas-extension` |
| R10 | Distinguir **dos modos** de transmutacion: `T_R` estricto (8/8 leyes preservadas) y `T_R` laxo (con `declared`); marcar el modo en `_transmutation.yml` | Preservacion | `urn:fxsl:kb:icas-preservacion` |
| R11 | Definir la **metrica de drift categorial** como distancia al counit del pullback fuente↔estado | Lifecycle | `urn:fxsl:kb:icas-lifecycle` |
| R12 | Promover las **leyes inter-eje** de `harness-spec §4.1` a axiomas formales del sketch (tabla) | Universales | `urn:fxsl:kb:icas-universales` |

---

## 7 - Conclusion

KORA tiene una **vocacion categorial explicita** (la constitucion, `autoria-spec`, `transmutation-spec`, `multiagente-spec` se declaran funtores / sheaves / adjuntos), pero la **verificacion de las leyes** es **declarativa, no mecanizada**. El corpus ICAS-BoK existe en el repo, esta cited por las specs, pero la mayoria de las veces **termina en prosa** y no en axiomas verificables.

**Faltan tres cosas para cerrar la auditoria**:

1. **Mecanizacion de las leyes**: no basta con declararlas; hay que **implementarlas en el check**.
2. **Drift categorial con metrica**: hoy se detecta drift estructural (campos), no categorial (counit).
3. **Las specs como ciudadanos de primera clase** en el `kb-graph` que las audita.

Las 12 recomendaciones estan priorizadas por impacto estructural y son **enderezables** con 2-3 sprints de trabajo en la toolchain y en las specs. La base categorial ya existe; lo que falta es **conectarla al enforcement**.

---

## 8 - Coexistencia con el informe v6

Este informe coexiste con `urn:kora:kb:auditoria-categorial-specs-v6` (`docs/audit/auditoria-categorial-specs-v6-2026-06-07.md`, autor `opencode/glm-5.1 + skill cat-thinking`). El v6 se centra en **15 hallazgos A1-A15 con severidad** sobre la fibration de capas y la adjuncion F ⊣ U. Este informe, autoria de **chiquito** (Claude + cat-thinking), se centra en **10 hallazgos transversales H1-H10 sobre la categoria Spec**, **23 hallazgos por spec (A-Z)**, **tabla de salud categorial** y **12 recomendaciones priorizadas**. Ambos son validos como lecturas complementarias: el v6 es mas doctrinal (severidad, alternativas, formal vs. heuristico); este es mas operativo (drift, perfil de cumplimiento, priorizacion de cambios).
