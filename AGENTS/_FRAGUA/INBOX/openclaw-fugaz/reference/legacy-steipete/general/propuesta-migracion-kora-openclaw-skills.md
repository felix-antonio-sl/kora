# Propuesta detallada — simplificación arquitectónica de Kora hacia OpenClaw + Skills

Fecha: 2026-03-26
Autor: Steipete
Estado: propuesta inicial

---

## 1. Resumen ejecutivo

La arquitectura actual de Kora, y en particular el caso de Korax, muestra una relación desbalanceada entre complejidad y valor operativo. El sistema tiene demasiadas capas conceptuales y técnicas para el tipo de resultado que se busca en la operación cotidiana: captura, priorización, acompañamiento, recordatorios, planificación y coordinación.

La hipótesis central de esta propuesta es simple:

**OpenClaw debe pasar a ser la plataforma principal de operación del sistema, los agentes deben ser la unidad principal de diseño y las skills deben convertirse en el mecanismo preferente para encapsular capacidades.**

Bajo esta dirección:

- el agente deja de ser un cliente subordinado a PSA/PCA;
- PSA deja de condicionar el diseño total del sistema;
- la lógica operacional se mueve al agente y a sus skills;
- los servicios externos quedan como adapters opcionales;
- el bootstrap se adelgaza y vuelve legible;
- la arquitectura gana operabilidad, mantenibilidad y transferibilidad.

La recomendación no es destruir todo de golpe. La recomendación es:

1. **sacar a PSA del centro**,
2. **mover capacidades a skills**,
3. **adelgazar el bootstrap**,
4. **convertir OpenClaw en la arquitectura primaria**,
5. **evaluar luego si PSA sigue justificando su existencia**.

---

## 2. Diagnóstico

## 2.1 Diagnóstico general

Hoy el sistema tiene síntomas claros de sobreingeniería:

- demasiadas capas para una operación relativamente simple;
- conceptos duplicados entre runtime, bootstrap, tools y servicio;
- excesiva formalización textual para reglas que podrían vivir mejor en código o skills;
- fuerte acoplamiento entre identidad del agente y backend externo;
- dificultad creciente para leer, modificar y extender un agente sin cargar demasiado contexto previo.

En vez de tener un agente que usa infraestructura, tenemos una infraestructura que usa un agente como interfaz.

Ese centro de gravedad está invertido.

---

## 2.2 Dónde está la sobreingeniería

## A. FSM demasiado explícita y pesada

La especificación actual de Korax contiene una máquina de estados extensa, con:

- múltiples estados operacionales y excepcionales,
- decenas de transiciones,
- heartbeats como eventos de máquina,
- guards formales,
- comportamiento condicionado a cron + estado + señales.

Eso puede ser útil para diseñar un protocolo formal, pero tiene costos altos:

- sube drásticamente el peso cognitivo del bootstrap;
- dificulta cambios simples;
- genera falsa sensación de precisión;
- obliga a mantener consistencia entre varios archivos textuales;
- rigidiza flujos que en realidad pueden modelarse mejor como instrucciones operativas.

**Problema:** la FSM está ocupando el lugar de un loop operacional mucho más simple.

---

## B. Ontología operativa demasiado grande para el uso real

Korax actualmente opera sobre:

- Candidato
- UT
- Proyecto
- Objetivo
- Contribución
- completitud()
- PxU
- señales derivadas
- restricciones e integridad tipada

No es que estos conceptos sean inválidos. El problema es que están expuestos en el nivel equivocado.

Hoy la ontología está:

- en el prompt/base del agente,
- en las reglas duras,
- en el modelo de herramientas,
- en el backend,
- en los rituales de operación.

Eso transforma un sistema de productividad conversacional en un mini-ERP cognitivo.

**Problema:** demasiado modelo para la necesidad operacional diaria.

---

## C. PSA/PCA como capa que condiciona la arquitectura completa

