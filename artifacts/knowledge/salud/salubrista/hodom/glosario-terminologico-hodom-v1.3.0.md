---
_manifest:
  urn: urn:salud:kb:hodom-glosario-terminologico
  provenance:
    created_by: Claude Code (Opus 4.7, 1M context) con Felix Sanhueza Luna
    created_at: '2026-05-14'
    updated_at: '2026-05-17'
    sources:
      - urn:salud:kb:hodom-reglamento-ds1-2022
      - urn:salud:kb:hodom-decreto-exento-31-2024
      - urn:salud:kb:hodom-norma-tecnica-2024
      - urn:salud:kb:hodom-direccion-tecnica
version: 1.3.2
status: published
tags:
  - hodom
  - glosario
  - terminologia
  - normativa
  - hospitalizacion-domiciliaria
  - vocabulario-controlado
lang: es
extensions:
  kora:
    family: normative
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:hodom-glosario-terminologico
relations:
  cites:
    - urn:salud:kb:hodom-reglamento-ds1-2022
    - urn:salud:kb:hodom-decreto-exento-31-2024
    - urn:salud:kb:hodom-norma-tecnica-2024
    - urn:salud:kb:hodom-direccion-tecnica
    - urn:salud:kb:salubrista
---

# Glosario Terminológico de Hospitalización Domiciliaria (HODOM)

Vocabulario controlado del dominio HODOM derivado de las fuentes normativas vigentes en Chile:

- **DS 1/2022 MINSAL** — Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria (25 artículos).
- **Acto Exento N° 31/2024 MINSAL** — Aprueba la Norma Técnica HODOM (05-jun-2024, Ministra Ximena Aguilera Sanhueza).
- **NT 2024** — Norma Técnica para Establecimientos que Otorgan Prestaciones de HD (texto anexo al Acto Exento, 16 páginas).

Cada entrada se sujeta a un esquema fijo: `Definición:` (denotativa, obligatoria) y `Fuente:` (cita normativa con artículo, letra o numeral cuando corresponda, obligatoria). Cuando agregan valor: `Sinónimos:`, `Relacionados:`, `Funciones:`, `Notas:`, `Excepciones:`, `Distinción:`, `Requisito profesional:`.

**Excepciones al esquema**: (i) las entradas de la sección 8 (Normativa cruzada citada) son descripciones de fuentes externas y usan prosa libre, sin los campos `Definición:` y `Fuente:`; (ii) las entradas redirectoras conservan la fórmula `→ ver X` y prescinden del campo `Fuente:` (su autoridad es el cambio editorial declarado en el changelog de la versión donde se introdujo la remisión).

**Criterio editorial de armonización**: si dos fuentes tensionan, prevalece **DS 1/2022 > NT 2024 > Acto Exento N° 31/2024**.

## Tabla de contenidos

