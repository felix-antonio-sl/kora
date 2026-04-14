# Patrones

## La intuicion que ya tenia nombre

Cada vez que reconozco un patron de diseno -- Observer, Factory, Strategy, Decorator -- estoy reconociendo una estructura que la teoria de categorias ya habia descubierto bajo otro nombre. No es una coincidencia. Los patrones de diseno de software son soluciones que se repiten porque resuelven problemas universales. Y las construcciones universales de la teoria de categorias son, por definicion, las soluciones canonicas a problemas formulados en terminos de composicion y estructura. El puente entre ambos mundos no es una analogia: es una identificacion.

Lo que me propongo aqui es hacer explicita esa identificacion. Cada patron clasico de diseno tiene una contraparte categorica precisa. Cada anti-patron es una violacion de una propiedad categorica. Y la tension entre heuristicas y metodos formales -- la tension que define la practica cotidiana de la ingenieria -- tiene una formulacion exacta como adjuncion.

## Patrones de diseno como construcciones universales

El patron Observer es un funtor representable. Un sujeto S que notifica a multiples observadores es exactamente la situacion de Yoneda: el sujeto define un funtor Hom(S, -) que a cada objeto O le asigna el conjunto de maneras en que O puede observar a S. La propiedad universal de Yoneda dice que toda la informacion sobre S esta capturada en este funtor -- el sujeto ES sus observadores potenciales, de la misma manera que un API endpoint ES el conjunto de llamadas validas que acepta. Cuando registro un observer, estoy eligiendo un elemento del hom-set. Cuando notifico, estoy evaluando el funtor representable.

El patron Factory es una construccion libre -- un adjunto izquierdo. La fabrica toma una especificacion minimal (un tipo, unos parametros) y produce el objeto mas general que satisface esa especificacion. Eso es exactamente lo que hace un funtor libre F : Set -> C: dado un conjunto de generadores, construye el objeto libre en C. La propiedad universal garantiza que cualquier otro objeto que use esos generadores factoriza a traves del objeto libre. En la practica, `List.of(1, 2, 3)` es la lista libre sobre tres generadores, y toda funcion que consuma esos tres enteros factoriza a traves de ella. La fabrica no inventa; construye lo universal.

El patron Adapter es una transformacion natural. Tengo dos interfaces -- dos funtores F, G : C -> D -- y necesito traducir de una a otra preservando la estructura. Un adapter alpha : F => G proporciona, para cada objeto A, un morfismo alpha_A : F(A) -> G(A) tal que la naturalidad se satisface: para todo morfismo f : A -> B, el diagrama conmuta. En codigo, un adapter que traduce de `XMLParser` a `JSONParser` debe respetar la composicion: parsear un documento compuesto da el mismo resultado que parsear las partes y componerlas.

El patron Strategy es un funtor parametrizado sobre un producto monoidal. Una familia de algoritmos intercambiables es un funtor F : Strategies tensor Input -> Output, donde el factor Strategies indexa el algoritmo y el factor Input proporciona los datos. El producto monoidal (documento 07) captura que la eleccion de estrategia y la provision de datos son independientes -- puedo cambiar uno sin afectar al otro. La interchange law garantiza que componer estrategias en paralelo con datos en paralelo es coherente.

El patron Decorator es una monada. Un Decorator envuelve un objeto, le agrega funcionalidad, y puede envolverse a su vez. La unit eta : A -> T(A) envuelve el objeto base. La multiplicacion mu : T(T(A)) -> T(A) aplana decoradores anidados -- un `BufferedStream(BufferedStream(file))` se simplifica a `BufferedStream(file)`. Las leyes de monada (asociatividad y unitalidad, documento 09) son exactamente las propiedades que hacen que los decoradores compongan limpiamente.

El patron Composite es un algebra inicial -- un tipo recursivo. Un arbol de componentes donde cada nodo es un componente individual o un grupo de componentes es el punto fijo inicial del funtor F(X) = Leaf + Node(X, X). La propiedad de inicialidad garantiza que existe un unico morfismo (catamorfismo) desde el composite a cualquier otro algebra -- que es exactamente el fold que recorre el arbol evaluando cada nodo. Cada vez que implemento un `render()` recursivo sobre un arbol de componentes UI, estoy ejecutando el catamorfismo unico desde el algebra inicial.

