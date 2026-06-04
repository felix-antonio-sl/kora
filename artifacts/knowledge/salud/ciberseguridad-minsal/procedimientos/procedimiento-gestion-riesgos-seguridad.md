---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-riesgos-seguridad
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-006 v1, Junio 2023
  minsal_id: PROS-NC-006
  minsal_version: '1'
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- gestion-riesgos
- iso-31000
- iso-27005
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-riesgos-seguridad
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento Gestion de Riesgos de la Seguridad de la Informacion


## Proposito y alcance

Establecer el procedimiento de gestion de riesgos del SGSI segun normativa ISO, identificando, cuantificando y priorizando riesgos de acuerdo con criterios de aceptacion y objetivos institucionales. Como resultado se determinan acciones apropiadas mediante controles de seguridad que protejan contra los riesgos identificados.

Aplica a todos los activos de informacion, incluso aquellos gestionados mediante contratos con terceros. Aplica a todos los funcionarios (planta, contrata, reemplazos, suplencias), personal a honorarios y terceros (proveedores) que presten servicios para las Subsecretarias de Salud Publica y Redes Asistenciales.

**Controles ISO 27001 asociados**: A.05.01.01 (Politicas para seguridad), A.05.01.02 (Roles y responsabilidades), A.18.01.02 (Revision de politicas).

## Terminologia

### Conceptos nucleo

**Amenaza** — Causa potencial de un incidente no deseado que puede resultar en dano a un sistema, persona u organizacion.

**Vulnerabilidad** — Debilidad de un activo o control que puede ser explotada por una o mas amenazas.

**Riesgo** — Posibilidad de que una amenaza explote una vulnerabilidad para causar perdida o dano en un activo de informacion. Combinacion de la probabilidad de un evento y sus consecuencias.

**Riesgo Inherente** (riesgo puro) — Riesgo implicito de toda actividad por el solo hecho de ser realizada, antes de aplicar controles.

**Riesgo Residual** — Riesgo que permanece tras el tratamiento del riesgo.

**Impacto** — Consecuencia de la materializacion de una amenaza sobre un activo. Costo para la institucion, medible o no en terminos financieros (ej. perdida de reputacion, implicaciones legales).

**Apetito del Riesgo** — Definicion institucional para determinar si el riesgo y su severidad estan dentro de limites aceptados para su manejo.

**Mapa de Calor** — Tecnica de medicion de valores por presentacion de colores bidimensional para observar relevancia a partir de valores entregados.

### Triada CID

**Confidencialidad** — La informacion solo debe ser accesible o divulgada a quienes estan autorizados.

**Integridad** — La informacion debe permanecer correcta (integridad de datos) y como el emisor la origino (integridad de fuente) sin manipulaciones por terceros.

**Disponibilidad** — La informacion debe estar siempre accesible para quienes esten autorizados.

## Documentos aplicables

- Norma NCh-ISO 31000:2018 — Directrices para la gestion de riesgos.
- Norma NCh-ISO/IEC 27005:2020 — Tecnologias de informacion, gestion del riesgo de seguridad de la informacion.
- Norma NCh-ISO/IEC 27001:2020 — Puntos 6.1.2 (evaluacion de riesgo) y 6.1.3 (tratamiento de riesgo).
- Marco Juridico SSI publicado en portal CSIRT del Ministerio del Interior.
- Decretos Supremos y Normas Internacionales de Seguridad de la Informacion y Ciberseguridad.
- Politica General de Seguridad de la Informacion.
- Politica de Gestion de Riesgos de Seguridad de la Informacion.

## Roles y responsabilidades

### Nivel Directivo

Responsable de generar condiciones adecuadas para la ejecucion y comunicacion del procedimiento. Asignar recursos necesarios para implementar y mantener el proceso de gestion de riesgos y tratamiento.

### Comite de Seguridad de la Informacion (CSI)

Supervisar y respaldar la gestion de riesgos de seguridad de la informacion. Revision regular de la efectividad de los procedimientos relacionados con la gestion de riesgos.

### Encargado de Seguridad de la Informacion / Ciberseguridad (CISO / Risk Manager)

Velar por la aplicacion del procedimiento y brindar asesoramiento en identificacion de amenazas que pueden afectar activos de informacion y vulnerabilidades que las propician. Informar al CSI sobre resultados de evaluacion de riesgos. Responsable, en conjunto con los propietarios de activos, por la definicion de acciones de tratamiento de riesgos.

### Dueños de activos de informacion (Risk Owners)

Aplicar el procedimiento e identificar, estimar y valorar los riesgos identificados. Responsables, en conjunto con el encargado de seguridad, por la definicion de acciones de tratamiento de riesgos.

