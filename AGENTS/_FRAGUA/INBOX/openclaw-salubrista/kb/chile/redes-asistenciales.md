# Redes Asistenciales en Chile

**Fecha**: 2026-04-01 | **Estado**: Versión inicial | **Fuentes**: Ley 19.937; MINSAL Subsecretaría de Redes Asistenciales; OPS RISS

---

## 1. Concepto de red asistencial

La red asistencial es el conjunto de establecimientos de salud de distinto nivel de complejidad, articulados funcionalmente para dar respuesta integral y continua a las necesidades de salud de una población en un territorio definido.

**Base normativa**: DFL 1/2005, Art. 17 y siguientes. Cada SS debe organizar y articular su red asistencial.

### 1.1 Principios de la red

- **Complementariedad**: Cada nivel resuelve lo que le corresponde
- **Continuidad asistencial**: Flujo sin interrupciones entre niveles
- **Territorialidad**: Adscripción poblacional a un territorio de red
- **Integralidad**: Promoción, prevención, curación, rehabilitación, cuidados paliativos
- **Resolutividad**: Cada nivel resuelve el máximo posible antes de derivar
- **Eficiencia**: Uso racional de recursos según nivel

---

## 2. Estructura de la red

### 2.1 Macro-red

- Corresponde al territorio de un **Servicio de Salud**
- Incluye todos los establecimientos de la red del SS
- El Director del SS es el gestor de la macro-red
- Puede incluir convenios con otros SS para prestaciones de alta complejidad (macro-red regional/nacional)

**Ejemplos de macro-redes nacionales**:
- Red de trasplante de órganos
- Red oncológica
- Red de cirugía cardíaca
- Red de neurocirugía
- Red neonatal

### 2.2 Micro-red

- Subdivisión territorial dentro de un SS
- Generalmente organizada en torno a un hospital base + establecimientos de APS de un territorio
- Articula: CESFAM/CECOSF/postas + hospital de referencia + centros de especialidades
- Permite la gestión local de la referencia-contrarreferencia

### 2.3 Niveles de la red

```
┌─────────────────────────────────────────┐
│        NIVEL TERCIARIO                  │
│   Hospital alta complejidad / Instituto │
│   UCI, subespecialidades, cirugía mayor │
├─────────────────────────────────────────┤
│        NIVEL SECUNDARIO                 │
│   Hospital mediana complejidad          │
│   CRS/CDT, COSAM                        │
│   Especialidades ambulatorias           │
├─────────────────────────────────────────┤
│        NIVEL PRIMARIO                   │
│   CESFAM, CECOSF, Postas rurales       │
│   SAPU, SAR, SUR                        │
│   Puerta de entrada al sistema          │
└─────────────────────────────────────────┘
```

---

## 3. Referencia y contrarreferencia

### 3.1 Sistema de referencia

- **Referencia**: Derivación desde un nivel de menor a mayor complejidad
- **Contrarreferencia**: Retorno del paciente al nivel de origen con indicaciones
- **Interconsulta (IC)**: Solicitud de evaluación por especialista sin transferir responsabilidad

### 3.2 Proceso

1. APS genera interconsulta electrónica (SIGTE o equivalente)
2. Consultorio de destino prioriza y agenda
3. Especialista evalúa y decide: resuelve, solicita exámenes, programa procedimiento, o devuelve a APS
4. Contrarreferencia con indicaciones y plan de seguimiento

### 3.3 Problemas estructurales

- **Tiempo de espera IC**: Principal cuello de botella del sistema
- **Pertinencia de la derivación**: IC mal formuladas o innecesarias
- **Contrarreferencia deficiente**: Especialista no informa de vuelta a APS
- **Fragmentación de la información**: Sistemas informáticos no interoperables
- **Pérdida de pacientes**: Pacientes que no acuden a la cita o se pierden del seguimiento

### 3.4 Estrategias de mejora

- **Teleconsulta / Telemedicina**: Especialista evalúa a distancia con APS
- **Consultorías de especialidad**: Especialista atiende en APS (acerca la especialidad)
- **Protocolos de derivación**: Criterios explícitos de cuándo derivar
- **Gestión de la demanda**: Revisión de IC pendientes, priorización, pertinencia
- **Resolución en APS**: Fortalecer capacidad resolutiva (ej: ecografía, laboratorio ampliado, salud mental)

---

## 4. Gestión de camas

### 4.1 Central de camas

- Cada SS/hospital de alta complejidad tiene una gestión centralizada de camas
- Funciones: asignación de camas según prioridad, gestión de flujos, coordinación de egresos
- Unidad de Gestión de Camas (UGC)

### 4.2 Gestión del flujo

| Componente | Descripción |
|---|---|
| Gestión del ingreso | Priorización desde urgencia, lista de espera quirúrgica, traslados |
| Gestión de la estadía | Reducción de días de estada innecesarios, planificación del alta desde el ingreso |
| Gestión del egreso | Alta temprana, hospitalización domiciliaria, coordinación con APS |
| Gestión de traslados | Entre servicios clínicos, entre hospitales, camas críticas |