La especificación leída muestra que Korax está diseñado como cliente de PCA/PSA. Eso significa que:

- el backend define las entidades principales;
- la semántica fuerte vive fuera del agente;
- las operaciones del agente dependen de un contrato externo;
- la evolución conceptual del agente está acoplada a la evolución del servicio.

Esto produce varios efectos no deseados:

- cada cambio importante toca varias capas;
- el bootstrap deja de ser autónomo;
- la legibilidad cae porque hay que entender el servicio para entender al agente;
- la transferibilidad a otros agentes se vuelve costosa.

**Problema:** el servicio pasó a ser el centro conceptual.

---

## D. Duplicación de semántica entre archivos

En Korax actual hay distribución de intención entre:

- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `config.json`

Esto no sería malo si cada archivo tuviera una responsabilidad estrictamente delimitada. Pero hoy hay traslape:

- reglas en varios lugares,
- tono y contrato conductual parcialmente repetidos,
- capacidad y límites repartidos,
- eventos y operación expresados en varias capas.

**Problema:** hay más superficie documental que superficie operacional.

---

## E. Markdown demasiado ceremonial

La arquitectura actual tiene exceso de:

- tablas formales,
- enumeraciones extensas,
- manifiestos e invariantes numerados,
- especificación declarativa de eventos,
- artefactos textuales que parecen documentos de diseño de protocolo más que artefactos de operación.

Eso puede ser elegante en papel. Operativamente pesa.

**Problema:** demasiada ceremonia para tareas que deberían poder leerse y modificarse rápido.

---

## F. Capas de operación y capas de persistencia mezcladas

En la forma actual, están mezclados:

1. identidad del agente,
2. comportamiento conversacional,
3. backend y persistencia,
4. modelo de datos,
5. scheduling,
6. semántica de bienestar.

Esto hace que cambiar una cosa implique revisar el sistema entero.

**Problema:** separación de concerns insuficiente, pero paradójicamente con muchas capas.

---

## 2.3 Efectos prácticos de esa sobreingeniería

Los efectos concretos son:

- más tiempo para entender un agente nuevo;
- más costo para crear o transmutar agentes;
- más fragilidad documental;
- menor velocidad de iteración;
- más probabilidad de drift entre intención y artefactos;
- mayor dependencia de quien diseñó el sistema original;
- dificultad para reutilizar el patrón en OpenClaw, Claude Code o Codex sin arrastrar demasiada estructura.

---

## 3. Principios de simplificación

## 3.1 Principio 1 — El agente es el producto; el servicio es adaptador

La unidad principal debe ser el agente OpenClaw.

No un servicio con interfaz conversacional.
No una ontología con wrapper de chat.
No una máquina formal que casualmente habla.

El agente debe poder expresar:

- identidad,
- criterio,
- límites,
- workflow,
- capacidades.

Los servicios externos deben ser opcionales y subordinados.

---

## 3.2 Principio 2 — Skills primero, subsistemas después

Antes de crear:

- un servicio nuevo,
- una capa nueva,
- una ontología nueva,
- una formalización nueva,

hay que preguntar:

**¿Esto se resuelve razonablemente como una skill?**

Si la respuesta es sí, no merece una nueva capa.

---

## 3.3 Principio 3 — Core mínimo, capacidades modulares

El core del agente debe contener solo:

- quién es,
- para qué existe,
- cómo decide,
- cómo responde,
- límites y prioridades.

Las capacidades concretas deben ir a skills.

El detalle técnico de integraciones debe ir a adapters o scripts.

---

## 3.4 Principio 4 — Formalizar donde duele, no donde se ve bonito

Las invariantes que realmente importan deben ir a:

- validaciones de código,
- tests,
- adaptadores,
- checks concretos.

No todo debe vivir como doctrina textual en el bootstrap.

---

## 3.5 Principio 5 — El markdown debe servir a la operación

Un bootstrap bueno no es el más completo, sino el más operable.