## Proceso de gestion del riesgo

### Actividades del proceso (15 pasos)

La gestion del riesgo es parte integral de todas las actividades de gestion de seguridad de la informacion y se aplica tanto a la implementacion como a la operacion en curso del SGSI.

| Paso | Fase | Actividad |
|------|------|-----------|
| 1 | Establecimiento del contexto | Consideraciones generales |
| 2 | | Levantamiento de informacion inicial |
| 3 | | Establecer criterios basicos para la gestion del riesgo |
| 4 | | Definir alcance y limites de la gestion del riesgo |
| 5 | Valoracion del riesgo | Identificar activos de informacion |
| 6 | | Identificar las amenazas y las vulnerabilidades |
| 7 | | Identificar los controles existentes |
| 8 | | Identificar consecuencias |
| 9 | | Valorar las consecuencias |
| 10 | | Valorar los incidentes |
| 11 | | Determinar el nivel de estimacion del riesgo |
| 12 | | Evaluar el riesgo |
| 13 | Tratamiento del riesgo | Seleccion de controles |
| 14 | Aceptacion del riesgo | Aceptar el riesgo |
| 15 | Comunicacion, monitoreo y revision | Comunicar, monitorear y revisar los riesgos |

### Flujo general

El proceso sigue un enfoque sistematico y estructurado para identificar, evaluar y tratar riesgos de seguridad de la informacion, alineado con NCh-ISO/IEC 27005:2018.

## Establecimiento del contexto

### Criterios basicos

Segun el alcance y objetivos de la gestion del riesgo se aplican diferentes enfoques:

**Criterios de identificacion del riesgo** — Considerar activos de informacion con valor de impacto alto para el proceso de evaluacion.

**Criterios de evaluacion del riesgo** — Desarrollar criterios para determinar el riesgo de seguridad de la informacion institucional.

**Criterios de impacto** — Especificar en terminos del grado de dano o costos para la organizacion causados por un evento de seguridad.

**Criterios de aceptacion del riesgo** — Dependen de politicas, metas, objetivos institucionales y partes interesadas.

### Alcance y limites

Definir el alcance para garantizar que todos los activos relevantes se consideran en la valoracion. Identificar limites para abordar riesgos que surgen al establecer dichos limites.

Para la comprension del contexto interno, externo y partes interesadas se pueden usar metodologias como FODA (fuerza, oportunidad, debilidad, amenaza) o PESTEL (politica, economia, social, tecnologia, ecologia, legal).

La operacion del proceso de gestion del riesgo esta radicada en el CSI y el Encargado de Seguridad de la Informacion y Ciberseguridad, mediante acto administrativo correspondiente.

## Identificacion de activos de informacion

Punto inicial de la gestion de riesgo. Se evaluan segun su criticidad e importancia institucional.

#### Clasificacion de activos

| Tipo | Descripcion |
|------|-------------|
| Instalaciones | Lugares donde se hospedan los sistemas de informacion y comunicaciones |
| Equipamiento auxiliar | Equipos de soporte a sistemas de informacion sin relacion directa con datos |
| Hardware | Bienes materiales fisicos que soportan servicios, depositan datos, ejecutan aplicaciones o procesan/transmiten datos |
| Software | Programas, aplicativos, desarrollos que automatizan tareas; gestionan, analizan y transforman datos |
| Soportes de informacion | Dispositivos fisicos que almacenan informacion de forma permanente o por largos periodos |
| Datos/Informacion | Elementos que representan conocimiento, singulares o agrupados |
| Servicios | Funcion que satisface una necesidad de usuarios (finales, instrumentales o contratados) |
| Personal | Personas relacionadas con los sistemas de informacion |

Se debe identificar al propietario de cada activo para asignar responsabilidad y rendicion de cuentas.

#### Estructura de identificacion de activos

Campos requeridos: Id. Proceso, Proceso, Sistema de Informacion, Nombre Activo, Descripcion, Responsable del Activo, Tipo de Activo, Cod. Tipo (3 caracteres, ej. SER, SOF), Numero (correlativo), Id. Activo (compuesto: ACT-{CodTipo}-{Numero}, ej. ACT-SER-0021), Ubicacion.

## Ponderacion de criticidad de activos (valoracion CID)

Se realiza en terminos cualitativos "alto, medio, bajo" con valor cuantitativo asociado. La valorizacion usa los tres atributos de la informacion.

#### Valoracion del impacto por perdida de confidencialidad

