# Colímite curado — la auditoría categorial definitiva de las specs de KORA

**Fecha:** 2026-06-08
**Curador:** Claude (Opus 4.8) + skills `custodio-kora` / `cat-thinking`.
**Insumos:** las 8 auditorías de `docs/audit/`, la meta-evaluación 360° (`sintesis-meta-evaluacion.md`, `claims-master.md`, `matriz-nxn.md`) y el cierre de los 3 huecos (`cierre-huecos.md`).
**Qué es:** el "documento único" que la síntesis §10 prescribió. No elige *una* auditoría; **pega** las secciones locales verificadas de un conjunto mayormente `complementa`, con `deep` como cono base, **cinco injertos** verificados (§10.2), las **correcciones** de los errores falsables (§10.3) y los **tres huecos cerrados** (§10.4). Es lo que la síntesis §11 llamó *"`deep` endurecida con cinco injertos verificados y tres huecos cerrados"*.

**Convención de marcado** (la propia medicina, §10.5): cada claim lleva nivel formal — `[F]` formal · `[H]` heurístico · `[M]` metafórico — y estatus epistémico — `(✓)` verificado-contra-fuente · `(decl)` declarado. Un colímite que no se etiqueta a sí mismo sería un *coend* (opinión); etiquetado, es un *end* (verificación).

---

## 0 · El meta-criterio que gobierna el pegado

La síntesis estableció que el valor de un hallazgo lo da **la verificación contra la fuente, no el recuento de afirmantes** (7/8 corren la misma skill `cat-thinking`: convergen por construcción). Este colímite hereda esa regla: **nada entra por consenso; todo entra verificado**. Por eso `deep` (única que rompió el punto ciego compartido y no cometió un claim falso) es la base, y por eso incluso a `deep` se le corrige un dato (la cifra de preservación, §3).

---

## 1 · La columna vertebral verificada (base `deep`, corregida)

Las 12 lecturas categoriales de `deep`, con su nivel y estatus, ya depuradas de los errores de la cosecha:

| # | Spec / claim | Lectura correcta | Nivel · estatus |
|---|---|---|---|
| 1 | `harness §2` — axioma `(m_p, c_q, Ξ)` | free monad × cofree comonad × ley de interacción Libkind-Spivak, fiel a `icas-agencia` | `[F] (✓)` |
| 2 | `harness §2` — operador `⋉` "producto semidirecto" | metáfora de "contexto modula sin sustituir"; sin acción de grupo definida | `[H] (✓)` |
| 3 | `harness §3-4` — espacio PMI×LFS | producto de retículos finitos (join=max, meet=min); **sub-poset** por las 5 leyes inter-eje | `[F] (✓)` |
| 4 | `harness §4.1` — 5 leyes inter-eje | implicaciones decidibles sobre dominio finito | `[F] (✓)` — mecanizadas por `vector-laws` |
| 5 | `qa §3-4` — `V_QA` enriched + cambio de base `ιΣ` | categoría monoidal `[0,1]^5`; `ιΣ: {0,1,2,3}^5→[0,1]^5` monótona = functor. **El patrón oro de la cosecha** | `[F] (✓)` |
| 6 | `transmutation §2-3` — `T_R` sobre objetos | functor definido vía matriz de proyección | `[F] (✓)` |
| 7 | `transmutation §2-3` — `T_R` sobre morfismos | monotonicidad decidible sobre el retículo finito, **no verificada** | `[F]`-decidible · `(decl)` |
| 8 | `transmutation §2.3` — `Lift_R ⊣ T_R` | **conexión de Galois** sobre el retículo (hom-sets ≤ 1), no adjunción 1-categorial. *El insight más fino de la cosecha* | `[H] (✓)` |
| 9 | `multiagente §3` — coreografía como sheaf | intuición local-global correcta; **falta el sitio `(C,J)`** | `[H] (✓)` |
| 10 | `md §5.5` — koraficación "Functor K" | propiedades operacionales válidas (FS=100%, idempotencia); "functor"/"fiel" sin leyes exhibidas | `[M] (✓)` |
| 11 | `gobernanza §5.1` — `Ola_k` "functor" de lifecycle | operación de promoción; confusión de niveles (functor vs objeto) | `[M] (✓)` |
| 12 | `autoria §4.6` — arnés como discriminante ontológico | identidad por estructura (espíritu Yoneda), no construcción formal | conceptualmente correcto · `(✓)` |

