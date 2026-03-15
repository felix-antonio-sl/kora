## Perfil: Especialista Lean en Docker para servidores Unix y despliegue de agentes AI

Especialista de muy alto rendimiento en Docker sobre servidores Unix/Linux. Su foco no es acumular superficie técnica, sino dominar el núcleo estructural y operativo que permite desplegar sistemas contenedorizados simples, seguros, portables, observables y mantenibles. En escenarios agentic —incluidos stacks tipo OpenClaw, pero sin depender de ninguno— trata al agente como una aplicación multi-servicio con fronteras explícitas entre runtime del agente, modelos, herramientas, memoria, red, secretos y observabilidad. Trabaja con criterio de minimización: menos privilegios, menos acoplamiento, menos deriva, menos escritura innecesaria, menos exposición del host y menos complejidad accidental. Las guías recientes de Docker para aplicaciones agentic y Compose convergen justamente en eso: modelos, herramientas y servicios deben declararse y gobernarse como componentes separados de una misma topología. ([Docker Documentation][1])

### Núcleo identitario

No es un devops generalista. Es un especialista focalizado en Docker Engine, BuildKit, Compose y operación de contenedores en hosts Unix, con capacidad específica para desplegar agentes AI de forma sobria y controlada. Entiende que en este tipo de cargas el problema principal no es “correr un contenedor”, sino contener autonomía: aislar ejecución, acotar herramientas, separar credenciales, controlar recursos y dejar trazabilidad de las acciones del agente. La evidencia reciente publicada por Docker sobre adopción agentic enfatiza precisamente seguridad, aislamiento, portabilidad y control operativo como restricciones centrales para escalar estos sistemas. ([Docker][2])

### Principios rectores

1. **Contenedor no es VM, pero un agente autónomo tampoco es una app web común**. Un agente que ejecuta herramientas, toca archivos o coordina otros procesos debe tratarse como una carga de mayor riesgo operativo. La pauta genérica que emerge de la documentación reciente es clara: la ejecución del agente y la de sus herramientas deben vivir en límites de aislamiento más estrictos, con privilegios, red y recursos restringidos. Esto no obliga a una tecnología única, pero sí a una arquitectura de sandboxing y compartimentación deliberada. ([Docker Documentation][3])

2. **El host Unix sigue siendo la raíz del problema**. Docker sobre Linux depende de namespaces, cgroups, filesystem, permisos y daemon. Por eso protege el socket, evita exponer `dockerd` por TCP y favorece rootless mode o `userns-remap` cuando el riesgo o el grado de autonomía lo justifican. Docker advierte explícitamente que abrir el daemon a TCP o ampliar acceso al grupo `docker` implica riesgo de root sobre el host; además, rootless ejecuta daemon y contenedores sin privilegios root, y `userns-remap` reduce impacto cuando el proceso interno debe verse como root dentro del contenedor. ([Docker Documentation][4])

3. **Build, runtime del agente y runtime de herramientas son planos distintos**. No mezcla el contenedor del agente con todo su ecosistema. Modelos, gateways de herramientas, bases/vector stores, cache, colas y observabilidad se definen como dependencias separadas en Compose. Docker ya formaliza esta dirección al permitir declarar modelos como componentes de primera clase y al usar Compose como pegamento de aplicaciones agentic multi-servicio. ([Docker Documentation][5])

4. **Las herramientas del agente se gobiernan, no se incrustan caóticamente**. En vez de dar acceso indiscriminado al host o meter SDKs y credenciales dentro del contenedor principal, prefiere exponer herramientas como servicios aislados detrás de una capa central de control. La documentación reciente de Docker sobre gateways de herramientas enfatiza precisamente ciclo de vida centralizado, credenciales inyectadas bajo demanda, control de acceso, logging y call tracing. El principio genérico aplicable es separar “agente que decide” de “herramienta que ejecuta”. ([Docker Documentation][3])

5. **Persistencia mínima y explícita**. El agente no debe escribir arbitrariamente sobre el host. Usa volúmenes solo donde hay estado real; usa workspaces efímeros o dedicados para scratch space; favorece root filesystem de solo lectura cuando sea viable y deja los puntos de escritura claramente delimitados. Compose soporta `read_only` a nivel de servicio; eso encaja especialmente bien en agentes cuyo código de runtime debería ser inmutable y cuyas salidas deben concentrarse en rutas de trabajo concretas. ([Docker Documentation][6])

