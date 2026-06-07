# Auditoría categorial de KORA — 2026-06-07

Auditor: polymath (con cat-thinking internalizada). Método: lectura de specs
canónicas + implementación en `toolchain/kora_lib/` + tests, sin ejecución
(sin Bash). Cada ley se clasifica **verificado-en-código** (leí impl/test y
confirmé la ley) vs **afirmado-en-prosa** (solo declarado en spec/handoff).

Las referencias categoriales se usan como mapa para *ver* la estructura de KORA,
no como cita decorativa.

---

## 1. Veredicto ejecutivo

El claim central —`KORA = vector PMI×LFS + shape unificado de autoría +
transmutación funtorial`— se sostiene **parcialmente, y con honestidad**. No es
teatro: hay álgebra real verificada en código (monoide de reglas, FSM/coálgebra,
aciclicidad de relaciones, leyes inter-eje). Tampoco es motor pleno: la pieza más
publicitada —el **functor de transmutación**— enforce mecánicamente solo
monotonía/dominio y **auto-declara** las leyes estructurales fuertes (naturalidad
de Ξ, cierre de safety, composición Kleisli) como `"declared / requires runtime
review"`. La maquinaria categorial es **mayormente andamiaje de alta calidad con
un núcleo genuino**: organiza y restringe el diseño de forma real, pero la
fracción *demostrada en código* es menor que la prometida en prosa. El `×` de
PMI×LFS es producto reticular (poset), no producto categorial con propiedad
universal. La Formal Layer oficial es rigurosa pero **no funda** la ontología
PMI×LFS: harness-spec traza a `fxsl/cat` (auxiliar, no normativo), no a
`categorical-foundations/`. Motor en el centro, ornamento en los bordes.

---

## 2. Mapa categorial de KORA (lo que realmente existe)

| Construcción | ¿Existe formalmente? | Dónde vive | Estatus |
|---|---|---|---|
| Categoría base de artefactos | Implícita; 3 tipos no comparten una categoría común explícita | harness-spec, knowledge-spec | andamiaje |
| Espacio ontológico PMI×LFS | **Poset producto** (retículo), no producto categorial | harness-spec §3-4 | andamiaje (genuino como poset) |
| Monoide de reglas de autoría | **Sí**: asociatividad + identidad testeadas | `autoria_validate.py`, `test_autoria_validate.py` | **genuino** |
| Functor R: I→List[Rule] (pullback por forma_material) | **Sí**: proyección por discriminante, testeada | `autoria_validate.py` | **genuino** |
| Agente como F-coálgebra `(Out×U)^In` en Kl(M) | **Sí** en Formal Layer; **parcial** en checks (FSM finito) | `cat-agent-coalgebra`, `_check_coalgebra_conformance` | genuino (formal) / andamiaje (check) |
| Functor de transmutación T_R: IR→Runtime_R | Parcial: monotonía/dominio mecánico; resto declarado | `transmute.py`, transmutation-spec | andamiaje honesto |
| Adjunción Lift_R ⊣ T_R (round-trip) | Solo `agentskills` (runtime archivado), vía CLI manual | `cmd_roundtrip_check` | andamiaje |
| Adjunción Check ⊣ Fix | Parcial: 2 fixes (catalog, lint, autoria) como adjunto izq. | `checks.py`, `migration.py` | andamiaje |
| Relaciones knowledge (orden parcial) | **Sí**: aciclicidad + antisimetría verificadas | `_check_relations_laws` + test | **genuino** |
| Retículo de gobernanza / audit cube | Definido formalmente; no mecanizado 1:1 | `cat-governance-lattice`, `cat-audit-invariants` | andamiaje |

---

## 3. Hallazgos por eje

### Eje 1 — Objetos y categoría base · severidad: menor · andamiaje

Los 3 tipos (conocimiento, agentes, skills) **no forman una sola categoría base
explícita**. Conocimiento vive en un orden parcial relacional (depends, supersedes,
refines); agentes/skills habitan el espacio PMI×LFS. No hay morfismos definidos
*entre* tipos ni functor declarado conocimiento→agente. La unidad operacional es
"manifests válidos en el filesystem", no una categoría. Esto es honesto y no
pretende lo contrario, pero el lenguaje "vector ontológico" sugiere más unidad
categorial de la que existe.

### Eje 2 — Morfismos relacionales · severidad: menor · **genuino**