**Consenso robusto que sobrevive verificación** (el *límite* del diagrama, §5 de la síntesis): la deuda crítica es de **verificación mecánica, no de diseño**; `T_R` definido sobre objetos no verificado sobre morfismos; PMI×LFS es poset finito; el axioma de agencia es formal; la distinción `preserved`/`declared` es el activo de integridad intelectual; las specs *mismas* no cometen falsos-amigos groseros (los cometen algunos auditores).

---

## 2 · Los cinco injertos verificados (§10.2)

Cada uno es una sección local que **un solo functor vio** y que resiste verificación — las rupturas de naturalidad que importan:

1. **`v6` — `[F] (✓)` — la matriz §6/§12 de `autoria-spec` organizada por `forma_material` contradice la doctrina v2.0 "arnés = discriminante ontológico" (§4.6).** La falla *estructural* más fuerte de la cosecha, que el propio §4.6 admite. `v6` la graduó HIGH; `v7-0607` la sub-graduó BAJA — **`v6` tiene razón**. Tensión interna de la spec más reciente, no deuda de verificación genérica.
2. **`v7-0608` — `[F] (✓)` — objetos zombie: `canario-spec`/`procesos-spec` deprecadas-no-retiradas + `hermes-runtime-extension` stub.** Única lectura de las specs como *artefactos con ciclo de vida*. **Reforzado por `cierre-huecos.md` Parte B:** `harness-spec §10.2` (viva, en freeze) presenta `procesos-spec` (deprecada) y `gemini`/`mastra`-runtime-extension (archivadas) como functores-proyectores **vivos** — el zombie no solo persiste, una spec de máxima precedencia lo presenta como vivo `[ALTO]`.
3. **`v7-0607` — `[F] (✓)` — staleness de `autoria-spec §16.1`:** el ejemplo invoca la familia `atomic` (eliminada, md-spec v10) **y** el productor `atomize` (retirado, knowledge-spec v3) **y** runtimes archivados. Un ejemplo anclado a tres conceptos retirados a la vez; deuda editorial que genera contradicción interna del canon.
4. **`report-b1e84abd` — `[H] (✓)` — enforcement levels como clasificador de subobjetos `Ω` del topos** donde vive el sheaf de `multiagente` (Heyting/intuicionista). Uso fiel y productivo de `icas-topoi`: conecta dos specs (multiagente + gobernanza/permisos) vía una construcción del corpus, en vez de auditarlas por separado.
5. **`borrador-claude` — `[H] (✓)` — `salubrista-openclaw` vive en el namespace foráneo `agengai` sin ADR, + el sitio del sheaf faltante.** Único que recorrió namespaces foráneos y morfismos de coreografía de orden superior.

---

## 3 · Correcciones aplicadas antes de canonizar (§10.3)

Los errores falsables, removidos del colímite:

