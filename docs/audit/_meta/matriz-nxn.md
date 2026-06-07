# Matriz NxN — Meta-evaluacion de 8 auditorias categoriales de las specs KORA

Fecha: 2026-06-07. Objeto de esta meta-evaluacion: las **relaciones entre las 8
auditorias** (no entre las specs). Cada auditoria es un funtor `F_i: Cat(specs) -> Cat(lectura categorial)`;
la matriz clasifica la relacion entre cada par `(F_a, F_b)`.

## Contexto minimo

KORA es un repositorio/catalogo/fabrica de artefactos para sistemas LLM
(conocimiento `.md`, agentes `AGENT.md`, skills `SKILL.md`). Las **specs no son
artefactos**: son la ley que define que cuenta como artefacto valido, y viven en
`governance/` `ontology/` `serialization/` `runtime/`. El **corpus ICAS-BoK** son
24 piezas de teoria de categorias (URNs `urn:fxsl:kb:icas-*`). Una auditoria
categorial de calidad debe: traducir las specs al vocabulario categorial
preservando estructura, verificar leyes, distinguir lo *declarado* de lo
*cumplido*, citar URNs por conclusion, y producir hallazgos falsables. Las 7
auditorias `scope_fit=specs` auditan ese objeto; la octava (`gemini`) audita el
sistema en general, lo que la vuelve **ortogonal** a las demas casi por
construccion.

## Insumo cuantitativo (score_total / 45 y scope)

| # | slug | score | scope | veredicto | eje fuerte | eje debil |
|---|------|-------|-------|-----------|------------|-----------|
| 1 | borrador-claude | 34 | specs | solido | anclaje (5), cobertura (5) | correccion-leyes (2) |
| 2 | report-b1e84abd | 39 | specs | solido | fidelidad/formal/anclaje/accion (5) | coherencia (3) |
| 3 | report-a3f7c2e1 | 35 | specs(4) | solido | accionabilidad (5) | coherencia (3), leyes (3) |
| 4 | deep | 44 | specs(7) | ejemplar | todo en 5 salvo cobertura (4) | cobertura (4) |
| 5 | gemini | 14 | **sistema** | deficiente | (ninguno alto) | diagnostico (0), accion (0) |
| 6 | v6 | 33 | specs(6) | solido | A7/A15 reales | leyes (3), coherencia (3), parsimonia (3) |
| 7 | v7-0607 | 32 | specs(8) | solido | cobertura (4), accion (4) | diagnostico (2) |
| 8 | v7-0608 | 32 | specs(8) | solido | tesis verificacion correcta | leyes (3), coherencia (3) |

Orden canonico (filas y columnas de la matriz NxN):
`borrador-claude, report-b1e84abd, report-a3f7c2e1, deep, gemini, v6, v7-0607, v7-0608`.

## Matriz NxN (triangular superior, 28 pares)

Leyenda de relaciones: **CC** concuerda, **SB** subsume, **CP** complementa,
**DV** diverge, **XX** contradice, **OR** ortogonal. La diagonal es la identidad
(autorrelacion, no se clasifica).

| a \\ b | borrador-claude | b1e84abd | a3f7c2e1 | deep | gemini | v6 | v7-0607 | v7-0608 |
|---|---|---|---|---|---|---|---|---|
| **borrador-claude** | — | CP | CP | DV | OR | CP | CP | CP |
| **b1e84abd** | | — | CC | CC | OR | CP | CP | CC |
| **a3f7c2e1** | | | — | DV | OR | CP | CP | CC |
| **deep** | | | | — | OR | SB | SB | SB |
| **gemini** | | | | | — | OR | OR | OR |
| **v6** | | | | | | — | CP | CP |
| **v7-0607** | | | | | | | — | CP |
| **v7-0608** | | | | | | | | — |

## Notas por celda (los 28 pares)

### Fila borrador-claude

