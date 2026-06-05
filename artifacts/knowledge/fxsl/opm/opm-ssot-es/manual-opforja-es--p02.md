---
_manifest:
  urn: urn:fxsl:kb:manual-opforja-es-p02
  provenance:
    created_by: deep-opm-pro/codex + custodio KORA
    created_at: '2026-06-04'
    source: >-
      Manual operativo derivado del corpus OPM/Forja SSOT ES vigente. Parte
      desde reglas-opm-estrictas-es v1.2.1, metodologia-forja-es v1.5.0, spec-forja-opd-es
      v1.0.3, spec-forja-opl-es v1.1.3, opm-categorial-es v1.2.4 y modelamiento-opm
      v1.5.0. Iniciado en REVIEW y promovido a productivo como manual v0.1.0;
      v0.2.0 expande de forma autónoma el núcleo estable que no depende de cambios
      de UI: modelo mental, flujo, construcción, refinamiento, OPD/OPL, validación
      y apéndices operativos.
version: 0.2.1
status: publicado
source_base: reglas-opm-estrictas-es.md v1.2.1; metodologia-forja-es.md v1.5.0; spec-forja-opd-es.md
  v1.0.3; spec-forja-opl-es.md v1.1.3; opm-categorial-es.md v1.2.4; modelamiento-opm
  v1.5.0.
derived_from:
- urn:fxsl:kb:reglas-opm-estrictas-es
- urn:fxsl:kb:metodologia-forja-opm-es
- urn:fxsl:kb:spec-forja-opd-es
- urn:fxsl:kb:spec-forja-opl-es
- urn:fxsl:kb:opm-categorial-es
scope: Manual operativo de uso de opforja para modeladores, agentes y mantenedores.
  Enseña flujo, criterio, lectura de OPD/OPL, validación y uso práctico sin duplicar
  el canon prescriptivo ni las specs modales. Las secciones dependientes de interfaz
  se marcan como vivas o pendientes de evidencia hasta estabilizar la app.
tags:
- opm
- opforja
- manual
- guia-operativa
- modelamiento
- opd
- opl
- deep-opm-pro
- ssot-forja
lang: es
extensions:
  kora:
    family: note
    lifecycle_note: publicado v0.2.1; mantener secciones dependientes de interfaz como vivo o pendiente de evidencia hasta sincronización con la app.
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:manual-opforja-es
relations:
  depends:
  - urn:fxsl:kb:reglas-opm-estrictas-es
  - urn:fxsl:kb:metodologia-forja-opm-es
  - urn:fxsl:kb:spec-forja-opd-es
  - urn:fxsl:kb:spec-forja-opl-es
  cites:
  - urn:fxsl:kb:opm-categorial-es
  - urn:fxsl:kb:opm-es
  - urn:fxsl:kb:opd-es
  - urn:fxsl:kb:opl-es
  - urn:fxsl:kb:manual-metodologico-opm-es
---

# Manual de opforja - Parte 02

## 5. Refinar sin romper el modelo

**Estado:** estable.

Refinar es hacer visible una estructura interna que ya estaba implicada por el
modelo, no cambiar la función sin decirlo. Cada refinamiento debe declarar:

- qué cosa o proceso se refina,
- qué pregunta responde,
- qué frontera conserva,
- qué enlaces se distribuyen,
- qué hechos se expresan o se suprimen,
- qué OPL confirma la equivalencia.

El refinamiento tiene dos riesgos opuestos: dejar el modelo demasiado grueso
para servir, o abrir detalle que cambia la función sin admitirlo. La disciplina
Forja exige que cada descenso tenga motivo y que cada ascenso conserve frontera.

### 5.1 In-zoom y frontera

Al descomponer un proceso, los subprocesos deben explicar cómo se realiza el
proceso padre. La firma de frontera del proceso abstracto se preserva. Si el
hijo necesita un nuevo input o produce un nuevo output neto, revisar si el padre
estaba incompleto o si se está modelando otra función.

Checklist de in-zoom:

1. El proceso padre está nombrado como transformación.
2. El OPD hijo agrega al menos dos subprocesos o una estructura interna no
   trivial.
