# Lineamientos y Directrices para Optimizar HODOM HSC
## Manual Operativo Vivo para conducción del Director Técnico

**Establecimiento:** Hospital de San Carlos Dr. Benicio Arzola Medina  
**Escala:** establecimiento, con articulación de red  
**Modalidad dominante:** hospitalización integrada hospital -> domicilio -> red  
**Versión:** borrador de conducción v1  
**Base:** normativa HODOM vigente, rol DT, plan de mejora 90 días, diseño del sistema operativo HODOM y desarrollo en `hdos` / `hdos-app`

---

## 1. Propósito

Este documento establece lineamientos y directrices para conducir y optimizar la Unidad de Hospitalización Domiciliaria del Hospital de San Carlos como una **unidad hospitalaria real, gobernable, trazable y simple de operar**.

Su objetivo no es reemplazar protocolos formales ni normativa. Su objetivo es traducirlos en una lógica de funcionamiento práctico para el equipo.

**Principio rector:**

> HODOM debe funcionar con conocimiento útil embebido en el flujo de trabajo, no depender de memoria individual ni de documentos largos difíciles de usar en la operación diaria.

---

## 2. Declaración de conducción

HODOM debe operar como un **sistema socio-técnico de hospitalización domiciliaria**, no como suma de visitas, planillas o decisiones individuales.

La unidad debe asegurar simultáneamente:
- pertinencia clínica de ingreso y permanencia,
- seguridad del paciente y del cuidador,
- continuidad hospital-domicilio-red,
- trazabilidad clínica y documental,
- coordinación operativa diaria,
- cumplimiento normativo,
- observabilidad para gestión y REM,
- capacidad de mejora continua.

---

## 3. Criterios rectores de funcionamiento

## 3.1 HODOM no es descongestión indiferenciada
La hospitalización domiciliaria no debe usarse como descarga inespecífica de camas.

Solo debe ingresar quien cumpla condiciones de:
- pertinencia clínica,
- estabilidad suficiente,
- entorno domiciliario adecuado,
- cuidador o red de apoyo viable,
- cobertura operativa real,
- posibilidad de seguimiento y rescate.

## 3.2 El episodio es la unidad central
La unidad no debe organizarse alrededor de papeles, ni de profesionales aislados, ni de planillas dispersas.

La unidad operativa es el **episodio de hospitalización domiciliaria**, desde postulación hasta egreso y contrarreferencia.

## 3.3 La conducción clínica y la operación deben estar unidas
No debe existir separación artificial entre:
- criterio clínico,
- agenda,
- rutas,
- llamadas,
- registro,
- egreso,
- REM.

Todo forma parte del mismo flujo asistencial.

## 3.4 La simplicidad operativa es una medida de seguridad
Si el sistema exige demasiadas planillas, demasiados pasos ocultos o demasiada memoria tácita, aumenta el riesgo de:
- omisiones,
- arbitrariedad,
- retrasos,
- mala trazabilidad,
- desgaste del equipo.

**Simplificar no es banalizar. Simplificar es hacer gobernable.**

---

## 4. Prioridades de optimización

## Prioridad 1. Ordenar el flujo completo del episodio
El flujo mínimo que debe quedar claro y visible es:

1. postulación
2. evaluación de elegibilidad
3. ingreso
4. planificación
5. programación diaria
6. visita / teleatención / llamada
7. monitoreo y escalamiento
8. egreso
9. contrarreferencia
10. REM y cierre documental

## Prioridad 2. Reducir dependencia de documentos dispersos
El equipo no debe depender de buscar la información crítica en carpetas, WhatsApp, memoria oral o múltiples formularios inconexos.

## Prioridad 3. Convertir `hdos-app` en herramienta de conducción
`hdos-app` no debe ser solo ficha o agenda. Debe transformarse en:
- tablero de operación diaria,
- sistema de coordinación,
- apoyo a decisiones,
- repositorio práctico de conocimiento,
- base de trazabilidad.

## Prioridad 4. Dejar lo formal como respaldo, no como puerta de entrada
Los protocolos, normativa y documentos largos deben permanecer disponibles, pero subordinados a una capa de uso práctico.

---

## 5. Directrices operativas para la unidad

## 5.1 Briefing matinal obligatorio
Debe instalarse un briefing diario breve, disciplinado y útil.

**Objetivos del briefing:**
- revisar ingresos potenciales,
- revisar pacientes activos complejos,
- identificar alertas y rescates posibles,
- confirmar egresos probables,
- ordenar agenda y rutas,
- asignar responsabilidades del día,
- detectar brechas logísticas y documentales.

