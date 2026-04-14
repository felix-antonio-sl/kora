# Infraestructura autonoma

## La frontera donde el sistema se toca a si mismo

Hay un momento en la vida de todo sistema donde deja de ser operado y empieza a operarse a si mismo. Un reconciliation loop de Kubernetes que ajusta el estado real para igualar el estado deseado. Un agente que invoca una herramienta externa para resolver un sub-problema. Un enjambre de robots que redistribuye tareas cuando uno falla. Un pipeline de ML que reentrena su propio modelo cuando la distribucion de datos drifta.

En todos estos casos, el sistema cruza una frontera: pasa de ser un objeto en una categoria a ser un funtor que actua sobre esa categoria. Deja de ser materia pasiva y se convierte en patron activo -- pero un patron que modifica la materia sobre la que corre, incluyendose a si mismo. La teoria de categorias tiene las herramientas para modelar esta auto-referencia sin caer en paradojas, porque distingue con precision entre niveles categoricos: objetos, morfismos, funtores, transformaciones naturales, 2-funtores.

## Tool use como morfismo externo

Cuando un agente en la categoria A invoca una herramienta en la categoria B, el acto de invocacion no es un morfismo en A ni en B. Es un morfismo en una estructura que conecta ambas categorias: un profunctor P : A^op x B -> Set.

Un elemento de P(a, b) es una interaccion valida entre el agente a y la herramienta b. El profunctor captura todas las interacciones posibles -- todos los pares (agente, herramienta) que pueden conectarse, junto con las formas especificas en que pueden hacerlo. Si P(a, b) es vacio, el agente a no puede usar la herramienta b. Si P(a, b) tiene multiples elementos, hay multiples maneras de invocar la herramienta -- distintos modos de uso, distintos parametros, distintas interpretaciones del resultado.

La composicion de profunctores modela la composicion de tool use. Si P : A^op x B -> Set conecta agentes con herramientas, y Q : B^op x C -> Set conecta herramientas con recursos, la composicion Q . P : A^op x C -> Set conecta agentes con recursos transitivamente. Un agente que usa una herramienta de busqueda (profunctor P) y la herramienta de busqueda accede a una base de datos (profunctor Q) produce un acceso agente-a-base-de-datos que es la composicion de profunctores -- exactamente la convolucion coend integral Q . P = integral^b Q(b, c) x P(a, b).

El lema de Yoneda aplica directamente: la herramienta ES su interfaz. El funtor representable Hom(-, b) captura todo lo que cualquier agente puede hacer con la herramienta b. El agente no necesita entender los internos de la herramienta -- solo necesita conocer su interfaz, que es su profunctor. Esta es la formalizacion de la opacidad que observo en la practica: un agente LLM que invoca una tool function no sabe como esta implementada, solo conoce su firma y su descripcion. La firma es un representante del profunctor.

Para agentes multi-tool, la estructura se enriquece. Un agente con acceso a n herramientas tiene un profunctor P : A^op x (B_1 + ... + B_n) -> Set, donde el coproducto de categorias de herramientas modela la eleccion. La composicion de herramientas en secuencia es composicion de profunctores. La invocacion en paralelo es el producto monoidal de profunctores. Las operads dinamicas del documento 14 entran naturalmente: el agente es el manager que delega a herramientas-subordinados, y la estructura operadica captura la jerarquia de delegacion.

## Sistemas que se mejoran a si mismos

Un sistema auto-mejorante modifica sus propios morfismos de transicion. No solo transiciona entre estados -- cambia las reglas por las que transiciona. Categoricamente, esto requiere subir un nivel: no es un endofunctor E : C -> C (que mapea objetos y morfismos de C a objetos y morfismos de C, preservando la estructura), sino un endo-2-functor que modifica la categoria C misma.

