# HODOM HSC
# Fase I — Plan Táctico Ejecutable

Versión: 1.5
Fecha: 2026-04-09
Estado: plan táctico inicial

Base:
- `opm-hodom-hsc-roadmap-ejecutable-v1.4.md`
- `opm-hodom-hsc-backlog-arquitectonico-v1.3.md`
- `opm-hodom-hsc-canonico-local-v1.0.md`

Objetivo de Fase I:
construir la columna vertebral semántica mínima del sistema HODOM HSC.

Resultados esperados al cierre:
1. objeto fuerte **Plan de Atención**
2. **máquina de estados del episodio** explícita
3. **categoría de riesgo** visible y operativa

---

## 1. Principio táctico

Fase I no debe intentar resolver toda la complejidad del sistema.

Debe resolver tres ambigüedades fundacionales:
- qué plan gobierna el episodio,
- en qué estado está realmente el episodio,
- con qué prioridad clínica-operacional debe tratarse hoy.

Si eso no se endurece, las capas siguientes quedan montadas sobre semántica blanda.

---

## 2. Estructura del trabajo

La fase se organiza en 3 épicas:

- **EPICA-1** — Plan de Atención
- **EPICA-2** — Estados del Episodio
- **EPICA-3** — Riesgo Clínico Operacional

Y una cuarta épica transversal:

- **EPICA-0** — Alineación semántica y validación con casos reales

---

# 3. EPICA-0 — Alineación semántica y validación

## Objetivo
Cerrar definiciones mínimas antes de construir demasiado.

## Entregables
1. glosario operativo corto
2. definiciones v1 de:
   - plan,
   - episodio,
   - riesgo
3. set de 5 casos reales de validación
4. criterio de aceptación clínica para cada épica

## Tareas
- T0.1 redactar glosario base
- T0.2 seleccionar 5 episodios reales heterogéneos
- T0.3 validar definiciones con Dirección Técnica + Coordinación + clínicos clave
- T0.4 congelar vocabulario mínimo de Fase I

## Riesgo principal
Querer programar antes de cerrar lenguaje compartido.

## Responsable lógico
Dirección Técnica + Coordinación + referente funcional/sistema

---

# 4. EPICA-1 — Plan de Atención

## Objetivo
Crear un objeto canónico visible y gobernable que exprese la intención clínica vigente del episodio.

## Resultado concreto
Cada episodio activo debe tener un **Plan de Atención actual** legible, resumido y utilizable por clínica, coordinación y agenda.

## Componentes mínimos del Plan
1. objetivo clínico principal
2. diagnóstico/problema activo principal
3. prestaciones activas por disciplina
4. frecuencia objetivo de atención
5. criterios de monitoreo
6. criterios de ajuste
7. criterios de egreso
8. estado del plan
9. fecha de vigencia / última actualización

## Paquetes de trabajo

### WP-1A — Modelo semántico del plan
- definir campos mínimos
- decidir si será tabla nueva, vista consolidada o híbrido
- definir relación con nota clínica y plan de enfermería

### WP-1B — Modelo de datos
- diseñar persistencia mínima
- definir versionado básico
- definir relación con `stay_id`

### WP-1C — Superficie UI mínima
- bloque “Plan actual” en ficha
- lectura breve y orientada a acción
- visibilidad de última actualización

### WP-1D — Integración con agenda
- agenda debe poder leer frecuencia/prioridad desde el plan
- no necesariamente automatizar todo aún, pero sí conectar semánticamente

## Historias tácticas

### H1.1
Como profesional,
quiero ver el plan actual resumido en la ficha,
para no depender de múltiples notas dispersas.

### H1.2
Como coordinación,
quiero entender desde el plan por qué este episodio requiere cierta frecuencia o disciplina,
para programar con criterio.

### H1.3
Como Dirección Técnica,
quiero que exista una intención clínica visible y auditable por episodio,
para disminuir opacidad y variabilidad.

## Criterios de aceptación
- existe un objeto/estructura “plan actual” por episodio activo
- la ficha lo muestra de forma estable
- el equipo puede explicar un caso usando ese bloque sin abrir 5 registros distintos
- al menos 5 casos reales quedan bien representados por la estructura elegida

## Riesgos
- plan demasiado narrativo
- plan demasiado rígido
- duplicar lo que ya existe sin integrarlo bien

## Responsable lógico
referente clínico + producto/sistema + coordinación

---

# 5. EPICA-2 — Estados del Episodio

## Objetivo
Formalizar la máquina de estados del episodio para que admisión, censo, ficha, egreso y REM hablen el mismo idioma.

## Propuesta inicial de estados
- postulado
- elegible
- admitido
- activo
- egresado
- cerrado
- seguido (opcional posterior)

## Resultado concreto
Toda superficie crítica debe mostrar un estado canónico coherente del episodio.

## Paquetes de trabajo

### WP-2A — Modelo de estados
- definir estados canónicos
- definir transiciones válidas
- definir eventos que disparan transición

### WP-2B — Mapeo con estado actual del sistema
- mapear `clinical.estadia.estado`
- mapear `tipo_egreso`
- mapear postulaciones y flujos previos a admisión

