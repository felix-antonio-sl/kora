---
_manifest:
  urn: urn:fxsl:kb:opl-es-p03
version: 2.0.0
status: published
tags:
- opm
- opl
- spanish
- es
- grammar
- i18n
- bimodal
- localization
lang: es
extensions:
  kora:
    family: specification
    depends_on:
    - urn:fxsl:kb:opm-es
    shard_index: 3
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opl-es
---

# OPL-ES — Lenguaje Objeto-Proceso en Español - Parte 03

## 16. Ejemplo Completo: Sistema de Preparación de Empanadas

### Contexto

Sistema doméstico de preparación de empanadas de pino (tradicionales chilenas). Modela el SD completo con los 5 componentes de un sistema artificial.

### Componentes del SD

| Componente | Elemento |
|-----------|---------|
| 1. Propósito | Cambiar **Nivel de Satisfacción** de **Grupo de Comensales** de `insatisfecho` a `satisfecho` |
| 2. Función principal | *Preparar Empanadas* (proceso principal) + **Grupo de Comensales** (operando) |
| 3. Habilitadores | **Cocinero** (agente), **Sistema de Preparación de Empanadas** (instrumento principal), **Horno**, **Utensilios de Cocina** (instrumentos) |
| 4. Entorno | **Receta** (informacional, ambiental) |
| 5. Ocurrencia del problema | *Cocinar sin Sistema* (proceso ambiental) causa estado `insatisfecho` |

### Tabla de Elementos

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Preparar Empanadas* | Físico | Sistémico | — |
| Objeto | **Grupo de Comensales** | Físico | Sistémico | — |
| Objeto | **Nivel de Satisfacción** | Informacional | Sistémico | `insatisfecho`, `satisfecho` |
| Objeto | **Cocinero** | Físico | Sistémico | — |
| Objeto | **Sistema de Prep. de Empanadas** | Físico | Sistémico | — |
| Objeto | **Horno** | Físico | Sistémico | — |
| Objeto | **Utensilios de Cocina** | Físico | Sistémico | — |
| Objeto | **Masa Cruda** | Físico | Sistémico | — |
| Objeto | **Relleno de Pino** | Físico | Sistémico | — |
| Objeto | **Empanada** | Físico | Sistémico | — |
| Objeto | **Receta** | Informacional | Ambiental | — |

### Tabla de Enlaces

| Tipo | Origen | Destino | ID |
|------|--------|---------|-----|
| Efecto (entrada-salida) | *Preparar Empanadas* | **Nivel de Satisfacción** | TS3 |
| Exhibición-caracterización | **Grupo de Comensales** | **Nivel de Satisfacción** | RF2 |
| Agente | **Cocinero** | *Preparar Empanadas* | H1 |
| Instrumento | **Sistema de Prep. de Empanadas** | *Preparar Empanadas* | H2 |
| Instrumento | **Horno** | *Preparar Empanadas* | H2 |
| Instrumento | **Utensilios de Cocina** | *Preparar Empanadas* | H2 |
| Consumo | **Masa Cruda** | *Preparar Empanadas* | T1 |
| Consumo | **Relleno de Pino** | *Preparar Empanadas* | T1 |
| Resultado | *Preparar Empanadas* | **Empanada** | T2 |
| Etiquetado (nulo) | **Receta** | *Preparar Empanadas* | SE2 |

### OPL-ES del SD

