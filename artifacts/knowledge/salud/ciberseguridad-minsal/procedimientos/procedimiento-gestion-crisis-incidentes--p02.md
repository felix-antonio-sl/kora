---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-crisis-incidentes-p02
  provenance:
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-012 v01
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- crisis
- incidentes-criticos
- bcp
- drp
lang: es
extensions:
  kora:
    family: note
    minsal_id: PROS-NC-012
    minsal_version: '01'
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-crisis-incidentes
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento Gestión de Crisis por Incidentes de Seguridad - Parte 02

## Anexo B: Criterios de evaluación y clasificación de crisis

### Matriz de niveles por dimensión

| Dimensión | Bajo | Medio | Alto | Muy Alto |
|-----------|------|-------|------|----------|
| **Afectación a las actividades** | Interno: afecta a los sistemas de la organización | Interno: afecta a más del 20% de los sistemas | Interno/Externo: afecta a más del 50% de los sistemas | Externo nacional: afecta a más del 75% de los sistemas. Externo extranjero |
| **Afectación a la seguridad ciudadana** | Sin afectación | Sin afectación | Afectación a la seguridad ciudadana con peligro para personas | Afectación a la seguridad ciudadana con peligro para personas |
| **Afectación a infraestructuras críticas / servicio esencial** | Sin afectación | Sin afectación | Afecta a infraestructura crítica | Afecta a infraestructura crítica |
| **Interrupción del servicio** | Interrupción en la prestación del servicio superior a 1 hora y superior a 5% de usuarios | Interrupción en la prestación del servicio superior a 4 horas y superior a 15% de usuarios | Interrupción en la prestación del servicio superior a 8 horas y superior a 35% de usuarios | Interrupción en la prestación del servicio superior a 12 horas y superior a 50% de usuarios |
| **Recursos para resolver** | Menos de 1 jornada-persona | Entre 1 y 5 jornadas-persona | Entre 5 y 50 jornadas-persona | Entre 50 y 100 jornadas-persona |
| **Impacto económico** | Entre 0.0001% y 0.001% del PIB actual | Entre 0.001% y 0.07% del PIB actual | Entre 0.07% y 0.1% del PIB actual | Superior a 0.1% del PIB actual |
| **Afectación geográfica** | 1 Región | 2 Regiones | 3 Regiones | 4 Regiones o más |
| **Impacto reputacional y mediático** | Sin afectación mediática | Impacto mediático con cobertura en medios de comunicación nacionales | Impacto reputacional con cobertura amplia y continua en medios de comunicación nacionales | Impacto reputacional con cobertura amplia y continua en medios de comunicación nacionales e internacionales. Afecta imagen del país (marca España) |
| **Afectación a procesos críticos** | Sin afectación. Actividad interrumpida por debajo de su capacidad | Con afectación. Recuperación de actividad interrumpida por debajo de su capacidad | Recuperación temporal por encima de su capacidad | Operaciones críticas interrumpidas por encima de su capacidad |
| **Afectación a las relaciones con grupos de interés** | Confianza de los grupos de interés no se ven afectadas | Confianza de los grupos de interés no se ven afectadas | Expectativas de los grupos de interés se verán afectadas de manera considerable | Confianza de los grupos de interés se verán afectadas de manera considerable durante un largo período |
| **Alarma social** | Sin alarma social | Alarma social sin causa justificada | Alarma social con causa justificada | Alarma social con causa justificada |
| **Daños a terceros** | Sin pérdidas o pérdidas insignificantes | Daños moderados | Pérdidas por valor hasta el coste de reposición | Pérdidas por valor hasta el coste de reposición |
| **Pérdidas económicas** | Coste dentro del coste de reposición. Sin implicaciones | Reclamaciones aisladas de terceros y/o indicios de delito | Reclamaciones. Implicaciones legales | Reclamaciones. Implicaciones legales |
| **Implicaciones legales** | Sin implicaciones | Reclamaciones aisladas de terceros y/o indicios de delito | Implicaciones legales | Implicaciones legales |

### Objetivos de recuperación

| Parámetro | Descripción |
|-----------|-------------|
| RTO | Tiempo objetivo de recuperación |
| RPO | Punto objetivo de recuperación |

*Nota: La fuente original no proporciona valores numéricos específicos para RTO y RPO; estos deben definirse por la organización según criticidad de los activos afectados y los niveles de la matriz de evaluación.*