## Patrones arquitectonicos categoricamente

Los patrones arquitectonicos operan a una escala mayor, pero la estructura categorica es igual de precisa.

Una arquitectura de microservicios es una categoria donde los objetos son servicios y los morfismos son API calls. La composicion de morfismos es el encadenamiento de llamadas: si A llama a B y B llama a C, la composicion A -> C es la llamada transitiva. La asociatividad garantiza que el orden de agrupamiento no importa. La identidad es el health-check -- el servicio que se llama a si mismo y verifica que esta vivo. Heyn et al. formalizan esta vision: las vistas arquitectonicas forman categorias por nivel de abstraccion, y los funtores entre niveles son los correspondence rules que preservan la estructura de un nivel al siguiente.

Una arquitectura en capas es una secuencia de funtores. Cada capa es una categoria con su propia logica interna: la capa de datos maneja entidades, la capa de negocio maneja reglas, la capa de presentacion maneja vistas. El funtor F : Datos -> Negocio traduce entidades a objetos de dominio preservando relaciones. El funtor G : Negocio -> Presentacion traduce reglas a componentes visuales. La composicion G . F : Datos -> Presentacion es la traza end-to-end. La functorialidad de cada capa garantiza que la estructura se preserva: si dos entidades estan relacionadas en la capa de datos, sus representaciones estan relacionadas en la capa de presentacion.

Una arquitectura event-driven es coalgebraica. Cada servicio tiene un estado interno y expone eventos -- exactamente la estructura de una coalgebra c : S -> F(S) donde F es el interface functor que determina que eventos se emiten y que transiciones se producen. Los eventos son las observaciones; los handlers son los morfismos de transicion. La diferencia con la arquitectura de microservicios es que los morfismos no son llamadas directas sino publicaciones y suscripciones -- la composicion es coalgebraica (por observacion) en lugar de algebraica (por invocacion).

Un pipeline es composicion en una Kleisli category. Cada stage del pipeline es un morfismo A -> T(B) donde T es una monada que captura los efectos (errores, logging, estado). La composicion Kleisli encadena stages propagando el efecto. Un pipeline de CI/CD donde cada stage puede fallar es composicion en la Kleisli category de la monada Maybe. Un pipeline de datos donde cada stage produce logs es composicion en la Kleisli category de la monada Writer.

## Patrones agenticos

Los patrones que emergen en el diseno de agentes inteligentes tienen su propia estructura categorica, construida sobre la maquinaria del documento 14.

El patron ReAct (Reason + Act) alterna entre razonamiento y accion. Categoricamente, es la alternancia entre un free monad (los pasos de razonamiento, que ramifican y terminan) y un cofree comonad (las invocaciones de herramientas, que observan y persisten). Cada ciclo de ReAct ejecuta un paso del free monad, cuyo resultado determina que herramienta invocar en el cofree comonad, cuya respuesta alimenta el siguiente paso del free monad. Es la ley de interaccion Xi de Libkind-Spivak: el patron (razonamiento) consume la materia (herramientas).

El Chain-of-Thought es un path en la free category. Dado un grafo de conceptos (objetos) y relaciones (generadores), una cadena de pensamiento es un camino: una secuencia de aristas que conecta una premisa con una conclusion. La free category sobre el grafo contiene todos los caminos posibles -- todas las cadenas de razonamiento validas. El chain-of-thought selecciona uno. Las path equivalences en la free category corresponden a cadenas de pensamiento que llegan a la misma conclusion por rutas distintas -- razonamientos equivalentes.

RAG (Retrieval-Augmented Generation) es un pullback. El query q vive en el espacio de preguntas Q. La knowledge base K es un funtor de Q a documentos. El modelo generativo G es un funtor de contextos a respuestas. El pullback Q x_D K captura exactamente los pares (query, documento) que son compatibles -- que comparten el mismo dominio de relevancia D. La generacion aumentada es la composicion del pullback con el funtor generativo.

