---
_manifest:
  urn: urn:fxsl:kb:opl-es-p04
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
    shard_index: 4
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opl-es
---

# OPL-ES — Lenguaje Objeto-Proceso en Español - Parte 04

## A.5 Oraciones procedimentales

```ebnf
oracion_procedimental = oracion_transformadora | oracion_habilitadora | oracion_de_control ;
oracion_transformadora = oracion_de_consumo | oracion_de_resultado | oracion_de_efecto | oracion_de_cambio ;

oracion_de_consumo = identificador_de_proceso, " consume ", objeto_con_opcion_de_estado ;
oracion_de_resultado = identificador_de_proceso, " genera ", objeto_con_opcion_de_estado ;
oracion_de_efecto = identificador_de_proceso, " afecta ", lista_de_objetos ;
oracion_de_cambio = oracion_de_cambio_entrada_salida | oracion_de_cambio_solo_entrada
 | oracion_de_cambio_solo_salida ;

frase_de_cambio_entrada_salida = identificador_de_objeto, " de ", estado_de_entrada, " a ", estado_de_salida ;
frase_de_cambio_solo_entrada = identificador_de_objeto, " de ", estado_de_entrada ;
frase_de_cambio_solo_salida = identificador_de_objeto, " a ", estado_de_salida ;
oracion_de_cambio_entrada_salida = identificador_de_proceso, " cambia ", frase_de_cambio_entrada_salida ;
oracion_de_cambio_solo_entrada = identificador_de_proceso, " cambia ", frase_de_cambio_solo_entrada ;
oracion_de_cambio_solo_salida = identificador_de_proceso, " cambia ", frase_de_cambio_solo_salida ;

oracion_habilitadora = oracion_de_agente | oracion_de_instrumento ;
oracion_de_agente = objeto_con_opcion_de_estado, " maneja ", identificador_de_proceso ;
oracion_de_instrumento = identificador_de_proceso, " requiere ", objeto_con_opcion_de_estado ;

oracion_de_control = oracion_de_evento | oracion_de_condicion | oracion_de_invocacion | oracion_de_excepcion ;
oracion_de_evento = oracion_de_evento_de_consumo | oracion_de_evento_de_efecto
 | oracion_de_evento_de_agente | oracion_de_evento_de_instrumento ;
oracion_de_evento_de_consumo = objeto_con_opcion_de_estado, " inicia ", identificador_de_proceso,
 ", que consume ", identificador_de_objeto ;
oracion_de_evento_de_efecto = identificador_de_objeto, " inicia ", identificador_de_proceso,
 ", que afecta ", identificador_de_objeto ;
oracion_de_evento_de_agente = objeto_con_opcion_de_estado, " inicia y maneja ", identificador_de_proceso ;
oracion_de_evento_de_instrumento = objeto_con_opcion_de_estado, " inicia ", identificador_de_proceso,
 ", que requiere ", objeto_con_opcion_de_estado ;

oracion_de_invocacion = identificador_de_proceso, " invoca ", lista_de_procesos
 | identificador_de_proceso, " se invoca a sí mismo" ;
oracion_de_excepcion_por_sobretiempo = identificador_de_proceso_activo,
 " ocurre si duración de ", identificador_de_proceso, " excede ", max_duracion_unidades_tiempo ;
oracion_de_excepcion_por_subtiempo = identificador_de_proceso_activo,
 " ocurre si duración de ", identificador_de_proceso, " es menor que ", min_duracion_unidades_tiempo ;
oracion_de_excepcion = oracion_de_excepcion_por_sobretiempo | oracion_de_excepcion_por_subtiempo ;

(* Etiquetas de ruta *)

oracion_de_ruta =
 "Por ruta ", cadena_etiqueta, ", ", oracion_procedimental ;

cadena_etiqueta = nombre ;
```

Las variantes XOR y OR usan `exactamente uno de` y `al menos uno de`. Las oraciones de condición siguen el patrón `ocurre si ... en cuyo caso ... de lo contrario ... se omite`.

## A.6 Oraciones de condición