1. **borrador-claude x b1e84abd — complementa.** Mismo objeto (la categoria Spec)
   y misma familia de hallazgo central (deuda functorial en transmutation), pero
   cubren sub-zonas distintas con metodos distintos: borrador recorre la categoria
   de morfismos spec->spec (depends/cites/supersedes, ciclos, kb-graph), b1e84abd
   ancla a la Formal Layer 00/01/05 y a evidencia verbatim de `_transmutation.yml`.
   No concuerdan como CC porque borrador comete el error 2/8 que b1e84abd no
   comete, y b1e84abd profundiza la verificacion mecanica que borrador solo
   enuncia. Utiles juntas: la lectura de morfismos de borrador + la evidencia
   literal de b1e84abd se suman sin chocar.

2. **borrador-claude x a3f7c2e1 — complementa.** Ambas atacan la matriz de
   preservacion de transmutation como hallazgo critico (borrador H/L/H3, a3f7c2e1
   H7). a3f7c2e1 es mas estrecha (4 specs nucleo) pero entra al detalle de
   `status: declared` con line-anchors; borrador es mas ancha (23 docs, incl.
   deprecadas y namespace foraneo) y aporta los morfismos. Cada una comete un
   error que la otra no (borrador: 2/8 falso; a3f7c2e1: H8 asociatividad
   fabricada), asi que no es subsuncion ni concordancia, sino cobertura
   complementaria con defectos disjuntos.

3. **borrador-claude x deep — diverge.** Mismo objeto, lecturas categoriales
   distintas del punto mas caliente: borrador lee `Lift_R ⊣ T_R` como adjuncion
   declarada-no-construida (deuda de adjuncion 1-categorial), deep la re-tipa como
   **conexion de Galois sobre el reticulo** (icas-adjunciones), un objeto
   categorial distinto. No es contradiccion estricta (Galois es un caso de
   adjuncion entre posets), pero el diagnostico y el remedio cambian de naturaleza.
   Ademas deep no comete el error 2/8 de borrador ni la incoherencia H1-vs-H6.
   Divergen en rigor y en la maquinaria elegida.

4. **borrador-claude x gemini — ortogonal.** Auditan objetos distintos: borrador
   audita las specs (23 docs nombrados); gemini audita el sistema/arquitectura y
   no cita una sola spec (grep verificado = 0 hits). No comparten dominio
   evaluable; la relacion es ortogonalidad de objeto, no de lectura.

5. **borrador-claude x v6 — complementa.** Las dos son auditorias functoriales
   genuinas de specs con buen anclaje, pero pegan en sub-categorias distintas:
   borrador en la categoria de morfismos spec->spec y en transmutation; v6 en la
   desalineacion doctrina/enforcement (A15: matriz por forma_material vs arnes-
   discriminante) y en el lattice de precedencia. No chocan; v6 aporta el hallazgo
   A15 que borrador no toca, y borrador aporta la lectura Yoneda/sheaf/2-categoria
   que v6 no desarrolla.

6. **borrador-claude x v7-0607 — complementa.** Cobertura solapada (ambas amplias)
   pero diagnosticos de distinta agresividad: borrador encuentra fallas (con un
   error de conteo); v7-0607 es de bajo poder diagnostico (0 criticas, hallazgo
   fantasma de cites). Se complementan porque v7-0607 cubre las 8 specs con
   honestidad de falsos-amigos y borrador aporta profundidad de morfismos; juntas
   dan amplitud + profundidad sin contradecirse en el fondo.

7. **borrador-claude x v7-0608 — complementa.** Caso notable: **comparten el mismo
   tipo de defecto falsable sobre el numero clave de transmutation pero en
   direccion opuesta**. borrador dice "2/8 preservadas" (confunde las 2 leyes
   basicas con el total); v7-0608 dice "5/8 declared, 3 preserved" (invierte el
   5-vs-3 canonico que es 5 preserved / 3 declared). Ambas yerran la cifra
   bandera; el valor real (5 preserved / 3 declared) no lo da ninguna. Por lo demas
   cubren zonas distintas (borrador: morfismos+kb-graph; v7-0608: objetos zombie
   canario/procesos, hermes stub). Complementan en cobertura, coinciden en el
   sintoma del error de conteo.

