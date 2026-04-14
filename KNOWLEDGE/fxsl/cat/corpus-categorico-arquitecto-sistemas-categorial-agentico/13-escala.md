# Escala

## El problema de componer a lo grande

Hay un momento en la vida de todo sistema donde la composicion secuencial -- un morfismo tras otro, un pipeline tras otro -- deja de ser suficiente. Necesito componer jerarquicamente: subsistemas dentro de sistemas, equipos dentro de organizaciones, pods dentro de servicios dentro de namespaces dentro de clusters. Y necesito hacerlo manteniendo interfaces explicitas en cada frontera.

Los funtores y las transformaciones naturales que domine en los primeros documentos me dieron composicion "horizontal" -- un nivel de abstraccion a la vez. Pero la realidad de los sistemas a escala es que hay composicion en multiples dimensiones simultaneas. Una celda en un cuadro de doble categoria, donde un componente (flecha horizontal) se conecta a otro a traves de un conector (flecha vertical), captura algo que un diagrama conmutativo ordinario no puede: la distincion entre lo que el sistema ES y como se COMUNICA.

## Operads: composicion jerarquica

Una operad es una estructura que formaliza la composicion de operaciones con multiples entradas y una salida. Una operacion en una operad tiene aridad n: toma n inputs y produce 1 output. Y lo crucial es que estas operaciones se pueden anidar: si tengo una operacion f de aridad 3 y tres operaciones g1, g2, g3 de aridades 2, 1, 4 respectivamente, puedo componer para obtener una operacion f(g1, g2, g3) de aridad 2+1+4 = 7.

Formalmente, una operad O consiste en:

- Para cada n >= 0, un conjunto O(n) de operaciones de aridad n
- Una operacion identidad id en O(1)
- Composicion: si f tiene aridad n y g_i tiene aridad k_i para i=1..n, entonces f(g_1, ..., g_n) tiene aridad k_1 + ... + k_n
- Leyes de asociatividad y unidad analogas a las de una categoria

La diferencia con una categoria es que en una categoria, la composicion es binaria y secuencial. En una operad, la composicion es n-aria y jerarquica. Esto es exactamente lo que necesito para modelar la infraestructura de Kubernetes:

```
cluster(namespace_1(svc_a(pod_x, pod_y), svc_b(pod_z)),
        namespace_2(svc_c(pod_w)))
```

Cada nivel de anidamiento es una operacion operadica. El cluster es una operacion de aridad 2 (dos namespaces). Cada namespace es una operacion de aridad variable (servicios). Cada servicio es una operacion sobre pods. La composicion total produce un unico sistema.

## Wiring diagrams: la sintaxis visual

Los wiring diagrams dan una representacion visual a la composicion operadica. Un wiring diagram es una caja con puertos de entrada y salida, que puede contener cajas internas cableadas entre si. Los cables conectan puertos de salida de unas cajas a puertos de entrada de otras, y los puertos no conectados internamente se exponen como la interfaz externa de la caja contenedora.

El poder de esta representacion es que cada caja es opaca -- solo veo sus puertos. La composicion operadica dice como cablear cajas para formar cajas mas grandes. Y puedo hacer zoom: abrir una caja para ver su estructura interna, o cerrarla para tratarla como un componente atomico.

Esto es exactamente el patron de un pipeline de CI/CD modelado correctamente:

```
pipeline(
  build(checkout, compile, test_unit),
  validate(lint, security_scan, test_integration),
  deploy(provision, rollout, healthcheck)
)
```

Cada stage es una operacion operadica. Los "cables" son los artefactos que pasan de una stage a otra: el codigo compilado fluye de build a validate, el binario validado fluye de validate a deploy. La composicion total es una operacion que toma un commit y produce un deployment.

## Double categories: componentes y conectores

Hay situaciones donde una sola dimension de morfismos no alcanza. Cuando modelo una arquitectura de microservicios, tengo dos tipos de relacion fundamentalmente distintos:

- Los servicios mismos y sus dependencias funcionales (Service A llama a Service B)
- Los mecanismos de comunicacion (HTTP, gRPC, message queue, shared database)

Una double category D tiene objetos, morfismos horizontales, morfismos verticales, y 2-cells que llenan cuadrados. Lambert, en su trabajo sobre double categories of relations, formaliza esto con precision: los objetos de D_0 son los mismos para ambas direcciones, pero los morfismos horizontales (proarrows) y verticales (arrows) capturan dimensiones distintas.