```ebnf
oracion_de_condicion = oracion_transformadora_condicional | oracion_habilitadora_condicional ;

oracion_transformadora_condicional = oracion_de_consumo_condicional
 | oracion_de_consumo_condicional_con_estado
 | oracion_de_efecto_condicional ;

oracion_de_consumo_condicional = ( identificador_de_proceso, " ocurre si ", identificador_de_objeto,
 " existe, en cuyo caso ", identificador_de_objeto, " se consume, de lo contrario ",
 identificador_de_proceso, " se omite" )
 | ( "Si ", identificador_de_objeto, " existe entonces ", identificador_de_proceso,
 " ocurre y consume ", identificador_de_objeto, ", de lo contrario se omite ",
 identificador_de_proceso ) ;

oracion_de_consumo_condicional_con_estado = ( identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_objeto, " se consume, de lo contrario ", identificador_de_proceso, " se omite" ) ;

oracion_de_efecto_condicional = oracion_de_efecto_condicional_simple
 | oracion_de_efecto_entrada_salida_condicional
 | oracion_de_efecto_entrada_condicional
 | oracion_de_efecto_salida_condicional ;

oracion_de_efecto_condicional_simple = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, en cuyo caso ", identificador_de_proceso,
 " afecta ", identificador_de_objeto, ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_entrada_salida_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_proceso, " cambia ", identificador_de_objeto, " de ", estado_de_entrada,
 " a ", estado_de_salida, ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_entrada_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_proceso, " cambia ", identificador_de_objeto, " de ", estado_de_entrada,
 ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_salida_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, en cuyo caso ", identificador_de_proceso,
 " cambia ", identificador_de_objeto, " a ", estado_de_salida,
 ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_habilitadora_condicional = oracion_de_agente_condicional
 | oracion_de_instrumento_condicional ;

oracion_de_agente_condicional = ( objeto_con_opcion_de_estado, " maneja ",
 identificador_de_proceso, " si ", identificador_de_objeto, " existe, de lo contrario ",
 identificador_de_proceso, " se omite" )
 | ( objeto_con_opcion_de_estado, " maneja ", identificador_de_proceso, " si ",
 identificador_de_objeto, " está en ", identificador_de_estado, ", de lo contrario ",
 identificador_de_proceso, " se omite" ) ;

oracion_de_instrumento_condicional = ( identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, de lo contrario ", identificador_de_proceso, " se omite" )
 | ( identificador_de_proceso, " ocurre si ", identificador_de_objeto, " está en ",
 identificador_de_estado, ", de lo contrario ", identificador_de_proceso, " se omite" ) ;
```

## A.7 Producciones adicionales

```ebnf
(* --- Restricciones de expresión para multiplicidad --- *)

restriccion_de_expresion = "donde ", nombre, ( ( operacion_logica, nombre_de_valor )
 | ( inicio_conjunto, ( nombre | nombre_de_valor ),
 { ",", ( nombre | nombre_de_valor ) }, fin_conjunto ) ) ;

operacion_logica = "=" | "<" | ">" | "<=" | ">=" ;
inicio_conjunto = " en {" ;
fin_conjunto = "}" ;

(* --- Listas bifurcadas con orden --- *)

conjunto_de_cosas_objeto = cosa_objeto, [ { ", ", cosa_objeto } ],
 " y ", ( cosa_objeto | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;

conjunto_de_cosas_proceso = cosa_proceso, [ { ", ", cosa_proceso } ],
 " y ", ( cosa_proceso | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;

criterio_de_orden = nombre ;
cosa_objeto = [ restriccion_de_participacion, " " ], objeto_con_opcion_de_estado ;
cosa_proceso = [ restriccion_de_participacion, " " ], identificador_de_proceso ;

(* --- Especialización XOR y herencia múltiple --- *)

oracion_de_especializacion_xor_objeto = oracion_basica_xor_objeto
 | oracion_xor_objeto_separada_por_comas ;
oracion_basica_xor_objeto = objeto_especial, " puede ser ",
 identificador_de_objeto, " o ", identificador_de_objeto ;
oracion_xor_objeto_separada_por_comas = objeto_especial, " puede ser uno de ",
 identificador_de_objeto, { ", ", identificador_de_objeto }, " o ", identificador_de_objeto ;

oracion_de_herencia_multiple_objeto = objeto_especial, " es ",
 lista_de_objetos_generales ;
lista_de_objetos_generales = " un ", identificador_de_objeto,
 [ { " un ", identificador_de_objeto } ], " y un ", identificador_de_objeto ;
```

