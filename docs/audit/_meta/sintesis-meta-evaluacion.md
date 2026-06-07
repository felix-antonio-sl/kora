# Síntesis 360° — Meta-evaluación categorial de 8 auditorías de las specs KORA

**Fecha:** 2026-06-08
**Evaluador:** Claude (Opus 4.8) + skill `cat-thinking`, vía workflow de 10 subagentes (8 evaluadores + alineador de claims + matriz N×N).
**Objeto evaluado:** las 8 auditorías categoriales depositadas en `docs/audit/`.
**Método:** rúbrica de 9 dimensiones ancladas a las 24 piezas del ICAS-BoK, con **verificación de los claims más fuertes de cada reporte contra las specs vivas** (`kora check --list`, `kora graph`, `_transmutation.yml`, el corpus). El peso de un hallazgo lo da la verificación contra la fuente, **no** el número de auditorías que lo afirman.

> Salidas de soporte (mismo directorio): `eval-<slug>.md` (8 evaluaciones en detalle), `claims-master.md` (alineación de claims), `matriz-nxn.md` (matriz relacional completa).

---

## 0 · Encuadre categorial de la propia meta-evaluación

Cada auditoría es un **functor** `Fᵢ : 𝐒 → 𝐂`, donde `𝐒` es la categoría de las specs KORA (objetos = specs; morfismos = `depends`/`cites`/`supersedes`) y `𝐂` el vocabulario categorial del ICAS-BoK. Evaluar la calidad de `Fᵢ` es medir cuán **fiel y pleno** es ese functor (`urn:fxsl:kb:icas-preservacion`): una buena auditoría preserva la estructura de las specs **y declara lo que pierde**; una mala colapsa todo a "todo correcto" (el functor constante, máximamente infiel).

- La **rúbrica de 9 dimensiones** es un *functor de medición* `Q : 𝐀𝐮𝐝 → [0,5]⁹` (`urn:fxsl:kb:icas-calidad-riesgo`): mide cada auditoría sobre nueve ejes y los compone en un retículo de calidad.
- La **comparación N×N** estudia las *transformaciones naturales* `α : Fᵢ ⇒ Fⱼ` (`urn:fxsl:kb:icas-comparacion`): dónde dos auditorías son casi la misma lectura (`concuerda`), dónde una contiene a la otra (`subsume`), dónde divergen y dónde ni siquiera comparten dominio (`ortogonal`).
- El **consenso** es el *límite* del diagrama de auditorías; la **cobertura** es el *colímite* (`urn:fxsl:kb:icas-universales`).

Con una advertencia que resultó ser el hallazgo central (§9): cuando los functores comparten el mismo *prior*, el límite no gana valor probatorio.

---

## 1 · Veredicto del conjunto

El corpus de 8 auditorías es, en promedio, **sólido pero no autosuficiente**. Hay **una** auditoría ejemplar (`deep`, 44/45), un **pelotón sólido y mutuamente complementario** de seis (39→32), y **un control negativo** (`gemini`, 14/45) que no audita las specs sino el sistema.

Tres conclusiones gobiernan la lectura:

1. **La calidad se concentra en la disciplina, no en la jerga.** Las dimensiones más fuertes del conjunto son *anclaje* (4.12) y *fidelidad* (3.88); las más débiles son **poder diagnóstico (3.25)** y **corrección de leyes (3.38)** y **coherencia interna (3.38)**. Es decir: el conjunto sabe *citar* y *traducir*, pero flojea en *hallar fallas reales*, en *que sus afirmaciones categóricas sean correctas* y en *no contradecirse a sí mismo*. La forma está por delante del fondo.

2. **El consenso es real pero su unanimidad es un artefacto de método** (§9). 7 de 8 corren la misma skill `cat-thinking` sobre el mismo corpus; convergen por construcción. El valor de los hallazgos compartidos viene de la verificación contra `_transmutation.yml` y `kora check`, no del recuento de afirmantes.