La distincion es sutil pero crucial. Un endofunctor ordinario preserva la estructura de C: si hay un morfismo f : A -> B en C, entonces hay un morfismo E(f) : E(A) -> E(B) en C. El endofunctor no crea ni destruye morfismos -- los transforma. Un sistema auto-mejorante, en cambio, crea nuevos morfismos (aprende nuevas capacidades), destruye morfismos antiguos (descarta estrategias obsoletas), o modifica la estructura de composicion misma (cambia como se combinan las capacidades).

Aguado, Rossi y Sanz capturan esta idea en su framework Sys-Self para robots autonomos: el robot usa un modelo formal de si mismo -- una representacion categorica de sus componentes, relaciones y capacidades -- y lo modifica en runtime cuando encuentra contingencias. La auto-conciencia del robot es la capacidad de razonar sobre su propio modelo categorico. La auto-mejora es la modificacion de ese modelo basada en la experiencia.

La convergencia de la auto-mejora es la pregunta central. Si aplico E iteradamente -- E, E(E), E(E(E)), ... -- el sistema converge cuando alcanza un punto fijo: una categoria C* tal que E(C*) es isomorfa a C*. Este punto fijo es la terminal coalgebra del endofunctor E -- el objeto que "ya no cambia" bajo la aplicacion de E. En un sistema de aprendizaje, la terminal coalgebra es el modelo optimo: el que ya no mejora con mas entrenamiento, porque ha convergido a la distribucion estacionaria.

La no-convergencia es igualmente informativa. Si E no tiene punto fijo, el sistema nunca se estabiliza -- sigue modificandose indefinidamente. Esto puede ser deseable (un sistema que se adapta continuamente a un entorno cambiante) o catastrofico (un sistema que oscila sin converger). La diferencia esta en la estructura de E: si E es contractivo (cada iteracion reduce la distancia al punto fijo), converge. Si E es expansivo, diverge.

## Sistemas distribuidos como funtores sheaf-valued

Un sistema distribuido es un funtor de una categoria de topologia (nodos y conectividad) a una categoria de sistemas locales. Cada nodo tiene su propio estado, su propia logica, su propia vista parcial del mundo. La pregunta es: estas vistas parciales son consistentes?

Formalmente, sea Top la categoria cuyo objetos son nodos y abiertos (conjuntos de nodos conectados) y cuyos morfismos son inclusiones. Un sistema distribuido es un funtor F : Top^op -> C que asigna a cada abierto U el estado local del sub-sistema en U, y a cada inclusion U hookrightarrow V un morfismo de restriccion F(V) -> F(U) que "restringe" el estado global al sub-sistema.

La consistencia fuerte es la condicion de sheaf. Si tengo dos nodos U y V con solapamiento U cap V, y los estados locales F(U) y F(V) coinciden en el solapamiento -- F(U)|_{U cap V} = F(V)|_{U cap V} -- entonces existe un unico estado global F(U cup V) que extiende ambos. Esta es la condicion de sheaf del documento 12. Un sistema distribuido consistente ES un sheaf.

La consistencia eventual es un presheaf que se aproxima a la sheafificacion. En cada instante, las secciones locales pueden no coincidir en los solapamientos -- hay conflictos. Pero el protocolo de consenso (Raft, Paxos, CRDTs) trabaja para resolver los conflictos, y eventualmente las secciones locales se pegan en una seccion global. La sheafificacion es el limite de este proceso.

El teorema CAP admite una lectura categorica sugestiva (aunque no una equivalencia formal demostrada): en la categoria de configuraciones distribuidas, ciertos limites no existen simultaneamente. La consistencia es la existencia de un equalizador (todos los nodos ven lo mismo). La disponibilidad es la existencia de un terminal object (siempre hay una respuesta). La tolerancia a particiones es la condicion de que el funtor este definido sobre una topologia no conexa. La intuicion categorica dice: si la topologia no es conexa (hay particiones), el equalizador y el terminal object no pueden coexistir -- al menos uno de los dos limites no existe. El teorema de Brewer es mas sutil (involucra el aspecto dinamico de seguir respondiendo durante la particion), pero la perspectiva categorica captura la tension estructural correcta.

