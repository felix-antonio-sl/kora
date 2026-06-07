# Auditoría Categorial de las Specs de KORA

**Generado por:** Skill `cat-thinking` (Pensamiento Categorial)
**Fecha de Evaluación:** 2026-06-07
**Framework de Referencia:** ICAS-BoK (24 URNs, corpus `urn:fxsl:kb:icas-*`)
**Alcance:** `gobernanza.md`, `harness-spec.md`, `qa-spec.md`, `autoria-spec.md`, `transmutation-spec.md`, `multiagente-spec.md`, `md-spec.md`
**Estado del repo:** `kora check --strict` = 34/34 ✅

---

## Resumen Ejecutivo

KORA es un sistema de ingeniería que **usa teoría de categorías como vocabulario de diseño**, no como formalismo verificado en todas sus partes. Esto no es una debilidad en sí mismo — es una decisión de arquitectura. El problema detectado es que el ecosistema de specs **no distingue sistemáticamente** entre lo que es formal (teorema o construcción verificable), lo que es heurístico (analogía útil, dirección correcta), y lo que es metafórico (vocabulario categorial sin estructura subyacente). Esta auditoría mapea esa distinción spec por spec.

De 10 claims categoriales mayores evaluados:

| Tipo | Cantidad |
|------|----------|
| **Formal** (construcción verificable, anclada al corpus) | 5 |
| **Heurístico de alta calidad** (dirección correcta, falta verificación o pieza) | 3 |
| **Metafórico** (vocabulario categorial sin estructura categorial subyacente) | 2 |

---

## 1. El Axioma Fundamental — `harness-spec §2`

**Claim**: `Artefacto = (m_p × c_q × Ξ) ⋉ (Contexto)` donde `m_p` es free monad (plan), `c_q` es cofree comonad (materia), `Ξ` es la ley de interacción Libkind-Spivak, y `⋉` es "producto semidirecto".

**Anclaje al corpus**:

La tripleta `(m_p, c_q, Ξ)` está sólidamente anclada en `urn:fxsl:kb:icas-agencia` (14-agencia.md:68-70), que cita directamente el resultado de Libkind-Spivak:

```
Ξ_{p,q} : m_p ⊗ c_q → m_{p⊗q}
```

- Free monad como árbol de decisión finito: `urn:fxsl:kb:icas-agencia` §"Free monad: el arbol de decisiones" (líneas 36-52). Construcción por inducción transfinita, isomorfismo `m_p ≅ y + p ◃ m_p`, leyes de mónada exhibidas.
- Cofree comonad como árbol de comportamiento infinito: `urn:fxsl:kb:icas-agencia` §"Cofree comonad: el arbol de comportamiento" (líneas 58-62). Construcción coinductiva, counit y comultiplicación exhibidas.
- Ley de interacción: `urn:fxsl:kb:icas-agencia` §"La ley de interacción" (líneas 66-76). Transformación natural exhibida, ejemplo canónico de la entrevista.

**Problema detectado — el operador `⋉`**:

En teoría de categorías, el producto semidirecto es una construcción algebraica sobre grupos o monoides donde uno actúa sobre el otro vía un homomorfismo de acción. La spec lo usa como metáfora para "el contexto modula la tripleta sin sustituirla". No hay:

- Definición de qué categoría algebraica soporta el `⋉`.
- Definición de la acción de Contexto sobre la tripleta.
- Leyes de compatibilidad entre la acción contextual y las leyes de mónada/comónada de `(m_p, c_q)`.

El `⋉` es una **conveniencia notacional** que captura una intuición correcta (el contexto modula, no reemplaza) pero no tiene respaldo en construcción categorial estándar.

**Veredicto**: `[Formal + Heurístico]`
- La tripleta `(m_p, c_q, Ξ)` es **formal** (anclada en corpus, leyes verificables).
- El `⋉` es **heurístico** (metáfora de modulación contextual, sin construcción categorial que lo respalde).

**Recomendación**: Reemplazar `⋉` por notación explícita de fibración o producto cartesiano con proyección, y declarar explícitamente que "contexto modula sin sustituir" es una restricción de diseño, no una construcción categorial. Alternativa: modelar el contexto como fibra sobre la tripleta vía fibración de Grothendieck (`urn:fxsl:kb:icas-extension`).

**Citas**: `urn:fxsl:kb:icas-agencia` §"La ley de interacción"; `urn:fxsl:kb:icas-extension` (fibraciones).

---

## 2. El Espacio Ontológico PMI × LFS — `harness-spec §3-4`

**Claim**: 6 ejes, cada uno es un retículo (poset con join y meet). El espacio total es "producto reticular con estructura de producto semidirecto". Hay leyes de consistencia inter-eje. Los morfismos son elevación (join) y proyección (meet).

**Mapeo de ejes al corpus**:

| Eje | Estructura formal | Corpus primario |
|-----|-------------------|-----------------|
| Π (Plan) | free monad `m_p` | `urn:fxsl:kb:icas-agencia` |
| Μ (Materia) | cofree comonad `c_q` | `urn:fxsl:kb:icas-agencia`, `urn:fxsl:kb:icas-tiempo` |
| Ξ (Interacción) | NT `Ξ: m_p ⊗ c_q → m_{p⊗q}`, lente polinomial | `urn:fxsl:kb:icas-agencia`, `urn:fxsl:kb:icas-interaccion` |
| Λ (Nivel) | fibración de Grothendieck | `urn:fxsl:kb:icas-escala` |
| Φ (Acoplamiento) | pullback humano×AI | `urn:fxsl:kb:icas-agencia` |
| Σ (Ético) | vector enriched sobre [0,1]^5 | `urn:fxsl:kb:icas-enriquecimiento`, `urn:fxsl:kb:icas-calidad-riesgo` |

**Lo que funciona — estructura de retículo**:

Cada eje es un conjunto totalmente ordenado finito (Π∈{0,1,2,3}, Μ∈{0,1,2,3}, Ξ∈{0,1,2,3,4}, Λ∈{0,1,2,3}, Φ∈{0,1,2,3,4}). Un conjunto totalmente ordenado finito es un retículo (join = max, meet = min). El producto de retículos es un retículo. Los morfismos del espacio como join (elevación) y meet (proyección) son correctos. Hasta aquí, **formalmente sólido**.

**Lo que funciona — leyes inter-eje**:

Las 5 leyes de consistencia inter-eje (§4.1) son restricciones de implicación sobre el dominio discreto: `Π≥3 ⟹ Μ≥1`, `Ξ=4 ⟹ Λ≥1`, `Φ≥2 ⟹ Μ≥1`, `Σ.accountability≥2 ⟹ Σ.transparency≥2`, `Λ=3 ⟹ Σ.i≥2 ∀i`. Son formalmente verificables. El toolchain las verifica vía `kora check --strict` (checks `pi-mu-consistency`, `xi-composition-consistency`, `phi-memory-consistency`, `sigma-accountability-transparency`, `lambda-societal-sigma`).

**Problema detectado — "producto semidirecto" nuevamente**:

La descripción del espacio total como "producto reticular con estructura de producto semidirecto" (gobernanza §1, harness-spec §3) repite el problema del `⋉`. No hay definición de una acción de los ejes LFS sobre los ejes PMI que justifique "semidirecto" en sentido algebraico. Las leyes inter-eje son restricciones estáticas de compatibilidad, no una acción de un grupo/monoide sobre otro.

**Veredicto**: `[Formal + Heurístico]`
- Estructura de retículo producto: **formalmente correcta**.
- Leyes inter-eje: **formalmente verificables** (y verificadas).
- "Producto semidirecto" para el espacio total: **heurístico** — describe intuición de acoplamiento, no estructura algebraica.

**Recomendación**: Describir el espacio como "producto de retículos con restricciones de compatibilidad inter-eje" en lugar de "producto semidirecto". La semántica se preserva sin fingir estructura algebraica inexistente.

**Citas**: `urn:fxsl:kb:icas-agencia` (free monad, cofree comonad, interacción); `urn:fxsl:kb:icas-escala` (fibraciones); `urn:fxsl:kb:icas-enriquecimiento` (enriched categories).

---

## 3. Transmutación Functorial — `transmutation-spec §2-3`

**Claim**: `T_R: KORA_IR → Runtime_R` es un functor para cada runtime R. Preserva composición e identidad (§3.1). La pérdida se declara, no se oculta (§4). Emite `_transmutation.yml` como proof-carrying artifact (§6).

**Anclaje al corpus**:

`urn:fxsl:kb:icas-preservacion` (02-preservacion.md:32-56) define functor con dos leyes: preservación de composición `F(g ∘ f) = F(g) ∘ F(f)` y preservación de identidad `F(id_A) = id_{F(A)}`. Distingue faithfulness (inyectividad en hom-sets) de fullness (sobreyectividad en hom-sets).

**Lo que funciona — transparencia estructural**:

La spec declara correctamente las leyes functoriales como obligatorias (§3.1-3.2). La matriz de preservación por eje (§7) es un mecanismo operacional para declarar qué valores del IR se proyectan a qué valores del runtime. La distinción entre `preserved` (verificado mecánicamente) y `declared` (documentado pero no verificado) en `_transmutation.yml` es **honesta y correcta**. El ejemplo en §6.1 muestra que de 8 leyes estructurales, 4 tienen status `preserved` y 4 tienen status `declared` — la spec no finge verificación donde no la hay.

**Problema detectado — brecha objeto/morfismo**:

Para que `T_R` sea un functor en sentido categorial, debe mapear:
1. **Objetos**: vectores IR → artefactos runtime. Esto se cumple vía matriz de preservación.
2. **Morfismos**: elevaciones/proyecciones entre vectores → relaciones entre artefactos runtime. Esto **no se verifica mecánicamente**.

La spec declara leyes de monotonicidad (`pi_monotonicity`, `mu_monotonicity`, `xi_monotonicity`) que capturan exactamente la preservación de morfismos en el caso posetal: si `v1 ≤ v2` en IR, entonces `T_R(v1) ≤ T_R(v2)` en Runtime_R. Pero en el `_transmutation.yml` de ejemplo, `xi_monotonicity` tiene status `preserved` mientras que `xi_naturality` tiene status `declared`. La distinción sugiere que la monotonicidad se verifica componente a componente pero la naturalidad (condición más fuerte) no.

**Análisis de verificabilidad**:

Las leyes de monotonicidad sobre el retículo finito del IR **son decidibles**: para cada runtime R y cada par de valores de cada eje `(v, v')` con `v ≤ v'`, verificar que `T_R(v) ≤ T_R(v')`. Esto es un número finito de chequeos (máximo 4×4×5×4×5 = 1600 combinaciones por runtime). El toolchain actual no implementa esta verificación — la declara sin ejecutarla.

**Veredicto**: `[Parcial — Formal en objetos, Declarado en morfismos]`
- La intención functorial es correcta y bien orientada.
- El functor está **definido sobre objetos** (vía matriz) pero **no verificado sobre morfismos** para la mayoría de runtimes.
- La spec es transparente al respecto — lo cual es bueno. Pero "La transmutación es functor" (§1.2) es una afirmación más fuerte que la evidencia disponible.

**Recomendación**:
1. Implementar verificación mecánica de monotonicidad en el toolchain (decidible sobre el retículo finito).
2. Reformular §1.2: "La transmutación aspira a ser functorial y declara sus desviaciones" en lugar de "La transmutación es functor".
3. Completar la verificación de `xi_naturality` para al menos un runtime como prueba de concepto.

**Citas**: `urn:fxsl:kb:icas-preservacion` (leyes functoriales); `transmutation-spec §6.1` (ejemplo con status mixto `preserved`/`declared`).

---

## 4. Adjunction Lift_R ⊣ T_R — `transmutation-spec §2.3, §9`

**Claim**: `Lift_R ⊣ T_R` es una adjunción (cuando el runtime la soporta), con `T_R ∘ Lift_R = id` y `Lift_R ∘ T_R ≤ id`. Round-trip test: `ingest → transmute → ingest ≡ ingest` y `transmute → ingest → transmute ≡ transmute`.

**Anclaje al corpus**:

`urn:fxsl:kb:icas-adjunciones` (06-adjunciones.md) define adjunción vía iso natural `Hom(FX, Y) ≅ Hom(X, GY)`, unit `η: Id → G∘F`, counit `ε: F∘G → Id`, e identidades triangulares.

**Problema detectado — adjunción vs. conexión de Galois**:

Lo que la spec describe (`Lift_R ∘ T_R ≤ id` usando orden parcial `≤`) es precisamente una **conexión de Galois** sobre el retículo de vectores, no una adjunción en el sentido 1-categorial completo.

En un poset, una conexión de Galois es un par de funciones monótonas `f ⊣ g` con:
```
f(x) ≤ y  ⟺  x ≤ g(y)
```
Esto es exactamente lo que las condiciones de round-trip intentan capturar cuando el espacio es un retículo.

La diferencia con una adjunción 1-categorial:
- Una adjunción requiere el iso natural `Hom(FX, Y) ≅ Hom(X, GY)` **para todos los objetos X, Y** y la naturalidad en ambas variables.
- Una conexión de Galois es el caso especial cuando la categoría es un poset (los hom-sets tienen a lo sumo un elemento).
- La spec no exhibe la unit `η` ni verifica las identidades triangulares (aunque en un poset, estas son automáticas si se cumple la condición de Galois).

**Veredicto**: `[Heurístico — conexión de Galois, no adjunción 1-categorial]`
- La estructura real es una **conexión de Galois** sobre el retículo PMI × LFS.
- El uso de "adjunción" es un caso de **falso amigo** (según taxonomía `falsos-amigos.md`): "F y G son inversos" vs. "tener `Hom(FX, Y) ≅ Hom(X, GY)` natural en X y Y".
- La diferencia práctica es menor porque el espacio IR es efectivamente un poset, pero la precisión terminológica importa.

**Recomendación**: Usar "conexión de Galois" o "adjunción en el retículo PMI × LFS" en lugar de "adjunción" a secas. Esto preserva la semántica correcta sin prometer estructura que excede el dominio posetal.

**Citas**: `urn:fxsl:kb:icas-adjunciones` (adjunciones en posets como conexiones de Galois); `falsos-amigos.md` §"Adjuncion".