1. [Sistema y unidades](#1-sistema-y-unidades)
2. [Roles profesionales del Equipo de Salud HD](#2-roles-profesionales-del-equipo-de-salud-hd)
3. [Pacientes, estados y conceptos clínicos](#3-pacientes-estados-y-conceptos-clínicos)
4. [Procesos asistenciales](#4-procesos-asistenciales)
5. [Documentos y registros](#5-documentos-y-registros)
6. [Capacidad operativa](#6-capacidad-operativa)
7. [Procedimientos y exigencias normativas](#7-procedimientos-y-exigencias-normativas)
8. [Normativa cruzada citada](#8-normativa-cruzada-citada)
9. [Índice alfabético](#9-índice-alfabético)
10. [Notas de uso](#10-notas-de-uso)

---

## Changelog v1.2 → v1.3

- **Renombramientos canónicos**: `Médico Cirujano de Atención Directa` → `Médico de Atención Directa`; `Médico Cirujano Regulador` → `Médico Regulador`; `Elaboración de Solicitud de Transferencia a HD` → `Solicitud de Transferencia a HD` (acto y documento se distinguen por contexto); `Realización de Transferencia a HD` → `Transferencia a HD`; `Tramitación de Egreso de HD` → `Egreso de HD`; `Otorgamiento de Consentimiento Informado` → `Suscripción de Consentimiento Informado`; `Equipo de Gestión de Camas` → `Unidad de Gestión de Camas (UGC)`; `Atención de Acciones Emergentes o No Planificadas` → `Atención No Programada`; `Capacidad Operacional Disponible` → `Capacidad Operacional HODOM`; `Reingreso Hospitalario Programado` → `Reingreso Hospitalario`; `Establecimiento que Otorga Prestaciones de Hospitalización Domiciliaria` → `Establecimiento HODOM`; `Unidad o Servicio de Hospitalización Domiciliaria` → `Unidad HODOM`; `Cartera de Prestaciones de HD` → `Cartera de Prestaciones HODOM`. El lema antiguo queda como entrada redirectora salvo cuando el cambio es trivial de forma.
- **Estabilización del marcador `HODOM`** en lemas compuestos: Establecimiento HODOM, Unidad HODOM, Cartera de Prestaciones HODOM, Receta Médica HODOM, Episodio HODOM, Capacidad Operacional HODOM.
- **`HaH`** reclasificado de lema autónomo a sinónimo internacional dentro de `Hospitalización Domiciliaria`.
- **Disolución** de `Coordinación Clínica HD` en tres lemas autónomos: `Seguimiento Clínico`, `Categorización del Paciente` y `Gestión de la Continuidad Asistencial`. Se conserva entrada redirectora.
- **Renombre** de `Reporte de Información Clínico-Asistencial Relevante` a `Registro Evolutivo en Ficha Clínica`. Se conserva entrada redirectora.
- **Desdobles**: `Red de Apoyo Familiar` ↔ `Tutor Responsable`; `Cuidador` ↔ `Tutor Legal`.
- **Fusión**: `Equipamiento Médico` + `Dispositivos de Uso Médico` en una entrada con sinónimo.
- **21 lemas nuevos**: Visita Domiciliaria, Seguimiento Clínico, Categorización del Paciente, Gestión de la Continuidad Asistencial, Receta Médica HODOM, Interconsulta, Plan de Egreso, Indicación Médica de HD, Agudización, Complicación durante HD, Alta Médica por Recuperación, Alta por Cumplimiento del Plan, Renuncia Voluntaria, Fallecimiento en HD, Pase de Visita Diario, Entrega de Turno, Paciente Transferible, Paciente en HD Activa, Paciente Egresado, Episodio HODOM, Diagnóstico Social del Hogar.
- **Anclaje normativo corregido al `DS 1/2022 art. 21 N° N`** para los registros obligatorios (Constancia de Fallecimiento N° 2, Encuesta de Satisfacción Usuaria al Egreso N° 3, Consentimiento Informado N° 4, Carta de Derechos y Deberes N° 5, Formulario de Ingreso N° 6, Plan de Cuidados de Enfermería y Plan Terapéutico N° 8, Reporte de Atención Profesional N° 9, Epicrisis al Alta en el N° correspondiente del art. 21). La v1.2.0 los referenciaba al art. 19 letra X; v1.3 adopta la corrección.
- **Eliminación de modelado OPM** en el cuerpo del glosario (sin URNs `e-*`, deltas `Δ-*`, supuestos `S-*`, refinamientos `RF*`, compromisos `F*`, Unfolds `#N`, subprocesos `SD-1.x`, ni state-expressions explícitas). El glosario es vocabulario normativo, no documento del modelo.
- **Cobertura íntegra de v1.2.0**: se conservan todos los lemas con sustento normativo o de práctica chilena documentada (Prestador en Convenio, Equipo de Salud HD, Otros Profesionales y Técnicos, Radio de Cobertura, Continuidad Asistencial, Documento de Indicaciones para Emergencias, Curso Clínico-Asistencial, Programa de Mantención Preventiva, Botiquín Autorizado, Cadena de Frío Domiciliaria, Plan de Contingencia Operacional, Sanción Sanitaria, Cambio de Director Técnico, Acuerdo de Traslado a Atención Cerrada, Uso Certificado de Desfibrilador, Vacunación del Personal Sanitario, Especialidad Pediátrica o Psiquiátrica, Registro de Prestador Individual, Certificación de Auxiliares por SEREMI, Confidencialidad y Reserva de Datos Sensibles, Ajuste de Procedimientos por Régimen Transitorio).

## Changelog v1.3.0 → v1.3.1

Pasada de auditoría editorial sobre v1.3.0 (2026-05-16). Cambios estrictamente correctivos sobre defectos detectados; sin reescritura de definiciones normativas ni cambio de la frontera del glosario.

- **P0-1 — Regresión en `Equipo de Salud HD`**: se reemplaza la denominación obsoleta "médico cirujano de atención directa, médico cirujano regulador" por los lemas canónicos `Médico de Atención Directa, Médico Regulador` consistentes con el resto del glosario. Se incorpora `Relacionados:` con la dotación completa.
- **P0-2 — Tres entradas redirectoras agregadas en el cuerpo** (estaban prometidas en el índice pero ausentes): `Establecimiento que Otorga Prestaciones de Hospitalización Domiciliaria → ver Establecimiento HODOM`; `Unidad o Servicio de Hospitalización Domiciliaria → ver Unidad HODOM`; `Cartera de Prestaciones de HD → ver Cartera de Prestaciones HODOM`.
- **P0-3 — Desambiguación sistemática de `Solicitud de Transferencia a HD`**: en cada referencia cruzada se agrega el sufijo explícito `(proceso)` cuando la mención refiere al acto del médico tratante, y `(documento)` cuando refiere al flujo documental con estados. Aplicado en `Servicio o Unidad de Atención Cerrada`, `Médico Tratante de Atención Cerrada` (definición y `Relacionados:`), `Indicación Médica de HD` (en `Relacionados:` agregado), `Formulario de Hospitalización Domiciliaria` (`Distinción:`).
- **P0-4 — Inconsistencia formal en el índice**: la entrada `Atención Cerrada` del índice alfabético se simplifica eliminando el paréntesis "(ver Servicio o Unidad de Atención Cerrada)", coherente con su naturaleza de sinónimo declarado en la entrada vigente, no de redirección por renombre.
- **P1-1 — Cinco causales de egreso completadas con `Relacionados:`**: `Alta Médica por Recuperación`, `Alta por Cumplimiento del Plan`, `Fallecimiento en HD`, `Renuncia Voluntaria` y `Alta Disciplinaria` reciben el campo `Relacionados:` con sus enlaces semánticos al sistema de egreso.
- **P1-2 — Hubs centrales completados con `Relacionados:`**: `Equipo de Salud HD`, `Seguimiento Clínico`, `Categorización del Paciente`, `Pase de Visita Diario`, `Entrega de Turno`, `Atención No Programada`, `Tutor Responsable`, `Cuidador` y `Tutor Legal` reciben el campo `Relacionados:`.
- **P1-3 — Reciprocidades cerradas**: `Solicitud de Transferencia a HD (proceso)` agrega `Médico Tratante de Atención Cerrada` a `Relacionados:`; `Cuidador` agrega `Trabajador o Trabajadora Social` (que verifica su disponibilidad).
- **P1-4 — Subprocesos de Evaluación con transición de estado documental**: `Recepción de Solicitud de Transferencia` (`creada → recibida`), `Verificación de Criterios de Ingreso a HD` (`recibida → evaluada`) y `Resolución de Solicitud de Transferencia` (`evaluada → respondida` con cuatro resultados) reciben `Notas:` que articulan la cadena de estados del documento Solicitud.
- **P1-5 — Cadena de estados del paciente completada**: `Paciente en HD Activa` y `Paciente Egresado` reciben `Distinción:` triangular paralela a la de `Paciente Transferible` (que marca su posición en la secuencia Transferible → en HD Activa → Egresado) y `Relacionados:`.
- **P1-6 — Excepciones al esquema declaradas**: en la introducción se agrega un párrafo explícito que documenta las dos excepciones legítimas al esquema fijo `Definición:`/`Fuente:`: (i) las entradas de la sección 8 (Normativa cruzada citada) y (ii) las entradas redirectoras `→ ver X`.

**Cambios no aplicados**: defectos clasificados como P2 por la auditoría (estilísticos, marginales o no críticos para la trazabilidad normativa) se difieren a una pasada posterior y no forman parte de v1.3.1.

## Changelog v1.3.1 → v1.3.2

Pasada de cierre P2 sobre v1.3.1 (2026-05-17). Cambios estrictamente correctivos sobre los hallazgos clasificados como P2 por la auditoría editorial; sin reescritura de definiciones normativas, sin nuevas entradas y sin cambio de la frontera del glosario.

- **P2-1 — Política de referencias cruzadas con sigla**: se documenta en sec. 10 (Notas de uso) que cuando un lema lleva sigla entre paréntesis (p. ej. `Plan de Capacitación Anual (PAC)`, `Unidad de Gestión de Camas (UGC)`, `Sistema de Registro Clínico y Administrativo` con sinónimo `SRCA`), las referencias cruzadas pueden omitir la sigla; el lema sigue siendo unívoco por la parte canónica. No se armoniza literalmente cita por cita; basta la política declarada.
- **P2-2 — Glosa anexa eliminada en redirector `Dispositivos de Uso Médico`**: el paréntesis explicativo que duplicaba la definición canónica de `Equipamiento Médico` se borra. El redirector queda en su forma canónica: "lema fusionado en v1.3.0. → ver Equipamiento Médico."
- **P2-3 — Letras unitarias del índice declaradas como reflejo del corpus**: se agrega en sec. 10 (Notas de uso) una nota corta que explica que las letras del índice alfabético con una sola entrada (B, G, K, N) reflejan vacíos del corpus normativo HODOM y no omisiones del glosario. No se agregan lemas nuevos por simetría visual.
- **P2-4 — Política sobre sinónimos y siglas en el índice alfabético**: se declara explícitamente en sec. 10 (Notas de uso) que los sinónimos y siglas declarados dentro de una entrada (DIGERA, UHD, TENS, CI, PAC, UGC, SRCA, CDD, AC, HD, HDOM, HaH, entre otros) no se replican como entradas independientes en el índice alfabético. El lector que busca por sigla debe consultar el lema canónico al que la sigla refiere.
- **P2-7 — `HaH` removido del índice alfabético**: en coherencia con la política P2-4, se elimina la entrada redirectora `HaH (→ ver Hospitalización Domiciliaria)` del índice. `HaH` permanece como sinónimo internacional dentro de la entrada `Hospitalización Domiciliaria` y allí se localiza.
- **P2-8 — Distinción recíproca entre Indicación Médica de HD y Solicitud de Transferencia a HD (proceso)**: se agrega `Distinción:` en ambas entradas, explicitando que la Indicación Médica es la decisión clínica del Médico Tratante de AC que precede al acto procesal, y la Solicitud de Transferencia a HD (proceso) es el acto institucional posterior que materializa esa decisión en el documento. Una sin la otra no produce transferencia.

**Hallazgos P2 verificados sin acción**: P2-5 (cobertura del art. 19 letras a–l) y P2-6 (consistencia de los pares registro↔proceso) se cierran como verificaciones positivas de v1.3.1 y no requieren modificación al texto.

**Anclajes normativos**: no se tocan; verificados como correctos en la auditoría previa.

---

## 1. Sistema y unidades

### Establecimiento HODOM

- **Definición**: establecimiento de salud de atención cerrada, público o privado; prestador público o privado en convenio con un establecimiento de atención cerrada; o unidad o servicio interno de aquellos, que otorga prestaciones de Hospitalización Domiciliaria bajo Autorización Sanitaria de la SEREMI.
- **Fuente**: DS 1/2022 art. 1 (concepto); art. 2 letras a, b y c (ámbito subjetivo); art. 4 (autorización).
- **Sinónimos**: Establecimiento que Otorga Prestaciones de Hospitalización Domiciliaria.
- **Relacionados**: Unidad HODOM, Servicio o Unidad de Atención Cerrada, SEREMI, Prestador en Convenio, Autorización Sanitaria.
- **Distinción**: el Establecimiento HODOM es la entidad autorizada en su conjunto; la Unidad HODOM es la parte operativa interna que organiza el equipo y los habilitadores.

### Establecimiento que Otorga Prestaciones de Hospitalización Domiciliaria

- **Definición**: lema renombrado en v1.3.0. → ver Establecimiento HODOM.
- **Fuente**: ajuste editorial v1.3.0 (estabilización del marcador HODOM en lemas compuestos).

### Unidad HODOM

- **Definición**: parte interna del Establecimiento HODOM que organiza al Equipo de Salud HD, la Dirección Técnica, el Conocimiento Normativo y Técnico, los registros, los procedimientos técnicos y los protocolos exigidos por la NT 2024 para prestar HD.
- **Fuente**: DS 1/2022 art. 2 letra c; NT 2024 §Ámbito de aplicación.
- **Sinónimos**: Unidad o Servicio de Hospitalización Domiciliaria, Servicio de HD, Unidad HD, UHD.
- **Relacionados**: Equipo de Salud HD, Dirección Técnica, Coordinación.

### Unidad o Servicio de Hospitalización Domiciliaria

- **Definición**: lema renombrado en v1.3.0. → ver Unidad HODOM.
- **Fuente**: ajuste editorial v1.3.0 (estabilización del marcador HODOM en lemas compuestos).

### Servicio o Unidad de Atención Cerrada

- **Definición**: dependencia hospitalaria que provee hospitalización en cama hospitalaria tradicional, desde la cual se origina la Solicitud de Transferencia a HD (proceso) y hacia la cual eventualmente se realiza el Reingreso Hospitalario por inestabilidad clínica o complicaciones.
- **Fuente**: DS 1/2022 art. 1 (modalidad alternativa); art. 16 letra c (causal de egreso por reingreso); art. 8 letra n (coordinación de reingreso por la DT).
- **Sinónimos**: Atención Cerrada, AC.
- **Distinción**: la **Atención Cerrada** se realiza en cama hospitalaria; la **Hospitalización Domiciliaria** se realiza en domicilio bajo régimen hospitalario; la **Atención Domiciliaria** corresponde a régimen ambulatorio de libre elección y queda fuera del DS 1/2022 (art. 3).
- **Relacionados**: Reingreso Hospitalario, Médico Tratante de Atención Cerrada.

### Prestador en Convenio

- **Definición**: prestador público o privado que ha suscrito convenio con un establecimiento de atención cerrada para otorgar HD a sus pacientes derivados.
- **Fuente**: DS 1/2022 art. 2 letra b; NT 2024 §Definiciones ("Prestador de HD en convenio") y §Convenios permitidos.
- **Relacionados**: Convenio con Terceros, Prestador de Hospitalización Domiciliaria en Convenio, ISAPRE, Ley 16.744.

### SEREMI

- **Definición**: Secretaría Regional Ministerial de Salud correspondiente al domicilio de las dependencias administrativas u oficina central del Establecimiento HODOM. Autoridad sanitaria que otorga la Autorización Sanitaria, fiscaliza las actividades del Establecimiento y certifica a los auxiliares de la salud.
- **Fuente**: DS 1/2022 art. 4 (competencia para autorizar), arts. 5–6 (antecedentes y vigencia), art. 24 (fiscalización), art. 10 inciso final (comunicación de cambios de DT); DS 90/2017 (certificación de auxiliares); Código Sanitario Libro X (régimen sancionatorio).
- **Sinónimos**: Autoridad Sanitaria Regional, Seremi de Salud.
- **Relacionados**: Autorización Sanitaria, Fiscalización, Certificación de Auxiliares por SEREMI.

### Servicios de Salud

- **Definición**: instituciones públicas integrantes de la red asistencial del Estado a las que se remite un ejemplar del Acto Exento N° 31/2024 como parte de su distribución operativa.
- **Fuente**: Acto Exento N° 31/2024 §Distribución operativa.
- **Sinónimos**: SS.

### División de Gestión de la Red Asistencial

- **Definición**: división de la Subsecretaría de Redes Asistenciales del MINSAL responsable de publicar el texto íntegro del Acto Exento N° 31/2024 y de la NT 2024 en el sitio institucional del MINSAL, una vez tramitado el acto.
- **Fuente**: Acto Exento N° 31/2024 §Publicación ordenada.
- **Sinónimos**: DIGERA.

### Unidad de Gestión de Camas (UGC)

- **Definición**: unidad institucional del Servicio de Atención Cerrada del hospital que coordina, cuando procede, la asignación, el traslado y la trazabilidad de camas hospitalarias, incluyendo el traslado coordinado del paciente desde la cama hospitalaria al domicilio durante la Transferencia a HD, en contraste con el traslado por medios propios de la Red de Apoyo.
- **Fuente**: práctica operativa hospitalaria chilena; complementa DS 1/2022 art. 8 letra ñ (asegurar traslado oportuno mediante servicio propio o tercero en convenio) y NT 2024 §Equipamiento (servicio de traslado propio o tercero en convenio).
- **Sinónimos**: UGC, Gestión de Camas.
- **Distinción**: la **UGC** pertenece al Servicio de Atención Cerrada del hospital y opera la logística de camas; el **Equipo de Salud HD** es la dotación clínica del Establecimiento HODOM que atiende en domicilio.
- **Relacionados**: Transferencia a HD, Reingreso Hospitalario, Red de Apoyo Familiar.

### Equipo de Gestión de Camas

- **Definición**: lema renombrado en v1.3.0. → ver Unidad de Gestión de Camas (UGC).

### Equipo de Salud HD

- **Definición**: dotación clínica del Establecimiento HODOM compuesta por la dotación mínima del art. 13 del DS 1/2022 (Médico de Atención Directa, Médico Regulador, enfermero o enfermera clínica, kinesiólogo o kinesióloga, auxiliar paramédico o técnico de enfermería, trabajador o trabajadora social) y, según cartera, otros profesionales y técnicos.
- **Fuente**: DS 1/2022 art. 13 letras a–f y art. 14.
- **Distinción**: no comprende a la Dirección Técnica ni a la Coordinación (cargos del art. 7 y art. 11, respectivamente), aunque ambos cargos articulan al equipo.
- **Relacionados**: Dirección Técnica, Coordinación, Médico de Atención Directa, Médico Regulador, Enfermero o Enfermera Clínica, Kinesiólogo o Kinesióloga, Técnico de Enfermería, Trabajador o Trabajadora Social, Otros Profesionales y Técnicos.

### Cartera de Prestaciones HODOM

- **Definición**: listado formal de prestaciones que el Establecimiento HODOM brinda en domicilio, declarado entre los antecedentes de la solicitud de Autorización Sanitaria. La necesidad de una prestación no incluida en la cartera configura **exclusión categórica** de ingreso (art. 17 letra c).
- **Fuente**: DS 1/2022 art. 5 letra n (antecedente exigido); art. 17 letra c (causal de exclusión); NT 2024 §Equipamiento (instrumentos adicionales según cartera).
- **Sinónimos**: Cartera de Prestaciones de HD, Listado de Prestaciones, Oferta de Prestaciones HODOM.

### Cartera de Prestaciones de HD

- **Definición**: lema renombrado en v1.3.0. → ver Cartera de Prestaciones HODOM.
- **Fuente**: ajuste editorial v1.3.0 (estabilización del marcador HODOM en lemas compuestos).

---

## 2. Roles profesionales del Equipo de Salud HD

### Dirección Técnica

- **Definición**: cargo obligatorio y unipersonal del Establecimiento HODOM, desempeñado por médico cirujano habilitado en el Registro de Prestador Individual de la Superintendencia de Salud (o con título revalidado o reconocido), con formación de postítulo o postgrado en gestión en salud y curso vigente de prevención de IAAS de 80 horas, jornada mínima de 22 horas semanales informada a la SEREMI. Es legalmente responsable de la organización y funcionamiento del Establecimiento y de las actividades técnicas y administrativas desarrolladas en él.
- **Fuente**: DS 1/2022 arts. 7, 8, 9 y 10; NT 2024 §Habilitación del personal (Dirección Técnica) y §Requisitos resumidos por cargo.
- **Sinónimos**: DT, Director Técnico, Directora Técnica.
- **Funciones (DS 1/2022 art. 8 letras a–p)**: representar al Establecimiento ante las autoridades de salud; aprobar manuales y procedimientos internos y velar por su actualización conforme a evidencia científica; aprobar funciones, jornada y sistema de turnos; velar por vacunación del personal sanitario conforme a programas MINSAL; mantener stock de insumos y medicamentos según la cartera; verificar programas preventivos y de reparación de maquinarias, equipos y vehículos; dotar al personal de elementos de protección personal; velar por el cumplimiento del Programa IAAS; cautelar el cumplimiento de la prestación ofrecida en información, cobertura y tiempo de respuesta; mantener registros clínicos íntegros y emitir certificados; velar por confidencialidad e información reservada; coordinar con instituciones derivadoras y médicos tratantes; coordinar agudización y reingreso hospitalario; asegurar traslado oportuno a Atención Cerrada; participar en gestión de calidad y auditorías; gestionar el programa de capacitación continua; resolver el alta disciplinaria del art. 16 letra f.
- **Notas**: todo cambio de Director Técnico debe comunicarse de forma inmediata a la SEREMI (DS 1/2022 art. 10 inciso final).
- **Relacionados**: Coordinación, Manual de Organización Interna, Plan de Capacitación Anual, Cambio de Director Técnico, Registro de Prestador Individual.

### Coordinación

- **Definición**: cargo institucional del Establecimiento HODOM, ejercido por un profesional de la salud (preferentemente enfermero o enfermera, conforme NT 2024) con 5 años de experiencia clínica, formación en gestión en salud y curso de prevención de IAAS de al menos 80 horas, con vigencia máxima de 5 años.
- **Fuente**: DS 1/2022 art. 11; NT 2024 §Habilitación del personal (Coordinación) y §Criterio armonizado sobre Coordinación.
- **Sinónimos**: Coordinador, Coordinadora del Establecimiento.
- **Funciones (DS 1/2022 art. 11 letras a–g)**: supervisar la actualización del manual de organización interna, normas y procedimientos; supervisar los procesos clínicos de HD y el respaldo de sus registros; gestionar el personal garantizando continuidad asistencial; supervisar la calidad de los cuidados; gestionar insumos operacionales, mantenciones preventivas y reparación de equipos; mantener el programa de inducción del personal y gestionar capacitaciones; coordinar la continuidad de la atención con establecimientos públicos o privados.
- **Distinción**: la **Coordinación** es un cargo institucional con funciones del art. 11; el **Seguimiento Clínico** es un proceso asistencial transversal del episodio.
- **Notas**: el curso de RCP de 3 horas **no sustituye** el requisito de IAAS de 80 horas; sólo aplica como exigencia adicional si la persona ejerce funciones clínicas directas (NT 2024 §Criterio armonizado).
- **Relacionados**: Dirección Técnica, Enfermera Coordinadora de HD, Seguimiento Clínico.

### Médico de Atención Directa

- **Definición**: integrante del Equipo de Salud HD, médico cirujano con experiencia mínima de 2 años en manejo de patologías médico-quirúrgicas, con cursos vigentes de IAAS de 80 horas, soporte vital básico / RCP de 3 horas y uso certificado de desfibrilador (vigencia 5 años cada certificación).
- **Fuente**: DS 1/2022 art. 13 letra a; NT 2024 §Habilitación y §Requisitos resumidos por cargo.
- **Requisito profesional**: médico cirujano con al menos 2 años de experiencia en patologías médico-quirúrgicas.
- **Sinónimos**: M.AD, Médico AD, Médico de HD.
- **Funciones (DS 1/2022 art. 13 letra a)**: supervisar las actividades asistenciales en domicilio; gestionar oferta y demanda del Establecimiento; apoyar técnicamente al equipo en atención directa; coordinar continuidad de atención con establecimientos públicos o privados; reforzar indicaciones médicas y del personal a paciente, familia y cuidadores; participar en la evaluación de pacientes hospitalizados para decidir ingreso y egreso a HD; evaluar e indicar tratamiento a pacientes hospitalizados en domicilio; emplear tecnologías de información y comunicación con fines de diagnóstico, tratamiento, prevención y rehabilitación.
- **Distinción**: el **Médico de Atención Directa** atiende presencialmente en domicilio durante el episodio HD; el **Médico Regulador** opera la regulación clínica (puede atender a distancia o ser la misma persona); el **Médico Tratante de AC** pertenece al hospital de origen y no es parte del Equipo de Salud HD.

### Médico Cirujano de Atención Directa

- **Definición**: lema renombrado en v1.3.0. → ver Médico de Atención Directa.

### Médico Regulador

- **Definición**: integrante del Equipo de Salud HD, médico cirujano con experiencia mínima de 2 años **en regulación médica** (no sustituible por experiencia médico-quirúrgica general), con cursos vigentes de IAAS de 80 horas, soporte vital básico / RCP de 3 horas y uso certificado de desfibrilador. Presta atención a distancia o atención directa durante la HD.
- **Fuente**: DS 1/2022 art. 13 letra b; NT 2024 §Requisitos resumidos por cargo; Acto Exento N° 31/2024 §Criterio de armonización (no sustitución por experiencia médico-quirúrgica general).
- **Requisito profesional**: médico cirujano con al menos 2 años de experiencia en regulación médica.
- **Sinónimos**: M.Reg, Médico Regulador HD.
- **Notas**: el mismo profesional del Médico de Atención Directa puede cumplir simultáneamente esta función (DS 1/2022 art. 13 letra b inciso final). Puede emplear tecnologías de información y comunicación con el mismo alcance clínico del Médico de Atención Directa.

### Médico Cirujano Regulador

- **Definición**: lema renombrado en v1.3.0. → ver Médico Regulador.

### Enfermero o Enfermera Clínica

- **Definición**: integrante del Equipo de Salud HD, enfermero o enfermera con experiencia clínica mínima de 2 años, curso vigente de soporte vital básico, curso vigente de IAAS de 80 horas y certificación vigente de uso de desfibrilador.
- **Fuente**: DS 1/2022 art. 13 letra c; NT 2024 §Habilitación y §Requisitos resumidos por cargo.
- **Requisito profesional**: 2 años de experiencia clínica y curso vigente de Soporte Vital Básico.
- **Sinónimos**: Enfermera Clínica, Enf.Clínica.
- **Funciones (DS 1/2022 art. 13 letra c)**: participar en la evaluación de pacientes hospitalizados para gestionar ingreso y egreso; evaluar al paciente en cada Visita Domiciliaria con instrumentos acordes para visualizar evolución y flujos de derivación; gestionar cuidados mediante el Plan de Cuidados de Enfermería y la ejecución del Plan Terapéutico y de Cuidados según complejidad; educar a paciente, familia y cuidadores sobre plan terapéutico y autocuidado.
- **Relacionados**: Plan de Cuidados de Enfermería, Visita Domiciliaria.

### Enfermera Coordinadora de HD

- **Definición**: forma de ejercicio de la Coordinación cuando este cargo es asumido por enfermería, modalidad preferente declarada por la NT 2024. Opera la articulación operativa del proceso (recepción de solicitudes, verificación territorial, voluntariedad inicial, logística).
- **Fuente**: DS 1/2022 art. 11; NT 2024 §Habilitación del personal (preferencia enfermería); práctica operativa nacional.
- **Sinónimos**: Enf.Coord HD, Coordinadora de HD.
- **Distinción**: el **rol de Enfermera Coordinadora** ejerce la Coordinación (cargo de gestión); el **rol de Enfermero o Enfermera Clínica** es un cargo asistencial del Equipo de Salud HD (art. 13 letra c). No deben confundirse.
- **Relacionados**: Coordinación, Enfermero o Enfermera Clínica.

### Kinesiólogo o Kinesióloga

- **Definición**: integrante del Equipo de Salud HD, kinesiólogo o kinesióloga con experiencia clínica mínima de 2 años, curso vigente de soporte vital básico, curso vigente de IAAS de 80 horas y certificación vigente de uso de desfibrilador. Otorga terapias motoras y respiratorias en domicilio.
- **Fuente**: DS 1/2022 art. 13 letra d; NT 2024 §Requisitos resumidos por cargo.
- **Requisito profesional**: 2 años de experiencia clínica y Soporte Vital Básico vigente.
- **Sinónimos**: Kine, Kinesiólogo HD.

### Técnico de Enfermería

- **Definición**: integrante técnico del Equipo de Salud HD, en una de tres categorías equivalentes: auxiliar paramédico de enfermería, técnico de nivel medio de enfermería o técnico de nivel superior de enfermería. Experiencia clínica mínima de 1 año, curso vigente de soporte vital básico, curso vigente de IAAS de 80 horas y certificación vigente de uso de desfibrilador. Los auxiliares paramédicos requieren certificación vigente de la SEREMI conforme al DS 90/2017.
- **Fuente**: DS 1/2022 art. 13 letra e; NT 2024 §Habilitación del personal (auxiliares) y §Requisitos resumidos por cargo; DS 90/2017.
- **Requisito profesional**: técnico de nivel medio o nivel superior de enfermería, o auxiliar paramédico certificado por SEREMI (DS 90/2017), con 1 año de experiencia y Soporte Vital Básico vigente.
- **Sinónimos**: TENS, Auxiliar Paramédico de Enfermería, Técnico Paramédico.
- **Funciones (DS 1/2022 art. 13 letra e)**: cumplir el Plan de Cuidados de Enfermería y el Plan Terapéutico y de Cuidados, dentro de la competencia definida por enfermería clínica.

### Trabajador o Trabajadora Social

- **Definición**: integrante del Equipo de Salud HD a cargo de la dimensión social del episodio.
- **Fuente**: DS 1/2022 art. 13 letra f.
- **Sinónimos**: Asistente Social, T.Social.
- **Funciones (DS 1/2022 art. 13 letra f)**: elaborar el Diagnóstico Social del Hogar (vivienda, servicios sanitarios básicos, acceso a telefonía y accesos viales); verificar la disponibilidad de Cuidador o Tutor Legal; evaluar la situación económica del grupo familiar; confeccionar el informe y seguimiento de evaluación e intervención social; elaborar el informe social; colaborar en la gestión y coordinación de derivaciones; participar en reuniones del equipo clínico.
- **Relacionados**: Diagnóstico Social del Hogar, Red de Apoyo Familiar, Cuidador.

### Fonoaudiólogo o Fonoaudióloga

- **Definición**: profesional adicional del Equipo de Salud HD que el Establecimiento HODOM incorpora según la Cartera de Prestaciones ofrecida al paciente y su familia.
- **Fuente**: DS 1/2022 art. 14 inciso primero (otros profesionales y técnicos según prestaciones).
- **Sinónimos**: Fono.

### Otros Profesionales y Técnicos

- **Definición**: profesionales o técnicos adicionales —fonoaudiólogo, nutricionista, terapeuta ocupacional, psicólogo u otros— que el Establecimiento HODOM puede incorporar al Equipo de Salud HD según la Cartera de Prestaciones ofrecida al paciente y su familia.
- **Fuente**: DS 1/2022 art. 14 inciso primero.
- **Sinónimos**: profesionales de cartera ampliada.

### Médico Tratante de Atención Cerrada

- **Definición**: médico del Servicio de Atención Cerrada de origen, responsable del paciente hospitalizado en cama hospitalaria. Origina la Solicitud de Transferencia a HD (proceso) usando el Formulario de Hospitalización Domiciliaria como plantilla; mantiene comunicación activa con la Dirección Técnica del Establecimiento HODOM para coordinar Agudización y Reingreso Hospitalario.
- **Fuente**: DS 1/2022 art. 8 letras m y n (coordinación a cargo de la DT con el médico tratante); art. 11 letra g (coordinación de la Coordinación con establecimientos derivadores); práctica operativa hospitalaria.
- **Sinónimos**: M.Tratante AC.
- **Distinción**: el **Médico Tratante de AC** pertenece al hospital de origen y no es parte del Equipo de Salud HD; el **Médico de Atención Directa** y el **Médico Regulador** sí lo son.
- **Relacionados**: Solicitud de Transferencia a HD (proceso), Reingreso Hospitalario.

### Personal Administrativo y Auxiliar

- **Definición**: personal no clínico del Establecimiento HODOM que cumple las actividades administrativas y auxiliares que defina la Dirección Técnica.
- **Fuente**: DS 1/2022 art. 14 inciso segundo.

---

## 3. Pacientes, estados y conceptos clínicos

### Paciente

- **Definición**: persona destinataria del proceso de Hospitalización Domiciliaria, en una de las dos categorías clínicas reconocidas por la NT 2024 —paciente agudo o paciente crónico reagudizado—, que cumple los Requisitos de Ingreso a HD y permanece bajo control y plan terapéutico del Equipo de Salud HD hasta el Egreso de HD.
- **Fuente**: NT 2024 §Definiciones; DS 1/2022 art. 1 (ámbito subjetivo) y art. 15 (requisitos de ingreso).
- **Relacionados**: Paciente Transferible, Paciente en HD Activa, Paciente Egresado.

### Paciente Agudo

- **Definición**: persona sin patología previa, con cuadro clínico agudo que requiere hospitalización para recuperar la salud.
- **Fuente**: NT 2024 §Definiciones.

### Paciente Crónico Reagudizado

- **Definición**: persona con patología previa y cuadro clínico agudo —asociado o no a esa patología de base— que requiere hospitalización para recuperar la salud.
- **Fuente**: NT 2024 §Definiciones.

### Paciente Transferible

- **Definición**: estado clínico-administrativo del paciente hospitalizado en Atención Cerrada que cumple los cuatro Requisitos de Ingreso a HD del art. 15 y por tanto es susceptible de Transferencia a HD.
- **Fuente**: derivado de DS 1/2022 art. 15.
- **Distinción**: **Transferible** es estado previo a la Transferencia; **en HD Activa** es estado durante el episodio; **Egresado** es estado tras el Egreso de HD.

### Paciente en HD Activa

- **Definición**: estado clínico-administrativo del paciente durante el Episodio HODOM, entre la Transferencia a HD exitosa y el Egreso de HD.
- **Fuente**: derivado de DS 1/2022 art. 1; art. 16.
- **Distinción**: **Transferible** es estado previo a la Transferencia; **en HD Activa** es el estado actual durante el episodio; **Egresado** es estado tras el Egreso de HD.
- **Relacionados**: Transferencia a HD, Episodio HODOM, Visita Domiciliaria, Plan Terapéutico y de Cuidados.

### Paciente Egresado

- **Definición**: estado clínico-administrativo del paciente al término del Episodio HODOM por cualquiera de las seis Causales de Egreso del art. 16.
- **Fuente**: DS 1/2022 art. 16.
- **Distinción**: **Transferible** es estado previo a la Transferencia; **en HD Activa** es estado durante el episodio; **Egresado** es el estado final tras el Egreso de HD.
- **Relacionados**: Egreso de HD, Causales de Egreso, Epicrisis al Alta, Encuesta de Satisfacción Usuaria al Egreso.

### Condición Clínica Estable

- **Definición**: equilibrio de las funciones vitales que permite el traslado del paciente al domicilio pese a una patología no resuelta o sólo parcialmente solucionada. Requisito de ingreso a HD.
- **Fuente**: NT 2024 §Definiciones; DS 1/2022 art. 15 letra a.

### Agudización

- **Definición**: empeoramiento clínico significativo del paciente durante el Episodio HODOM, no necesariamente atribuible a una complicación, que exige reevaluación por el Equipo de Salud HD y eventual escalamiento a Atención Cerrada.
- **Fuente**: DS 1/2022 art. 8 letra l (coordinación de agudización y reingreso); art. 16 letra c.
- **Distinción**: la **Agudización** es deterioro clínico (eje fisiopatológico); la **Complicación durante HD** es evento adverso o intercurrencia (eje causal); ambas pueden detonar Reingreso Hospitalario.

### Complicación durante HD

- **Definición**: evento adverso o intercurrencia clínica durante el Episodio HODOM (infección, sangrado, descompensación de comorbilidad, eventos relacionados con el procedimiento) que se gestiona dentro del proceso o que detona Reingreso Hospitalario según gravedad.
- **Fuente**: DS 1/2022 art. 8 letra l; art. 16 letra c.

### Red de Apoyo Familiar

- **Definición**: red personal colectiva del paciente (familia, allegados, vecinos) a cargo de su cuidado, compañía y sostén en el domicilio durante el Episodio HODOM. Su existencia y disponibilidad efectiva son requisito de ingreso a HD y son verificadas por el o la Trabajador Social.
- **Fuente**: DS 1/2022 art. 15 letra c; art. 13 letra f.
- **Sinónimos**: Red de Apoyo.
- **Relacionados**: Tutor Responsable, Cuidador, Tutor Legal, Diagnóstico Social del Hogar.
- **Distinción**: la **Red de Apoyo Familiar** es colectiva; el **Tutor Responsable** es la figura individual nominada como referente del paciente ante el equipo.

### Red de Apoyo Familiar, Social o Tutor Responsable

- **Definición**: lema desdoblado en v1.3.0. → ver Red de Apoyo Familiar y Tutor Responsable.

### Tutor Responsable

- **Definición**: persona individual nominada como referente del paciente ante el Equipo de Salud HD cuando el paciente no puede ejercer por sí mismo la representación operativa del proceso. Requisito de ingreso alternativo o complementario a la Red de Apoyo Familiar.
- **Fuente**: DS 1/2022 art. 15 letra c.
- **Distinción**: el **Tutor Responsable** es figura referencial ante el equipo de salud; el **Tutor Legal** es figura jurídica con representación formal del paciente.
- **Relacionados**: Red de Apoyo Familiar, Cuidador, Tutor Legal.

### Cuidador

- **Definición**: persona que ejerce la función práctica de cuidado directo del paciente en el domicilio durante el Episodio HODOM. Su disponibilidad es verificada por el o la Trabajador Social como parte del Diagnóstico Social del Hogar.
- **Fuente**: DS 1/2022 art. 13 letra f; art. 15 letra c.
- **Distinción**: el **Cuidador** realiza función práctica de cuidado en el domicilio; el **Tutor Legal** puede o no ser cuidador y opera en el plano jurídico.
- **Relacionados**: Tutor Responsable, Tutor Legal, Red de Apoyo Familiar, Diagnóstico Social del Hogar, Trabajador o Trabajadora Social.

### Cuidador / Tutor Legal

- **Definición**: lema desdoblado en v1.3.0. → ver Cuidador y Tutor Legal.

### Tutor Legal

- **Definición**: persona con representación legal formal del paciente (curador, tutor judicial o equivalente) habilitada para suscribir el Consentimiento Informado y otros actos jurídicos en nombre del paciente.
- **Fuente**: DS 1/2022 art. 15 letra d; Ley 20.584.
- **Sinónimos**: Representante Legal.
- **Relacionados**: Tutor Responsable, Cuidador, Consentimiento Informado, Suscripción de Consentimiento Informado.

### Domicilio del Paciente

- **Definición**: residencia del paciente que cumple condiciones sanitarias mínimas, servicios básicos y telefonía, situada dentro del Radio de Cobertura del Establecimiento HODOM. Requisito de ingreso a HD.
- **Fuente**: DS 1/2022 art. 15 letra b.
- **Relacionados**: Coordenadas del Domicilio, Radio de Cobertura, Diagnóstico Social del Hogar.

### Radio de Cobertura

- **Definición**: área geográfica dentro de la cual el Establecimiento HODOM garantiza factibilidad de acceso para la atención en domicilio, declarada en el contexto de los vehículos de transporte y la cartera. La residencia del paciente debe encontrarse dentro de él para configurar el requisito de ingreso de la letra b del art. 15.
- **Fuente**: DS 1/2022 art. 15 letra b (referencia textual); NT 2024 §Equipamiento (vehículos de transporte y radio operativo).
- **Relacionados**: Domicilio del Paciente, Coordenadas del Domicilio, Vehículos de Transporte.

### Diagnóstico Social del Hogar

- **Definición**: informe del Trabajador o Trabajadora Social que caracteriza la vivienda, los servicios sanitarios básicos, la telefonía, los accesos viales, la disponibilidad de Cuidador o Tutor Legal y la situación socioeconómica del grupo familiar del paciente. Insumo de la Verificación de Criterios de Ingreso.
- **Fuente**: DS 1/2022 art. 13 letra f.
- **Sinónimos**: Informe Social del Hogar.

### Episodio HODOM

- **Definición**: unidad temporal y administrativa de hospitalización domiciliaria, que comienza con la Transferencia a HD del paciente y termina con el Egreso de HD por una de las seis Causales del art. 16. Es la unidad mínima de agregación documental de los registros formales obligatorios.
- **Fuente**: DS 1/2022 art. 1; art. 16; art. 21.
- **Sinónimos**: Episodio de HD.

---

## 4. Procesos asistenciales

### Hospitalización Domiciliaria

- **Definición**: modalidad asistencial alternativa a la hospitalización tradicional en atención cerrada, dirigida a pacientes agudos o crónicos reagudizados, en la que el usuario recibe cuidados similares en calidad y cantidad a los otorgados en establecimientos hospitalarios, sin los cuales habría sido necesaria su permanencia en atención cerrada; requiere indicación médica, control médico, un plan terapéutico del equipo de salud y término por egreso.
- **Fuente**: DS 1/2022 art. 1 incisos primero y segundo; NT 2024 §Definiciones.
- **Sinónimos**: HD, HDOM, HaH (Hospital at Home, designación internacional), Hospitalización en Domicilio.
- **Distinción**: la **HD** es régimen hospitalario en domicilio; la **Atención Cerrada** es régimen hospitalario en cama hospitalaria; la **Atención Domiciliaria** es régimen ambulatorio de libre elección, no regida por el DS 1/2022 (art. 3).

### Atención Domiciliaria

- **Definición**: acciones de salud realizadas en domicilio por prestadores en modalidad **ambulatoria y de libre elección**. **No constituye** Hospitalización Domiciliaria y se encuentra expresamente excluida del ámbito del DS 1/2022.
- **Fuente**: NT 2024 §Definiciones; DS 1/2022 art. 3 (exclusión expresa).
- **Distinción**: ver "Hospitalización Domiciliaria".

### Indicación Médica de HD

- **Definición**: decisión clínica del Médico Tratante de Atención Cerrada que indica el ingreso del paciente a la modalidad de Hospitalización Domiciliaria por cumplir Condición Clínica Estable, factibilidad terapéutica en domicilio y Requisitos de Ingreso a HD.
- **Fuente**: DS 1/2022 art. 1 (componente estructural de la HD); art. 15.
- **Distinción**: la Indicación Médica de HD es la **decisión clínica** del Médico Tratante de Atención Cerrada que precede al acto procesal. La Solicitud de Transferencia a HD (proceso) es el **acto institucional posterior** que materializa esa decisión en el documento Solicitud. Una sin la otra no produce transferencia: sin Indicación Médica previa no hay legitimidad clínica para iniciar el proceso documental.
- **Relacionados**: Solicitud de Transferencia a HD (proceso), Médico Tratante de Atención Cerrada, Requisitos de Ingreso a HD.

### Atención Profesional

- **Definición**: cada acción asistencial individual ejecutada en domicilio por un integrante del Equipo de Salud HD durante una Visita Domiciliaria (consulta médica, kinesiterapia motora o respiratoria, curaciones, administración de medicamentos, evaluación de enfermería, educación al paciente y cuidador, intervención social, otros).
- **Fuente**: DS 1/2022 art. 13 (funciones por cargo); art. 21 N° 9 (registro descriptivo del proceso asistencial).

### Visita Domiciliaria

- **Definición**: acto unitario en que un integrante del Equipo de Salud HD se presenta físicamente en el Domicilio del Paciente para ejecutar una o más Atenciones Profesionales según el Plan Terapéutico y de Cuidados.
- **Fuente**: DS 1/2022 art. 13; NT 2024 §Protocolos clínicos (programación de rutas y visitas domiciliarias).
- **Distinción**: la **Visita Domiciliaria** es el acto presencial unitario; la **Atención Profesional** es la acción asistencial específica realizada durante la visita; el **Seguimiento Clínico** es el proceso longitudinal del Episodio HODOM.

### Solicitud de Transferencia a HD (proceso)

- **Definición**: acto del Médico Tratante de Atención Cerrada por el cual origina el proceso de transferencia mediante la generación del documento Solicitud de Transferencia a HD, usando el Formulario de Hospitalización Domiciliaria como plantilla, con el contenido mínimo aplicable de los registros del art. 21 del DS 1/2022.
- **Fuente**: DS 1/2022 art. 15; art. 21; práctica operativa hospitalaria.
- **Distinción**: el proceso supone una Indicación Médica de HD previa (decisión clínica del Médico Tratante de Atención Cerrada). Sin Indicación no hay legitimidad clínica para iniciar el proceso documental: la Indicación es la decisión clínica anterior; este proceso es el acto institucional que la materializa en el documento Solicitud.
- **Notas**: el acto procesal de Solicitud y el documento Solicitud se distinguen por el contexto; cuando se requiere precisión, usar "acto de Solicitud" para el proceso y "documento Solicitud" para la instancia documental.
- **Relacionados**: Solicitud de Transferencia a HD (documento), Formulario de Hospitalización Domiciliaria, Médico Tratante de Atención Cerrada.

### Elaboración de Solicitud de Transferencia a HD

- **Definición**: lema renombrado en v1.3.0. → ver Solicitud de Transferencia a HD (proceso).

### Evaluación de Solicitud de Transferencia a HD

- **Definición**: proceso por el cual el Equipo de Salud HD examina la Solicitud y resuelve sobre el ingreso del paciente. Se realiza en tres etapas operativas sucesivas: recepción, verificación de criterios y resolución.
- **Fuente**: DS 1/2022 art. 13 letra a (participación del Médico AD en evaluación de pacientes para ingreso y egreso); art. 13 letra c (idem para Enfermero o Enfermera Clínica); art. 15 (requisitos); art. 17 (exclusiones); práctica operativa.
- **Relacionados**: Recepción de Solicitud de Transferencia, Verificación de Criterios de Ingreso a HD, Resolución de Solicitud de Transferencia.

### Recepción de Solicitud de Transferencia

- **Definición**: primera etapa operativa de la Evaluación; la Solicitud entra al canal institucional del Establecimiento HODOM y queda formalmente recibida para su revisión. Habitualmente ejecutada por la Enfermera Coordinadora de HD.
- **Fuente**: práctica operativa hospitalaria.
- **Notas**: transición del estado del documento: `creada → recibida`.

### Verificación de Criterios de Ingreso a HD

- **Definición**: segunda etapa operativa de la Evaluación; contraste de los antecedentes del paciente contra los cuatro Requisitos de Ingreso del art. 15 (clínico, residencial, red de apoyo, consentimiento) y las cuatro Exclusiones del art. 17 (inestabilidad clínica o sin diagnóstico; salud mental descompensada; prestación no incluida en cartera; alta disciplinaria previa). Incluye dimensiones concurrentes: la clínica, a cargo del médico (Regulador o de Atención Directa); y las dimensiones territorial, red de apoyo, voluntariedad y logística, a cargo de la Enfermera Coordinadora con apoyo del o de la Trabajador Social.
- **Fuente**: DS 1/2022 art. 15 letras a–d; art. 17 letras a–d; art. 13 letras a, c y f.
- **Relacionados**: Requisitos de Ingreso a HD, Exclusiones de Ingreso a HD.
- **Notas**: transición del estado del documento: `recibida → evaluada`.

### Resolución de Solicitud de Transferencia

- **Definición**: tercera etapa operativa de la Evaluación; cierra la Solicitud con uno de cuatro resultados: aceptación, rechazo categórico (configuración de exclusión del art. 17), rechazo condicional (subsanable mediante antecedentes o adecuaciones) o resultado no concluyente que requiere antecedentes adicionales.
- **Fuente**: DS 1/2022 art. 15 (criterios) y art. 17 (exclusiones); práctica operativa.
- **Notas**: transición del estado del documento: `evaluada → respondida` con uno de los cuatro resultados (aceptada, rechazo categórico, rechazo condicional, no concluyente).

### Transferencia a HD

- **Definición**: proceso por el cual el paciente pasa físicamente desde el Servicio de Atención Cerrada al Domicilio. Admite dos modalidades excluyentes de traslado: (i) por medios propios de la Red de Apoyo, y (ii) traslado coordinado institucional, en cuyo caso se ejecuta por servicio de traslado propio del Establecimiento HODOM o por tercero en convenio gestionado en el hospital por la Unidad de Gestión de Camas.
- **Fuente**: DS 1/2022 art. 1; art. 8 letra ñ; art. 15; NT 2024 §Equipamiento (servicio de traslado propio o tercero en convenio).
- **Relacionados**: Unidad de Gestión de Camas, Red de Apoyo Familiar, Acuerdo de Traslado a Atención Cerrada.

### Realización de Transferencia a HD

- **Definición**: lema renombrado en v1.3.0. → ver Transferencia a HD.

### Suscripción de Consentimiento Informado

- **Definición**: acto por el cual el paciente, su Tutor Legal o un familiar autorizado suscribe por escrito el Consentimiento Informado, acreditando la aceptación voluntaria de la modalidad HD y la recepción de la Carta de Derechos y Deberes. Requisito de ingreso a HD.
- **Fuente**: DS 1/2022 art. 15 letra d; art. 21 N° 4 (Consentimiento Informado); Ley 20.584 (derechos y deberes).
- **Sinónimos**: Otorgamiento de Consentimiento Informado (forma operativa anterior).
- **Relacionados**: Consentimiento Informado, Carta de Derechos y Deberes.

### Otorgamiento de Consentimiento Informado

- **Definición**: lema renombrado en v1.3.0. → ver Suscripción de Consentimiento Informado.

### Evaluación Domiciliaria Inicial

- **Definición**: conjunto de evaluaciones profesionales del Equipo de Salud HD ejecutadas al inicio del Episodio HODOM en el domicilio (médica de atención directa, de enfermería, kinésica, social y otras según cartera), cuyas conclusiones se integran para constituir y ajustar el Plan Terapéutico y de Cuidados. Las evaluaciones pueden ser asincrónicas.
- **Fuente**: DS 1/2022 art. 13 letras a, c, d, f (funciones de evaluación inicial por cargo); NT 2024 §Protocolos clínicos (evaluación e ingreso).

### Ejecución de Atenciones Profesionales Programadas

- **Definición**: ejecución, registro y trazabilidad de las Visitas Domiciliarias y Atenciones Profesionales planificadas en el Plan Terapéutico y de Cuidados durante el Episodio HODOM; comprende programación, preparación, ejecución en domicilio y consignación en el Reporte de Atención Profesional.
- **Fuente**: DS 1/2022 art. 13 (funciones por cargo); art. 21 N° 9 (descripción del proceso asistencial con todas las atenciones); NT 2024 §Protocolos clínicos (programación de rutas y visitas domiciliarias).

### Seguimiento Clínico

- **Definición**: proceso longitudinal del Equipo de Salud HD durante el Episodio HODOM que comprende la observación clínica continua del paciente, el ajuste del plan terapéutico, la valoración de la evolución y el Registro Evolutivo en Ficha Clínica.
- **Fuente**: derivado de DS 1/2022 art. 11 letra b; art. 13 (funciones por cargo); art. 21; NT 2024 §Protocolos clínicos.
- **Relacionados**: Categorización del Paciente, Gestión de la Continuidad Asistencial, Coordinación, Pase de Visita Diario.

### Categorización del Paciente

- **Definición**: proceso del Equipo de Salud HD que clasifica al paciente por complejidad clínica y demanda asistencial, para asignar la frecuencia y composición de las Visitas Domiciliarias y la intensidad del Plan de Cuidados.
- **Fuente**: NT 2024 §Protocolos clínicos (categorización del paciente).
- **Relacionados**: Seguimiento Clínico, Plan Terapéutico y de Cuidados, Visita Domiciliaria.

### Gestión de la Continuidad Asistencial

- **Definición**: proceso del Equipo de Salud HD que articula los pasos de continuidad entre el Episodio HODOM y los actores externos (Atención Cerrada, Atención Primaria, especialidades, redes sociales) durante el episodio y al Egreso, asegurando que la atención del paciente no se interrumpa.
- **Fuente**: derivado de DS 1/2022 art. 8 letras l y n; art. 11 letras c y g; NT 2024 §Protocolos clínicos.
- **Relacionados**: Continuidad Asistencial, Plan de Egreso, Reingreso Hospitalario.

### Coordinación Clínica HD

- **Definición**: lema disuelto en v1.3.0. → ver Seguimiento Clínico, Categorización del Paciente, Gestión de la Continuidad Asistencial.

### Continuidad Asistencial

- **Definición**: obligación transversal del Establecimiento HODOM de garantizar que la atención del paciente se mantenga sin interrupción entre dispositivos asistenciales y en el tiempo, incluyendo coordinación con establecimientos públicos y privados, gestión de personal que asegure cobertura ininterrumpida, y entrega al paciente o representante de indicaciones de cuidados e instrucciones para emergencias o episodios que afecten dicha continuidad.
- **Fuente**: DS 1/2022 art. 1 inciso final (acceso, oportunidad, continuidad y calidad); art. 8 letra i; art. 11 letras c y g; art. 22 (documento de indicaciones para emergencias); NT 2024 §Finalidad y obligación transversal.
- **Relacionados**: Gestión de la Continuidad Asistencial, Documento de Indicaciones para Emergencias.

### Interconsulta

- **Definición**: solicitud formal del Equipo de Salud HD a un especialista o servicio externo para evaluación, opinión diagnóstica o tratamiento específico durante el Episodio HODOM. Se registra en la Ficha Clínica del paciente.
- **Fuente**: NT 2024 §Protocolos clínicos (gestión de recetas, interconsultas y evolución en ficha); práctica clínica.

### Pase de Visita Diario

- **Definición**: reunión clínica diaria del Equipo de Salud HD para revisar el estado de cada paciente activo, ajustar el Plan Terapéutico y de Cuidados y planificar las Visitas Domiciliarias del día.
- **Fuente**: NT 2024 §Protocolos clínicos; práctica operativa.
- **Relacionados**: Visita Domiciliaria, Entrega de Turno, Seguimiento Clínico.

### Entrega de Turno

- **Definición**: traspaso formal de información clínica y operativa entre turnos del Equipo de Salud HD, que asegura la continuidad del Seguimiento Clínico y la cobertura del sistema 24/7.
- **Fuente**: NT 2024 §Protocolos clínicos; DS 1/2022 art. 11 letra c (gestión del personal garantizando continuidad).
- **Relacionados**: Pase de Visita Diario, Seguimiento Clínico, Registro Evolutivo en Ficha Clínica.

### Atención No Programada

- **Definición**: detección, clasificación y escalamiento de eventos clínicos no programados durante el Episodio HODOM —agudización del cuadro, complicaciones, llamadas o consultas urgentes del paciente o cuidador— con resolución por el Equipo de Salud HD, eventual Reingreso Hospitalario o derivación a urgencias. Coexiste con la Ejecución de Atenciones Profesionales Programadas y con el Seguimiento Clínico.
- **Fuente**: DS 1/2022 art. 8 letra l (coordinación de agudización y reingreso); NT 2024 §Protocolos clínicos (actuación ante emergencias y agresiones al equipo de salud).
- **Relacionados**: Visita Domiciliaria, Agudización, Complicación durante HD, Sistema de Comunicaciones 24/7.

### Atención de Acciones Emergentes o No Planificadas

- **Definición**: lema renombrado en v1.3.0. → ver Atención No Programada.

### Egreso de HD

- **Definición**: proceso de cierre del Episodio HODOM por configuración de alguna de las seis Causales del art. 16: Alta Médica por Recuperación; Alta por Cumplimiento del Plan; Reingreso Hospitalario; Fallecimiento en HD; Renuncia Voluntaria; Alta Disciplinaria.
- **Fuente**: DS 1/2022 art. 16 letras a–f; art. 21 (registros del episodio).
- **Relacionados**: Causales de Egreso, Reingreso Hospitalario, Alta Disciplinaria, Epicrisis al Alta, Encuesta de Satisfacción Usuaria al Egreso, Constancia de Acciones en caso de Fallecimiento.

### Tramitación de Egreso de HD

- **Definición**: lema renombrado en v1.3.0. → ver Egreso de HD.

### Alta Médica por Recuperación

- **Definición**: causal (a) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por recuperación del cuadro clínico que motivó la hospitalización.
- **Fuente**: DS 1/2022 art. 16 letra a.
- **Relacionados**: Egreso de HD, Causales de Egreso, Alta Médica.

### Alta por Cumplimiento del Plan

- **Definición**: causal (b) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por término del cumplimiento del Plan Terapéutico y de Cuidados, aun cuando la patología no se haya resuelto completamente.
- **Fuente**: DS 1/2022 art. 16 letra b.
- **Relacionados**: Egreso de HD, Causales de Egreso, Plan Terapéutico y de Cuidados, Plan de Egreso.

### Reingreso Hospitalario

- **Definición**: causal (c) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por traslado del paciente a Atención Cerrada, sea de manera programada (cumplimiento de etapa terapéutica que requiere cama hospitalaria) o por Agudización o Complicación durante HD. La Dirección Técnica lo coordina con el médico tratante y asegura el traslado oportuno mediante servicio propio o tercero en convenio.
- **Fuente**: DS 1/2022 art. 16 letra c; art. 8 letras m, n y ñ.
- **Sinónimos**: Reingreso a Atención Cerrada, Reingreso Hospitalario Programado (denominación anterior).
- **Relacionados**: Acuerdo de Traslado a Atención Cerrada, Médico Tratante de Atención Cerrada.

### Reingreso Hospitalario Programado

- **Definición**: lema renombrado en v1.3.0. → ver Reingreso Hospitalario.

### Fallecimiento en HD

- **Definición**: causal (d) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por fallecimiento del paciente durante la HD. Detona el registro obligatorio de Constancia de Acciones en caso de Fallecimiento (art. 21 N° 2).
- **Fuente**: DS 1/2022 art. 16 letra d; art. 21 N° 2.
- **Relacionados**: Egreso de HD, Causales de Egreso, Constancia de Acciones en caso de Fallecimiento.

### Renuncia Voluntaria

- **Definición**: causal (e) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por decisión voluntaria del paciente, su Tutor Legal o un familiar autorizado de no continuar en la modalidad de HD.
- **Fuente**: DS 1/2022 art. 16 letra e; Ley 20.584.
- **Relacionados**: Egreso de HD, Causales de Egreso, Consentimiento Informado.

### Alta Disciplinaria

- **Definición**: causal (f) del art. 16 del DS 1/2022, resuelta por la Dirección Técnica al verificarse no adherencia al tratamiento o indicaciones por el tutor o cuidador, conductas irrespetuosas hacia el personal o falta de respuesta o rechazo a las visitas domiciliarias. Su configuración en un episodio previo opera como causal autónoma de **exclusión** para futuros ingresos del mismo paciente.
- **Fuente**: DS 1/2022 art. 16 letra f (causal de egreso); art. 17 letra d (causal de exclusión por antecedente previo); art. 8 letra p (atribución resolutiva de la DT).
- **Relacionados**: Egreso de HD, Causales de Egreso, Exclusiones de Ingreso a HD, Dirección Técnica.

### Plan de Egreso

- **Definición**: conjunto estructurado de indicaciones, derivaciones, recetas y orientaciones que el Equipo de Salud HD entrega al paciente, a su Cuidador y a la red asistencial al término del Episodio HODOM, para asegurar la continuidad del cuidado post-egreso.
- **Fuente**: DS 1/2022 art. 16; art. 21 (registros del episodio); práctica clínica.

---

## 5. Documentos y registros

### Solicitud de Transferencia a HD (documento)

- **Definición**: documento clínico-administrativo concreto generado por el Médico Tratante de Atención Cerrada al solicitar el traslado del paciente al Establecimiento HODOM. Atraviesa cuatro estados operativos sucesivos —creada, recibida, evaluada, respondida— y se cierra con uno de cuatro resultados: aceptada, rechazo categórico, rechazo condicional, no concluyente. Su contenido mínimo cumple los registros formales aplicables del art. 21 (identificación, plan, consentimiento, formulario de ingreso).
- **Fuente**: DS 1/2022 art. 21; práctica operativa hospitalaria.
- **Distinción**: la **Solicitud** es la instancia documental concreta de un paciente, con estados; el **Formulario de HD** es la plantilla estable utilizada para construirla; el **Formulario de Ingreso** se aplica al admitir al paciente en HD y es distinto de la Solicitud.
- **Relacionados**: Formulario de Hospitalización Domiciliaria, Plan Terapéutico y de Cuidados.

### Formulario de Hospitalización Domiciliaria

- **Definición**: plantilla estándar utilizada como instrumento para elaborar el documento Solicitud de Transferencia a HD. Esquema estable, sin estados operativos por sí mismo.
- **Fuente**: práctica operativa hospitalaria; complementa DS 1/2022 art. 21.
- **Distinción**: ver "Solicitud de Transferencia a HD (documento)".

### Plan Terapéutico y de Cuidados

- **Definición**: documento estructurado que define las indicaciones terapéuticas, frecuencias de visita, cuidados y objetivos asistenciales del paciente bajo HD; se propone con la Solicitud, se ajusta tras la Evaluación Domiciliaria Inicial y se modifica durante el Episodio HODOM según el Seguimiento Clínico.
- **Fuente**: DS 1/2022 art. 1 inciso primero (componente estructural de la HD); art. 21 N° 8 (plan de cuidados acorde a necesidades de la persona); art. 13 letra c (gestión del plan por enfermería).
- **Distinción**: el **Plan Terapéutico y de Cuidados** es el documento integrado e interdisciplinario del paciente bajo HD; el **Plan de Cuidados de Enfermería** es la dimensión específica de enfermería, anidada en el plan integrado.

### Plan de Cuidados de Enfermería

- **Definición**: registro específico de la dimensión enfermería del Plan Terapéutico y de Cuidados, que detalla las intervenciones de cuidado a ejecutar por el Enfermero o Enfermera Clínica durante el Episodio HODOM.
- **Fuente**: DS 1/2022 art. 13 letra c; art. 21 N° 8.
- **Distinción**: ver "Plan Terapéutico y de Cuidados".

### Consentimiento Informado

- **Definición**: documento firmado por el paciente, su Tutor Legal o un familiar autorizado, que acredita la aceptación voluntaria de la modalidad HD y la recepción de la Carta de Derechos y Deberes. Requisito de ingreso y registro formal obligatorio.
- **Fuente**: DS 1/2022 art. 15 letra d; art. 21 N° 4; Ley 20.584; NT 2024 §Registros obligatorios.
- **Sinónimos**: CI.
- **Relacionados**: Carta de Derechos y Deberes, Suscripción de Consentimiento Informado.

### Carta de Derechos y Deberes

- **Definición**: documento institucional con los derechos y deberes de la persona en relación con su atención en salud, entregado por el Establecimiento HODOM al paciente o representante al ingreso. La firma del Consentimiento Informado acredita su entrega.
- **Fuente**: Ley 20.584; DS 1/2022 art. 21 N° 5; NT 2024 §Registros obligatorios.
- **Sinónimos**: CDD.

### Formulario de Ingreso

- **Definición**: documento estructurado que se aplica al ingreso del paciente a HD, distinto del Consentimiento Informado y de la Solicitud de Transferencia; recoge datos administrativos y clínicos iniciales del Episodio HODOM.
- **Fuente**: DS 1/2022 art. 21 N° 6.

### Resumen Clínico en Domicilio

- **Definición**: documento físico o electrónico que permanece en el domicilio del paciente y contiene sus diagnósticos, tratamientos vigentes y cuidados, para consulta en una emergencia por equipos externos al Establecimiento HODOM.
- **Fuente**: NT 2024 §Registros obligatorios (Resumen clínico en domicilio).
- **Relacionados**: Atención No Programada, Documento de Indicaciones para Emergencias.

### Documento de Indicaciones para Emergencias

- **Definición**: documento entregado al paciente o a su representante con indicaciones de cuidados e instrucciones para emergencias o episodios que afecten la continuidad de la atención durante el Episodio HODOM.
- **Fuente**: DS 1/2022 art. 22.
- **Relacionados**: Resumen Clínico en Domicilio, Continuidad Asistencial.

### Receta Médica HODOM

- **Definición**: prescripción farmacológica emitida por el Médico de Atención Directa o el Médico Regulador en el contexto de un Episodio HODOM, conforme a la normativa general de recetas, al Código Sanitario y a los protocolos institucionales del Establecimiento HODOM.
- **Fuente**: DS 1/2022 art. 21; NT 2024 §Protocolos clínicos (gestión de recetas); normativa general de prescripción.

### Registro Evolutivo en Ficha Clínica

- **Definición**: registro longitudinal en la Ficha Clínica donde el Equipo de Salud HD consigna observaciones, resultados, indicaciones, llamadas, videollamadas, eventos relevantes y alertas durante el Episodio HODOM. Reemplaza la denominación previa de "Reporte de Información Clínico-Asistencial Relevante".
- **Fuente**: DS 1/2022 art. 21 (registros clínicos íntegros); DS 41/2012; NT 2024 §Registros y §Infraestructura mínima (trazabilidad con fecha, hora, emisor, receptor y derivación).
- **Sinónimos**: Evolución en Ficha Clínica.

### Reporte de Información Clínico-Asistencial Relevante

- **Definición**: lema renombrado en v1.3.0. → ver Registro Evolutivo en Ficha Clínica.

### Reporte de Atención Profesional

- **Definición**: registro que produce el profesional luego de cada Atención Profesional individual ejecutada en domicilio, cumpliendo la exigencia normativa de descripción del proceso asistencial con todas las atenciones del paciente.
- **Fuente**: DS 1/2022 art. 21 N° 9.

### Curso Clínico-Asistencial

- **Definición**: síntesis evolutiva de la dinámica clínica del paciente durante el Episodio HODOM, integrada en la Ficha Clínica.
- **Fuente**: práctica clínica; DS 41/2012 (estructura de la ficha clínica).

### Epicrisis al Alta

- **Definición**: documento de cierre del Episodio HODOM que consigna evolución, intervenciones, resultados, diagnóstico final y disposición al egreso del paciente.
- **Fuente**: DS 1/2022 art. 21 (registros del episodio asociados al egreso).
- **Relacionados**: Egreso de HD, Plan de Egreso.

### Encuesta de Satisfacción Usuaria al Egreso

- **Definición**: registro obligatorio aplicado al paciente o a su familiar al Egreso del Episodio HODOM para evaluar la experiencia con la modalidad HD.
- **Fuente**: DS 1/2022 art. 21 N° 3.

### Constancia de Acciones en caso de Fallecimiento

- **Definición**: registro obligatorio que documenta las acciones realizadas por el Equipo de Salud HD cuando la causal de Egreso es el Fallecimiento en HD del paciente.
- **Fuente**: DS 1/2022 art. 21 N° 2.

### Ficha Clínica

- **Definición**: registro clínico del paciente en soporte físico o electrónico, que cumple las exigencias del Reglamento sobre Fichas Clínicas y almacena la información clínica producida durante el Episodio HODOM.
- **Fuente**: DS 41/2012; DS 1/2022 art. 21; Ley 19.628 (datos sensibles); NT 2024 §Registros obligatorios (Ficha Clínica).

### Sistema de Registro Clínico y Administrativo

- **Definición**: soporte institucional del registro clínico y administrativo del Establecimiento HODOM, materializado como ficha manual, sistema electrónico, archivos o protocolos de trazabilidad. Atraviesa todos los procesos asistenciales.
- **Fuente**: DS 1/2022 art. 21 (registros formales); art. 23 (confidencialidad y reserva).
- **Sinónimos**: SRCA.

### Registro del Episodio de HD

- **Definición**: agregación documental de los registros formales obligatorios del art. 21 producidos durante un Episodio HODOM (Constancia de Fallecimiento N° 2 cuando corresponde, Encuesta de Satisfacción Usuaria al Egreso N° 3, Consentimiento Informado N° 4, Carta de Derechos y Deberes N° 5, Formulario de Ingreso N° 6, Plan Terapéutico y de Cuidados y Plan de Cuidados de Enfermería N° 8, Reporte de Atención Profesional N° 9, Epicrisis al Alta y demás registros aplicables).
- **Fuente**: DS 1/2022 art. 21.

### Manual de Organización Interna

- **Definición**: documento aprobado y actualizado por la Dirección Técnica, que define el organigrama, roles, horarios y reglamento de higiene del Establecimiento HODOM.
- **Fuente**: NT 2024 §Protocolos y manuales obligatorios (Manual de Organización Interna); DS 1/2022 art. 5 letra m (manual de normas y procedimientos técnicos como antecedente exigido); art. 8 letra b (aprobación por la DT).

### Protocolos Clínicos

- **Definición**: documentos aprobados por la Dirección Técnica que normalizan: evaluación e ingreso de pacientes; programación de rutas y visitas domiciliarias; categorización y egreso de pacientes —incluidos altas y fallecidos—; gestión de recetas, interconsultas y evolución en ficha; actuación ante emergencias y agresiones al equipo de salud.
- **Fuente**: NT 2024 §Protocolos clínicos obligatorios.

### Manual de Procedimientos

- **Definición**: documento que detalla procedimientos técnicos específicos del Establecimiento HODOM: manejo de vías venosas periféricas y centrales, catéteres urinarios, traqueostomías, toma de muestras, precauciones de aislamiento.
- **Fuente**: NT 2024 §Protocolos y manuales obligatorios (Manual de procedimientos); DS 1/2022 art. 5 letra m.

### Plan de Capacitación Anual (PAC)

- **Definición**: plan formativo anual obligatorio del Establecimiento HODOM, aprobado por la Dirección Técnica, que cubre como contenidos mínimos IAAS, RCP básica, inducción del personal y cursos de humanización del cuidado.
- **Fuente**: NT 2024 §Plan de Capacitación Anual.
- **Sinónimos**: PAC.

### Reglamento Interno de Orden, Higiene y Seguridad

- **Definición**: reglamento institucional del Establecimiento HODOM, exigido entre los antecedentes para la solicitud de Autorización Sanitaria.
- **Fuente**: DS 1/2022 art. 5 letra l.

### Programa de Mantención Preventiva

- **Definición**: programa de mantención preventiva de maquinarias, equipos médicos y vehículos de transporte —propios o arrendados— del Establecimiento HODOM, exigido entre los antecedentes para la solicitud de Autorización Sanitaria, y supervisado por la Dirección Técnica.
- **Fuente**: DS 1/2022 art. 5 letra j; art. 8 letra f (verificación de programas preventivos y de reparación).
- **Sinónimos**: Programa de Mantención de Equipos.

---

## 6. Capacidad operativa

### Capacidad Operacional HODOM

- **Definición**: conjunto efectivo de recursos materiales, humanos y logísticos del Establecimiento HODOM —vehículos de transporte, equipamiento médico, dispositivos de uso médico, insumos clínicos, medicamentos, sistema de comunicaciones 24/7, respaldo eléctrico autorizado por la SEC— que habilitan la prestación del servicio HODOM; su disponibilidad condiciona la aceptación de nuevos pacientes y la sostenibilidad del Episodio HODOM.
- **Fuente**: DS 1/2022 arts. 19–21; NT 2024 §Infraestructura mínima y §Equipamiento y dispositivos de uso médico.
- **Sinónimos**: Capacidad Operacional Disponible (denominación anterior), Cap.Op HODOM.

### Capacidad Operacional Disponible

- **Definición**: lema renombrado en v1.3.0. → ver Capacidad Operacional HODOM.

### Infraestructura

- **Definición**: conjunto de dependencias administrativas y operativas del Establecimiento HODOM que incluye: sistema telefónico o radial 24/7 con grabación continua o registro manual; soporte informático e internet; respaldo eléctrico autorizado por la SEC; área administrativa para archivos y fichas clínicas en condiciones seguras; bodegas para equipamiento, insumos y medicamentos, con condiciones que mantengan integridad y, para termolábiles, refrigeradores con temperatura controlada y registro; acceso a servicios de alimentación, servicios higiénicos con ducha, casilleros y sala de guardarropía o estar para personal de turno; área cerrada de disposición transitoria de residuos con plan de manejo; protocolo y flujo de desecho de cortopunzantes; estacionamiento para vehículos de traslado; señalización y vías de evacuación; recinto de depósito de material de aseo.
- **Fuente**: DS 1/2022 art. 19 letras a–l (literal de exigencias de dependencias); NT 2024 §Infraestructura mínima.

### Vehículos de Transporte

- **Definición**: vehículos destinados al traslado del Equipo de Salud HD y, cuando corresponde, del paciente. Pueden ser propios o de terceros en convenio; deben contar con estacionamiento o lugar de detención transitoria; están sujetos al Programa de Mantención Preventiva.
- **Fuente**: DS 1/2022 art. 5 letra j; art. 19 letra k (estacionamiento); NT 2024 §Equipamiento y dispositivos de uso médico (vehículos de transporte).

### Equipamiento Médico

- **Definición**: conjunto de equipos, instrumentos, aparatos, dispositivos y elementos de uso médico necesarios para diagnóstico y tratamiento adecuados, en especial los vinculados a la mantención de funciones vitales y al monitoreo permanente; incluye, como mínimo obligatorio, equipos para monitorizar presión arterial, frecuencia cardíaca, frecuencia respiratoria y saturación de oxígeno, y los instrumentos adicionales según la Cartera de Prestaciones. Cada elemento debe cumplir la normativa vigente sobre dispositivos de uso médico (instrumento, aparato, implemento, máquina, equipo, artefacto, implante u otro artículo similar destinado a uso médico).
- **Fuente**: DS 1/2022 art. 20; NT 2024 §Equipamiento y dispositivos de uso médico; NT 2024 §Definiciones (Dispositivos de Uso Médico).
- **Sinónimos**: Dispositivos de Uso Médico.

### Dispositivos de Uso Médico

- **Definición**: lema fusionado en v1.3.0. → ver Equipamiento Médico.

### Insumos Clínicos

- **Definición**: material clínico fungible utilizado en los procedimientos del Equipo de Salud HD, almacenado en bodegas con control de temperatura según especificaciones del fabricante.
- **Fuente**: DS 1/2022 art. 19 letra e (bodegas con condiciones); NT 2024 §Infraestructura mínima (bodegas).

### Medicamentos

- **Definición**: stock farmacológico del Establecimiento HODOM, gestionado mediante farmacia o Botiquín Autorizado del propio Establecimiento, o mediante convenios que aseguren el abastecimiento y la Cadena de Frío Domiciliaria.
- **Fuente**: NT 2024 §Infraestructura mínima (farmacia o botiquín autorizado, o convenios); DS 1/2022 art. 5 letra m (autorización sanitaria de botiquín, cuando corresponda); art. 8 letra e (mantención de stock).

### Botiquín Autorizado

- **Definición**: dispositivo farmacéutico del Establecimiento HODOM sujeto a autorización sanitaria sectorial, exigido entre los antecedentes de la solicitud de Autorización Sanitaria cuando corresponda al modelo de gestión farmacéutica adoptado.
- **Fuente**: DS 1/2022 art. 5 letra m; NT 2024 §Infraestructura mínima (farmacia o botiquín autorizado).
- **Relacionados**: Medicamentos, Cadena de Frío Domiciliaria.

### Cadena de Frío Domiciliaria

- **Definición**: aseguramiento de la conservación de medicamentos termolábiles en condiciones de temperatura controlada desde el Establecimiento HODOM hasta el domicilio del paciente, sea por gestión interna o por convenios suscritos a tal efecto.
- **Fuente**: NT 2024 §Infraestructura mínima (convenios que aseguren abastecimiento y cadena de frío en domicilio); DS 1/2022 art. 19 letra e inciso final (termolábiles en refrigeradores con temperatura controlada y registro, en bodega).

### Sistema de Comunicaciones 24/7

- **Definición**: sistema telefónico o radial del Establecimiento HODOM disponible las 24 horas los 7 días de la semana, con grabación continua o registro manual y protocolo de atención de llamadas (con trazabilidad de fecha, hora, emisor, receptor y derivación), soporte informático e internet permanente.
- **Fuente**: DS 1/2022 art. 19 letra a; NT 2024 §Infraestructura mínima.

### Respaldo Eléctrico

- **Definición**: respaldo de energía eléctrica del Establecimiento HODOM autorizado por la Superintendencia de Electricidad y Combustibles (SEC). Exigencia reglamentaria que **no se sustituye** por un plan de contingencia operacional, el cual opera como complemento.
- **Fuente**: DS 1/2022 art. 19 letra b; NT 2024 §Infraestructura mínima; Acto Exento N° 31/2024 §Criterio de armonización (no sustitución por plan de contingencia).

### Plan de Contingencia Operacional

- **Definición**: plan exigido para asegurar la continuidad eléctrica y de comunicaciones del Establecimiento HODOM ante eventos disruptivos; complemento del Respaldo Eléctrico autorizado por la SEC, no sustituto de él.
- **Fuente**: NT 2024 §Infraestructura mínima (plan de contingencia operacional para continuidad eléctrica y de comunicaciones); Acto Exento N° 31/2024 §Criterio de armonización.

### Conocimiento Normativo y Técnico

- **Definición**: corpus institucionalizado de manuales, protocolos, planes de capacitación y normativa absorbida localmente por el Establecimiento HODOM; instrumento transversal de los procesos asistenciales, aprobado y mantenido actualizado por la Dirección Técnica.
- **Fuente**: DS 1/2022 art. 8 letra b (aprobación y actualización de manuales y procedimientos); NT 2024 §Protocolos y manuales obligatorios.

### Coordenadas del Domicilio

- **Definición**: representación informacional de la ubicación geográfica del Domicilio del Paciente, generada durante la Verificación de Criterios de Ingreso a HD. Sustenta la verificación del Radio de Cobertura y la planificación logística de las Visitas Domiciliarias.
- **Fuente**: práctica operativa; complementa DS 1/2022 art. 15 letra b y NT 2024 §Protocolos clínicos (programación de rutas y visitas domiciliarias).
- **Relacionados**: Domicilio del Paciente, Radio de Cobertura.

---

## 7. Procedimientos y exigencias normativas

### Autorización Sanitaria

- **Definición**: acto administrativo de la SEREMI que habilita al Establecimiento HODOM a otorgar prestaciones de HD. Vigencia de 3 años, prorrogable de manera automática y sucesiva por períodos iguales, salvo que la autoridad la deje sin efecto expresamente.
- **Fuente**: DS 1/2022 arts. 4 (competencia), 5 (antecedentes), 6 (vigencia y prórroga).
- **Excepción**: si la autorización sanitaria del establecimiento de atención cerrada ya contempla atenciones en modalidad de HD, esa autorización basta y no se requiere una adicional (DS 1/2022 art. 4 inciso segundo).

### Antecedentes de la Solicitud de Autorización Sanitaria

- **Definición**: conjunto cerrado de antecedentes que el interesado o su representante legal acompaña a la solicitud de Autorización Sanitaria del Establecimiento HODOM: a) identificación; b) dominio del inmueble o derecho a uso; c) certificado municipal o de recepción definitiva; d) escritura de constitución e individualización de representantes legales o del propietario natural; e) individualización del profesional que asumirá la Dirección Técnica más declaración jurada simple de aceptación; f) nómina del personal de salud habilitado conforme al Registro de Prestador Individual de la Superintendencia de Salud o título revalidado o reconocido; g) planos de planta con distribución funcional, flujos de circulación y dependencias; h) planos o certificados de instalaciones de electricidad, agua potable y gas visados; i) listado de equipos con autorización cuando corresponda; j) Programa de Mantención Preventiva; k) listado de elementos de protección personal; l) horario de funcionamiento y distribución de turnos; m) manual de normas y procedimientos técnicos; n) Reglamento Interno de Orden, Higiene y Seguridad; ñ) autorización sanitaria de botiquín cuando corresponda; o) listado de prestaciones brindadas; p) protocolo de manejo de residuos especiales según reglamento REAS.
- **Fuente**: DS 1/2022 art. 5 letras a–p.

