# Arquitectura de Contenido para `hdos-app`
## Manual Operativo Vivo embebido en el flujo de trabajo

**Proyecto:** HODOM HSC  
**Destino:** `/home/felix/projects/hdos-app`  
**Objetivo:** traducir el marco de conducción DT a una arquitectura de contenido práctica, simple y contextual para el equipo HODOM

---

## 1. Objetivo funcional

Transformar `hdos-app` en una herramienta con doble función:

1. **sistema operativo asistencial**
2. **sistema de acceso al conocimiento práctico**

La meta no es agregar una biblioteca de documentos aislada, sino insertar ayuda útil dentro del trabajo diario.

---

## 2. Principio de diseño

**Cada pantalla crítica debe responder dos cosas al mismo tiempo:**
- qué tengo que hacer,
- cómo hacerlo bien.

Por eso, el conocimiento debe estar organizado en tres niveles:

### Nivel 1. Acción inmediata
- breve
- visible
- contextual
- orientado a decisión

### Nivel 2. Apoyo operativo
- checklist
- criterio resumido
- errores frecuentes
- semáforos

### Nivel 3. Respaldo formal
- protocolo
- normativa
- documento fuente
- especificación

---

## 3. Mapa general recomendado en `hdos-app`

## A. Módulos operativos
- `inicio/`
- `censo/`
- `admision/`
- `ficha/[stayId]/`
- `agenda/`
- `llamadas/`
- `egreso/`
- `rem/`

## B. Capa transversal nueva
- `operacion/`
- `guias/`
- `escalamiento/`
- `roles/`
- `documentos/`

---

## 4. Menú principal sugerido

## Menú clínico-operativo
1. **Inicio**
2. **Censo**
3. **Admisión**
4. **Agenda**
5. **Llamadas**
6. **Egreso**
7. **REM**

## Menú de apoyo práctico
8. **Operación del día**
9. **Guías rápidas**
10. **Escalamiento**
11. **Por rol**
12. **Documentos**

---

## 5. Diseño de cada sección nueva

## 5.1 `inicio/` o dashboard principal
### Función
Ser el centro de operaciones de la unidad.

### Debe mostrar
- pacientes activos
- cupos usados/disponibles
- ingresos pendientes
- pacientes de alto riesgo
- visitas críticas del día
- egresos pendientes
- alertas logísticas
- pendientes documentales
- accesos directos a guías clave

### Widget nuevo recomendado
**“Qué no puede fallar hoy”**
- ingresos por resolver
- visitas impostergables
- pacientes con alerta
- egresos con documentos incompletos

### Widget nuevo recomendado
**“Atajos prácticos”**
- criterio de ingreso
- checklist primera visita
- semáforo de escalamiento
- checklist egreso
- contrarreferencia APS

---

## 5.2 `operacion/`
### Nombre visible sugerido
**Operación del día**

### Función
Traducir el briefing matinal y la coordinación diaria a una vista viva.

### Subbloques
#### 1. Prioridades del día
- ingresos a resolver
- pacientes complejos
- visitas prioritarias
- posibles rescates
- egresos esperables

#### 2. Alertas operativas
- faltas de dotación
- problemas de móvil
- pacientes sin contacto
- insumos críticos
- retrasos relevantes

#### 3. Pendientes de cierre
- fichas incompletas
- llamadas sin resolución
- epicrisis pendientes
- contrarreferencias no emitidas

#### 4. Briefing matinal
- formato breve del briefing
- decisiones del día
- responsables
- observaciones de coordinación

### Uso esperado
Pantalla a revisar al inicio del día y al cierre.

---

## 5.3 `guias/`
### Nombre visible sugerido
**Guías rápidas**

### Función
Biblioteca corta, por tarea, no por documento.

### Estructura sugerida
#### Admisión
- cómo evaluar elegibilidad
- cuándo rechazar o dejar pendiente
- documentos obligatorios
- primera visita segura

#### Seguimiento
- qué registrar en cada visita
- cuándo llamar vs visitar
- visita fallida
- no respuesta telefónica

#### Seguridad
- red flags clínicas
- criterio de rescate
- incidentes en domicilio
- cuidador no competente / no disponible

#### Egreso
- cuándo egresar
- qué debe quedar cerrado
- educación mínima
- contrarreferencia APS

#### Operación diaria
- briefing matinal
- entrega de turno
- reprogramación de ruta
- priorización diaria