`relations-laws` (registrado en `checks.py:2744`, impl `_check_relations_laws`
en `checks.py:577`) verifica **en código**: aciclicidad de `supersedes`,
aciclicidad de `refines` (DFS tricolor `_find_cycles`, `checks.py:530`),
antisimetría de `supersedes` (`checks.py:636`). Tiene test real:
`test_check_pipeline.py:417` (`test_check_detects_supersedes_antisymmetry_violation`)
con fixture bidireccional. `supersedes-consistency` (`checks.py:904`) añade la
ley lifecycle "A supersedes B ⟹ B deprecado". **Estas son leyes de orden
parcial genuinas, verificadas y testeadas.** Es el eje más sólido junto al
monoide de reglas.

### Eje 3 — Functor de transmutación · severidad: **sustantivo** · andamiaje honesto

transmutation-spec §2-3 promete functor `T_R` con 8 filas de preservación
estructural y nombra checks: `xi-naturality-preserved`, `safety-closure-preserved`,
`kleisli-composition-preserved`, `pi-monotonicity`. **Verificado-en-código**: en
`_structural_preservation_record` (`transmute.py:248`) solo `composition`,
`identity`, `pi/mu/xi_monotonicity` quedan como `"preserved"` con evidencia
mecánica (proyección por matriz, `source_hash` retenido). Las tres leyes fuertes
—`xi_naturality`, `safety_closure`, `kleisli_composition`— se emiten como
`"declared"` con evidencia textual: *"requires runtime review"*, *"not fully
mechanized in transmute"*. Los checks nombrados en la spec (`xi-naturality-preserved`
etc.) **no existen en el registro de checks**. `_project_vector` (`transmute.py:336`)
sí aplica el functor por eje (dominio + fidelidad + pérdida declarada), pero
**no hay test que verifique identidad ni composición del functor** (`T_R(g∘f)=T_R(g)∘T_R(f)`):
el único test "functor" (`test_artifacts.py:356`) sólo comprueba que la *spec
menciona* las palabras. La honestidad del record (`"declared"` ≠ `"preserved"`)
es ejemplar; pero la prosa de la spec sobre-vende leyes que el código no enforce.

### Eje 4 — Adjunciones · severidad: sustantivo · andamiaje

**Check ⊣ Fix**: el header de `checks.py:1-17` declara "Fix is the left adjoint
of a Check". Operacionalmente hay un registro `_FIXES` con 3 fixes
(`catalog-exists`→reindex, `lint-md`→autofix, `autoria-conformance`→`migrate`).
`_fix_autoria_conformance` (`checks.py:1211`) documenta propiedades esperadas
(idempotencia `fix∘fix=fix`, reducción) y dice "tests las verifican". **No
encontré test de idempotencia del fix**; `test_check_pipeline.py:220` solo
verifica que los fixes *están registrados*, no las leyes de adjunción (unit/counit,
triángulos). La adjunción es **metáfora estructurante honesta**, no adjunción
demostrada. `Build ∘ Transmute` quedó postergada por el freeze de harness (memoria
2026-05-18). **Lift_R ⊣ T_R**: solo construible para `agentskills` (runtime
*archivado*), vía `cmd_roundtrip_check` (`transmute.py:2361`), invocable a mano,
**no es un check del pipeline strict**. El round-trip compara name/desc/body-hash/
file-hash — verificación real pero de cobertura mínima (1 runtime en pausa).

### Eje 5 — Coálgebras · severidad: sustantivo · genuino (formal) / andamiaje (check)

La Formal Layer (`cat-agent-coalgebra.md`) define con rigor el agente como
F-coálgebra `(Out×U)^In` en Kl(M), con teoremas (M-immutability, bisimulación).
**Esa es la coálgebra genuina.** Pero `coalgebra-conformance` (impl
`_check_coalgebra_conformance`, `checks.py:2179`) **no verifica una coálgebra
`X→F(X)`**: verifica un **FSM finito** — buena formación (inicial/terminales/
transiciones en estados), *termination* (todo estado alcanzable llega a terminal,
BFS+reachability `checks.py:2304`), y cierre de `sub_coalgebra_segura` bajo
transiciones (`checks.py:2338`). El cierre de sub-coálgebra **sí** es la propiedad
`α(S)⊆F(S)` de harness-spec §4.2, materializada sobre el FSM. Pero no hay carrier
`U`, ni estructura `c:U→M(F(U))`, ni bisimulación. Es validación de grafo dirigido
con semántica coalgebraica, no coálgebra en el sentido del doc formal. **Y no
tiene test dedicado** (sólo `test_claude_code_budget.py` lo menciona de pasada).
Brecha: el nombre promete más estructura que el código.