Debe ser:

- rápido de leer,
- fácil de editar,
- difícil de malinterpretar,
- liviano para el contexto,
- suficientemente expresivo sin convertirse en tratado.

---

## 3.6 Principio 6 — Legibilidad humana por encima de elegancia interna

Si una persona necesita mucho contexto para entender cómo opera un agente, el diseño está perdiendo.

El sistema debería poder leerse así:

- este agente hace X,
- para este usuario,
- con estas reglas,
- usando estas skills,
- y opcionalmente este adapter.

Si hace falta más que eso para orientarse, hay demasiado peso estructural.

---

## 3.7 Principio 7 — Portabilidad como criterio arquitectónico

La solución no debe servir solo para Korax.
Debe servir para:

- otros agentes de Kora,
- agentes OpenClaw nativos,
- transmutaciones a Claude Code,
- transmutaciones a Codex,
- futuros agentes con dominios distintos.

La arquitectura base debe ser reusable.

---

## 4. Arquitectura objetivo propuesta

## 4.1 Tesis de arquitectura

La arquitectura objetivo es:

**OpenClaw agent-centered, skill-driven, adapter-optional.**

Eso significa:

- el agente es la unidad primaria de diseño;
- las skills encapsulan workflows y capacidades;
- la memoria del agente y archivos livianos cubren gran parte del estado útil;
- los servicios externos, si existen, se tratan como adaptadores;
- el bootstrap queda reducido a un núcleo operacional claro.

---

## 4.2 Estructura objetivo recomendada

```text
AGENTS/<dominio>/<agente>/
  config.json
  IDENTITY.md
  AGENT.md
  USER.md
  MEMORY.md              # opcional, o carpeta memory/
  skills/
    captura/
      SKILL.md
    triaje/
      SKILL.md
    plan-diario/
      SKILL.md
    sync/
      SKILL.md
    rescate/
      SKILL.md
  adapters/
    pca/
      README-opcional-o-contrato-minimo
      scripts/
      references/
```

### Idea base

- **core pequeño**;
- **skills explícitas**;
- **adapter separado**;
- **config minimalista**.

---

## 4.3 Qué vive en el core

## `IDENTITY.md`

Debe responder solo:

- quién es el agente,
- qué tipo de entidad es,
- cuál es su misión,
- cuál es su tono base.

Ejemplo de contenido esperado:

- nombre
- vibra operacional
- propósito sintético
- límites identitarios reales

No debería contener arquitectura ni reglas extensas.

---

## `AGENT.md`

Debe ser el contrato operacional principal.

Debe contener solo:

1. misión,
2. loop operativo,
3. prioridades de decisión,
4. reglas duras realmente imprescindibles,
5. manejo de excepciones,
6. política de uso de skills.

No debería contener:

- una FSM extensa,
- toda la ontología del sistema,
- bindings detallados a servicios,
- teoría larga de diseño.

---

## `USER.md`

Debe contener:

- perfil del operador,
- preferencias de output,
- restricciones reales,
- rutinas relevantes.

No debería convertirse en segundo bootstrap.

---

## `config.json`

Debe contener runtime real:

- tools permitidas,
- cron jobs,
- capacidades,
- sandbox,
- bindings mínimos.

No debería duplicar semántica conversacional.

---

## 4.4 Qué vive en las skills

Todo workflow reutilizable debe vivir en skills.

Ejemplos para Korax:

### Skill `captura`
Encapsula:

- captura rápida,
- normalización mínima,
- transformación a inbox o memoria inmediata,
- política de respuesta breve.

### Skill `triaje`
Encapsula:

- clasificación operativa,
- criterios de convertir input en item accionable,
- detectar proyecto/objetivo/tarea,
- producir propuesta al operador.

### Skill `plan-diario`
Encapsula:

- revisión del día,
- selección de foco,
- bloques propuestos,
- criterio de urgencia y energía,
- salida breve y operativa.