---

## 5. QA Enrichment — `qa-spec §3-4`

**Claim**: `V_QA = ([0,1]^5, <=, 1̄, ⊗)` como monoidal preorder canónico de KORA para compromisos de calidad. `ιΣ: {0,1,2,3}^5 → [0,1]^5` como cambio de base monoidal monótono. `Bool` y `Cost` como vistas derivadas por cambio de base.

**Anclaje al corpus**:

`urn:fxsl:kb:icas-enriquecimiento` (08-enriquecimiento.md:70-76) define exactamente `[0,1]`-enrichment con multiplicación como tensor para modelar QoS/fiabilidad:

```
X(x, y) * X(y, z) <= X(x, z)    — composición
X(x, x) = 1                      — identidad
```

El cambio de base (08-enriquecimiento.md:78-80) es una operación canónica: dado un funtor monoidal laxo `f: V → W`, toda V-category induce una W-category aplicando `f` a los hom-objects.

**Lo que funciona**:

1. **Moneda canónica correcta**: `V_QA` está correctamente definida como categoría monoidal (el intervalo [0,1] con orden ≤, multiplicación como tensor, 1 como unidad). Las leyes de categoría monoidal se satisfacen: asociatividad de la multiplicación, 1 como unidad.

2. **Cambio de base `ιΣ` correcto**: La inclusión `ιΣ: {0,1,2,3}^5 → [0,1]^5` con `ιΣ(0)=0, ιΣ(1)=1/3, ιΣ(2)=2/3, ιΣ(3)=1` es un funtor monoidal monótono. Preserva orden (si `v ≤ w` entonces `ιΣ(v) ≤ ιΣ(w)` componente a componente) y la estructura monoidal (`ιΣ(3) = 1` que corresponde a la unidad `1̄`). Esto permite tratar `Σ` discreto y `Σ̃` enriched como vistas de la misma estructura subyacente.

3. **Threshold `θ_hard` correcto**: `θ_hard(x) = true ssi x >= 2/3` es un cambio de base `[0,1] → Bool` válido. La spec explícitamente declara que `Bool` es una vista derivada, no la moneda canónica.

4. **Separación V_QA vs. Cost correcta**: La spec insiste correctamente en que `Cost` (latencia, MTTR, costo monetario) usa el tensor aditivo `+` mientras que `V_QA` usa el tensor multiplicativo `*`. Son monedas de enriquecimiento distintas para fenómenos cuantitativos distintos. Esto sigue exactamente la enseñanza de `08-enriquecimiento`: `Cost = ([0,∞], >=, 0, +)` para distancias/latencias vs. `[0,1]` para fiabilidades.

**Veredicto**: `[Formal]` ✅
- Es la construcción categorial **más sólida** de todas las specs de KORA.
- No tiene desviaciones entre lo declarado y lo verificado.
- El puente entre `Σ` discreto (authoring humano) y `Σ̃` enriched (razonamiento continuo) está correctamente modelado como cambio de base.
- La separación entre monedas de enriquecimiento (V_QA normativo vs. Cost operacional) es rigurosa.

**Recomendación**: Usar `qa-spec` como modelo de referencia para cómo deberían formularse las demás specs: anclaje explícito al corpus, construcción exhibida, leyes verificables, separación clara de monedas de medición.

**Citas**: `urn:fxsl:kb:icas-enriquecimiento` §"[0,1]-enrichment: calidad de servicio", §"Cambio de base de enriquecimiento".

---

## 6. Coreografía Multiagente como Sheaf — `multiagente-spec §3`

**Claim**: `Ch = (Roles, Fases, Cover, Sec, Glue)` modela la coreografía como sheaf de secciones locales sobre un cubrimiento de fases por roles. El pegado (Glue) construye una sección global solo si las secciones locales coinciden en los solapamientos obligatorios.

**Anclaje al corpus**:

- `urn:fxsl:kb:icas-topoi` (12-topoi.md): sheaves sobre un sitio, condición de pegado, clasificador de subobjetos.
- `urn:fxsl:kb:icas-protocolos` (14b-protocolos.md:66,109): protocolos como interacción entre free monads y cofree comonads; coreografía emerge cuando los profunctors de interacción componen sin coordinador central.

**Lo que funciona — intuición de sheaf**:

La analogía es productiva y correcta en su dirección:
- **Secciones locales**: cada agente/rol produce una vista parcial sobre las fases que cubre.
- **Solapamientos**: los handoffs entre agentes son las intersecciones donde las secciones deben ser compatibles.
- **Pegado**: la coherencia global requiere que las secciones locales coincidan en los solapamientos — exactamente la condición de sheaf.

Los solapamientos obligatorios (§3.2) son restricciones de compatibilidad bien definidas y operacionalmente verificables: `session_id`, `protocol_id`, `ticket de procedencia`, `qa_floor`, `capabilities`, `resume_token`.