3. **Las auditorías cometen, a veces, el mismo pecado que denuncian.** El hallazgo unánime es "las specs *declaran* functores/adjunciones sin *verificar* las leyes". Pero varias auditorías *declaran* "esto es una adjunción / es faithful / es Formal" sin verificar las leyes — y lo hacen citando el corpus que lo prohíbe. La auditoría es un espejo del defecto auditado.

---

## 2 · Ranking y scores

Dimensiones: `fid` fidelidad functorial · `ley` corrección de leyes · `f/h` formal-vs-heurístico · `anc` anclaje/trazabilidad · `cob` cobertura · `dia` poder diagnóstico · `acc` accionabilidad · `par` parsimonia · `coh` coherencia interna.

| # | Auditoría | fid | ley | f/h | anc | cob | dia | acc | par | coh | **TOT** | Veredicto |
|---|-----------|----|----|----|----|----|----|----|----|----|--------|-----------|
| 1 | **deep** | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | **44** | ejemplar |
| 2 | report-b1e84abd | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 3 | **39** | sólido |
| 3 | report-a3f7c2e1 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | **35** | sólido |
| 4 | borrador-claude | 4 | 2 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | **34** | sólido |
| 5 | v6 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | **33** | sólido |
| 6 | v7-0608 | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | **32** | sólido |
| 7 | v7-0607 | 3 | 4 | 3 | 4 | 4 | 2 | 4 | 4 | 4 | **32** | sólido |
| 8 | **gemini** | 2 | 3 | 1 | 2 | 1 | 0 | 0 | 2 | 3 | **14** | deficiente |

El salto `deep (44) → resto (≤39)` es de 5 puntos: `deep` no es "el mejor del montón", es de otra liga. El salto `pelotón (≥32) → gemini (14)` es de 18 puntos: `gemini` no es comparable en la misma escala (es ortogonal de dominio, §4).

---

## 3 · Lectura categorial de cada auditoría (qué tipo de functor es)

- **deep — functor fiel y pleno.** Único veredicto *ejemplar*. Separa formal/heurístico/metafórico como eje vertebral (no como decoración), ancla con URN + número de línea, hizo 5 verificaciones y **no cometió un solo claim falso**. Sus dos únicas debilidades son de *cobertura declarada* (no abrió la Formal Layer oficial ni 7 de las specs periféricas) — y las **declara transparentemente**, que es justo lo que `icas-preservacion` exige de un functor honesto. Es el modelo.
- **report-b1e84abd — functor fiel con una arruga de coherencia.** La mejor del resto. Su tesis central ("el gap es de verificación, no de diseño"; `ξ_naturality` como deuda citada verbatim) se confirma contra la fuente. Lastrada por **una contradicción interna**: F1 cita `relations-laws` como verificador de las leyes de relaciones, pero D11 afirma que falta un check de aciclicidad de `refines` — que `relations-laws` ya hace.
- **report-a3f7c2e1 — functor sólido con un punto no bien-definido.** Hallazgo crítico verdadero (H7: matriz de preservación `status:declared`) y accionabilidad ejemplar. Cae por un **hallazgo fabricado** (H8: "§10 sugiere que la composición podría no ser asociativa" — `grep asociativ` = 0 en toda la spec) y un falso-amigo en su propia prosa (§3.2 tipa una restricción reticular `Π≥3 ⇒ Μ≥1` como "transformación natural").
- **borrador-claude — functor de anclaje y scope ejemplares, con el dato bandera mal contado.** Único que recorre los morfismos (`depends`/`cites`/`supersedes`), 23 docs incluidas deprecadas y un namespace foráneo. Pero su hallazgo estrella es **falso por aritmética**: afirma "2/8 leyes preservadas" cuando el `_transmutation.yml` canónico tiene 5 preserved / 3 declared; y se **autocontradice** (H1: "el toolchain trata `cites` como `depends`" vs H6: "las specs ni siquiera están en el grafo").
- **v6 — functor genuino con tres falsos-amigos.** Halla la falla estructural más fuerte de toda la cosecha (A15: la matriz §6 de `autoria-spec` organizada por `forma_material` contradice la doctrina v2.0 "arnés = discriminante"). Pero conflaciona `faithful` con "preserva monomorfismos" (A13), `sección` con "adjunto izquierdo" (A2), y **sobre-formaliza `F⊣U` como "Formal" contra la advertencia explícita del corpus que cita**.
- **v7-0608 — functor honesto con la cifra invertida.** Tesis correcta y único que audita las specs como **artefactos con ciclo de vida** (objetos zombie: `canario`/`procesos` deprecadas-no-retiradas; `hermes` stub). Pero invierte el dato bandera (dice "5 declared / 3 preserved"; es al revés) y cuenta `gemini`/`mastra` como runtimes canónicos cuando están archivados.
- **v7-0607 — functor disciplinado pero sin dientes.** Cobertura amplia (8 specs), sin falsos-amigos groseros, parsimonioso. Su falla es el **poder diagnóstico (2)**: 0 críticas y un checklist de 14 "✅ satisfecha" cuya evidencia es *una sección de spec* — confunde lo que la spec **declara** con lo que **cumple**, deslizándose hacia el functor constante.
- **gemini — el functor constante.** No audita las specs: audita "la arquitectura/sistema KORA", **no cita un solo archivo de spec**, no halla un solo defecto, marca todo el checklist en "Sí" e **inventa estructura** (`U = U_phen × U_ctx × U_epi × U_sta`, inexistente: `grep` = 0 en el corpus y en `harness-spec`). Es el anti-patrón Goodhart en estado puro (§9).

