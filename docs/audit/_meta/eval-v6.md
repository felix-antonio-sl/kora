# Meta-evaluacion — `auditoria-categorial-specs-v6-2026-06-07.md`

- **Slug:** v6
- **Objeto auditado por el reporte:** specs vigentes de KORA v6.0–v6.2 (gobernanza v6.2.0, harness-spec v1.1.0, autoria-spec v2.0.0, md-spec v12.0.0, knowledge-spec v3.0.0, transmutation-spec v1.2.0).
- **Metodo declarado:** opencode/glm-5.1 + skill `cat-thinking`, contra corpus ICAS-BoK (24 URNs).
- **Scope fit:** `specs` (correcto: el objeto auditado SON las specs, no "el sistema KORA en general").
- **Meta-evaluador:** Opus 4.8, contra corpus ICAS-BoK y specs vivas.

---

## Veredicto en una linea

Auditoria functorial genuina y bien anclada que halla dos fallas estructurales reales (A7, A15) y separa formal de heuristico de forma explicita, pero se desliza en tres falsos-amigos categoriales (faithful≠preserva-monos, seccion≠adjunto-izquierdo, subsheaf sin coverage) y sobre-formaliza una adjuncion `F ⊣ U` que el propio corpus que cita advierte tratar como "no literal".

**Veredicto global: solido.**

---

## Tabla de 9 dimensiones

| # | Dimension | Score | Sintesis |
|---|-----------|-------|----------|
| 1 | fidelidad_functorial | 4 | Traduccion fiel y estructurada; distingue funtor/seccion/adjuncion/bisimulacion. Pierde un punto por confundir faithful con mono-preservation (A13) y seccion con adjunto izquierdo (A2). |
| 2 | correccion_leyes | 3 | La mayoria de los claims son correctos; tres errores categoriales concretos (ver abajo). |
| 3 | formal_vs_heuristico | 4 | §6 declara explicitamente formal vs heuristico por conclusion; penaliza marcar F⊣U y "subsheaf" como Formal sin demostracion. |
| 4 | anclaje_trazabilidad | 4 | Cita URN icas-* Y la spec+seccion (`§`) por hallazgo. Falla: una atribucion factual erronea (atribuye "ortogonales" a harness-spec §5, que dice "complementarios"). |
| 5 | cobertura_completitud | 4 | Cubre las 6 specs nucleares, examina objetos Y morfismos. No toca qa-spec, procesos-spec, risk-register-spec, multiagente-spec, runtime-spec-md. |
| 6 | poder_diagnostico | 4 | Halla 2 fallas Alta falsables y accionables (A7, A15) + medias reales. No es celebratorio pese a varios "positiva". |
| 7 | accionabilidad | 4 | Cada hallazgo conecta finding→remedio→check; remedios concretos y priorizados por severidad. |
| 8 | parsimonia | 3 | Buena en general, pero A14/A9/A13 acumulan maquinaria (adjuncion implicita, Bool-enriquecimiento, monos en DocHumano) mas fuerte de lo que el material soporta. |
| 9 | coherencia_interna | 3 | Mayormente compone. Defectos: A5 se colapsa en A4 (linea 135) y reaparece como item propio en §7 (linea 335); A13 oscila entre "formal" (cuerpo) y "heuristico" (§6). |

**Score total: 33/45.**

---

## Verificacion de los claims mas fuertes (5)

### V1 — A7 "atlas ortogonales es impreciso" (severidad Alta) — PARCIALMENTE VERIFICADO, con error de atribucion

El reporte (lineas 148-157) afirma que **harness-spec §5 y autoria-spec §4.5** declaran los atlas "ortogonales"/"ejes independientes".

- **harness-spec §5 (linea 207):** el titulo real es "## 5. Tres atlas **complementarios**" y el cuerpo dice "Los atlas son **proyecciones semanticas**, no clasificaciones disjuntas." NO usa "ortogonales". harness-spec §5.1 (linea 226) ademas dice "los arneses son **clusters**, no particiones". Es decir, harness-spec ya emplea exactamente la terminologia que el reporte "recomienda".
- **autoria-spec §4.5 (linea 436):** el titulo SI es "### 4.5 **Ortogonalidad** de los tres atlas" y dice "Los tres atlas son **ejes independientes**". Pero el mismo §4.5 (linea 458) anota "Servicio — solo como agente-plataforma" y (linea 461) "No todas las combinaciones son realizables".
- **autoria-spec §6 (linea 681):** la fila `atlas.arnes_categorico` restringe arnes por forma material: `habilidad`→{utilidad,disciplina,delegado}, `agente-propiamente-tal`→{persona,orquestador}. Confirma la restriccion cruzada que el reporte invoca, incluido que `utilidad` queda excluida de `agente-propiamente-tal`.