### Fila report-b1e84abd

8. **b1e84abd x a3f7c2e1 — concuerda.** Casi una transformacion natural
   `F_b1e84abd => F_a3f7c2e1` en el hallazgo central: ambas identifican que la
   matriz de preservacion de transmutation marca `xi_naturality` (y companeras)
   como `status: declared`, no `preserved`, y aplican el mismo lema del corpus
   ("functor sin verificacion mecanica = funcion con intencion"). Mismo line-anchor
   (l.236-248), misma severidad ALTA, misma lectura. Difieren solo en cobertura
   (b1e84abd 8 specs + Formal Layer; a3f7c2e1 4 nucleo) y en que a3f7c2e1 ensucia
   con H8 fabricado. El nucleo concuerda fuertemente.

9. **b1e84abd x deep — concuerda.** Las dos auditorias de mayor calidad (39 y 44)
   convergen en la tesis: el gap es de **verificacion**, no de diseno; las leyes
   functoriales estan declaradas pero no exhibidas con instancias. Ambas tratan la
   distincion `preserved`/`declared` de `_transmutation.yml` como el activo de
   integridad intelectual del sistema. Concuerdan en lectura y en honestidad
   formal/heuristico. Diferencia fina: deep tipa la adjuncion como Galois (mas
   preciso) y b1e84abd la deja como adjuncion lax aplanada a igualdad triangular
   (D2); pero la conclusion operativa es la misma -> CC, no DV.

10. **b1e84abd x gemini — ortogonal.** b1e84abd audita las specs con evidencia
    verbatim; gemini audita el sistema sin citar specs y es celebratorio (0
    hallazgos). Objetos distintos; ademas posturas opuestas (b1e84abd halla deuda
    real, gemini no halla nada), pero no es XX porque no hablan del mismo objeto:
    es ortogonalidad de dominio.

11. **b1e84abd x v6 — complementa.** Ambas specs-scope y functoriales, pero
    b1e84abd centra en verificacion de leyes (Xi-naturality, round-trip) y v6 en
    desalineacion doctrina/enforcement (A15) y precedencia como preorden. b1e84abd
    evita falsos-amigos; v6 comete tres (faithful=monos, seccion=adjunto, subsheaf).
    Se complementan: v6 aporta A7/A15, b1e84abd aporta la red de verificacion y la
    Formal Layer. Convergen en transmutation pero no es CC porque la calidad y el
    set de hallazgos difieren bastante.

12. **b1e84abd x v7-0607 — complementa.** Mismo set de 8 specs (cobertura pareja),
    pero b1e84abd tiene poder diagnostico alto (halla deuda critica verificada) y
    v7-0607 bajo (0 criticas). Ambas comparten la virtud de no fabricar falsos-
    amigos. Complementan: v7-0607 da la lectura amplia y prudente, b1e84abd la
    profundidad diagnostica. No CC porque v7-0607 no llega al hallazgo critico que
    b1e84abd verifica.

13. **b1e84abd x v7-0608 — concuerda.** Misma tesis central palabra por palabra:
    "la deuda critica es de verificacion mecanica, no doctrinal". Ambas anclan a
    icas-preservacion y a la regla de la propia transmutation-spec §6.3. La
    diferencia decisiva: b1e84abd cita la cifra correcta implicitamente y v7-0608
    la **invierte** (5 declared / 3 preserved). El meta-eval nota explicitamente
    que v7-0608 "compara por debajo del sibling cat-thinking (eval-report-b1e84abd,
    39/45)". Son la misma lectura (CC) con v7-0608 como version mas ruidosa y con
    un error falsable que b1e84abd evita; concuerdan en el funtor, divergen en
    fidelidad de un dato.

