---
_manifest:
  urn: urn:fxsl:kb:opm-es-p04
version: 2.0.0
status: published
tags:
- opm
- fundamentos
- ingenieria-de-sistemas
- modelado-conceptual
- representacion-bimodal
- mbse
- opl-es
lang: es
extensions:
  kora:
    family: specification
    consolidado: true
    shard_index: 4
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opm-es
relations:
  cites:
  - urn:fxsl:kb:manual-metodologico-opm-es
  - urn:fxsl:kb:opd-es
  - urn:fxsl:kb:opl-es
---


# OPM — Núcleo conceptual - Parte 04

## Modelo de enlace

Un enlace consta de:

- origen;
- destino;
- conector;
- línea;
- símbolo;
- etiqueta opcional;
- nombre de ruta opcional.

La multiplicidad tiene límites inferior y superior: `0..1`, `0..*`, `1..1`, `1..*`.

## Modelo de cosa

Una cosa es:

- **objeto**, o
- **proceso**.

Los objetos pueden ser sin estados o con estados. Los objetos con estados generan referencias a estados específicos.

**Objeto Específico de Estado (State-Specific Object).** Un objeto con estados que tiene `s` estados genera un conjunto de `s` **objetos específicos de estado**, cada uno de los cuales es una especialización sin estados del objeto original que "refiere a" un estado concreto. El concepto permite simplificar el modelo conceptual: cuando se necesita referenciar un objeto en un estado particular, se puede tratar como un objeto independiente sin estados. Por ejemplo, un **Producto** con estados `diseñado`, `fabricado`, `probado`, `comprado` y `usado` genera cinco especializaciones: **Producto Diseñado**, **Producto Fabricado**, etc. Cada una refiere al estado correspondiente de **Producto** mediante un enlace estructural etiquetado `refiere al estado de`.

- Un objeto sin estados tiene un conjunto de estados de cardinalidad `s=0`.
- Un objeto con estados tiene cardinalidad `s≥1`.
- El estado actual es una instancia de **Estado** dentro del **Conjunto de Estados** del objeto.
- Los estados se especializan en **Estado Inicial**, **Estado Final** y **Estado por Defecto**, cada uno con su designación y símbolo gráfico propio (rectángulo redondeado de borde grueso, doble borde, y señalador con flecha diagonal, respectivamente).

## Modelo de constructo estructural

Un constructo estructural básico = refinable + refinador + enlace estructural. Cinco variantes:

- agregación-participación;
- exhibición-caracterización;
- generalización-especialización;
- clasificación-instanciación;
- enlace estructural etiquetado.

## Modelo de constructo procedimental

Un constructo procedimental básico = objeto + proceso + enlace procedimental.

Las semánticas básicas son:

- transformación;
- habilitación;
- transformación con control;
- habilitación con control.

Los constructos transformadores se descomponen en:

- consumo;
- efecto;
- resultado.

Los habilitadores se descomponen en:

- agente;
- instrumento.

## Modelos de descomposición y recomposición en nuevo diagrama

Esta adaptación modela la descomposición y la recomposición en nuevo diagrama como procesos OPM de primera clase:

- **Descomposición en nuevo diagrama**: requiere `SDn`, realiza Mostrar Contenido y luego Refinar Enlaces, y genera `SDn+1`.
- **Recomposición en nuevo diagrama**: requiere `SDn+1`, realiza Abstraer Enlaces y luego Ocultar Contenido, y genera `SDn`.
- **OPD semidescompuesto**: objeto transitorio que existe solo dentro de esas transformaciones.

Las figuras de referencia muestran la migración de enlaces desde un proceso refinado `P` hacia subprocesos `P1`, `P2`, `P3`, reubicando consumidos, agentes, instrumentos y resultantes en el nivel detallado.

## Simplificación de un OPD

Un OPD sobrecargado puede simplificarse abstrayendo un conjunto acotado de procesos y objetos hacia un constructo de nivel superior, siempre que la abstracción no cree enlaces procedimentales ilegales entre procesos pares.

## Modelo de control del desempeño de procesos