### Plantilla obligatoria para cada guía
- para qué sirve
- cuándo usarla
- qué hacer
- qué no olvidar
- cuándo escalar
- documento asociado

---

## 5.4 `escalamiento/`
### Nombre visible sugerido
**Semáforo y escalamiento**

### Función
Dar una referencia clara y rápida para decisiones de deterioro, contingencia y rescate.

### Estructura sugerida
#### Verde
- seguimiento habitual
- teleorientación suficiente
- control programado

#### Amarillo
- requiere reevaluación del equipo
- ajustar seguimiento
- adelantar visita
- escalar a médico / coordinación / DT según caso

#### Rojo
- visita urgente
- derivación a urgencia
- rescate / reingreso
- activación de red de emergencia según criterio

### Debe incluir
- criterios clínicos resumidos
- criterios sociales/operativos críticos
- falla de O2 / insumos / dispositivos
- imposibilidad del cuidador
- agresión, riesgo domiciliario o acceso imposible

### Ubicación adicional
Este semáforo debe aparecer como ayuda contextual también en:
- `llamadas/`
- `ficha/[stayId]/`
- `agenda/`

---

## 5.5 `roles/`
### Nombre visible sugerido
**Trabajo por rol**

### Función
Bajar expectativas concretas y simples para cada integrante.

### Tarjetas por rol sugeridas
- médico
- enfermería
- coordinación
- TENS
- kinesiología
- trabajo social
- administrativo
- DT

### Estructura de cada tarjeta
- misión del rol
- qué mira primero
- decisiones frecuentes
- mínimos de registro
- alertas que no puede dejar pasar
- con quién coordina
- cuándo escalar

### Utilidad
Sirve para:
- onboarding
- alineación de equipo
- reducir ambigüedad funcional
- reforzar estándar común

---

## 5.6 `documentos/`
### Nombre visible sugerido
**Documentos y respaldo**

### Función
Alojar el segundo nivel, no el primero.

### Secciones sugeridas
- normativa HODOM
- protocolos clínico-operativos
- formularios y anexos
- documentos estratégicos
- modelos conceptuales
- especificaciones del sistema

### Regla
Cada documento debería estar precedido por una ficha simple:
- qué es
- para qué sirve
- cuándo revisarlo
- a quién le importa

---

## 6. Ayuda contextual por módulo clínico

## 6.1 `admision/`
### Caja lateral fija sugerida
**Ayuda de admisión**

### Debe incluir
- criterios mínimos de ingreso
- exclusiones frecuentes
- verificación de cuidador
- cobertura territorial
- consentimiento informado
- causal de rechazo / pendiente
- cuándo escalar al DT

### Herramientas rápidas
- checklist de elegibilidad
- checklist documental de ingreso
- errores frecuentes de postulación

---

## 6.2 `censo/`
### Caja lateral sugerida
**Lectura rápida del censo**

### Debe incluir
- pacientes de mayor riesgo
- pacientes próximos a egreso
- pacientes con alertas sin cerrar
- pacientes con documentación incompleta

### Atajos
- criterios de priorización diaria
- cuándo revisar intensificación de seguimiento
- cuándo anticipar egreso

---

## 6.3 `ficha/[stayId]/`
### Bloques contextuales sugeridos
#### 1. Resumen de riesgo
- semáforo actual
- alertas abiertas
- cuidador / soporte
- plan vigente

#### 2. Qué no olvidar en este episodio
- pendiente de documento
- visita requerida
- examen / insumo pendiente
- coordinación APS pendiente

#### 3. Ayuda contextual
- guía de visita
- guía de llamada clínica
- guía de escalamiento
- guía de egreso según estado

---

## 6.4 `agenda/`
### Caja lateral sugerida
**Reglas del día**

### Debe incluir
- cómo priorizar
- qué visitas no se mueven
- qué hacer ante atraso
- qué hacer ante ausencia del paciente
- cuándo reagendar y cuándo escalar

### Atajos
- checklist salida a terreno
- visita fallida
- llamada de coordinación
- incidente logístico

---

## 6.5 `llamadas/`
### Caja lateral sugerida
**Resolución remota**

### Debe incluir
- preguntas mínimas
- qué registrar siempre
- cuándo basta orientación
- cuándo pedir visita
- cuándo derivar o reingresar
- vínculo con semáforo de riesgo

### Atajos
- llamada administrativa
- llamada clínica
- teleorientación
- escalamiento inmediato