**Problema detectado — falta de definición del sitio**:

Un sheaf se define sobre un **sitio** `(C, J)` donde `C` es una categoría y `J` es una topología de Grothendieck. La spec define:
- `Fases`: conjunto ordenado de fases (podría formar una categoría con morfismos de precedencia).
- `Cover`: asigna a cada rol la subfamilia de fases que cubre.
- Pero **no define la topología J**: ¿es la topología discreta? ¿La generada por los covers? ¿La topología de intervalos sobre el orden de fases?

Sin sitio, "sheaf" es una metáfora estructural de alta calidad, no una construcción verificable. La condición de pegado se enuncia pero no se puede verificar mecánicamente sin especificar qué cubrimientos son admisibles y cómo se relacionan.

**Veredicto**: `[Heurístico de alta calidad]`
- La aplicación de pensamiento de sheaf es correcta, productiva y bien orientada.
- La construcción formal de sheaf está incompleta (falta el sitio y la topología).
- La estructura de compatibilidad local-global captura exactamente lo que se necesita para handoffs multiagente.

**Recomendación**: Definir explícitamente el sitio: tomar como categoría base el conjunto ordenado de fases (morfismos = precedencia), y declarar la topología de Grothendieck generada por los covers de cada rol (los sieves que contienen todas las fases asignadas a un rol). Con esto, la condición de sheaf se vuelve formalmente enunciable y potencialmente verificable.

**Citas**: `urn:fxsl:kb:icas-topoi` (sheaves, condición de pegado); `urn:fxsl:kb:icas-protocolos` (protocolos como estructuras categoriales).

---

## 7. Koraficación como "Functor K" — `md-spec §5.5`

**Claim**: "Koraficacion Functor K" con propiedades: fiel, comprimido, promotor de estructura, realizador de superficie, normalizador, idempotente, invariante en idioma. `FS=100%` es el criterio de fidelidad.

**Anclaje al corpus**:

La spec referencia `urn:kora:kb:05-governance-lattice` §2.2 como origen del "Koraficacion Functor K". No se consultó este documento en la presente auditoría.

**Problema detectado — uso del vocabulario categorial**:

1. **"Functor"**: No se definen las categorías dominio y codominio de K. No se exhiben las leyes de preservación de composición e identidad. La koraficación es una transformación `DocHumano → KORA/MD`, pero no se demuestra que esta transformación sea un functor entre categorías de documentos.

2. **"Fiel"**: Significa "preserva todos los hechos (FS=100%)", no "faithful functor" (inyectivo en hom-sets). Es un **falso amigo** según `falsos-amigos.md`: "faithful" en teoría de categorías significa que el functor es inyectivo en cada hom-set — `F(f) = F(g) ⟹ f = g`. La spec usa "fiel" en sentido coloquial (fidelidad factual), no categorial.

3. **"Idempotente"**: `K(K(x)) = K(x)`. Esta es una propiedad operacional válida y verificable, pero no se deriva de una estructura categorial — es una restricción de diseño sobre la transformación.

**Veredicto**: `[Metafórico]`
- Uso de vocabulario categorial sin estructura categorial subyacente verificada.
- "Functor K" es una analogía, no una construcción formal.
- Las propiedades declaradas (FS=100%, idempotencia, compresión) son valiosas y operacionalmente verificables, pero no necesitan el wrapper de "functor" para sostenerse.

**Recomendación**: Mantener "Koraficación" como nombre del proceso y declarar las propiedades operacionales (FS=100%, CR>1.5, idempotencia, etc.) sin el wrapper de "functor". O bien, definir formalmente las categorías dominio (documentos fuente con morfismos de referencia) y codominio (documentos KORA/MD con morfismos de cita/dependencia) y verificar las leyes functoriales.

**Citas**: `falsos-amigos.md` §"Funtor" (distingue functor de "una función entre dos cosas"); `urn:fxsl:kb:icas-preservacion` (leyes functoriales).

---

## 8. Lifecycle como "Functor" — `gobernanza §5.1`

**Claim**: "Ola_k : Staging -> Productivo" como functor de lifecycle. Cada ola declara perímetro, invariante de cierre, y deuda residual. "El functor de transición Ola_k -> Ola_{k+1} tiene como dominio la deuda residual declarada de la ola anterior".

**Problema detectado**:

1. No se definen `Staging` ni `Productivo` como categorías (objetos, morfismos, composición).
2. Una "ola" es una operación de migración/promoción de un conjunto de artefactos, no un functor entre categorías.
3. No se exhiben leyes de preservación de composición ni de identidad.
4. "El functor de transición Ola_k -> Ola_{k+1}" trata las olas como objetos de una categoría, no como functores. Hay confusión entre niveles: si Ola_k es un functor, Ola_k -> Ola_{k+1} sería una transformación natural, no un functor.