```
*Preparar Empanadas* afecta **Grupo de Comensales**.
**Grupo de Comensales** exhibe **Nivel de Satisfacción**.
**Nivel de Satisfacción** puede estar `insatisfecho` o `satisfecho`.
Estado `insatisfecho` de **Nivel de Satisfacción** es inicial.
Estado `satisfecho` de **Nivel de Satisfacción** es final.
*Preparar Empanadas* cambia **Nivel de Satisfacción** de `insatisfecho` a `satisfecho`.
**Cocinero** maneja *Preparar Empanadas*.
*Preparar Empanadas* requiere **Sistema de Preparación de Empanadas**.
*Preparar Empanadas* requiere **Horno**.
*Preparar Empanadas* requiere **Utensilios de Cocina**.
*Preparar Empanadas* consume **Masa Cruda**.
*Preparar Empanadas* consume **Relleno de Pino**.
*Preparar Empanadas* genera **Empanada**.
**Receta** es ambiental.
**Receta** se relaciona con *Preparar Empanadas*.
```

### OPL-EN Equivalente

```
Preparing Empanadas affects Diner Group.
Diner Group exhibits Satisfaction Level.
Satisfaction Level can be unsatisfied or satisfied.
State unsatisfied of Satisfaction Level is initial.
State satisfied of Satisfaction Level is final.
Preparing Empanadas changes Satisfaction Level from unsatisfied to satisfied.
Cook handles Preparing Empanadas.
Preparing Empanadas requires Empanada Preparation System.
Preparing Empanadas requires Oven.
Preparing Empanadas requires Kitchen Utensils.
Preparing Empanadas consumes Raw Dough.
Preparing Empanadas consumes Pino Filling.
Preparing Empanadas yields Empanada.
Recipe is Environmental.
Recipe relates to Preparing Empanadas.
```

### SD1: Descomposición de Preparar Empanadas

```
SD se refina por descomposición de *Preparar Empanadas* en SD1.
*Preparar Empanadas* se descompone en *Preparar Masa*, *Preparar Relleno*,
 *Armar Empanadas* y *Hornear Empanadas*, en esa secuencia.
*Preparar Masa* consume **Masa Cruda**.
*Preparar Masa* genera **Masa Estirada**.
*Preparar Relleno* consume **Relleno de Pino**.
*Preparar Relleno* genera **Relleno Cocido**.
*Armar Empanadas* consume **Masa Estirada**.
*Armar Empanadas* consume **Relleno Cocido**.
*Armar Empanadas* genera **Empanada** en `cruda`.
**Horno** puede estar `frío` o `precalentado`.
*Hornear Empanadas* requiere **Horno** en `precalentado`.
*Hornear Empanadas* cambia **Empanada** de `cruda` a `horneada`.
```

---

## 17. Adaptaciones de la EBNF al español

La EBNF de esta capa textual define la superficie canónica de OPL en español. Frente a la formulación inglesa de referencia, requiere las siguientes adaptaciones:

### 17.1 Terminales Léxicos

Sustituir cada terminal reservado EN por su equivalente ES según la tabla de la sección 2.

### 17.2 Identificadores

```ebnf
(* EN *)
process identifier = singular process name | singular process name, " process" ;
(* ES *)
identificador de proceso = nombre singular de proceso | nombre singular de proceso, " proceso" ;
```

Nombre de proceso EN: frase en gerundio capitalizada (-ing). Nombre de proceso ES: frase capitalizada encabezada por infinitivo (`-ar`, `-er`, `-ir`) o por nominalización en `-ción`; `-miento` también se acepta cuando el dominio lo requiere.

```ebnf
(* EN *)
state identifier = non capitalized word ;
(* ES — sin cambio *)
identificador de estado = palabra no capitalizada ;
```

### 17.3 Participación

```ebnf
(* EN *)
lower single = "a" | "an" | "an optional" | "at least one" ;
(* ES *)
singular inferior = "un" | "una" | "un opcional" | "una opcional" | "al menos un" | "al menos una" ;
```

### 17.4 Sentencias de Cambio de Estado

```ebnf
(* EN *)
in out object change phrase = object identifier, " from ", input state, " to ", output state ;
(* ES *)
frase de cambio entrada-salida = identificador de objeto, " de ", estado entrada, " a ", estado salida ;
```

### 17.5 Estructura de Producción