### Fila report-a3f7c2e1

14. **a3f7c2e1 x deep — diverge.** Comparten el hallazgo H7/C6 verdadero (T_R no
    verificado sobre morfismos) pero divergen en disciplina categorial: deep es
    ejemplar (0 claims falsos, formal/heuristico/metaforico sistematico), mientras
    a3f7c2e1 fabrica H8 (no-asociatividad inexistente en §10), sobre-atribuye H4 al
    corpus y comete un falso-amigo en su propia prosa (§3.2, Pi>=3=>Mu>=1 como
    "transformacion natural"). Es el mismo objeto leido con dos niveles de rigor
    distintos y con un hallazgo fabricado de un lado: diverge, no concuerda.

15. **a3f7c2e1 x gemini — ortogonal.** a3f7c2e1 audita 4 specs nucleo con
    line-anchors; gemini audita el sistema sin citar specs. Objetos distintos ->
    ortogonal.

16. **a3f7c2e1 x v6 — complementa.** Ambas specs-scope solidas (35 y 33) con un
    rasgo compartido incomodo: **las dos cometen un falso-amigo en su propia prosa**
    (a3f7c2e1: naturalidad espuria en §3.2; v6: faithful=monos, seccion=adjunto).
    Pero cubren zonas distintas: a3f7c2e1 transmutation+autoria+Yoneda; v6
    precedencia+doctrina/enforcement (A15)+md-spec. Complementan en cobertura y
    comparten el patron de resbalon, sin chocar en conclusiones.

17. **a3f7c2e1 x v7-0607 — complementa.** Ambas tienen accionabilidad fuerte
    (tablas priorizadas con remedio y severidad). a3f7c2e1 es mas agresiva (halla,
    aunque fabrica H8); v7-0607 es prudente pero sub-diagnostica. Complementan:
    a3f7c2e1 entra mas hondo en transmutation/autoria, v7-0607 da la cobertura de
    las 8 specs sin fabricar. No CC por la diferencia de agresividad y por H8.

18. **a3f7c2e1 x v7-0608 — concuerda.** Convergen en el hallazgo bandera (matriz
    de preservacion con `status: declared` como deuda critica verificada;
    a3f7c2e1 H7, v7-0608 R-D1). Ambas son specs-scope, ambas accionables, ambas
    con un error falsable en lo ruidoso (a3f7c2e1: H8 fabricado; v7-0608: 5-vs-3
    invertido). La lectura categorial del nucleo es la misma -> CC, con la salvedad
    de que cada una arrastra un defecto distinto.

### Fila deep

19. **deep x gemini — ortogonal.** Maxima distancia del conjunto. deep audita las
    specs como ley con disciplina ejemplar; gemini audita el sistema, no cita una
    spec, no halla un defecto e inventa estructura (`U_phen x U_ctx x U_epi x U_sta`).
    Objetos distintos (ortogonal por definicion) y ademas posturas opuestas (deep
    diagnostica, gemini celebra). El par deep-gemini es el contraste de referencia:
    el mejor funtor fiel vs. el funtor constante a "todo correcto".

20. **deep x v6 — subsume.** deep (44) cubre lo que v6 (33) cubre y mas, con mayor
    rigor: ambas tocan la adjuncion/conexion de transmutation, el lattice/poset
    PMI x LFS y el sheaf de multiagente, pero deep tipa **correctamente** lo que v6
    **falsea** (deep: Galois en vez de adjuncion 1-categorial, sin cometer
    faithful=monos; v6 comete los tres falsos-amigos). La unica zona donde v6
    aporta algo que deep no profundiza es la matriz A15 por forma_material; pero
    deep cubre el mismo territorio doctrinal con autoria-spec §4.6 y lo hace sin
    error. Cobertura+profundidad de deep >= v6 en casi todo -> subsume.