### 4.3 Indicadores de gestión de camas

- Índice ocupacional por servicio clínico
- Promedio de días de estada por GRD
- Pacientes en espera de cama (boarding en urgencia)
- Tiempo de sustitución de cama
- Egresos antes de mediodía (meta de gestión)
- Tasa de hospitalización domiciliaria

### 4.4 Hospitalización domiciliaria

- Alternativa a la hospitalización convencional para pacientes estables
- Equipo de salud realiza visitas domiciliarias con enfoque hospitalario
- Reduce estancia hospitalaria y libera camas
- Mejor satisfacción usuaria
- Requiere criterios de inclusión/exclusión y logística

---

## 5. Telemedicina

### 5.1 Modalidades

| Modalidad | Descripción | Aplicación |
|---|---|---|
| **Teleconsulta** | Consulta sincrónica a distancia (videoconferencia) | Especialidades médicas, salud mental, seguimiento |
| **Teleinterconsulta** | Especialista evalúa caso a distancia con médico de APS | Reducción de IC presenciales |
| **Teledermatología** | Imágenes enviadas para evaluación asincrónica (store-and-forward) | Dermatología, oftalmología |
| **Telerradiología** | Lectura de imágenes a distancia | Radiología, TAC |
| **Telemonitoreo** | Monitoreo remoto de pacientes crónicos | DM, HTA, ICC, EPOC |
| **Teleurgencia** | Apoyo a distancia para urgencias en establecimientos remotos | Zonas rurales, ACV |

### 5.2 Marco regulatorio [VERIFICAR]

- Resoluciones MINSAL que regulan telemedicina (aceleradas post-COVID-19)
- Decreto de telemedicina [VERIFICAR si se promulgó como decreto o resolución]
- Registro en ficha clínica electrónica
- Consentimiento informado para atención remota

### 5.3 Plataformas

- Cada SS ha implementado soluciones heterogéneas [VERIFICAR estandarización]
- Programa Nacional de Telesalud del MINSAL
- Desafío de interoperabilidad entre plataformas

---

## 6. Centros de especialidades

### 6.1 Centro de Referencia de Salud (CRS)

- Atención ambulatoria de especialidades médicas
- Modelo de referencia desde APS
- Puede estar adosado o separado del hospital

### 6.2 Centro Diagnóstico Terapéutico (CDT)

- Procedimientos ambulatorios de mediana complejidad
- Endoscopías, biopsias, cirugía menor, procedimientos bajo sedación
- Laboratorio e imagenología de especialidad

### 6.3 Hospital de Día

- Atención sin hospitalización nocturna
- Modelos: quirúrgico (CMA), médico (quimioterapia, diálisis), psiquiátrico

---

## 7. Gestión de la demanda

### 7.1 Análisis de demanda

- Estudio de la demanda referida (IC pendientes)
- Análisis de pertinencia de derivaciones
- Modelamiento de oferta vs demanda por especialidad
- Proyección demográfica y epidemiológica

### 7.2 Estrategias de gestión de demanda

| Estrategia | Descripción |
|---|---|
| Fortalecimiento de APS | Mayor resolutividad reduce derivaciones |
| Consultorías | Especialista capacita y resuelve en APS |
| Telemedicina | Evaluación remota sin desplazamiento |
| Protocolos de derivación | Derivaciones pertinentes y bien documentadas |
| Gestión activa de LE | Revisión periódica de lista, contacto, depuración |
| CMA | Cirugía ambulatoria libera camas y reduce espera quirúrgica |
| Extensiones horarias | Tercer turno, sábados |
| Compra de servicios | A prestadores privados cuando la red pública no da abasto |

---

## 8. Redes Integradas de Servicios de Salud (RISS) — Marco OPS

Chile ha adoptado el marco de RISS de la OPS (2010) como referente para la organización de redes.

**Atributos esenciales de las RISS**:
1. Población y territorio definidos
2. Red extensa de establecimientos de salud
3. Primer nivel de atención como puerta de entrada
4. Prestación de servicios especializados en el lugar más apropiado
5. Existencia de mecanismos de coordinación asistencial
6. Atención centrada en la persona, familia y comunidad
7. Gobernanza única para toda la red
8. Gestión integrada de los sistemas de apoyo
9. Recursos humanos suficientes y comprometidos
10. Sistema de información integrado
11. Financiamiento adecuado e incentivos alineados
12. Gestión basada en resultados
13. Participación social
14. Acción intersectorial

---

## 9. Fuentes

- Chile. DFL 1/2005. Ministerio de Salud.
- Chile. Ley 19.937 (2004). Autoridad Sanitaria y Gestión.
- MINSAL. Subsecretaría de Redes Asistenciales. Orientaciones para la planificación y programación en red.
- OPS. Redes Integradas de Servicios de Salud: conceptos, opciones de política y hoja de ruta para su implementación en las Américas. Washington, 2010.
- MINSAL. Programa Nacional de Telesalud. Orientaciones técnicas.
- MINSAL. Gestión de listas de espera. Orientaciones.
