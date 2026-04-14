# Adjunciones

## El mecanismo óptimo de traducción

Llevo cinco documentos construyendo un vocabulario: composición, preservación, comparación, identidad relacional, y ahora construcciones universales. Y hay un hilo que reaparece en cada una. Cuando traduzco entre mundos con funtores, hay traducciones que están "perfectamente emparejadas" -- una va en un sentido y la otra en el sentido contrario, y juntas forman algo mejor que un simple par de funtores. No son inversas (eso sería una equivalencia), pero están coordinadas de una manera que genera estructura nueva.

Esa coordinación se llama **adjunción**, y es posiblemente el concepto más ubicuo de toda la teoría de categorías. Saunders Mac Lane dijo que los conceptos surgen cuando se encuentran adjunciones. Después de trabajar con ellas, estoy convencido de que tenía razón: cada par de operaciones que "van y vienen" de manera natural resulta ser una adjunción cuando lo miro con cuidado.

## La definición: unit y counit

Dados dos funtores L : D → C y R : C → D, digo que L es **left adjoint** de R (notado L ⊣ R) cuando existen dos transformaciones naturales:

```
η : Id_D → R ∘ L       (unit)
ε : L ∘ R → Id_C       (counit)
```

que satisfacen las **identidades triangulares**:

```
ε_{L d} ∘ L(η_d) = id_{L d}
R(ε_c) ∘ η_{R c} = id_{R c}
```

La unit η me permite "introducir" el viaje de ida y vuelta R ∘ L: dado cualquier objeto d en D, obtengo un morfismo η_d : d → R(L(d)) que mete a d en la imagen del viaje redondo. Es como una inyección canónica.

La counit ε me permite "eliminar" el viaje L ∘ R: dado cualquier c en C, obtengo ε_c : L(R(c)) → c que proyecta desde la imagen del viaje redondo de vuelta al original. Es como una evaluación canónica.

Las identidades triangulares garantizan coherencia: si primero introduzco con η y luego elimino con ε, recupero lo que tenía. Pero nota la asimetría: R ∘ L no es necesariamente la identidad, ni L ∘ R tampoco. La adjunción no es un isomorfismo -- es algo más sutil y más útil.

## La definición equivalente: isomorfismo de hom-sets

Hay una formulación alternativa que revela el significado profundo. L ⊣ R si y solo si hay un isomorfismo natural:

```
C(L d, c) ≅ D(d, R c)
```

para todo d en D y c en C. Es decir: los morfismos desde L(d) hacia c en C están en correspondencia biyectiva con los morfismos desde d hacia R(c) en D, y esta correspondencia es natural en ambas variables.

Esto dice algo extraordinario: **preguntar en C después de traducir con L equivale a preguntar en D antes de traducir con R**. Los dos funtores dan "vistas" del mismo fenómeno desde mundos distintos, y las vistas son perfectamente compatibles.

La conexión entre las dos definiciones es directa. De la isomorfía de hom-sets, tomando c = L(d), obtengo id_{L d} ∈ C(L d, L d) que corresponde a η_d ∈ D(d, R(L d)): eso es la unit. Tomando d = R(c), obtengo id_{R c} ∈ D(R c, R c) que corresponde a ε_c ∈ C(L(R c), c): eso es la counit.

## Conexiones de Galois: la adjunción más simple

La forma más elemental de adjunción ocurre entre preórdenes. Una **conexión de Galois** entre posets P y Q es un par de funciones monótonas f : P → Q y g : Q → P tales que:

```
f(p) ≤ q   si y solo si   p ≤ g(q)
```

Esto es exactamente la definición de adjunción con hom-sets reemplazados por la relación de orden (en un poset, el hom-set tiene a lo sumo un elemento). Fong y Spivak lo desarrollan en detalle: f es el left adjoint, g el right adjoint, y la composición g ∘ f : P → P es un **operador clausura** -- idempotente y extensivo.

Un ejemplo concreto: la función piso ⌊·⌋ : R → Z y la inclusión i : Z → R forman una conexión de Galois:

```
⌊x⌋ ≤ n   si y solo si   x ≤ i(n) = n
```

El left adjoint (piso) es la mejor aproximación entera por debajo. El right adjoint (inclusión) preserva la estructura exacta. Este patrón aparece en cada par de niveles de abstracción que manejo: el left adjoint "comprime" o "aproxima", el right adjoint "expande" o "incluye."