El multi-agent debate es un coequalizer. Multiples agentes producen respuestas distintas -- morfismos paralelos f, g : A -> B. El debate es el proceso de converger a un consenso -- el coequalizer C con q : B -> C tal que q . f = q . g. El coequalizer identifica exactamente las diferencias entre las respuestas de los agentes, produciendo el resultado mas general en el que todos coinciden. Si el coequalizer no existe, no hay consenso posible -- los agentes estan en desacuerdo irreducible.

## Anti-patrones como propiedades categoricas rotas

Si los patrones son construcciones universales, los anti-patrones son violaciones de propiedades categoricas.

El God Object es un objeto con demasiados morfismos entrantes y salientes -- un objeto que participa en casi todos los hom-sets de la categoria. Categoricamente, es un objeto cuyo funtor representable Hom(G, -) tiene demasiada estructura, lo que significa que G "sabe demasiado" sobre el resto de la categoria. La solucion es factorizar: descomponer G en un diagrama de objetos mas pequenos cuyo colimite sea G, de modo que cada parte tenga responsabilidad acotada.

La dependencia circular es una composicion no bien fundada. En una categoria bien fundada, las cadenas de composicion terminan -- todo camino de morfismos es finito y no hay ciclos no triviales (excepto identidades). Una dependencia circular A -> B -> C -> A crea un endomorfismo no trivial A -> A que no es la identidad, y la composicion iterada no converge. La solucion categorica es hacer explicitas las identidades: si A -> B -> C -> A debe ser id_A, entonces el ciclo es un invariante que debo verificar, no un bug.

El tight coupling es un funtor no faithful. Si el funtor F : Internal -> External mapea la estructura interna de un modulo a su interfaz externa, y F no es faithful (colapsa morfismos internos distintos al mismo morfismo externo), entonces los cambios internos no son distinguibles desde afuera -- pero tampoco estan encapsulados, porque la interfaz externa expone demasiado. El acoplamiento fuerte ocurre cuando F no es ni faithful ni full -- ni inyectivo ni sobreyectivo en hom-sets. La interfaz esta mal calibrada.

El Feature Envy es un morfismo en la categoria equivocada. Cuando un metodo de la clase A accede mas a los datos de la clase B que a los propios, ese morfismo deberia vivir en B, no en A. Categoricamente, es un morfismo f en la categoria C_A que factoriza a traves de un objeto de C_B -- evidencia de que f pertenece a la categoria B y deberia moverse ahi.

## Heuristicas versus metodos formales

La tension entre heuristicas y metodos formales es la tension que define la practica diaria de la ingenieria. Las heuristicas son rapidas pero no garantizan composicion. Los metodos formales son precisos pero costosos. Esta tension no es un dilema ad hoc -- es una adjuncion.

El funtor de formalizacion L : Heuristic -> Formal toma una heuristica y produce su version formal: la especificacion precisa, la prueba de correccion, la verificacion exhaustiva. Es el adjunto izquierdo -- preciso, caro, libre de ambiguedad. El funtor de relajacion R : Formal -> Heuristic toma una especificacion formal y produce una heuristica practica: la regla de oro, la aproximacion, la buena practica. Es el adjunto derecho -- flexible, barato, preservando la practica existente.

La adjuncion L ⊣ R dice: formalizar una heuristica y luego relajar la formalizacion produce algo mas estructurado que la heuristica original (la counit es un morfismo RL(h) -> h que "pierde algo"). Relajar una formalizacion y luego re-formalizar la relajacion produce algo menos preciso que la formalizacion original (la unit es un morfismo f -> LR(f) que "agrega ruido"). El gap entre la unit y la counit mide exactamente la distancia entre lo formal y lo practico.

Las heuristicas son morfismos aproximados: no hay garantia de que la composicion de dos heuristicas produzca una heuristica valida. Si la heuristica "usa cache para mejorar performance" y la heuristica "invalida cache cuando cambian los datos" se componen ingenuamente, el resultado puede ser incoherente. Los metodos formales son morfismos exactos: la composicion esta garantizada por construccion. Si formalizo ambas como invariantes de un sistema de tipos, la composicion se verifica en compile time.

## Wrapper functors: integración multi-modelo

