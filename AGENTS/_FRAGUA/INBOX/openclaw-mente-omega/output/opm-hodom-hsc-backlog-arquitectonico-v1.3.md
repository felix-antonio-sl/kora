# HODOM HSC
# Backlog Arquitectónico Priorizado

Versión: 1.3
Fecha: 2026-04-09
Estado: backlog estratégico inicial

Base de trabajo:
- `opm-hodom-hsc-canonico-local-v1.0.md`
- `opm-hodom-hsc-matriz-proceso-modulo-datos-v1.1.md`
- `opm-hodom-hsc-gap-analysis-v1.2.md`

Objetivo: convertir el análisis ontológico y procesual en una secuencia de evolución realista para software, datos y operación.

---

## 1. Criterio de priorización

Cada iniciativa se evalúa por:
- **Impacto clínico-operacional**
- **Impacto directivo**
- **Dependencia estructural**
- **Complejidad**
- **Tiempo a valor**

Escalas:
- Impacto: alto / medio / bajo
- Complejidad: alta / media / baja
- Horizonte: quick win / trimestre / estructural

---

## 2. Las 3 iniciativas fundacionales

## A1. Objeto fuerte de Plan de Atención

### Problema
El sistema parece coordinarse hoy por fragmentos de plan, no por un objeto plan suficientemente unificado.

### Qué crear
Un objeto canónico **Plan de Atención** que articule:
- objetivo clínico principal
- problemas/condiciones activas
- prestaciones activas por disciplina
- frecuencia objetivo
- criterios de monitoreo
- criterios de ajuste
- criterios de egreso
- vigencia / versión

### Impacto
- clínico-operacional: **alto**
- directivo: **alto**
- complejidad: **media-alta**
- horizonte: **estructural**

### Procesos impactados
- *Planificar Atención Interdisciplinaria*
- *Programar Visitas y Rutas*
- *Ejecutar Atención Domiciliaria*
- *Monitorear Evolución Clínica*
- *Egresar Episodio*

### Dependencias
Ninguna mayor. Esta iniciativa, de hecho, ordena muchas otras.

### Entregables mínimos
1. modelo semántico del objeto
2. tabla o vista unificada
3. UI de lectura del plan en ficha
4. versionado básico del plan
5. vínculo agenda ↔ plan

---

## A2. Cockpit directivo HODOM

### Problema
La información de gestión existe, pero está dispersa.

### Qué crear
Una superficie integrada para Dirección Técnica y Coordinación con:
- cupos y ocupación
- pacientes sin visita / riesgo de continuidad
- alertas críticas
- llamadas clínicas relevantes
- reingresos / fallecidos / egresos pendientes
- consistencia REM
- presión territorial por comuna/zona/profesional

### Impacto
- clínico-operacional: **alto**
- directivo: **muy alto**
- complejidad: **media**
- horizonte: **trimestre**

### Procesos impactados
- *Gestionar Capacidad y Continuidad Operativa*
- *Auditar Calidad y Seguridad*
- *Validar Observabilidad y REM*

### Dependencias
Idealmente apoyarse en A1, pero puede arrancar en paralelo con los datos actuales.

### Entregables mínimos
1. dashboard directivo único
2. indicadores priorizados
3. vistas de excepción y riesgo
4. drill-down por episodio

---

## A3. Subdominio unificado de Comunicación Clínica

### Problema
Llamadas, portal, coordinación y mensajes viven fragmentados.

### Qué crear
Un subdominio **Comunicación Clínica** con un objeto/evento central:
- tipo de comunicación
- canal
- emisor/receptor
- motivo
- prioridad
- decisión
- escalamiento
- vínculo a episodio
- trazabilidad temporal

### Impacto
- clínico-operacional: **alto**
- directivo: **medio-alto**
- complejidad: **media**
- horizonte: **trimestre**

### Procesos impactados
- *Regular Atención a Distancia*
- *Gestionar Comunicación Clínica*
- *Auditar Calidad y Seguridad*

### Dependencias
Convive bien con A2. Puede implementarse incrementalmente partiendo por llamadas.

### Entregables mínimos
1. modelo canónico de evento de comunicación
2. mapeo llamadas ↔ portal ↔ ficha
3. bandeja unificada o al menos indexada por episodio
4. reglas de escalamiento

---

## 3. Iniciativas de segundo nivel

## B1. Máquina de estados del episodio

### Problema
El episodio existe, pero sus estados no parecen estar explícitamente gobernados como máquina canónica.

### Qué crear
Estados mínimos:
- postulado
- elegible
- admitido
- activo
- egresado
- cerrado
- seguido (si aplica)

### Impacto
- clínico-operacional: **alto**
- directivo: **alto**
- complejidad: **media**
- horizonte: **trimestre**

### Dependencias
Muy recomendable después o junto con A1.

---

## B2. Seguimiento post-egreso explícito

### Problema
Proceso importante, pero con poca encarnación visible.