### WP-2C — Exposición UI
- mostrar estado canónico en admisión
- mostrar estado canónico en ficha
- mostrar estado canónico en censo
- mostrar estado canónico en egreso

### WP-2D — Consistencia reporting
- asegurar que REM y resumen mensual no contradigan el estado canónico

## Historias tácticas

### H2.1
Como sistema,
quiero que un episodio tenga un único estado canónico,
para evitar contradicciones entre módulos.

### H2.2
Como coordinación,
quiero distinguir claramente postulado, admitido, activo y egresado,
para ordenar trabajo y capacidad.

### H2.3
Como estadístico/referente REM,
quiero que el estado del episodio sea consistente con producción y egreso,
para no corregir manualmente datos ambiguos.

## Criterios de aceptación
- estados definidos y documentados
- reglas de transición explícitas
- al menos 4 superficies muestran el estado canónico
- casos reales no generan contradicción evidente entre estado clínico y administrativo

## Riesgos
- meter demasiados estados prematuramente
- mezclar estado clínico con estado administrativo
- no definir responsable de transición

## Responsable lógico
producto/sistema + coordinación + referente de datos/reporting

---

# 6. EPICA-3 — Riesgo Clínico Operacional

## Objetivo
Introducir una categoría de riesgo simple y útil para priorización clínica y coordinación territorial.

## Propuesta inicial
- estable
- en observación
- inestable

## Resultado concreto
El sistema debe permitir ver rápidamente qué episodios requieren mayor atención hoy.

## Paquetes de trabajo

### WP-3A — Definición clínica mínima
- acordar qué significa cada categoría
- acordar disparadores mínimos de cambio

### WP-3B — Modelo de datos
- decidir dónde vive el riesgo
- definir actualización manual, automática o híbrida

### WP-3C — Exposición UI
- riesgo visible en censo
- riesgo visible en ficha
- riesgo utilizable por agenda/coordinación

### WP-3D — Regla operativa
- definir qué cambia cuando un episodio es `inestable`
- escalamiento sugerido, contacto, prioridad de visita, revisión directiva si aplica

## Historias tácticas

### H3.1
Como coordinación,
quiero ver el riesgo de cada episodio en el censo,
para priorizar visitas y seguimiento.

### H3.2
Como profesional,
quiero que el riesgo sea una señal breve y compartida,
para disminuir variabilidad interpretativa.

### H3.3
Como Dirección Técnica,
quiero poder detectar episodios inestables rápidamente,
para supervisar continuidad y seguridad.

## Criterios de aceptación
- las 3 categorías están definidas y entendidas por el equipo
- el riesgo es visible al menos en ficha y censo
- existe regla operativa mínima asociada a cada categoría
- validación positiva con casos reales seleccionados

## Riesgos
- sobrecomplicar la escala
- confundir riesgo con gravedad médica pura
- no vincular riesgo a acción concreta

## Responsable lógico
referente clínico + coordinación + producto/sistema

---

# 7. Dependencias entre épicas

## Dependencia principal
EPICA-0 precede lógicamente a todas.

## Dependencias funcionales
- EPICA-1 y EPICA-2 pueden avanzar en paralelo
- EPICA-3 puede arrancar en paralelo, pero gana mucho con EPICA-2 ya más clara
- integración agenda/plan se apoya en EPICA-1
- consistencia reporting se apoya en EPICA-2

---

# 8. Secuencia sugerida de ejecución

## Semana 1
- cerrar glosario y casos reales
- bosquejo del objeto plan
- bosquejo de estados canónicos
- bosquejo de categorías de riesgo

## Semana 2
- decisión semántica final Fase I
- diseño de datos mínimo
- prototipos UI mínimos (bloque plan, estado, riesgo)

## Semana 3
- implementación de plan visible
- implementación de estado canónico visible
- implementación de riesgo visible

## Semana 4
- validación con casos reales
- corrección de inconsistencias
- revisión de impacto operativo inicial

## Semanas 5-6 opcionales
- endurecimiento de integración con agenda
- endurecimiento con reporting
- limpieza de naming y reglas de transición

---

# 9. Métricas de ejecución

## Métricas de entrega
- % historias de Fase I implementadas
- % superficies críticas con estado canónico visible
- % episodios activos con plan visible
- % episodios activos con riesgo visible

## Métricas de adopción
- uso del bloque plan en revisión clínica
- uso del estado canónico en coordinación
- uso del riesgo en priorización diaria

## Métricas de calidad
- número de contradicciones detectadas entre módulos
- número de episodios sin semántica mínima completa
- retrabajo manual necesario para explicar un episodio

---

# 10. Señales de éxito real

Fase I estará bien hecha si ocurre esto en la práctica:

1. el equipo deja de hablar del episodio de forma dispersa
2. coordinación puede explicar por qué un episodio está así, qué plan tiene y qué riesgo porta
3. ficha, censo y admisión dejan de contradecirse semánticamente
4. el sistema se vuelve más inteligible sin haberse vuelto más pesado

---

# 11. Veredicto táctico

Fase I no es glamorosa, pero es probablemente la fase más decisiva.

Porque aquí no se está agregando una capa decorativa al software.
Se está definiendo el esqueleto con el que el sistema va a pensar su propia operación.