### Fiscalización

- **Definición**: actividad de la SEREMI del lugar donde se ubica el Establecimiento HODOM que controla las actividades de éste y conoce de las contravenciones a la normativa.
- **Fuente**: DS 1/2022 art. 24.
- **Relacionados**: Sanción Sanitaria.

### Sanción Sanitaria

- **Definición**: consecuencia jurídica de las contravenciones constatadas en Fiscalización, conforme al Libro X del Código Sanitario.
- **Fuente**: DS 1/2022 art. 24 inciso final; Código Sanitario Libro X.

### Cambio de Director Técnico

- **Definición**: hecho que origina la obligación del Establecimiento HODOM de comunicar de manera inmediata a la SEREMI la sustitución del profesional que ejerce la Dirección Técnica.
- **Fuente**: DS 1/2022 art. 10 inciso final.

### Requisitos de Ingreso a HD

- **Definición**: cuatro condiciones concurrentes que el paciente debe cumplir para ser admitido a HD:
  - **a)** situación clínica: patología aguda o crónica reagudizada, clínicamente estable y susceptible de tratamiento en domicilio o adecuación del esfuerzo terapéutico;
  - **b)** residencia: condiciones sanitarias mínimas, servicios básicos y telefonía, dentro del Radio de Cobertura;
  - **c)** apoyo: red de apoyo familiar, social o tutor responsable a cargo del cuidado;
  - **d)** consentimiento: aceptación escrita e informada del paciente, tutor o familiar.