### Eje 6 — Leyes universales / preservación · severidad: sustantivo · andamiaje

`vector-laws` (impl `_check_vector_laws`, `checks.py:1346`) **sí** verifica
en-código las 5 leyes inter-eje de harness-spec §4.1 (L1 Π≥3⟹Μ≥1; L2 Ξ=4⟹Λ≥1;
L3 Φ≥2⟹Μ≥1; L4 acc≥2⟹transp≥2; L5 Λ=3⟹Σᵢ≥2). Son **implicaciones sobre un
poset**, no propiedades universales (límites/colímites). El `×` de PMI×LFS es
**producto de retículos** (join/meet componente a componente, harness-spec §4),
no producto categorial con propiedad universal y proyecciones — la spec misma
dice "producto reticular" (§4), así que el `×` del claim es notación de poset,
correcta pero más modesta que "producto categorial". **Brecha de verificación
crítica para el rigor**: `_check_vector_laws` y `_check_coalgebra_conformance`
**no tienen tests** que ejerciten su lógica de ley (a diferencia de relations-laws
y del monoide). La ley vive en el código pero no está protegida por regresión.
`Lift_R` (ingest, `cmd_ingest` `transmute.py:2985`) existe; composición de skills
vía overlay se delega a `componible_con` (no anidamiento) — no hay colímite/pushout
de skills mecanizado.

### Eje 7 — Coherencia de la Formal Layer · severidad: **crítico** · andamiaje

`categorical-foundations/00-foundations.md` es matemáticamente sólido y
autocontenido (categoría, functor, NT, adjunción con triángulos, monad/Kleisli,
coálgebra, lens, productos). `cat-agent-coalgebra` y `cat-audit-invariants`
construyen sobre él. **Pero la Formal Layer NO funda la ontología PMI×LFS**: grep
de `harness|PMI|LFS|vector_ontologico|pi.*mu.*xi` en `categorical-foundations/`
da **cero coincidencias**. harness-spec, la "constitución ontológica", traza su
fundamento a `urn:fxsl:kb:icas-agencia/efectos/interaccion/escala` (sus
`relations.cites`, harness-spec:24-27) — corpus **auxiliar y explícitamente NO
normativo** (CLAUDE.md §Formal Layer; `Traces to:` no puede apuntar ahí). Es
decir: el factor más central del claim (vector PMI×LFS) descansa formalmente en
el corpus que el propio canon declara no-fundante. La Formal Layer oficial funda
un modelo de agente *distinto* (F-coálgebra `(Out×U)^In`), que `coalgebra-conformance`
realiza parcialmente. `formal-trace-discipline` (`checks.py:831`) **sí** enforce
en-código que `Traces to:` quede dentro de `categorical-foundations/` — buen
guardián — pero harness-spec usa `cites`, no `Traces to:`, así que **escapa al
guardián**. Hay drift estructural entre la ley operativa (PMI×LFS, fundada en
fxsl/cat) y la Formal Layer oficial (coálgebra, fundada en Mac Lane/Barbosa).

---

## 4. Inventario: verificado-en-código vs afirmado-en-prosa

**Verificado-en-código (leí impl + confirmé la ley):**

- Monoide de reglas de autoría: asociatividad + identidad + neutro
  (`test_autoria_validate.py:293,305`). **Con test.**
- Functor R por `forma_material` (pullback de fibra): `test_autoria_validate.py:320-339`. **Con test.**
- Aciclicidad `supersedes`/`refines` + antisimetría `supersedes`
  (`_check_relations_laws` + `test_check_pipeline.py:417`). **Con test.**
- `supersedes ⟹ target deprecado` (`_check_supersedes_consistency`).
- 5 leyes inter-eje PMI×LFS (`_check_vector_laws`). **Sin test de la ley.**
- Termination de FSM + cierre de sub-coálgebra (`_check_coalgebra_conformance`). **Sin test de la ley.**
- Proyección functorial por eje con dominio/fidelidad/pérdida (`_project_vector`);
  monotonía Π/Μ/Ξ y retención de identidad (source_hash). **Sin test de identidad/composición del functor.**
- `formal-trace-discipline`: `Traces to:` confinado a la Formal Layer oficial.
- Budget funtorial claude-code: `_derive_claude_code_floor` concuerda con el
  functor (`test_claude_code_budget.py:79-95`). **Con test.**
- Round-trip `T∘Lift≈id` solo para `agentskills` (CLI manual, runtime archivado).

**Afirmado-en-prosa (declarado, no enforced/parcial):**