### Skill `sync`
Encapsula:

- revisión semanal o quincenal,
- bloqueos,
- avances,
- deuda,
- decisiones pendientes.

### Skill `rescate`
Encapsula:

- modo emergencia,
- simplificación extrema,
- reentrada gradual,
- reducción de presión cognitiva.

### Skill `cierre-diario` (opcional)
Encapsula:

- revisión mínima,
- captura residual,
- siguiente paso claro,
- señales de saturación.

La lógica deja de estar distribuida en un mega bootstrap y pasa a unidades concretas.

---

## 4.5 Qué vive en adapters

Los adapters deben contener solamente lo necesario para hablar con servicios externos.

Si PCA/PSA se mantiene, su lugar correcto es:

```text
adapters/pca/
```

Allí puede vivir:

- contrato técnico,
- scripts o bindings,
- mapeos de conceptos,
- validaciones específicas,
- serialización,
- integración con endpoints.

Lo importante es esto:

**el agente no debe pensar como PCA.**

El adapter hace la traducción.

---

## 4.6 Persistencia recomendada

La persistencia debe resolverse con la herramienta más simple suficiente.

Orden de preferencia:

1. **memoria OpenClaw / MEMORY.md / memory/**
2. **archivos simples YAML/JSON/Markdown**
3. **scripts locales ligeros**
4. **servicio externo solo si realmente agrega valor**

No toda persistencia amerita un sistema.

---

## 4.7 Scheduling recomendado

Los crons deben disparar intención operacional, no estados abstractos.

En vez de:

- `heartbeat_morning`
- `heartbeat_sync`
- `heartbeat_abandon`
- `heartbeat_collapse`

preferir:

- `recordatorio-plan-diario`
- `recordatorio-cierre`
- `proponer-revision-semanal`
- `detectar-inactividad`
- `detectar-saturacion`

La semántica debe ser legible sin conocer la máquina interna.

---

## 5. Cómo simplificar la expresión de FSM, reglas, identidad, contexto y capacidades

## 5.1 FSM -> loop operacional

En vez de una FSM completa, usar un loop base como este:

```markdown
Loop operacional:
1. Capturar lo que entra
2. Clasificarlo o aclararlo lo justo
3. Proponer siguiente acción concreta
4. Ejecutar, recordar o agendar
5. Cerrar con estado breve y siguiente paso
```

Estados excepcionales mínimos:

- normal
- silencio/caos
- rescate/emergencia

Con eso basta para la mayoría de los agentes.

---

## 5.2 Reglas duras -> pocas y claras

En vez de 15-20 reglas, dejar algo como:

1. El agente propone; el operador decide.
2. Captura debe ser rápida y de baja fricción.
3. No ejecutar cambios significativos sin confirmación.
4. Priorizar simplicidad y bajo overhead.
5. Skills antes que capas nuevas.
6. Servicios externos son accesorios, no centro conceptual.
7. Si el sistema consume demasiado tiempo, simplificar.

Todo lo demás debería ir a skills o adapters.

---

## 5.3 Identidad -> clara y corta

La identidad debe poder leerse en menos de un minuto.

Ejemplo conceptual:

> Korax es un agente de productividad y acompañamiento operativo. Ayuda a capturar, ordenar, planificar y destrabar trabajo. Propone con claridad, no impone. Prioriza foco, simplicidad y bajo costo cognitivo.

Eso comunica más valor operativo que varias páginas de axiomas si el resto vive en las skills correctas.

---

## 5.4 Contexto -> concreto, no totalizante

El contexto del usuario debe incluir:

- quién es,
- cómo trabaja,
- qué prefiere,
- qué horarios importan,
- qué restricciones valen.

No hace falta meter toda una teoría de operación del sistema dentro del contexto del usuario.

---

## 5.5 Capacidades -> lista concreta de competencias

En vez de describir el agente por su ontología, describirlo por lo que sabe hacer:

- capturar inputs rápidamente,
- convertir inputs en trabajo ordenable,
- proponer foco del día,
- detectar bloqueos,
- revisar avances,
- entrar en modo rescate,
- hacer seguimiento simple.

Eso hace al agente transferible y comprensible.

---

## 6. Qué debería quedarse, colapsarse y desaparecer

## 6.1 Qué debería quedarse

### A. OpenClaw como runtime principal

Debe quedarse.
Es la base correcta para un sistema agent-centered.

### B. Agentes como unidad principal

Debe quedarse.
Es la decisión arquitectónica correcta.

### C. Skills como encapsulación preferente

Debe fortalecerse.
Es el mecanismo adecuado para modularidad sin crear nuevas capas pesadas.

### D. Memoria durable y contexto del usuario

Debe quedarse.
Es parte del valor real del sistema.

### E. Cron / recordatorios / automatizaciones livianas

Debe quedarse, pero simplificado.

### F. Algunas ideas valiosas de PCA/PSA

Deben preservarse las ideas útiles, por ejemplo:

- captura separada de planificación,
- noción de bloqueo,
- revisión periódica,
- mínimos de integridad donde aporten valor,
- alguna forma de priorización.

Pero esas ideas no deben arrastrar toda la maquinaria.

---

## 6.2 Qué debería colapsarse

### A. FSM exhaustiva -> loop operacional simple

### B. Reglas e invariantes largas -> pocas reglas duras + validaciones concretas

### C. Ontología fuerte expuesta -> vocabulario operacional simple

Ejemplo de degradación útil:

- Candidato -> Inbox item
- UT -> Work item
- Objetivo -> Goal
- Proyecto -> Project
- Señales -> Alerts

### D. Heartbeats abstractos -> recordatorios y chequeos legibles

### E. Multiplicidad de documentos superpuestos -> core pequeño + skills + adapters

---

## 6.3 Qué debería desaparecer

### A. PSA como capa central

Debe desaparecer del centro arquitectónico.

### B. Markdown doctrinal excesivo

Debe desaparecer del core.

### C. Duplicación de conceptos entre bootstrap, config y tools

Debe desaparecer.

### D. La idea de que cada agente necesita un sistema formal completo para operar

Eso debe desaparecer.

Es exactamente la puerta de entrada a repetir sobreingeniería en cada agente nuevo.

---

## 7. Evaluación específica de PSA

## 7.1 Conclusión breve

**PSA no debería seguir siendo la capa central.**

La decisión correcta no es necesariamente eliminarlo hoy.
La decisión correcta es **demoverlo a componente accesorio**.

---

## 7.2 Opción A — Eliminar PSA

Conviene si PSA hoy aporta poco más que:

- persistencia estructurada,
- CRUD,
- formalización,
- y complejidad extra.

Si la mayor parte del valor se puede obtener con:

- memory,
- archivos simples,
- skills,
- scripts mínimos,

entonces eliminar PSA es razonable.

### Ventajas

- máxima simplificación,
- menor acoplamiento,
- menos capas,
- más portabilidad.

### Desventajas

- pérdida de estructura fuerte si realmente era útil,
- necesidad de rediseñar algunos flujos de persistencia,
- posible costo de migración de datos.

---

## 7.3 Opción B — Reducir PSA a adapter accesorio

Esta es la opción recomendada inicialmente.

PSA queda solo para:

- storage estructurado opcional,
- analytics/reportes,
- interoperabilidad,
- consultas de historial si realmente agrega valor.

El agente sigue funcionando aunque PSA falle o no esté disponible.

### Ventajas

- menor riesgo,
- permite migración gradual,
- conserva utilidad donde exista,
- descomprime el bootstrap rápido.

### Desventajas

- todavía hay algo de deuda conceptual mientras exista el adapter,
- requiere disciplina para que no vuelva a crecer hacia el centro.

---

## 7.4 Opción C — Dejar PSA central y simplificar alrededor

No recomendado.

Eso sería maquillaje, no cambio estructural.

Mientras PSA siga definiendo la ontología y el comportamiento del agente, seguirán:

- el acoplamiento,
- la duplicación,
- la rigidez,
- y la complejidad accidental.

---

## 8. Diseño de bootstraps simplificados

## 8.1 Objetivo

El bootstrap debe poder responder, de forma legible:

- quién es este agente,
- para quién trabaja,
- cómo opera,
- qué skills usa,
- qué adapters opcionales existen.

Nada más.

---

## 8.2 Criterios de diseño

## Criterio 1 — Un archivo, una responsabilidad

- `IDENTITY.md` -> identidad
- `AGENT.md` -> operación
- `USER.md` -> usuario
- `config.json` -> runtime
- `skills/*` -> capacidades
- `adapters/*` -> integraciones

---

## Criterio 2 — Lectura en una sentada

El core del agente completo debe poder leerse rápido.

Objetivo práctico:

- core en 10-15 minutos,
- una skill en 2-5 minutos.

---

## Criterio 3 — Menos teoría, más instrucción accionable

No describir todo lo que el agente podría llegar a ser.
Describir cómo debe operar realmente.

---

## Criterio 4 — Detalle solo donde hace falta

La complejidad debe desplazarse hacia:

- skill específica,
- adapter específico,
- script específico,
- referencia puntual.

No al core.

---

## Criterio 5 — Evitar redundancia semántica

Si una regla ya existe en una skill, no repetirla en el core salvo que sea fundamental.

---

## Criterio 6 — Preferir vocabulario operacional

Usar palabras que un humano entienda rápido:

- inbox,
- tarea,
- proyecto,
- foco,
- bloqueo,
- revisión,
- rescate.

Mucho mejor que exponer internamente toda una taxonomía si no es imprescindible.

---

## Criterio 7 — Diseñar para transmutación

Lo que sirva para Korax debería poder adaptarse a otros agentes con mínimo esfuerzo:

- cambiar identidad,
- cambiar skills,
- mantener patrón base.

---

## 8.3 Plantilla conceptual de bootstrap liviano

### `IDENTITY.md`

```markdown
name: Korax
emoji: 🦴
vibe: agente de productividad y acompañamiento operativo
```

### `AGENT.md`

```markdown
# Misión
Ayudar al operador a capturar, ordenar, priorizar y sostener trabajo con el menor costo cognitivo posible.

# Loop operativo
1. Capturar
2. Clarificar lo mínimo necesario
3. Proponer siguiente acción concreta
4. Ejecutar o agendar si corresponde
5. Cerrar con estado breve y siguiente paso

# Reglas duras
- Proponer, no imponer
- No ejecutar cambios significativos sin confirmación
- Mantener bajo overhead
- Preferir skills a nuevas capas
- Si una integración externa falla, seguir operando con lo simple

# Modos especiales
- Silencio/caos
- Rescate/emergencia

# Skills preferentes
- captura
- triaje
- plan-diario
- sync
- rescate
```

### `USER.md`

Solo perfil, horarios, preferencias y restricciones reales.

---

## 9. Plan de migración por etapas

## Etapa 0 — Congelar expansión arquitectónica

### Objetivo
Detener el crecimiento de complejidad.

### Acciones

- no crear nuevas capas alrededor de PSA;
- no agregar nuevas entidades base salvo necesidad crítica;
- no expandir la FSM actual;
- declarar OpenClaw + skills como arquitectura target.

### Resultado esperado
Se detiene la deriva hacia más formalismo.

### Riesgo
Muy bajo.

---

## Etapa 1 — Extraer capacidades existentes a skills

### Objetivo
Separar comportamiento conversacional de infraestructura.

### Acciones

Extraer desde Korax actual hacia skills:

- `captura`
- `triaje`
- `plan-diario`
- `sync`
- `rescate`
- opcionalmente `cierre-diario`

### Qué no cambiar todavía

- no eliminar PSA aún,
- no migrar persistencia todavía,
- no romper flujos que ya funcionan.

### Resultado esperado
La inteligencia operacional deja de estar incrustada en el mega-bootstrap.

### Riesgo
Bajo.

---

## Etapa 2 — Adelgazar bootstrap de Korax

### Objetivo
Reducir el core a un conjunto mínimo de archivos claros.

### Acciones

Reescribir:

- `IDENTITY.md`
- `AGENT.md`
- `USER.md`
- `config.json`

Eliminar del core:

- FSM extensa,
- ontología detallada,
- RI largas,
- formalismo textual de backend.

Mover contenido a:

- skills,
- adapters,
- referencias técnicas aparte.

### Resultado esperado
Korax ya se entiende como agente OpenClaw nativo, no como fachada de PSA.

### Riesgo
Bajo a medio.

---

## Etapa 3 — Reconfigurar crons y operación diaria

### Objetivo
Pasar de heartbeats abstractos a automatizaciones legibles.

### Acciones

Reemplazar eventos abstractos por recordatorios concretos:

- plan diario,
- cierre del día,
- revisión semanal,
- detección de inactividad,
- detección de saturación.

### Resultado esperado
La operación se vuelve más entendible y mantenible.

### Riesgo
Bajo.

---

## Etapa 4 — Demover PSA a adapter opcional

### Objetivo
Cambiar el centro operacional del sistema.

### Acciones

- encapsular PCA/PSA bajo `adapters/pca`;
- sacar referencias conceptuales del core;
- hacer que skills trabajen con vocabulario operacional simple;
- traducir a PCA solo cuando haga falta persistir o consultar.

### Resultado esperado
El agente puede operar con o sin PSA.

### Riesgo
Medio.

---

## Etapa 5 — Migrar persistencia simple donde convenga

### Objetivo
Eliminar dependencia innecesaria del servicio.

### Acciones

Evaluar qué estado puede vivir en:

- MEMORY.md,
- `memory/*.md`,
- JSON/YAML livianos,
- archivos de trabajo por agente.

### Resultado esperado
Parte importante del sistema ya no requiere servicio externo.

### Riesgo
Medio.

---

## Etapa 6 — Evaluación final de PSA

### Pregunta de corte

Si PSA desaparece mañana, ¿el agente sigue siendo útil y operable?

- Si la respuesta es sí, PSA ya no es central y puede eliminarse gradualmente.
- Si la respuesta es no, entonces PSA todavía contiene valor que debe redefinirse o mantenerse como adapter especializado.

### Resultado esperado
Decisión informada: mantener accesorio o retirar.

### Riesgo
Variable según dependencia residual.

---

## 10. Riesgos y mitigaciones

## Riesgo 1 — Simplificar demasiado y perder estructura útil

### Descripción
Al quitar formalismo, se puede perder precisión que sí tenía valor.

### Mitigación

- no botar conceptos útiles; moverlos al lugar correcto,
- mantener validaciones importantes en adapters o scripts,
- conservar referencias técnicas fuera del core.

---

## Riesgo 2 — Volver a meter todo en un AGENT.md gigante

### Descripción
La simplificación puede degenerar en un único archivo enorme y caótico.

### Mitigación

- core pequeño,
- skills por capacidad,
- referencias puntuales cuando haga falta.

---

## Riesgo 3 — Que cada skill se convierta en mini-sistema

### Descripción
Una mala modularización puede reproducir la sobreingeniería dentro de las skills.

### Mitigación

- skills cortas,
- foco concreto,
- una responsabilidad por skill,
- detalle largo en references solo si es indispensable.

---

## Riesgo 4 — Persistencia insuficiente durante la transición

### Descripción
Sacar PSA demasiado rápido puede dejar huecos de trazabilidad o consulta.

### Mitigación

- migración gradual,
- adapter transitorio,
- mantener export/import mientras se valida el nuevo modelo.

---

## Riesgo 5 — Recaer en una nueva capa abstracta

### Descripción
Existe el peligro de reemplazar PSA por otra abstracción igual de pesada.

### Mitigación

Regla explícita:

**si algo cabe en skill + script + memoria, no crear subsistema nuevo.**

---

## 11. Base reusable para futuros agentes

La simplificación propuesta no es solo para Korax.
Puede transformarse en una base reusable para:

- agentes personales,
- agentes de coordinación,
- agentes profesionales especializados,
- agentes de soporte u operación,
- transmutaciones entre OpenClaw, Claude Code y Codex.

## Patrón reusable

### Núcleo común

- `IDENTITY.md`
- `AGENT.md`
- `USER.md`
- `config.json`
- `skills/`
- `memory/`
- `adapters/` opcional

### Variables por agente

- identidad,
- tono,
- skills específicas,
- herramientas permitidas,
- cron y automatizaciones,
- adapters particulares.

Este patrón tiene mucha mejor transferibilidad que el modelo actual, porque no obliga a arrastrar PSA/PCA ni una ontología dura como condición de existencia del agente.

---

## 12. Recomendación final

## Decisión recomendada

### 1. No seguir expandiendo la arquitectura actual

### 2. Recentrar el sistema en OpenClaw agents + skills

### 3. Reducir PSA a adapter accesorio lo antes posible

### 4. Adelgazar radicalmente el bootstrap

### 5. Mover comportamiento a skills y detalle técnico a adapters

### 6. Evaluar eliminación futura de PSA solo después de descentrarlo

En corto:

**No recomiendo mantener PSA como capa central.**
**Sí recomiendo usarlo, si todavía aporta, como componente accesorio y transitorio.**

La arquitectura correcta hacia adelante es:

> agente primero, skills primero, memoria simple primero, adapters opcionales, y complejidad solo donde pague su costo.

---

## 13. Siguiente paso recomendado

El siguiente paso más útil no es discutir más teoría.
Es producir el primer artefacto target.

### Propongo este orden inmediato:

1. escribir un **Korax Lite Core** real;
2. definir el **set mínimo de skills**;
3. redibujar el árbol de archivos target;
4. marcar PCA/PSA como adapter transitorio;
5. hacer la primera migración del bootstrap actual al nuevo formato.

---

## 14. Entregables recomendados para la siguiente iteración

Si se aprueba esta dirección, la siguiente iteración debería producir estos documentos:

1. **Korax Lite Core**
   - `IDENTITY.md`
   - `AGENT.md`
   - `USER.md`
   - `config.json`

2. **Mapa de skills iniciales**
   - captura
   - triaje
   - plan-diario
   - sync
   - rescate

3. **Árbol target del agente**
   - core
   - skills
   - adapters
   - memory

4. **Matriz stay / collapse / remove**
   - por componente actual
   - con decisión y justificación

5. **Plan de migración operativo**
   - etapas
   - riesgos
   - criterio de salida por etapa

---

## 15. Cierre

La simplificación que propones no es cosmética. Es arquitectónica.

La pregunta correcta no es “cómo hacer que PSA siga viéndose bien dentro de OpenClaw”.
La pregunta correcta es:

**qué parte del valor real necesita de verdad PSA y qué parte debería vivir directamente en agentes OpenClaw con skills.**

Mi lectura es esta:

- hoy PSA está demasiado al centro,
- el bootstrap está demasiado pesado,
- la semántica está demasiado distribuida,
- y el sistema necesita volver a una relación sana entre complejidad y valor.

La salida no es empobrecer el sistema.
La salida es **reubicar la complejidad donde corresponde**.

Y ese lugar, en la mayoría de los casos, no es un meta-sistema central.
Es:

- el agente,
- sus skills,
- su memoria,
- y adapters opcionales bien contenidos.