Las reglas de producción de alto nivel no cambian. En OPL-ES se sustituyen los terminales léxicos y se introducen alias de no terminales auxiliares para mantener claridad en español. El criterio normativo es que la gramática quede cerrada y semánticamente equivalente, no que replique literalmente todos los identificadores internos del anexo inglés.

---

## Apéndice A. Gramática formal OPL-ES completa

Este apéndice reúne la EBNF completa de OPL-ES. Se traslada aquí desde la capa base para eliminar solapamiento editorial: la semántica del hecho sigue perteneciendo a `opm-es`, pero la definición formal de su superficie textual canónica pertenece a OPL-ES.

## A.1 Estructura del documento

```ebnf
parrafo_opl_es = oracion_opl_es, { salto_de_linea, oracion_opl_es } ;
oracion_opl_es = oracion_formal_opl_es, "." ;
oracion_formal_opl_es = oracion_de_descripcion_de_cosa
 | oracion_procedimental
 | oracion_estructural
 | oracion_de_gestion_de_contexto ;
```

## A.2 Declaraciones base

```ebnf
digito_no_cero = '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
digito_decimal = '0' | digito_no_cero ;
entero_positivo = digito_no_cero, {digito_decimal} ;
nombre = letra, {caracter_de_cadena} ;
palabra_capitalizada = letra_mayuscula, {caracter_de_cadena} ;
palabra_no_capitalizada = letra_minuscula, {caracter_de_cadena} ;
frase_no_capitalizada = palabra_no_capitalizada, { " ", palabra_no_capitalizada } ;
letra = letra_mayuscula | letra_minuscula ;
letra_mayuscula = 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
 | 'Á' | 'É' | 'Í' | 'Ó' | 'Ú' | 'Ñ' | 'Ü' ;
letra_minuscula = 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
 | 'á' | 'é' | 'í' | 'ó' | 'ú' | 'ñ' | 'ü' ;
(* OPL-ES amplía el alfabeto básico para cubrir caracteres propios del español:
 vocales acentuadas, eñe y diéresis. *)
caracter_de_cadena = letra | digito_decimal | '-' | '_' ;
identificador_de_tipo = "boolean" | "string" | tipo_numerico | "enumerated" ;
tipo_numerico = [prefijo], "integer" | "float" | "double" | "short" | "long" ;
restriccion_de_participacion = singular_inferior | singular_superior | plural_inferior | plural_superior
 | ( "0" | limite_de_participacion, [ " a ", limite_de_participacion ] ) ;
singular_inferior = "un" | "una" | "un opcional" | "una opcional" | "al menos un" | "al menos una" ;
singular_superior = "exactamente un" | "exactamente una" ;
plural_inferior = "al menos dos" ;
plural_superior = "dos o más" ;
limite_de_participacion = entero_positivo | nombre ;
prefijo = "unsigned " | "signed " ;
unidad_de_medida = nombre ;
nombre_de_valor = nombre | entero_positivo ;
clausula_de_rango = " es ", nombre_de_valor | " varía de ", nombre_de_valor, " a ", nombre_de_valor ;
```

## A.3 Identificadores

