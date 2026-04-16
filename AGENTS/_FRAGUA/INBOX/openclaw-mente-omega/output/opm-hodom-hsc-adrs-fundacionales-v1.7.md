# HODOM HSC
# ADRs Fundacionales — Fase I

Versión: 1.7
Fecha: 2026-04-09
Estado: set inicial de decisiones arquitectónicas

Propósito: fijar las decisiones fundacionales de Fase I para evitar deriva semántica y técnica.

---

# ADR-001 — El sistema se organiza alrededor del Episodio, no del Paciente aislado

## Estado
Aceptado

## Contexto
La normativa habla muchas veces en clave de paciente. Pero la operación HSC, la ficha longitudinal, el `stay_id`, la admisión, la agenda, el egreso y el REM se comportan de hecho como procesos centrados en una estadía/episodio.

## Decisión
La unidad canónica de operación, coordinación, seguimiento, egreso y observabilidad será el:

**Episodio de Hospitalización Domiciliaria**

El paciente sigue siendo entidad clínica fundamental, pero no será la unidad primaria de proceso.

## Consecuencias
### Positivas
- ordena admisión, ficha, agenda, llamadas, egreso y REM bajo un mismo eje
- reduce ambigüedad entre historia longitudinal del paciente y situación actual de atención
- mejora trazabilidad end-to-end

### Costos
- obliga a explicitar mejor estados del episodio
- obliga a mapear campos actuales y corregir inconsistencias históricas

## Implicancias de diseño
- `stay_id` o equivalente se trata como identificador canónico de proceso
- las comunicaciones relevantes deben vincularse al episodio
- el plan actual debe pertenecer al episodio
- el riesgo debe pertenecer al episodio

---

# ADR-002 — Debe existir un objeto fuerte llamado Plan de Atención

## Estado
Aceptado

## Contexto
Hoy la intención clínica parece repartida entre notas, indicaciones, plan de enfermería, frecuencia de visitas y agenda. Eso debilita coordinación y trazabilidad.

## Decisión
Se creará o consolidará un objeto canónico:

**Plan de Atención**

Este objeto será la representación vigente y resumida de la intención clínica-operacional del episodio.

## Contenido mínimo
- objetivo clínico principal
- problema/diagnóstico activo principal
- prestaciones activas por disciplina
- frecuencia objetivo
- criterios de monitoreo
- criterios de ajuste
- criterios de egreso
- vigencia / última actualización

## Consecuencias
### Positivas
- conecta clínica con agenda
- mejora legibilidad para coordinación
- mejora auditabilidad clínica y directiva

### Costos
- obliga a decidir relación con objetos existentes
- puede requerir tabla nueva, vista o agregación híbrida

## Alternativas descartadas
1. seguir coordinándose solo por notas narrativas
2. hacer que agenda sea la representación implícita del plan
3. dividir el plan por disciplina sin objeto integrador

---

# ADR-003 — El episodio debe tener una máquina de estados canónica

## Estado
Aceptado

## Contexto
El sistema ya usa estados y tipos de egreso, pero la semántica parece dispersa entre módulos.

## Decisión
Se definirá una máquina de estados canónica del episodio.

## Propuesta inicial
- postulado
- elegible
- admitido
- activo
- egresado
- cerrado

## Consecuencias
### Positivas
- coherencia entre admisión, censo, ficha, egreso y reporting
- menor ambigüedad operativa
- mejor base para automatización futura

### Costos
- habrá que mapear realidad actual y resolver zonas grises
- puede exponer deuda histórica en datos

## Regla clave
No confundir:
- estado del episodio,
- estado clínico,
- tipo de egreso.

Son cosas distintas.

---

# ADR-004 — El riesgo clínico debe representarse como señal operacional explícita

## Estado
Aceptado

## Contexto
Hay signos vitales, alertas y juicios clínicos, pero no una categoría breve y compartida de riesgo que sirva para coordinación.

## Decisión
Se introducirá una categoría de riesgo operacional explícita por episodio.

## Propuesta inicial
- estable
- en observación
- inestable

## Propósito
No reemplazar juicio clínico fino, sino producir una señal compacta de priorización para operación diaria.

## Consecuencias
### Positivas
- mejora priorización de visitas y seguimiento
- conecta monitoreo con agenda y escalamiento
- mejora supervisión directiva

### Costos
- requiere acuerdo clínico mínimo
- requiere disciplina de actualización

## Alternativas descartadas
1. inferir riesgo solo desde alertas aisladas
2. dejar riesgo completamente implícito en narrativa clínica

---

# ADR-005 — La agenda y la ruta son parte del cuidado, no solo logística

## Estado
Aceptado

## Contexto
En HODOM, una visita no ocurre en abstracto. Debe territorializarse. La app ya tiene agenda, rutas, conflictos y cobertura comunal.

## Decisión
Agenda y ruta se modelan como componentes estructurales del sistema asistencial-operativo, no como mera capa administrativa.

## Consecuencias
### Positivas
- alinea clínica con territorio
- legitima el peso arquitectónico de `agenda/`
- mejora decisiones sobre capacidad y continuidad

### Costos
- obliga a integrar mejor plan, riesgo y agenda

---

# ADR-006 — La regulación a distancia es acto clínico posible, no canal accesorio

## Estado
Aceptado

## Contexto
La normativa habilita atención remota con alcance clínico y exige trazabilidad telefónica. La app ya tiene módulo de llamadas maduro.

## Decisión
La atención a distancia se tratará como macroproceso clínico-regulatorio explícito.

## Consecuencias
### Positivas
- da peso correcto a llamadas y regulación
- mejora trazabilidad de decisiones remotas
- prepara el terreno para subdominio de comunicación clínica

### Costos
- exige distinguir mejor comunicación administrativa vs clínica

---

# ADR-007 — El REM y la producción son parte constitutiva del sistema, no apéndice administrativo

## Estado
Aceptado

## Contexto
El sistema HSC ya tiene reporting, funciones REM, ocupación y edición de cupos.

## Decisión
La producción y el REM se modelarán como salida constitutiva del sistema y, progresivamente, como parte de la capa de gobernanza.

## Consecuencias
### Positivas
- fortalece visión directiva
- evita subestimar datos de operación
- permite cerrar el ciclo episodio → producción

### Costos
- obliga a cuidar consistencia semántica entre clínica y reporting

---

# ADR-008 — La HODOM HSC exhibe doble función: asistir y gobernarse

## Estado
Aceptado

## Contexto
El trabajo previo muestra que la unidad no solo cuida pacientes. También necesita sostener capacidad, calidad, protocolos, consistencia y observabilidad.

## Decisión
El sistema local exhibe dos macrofunciones:
- *Hospitalizar en Domicilio*
- *Gobernar Sistema HODOM HSC*

## Consecuencias
### Positivas
- separa mejor lo asistencial de lo directivo
- permite construir SD1 y SD3 con mayor limpieza
- mejora lectura de roles de Dirección Técnica y Coordinación

### Costos
- incrementa complejidad conceptual inicial
- requiere disciplina para no mezclar capas en cada discusión

---

## Cierre

Estos ADRs no son accesorios. Son el set mínimo de decisiones que impide que la evolución del sistema se fragmente en implementaciones localmente razonables pero globalmente incoherentes.
