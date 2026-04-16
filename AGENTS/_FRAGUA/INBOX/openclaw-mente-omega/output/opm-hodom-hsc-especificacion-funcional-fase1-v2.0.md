# HODOM HSC
# Especificación Funcional — Fase I

Versión: 2.0
Fecha: 2026-04-09
Estado: especificación funcional inicial

Alcance de Fase I:
1. Plan de Atención
2. Estados del Episodio
3. Riesgo Clínico Operacional

Propósito: ofrecer una especificación funcional suficientemente concreta para implementación, sin entrar todavía a detalle técnico exhaustivo.

---

## 1. Objetivo funcional de la fase

Fase I debe hacer visible y operable la columna vertebral mínima del sistema.

Eso significa que, al terminar esta fase, cualquier episodio activo debe responder de forma simple a tres preguntas:

1. ¿Cuál es el plan vigente?
2. ¿En qué estado está este episodio?
3. ¿Qué prioridad clínica-operacional tiene hoy?

---

# 2. Módulo funcional 1 — Plan de Atención

## 2.1 Objetivo

Consolidar en una única superficie resumida la intención clínica vigente del episodio.

## 2.2 Alcance funcional mínimo

El sistema debe permitir visualizar por episodio activo un **Plan de Atención actual** con:
- objetivo clínico principal
- diagnóstico/problema principal
- prestaciones activas por disciplina
- frecuencia objetivo de atención
- criterios de monitoreo
- criterios de ajuste
- criterios de egreso
- fecha de actualización
- responsable o fuente clínica de actualización

## 2.3 Reglas funcionales

1. Cada episodio activo debe tener un plan visible.
2. El plan visible puede consolidarse desde fuentes existentes durante una primera etapa.
3. El plan debe pertenecer al episodio, no a una visita aislada.
4. El plan debe poder leerse sin necesidad de recorrer múltiples notas.
5. Si el plan no está completo, el sistema debe mostrarlo como incompleto o pendiente de consolidación.

## 2.4 Superficies donde debe aparecer

- ficha del episodio
- eventualmente censo resumido o preview contextual
- insumo para agenda/programación

## 2.5 Casos de uso clave

### CU-PLAN-01 — Ver plan actual
Como profesional,
quiero ver el plan actual del episodio,
para entender la intención clínica vigente.

### CU-PLAN-02 — Usar plan para coordinar
Como coordinación,
quiero usar el plan para orientar frecuencia y prioridad de visitas,
para programar con sentido clínico.

### CU-PLAN-03 — Auditar plan
Como Dirección Técnica,
quiero ver que cada episodio activo tenga un plan visible,
para reducir opacidad y variabilidad.

## 2.6 Criterios de aceptación

- el plan existe visualmente en ficha
- su lectura toma menos de 30 segundos
- se puede explicar el episodio con ese bloque y sin abrir 5 registros distintos
- el plan tiene vínculo explícito con el episodio

---

# 3. Módulo funcional 2 — Estados del Episodio

## 3.1 Objetivo

Establecer una semántica única del curso del episodio, visible y compartida por todas las superficies críticas.

## 3.2 Propuesta de estados

- postulado
- elegible
- admitido
- activo
- egresado
- cerrado

## 3.3 Reglas funcionales

1. Cada episodio debe tener un único estado canónico visible.
2. El estado canónico no reemplaza el estado clínico.
3. El estado canónico no equivale al tipo de egreso.
4. Las transiciones deben ser explícitas y válidas.
5. Las pantallas críticas no deben contradecirse entre sí.

## 3.4 Superficies donde debe aparecer

- admisión
- ficha
- censo
- egreso
- reporting relevante cuando aplique

## 3.5 Casos de uso clave

### CU-ESTADO-01 — Ver estado actual
Como usuario del sistema,
quiero ver el estado canónico del episodio,
para saber en qué punto del flujo está.

### CU-ESTADO-02 — Cambiar estado por evento válido
Como sistema o usuario autorizado,
quiero que un evento válido actualice el estado del episodio,
para mantener coherencia de proceso.

