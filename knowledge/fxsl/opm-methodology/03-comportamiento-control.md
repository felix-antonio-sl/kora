---
_manifest:
  urn: "urn:fxsl:kb:opm-comportamiento-control"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-06"
    source: "opm_youtube.md + OPM version felix.md + ISO 19450"
version: "1.0.1"
status: published
tags: [opm, iso19450, eca, condiciones, operadores-logicos, rutas, invocacion, duracion, probabilidades, control]
lang: es
---

# OPM — Comportamiento Condicional, Control y Detalle Avanzado

Mecanismos de control de flujo, decisiones, temporalidad y probabilidades en modelos OPM.

---

## Paradigma ECA (Event-Condition-Action)

Semantica operacional de OPM. Todo proceso necesita dos prerequisitos para ejecutarse:
1. **Evento disparador:** objeto creado o que entra en estado especificado.
2. **Precondicion satisfecha:** preprocess object set disponible.

- Evento dispara evaluacion de precondicion. Si no satisfecha → proceso no ejecuta; evento se pierde.
- Evento ocurre una sola vez; si precondicion falla debe llegar nuevo evento.

---

## Preprocess y Postprocess Object Sets

**Preprocess Object Set:** objetos evaluados antes de iniciar proceso.
- Consumees en estado requerido.
- Affectees listos para transicion de estado de entrada.
- En ejecucion de instancia, cada consumee deja de existir al inicio del subproceso de menor nivel que lo consume.
- En ejecucion de instancia, cada affectee sale de su estado de entrada al inicio del subproceso de menor nivel que lo afecta.

**Postprocess Object Set:** objetos resultantes tras ejecutar proceso.
- Resultees creados.
- Affectees en estado de salida.
- En ejecucion de instancia, cada resultee empieza a existir al final del subproceso de menor nivel que lo crea.
- En ejecucion de instancia, cada affectee entra a su estado de salida al final del subproceso de menor nivel que lo afecta.

---

## Control Links (Modificadores de Control)

Enlace procedimental con letra de control:
- **`e` (event):** objeto o estado de objeto dispara (activa) el proceso.
- **`c` (condition):** objeto o estado es condicion; si no existe/cumple → proceso se salta (bypass).

Diferencia clave entre `c` (condition) y enlace habilitador sin modificador:
- `c`: si condicion no cumple → proceso saltado; ejecucion continua con siguiente.
- Sin `c` (instrument sin condicion): si instrumento no disponible → ejecucion se detiene hasta que instrumento exista.

---

## Event Links

**Consumption event link:** objeto activa y es consumido por proceso.
OPL: `Object triggers Process, which consumes Object.`

**Effect event link:** objeto activa y es afectado por proceso.
OPL: `Object triggers Process, which affects Object.`

**Agent event link:** agente activa y habilita proceso.
OPL: `Agent triggers and handles Process.`

**Instrument event link:** instrumento activa proceso (presencia o estado especificado).
OPL: `Instrument triggers Process, which requires Instrument.`

**State-specified event links:** originan desde estado especifico de objeto.
- Input-output-specified: `Input-state Object triggers Process, which changes Object from input-state to output-state.`
- Input-specified: `Input-state Object triggers Process, which changes Object from input-state.`
- Output-specified: `Object in any state triggers Process, which changes Object to destination-state.`
- State agent: `Qualifying-state Agent triggers and handles Processing.`
- State instrument: `Qualifying-state Instrument triggers Processing, which requires qualifying-state Instrument.`

---

## Condition Links (Bypass)

Enlace procedimental con `c` que permite saltar proceso si condicion no cumple.

| Tipo | OPL |
|------|-----|
| Condition consumption | Si objeto existe → proceso ejecuta y consume. Si no → proceso saltado. |
| Condition effect | Si objeto existe en estado entrada → proceso ejecuta. Si no → saltado. OPL: `Process occurs if Object is input-state, in which case Process changes Object from input-state to output-state, otherwise Process is skipped.` |
| Condition agent | `Agent handles Process if Agent exists, else Process is skipped.` |
| Condition instrument | `Process occurs if Instrument exists, else Process is skipped.` |
| Condition state-specified consumption | Si objeto existe en estado calificador → proceso ejecuta y consume. Si no → proceso saltado. |
| Condition input-output-specified effect | `Process occurs if Object is input-state, in which case Process changes Object from input-state to output-state, otherwise Process is skipped.` |
| Condition input-specified effect | `Process occurs if Object is input state, in which case Process changes Object from input-state, otherwise Process is skipped.` |
| Condition output-specified effect | `Process occurs if Object exists, in which case Process changes Object to output-state, otherwise Process is skipped.` |
| Condition state-specified agent | `Agent handles Process if Agent is qualifying-state, else Process is skipped.` |
| Condition state-specified instrument | Instrumento en estado calificador: mismo patron de bypass; si no cumple la condicion, el proceso se salta. |

