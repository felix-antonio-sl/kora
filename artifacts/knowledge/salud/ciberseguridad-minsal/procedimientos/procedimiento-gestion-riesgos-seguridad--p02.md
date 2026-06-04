---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-riesgos-seguridad-p02
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
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-riesgos-seguridad
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento Gestion de Riesgos de la Seguridad de la Informacion - Parte 02

## Tratamiento del riesgo

Tomar decisiones frente a los riesgos existentes de acuerdo con la estrategia institucional. Las opciones se seleccionan con base en el resultado de la valoracion del riesgo, el costo esperado de implementacion y los beneficios esperados.

### Opciones de tratamiento

| Opcion | Descripcion |
|--------|-------------|
| **Reduccion del riesgo** | Mediante seleccion de controles, de manera que el riesgo residual se pueda reevaluar como aceptable |
| **Aceptacion/Retencion del riesgo** | Decision de retencion del riesgo sin accion posterior, dependiendo de la evaluacion del riesgo |
| **Evitacion del riesgo** | Evitar la actividad o accion que da origen al riesgo particular |
| **Transferencia del riesgo** | Transferir a otra parte que pueda gestionar mas eficazmente el riesgo particular |

## Aceptacion del riesgo

Decision formal de aceptar riesgos y responsabilidades. Se toma cuando los costos de implementacion de un control sobrepasan el valor del activo a proteger o cuando el nivel del riesgo es muy bajo. En ambos casos la organizacion asume los danos de la materializacion.

### Criterios de aceptacion

- Pueden incluir umbrales multiples, con meta de nivel deseable y disposiciones para que la alta direccion acepte riesgos por encima en circunstancias definidas.
- Se pueden expresar como relacion entre beneficio estimado y riesgo estimado.
- Pueden aplicarse diferentes criterios a diferentes clases de riesgos (ej. riesgos de incumplimiento normativo podrian no ser aceptados).
- Pueden incluir requisitos para tratamiento adicional futuro (ej. aceptar un riesgo si existe aprobacion y compromiso para reducirlo a nivel aceptable en un periodo definido).

### Identificacion de controles existentes

Mantener listado de controles segun planificaciones y Anexo A de NCh-ISO/IEC 27001 (114 controles en 14 dominios). Se deben generar controles adicionales complementarios. Cada control debe tener:

- Identificador
- Nombre del control
- Descripcion del control

### Plan de tratamiento

Para cada activo y su riesgo se debe registrar:

| Campo | Descripcion |
|-------|-------------|
| Opcion de Tratamiento | Reducir, retener, evitar o compartir |
| Controles Aplicados NCh-ISO 27001 | Controles de la norma como medida de gestion |

### Efectividad del control

Se registra en tres dimensiones:

| Dimension | Opciones |
|-----------|----------|
| Oportunidad de aplicacion | Preventivo, Correctivo, Detectivo |
| Periodicidad de aplicacion | Permanente, Periodico, Ocasional |
| Automatizacion del control | Automatico, Semi-automatico, Manual |

La efectividad del control y la exposicion al riesgo se miden cualitativamente a criterio del evaluador, observando los tres factores y deduciendo efectividad y exposicion.

### Madurez del control

#### Niveles de madurez (5 niveles)

| Nivel | Rango | Detalle |
|-------|-------|---------|
| 1. Inicial | 0% - 35% | Pobre: inexistente, inapropiado, ineficaz, inadecuado, irrelevante |
| 2. Repetible | — | — |
| 3. Definido | 36% - 65% | Insuficiente: informal, no escrito, esporadico, parcial, en proceso |
| 4. Gestionado | 66% - 85% | Aceptable: implementado, cumplido, en practica, hecho, preparado, completo |
| 5. Optimizado | 86% - 100% | Sobresaliente: superior, ejemplar, de clase mundial, el mejor de su clase |

#### Clasificacion de solidez del control