## A.8 Oraciones estructurales

```ebnf
oracion_estructural = oracion_de_enlace_estructural_etiquetado | oracion_de_agregacion
 | oracion_de_caracterizacion
 (* | oracion_de_exhibicion — eliminada de oracion_estructural: alias de oracion_de_caracterizacion, genera ambiguedad *)
 | oracion_de_especializacion | oracion_de_instanciacion ;

(* --- Oraciones de enlace estructural etiquetado --- *)

oracion_de_enlace_estructural_etiquetado = oracion_etiquetado_unidireccional
 | oracion_etiquetado_bidireccional ;

oracion_etiquetado_unidireccional = oracion_etiquetado_unidireccional_simple
 | oracion_etiquetado_bifurcada ;

oracion_etiquetado_unidireccional_simple =
 oracion_etiquetado_nullTag_objeto
 | oracion_etiquetado_nullTag_proceso
 | oracion_etiquetado_nonNullTag_objeto
 | oracion_etiquetado_nonNullTag_proceso ;

oracion_etiquetado_nullTag_objeto = [restriccion_de_participacion, " "],
 objeto_origen, etiqueta_nula_unidireccional, [restriccion_de_participacion, " "], objeto_destino ;
oracion_etiquetado_nullTag_proceso = [restriccion_de_participacion, " "],
 proceso_origen, etiqueta_nula_unidireccional, [restriccion_de_participacion, " "], proceso_destino ;
oracion_etiquetado_nonNullTag_objeto = [restriccion_de_participacion, " "],
 objeto_origen, " ", etiqueta_directa, " ", [restriccion_de_participacion, " "], objeto_destino,
 [", ", restriccion_de_expresion] ;
oracion_etiquetado_nonNullTag_proceso = [restriccion_de_participacion, " "],
 proceso_origen, " ", etiqueta_directa, " ", [restriccion_de_participacion, " "], proceso_destino ;

etiqueta_nula_unidireccional = " se relaciona con "
 | etiqueta_nula_definida_por_usuario ;

(* Variantes bifurcadas: listas de refinadores con orden o secuencia *)
oracion_etiquetado_bifurcada = oracion_bifurcada_nullTag_objeto
 | oracion_bifurcada_nullTag_proceso
 | oracion_bifurcada_nonNullTag_objeto
 | oracion_bifurcada_nonNullTag_proceso ;

oracion_bifurcada_nullTag_objeto = [restriccion_de_participacion, " "], objeto_origen,
 etiqueta_nula_unidireccional, conjunto_de_cosas_objeto ;
oracion_bifurcada_nullTag_proceso = [restriccion_de_participacion, " "], proceso_origen,
 etiqueta_nula_unidireccional, conjunto_de_cosas_proceso ;
oracion_bifurcada_nonNullTag_objeto = [restriccion_de_participacion, " "], objeto_origen,
 " ", etiqueta_directa, " ", conjunto_de_cosas_objeto ;
oracion_bifurcada_nonNullTag_proceso = [restriccion_de_participacion, " "], proceso_origen,
 " ", etiqueta_directa, " ", conjunto_de_cosas_proceso ;

(* conjunto_de_cosas_objeto y conjunto_de_cosas_proceso ya definidos en A.7 — no redefinir aquí *)

(* Variantes bidireccionales *)
oracion_etiquetado_bidireccional = oracion_bidireccional_asimetrica_objeto
 | oracion_bidireccional_asimetrica_proceso
 | oracion_bidireccional_simetrica_objeto
 | oracion_bidireccional_simetrica_proceso ;

oracion_bidireccional_asimetrica_objeto = ( [restriccion_de_participacion, " "],
 objeto_origen, etiqueta_directa_bidireccional, [restriccion_de_participacion, " "], objeto_destino,
 [", ", restriccion_de_expresion] )
 | ( [restriccion_de_participacion, " "], objeto_destino, etiqueta_inversa_bidireccional,
 [restriccion_de_participacion, " "], objeto_origen, [", ", restriccion_de_expresion] ) ;
oracion_bidireccional_simetrica_objeto = ( [restriccion_de_participacion, " "],
 objeto_origen, " y ", [restriccion_de_participacion, " "], objeto_destino, " son ", etiqueta_simetrica )
 | ( [restriccion_de_participacion, " "], objeto_origen, " y ", [restriccion_de_participacion, " "],
 objeto_destino, etiqueta_nula_bidireccional ) ;

oracion_bidireccional_asimetrica_proceso = ( [restriccion_de_participacion, " "],
 proceso_origen, etiqueta_directa_bidireccional, [restriccion_de_participacion, " "], proceso_destino )
 | ( [restriccion_de_participacion, " "], proceso_destino, etiqueta_inversa_bidireccional,
 [restriccion_de_participacion, " "], proceso_origen ) ;
oracion_bidireccional_simetrica_proceso = ( [restriccion_de_participacion, " "],
 proceso_origen, " y ", [restriccion_de_participacion, " "], proceso_destino, " son ", etiqueta_simetrica )
 | ( [restriccion_de_participacion, " "], proceso_origen, " y ", [restriccion_de_participacion, " "],
 proceso_destino, etiqueta_nula_bidireccional ) ;

etiqueta_simetrica = expresion_de_etiqueta ;
etiqueta_directa_bidireccional = expresion_de_etiqueta ;
etiqueta_inversa_bidireccional = expresion_de_etiqueta ;
etiqueta_nula_bidireccional = " se relacionan"
 | etiqueta_nula_definida_por_usuario ;

```