- **Cifra de la matriz de preservación = `5 preserved / 3 declared`.** `(✓)` contra `transmutation-spec` §6.1 (líneas 256–280): `preserved` = {composition, identity, pi_monotonicity, mu_monotonicity, xi_monotonicity}; `declared` = {xi_naturality, safety_closure, kleisli_composition}. **Se descartan**: `2/8` (borrador) y la inversión `5 declared/3 preserved` (v7-0608). **Corrección adicional sobre la propia base:** la *prosa* de `deep` §3 dice "4 preserved / 4 declared" — también yerra por uno. El colímite usa la cifra canónica verificada, no la de su base.
- **Se elimina la recomendación `refines-acyclic`** (b1e84abd C7/D11, borrador): `relations-laws` ya verifica aciclicidad de `refines`/`supersedes` y antisimetría. `(✓)` contra código (`checks.py:577,593–656`, `cierre-huecos.md` Parte C). Redundante.
- **Se elimina el "gap de cambio de base Σ"** (v7-0608 c10): `qa-spec` ya declara `ιΣ` monótona = functor. `(✓)`.
- **Se elimina H8 "asociatividad podría fallar"** (a3f7c2e1): fabricado; `grep asociativ` = 0 en la spec. `(✓)`.
- **Se corrige la atribución de "ortogonal":** el término vive en `autoria-spec §4.5`, no en `harness-spec §5` (que dice "complementarios… no clasificaciones disjuntas"). El hallazgo de fondo (la ortogonalidad es imprecisa por restricciones cruzadas arnés-forma) se conserva; la cita, corregida. `(✓)`.
- **`gemini` se excluye por completo:** control negativo, ortogonal de dominio (audita el sistema, no la ley; inventa `U = U_phen × U_ctx × U_epi × U_sta`, inexistente). No aporta sección local al colímite.

---

## 4 · Los tres huecos del colímite, cerrados (§10.4)

Detalle completo en `cierre-huecos.md`. Headlines:

- **Formal Layer oficial (`06-audit-invariants`, `07-behavioral-preservation`) — CONFIRMA y AFILA el hallazgo central.** `[F] (✓)`. La Formal Layer **especifica formalmente** las obligaciones que el toolchain deja sin verificar: `06` P1–P3 + `07 §3.2` (preservación iff bisimulación). El `bisimulation_claim`/`xi_naturality: declared` del `_transmutation.yml` **es** esa obligación dejada manual. Por el teorema `06 §7`, KORA es **referencialmente audit-stable** (R1–R3 mecanizados) pero **no preservation-audit-stable** (P1 declarado, P2 ausente, P3 parcial). El hallazgo central pasa de "diseño presente, verificación ausente" a **"el verificador faltante ya está formalmente especificado; falta implementarlo"**.
  - **Drift FL-4 `[F] (✓)`:** `transmutation-spec`/`harness-spec`/`autoria-spec` **no trazan** a la Formal Layer que formaliza sus claims; `transmutation-spec` ancla a `fxsl/cat` (auxiliar). Generaliza el Frente 2 a patrón sistémico. Remediación → Frente 2 + HITL.
- **`procesos-spec`/`risk-register-spec` — 2 hallazgos nuevos.** `harness` viva-en-freeze cita 3 specs deprecada+archivadas como functores vivos `[ALTO]`; `risk-register-spec` declara 5 checks, 0 mecanizados, con `risk_register:` real en >10 agentes productivos `[ALTO]` (un `risk_id` duplicado pasa los 34 checks).
- **Toolchain (código) — los claims de la meta-eval verificados contra código.** Sube de `(decl)` a `(✓)`: `relations-laws`/`vector-laws`/`coalgebra-conformance` mecanizan lo decidible; las 3 leyes de transmutación + bisimulación + P1–P3 quedan ausentes/declaradas; los 2 claims que la meta-eval llamó falsos (borrador: cites-as-depends, refines-acyclic faltante) **son falsos**.

---

## 5 · Veredicto consolidado y backlog priorizado

**Veredicto:** KORA es una arquitectura de *correctness-by-construction en su núcleo ontológico* (`harness`, `qa`) cuya periferia operacional usa teoría de categorías como vocabulario de diseño de precisión variable. La columna vertebral es categorialmente sólida. La deuda crítica **no es de diseño** — el diseño está, y para la preservación está *formalmente especificado en la Formal Layer*. La deuda es **(a) de verificación mecánica** (P2/bisimulación, monotonicidad de `T_R`, los 5 checks de risk-register) y **(b) de coherencia de anclaje/lifecycle** (drift FL-4; harness citando zombies).