### CU-ESTADO-03 — Revisar coherencia de estados
Como referente de datos o coordinación,
quiero detectar episodios con estados incoherentes,
para corregir inconsistencias.

## 3.6 Criterios de aceptación

- estado visible en 4 superficies críticas
- el mismo episodio conserva coherencia entre pantallas
- las transiciones más comunes están definidas
- no se mezcla estado del episodio con tipo de egreso

---

# 4. Módulo funcional 3 — Riesgo Clínico Operacional

## 4.1 Objetivo

Generar una señal breve y compartida de priorización clínica-operacional por episodio.

## 4.2 Propuesta inicial de categorías

- estable
- en observación
- inestable

## 4.3 Reglas funcionales

1. Todo episodio activo debe poder tener una categoría de riesgo visible.
2. La categoría de riesgo debe ser entendible por clínica y coordinación.
3. El riesgo debe servir para priorización, no solo para descripción.
4. El riesgo debe tener consecuencia operativa mínima.
5. El riesgo no reemplaza el juicio clínico detallado.

## 4.4 Superficies donde debe aparecer

- censo
- ficha
- opcionalmente agenda y cockpit futuro

## 4.5 Casos de uso clave

### CU-RIESGO-01 — Ver riesgo en censo
Como coordinación,
quiero ver el riesgo del episodio en el censo,
para priorizar trabajo diario.

### CU-RIESGO-02 — Ver riesgo en ficha
Como profesional,
quiero ver el riesgo del episodio en ficha,
para compartir una lectura resumida de prioridad.

### CU-RIESGO-03 — Usar riesgo para priorizar
Como unidad,
quiero que el riesgo oriente seguimiento, visitas y escalamiento,
para traducir señal clínica a operación.

## 4.6 Criterios de aceptación

- riesgo visible en censo y ficha
- categorías comprendidas por usuarios clave
- existe regla mínima de uso operativo por categoría
- validación positiva sobre casos reales seleccionados

---

# 5. Requerimientos transversales

## 5.1 Requerimientos de consistencia

- plan, estado y riesgo deben pertenecer al mismo episodio
- no debe haber contradicción evidente entre esas tres capas
- los datos deben poder leerse sin navegación excesiva

## 5.2 Requerimientos de usabilidad

- lectura rápida
- mínima carga cognitiva
- integración con flujos existentes
- no duplicar innecesariamente registros ya visibles

## 5.3 Requerimientos de gobierno

- definiciones cerradas por Dirección Técnica + Coordinación + referente funcional
- cambios semánticos posteriores deben documentarse
- los 5 casos reales de validación se usan como baseline funcional

---

# 6. Fuera de alcance en esta fase

Quedan fuera por ahora:
- cockpit directivo completo
- comunicación clínica unificada completa
- seguimiento post-egreso completo
- integración profunda del portal
- automatizaciones avanzadas basadas en IA
- rediseño masivo de UI

---

# 7. Dependencias funcionales

## Dependencias previas
- glosario operativo mínimo
- selección de casos reales de validación
- decisiones semánticas fundacionales ya aceptadas

## Dependencias posteriores
Fase II dependerá críticamente de esta fase, porque:
- el cockpit necesita episodio/riesgo
- la comunicación unificada necesita mejor semántica base
- la capacidad operativa necesita lectura consistente del episodio

---

# 8. Criterio de cierre de Fase I

Fase I se considera funcionalmente lograda cuando:

1. el episodio tiene plan visible,
2. el episodio tiene estado canónico visible,
3. el episodio tiene riesgo visible,
4. las principales superficies ya no se contradicen semánticamente,
5. el equipo clínico y de coordinación puede usar estas tres piezas para explicar y conducir casos reales.

---

# 9. Veredicto funcional

La Fase I no busca complejidad.
Busca legibilidad operativa.

Su meta no es hacer el sistema más espectacular.
Su meta es hacer que el sistema piense y se deje pensar mejor.
