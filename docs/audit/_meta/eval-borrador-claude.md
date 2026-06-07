# Meta-evaluacion: `borrador-claude`

**Reporte evaluado:** `/home/felix/kora/docs/audit/2026-06-07-auditoria-categorial-specs-borrador-claude.md`
**URN:** `urn:kora:kb:auditoria-categorial-specs-borrador-claude`
**Autor declarado:** chiquito (Claude/Sonnet + skill `cat-thinking` v1.0.0)
**Objeto auditado por el reporte:** el estrato Spec de KORA (declara 14 specs vigentes; en realidad cubre ~23 docs con `family=spec` incluyendo deprecadas y runtime-extensions).
**Meta-evaluador:** Opus 4.8, metodo de 9 dimensiones + verificacion de 5 claims fuertes.

---

## 0. Encuadre

Una auditoria categorial es un functor `F: Cat(specs-KORA) -> Cat(vocabulario-categorial)`. La pregunta es cuan fiel/pleno es ese functor: ¿preserva la estructura real de las specs, o colapsa a "todo bien" (functor constante, infiel) o inventa estructura (no bien-definido)?

Este reporte es de los **fieles y criticos**: no celebra, halla deuda estructural, distingue lo declarado de lo cumplido, y casi siempre cita URN del corpus por hallazgo. Su problema principal no es la postura sino la **precision aritmetica de su claim central** (el conteo de leyes de transmutation) y algo de **decoracion categorial** en los tipos asignados a `gobernanza`.

---

## 1. Verificacion de los claims mas fuertes (5)

### V1 — "transmutation-spec: 2/8 leyes preservadas, 6 declaradas" → **ERRONEO**
El reporte afirma repetidamente (Hallazgo L, H3, tabla §5: *"declarado, no verificado (2/8 leyes)"*; conclusion: *"el funtor real tiene 2 leyes verificadas y 6 declaradas"*) que solo 2 de 8 leyes estructurales estan `preserved`.

El ejemplo canonico de `_transmutation.yml` en `runtime/transmutation-spec.md` (lineas 229-253) declara:
- `preserved`: composition, identity, pi_monotonicity, mu_monotonicity, xi_monotonicity = **5**
- `declared`: xi_naturality, safety_closure, kleisli_composition = **3**

Conteo mecanico confirmado: 5 preserved / 3 declared, no 2/6. La spec ademas separa explicitamente (§3.1) las leyes functoriales **basicas** (composition + identity = 2, cuya violacion "rompe la transmutacion, no es perdida") de las 6 de **preservacion estructural** (§3.2). El reporte parece haber confundido "2 leyes basicas de §3.1" con "2 leyes verificadas en total" y luego haber generalizado a un conteo global falso. El claim cuantitativo central — del que cuelga "no es un funtor, es un funtor parcial con deuda categorial" — esta **mal medido**. La *direccion* del diagnostico (parte de las leyes quedan declarativas) es correcta y valiosa; el *numero* es falso, y el numero es lo que el reporte pone en negrita en tres lugares.

### V2 — "transmutacion es funtor parcial con perdida documentada" (lente preservacion) → **VERIFICADO (lente), parcialmente mal aplicado (numero)**
La spec se autodeclara funtor (§2: *"La transmutacion es functor. Preserva composicion e identidad; la perdida se declara, nunca se oculta"*), declara dominio de definicion `D_R ⊆ KORA_IR` (lin. 73) y admite `Lift_R` solo "cuando es construible". El corpus `02-preservacion` dice textualmente: *"la mayoria de los functores que encuentro son fieles pero no plenos... el punto no es preservar todo, sino saber exactamente que se preserva y que no. Cada falla tiene un nombre y un remedio."* La lectura del reporte (funtor parcial / `T_R` estricto vs laxo, Hallazgo O sobre `D_R` y composicion que podria salir del dominio) es **fiel al corpus y bien aplicada**. Esta es la mejor pieza categorial del reporte. Solo la cuantificacion (V1) la contamina.