## Systems of Systems como 2-categorias

Un System of Systems (SoS) es una categoria de categorias -- la 2-categoria que introduje en el documento 13 para la composicion a escala. Aqui la extiendo con la dimension de autonomia. Cada sistema constituyente es una categoria con su propia estructura interna -- objetos, morfismos, composicion. Los sistemas interactuan entre si a traves de interfaces, que son funtores entre las categorias constituyentes. Y las interfaces se adaptan a lo largo del tiempo, a traves de transformaciones naturales entre funtores.

Esta es exactamente la estructura de una 2-categoria. Los objetos son los sistemas constituyentes. Los 1-morfismos son las interfaces (funtores). Los 2-cells son las adaptaciones de interfaces (transformaciones naturales). La composicion horizontal de 2-cells es la adaptacion compuesta: si adapto la interfaz A-B y la interfaz B-C, obtengo una adaptacion compuesta A-C. La composicion vertical es la adaptacion secuencial: primero adapto de una manera, luego de otra.

El comportamiento emergente es un colimite en la 2-categoria del SoS que no existe en ninguna categoria constituyente. Un enjambre de drones que se coordina para cubrir un area no tiene la capacidad de cobertura como propiedad de ningun drone individual -- es una propiedad del colimite. Si el colimite no existe, la propiedad emergente no se manifiesta. Si existe, es universal: es la propiedad mas general que emerge de la composicion de los constituyentes.

Los tipos de SoS que reconoce la ingenieria de sistemas tienen contrapartes 2-categoricas precisas. Un Acknowledged SoS -- con gobernanza central y composicion coordinada -- es una composicion 2-categorica fuerte, donde los 2-cells son naturales y conmutan. Un Collaborative SoS -- donde los sistemas negocian sus interfaces -- es una composicion debil, donde los 2-cells se ajustan por lax-naturalidad. Un Virtual SoS -- donde los sistemas coexisten sin coordinacion explicita -- es una mera yuxtaposicion, un coproducto sin interaccion, donde los sistemas comparten el espacio pero no componen activamente.

## Infraestructura autonoma: codigo declarativo y reconciliacion

Infrastructure-as-code es un funtor. La especificacion declarativa vive en una categoria Spec cuyos objetos son estados deseados y cuyos morfismos son transiciones validas. El estado real del runtime vive en una categoria Runtime cuyos objetos son estados actuales y cuyos morfismos son operaciones de infraestructura. El funtor Deploy : Spec -> Runtime traduce especificaciones a operaciones.

El reconciliation loop de un controlador de Kubernetes es un traced morphism. El controlador observa el estado actual (funtor Observe : Runtime -> Status), lo compara con el estado deseado (funtor Desired : Spec -> Status), y emite las acciones necesarias para converger (funtor Reconcile : Status x Status -> Runtime). El loop es traced porque la salida de Reconcile alimenta la siguiente observacion de Observe -- hay un cable que "vuelve atras" en el string diagram, como los feedback loops de la categoria compact closed del documento 07.

La convergencia del reconciliation loop es la condicion de que los funtores Deploy y Observe se vuelvan naturalmente isomorfos: Observe . Deploy ~ Desired. Cuando el isomorfismo natural existe, el estado real refleja fielmente la especificacion. Cuando no existe, hay drift -- diferencia entre lo declarado y lo real. El drift es la obstruccion a la existencia de la transformacion natural.

El self-healing es la aplicacion automatica de un morfismo de recuperacion por un cofree comonad. El cofree comonad c_p del documento 14 es un behavior tree infinito: en cada instante, observa el estado del sistema, emite una correccion si detecta drift, y transiciona a un nuevo estado de observacion. La counit extrae la observacion actual. La comultiplicacion despliega el plan de correccion en "lo que corrijo ahora" y "lo que corregire despues." El self-healing nunca termina -- es coinductivo, como toda comonada cofree -- porque la infraestructura nunca deja de necesitar supervision.

