# Cierre de huecos del colímite — Formal Layer, procesos/risk-register y toolchain

**Fecha:** 2026-06-08
**Evaluador:** Claude (Opus 4.8) + skill `custodio-kora`, con dos subagentes de soporte (inventario de toolchain read-only; auditoría de procesos/risk-register).
**Objeto:** los tres huecos que la meta-evaluación 360° (`sintesis-meta-evaluacion.md` §6, §10.4) declaró sin cubrir a fondo.
**Método:** lectura directa de la Formal Layer oficial y de las dos specs, **verificada contra el toolchain vivo** (`kora check --strict` = 34/34; inventario del código de los 34 checks; `kora graph`/`kb-graph`) y contra el corpus. Cada afirmación está etiquetada `verificado-contra-fuente (✓)` o `declarado (decl)`. Este documento es el detalle de evidencia; la síntesis curada vive en `colimite-curado.md`.

> Estado vivo al cierre: `check --strict` 34/34 · `kb-graph` 689 nodos, 1179 aristas, **0 huérfanos**, 0 aristas rotas, 0 ciclos en `depends`.

---

## Parte A — Formal Layer oficial (el hueco más grave)

**Pregunta del encargo:** ¿los invariantes de auditoría (`06-audit-invariants`) y la preservación comportamental (`07-behavioral-preservation`) que la Formal Layer declara están **mecanizados, declarados o ausentes**? ¿Refutan o confirman el hallazgo central ("la deuda crítica es de verificación, no de diseño")?

**Veredicto:** lo **confirman y lo afilan**. La Formal Layer no solo *tiene* el diseño de las obligaciones de preservación: las **especifica formalmente al nivel canónico más alto**, con el criterio exacto (testigo de bisimulación bajo la interfaz declarada) que el check ausente tendría que computar. El hallazgo central pasa de "el diseño está presente" a "**el remedio del hallazgo central ya está escrito; solo falta mecanizarlo**".

### A.1 Qué declara la Formal Layer (las obligaciones)

`06-audit-invariants` (`urn:kora:kb:cat-audit-invariants`, v1.0.0, published):

- **§1.2** — `Audit: Artifact → Pos`, functor a valores de predicado, con poset de severidad `OK < LOW < MEDIUM < HIGH < CRITICAL`.
- **§2** — cuatro familias de invariantes: estructurales `S1–S3`, referenciales `R1–R3`, completitud `C1–C3`, **preservación `P1–P3`**.
  - **P1 (Constraint Preservation):** una migración `F: S → T` es aceptable solo si las restricciones preservadas y las intencionalmente perdidas son **ambas explícitas**.
  - **P2 (Behavior Preservation):** una transformación entre artefactos comportamentales es aceptable solo si la interfaz compartida se preserva y el comportamiento inducido **sigue siendo bisimilar o la divergencia se clasifica explícitamente**.
  - **P3 (Provenance Preservation):** todo dato/claim derivado tiene un **path de procedencia recuperable**.
- **§7 Teorema:** un corpus es *audit-stable* **iff** todos los artefactos satisfacen `R1–R3` globalmente **y** todo puente formal descriptivo↔operacional satisface `P1–P3`.

`07-behavioral-preservation` (`urn:kora:kb:cat-behavioral-preservation`, v1.0.0, published):

- **§1** — artefacto comportamental = F-coalgebra `c: U → F(U)`; preservación se juzga solo por la acción observable de `F`.
- **§3.2 Teorema (criterio de preservación):** una migración `m: U1 → U2` preserva comportamiento **iff** los estados iniciales están relacionados por una bisimulación o ambos colapsan al mismo elemento de la coálgebra final.
- **§3.3 Corolario:** una regresión comportamental es **precisamente un testigo de bisimulación fallido** bajo la interfaz declarada.
- **§8** — auditoría comportamental canónica: (1) fijar interfaz observable, (2) extraer coálgebras, (3) enunciar la migración, (4) **probar bisimulación o reportar trazas de divergencia concretas**, (5) clasificar la divergencia.

### A.2 Mapa de mecanización (mecanizado / declarado / ausente)

Cruzando cada invariante de `06` contra el inventario verificado de los 34 checks (Parte C):