**Veredicto**: `[Metafórico]`
- Uso puramente decorativo del término "functor".
- El concepto de ola como agrupación de artefactos con invariante de cierre es valioso por sí mismo sin necesidad del wrapper categorial.
- La confusión de niveles (ola como functor vs. ola como objeto) revela que el término no está anclado a estructura verificable.

**Recomendación**: Usar "transición" u "operación de promoción" para las olas. El concepto de deuda residual como input de la siguiente ola es una estructura de pipeline válida sin necesidad de nombrarla "functor". Si se desea mantener lenguaje categorial, modelar las olas como **objetos** de una categoría de pipelines y las transiciones como **morfismos** — no como functores.

---

## 9. Arnés como Discriminante Ontológico — `autoria-spec §4.6`

**Claim**: "Skills y agents NO son ontologicamente categorias distintas. Son proyecciones operacionales del mismo objeto agentico, distinguidas por el arnes categorial que ocupan en el espacio PMI × LFS." La forma material es derivada operacional; el arnés + vector define la identidad ontológica.

**Anclaje al corpus**:

Implícitamente consistente con `urn:fxsl:kb:icas-identidad-relacion` (04-identidad-es-relacion.md): el lema de Yoneda establece que un objeto está determinado (salvo isomorfismo) por sus relaciones con todos los demás objetos — es decir, por su posición en la categoría. La spec aplica este principio: la identidad de un artefacto es su posición en el espacio PMI × LFS (arnés + vector), no su presentación operacional (forma material).

**Lo que funciona**:

La decisión es arquitecturalmente sólida:
- Distingue lo que un artefacto **es** (arnés + vector) de cómo se **materializa** (forma material).
- Sigue el principio de separación ontología/serialización que es central en KORA.
- Elimina la duplicación ontológica que existía pre-v2.0 (agentes y skills como categorías separadas).

**Limitación**:

No es una construcción categorial formal — no hay una categoría de arneses con funtores. Pero la intuición subyacente (identidad por estructura, no por presentación) es categorialmente sana. La spec no pretende ser una construcción categorial en este punto; es una decisión de arquitectura informada por pensamiento categorial.

**Veredicto**: `[Conceptualmente correcto]`
- No es formal (no hay categoría de arneses), pero la dirección es correcta.
- La distinción objeto/materialización es una aplicación válida de principios categoriales.

**Citas**: `urn:fxsl:kb:icas-identidad-relacion` (Yoneda, embedding); `autoria-spec §4.6` (HITL 2026-05-20).

---

## 10. Tabla de Consistencia General

| # | Spec | Claim categorial | Tipo | ¿Formalmente respaldado? | ¿Verificable? |
|---|------|-----------------|------|--------------------------|---------------|
| 1 | `harness-spec §2` | Axioma `(m_p, c_q, Ξ)` | **Formal** | Sí (`urn:fxsl:kb:icas-agencia`) | Sí (leyes de mónada/comónada) |
| 2 | `harness-spec §2` | `⋉` producto semidirecto | **Heurístico** | No | No (sin construcción) |
| 3 | `harness-spec §3-4` | Espacio PMI × LFS como retículo | **Formal** | Sí (retículos finitos) | Sí (join/meet) |
| 4 | `harness-spec §4.1` | Leyes inter-eje | **Formal** | Sí (implicaciones sobre dominio finito) | Sí (`kora check --strict`) |
| 5 | `qa-spec §3-4` | `V_QA` enriched, cambio de base `ιΣ` | **Formal** | Sí (`urn:fxsl:kb:icas-enriquecimiento`) | Sí (leyes de categoría monoidal) |
| 6 | `transmutation-spec §2-3` | `T_R` functor (objetos) | **Parcial** | Sí (matriz de preservación) | Sí |
| 7 | `transmutation-spec §2-3` | `T_R` functor (morfismos) | **Declarado** | Dirección correcta | No verificado mecánicamente |
| 8 | `transmutation-spec §2.3` | `Lift_R ⊣ T_R` adjunción | **Heurístico** | Es conexión de Galois, no adjunción | Parcial (round-trip test) |
| 9 | `multiagente-spec §3` | Sheaf de coreografía | **Heurístico de alta calidad** | Dirección correcta | Falta definición de sitio |
| 10 | `md-spec §5.5` | Koraficación "Functor K" | **Metafórico** | No | Propiedades operacionales sí, leyes functoriales no |
| 11 | `gobernanza §5.1` | Ola_k "functor" de lifecycle | **Metafórico** | No | No |
| 12 | `autoria-spec §4.6` | Arnés como discriminante ontológico | **Conceptualmente correcto** | Principio de identidad estructural | Sí (check `arnes-compatible-con-forma`) |

---

## 11. Hallazgos Transversales

### A. Sobreuso de "producto semidirecto" (⋉)