---

## 4 · Comparación N×N

Distribución de las 28 relaciones: **complementa 12 · ortogonal 7 · concuerda 4 · subsume 3 · diverge 2**.

Cuatro lecturas categoriales de la matriz:

1. **Los 7 pares `ortogonal` son exactamente los 7 que incluyen a `gemini`.** No es que `gemini` sea peor *en el mismo eje*: vive en otra categoría de dominio (`dom(F_gemini) ≠ 𝐒`). No existe transformación natural posible hacia/desde las demás porque audita otro objeto. Es un error de *scope*, no de grado.
2. **`deep` `subsume` a v6, v7-0607 y v7-0608** (las cubre y supera con mayor rigor) y **`concuerda` con b1e84abd**: las dos de mayor calidad son casi una transformación natural identidad — convergen en "el gap es de verificación, no de diseño".
3. **`deep` `diverge` de borrador y de a3f7c2e1** en el punto caliente (`Lift_R ⊣ T_R`): mismo objeto, lectura distinta. Aquí `deep` tiene razón (§7), y es la divergencia más productiva del conjunto.
4. **El grueso es `complementa` (12):** las auditorías de specs cubren sub-zonas distintas de `𝐒`. Esto es lo que habilita la recomendación del colímite curado (§10): se pueden **pegar**.

**Clusters de similitud:**
- **A — "el gap es de verificación"** `{deep, b1e84abd, a3f7c2e1, v7-0608}`: alta calidad, lectura convergente, anclada al corpus.
- **B — "functorial honesto con resbalón de ejecución"** `{v6, borrador-claude}`: genuinas y bien ancladas, cada una con un defecto que toca lo central.
- **C — "cobertura amplia, temple variable"** `{v7-0607, v7-0608}`: mismo nombre "v7" y misma skill, **distinto productor** (v7-0607 = OpenCode/kimi; v7-0608 = cat-thinking/Claude) — no son iteración una de otra.
- **D — outlier de scope** `{gemini}`.

---

## 5 · Consenso robusto (el límite) — con advertencia

Lo que afirman casi todas **y se sostiene contra la fuente**:

1. **La deuda crítica de KORA es de *verificación mecánica*, no de diseño.** `ξ_naturality`, `safety_closure`, `kleisli_composition` están `declared` (no `preserved`) y **ningún check las verifica**; el `preserved` del resto es palabra del autor, no enforcement.
2. `T_R` está definido sobre **objetos** (matriz de proyección) pero no verificado sobre **morfismos** (naturalidad de Ξ).
3. **`PMI × LFS` es un poset/retículo finito**, no una categoría con morfismos ricos.
4. El **axioma de agencia** (Π = free monad, Μ = cofree comonad, Ξ = ley de interacción) es formal y fiel a `icas-agencia`.
5. La distinción **`preserved`/`declared`** del `_transmutation.yml` es el activo de integridad intelectual de KORA y debería extenderse a todas las specs.
6. **Las specs *mismas* no cometen falsos-amigos groseros.** Los falsos-amigos aparecen en los **auditores**, no en el objeto auditado.

> **Advertencia (§9):** este "consenso" es en buena parte correlación de instrumento. Cada punto está marcado *verificado contra la fuente* porque ahí — y no en el recuento — reside su valor.

---

## 6 · Cobertura (el colímite) y sus huecos

La **unión** de lo auditado cubre casi todo el estrato Spec: `transmutation` (matriz preserved/declared, naturalidad Ξ, Galois, bisimulación módulo pérdida), `harness` (poset PMI×LFS, 5 leyes inter-eje, axioma de agencia, Σ como retículo), `autoria` (Yoneda/`api_observable`, arnés-vs-forma_material, shape coalgebraico), `knowledge` (DAG/poset/preorden/cíclico de las relaciones), `gobernanza` (4 capas como fibración, precedencia como preorden), `qa` (`V_QA` monoidal, `ιΣ` cambio de base), `multiagente` (sheaf, sitio faltante, 2-categoría).

**Huecos del colímite — lo que *nadie* cubrió a fondo:**
- La **Formal Layer oficial** (`artifacts/knowledge/kora/categorical-foundations/`), en particular `06-audit-invariants` y `07-behavioral-preservation`, que **refutarían o confirmarían el hallazgo central** sobre verificación de leyes. Es la omisión más grave del conjunto.
- `procesos-spec` y `risk-register-spec` (tocadas de refilón).
- **El toolchain mismo** (el código): varios claims sobre qué hace o deja de hacer el toolchain se afirman sin auditar el código — y dos resultaron falsos (§7).

---

## 7 · Contradicciones entre reportes, resueltas contra la fuente

Todas se dirimen **contra la spec viva**, no por mayoría:

| Tema | Lado correcto | Veredicto |
|------|---------------|-----------|
| Cifra de la matriz de preservación | **5 preserved / 3 declared** (deep, b1e84abd, a3f7c2e1) | borrador ("2/8") y v7-0608 ("5 declared/3 preserved") **erran**; ambos inflan su hallazgo bandera con cifra falsa |
| `Lift_R ⊣ T_R`: ¿adjunción Formal o conexión de Galois? | **Conexión de Galois sobre el retículo** (deep) | En un poset (hom-sets ≤ 1) `Lift∘T ≤ id` *es* una conexión de Galois. v6/v7-0608/gemini la marcan "Formal" sin probar identidades triangulares, contra el corpus que citan |
| Koraficación `faithful` = ¿preserva monos? | **No** (deep, b1e84abd, v7-0607) | `faithful` = inyectividad sobre hom-sets ≠ preservar monos. v6 conflaciona (A13) y se autocontradice |
| ¿El toolchain conflaciona `cites` con `depends`? | **No** | Las aristas spec→spec son XRef (67), 0 `DependsOn`/`Cites`; el kb-graph ni siquiera incluye las specs. borrador se autocontradice (H1 vs H6) |
| ¿Falta un check `refines-acyclic`? | **No** | `relations-laws` (HIGH) ya verifica "supersedes/refines acyclic". b1e84abd se autocontradice (F1 vs D11) |
| ¿El cambio de base Σ es functorial? | **Sí** | `qa-spec` ya declara `ιΣ : {0,1,2,3}⁵ → [0,1]⁵` monótona = functor. v7-0608 reporta un gap inexistente |
| ¿Qué es "auditar las specs"? | **Las specs como ley**, no el sistema | `gemini` audita el sistema, no nombra una sola spec |
| Atlas "ortogonales": ¿harness o autoria? | **`autoria-spec §4.5`** (harness §5 dice "complementarios") | v6 mal-atribuye la cita (el hallazgo de fondo es correcto; la cita, no) |

