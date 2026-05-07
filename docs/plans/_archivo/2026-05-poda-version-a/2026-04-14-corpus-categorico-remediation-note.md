# Remediacion del corpus categorico agentico

Fecha: 2026-04-14
Scope: `KNOWLEDGE/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`

## Objetivo

Dejar el corpus en un estado mas consistente internamente, con mejor separacion entre:

- resultado formal
- modelo de ingenieria
- analogia disciplinada

La meta no fue "aplanar" el corpus ni volverlo academico en exceso, sino conservar su potencia conceptual mientras se reducian afirmaciones demasiado literales o formalmente mal tipadas.

## Tipos de cambios aplicados

- Correccion de errores formales duros:
  - ejemplo de conexion de Galois en `06-adjunciones.md`
  - tipado de formulas pointwise en `10-extension.md`
  - uso impropio de `C/X` para instancias en `05-universales.md`
  - unidad del producto cartesiano en `11-interaccion.md`
  - mezcla indebida entre compact closed y Frobenius en `07-composicion-con-estructura.md`

- Normalizacion de claims fuertes:
  - Yoneda ya no se presenta como licencia para identificar literalmente objeto e interfaz
  - `faithful`/`full` ya no se usan como sinonimos generales de "buena traduccion" o "buen encapsulamiento"
  - varias afirmaciones del tipo "X es una adjuncion", "X es un sheaf", "X es una 2-categoria" pasaron a "X se deja modelar como..." o "X puede leerse como..."

- Alineacion cruzada entre documentos:
  - base temporal de `12-topoi.md` y `15-tiempo.md`
  - tool use / profunctors entre `14-agencia.md` y `20-infraestructura-autonoma.md`
  - patrones y sintesis alineados con los capitulos base

- Normalizacion terminologica:
  - mayor consistencia en `tipo de comportamiento`, `categoria de Kleisli`, `morfismo de recuperacion`, `morfismo geometrico`, `uso de herramientas`, `2-categoria`

## Regla editorial adoptada

En este corpus:

- usar "es" cuando el resultado formal ya fue introducido y realmente cierra
- usar "se deja modelar como" cuando la construccion es una presentacion util pero dependiente del marco
- usar "se parece a", "tiene lectura", o "captura bien" cuando estamos en analogia controlada

## Resultado

El corpus mantiene su arco conceptual original:

`composicion -> preservacion -> naturalidad -> universalidad -> adjunciones -> efectos -> interaccion -> topoi -> tiempo -> escala -> agencia -> operacion`

pero con menos sobreextensiones, menos cambios bruscos de nivel semantico y mejor trazabilidad entre capitulos.
