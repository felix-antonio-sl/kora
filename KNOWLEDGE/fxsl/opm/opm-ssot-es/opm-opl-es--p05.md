---
_manifest:
  urn: urn:fxsl:kb:opl-es-p05
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
    shard_index: 5
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opl-es
---

# OPL-ES — Lenguaje Objeto-Proceso en Español - Parte 05

## A.9 Oraciones de gestión de contexto

```ebnf
oracion_de_gestion_de_contexto = oracion_de_despliegue | oracion_de_plegado
 | oracion_de_descomposicion | oracion_de_recomposicion ;

(* --- Oraciones de despliegue (unfolding) --- *)

oracion_de_despliegue = oracion_de_despliegue_objeto | oracion_de_despliegue_proceso ;

oracion_de_despliegue_objeto = oracion_de_despliegue_objeto_inespecificado
 | oracion_de_despliegue_objeto_todo
 | oracion_de_despliegue_objeto_general
 | oracion_de_despliegue_objeto_clase
 | oracion_de_despliegue_objeto_exhibidor ;

oracion_de_despliegue_objeto_inespecificado = identificador_de_objeto,
 " se despliega en ", lista_de_atributos, [", así como ", lista_de_operadores] ;
oracion_de_despliegue_objeto_todo = objeto_todo, " desde ", opd_padre,
 " se despliega por partes en ", opd_hijo, " en ", lista_de_partes_objeto ;
oracion_de_despliegue_objeto_general = objeto_general, " desde ", opd_padre,
 " se despliega por especialización en ", opd_hijo, " en ", lista_de_objetos_especiales ;
oracion_de_despliegue_objeto_clase = clase_de_objeto, " desde ", opd_padre,
 " se despliega por instanciación en ", opd_hijo, " en ", lista_de_objetos_instancia ;
oracion_de_despliegue_objeto_exhibidor = identificador_de_objeto, " desde ", opd_padre,
 " se despliega por rasgos en ", opd_hijo, " en ", lista_de_atributos, [", así como ", lista_de_operadores] ;

oracion_de_despliegue_proceso = oracion_de_despliegue_proceso_inespecificado
 | oracion_de_despliegue_proceso_todo
 | oracion_de_despliegue_proceso_general
 | oracion_de_despliegue_proceso_clase
 | oracion_de_despliegue_proceso_exhibidor ;

oracion_de_despliegue_proceso_inespecificado = identificador_de_proceso,
 " se despliega en ", lista_de_operadores, [", así como ", lista_de_atributos] ;
oracion_de_despliegue_proceso_todo = proceso_todo, " desde ", opd_padre,
 " se despliega por partes en ", opd_hijo, " en ", lista_de_partes_proceso ;
oracion_de_despliegue_proceso_general = proceso_general, " desde ", opd_padre,
 " se despliega por especialización en ", opd_hijo, " en ", lista_de_procesos_especiales ;
oracion_de_despliegue_proceso_clase = clase_de_proceso, " desde ", opd_padre,
 " se despliega por instanciación en ", opd_hijo, " en ", lista_de_procesos_instancia ;
oracion_de_despliegue_proceso_exhibidor = identificador_de_proceso, " desde ", opd_padre,
 " se despliega por rasgos en ", opd_hijo, " en ", lista_de_operadores, [", así como ", lista_de_atributos] ;

(* --- Oraciones de plegado (folding) --- *)

oracion_de_plegado = oracion_de_plegado_objeto | oracion_de_plegado_proceso ;
oracion_de_plegado_objeto = identificador_de_objeto, " se pliega en ", opd_hijo ;
oracion_de_plegado_proceso = identificador_de_proceso, " se pliega en ", opd_hijo ;

(* --- Oraciones de descomposición (in-zooming) --- *)

oracion_de_descomposicion = oracion_de_descomposicion_en_diagrama
 | oracion_de_descomposicion_en_nuevo_diagrama
 | oracion_de_descomposicion_objeto_en_diagrama
 | oracion_de_descomposicion_objeto_en_nuevo_diagrama ;

oracion_de_descomposicion_en_diagrama = ( identificador_de_proceso, " se descompone en ",
 lista_de_procesos, ", en esa secuencia", [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " se descompone en paralelo ", lista_de_procesos,
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " se descompone en ", lista_de_procesos,
 " y en paralelo ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] ) ;

oracion_de_descomposicion_en_nuevo_diagrama = ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en paralelo ", lista_de_procesos,
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_procesos,
 " y en paralelo ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] ) ;

oracion_de_descomposicion_objeto_en_diagrama = ( identificador_de_objeto, " se descompone en ",
 lista_de_objetos, ", en esa secuencia", [", así como ", lista_de_procesos_en_zoom] ) ;

oracion_de_descomposicion_objeto_en_nuevo_diagrama = ( identificador_de_objeto, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_objetos, ", en esa secuencia",
 [", así como ", lista_de_procesos_en_zoom] ) ;

lista_de_objetos_en_zoom = identificador_de_objeto, [ { ", ", identificador_de_objeto } ], " y ", identificador_de_objeto,
 ", en esa secuencia" ;
lista_de_procesos_en_zoom = identificador_de_proceso, [ { ", ", identificador_de_proceso } ] ;

(* --- Oraciones de recomposición (out-zooming) --- *)

oracion_de_recomposicion = oracion_de_recomposicion_proceso | oracion_de_recomposicion_objeto ;
oracion_de_recomposicion_proceso = identificador_de_proceso, " se recompone desde ", opd_hijo ;
oracion_de_recomposicion_objeto = identificador_de_objeto, " se recompone desde ", opd_hijo ;
```