El Adjoint Functor Theorem para preórdenes dice algo poderoso: si un poset tiene todos los meets y un mapa monótono los preserva, entonces ese mapa es right adjoint -- el left adjoint existe automáticamente. Esto explica por qué tantas construcciones "obvias" en la práctica resultan ser adjunciones: si preservas suficiente estructura, tu pareja óptima existe gratis.

## Free/forgetful: el arquetipo

El ejemplo más importante de adjunción en la práctica es el par **free/forgetful**. El funtor olvidadizo U : Mon → Set toma un monoide y devuelve su conjunto subyacente, olvidando la operación y la unidad. El funtor libre F : Set → Mon toma un conjunto de generadores y construye el monoide libre sobre él (todas las listas finitas con concatenación).

La adjunción F ⊣ U dice:

```
Mon(F(X), M) ≅ Set(X, U(M))
```

Un homomorfismo desde el monoide libre F(X) al monoide M está determinado por una función del conjunto generador X al conjunto subyacente de M. Es decir: para definir un homomorfismo desde algo libre, basta decir a dónde van los generadores. Todo lo demás se deduce de la estructura.

En Haskell, esto es concreto: `[a]` (listas finitas) es el monoide libre sobre `a`. Un homomorfismo de monoides `[a] → m` está determinado por una función `a → m` -- que es exactamente `foldMap`:

```haskell
foldMap :: (Monoid m) => (a -> m) -> [a] -> m
foldMap f = mconcat . map f
```

En la práctica, el patrón free/forgetful aparece en todas partes:

- **ORM ⊣ SQL**: el ORM construye "libremente" objetos con relaciones; la ejecución SQL olvida la estructura de objetos y trabaja con tablas y filas.
- **AST ⊣ Source**: el parser construye un AST libre a partir del código fuente; el pretty-printer olvida la estructura arbórea y produce texto.
- **Docker image ⊣ Dockerfile**: la imagen es la construcción libre; el Dockerfile es la especificación que genera libremente la imagen.

El patrón es: uno crea estructura libremente (sin imponer relaciones más allá de las leyes algebraicas mínimas), el otro olvida con gracia (retiene solo lo esencial). Cada vez que digo "X se genera a partir de Y", probablemente estoy mirando un left adjoint libre.

## Las adjunciones generan límites

Hay un resultado que conecta este documento con el anterior de manera profunda: **los right adjoints preservan límites y los left adjoints preservan colímites**.

Esto no es solo un teorema elegante -- tiene consecuencias prácticas inmediatas. Si sé que un funtor R es right adjoint, entonces automáticamente preserva productos, pullbacks, ecualizadores, y todo tipo de límite. No necesito verificar cada caso: la adjunción me lo da gratis.

Y el converso es casi cierto: el Adjoint Functor Theorem (que ya vimos para preórdenes) se generaliza. Si una categoría es completa y un funtor preserva todos los límites, bajo ciertas condiciones de tamaño, ese funtor es right adjoint. La preservación de estructura delata la adjunción.

En la práctica esto significa: si un funtor "se porta bien" con JOINs (pullbacks), con productos cartesianos, con restricciones (ecualizadores), entonces tiene una pareja óptima esperándolo.

## Las adjunciones generan monads

Y hay otro resultado que anticipo aquí para el documento 09. Dada una adjunción L ⊣ R con unit η y counit ε, la composición T = R ∘ L es una monad:

```
T = R ∘ L : D → D
η : Id → T           (unit de la monad)
μ = R ε L : T² → T   (multiplication)
```

La monad codifica el "efecto" del viaje de ida y vuelta. Si L traduce "hacia abajo" y R traduce "de vuelta," T es la huella que deja el viaje redondo en el mundo original. No profundizo más aquí, pero esto explica por qué las monads aparecen en tantos lugares: cada adjunción genera una, y las adjunciones son ubicuas.

## La triple adjunción: Sigma ⊣ Delta ⊣ Pi

Y ahora la aplicación que considero la más importante para un arquitecto de sistemas: la **triple adjunción para migración funcional de datos**. Spivak demuestra que un funtor entre esquemas de bases de datos F : C → D induce tres funtores de migración:

```
Σ_F ⊣ Δ_F ⊣ Π_F
```

donde:

- **Δ_F** (pullback migration): tira datos de D-instancias a C-instancias por composición con F. Produce **proyecciones** automáticamente.
- **Σ_F** (left pushforward): empuja datos de C-instancias a D-instancias. Produce **uniones** y **Skolemiza** valores desconocidos.
- **Π_F** (right pushforward): empuja datos de C-instancias a D-instancias. Produce **joins** automáticamente.

El paper de Spivak lo ilustra con un ejemplo concreto. Si tengo un esquema C con dos tablas T1 (SSN, First, Last) y T2 (First, Last, Salary), y un esquema D con una sola tabla T que unifica ambas, entonces:

- Δ_F(J) divide la tabla unificada en las dos originales (proyección).
- Σ_F(I) toma la unión de T1 y T2 en una sola tabla, inventando variables Skolem para los campos que faltan (T1 no tiene Salary, T2 no tiene SSN).
- Π_F(I) hace el join de T1 y T2, quedándose solo con los registros que matchean en First y Last.

Brown, Spivak y Wisnesky implementan esto en CQL (Categorical Query Language), donde un script real de migración se ve así:

```
schema S = literal : empty {
  entities
    Employee Department
  foreign_keys
    worksIn : Employee -> Department
  attributes
    name : Employee -> Varchar
    dept_name : Department -> Varchar
}

mapping F = literal : S -> T { ... }

-- Δ_F produce la vista automáticamente
-- Σ_F produce la unión con nulls tipados
-- Π_F produce el join
```

Lo que me impresionó del CQL paper es que la garantía de corrección no es ad hoc: viene del hecho de que Σ, Δ y Π son adjuntos. Las "round-trip properties" (Σ_F Δ_F y Δ_F Π_F se comportan bien) son consecuencias directas de las identidades triangulares. La categoría hace el trabajo pesado.

## Adjunciones en la práctica cotidiana

Más allá de la migración de datos, las adjunciones organizan pares de operaciones que encuentro cada día:

**Compilar ⊣ Interpretar.** La compilación es left adjoint: transforma código fuente en una representación eficiente, comprimiendo la información semántica en instrucciones de máquina. La interpretación es right adjoint: preserva toda la información del código, evaluándolo paso a paso sin perder contexto.

**Normalizar ⊣ Desnormalizar.** La normalización de bases de datos elimina redundancia (left adjoint: comprime). La desnormalización introduce redundancia estratégica para performance (right adjoint: expande). El trade-off entre ambas es exactamente la tensión de una adjunción.

**Comprimir ⊣ Expandir.** gzip ⊣ gunzip, pero a nivel profundo: la compresión es la mejor aproximación compacta (left adjoint), la expansión recupera la estructura original (right adjoint).

**Abstraer ⊣ Concretar.** Subir un nivel de abstracción (interfaces, traits, protocolos) es left adjoint. Bajar a una implementación concreta es right adjoint. La interfaz captura lo mínimo necesario; la implementación rellena los detalles.

**Currying como adjunción.** Anticipo aquí una estructura que el documento 07 formalizará como categoría cartesiana cerrada (CCC). Es quizás la adjunción más limpia:

```
C(A × B, C) ≅ C(A, C^B)
```

El funtor − × B (tomar producto con B) es left adjoint del funtor (−)^B (exponencial, o función desde B). Dar una función de dos argumentos es lo mismo que dar una función de un argumento que devuelve otra función. Esto es `curry`/`uncurry` en Haskell:

```haskell
curry   :: ((a, b) -> c) -> a -> b -> c
uncurry :: (a -> b -> c) -> (a, b) -> c
```

Y la counit de esta adjunción es la función `eval`:

```haskell
eval :: (b -> c, b) -> c
eval (f, x) = f x
```

que toma un par (función, argumento) y produce el resultado. Es la eliminación del exponencial, exactamente como la counit elimina L ∘ R.

## El principio unificador

Las adjunciones son el mecanismo universal de traducción óptima. Cada vez que tengo dos mundos y dos formas de ir y venir entre ellos, con la propiedad de que "preguntar aquí después de traducir" equivale a "preguntar allá antes de traducir," estoy ante una adjunción.

El left adjoint encuentra la mejor aproximación en un sentido: la más libre, la más compacta, la que pierde menos. El right adjoint encuentra la mejor aproximación en el otro sentido: la más fiel, la que preserva más estructura, la que olvida con gracia. Y la isomorfía de hom-sets garantiza que ambas vistas son perfectamente consistentes.

Esto me ha cambiado la manera de diseñar sistemas. Cuando detecto que un par de operaciones forma una adjunción, sé que: (1) la traducción es óptima en ambas direcciones, (2) los right adjoints preservan límites automáticamente, (3) la composición R ∘ L genera una monad que captura el efecto del viaje redondo, y (4) las propiedades de round-trip son teoremas, no esperanzas.

Las construcciones universales del documento anterior me dieron la mejor solución a cada problema estructural. Las adjunciones me dan el mecanismo óptimo para traducir entre las soluciones de distintos mundos. Y juntas, construyen los cimientos para todo lo que viene después.