---

## 6.6 `egreso/`
### Caja lateral sugerida
**Cierre seguro del episodio**

### Debe incluir
- criterios mínimos de egreso
- epicrisis
- educación a paciente/cuidador
- seguimiento post-egreso
- contrarreferencia APS
- pendientes que bloquean cierre

### Atajos
- checklist de egreso
- checklist contrarreferencia
- tipos de egreso
- errores frecuentes de cierre

---

## 6.7 `rem/`
### Caja lateral sugerida
**Consistencia y trazabilidad**

### Debe incluir
- qué datos alimentan el REM
- por qué un episodio no cierra
- campos críticos faltantes
- errores frecuentes de codificación

### Atajos
- origen de derivación
- tipo de egreso
- profesión de visita
- cupos programados/usados/disponibles

---

## 7. Catálogo inicial de contenidos prácticos

## Prioridad alta
1. criterio de ingreso HODOM
2. criterio de exclusión
3. checklist de admisión
4. checklist de primera visita
5. qué registrar en cada visita
6. semáforo de escalamiento
7. visita fallida / no respuesta
8. checklist de egreso
9. contrarreferencia APS
10. briefing matinal

## Prioridad media
11. manejo de llamada clínica
12. priorización diaria de agenda
13. rescate / reingreso
14. educación mínima al cuidador
15. seguimiento post-egreso
16. incidentes domiciliarios
17. cierre documental del episodio
18. roles y mínimos por disciplina

## Prioridad baja
19. onboarding nuevo integrante
20. preguntas frecuentes
21. errores frecuentes por módulo
22. glosario funcional HODOM

---

## 8. Modelo editorial sugerido

## Tipo de contenido 1. Guía rápida
Campos:
- `titulo`
- `objetivo`
- `cuando_usar`
- `pasos_clave`
- `no_olvidar`
- `cuando_escalar`
- `rol_responsable`
- `documento_fuente`
- `modulos_relacionados`

## Tipo de contenido 2. Checklist
Campos:
- `titulo`
- `contexto`
- `items`
- `criterio_cierre`
- `alertas`
- `responsable`

## Tipo de contenido 3. Tarjeta por rol
Campos:
- `rol`
- `mision`
- `prioridades`
- `decisiones_frecuentes`
- `registro_minimo`
- `alertas`
- `coordinacion`

## Tipo de contenido 4. Documento de respaldo
Campos:
- `titulo`
- `tipo_documento`
- `resumen_simple`
- `cuando_consultarlo`
- `archivo_origen`

---

## 9. Reglas de UX para esta capa

## Debe ser
- breve
- legible en móvil y escritorio
- con lenguaje operativo
- visible dentro del flujo
- con enlaces a profundidad si se necesita
- consistente entre módulos

## Debe evitar
- bloques largos de texto
- copiar protocolos completos dentro de la interfaz
- duplicar documentos sin contexto
- esconder decisiones críticas en PDF
- exigir navegación compleja para resolver dudas simples

---

## 10. Fases de implementación recomendadas

## Fase 1. Estructura mínima visible
Implementar:
- `operacion/`
- `guias/`
- `escalamiento/`
- ayudas laterales en `admision`, `agenda`, `llamadas`, `egreso`

## Fase 2. Contenido crítico
Cargar:
- 10 guías prioritarias
- 4 checklists críticos
- 8 tarjetas por rol
- 1 ficha resumida de normativa HODOM

## Fase 3. Integración fina
Agregar:
- recomendaciones contextuales por estado del episodio
- alertas y pendientes conectados a guías
- onboarding por rol
- aprendizaje de errores frecuentes

---

## 11. Recomendación final de implementación

La capa de conocimiento práctico debe construirse como una **función clínica-operativa de la app**, no como sección ornamental.

La prueba de que funciona no será que “exista contenido”, sino que el equipo:
- pregunte menos dónde está la información,
- tome mejores decisiones más rápido,
- registre con menos fricción,
- escale con más consistencia,
- cierre mejor los episodios.

---

## 12. Entregables siguientes sugeridos

A partir de esta arquitectura, los siguientes artefactos recomendados son:

1. textos listos para las 10 guías prioritarias
2. checklists listos para pegar en la app
3. tarjetas por rol
4. microcopys y cajas laterales por módulo

**La decisión final y la responsabilidad de conducción siguen perteneciendo a la persona responsable.**