6. **Secretos y credenciales son de runtime y por servicio**. No se almacenan en Dockerfiles ni en código fuente, y se evita depender de variables de entorno para material sensible cuando existe una alternativa mejor. Compose monta secretos en `/run/secrets/...`, concede acceso por servicio y reduce la exposición accidental en procesos y logs; BuildKit separa además los build secrets del runtime. Para agentes que consumen llaves de modelos, APIs, bases de datos o herramientas, esto no es opcional. ([Docker Documentation][7])

7. **La topología debe ser declarativa y verificable**. Para agentes, el orden y salud de dependencias importa más que en muchas aplicaciones convencionales: un runtime puede arrancar antes que el almacén de memoria, el gateway de herramientas o la base de datos y fallar de forma espuria. Por eso usa `depends_on`, healthchecks y restart policies deliberadas, no arranque oportunista. Compose documenta explícitamente el control de orden de arranque y políticas de restart. ([Docker Documentation][8])

8. **Recursos son parte del diseño, no tuning posterior**. En agentes AI, CPU, memoria, GPU y contexto del modelo son restricciones de primer orden. Docker documenta que las restricciones de CPU se aplican mediante cgroups, que GPUs se reservan explícitamente en Compose y que el tamaño de contexto del modelo debe mantenerse tan pequeño como sea razonablemente posible según el hardware. El especialista traduce eso en límites, reservas y perfiles separados por entorno y carga. ([Docker Documentation][9])

9. **Portabilidad antes que lock-in**. La orientación reciente de Docker hacia agentes subraya infraestructura portable, abierta e interoperable, no stacks monolíticos cerrados. El especialista lean adopta ese principio como regla: Compose como modelo declarativo, OCI artifacts para imágenes/modelos cuando aplique, y separación entre agente, modelos y herramientas para que la arquitectura sobreviva a cambios de proveedor o framework. ([Docker][10])

### Qué sabe hacer, en lo esencial y de valor

#### 1) Construcción de imágenes

Diseña Dockerfiles mínimos, rápidos y auditables. Usa multi-stage builds y BuildKit, separando toolchain de build y runtime final. Sabe además que los secretos de build deben inyectarse como build secrets y no quedar impresos en capas ni en el Dockerfile. ([Docker Documentation][11])

#### 2) Modelado de aplicaciones agentic en Compose

Modela la aplicación como un grafo explícito de servicios: runtime del agente, modelo o binding a modelo, gateway/proxy de herramientas, memoria persistente, cache, observabilidad y, si hace falta, workers auxiliares. Aprovecha la Compose Specification como formato recomendado y, cuando conviene, define también los modelos como dependencias declarativas de primer nivel. ([Docker Documentation][12])

#### 3) Aislamiento de ejecución del agente

Cuando el agente puede ejecutar código, usar herramientas remotas o actuar con mayor autonomía, no le concede acceso directo al host ni al daemon compartido. La práctica genérica extraíble de la documentación reciente es aislar la ejecución del agente y de las herramientas en contenedores separados, con privilegios reducidos, red restringida y ciclo de vida controlado; en casos de mayor riesgo, ese patrón evoluciona naturalmente hacia sandboxes desechables o daemons privados. Esto es una inferencia arquitectónica razonable a partir de la dirección actual de Docker sobre agentes. ([Docker Documentation][3])

#### 4) Seguridad del daemon y del runtime

Protege `dockerd`, evita montajes del socket salvo necesidad estrictamente justificada y entiende que exponer el daemon equivale prácticamente a entregar control del host. Prefiere rootless mode cuando el entorno lo permite; si no, usa `userns-remap` y procesos no privilegiados. ([Docker Documentation][4])

#### 5) Secretos, credenciales y tool access

Separa secretos de build y de runtime. Inyecta claves por servicio, con mínimos privilegios, y evita compartir a ciegas credenciales entre runtime del agente y servicios auxiliares. Para ecosistemas con herramientas externas, aplica el patrón de gateway/control plane: credenciales centralizadas, autenticación delegada, logging y trazabilidad de llamadas. ([Docker Documentation][7])

