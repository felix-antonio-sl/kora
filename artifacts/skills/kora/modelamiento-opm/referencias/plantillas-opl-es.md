# Plantillas OPL-ES por tipo de hecho

Plantillas operativas tomadas de `urn:fxsl:kb:opl-es`. Para gramatica completa y EBNF, consultar el apendice A de la SSOT.

## Existencia de cosa

| Hecho | Plantilla |
|-------|-----------|
| una cosa es objeto | `<Cosa> es un objeto.` |
| una cosa es proceso | `<Cosa> es un proceso.` |
| una cosa es objeto fisico | `<Cosa> es un objeto fisico.` |
| una cosa es objeto informatico | `<Cosa> es un objeto informatico.` |
| una cosa es proceso fisico | `<Cosa> es un proceso fisico.` |

Ejemplo: `Cafetera es un objeto fisico.`

## Estados de un objeto

| Hecho | Plantilla |
|-------|-----------|
| estado simple | `<Objeto> esta en <estado>.` |
| conjunto de estados | `<Objeto> puede estar en <estado1>, <estado2>, ..., <estadoN>.` |
| estado inicial | `<Objeto> esta inicialmente en <estado>.` |
| estado terminal | `<Objeto> esta terminalmente en <estado>.` |

Ejemplos:
```
Paciente puede estar en no-diagnosticado o diagnosticado.
Paciente esta inicialmente en no-diagnosticado.
```

## Enlaces procedurales transformadores

| Tipo | Plantilla |
|------|-----------|
| consumption | `<Proceso> consume <Objeto>.` |
| result | `<Proceso> produce <Objeto>.` |
| effect | `<Proceso> afecta <Objeto>.` |
| effect con cambio de estado | `<Proceso> cambia <Objeto> de <estado-A> a <estado-B>.` |

Ejemplos:
```
Hacer Cafe consume Agua y Cafe Molido.
Hacer Cafe produce Cafe Hecho.
Diagnosticar cambia Paciente de no-diagnosticado a diagnosticado.
```

## Enlaces procedurales habilitantes

| Tipo | Plantilla |
|------|-----------|
| agent | `<Agente> manipula <Proceso>.` |
| instrument | `<Proceso> usa <Instrumento>.` |
| instrument con condicion | `<Proceso> usa <Instrumento> cuando <Objeto> esta en <estado>.` |

Ejemplos:
```
Persona manipula Hacer Cafe.
Hacer Cafe usa Cafetera.
```

## Enlaces de control

| Tipo | Plantilla |
|------|-----------|
| event | `<Proceso> ocurre cuando <Evento>.` |
| condition | `<Proceso> ocurre si <Objeto> esta en <estado>.` |
| exception | `<Proceso> lanza excepcion <Excepcion>.` |
| invocation | `<Proceso-A> invoca <Proceso-B>.` |

Ejemplos:
```
Resolver Solicitud ocurre cuando Solicitud esta en pendiente.
Diagnosticar invoca Pedir Examen.
```

## Enlaces estructurales

### Agregacion-participacion

| Hecho | Plantilla |
|-------|-----------|
| simple | `<Todo> consta de <Parte1>, <Parte2>, ..., <ParteN>.` |
| con multiplicidad | `<Todo> consta de <N> <Parte>.` |
| opcional | `<Todo> opcionalmente consta de <Parte>.` |

Ejemplo: `Cafe Hecho consta de Liquido y Aroma.`

### Generalizacion-especializacion

| Hecho | Plantilla |
|-------|-----------|
| simple | `<General> es de tipo <Especifico1>, <Especifico2>, ..., <EspecificoN>.` |

Ejemplo: `Vehiculo es de tipo Auto, Camion, Bus.`

### Clasificacion-instanciacion

| Hecho | Plantilla |
|-------|-----------|
| simple | `<Clase> tiene como instancia <Inst1>, <Inst2>, ..., <InstN>.` |

Ejemplo: `Pais tiene como instancia Chile, Argentina, Uruguay.`

### Exhibicion-caracterizacion

| Hecho | Plantilla |
|-------|-----------|
| simple | `<Objeto> exhibe <Atributo1>, <Atributo2>, ..., <AtributoN>.` |
| con tipo | `<Objeto> exhibe <Atributo> de tipo <Tipo>.` |

Ejemplo: `Paciente exhibe Edad, Sexo, Diagnostico.`

## Operadores logicos en fans de enlaces

| Tipo | Plantilla |
|------|-----------|
| AND | `<Proceso> consume <Objeto1> y <Objeto2>.` |
| OR | `<Proceso> consume <Objeto1> o <Objeto2>.` |
| XOR | `<Proceso> consume exactamente uno de <Objeto1> o <Objeto2>.` |

## Sub-modelo (composicion inter-modelo)

| Hecho | Plantilla |
|-------|-----------|
| declaracion | `<Sub-Modelo> es un sub-modelo cargado y sincronizado.` |
| uso | `<Proceso del modelo actual> usa <Sub-Modelo>.` |
| referencia externa | `<Cosa-Externa> esta referenciada desde <Sub-Modelo>.` |

## Reglas generales de surface form

1. **Capitalizacion**: nombres propios (cosas, procesos) en title case. Conectores en minuscula.
2. **Plurales**: `consume Agua y Cafe Molido` (and-fan), nunca `consume Aguas y Cafes Molidos`.
3. **Puntuacion**: cada sentencia termina en punto. Una sentencia por hecho.
4. **Articulos**: la plantilla "<Cosa> es un objeto" usa articulo indeterminado por convencion KORA. Variantes admisibles si la SSOT las autoriza.
5. **Idioma**: prosa de la skill en español. Sentencias OPL en español por defecto. Si el usuario pide OPL-EN explicitamente, traducir manteniendo equivalencia semantica.
6. **Nombres de cosas**: identicos en OPD y OPL-ES. Si el OPD dice `Hacer Cafe`, OPL-ES dice `Hacer Cafe`, no `hacer cafe` ni `el proceso de hacer cafe`.

## Cuando consultar la SSOT directa

Cualquier sentencia que no encaja en las plantillas anteriores requiere consulta directa a `urn:fxsl:kb:opl-es` (apendice A EBNF) y a `urn:fxsl:kb:opd-es` (gramatica visual). Las plantillas son el subset operativo, no el lenguaje completo.