**Conclusion:** la *tension* es real y bien diagnosticada (autoria-spec §4.5 afirma independencia mientras su §4.6 y §6 imponen restricciones), pero el reporte **misatribuye** el termino a harness-spec §5, que ya es preciso. El remedio "reemplazar en harness-spec §5" apunta a una spec que no contiene el error. Hallazgo valido en sustancia, mal calibrado en blanco.

### V2 — A15 "matriz organizada por forma_material, no por arnes" (severidad Alta) — VERIFICADO

autoria-spec §6 (linea 678) tiene columnas = las cuatro formas materiales y filas = campos del shape. autoria-spec §4.6 (lineas 469-471) declara explicitamente: "Skills y agents... son proyecciones operacionales del mismo objeto agentico, distinguidas por el arnes categorial." La doctrina (arnes = discriminante ontologico) y el enforcement (matriz §6 por forma material = proyeccion operacional) estan efectivamente desalineados. Hallazgo estructural real, falsable, bien dirigido. El propio §4.6 (lineas 502-506) admite el desfase: "las reglas condicionales por forma material que ya estan implicitas en el arnes se simplifican". Es el hallazgo mas fuerte del reporte.

### V3 — A2 + A14 "seccion del olvidadizo / adjuncion F⊣U / vector como unidad η" — MIXTO, contiene error categorial

- La observacion base de A2 (linea 104) es defendible: insertar `vector_ontologico` en el frontmatter es una **seccion** `s: KORA_IR → SerCat` con `U ∘ s = id` (inverso a derecha del olvidadizo). Correcto.
- **Error:** la recomendacion de A2 (linea 109) dice "Declarar que `vector_ontologico` es la unidad `η: Id → U ∘ s` de la adjuncion `F ⊣ U`." Por construccion `U ∘ s = id`, asi que `η: Id → U∘s` seria `η: Id → Id` = identidad — trivial y vacua. La unidad de `F ⊣ U` es `η: Id → U ∘ F` con **F el funtor libre, distinto de la seccion s**. El reporte conflaciona la seccion `s` con el adjunto izquierdo `F`. Falso-amigo: seccion ≠ adjunto izquierdo.
- A14 (lineas 229-240) postula `F ⊣ U` y la marca como "Formal (implicito)" en §6 (linea 322). El corpus que el propio reporte cita, `06-adjunciones` (lineas 108-112), advierte explicitamente que los pares free/forgetful aplicados (ORM, Docker) son "lectura estructural util pero no literal" y "rara vez una adjuncion exacta". El reporte afirma la adjuncion como formal sin esa cautela ni prueba de las identidades triangulares. Sobre-formalizacion contra la propia fuente.

### V4 — A4/A5 "bisimulacion modulo perdida" y orden de `≤` — VERIFICADO pero sobre-declarado como brecha

transmutation-spec §5 (lineas 182-184) **ya** dice: "La bisimulacion runtime es respecto a las observaciones que el runtime puede expresar... la bisimulacion es 'modulo esa proyeccion'." Es exactamente la reformulacion que A4 "recomienda" (linea 130: "preserva equivalencia observacional en la subcategoria de observaciones soportadas por R"). El reporte presenta como deficiencia algo que la spec ya enuncia. Sobre `≤` (A5): transmutation-spec linea 96 confirma `Lift_R ∘ T_R ≤ id (modulo atlas de encaje)`; harness-spec lineas 203-204 definen `≤` como orden componente-a-componente del lattice. La aclaracion que A5 pide es razonable pero menor; "modulo atlas de encaje" ya gesticula hacia ella. Hallazgo correcto, severidad bien puesta (Baja), pero el marco de "necesita precision" exagera la brecha real.

### V5 — A13 "koraficacion monada idempotente; FS=100% = faithful" — VERIFICADO en declaracion, con error categorial

md-spec §6 (lineas 513-518, 899) declara la koraficacion "fiel, comprimida, idempotente". El corpus `06-adjunciones` (linea 77) confirma que `g∘f` en un poset es un operador clausura (idempotente+extensivo) — la lectura monada idempotente/reflector es solida y bien anclada.

**Error:** A13 (linea 219) afirma "La condicion FS=100%... equivale a decir que K es **faithful** — preserva todos los monomorfismos." Esto conflaciona dos propiedades distintas. Segun el corpus `02-preservacion` (linea 106), faithful = la funcion **sobre morfismos** es inyectiva. "Preserva todos los monos" es una propiedad **diferente** (mono-preservation). Falso-amigo. Ademas hay tension interna: el cuerpo de A13 trata FS=100%=faithful como casi-formal, pero §6 (linea 320) lista "la koraficacion preserva todos los hechos" como **Heuristico (operativamente definido)**.

---

## Errores categoriales detectados