3. Cada subproceso tiene transformee o rol claro.
4. Los enlaces del padre se distribuyen sin cambiar la firma neta.
5. El orden vertical representa secuencia cuando corresponde.
6. El OPL del hijo puede leerse como realización del padre.
7. Si aparece una nueva entidad de frontera, se declara como corrección del
   padre o se rechaza el refinamiento.

Ejemplo:

```text
Padre: *Pedido despachando*
Frontera: consume **Pedido confirmado**, requiere **Operador**, requiere **Sistema de bodega**, genera **Pedido despachado**.
Hijo: *Pedido preparando* -> *Paquete entregando* -> *Despacho registrando*.
```

Si el hijo agrega **Pago autorizado** como nuevo input neto, no es un detalle
interno inocente: el padre omitía una frontera o el proceso realmente es otro.

### 5.2 Unfold y estructura

Al desplegar una cosa, las partes, rasgos, especializaciones o instancias deben
usar el enlace estructural correcto. No todo detalle interno es parte; algunos
son atributos exhibidos, tipos especializados o instancias clasificadas.

Guía rápida:

| Pregunta | Relación |
| --- | --- |
| ¿El todo necesita estas partes? | Agregación-participación. |
| ¿La cosa porta este rasgo o atributo? | Exhibición-caracterización. |
| ¿Esto es un tipo más específico? | Generalización-especialización. |
| ¿Esto es una ocurrencia concreta de una clase? | Clasificación-instanciación. |

No usar agregación como cajón universal. "Prioridad" de un pedido no es parte
del pedido; es atributo exhibido. "Pedido urgente" no es parte de pedido; es
especialización o estado/atributo, según el dominio.

### 5.3 Estados expresados y suprimidos

La supresión de estados es una decisión de vista, no una eliminación del modelo.
Debe mantenerse claro qué estados existen canónicamente y cuáles están ocultos
en una aparición para controlar altitud.

Reglas prácticas:

- expresar estados cuando son necesarios para entender transformación,
- suprimir estados cuando congestionan una vista superior,
- no suprimir un estado que participa en un enlace visible,
- no inventar estados para compensar nombres pobres,
- si un estado parece atributo independiente, considerar exhibición-caracterización.

### 5.4 Realizaciones hermanas

Dos realizaciones hermanas son alternativas internas comparables para cumplir la
misma función. Pueden diferir en pasos, instrumentos, costo o riesgo, pero deben
preservar la firma de frontera si se declaran funcionalmente equivalentes.

Uso práctico:

1. Definir el proceso abstracto.
2. Declarar su frontera.
3. Construir realización A.
4. Construir realización B.
5. Comparar roles netos de frontera.
6. Si coinciden, comparar atributos no funcionales.
7. Si no coinciden, no son la misma función: ajustar frontera o separar funciones.

### 5.5 Cuándo no refinar

No refinar cuando:

- el SD aún tiene barro,
- el refinamiento solo repite el padre,
- el detalle responde curiosidad pero no propósito,
- la vista padre ya sirve al lector y al objetivo,
- el supuesto de dominio no está confirmado,
- el refinamiento requiere una capacidad de UI no estabilizada y puede
  documentarse como brecha.

## 6. Reglas prácticas de OPD

**Estado:** estable como criterio; vivo en detalles visuales.

El OPD comunica con geometría. Los detalles exactos de glifos, marcadores y
tokens visuales viven en `spec-forja-opd-es`; este manual conserva solo la
lectura práctica.

| Elemento | Lectura práctica |
| --- | --- |
| Rectángulo | Objeto. Existe y puede portar estados. |
| Elipse | Proceso. Transforma y puede refinarse por in-zoom. |
| Rountangle interno | Estado de un objeto. |
| Sombra | Esencia física cuando está visible. |
| Contorno discontinuo | Afiliación ambiental. |
| Enlace transformador | El proceso consume, produce o cambia algo. |
| Piruleta | Habilitación: agente o instrumento. |
| Triángulo estructural | Agregación, exhibición, generalización o clasificación según glifo. |
| Rayo | Invocación entre procesos. |
| `e` / `c` | Evento o condición sobre enlace permitido. |

Regla de lectura: si un elemento visual no puedes traducirlo a una oración OPL
clara, no lo trates como hecho terminado.

### 6.1 Lectura de enlaces procedimentales