**Resultado esperado:**
ningún paciente crítico, ingreso pendiente o visita prioritaria debe quedar “huérfano de decisión”.

## 5.2 Criterios visibles de ingreso, seguimiento y alta
La unidad debe operar con criterios comunes, escritos y fáciles de consultar.

No basta con que existan en protocolo. Deben estar traducidos en formato simple para uso cotidiano.

## 5.3 Escalamiento clínico explícito
Toda la unidad debe saber:
- qué constituye alerta,
- qué debe escalarse al momento,
- quién decide,
- cuándo basta teleorientación,
- cuándo corresponde visita,
- cuándo corresponde derivación a urgencia o reingreso.

## 5.4 Registro clínico mínimo suficiente
El estándar de registro debe ser uniforme, breve y defendible.

Debe evitarse tanto el subregistro como el exceso inútil de texto.

## 5.5 Egreso como transición, no como cierre administrativo aislado
Todo egreso debe asegurar:
- criterio clínico explícito,
- documentación mínima completa,
- educación al paciente/cuidador,
- continuidad con APS u otra red,
- contrarreferencia cuando corresponda,
- cierre útil para REM y auditoría.

---

## 6. Modelo de conocimiento práctico para el equipo

## 6.1 Principio de acceso
El conocimiento operativo debe organizarse **por tarea y por decisión**, no por tipo de documento.

## 6.2 Estructura recomendada
La capa de conocimiento práctico debe responder cinco preguntas:
- qué hacer,
- cómo hacerlo,
- qué no olvidar,
- cuándo escalar,
- dónde está el respaldo formal.

## 6.3 Formatos recomendados

### A. Guías rápidas
Piezas breves para tareas críticas:
- admitir paciente,
- validar elegibilidad,
- programar visita,
- registrar visita,
- manejar visita fallida,
- manejar no respuesta telefónica,
- escalar deterioro,
- cerrar egreso.

### B. Checklists
- checklist de ingreso,
- checklist de primera visita,
- checklist de monitoreo,
- checklist de egreso,
- checklist de contrarreferencia,
- checklist de cierre diario.

### C. Árboles de decisión
- elegible / no elegible,
- seguir en domicilio / reevaluar / rescatar,
- teleorientar / visitar / derivar,
- egreso simple / egreso con continuidad reforzada.

### D. Tarjetas por rol
- médico,
- enfermería,
- coordinación,
- TENS,
- kinesiología,
- trabajo social,
- DT.

Cada una debe mostrar:
- prioridades del rol,
- decisiones frecuentes,
- alertas,
- entregables mínimos.

---

## 7. Directrices para `hdos-app`

## 7.1 Rol esperado de la app
`hdos-app` debe convertirse en el punto principal de acceso a la operación y al conocimiento útil de la unidad.

Debe tener tres capas integradas:

### 1. Capa operativa
Lo que el equipo hace:
- censo,
- admisión,
- ficha,
- agenda,
- llamadas,
- egreso,
- REM.

### 2. Capa de ayuda práctica
Lo que el equipo necesita saber para hacerlo bien:
- criterios,
- pasos,
- alertas,
- errores frecuentes,
- escalamiento,
- checklists.

### 3. Capa documental
Respaldo formal:
- normativa,
- protocolos,
- especificaciones,
- modelos,
- documentos estratégicos.

## 7.2 Regla de diseño
Ninguna pantalla crítica debería obligar al equipo a salir del flujo para entender qué hacer.

## 7.3 Ayuda contextual por módulo

### Admisión
Debe mostrar:
- criterios resumidos de ingreso,
- exclusiones resumidas,
- documentos obligatorios,
- campos críticos,
- causal de rechazo o pendiente,
- cuándo escalar al DT.

### Agenda
Debe mostrar:
- priorización clínica del día,
- visitas impostergables,
- pacientes de alto riesgo,
- reglas mínimas de reprogramación,
- incidentes logísticos que afectan seguridad.

### Llamadas / regulación
Debe mostrar:
- semáforo de riesgo,
- preguntas mínimas,
- criterios de resolución remota,
- criterios de visita,
- criterios de derivación.

### Egreso
Debe mostrar:
- criterios mínimos de egreso,
- documentos requeridos,
- contrarreferencia requerida,
- seguimiento post-egreso,
- pendientes que bloquean cierre.

---

## 8. Ejes de mejora priorizados para los próximos meses

## Eje 1. Gobernanza clínica
- criterio común de ingreso, permanencia, rescate y alta,
- revisión regular de casos complejos,
- disminución de variabilidad clínica evitable,
- función reguladora visible del DT.