1. **faithful ≠ preserva-monos (A13, linea 219)** — severidad media. Confunde inyectividad sobre hom-sets (definicion de faithful, corpus 02 linea 106) con preservacion de monomorfismos.
2. **seccion ≠ adjunto izquierdo (A2, linea 109)** — severidad media. `η: Id → U∘s` con `U∘s=id` es trivial; la unidad de F⊣U es `η: Id → U∘F` con F≠s.
3. **F ⊣ U declarada "Formal" sin prueba ni cautela (A14/§6 linea 322)** — severidad media. El corpus citado (06 lineas 108-112) advierte que free/forgetful aplicado es "no literal" y "rara vez adjuncion exacta"; el reporte la asienta como formal.
4. **"subsheaf" sin coverage (A11/A12, §6 linea 321 "Formal")** — severidad baja. "Estrechar no relajar" mapea naturalmente a sub-presheaf/subobjeto; llamarlo **subsheaf** invoca la condicion de pegado y un site (corpus 12-topoi lineas 35-37) que el reporte no establece para extensiones de namespace.
5. **Error de atribucion factual (A7, linea 156)** — severidad baja (no es error categorial sino de lectura de fuente). Atribuye "ortogonales" a harness-spec §5, que dice "complementarios"; el termino vive solo en autoria-spec §4.5.

---

## Claims atomicos extraidos (con status)

| ID | Tema | Tipo | Statement (resumido) | Status |
|----|------|------|----------------------|--------|
| c1 | harness/capas | afirmacion-correccion | Las 4 capas con funtores entre ellas son una fibration (A1) | plausible |
| c2 | autoria-spec | hallazgo-falla | vector_ontologico es seccion del olvidadizo, no proyeccion (A2) | dudoso |
| c3 | transmutation-spec | afirmacion-correccion | T_R es el funtor mas explicito y correcto del sistema (A3) | verificado |
| c4 | transmutation-spec | hallazgo-falla | bisimulacion "modulo perdida" no es bisimulacion estandar (A4) | plausible |
| c5 | transmutation-spec | recomendacion | especificar `≤` como orden del lattice PMI×LFS (A5) | verificado |
| c6 | harness-spec | afirmacion-correccion | PMI×LFS es sub-poset del producto de lattices (A6) | verificado |
| c7 | autoria/harness | hallazgo-falla | "atlas ortogonales" es impreciso; hay restricciones cruzadas (A7) | plausible |
| c8 | knowledge-spec | hallazgo-falla | `refines` necesita antisimetrizacion / poset reflection (A8) | plausible |
| c9 | knowledge-spec | observacion | KnowCat es potencialmente Bool-enriquecida (A9) | dudoso |
| c10 | lifecycle | observacion | dos cadenas de lifecycle = dos poset-categories; CLI = funtor testigo (A10) | plausible |
| c11 | gobernanza | hallazgo-falla | precedencia es preorden, no orden total (A11) | verificado |
| c12 | gobernanza | observacion | extensiones de namespace son subsheaves del canon (A12) | dudoso |
| c13 | md-spec | hallazgo-falla | koraficacion = monada idempotente; "hecho" no es morfismo formal (A13) | plausible |
| c14 | harness/autoria | observacion | existe adjuncion implicita F ⊣ U entre IR y SerCat (A14) | dudoso |
| c15 | autoria-spec | hallazgo-falla | matriz §6 organizada por forma_material, no por arnes (A15) | verificado |
| c16 | md-spec | afirmacion-correccion | FS=100% equivale a K faithful (A13 cuerpo) | erroneo |
| c17 | autoria-spec | afirmacion-correccion | atribuye "ortogonales" a harness-spec §5 (A7) | erroneo |

---

## Fortalezas

- Triaje honesto (linea 48): declara que la auditoria es sustantiva por el vocabulario categorial explicito de las specs — no decorativa.
- Anclaje doble por hallazgo: URN icas-* + spec+seccion concreta. Yoneda respetado (el claim se conoce por sus referencias).
- §6 separa formal de heuristico explicitamente, e identifica correctamente como heuristicos los claims debiles (ortogonalidad, bisimulacion-estandar, orden-total-de-precedencia).
- Dos hallazgos Alta (A7, A15) son fallas estructurales reales, falsables y accionables, verificadas contra las specs vivas.
- No es celebratorio: pese a 6 hallazgos "positiva", el reporte localiza desalineacion doctrina/enforcement genuina.
- Cobertura de objetos Y morfismos (no solo enumera componentes): trata cites/depends/supersedes/refines como morfismos con algebra distinta.

## Debilidades

- Tres falsos-amigos categoriales (faithful=preserva-monos; seccion=adjunto-izquierdo; subsheaf sin coverage).
- Sobre-formaliza F⊣U como "Formal" contra la advertencia explicita del corpus que cita (06-adjunciones).
- Error de atribucion factual en A7 (harness-spec §5 ya dice "complementarios").
- Presenta como brecha (A4) una reformulacion que transmutation-spec §5 ya enuncia.
- Inconsistencia editorial: A5 colapsado en A4 (linea 135) reaparece como item en §7 (linea 335); A12 igual.
- Cobertura parcial: omite qa-spec, procesos-spec, risk-register-spec, multiagente-spec (sheaf operacional, directamente relevante a la lectura sheaf/subsheaf que el reporte intenta), runtime-spec-md.