| Invariante (Formal Layer) | Obligación | Check(s) del toolchain | Veredicto |
|---|---|---|---|
| §1.2 functor `Audit` + poset de severidad | `Artifact → Pos`, severidad ordenada | los 34 checks **instancian literalmente** el poset `LOW<MEDIUM<HIGH<CRITICAL` y emiten findings | **mecanizado (la maquinaria existe)** |
| S1 Identity | identidad por objeto | — (trivial en poset) | n/a automático |
| S2 Composition | `g∘f` bien-tipada | `coalgebra-conformance` (transiciones) | parcial |
| S3 Path equality | igualdades de caminos paralelos | — | **ausente** |
| R1 Internal resolution | refs internas resuelven | `lint-md`, `spec-traces` | parcial |
| **R2 External resolution** | URN → artefacto indexado | `urn-integrity` (HIGH) | **mecanizado** |
| R3 Fragment resolution | fragmento → ancla estable | `spec-traces`, `formal-trace-discipline` | parcial |
| C1 Schema completeness | declara objetos/morfismos requeridos | `autoria-conformance`, `agentfile-dimensions` | mecanizado (capa agéntica) |
| C2 Procedure completeness | proceso ejecutable expone su procedimiento | — (`procesos-spec §6` declara 8 checks; **0 existen**) | **ausente** |
| C3 Topology completeness | componentes obligatorios de la topología | `skill-structure`, `bundle-coherence` | parcial |
| **P1 Constraint preservation** | preservadas + pérdidas explícitas | `transmute` escribe el record; schema §6.3 valida **forma**, no **verdad** | **declarado, no verificado** |
| **P2 Behavior preservation** | bisimilar o divergencia clasificada | **ninguno**; `coalgebra-conformance` solo FSM + terminación + cierre de safety, **no bisimulación** | **ausente** |
| **P3 Provenance preservation** | path de procedencia recuperable | `provenance` en frontmatter; sin check de recuperabilidad del path | parcial |

**Lectura del mapa:** la mecanización viva cubre con solidez la columna **referencial** (R2 = `urn-integrity`, ciclos = `kb-graph-cycles`) y buena parte de la **estructural/completitud agéntica**. La columna que queda **declarada o ausente es exactamente la de preservación (P1–P3)** — la que el hallazgo central nombra.

### A.3 FL-1 — el titular: la Formal Layer confirma y *localiza* el check faltante `[F] (✓)`

El `_transmutation.yml` canónico (transmutation-spec §6.1) declara `bisimulation_claim: "equivalent-modulo-projections"` y `xi_naturality: status: declared, evidence: "requires runtime review"`. Eso es, palabra por palabra, la obligación **P2 / §3.2**: probar una bisimulación (módulo la proyección de interfaz) o clasificar la divergencia. La Formal Layer **ya escribió el criterio** que el check ausente debe computar (07 §3.2 + procedimiento §8). Por tanto:

> El hallazgo central no es solo "diseño presente, verificación ausente". Es: **la especificación formal del verificador faltante ya existe en la capa canónica**; la deuda es de implementación, no de diseño ni de definición. Esto es más fuerte que lo que cualquiera de las 8 auditorías afirmó (ninguna abrió la Formal Layer).

### A.4 FL-2 — el functor de auditoría está parcialmente mecanizado `[F] (✓)`

`06 §1.2` define la auditoría como functor a un poset de severidad. El toolchain **es una realización parcial de ese functor**: cada uno de los 34 checks tiene severidad en `{LOW, MEDIUM, HIGH, CRITICAL}` y emite findings — el poset de `06` no es metáfora, es la escala de severidad implementada. La fracción mecanizada mapea limpiamente a los invariantes **no-preservacionales**.

### A.5 FL-3 — el gap preciso, vía el propio teorema de `06` `[F] (✓)`

Por `06 §7`, un corpus es audit-stable **iff** `R1–R3` globalmente **y** los puentes descriptivo↔operacional satisfacen `P1–P3`. Estado verificado:

- `R1–R3`: **mecanizados** (urn-integrity HIGH; kb-graph 0 aristas rotas, 0 ciclos). KORA es **referencialmente audit-stable**.
- `P1–P3`: P1 **solo declarado**, P2 **ausente**, P3 **parcial**. KORA **no es preservation-audit-stable**.

