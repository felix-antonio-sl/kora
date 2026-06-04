---
_manifest:
  urn: urn:salud:kb:procedimiento-gobernanza-sgsi
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-011 v01
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- gobernanza
- comite
- direccion
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-gobernanza-sgsi
  salud:
    minsal_id: PROS-NC-011
    minsal_version: '01'
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento de Gobernanza SGSI

**PROS-NC-011 v01, Noviembre 2024.**

## Proposito y alcance

Gobierna la direccion estrategica, supervision ejecutiva y mejora continua del SGSI MINSAL alineando objetivos estrategicos, normativa legal y mejores practicas internacionales.

| Eje | Accion |
|---|---|
| Alineacion | Objetivos estrategicos institucionales, normativa legal, mejores practicas internacionales |
| Definicion estrategica | SGSI |
| Supervision ejecutiva | Alta direccion |
| Roles | Definicion y asignacion de responsabilidades |
| Comunicacion | Gestion de instancias criticas |
| Mejora continua | Ciclo planificar-hacer-verificar-actuar |

Siete subprocesos:

1. **Analisis del Contexto** — levantamiento por Encargado SGSI hasta aprobacion por Direccion
2. **Diseno de Objetivos y Planificacion Estrategica** — propuesta por Encargado SGSI hasta aprobacion por Direccion
3. **Creacion y Actualizacion de Politicas** — propuesta por responsable SGSI hasta aprobacion por Direccion
4. **Definicion de Roles y Responsabilidades** — formulacion del modelo de gobernanza por responsable SGSI hasta aprobacion por Direccion
5. **Comunicaciones** — diseno de mecanismos y comunicaciones criticas por responsable SGSI hasta aprobacion por Direccion
6. **Revision por la Direccion** — definicion de calendario de revisiones, formulacion de acciones correctivas y revision directiva
7. **Tratamiento de No Conformidades** — identificacion, evaluacion, planificacion de acciones de mejora hasta cierre

### Controles ISO 27001:2022 asociados

| Control | Nombre |
|---|---|
| A.04.1 | Comprender la organizacion y su contexto |
| A.05.1 | Politicas para la seguridad de la informacion |
| A.05.2 | Organizacion de la seguridad de la informacion |
| A.05.3 | Responsabilidades de la alta direccion |
| A.05.6 | Gestion de roles y responsabilidades |
| A.06.1 | Acciones para abordar riesgos y oportunidades |
| A.06.2 | Objetivos de seguridad de la informacion y planificacion para lograrlo |
| A.07.4 | Relaciones con las partes interesadas |
| A.08.6 | Monitoreo de cumplimiento de la seguridad de la informacion |

## Terminologia

**Contexto Externo** — entorno fuera de la organizacion: ambiente cultural, social, politico, legal, regulatorio, financiero, tecnologico, economico, natural y competitivo (internacional, nacional, regional, local); factores y tendencias que influyen en objetivos; relaciones con partes interesadas externas, sus percepciones y valores.

**Contexto Interno** — entorno interno: estructura de gobierno (funciones, rendicion de cuentas), politicas, objetivos y estrategias, capacidades (capital, tiempo, personal, procesos, sistemas, tecnologias), sistemas y flujos de informacion (formales e informales), relaciones y percepciones de partes interesadas internas, cultura organizacional, normas y modelos adoptados, alcance contractual.

**Direccion Ejecutiva** — persona o grupo responsable de ejecutar estrategias y politicas para alcanzar objetivos de la mision. Conocida como alta direccion; compuesta por directores generales, directores financieros, directores de informacion y roles similares.

**Gobernanza de la Seguridad de la Informacion** — sistema que permite dirigir y supervisar las actividades de seguridad de la informacion.

**Indicador** — medida que proporciona estimacion o evaluacion de atributos mediante modelo analitico para satisfacer necesidades de informacion especificas.

**Objetivo** — meta o resultado a alcanzar. Estrategico, tactico u operativo. Aplica a finanzas, seguridad, salud, ambiente y a niveles estrategico, organizacional, proyectos, productos, procesos. Puede formularse como resultado, proposito, criterio o meta de seguridad.

**Organizacion** — persona o grupo con funciones, responsabilidad, autoridad y relaciones para alcanzar objetivos. Incluye empresas, corporaciones, entidades gubernamentales, asociaciones (publicas o privadas).

**Organo de Gobierno** — grupo responsable y que rinde cuentas por el desempeno organizacional (ej. consejo de administracion).

**Politica de Seguridad de la Informacion** — documento que define directrices generales, principios y objetivos para proteccion de la informacion.

**Proyecto del SGSI** — actividades estructuradas para implementar un SGSI.