21. **deep x v7-0607 — subsume.** deep (44) >= v7-0607 (32). Ambas separan
    formal/heuristico y evitan falsos-amigos groseros, pero deep tiene poder
    diagnostico alto (hallazgos Galois, sitio del sheaf, Functor K metaforico) y
    v7-0607 lo tiene debil (0 criticas, hallazgo fantasma de cites, checklist de
    14 que confunde declarado con cumplido). v7-0607 audita 8 specs y deep 7, asi
    que v7-0607 tiene una pizca mas de cobertura nominal; pero en todo lo demas
    (rigor, diagnostico, parsimonia, ausencia de error) deep domina. Subsume con
    la salvedad menor de la cobertura nominal.

22. **deep x v7-0608 — subsume.** deep (44) >= v7-0608 (32). Comparten la tesis
    correcta (deuda de verificacion) y la valoracion de `preserved`/`declared`,
    pero v7-0608 **invierte la cifra** (5-vs-3) y trata gemini/mastra como
    canonicos siendo archivados, errores falsables que deep no comete. deep ademas
    tipa la adjuncion como Galois (v7-0608 la sobre-formaliza como "Formal" sin
    probar identidades triangulares). deep contiene la lectura de v7-0608 corregida
    y mas profunda -> subsume.

### Fila gemini

23. **gemini x v6 — ortogonal.** v6 audita specs; gemini audita el sistema.
    Objetos distintos -> ortogonal.

24. **gemini x v7-0607 — ortogonal.** v7-0607 audita las 8 specs; gemini audita el
    sistema sin citarlas. Ortogonal de dominio.

25. **gemini x v7-0608 — ortogonal.** v7-0608 audita specs (con cifras, aunque
    invertidas); gemini audita el sistema y no cita specs. Ortogonal. (Nota: ambos
    tocan la transmutation, pero gemini la afirma como functor pleno/conmutativo
    -celebratorio- y v7-0608 la critica como deuda; aun asi no comparten objeto
    auditado, por lo que prima la ortogonalidad de scope sobre una contradiccion
    puntual.)

### Fila v6

26. **v6 x v7-0607 — complementa.** Par muy informativo: **auditan casi el mismo
    objeto pero discrepan en severidad de la MISMA desalineacion**. La matriz §6 de
    autoria-spec organizada por forma_material vs. doctrina arnes-discriminante es,
    para v6, su hallazgo HIGH mas fuerte (A15); para v7-0607, gradado BAJA (el
    meta-eval lo marca como falla de v7-0607). No es contradiccion factual (ambas
    ven la tension), es divergencia de juicio de severidad dentro de cobertura
    solapada -> complementa con tension de severidad. v6 aporta agresividad
    diagnostica, v7-0607 aporta limpieza de falsos-amigos.

27. **v6 x v7-0608 — complementa.** Ambas specs-scope solidas con un error falsable
    cada una: v6 sobre-formaliza la adjuncion `F⊣U` como "Formal" contra el corpus;
    v7-0608 sobre-formaliza `Lift_R ⊣ T_R` como "Formal" igual y ademas invierte el
    5-vs-3. Comparten el patron "sobre-formalizar una adjuncion contra la
    advertencia de icas-adjunciones", pero pegan en zonas distintas (v6: precedencia,
    A15, md-spec; v7-0608: objetos zombie canario/procesos, hermes stub).
    Complementan en cobertura, coinciden en el anti-patron de adjuncion-sin-prueba.

### Fila v7-0607