| Nivel | Valor | Criterio |
|-------|-------|----------|
| Alto | 3 | Divulgacion no autorizada tiene efecto critico. Ej. Informacion confidencial o sensible |
| Medio | 2 | Divulgacion no autorizada tiene efecto limitado. Ej. Informacion de uso interno |
| Bajo | 1 | Divulgacion no autorizada no tiene efecto. Ej. Informacion publica |

#### Valoracion del impacto por perdida de integridad

| Nivel | Valor | Criterio |
|-------|-------|----------|
| Alto | 3 | Destruccion o modificacion no autorizada tiene efecto severo |
| Medio | 2 | Destruccion o modificacion no autorizada tiene efecto considerable |
| Bajo | 1 | Destruccion o modificacion no autorizada tiene efecto leve |

#### Valoracion del impacto por perdida de disponibilidad

| Nivel | Valor | Criterio |
|-------|-------|----------|
| Alto | 3 | Interrupcion al acceso tiene efecto critico/grave |
| Medio | 2 | Interrupcion al acceso tiene efecto considerable |
| Bajo | 1 | Interrupcion al acceso tiene efecto minimo |

#### Calculo del valor del activo (VA)

```
VA = (C + I + D) / 3
```

Donde: C = Confidencialidad, I = Integridad, D = Disponibilidad.

#### Escala de criticidad del activo segun VA

| Rango VA | Nivel Criticidad |
|----------|-----------------|
| VA > 2.5 | Alto |
| 1.5 <= VA <= 2.5 | Medio |
| VA < 1.5 | Bajo |

## Analisis y evaluacion de riesgos

El analisis de riesgos se realiza considerando escenarios de identificacion de amenazas, vulnerabilidades y su probabilidad de materializacion. Este es el proceso minimo para su consideracion.

#### Identificacion del riesgo

Busca una relacion de los posibles puntos de peligro. Lo identificado se analiza en etapa siguiente. Lo no identificado queda como riesgo oculto o ignorado.

#### Analisis de los riesgos

Calificar los riesgos identificados cuantificando consecuencias (analisis cuantitativo) u ordenando importancia relativa (analisis cualitativo). El resultado es una vision estructurada que permite centrarse en lo mas importante.

## Identificacion de amenazas

Las amenazas se relacionan directamente con sus fuentes. Segun NCh-ISO/IEC 27005:2020, una amenaza tiene potencial de danar activos y puede ser de origen natural o humano, accidental o deliberado.

La identificacion debe agrupar amenazas por tipo y luego individualizarlas. Se deben considerar las amenazas del Anexo 1 (informativo de ejemplos de amenazas tipicas) de NCh-ISO/IEC 27005:2020.

#### Campos de registro de amenazas

| Campo | Descripcion |
|-------|-------------|
| Amenaza (Descripcion) | Descripcion objetiva de la amenaza con antecedentes relevantes |
| Tipo Amenaza | Agrupador de conjunto |
| Fuente Amenaza | Origen: Deliberada (D), Accidental (A), Entorno (E) |
| Valor Amenaza | Valor cuantitativo para medir importancia en afeccion del activo |
| Nivel Amenaza | Valor cualitativo de medicion |

#### Escala de valorizacion de amenazas

| Nivel | Valor | Criterio de evaluacion |
|-------|-------|----------------------|
| Muy Alto | 5 | Adversario con experiencia muy sofisticada, buenos recursos y capacidades para ataques exitosos, continuos y coordinados. Busca obstaculizar gravemente o destruir la funcion principal del negocio. Efectos de tercero/error/accidente/naturaleza devastadores, involucran practicamente todos los usuarios, sistemas, infraestructura y servicios. |
| Alto | 4 | Adversario con nivel sofisticado de experiencia, capacidades y oportunidades para ataques coordinados exitosos. Busca impedir aspectos criticos de una funcion principal o colocarse en posicion para hacerlo en el futuro. Efectos de tercero/error/accidente/naturaleza extensos, involucran mayoria de usuarios, sistemas, infraestructura y servicios. |
| Medio | 3 | Adversario con recursos, experiencia y oportunidades moderados. Busca obtener o modificar informacion critica o sensible especifica o usurpar recursos ciberneticos estableciendo punto de apoyo. Efectos de tercero/error/accidente/naturaleza de amplio alcance, involucran parte significativa de usuarios, sistemas y servicios. |
| Bajo | 2 | Adversario con recursos, experiencia y oportunidades limitados para ataque exitoso. Busca activamente obtener informacion critica o sensible interrumpiendo uso de recursos ciberneticos sin preocuparse por deteccion. Efectos de tercero/error/accidente/naturaleza limitados, involucran algunos usuarios, sistemas, infraestructura y servicios. |
| Muy Bajo | 1 | Adversario con recursos, experiencia y oportunidades muy limitados. Busca usurpar, interrumpir o desfigurar recursos ciberneticos sin preocuparse por deteccion. Efectos de tercero/error/accidente/naturaleza minimos, afectan pocos o ningun usuario, sistema, infraestructura o servicio. |