**Seguridad de la Informacion** — preservacion de confidencialidad, integridad y disponibilidad. Incluye autenticidad, responsabilidad, no repudio y fiabilidad.

**Sistema de Gestion** — conjunto de elementos interrelacionados (estructura, roles, responsabilidades, planificacion, operacion) que coordinan politicas, objetivos y procesos. Puede cubrir toda la organizacion, funciones especificas, areas particulares o funciones en un grupo de organizaciones.

## Marco Normativo

| Instrumento | Referencia |
|---|---|
| NCh 15027001:2022 | Seguridad de la informacion, ciberseguridad y proteccion de la privacidad |
| Marco Juridico SSI | Publicado en portal CSIRT del Ministerio del Interior |
| Ley 21.663 | Marco de Ciberseguridad |
| Decreto 273 (2022) | Obligacion de reportar incidentes de ciberseguridad al CSIRT de Gobierno |
| Ley 21.180 | Transformacion Digital del Estado |
| Decreto Supremo N° 7 | Norma Tecnica de Seguridad de la Informacion y Ciberseguridad |

Documentos SGSI disponibles en `isalud.minsal.cl`.

## Estructura de Gobernanza

### Directorio de actores

#### Direccion Ejecutiva (Alta Direccion)

Responsable ultimo del resultado (A) de los subprocesos de gobernanza. Aprueba: analisis del contexto, objetivos estrategicos, politicas, modelo de gobernanza y plan comunicacional. En la Revision por la Direccion comparte responsabilidad de ejecucion y resultado (A/R) con el Comite.

#### Comite de Seguridad de la Informacion (CISO)

Revisa, valida y aprueba: analisis del contexto, objetivos, politicas, procesos, modelo de gobernanza y calendario de sesiones. Responsable del resultado (A) en todos los subprocesos. En Revision por la Direccion comparte ejecucion y resultado (A/R) con la Direccion.

#### Encargado del SGSI

Coordina y ejecuta actividades clave del SGSI:

- Planificacion de analisis internos y externos
- Diseno y actualizacion de politicas de seguridad
- Definicion del modelo de gobernanza y proceso comunicacional
- Preparacion de presentaciones ejecutivas y calendario de sesiones del Comite
- Enlace principal con partes interesadas internas y externas

Responsable de ejecucion (R) en todos los subprocesos.

#### Dueño de Proceso de Gestion Documental

Gestiona registros del SGSI: asignacion de numeros de documento, clasificacion, control de versiones, almacenamiento. Consultado (C) para planificacion, politicas, roles, comunicacion y no conformidades. Informado (I) del analisis del contexto.

#### Departamento de Tecnologias de la Informacion (Jefe TIC)

Apoya implementacion tecnica de medidas del SGSI, supervisa controles tecnologicos en infraestructura, colabora en analisis de riesgos, asegura disponibilidad de herramientas de monitoreo.

#### Propietarios de Activos de Informacion

Representantes de areas clave: identifican y gestionan riesgos de activos bajo su control, implementan medidas de seguridad, participan en sesiones del Comite cuando se requiere. Enlace entre estrategia de seguridad y operaciones diarias.

#### Departamento de Auditoria Interna

Evaluaciones periodicas de conformidad del SGSI con normativas y estandares aplicables. Identifica desviaciones y oportunidades de mejora.

#### Juridica

Participa como area consultada en los subprocesos de gobernanza que requieren validacion normativa.

### Matriz RACI

| Subproceso | Comite (CISO) | Encargado SGSI | Dueño Proceso Documental | Direccion |
|---|---|---|---|---|
| Analisis del Contexto | A | R | I | A |
| Planificacion Estrategica | A | R | C | A |
| Creacion y Actualizacion de Politicas | A | R | C | A |
| Definicion de Roles y Responsabilidades | A | R | C | A |
| Comunicacion | A | R | C | A |
| Revision por la Direccion | A/R | R | C | A/R |
| Tratamiento de No Conformidades | A | R | C | A |

R: Responsable de Ejecutar | A: Responsable del Resultado | C: Consultado | I: Informado

Jefe TIC y Juridica participan como areas consultadas segun corresponda; sus celdas RACI no pudieron recuperarse del documento fuente.

## Toma de Decisiones

### Flujo por subproceso

| Subproceso | Propone | Revisa/Valida | Aprueba |
|---|---|---|---|
| Analisis del Contexto | Encargado SGSI | Comite | Direccion |
| Objetivos y Planificacion | Encargado SGSI | Comite | Direccion |
| Politicas | Encargado SGSI | Comite | Direccion |
| Modelo de Gobernanza | Encargado SGSI | Comite | Direccion |
| Comunicaciones | Encargado SGSI | Comite | Direccion |
| Calendario de Revisiones | Encargado SGSI | Comite | Direccion |
| Acciones Correctivas | Encargado SGSI | Comite | Direccion y Comite (A/R) |