Un patrón de integración que combina varias de estas ideas es el **wrapper functor** para entornos multi-modelo. Cuando una arquitectura combina PostgreSQL, MongoDB y Neo4j, cada base de datos tiene su propio "idioma" categorial: tablas y foreign keys, documentos y embedding, nodos y aristas. El patrón consiste en definir un **Schema Category global** cuyos objetos son tipos lógicos unificados y cuyos morfismos son relaciones semánticas, y construir un wrapper functor W_db : DB_specific → SchemaCategory para cada base de datos. W_postgres mapea tablas a tipos, foreign keys a morfismos. W_mongo mapea collections a tipos, nested refs a morfismos. W_neo4j mapea node labels a tipos, edge types a morfismos.

Cada wrapper es un funtor -- debe preservar composición e identidad. La composición de queries en el Schema Category global se traduce automáticamente a queries concretas en cada base vía los wrappers. Y una query multi-modelo es un bimodule sobre el Schema Category global (como los que describí en el documento 06) cuya evaluación se descompone a través de los wrappers. La inversión de control es total: el Schema Category global define la semántica; los wrappers solo implementan la traducción. Si agrego una nueva base de datos, agrego un wrapper; el Schema Category y las queries no cambian.

## Co-design como lattice de problemas de diseno

La monotone co-design theory de Censi, formalizada en el ACT4E de Fong y Spivak, ofrece un marco donde los problemas de diseno forman una estructura de lattice. Un Design Problem with Implementation (DPI) es una tupla (F, R, I, prov, req) donde F es un poset de funcionalidades, R es un poset de recursos, I es un espacio de implementaciones, prov : I -> F mapea cada implementacion a la funcionalidad que provee, y req : I -> R mapea cada implementacion a los recursos que requiere.

La dualidad entre funcionalidad y recursos es fundamental: la funcionalidad es un lower bound (lo minimo que debo proveer), los recursos son un upper bound (lo maximo que puedo consumir). El diseno es factible cuando existe una implementacion i tal que prov(i) >= f_min y req(i) <= r_max.

Los DPIs se componen: si el motor provee torque y requiere electricidad, y el chasis provee movilidad y requiere torque, la composicion en serie conecta el output del motor al input del chasis. Los DPIs forman una semicategoria donde la composicion preserva la estructura de poset. Y los design problems (sin implementacion, solo la relacion funcionalidad-recursos) forman un lattice: el meet de dos design problems es la interseccion de disenos factibles (ambos constraints se satisfacen), el join es la union (al menos un constraint se satisface).

Esta estructura de lattice es la formalizacion de lo que hago intuitivamente cuando exploro un espacio de diseno. Cada decision de diseno restringe el lattice -- elimina opciones no factibles. Cada trade-off es un movimiento entre el meet y el join. Y la monotonia de los mapas garantiza que las decisiones locales se propagan coherentemente al diseno global -- que la composicion de sub-disenos factibles produce un diseno global factible.

Heyn et al. extienden esta perspectiva al framework arquitectonico: las vistas arquitectonicas forman un lattice parcialmente ordenado por nivel de detalle, con funtores de correspondencia entre niveles. La consistencia del framework es la condicion de que el producto de vistas en cada nivel sea valido -- que los diagramas conmuten. Un framework arquitectonico composicional permite agregar clusters of concern sin romper la estructura existente, porque la adicion es un join en el lattice.

## La convergencia practica

Lo que emerge de esta cartografia de patrones es una vision donde el diseno de software no es una actividad artesanal separada de la matematica, sino una instanciacion de construcciones universales. No pierdo la intuicion del artesano -- el olfato que me dice "esto huele a Observer" o "esto necesita un Factory." Lo que gano es composabilidad: la certeza de que los patrones no son recetas aisladas sino facetas de una estructura coherente.

Los anti-patrones dejan de ser "malas practicas" subjetivas y se convierten en violaciones verificables de propiedades categoricas. El God Object es un fallo de factorizacion. La dependencia circular es un fallo de well-foundedness. El tight coupling es un fallo de faithfulness. Y la heuristica de "buscar el patron correcto" se revela como la busqueda de la construccion universal adecuada -- la solucion que, por su propiedad universal, es automaticamente la mejor posible en su contexto.