En la practica, puedo modelar la arquitectura de microservicios como una double category donde:

- Los objetos son los servicios
- Los morfismos horizontales son los flujos de datos (Service A envia eventos a Service B)
- Los morfismos verticales son las dependencias funcionales (Service A requiere Service B para su operacion)
- Las 2-cells capturan la relacion entre ambas: "el flujo de datos de A a B se implementa via la dependencia funcional de A sobre B a traves del protocolo gRPC"

La estructura de equipment que Lambert describe -- donde un double category tiene todas las restrictions y extensions -- garantiza que puedo razonar sobre como los flujos de datos se transforman cuando reestructuro las dependencias. Si muevo un servicio, las 2-cells me dicen exactamente que flujos de datos se afectan.

## Structured cospans: sistemas abiertos con interfaces compartidas

Un cospan en una categoria C es un diagrama A -> N <- B: dos objetos A y B que se mapean a un objeto intermedio N. Si pienso en A y B como las interfaces de un sistema y N como su implementacion, un cospan dice: "este sistema tiene interfaz izquierda A e interfaz derecha B, y ambas se conectan a la implementacion N."

Los structured cospans refinan esto exigiendo que N tenga estructura adicional -- por ejemplo, que sea un grafo, un tipo algebraico, o un diagrama en alguna categoria. La composicion de structured cospans es via pushout: para componer A -> N1 <- B y B -> N2 <- C, pego N1 y N2 por su interfaz comun B.

Este es exactamente el patron de Terraform modules. Un modulo de Terraform tiene:

- Variables de entrada (interfaz izquierda A)
- Outputs (interfaz derecha B)
- Recursos internos (implementacion N)

Cuando compongo dos modulos, la composicion es un pushout: los outputs de uno se identifican con las variables de entrada del otro en la interfaz compartida. Los recursos internos se pegan coherentemente. Y la propiedad universal del pushout garantiza que el modulo compuesto es el "mas pequeno" que implementa ambas partes.

```
module_vpc(cidr) -> [vpc_id, subnet_ids]
module_eks(vpc_id, subnet_ids) -> [cluster_endpoint, kubeconfig]

composed = pushout(module_vpc, module_eks, over: {vpc_id, subnet_ids})
```

## El metodo CMD: ingenieria de sistemas categorica paso a paso

Mordecai y Engel proponen un proceso concreto -- el Categorical Multimodal Design (CMD) -- para aplicar teoria de categorias a la ingenieria de sistemas reales. Lo que me resulta valioso no es solo la formalizacion, sino el proceso iterativo que definen:

**Paso 0: CMD Master.** Un equipo que supervisa la consistencia de todo el diseno. En terminos categoricos, es el funtor que conecta todas las categorias de diseno con la Common Design Knowledge Base (CDKB).

**Paso 1: Expert Knowledge Bases (EKB).** Cada disciplina (mecanica, electrica, software, seguridad) define su propia categoria de diseno con sus objetos, morfismos y reglas. Esto es lo que en el documento 10 llame una fibra: cada disciplina es una fibra sobre la base comun.

**Paso 2: Expert Models (EM).** Cada disciplina construye sus modelos especificos usando los tipos y relaciones de su EKB. Un EM es un diagrama en la categoria de la disciplina.

**Paso 3: Semantic Integration Model (SIM).** Las reglas de traduccion entre disciplinas se formalizan como funtores entre las categorias de diseno. Estos funtores deben preservar los boundary objects -- los objetos compartidos entre disciplinas.

**Paso 4: Integrated Design Graph (IDG).** Toda la informacion se funde en un unico diagrama, que es el colimite de todos los EMs sobre sus interfaces compartidas. Aqui aparecen las construcciones universales del documento 05.

**Paso 5: Integrated Design Views (IDV).** Vistas especificas para stakeholders, generadas por funtores desde el IDG.

## El BEV: un ejemplo concreto de composicion categorica

En el ejemplo del Battery Electric Vehicle que Engel detalla, la categoria base tiene tres tipos fundamentales: Vehicle, PowerSystem y Energy, conectados por los morfismos *has* (Vehicle -> PowerSystem) y *uses* (PowerSystem -> Energy). La composicion has;uses dice: todo vehiculo usa alguna forma de energia, indirectamente a traves de su power system.

Lo que la estructura categorica revela es que las especializaciones (BatteryElectricVehicle, BatteryPowerSystem, ElectricalEnergy) estan conectadas por isomorfismos y composiciones que derivan automaticamente:

```
BEV  --is-->  Vehicle  --has-->  PowerSystem  --uses-->  Energy
                                      |                     |
                                    canBe                 canBe
                                      |                     |
                              BatteryPowerSystem  --uses--> ElectricalEnergy
```

La composicion *is;has;uses;canBe* se simplifica a *uses''* : BEV -> ElectricalEnergy. Y las design rules de la Expert Knowledge Base -- "todo PowerSystem debe tener Lifespan >= 15 anos y OpHrs >= 12000" -- se propagan automaticamente a BatteryPowerSystem por la functorialidad del mapeo de EKB a EM.

Los boundary objects (el voltaje bajo que fluye del power converter al sistema auxiliar, el torque que el motor electrico transmite a la transmision) son exactamente los objetos compartidos entre subsystem categories. Coordinar boundary objects es coordinar las interfaces del pushout.

## Lambda+ y la verificacion composicional de arquitecturas

Gillet, Leclercq y Cullot atacan un problema que todo arquitecto de datos enfrenta: ¿como garantizar que las propiedades de los componentes individuales se conservan en la composicion? Su formalizacion de la Lambda Architecture con teoria de categorias revela algo que la arquitectura original escondia.

Definen tres categorias: Components (los componentes del sistema), Architecture (las interacciones entre ellos), y ComponentsPS (el power set de componentes para rastrear composiciones). Los funtores CPS-Correctness y CPS-RealTime mapean composiciones de componentes a sus propiedades.

El resultado es brutal en su claridad: la Lambda Architecture original no conserva ni la propiedad de correctness ni la de real-time en la composicion total. Batch tiene Correctness = True, Speed tiene Real-time = True, pero la composicion {Batch, Serving, Speed} tiene ambas en False. La razon es categorica: si un componente individual no soporta una propiedad, la composicion la pierde.

Este es un principio general que aplico constantemente: las propiedades no se suman en la composicion. Se intersecan. Un pipeline es tan confiable como su componente menos confiable. Un sistema es tan seguro como su eslabón mas débil. Y la teoria de categorias formaliza exactamente por que: los funtores que mapean composiciones a propiedades son monotonos, y el preorder de propiedades tiene la interseccion como meet.

## Manufactura como colimite

Kovalyov cierra el circulo con una aplicacion que conecta directamente con las construcciones universales del documento 05. En la manufactura model-based, un producto ensamblado de partes P y S con un pegamento G es literalmente un pushout:

```
    P <--f-- G --g--> S
    |                  |
    v                  v
    R = pushout(f, g)
```

El modelo del producto R es el colimite del diagrama. La propiedad universal dice: R es el modelo mas pequeno que contiene tanto P como S y respeta las relaciones de ensamblaje definidas por G. Si el pushout no existe -- si las piezas no encajan -- no hay modelo consistente del producto ensamblado.

Lo notable es que Kovalyov extiende esto al problema inverso: dada una especificacion R del producto final, encontrar las configuraciones de ensamblaje que lo producen. Esto es exactamente el problema de factorizar un colimite en sus componentes -- el dual del problema de descomposicion que uso cada vez que refactorizo un sistema monolitico en microservicios.

## Composicion a escala: la perspectiva unificada

Lo que une las operads, las double categories, los structured cospans y el metodo CMD es una misma intuicion: componer a escala requiere ser explicito sobre las interfaces. En una categoria ordinaria, los morfismos son la unica dimension de estructura. Pero los sistemas reales tienen jerarquia (operads), tienen multiples dimensiones de relacion (double categories), y tienen interfaces compartidas que deben coordinarse (structured cospans y pushouts).

El metodo CMD de Mordecai y Engel traduce esta intuicion a un proceso de ingenieria: definir categorias de diseno, especificar boundary objects, construir funtores entre vistas, y validar la consistencia del colimite integrado. Los pasos formales son los del documento 05 -- limites, colimites, pullbacks, pushouts -- pero aplicados sistematicamente a un proceso de diseno multimodal.

Para mi practica diaria, la leccion es que la composicion no escala si las interfaces son implicitas. Cada modulo de Terraform necesita variables y outputs explícitos. Cada microservicio necesita un contrato de API. Cada disciplina de ingenieria necesita boundary objects declarados. La teoria de categorias no inventa esta necesidad -- la formaliza, y al formalizarla, me da herramientas para verificar que la composicion es correcta antes de construirla.