### Qué crear
Workflow post-egreso con:
- llamada programada
- contrarreferencia APS
- validación de continuidad
- desenlace temprano
- detección de reconsulta/reingreso

### Impacto
- clínico-operacional: **medio-alto**
- directivo: **medio**
- complejidad: **media**
- horizonte: **trimestre**

### Dependencias
Se beneficia de A3.

---

## B3. Categorización de riesgo explícita

### Problema
Hay alertas y signos, pero el riesgo no parece estabilizado como objeto fuerte.

### Qué crear
Clasificación simple y operativa:
- estable
- observación
- inestable

Con efecto sobre:
- agenda
- escalamiento
- cupos
- monitoreo

### Impacto
- clínico-operacional: **alto**
- directivo: **medio**
- complejidad: **media-baja**
- horizonte: **quick win / trimestre**

### Dependencias
Puede empezar antes de A1, pero se fortalece si A1 existe.

---

## B4. Capacidad operativa disponible como objeto canónico

### Problema
Hoy cupos, agenda y continuidad están conectados, pero no plenamente cerrados en un solo objeto de gobierno.

### Qué crear
Objeto **Capacidad Operativa Disponible** derivado de:
- cupos permanentes
- pacientes activos
- carga territorial
- profesionales disponibles
- visitas críticas pendientes
- vehículos operativos

### Impacto
- clínico-operacional: **alto**
- directivo: **alto**
- complejidad: **media**
- horizonte: **trimestre**

### Dependencias
A2 se vuelve mucho mejor con esto.

---

## 4. Iniciativas de tercer nivel

## C1. Integración portal paciente/cuidador al canon principal
- impacto: medio
- complejidad: media
- horizonte: trimestre

## C2. Knowledge-in-the-loop
- llevar guías y conocimiento al punto exacto del proceso
- impacto: medio
- complejidad: baja-media
- horizonte: quick win

## C3. Auditoría operativa explícita como objeto de gobierno
- impacto: medio
- complejidad: media
- horizonte: trimestre

## C4. Submodelo de insumos y botiquín
- impacto: medio
- complejidad: media-alta
- horizonte: estructural

---

## 5. Secuencia recomendada de ejecución

## Fase 1 — Orden semántico mínimo

1. A1 — Plan de Atención
2. B1 — Máquina de estados del episodio
3. B3 — Categorización de riesgo

### Resultado esperado
El sistema gana columna vertebral clínica y semántica.

## Fase 2 — Gobierno y continuidad

4. A2 — Cockpit directivo
5. A3 — Comunicación clínica unificada
6. B4 — Capacidad operativa disponible

### Resultado esperado
El sistema gana gobierno en tiempo real.

## Fase 3 — Cierre y entorno

7. B2 — Seguimiento post-egreso
8. C1 — Integración portal
9. C2 — Knowledge-in-the-loop

### Resultado esperado
El sistema gana continuidad ampliada y soporte al cuidador.

---

## 6. Quick wins concretos

### QW-01
Hacer visible en ficha un bloque único “Plan actual” aunque inicialmente se arme por agregación.

### QW-02
Agregar categoría de riesgo visible por episodio en censo/ficha.

### QW-03
Marcar toda llamada con resultado estructurado:
- resuelta remoto
- escalar visita
- derivación urgente

### QW-04
Crear vista directiva mínima combinando:
- ocupación
- alertas activas
- pacientes sin visita
- llamadas críticas
- reingresos del mes

### QW-05
Agregar checklist post-egreso estructurado y fecha objetivo de seguimiento.

---

## 7. Lo que NO recomiendo hacer primero

1. rediseñar visualmente toda la app sin cerrar primero la ontología de proceso
2. agregar módulos nuevos desconectados del canon
3. sobreautomatizar REM antes de resolver consistencia episódica
4. construir IA clínica encima de un plan implícito y estados ambiguos

---

## 8. Dependencias fundacionales

| Iniciativa | Depende de | Comentario |
|------------|------------|------------|
| Cockpit directivo | ninguna dura, idealmente A1/B1 | puede empezar con datos actuales |
| Comunicación clínica unificada | ninguna dura | buen candidato paralelo |
| Post-egreso | A3 deseable | mejor si la comunicación ya es canónica |
| Capacidad operativa disponible | A2 deseable | se potencia con cockpit |
| Portal integrado | A3 deseable | compartir semántica de comunicación |
| Knowledge-in-the-loop | ninguna dura | quick win contextual |

---

## 9. Veredicto estratégico

Si tuviera que resumir la jugada arquitectónica correcta en una frase, sería esta:

**antes de agregar más software, hay que terminar de darle esqueleto semántico al sistema que ya existe.**

La prioridad no es expansión indiscriminada.
La prioridad es consolidación estructural.

Y el punto de máxima palanca hoy parece ser:
- plan,
- episodio,
- riesgo,
- comunicación,
- capacidad.
