# OPL Plantillas — Espanol

Fuente normativa: `urn:fxsl:kb:opm-opl-es`.
Convenciones: **Objeto** en negrita, *Proceso* en cursiva, `Estado` en monoespaciado.

---

## Propiedades Genericas (D)

| ID | OPL-ES |
|----|--------|
| D1 | **Cosa** es fisica. |
| D2 | **Cosa** es informatica. |
| D3 | **Cosa** es ambiental. |
| D4 | **Cosa** es sistemica. |
| D5 | **Objeto** puede estar `estado1`, `estado2` o `estado3`. |
| D7 | Estado `s` de **Objeto** es inicial. |
| D8 | Estado `s` de **Objeto** es final. |
| D9 | Estado `s` de **Objeto** es por defecto. |

---

## Links Transformadores — Basicos (T)

| ID | Tipo | OPL-ES |
|----|------|--------|
| T1 | Consumo | *Proceso* consume **Consumido**. |
| T2 | Resultado | *Proceso* genera **Resultado**. |
| T3 | Efecto | *Proceso* afecta **Afectado**. |

## Links Transformadores — State-Specified (TS)

| ID | Tipo | OPL-ES |
|----|------|--------|
| TS1 | Consumo s-s | *Proceso* consume **Objeto** en `estado`. |
| TS2 | Resultado s-s | *Proceso* genera **Objeto** en `estado`. |
| TS3 | Efecto entrada-salida | *Proceso* cambia **Objeto** de `estado-entrada` a `estado-salida`. |
| TS4 | Efecto solo entrada | *Proceso* cambia **Objeto** de `estado-entrada`. |
| TS5 | Efecto solo salida | *Proceso* cambia **Objeto** a `estado-salida`. |

---

## Links Habilitadores — Basicos (H)

| ID | Tipo | OPL-ES |
|----|------|--------|
| H1 | Agente | **Agente** maneja *Proceso*. |
| H2 | Instrumento | *Proceso* requiere **Instrumento**. |

## Links Habilitadores — State-Specified (HS)

| ID | Tipo | OPL-ES |
|----|------|--------|
| HS1 | Agente s-s | **Agente** en `estado` maneja *Proceso*. |
| HS2 | Instrumento s-s | *Proceso* requiere **Instrumento** en `estado`. |

---

## Links de Evento — Transformadores (ET)

| ID | Tipo | OPL-ES |
|----|------|--------|
| ET1 | Consumo evento | **Objeto** inicia *Proceso*, que consume **Objeto**. |
| ET2 | Efecto evento | **Objeto** inicia *Proceso*, que afecta **Objeto**. |
| ETS1 | Consumo evento s-s | **Objeto** en `estado` inicia *Proceso*, que consume **Objeto**. |
| ETS2 | Efecto evento s-s | **Objeto** en `estado-entrada` inicia *Proceso*, que cambia **Objeto** de `estado-entrada` a `estado-salida`. |
| ETS3 | Efecto evento entrada | **Objeto** en `estado-entrada` inicia *Proceso*, que cambia **Objeto** de `estado-entrada`. |
| ETS4 | Efecto evento salida | **Objeto** en cualquier estado inicia *Proceso*, que cambia **Objeto** a `estado-destino`. |

## Links de Evento — Habilitadores (EH)

| ID | Tipo | OPL-ES |
|----|------|--------|
| EH1 | Agente evento | **Agente** inicia y maneja *Proceso*. |
| EH2 | Instrumento evento | **Instrumento** inicia *Proceso*, que requiere **Instrumento**. |
| EHS1 | Agente evento s-s | **Agente** en `estado` inicia y maneja *Proceso*. |
| EHS2 | Instrumento evento s-s | **Instrumento** en `estado` inicia *Proceso*, que requiere **Instrumento** en `estado`. |

---

## Links de Condicion — Transformadores (CT)

| ID | OPL-ES |
|----|--------|
| CT1 | *Proceso* ocurre si **Objeto** existe, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite. |
| CT2 | *Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* afecta **Objeto**, de lo contrario *Proceso* se omite. |
| CS1 | *Proceso* ocurre si **Objeto** esta en `estado`, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite. |
| CS2 | *Proceso* ocurre si **Objeto** esta en `estado-entrada`, en cuyo caso *Proceso* cambia **Objeto** de `estado-entrada` a `estado-salida`, de lo contrario *Proceso* se omite. |
| CS3 | *Proceso* ocurre si **Objeto** esta en `estado-entrada`, en cuyo caso *Proceso* cambia **Objeto** de `estado-entrada`, de lo contrario *Proceso* se omite. |
| CS4 | *Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* cambia **Objeto** a `estado-salida`, de lo contrario *Proceso* se omite. |