```ebnf
identificador_de_objeto = nombre_singular_de_objeto, [ " en ", unidad_de_medida ], [ clausula_de_rango ] ;
identificador_de_proceso = nombre_singular_de_proceso | nombre_singular_de_proceso, " proceso" ;
identificador_de_cosa = identificador_de_objeto | identificador_de_proceso ;
identificador_de_estado = palabra_no_capitalizada ;
expresion_de_etiqueta = frase_no_capitalizada ;
nombre_singular_de_objeto = palabra_capitalizada, { " ", palabra_capitalizada | palabra_no_capitalizada } ;
nombre_singular_de_proceso = palabra_capitalizada, { " ", palabra_capitalizada | palabra_no_capitalizada } ;
estado_de_entrada = identificador_de_estado ;
estado_de_salida = identificador_de_estado ;
objeto_con_opcion_de_estado = identificador_de_objeto, [ " en ", identificador_de_estado ] ;
objeto_con_opcion = identificador_de_objeto ;
proceso_con_opcion = identificador_de_proceso ;
objeto_origen = identificador_de_objeto ;
objeto_destino = identificador_de_objeto ;
proceso_origen = identificador_de_proceso ;
proceso_destino = identificador_de_proceso ;
objeto_todo = identificador_de_objeto ;
proceso_todo = identificador_de_proceso ;
objeto_general = identificador_de_objeto ;
proceso_general = identificador_de_proceso ;
clase_de_objeto = identificador_de_objeto ;
clase_de_proceso = identificador_de_proceso ;
objeto_especial = identificador_de_objeto ;
objeto_con_estado = identificador_de_objeto, " en ", identificador_de_estado ;
opd_padre = nombre ;
opd_hijo = nombre ;
identificador_de_proceso_activo = identificador_de_proceso ;
max_duracion_unidades_tiempo = nombre_de_valor, " unidades-tiempo" ;
min_duracion_unidades_tiempo = nombre_de_valor, " unidades-tiempo" ;
lista_de_estados = identificador_de_estado, { ", ", identificador_de_estado }, [ " o ", identificador_de_estado ] ;
lista_de_objetos = identificador_de_objeto, { ", ", identificador_de_objeto }, [ " y ", identificador_de_objeto ] ;
lista_de_procesos = identificador_de_proceso, { ", ", identificador_de_proceso }, [ " y ", identificador_de_proceso ] ;
lista_de_atributos = identificador_de_objeto, { ", ", identificador_de_objeto }, [ " y ", identificador_de_objeto ] ;
lista_de_operadores = identificador_de_proceso, { ", ", identificador_de_proceso }, [ " y ", identificador_de_proceso ] ;
lista_de_objetos_especiales = lista_de_objetos ;
lista_de_procesos_especiales = lista_de_procesos ;
lista_de_objetos_instancia = lista_de_objetos ;
lista_de_procesos_instancia = lista_de_procesos ;
lista_de_objetos_con_estado = objeto_con_estado, { ", ", objeto_con_estado }, [ " y ", objeto_con_estado ] ;
etiqueta_directa = expresion_de_etiqueta ;
etiqueta_nula_definida_por_usuario = expresion_de_etiqueta ;
```

Convenciones:

- nombres de objeto: sintagmas nominales en singular, con mayúscula en palabras léxicas;
- nombres de proceso: infinitivo o nominalización técnica canónica del dominio;
- nombres de estado: en minúscula;
- etiquetas: frases breves en minúscula.

## A.4 Oraciones de descripción de cosas

```ebnf
oracion_de_descripcion_de_cosa = oracion_de_propiedad_generica
 | oracion_de_enumeracion_de_estados
 | oracion_de_estados_iniciales
 | oracion_de_estados_finales
 | oracion_de_estado_por_defecto
 | oracion_de_tipo_de_dato ;

oracion_de_tipo_de_dato =
 identificador_de_objeto, " es de tipo ", identificador_de_tipo ;

oracion_de_propiedad_generica = identificador_de_cosa, " es ", [esencia], [afiliacion], [perseverancia] ;
oracion_de_enumeracion_de_estados = identificador_de_objeto, " puede estar ", lista_de_estados | "..., y otros estados" ;
oracion_de_estados_iniciales = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es inicial" ;
oracion_de_estados_finales = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es final" ;
oracion_de_estado_por_defecto = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es por defecto" ;
esencia = "física" | "informacional" ;
afiliacion = "ambiental" | "sistémica" ;
perseverancia = "persistente" | "transitoria" ;
```

Esencia: `Física` o `Informacional`. Afiliación: `Sistémica` o `Ambiental`. Perseverancia: `Persistente` o `Transitoria`.
