# HODOM HSC
# Gap Analysis — Canon OPM Local vs Software Observado

Versión: 1.2
Fecha: 2026-04-09
Estado: diagnóstico arquitectónico inicial

Propósito: comparar el canon OPM local ya consolidado con la realidad observada del software HSC, para detectar brechas relevantes y orientar decisiones de evolución.

Base comparada:
- `opm-hodom-hsc-canonico-local-v1.0.md`
- `opm-hodom-hsc-matriz-proceso-modulo-datos-v1.1.md`

---

## 1. Método de lectura

Cada brecha se clasifica por naturaleza:
- **FM** = falta de modelo explícito
- **FD** = falta de dato/objeto suficientemente fuerte
- **FU** = falta de superficie UI o workflow visible
- **FI** = falta de integración entre piezas que sí existen

Y por severidad:
- **A** alta
- **M** media
- **B** baja

---

## 2. Brechas principales

## GAP-01 — El Plan de Atención no aparece aún como objeto fuerte y unificado

**Tipo:** FD + FI  
**Severidad:** A

### Síntoma
Se observan fragmentos:
- plan de enfermería,
- notas clínicas,
- indicaciones,
- frecuencia de visitas,
- agenda,
- prestaciones.

Pero no aparece todavía, en lo leído, un objeto fuerte equivalente a:
**Plan de Atención** o **Plan Terapéutico Interdisciplinario** como spine explícito del episodio.

### Riesgo
- fragmentación del juicio clínico,
- coordinación por agregación implícita,
- difícil trazabilidad de cambios del plan,
- agenda desacoplada del plan real.

### Recomendación
Crear o visibilizar un objeto canónico único de plan, con al menos:
- objetivo clínico,
- prestaciones activas,
- frecuencia,
- disciplina responsable,
- criterios de ajuste,
- criterios de egreso.

---

## GAP-02 — Seguimiento post-egreso subrepresentado

**Tipo:** FU + FD  
**Severidad:** A

### Síntoma
En el canon local el post-egreso es proceso propio.
En lo observado del software todavía no aparece como módulo o flujo fuerte.

### Riesgo
- cierre abrupto del episodio,
- pobre continuidad con APS,
- menor aprendizaje sobre desenlace temprano,
- pérdida de trazabilidad sobre reconsultas/reingresos evitables.

### Recomendación
Dar al post-egreso una de estas dos formas:
1. módulo propio liviano, o
2. extensión explícita de egreso con llamadas y contrarreferencia obligatorias.

---

## GAP-03 — Comunicación clínica existe, pero demasiado fragmentada

**Tipo:** FI  
**Severidad:** A

### Síntoma
La comunicación clínica vive repartida en:
- llamadas,
- ficha,
- portal,
- documento de emergencia,
- links a conocimiento,
- coordinación con derivadores.

### Riesgo
- decisiones y mensajes distribuidos en múltiples artefactos,
- difícil trazabilidad completa por episodio,
- ambigüedad entre orientación, regulación y documentación.

### Recomendación
Definir un subdominio explícito de **Comunicación Clínica**, con objetos mínimos:
- evento de comunicación,
- canal,
- emisor/receptor,
- motivo,
- decisión,
- escalamiento,
- vínculo a episodio.

---

## GAP-04 — Gobernanza directiva dispersa en vez de cockpit integrado

**Tipo:** FU + FI  
**Severidad:** A

### Síntoma
Existen piezas potentes:
- censo,
- cupos,
- REM,
- auditoría,
- llamadas,
- alertas,
- resumen mensual.

Pero no se ve todavía una superficie integrada para Dirección Técnica/Coordinación.

### Riesgo
- dirección operando por navegación entre módulos en vez de cockpit,
- menor capacidad de anticipación,
- decisiones menos sincronizadas entre calidad, capacidad y producción.

### Recomendación
Diseñar una vista directiva HODOM que unifique:
- ocupación,
- presión de egresos,
- pacientes sin visita,
- alertas críticas,
- trazabilidad de llamadas,
- consistencia REM,
- quiebres de continuidad.

---

## GAP-05 — Estados del episodio probablemente insuficientemente explicitados

**Tipo:** FM + FD  
**Severidad:** M

### Síntoma
El software ya trabaja con `stay_id`, `estado`, `tipo_egreso`, `activo`, `admitido`.
Pero el canon local sugiere una máquina de estados más rica:
- postulado,
- elegible,
- admitido,
- activo,
- egresado,
- cerrado,
- seguido.

### Riesgo
- opacidad en frontera entre admisión, actividad y cierre,
- dificultad para reporting coherente,
- confusión entre estado clínico y estado administrativo.

### Recomendación
Formalizar la máquina de estados del episodio como objeto de primer orden.

---

## GAP-06 — Monitoreo clínico rico, pero categorización de riesgo aún blanda

**Tipo:** FM  
**Severidad:** M

### Síntoma
Hay signos vitales, alertas y tendencias.
Pero la **Categoría de Riesgo** aún no aparece claramente como objeto estabilizado del sistema.