Este modelo autorreferencial completo demuestra cómo OPM controla la ejecución de procesos en tiempo de simulación.

Jerarquía principal:

- `SD`
- `SD1`
- `SD1.1`
- `SD1.1.1`
- `SD1.1.1.1`
- `SD1.2`
- `SD1.2.1`
- `SD1.2.2`
- `SD1.2.3`

**SD: Control del Desempeño de Procesos**
Un *Proceso Ejecutable* invoca *Controlar Desempeño de Proceso*, que afecta el **Conjunto de Objetos Involucrados** y genera un **Mensaje de Éxito** o un **Mensaje de Falla**.

**SD1: Descomposición principal**
*Controlar Desempeño de Proceso* se descompone en *Iniciar Proceso* y *Ejecutar Proceso*, en esa secuencia. **Estado del Proceso** recorre `inactivo → iniciado(t=0) → operando(t<n) → completando(t=n) → completado(t=n)` o `abortado`. **Poscondición** pasa de `falsa` a `verdadera`.

**SD1.1: Iniciar Proceso**
Se descompone en *Evaluar Precondición* → (`Cancelar` | `Iniciar`). Si la precondición es falsa, *Cancelar* genera **Mensaje de Cancelación** y devuelve el estado a `inactivo`. Si es verdadera, *Iniciar* consume la precondición, genera poscondición falsa y cambia el estado del proceso a `iniciado(t=0)`.

**SD1.1.1: Evaluar Precondición**
Se descompone en *Verificar Habilitadores* → *Verificar Consumidos y Afectados* → (`Refutar Precondición` | `Confirmar Precondición`). Si alguna verificación falla, se refuta la precondición; si todas pasan, se confirma.

**SD1.2: Ejecutar Proceso**
Se descompone en *Ejecución Inicial* → *Ejecución Principal* → *Ejecución Final*.

- Inicial: en paralelo, *Salir de Estado de Entrada* + *Consumir Conjunto de Consumidos*.
- Principal: ciclo de *Comparar Tiempo y Duración* → *Verificar Habilitadores y Afectados* → *Ejecutar Proceso e Incrementar Tiempo*.
- Final: en paralelo, *Generar Resultantes* + *Entrar en Estado de Salida* + *Notificar Éxito*.

Ese modelo muestra:

- descomposición multinivel;
- transiciones de estado a través de la jerarquía;
- enlaces condicionales y omisión condicional;
- manejo de excepciones;
- subprocesos paralelos;
- cambio de rol entre instrumento y afectado según el nivel de abstracción.

---

## Dinámica y simulación

### Ejecutabilidad

Un modelo OPM puede ser ejecutable: la simulación anima el sistema ejecutando el modelo en un entorno de software.

### Modos de transformación

| Modo | Significado |
|---|---|
| Construcción | El objeto es creado o generado |
| Efecto | El objeto cambia de estado y mantiene identidad |
| Consumo | El objeto es eliminado y deja de existir |

Construcción y consumo son transformaciones más profundas que efecto porque cambian existencia, no solo estado.

### Principio de línea de tiempo

La línea temporal por defecto en una descomposición fluye de arriba hacia abajo. Subprocesos a la misma altura se ejecutan en paralelo. Un proceso de salida por excepción puede provocar salida inmediata sin importar su posición gráfica.

### Eventos temporizados

Los eventos de estado pueden representar eventos temporales. Objetos tipo reloj o temporizador del sistema con valores concretos pueden iniciar procesos en instantes definidos.

### Diagrama de vida útil

Un diagrama de vida útil muestra, para cualquier instante:

- qué objetos existen;
- en qué estado está cada uno;
- qué procesos están activos.

Es útil para seguir transiciones a lo largo de la vida del sistema.

### Propiedades de duración de proceso

Las propiedades de duración de proceso (mínima, esperada, máxima, distribución) son propiedades semánticas del proceso. Su especificación formal y representación gráfica (ubicación dentro de la elipse, formato) viven en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §14.

La unidad temporal del sistema es la unidad por defecto para todos los procesos, salvo que se redefina.

Ejemplo:

- `Procesar [min] (30.0, 45.6, 60.0)` con distribución `normal, media=45.6, desviación=7.3`.

### Ejemplos de duración

Esta adaptación recoge cuatro patrones recuperables:

1. **Metamodelo de duración de proceso:** una notación compacta puede codificar duración mínima, esperada y máxima junto con parámetros de distribución; la duración real sigue siendo propiedad de ejecución.
2. **Variantes de distribución:** un mismo proceso puede parametrizarse con distribuciones exponencial, normal o uniforme.
3. **Excepción por sobretiempo:** si la duración real supera la duración máxima, ocurre el proceso de manejo de sobretiempo.
4. **Excepción por subtiempo:** si la duración real cae por debajo de la mínima, ocurre el proceso de manejo de subtiempo.

Ejemplos canónicos:

- `Procesar [min] (30.0, 45.6, 60.0)` con `uniforme, a=5.0, b=70.0`, duración real `63.3`, instancia `1`, para el caso de sobretiempo.
- El mismo intervalo de duración, con duración real `23.4` e instancia `2`, corresponde al caso de subtiempo.

---

## Convenciones editoriales delegadas

Las siguientes materias dejan de definirse en esta capa para evitar duplicación interna del corpus:

- buenas prácticas de legibilidad, densidad visual, apariencias múltiples y copias visuales: [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §15–§16;
- política de nombrado, capitalización, unicidad nominal y patrones de superficie en español: [OPL-ES](urn:fxsl:kb:opl-es) §1;
- reglas operativas para decidir cuándo descomponer, cuándo duplicar una apariencia y cómo resolver ambigüedad durante el modelado: [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

Este documento conserva como invariantes semánticos transversales:

- un estado no existe sin su objeto propietario;
- el objeto consumido desaparece al inicio del proceso, no al final;
- un objeto puede además actuar como disparador (`e`) y/o como condicionante (`c`) sin perder su rol principal como transformado o habilitador;
- la importancia relativa de una cosa suele ser proporcional al OPD más alto de la jerarquía en el que aparece.

---

## Ejemplos aplicados

Ejemplos canónicos del corpus que muestran la notación OPM en uso.

### Mecanizado de barra de acero (enlaces con estado especificado)

Objetos: **Barra de Metal** con estados `pre-cortada`, `cortada`; **Pieza** con estados `pre-probada`, `probada`. Procesos: *Cortar* (ambiental), *Mecanizar* (físico), *Probar* (ambiental). Habilitadores: **Operario de Máquina** y **Refrigerante**.

Composición OPL-ES:

- `*Cortar* cambia **Barra de Metal** de \`pre-cortada\` a \`cortada\`.`
- `*Mecanizar* consume **Barra de Metal** en \`cortada\`.`
- `*Mecanizar* genera **Pieza** en \`pre-probada\`.`
- `**Operario de Máquina** maneja *Mecanizar*.`
- `*Mecanizar* requiere **Refrigerante**.`
- `*Probar* cambia **Pieza** de \`pre-probada\` a \`probada\`.`

### Pago con cheque (descomposición con transiciones de estado)

Objeto: **Cheque** con estados `en blanco → firmado → endosado → cobrado y cancelado`. Atributo: **Custodio** con estados `pagador → beneficiario → institución financiera`. Agentes: **Pagador**, **Beneficiario**, **Banco**.

`*Pagar con Cheque*` se descompone en:

1. `*Escribir y Firmar*`
2. `*Entregar y Aceptar*`
3. `*Endosar y Presentar*`
4. `*Cobrar y Cancelar*`

Ejemplos OPL-ES:

- `*Escribir y Firmar* cambia **Cheque** de \`en blanco\` a \`firmado\`.`
- `*Entregar y Aceptar* cambia **Custodio** de \`pagador\` a \`beneficiario\`.`
- `*Endosar y Presentar* cambia **Cheque** de \`firmado\` a \`endosado\`.`
- `*Cobrar y Cancelar* cambia **Cheque** de \`endosado\` a \`cobrado y cancelado\`.`

### Lavado de platos (cambio de rol según nivel de abstracción)

SD:

- `**Usuario Doméstico** maneja *Lavar Platos*.`
- `*Lavar Platos* requiere **Lavavajillas**.`
- `*Lavar Platos* consume **Jabón**.`
- `*Lavar Platos* afecta **Conjunto de Platos**.`

`SD1`:

- `*Lavar Platos* se descompone en *Cargar Platos*, *Insertar Detergente*, *Lavar y Secar Platos* y *Descargar Platos*, en esa secuencia.`
- `*Cargar Platos* cambia **Lavavajillas** de \`vacío\` a \`cargado\`.`
- `*Descargar Platos* cambia **Lavavajillas** de \`cargado\` a \`vacío\`.`

El punto clave es que **Lavavajillas** es instrumento en el nivel abstracto, pero afectado en el nivel detallado.

### Apertura de caja fuerte (operadores lógicos)

Ejemplos:

- XOR: exactamente uno entre **Propietario A** y **Propietario B** maneja *Abrir Caja Fuerte*.
- OR: al menos uno entre **Propietario A** y **Propietario B** maneja *Abrir Caja Fuerte*.
- AND: `*Abrir Caja Fuerte* requiere **Llave A**, **Llave B** y **Llave C**.`

### Especialización de vehículos (atributo discriminante)

- `**Vehículo** exhibe **Medio de Desplazamiento**.`
- `**Medio de Desplazamiento** puede estar \`tierra\`, \`aire\` o \`superficie acuática\`.`
- `**Auto**, **Aeronave** y **Barco** son **Vehículo**.`
- `**Auto** exhibe **Medio de Desplazamiento** en \`tierra\`.`
- `**Aeronave** exhibe **Medio de Desplazamiento** en \`aire\`.`
- `**Barco** exhibe **Medio de Desplazamiento** en \`superficie acuática\`.`

### Seguridad del hogar (proceso asincrónico)

`*Mantener Seguridad del Hogar*` consta de:

- *Atender Robo*;
- *Proteger contra Incendio*;
- *Alertar Terremoto*.

Como no se conoce el orden temporal, se usa despliegue por agregación-participación y no descomposición temporal.

### Preparación de café (estructura-comportamiento-función)

Estructura:

- `**Máquina de Café** consta de **Depósito de Agua**, **Espumador de Leche**, **Calentador de Agua**, **Compartimento de Cápsulas** y **Portataza**.`

Comportamiento:

- `*Preparar Café*` se descompone en *Calentar Agua*, *Espumar Leche*, *Preparar Café* y *Agregar Leche*.

Función:

- el beneficiario es **Persona que Bebe Café**;
- la función cambia **Satisfacción** de `insatisfecha` a `satisfecha`.

### Operación de auto eléctrico (componentes del SD)

Ejemplo de SD:

- propósito: mejorar **Éxito del Negocio** de **Grupo de Interesados de la Empresa**;
- función: `*Operar Auto Eléctrico*` cambia **Auto Eléctrico** de `detenido` a `en movimiento`;
- agente: **Conductor**;
- instrumento: **Sistema Operativo del Auto Eléctrico**;
- entorno: **Tipo de Terreno**, **Regulaciones**.

### Ejemplos sociales y sociotécnicos auxiliares

- **Control de Tráfico Aéreo:** **Piloto** y **Controlador Aéreo** son agentes; **Torre de Control** es instrumento.
- **Aprendizaje MOOC:** **Grupo de Estudiantes** actúa como agente; la plataforma MOOC como instrumento.
- **Gestión de Identidad Profesional en Línea:** el perfil en línea representa a la persona mediante enlace estructural etiquetado.
- **Transporte de Equipaje:** la función principal cambia la ubicación del equipaje del aeropuerto de origen al de destino.
- **Sistema de Conferencia:** **Organizador** y **Acomodadores** son agentes; instalaciones y equipamiento son instrumentos; el clima puede ser ambiental.

Los flujos de interfaz y los detalles específicos de herramienta que no alteren la semántica del modelo deben mantenerse en documentación operacional separada de este SSOT.

---