### V3 — "api_observable es Yoneda operativo; falta cerrar la conversa" (Hallazgo H) → **VERIFICADO**
`autoria-spec §3.5.1` se titula literalmente "API observable (Yoneda operativo)", cita `04-identidad-es-relacion`, y dice (lin. 294): *"Dos artefactos con el mismo api_observable son indistinguibles por cualquier caller."* El corpus 04 define el embedding de Yoneda como **plenamente fiel** y los presheaves representables como los que "vienen de objetos". El refinamiento del reporte — tratar la igualdad `api_observable` como **igualdad de representables, no de objetos**, y declarar la sub-categoria de observacion — es exactamente la distincion corpus (representables vs presheaves generales). Hallazgo solido, falsable y bien anclado.

### V4 — "multiagente-spec declara sheaf pero no declara el sitio (J)/topologia de Grothendieck" (Hallazgo R) → **VERIFICADO**
`multiagente-spec §3.1` declara `Ch = (Roles, Fases, Cover, Sec, Glue)` y la condicion de pegado (§3.2 / lin. 90), y se autodenomina "sheaf operacional". No declara una topologia de Grothendieck / sitio sobre el cual `Sec` sea presheaf y `Glue` lo haga sheaf. La observacion del reporte es correcta y verificable contra el texto. La distincion coreografia (sheaf) vs orquestacion (operad/wiring) tambien esta en la spec (§4, lin. 129) en prosa, como dice el reporte (Hallazgo S/H7). Buen anclaje a `12-topoi` y `08b-higher-categories`.

### V5 — "el grafo es aciclico por depends pero ciclico por cites; 21 ciclos" (H1) → **PARCIALMENTE VERIFICADO**
Los dos ciclos concretos citados son **reales** en el frontmatter:
- `autoria-spec ↔ qa-spec`: autoria cita qa-spec; qa-spec cita autoria-spec. Mutuo confirmado.
- `md-spec -> knowledge-spec -> autoria-spec -> md-spec`: las tres aristas existen. 3-ciclo confirmado.

Los `depends` apuntan todos hacia `gobernanza`/`harness`/`md-spec` (sin ciclos visibles). La estructura (cites ciclico, depends acerca a gobernanza) es correcta. El **numero "21"** no es verificable en detalle y es sospechoso de precision falsa. Mas grave: el sub-claim *"Hoy el toolchain trata `cites` como si fuera `depends` y eso es lo que produce el ruido"* (H1, parrafo final) **no se sostiene**: al construir el grafo (`kora graph --json`) hay **0 aristas Cites y 0 DependsOn originadas en los docs de spec vigentes** — el toolchain no procesa las relaciones de frontmatter de las specs al grafo en absoluto (las 863 Cites/148 DependsOn provienen de artefactos, no de specs). Esto *confirma* el Hallazgo H6 del propio reporte ("las specs no se auditan a si mismas en kb-graph") pero *contradice* su H1 ("el toolchain trata cites como depends"). Inconsistencia interna entre H1 y H6.

---

## 2. Tabla de scores (9 dimensiones, 0-5)