## Links de Condicion — Habilitadores (CH)

| ID | OPL-ES |
|----|--------|
| CH1 | **Agente** maneja *Proceso* si **Agente** existe, de lo contrario *Proceso* se omite. |
| CH2 | *Proceso* ocurre si **Instrumento** existe, de lo contrario *Proceso* se omite. |
| CS5 | **Agente** maneja *Proceso* si **Agente** esta en `estado`, de lo contrario *Proceso* se omite. |
| CS6 | *Proceso* ocurre si **Instrumento** esta en `estado`, de lo contrario *Proceso* se omite. |

---

## Excepcion e Invocacion (EX/INV)

| ID | Tipo | OPL-ES |
|----|------|--------|
| EX1 | Overtime | *Manejo* ocurre si duracion de *Fuente* excede max-duracion unidades-tiempo. |
| EX2 | Undertime | *Manejo* ocurre si duracion de *Fuente* es menor que min-duracion unidades-tiempo. |
| INV1 | Invocacion simple | *Proceso1* invoca *Proceso2*. |
| INV2 | Auto-invocacion | *Proceso* se auto-invoca. |

---

## Relaciones Estructurales Fundamentales (S)

| ID | Tipo | OPL-ES |
|----|------|--------|
| S1 | Aggregation | **Todo** consta de **Parte1**, **Parte2** y **Parte3**. |
| S2 | Aggregation parcial | **Todo** consta de **Parte1** y **Parte2**, entre otras. |
| S3 | Exhibition | **Exhibidor** exhibe **Feature**. |
| S4 | Generalization | **General** se especializa en **Especializacion1** y **Especializacion2**. |
| S5 | Generalization (sg) | **Especializacion** es un/una **General**. |
| S6 | Classification | **Clase** se instancia como **Instancia1** e **Instancia2**. |
| S7 | Classification (sg) | **Instancia** es una instancia de **Clase**. |
| S8 | Tagged unidireccional | **Origen** se relaciona con **Destino** via [etiqueta]. |

---

## Operadores Logicos

| Operador | Grafico | OPL patron |
|----------|---------|------------|
| AND | Links separados sin arco | (sin keyword — multiples sentencias independientes) |
| XOR | Arco discontinuo simple | exactamente uno de: *P1*, *P2*, *P3* |
| OR | Dos arcos discontinuos concentricos | al menos uno de: *P1*, *P2*, *P3* |
| Probabilistico | Anotacion `Pr=p` en cada link | *P1* con probabilidad p1; *P2* con probabilidad p2. |

---

## Refinamiento — Descomposicion y Despliegue

| ID | Tipo | OPL-ES |
|----|------|--------|
| R1 | In-zooming proceso | *Proceso* se descompone en *Sub1*, *Sub2* y *Sub3* en esa secuencia. |
| R2 | In-zooming paralelo | *Sub1* y *Sub2* ocurren en paralelo. |
| R3 | Unfolding proceso | *Proceso* se despliega en *Sub1* y *Sub2*. |
| R4 | Object in-zooming | **Objeto** se descompone en **Parte1** y **Parte2**. |

---

## Vocabulario de Verbos OPL-ES

| Funcion | EN | ES (3a sg presente) |
|---------|----|--------------------|
| Consumo | consumes | consume |
| Resultado | yields | genera |
| Efecto | affects | afecta |
| Cambio de estado | changes … from … to | cambia … de … a |
| Agente | handles | maneja |
| Instrumento | requires | requiere |
| Iniciacion | initiates | inicia |
| Invocacion | invokes | invoca |
| Existencia | exists | existe |
| Omision (pasiva) | is skipped | se omite |
| Consumo (pasiva) | is consumed | se consume |
| Agregacion | consists of | consta de |
| Exhibicion | exhibits | exhibe |
| Especializacion (pl) | are | son |
| Especializacion (sg) | is a | es un/una |
| Instanciacion | is an instance of | es una instancia de |
| Declaracion de estados | can be | puede estar |
| Descomposicion | zooms into … in that sequence | se descompone en … en esa secuencia |
| Despliegue | unfolds into | se despliega en |