- **Fuente**: DS 1/2022 art. 15 letras a–d.

### Causales de Egreso

- **Definición**: seis causales enumeradas taxativamente por las cuales se cierra el Episodio HODOM:
  - **a)** Alta Médica por Recuperación del cuadro clínico;
  - **b)** Alta por Cumplimiento del Plan terapéutico y de cuidados;
  - **c)** Reingreso Hospitalario por inestabilidad del cuadro clínico o complicaciones;
  - **d)** Fallecimiento en HD;
  - **e)** Renuncia Voluntaria del paciente o de quien lo represente;
  - **f)** Alta Disciplinaria determinada por la Dirección Técnica.
- **Fuente**: DS 1/2022 art. 16 letras a–f.

### Acuerdo de Traslado a Atención Cerrada

- **Definición**: arreglo formal —con servicio propio del Establecimiento HODOM o tercero en convenio— que asegura el traslado oportuno del paciente desde el domicilio a un establecimiento de Atención Cerrada cuando se configura Agudización o Reingreso Hospitalario.
- **Fuente**: DS 1/2022 art. 8 letra ñ; NT 2024 §Equipamiento (servicio de traslado propio o tercero en convenio).
- **Relacionados**: Reingreso Hospitalario, Vehículos de Transporte.

### Exclusiones de Ingreso a HD

