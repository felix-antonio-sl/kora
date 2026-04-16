# HODOM HSC
# ADRs Técnicos — Implementación Fase I

Versión: 2.7
Fecha: 2026-04-09
Estado: set técnico inicial

Propósito: fijar decisiones técnicas de implementación para Fase I y evitar deriva durante ejecución.

Base:
- `opm-hodom-hsc-contratos-datos-fase1-v2.5.md`
- `opm-hodom-hsc-mapa-impacto-pantallas-fase1-v2.6.md`
- `opm-hodom-hsc-arquitectura-implementacion-fase1-v2.3.md`

---

# ADR-T01 — Fase I se implementa con capa semántica nueva y mínima, no con refactor masivo

## Estado
Aceptado

## Contexto
El sistema actual ya tiene piezas valiosas y funcionales. Un refactor amplio de BD o frontend al inicio aumentaría riesgo y retrasaría aprendizaje.

## Decisión
Fase I se implementará agregando una capa semántica mínima, compuesta por vistas y estructuras livianas nuevas, consumidas primero por pantallas de alto valor.

## Consecuencias
### Positivas
- menor riesgo de ruptura
- time-to-value más corto
- aprendizaje temprano con casos reales

### Costos
- convivencia temporal entre semántica vieja y nueva
- necesidad de disciplina para no duplicar lógica

---

# ADR-T02 — El estado canónico del episodio se entrega primero como vista, no como tabla nueva

## Estado
Aceptado

## Contexto
El estado del episodio ya está insinuado por campos existentes (`estado`, `tipo_egreso`, postulaciones). Antes de persistir un nuevo estado, conviene observar si una vista canónica resuelve el problema.

## Decisión
Crear primero:

`clinical.v_estado_episodio_canonico`

como fuente principal de lectura del estado canónico.

## Consecuencias
### Positivas
- implementación rápida
- menos fricción con datos existentes
- facilita validación con casos reales

### Costos
- lógica de mapeo puede complejizarse
- si el sistema evoluciona, podría necesitar persistencia posterior

---

# ADR-T03 — El riesgo operacional se implementa con estructura liviana y trazable

## Estado
Aceptado

## Contexto
El riesgo requiere responsable, motivo y timestamp. Una vista puramente derivada podría ser demasiado débil en la primera iteración.

## Decisión
Implementar el riesgo mediante una estructura liviana por episodio vigente, con trazabilidad mínima, y exponerla vía vista actual si conviene.

## Consecuencias
### Positivas
- mejor trazabilidad
- mejor uso por coordinación y clínica
- más fácil revisar con casos reales

### Costos
- requiere pequeña persistencia adicional
- exige disciplina de actualización

---

# ADR-T04 — El Plan de Atención parte como consolidación operativa, no como modelo profundamente normalizado

## Estado
Aceptado

## Contexto
El significado del plan todavía se está cerrando con operación real. Normalizarlo de entrada sería prematuro.

## Decisión
El Plan de Atención comenzará como vista consolidada o estructura híbrida de lectura operativa, con posibilidad de evolucionar luego a tabla rica.

## Consecuencias
### Positivas
- acelera entrega
- reduce sobreingeniería
- permite aprender con casos reales

### Costos
- menor pureza inicial del modelo de datos
- potencial deuda técnica si no se revisa después

---

# ADR-T05 — La ficha es la primera superficie de consumo de la nueva semántica

## Estado
Aceptado

## Contexto
La ficha ya es la superficie con mayor densidad clínica y mejor punto de integración por episodio.

## Decisión
La primera pantalla intervenida será:
- `ficha/[stayId]`

consumiendo:
- estado canónico
- plan actual
- riesgo actual

## Consecuencias
### Positivas
- máximo valor clínico temprano
- mejor campo de prueba para semántica nueva

### Costos
- la ficha puede sobrecargarse si no se diseña con cuidado

---

# ADR-T06 — El censo es la segunda superficie prioritaria por su valor coordinativo

## Estado
Aceptado

## Contexto
El censo ya funciona como tablero de coordinación. Estado y riesgo le aportarían valor inmediato.

## Decisión
La segunda pantalla intervenida será:
- `censo`

mostrando:
- estado canónico
- riesgo actual

## Consecuencias
### Positivas
- mayor retorno operativo
- mejora rápida para coordinación

### Costos
- riesgo de sobrecargar tabla si diseño visual es pobre

---

# ADR-T07 — La lógica semántica no debe enterrarse en frontend página por página

## Estado
Aceptado

## Contexto
Si cada pantalla calcula su propio canon de plan/estado/riesgo, aparecerán inconsistencias.

## Decisión
La lógica semántica principal debe vivir en:
- vistas SQL,
- helpers compartidos,
- o capa de consolidación común,

pero no replicarse libremente en cada page.tsx.

## Consecuencias
### Positivas
- consistencia transversal
- menor deuda de frontend

### Costos
- mayor disciplina en backend/datos

---

# ADR-T08 — Agenda recibe semántica nueva solo de forma liviana en Fase I

## Estado
Aceptado

## Contexto
Agenda es crítica, pero no debe convertirse en el lugar donde se estabiliza semántica aún inmadura.

## Decisión
En Fase I, agenda solo consumirá señales mínimas si ya están consolidadas en ficha y censo.

## Consecuencias
### Positivas
- menor riesgo de ruido operacional
- foco en pantallas de mayor claridad semántica

### Costos
- agenda no capturará todo el valor potencial todavía

---

## Cierre

Estos ADRs técnicos sostienen una estrategia clara:

**Fase I debe implementarse con mínima invasión, máxima claridad semántica y validación temprana con casos reales.**