Aparece en `harness-spec §2` y `gobernanza §1`. En ambos casos se usa para expresar "el contexto modula la estructura sin reemplazarla". No es una construcción categorial estándar en este contexto. Alternativas más precisas:
- Producto cartesiano con proyección (si el contexto es independiente).
- Fibración de Grothendieck (`urn:fxsl:kb:icas-extension`) si el contexto varía sobre una base.
- Simple conjunción "×" con nota de que el contexto modula sin sustituir.

### B. Tensión posetal vs. 1-categorial

Varias construcciones de KORA viven en retículos/posets (espacio PMI × LFS, enriquecimiento de calidad). Sin embargo, el vocabulario usado a veces es 1-categorial (adjunción en vez de conexión de Galois, functor en vez de mapa monótono). Esto crea una brecha entre el vocabulario empleado y la estructura formalizada:

| Estructura real | Vocabulario usado | Vocabulario preciso |
|-----------------|-------------------|---------------------|
| Mapa monótono entre retículos | Functor | Mapa monótono / functor entre posets |
| Conexión de Galois en retículo | Adjunción | Conexión de Galois / adjunción en poset |
| Operación de promoción | Functor de lifecycle | Transición / morfismo en categoría de pipelines |

### C. Verificabilidad no explotada

Varias leyes categoriales declaradas en las specs son **decidibles** sobre los dominios finitos del IR pero no están implementadas en el toolchain:
- Monotonicidad de `T_R` por eje (verificable componente a componente).
- Condición de sheaf para coreografías con conjunto finito de fases y roles.
- Leyes functoriales para koraficación sobre corpus finito.

### D. Honestidad estructural — el activo más valioso

La distinción `preserved` vs. `declared` en `_transmutation.yml` es el mecanismo más importante de integridad intelectual en las specs. Extender este patrón a todas las specs — marcando explícitamente qué es formal, qué es heurístico y qué es metafórico — fortalecería la arquitectura sin requerir rehacer nada.

---

## 12. Conclusiones

### 12.1 Diagnóstico Global

KORA es una arquitectura cuya **columna vertebral es categorialmente sólida** (`harness-spec`, `qa-spec`) pero cuya **periferia operacional usa vocabulario categorial con precisión variable** (`transmutation-spec` parcial, `gobernanza` metafórica, `md-spec` metafórica). Esto es esperable y no es una falla: el núcleo ontológico (PMI × LFS) necesita ser riguroso; la periferia operacional necesita ser usable.

La teoría de categorías funciona en KORA como **lenguaje de diseño**, no como proof assistant. Esto es una decisión de ingeniería legítima y productiva. El riesgo no está en que haya claims heurísticos o metafóricos, sino en que no estén **marcados como tales**, lo que puede inducir a error sobre el nivel de garantía formal que ofrece cada parte del sistema.

### 12.2 Fortalezas

1. **Núcleo ontológico sólido**: La tripleta `(m_p, c_q, Ξ)` de `harness-spec` está correctamente anclada en Libkind-Spivak vía `urn:fxsl:kb:icas-agencia`. El espacio PMI × LFS como retículo es una construcción formal correcta.

2. **QA-spec como referencia de calidad**: La construcción de `V_QA` como categoría enriched, con cambio de base explícito y separación de monedas de medición, es impecable.

3. **Transparencia en transmutación**: La distinción `preserved`/`declared` en `_transmutation.yml` es un mecanismo ejemplar de honestidad intelectual que debería extenderse a todo el ecosistema.

4. **Separación ontología/serialización/runtime**: Las 4 capas de `gobernanza §3.1` son una decisión arquitectural que refleja principios categoriales genuinos (funtores de proyección entre capas).

5. **Toolchain verificador**: `kora check --strict` aprueba 34/34 checks. Las leyes inter-eje, la consistencia de formas materiales, y la integridad de URNs están verificadas mecánicamente.

### 12.3 Debilidades

1. **"Producto semidirecto" sin definición**: Usado en dos specs clave sin construcción algebraica que lo respalde. Es el caso más claro de vocabulario que promete más estructura de la que se exhibe.

2. **"Functor" usado como metáfora**: En gobernanza (olas) y md-spec (koraficación), el término no está respaldado por verificación de leyes functoriales.

3. **Verificación de morfismos pendiente**: `T_R` mapea objetos pero la preservación de morfismos (monotonicidad, naturalidad) no está verificada mecánicamente para la mayoría de los runtimes.

4. **Sheaf sin sitio**: La coreografía multiagente usa la intuición correcta pero no completa la construcción formal.

5. **Sin convención de marcado**: No hay forma sistemática de saber, al leer una spec, si un claim categorial es formal, heurístico o metafórico.

### 12.4 Veredicto Final