| # | Dimension | Score | Evidencia |
|---|-----------|-------|-----------|
| 1 | fidelidad_functorial | 4 | Distingue funtor/funtor-parcial (Hallazgo L,O), monada/pipeline, Yoneda/igualdad (H), sheaf/site (R), 1-cat/2-cat (S,H7). No colapsa a "todo bien". Resta: gobernanza recibe tres tipos a la vez (terminal + counit + functor constante) sin desambiguar — colapso decorativo de falsos amigos. |
| 2 | correccion_leyes | 2 | El claim categorico cuantitativo central (2/8 preserved en transmutation) es **FALSO**: el ejemplo canonico tiene 5/3. Errores menores: gobernanza como "counit" no construido; "21 ciclos" no verificable; H1 vs H6 se contradicen. Aciertos: ciclos cites concretos correctos, Yoneda correcto. |
| 3 | formal_vs_heuristico | 4 | Declara cuando algo es "declarado vs preservado", "en prosa, no axiomatizado", "aspiracional", usa la tabla de salud para separar `si`/`parcial`/`declarado-no-verificado`. Cumple la regla dura. Resta: presenta el conteo erroneo como hecho duro (negrita) sin verificarlo. |
| 4 | anclaje_trazabilidad | 5 | Casi todo hallazgo cierra con URN `icas-*` especifica y la URN KORA de la spec; §2 mapea cada pieza del corpus a su rol; §6 prioriza con cita categorial. Anclaje ejemplar y por-hallazgo. |
| 5 | cobertura_completitud | 5 | Audita el objeto correcto (las specs, no "el sistema"); recorre objetos Y morfismos (depends/cites/supersedes, promocion, composicion); 23 hallazgos por spec + 10 transversales + deprecadas + namespace foraneo. Scope impecable. |
| 6 | poder_diagnostico | 4 | Hallazgos estructurales reales y falsables (Yoneda conversa, sitio del sheaf, D_R no cerrado, filename load-bearing vs §2, redireccion sin test). No es celebratorio. Resta: el hallazgo "estrella" (2/8) es un falso positivo de severidad inflada por mala medicion. |
| 7 | accionabilidad | 4 | 12 recomendaciones priorizadas, cada una con categoria y URN; conecta hallazgo->remedio. Resta: "enderezables en 2-3 sprints" sin desglose; algunas recos (R1 perfil de cumplimiento) ya estan parcialmente en la spec (§6.1/§6.3 ya pide las 8 filas con status). |
| 8 | parsimonia | 3 | En general usa la maquinaria minima. Pero sobre-tipa gobernanza (counit+terminal+functor constante), invoca fibracion/sitio/2-poset donde a veces basta "grafo con dos relaciones tipadas", y propone formalismos (Lawvere theory, nerve, comonoide) sin mostrar el trabajo que justifique la maquinaria. Jerga ocasionalmente decorativa. |
| 9 | coherencia_interna | 3 | Mayormente compone. Dos roturas: (a) H1 ("toolchain trata cites como depends") vs H6 ("specs no estan en kb-graph") son incompatibles; (b) el conteo 2/8 contradice la propia logica del reporte (que sabe que hay 6 leyes estructurales + 2 basicas). |

**score_total = 4+2+4+5+5+4+4+3+3 = 34 / 45**

---

## 3. Claims atomicos extraidos (con status)

1. (Hallazgo L/H3/§5) transmutation tiene 2/8 leyes preservadas y 6 declaradas — **erroneo** (canonico: 5/3).
2. (Hallazgo L/O) `T_R` es funtor parcial con dominio `D_R`; conviene distinguir `T_R` estricto vs laxo — **verificado** (spec declara D_R y `status: declared`).
3. (Hallazgo M) `Lift_R ⊣ T_R` declarada pero ningun runtime la construye verificadamente — **verificado** (spec lin. 92-102: "no todos los runtimes tienen Lift_R").
4. (Hallazgo H) `api_observable` = Yoneda operativo; falta declarar la conversa / sub-categoria de observacion — **verificado**.
5. (Hallazgo R/H7/S) multiagente declara sheaf y distingue coreografia/orquestacion en prosa, pero no declara el sitio (J) ni la 2-categoria — **verificado**.
6. (H1) ciclos por `cites` reales: `autoria↔qa`, `md->knowledge->autoria->md` — **verificado** (frontmatter).
7. (H1) "21 ciclos" totales — **dudoso** (no verificable, precision sospechosa).
8. (H1) el toolchain trata `cites` como `depends` y eso produce ruido — **erroneo** (toolchain no mete relaciones de spec al grafo; 0 aristas spec->spec).
9. (H6) kb-graph no incluye las specs como nodos de primera clase con su grafo — **verificado** (0 Cites/DependsOn desde docs spec).
10. (Hallazgo F/H5) el path (`skills/` vs `agents/`) no debe implicar forma material; solo el frontmatter decide; el check acopla filename↔forma_material — **plausible** (el check `construction-source-primary` cruza `path.name` con `forma_material`; pero lo *cruza*, no "decide schema desde path antes de leer frontmatter": mecanismo descrito impreciso, tension real).
11. (Hallazgo I/V) `qa_budget` solo puede igualar o estrechar `Σ` = morfismo de subobjetos en `[0,1]^5` — **verificado** (autoria-spec §3.5.2 delega a qa-spec; consistente).
12. (Hallazgo U/H9) `⊗` monoidal en `[0,1]^5` no axiomatiza asociatividad; si es min/media geometrica no es monoidal categorico estandar — **plausible** (la spec no exhibe la ley; observacion razonable, no verifique el texto de qa-spec a fondo).
13. (Hallazgo G/H8) la cadena de formas materiales deberia tener adjuncion libre/counit explicito; democion prohibida = perdida no functorial — **plausible** (autoria-spec §8.1-8.2 confirma promocion preserva URN + bump major + democion prohibida; el "deberia ser adjuncion libre" es propuesta, no defecto demostrado).
14. (Hallazgo C) cambio de runtime canonico se hizo como punto en gobernanza, no como ADR archivado — **plausible** (no verificado; recomendacion de higiene razonable).
15. (Hallazgo Z) `salubrista-openclaw-spec` vive en namespace `agengai` y necesita ADR — **plausible**.
16. (gobernanza) gobernanza = objeto terminal + counit + functor constante del sistema — **dudoso** (tres tipos categoriales distintos conflados; el reporte hedge "no topologico" pero no construye ningun counit).