28. **v7-0607 x v7-0608 — complementa.** Mismo nombre de archivo "v7" y misma
    skill (cat-thinking) pero, como nota el meta-eval, **no son iteracion uno del
    otro**: v7-0607 es OpenCode/kimi-k2.6 y v7-0608 es un documento cat-thinking
    distinto y mas agresivo. v7-0607 es prudente y sub-diagnostico (0 criticas);
    v7-0608 declara Criticas y halla objetos zombie reales, pero invierte la cifra
    de transmutation. Cubren las 8 specs ambos pero con temple opuesto: v7-0607
    conservador y limpio, v7-0608 agresivo y con un error falsable. Complementan:
    juntos delimitan el rango entre prudencia-sin-hallazgos y agresividad-con-ruido.

## Ranking global (rank 1 = mejor)

1. **deep (44)** — Auditoria ejemplar. Funtor fiel y pleno: separa
   formal/heuristico/metaforico como eje vertebral (no decoracion), ancla con URN
   + numero de linea, y **no comete un solo falso-amigo** (al contrario, diagnostica
   el de la adjuncion correctamente como conexion de Galois). 5 verificaciones, 0
   claims falsos. Unico costo: cobertura no exhaustiva (no abre la Formal Layer
   oficial ni 05-governance-lattice). Es la unica con veredicto "ejemplar".

2. **report-b1e84abd (39)** — La mejor del resto. Hallazgo central correcto y
   verificado ("el gap es de verificacion, no de diseno"; Xi-naturality como deuda
   citada verbatim), distincion formal/heuristico ejemplar, anclaje doble, alta
   accionabilidad, sin fabricar estructura. La lastra una contradiccion interna
   F1-vs-D11 (la aciclicidad de refines SI esta enforced por relations-laws), un
   falso positivo, no un error de teoria.

3. **report-a3f7c2e1 (35)** — Solida y mayormente fiel, con H7 verdadero y
   accionabilidad ejemplar (remedio bifurcado por hallazgo). Cae al puesto 3 por
   un hallazgo **fabricado** (H8: no-asociatividad inexistente en §10, grep
   verificado = 0), un overclaim de anclaje (H4) y un falso-amigo en su propia
   prosa (§3.2). Fabricar un defecto es mas grave que omitir uno, lo que la pone
   bajo borrador pese al score cercano.

4. **borrador-claude (34)** — Anclaje y scope ejemplares (audita morfismos, no solo
   objetos; recorre 23 docs incl. deprecadas y namespace foraneo), lente
   "funtor parcial con perdida documentada" fiel al corpus. Pero su **hallazgo
   estrella esta mal contado** (afirma 2/8 leyes preservadas en transmutation
   cuando el ejemplo canonico tiene 5/3) y tiene una incoherencia interna H1-vs-H6
   sobre que hace el toolchain con cites. El error toca el claim central, no uno
   periferico.

5. **v6 (33)** — Auditoria functorial genuina que halla **dos fallas estructurales
   reales** (A7 y, sobre todo, A15: matriz por forma_material vs arnes-discriminante,
   el hallazgo HIGH mas fuerte de todo el conjunto). La bajan tres falsos-amigos
   categoriales (faithful=preserva-monos, seccion=adjunto-izquierdo, subsheaf sin
   coverage) y una sobre-formalizacion de `F⊣U` contra el corpus que cita. Hallazgo
   sustantivo fuerte, ejecucion categorial con resbalones.

6. **v7-0608 (32)** — Tesis central correcta (deuda de verificacion) y hallazgos
   estructurales reales (objetos zombie canario/procesos, hermes stub). Pero sus
   dos hallazgos Critica mas ruidosos tienen **errores falsables**: cuenta
   declared/preserved invertida (5-vs-3) y gemini/mastra contados como canonicos
   siendo archivados. Empata en score con v7-0607 pero los errores tocan los
   hallazgos bandera.

7. **v7-0607 (32)** — Cobertura amplia (8 specs), sin falsos-amigos groseros, bien
   anclada y parsimoniosa. Su falla es el **poder diagnostico debil**: 0 criticas,
   un checklist de 14 "satisfecha" que confunde declarado con cumplido (deriva al
   functor constante), un hallazgo fantasma (cites, ya declarado en knowledge-spec
   §6.3) y una staleness sub-dimensionada. Honesta pero tibia; queda bajo v7-0608
   por aportar menos hallazgos reales pese a no invertir cifras.