## Identificacion de vulnerabilidades

Una vulnerabilidad que no tiene amenaza correspondiente puede no requerir control, pero es recomendable reconocerla y monitorearla para determinar cambios. Se referencia el Anexo 2 (ejemplos de vulnerabilidades) de NCh-ISO/IEC 27005:2020.

#### Campos de registro de vulnerabilidades

| Campo | Descripcion |
|-------|-------------|
| Vulnerabilidad (Descripcion) | Descripcion relacionada con el activo de informacion |
| Valor Vulnerabilidad | Valor cuantitativo para valorar incidencia sobre el activo |
| Nivel Vulnerabilidad | Valor cualitativo para valorar incidencia sobre el activo |

#### Escala de valorizacion de vulnerabilidades

| Nivel | Valor | Criterio de evaluacion |
|-------|-------|----------------------|
| Muy Alto | 5 | Vulnerabilidad expuesta y explotable, su explotacion podria resultar en impactos severos. Es casi certeza que un tercero, error, accidente o acto de la naturaleza pueda explotarla diariamente. |
| Alto | 4 | Vulnerabilidad de gran preocupacion basada en exposicion y facilidad de explotacion y/o gravedad de impactos. Es muy probable que sea explotada mensualmente. |
| Medio | 3 | Vulnerabilidad de preocupacion moderada. Es algo probable que sea explotada al menos una vez por ano. |
| Bajo | 2 | Vulnerabilidad de preocupacion menor, pero la efectividad de la remediacion podria mejorarse. Es improbable que sea explotada al menos una vez al ano. |
| Muy Bajo | 1 | Vulnerabilidad no es motivo de preocupacion. Es muy improbable que sea explotada; ocurre despues de cada 5 anos o mas. |

## Establecimiento del nivel de probabilidad

La probabilidad refiere a la posibilidad de que se materialice un riesgo cuando una amenaza explota una vulnerabilidad. Se debe indicar el nivel de probabilidad considerando la medicion de amenaza y vulnerabilidad.

#### Escala de probabilidad

| Nivel | Valor | Descripcion |
|-------|-------|-------------|
| Muy improbable | 1 | 1% a 10% de seguridad de que se presente en el ano en curso |
| Improbable | 2 | 11% a 30% de seguridad de que se presente en el ano en curso |
| Moderado | 3 | 31% a 65% de seguridad de que se presente en el ano en curso |
| Probable | 4 | 66% a 89% de seguridad de que se presente en el ano en curso |
| Casi certeza | 5 | 90% a 100% de seguridad de que se presente en el ano en curso |

El registro debe ser dual: valor y nivel, ej. "3. Moderado" o "2. Improbable".

## Evaluacion del riesgo

La evaluacion incluye los atributos de seguridad de la informacion y su proteccion, considerando medicion de amenazas, vulnerabilidades y probabilidad de materializacion.

#### Identificacion de consecuencias (cuatro dimensiones de impacto)

| Dimension | Descripcion |
|-----------|-------------|
| Impacto Financiero | Perdidas financieras; recursos necesarios para reemplazar/reparar un activo que se habrian utilizado en otro lugar |
| Impacto Operacional | Impactos a servicios, disponibilidad de recursos operativos ante materializacion del riesgo |
| Impacto Reputacional/Politico | Impacto en reputacion del servicio: credibilidad, profesionalismo, responsabilidad, buena imagen institucional |
| Impacto Normativo | Consecuencias de no cumplir normas establecidas, incluyendo leyes y decretos oficiales |

#### Matriz de evaluacion de impacto (escala 1-5)