> La "deuda de verificación" de la meta-evaluación queda **relocalizada con precisión spec-anclada**: son los checks `P1-verdad`, `P2-bisimulación` y `P3-provenance-path`, nombrados por la Formal Layer. No es una deuda difusa; es una lista de tres obligaciones formales sin contraparte ejecutable.

### A.6 FL-4 — drift de anclaje (hallazgo NUEVO que ninguna auditoría tuvo) `[F] (✓)`

Las specs que **hacen** las afirmaciones de preservación **no trazan a la Formal Layer que las formaliza**:

- `transmutation-spec` ancla su preservación a `urn:fxsl:kb:icas-preservacion` — el corpus **auxiliar** `fxsl/cat`, **no** al oficial `07-behavioral-preservation`. (Único cite categorial en su frontmatter: línea 22.)
- `harness-spec` y `autoria-spec`: **sin traza** a la Formal Layer.
- Quienes sí citan `06/07`: `procesos-spec` (deprecada/zombie), `agent-skill-construction-spec` (archivada), `risk-register-spec` y `multiagente-spec`.

Por la regla de Formal Layer de `CLAUDE.md`: `fxsl/cat` es corpus auxiliar (solo `Rationale:`/apoyo); `Traces to:` debe apuntar a la Formal Layer oficial. `transmutation-spec` ancla su obligación de preservación al corpus auxiliar y **puentea la capa oficial que existe justamente para formalizarla**.

Esto **generaliza el Frente 2** (drift `harness-spec ↔ Formal Layer` sobre PMI×LFS) a un **patrón sistémico de las specs núcleo**: la Formal Layer oficial está viva y bien conectada (kb-graph 0 huérfanos; 23 refs entrantes a cada uno de 06/07), pero las specs cuyas obligaciones formaliza anclan al corpus auxiliar. **El drift es de anclaje, no de orfandad.**

> Remediación: re-anclar `transmutation-spec`/`harness-spec`/`autoria-spec` a la Formal Layer oficial **pertenece al Frente 2 (HITL)**; `harness-spec` está en freeze y `transmutation-spec` es núcleo. Este documento **registra** el hallazgo; **no edita** esas specs.

### A.7 No-hallazgos y honestidad de alcance

- `06/07` **no son huérfanas** (kb-graph: 0 huérfanos totales; 23 refs entrantes c/u). FL-4 es drift de anclaje, no orfandad.
- **No** rederivé pruebas de bisimulación ni verifiqué comportamiento de runtime; verifiqué el **mapeo obligación↔check** y el estado `declared/preserved` del record, no que las leyes se cumplan en el target.

---

## Parte B — `procesos-spec` y `risk-register-spec`

### B.1 `ontology/procesos-spec.md` — **zombie honesta en sí, deshonesta en quien la cita**

`status: deprecado` confirmado (frontmatter línea 9; catálogo). gobernanza §13.2 la reconoce deprecada, "contenido válido pero no canon vigente, sin clientes mecánicos". Su propio frontmatter está bien hecho. El defecto es **externo**:

- **[ALTO] `(✓)` — `harness-spec` (viva, en freeze, máxima precedencia ontológica) presenta tres specs no-canónicas como functores-proyectores vivos.** Evidencia verificada por mí: `harness-spec.md:21` la declara en `depends`; `harness-spec.md:348` (§10.2) lista, como specs que "definen functores `T_R: Espacio → Ideal_R`":
  - `procesos-spec` → **deprecada** (`status: deprecado`).
  - `gemini-runtime-extension` y `mastra-runtime-extension` → **archivadas** (gobernanza §8.4).
  
  Una spec **viva-y-congelada** de precedencia máxima depende de / presenta-como-viva una spec deprecada y dos archivadas. **Ningún check lo captura:** `urn-integrity` pasa porque los tres URNs resuelven; no existe un check "`depends` de spec publicada no debe apuntar a `status: deprecado`/archivado". La meta-evaluación previa no lo registró porque mirar `procesos-spec` en aislamiento da "deprecada honesta" — el defecto solo aparece al cruzar hacia **quién la cita**. `[F] (✓)`. Fix: **spec-fix** en `harness-spec §10.2` (reclasificar como referencias históricas) — pero harness está en freeze ⇒ **HITL / coordinar con Frente 2**. Alternativa inmediata: **deuda-declarada**. No editar harness aquí.
