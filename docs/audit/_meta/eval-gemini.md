# Meta-evaluación: `auditoria_categorial_kora_gemini.md`

- **Reporte:** `/home/felix/kora/docs/audit/auditoria_categorial_kora_gemini.md`
- **Slug:** gemini
- **Auto-atribución del reporte:** Skill `cat-thinking` (línea 3). La pista de origen (Gemini) refiere al modelo productor, no a una afirmación interna.
- **Objeto que el reporte audita REALMENTE:** la arquitectura / el sistema KORA en general (no las specs).
- **Objeto que la tarea pedía auditar:** las specs de KORA (`governance/ ontology/ serialization/ runtime/`).
- **scope_fit:** `sistema` (desajuste de alcance).

---

## 1. Resumen del veredicto

El reporte es **competente en vocabulario categorial y mayormente fiel al corpus ICAS-BoK en sus claims de teoría**, pero **falla como auditoría de specs** por tres razones estructurales:

1. **No audita el objeto correcto.** Audita "la arquitectura KORA" / "el toolchain" / "el sistema", nunca las specs. No menciona *ni un solo* archivo de spec (verificado: grep de `autoria-spec|harness-spec|md-spec|knowledge-spec|transmutation-spec|gobernanza|ontology/|serialization/|runtime/` sobre el reporte → 0 hits).
2. **Es el functor constante hacia "todo correcto".** Todo checkbox es `Sí` / `[x]`. No hay un solo hallazgo negativo, falla, severidad ni recomendación. Esto es exactamente el anti-patrón que la rúbrica penaliza: una auditoría que no halla nada es sospechosa, y aquí el funtor F: Cat(specs) → Cat(categorial) colapsa a la constante "correctness-by-construction".
3. **No distingue declarado de cumplido** — y lo hace peor que las propias specs. La `harness-spec` y la `transmutation-spec` *ya* declaran la estructura categorial que el reporte presenta como hallazgo, y la declaran con más honestidad (pérdida declarada, fidelidad fiel-pero-no-plena, checks). El reporte re-narra la auto-descripción de las specs y la **suaviza** a checkmarks acríticos.

A esto se suma **una estructura inventada y atribuida a una URN del corpus que no la contiene** (el producto fibrado de estado de cuatro vías), y **dos adjunciones/funtorialidades afirmadas como cumplidas sin el test que el propio corpus exige**.

---

## 2. Verificación de los claims fuertes (5 comprobaciones contra corpus/specs)

### V1 — Agencia: free monad `m_p` (plan) ⊗ cofree comonad `c_q` (ejecutor), `Ξ: m_p ⊗ c_q → m_{p⊗q}`, "modelo exacto de un agente LLM" (reporte §2.C, §5)
**VERIFICADO / FIEL.** `14-agencia.md` líneas 66-76 declaran literalmente `Xi_{p,q}: m_p tensor c_q -> m_{p tensor q}` y, en la 76, "Este es el modelo exacto de un agente LLM: el prompt chain es el patron m_p, el motor de inferencia es la materia c_q". El reporte reproduce esto correctamente (patrón=KORA, materia=LLM). Además la `harness-spec` línea 63 eleva esta tripleta a axioma central. Claim correcto. *Pero* es re-narración de lo que la spec ya dice de sí misma, no un hallazgo de auditoría.

### V2 — Efectos: agente como "F-Coálgebra en la categoría de Kleisli Kl(M)", con `c: U → M(F(U))` y `U = U_phen × U_ctx × U_epi × U_sta` (reporte §2.B)
**PARCIALMENTE VERIFICADO, CON INVENCIÓN.** La parte coalgebraica genérica es fiel: `09-efectos.md` define F-coálgebra `alpha: U -> F(U)` (línea 177), categoría de Kleisli `Kl(T)` (línea 55 ss.), bisimulación (líneas 214-222). Pero la **descomposición de estado de cuatro vías `U_phen × U_ctx × U_epi × U_sta` y el "Principio de Segregación" NO existen** ni en `09-efectos.md` ni en la `harness-spec` ni en `autoria-spec` (verificado: grep de `U_phen|U_ctx|U_epi|U_sta|Segregaci` sobre todo el corpus ICAS + ontology + autoria-spec → 0 hits). La `harness-spec` descompone el agente en los 6 ejes PMI×LFS (Π·Μ·Ξ × Λ·Φ·Σ), **no** en un producto fibrado de un carrier coalgebraico. El reporte fabrica estructura y la atribuye a `urn:fxsl:kb:icas-efectos`. Falso amigo de **buena-definición** (functor no bien-definido: inventa objetos en el dominio).