| Nivel | Rango | Influencia en probabilidad e impacto |
|-------|-------|-------------------------------------|
| Debil | 0% - 49% | Baja influencia |
| Moderado | 50% - 99% | Influencia parcial |
| Fuerte | 100% | Alta influencia |

### Evaluacion del riesgo residual

Utiliza las mismas mediciones, escalas y criterios que el riesgo inherente. La diferencia radica en que se consideran las mediciones de nivel de madurez y solidez del control para ajustar probabilidad e impacto tratados.

#### Procedimiento de calculo

```
Valor Riesgo Residual = Probabilidad_Tratada × Impacto_Tratado
```

Donde:
- **Probabilidad_Tratada**: probabilidad de ocurrencia del riesgo considerando los nuevos escenarios de madurez definidos para el tratamiento (Nivel de Madurez × Solidez del Control).
- **Impacto_Tratado**: impacto del riesgo considerando los nuevos escenarios de madurez definidos para el tratamiento.

**Riesgo Residual**: se clasifica con la misma tabla y mapa de calor que el riesgo inherente.

#### Escalas de probabilidad e impacto para residual

| Valor | Probabilidad | Impacto |
|-------|-------------|---------|
| 5 | Casi certeza | Catastrofico |
| 4 | Probable | Mayor |
| 3 | Moderado | Moderado |
| 2 | Improbable | Menor |
| 1 | Muy improbable | Insignificante |

## Comunicacion de los riesgos

La informacion sobre riesgos se debe intercambiar y compartir entre quienes toman decisiones y las partes involucradas. Objetivos de la comunicacion:

- Proporcionar seguridad del resultado de la gestion del riesgo.
- Recolectar informacion del riesgo.
- Compartir resultados de la valoracion y presentar el plan de tratamiento.
- Evitar o reducir ocurrencia y consecuencias de brechas por falta de entendimiento mutuo.
- Brindar soporte para la toma de decisiones.
- Obtener conocimientos nuevos sobre seguridad de la informacion.
- Coordinar con otras partes y planificar respuestas para reducir consecuencias de incidentes.
- Dar sentido de responsabilidad acerca de los riesgos a quienes toman decisiones y partes involucradas.
- Mejorar la toma de conciencia.

La coordinacion entre decisores y partes involucradas se logra en el CSI, donde se debate acerca de riesgos, prioridad, tratamiento adecuado y aceptacion.

## Monitoreo y revision

El proceso de gestion del riesgo se debe monitorear, revisar y mejorar continuamente. La organizacion debe garantizar que el proceso y las actividades relacionadas siguen siendo adecuadas en las circunstancias actuales y se cumplen. Toda mejora acordada o accion necesaria para mejorar conformidad se notifica al CSI para asegurar que no se omite ni subestima ningun riesgo o elemento del riesgo.

## Validacion y tratamiento

Dos niveles de validacion:

1. **Primer nivel** — El Oficial de Seguridad de la Informacion valida el analisis de riesgos realizado por los responsables de las distintas areas.
2. **Segundo nivel** — Aceptacion de responsabilidad por el riesgo actual por parte de los propietarios de los riesgos, aprobando la matriz final, el informe de analisis de riesgos y el plan de tratamiento.

El seguimiento de los planes de tratamiento lo realiza el Oficial de Seguridad de la Informacion y, cuando sea necesario, el CSI. El avance de todos los planes de tratamiento es registrado por sus responsables en la planilla elaborada para tal fin.

## Registros

- Matriz de riesgos de seguridad de la informacion de la institucion.
- Informe de analisis de riesgos y plan de tratamientos.
- Acta de aprobacion de la matriz de riesgo de seguridad.

## Difusion

- Publicacion en sitio web MINSAL: http://www.minsal.cl/seguridad_de_la_informacion/
- Publicacion en intranet MINSAL: http://isalud.minsal.cl/
- Correo informativo.

## Periodo de revision

