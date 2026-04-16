# HODOM HSC
# Fase I — Paquetes de Trabajo Ejecutables

Versión: 1.6
Fecha: 2026-04-09
Estado: desglose operativo inicial

Base:
- `opm-hodom-hsc-fase1-plan-tactico-v1.5.md`

Objetivo: traducir las épicas de Fase I a paquetes de trabajo ejecutables, suficientemente concretos para planificación de producto, datos y operación.

---

## 1. Estructura de paquetes

Cada paquete incluye:
- propósito
- entregable
- tipo de trabajo
- dependencias
- riesgo principal
- definición de terminado

---

# 2. Paquetes transversales

## PT-01 — Glosario operativo mínimo

### Propósito
Alinear lenguaje entre clínica, coordinación, datos y producto.

### Entregable
Documento corto con definiciones de:
- episodio
- plan
- estado del episodio
- riesgo
- cierre clínico
- cierre estadístico

### Tipo de trabajo
proceso / gobierno

### Dependencias
ninguna

### Riesgo principal
quedar demasiado abstracto o demasiado largo

### Definición de terminado
- 1 documento breve
- validado por núcleo decisor
- usado como referencia en Fase I

---

## PT-02 — Set de casos reales de validación

### Propósito
No diseñar en abstracto.

### Entregable
5 episodios reales representativos:
- uno simple y estable
- uno de alta carga de enfermería
- uno con alta incertidumbre o riesgo
- uno con llamada/escalamiento relevante
- uno con egreso complejo o reingreso

### Tipo de trabajo
proceso / validación

### Dependencias
ninguna

### Riesgo principal
elegir casos demasiado homogéneos

### Definición de terminado
- 5 casos seleccionados
- con datos suficientes para probar plan, estado y riesgo

---

# 3. Paquetes EPICA-1 — Plan de Atención

## P1-01 — Diseño semántico del Plan de Atención

### Propósito
Definir la forma mínima del objeto plan.

### Entregable
Especificación v1 del Plan de Atención con campos obligatorios y opcionales.

### Tipo de trabajo
modelo / proceso

### Dependencias
PT-01, PT-02

### Riesgo principal
querer representar todo desde el primer diseño

### Definición de terminado
- campos mínimos definidos
- relación con notas/indicaciones aclarada
- ejemplos cargados con casos reales

---

## P1-02 — Diseño de persistencia del Plan

### Propósito
Resolver dónde y cómo vive el plan.

### Entregable
Decisión de persistencia:
- tabla nueva,
- vista materializada,
- agregación calculada,
- o híbrido.

### Tipo de trabajo
datos / arquitectura

### Dependencias
P1-01

### Riesgo principal
generar duplicación inconsistente con notas existentes

### Definición de terminado
- decisión tomada
- esquema o contrato de vista definido
- relación con `stay_id` explícita

---

## P1-03 — UI del bloque “Plan actual”

### Propósito
Hacer visible el objeto plan en la operación diaria.

### Entregable
Bloque en ficha con resumen del plan actual.

### Tipo de trabajo
software / UX

### Dependencias
P1-01, idealmente P1-02

### Riesgo principal
mostrar una caja bonita pero semánticamente vacía

### Definición de terminado
- renderiza datos reales
- visible en ficha del episodio
- entendible en menos de 30 segundos por un usuario clínico

---

## P1-04 — Integración plan ↔ agenda

### Propósito
Conectar intención clínica con programación territorial.

### Entregable
Regla o vista que permita leer prioridad/frecuencia desde el plan para agenda.

### Tipo de trabajo
datos / integración

### Dependencias
P1-02, P3-01 opcional

### Riesgo principal
sobrediseñar automatización antes de cerrar semántica

### Definición de terminado
- agenda puede consumir al menos una señal del plan
- existe trazabilidad mínima entre plan y visita

---

# 4. Paquetes EPICA-2 — Estados del Episodio

## P2-01 — Diseño de máquina de estados

### Propósito
Definir estados y transiciones válidas.

### Entregable
Diagrama/tabla de estados del episodio.

### Tipo de trabajo
modelo / proceso

### Dependencias
PT-01, PT-02

### Riesgo principal
confundir estado clínico con administrativo

### Definición de terminado
- estados definidos
- eventos de transición definidos
- responsables lógicos de transición identificados

---

## P2-02 — Mapeo con datos actuales

### Propósito
Alinear canon con realidad actual de BD.

### Entregable
Mapa entre estados canónicos y campos actuales (`estado`, `tipo_egreso`, postulaciones, etc.).

### Tipo de trabajo
datos / análisis

### Dependencias
P2-01

### Riesgo principal
descubrir que hay más ambigüedad histórica de la esperada

### Definición de terminado
- matriz de mapeo publicada
- casos no mapeables listados explícitamente