### V3 — Adjunción: `Instantiate ⊣ Observe` (Free ⊣ Forgetful) para instanciar subagentes; "La delegación se garantiza segura mediante el par adjunto" (reporte §2.D, §5)
**DUDOSO / NO SOPORTADO.** `06-adjunciones.md` discute Free/Forgetful como arquetipo (líneas 89-93), pero **no contiene** `Instantiate ⊣ Observe` ni una adjunción para instanciación de subagentes. Más grave: el corpus citado **advierte explícitamente** contra el movimiento que el reporte hace. Línea 108: el patrón free/forgetful "en algunos casos es una adjunción exacta; en otros, una lectura estructural útil pero no literal". Líneas 240-244: Compilar/Interpretar, Normalizar/Desnormalizar, Comprimir/Expandir "no debe leerse como teorema sin más", "no toda pareja codec forma una adjunción categórica literal". El reporte afirma la adjunción como **cumplida y garante de seguridad** sin verificar identidades triangulares ni fijar las categorías — exactamente lo que el corpus prohíbe. Falso amigo de **adjunción vs par de operaciones que van y vienen**.

### V4 — Transmute como functor que "respeta homomorfismos: el código compilado preserva los axiomas del Markdown original. Sí" (reporte §3, checklist; §5 "Fidelidad y Conmutatividad")
**ERRÓNEO POR OMISIÓN DEL TEST.** La `transmutation-spec` línea 48 sí declara "La transmutacion es functor", pero el reporte ignora que la misma spec (§4.1, líneas 144-148) distingue **fiel-y-plena vs fiel-pero-no-plena por eje** y monta toda una máquina de **pérdida declarada** ("Perdida declarada por eje con matriz de preservacion explicita", línea 552; anti-patrón "Declarar fidelidad full cuando hay perdida real", línea 447). El corpus que ancla esto (`02-preservacion.md` línea 114) dice que "la mayoria de los functores... son fieles pero no plenos" y que las leyes son "un TEST" (línea 45) a aplicar. El reporte pone checkmark `Sí` afirmando **preservación de homomorfismos / conmutatividad** sin aplicar el test y sin reconocer la pérdida que la propia spec declara obligatoriamente. La spec es más rigurosa que la auditoría. Falso amigo de **isomorfismo/igualdad vs functor fiel-pero-no-pleno**.

### V5 — Action-Primary-Key vs State-Primary-Key, catamorfismo sobre logs, P-D-A como traced morphism (reporte §4)
**VERIFICADO / FIEL.** `14-agencia.md` línea 152 ("event sourcing es action-primary-key... fold (catamorfismo) sobre la secuencia de acciones... el append-only log es la categoría libre... reconstrucción del estado es el único homomorfismo") y líneas 162-172 (P-D-A como traced morphism en categoría compact closed). El reporte reproduce el trade-off correctamente. Buen anclaje. *Pero* el reporte **afirma que KORA "eligió explícitamente" Action-Primary-Key** (§4) — esto es una atribución al sistema, no respaldada por cita a spec alguna; es plausible como lectura pero no verificada contra el objeto-spec.

---

## 3. Puntuación por dimensión (0-5)