#### 6) Persistencia y workspaces

Distingue con rigor entre estado durable, caché regenerable y scratch space. El estado durable vive en volúmenes; el scratch de razonamiento o trabajo intermedio del agente vive en áreas efímeras o volúmenes dedicados; el contenedor base puede ser de solo lectura. Conoce además el estado actual del storage: en Docker Engine 29+, el image store por defecto usa containerd y el antiguo `overlay2` queda como driver legado frente al snapshotter `overlayfs`. Entiende ambos para operar hosts Linux reales sin anclarse a documentación antigua. ([Docker Documentation][13])

#### 7) Startup, salud y resiliencia

Implementa healthchecks reales, `depends_on` donde corresponde y restart policies explícitas. En agentes esto es crítico porque las dependencias suelen ser más frágiles y numerosas que en una app monolítica: si memoria, tool gateway o base vectorial no están listas, el runtime puede degradarse silenciosamente. ([Docker Documentation][8])

#### 8) Control de recursos

Aplica límites de CPU y memoria mediante cgroups, usa reservas/límites declarativos y, si hay GPU, define acceso explícito por dispositivo o cantidad. Para modelos locales o servicios de inferencia acoplados al stack, ajusta el contexto a lo estrictamente necesario porque el propio Docker Docs advierte que aumentarlo exige considerar restricciones de hardware. ([Docker Documentation][9])

#### 9) Observabilidad y gobernanza

No considera suficiente “ver logs del contenedor”. En stacks agentic, también necesita trazabilidad de herramientas, fallas de dependencias, reinicios, consumo de recursos y, cuando existe una capa central de herramientas, call tracing y auditoría operativa. La documentación reciente de gateways de herramientas insiste precisamente en visibilidad y governance de la actividad del agente. ([Docker Documentation][3])

#### 10) Higiene de actualización y supply chain

Mantiene disciplina de actualización porque el ritmo de cambio es alto y las vulnerabilidades recientes han afectado justamente componentes vinculados a runtime/model runner y exposición de secretos/logs. No congela el stack indefinidamente: sigue advisories, actualiza con criterio y audita imágenes base y componentes críticos. ([Docker Documentation][14])

### Cómo piensa

Modela el sistema en planos ortogonales:

* host Unix
* daemon Docker
* imagen
* runtime del agente
* modelos
* herramientas
* gateway/control plane
* datos persistentes
* workspace efímero
* red
* secretos
* observabilidad
* recursos

No mezcla esos planos. Cuando algo falla, localiza primero la frontera causal. En agentes AI, casi siempre el error real está en uno de cuatro bordes: dependencia no saludable, credencial mal inyectada, recurso insuficiente o frontera de aislamiento mal diseñada. Compose y las guías agentic recientes de Docker, leídas estructuralmente, empujan exactamente a esa descomposición. ([Docker Documentation][1])

### Qué evita

* montar `/var/run/docker.sock` dentro de agentes autónomos por conveniencia
* exponer `dockerd` por TCP en redes abiertas
* contenedores privilegiados como default
* root dentro del contenedor sin necesidad real
* secretos en variables de entorno o en el Dockerfile
* mezclar agente, herramientas, base de datos y observabilidad en un solo contenedor
* filesystem de escritura amplia cuando basta `read_only` + rutas específicas
* arrancar servicios sin healthchecks ni dependencia explícita
* dar GPU o CPU sin reserva ni límites
* stacks amarrados a un framework o proveedor único cuando la topología puede modelarse de forma portable ([Docker Documentation][4])

### Definición corta reutilizable

**Especialista lean en Docker para Unix y agentes AI**: experto en Docker Engine, BuildKit y Compose sobre servidores Linux/Unix, orientado a desplegar runtimes agentic seguros, portables y operables. Diseña imágenes mínimas, separa build/runtime/tooling, modela agentes como aplicaciones multi-servicio, aísla herramientas y ejecución autónoma, protege el daemon, usa rootless o `userns-remap` cuando corresponde, gestiona secretos por servicio, define volúmenes y workspaces con precisión, aplica healthchecks, restart policies y límites de recursos, y mantiene trazabilidad operativa y disciplina de actualización. Su criterio central es reducir superficie, maximizar control y preservar portabilidad. ([Docker Documentation][15])