- **Definición**: cuatro condiciones que impiden el ingreso de un paciente a HD:
  - **a)** inestabilidad clínica o ausencia de diagnóstico establecido;
  - **b)** patología de salud mental descompensada;
  - **c)** necesidad de una prestación no incluida en el listado del Establecimiento HODOM (Cartera de Prestaciones HODOM);
  - **d)** concurrencia previa de alguna condición de Alta Disciplinaria del art. 16 letra f.
- **Fuente**: DS 1/2022 art. 17 letras a–d.

### IAAS (Infecciones Asociadas a la Atención de Salud)

- **Definición**: programa de prevención y control de infecciones asociadas a la atención de salud. Exigencia formativa transversal: curso vigente de al menos 80 horas para Dirección Técnica, Coordinación y personal clínico que realiza atención directa; vigencia máxima 5 años. Curso obligatorio del Plan de Capacitación Anual del Establecimiento HODOM.
- **Fuente**: Res. Ex. N° 60/2022 MINSAL; DS 1/2022 arts. 7, 11 y 13 (exigencias por cargo); NT 2024 §Habilitación, §Inducción y certificación y §Plan de Capacitación Anual.

### REAS (Reglamento de Manejo de Residuos de Establecimientos de Atención de Salud)

- **Definición**: reglamento sobre manejo de residuos especiales aplicable al Establecimiento HODOM, que debe contar con protocolo ajustado para retiro y eliminación.
- **Fuente**: DS 6/2009 MINSAL; DS 1/2022 art. 5 letra p; NT 2024 §Protocolos y manuales obligatorios (Manejo de residuos).