Revision cada **2 anos** por el CSI, o atendiendo necesidades de cambios para garantizar idoneidad, adecuacion y efectividad.

## Referencias

- [1] Politica General de Seguridad de la Informacion — https://www.minsal.cl/seguridad_de_la_informacion/
- [2] Procedimiento de Riesgos de Seguridad de la Informacion (intranet) — http://isalud.minsal.cl/ministerio/dgstic/SGSI/Paginas/default.aspx
- [3] Definicion de riesgo — https://dle.rae.es/riesgo
- NCh-ISO 31000:2018
- NCh-ISO/IEC 27005:2020
- NCh-ISO/IEC 27001:2020

## Control de versiones

| Version | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| v1.0 | Junio 2023 | Pablo Fabres | Creacion del documento |

## Anexo 1: Ejemplos de amenazas tipicas

Ejemplos provenientes de NCh-ISO/IEC 27005:2020, Anexo informativo. Origenes: A = Accidental, D = Deliberada, E = Entorno.

Tipos de amenazas de referencia (catalogo no exhaustivo):

- **Fenomenos fisicos**: fuego, dano por agua, contaminacion, accidente mayor, destruccion de equipamiento, polvo/corrosion/helada.
- **Eventos naturales**: fenomeno climatico, fenomeno sismico, fenomeno volcanico, fenomeno meteorologico, inundacion.
- **Perdida de servicios esenciales**: fallo en suministro de aire acondicionado/agua, fallo en equipamiento de telecomunicaciones.
- **Perturbacion por radiacion**: radiacion electromagnetica, radiacion termica, pulsos electromagneticos.
- **Compromiso de la informacion**: escuchas a escondidas, robo de medios/documentos, recuperacion de medios reciclados/desechados, divulgacion, espionaje remoto, fuga de informacion, manipulacion de hardware/software, alteracion de datos.
- **Fallas tecnicas**: fallo de equipamiento, mal funcionamiento de equipos, saturacion del sistema de informacion, fallo de software, incumplimiento en mantenimiento del sistema.
- **Acciones no autorizadas**: uso no autorizado de equipamiento, copia fraudulenta de software, uso de software falsificado/falso, corrupcion de datos, procesamiento ilegal de datos.
- **Compromiso de funciones**: error de uso, abuso de derechos, usurpacion de derechos, denegacion de acciones, incumplimiento de disponibilidad de personal.

## Anexo 2: Ejemplos de vulnerabilidades

Ejemplos provenientes de NCh-ISO/IEC 27005:2020, Anexo D, D.1. Organizados por tipo:

- **Informacion**: falta de clasificacion de informacion, falta de procedimientos de etiquetado.
- **Usuario**: falta de formacion en seguridad, falta de conciencia de seguridad.
- **Personal**: falta de personal, falta de procedimientos de seleccion de personal, falta de politicas de uso aceptable de activos.
- **Organizacion**: falta de politicas formales de seguridad, falta de procedimientos de auditoria, falta de acuerdos de confidencialidad en contratos con terceros, falta de informes de fallas, falta de registros de sesiones de administrador y operador, falta de politica formal sobre uso de computadores portatiles.
- **Red**: conexiones de red no protegidas, cableado no protegido, falta de identificacion y autenticacion de emisor/receptor, falta de filtrado de trafico, arquitectura de red insegura, transferencia de contraseñas en claro.
- **Hardware**: falta de reemplazo periodico, susceptibilidad a humedad/polvo/suciedad, almacenamiento sin proteccion, sensibilidad a radiacion electromagnetica, falta de copias de seguridad.
- **Software**: interfaz de usuario compleja, falta de facilidades de auditoria, falta de terminacion de sesion, falta de politica de seguridad de software, falta de pruebas de software/documentacion, falta de mecanismos de proteccion de propiedad intelectual.
- **Sistema de informacion**: falta de politicas sobre uso de criptografia, falta de mecanismos de identificacion y autenticacion, falta de proteccion de datos.