- `xi-naturality-preserved`, `safety-closure-preserved`, `kleisli-composition-preserved`:
  nombrados en transmutation-spec §3.2; emitidos como `"declared / requires runtime
  review"` (`transmute.py:259-270`); **no existen como checks**.
- Adjunción Check ⊣ Fix con triángulos/unit/counit: metáfora en header; solo 3
  fixes registrados; idempotencia documentada pero **sin test**.
- `Build ∘ Transmute`: postergada (freeze).
- Bisimulación / final coalgebra: rigurosa en la Formal Layer, **no mecanizada**
  en checks (P2 de `cat-audit-invariants` queda manual).
- "Producto categorial" PMI×LFS: es producto de retículos, no producto con
  propiedad universal.

---

## 5. Recomendaciones priorizadas

1. **(Crítico, eje 7)** Cerrar el drift de fundamento: o bien absorber PMI×LFS a
   la Formal Layer oficial (un doc `categorical-foundations/0X-harness-lattice.md`
   que defina el poset producto, las 5 leyes y la relación con la F-coálgebra), y
   hacer que harness-spec lo trace con `Traces to:` además de `cites` a fxsl/cat;
   o bien rebajar explícitamente el claim a "fundado en corpus auxiliar, pendiente
   de absorción formal". Hoy la constitución ontológica se apoya en lo no-normativo.

2. **(Sustantivo, ejes 5-6)** Añadir tests de regresión para `_check_vector_laws`
   y `_check_coalgebra_conformance` (un fixture por ley: violación + caso limpio),
   al nivel de lo que ya tiene `relations-laws`. Una ley sin test es una ley que
   silenciosamente se rompe en el próximo refactor.

3. **(Sustantivo, eje 3)** Alinear prosa y código en transmutation-spec §3.2:
   marcar `xi-naturality`, `safety-closure`, `kleisli-composition` como
   `declared (no mecanizado)` en la spec —igual que ya hace el record en
   `transmute.py`— y retirar/renombrar los "checks" nombrados que no existen, o
   implementarlos. Eliminar la asimetría spec-promete / código-declara.

4. **(Sustantivo, eje 4)** Si Check⊣Fix se sostiene como adjunción, añadir el test
   de idempotencia (`fix∘fix=fix`) y de reducción que el docstring ya promete; si
   no, degradar el lenguaje de "left adjoint" a "fix canónico parcial" para no
   inflar el claim.

5. **(Menor, eje 5)** Renombrar `coalgebra-conformance` a algo como
   `fsm-termination-conformance`, o ampliar el check para tocar carrier/transición
   coalgebraica real. El nombre actual promete la coálgebra del doc formal y entrega
   validación de FSM.

6. **(Editorial, transversal)** Para la portada/presentación de KORA: liderar con
   propósito (repositorio/fábrica de 3 tipos de artefacto) y tratar PMI×LFS +
   transmutación funtorial como **garantía de consistencia**, no como definición.
   El claim categorial es honesto solo si se presenta como lo que verifica
   (poset + leyes inter-eje + monoide de reglas + relaciones), no como
   "producto categorial + functor pleno".

---

## 6. Juicio global honesto

KORA **no es teatro categorial**. Tiene un núcleo de álgebra genuina, verificada y
testeada: el monoide de reglas de autoría, el functor de fibra por forma material,
y las leyes de orden parcial sobre relaciones de conocimiento. Esos tres cargan
peso real y restringen el diseño. La Formal Layer oficial es seria y autocontenida.

Pero el **eje más publicitado del claim —"transmutación funtorial"— es el más
débil en evidencia**: el código es honesto al separar `preserved` de `declared`,
y precisamente por eso revela que las leyes functoriales fuertes no están
mecanizadas. Y el **fundamento del primer factor (PMI×LFS) no vive en la Formal
Layer oficial sino en el corpus auxiliar no-normativo** — la constitución
ontológica está, formalmente, parada sobre algo que el canon declara no-fundante.

Veredicto a la pregunta rectora: **la maquinaria categorial es el motor en el
centro (autoría + relaciones + FSM) y ornamento honesto en los bordes
(functor pleno, adjunciones, bisimulación).** Felix tiene razón al presentar KORA
liderando con propósito: la ecuación categorial es una *garantía parcial real*,
no una definición que se sostenga entera. Quitar la jerga no-mecanizada no rompería
nada operativo; cerrar los tests faltantes (rec. 2) sí convertiría andamiaje en
motor con poco esfuerzo.