- **[MEDIO] `(decl)` — §6 declara 8 checks de validación; 0 mecanizados.** `grep` de esos nombres en `toolchain/kora_lib/` = 0. Esperado para spec deprecada ("sin clientes mecánicos"), pero la tabla promete enforcement que nunca existió. Fix: ninguna acción / deuda-declarada.
- **[MEDIO] `[H/M]` — "9 procesos como funtores" es lenguaje heurístico con núcleo metafórico.** Las "categorías operativas" no definen morfismos ni identidades; llamar "funtor" a `Migrate` sin exhibir su acción sobre morfismos es falso-amigo parcial. Mitigante honesto: §5 "invariantes coinductivas" (idempotencia de `index`/`kb-graph`, estabilidad de `check`) sí es verificable en principio.

### B.2 `ontology/risk-register-spec.md` — **vigente, bien anclada, sin mecanización pese a tener datos reales**

`status: publicado` confirmado. Dependencias vivas y resolubles (`gobernanza`, `harness-spec`, `qa-spec` publicado, `autoria-spec`). Handshake H13 con `qa-spec` bidireccional y consistente (`qa-spec.md:257,342` ↔ `risk-register-spec.md:180-181`). `(✓)`.

- **[ALTO] `(decl)` — declara 5 checks de validación; 0 mecanizados, con data productiva real que los necesitaría.** `risk-register-spec.md:162-170` lista `risk-entry-shape`, `risk-id-unique`, `risk-floor-coherent`, `accepted-risk-owned`, `risk-vs-qa-floor` (todos "Enforcement: manual"). `grep` en `toolchain/kora_lib/` = 0. El único toque es `construction-risk-declared` (`checks.py:1961`), que solo verifica **presencia** de la clave (alternativa entre `invariantes`/`qa_budget`/`risk_register`), **no** shape, dominios `[0,1]`, unicidad de `risk_id`, ni los 5 componentes. **Agravante verificado:** existe `risk_register:` real en >10 agentes productivos (`fugaz`, `polymath`, `steipete`, `agent-architect`, `opm-specialist`, `allan-kelly`…). Un `risk_id` duplicado o un `likelihood: 1.5` **pasa los 34 checks limpio**. A diferencia de `procesos-spec`, esta spec **viva** promete enforcement sobre datos que ya existen. Fix: **check-fix** — `risk-id-unique` + `risk-entry-shape` son baratos y tienen data real que cubrir (ver backlog P0 del colímite).
- **[MEDIO] `[F] (✓)` — la estructura de mónada writer es formal y *legítima*, no falso-amigo.** `Risk_M(X) = X × RiskLedger`, `RiskLedger = List[RiskEntry]` (monoide libre), unit + composición Kleisli. Es la mónada escritor estándar; la estructura algebraica declarada **existe y es correcta** — de los pocos usos formales legítimos de la cosecha. Sutileza menor: el `meet=min` sobre `residual_sigma_floor` es estructura *adicional* sobre el writer (coherente con `qa-spec.md:97` que reserva `⊗` para compromisos), no parte del bind puro; es writer enriquecido, no Kleisli puro. Defecto de nomenclatura, no de estructura.

### B.3 Riesgo de coherencia no registrado por la meta-evaluación

El hallazgo **B.1 [ALTO]** (harness viva-en-freeze citando specs deprecada+archivadas como functores vivos) es una incoherencia cruzada de lifecycle que la meta-evaluación, al tocar estas specs "de refilón", **no había registrado** — y que **corrobora y localiza** el graft #2 de la cosecha (objetos zombie de v7-0608), llevándolo desde "specs deprecadas-no-retiradas" hasta "una spec **viva** de máxima precedencia las presenta como vivas".

---

## Parte C — Toolchain (código), no solo el texto de las specs