### RCP Básica (Reanimación Cardiopulmonar Básica)

- **Definición**: capacitación en soporte vital básico de 3 horas conforme al Decreto Exento N° 52/2022. Constituye exigencia **acumulativa** —no sustitutiva— del curso IAAS de 80 horas y del uso certificado de desfibrilador para el personal clínico que realiza atención directa.
- **Fuente**: Decreto Exento N° 52/2022 MINSAL; DS 1/2022 art. 13 letras c, d, e; NT 2024 §Requisitos resumidos por cargo, §Inducción y certificación y §Criterio armonizado sobre Coordinación.

### Soporte Vital Básico

- **Definición**: capacitación obligatoria del personal profesional y técnico que ejecuta atención clínica directa, materializada en el curso de RCP Básica vigente.
- **Fuente**: NT 2024 §Inducción y certificación; DS 1/2022 art. 13 letras c, d, e.
- **Notas**: requisito acumulativo con el curso IAAS de 80 horas y con la certificación vigente de uso de desfibrilador.

### Uso Certificado de Desfibrilador

- **Definición**: certificación vigente de uso de desfibrilador exigida al personal clínico que realiza atención directa, con vigencia máxima de 5 años.
- **Fuente**: NT 2024 §Requisitos resumidos por cargo e §Inducción y certificación; Decreto Exento N° 52/2022.
- **Notas**: requisito acumulativo con IAAS y soporte vital básico.

