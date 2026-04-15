---
_manifest:
  urn: urn:fxsl:kb:opm-es-p05
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
    shard_index: 5
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opm-es
---

# OPM — Núcleo conceptual - Parte 05

## Notas para implementadores de herramientas

Las siguientes notas informativas del estándar están dirigidas a quienes desarrollan herramientas compatibles con OPM:

- Una herramienta puede rastrear el conjunto de refinadores de cada refinable y ajustar automáticamente el símbolo gráfico y las oraciones OPL correspondientes cuando quien modela cambia la colección de refinadores.
- Una herramienta puede ofrecer la opción de especificar la esencia primaria del sistema como medio para establecer el valor por defecto del atributo genérico de esencia.
- Una herramienta puede notificar a quien modela cuando se intenta incluir un objeto como refinador en más de un contexto, para que determine la pertinencia de la inclusión.
- Una herramienta puede establecer una sintaxis por defecto para resolver nombres de refinadores ambiguos.
- El OPL correspondiente a un OPD debe expresar solo los estados de los objetos tal como aparecen en ese OPD; la unión de estados de un objeto a través de todos los OPDs constituye el conjunto completo de estados de ese objeto.
- Cuando un enlace de evento desde un objeto o estado sistémico cruza el límite de un proceso descompuesto para iniciar un subproceso, la herramienta debería advertir que esto puede interferir con el orden temporal prescrito de la descomposición síncrona. Si el evento proviene de un objeto ambiental, la herramienta debería guiar a quien modela para definir cómo manejar la contingencia.
- Las herramientas de modelado OPM necesitan rastrear el número e identidades de las instancias operacionales de cada objeto y de cada proceso para poder realizar simulaciones.
