# HODOM HSC
# Matriz Proceso ↔ Módulo ↔ Datos

Versión: 1.1
Fecha: 2026-04-09
Estado: matriz operativa inicial

Propósito: aterrizar el canon local OPM a la realidad observable del software HSC, vinculando:
- proceso OPM,
- módulo UI,
- vistas / tablas / funciones de datos,
- huecos o tensiones arquitectónicas.

Fuentes efectivamente leídas para esta matriz:
- `/home/felix/projects/hdos-app/README.md`
- `/home/felix/projects/hdos-app/src/app/(app)/admision/page.tsx`
- `/home/felix/projects/hdos-app/src/app/(app)/agenda/page.tsx`
- `/home/felix/projects/hdos-app/src/app/(app)/llamadas/page.tsx`
- `/home/felix/projects/hdos-app/src/app/(app)/egreso/page.tsx`
- `/home/felix/projects/hdos-app/src/app/(app)/rem/page.tsx`
- `/home/felix/projects/hdos-app/src/app/(app)/rem/cupos-form.tsx`
- `/home/felix/projects/hdos-app/src/app/(app)/censo/page.tsx`
- `/home/felix/projects/hdos-app/src/app/(app)/ficha/[stayId]/page.tsx`
- `/home/felix/projects/hdos/README.md`
- `opm-hodom-hsc-canonico-local-v1.0.md`

---

## 1. Principio de lectura

La pregunta aquí no es “qué pantallas tiene el sistema”, sino algo más exigente:

**¿Qué procesos reales ya están suficientemente encarnados en módulos y datos, y cuáles todavía están semánticamente incompletos?**

---

## 2. Matriz principal

| Proceso OPM | Módulo/UI observado | Datos observados | Lectura | Estado |
|-------------|---------------------|------------------|---------|--------|
| *Evaluar Elegibilidad* | `/admision` | `operational.v_postulaciones_pendientes` | ya existe una cola de postulaciones con estado, origen, checklist y consentimiento | fuerte |
| *Admitir Episodio* | `/admision`, `/ficha/[stayId]` | `stay_id`, `clinical.estadia`, `clinical.paciente` | el episodio ya está materializado operacionalmente | fuerte |
| *Planificar Atención Interdisciplinaria* | parcialmente en `/ficha/[stayId]` | `clinical.nota_evolucion`, campos `plan_enfermeria`; inferencia de plan | existe señal parcial, pero el plan aún no aparece como objeto UI autónomo claro | medio |
| *Programar Visitas y Rutas* | `/agenda` | `operational.v_agenda_dia`, `operational.visita`, `route_id`, `provider_id`, `seq_en_ruta` | muy buen soporte real para agenda territorial | fuerte |
| *Ejecutar Atención Domiciliaria* | `/ficha/[stayId]` | timeline, visitas, notas, observaciones, dispositivos, exámenes | la ejecución está dispersa, pero rica | fuerte |
| *Regular Atención a Distancia* | `/llamadas` | `operational.v_llamadas`, `operational.registro_llamada` | trazabilidad telefónica fuerte, con motivo, profesional y stay_id | fuerte |
| *Monitorear Evolución Clínica* | `/ficha/[stayId]`, `/censo` | `clinical.observacion`, `clinical.alerta`, `clinical.v_timeline_episodio` | muy buena base para monitoreo y alertas | fuerte |
| *Gestionar Comunicación Clínica* | `/llamadas`, portal, `/ficha/[stayId]` | llamadas, contactos, mensajes portal inferidos, teléfonos, links a conocimiento | está repartido en varios módulos; semánticamente existe pero aún no está unificado | medio |
| *Egresar Episodio* | `/egreso` | `clinical.estadia.estado`, `tipo_egreso`, `fecha_egreso` | muy clara existencia de flujo y tipología de egreso | fuerte |
| *Realizar Seguimiento Post-Egreso* | aún no visible como módulo autónomo leído | inferido por conocimiento y modelo | todavía débil en evidencia UI directa | débil |
| *Tributar Producción y REM* | `/rem`, `/censo` | `reporting.fn_rem_personas_atendidas`, `fn_rem_visitas`, `fn_rem_origen_derivacion`, `fn_ocupacion_dia`, `v_resumen_mes` | extremadamente explícito y maduro | muy fuerte |
| *Gobernar Sistema HODOM HSC* | disperso, no como módulo único | cupos editables, auditoría, consistencia, capacidad, conocimiento | existe por fragmentos, aún no como cockpit directivo integrado | medio |

---

## 3. Objetos que ya están materializados de forma robusta

### 3.1 Episodio