## Composition machines: auto-organizacion categorica

Arellanes propone las composition machines como un paradigma donde el software no se programa monoliticamente sino que emerge de la composicion auto-organizada de computones -- unidades atomicas de computacion. Una composition machine M = (D, F, Q, mu, S, N, delta) tiene un conjunto de tipos de datos D, un conjunto de computones F (funciones atomicas), un quiver Q que define la topologia de interaccion, funciones de asignacion mu, un conjunto de estados S, una estructura de vecindad N, y funciones de transicion local delta.

Lo notable de las composition machines es que el espacio de programas no se define a priori sino que emerge de las reglas locales de transicion. Cada computon tiene un estado (vivo o muerto). En cada paso temporal, los estados se actualizan segun las reglas delta que dependen de la vecindad. El espacio de programas en el tiempo t es la path category del quiver de computones vivos -- todas las composiciones secuenciales posibles en ese instante.

La evolucion temporal de la composition machine se describe por la aplicacion iterada de un funtor global G : configuracion -> configuracion. La orbita de la maquina es la secuencia c, G(c), G(G(c)), ... que muestra como el espacio de programas emerge, crece, se contrae y eventualmente puede estabilizarse en un patron periodico. Los ejemplos de Arellanes con reglas booleanas (NOT, XOR, Rule 54, Rule 122) demuestran que programas complejos -- composiciones secuenciales largas y no triviales -- emergen de reglas locales simples.

La conexion con las operads dinamicas del documento 14 es directa. Una composition machine es una operad dinamica donde los objetos son computones, las operaciones son composiciones, y la dinamica (el cambio de estructura en cada paso temporal) esta gobernada por las reglas locales delta. La diferencia es que Arellanes trabaja con quivers y path categories (estructura libre), mientras que las operads dinamicas de Shapiro-Spivak trabajan con polynomial functors y coalgebras. Ambas capturan el mismo fenomeno: sistemas que reorganizan su propia estructura de composicion en respuesta al feedback.

## La coherencia en todos los niveles

Lo que une todas estas manifestaciones de infraestructura autonoma es una observacion recursiva: cada nivel de autonomia requiere subir un nivel en la jerarquia categorica.

Un sistema pasivo vive en una categoria. Sus estados son objetos, sus transiciones son morfismos. No se modifica a si mismo.

Un sistema que se opera a si mismo vive como un funtor. Mapea especificaciones a ejecuciones, preservando estructura. Se modifica dentro de los limites que su tipo permite.

Un sistema que se mejora a si mismo vive como un 2-funtor. Modifica la categoria donde opera -- crea nuevos morfismos, destruye antiguos, cambia la composicion. Se modifica sin limites predefinidos.

Un System of Systems vive como una 2-categoria. Sus constituyentes son categorias, sus interfaces son funtores, sus adaptaciones son transformaciones naturales. La emergencia es un colimite 2-categorico.

Y una composition machine vive en la frontera: su estructura de composicion cambia en cada paso temporal, pero las reglas de cambio son fijas. Es un sistema auto-organizante que no se auto-mejora -- que reorganiza su materia sin modificar sus propias reglas. La diferencia entre auto-organizacion y auto-mejora es la diferencia entre un endofuntor (reorganizar dentro de la categoria) y un endo-2-funtor (reorganizar la categoria misma).

En la practica, esta jerarquia me da un lenguaje para clasificar los sistemas autonomos que construyo. Un deployment pipeline es un funtor. Un controlador Kubernetes es un traced morphism con feedback. Un agente con tool use opera via profunctores. Un enjambre auto-organizante es una composition machine. Y un sistema que aprende a mejorar su propia arquitectura es un 2-funtor -- el nivel mas alto de autonomia, y el mas peligroso, porque las garantias composicionales se vuelven mas dificiles de verificar a medida que subo en la jerarquia.