| Pregunta | Enlace probable | Error frecuente |
| --- | --- | --- |
| ¿El proceso consume la cosa? | Consumo. | Dibujar como instrumento porque "se usa". |
| ¿El proceso produce la cosa? | Resultado. | Modelar el producto como estado del proceso. |
| ¿El proceso cambia estado de la cosa? | Efecto. | Crear objeto nuevo cuando el objeto persiste. |
| ¿Una persona u organización maneja el proceso? | Agente. | Tratar software como agente. |
| ¿Una herramienta habilita el proceso? | Instrumento. | Ignorar desgaste relevante. |
| ¿Un proceso llama a otro? | Invocación. | Usar condición/evento sobre invocación. |

### 6.2 Lectura de enlaces estructurales

Las relaciones estructurales no expresan flujo temporal. Expresan cómo una cosa
se organiza, caracteriza, especializa o instancia. No deben usarse para decir
"después de" ni "requiere".

| Relación | Pregunta de prueba |
| --- | --- |
| Agregación | ¿sin esta parte el todo pierde composición? |
| Exhibición | ¿esto es rasgo, atributo o propiedad de la cosa? |
| Generalización | ¿cada especialización sigue siendo el general? |
| Clasificación | ¿esto es una instancia concreta de la clase? |
| Etiquetado | ¿la relación no cabe en las cuatro fundamentales y está justificada? |

### 6.3 Densidad visual

Un OPD legible tiene foco. Si el lector necesita memorizar veinte cosas antes de
entender el proceso, la vista no está en buena altitud.

Acciones posibles:

- in-zoom del proceso central,
- unfold parcial de una cosa,
- supresión de estados no usados,
- separar una vista explicativa de un OPD canónico,
- registrar brecha en vez de forzar detalle.

### 6.4 UI transitoria vs canon

No todo lo visible en pantalla es modelo. Handles, selección, grillas, overlays
de validación, ayudas, halos runtime y mensajes de error son UI o vistas salvo
que un perfil canónico los declare como persistentes. El manual nunca debe usar
un affordance de edición como regla OPM.

## 7. Reglas prácticas de OPL

**Estado:** estable como criterio; vivo en parser/edición.

OPL-ES es lenguaje natural controlado. Su valor está en ser legible por humanos
y suficientemente formal para roundtrip.

Principios prácticos:

- una oración atómica expresa un hecho,
- los nombres canónicos deben ser singulares y específicos,
- esencia y afiliación son declaraciones de cosa,
- consumo, resultado y efecto no son sinónimos,
- agente e instrumento usan predicados distintos,
- la prosa compuesta solo coordina hechos elegibles,
- una oración no parseable puede servir como comentario humano, pero no como
 hecho canónico importable.

El parser no es corrector literario. Si el operador escribe una frase ambigua,
opforja debe rechazarla, suspenderla o pedir aclaración según la política de la
spec OPL; no debe inventar el hecho.

### 7.1 Pruebas rápidas de una oración OPL

Una oración OPL práctica debe pasar estas preguntas:

1. ¿Tiene sujeto OPM claro?
2. ¿El verbo pertenece al vocabulario esperado?
3. ¿Expresa un solo hecho o una composición elegible?
4. ¿Los nombres son canónicos y consistentes?
5. ¿Puede mapearse de vuelta a entidad/enlace/estado?
6. ¿El operador confirma que dice lo que quería decir?

### 7.2 Nombres canónicos

Los nombres canónicos deben evitar:

- plurales innecesarios,
- comodines como "sistema", "módulo", "gestión",
- verbos vagos como "procesar" o "manejar",
- nombres de implementación cuando la función aún es neutral,
- siglas no explicadas,
- mezcla de infinitivo y nominalización en procesos del mismo modelo.

### 7.3 Prosa atómica y prosa compuesta

La prosa atómica es preferida para validar y depurar. La prosa compuesta sirve
para lectura humana cuando la composición no oculta hechos ni mezcla familias
incompatibles.

Regla práctica: si una frase compuesta dificulta señalar qué cosa, enlace o
estado se está editando, volver a atómica.

### 7.4 Qué hacer con OPL no parseable

Una oración no parseable puede conservarse como nota humana si está claramente
separada del modelo canónico. No debe importarse como hecho ni forzar al parser
a inventar entidades.

Opciones correctas:

- reescribir a plantilla canónica,
- partir en oraciones atómicas,
- pedir aclaración,
- registrar como comentario o brecha,
- declarar que la app aún no soporta una oración canónica específica.