### Inducción Obligatoria

- **Definición**: capacitación al ingreso del personal del Establecimiento HODOM, con duración mínima de 44 horas, carácter teórico-práctico y registro obligatorio en la hoja de vida del trabajador.
- **Fuente**: NT 2024 §Inducción y certificación.

### Vacunación del Personal Sanitario

- **Definición**: obligación de la Dirección Técnica de velar porque el personal sanitario del Establecimiento HODOM se encuentre vacunado conforme a los programas oficiales del MINSAL.
- **Fuente**: DS 1/2022 art. 8 letra d.

### Especialidad Pediátrica o Psiquiátrica

- **Definición**: cuando el Establecimiento HODOM declara prestaciones de HD pediátricas o psiquiátricas, exigencia de contar con médico cirujano con la especialidad correspondiente o con experiencia demostrable de al menos 2 años en esos servicios.
- **Fuente**: NT 2024 §Habilitación del personal (Especialidades exigidas).

### Convenio con Terceros

- **Definición**: facultad de los prestadores públicos y privados de celebrar convenios con terceros —incluidas Instituciones de Salud Previsional y organismos administradores de la Ley N° 16.744— para garantizar continuidad de las atenciones en domicilio según el seguro de salud del paciente.
- **Fuente**: NT 2024 §Convenios permitidos.

### Prestador de Hospitalización Domiciliaria en Convenio

- **Definición**: prestador público o privado que recibe pacientes derivados desde establecimientos de salud para continuar tratamiento en modalidad HD.
- **Fuente**: NT 2024 §Definiciones (Prestador de hospitalización domiciliaria en convenio); DS 1/2022 art. 2 letra b.

### Registro de Prestador Individual

- **Definición**: registro de la Superintendencia de Salud en el que debe constar la habilitación profesional del personal de salud del Establecimiento HODOM; alternativamente, título revalidado o reconocido conforme a la normativa vigente.
- **Fuente**: DS 1/2022 art. 5 letra f y art. 7 (Dirección Técnica habilitada).

### Certificación de Auxiliares por SEREMI

- **Definición**: certificación de los auxiliares de la salud por la Secretaría Regional Ministerial de Salud, exigida para los auxiliares paramédicos integrantes del Equipo de Salud HD.
- **Fuente**: DS 90/2017 MINSAL; NT 2024 §Habilitación del personal (auxiliares).

### Confidencialidad y Reserva de Datos Sensibles

- **Definición**: obligación del Establecimiento HODOM de resguardar la confidencialidad y la reserva de los registros manuales o electrónicos cuyo contenido constituya información de salud considerada dato sensible; el tratamiento sólo procede cuando la ley lo autorice expresamente y en los casos previstos por el ordenamiento vigente.
- **Fuente**: DS 1/2022 art. 23; Ley 19.628; Ley 20.575; Ley 20.584 art. 12.

### Ajuste de Procedimientos por Régimen Transitorio

- **Definición**: obligación de los establecimientos, prestadores, unidades o servicios que ya prestaban HD a la fecha de publicación del DS 1/2022 de ajustar sus procedimientos en un plazo de 6 meses contados desde dicha publicación.
- **Fuente**: DS 1/2022 art. 25.

---

## 8. Normativa cruzada citada

### DS 1/2022 MINSAL — Reglamento HODOM

Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria. Fuente primaria del corpus. Anclaje: `urn:salud:kb:hodom-reglamento-ds1-2022`.

### Acto Exento N° 31/2024 MINSAL

Acto administrativo del Ministerio de Salud que aprueba la Norma Técnica HODOM, suscrito el 05-jun-2024 por la Ministra Ximena Aguilera Sanhueza. Anclaje: `urn:salud:kb:hodom-decreto-exento-31-2024`.

### NT 2024 — Norma Técnica HODOM

Norma Técnica para Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria, texto anexo de 16 páginas al Acto Exento N° 31/2024. Anclaje: `urn:salud:kb:hodom-norma-tecnica-2024`.

### Ley 20.584

Ley sobre derechos y deberes de las personas en relación con acciones vinculadas a su atención en salud (2012). Sustento del Consentimiento Informado, la Carta de Derechos y Deberes y la calificación de la información clínica como dato sensible (art. 12).

### Ley 19.628

Ley sobre protección de la vida privada y de los datos de carácter personal (1999). Aplica al tratamiento de información clínica como dato sensible.

### Ley 20.575

Ley que establece el principio de finalidad en el tratamiento de datos personales (2012). Refuerza la Ley 19.628.

### DS 41/2012 MINSAL — Reglamento sobre Fichas Clínicas

Reglamento que regula el manejo de fichas clínicas; aplicable a la Ficha Clínica del Establecimiento HODOM.

### DS 594/2000 MINSAL

Reglamento sobre condiciones sanitarias y ambientales básicas en lugares de trabajo. Aplicable a las dependencias administrativas del Establecimiento HODOM.

### DS 6/2009 MINSAL — Reglamento REAS

Reglamento sobre manejo de residuos de establecimientos de atención de salud.

### Res. Ex. N° 60/2022 MINSAL — Norma Técnica IAAS

Norma Técnica sobre Programa Nacional de Prevención y Control de IAAS.

### Decreto Exento N° 52/2022 MINSAL — Norma Técnica RCP y Desfibriladores

Norma técnica de contenidos para capacitación en reanimación cardiopulmonar básica y uso de desfibriladores.

### Res. Exenta N° 875/2013 MINSAL — Norma Técnica N° 154

