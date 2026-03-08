---
_manifest:
  urn: "urn:fxsl:skill:opm-specialist-example-builder:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Construir ejemplos OPM completos que ilustren conceptos, tipos de enlaces, patrones de modelado y tipos de sistemas, generando OPL textual equivalente.

## Input/Output

- **Input:** sistema a ejemplificar (string) O concepto a ilustrar (string)
- **Output:** ejemplo OPM completo con identificacion de elementos + OPL textual

## Procedimiento

1. DETERMINAR tipo de ejemplo:
   a. Sistema completo (SD) — si usuario pide modelar algo
   b. Concepto aislado — si usuario pide ilustrar un tipo de enlace, entidad o mecanismo
2. IDENTIFICAR elementos del ejemplo:
   - **Objetos**: fisicos (sombreado) vs informaticos (plano), con estados si aplica
   - **Procesos**: sincronos vs asincronos, con subprocesos si aplica
   - **Enlaces**: clasificar cada relacion (transformacion, estructural, habilitacion)
3. GENERAR OPL textual siguiendo grammar OPM:
   - Consumo: "_Processing_ consumes **Consumee**"
   - Resultado: "_Processing_ yields **Resultee**"
   - Efecto: "_Processing_ affects **Affectee**"
   - Cambio estado: "_Processing_ changes **Object** from `input-state` to `output-state`"
   - Agente: "**Agent** handles _Processing_"
   - Instrumento: "_Processing_ requires **Instrument**"
   - Agregacion: "**Whole** consists of **Part1**, **Part2** and **Part3**"
   - Exhibicion: "**Exhibitor** exhibits **Attribute**"
   - Especializacion: "**Specialization** is a **General**"
4. PRESENTAR ejemplo estructurado:
   a. Contexto del sistema
   b. Tabla de elementos (tipo, nombre, fisico/informatico, estados)
   c. Tabla de enlaces (tipo, origen, destino, OPL)
   d. OPL completo del SD
5. SI sistema completo → incluir los 5 componentes del SD (proposito, funcion, habilitadores, entorno, problema)

## Signature Output

Ejemplo en Markdown: contexto + tabla elementos + tabla enlaces + OPL completo.