## 8. Validación y diagnóstico

**Estado:** estable.

Validar en opforja combina reglas, método y lectura humana:

1. Correr validación de hechos y severidades.
2. Revisar checklist OPD<->OPL.
3. Leer el OPL completo con el operador.
4. Revisar frontera y firma de procesos refinados.
5. Revisar densidad y legibilidad de cada OPD.
6. Separar errores de modelo, advertencias, deuda de herramienta y brechas de
 canon.
7. Declarar si el modelo está bien formado, representa y sirve.

### 8.1 Diagnóstico honesto

Un diagnóstico debe decir qué se rompe y en qué plano:

- **Validez:** regla estricta violada.
- **Modalidad OPD:** realización visual incorrecta.
- **Modalidad OPL:** oración, parseo o roundtrip incorrecto.
- **Método:** modelo conforme pero mal construido o insuficiente.
- **Herramienta:** capacidad no implementada, UI transitoria o GAP.
- **Dominio:** falta evidencia del operador.

### 8.2 Matriz de severidad práctica

| Situación | Conducta |
| --- | --- |
| Viola regla estricta de validez | Bloquear o corregir antes de seguir. |
| Rompe OPD<->OPL | No publicar el hecho; reparar modalidad o roundtrip. |
| Es conforme pero confuso | Marcar como problema metodológico y simplificar. |
| Depende de UI no estable | Marcar como vivo o brecha de herramienta. |
| Falta verdad de dominio | Devolver al operador; no inventar. |
| Es mejora de legibilidad | Recomendar, no bloquear salvo export canónico. |

### 8.3 Checklist de cierre

Antes de cerrar una entrega, revisar:

- cada OPD tiene foco,
- cada hecho visible tiene OPL,
- cada OPL canónico apunta a hecho,
- no hay estados flotantes,
- cada entidad con estados está clasificada como flujo, caracterización o
 ambiental-observado,
- no hay nombres duplicados ambiguos,
- no hay agentes no humanos salvo decisión explícita,
- los refinamientos preservan frontera,
- los supuestos están separados de hechos,
- las brechas de app no se presentan como canon,
- se declara el nivel validado: bien formado, representa o sirve.

## 9. Patrones de modelado

**Estado:** estable para la estructura; pendiente de evidencia para catálogo completo.

Esta sección reunirá patrones probados que ya existen como lecciones Forja o
como apéndices OPL. En v0.2 se conserva el índice de patrones candidatos y se
desarrollan las primeras fichas estables:

- sistemas sociotécnicos,
- agente, rol y autoridad,
- decisión y supervisión humana,
- interfaz crítica,
- control loop,
- estados ortogonales,
- composición por interfaz,
- configuración y tradeoffs,
- digital twin y simulación conceptual.

Cada patrón publicable debe incluir: intención, cuándo usarlo, cuándo no usarlo,
OPD mínimo, OPL esperado, reglas propietarias, brechas conocidas y ejemplo.

### 9.1 Molde de patrón

```text
Nombre:
Intención:
Cuándo usar:
Cuándo no usar:
OPD mínimo:
OPL esperado:
Reglas propietarias:
Brechas / riesgos:
Ejemplo:
```

### 9.2 Patrón: interfaz crítica

**Intención:** hacer visible una interfaz que explica comportamiento,
responsabilidad o falla.

Usar cuando una frontera entre sistemas, roles o subsistemas decide el valor del
modelo. No usar cuando la interfaz es mero detalle técnico que no cambia la
función ni la validación.

OPD mínimo: dos procesos o sistemas conectados mediante objeto frontera o
intermedio explícito. El objeto frontera debe tener identidad y rol, no ser una
línea anónima.

OPL esperado: la interfaz aparece como objeto, instrumento, transformee o
referencia estructural según su rol. Si solo existe como nota, no es todavía un
hecho OPM.

### 9.3 Patrón: decisión con supervisión humana

**Intención:** modelar una decisión sin esconder responsabilidad.

Usar cuando un proceso selecciona ruta, aprueba, rechaza o deriva y existe una
persona/organización responsable. No reemplaza el agente por IA o software: la
herramienta puede ser instrumento, la responsabilidad humana sigue siendo agente
si el dominio la declara.