Indicadores observados:
- `stay_id` está por todas partes
- `/ficha/[stayId]`
- `clinical.estadia`
- llamadas asociadas al episodio
- visitas asociadas al episodio
- egreso asociado al episodio

Conclusión:
**Episodio de Hospitalización Domiciliaria** no es solo decisión conceptual. Ya es objeto canónico operativo real.

### 3.2 Visita domiciliaria

Indicadores observados:
- `operational.visita`
- estados de visita
- profesional asignado
- ruta
- horario planificado
- fallidas/canceladas/completas

Conclusión:
**Visita Domiciliaria** es un objeto de primer orden, y uno de los mejores candidatos a spine operacional del sistema junto al episodio.

### 3.3 Llamado clínico

Indicadores observados:
- `operational.v_llamadas`
- `operational.registro_llamada`
- tipo emitida/recibida
- motivo
- observaciones
- profesional
- stay_id

Conclusión:
**Llamado Clínico** ya está muy bien objetualizado. La regulación remota no necesita inventarse, necesita modelarse mejor.

### 3.4 REM y producción

Indicadores observados:
- funciones reporting explícitas
- ocupación diaria
- resumen mensual
- exportación CSV
- edición de cupos permanentes

Conclusión:
la capa de observabilidad no es un adorno. Está ya implementada como sistema parcial de gobierno.

---

## 4. Mapa más fino por módulo

## 4.1 `/admision`

### Qué modela bien
- postulación
- origen de derivación
- estado de elegibilidad
- consentimiento
- checklist de elegibilidad

### Qué sugiere del dominio
- la elegibilidad es tratada como pipeline, no como juicio instantáneo
- existe una cola explícita de entrada
- el episodio parece nacer muy temprano, incluso antes de la admisión plena, porque ya hay `stay_id` en postulaciones

### Tensión
Si `stay_id` existe antes de la admisión final, hay que distinguir mejor entre:
- episodio postulado
- episodio admitido
- episodio activo

Eso le da mucha fuerza a modelar estados del episodio. 

## 4.2 `/agenda`

### Qué modela bien
- día operativo
- visitas visibles
- programadas/asignadas
- comunas cubiertas
- conflictos de horario
- `route_id`
- profesional asignado o no asignado
- preparación offline por `stay_id`

### Qué sugiere del dominio
- la agenda no es lista plana, es estructura territorial con conflictos y carga
- la secuenciación y la asignación son operaciones separables
- la ruta ya existe semánticamente en datos, no solo en UI

### Tensión
El modelo canónico debe resistir la tentación de fundir “agenda” y “visita”. No son lo mismo.

## 4.3 `/llamadas`

### Qué modela bien
- trazabilidad histórica
- llamada emitida/recibida
- motivo tipificado
- profesional responsable
- vínculo con el episodio

### Qué sugiere del dominio
- la llamada es ya entidad documental seria
- la resolución remota puede auditarse
- el sistema ya presupone escalamiento y semáforo clínico

### Tensión
Falta ver si toda llamada clínica produce siempre un objeto de decisión o si a veces queda solo como observación narrativa.

## 4.4 `/ficha/[stayId]`

### Qué modela bien
- longitudinalidad clínica
- observaciones y signos vitales
- alertas activas
- contexto por disciplina
- timeline integrado de visitas, notas y llamadas
- domicilio, cuidador, dispositivos, exámenes, actividad

### Qué sugiere del dominio
- la ficha es el principal objeto de integración temporal del sistema
- el episodio es leíble como timeline multimodal
- la ficha no es solo memoria, es superficie de coordinación y juicio

### Tensión
La ficha parece estar soportando demasiadas funciones a la vez:
- memoria clínica,
- tablero operativo,
- monitor de riesgo,
- integrador de comunicaciones.

Eso es potente, pero hay que vigilar sobrecarga semántica.

## 4.5 `/egreso`

### Qué modela bien
- pacientes activos elegibles para egreso
- tipo de egreso normalizado
- contadores de altas, reingresos, fallecidos
- checklist mental de cierre seguro

### Qué sugiere del dominio
- el egreso se trata como proceso activo de selección y cierre
- la tipología de causal importa realmente en operación

### Tensión
Hay evidencia del acto de egreso, pero todavía poca evidencia directa del post-egreso en UI leída.

## 4.6 `/rem`

### Qué modela bien
- personas atendidas
- visitas por profesión
- origen de derivación
- cupos programados/utilizados/disponibles
- exportación
- validación implícita por función y panel

### Qué sugiere del dominio
- producción y cupos ya forman un sub-sistema con lógica propia
- la capacidad es editable y, por tanto, gobernada