### Riesgo
- decisiones heterogéneas,
- poca legibilidad de por qué se prioriza una visita o un egreso,
- débil vínculo entre alertas y operación territorial.

### Recomendación
Modelar y luego operacionalizar una categorización breve y explícita:
- estable,
- observación,
- inestable.

Y amarrarla a:
- agenda,
- escalamiento,
- cupos,
- regulación remota.

---

## GAP-07 — La capa de conocimiento aparece como apoyo, pero no como parte integrada del sistema de trabajo

**Tipo:** FI  
**Severidad:** M

### Síntoma
Desde llamadas y egreso aparecen rutas a guías de conocimiento.

### Riesgo
- el conocimiento queda como biblioteca lateral,
- no como soporte activo al proceso.

### Recomendación
Conectar explícitamente conocimiento con contexto de proceso:
- motivo de llamada,
- tipo de egreso,
- semáforo clínico,
- checklist de cierre.

---

## GAP-08 — El portal paciente/cuidador asoma como capa relevante, pero no está aún integrado al modelo principal

**Tipo:** FM + FI  
**Severidad:** M

### Síntoma
El portal ya tiene:
- dashboard,
- indicaciones,
- documento de emergencia,
- reporte de síntoma,
- mensajes.

### Riesgo
- subestimar el rol del cuidador como coproductor de continuidad,
- perder oportunidades de regulación temprana,
- dejar fuera una parte importante de la interfaz del sistema con el ambiente.

### Recomendación
Crear en próxima iteración un submodelo del **Paciente/Cuidador como nodo activo**.

---

## GAP-09 — La relación entre capacidad, agenda y cupos es fuerte, pero todavía no se ve cerrada como circuito único

**Tipo:** FI  
**Severidad:** M

### Síntoma
Hay:
- agenda diaria,
- cupos editables,
- ocupación,
- censo,
- resumen.

Pero no se ve aún una pieza explícita que cierre el circuito:
capacidad disponible → admisión posible → carga territorial → continuidad segura.

### Riesgo
- aceptar más casos que lo ejecutable,
- o subutilizar capacidad por falta de integración.

### Recomendación
Modelar un objeto transversal:
**Capacidad Operativa Disponible**
como vínculo entre admisión, agenda y gobernanza.

---

## 3. Brechas secundarias

### GAP-10 — Documento de emergencia poco integrado a regulación
**Tipo:** FI  
**Severidad:** B

### GAP-11 — Audit log operativo aún no está explícitamente modelado como objeto de gobierno
**Tipo:** FM  
**Severidad:** B

### GAP-12 — No vimos todavía en lo leído un workflow claro de insumos/botiquín encarnado en UI
**Tipo:** FU  
**Severidad:** M

---

## 4. Lo que NO es brecha hoy

Conviene fijarlo para no sobrediagnosticar.

### No-brecha 1 — Episodio
Está suficientemente fuerte como entidad real.

### No-brecha 2 — Agenda/ruta
Ya está muy bien encarnada en software y datos.

### No-brecha 3 — Llamadas
La trazabilidad telefónica ya tiene buen peso ontológico.

### No-brecha 4 — REM/producción
Esta capa está sorprendentemente madura.

### No-brecha 5 — Ficha longitudinal
La ficha ya funciona como integrador temporal serio.

---

## 5. Priorización arquitectónica sugerida

### Prioridad 1
1. Objeto fuerte **Plan de Atención**
2. Gobernanza directiva integrada
3. Comunicación clínica unificada

### Prioridad 2
4. Seguimiento post-egreso
5. Máquina de estados del episodio
6. Categorización de riesgo explícita

### Prioridad 3
7. Integración del portal al canon principal
8. Circuito formal de capacidad operativa
9. Integración más activa del conocimiento

---

## 6. Backlog orientado por proceso

| Iniciativa | Proceso principal impactado | Beneficio esperado |
|------------|-----------------------------|--------------------|
| Diseñar objeto Plan de Atención | planificación / agenda / atención | coherencia clínica y trazabilidad |
| Cockpit directivo HODOM | gobernanza | mejor gobierno en tiempo real |
| Subdominio Comunicación Clínica | llamadas / portal / red | continuidad y trazabilidad |
| Workflow post-egreso | egreso / seguimiento | continuidad y aprendizaje |
| Máquina de estados del episodio | admisión / censo / egreso / REM | consistencia end-to-end |
| Riesgo clínico explícito | monitoreo / agenda / regulación | priorización mejor fundada |

---

## 7. Veredicto

El software HODOM HSC no está inmaduro. Al contrario.

La mayor parte de sus procesos esenciales ya tiene expresión suficiente. Las brechas más importantes no parecen ser “falta de sistema”, sino **falta de unificación semántica** entre componentes ya poderosos.

Ese hallazgo es bueno.

Significa que la siguiente etapa no debería ser solo construir más pantallas. Debería ser consolidar mejor la ontología operativa del sistema.