OPD mínimo: proceso de decisión, agente humano/organizacional, información de
entrada, resultado/estado de decisión y rutas condicionadas.

### 9.4 Patrón: control loop

**Intención:** representar sensar, decidir y actuar cuando la adaptabilidad es
parte del sistema.

Usar cuando feedback, condición o medición cambia el flujo. No usar para
decorar cualquier monitoreo. Si el sensor solo entrega datos y no altera el
comportamiento, modelar dato/instrumento sin loop.

OPD mínimo: proceso de sensado, objeto informacional medido, proceso de decisión
y proceso actuador o invocado.

## 10. Ejemplo end-to-end

**Estado:** estable como ejemplo textual; pendiente de evidencia UI.

El ejemplo principal debe ser pequeño, completo y verificable. Para v0.2 se usa
un dominio deliberadamente simple: despacho de pedido. Sirve para enseñar
opforja, no logística.

### 10.1 Enunciado inicial

> "Quiero modelar el sistema de despacho de pedidos."

Barro detectado: "sistema de despacho" nombra un área, pero aún no declara qué
cambia, quién recibe valor ni cuál es la frontera.

Pregunta: ¿qué objeto entra distinto y sale distinto por el despacho?

Respuesta aceptada para el ejemplo: un **Pedido confirmado** se transforma en
**Pedido despachado**; el cliente recibe valor por disponibilidad de entrega.

### 10.2 SD inicial

```text
Sistema: Sistema de despacho
Tipo: sociotécnico
Propósito: despachar pedidos confirmados
Proceso central: Pedido despachando
Beneficiario: Cliente
Atributo de valor: estado de cumplimiento del pedido
Estado inicial: confirmado
Estado buscado: despachado
Transformee principal: Pedido
Agente: Operador de bodega
Instrumento: Sistema de bodega
Ambiental relevante: Cliente
Supuestos: el pago ya fue confirmado fuera del modelo
Brechas: reglas de excepción por quiebre de stock no refinadas en SD
```

### 10.3 Primer OPL esperado

```text
**Sistema de despacho** exhibe *Pedido despachando*.
*Pedido despachando* afecta **Pedido** de `confirmado` a `despachado`.
*Pedido despachando* requiere **Sistema de bodega**.
**Operador de bodega** maneja *Pedido despachando*.
**Cliente** es ambiental.
```

Este OPL es didáctico: la forma exacta debe ajustarse a las plantillas vigentes
de `spec-forja-opl-es`. Lo importante para el manual es que cada oración tenga
un hecho rastreable.

### 10.4 Primer refinamiento

Pregunta de refinamiento: ¿cómo se realiza *Pedido despachando* sin cambiar su
frontera?

```text
*Pedido preparando*
*Paquete entregando*
*Despacho registrando*
```

La frontera se conserva si el conjunto de subprocesos sigue consumiendo/cambiando
el **Pedido confirmado**, requiriendo los mismos enablers netos y generando el
**Pedido despachado**. Si aparece **Pago autorizado** como nuevo input, se
declara que estaba fuera del alcance o se corrige la frontera del padre.

### 10.5 Validación tripartita del ejemplo

| Nivel | Pregunta | Resultado esperado |
| --- | --- | --- |
| Bien formado | ¿cada cosa/enlace/estado cumple reglas? | Sin agentes no humanos, sin estados flotantes, sin enlace ambiguo. |
| Representa | ¿el operador confirma el flujo? | Confirmar que pago queda fuera y bodega ejecuta despacho. |
| Sirve | ¿responde al propósito didáctico? | Sí: enseña SD, OPL y primer in-zoom. |

### 10.6 Errores intencionales

| Error | Por qué falla | Corrección |
| --- | --- | --- |
| Modelar **Sistema de bodega** como agente. | El software no es agente humano. | Usarlo como instrumento. |
| Crear *Gestionar despacho* sin transformee. | Proceso sin objeto que cambia. | Nombrar *Pedido despachando* y conectar **Pedido**. |
| Agregar **Pago autorizado** en el hijo sin padre. | Rompe firma de frontera. | Declararlo fuera de alcance o corregir SD. |
| Dibujar **Cliente** dentro del sistema por cercanía visual. | Afiliación no depende de layout. | Marcarlo ambiental si no está bajo control del sistema. |