---

## 8 · Los seis anti-patrones de auditoría categorial (patrones meta)

Destilados de los errores transversales — son la lista de control para producir o revisar una auditoría categorial:

1. **Sobre-formalización** — marcar "Formal/teorema/cumplida" una adjunción sin verificar las identidades triangulares (v6, v7-0608, gemini). Agravante: lo hacen **citando `icas-adjunciones`, que advierte que free/forgetful aplicado "rara vez es una adjunción exacta"**.
2. **Declarado ≠ cumplido (deriva al functor constante)** — tomar la *declaración* de una ley en la spec por su *enforcement* (checklist de ✅ en v7-0607 y v7-0608; total en gemini). Es el deslizamiento hacia el functor constante "todo bien".
3. **Error de conteo del dato bandera** — el dato más fuerte del repo (`preserved`/`declared`), mal leído: borrador (2/8) y v7-0608 (invertido). Un hallazgo cuantitativo falso contamina la conclusión que sostiene.
4. **Hallazgo fabricado / fantasma** — inventar un defecto que no existe en el dominio (a3f7c2e1 H8 asociatividad; v7-0607 T6 ya en §6.3; v7-0608 C4 ya en qa-spec; borrador H1). Categorialmente: el functor *no está bien definido*, mapea un objeto del dominio que no existe.
5. **Contradicción interna** — dos caminos del argumento que no conmutan (b1e84abd F1/D11; borrador H1/H6; v6 A5/A12; v7-0608 anexo/cuerpo). Es falla de coherencia del propio functor.
6. **Falsos-amigos** — `faithful`=preserva-monos, `sección`=adjunto-izquierdo, restricción reticular=transformación natural, `gobernanza`=terminal+counit+functor-constante a la vez. La disciplina exacta que `cat-thinking` predica, violada por quienes la invocan.

---

## 9 · El meta-hallazgo central (en tres capas)

**(A) La auditoría como espejo / punto fijo.** El defecto que el conjunto denuncia unánimemente — *"declarar estructura categorial sin verificar las leyes"* — es el que la mayoría comete (anti-patrones 1 y 6). La calidad de una auditoría categorial se mide por **el mismo criterio que ella aplica a su objeto**: ¿verifica sus claims contra la fuente o solo los declara? Es una auto-aplicación. Solo `deep` (y casi `b1e84abd`) la pasan.

**(B) Consenso ≠ verdad (sesgo de método).** 7 de 8 ejecutan la misma skill `cat-thinking` sobre el mismo corpus: el prior ("busca la lectura más débil, distingue formal/heurístico, ancla a URN, no cometas falsos-amigos") los hace **converger por construcción**. El límite de un diagrama casi-constante no añade evidencia. Prueba viva: cinco reportes leen `Lift_R ⊣ T_R` como "adjunción lax declarada"; **solo `deep`, con la misma skill, rompe el patrón** y la diagnostica como conexión de Galois — y tiene razón. *La mayoría coincidiendo en la lectura más débil-pero-imprecisa no la vuelve correcta.*