---

## P2-03 — Exposición UI del estado canónico

### Propósito
Hacer operativo el estado del episodio.

### Entregable
Estado canónico visible en:
- admisión
- ficha
- censo
- egreso

### Tipo de trabajo
software / UX

### Dependencias
P2-02

### Riesgo principal
mostrar el estado sin resolver antes su consistencia real

### Definición de terminado
- aparece en las 4 superficies críticas
- el mismo episodio no se contradice entre pantallas

---

## P2-04 — Consistencia reporting ↔ episodio

### Propósito
Evitar que el episodio semántico y la producción estadística hablen idiomas distintos.

### Entregable
Reglas de coherencia mínimas entre estado del episodio y reporting.

### Tipo de trabajo
datos / reporting

### Dependencias
P2-02

### Riesgo principal
descubrir deuda histórica en datos que no cabe “parchar” sin limpieza

### Definición de terminado
- reglas documentadas
- chequeos básicos definidos

---

# 5. Paquetes EPICA-3 — Riesgo Clínico Operacional

## P3-01 — Definición mínima de riesgo

### Propósito
Cerrar la semántica del riesgo con utilidad real.

### Entregable
Definición v1 de:
- estable
- en observación
- inestable

### Tipo de trabajo
proceso / clínica

### Dependencias
PT-01, PT-02

### Riesgo principal
definiciones demasiado vagas o demasiado complejas

### Definición de terminado
- categorías cerradas
- ejemplos de uso por caso real
- consecuencias operativas mínimas por categoría

---

## P3-02 — Persistencia del riesgo

### Propósito
Resolver dónde vive el riesgo y cómo se actualiza.

### Entregable
Modelo de datos o cálculo para riesgo por episodio.

### Tipo de trabajo
datos / arquitectura

### Dependencias
P3-01

### Riesgo principal
hacerlo totalmente manual o totalmente automático demasiado pronto

### Definición de terminado
- fuente de verdad definida
- política de actualización definida

---

## P3-03 — UI de riesgo

### Propósito
Volver visible el riesgo para priorización diaria.

### Entregable
Riesgo visible en:
- censo
- ficha
- opcionalmente agenda

### Tipo de trabajo
software / UX

### Dependencias
P3-02

### Riesgo principal
mostrar riesgo sin acción asociada

### Definición de terminado
- riesgo visible
- colores/etiquetas consistentes
- lectura clara para coordinación

---

## P3-04 — Regla operativa de escalamiento

### Propósito
Asegurar que el riesgo afecte realmente la operación.

### Entregable
Regla mínima de priorización y escalamiento por categoría de riesgo.

### Tipo de trabajo
proceso / gobierno

### Dependencias
P3-01

### Riesgo principal
no traducir riesgo a acción concreta

### Definición de terminado
- protocolo breve definido
- coordinación sabe qué hacer con cada categoría

---

# 6. Paquetes de consolidación

## PC-01 — Revisión integrada con casos reales

### Propósito
Probar Fase I como sistema, no como piezas aisladas.

### Entregable
Revisión de 5 casos usando:
- plan
- estado
- riesgo

### Tipo de trabajo
validación / proceso

### Dependencias
P1-03, P2-03, P3-03

### Riesgo principal
que cada componente funcione solo pero no juntos

### Definición de terminado
- 5 casos revisados
- issues detectados listados
- correcciones priorizadas

---

## PC-02 — Cierre semántico de Fase I

### Propósito
Declarar estable la columna vertebral mínima.

### Entregable
Acta o documento de cierre de Fase I.

### Tipo de trabajo
gobierno

### Dependencias
PC-01

### Riesgo principal
declarar cierre prematuro

### Definición de terminado
- criterios de Fase I cumplidos o gaps residuales explícitos
- base lista para Fase II

---

# 7. Orden recomendado de ejecución

## Orden corto
1. PT-01
2. PT-02
3. P1-01
4. P2-01
5. P3-01
6. P1-02
7. P2-02
8. P3-02
9. P1-03
10. P2-03
11. P3-03
12. P3-04
13. P1-04
14. P2-04
15. PC-01
16. PC-02

---

# 8. Señales de mala ejecución

Fase I va mal si pasa alguna de estas cosas:
- se implementa UI antes de cerrar semántica
- cada equipo usa definiciones distintas
- plan, estado y riesgo existen pero no se usan en coordinación real
- reporting sigue contradiciendo el estado del episodio
- no se prueban casos reales hasta demasiado tarde

---

# 9. Veredicto operativo

Este desglose muestra algo útil:

Fase I no necesita un gran programa de transformación imposible.
Necesita una secuencia disciplinada de paquetes relativamente concretos.

Lo difícil no es tanto programarlos.
Lo difícil es no perder rigor semántico mientras se programan.