| # | Dimensión | Score | Justificación (con cita del reporte) |
|---|-----------|------:|--------------------------------------|
| 1 | fidelidad_functorial | 2 | Distingue bien functor/mónada/coálgebra/bisimulación a nivel de vocabulario (§2.B-C correctos). Pero como functor F: specs→categorial **colapsa a la constante "todo correcto"** (toda casilla §3 = Sí), que es la máxima infidelidad. Además inventa estructura (V2: `U_phen×U_ctx×U_epi×U_sta`). Faithful a ratos, no bien-definido en otros. |
| 2 | correccion_leyes | 3 | Los claims de V1 y V5 son categorialmente correctos. Pero afirma conmutatividad/preservación de homomorfismos de `transmute` (§3) **sin** la pérdida que la spec declara (V4), y una adjunción no soportada (V3). Hay claims fuertes presentados como cumplidos que no se sostienen. |
| 3 | formal_vs_heuristico | 1 | Regla dura violada de raíz: **no declara en ningún punto qué es teorema/lema vs analogía**. Todo se presenta como hecho ("demostrando bisimulación estructural" §2.B, "matemáticamente imposible" §5) sin una sola demostración. Checkmarks `[x] ... Sí` (§3) son aserciones sin prueba. El corpus que cita (V3, V4) pide exactamente la cautela que el reporte omite. |
| 4 | anclaje_trazabilidad | 2 | Cita URNs `icas-*` por sección (composicion, preservacion, efectos, agencia, adjunciones) — eso suma. Pero **no cita ni una sola spec concreta** por hallazgo (verificado: 0 hits de filenames de spec). Por Yoneda, un claim sobre las specs que no referencia las specs no está anclado a su objeto. Anclaje al corpus sí, al objeto auditado no. |
| 5 | cobertura_completitud | 1 | **Audita el objeto equivocado.** Cubre "arquitectura/sistema/toolchain KORA", no las specs (governance/ontology/serialization/runtime). No examina precedencia, lifecycle, freeze formal de harness, regímenes URN, ni una sola spec por nombre. Examina algunos morfismos (depends/supersedes §2.A) pero como propiedades del grafo de conocimiento, no de la ley. Scope_fit roto. |
| 6 | poder_diagnostico | 0 | **Cero hallazgos negativos, cero severidad, cero falsabilidad.** Es puramente celebratorio: "diseño contundente", "arquitectura de estado sólido", "correctness-by-construction llevado al extremo", "matemáticamente imposible expresar estados contradictorios" (§5). Anti-patrón Goodhart/decoración en estado puro: optimiza la apariencia de rigor. Una auditoría sin un solo defecto es el síntoma exacto que la rúbrica marca como sospechoso. |
| 7 | accionabilidad | 0 | **No hay ninguna recomendación.** Ni una sola línea hallazgo→remedio→enforcement. El §5 es un veredicto laudatorio, no un plan. Nada priorizado, nada implementable. |
| 8 | parsimonia | 2 | Usa maquinaria pesada (operads dinámicas, contextads implícitos, comónadas cofree, producto fibrado) donde a veces basta menos. El producto fibrado de 4 vías (V2) es jerga añadida que **no hace trabajo** (no deriva ningún hallazgo) y encima es inventada. No es la lectura más débil que cumple; sobre-formaliza para impresionar. |
| 9 | coherencia_interna | 3 | Internamente el argumento compone razonablemente: las secciones encadenan (estructura→patrones→checklist→trade-offs→conclusión) y no hay contradicciones flagrantes. El no-sequitur principal es saltar de "las specs declaran X" (que ni siquiera cita) a "el sistema *cumple* X, Sí" sin puente probatorio, pero la prosa es consistente consigo misma. |

**score_total = 2+3+1+2+1+0+0+2+3 = 14 / 45**

---

## 4. Claims atómicos extraídos