### Escalamiento y excepciones

El Jefe TIC, el CISO o el Comite evaluan y establecen condiciones especificas para excepcion al cumplimiento, siempre que no infrinjan legislacion vigente ni comprometan seguridad de la informacion. Cada excepcion se documenta e inicia un proceso de revision de politica para determinar si se requieren directrices adicionales o modificaciones especificas.

## Comunicaciones y Reportes

### Lineas de reporte

- Encargado SGSI reporta al Comite de Seguridad
- Comite reporta a la Direccion Ejecutiva
- Auditoria Interna reporta hallazgos al Comite y a la Direccion

### Canales de difusion

| Canal | Destino |
|---|---|
| Intranet MINSAL | `http://isalud.minsal.cl` |
| Correo informativo | Funcionarios y partes interesadas |
| Sitio web MINSAL | `http://www.minsal.cl/seguridad_de_la_informacion/` |

## Comite de Seguridad de la Informacion

### Frecuencia

**Al menos una sesion anual.** El Encargado del SGSI prepara el calendario de sesiones y lo somete a aprobacion del Comite.

### Agenda tipica

- Analisis del contexto (PESTEL)
- Revision de objetivos del SGSI
- Estado de politicas de seguridad
- Resultados de auditoria interna
- Indicadores de desempeno
- No conformidades y acciones correctivas
- Cambios en partes interesadas, marco legal o normativo

### Registros

- Agenda y actas de cada sesion
- Planilla de analisis del contexto (PESTEL)
- Informes ejecutivos para alta direccion
- Plan de ciberseguridad y seguridad de la informacion para el sector salud

## Revision por la Direccion (ISO 27001:2022 §9.3)

### Entradas

| Entrada | Origen |
|---|---|
| Estado de acciones de revisiones previas | Actas del Comite |
| Cambios en contexto externo e interno | Analisis PESTEL, partes interesadas |
| Desempeno del SGSI: no conformidades, acciones correctivas | Registro de no conformidades |
| Resultados de monitoreo y medicion | Indicadores (§Metricas) |
| Resultados de auditoria interna | Departamento de Auditoria Interna |
| Oportunidades de mejora continua | Todos los subprocesos |
| Cambios normativos o legales | Juridica, marco normativo |

### Salidas

| Salida | Destino |
|---|---|
| Decisiones de mejora continua | Plan Director, politicas actualizadas |
| Cambios al SGSI | Modelo de gobernanza, politicas, controles |
| Acciones correctivas | Plan de tratamiento de no conformidades |
| Actualizacion de objetivos | Planificacion estrategica |
| Ajuste a recursos | Alta Direccion |

### Periodicidad

Revision definida en calendario aprobado por Direccion y Comite. Vinculada a la sesion anual del Comite de Seguridad como minimo.

## Metricas

| Indicador | Calculo | Frecuencia | Umbral Verde | Umbral Naranja |
|---|---|---|---|---|
| Cumplimiento objetivos SGSI | Objetivos cumplidos / Total planificados x 100% | Anual | ≥80% | <80% |
| Revision de politicas | Politicas revisadas en el año / Total politicas x 100% | Anual | 100% | <100% |
| Frecuencia sesiones Comite | Reuniones realizadas / Reuniones planificadas | Anual | Al menos 1 por año | Ninguna sesion |
| Acciones correctivas a tiempo | Acciones implementadas a tiempo / Total acciones x 100% | Anual | ≥100% | <100% |

## Registros

- Plan de ciberseguridad y seguridad de la informacion para el sector salud
- Actualizacion de politicas y procedimientos del SGSI
- Planilla Analisis de contexto (PESTEL)
- Informes ejecutivos para alta direccion
- Agenda y actas de sesiones del Comite de Seguridad

## Ciclo de Revision

Revision **cada dos años** o ante cambios significativos. Criterios de vigencia:

- Adecuacion al proposito y precision
- Reflejo de cambios tecnologicos
- Alineacion con legislacion vigente, estandares internacionales y mejores practicas

## Excepciones

En situaciones excepcionales, el Jefe TIC, el CISO o el Comite evaluan y establecen condiciones especificas de excepcion al cumplimiento, siempre que:

- No infrinjan legislacion vigente
- No comprometan seguridad de la informacion

Cada excepcion se documenta. Se inicia revision de politica para determinar si se requieren directrices adicionales o modificaciones.

## Control de Versiones

| Version | Fecha | Secciones | Motivo |
|---|---|---|---|
| 01 | Noviembre 2024 | Todas | Creacion del documento |