## Eje 2. Operación diaria
- briefing matinal,
- agenda priorizada,
- reducción de tiempos muertos,
- reglas claras de reprogramación,
- mejor trazabilidad de visitas, llamadas e incidentes.

## Eje 3. Documentación y trazabilidad
- consentimiento,
- ingreso,
- evolución,
- escalamiento,
- egreso,
- contrarreferencia,
- completitud suficiente para REM y auditoría.

## Eje 4. Continuidad hospital-domicilio-red
- mejor interfaz con servicios derivadores,
- mejor contrarreferencia APS,
- continuidad post-egreso,
- reducción de quiebres entre hospital, domicilio y red.

## Eje 5. Capa digital útil
- convertir `hdos-app` en herramienta real del equipo,
- dejar `hdos` como soporte de migración, analítica, depuración y dashboards,
- asegurar consistencia entre operación, dato y visualización.

---

## 9. Regla editorial para todo contenido práctico

Todo contenido de uso cotidiano debe cumplir estas condiciones:

- breve,
- visible,
- accionable,
- asociado a una tarea o decisión,
- consistente con normativa,
- fácil de actualizar,
- enlazado con el documento formal de respaldo.

### Plantilla mínima recomendada
Cada pieza debería responder:
1. para qué sirve,
2. cuándo usarla,
3. qué hacer,
4. qué no olvidar,
5. cuándo escalar,
6. documento asociado.

---

## 10. KPIs sugeridos para conducción

## Proceso
- tiempo postulación -> decisión de elegibilidad,
- tiempo decisión -> primera visita,
- % briefing realizados,
- % visitas ejecutadas según programación,
- % llamadas trazadas en sistema.

## Resultado operativo
- ocupación de cupos,
- días-persona,
- % egresos con epicrisis cerrada,
- % contrarreferencias emitidas,
- tiempo de generación REM.

## Seguridad y continuidad
- tasa de rescate o reingreso,
- eventos adversos o casi fallas,
- % pacientes con criterios/documentos críticos completos,
- seguimiento post-egreso dentro del plazo definido.

---

## 11. Hoja de implementación sugerida

## Fase 1. Orden mínimo visible
- briefing diario,
- criterios escritos simples,
- registro clínico mínimo,
- semáforo de escalamiento,
- checklist de egreso,
- tablero operativo básico.

## Fase 2. Conocimiento embebido en `hdos-app`
- ayuda contextual por módulo,
- guías rápidas,
- checklists por tarea,
- tarjetas por rol,
- acceso a documentos formales enlazados.

## Fase 3. Cierre end-to-end
- trazabilidad completa del episodio,
- mejor integración llamada -> decisión -> acción,
- mejor continuidad APS,
- REM desde datos operacionales,
- auditoría de coherencia flujo-documentación.

---

## 12. Mensaje de conducción al equipo

La optimización de HODOM no busca burocratizar el trabajo.
Busca:
- proteger mejor al paciente,
- ordenar mejor al equipo,
- disminuir arbitrariedad,
- facilitar decisiones,
- hacer visible lo importante,
- sostener crecimiento con seguridad.

**Idea fuerza para transmitir:**

> Ordenar sin rigidizar. Regular sin enlentecer. Formalizar sin burocratizar. Hacer simple lo crítico.

---

## 13. Síntesis ejecutiva final

HODOM HSC debe evolucionar desde una operación sostenida por documentos, memoria y esfuerzo local hacia una **unidad hospitalaria domiciliaria conducida con criterio común, flujo visible, registro suficiente y conocimiento práctico accesible**.

La función del DT es convertir esa transición en sistema.

La función de `hdos-app` debe ser transformarse en la interfaz práctica de esa conducción.

Los protocolos y la normativa deben seguir disponibles, pero subordinados a una capa de uso simple, concreta y fácil para el equipo.

---

## Referencias base
- DS 1/2022, Reglamento de Hospitalización Domiciliaria
- Decreto Exento 31/2024 y Norma Técnica HODOM 2024
- Ley 20.584, derechos y deberes de las personas
- Manual REM 2026, Serie A21 Sección C
- `marco-rol-dt-hodom-hsc.md`
- `plan-90-dias-dt.md`
- `01-diseno-sistema-operativo-hodom-hsc.md`
- `11-resumen-ejecutivo.md`
- repositorios `hdos` y `hdos-app`

**La decisión final y la responsabilidad de conducción siguen perteneciendo a la persona responsable.**