| id | tema | tipo | statement | status |
|----|------|------|-----------|--------|
| C1 | icas-composicion / grafo conocimiento | afirmacion-correccion | El grafo de documentos es una categoría finitamente presentada; depends es DAG estricto, supersedes antisimétrico | plausible |
| C2 | icas-preservacion / pipeline | afirmacion-correccion | El pipeline Intake∘Normalize∘Enrich∘Publish es cadena de functores que preserva identidad URN (isomorfismo de identidad) | plausible |
| C3 | icas-efectos / agente | afirmacion-correccion | El agente es F-coálgebra en Kl(M) con c: U→M(F(U)); el LLM no puede modificar M desde dentro | plausible |
| C4 | icas-efectos / estado | afirmacion-correccion | El estado se descompone como producto fibrado U_phen×U_ctx×U_epi×U_sta (Principio de Segregación, bisimulación estructural) | erroneo |
| C5 | icas-agencia / interacción | afirmacion-correccion | Plan=free monad m_p, ejecutor=cofree comonad c_q, ejecución=Ξ: m_p⊗c_q→m_{p⊗q}; modelo exacto del agente LLM | verificado |
| C6 | icas-adjunciones / subagentes | afirmacion-correccion | La instanciación de subagente es par adjunto Instantiate⊣Observe (Free⊣Forgetful); la delegación se garantiza segura por ello | dudoso |
| C7 | transmutation / functor | afirmacion-correccion | transmute es functor que respeta homomorfismos: el código compilado preserva los axiomas del Markdown original (Sí) | dudoso |
| C8 | icas-agencia / modelo de datos | observacion | KORA eligió Action-Primary-Key sobre State-Primary-Key; estado vía catamorfismo sobre logs; P-D-A como traced morphism | plausible |
| C9 | composicionalidad / wiring | afirmacion-correccion | La conexión de agentes vía diagramas de cableado W preserva comportamiento sin abrir cajas negras, por ortogonalidad fibrada (Sí) | dudoso |
| C10 | sistema KORA / veredicto | observacion | KORA es "correctness-by-construction llevado al extremo"; hace matemáticamente imposible expresar estados contradictorios | dudoso |

(Sin claims de tipo recomendacion ni hallazgo-falla: el reporte no produce ninguno.)

---

## 5. Errores categóricos detectados

| claim | problema | severidad |
|-------|----------|-----------|
| C4: `U = U_phen × U_ctx × U_epi × U_sta` atribuido a icas-efectos | Estructura **inventada**; no existe en el corpus ni en harness-spec (que usa 6 ejes PMI×LFS, no un producto fibrado de 4 estados). Functor **no bien-definido**: fabrica objetos en el dominio y los atribuye a una URN. | alta |
| C7 + C9 + checklist §3 (todo "Sí"): transmute/wiring preservan homomorfismos/conmutan, afirmado con checkmark | **Isomorfismo/conmutatividad afirmada sin el test** que el propio `02-preservacion` exige y contra la pérdida fiel-pero-no-plena que `transmutation-spec` §4.1 declara obligatoriamente. Confunde "functor" con "functor pleno / equivalencia". | alta |
| C6: `Instantiate ⊣ Observe` como adjunción cumplida y garante de seguridad | Afirma **adjunción** donde el corpus citado (`06-adjunciones` líneas 108, 240-244) advierte que estos pares suelen ser "lectura estructural útil pero no literal, no teorema". Confunde adjunción con par de operaciones ida-vuelta. | media |
| Conclusión §5 global = functor constante a "todo correcto" | Toda casilla en `Sí`/`[x]`, cero defectos. Es el **functor constante**: máximamente infiel a Cat(specs). Anti-patrón Goodhart. | alta |
| Marco metodológico | **No declara formal vs heurístico** en ningún punto (regla dura), presentando analogías ("bisimulación estructural", "matemáticamente imposible") como hechos probados. | alta |

---

## 6. Veredicto

**deficiente.**

El reporte demuestra alfabetización categorial real y reproduce con fidelidad varios resultados del corpus (V1, V5, y la base coalgebraica/functorial de V2-V4). Si la tarea hubiera sido "narra la lectura categorial del sistema KORA", sería aceptable. Pero como **auditoría de las specs** fracasa en lo esencial: (a) audita el sistema, no las specs, y no cita una sola spec; (b) no halla ni un defecto, recomendación ni severidad — es celebratorio, no diagnóstico; (c) no separa declarado de cumplido y, paradójicamente, es **menos riguroso que las propias specs**, que ya declaran la estructura con pérdida explícita y checks; (d) inventa estructura (el producto fibrado de estado de 4 vías) y la atribuye a una URN que no la contiene; (e) afirma una adjunción y una conmutatividad como cumplidas violando la cautela del corpus que cita. Es, en términos de la propia rúbrica, cercano al **functor constante hacia "todo bien"**: el grado máximo de infidelidad para una auditoría.

**One-liner:** Prosa categorial fluida y mayormente fiel al corpus, pero como auditoría de specs es el functor constante a "todo correcto" — audita el sistema en vez de la ley, no cita una sola spec, no halla un solo defecto, e inventa un producto fibrado de estado inexistente.