---

## Nodos de Decision y Objetos Booleanos

**Nodo de decision:** objeto informatico que representa eleccion. Nombrar como pregunta (ej. "¿Funcion suficientemente detallada?").

**Objeto booleano:** nodo de decision con exactamente dos estados opuestos (ej. `Yes`/`No`). Cada estado dirige a curso de accion diferente via condition links.

---

## Operadores Logicos: AND, XOR, OR

Especifican condiciones compuestas de precondicion/postcondicion:

| Operador | Semantica | Representacion OPD | Cuando aplica |
|----------|-----------|-------------------|---------------|
| AND | Todos los enlaces deben cumplirse | Sin marca (default: enlaces separados no tocantes) | Todas las condiciones requeridas |
| XOR | Exactamente uno de los enlaces cumple | Arco discontinuo con punto focal en extremo convergente | Opciones mutuamente excluyentes |
| OR | Al menos uno de los enlaces cumple | Dos arcos concentricos discontinuos | Una o mas condiciones suficientes |

**XOR:** Si divergent-end tiene objetos → exactamente uno existe. Si tiene procesos → exactamente uno ocurre.
**OR:** Si divergent-end tiene objetos → al menos uno existe. Si tiene procesos → al menos uno ocurre.

---

## Rutas de Ejecucion (Execution Paths)

Serie de dos o mas enlaces procedurales consecutivos. Forma compacta de representar flujo sin OPD descendiente.

**Etiquetas de ruta (Path Labels):** etiqueta a lo largo de enlace procedimental. Si multiples enlaces salen de un proceso, etiqueta prescribe que seguir el enlace con misma etiqueta de entrada.

**Escenario:** una o mas etiquetas de ruta que determinan conjunto especifico de enlaces a seguir.

---

## Invocacion Proceso-a-Proceso

**Invocacion implicita:** al terminar subproceso en contexto in-zoom → invoca siguiente en orden vertical. Sin enlace grafico.

**Invocacion explicita:** enlace de invocacion (flecha proceso → proceso). Modela:
- Ciclos iterativos (proceso se reinvoca).
- Manejo de excepciones (proceso alternativo al fallar condicion).

Al reinvocar, subprocesos cuyas condiciones ya esten satisfechas pueden omitirse.

---

## Subprocesos Iterativos

Patron de modelado para procesos que se repiten hasta condicion:
1. Proceso principal con in-zoom.
2. Dentro: nodo de decision booleano + condition links.
3. Enlace de invocacion al proceso raiz si condicion indica continuar.
4. Respetar timeline (no ir contra orden vertical del in-zoom).

---

## Duracion de Proceso

| Especificacion | Posicion en OPD | Descripcion |
|----------------|-----------------|-------------|
| Duracion nominal | Dentro de elipse, bajo nombre del proceso + unidad | Duracion esperada/promedio |
| Duracion minima | A izquierda de nominal | Umbral inferior |
| Duracion maxima | A derecha de nominal | Umbral superior |

---

## Excepciones de Proceso

**Overtime exception link:** enlace procedimental de proceso-origen a proceso-destino.
Semantica: si duracion-maxima del proceso-origen es excedida → proceso-destino se activa.
OPL: si `Process` excede `max-duration` → `Exception-Process` se ejecuta.

Aplicacion: timeout de transacciones, alarmas por tiempo insuficiente.

---

## Instrument Event Link (Evento de Instrumento)

Instrumento con modificador `e`: si objeto existe o esta en estado especificado → proceso se activa.
OPD: paleta blanca + letra `e` junto al circulo.
Uso: interrupciones, deteccion de eventos ambientales (ej. proximidad de objeto a umbral especifico).

---

## Probabilidades de Enlace Procedimental

Probabilidad registrada a lo largo de enlace procedimental para el resultado indicado.
- Suma de probabilidades de todos los posibles resultados de un proceso = 1.
- Permite modelar escenarios con diferentes resultados probables (ej. duracion de viaje: corta/mediana/larga con probabilidad asignada a cada una).
- **Link fan probabilistico:** conjunto de enlaces con probabilidades desde un proceso; requiere que sumen 1.

---

## Estados Iniciales y Finales

**Estado inicial:** estado asumido por objeto al ser creado. OPD: contorno grueso.
**Valor inicial:** valor asumido por atributo al crearse su exhibidor.

**Estado final:** estado de objeto al fin de su ciclo de vida; no puede cambiar. OPD: doble contorno.
**Valor final:** valor de atributo al fin del ciclo de vida del exhibidor; no puede cambiar.

---

## Vistas (View Diagrams)

OPD que presenta coleccion de hechos del modelo de varios OPDs. No es parte del arbol OPD jerarquico.
Proposito: explicar fenomeno especifico o enfatizar punto del sistema.
Construccion: seleccionar cualquier elemento y agregar elementos conectados de manera util para comprension.