### Tensión
Esto ya no parece solo “tributación”. Parece parte del sistema de management control de la unidad.

## 4.7 `/censo`

### Qué modela bien
- pacientes activos
- cupos
- filtros por profesional/comuna/zona
- alertas activas
- días sin visita
- resumen mensual
- postulaciones pendientes

### Qué sugiere del dominio
- el censo es un tablero de coordinación, no una mera lista de pacientes
- mezcla presente clínico con presión operativa y capacidad

### Tensión
El censo podría ser la verdadera interfaz principal de coordinación, más que agenda o ficha aisladas.

---

## 5. Mapa de vistas, tablas y funciones ya detectadas

### Vistas operativas
- `operational.v_postulaciones_pendientes`
- `operational.v_agenda_dia`
- `operational.v_llamadas`
- `operational.v_tablero_coordinacion`

### Tablas operativas / clínicas observadas
- `clinical.estadia`
- `clinical.paciente`
- `clinical.domicilio`
- `clinical.cuidador`
- `clinical.observacion`
- `clinical.alerta`
- `clinical.nota_evolucion`
- `clinical.condicion`
- `clinical.dispositivo`
- `clinical.solicitud_examen`
- `clinical.voluntad_anticipada`
- `operational.visita`
- `operational.profesional`
- `operational.registro_llamada`
- `operational.audit_log`
- `territorial.localizacion`

### Vistas / funciones de reporting
- `reporting.fn_rem_personas_atendidas(periodo)`
- `reporting.fn_rem_visitas(periodo)`
- `reporting.fn_rem_origen_derivacion(periodo)`
- `reporting.fn_ocupacion_dia(fecha)`
- `reporting.v_resumen_mes`

---

## 6. Huecos arquitectónicos detectados

## 6.1 Objeto “Plan de Atención” aún demasiado implícito

Tenemos señales de:
- plan de enfermería,
- notas clínicas,
- indicaciones,
- frecuencia,
- visitas.

Pero no vimos aún, en lo leído, un objeto fuerte y unificado llamado plan.

Riesgo:
el sistema puede terminar coordinándose por agregación de fragmentos, no por un objeto plan verdaderamente gobernable.

## 6.2 Seguimiento post-egreso con evidencia débil

Normativamente y conceptualmente importa, pero no apareció aún como módulo o flujo robusto en lo leído.

Riesgo:
que el episodio cierre clínicamente, pero no tenga buena vida posterior en continuidad o contrarreferencia.

## 6.3 Comunicación clínica está fragmentada

Hoy se reparte entre:
- llamadas,
- ficha,
- portal,
- conocimiento,
- documentos de emergencia.

Riesgo:
que exista semánticamente pero no como subsistema bien delimitado.

## 6.4 Gobierno directivo aún disperso

Hay piezas claras:
- cupos,
- resumen,
- auditoría,
- REM,
- censo,
- llamadas trazadas.

Pero no aparece aún una superficie directiva verdaderamente unificada para Dirección Técnica/Coordinación.

---

## 7. Diagnóstico de madurez por proceso

| Proceso | Madurez software observada | Comentario |
|---------|----------------------------|------------|
| Elegibilidad | alta | cola y checklist ya visibles |
| Admisión episódica | alta | `stay_id` y estadía bien presentes |
| Agenda/ruta | muy alta | probablemente una de las capas más maduras |
| Atención presencial | alta | fuerte integración en ficha |
| Regulación remota | alta | llamadas bien trazadas |
| Monitoreo clínico | alta | signos, alertas, timeline |
| Egreso | media-alta | buena base, falta ver post-egreso |
| Seguimiento post-egreso | baja | poca evidencia directa aún |
| REM/producción | muy alta | reporting explícito y funcional |
| Gobierno sistémico | media | existe por fragmentos, no como cockpit |

---

## 8. Conclusión fuerte

El sistema HSC ya tiene una arquitectura real bastante más avanzada de lo que aparentaría una simple app clínica.

Lo más maduro parece ser la triada:
- episodio,
- territorialidad operativa,
- observabilidad.

Eso confirma la intuición del modelo canónico local: el valor diferencial de HODOM HSC no está solo en la clínica domiciliaria, sino en haber empezado a construir un sistema que articula cuidado, territorio y gobierno operativo en una misma ontología.

---

## 9. Próximo paso autónomo recomendado

La secuencia útil después de esta matriz es:

1. producir un **gap analysis** entre canon OPM local y software realmente observado,
2. clasificar huecos en:
   - falta de modelo,
   - falta de UI,
   - falta de datos,
   - falta de integración,
3. proponer backlog arquitectónico orientado por proceso.