El ejemplo no debe depender de conocimiento experto de dominio. Su función es
enseñar opforja, no enseñar medicina, logística o software.

## 11. Apéndices

**Estado:** estable como apéndices iniciales; vivo para detectores dependientes de app.

### Apéndice A — Glosario opforja

| Término | Definición operativa |
| --- | --- |
| Barro | Ambigüedad que impide plasmar un hecho sin inventar dominio o violar canon. |
| Firma de frontera | Conjunto de roles netos de entrada, salida y habilitación que un proceso presenta al exterior. |
| Realización hermana | Alternativa interna comparable que realiza la misma función abstracta si preserva firma de frontera. |
| Aparición | Presencia visual local de una cosa en un OPD; no equivale a nueva identidad. |
| Display-vs-canónico | Diferencia entre forma visible local y hecho persistente del modelo. |
| Bundle | Paquete serializado que permite rehidratar/auditar el modelo más allá de una imagen. |
| Roundtrip | Capacidad de ir de OPD a OPL y volver al mismo hecho sin pérdida relevante. |
| Gate | Chequeo, regla o revisión que decide si se puede avanzar. |
| GAP | Brecha explícita de canon, implementación o evidencia; no debe ocultarse como comportamiento normal. |

### Apéndice B — Cheatsheet OPD

| Veo | Leo |
| --- | --- |
| Rectángulo | Objeto. |
| Elipse | Proceso. |
| Estado dentro de objeto | Situación posible del objeto. |
| Sombra | Físico si la spec visual lo marca así. |
| Discontinuo | Ambiental cuando aplica a afiliación. |
| Swallowtail | Transformación. |
| Piruleta | Habilitación. |
| Triángulo | Relación estructural. |
| Rayo | Invocación. |
| Badge `e`/`c` | Evento o condición sobre enlace permitido. |

Fuente completa: `spec-forja-opd-es`.

### Apéndice C — Cheatsheet OPL

Patrones de lectura frecuente:

```text
**Objeto** puede estar `estado1` o `estado2`.
*Proceso* afecta **Objeto** de `estado1` a `estado2`.
*Proceso* requiere **Instrumento**.
**Agente** maneja *Proceso*.
**Todo** consta de **Parte**.
**Exhibidor** exhibe **Atributo**.
**Especialización** es **General**.
**Instancia** es instancia de **Clase**.
```

Fuente completa y obligatoria para generación/parser: `spec-forja-opl-es`.

### Apéndice D — Mapa de reglas a specs canónicas

| Si el problema es... | Ir a |
| --- | --- |
| ¿Este hecho es válido? | `reglas-opm-estrictas-es` |
| ¿Qué severidad tiene? | `reglas-opm-estrictas-es` |
| ¿Cómo debería modelarlo? | `metodologia-forja-es` |
| ¿Cómo se dibuja? | `spec-forja-opd-es` |
| ¿Cómo se dice/parsea en OPL? | `spec-forja-opl-es` |
| ¿Qué ley explica equivalencia/composición? | `opm-categorial-es` |
| ¿Cómo se enseña al operador? | `manual-opforja-es` |
| ¿La app no lo soporta? | Registrar GAP o deuda de herramienta. |

### Apéndice E — Índice de detectores/checkers

Ranura viva. Detectores mencionables cuando estén expuestos de forma estable:

- preservación de firma de frontera,
- estados flotantes,
- nombre duplicado ambiguo,
- enlace con firma inválida,
- agente no humano,
- modificador de control en familia prohibida,
- ruptura OPD<->OPL,
- referencias colgantes,
- densidad/export canónico.

## Bitácora del manual

| Fecha | Versión | Cambio |
| --- | --- | --- |
| 2026-06-05 | 0.2.1 | Alineación con metodologia-forja-es v1.5.0: incorpora LF-19 como disciplina operativa para validar estados y fija barridos de integridad sobre JSON canónico. |
| 2026-06-05 | 0.2.0 | Expansión autónoma de contenido estable: walkthrough SD, refinamiento, OPD/OPL práctico, diagnóstico, patrones iniciales, ejemplo textual end-to-end y apéndices operativos. |
| 2026-06-04 | 0.1.0 | Creación, promoción a productivo y particionado en dos shards. Fija contrato editorial, TOC, capítulos estables iniciales, secciones vivas y ranuras para evidencia UI/casos. |