**(C) End vs coend** (`urn:fxsl:kb:icas-safety-alignment`). "7 lo dicen" es un **coend** (∃ muchos afirmantes); "es verdad" requiere un **end** (∀, contra la fuente). Pesar por consenso es confundir coend con end — el mismo error categorial que las auditorías cometen sobre las specs cuando confunden `declared` (∃ una declaración) con `preserved` (∀, verificado). Y `gemini` es el **reward hacking como functor infiel** del §95 del corpus: optimizó el proxy *"parecer una auditoría categorial rigurosa"* (jerga + checkmarks) y dejó vacío el goal *"detectar fallas estructurales"*. La defensa que el corpus prescribe —*hacer el functor más faithful añadiendo señales discriminantes*— es exactamente lo que hacen la rúbrica de 9 dimensiones y la verificación contra la fuente.

---

## 10 · Recomendación: el colímite curado

No hay que elegir *una*; hay que **pegar** (el conjunto es mayormente `complementa`). Pero el pegado debe ser curado contra la fuente, no una unión ingenua.

1. **Base canónica: `deep`.** Única ejemplar, internamente coherente, 0 falsos-amigos, la lectura correcta de Galois. Es el cono base.

2. **Injertar los claims únicos valiosos** (cada uno rompe la naturalidad pero se sostiene — son las secciones locales del colímite que solo un auditor vio):
   - **v6** → la matriz §6 de `autoria-spec` por `forma_material` vs arnés-discriminante (la falla estructural más fuerte; v6 la graduó HIGH, v7-0607 la sub-graduó BAJA — v6 tiene razón).
   - **v7-0608** → objetos zombie (`canario`/`procesos` deprecadas-no-retiradas; `hermes` stub): la única lectura de *ciclo de vida*.
   - **v7-0607** → staleness de `autoria-spec §16.1` (ejemplo anclado a la familia `atomic` y al productor `atomize`, ambos retirados).
   - **b1e84abd** → enforcement levels como clasificador de subobjetos Ω del topos donde vive el sheaf de `multiagente` (conecta dos specs vía el corpus).
   - **borrador-claude** → `salubrista-openclaw` en el namespace foráneo `agengai` sin ADR + el sitio del sheaf faltante.

3. **Corregir antes de canonizar** (los errores falsables ya identificados): cifra **5 preserved / 3 declared** (no 2/8 ni invertida); **eliminar** la recomendación `refines-acyclic` (ya existe en `relations-laws`); **eliminar** el gap de cambio-de-base Σ (ya existe `ιΣ`); **eliminar** H8 (asociatividad, fabricado); **corregir** la atribución del término "ortogonal" (autoria §4.5, no harness §5).

4. **Completar los huecos del colímite**: abrir la **Formal Layer oficial** (`06-audit-invariants`, `07-behavioral-preservation`) — refuta o confirma el hallazgo central; auditar `procesos`/`risk-register`; y auditar el **toolchain (código)**, no solo el texto de las specs.

5. **Aplicarse la propia medicina.** La recomendación que el consenso hace a KORA — *un perfil de cumplimiento `(ley, status: preserved|declared|verified-by-check)` por spec* — debe aplicarse **a la auditoría misma**: cada hallazgo etiquetado `formal | heurístico | metafórico` y `verificado-contra-fuente | declarado`. Eso es lo que `deep` ya hace y lo que convierte una auditoría en un *end* (verificación) en vez de un *coend* (opinión).

---

## 11 · Cierre

> "La teoría de categorías no resuelve el alignment problem — pero da un lenguaje donde las preguntas se formulan con precisión suficiente para **saber cuándo una respuesta es respuesta y cuándo es wishful thinking**." — `urn:fxsl:kb:icas-safety-alignment`

Esa frase es el criterio de toda esta cosecha. `deep` es una respuesta. `gemini` es wishful thinking. Las seis del medio son respuestas con un defecto falsable cada una — valiosas precisamente porque sus errores **son corregibles contra la fuente**. La auditoría categorial definitiva de KORA no es ninguna de las ocho: es `deep` endurecida con cinco injertos verificados y tres huecos cerrados.