| Valor | Nivel | Financiero | Operacional | Reputacional | Normativo |
|-------|-------|------------|-------------|--------------|-----------|
| 5 | Catastrofico | Perdidas financieras con impacto catastrofico en mas del 50% de los procesos. Multas o costos superiores a $25.000.000 | Suspension de operaciones claves generalizada por mas de 4 horas. Perdida de procesos claves y de soporte. Perdida de empleados (>10%). Perdida de clientes (>=10%). Caida en acciones (>10%) | Cobertura negativa generalizada en medios masivos y redes sociales (>=1 semana). Comentarios de Stakeholders claves. Perdida fuertemente de la imagen de la organizacion | Riesgo de incumplimiento muy alto con reguladores y/o clientes con consecuencias muy graves en caso de incumplimiento y/o sanciones economicas, cese definitivo, perdida de licencia, restriccion financiera, juicios. Resolucion judicial con determinacion de multas |
| 4 | Mayor | Perdidas financieras con impacto importante en mas del 30% de los procesos. Multas o costos entre $10.000.000 y hasta $25.000.000 | Suspension de operaciones claves generalizada por mas de 2 horas. Perdida de procesos claves y de soporte. Perdida de empleados (entre 5% y 10%). Perdida de clientes (entre 5% y 10%). Caida en acciones (entre 5% y 10%) | Cobertura negativa generalizada en medios masivos y redes sociales (entre 4 dias y 1 semana). Perdida de Stakeholders empresarial | Riesgo de incumplimiento alto con reguladores y/o clientes con consecuencias graves en caso de incumplimiento y/o sanciones economicas, cese definitivo, perdida de licencia, restriccion financiera, juicio, sanciones administrativas. Resolucion judicial con determinacion de multas |
| 3 | Moderado | Perdidas financieras con impacto moderado en mas del 10% de los procesos. Multas o costos entre $2.000.000 y hasta $5.000.000 | Suspension de operaciones claves generalizada por mas de 1 hora. Perdida de procesos claves y de soporte. Perdida de empleados (entre 1% y 4%). Perdida de clientes (entre 2% y 4%). Caida en acciones (entre 1% y 4%) | Cobertura negativa generalizada en medios masivos y redes sociales (entre 2 a 3 dias). Procesos judiciales o prejudiciales con potencial de acuerdo | Riesgo de incumplimiento con reguladores y/o clientes con consecuencias moderadas. Oficios o reclamos formales |
| 2 | Menor | Perdidas financieras con impacto menor en menos del 10% de los procesos. Multas o costos menores a $2.000.000 | Suspension de operaciones de procesos de soporte por mas de 2 horas. Perdida de empleados (menor al 2%). Perdida de clientes (menor al 2%). Caida en acciones (menor al 1%) | Cobertura aislada o esporadica en medios masivos y redes sociales (menor a 1 dia). Amonestaciones formales o reclamos informales | Riesgo de incumplimiento con reguladores y/o clientes con consecuencias menores. Acuerdos formales de reparacion dentro de lo establecido en regulacion o contractualmente |
| 1 | Insignificante | No genera perdidas financieras ni compromete de ninguna forma la imagen de la organizacion. Sin multa o costo economico relacionado | Suspension de operaciones de procesos de soporte por menos de 1 hora. Sin perdida de continuidad operativa | Cobertura negativa limitada en redes sociales (escasos comentarios), sin menciones en otros medios masivos | Incumplimiento sin efectos en reguladores o clientes |

El registro debe ser dual: valor y nivel, ej. "5. Catastrofico" o "1. Insignificante".

## Riesgo inherente

El riesgo inherente se determina combinando probabilidad e impacto. Se definen 4 zonas de severidad en la matriz de calor.

#### Escalas de probabilidad e impacto

| Valor | Probabilidad | Impacto |
|-------|-------------|---------|
| 5 | Casi certeza | Catastrofico |
| 4 | Probable | Mayor |
| 3 | Moderado | Moderado |
| 2 | Improbable | Menor |
| 1 | Muy improbable | Insignificante |

#### Calculo de severidad

```
Riesgo Inherente = Probabilidad × Impacto
```

El producto de probabilidad e impacto produce valores entre 1 y 25, estableciendo el valor de severidad del riesgo por medio del mapa de calor. Cada combinacion queda en una zona de severidad segun el apetito de riesgo institucional.

**Mapa de calor (Probabilidad x Impacto)**:

| Prob \ Imp | 1 (Insig) | 2 (Menor) | 3 (Moderado) | 4 (Mayor) | 5 (Catastr) |
|------------|-----------|-----------|--------------|-----------|-------------|
| 5 (Casi certeza) | 5 | 10 | 15 | 20 | 25 |
| 4 (Probable) | 4 | 8 | 12 | 16 | 20 |
| 3 (Moderado) | 3 | 6 | 9 | 12 | 15 |
| 2 (Improbable) | 2 | 4 | 6 | 8 | 10 |
| 1 (Muy improbable) | 1 | 2 | 3 | 4 | 5 |

La institucion establece la escala de mapa de calor y apetito del riesgo para determinar zonas de severidad (ej. Bajo: 1-5, Medio: 6-10, Alto: 11-17, Critico: 18-25).

**Campos de registro**: Valor de Severidad del Riesgo (producto probabilidad x impacto). Nivel de Severidad (segun rango del valor de severidad).