**KORA es una arquitectura de "correctness-by-construction" en su núcleo ontológico, con una periferia operacional que usa teoría de categorías como vocabulario de diseño de precisión variable.** La dirección general es correcta. Las debilidades identificadas no requieren rehacer la arquitectura; requieren una pasada de **precisión conceptual** y, donde sea posible, **verificación mecánica** de leyes que ya son decidibles.

La brecha principal no es de corrección sino de **consistencia terminológica**: el mismo término ("functor", "producto semidirecto", "adjunción") se usa con distintos niveles de rigor formal en distintas specs. Cerrar esta brecha fortalecería la arquitectura sin cambiar su estructura.

---

## 13. Recomendaciones

### R1. Convención de marcado de claims categoriales

Crear una convención explícita para marcar el nivel de formalización de cada claim categorial en las specs. Propuesta:

| Marca | Significado | Ejemplo |
|-------|-------------|---------|
| `[F]` | Formal: construcción verificable, leyes exhibidas, anclaje al corpus | `V_QA = ([0,1]^5, <=, 1̄, ⊗)` |
| `[H]` | Heurístico: dirección correcta, verificación parcial o pendiente, anclaje parcial | `Lift_R ⊣ T_R` |
| `[M]` | Metafórico: vocabulario categorial sin estructura subyacente verificable | "Ola_k : Staging -> Productivo" |

Aplicar retroactivamente a las 4 specs principales. Mantener una tabla de "Nivel de formalización" por sección.

### R2. Eliminar "producto semidirecto"

Reemplazar `⋉` en `harness-spec §2` y `gobernanza §1` por:
- "Producto cartesiano con restricciones de compatibilidad inter-eje", o
- Si se desea preservar `⋉` como conveniencia notacional, agregar una nota explícita: "El símbolo ⋉ no denota el producto semidirecto algebraico; es una conveniencia notacional para 'contexto que modula sin sustituir'. La estructura formal subyacente es el producto de retículos con restricciones de compatibilidad."

### R3. Verificar monotonicidad de T_R en el toolchain

Las leyes de monotonicidad para `T_R` son decidibles sobre el retículo finito del IR. Implementar en `toolchain/`:
- Para cada runtime R, para cada eje E, para cada par `(v, v')` con `v ≤ v'`, verificar que `T_R(v) ≤ T_R(v')`.
- Agregar check `transmutation-monotonicity` al pipeline de `kora check --strict`.
- Esto acerca `T_R` a un functor verificado sobre la parte posetal del espacio.

### R4. Definir el sitio de la coreografía

En `multiagente-spec §3`:
- Declarar la categoría base: el conjunto ordenado de fases con morfismos de precedencia.
- Declarar la topología de Grothendieck: la generada por los cubrimientos de cada rol.
- Verificar la condición de sheaf para coreografías concretas (conjunto finito de fases y roles).

### R5. Degradar claims no verificados

Reformular claims donde el vocabulario excede la estructura:
- `gobernanza §5.1`: "Ola_k como transición de pipeline" (no "functor").
- `md-spec §5.5`: "Koraficación K" con propiedades declaradas (no "Functor K").
- `transmutation-spec §1.2`: "La transmutación aspira a ser functorial y declara sus desviaciones" (no "La transmutación es functor").
- `transmutation-spec §2.3`: "Conexión de Galois entre ingesta y proyección" (no "adjunción").

### R6. Usar qa-spec como modelo de calidad formal

`qa-spec` es la spec mejor construida categorialmente. Usarla como template para:
- Anclaje explícito de cada construcción a URNs del corpus.
- Exhibición de leyes verificables.
- Separación de monedas de medición.
- Declaración explícita de cambios de base autorizados.

---

## 14. Trazabilidad

| Sección | URNs citadas |
|---------|-------------|
| §1 Axioma Fundamental | `urn:fxsl:kb:icas-agencia`, `urn:fxsl:kb:icas-extension` |
| §2 Espacio PMI × LFS | `urn:fxsl:kb:icas-agencia`, `urn:fxsl:kb:icas-escala`, `urn:fxsl:kb:icas-enriquecimiento` |
| §3 Transmutación | `urn:fxsl:kb:icas-preservacion` |
| §4 Adjunction | `urn:fxsl:kb:icas-adjunciones` |
| §5 QA Enrichment | `urn:fxsl:kb:icas-enriquecimiento` |
| §6 Coreografía | `urn:fxsl:kb:icas-topoi`, `urn:fxsl:kb:icas-protocolos` |
| §7 Koraficación | `urn:fxsl:kb:icas-preservacion` |
| §8 Lifecycle | — (claim metafórico, sin anclaje) |
| §9 Arnés | `urn:fxsl:kb:icas-identidad-relacion` |

---

*Este informe reemplaza cualquier versión anterior de auditoría categorial de KORA. Los hallazgos están anclados a las specs en su versión vigente al 2026-06-07 y al corpus ICAS-BoK en su estado actual.*