**Citas de corpus correctas** (URNs efectivamente usadas por el reporte y pertinentes): icas-preservacion, icas-identidad-relacion, icas-topoi, icas-adjunciones, icas-enriquecimiento, icas-universales, icas-higher-categories, icas-lifecycle, icas-efectos, icas-composicion, icas-escala, icas-composicion-estructura, icas-extension.

---

## 4. Errores categoricos detectados

| Claim | Problema | Severidad |
|-------|----------|-----------|
| "transmutation: 2/8 leyes preservadas, 6 declaradas" (negrita en L, H3, §5, conclusion) | Conteo falso. El ejemplo canonico de la spec tiene 5 preserved / 3 declared. Inflacion de severidad por mala medicion del claim central. | alta |
| "el toolchain trata `cites` como si fuera `depends` y eso produce el ruido" (H1) | El toolchain no inyecta ninguna relacion de spec al grafo (0 aristas spec->spec). Contradice ademas el propio H6. | media |
| gobernanza = "objeto terminal" + "counit" + "functor constante" simultaneamente | Tres nociones categoriales distintas asignadas a un mismo documento sin construir ninguna; falso-amigo / decoracion. El hedge "no topologico" no salva la imprecision. | baja |
| "21 ciclos detectados" | Precision numerica no verificable; los ejemplos son correctos pero el total parece fabricado. | baja |

---

## 5. Fortalezas

- Anclaje por-hallazgo a URN del corpus y a la spec concreta: ejemplar (dimension 4 = 5).
- Scope correcto y completo: audita las specs (no "el sistema"), objetos y morfismos, 23+10 hallazgos + deprecadas + namespace foraneo (dimension 5 = 5).
- Postura critica genuina: la lente "funtor parcial con perdida documentada" es fiel al corpus 02-preservacion y diagnostica deuda real.
- Hallazgos Yoneda (H), sitio del sheaf (R), 2-categoria de coreografia (S/H7) y filename load-bearing (F/H5) son falsables, correctos y accionables.
- Honestidad declarativa: separa "preservado/declarado/en prosa/aspiracional" en casi todo el texto.

## 6. Debilidades

- El claim cuantitativo estrella (2/8) es falso y esta en negrita en cuatro lugares: erosiona la credibilidad de la pieza mas fuerte.
- Incoherencia H1 vs H6 sobre que hace el toolchain con `cites`.
- Sobre-tipado de gobernanza y maquinaria ocasionalmente decorativa (Lawvere theory, nerve, comonoide) sin mostrar el trabajo (parsimonia).
- Algunas "recomendaciones" piden algo que la spec ya tiene parcialmente (R1 vs §6.1/§6.3 de transmutation, que ya exige las 8 filas con status).

---

## 7. Veredicto

**solido.** Es una auditoria genuinamente categorial, fiel al corpus, con scope correcto, anclaje ejemplar y criticidad real — claramente por encima del functor constante. Lo que la baja de "ejemplar" a "solido" es un error de medicion en su claim central (2/8 vs 5/3 real en transmutation), una contradiccion interna H1/H6, y decoracion categorial puntual sobre gobernanza. Corregido el conteo y resuelta la incoherencia, seria un reporte de primer nivel.

**Una linea:** functor fiel y critico de las specs, con anclaje y scope ejemplares, pero su hallazgo estrella sobre transmutation esta mal contado (2/8 cuando es 5/3) y H1 se contradice con H6.