8. **gemini (14)** — Deficiente como auditoria de specs. **Audita el objeto
   equivocado** (el sistema, no la ley), no cita una sola spec, no halla un solo
   defecto (functor constante a "todo correcto", anti-patron Goodhart), no declara
   formal vs heuristico en ningun punto (regla dura violada) e **inventa estructura**
   atribuida al corpus (`U_phen x U_ctx x U_epi x U_sta`, inexistente). Su unico
   merito es reproducir con fidelidad el resultado de icas-agencia (plan=free monad,
   ejecutor=cofree comonad), pero eso es recitar el corpus, no auditar.

## Convergencia (donde TODAS coinciden)

Considerando las 7 auditorias `scope=specs` mas el caso gemini donde aplica:

- **La transmutation-spec es el centro de gravedad de toda auditoria.** Las 8
  (incluida gemini, que la trata) hacen de `T_R` y su matriz de preservacion el
  objeto mas comentado. Es el unico punto que aparece en los 8 reportes.
- **Entre las 7 specs-scope: la deuda critica del sistema es de VERIFICACION, no
  de diseno.** Todas concluyen que las leyes functoriales/adjunciones estan
  *declaradas* pero no *exhibidas con instancias ni enforced mecanicamente*
  (`status: declared`, `requires runtime review`). Deep, b1e84abd y v7-0608 lo
  dicen explicitamente; a3f7c2e1 (H7), borrador (H/L), v6 (A14) y v7-0607 (T_R) lo
  implican. gemini es la excepcion: niega la deuda.
- **Entre las 7 specs-scope: el corpus es vinculante por hallazgo.** Todas anclan
  conclusiones a URNs `urn:fxsl:kb:icas-*` (icas-preservacion y icas-adjunciones
  aparecen en las 7; icas-agencia y icas-composicion casi siempre). El anclaje a
  corpus es practica universal del conjunto.
- **El espacio PMI x LFS es a lo sumo un poset/reticulo, no una categoria rica.**
  Donde se examina (b1e84abd C8, deep C3, a3f7c2e1 H1, v6 A6, v7-0608 O-F1) hay
  acuerdo: producto de reticulos finitos con restricciones inter-eje.
- **La distincion `preserved`/`declared` de `_transmutation.yml` es el activo de
  integridad intelectual de KORA.** Reconocido como virtud por deep (C14),
  b1e84abd, a3f7c2e1 y v7-0608; nadie lo disputa.

## Ejes de divergencia (dimensiones en que mas difieren)

1. **Scope del objeto auditado (eje dominante).** 7 auditan las specs; gemini
   audita el sistema. Es la divergencia mas grande: separa a gemini del resto por
   ortogonalidad de dominio y explica su score de 14 vs. la media ~35.

2. **Poder diagnostico vs. functor constante.** Rango enorme: deep/b1e84abd/v6
   hallan fallas estructurales falsables; v7-0607 tiene 0 criticas con checklist de
   "todo satisfecho"; gemini no halla nada. Es el eje que mas separa a los
   specs-scope entre si (diagnostico va de 5 a 0).

3. **Fidelidad del dato cuantitativo de transmutation.** El numero canonico es
   **5 preserved / 3 declared**. deep, b1e84abd, a3f7c2e1 y v7-0607 no lo
   contradicen; borrador dice "2/8 preservadas" (falso); v7-0608 dice "5 declared /
   3 preserved" (invertido). Mismo dato, tres versiones. Eje de divergencia
   factual puro.