## A.9 Oraciones de estructuras fundamentales

```ebnf
oracion_de_agregacion = oracion_de_agregacion_objeto | oracion_de_agregacion_proceso ;
oracion_de_agregacion_objeto = objeto_todo, " consta de ", lista_de_partes_objeto ;
oracion_de_agregacion_proceso = proceso_todo, " consta de ", lista_de_partes_proceso ;
lista_de_partes_objeto = parte_objeto, [ { ", ", parte_objeto } ], " y ", ( parte_objeto | "al menos otra parte" ) ;
lista_de_partes_proceso = parte_proceso, [ { ", ", parte_proceso } ], " y ", ( parte_proceso | "al menos otra parte" ) ;
parte_objeto = [restriccion_de_participacion, " "], identificador_de_objeto ;
parte_proceso = [restriccion_de_participacion, " "], identificador_de_proceso ;

oracion_de_caracterizacion = oracion_de_caract_objeto | oracion_de_caract_proceso ;
oracion_de_caract_objeto = identificador_de_objeto, " exhibe ",
 ( lista_de_atributos | lista_de_operadores
 | lista_de_atributos, ", así como ", lista_de_operadores ) ;
oracion_de_caract_proceso = identificador_de_proceso, " exhibe ",
 ( lista_de_operadores | lista_de_atributos
 | lista_de_operadores, ", así como ", lista_de_atributos ) ;

(* Alias conservado como documentacion; no referenciado desde oracion_estructural para evitar ambiguedad *)
oracion_de_exhibicion = oracion_de_caract_objeto | oracion_de_caract_proceso ;

oracion_de_especializacion = oracion_de_especializacion_objeto | oracion_de_especializacion_proceso
 | oracion_de_especializacion_estado
 | oracion_de_especializacion_individual
 | oracion_de_especializacion_xor_objeto
 | oracion_de_herencia_multiple_objeto ;
oracion_de_especializacion_objeto = lista_de_objetos_especiales, " son ", identificador_de_objeto ;
oracion_de_especializacion_proceso = lista_de_procesos_especiales, " son ", identificador_de_proceso ;
oracion_de_especializacion_estado = lista_de_objetos_con_estado, " son ", objeto_con_estado ;

oracion_de_especializacion_individual =
 identificador_de_objeto, " es ", articulo, identificador_de_objeto ;

articulo = "un " | "una " ;

oracion_de_instanciacion = oracion_de_instanciacion_objeto | oracion_de_instanciacion_proceso ;
oracion_de_instanciacion_objeto = identificador_de_objeto, " es una instancia de ", identificador_de_objeto
 | lista_de_objetos_instancia, " son instancias de ", identificador_de_objeto ;
oracion_de_instanciacion_proceso = identificador_de_proceso, " es una instancia de ", identificador_de_proceso
 | lista_de_procesos_instancia, " son instancias de ", identificador_de_proceso ;

atributo = identificador_de_objeto ;
operador = identificador_de_proceso ;
rasgo = atributo | operador ;
```