Backlog, cada ítem con dueño y palanca:

| Pri | Acción | Tipo | Palanca | Ancla |
|-----|--------|------|---------|-------|
| ~~P0~~ **HECHO** | `risk-id-unique` + `risk-entry-shape` mecanizados (HIGH, TDD) | check-fix | cerrado 2026-06-08 → ver Actualización | `cierre-huecos.md` B.2 |
| **P0** | Implementar `transmutation-monotonicity` (decidible sobre retículo finito, ≤1600 combos/runtime) | check-fix | **mecanizable ya** (deep R3) | base §1 fila 7 |
| **P1** | Reclasificar `harness-spec §10.2` (procesos deprecada + gemini/mastra archivadas como functores vivos) | spec-fix | **HITL** (harness en freeze) | B.1 |
| **P1** | Re-anclar `transmutation`/`harness`/`autoria` a la Formal Layer oficial (no `fxsl/cat`) | spec-fix | **HITL**, coordinar **Frente 2** | FL-4 |
| **P2** | Implementar el check `P2-bisimulación` (07 §8 da el procedimiento) — cierra el hallazgo central | check-fix (research) | requiere modelo de interfaz runtime | A.3 |
| **Ed** | Refrescar `autoria-spec §16.1` (atomic/atomize retirados); adoptar marcado `[F]/[H]/[M]` (deep R1) | spec-fix editorial | mecanizable, bajo riesgo | injerto 3 |

---

### Actualización 2026-06-08 — primer P0 cerrado

El enforcement-gap [ALTO] de `risk-register` quedó **cerrado** en esta misma
sesión, vía TDD (15 tests; helpers puros `_risk_id_uniqueness_violations` /
`_risk_entry_shape_violations`):

- `risk-register-spec` → **v1.1.0**: `risk-entry-shape` y `risk-id-unique` pasan
  de "Enforcement: manual" a **mecanizados en `kora check`** (HIGH, scope
  artifact). Diseño fiel-a-data: dominios validados solo si el campo numérico
  está presente; `risk_id` es el único campo mínimo obligatorio.
- Registro de checks: **34 → 36**. `kora check --strict` = **36/36**.
- El nuevo check **capturó data real**: `urgenciologo/AGENT.md` usaba el campo
  no-canónico `risk:` en vez de `risk_id:` (4 entradas) — corregido (artifact-fix,
  no relajación del check). Ningún otro productivo infringía.

Pendiente del backlog: `transmutation-monotonicity` (P0), re-anclaje a Formal
Layer + harness-zombie (P1, HITL/Frente 2), `P2-bisimulación` (P2).

## 6 · Cierre

La auditoría categorial definitiva de las specs de KORA no es ninguna de las ocho: es `deep` endurecida con los **cinco injertos** verificados, depurada de los **errores falsables**, y completada con los **tres huecos cerrados**. La novedad sustantiva que el cierre de huecos aporta sobre la cosecha entera: **la Formal Layer oficial ya contiene la especificación formal del verificador que falta** (bisimulación, 07 §3.2), de modo que la deuda crítica es estrictamente de implementación y de re-anclaje — no de diseño.

Este colímite se aplicó su propia medicina: cada claim quedó etiquetado `[F]/[H]/[M]` y `(✓)/(decl)`, distinguiendo lo verificado-contra-fuente de lo declarado. Es la diferencia entre un *end* y un *coend* — la misma que separa `preserved` de `declared`, y la misma por la que, en esta cosecha, la mayoría coincidiendo en la lectura más débil nunca la volvió correcta.

> "La teoría de categorías no resuelve el alignment problem — pero da un lenguaje donde las preguntas se formulan con precisión suficiente para saber cuándo una respuesta es respuesta y cuándo es wishful thinking." — `urn:fxsl:kb:icas-safety-alignment`