4. **Disciplina contra falsos-amigos.** deep, b1e84abd y v7-0607 no cometen
   falsos-amigos groseros; v6 comete tres (faithful=monos, seccion=adjunto,
   subsheaf), a3f7c2e1 uno en su propia prosa (§3.2), gemini varios y graves
   (inventa producto fibrado, afirma adjuncion sin verificar). Eje de rigor
   categorial.

5. **Severidad asignada a la desalineacion doctrina/enforcement (A15).** La misma
   tension (matriz §6 por forma_material vs arnes-discriminante) es HIGH para v6,
   BAJA para v7-0607, no tocada por varias. Eje de juicio de severidad sobre un
   hecho compartido.

6. **Tipo categorial de `Lift_R ⊣ T_R`.** Adjuncion 1-categorial declarada
   (borrador, b1e84abd D2), conexion de Galois sobre reticulo (deep, la lectura
   correcta), o "Formal" sobre-afirmada sin prueba (v6, v7-0608). Eje de eleccion
   de maquinaria.

## Clusters de similitud

- **Cluster A — "El gap es de verificacion" (alta calidad, lectura convergente):**
  `deep`, `report-b1e84abd`, `report-a3f7c2e1`, `v7-0608`. Comparten la tesis
  central (leyes/adjunciones declaradas pero no verificadas mecanicamente), anclan
  a icas-preservacion, valoran la distincion preserved/declared y centran el
  hallazgo en la matriz de transmutation. Internamente: deep es el techo de rigor,
  b1e84abd lo sigue, a3f7c2e1 y v7-0608 concuerdan en el nucleo pero arrastran cada
  uno un error falsable (H8 fabricado / 5-vs-3 invertido). Es el cluster de
  relaciones CC de la matriz.

- **Cluster B — "Functorial honesto pero con resbalon de ejecucion":** `v6`,
  `borrador-claude`. Auditorias genuinas con anclaje fuerte y hallazgos reales,
  pero cada una con un defecto de ejecucion que toca lo central: borrador yerra el
  conteo 2/8 y se autocontradice (H1-vs-H6); v6 comete tres falsos-amigos y
  sobre-formaliza `F⊣U`. Criterio: hallazgo sustantivo + error categorial o
  factual propio.

- **Cluster C — "Cobertura amplia, temple prudente":** `v7-0607` (y parcialmente
  `v7-0608` por cobertura). Auditan las 8 specs, evitan falsos-amigos groseros,
  parsimoniosos; el riesgo del cluster es deslizarse al functor constante por bajo
  poder diagnostico. v7-0607 es el caso puro (0 criticas); v7-0608 comparte la
  cobertura pero rompe hacia la agresividad, por eso tambien entra en Cluster A.

- **Cluster D — outlier de scope:** `gemini`, solo. (Ver outlier.)

Criterio transversal de los clusters: la combinacion (tesis central) x (disciplina
categorial) x (fidelidad del dato) agrupa A (convergentes y fieles), B (fieles con
resbalon), C (amplios y tibios), D (fuera de scope).

## Outlier

**gemini.** Es el mas divergente del conjunto por margen amplio y por una razon
estructural, no de grado: es el unico con `scope_fit=sistema` (audita la
arquitectura/toolchain en vez de las specs, verificado con grep = 0 citas de spec),
el unico con veredicto "deficiente", el unico con score de dos cifras bajas (14 vs.
media ~34), el unico que **no halla un solo defecto** (functor constante a "todo
correcto"), el unico que **viola la regla dura** de declarar formal vs heuristico, y
el unico que **inventa estructura** atribuyendola al corpus (`U_phen x U_ctx x U_epi
x U_sta` con "Principio de Segregacion", inexistente en ICAS y en harness-spec). Su
relacion con las otras 7 es ortogonal en todos los pares: no comparte el objeto
auditado, asi que ni concuerda ni contradice, simplemente mira otra cosa. Funciona
como el contraejemplo de referencia (el funtor constante) contra el cual se mide la
fidelidad de las demas, y muy en particular su opuesto exacto, `deep`.