Norma Técnica N° 154 sobre Programa Nacional de Calidad y Seguridad de la Atención en Salud.

### DS 90/2017 MINSAL — Certificación de Auxiliares

Reglamento sobre certificación de auxiliares de la salud por la SEREMI. Aplica a auxiliares paramédicos de enfermería del Equipo de Salud HD.

### DS 725/1968 — Código Sanitario

Código Sanitario; su Libro X regula las sanciones por contravenciones de los Establecimientos HODOM.

### DFL N° 1/2005 MINSAL

DFL que fija el texto refundido, coordinado y sistematizado del DL N° 2.763/1979 y de las Leyes N° 18.933 y N° 18.469. Sustento jurídico del Acto Exento N° 31/2024.

### Ley 19.880

Ley de Bases de los Procedimientos Administrativos. Sustento jurídico del Acto Exento N° 31/2024.

### Ley 16.744

Ley sobre accidentes del trabajo y enfermedades profesionales. Sus organismos administradores pueden suscribir convenios con prestadores HODOM.

### Decreto N° 136/2004 MINSAL

Reglamento Orgánico del Ministerio de Salud.

### Decreto N° 140/2004 MINSAL

Reglamento Orgánico de los Servicios de Salud.

### DS N° 28/2009 MINSAL

Reglamento que delega en la Ministra de Salud la facultad de suscribir, bajo la fórmula "Por orden del Presidente de la República", los decretos que aprueban normas técnicas.

### Resolución N° 7/2019 (Contraloría)

Resolución de la Contraloría General de la República invocada como fundamento jurídico del Acto Exento N° 31/2024.

### Res. Ex. N° 328/2023 (Subsecretaría de Salud Pública)

Resolución que creó el grupo de trabajo encargado de elaborar la propuesta de Norma Técnica HODOM 2024.

### SEC — Superintendencia de Electricidad y Combustibles

Organismo que autoriza el respaldo eléctrico del Establecimiento HODOM.

### Superintendencia de Salud

Organismo que mantiene el Registro de Prestador Individual del personal de salud habilitado.

### ISAPRE — Institución de Salud Previsional

Entidad con la que el Prestador HODOM puede suscribir Convenios con Terceros para asegurar continuidad de la atención en domicilio según el seguro de salud del paciente.

---

## 9. Índice alfabético

**A** — Acto Exento N° 31/2024 · Acuerdo de Traslado a Atención Cerrada · Agudización · Ajuste de Procedimientos por Régimen Transitorio · Alta Disciplinaria · Alta Médica por Recuperación · Alta por Cumplimiento del Plan · Antecedentes de la Solicitud de Autorización Sanitaria · Atención Cerrada · Atención de Acciones Emergentes o No Planificadas (→ ver Atención No Programada) · Atención Domiciliaria · Atención No Programada · Atención Profesional · Autorización Sanitaria.

**B** — Botiquín Autorizado.

**C** — Cadena de Frío Domiciliaria · Cambio de Director Técnico · Capacidad Operacional Disponible (→ ver Capacidad Operacional HODOM) · Capacidad Operacional HODOM · Carta de Derechos y Deberes · Cartera de Prestaciones de HD (→ ver Cartera de Prestaciones HODOM) · Cartera de Prestaciones HODOM · Categorización del Paciente · Causales de Egreso · Certificación de Auxiliares por SEREMI · Complicación durante HD · Condición Clínica Estable · Confidencialidad y Reserva de Datos Sensibles · Conocimiento Normativo y Técnico · Consentimiento Informado · Constancia de Acciones en caso de Fallecimiento · Continuidad Asistencial · Convenio con Terceros · Coordenadas del Domicilio · Coordinación · Coordinación Clínica HD (→ ver Seguimiento Clínico; Categorización del Paciente; Gestión de la Continuidad Asistencial) · Cuidador · Cuidador / Tutor Legal (→ ver Cuidador y Tutor Legal) · Curso Clínico-Asistencial.

**D** — Decreto Exento N° 52/2022 · Decreto N° 136/2004 · Decreto N° 140/2004 · DFL N° 1/2005 · Diagnóstico Social del Hogar · Dirección Técnica · Dispositivos de Uso Médico (→ ver Equipamiento Médico) · División de Gestión de la Red Asistencial · Documento de Indicaciones para Emergencias · Domicilio del Paciente · DS 1/2022 · DS 6/2009 · DS 28/2009 · DS 41/2012 · DS 90/2017 · DS 594/2000 · DS 725/1968.

**E** — Egreso de HD · Ejecución de Atenciones Profesionales Programadas · Elaboración de Solicitud de Transferencia a HD (→ ver Solicitud de Transferencia a HD (proceso)) · Encuesta de Satisfacción Usuaria al Egreso · Enfermera Coordinadora de HD · Enfermero o Enfermera Clínica · Entrega de Turno · Epicrisis al Alta · Episodio HODOM · Equipamiento Médico · Equipo de Gestión de Camas (→ ver Unidad de Gestión de Camas) · Equipo de Salud HD · Especialidad Pediátrica o Psiquiátrica · Establecimiento HODOM · Establecimiento que Otorga Prestaciones de Hospitalización Domiciliaria (→ ver Establecimiento HODOM) · Evaluación de Solicitud de Transferencia a HD · Evaluación Domiciliaria Inicial · Exclusiones de Ingreso a HD.

**F** — Fallecimiento en HD · Ficha Clínica · Fiscalización · Fonoaudiólogo o Fonoaudióloga · Formulario de Hospitalización Domiciliaria · Formulario de Ingreso.

**G** — Gestión de la Continuidad Asistencial.

**H** — Hospitalización Domiciliaria.

**I** — IAAS · Indicación Médica de HD · Inducción Obligatoria · Infraestructura · Insumos Clínicos · Interconsulta · ISAPRE.

**K** — Kinesiólogo o Kinesióloga.

**L** — Ley 16.744 · Ley 19.628 · Ley 19.880 · Ley 20.575 · Ley 20.584.

**M** — Manual de Organización Interna · Manual de Procedimientos · Medicamentos · Médico Cirujano de Atención Directa (→ ver Médico de Atención Directa) · Médico Cirujano Regulador (→ ver Médico Regulador) · Médico de Atención Directa · Médico Regulador · Médico Tratante de Atención Cerrada.

**N** — NT 2024 — Norma Técnica HODOM.

**O** — Otorgamiento de Consentimiento Informado (→ ver Suscripción de Consentimiento Informado) · Otros Profesionales y Técnicos.

**P** — Paciente · Paciente Agudo · Paciente Crónico Reagudizado · Paciente Egresado · Paciente en HD Activa · Paciente Transferible · Pase de Visita Diario · Personal Administrativo y Auxiliar · Plan de Capacitación Anual (PAC) · Plan de Contingencia Operacional · Plan de Cuidados de Enfermería · Plan de Egreso · Plan Terapéutico y de Cuidados · Prestador de Hospitalización Domiciliaria en Convenio · Prestador en Convenio · Programa de Mantención Preventiva · Protocolos Clínicos.

**R** — Radio de Cobertura · RCP Básica · Realización de Transferencia a HD (→ ver Transferencia a HD) · Receta Médica HODOM · Recepción de Solicitud de Transferencia · Red de Apoyo Familiar · Red de Apoyo Familiar, Social o Tutor Responsable (→ ver Red de Apoyo Familiar y Tutor Responsable) · REAS · Registro de Prestador Individual · Registro del Episodio de HD · Registro Evolutivo en Ficha Clínica · Reglamento Interno de Orden, Higiene y Seguridad · Reingreso Hospitalario · Reingreso Hospitalario Programado (→ ver Reingreso Hospitalario) · Renuncia Voluntaria · Reporte de Atención Profesional · Reporte de Información Clínico-Asistencial Relevante (→ ver Registro Evolutivo en Ficha Clínica) · Requisitos de Ingreso a HD · Res. Ex. N° 60/2022 · Res. Ex. N° 328/2023 · Res. Exenta N° 875/2013 · Resolución N° 7/2019 · Resolución de Solicitud de Transferencia · Respaldo Eléctrico · Resumen Clínico en Domicilio.

**S** — Sanción Sanitaria · SEC · Seguimiento Clínico · SEREMI · Servicios de Salud · Servicio o Unidad de Atención Cerrada · Sistema de Comunicaciones 24/7 · Sistema de Registro Clínico y Administrativo · Solicitud de Transferencia a HD (documento) · Solicitud de Transferencia a HD (proceso) · Soporte Vital Básico · Superintendencia de Salud · Suscripción de Consentimiento Informado.

**T** — Técnico de Enfermería · Trabajador o Trabajadora Social · Tramitación de Egreso de HD (→ ver Egreso de HD) · Transferencia a HD · Tutor Legal · Tutor Responsable.

**U** — Unidad de Gestión de Camas (UGC) · Unidad HODOM · Unidad o Servicio de Hospitalización Domiciliaria (→ ver Unidad HODOM) · Uso Certificado de Desfibrilador.

**V** — Vacunación del Personal Sanitario · Vehículos de Transporte · Verificación de Criterios de Ingreso a HD · Visita Domiciliaria.

---

## 10. Notas de uso

- **Trazabilidad normativa estricta**: cada entrada normada referencia artículo, letra o numeral y, cuando existe, inciso de la fuente primaria. Cuando una entrada compila exigencias de varios artículos, todos se citan. Las entradas derivadas de práctica operativa declaran expresamente esa naturaleza.
- **Forma denotativa**: la definición está formulada como predicado normativo (sujeto + obligación + condición). Las coletillas valorativas no son admisibles.
- **Umbrales y plazos textuales**: horas, años de experiencia, vigencias y plazos figuran con su valor exacto y su carácter (mínimo, máximo, acumulativo, sustitutivo, prorrogable).
- **Sinónimos disciplinados**: sólo aquellas formas efectivamente usadas en la práctica chilena o en las fuentes citadas.
- **Términos relacionados**: red semántica funcional; no son referencias decorativas.
- **Campos auxiliares** (`Funciones`, `Notas`, `Excepciones`, `Distinción`, `Requisito profesional`): se usan únicamente cuando la normativa enumera obligaciones específicas, plantea matices interpretativos críticos, contempla salvedades expresas, existe riesgo objetivo de confusión entre términos próximos o se requiere precisar el perfil profesional.
- **Distinciones explícitas**: el glosario fuerza distinciones entre pares confundibles que históricamente se mezclan en la práctica: Solicitud (acto y documento) vs Formulario de HD (plantilla) vs Formulario de Ingreso; Plan Terapéutico y de Cuidados vs Plan de Cuidados de Enfermería; Atención Cerrada vs Atención Domiciliaria vs Hospitalización Domiciliaria; Coordinación (cargo institucional) vs Seguimiento Clínico (proceso asistencial); Unidad de Gestión de Camas vs Equipo de Salud HD; Médico de Atención Directa vs Médico Regulador vs Médico Tratante de Atención Cerrada; Red de Apoyo Familiar vs Tutor Responsable; Cuidador vs Tutor Legal; Agudización vs Complicación durante HD.
- **Entradas redirectoras**: los lemas reemplazados, disueltos, fusionados o desdoblados se conservan como entrada con la fórmula "→ ver X" hacia su sucesor canónico, para preservar la trazabilidad histórica del glosario.
- **Anclaje normativo art. 21 N° N**: los registros obligatorios derivados del art. 21 del DS 1/2022 se citan con su numeral exacto (Constancia de Fallecimiento N° 2, Encuesta de Satisfacción N° 3, Consentimiento Informado N° 4, Carta de Derechos y Deberes N° 5, Formulario de Ingreso N° 6, Plan de Cuidados de Enfermería y Plan Terapéutico N° 8, Reporte de Atención Profesional N° 9). Se corrige así la cita al art. 19 letra X que aparecía en v1.2.0 y versiones anteriores.
- **Referencias cruzadas con sigla entre paréntesis**: cuando un lema lleva sigla entre paréntesis como parte del rótulo canónico (p. ej. `Plan de Capacitación Anual (PAC)`, `Unidad de Gestión de Camas (UGC)`), las referencias cruzadas en otros campos `Relacionados:` pueden omitir la sigla y citar solo la parte canónica (`Plan de Capacitación Anual`, `Unidad de Gestión de Camas`). El lema sigue siendo unívoco por la parte canónica; no se requiere armonización literal cita por cita.
- **Sinónimos y siglas no se replican en el índice alfabético**: los sinónimos y siglas declarados dentro del campo `Sinónimos:` de una entrada (p. ej. DIGERA, UHD, TENS, CI, PAC, UGC, SRCA, CDD, AC, HD, HDOM, HaH, M.AD, M.Reg, M.Tratante AC, Enf.Coord HD, T.Social, Fono, DT) no se replican como entradas independientes ni como redirectores en el índice alfabético (sec. 9). El lector que busca por sigla debe consultar el lema canónico al que la sigla refiere. Se reservan los redirectores del índice exclusivamente para lemas renombrados, fusionados, disueltos o desdoblados en versiones previas (cambios editoriales de identidad del lema), no para sinónimos vigentes dentro de una entrada.
- **Letras unitarias del índice alfabético**: algunas letras del índice contienen una sola entrada (B, G, K, N). Es un reflejo del corpus normativo HODOM —ámbito acotado de fuentes primarias—, no una omisión del glosario. No se agregan lemas nuevos por simetría visual.
- **Criterio editorial de armonización**: si dos fuentes tensionan, prevalece DS 1/2022 sobre NT 2024 sobre Acto Exento N° 31/2024.
- **Versionado**: este glosario es v1.3.2. Cualquier cambio en la normativa o en la práctica institucional consolidada exige incrementar versión y registrar el motivo en el manifiesto.