Para subprocesos paralelos, la forma abreviada es:

- `*Proceso* se descompone en paralelo *A* y *B*.`

Para subprocesos mixtos (secuenciales y paralelos):

- `*Proceso* se descompone en *A*, paralelo *B* y *C*, y *D*, en esa secuencia.`

---

## 18. Notas de Implementación

### 18.1 Análisis Sintáctico Bidireccional

Una herramienta OPM bilingüe debería:

1. Detectar idioma de la sentencia OPL por verbo principal (consume/consumes, genera/yields, etc.)
2. Permitir cambio de idioma global del modelo (re-generar todas las sentencias OPL)
3. Mantener el modelo semántico (OPD) independiente del idioma OPL
4. Permitir modelos mixtos solo si el usuario lo habilita explícitamente (no recomendado)

### 18.2 Soporte de herramienta

Una herramienta OPM multilingüe puede implementar OPL-ES como idioma textual alternativo del mismo modelo semántico.

A nivel de superficie textual, una implementación operativa DEBERÍA además permitir:

1. Elegir idioma OPL a nivel de usuario/modelo sin alterar el OPD subyacente
2. Mostrar todas las sentencias o solo las de esencia no predeterminada
3. Alternar numeración, alias y visualización de unidades sin afectar la semántica
4. Regenerar el párrafo OPL completo al cambiar idioma, manteniendo invariantes de ida y vuelta

### 18.3 Compatibilidad Semántica

OPL-ES no modifica la semántica OPM. Un modelo creado con OPL-ES es semánticamente idéntico a su equivalente OPL-EN. La traducción es puramente léxica y sintáctica, no semántica. El modelo interno (constructos OPD, conjuntos de enlaces, conjuntos de cosas) permanece invariante.

### 18.4 Equivalencia de Ida y Vuelta

Toda sentencia OPL-EN en forma canónica tiene al menos una sentencia OPL-ES semánticamente equivalente y viceversa. La transformación EN→ES→EN DEBE preservar la semántica original, aunque la superficie española pueda realizarse con infinitivo o con nominalización encabezada por `-ción` (y, cuando aplique, `-miento`). La herramienta DEBERÍA respetar la forma elegida por el modelo o normalizarla al registro configurado, pero NO forzar exclusivamente infinitivo.

**Nota normativa sobre ida y vuelta y superficie:** preservar ida y vuelta NO significa imponer una única forma superficial en español. Significa preservar el mismo hecho del modelo y la misma estructura argumental. Por lo tanto, si dos nombres de proceso en OPL-ES son semánticamente equivalentes y válidos en el dominio, ambos PUEDEN mapear al mismo proceso interno, siempre que el modelo conserve un nombre canónico interno por cosa. Ejemplo: `Verificar Identidad` y `Verificación de Identidad` PUEDEN representar el mismo proceso. Al volver de ES a EN, la herramienta DEBE recuperar un nombre inglés semánticamente equivalente, aunque la superficie española original no haya sido la única posible. La normalización de superficie, si existe, DEBERÍA ser configurable por política editorial del modelo, no una imposición semántica fija del lenguaje.

### 18.5 Política de Modelos Mixtos

Un modelo con prosa de apoyo en español y OPL canónica en inglés es aceptable como artefacto editorial, pero una herramienta bilingüe NO DEBERÍA mezclar OPL-EN y OPL-ES dentro del mismo párrafo generado salvo habilitación explícita del usuario. La política recomendada es:

1. Un idioma OPL canónico por modelo activo
2. Cambio de idioma mediante re-generación completa, no edición parcial
3. Mezcla EN/ES solo para revisión o migración, nunca como estado estable por defecto