Inventario verificado contra el código de los 34 checks (`toolchain/kora_lib/checks.py`, ~2978 líneas; `transmute.py`; `graph.py`). Cierra el hueco "varios claims sobre el toolchain se afirmaron sin auditar el código". **Resultado neto: los claims del toolchain de la meta-evaluación se sostienen contra el código; los dos que calificó de falsos son, en efecto, falsos.**

| Claim de la meta-evaluación sobre el toolchain | Veredicto contra código | Evidencia |
|---|---|---|
| `relations-laws` ya verifica aciclicidad de `supersedes`/`refines` y antisimetría de `supersedes` ⇒ recomendar `refines-acyclic` es redundante | **CONFIRMADO** | `checks.py:577,593–656` (DFS 3-color para `supersedes`, `refines`; antisimetría) |
| `vector-laws` verifica las 5 leyes inter-eje | **CONFIRMADO** | `checks.py:1346–1404` (L1–L5) |
| `coalgebra-conformance` verifica FSM/safety pero **no** bisimulación | **CONFIRMADO** | `checks.py:2256,2206–2253` (inicial/terminales/targets ∈ estados, terminación, cierre de `sub_coalgebra_segura`) — sin bisimulación |
| Ningún check verifica `xi_naturality`/`safety_closure`/`kleisli_composition` | **CONFIRMADO (ausente)** | solo declarados en `transmute.py:259–271`; transmutation-spec §3.2 lo dice explícito ("hoy no existe un check de enforcement por-ley") |
| El toolchain **no** conflaciona `cites` con `depends` (borrador H1) | **CONFIRMADO falso el de borrador** | `graph.py:94–96`: aristas spec→spec son `XRef`; 0 `DependsOn`/`Cites` spec→spec |
| El `kb-graph` **no** incluye las specs como nodos (borrador H6/ac9) | **CONFIRMADO** | `kb-graph` itera solo `artifacts/knowledge/`; las specs de governance/ontology/serialization/runtime quedan fuera por **raíz de escaneo** (689 nodos, specs ausentes) |

**Leyes/invariantes que las specs DECLARAN y NINGÚN check verifica (lista cerrada):**

1. `xi_naturality` (transmutation-spec §3.2) — `status: declared`.
2. `safety_closure` (transmutation-spec §3.2) — `status: declared`.
3. `kleisli_composition` (transmutation-spec §3.2) — `status: declared`.
4. Bisimulación módulo proyecciones (transmutation-spec §5; Formal Layer 07 §3) — `bisimulation_claim` no verificado.
5. Invariantes de preservación `P1`(verdad)/`P2`/`P3` (Formal Layer 06 §2.4, §7) — sin contraparte mecánica.
6. Los 5 checks de `risk-register-spec §`-validación y los 8 de `procesos-spec §6` — declarados, inexistentes en el registro.

**Conclusión Parte C:** de las ~14 leyes/invariantes que el ecosistema declara como functoriales/preservacionales/coalgebraicas, el toolchain **mecaniza con rigor** las decidibles sobre dominio finito (5 leyes inter-eje, 3 leyes de relaciones, FSM+terminación+safety, integridad de URN) y deja **declaradas o ausentes** las de preservación functorial, bisimulación y preservación comportamental. El gap es exactamente el que la Formal Layer (Parte A) nombra.

---

## Tabla maestra — los tres huecos, cerrados

| Hueco (§6 / §10.4 de la síntesis) | Estado | Hallazgo headline | Efecto sobre el hallazgo central |
|---|---|---|---|
| Formal Layer oficial (06/07) | **cerrado** | P2/bisimulación es el check ausente **ya formalmente especificado**; KORA es referencialmente audit-stable pero no preservation-audit-stable (06 §7); + drift FL-4 | **CONFIRMA y AFILA** |
| `procesos-spec` / `risk-register-spec` | **cerrado** | harness viva-en-freeze cita 3 specs deprecada+archivadas como functores vivos [ALTO]; risk-register enforcement-gap sobre data real [ALTO] | añade 2 hallazgos nuevos no vistos por las 8 |
| Toolchain (código) | **cerrado** | claims del toolchain de la meta-eval verificados contra código; los 2 falsos confirmados falsos | sube los claims de toolchain de `(decl)` a `(✓)` |
