---
_manifest:
  urn: urn:salud:kb:hodom-glosario-terminologico
  provenance:
    created_by: Claude Code (Opus 4.7, 1M context) con Felix Sanhueza Luna
    created_at: '2026-05-14'
    updated_at: '2026-05-18'
    sources:
      - urn:salud:kb:hodom-reglamento-ds1-2022
      - urn:salud:kb:hodom-decreto-exento-31-2024
      - urn:salud:kb:hodom-norma-tecnica-2024
      - urn:salud:kb:hodom-direccion-tecnica
      - urn:salud:kb:salubrista
      - urn:salud:kb:hodom-manual-alta-complejidad
version: 1.4.0
status: published
tags:
  - hodom
  - glosario
  - terminologia
  - normativa
  - hospitalizacion-domiciliaria
  - vocabulario-controlado
  - polymath-authored
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:hodom-glosario-terminologico
    polymath_authored: true
    authority_layer: polymath
relations:
  cites:
    - urn:salud:kb:hodom-reglamento-ds1-2022
    - urn:salud:kb:hodom-decreto-exento-31-2024
    - urn:salud:kb:hodom-norma-tecnica-2024
    - urn:salud:kb:hodom-direccion-tecnica
    - urn:salud:kb:salubrista
    - urn:salud:kb:hodom-manual-alta-complejidad
---

# Glosario Terminológico de Hospitalización Domiciliaria (HODOM)

Vocabulario controlado del dominio HODOM derivado de las fuentes normativas vigentes en Chile y, desde v1.4.0, ampliado con vocabulario técnico-salubrista internacional cuando la precisión semántica lo exige.

**Fuentes normativas primarias chilenas:**

- **DS 1/2022 MINSAL** — Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria (25 artículos).
- **Acto Exento N° 31/2024 MINSAL** — Aprueba la Norma Técnica HODOM (05-jun-2024, Ministra Ximena Aguilera Sanhueza).
- **NT 2024** — Norma Técnica para Establecimientos que Otorgan Prestaciones de HD (texto anexo al Acto Exento, 16 páginas).

**Fuentes técnicas no normativas** (introducidas en v1.4.0 como anclaje complementario): Hospital at Home Society (USA), NHS Virtual Wards Operational Framework, Victoria Health HITH Guidelines, Cochrane Reviews HaH, CMS Acute Hospital Care at Home Waiver, OMS (CISP, High 5s, telemedicina), AHRQ, NANDA/NIC/NOC, AHA, NEWS2, LACE, Zarit, Donabedian, Reid-Haggerty, entre otros.

## Criterio editorial — autoridad polymath (v1.4.0)

Hasta v1.3.2, el glosario operaba bajo la regla `norma > técnica`. Desde v1.4.0, el criterio editorial es:

> **La norma chilena es piso, no techo. La precisión semántica es vector primario. Cuando la precisión clínica, salubrista o internacional exija una distinción que la norma chilena no hace, el glosario la propone con anclaje técnico explícito y declarado.**

Esto **no** desautoriza la norma: cada lema con sustento normativo conserva su cita `Fuente:` con artículo, letra o numeral exactos. La armonización entre fuentes chilenas se mantiene como antes: `DS 1/2022 > NT 2024 > Acto Exento N° 31/2024`. La novedad es que el glosario:

- **Refina definiciones normativas** cuando son operacionalmente sub-precisas, declarando el alza en un campo `Refinamiento polymath:`.
- **Incorpora lemas sin sustento normativo chileno** cuando la práctica salubrista internacional o local los requiere, declarando la autoridad sustantiva en un campo `Anclaje técnico:`.
- **Distingue conceptos que la norma chilena confunde** (Complicación vs Evento Adverso vs Incidente; Agudización vs Descompensación vs Exacerbación; Categorización vs Estratificación de Riesgo).

## Esquema por entrada

Esquema fijo: `Definición:` y `Fuente:` (obligatorios, salvo excepciones declaradas). Campos opcionales: `Sinónimos:`, `Relacionados:`, `Funciones:`, `Notas:`, `Excepciones:`, `Distinción:`, `Requisito profesional:`.

**Campos introducidos en v1.4.0** (autoridad polymath):

- **`Anclaje técnico:`** — autoridad sustantiva no normativa (literatura, sociedad científica, estándar internacional). Obligatorio en lemas sin anclaje normativo chileno; opcional como complemento en lemas normativos.
- **`Refinamiento polymath:`** — declaración explícita cuando la definición va más allá de la literalidad normativa. Visibiliza el delta sobre la norma chilena.

**Excepciones al esquema**: (i) las entradas de la sección 8 (Normativa cruzada citada) son descripciones de fuentes y usan prosa libre, sin `Definición:` ni `Fuente:`; (ii) las entradas redirectoras conservan la fórmula `→ ver X` y prescinden de `Fuente:` (su autoridad es el cambio editorial declarado en el changelog); (iii) las entradas del Anexo Internacional (sección 11) usan `Estatus:` en lugar de `Fuente:` y son informativas, no prescriptivas para el modelo chileno.

## Tabla de contenidos

1. [Sistema y unidades](#1-sistema-y-unidades)
2. [Roles profesionales del Equipo de Salud HD](#2-roles-profesionales-del-equipo-de-salud-hd)
3. [Pacientes, estados y conceptos clínicos](#3-pacientes-estados-y-conceptos-clinicos)
4. [Procesos asistenciales](#4-procesos-asistenciales)
5. [Documentos y registros](#5-documentos-y-registros)
6. [Capacidad operativa](#6-capacidad-operativa)
7. [Indicadores operativos y de desempeño HODOM](#7-indicadores-operativos-y-de-desempeno-hodom) — **nueva en v1.4.0**
8. [Procedimientos y exigencias normativas](#8-procedimientos-y-exigencias-normativas)
9. [Calidad, seguridad y resultados](#9-calidad-seguridad-y-resultados) — **nueva en v1.4.0**
10. [Normativa cruzada citada](#10-normativa-cruzada-citada)
11. [Anexo terminológico internacional](#11-anexo-terminologico-internacional) — **nueva en v1.4.0**
12. [Índice alfabético](#12-indice-alfabetico)
13. [Notas de uso](#13-notas-de-uso)

---

## Changelog v1.3.2 → v1.4.0

Pasada de ampliación semántica con autoridad polymath sobre v1.3.2 (2026-05-18). Cambio mayor de criterio editorial; incorporación de vocabulario técnico-salubrista; reestructuración macro acotada.

### Cambio editorial mayor

- **Cambio del vector axiológico**: la norma chilena pasa de ser techo a ser piso del glosario. Se introduce el criterio editorial `precisión semántica como vector primario, anclaje técnico declarado cuando se va sobre la norma`.
- **Dos campos nuevos**: `Anclaje técnico:` (obligatorio en lemas sin sustento normativo chileno) y `Refinamiento polymath:` (declara delta sobre literalidad normativa).
- **Identidad del glosario**: pasa de `vocabulario controlado normativo` a `vocabulario controlado normativo-técnico` (declarado en frontmatter `family: normative-technical`).

### Reestructuración macro

- **Tres secciones nuevas**: 7 (Indicadores operativos y de desempeño HODOM), 9 (Calidad, seguridad y resultados), 11 (Anexo terminológico internacional). El resto de la macroestructura se conserva — la sec. 3 no se fragmenta (propuesta E.1 del salubrista rechazada por sobre-modularización; se usan encabezados `###` agrupadores dentro de la sección).
- **Renumeración**: las antiguas secciones 7 (Procedimientos y exigencias normativas), 8 (Normativa cruzada citada), 9 (Índice alfabético) y 10 (Notas de uso) pasan a 8, 10, 12 y 13 respectivamente.

### Refinamientos sobre lemas existentes (14, todos incorporados)

Se aplica `Refinamiento polymath:` a: `Hospitalización Domiciliaria`, `Paciente Agudo`, `Paciente Crónico Reagudizado`, `Condición Clínica Estable`, `Categorización del Paciente`, `Agudización`, `Complicación durante HD`, `Indicación Médica de HD`, `Plan Terapéutico y de Cuidados`, `Visita Domiciliaria`, `Atención No Programada`, `Seguimiento Clínico`, `Reingreso Hospitalario`, `Episodio HODOM`, `Egreso de HD`/`Causales de Egreso`.

### Lemas nuevos incorporados (27)

**Distinciones clínicas finas** (sec. 3): `Descompensación`, `Exacerbación`, `Reagudización`, `Intercurrencia`, `Evento Adverso en HD` (sec. 9), `Incidente en HD` (sec. 9), `Casi-Evento (Near Miss) en HD` (sec. 9).

**Procesos de evaluación y respuesta** (sec. 4): `Cribado de Idoneidad`, `Estratificación de Riesgo`, `Triage Domiciliario`, `Contacto Asincrónico`, `Conciliación de Medicamentos`.

**Modalidades de HD** (sec. 4, lema agrupador): `Modalidades de HD por Línea Clínica` (incluye HD Médico, Quirúrgico, Paliativo, Pediátrico, Salud Mental — agrupados, no como cinco lemas separados por anti-inflación). `HD Admisión-Evitada` y `HD Alta-Temprana Asistida` se mantienen como lemas autónomos por su impacto operativo.

**Entorno social** (sec. 3): `Cuidador Formal`, `Cuidador Informal`, `Carga del Cuidador`, `Determinantes Sociales de la Salud aplicables a HD`.

**Conceptos farmacológicos** (sec. 3): `Polifarmacia`, `Adherencia al Plan`.

**Coordinación sistémica** (sec. 4): `Coordinación Interniveles`, `Continuum Asistencial`.

**Indicadores** (sec. 7, nueva): `Día-Cama HODOM`, `Índice Ocupacional HODOM`, `Estancia Media HODOM`, `Densidad de Visita`, `Carga Asistencial Domiciliaria`, `Tiempo de Respuesta a Evento No Programado`, `Reingreso Evitable`, `Marco Donabedian aplicado a HODOM`.

**Tipología de transferencia** (sec. 4): `Step-Up vs Step-Down`.

**Cartera complejizada** (sec. 1): `Cesta de Prestaciones Complejas (Alta Complejidad HODOM)`.

### Propuestas del salubrista rechazadas con razón

- **C.33 Brecha Territorial**: rechazada como lema autónomo. Razón: concepto de política sanitaria territorial, útil para diseño de red pero no para operación clínica HODOM. Se menciona como nota en `Radio de Cobertura`.
- **C.34 Caso Índice**: rechazada. Razón: terminología epidemiológica general, no específica HODOM. Su uso en HODOM no requiere lema propio; el lector que necesita el concepto lo consulta en texto epidemiológico estándar.
- **C.35 Cohorte HODOM**: rechazada. Razón: redundante con `Episodio HODOM` como unidad de análisis. Construcción académica que no aporta utilidad operativa al clínico.
- **C.13–C.17 cinco modalidades por línea clínica**: reformuladas en un único lema agrupador `Modalidades de HD por Línea Clínica`. Razón: cinco lemas separados producirían inflación lemática sin ganancia semántica neta; la distinción operacional es suficiente con un lema agrupador.
- **E.1 fragmentación de sec. 3 en seis subsecciones**: rechazada. Razón: sobre-modularización que rompe familiaridad del lector. Se reemplaza por agrupamiento visual con encabezados `###` dentro de la sección.
- **E.2 reclasificación de `Indicación Médica de HD` como acto clínico separado**: rechazada. Razón: la distinción acto-clínico vs proceso-institucional ya está resuelta por la `Distinción:` recíproca con `Solicitud de Transferencia a HD (proceso)` (P2-8 de v1.3.2). Crear una subsección editorial nueva aporta menos de lo que cuesta.
- **B.1 separación de HaH como lema autónomo dentro del cuerpo principal**: parcialmente aceptada. Razón: se mantiene `HaH` como sinónimo internacional dentro de `Hospitalización Domiciliaria` y se define `Hospital at Home (HaH)` como lema autónomo del **Anexo Internacional (sec. 11)**, no como duplicado en sec. 4. Esto resuelve la tensión taxonómica sin romper la coherencia interna del corpus chileno.

### Anclajes técnicos complementarios (11 incorporados)

A las entradas existentes: `IAAS`, `Soporte Vital Básico / RCP`, `Plan Terapéutico y de Cuidados`, `Consentimiento Informado`, `Encuesta de Satisfacción Usuaria al Egreso`, `Reingreso Hospitalario`, `Ficha Clínica / SRCA`, `Sistema de Comunicaciones 24/7`, `Categorización del Paciente`, `Continuidad Asistencial`, `Programa de Mantención Preventiva`.

### Anexo internacional (sec. 11)

Once entradas informativas: `Hospital at Home (HaH)`, `Virtual Ward`, `Hospital in the Home (HITH)`, `Inpatient-at-Home`, `Subacute Care / SNF-ST`, `LTACH`, `IRF`, `Transitional Care`, `Step-Down Unit`, `Rapid Response Team`, `OPAT`.

### Conteo

- Lemas v1.3.2: 174.
- Lemas v1.4.0: aprox. 218 (174 + 27 nuevos cuerpo principal + 11 anexo internacional + 6 indicadores; ajustes por agrupamientos y redirectores).
- Secciones: 13 (vs 10 en v1.3.2).
- Anclajes técnicos no normativos declarados: 38 entradas con campo `Anclaje técnico:`.

### Anclajes normativos previos

No se modifican. Los anclajes art. 19 y art. 21 N° N verificados en v1.3.0–v1.3.2 se conservan idénticos.

---

## Changelog histórico

Para los changelogs previos (v1.2 → v1.3, v1.3.0 → v1.3.1, v1.3.1 → v1.3.2) consultar el archivo `glosario-terminologico-hodom-v1.3.0.md`, conservado como histórico.

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

- **Definición**: listado formal de prestaciones que el Establecimiento HODOM brinda en domicilio, declarado entre los antecedentes de la solicitud de Autorización Sanitaria. La necesidad de una prestación no incluida en la cartera configura **exclusión categórica** de ingreso (art. 17 letra c). En la práctica operativa chilena y según el catálogo FONASA, se distinguen al menos dos niveles de intensidad: **baja complejidad** (código FONASA 0201408 y derivados, cuidados básicos post-egreso) y **alta complejidad** (Cesta de Prestaciones Complejas, ver entrada siguiente). Cada Establecimiento HODOM declara explícitamente qué prestaciones de cada nivel ofrece.
- **Fuente**: DS 1/2022 art. 5 letra n (antecedente exigido); art. 17 letra c (causal de exclusión); NT 2024 §Equipamiento (instrumentos adicionales según cartera).
- **Anclaje técnico**: MINSAL Norma Técnica N° 238/2024; FONASA Catálogo de Prestaciones (códigos 0201408 y derivados); Manual de Alta Complejidad HODOM (KB local).
- **Refinamiento polymath**: la norma chilena trata la cartera como listado plano; el glosario v1.4.0 introduce la **distinción operativa por nivel de complejidad** (baja vs alta), reconocida en la práctica chilena por FONASA y en la literatura HaH internacional. El delta sobre la norma: la cartera ya no es solo "qué hace" sino "con qué intensidad".
- **Sinónimos**: Cartera de Prestaciones de HD, Listado de Prestaciones, Oferta de Prestaciones HODOM.
- **Relacionados**: Cesta de Prestaciones Complejas (Alta Complejidad HODOM), Modalidades de HD por Línea Clínica.

### Cesta de Prestaciones Complejas (Alta Complejidad HODOM)

- **Definición**: subconjunto de la Cartera de Prestaciones HODOM correspondiente a procedimientos y terapias de alta intensidad que aproximan el cuidado domiciliario al estándar de cama hospitalaria. Incluye, entre otras: terapias endovenosas prolongadas, oxigenoterapia con titulación dinámica, ventilación mecánica no invasiva domiciliaria, manejo de drenajes y catéteres venosos centrales, soporte transfusional, quimioterapia domiciliaria, antibioticoterapia parenteral OPAT, manejo de heridas complejas y ostomías de alta demanda. **Se distingue** del modelo HODOM de baja complejidad (cuidados básicos post-egreso) y, cuando se ofrece, exige equipamiento, protocolos y dotación específicos.
- **Fuente**: práctica operativa chilena emergente; complementa DS 1/2022 art. 5 letra n y NT 2024 §Equipamiento.
- **Anclaje técnico**: Manual de Alta Complejidad HODOM (KB local); MINSAL Norma Técnica N° 238/2024; código FONASA 0201408 (baja complejidad, contraste); Levine DM et al. *Hospital-Level Care at Home for Acutely Ill Adults* Ann Intern Med 2020;172:77–85 (modelo CMS de alta complejidad); Caplan GA *Hospital in the Home — Then and Now* MJA 2020.
- **Distinción**: la **Cesta de Prestaciones Complejas** define el techo de intensidad clínica que el Establecimiento HODOM puede asumir; la **Cartera de Prestaciones HODOM** es el listado completo (baja + alta complejidad).
- **Relacionados**: Cartera de Prestaciones HODOM, Modalidades de HD por Línea Clínica, OPAT (sec. 11), Equipamiento Médico.

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

- **Definición**: integrante del Equipo de Salud HD, médico cirujano con experiencia mínima de 2 años **en regulación médica** (no sustituible por experiencia médico-quirúrgica general), con cursos vigentes de IAAS de 80 horas, soporte vital básico / RCP de 3 horas y uso certificado de desfibrilador. Presta atención a distancia o atención directa durante la HD. Opera además como triador en Atención No Programada (Triage Domiciliario).
- **Fuente**: DS 1/2022 art. 13 letra b; NT 2024 §Requisitos resumidos por cargo; Acto Exento N° 31/2024 §Criterio de armonización (no sustitución por experiencia médico-quirúrgica general).
- **Requisito profesional**: médico cirujano con al menos 2 años de experiencia en regulación médica.
- **Sinónimos**: M.Reg, Médico Regulador HD.
- **Notas**: el mismo profesional del Médico de Atención Directa puede cumplir simultáneamente esta función (DS 1/2022 art. 13 letra b inciso final). Puede emplear tecnologías de información y comunicación con el mismo alcance clínico del Médico de Atención Directa.
- **Relacionados**: Médico de Atención Directa, Triage Domiciliario, Atención No Programada, Sistema de Comunicaciones 24/7.

### Médico Cirujano Regulador

- **Definición**: lema renombrado en v1.3.0. → ver Médico Regulador.

### Enfermero o Enfermera Clínica

- **Definición**: integrante del Equipo de Salud HD, enfermero o enfermera con experiencia clínica mínima de 2 años, curso vigente de soporte vital básico, curso vigente de IAAS de 80 horas y certificación vigente de uso de desfibrilador.
- **Fuente**: DS 1/2022 art. 13 letra c; NT 2024 §Habilitación y §Requisitos resumidos por cargo.
- **Requisito profesional**: 2 años de experiencia clínica y curso vigente de Soporte Vital Básico.
- **Sinónimos**: Enfermera Clínica, Enf.Clínica.
- **Funciones (DS 1/2022 art. 13 letra c)**: participar en la evaluación de pacientes hospitalizados para gestionar ingreso y egreso; evaluar al paciente en cada Visita Domiciliaria con instrumentos acordes para visualizar evolución y flujos de derivación; gestionar cuidados mediante el Plan de Cuidados de Enfermería y la ejecución del Plan Terapéutico y de Cuidados según complejidad; educar a paciente, familia y cuidadores sobre plan terapéutico y autocuidado.
- **Relacionados**: Plan de Cuidados de Enfermería, Visita Domiciliaria, Conciliación de Medicamentos.

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
- **Funciones (DS 1/2022 art. 13 letra f)**: elaborar el Diagnóstico Social del Hogar (vivienda, servicios sanitarios básicos, acceso a telefonía y accesos viales); verificar la disponibilidad de Cuidador o Tutor Legal; evaluar la situación económica del grupo familiar; confeccionar el informe y seguimiento de evaluación e intervención social; elaborar el informe social; colaborar en la gestión y coordinación de derivaciones; participar en reuniones del equipo clínico; **valorar Carga del Cuidador y Determinantes Sociales de la Salud aplicables a HD cuando el riesgo lo amerite**.
- **Relacionados**: Diagnóstico Social del Hogar, Red de Apoyo Familiar, Cuidador, Carga del Cuidador, Determinantes Sociales de la Salud aplicables a HD.

### Fonoaudiólogo o Fonoaudióloga

- **Definición**: profesional adicional del Equipo de Salud HD que el Establecimiento HODOM incorpora según la Cartera de Prestaciones ofrecida al paciente y su familia.
- **Fuente**: DS 1/2022 art. 14 inciso primero (otros profesionales y técnicos según prestaciones).
- **Sinónimos**: Fono.

### Otros Profesionales y Técnicos

- **Definición**: profesionales o técnicos adicionales —fonoaudiólogo, nutricionista, terapeuta ocupacional, psicólogo, químico farmacéutico u otros— que el Establecimiento HODOM puede incorporar al Equipo de Salud HD según la Cartera de Prestaciones ofrecida al paciente y su familia.
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

### Tipología clínica del paciente

#### Paciente

- **Definición**: persona destinataria del proceso de Hospitalización Domiciliaria, en una de las dos categorías clínicas reconocidas por la NT 2024 —paciente agudo o paciente crónico reagudizado—, que cumple los Requisitos de Ingreso a HD y permanece bajo control y plan terapéutico del Equipo de Salud HD hasta el Egreso de HD.
- **Fuente**: NT 2024 §Definiciones; DS 1/2022 art. 1 (ámbito subjetivo) y art. 15 (requisitos de ingreso).
- **Relacionados**: Paciente Transferible, Paciente en HD Activa, Paciente Egresado.

#### Paciente Agudo

- **Definición**: persona con cuadro clínico agudo **de novo** o sin comorbilidad clínicamente significativa que condicione el manejo, en estado de inestabilidad fisiopatológica que justifica régimen hospitalario y que, una vez alcanzada Condición Clínica Estable, puede completar tratamiento en HD.
- **Fuente**: NT 2024 §Definiciones (texto base: "persona sin patología previa, con cuadro clínico agudo que requiere hospitalización para recuperar la salud").
- **Refinamiento polymath**: la NT 2024 usa la cláusula "sin patología previa", clínicamente vacía dado que prácticamente todo adulto que se hospitaliza tiene comorbilidades. El refinamiento sustituye por "**de novo** o sin comorbilidad clínicamente significativa que condicione el manejo", criterio operacionalmente útil para la triagación y el plan terapéutico.
- **Anclaje técnico**: Charlson ME *A new method of classifying prognostic comorbidity in longitudinal studies* J Chronic Dis 1987 (Charlson Comorbidity Index); Vincent C, Amalberti R *Safer Healthcare* 2016.
- **Distinción**: a diferencia del **Paciente Crónico Reagudizado**, el Paciente Agudo no exige plan estructurado de manejo de condición de base, sólo del evento agudo y su recuperación.

#### Paciente Crónico Reagudizado

- **Definición**: persona con una o más patologías crónicas conocidas que presenta **exacerbación o descompensación clínica** —de su enfermedad de base o intercurrente— suficiente para requerir régimen hospitalario, y que, una vez alcanzada Condición Clínica Estable, puede completar tratamiento o el período crítico de monitorización en HD. **Implica** evaluación explícita de carga de comorbilidad (Charlson, CIRS-G) y plan de manejo de la condición de base, no sólo del evento agudo.
- **Fuente**: NT 2024 §Definiciones (texto base: "persona con patología previa y cuadro clínico agudo —asociado o no a esa patología de base— que requiere hospitalización para recuperar la salud").
- **Refinamiento polymath**: el glosario explicita el mecanismo (exacerbación / descompensación / intercurrencia) y exige plan de manejo de la condición de base. La norma chilena enuncia el caso pero no operacionaliza el manejo.
- **Anclaje técnico**: Charlson CCI 1987; CIRS-G (Miller MD et al. *Rating chronic medical illness burden* Psychiatry Res 1992); GOLD Report (exacerbación EPOC); ACC/AHA/HFSA Guidelines (descompensación IC).
- **Relacionados**: Exacerbación, Descompensación, Reagudización, Intercurrencia, Polifarmacia.

#### Condición Clínica Estable

- **Definición**: estado clínico que cumple, en conjunto, los siguientes criterios operacionalizables: (i) **estabilidad hemodinámica** (PAS ≥ 90 mmHg sin drogas vasoactivas, FC dentro de rango individualizado); (ii) **estabilidad respiratoria** (SatO2 ≥ 90% con FiO2 manejable en domicilio, sin requerimiento de ventilación mecánica invasiva ni VNI de soporte vital continuo no manejable en domicilio); (iii) **estabilidad neurológica** (sin deterioro agudo del estado de conciencia); (iv) **estabilidad metabólica** (sin trastornos electrolíticos o glicémicos no controlables ambulatoriamente); (v) **ausencia de necesidad de monitorización continua invasiva**; (vi) **ausencia de necesidad previsible de cuidados intensivos en 24–48 horas**. Permite el traslado seguro al domicilio aún con patología no resuelta o sólo parcialmente solucionada. Requisito de ingreso a HD.
- **Fuente**: NT 2024 §Definiciones (texto base: "equilibrio de las funciones vitales que permite el traslado del paciente al domicilio pese a una patología no resuelta o sólo parcialmente solucionada"); DS 1/2022 art. 15 letra a.
- **Refinamiento polymath**: la definición normativa "equilibrio de funciones vitales" es semánticamente vaga. El glosario v1.4.0 introduce seis criterios operacionalizables convergentes con la práctica HaH internacional, sin contradecir la norma sino convirtiéndola en aplicable a la cabecera de la cama.
- **Anclaje técnico**: Manual de Alta Complejidad HODOM (KB local); Levine DM *Hospital-Level Care at Home for Acutely Ill Adults* Ann Intern Med 2020 (criterios CMS Acute Hospital Care at Home Waiver); InterQual criteria; MCG Health Care Guidelines.

### Estados del paciente en el episodio

#### Paciente Transferible

- **Definición**: estado clínico-administrativo del paciente hospitalizado en Atención Cerrada que cumple los cuatro Requisitos de Ingreso a HD del art. 15 y por tanto es susceptible de Transferencia a HD.
- **Fuente**: derivado de DS 1/2022 art. 15.
- **Distinción**: **Transferible** es estado previo a la Transferencia; **en HD Activa** es estado durante el episodio; **Egresado** es estado tras el Egreso de HD.

#### Paciente en HD Activa

- **Definición**: estado clínico-administrativo del paciente durante el Episodio HODOM, entre la Transferencia a HD exitosa y el Egreso de HD.
- **Fuente**: derivado de DS 1/2022 art. 1; art. 16.
- **Distinción**: **Transferible** es estado previo a la Transferencia; **en HD Activa** es el estado actual durante el episodio; **Egresado** es estado tras el Egreso de HD.
- **Relacionados**: Transferencia a HD, Episodio HODOM, Visita Domiciliaria, Plan Terapéutico y de Cuidados.

#### Paciente Egresado

- **Definición**: estado clínico-administrativo del paciente al término del Episodio HODOM por cualquiera de las seis Causales de Egreso del art. 16.
- **Fuente**: DS 1/2022 art. 16.
- **Distinción**: **Transferible** es estado previo a la Transferencia; **en HD Activa** es estado durante el episodio; **Egresado** es el estado final tras el Egreso de HD.
- **Relacionados**: Egreso de HD, Causales de Egreso, Epicrisis al Alta, Encuesta de Satisfacción Usuaria al Egreso.

### Conceptos clínicos transversales del episodio

#### Agudización

- **Definición**: empeoramiento clínico significativo del paciente durante el Episodio HODOM, agnóstico respecto del mecanismo causal específico, que exige reevaluación por el Equipo de Salud HD y eventual escalamiento. **Comprende cuatro mecanismos diferenciables** —descompensación de la condición índice, exacerbación de enfermedad crónica de base, reagudización tras mejoría transitoria, intercurrencia clínica no relacionada— cuya distinción es clínicamente relevante para la decisión de Reingreso Hospitalario y para la trazabilidad epidemiológica del Episodio HODOM.
- **Fuente**: DS 1/2022 art. 8 letra l (coordinación de agudización y reingreso); art. 16 letra c.
- **Refinamiento polymath**: la norma usa `Agudización` como término genérico sin desagregar mecanismos. El glosario v1.4.0 lo conserva como término paraguas y agrega cuatro lemas autónomos (Descompensación, Exacerbación, Reagudización, Intercurrencia) para precisar el mecanismo causal cuando importa.
- **Anclaje técnico**: GOLD Report (definición operacional de exacerbación EPOC); ESC HF Guidelines (descompensación IC); Cochrane Reviews HaH (clasificación de eventos adversos durante HaH).
- **Distinción**: la **Agudización** es deterioro clínico (eje fisiopatológico, agnóstico); la **Complicación durante HD** es evento adverso o intercurrencia (eje causal); el **Evento Adverso en HD** es daño atribuible a la atención (sec. 9). Los tres pueden detonar Reingreso Hospitalario pero por razones distintas.

#### Descompensación

- **Definición**: ruptura del equilibrio fisiopatológico de la condición clínica que motivó el ingreso del paciente, durante el Episodio HODOM, con manifestación clínica detectable que requiere reevaluación e intervención. Subtipo específico de Agudización por el eje causal: el mecanismo es el deterioro de la condición índice misma, no de una comorbilidad ni de un evento nuevo.
- **Fuente**: no normada por DS 1/2022 ni NT 2024 con definición específica; uso clínico estándar.
- **Anclaje técnico**: ESC Heart Failure Guidelines (descompensación IC, criterios diagnósticos); ADA Diabetes Standards of Care (descompensación cetoacidótica); Dorland's Illustrated Medical Dictionary (32 ed).
- **Distinción**: la **Descompensación** afecta a la condición índice; la **Exacerbación** afecta a una enfermedad crónica de base; la **Intercurrencia** es un evento nuevo no relacionado.
- **Relacionados**: Agudización, Atención No Programada, Reingreso Hospitalario.

#### Exacerbación

- **Definición**: intensificación aguda y habitualmente reversible de una enfermedad crónica preexistente del paciente durante el Episodio HODOM, definida operacionalmente conforme guías clínicas específicas según la enfermedad (p.ej. exacerbación de EPOC: aumento sostenido de disnea, tos o producción de esputo más allá de la variabilidad habitual, GOLD).
- **Fuente**: no normada; uso clínico estándar.
- **Anclaje técnico**: GOLD Report 2024 (exacerbación EPOC); GINA *Global Strategy for Asthma Management* (exacerbación asma); ACC/AHA/HRS Atrial Fibrillation Guidelines.
- **Distinción**: la **Exacerbación** se aplica típicamente a condiciones crónicas con curso fluctuante (EPOC, asma, IC, EM, AR); la **Descompensación** denota colapso fisiopatológico, habitualmente más severo; la **Reagudización** enfatiza el patrón temporal (segundo episodio tras estabilización).
- **Relacionados**: Paciente Crónico Reagudizado, Agudización, Atención No Programada.

#### Reagudización

- **Definición**: nueva fase clínica aguda del paciente tras un período de estabilización transitoria durante el Episodio HODOM. Implica trayectoria temporal en al menos dos tiempos (agudización inicial → estabilización → reagudización). Subtipo específico de Agudización con énfasis cronológico.
- **Fuente**: no normada; terminología clínica estándar empleada también por la NT 2024 en el descriptor `Paciente Crónico Reagudizado`.
- **Anclaje técnico**: terminología clínica estándar; práctica salubrista nacional; Diccionario de la Real Academia Nacional de Medicina de España.
- **Distinción**: la **Reagudización** enfatiza el patrón temporal de retorno tras mejoría; la **Exacerbación** enfatiza la intensificación de una crónica; la **Descompensación** enfatiza el mecanismo fisiopatológico.
- **Relacionados**: Paciente Crónico Reagudizado, Agudización.

#### Intercurrencia

- **Definición**: evento clínico nuevo durante el Episodio HODOM **no relacionado** con la condición que motivó el ingreso ni con sus comorbilidades conocidas, que exige reevaluación independiente (p.ej. infección urinaria en paciente ingresado por celulitis; síndrome coronario agudo en paciente en HD por exacerbación de EPOC).
- **Fuente**: no normada; terminología clínica estándar.
- **Anclaje técnico**: terminología clínica estándar; Diccionario de la Real Academia Nacional de Medicina de España; Dorland Medical Dictionary.
- **Distinción**: la **Intercurrencia** es evento nuevo no relacionado; la **Complicación durante HD** suele estar causalmente vinculada a la enfermedad índice o al procedimiento; el **Evento Adverso en HD** es daño atribuible a la atención misma.
- **Relacionados**: Agudización, Complicación durante HD, Atención No Programada, Reingreso Hospitalario.

#### Complicación durante HD

- **Definición**: evento clínico desfavorable durante el Episodio HODOM **causado por la condición clínica de base o por su tratamiento** (infección, sangrado, descompensación de comorbilidad, evento relacionado con un procedimiento), que se gestiona dentro del proceso o detona Reingreso Hospitalario según gravedad. **Se distingue conceptualmente de Evento Adverso en HD** (lesión causada por la atención de salud, no por la enfermedad subyacente) y de **Incidente en HD** (acción u omisión que pudo o no causar daño).
- **Fuente**: DS 1/2022 art. 8 letra l; art. 16 letra c.
- **Refinamiento polymath**: el texto previo del glosario fundía Complicación, Evento Adverso e Intercurrencia. El glosario v1.4.0 las separa conforme la convención internacional de seguridad del paciente (OMS CISP). Las Complicaciones se registran en el Registro Evolutivo en Ficha Clínica; los Eventos Adversos exigen además notificación al sistema de calidad y seguridad institucional conforme Norma Técnica N° 154/2013.
- **Anclaje técnico**: OMS *Marco Conceptual de la Clasificación Internacional para la Seguridad del Paciente* (CISP, 2009); IOM *To Err is Human* 1999; AHRQ Patient Safety Network 2024; Norma Técnica N° 154/2013 MINSAL.
- **Relacionados**: Evento Adverso en HD (sec. 9), Incidente en HD (sec. 9), Agudización, Intercurrencia, Atención No Programada, Reingreso Hospitalario.

### Entorno social y soporte

#### Red de Apoyo Familiar

- **Definición**: red personal colectiva del paciente (familia, allegados, vecinos) a cargo de su cuidado, compañía y sostén en el domicilio durante el Episodio HODOM. Su existencia y disponibilidad efectiva son requisito de ingreso a HD y son verificadas por el o la Trabajador Social.
- **Fuente**: DS 1/2022 art. 15 letra c; art. 13 letra f.
- **Sinónimos**: Red de Apoyo.
- **Relacionados**: Tutor Responsable, Cuidador, Cuidador Formal, Cuidador Informal, Tutor Legal, Diagnóstico Social del Hogar, Carga del Cuidador.
- **Distinción**: la **Red de Apoyo Familiar** es colectiva; el **Tutor Responsable** es la figura individual nominada como referente del paciente ante el equipo.

#### Red de Apoyo Familiar, Social o Tutor Responsable

- **Definición**: lema desdoblado en v1.3.0. → ver Red de Apoyo Familiar y Tutor Responsable.

#### Tutor Responsable

- **Definición**: persona individual nominada como referente del paciente ante el Equipo de Salud HD cuando el paciente no puede ejercer por sí mismo la representación operativa del proceso. Requisito de ingreso alternativo o complementario a la Red de Apoyo Familiar.
- **Fuente**: DS 1/2022 art. 15 letra c.
- **Distinción**: el **Tutor Responsable** es figura referencial ante el equipo de salud; el **Tutor Legal** es figura jurídica con representación formal del paciente.
- **Relacionados**: Red de Apoyo Familiar, Cuidador, Tutor Legal.

#### Cuidador

- **Definición**: persona que ejerce la función práctica de cuidado directo del paciente en el domicilio durante el Episodio HODOM. Su disponibilidad es verificada por el o la Trabajador Social como parte del Diagnóstico Social del Hogar. Comprende dos subtipos operativos: **Cuidador Informal** (familiar o allegado sin formación profesional ni remuneración formal — patrón mayoritario en HODOM Chile) y **Cuidador Formal** (persona asignada por sistema sociosanitario con función específica).
- **Fuente**: DS 1/2022 art. 13 letra f; art. 15 letra c.
- **Distinción**: el **Cuidador** realiza función práctica de cuidado en el domicilio; el **Tutor Legal** puede o no ser cuidador y opera en el plano jurídico.
- **Relacionados**: Cuidador Formal, Cuidador Informal, Carga del Cuidador, Tutor Responsable, Tutor Legal, Red de Apoyo Familiar, Diagnóstico Social del Hogar, Trabajador o Trabajadora Social.

#### Cuidador Informal

- **Definición**: persona del entorno del paciente (familiar, allegado, vecino), sin formación profesional específica ni remuneración formal del sistema, que ejerce función práctica de cuidado en domicilio durante el Episodio HODOM. Patrón mayoritario en HODOM Chile. Su disponibilidad efectiva y suficiencia para la carga estimada es verificada por el Trabajador o Trabajadora Social.
- **Fuente**: no normada; práctica nacional y literatura sociosanitaria.
- **Anclaje técnico**: SENAMA (programa Cuidados Domiciliarios); OMS *Long-Term Care for Older People* 2017; SUBDERE-Chile *Política Nacional de Cuidados*; Programa Chile Cuida (Subsecretaría de Servicios Sociales).
- **Relacionados**: Cuidador, Cuidador Formal, Carga del Cuidador, Red de Apoyo Familiar.

#### Cuidador Formal

- **Definición**: persona contratada o asignada por el sistema sanitario o social, con función específica de cuidado al paciente en domicilio, que **complementa** o **suple** al cuidador informal cuando éste no existe o presenta carga insostenible. En Chile aplicable cuando el paciente es beneficiario de Chile Cuida o SENAMA, o cuando el Establecimiento contrata directamente cuidador. No exime al Establecimiento HODOM de verificar disponibilidad efectiva de cuidador conforme DS 1/2022 art. 15 letra c.
- **Fuente**: no normada en DS 1/2022 ni NT 2024 específicamente.
- **Anclaje técnico**: Programa Chile Cuida (Subsecretaría de Servicios Sociales); SENAMA; OMS *Long-Term Care*.
- **Relacionados**: Cuidador, Cuidador Informal, Diagnóstico Social del Hogar.

#### Cuidador / Tutor Legal

- **Definición**: lema desdoblado en v1.3.0. → ver Cuidador y Tutor Legal.

#### Tutor Legal

- **Definición**: persona con representación legal formal del paciente (curador, tutor judicial o equivalente) habilitada para suscribir el Consentimiento Informado y otros actos jurídicos en nombre del paciente.
- **Fuente**: DS 1/2022 art. 15 letra d; Ley 20.584.
- **Sinónimos**: Representante Legal.
- **Relacionados**: Tutor Responsable, Cuidador, Consentimiento Informado, Suscripción de Consentimiento Informado.

#### Carga del Cuidador

- **Definición**: dimensión clínico-social del impacto físico, emocional, financiero y social del cuidado prolongado sobre el cuidador (formal o informal). Se valora con instrumentos estandarizados, principalmente la **Escala de Sobrecarga del Cuidador de Zarit** (versiones de 22, 12 o 7 ítems) o el **Caregiver Strain Index** (Robinson). Carga alta es predictor de Renuncia Voluntaria, claudicación del cuidado y desenlaces adversos del paciente. Su evaluación basal y seguimiento son recomendables en HD prolongada.
- **Fuente**: no normada por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: Zarit SH, Reever KE, Bach-Peterson J *Relatives of the impaired elderly: correlates of feelings of burden* The Gerontologist 1980;20:649–55; Robinson BC *Validation of a Caregiver Strain Index* J Gerontol 1983;38:344–8; Adelman RD et al. *Caregiver Burden: A Clinical Review* JAMA 2014;311:1052–60; OMS *Long-Term Care for Older People* 2017.
- **Relacionados**: Cuidador, Diagnóstico Social del Hogar, Renuncia Voluntaria, Trabajador o Trabajadora Social.

#### Diagnóstico Social del Hogar

- **Definición**: informe del Trabajador o Trabajadora Social que caracteriza la vivienda, los servicios sanitarios básicos, la telefonía, los accesos viales, la disponibilidad de Cuidador o Tutor Legal, la situación socioeconómica del grupo familiar del paciente y, cuando proceda, la Carga del Cuidador y los Determinantes Sociales de la Salud aplicables a HD. Insumo de la Verificación de Criterios de Ingreso.
- **Fuente**: DS 1/2022 art. 13 letra f.
- **Refinamiento polymath**: el glosario v1.4.0 incorpora explícitamente la Carga del Cuidador y los Determinantes Sociales de la Salud como dimensiones a integrar en el informe cuando el riesgo lo amerite. La norma chilena no lista estas dimensiones pero tampoco las excluye.
- **Anclaje técnico**: OMS *Social Determinants of Health Framework* 2010; SENAMA; Manual Alta Complejidad HODOM (KB local).
- **Sinónimos**: Informe Social del Hogar.
- **Relacionados**: Carga del Cuidador, Determinantes Sociales de la Salud aplicables a HD, Cuidador.

#### Determinantes Sociales de la Salud aplicables a HD

- **Definición**: condiciones del entorno del paciente que modulan la viabilidad y los outcomes del Episodio HODOM: ingreso económico del hogar, hacinamiento, seguridad alimentaria, acceso a transporte de emergencia, brecha digital, alfabetización en salud, idioma primario del cuidador, seguridad del vecindario. Su evaluación es competencia del Trabajador Social y se integra al Diagnóstico Social del Hogar. **Determinantes sociales adversos pueden configurar exclusión funcional del ingreso a HD aun sin estar listados taxativamente en el art. 17 del DS 1/2022.**
- **Fuente**: no normada por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: OMS *Social Determinants of Health Framework* 2010; CSDH *Closing the Gap in a Generation* 2008; Marmot M *The Health Gap* 2015; Manual de Alta Complejidad HODOM (KB local); literatura HaH (Leff, Levine).
- **Refinamiento polymath**: la norma chilena enumera taxativamente las exclusiones de ingreso en el art. 17 (cuatro causales). El glosario v1.4.0 introduce la noción de **exclusión funcional** por determinantes sociales adversos —no equivalente a una nueva exclusión jurídica, sino a una imposibilidad operativa que el Equipo de Salud HD debe reconocer y registrar—. Esto va sobre la norma porque la norma chilena tiene un déficit operativo en este punto.
- **Relacionados**: Diagnóstico Social del Hogar, Cuidador, Carga del Cuidador, Hospitalización Domiciliaria.

### Conceptos farmacológicos transversales

#### Polifarmacia

- **Definición**: uso simultáneo de **5 o más medicamentos** por el paciente (definición operativa OMS más extendida; "polifarmacia mayor" con ≥10 medicamentos según algunos autores). Factor de riesgo independiente de eventos adversos medicamentosos, interacciones, caídas y reingreso. Indicación expresa de Conciliación de Medicamentos al ingreso y de evaluación periódica durante el Episodio HODOM.
- **Fuente**: no normada por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: OMS *Medication Without Harm — Polypharmacy* (Technical Report 2019); Masnoon N et al. *What is polypharmacy? A systematic review of definitions* BMC Geriatrics 2017;17:230; Beers Criteria (AGS 2023); STOPP/START Criteria (O'Mahony 2015).
- **Relacionados**: Plan Terapéutico y de Cuidados, Conciliación de Medicamentos, Adherencia al Plan, Evento Adverso en HD.

#### Adherencia al Plan

- **Definición**: grado en que el paciente y su cuidador siguen las indicaciones farmacológicas, dietéticas, de cuidados y de seguimiento del Plan Terapéutico y de Cuidados durante el Episodio HODOM. Distinta de la adherencia ambulatoria por el contexto institucional supervisado del régimen hospitalario domiciliario. Su evaluación periódica es responsabilidad del Equipo de Salud HD; la no adherencia activa atribuible al paciente, tutor o cuidador puede configurar Alta Disciplinaria (art. 16 letra f).
- **Fuente**: no normada explícitamente como concepto, pero referida implícitamente por DS 1/2022 art. 16 letra f (no adherencia al tratamiento o indicaciones como causal de Alta Disciplinaria).
- **Anclaje técnico**: OMS *Adherence to Long-Term Therapies: Evidence for Action* 2003; Sabaté E (ed) *Adherence concepts*; Osterberg L, Blaschke T *Adherence to Medication* N Engl J Med 2005;353:487–97.
- **Relacionados**: Plan Terapéutico y de Cuidados, Polifarmacia, Conciliación de Medicamentos, Alta Disciplinaria.

### Entorno espacial del paciente

#### Domicilio del Paciente

- **Definición**: residencia del paciente que cumple condiciones sanitarias mínimas, servicios básicos y telefonía, situada dentro del Radio de Cobertura del Establecimiento HODOM. Requisito de ingreso a HD.
- **Fuente**: DS 1/2022 art. 15 letra b.
- **Relacionados**: Coordenadas del Domicilio, Radio de Cobertura, Diagnóstico Social del Hogar.

#### Radio de Cobertura

- **Definición**: área geográfica dentro de la cual el Establecimiento HODOM garantiza factibilidad de acceso para la atención en domicilio, declarada en el contexto de los vehículos de transporte y la cartera. La residencia del paciente debe encontrarse dentro de él para configurar el requisito de ingreso de la letra b del art. 15.
- **Fuente**: DS 1/2022 art. 15 letra b (referencia textual); NT 2024 §Equipamiento (vehículos de transporte y radio operativo).
- **Notas**: el Radio de Cobertura es un parámetro operativo; la equidad territorial efectiva del sistema HODOM país depende también de la densidad de Establecimientos por área (brecha territorial), tema de política sanitaria fuera del alcance de este glosario.
- **Relacionados**: Domicilio del Paciente, Coordenadas del Domicilio, Vehículos de Transporte.

### Unidad temporal-administrativa

#### Episodio HODOM

- **Definición**: unidad temporal, administrativa, **clínica y económica** de hospitalización domiciliaria. Comienza con la Transferencia a HD del paciente y termina con el Egreso de HD por una de las seis Causales del art. 16 del DS 1/2022. Es la unidad mínima de: (i) **agregación documental** de los registros obligatorios; (ii) **codificación clínica y costeo** (CIE-10, GRD HD cuando aplica); (iii) **producción de indicadores** (Estancia Media, Índice Ocupacional, reingreso); (iv) **comparación interinstitucional**. **Regla operativa de continuidad**: un Reingreso Hospitalario a Atención Cerrada cierra el Episodio HODOM (causal c del art. 16). Si tras ese reingreso el paciente vuelve a HD, se considera **nuevo Episodio HODOM**; la trazabilidad longitudinal del paciente se preserva en la Ficha Clínica unificada, no en el Episodio.
- **Fuente**: DS 1/2022 art. 1; art. 16; art. 21.
- **Refinamiento polymath**: la norma chilena trata el Episodio como unidad temporal-administrativa. El glosario v1.4.0 lo amplía a unidad clínica y económica, base de codificación e indicadores, y agrega la regla operativa de continuidad (reingreso → cierre del episodio → eventual nuevo episodio), no explícita en la norma.
- **Anclaje técnico**: CMS *Acute Hospital Care at Home Waiver* — definición de episode of care; MINSAL *Norma de Codificación GRD* 2023; OECD *Health Care Quality Indicators framework* 2023.
- **Sinónimos**: Episodio de HD.
- **Relacionados**: Día-Cama HODOM, Índice Ocupacional HODOM, Estancia Media HODOM.

#### Coordenadas del Domicilio

- **Definición**: representación informacional de la ubicación geográfica del Domicilio del Paciente, generada durante la Verificación de Criterios de Ingreso a HD. Sustenta la verificación del Radio de Cobertura y la planificación logística de las Visitas Domiciliarias.
- **Fuente**: práctica operativa; complementa DS 1/2022 art. 15 letra b y NT 2024 §Protocolos clínicos (programación de rutas y visitas domiciliarias).
- **Relacionados**: Domicilio del Paciente, Radio de Cobertura.

---

## 4. Procesos asistenciales

### Hospitalización Domiciliaria

- **Definición**: modalidad asistencial **sustitutiva o continuatoria** de la hospitalización tradicional en atención cerrada, dirigida a pacientes agudos o crónicos reagudizados clínicamente estables, en la que el equipo de salud traslada al domicilio la **intensidad clínica, los recursos diagnósticos y terapéuticos y la responsabilidad médica continua** propios del régimen hospitalario, bajo el criterio de **equivalencia o no inferioridad de outcomes** respecto a la cama hospitalaria. Requiere indicación médica, plan terapéutico interdisciplinario, control médico al menos diario (presencial o por equivalente tecnológico clínicamente justificado), cobertura 24/7 y término por egreso formal. Sin HD, el paciente habría requerido permanencia en atención cerrada (criterio jurídico de pertinencia, DS 1/2022 art. 1).
- **Fuente**: DS 1/2022 art. 1 incisos primero y segundo (texto base: "modalidad asistencial alternativa a la hospitalización tradicional ... con cuidados similares en calidad y cantidad ... sin los cuales habría sido necesaria su permanencia en atención cerrada"); NT 2024 §Definiciones.
- **Refinamiento polymath**: el texto normativo "similares en calidad y cantidad" oculta tres precisiones operativas críticas: (i) el criterio de **equivalencia de outcomes** (la HaH internacional se valida por outcomes equivalentes o superiores, no por similitud de procesos); (ii) la dicotomía técnica **sustitutiva** (admisión evitada) vs **continuatoria** (alta temprana asistida), que la norma chilena oblitera al sesgar implícitamente hacia ESD; (iii) la exigencia operativa nuclear de **visita médica diaria o equivalente** y de cobertura 24/7, criterio definitorio internacional de HaH. El glosario v1.4.0 las explicita.
- **Anclaje técnico**: Leff B *Hospital at home: feasibility and outcomes of a program to provide hospital-level care at home for acutely ill older patients* Ann Intern Med 2005;143:798–808; Levine DM et al. *Hospital-Level Care at Home for Acutely Ill Adults* Ann Intern Med 2020;172:77–85; Shepperd S et al. *Admission avoidance hospital at home* Cochrane Database Syst Rev 2016;9:CD007491; Hospital at Home Society USA *Standards for Hospital at Home Programs* 2024; Manual de Alta Complejidad HODOM (KB local).
- **Sinónimos**: HD, HDOM, HaH (Hospital at Home, designación internacional — relación de género/especie: HaH es género internacional, HODOM es variante chilena; ver Anexo Internacional sec. 11), Hospitalización en Domicilio.
- **Distinción**: la **HD** es régimen hospitalario en domicilio; la **Atención Cerrada** es régimen hospitalario en cama hospitalaria; la **Atención Domiciliaria** es régimen ambulatorio de libre elección, no regida por el DS 1/2022 (art. 3).
- **Relacionados**: HD Admisión-Evitada, HD Alta-Temprana Asistida, Modalidades de HD por Línea Clínica, Hospital at Home (HaH) (sec. 11).

### Atención Domiciliaria

- **Definición**: acciones de salud realizadas en domicilio por prestadores en modalidad **ambulatoria y de libre elección**. **No constituye** Hospitalización Domiciliaria y se encuentra expresamente excluida del ámbito del DS 1/2022.
- **Fuente**: NT 2024 §Definiciones; DS 1/2022 art. 3 (exclusión expresa).
- **Distinción**: ver "Hospitalización Domiciliaria".

### Indicación Médica de HD

- **Definición**: acto clínico —no acto institucional procesal— por el cual un médico habilitado indica el ingreso del paciente a la modalidad HD por cumplir Condición Clínica Estable, factibilidad terapéutica en domicilio y Requisitos de Ingreso. **Origen institucional posible**: (i) Médico Tratante de Atención Cerrada, en el modelo Early-Supported-Discharge (alta hospitalaria asistida, modelo chileno hegemónico); (ii) médico de urgencia o (iii) médico de atención primaria, en el modelo Admission-Avoidance (admisión evitada, no formalmente desarrollado por la NT 2024 pero compatible con DS 1/2022 art. 1); (iv) Médico Regulador HD en triaje proactivo. La Indicación es la **decisión clínica anterior**; la Solicitud de Transferencia a HD (proceso) es el **acto institucional posterior** que la materializa en el documento Solicitud.
- **Fuente**: DS 1/2022 art. 1 (componente estructural de la HD: "requiere indicación médica"); art. 15.
- **Refinamiento polymath**: el glosario hasta v1.3.2 restringía la Indicación al Médico Tratante de AC, lo que excluía implícitamente los modelos de Admission-Avoidance. El glosario v1.4.0 expande el origen institucional posible a cuatro fuentes, coherente con DS 1/2022 art. 1 (que no restringe quién emite la Indicación) y con la práctica HaH internacional.
- **Anclaje técnico**: Shepperd S et al. *Admission avoidance hospital at home* Cochrane 2016;9:CD007491; Levine DM 2020 (CMS Acute Hospital Care at Home Waiver, admisión desde urgencias); NHS England *Virtual Wards Operational Framework* 2022; Australia Victoria Health *Hospital in the Home Guidelines* 2017.
- **Distinción**: la Indicación Médica de HD es la **decisión clínica** del médico habilitado que precede al acto procesal. La Solicitud de Transferencia a HD (proceso) es el **acto institucional posterior** que materializa esa decisión en el documento Solicitud. Una sin la otra no produce transferencia: sin Indicación Médica previa no hay legitimidad clínica para iniciar el proceso documental.
- **Relacionados**: Solicitud de Transferencia a HD (proceso), Médico Tratante de Atención Cerrada, Médico Regulador, Requisitos de Ingreso a HD, HD Admisión-Evitada, HD Alta-Temprana Asistida.

### HD Admisión-Evitada

- **Definición**: modalidad de Hospitalización Domiciliaria en que el paciente ingresa **directamente** a HD desde servicios de urgencia, atención primaria o comunidad, **sin pasar por hospitalización en cama hospitalaria**. La Indicación Médica puede originarse en el médico de urgencia, médico de APS o Médico Regulador HD vía triaje proactivo. Aporta mayor evitación de costos hospitalarios y menor exposición a IAAS hospitalaria. Compatible con DS 1/2022 art. 1 (que no exige paso previo por AC), no formalmente desarrollada en la NT 2024.
- **Fuente**: no normada explícitamente en DS 1/2022 ni NT 2024.
- **Anclaje técnico**: Shepperd S *Admission avoidance hospital at home* Cochrane 2016;9:CD007491; Levine DM 2020 (CMS waiver, admisión desde urgencias); NHS Virtual Wards Operational Framework.
- **Refinamiento polymath**: la norma chilena sesga implícitamente hacia ESD pero no prohíbe AA. El glosario v1.4.0 introduce el lema para visibilizar la modalidad como compatible con el marco normativo y para abrir espacio operativo a programas que la implementen.
- **Sinónimos**: HD-AA, Admission-Avoidance HD.
- **Distinción**: contrasta con HD Alta-Temprana Asistida (paciente proviene de AC con paso previo por cama hospitalaria).
- **Relacionados**: HD Alta-Temprana Asistida, Step-Up vs Step-Down, Indicación Médica de HD.

### HD Alta-Temprana Asistida

- **Definición**: modalidad de Hospitalización Domiciliaria en que el paciente, previamente hospitalizado en Atención Cerrada, completa la fase final de su tratamiento hospitalario en domicilio bajo el Equipo de Salud HD. La Indicación Médica se origina en el Médico Tratante de Atención Cerrada. **Modelo operativo dominante en el sistema HODOM chileno** conforme DS 1/2022 y NT 2024.
- **Fuente**: implícita en DS 1/2022 art. 1 y arts. 15–16 (paso AC → HD → Egreso); NT 2024 §Definiciones.
- **Anclaje técnico**: Shepperd S et al. *Early discharge hospital at home* Cochrane Database Syst Rev 2017;6:CD000356; Norma Técnica N° 243/2025 MINSAL (HD como proceso transversal); Manual de Alta Complejidad HODOM (KB local).
- **Sinónimos**: HD-ESD, Early-Supported-Discharge HD.
- **Distinción**: contrasta con HD Admisión-Evitada (sin paso previo por AC).
- **Relacionados**: HD Admisión-Evitada, Step-Up vs Step-Down, Médico Tratante de Atención Cerrada.

### Modalidades de HD por Línea Clínica

- **Definición**: clasificación operativa de la HD según el perfil clínico del paciente y la cartera de prestaciones especializadas que requiere. Cinco modalidades reconocidas en la práctica HaH internacional y emergentes en el sistema HODOM chileno:
  - **HD Médico**: pacientes con condición médica aguda (neumonía, insuficiencia cardiaca descompensada, ITU complicada, celulitis, exacerbación de EPOC). Modelo fundacional y mayoritario.
  - **HD Quirúrgico**: pacientes post-operatorios o con complicaciones quirúrgicas no resolutivas: infección de sitio quirúrgico, manejo de ostomías, recuperación tras cirugía mayor (laparoscopía, bariátrica, reversión de ileostomía), íleo prolongado. Requiere exclusión absoluta de necesidad de reintervención inminente.
  - **HD Paliativa**: pacientes con enfermedad avanzada o terminal que requieren cuidados paliativos de **intensidad hospitalaria**: manejo de síntomas refractarios, sedación paliativa, soporte transfusional, paracentesis evacuadora repetida. Se distingue del programa GES de Alivio del Dolor y Cuidados Paliativos (ambulatorio) por la intensidad y el régimen.
  - **HD Pediátrica**: niños y adolescentes que requieren régimen hospitalario en domicilio. Requiere médico cirujano pediatra o con experiencia documentada de al menos 2 años en pediatría (NT 2024) y adecuaciones operativas específicas.
  - **HD en Salud Mental**: pacientes psiquiátricos **estables** en continuación de tratamiento, **excluyendo los descompensados** (DS 1/2022 art. 17 letra b). Modelo emergente internacional (crisis resolution home treatment teams).
- **Fuente**: no normada con esta taxonomía completa por DS 1/2022 ni NT 2024; HD Pediátrica y HD en Salud Mental están parcialmente abordadas por NT 2024 §Especialidades exigidas y por la Norma Técnica N° 243/2025; las demás son distinciones operativas.
- **Anclaje técnico**: Manual de Alta Complejidad HODOM (KB local); NHS Virtual Wards (virtual wards específicas por especialidad); Norma Técnica N° 243/2025 MINSAL; AAP *Pediatric Hospital at Home Statement*; NHS *Crisis Resolution Home Treatment Teams Manual* 2014.
- **Refinamiento polymath**: el glosario v1.4.0 introduce una taxonomía por línea clínica que la norma chilena no formula como tal. La decisión editorial es agruparlas en **un solo lema** (vs cinco lemas autónomos propuestos por el salubrista) para evitar inflación lemática sin perder la distinción operativa.
- **Relacionados**: Cartera de Prestaciones HODOM, Cesta de Prestaciones Complejas, Especialidad Pediátrica o Psiquiátrica.

### Step-Up vs Step-Down

- **Definición**: tipología operativa de la Transferencia que el Establecimiento HODOM puede recibir, según la intensidad de cuidado previa del paciente:
  - **Step-Down HD**: paciente proveniente de **mayor intensidad de cuidado** (Atención Cerrada, unidad de cuidados intermedios) que continúa en HD. Modalidad estándar del Early-Supported-Discharge.
  - **Step-Up HD**: paciente proveniente de **menor intensidad de cuidado** (APS, ambulatorio, urgencia sin ingreso) que escala a HD por necesidad clínica. Modalidad propia del Admission-Avoidance.

  La operación inicial recomendada de un Establecimiento HODOM es step-down para consolidar logística; la expansión madura incorpora step-up.
- **Fuente**: no normada por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: Manual de Alta Complejidad HODOM (KB local); literatura HaH (terminología estándar); Levine DM 2020.
- **Relacionados**: HD Admisión-Evitada, HD Alta-Temprana Asistida, Transferencia a HD, Indicación Médica de HD.

### Atención Profesional

- **Definición**: cada acción asistencial individual ejecutada en domicilio por un integrante del Equipo de Salud HD durante una Visita Domiciliaria o, según corresponda, durante un Contacto Asincrónico (consulta médica, kinesiterapia motora o respiratoria, curaciones, administración de medicamentos, evaluación de enfermería, educación al paciente y cuidador, intervención social, otros).
- **Fuente**: DS 1/2022 art. 13 (funciones por cargo); art. 21 N° 9 (registro descriptivo del proceso asistencial).
- **Distinción**: la Atención Profesional es la **acción asistencial específica**; la Visita Domiciliaria es el **acto unitario** (presencial o virtual sincrónico) que la contiene; el Contacto Asincrónico es interacción no sincrónica.
- **Relacionados**: Visita Domiciliaria, Contacto Asincrónico.

### Visita Domiciliaria

- **Definición**: acto asistencial unitario en que un integrante del Equipo de Salud HD interactúa con el paciente en su Domicilio para ejecutar una o más Atenciones Profesionales según el Plan Terapéutico y de Cuidados. **Tipología**: (i) **Visita Domiciliaria Presencial** —el profesional se presenta físicamente en el domicilio—; (ii) **Visita Domiciliaria Virtual** (videoconsulta sincrónica con interacción audiovisual bidireccional). El **Contacto Asincrónico** (mensajería, telemetría, monitoreo remoto) **no constituye** Visita Domiciliaria stricto sensu pero forma parte del Seguimiento Clínico. La sustitución de visita presencial por virtual requiere criterio clínico expreso y registro en Ficha Clínica.
- **Fuente**: DS 1/2022 art. 13; NT 2024 §Protocolos clínicos (programación de rutas y visitas domiciliarias).
- **Refinamiento polymath**: la definición previa restringía la visita a presencia física, lo que excluía la visita virtual que en HaH avanzado es parte sustantiva del seguimiento. El glosario v1.4.0 tipifica presencial vs virtual sincrónica y separa el Contacto Asincrónico como categoría distinta. Internacionalmente hay debate sobre si la visita virtual puede sustituir la visita médica diaria exigida; el glosario adopta posición intermedia (requiere criterio clínico expreso y registro).
- **Anclaje técnico**: NHS England *Virtual Wards Operational Framework* 2022; American Telemedicine Association *Telehealth Practice Guidelines* 2023; Hospital at Home Society *Standards for Hospital at Home Programs* 2024 (definición de "visit equivalence"); OMS *Consolidated telemedicine implementation guide* 2022.
- **Distinción**: la **Visita Domiciliaria** es el acto unitario; la **Atención Profesional** es la acción asistencial específica realizada durante la visita; el **Seguimiento Clínico** es el proceso longitudinal del Episodio HODOM; el **Contacto Asincrónico** es interacción no sincrónica.
- **Relacionados**: Atención Profesional, Contacto Asincrónico, Seguimiento Clínico, Densidad de Visita.

### Contacto Asincrónico

- **Definición**: interacción del Equipo de Salud HD con el paciente o cuidador **no sincrónica**: mensajería de texto clínica, correo electrónico, telemetría, monitoreo remoto de signos vitales, alertas automatizadas. **No constituye** Visita Domiciliaria pero forma parte del Seguimiento Clínico. Se registra en Ficha Clínica con trazabilidad de fecha, hora, contenido y respuesta.
- **Fuente**: no normada por DS 1/2022 ni NT 2024 con definición específica; complementa NT 2024 §Infraestructura mínima (sistema de comunicaciones con trazabilidad).
- **Anclaje técnico**: NHS Virtual Wards Framework; American Telemedicine Association *Telehealth Practice Guidelines* 2023; OMS *Consolidated telemedicine implementation guide* 2022.
- **Distinción**: el **Contacto Asincrónico** es no sincrónico y no requiere presencia simultánea; la **Visita Domiciliaria Virtual** es sincrónica con interacción audiovisual bidireccional; la **Visita Domiciliaria Presencial** es in situ.
- **Relacionados**: Visita Domiciliaria, Seguimiento Clínico, Atención No Programada, Sistema de Comunicaciones 24/7.

### Solicitud de Transferencia a HD (proceso)

- **Definición**: acto del Médico Tratante de Atención Cerrada (o del médico habilitado conforme el modelo operativo, ver Indicación Médica de HD) por el cual origina el proceso de transferencia mediante la generación del documento Solicitud de Transferencia a HD, usando el Formulario de Hospitalización Domiciliaria como plantilla, con el contenido mínimo aplicable de los registros del art. 21 del DS 1/2022.
- **Fuente**: DS 1/2022 art. 15; art. 21; práctica operativa hospitalaria.
- **Distinción**: el proceso supone una Indicación Médica de HD previa (decisión clínica). Sin Indicación no hay legitimidad clínica para iniciar el proceso documental: la Indicación es la decisión clínica anterior; este proceso es el acto institucional que la materializa en el documento Solicitud.
- **Notas**: el acto procesal de Solicitud y el documento Solicitud se distinguen por el contexto; cuando se requiere precisión, usar "acto de Solicitud" para el proceso y "documento Solicitud" para la instancia documental.
- **Relacionados**: Solicitud de Transferencia a HD (documento), Formulario de Hospitalización Domiciliaria, Médico Tratante de Atención Cerrada, Indicación Médica de HD.

### Elaboración de Solicitud de Transferencia a HD

- **Definición**: lema renombrado en v1.3.0. → ver Solicitud de Transferencia a HD (proceso).

### Evaluación de Solicitud de Transferencia a HD

- **Definición**: proceso por el cual el Equipo de Salud HD examina la Solicitud y resuelve sobre el ingreso del paciente. Se realiza en tres etapas operativas sucesivas: recepción, verificación de criterios y resolución.
- **Fuente**: DS 1/2022 art. 13 letra a (participación del Médico AD en evaluación de pacientes para ingreso y egreso); art. 13 letra c (idem para Enfermero o Enfermera Clínica); art. 15 (requisitos); art. 17 (exclusiones); práctica operativa.
- **Relacionados**: Recepción de Solicitud de Transferencia, Verificación de Criterios de Ingreso a HD, Resolución de Solicitud de Transferencia, Cribado de Idoneidad.

### Cribado de Idoneidad

- **Definición**: filtro inicial binario que aplica el Equipo de Salud HD para determinar si un paciente es candidato a ingreso a HD, basado en criterios duros: diagnóstico elegible conforme cartera, Condición Clínica Estable, residencia en Radio de Cobertura, presencia de Red de Apoyo o Cuidador, y ausencia de Exclusiones del art. 17. Es operación **previa** a la Categorización del Paciente y a la Estratificación de Riesgo. **Equivale operacionalmente** a la Verificación de Criterios de Ingreso a HD del corpus normativo chileno, expresada en la terminología internacional de eligibility screening.
- **Fuente**: no normada con este nombre por DS 1/2022 ni NT 2024; equivalente operativo a Verificación de Criterios de Ingreso a HD.
- **Anclaje técnico**: Hospital at Home Society *Eligibility Screening Standards* 2024; NHS Virtual Wards Framework 2022.
- **Distinción**: el **Cribado de Idoneidad** es binario y categórico; la **Estratificación de Riesgo** es continua y probabilística (riesgo de eventos adversos); la **Categorización del Paciente** clasifica demanda de cuidado (intensidad asistencial).
- **Relacionados**: Verificación de Criterios de Ingreso a HD, Estratificación de Riesgo, Categorización del Paciente.

### Recepción de Solicitud de Transferencia

- **Definición**: primera etapa operativa de la Evaluación; la Solicitud entra al canal institucional del Establecimiento HODOM y queda formalmente recibida para su revisión. Habitualmente ejecutada por la Enfermera Coordinadora de HD.
- **Fuente**: práctica operativa hospitalaria.
- **Notas**: transición del estado del documento: `creada → recibida`.

### Verificación de Criterios de Ingreso a HD

- **Definición**: segunda etapa operativa de la Evaluación; contraste de los antecedentes del paciente contra los cuatro Requisitos de Ingreso del art. 15 (clínico, residencial, red de apoyo, consentimiento) y las cuatro Exclusiones del art. 17 (inestabilidad clínica o sin diagnóstico; salud mental descompensada; prestación no incluida en cartera; alta disciplinaria previa). Incluye dimensiones concurrentes: la clínica, a cargo del médico (Regulador o de Atención Directa); y las dimensiones territorial, red de apoyo, voluntariedad y logística, a cargo de la Enfermera Coordinadora con apoyo del o de la Trabajador Social.
- **Fuente**: DS 1/2022 art. 15 letras a–d; art. 17 letras a–d; art. 13 letras a, c y f.
- **Relacionados**: Requisitos de Ingreso a HD, Exclusiones de Ingreso a HD, Cribado de Idoneidad.
- **Notas**: transición del estado del documento: `recibida → evaluada`.

### Resolución de Solicitud de Transferencia

- **Definición**: tercera etapa operativa de la Evaluación; cierra la Solicitud con uno de cuatro resultados: aceptación, rechazo categórico (configuración de exclusión del art. 17), rechazo condicional (subsanable mediante antecedentes o adecuaciones) o resultado no concluyente que requiere antecedentes adicionales.
- **Fuente**: DS 1/2022 art. 15 (criterios) y art. 17 (exclusiones); práctica operativa.
- **Notas**: transición del estado del documento: `evaluada → respondida` con uno de los cuatro resultados (aceptada, rechazo categórico, rechazo condicional, no concluyente).

### Transferencia a HD

- **Definición**: proceso por el cual el paciente pasa físicamente desde el Servicio de Atención Cerrada al Domicilio. Admite dos modalidades excluyentes de traslado: (i) por medios propios de la Red de Apoyo, y (ii) traslado coordinado institucional, en cuyo caso se ejecuta por servicio de traslado propio del Establecimiento HODOM o por tercero en convenio gestionado en el hospital por la Unidad de Gestión de Camas.
- **Fuente**: DS 1/2022 art. 1; art. 8 letra ñ; art. 15; NT 2024 §Equipamiento (servicio de traslado propio o tercero en convenio).
- **Relacionados**: Unidad de Gestión de Camas, Red de Apoyo Familiar, Acuerdo de Traslado a Atención Cerrada, Step-Up vs Step-Down.

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

- **Definición**: conjunto de evaluaciones profesionales del Equipo de Salud HD ejecutadas al inicio del Episodio HODOM en el domicilio (médica de atención directa, de enfermería, kinésica, social y otras según cartera), cuyas conclusiones se integran para constituir y ajustar el Plan Terapéutico y de Cuidados. Incluye la **Conciliación de Medicamentos al ingreso**. Las evaluaciones pueden ser asincrónicas.
- **Fuente**: DS 1/2022 art. 13 letras a, c, d, f (funciones de evaluación inicial por cargo); NT 2024 §Protocolos clínicos (evaluación e ingreso).
- **Relacionados**: Plan Terapéutico y de Cuidados, Conciliación de Medicamentos, Estratificación de Riesgo, Categorización del Paciente.

### Conciliación de Medicamentos

- **Definición**: proceso estructurado, realizado por médico o enfermero clínico al ingreso del paciente al Episodio HODOM, de comparar la lista de medicamentos previa a la hospitalización con las indicaciones generadas durante AC y con el plan de HD, identificando omisiones, duplicaciones, interacciones y errores. **Se repite al Egreso** comparando indicaciones HD con plan ambulatorio. Estándar internacional de seguridad del paciente (OMS High 5s Project: 'Medication Reconciliation').
- **Fuente**: no normada por DS 1/2022 ni NT 2024 con esta denominación; complementa DS 1/2022 art. 8 letra j (registros clínicos íntegros) y art. 21 N° 8 (plan terapéutico).
- **Anclaje técnico**: OMS *High 5s Action on Patient Safety: Standard Operating Protocol for Medication Reconciliation* 2014; IHI *How-to Guide: Prevent Adverse Drug Events Medication Reconciliation* 2011; JCI International Patient Safety Goals (Goal 3); Norma Técnica N° 154/2013 MINSAL.
- **Distinción**: la **Conciliación de Medicamentos** se ejecuta al ingreso y al egreso del episodio; el **Plan Terapéutico y de Cuidados** es el instrumento que la incorpora; la **Polifarmacia** es factor de riesgo que la hace especialmente necesaria.
- **Relacionados**: Plan Terapéutico y de Cuidados, Plan de Egreso, Polifarmacia, Evento Adverso en HD, Receta Médica HODOM.

### Ejecución de Atenciones Profesionales Programadas

- **Definición**: ejecución, registro y trazabilidad de las Visitas Domiciliarias y Atenciones Profesionales planificadas en el Plan Terapéutico y de Cuidados durante el Episodio HODOM; comprende programación, preparación, ejecución en domicilio y consignación en el Reporte de Atención Profesional.
- **Fuente**: DS 1/2022 art. 13 (funciones por cargo); art. 21 N° 9 (descripción del proceso asistencial con todas las atenciones); NT 2024 §Protocolos clínicos (programación de rutas y visitas domiciliarias).

### Seguimiento Clínico

- **Definición**: proceso longitudinal **interdisciplinario** del Equipo de Salud HD durante el Episodio HODOM que comprende la observación clínica continua del paciente, la valoración de su evolución, el ajuste del Plan Terapéutico y de Cuidados, la Categorización del Paciente y la Estratificación de Riesgo, y el Registro Evolutivo en Ficha Clínica. **Exige frecuencia mínima de evaluación médica equivalente a la visita diaria hospitalaria**, sea presencial o por equivalente tecnológico clínicamente justificado. Se materializa operativamente en el Pase de Visita Diario y se documenta continuamente.
- **Fuente**: derivado de DS 1/2022 art. 11 letra b; art. 13 (funciones por cargo); art. 21; NT 2024 §Protocolos clínicos.
- **Refinamiento polymath**: el glosario v1.4.0 explicita el carácter interdisciplinario y la frecuencia mínima de evaluación médica (criterio definitorio internacional de HaH). La norma chilena exige seguimiento sin especificar frecuencia.
- **Anclaje técnico**: Leff B 2005; Levine DM 2020; Hospital at Home Society *Standards* — "daily physician encounter requirement"; NHS Virtual Wards Framework.
- **Relacionados**: Categorización del Paciente, Estratificación de Riesgo, Gestión de la Continuidad Asistencial, Coordinación, Pase de Visita Diario, Contacto Asincrónico.

### Categorización del Paciente

- **Definición**: proceso del Equipo de Salud HD que asigna a cada paciente una **categoría operacional** —típicamente alta/media/baja complejidad— que combina dos dimensiones distintas: (i) **estratificación de riesgo clínico** (probabilidad de deterioro, reingreso o mortalidad, valorada con instrumentos como Charlson, NEWS2, LACE Index o equivalentes); (ii) **categorización de carga asistencial** (intensidad de cuidado requerida: frecuencia y composición de Visitas Domiciliarias, complejidad de procedimientos, soporte ventilatorio o farmacológico). La categoría resultante determina la asignación de Densidad de Visita, la composición del equipo y la intensidad del Plan Terapéutico y de Cuidados. Se reevalúa al menos diariamente (Pase de Visita Diario).
- **Fuente**: NT 2024 §Protocolos clínicos (categorización del paciente).
- **Refinamiento polymath**: la norma chilena define la categorización como proceso para asignar frecuencia y composición de visitas, sin explicitar las dos dimensiones operativas que técnicamente la componen (riesgo y carga). El glosario v1.4.0 las desagrega; cuando la operación requiere precisión, ver Estratificación de Riesgo como lema autónomo para la dimensión probabilística pura.
- **Anclaje técnico**: NEWS2 (Royal College of Physicians UK, 2017); LACE Index (van Walraven C *Derivation and validation of an index to predict early death or unplanned readmission after discharge from hospital to the community* CMAJ 2010;182:551–7); Charlson Comorbidity Index 1987; AHRQ *Care Coordination Quality Measures* 2023; Hospital at Home Society *Standards for HaH Programs* 2024.
- **Distinción**: la **Categorización del Paciente** combina riesgo y carga; la **Estratificación de Riesgo** mide solo riesgo (probabilístico); el **Cribado de Idoneidad** es filtro binario previo; el **Triage Domiciliario** clasifica eventos no programados.
- **Relacionados**: Estratificación de Riesgo, Cribado de Idoneidad, Triage Domiciliario, Seguimiento Clínico, Plan Terapéutico y de Cuidados, Visita Domiciliaria, Densidad de Visita.

### Estratificación de Riesgo

- **Definición**: clasificación continua del paciente por probabilidad de eventos adversos durante el Episodio HODOM (deterioro clínico, Reingreso Hospitalario, Fallecimiento), valorada con instrumentos estandarizados como LACE Index, HOSPITAL Score, NEWS2, Charlson Comorbidity Index. **Operación distinta** de la Categorización del Paciente (que combina riesgo y demanda de cuidado). Se actualiza al menos diariamente y al cambio significativo del estado clínico.
- **Fuente**: no normada explícitamente por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: van Walraven C *LACE Index* CMAJ 2010; Donzé J et al. *HOSPITAL Score* JAMA Intern Med 2013;173:632–8; Royal College of Physicians UK *NEWS2* 2017; Charlson ME 1987.
- **Distinción**: ver Categorización del Paciente.
- **Relacionados**: Categorización del Paciente, Plan Terapéutico y de Cuidados, Reingreso Evitable.

### Triage Domiciliario

- **Definición**: proceso operativo de clasificación de eventos clínicos no programados durante el Episodio HODOM —análogo al triage de urgencias— que aplica el Médico Regulador o profesional habilitado del Equipo de Salud HD ante una llamada, alerta o evento detectado en domicilio. Asigna nivel de prioridad (p.ej. emergencia / urgente / consulta diferible) y modalidad de respuesta (visita inmediata presencial / consulta telefónica resolutiva / agendamiento próxima visita / escalamiento a urgencias).
- **Fuente**: no normada con este nombre por DS 1/2022 ni NT 2024; componente operativo implícito en NT 2024 §Protocolos clínicos (actuación ante emergencias).
- **Anclaje técnico**: NHS Virtual Wards Framework; Australia Victoria Health HITH Guidelines; analogía con sistemas ESI (Emergency Severity Index) y MTS (Manchester Triage System).
- **Relacionados**: Atención No Programada, Médico Regulador, Sistema de Comunicaciones 24/7, Tiempo de Respuesta a Evento No Programado.

### Gestión de la Continuidad Asistencial

- **Definición**: proceso del Equipo de Salud HD que articula los pasos de continuidad entre el Episodio HODOM y los actores externos (Atención Cerrada, Atención Primaria, especialidades, redes sociales) durante el episodio y al Egreso, asegurando que la atención del paciente no se interrumpa.
- **Fuente**: derivado de DS 1/2022 art. 8 letras l y n; art. 11 letras c y g; NT 2024 §Protocolos clínicos.
- **Relacionados**: Continuidad Asistencial, Coordinación Interniveles, Continuum Asistencial, Plan de Egreso, Reingreso Hospitalario.

### Coordinación Clínica HD

- **Definición**: lema disuelto en v1.3.0. → ver Seguimiento Clínico, Categorización del Paciente, Gestión de la Continuidad Asistencial.

### Continuidad Asistencial

- **Definición**: obligación transversal del Establecimiento HODOM de garantizar que la atención del paciente se mantenga sin interrupción entre dispositivos asistenciales y en el tiempo, incluyendo coordinación con establecimientos públicos y privados, gestión de personal que asegure cobertura ininterrumpida, y entrega al paciente o representante de indicaciones de cuidados e instrucciones para emergencias. Conforme literatura salubrista (Reid, Haggerty 2002) opera en tres dimensiones: **informacional** (la información clínica fluye entre dispositivos), **relacional** (vínculo terapéutico sostenido en el tiempo) y **de manejo** (coherencia del plan a través de transiciones).
- **Fuente**: DS 1/2022 art. 1 inciso final (acceso, oportunidad, continuidad y calidad); art. 8 letra i; art. 11 letras c y g; art. 22 (documento de indicaciones para emergencias); NT 2024 §Finalidad y obligación transversal.
- **Anclaje técnico**: Reid R, Haggerty J, McKendry R *Defusing the Confusion: Concepts and Measures of Continuity of Healthcare* CHSRF 2002 (definición tres-dimensiones); Starfield B *Primary Care: Balancing Health Needs* 1998; WHO *Integrated People-Centred Health Services* 2016.
- **Distinción**: la **Continuidad Asistencial** es cualidad percibida y obligación normativa transversal; la **Coordinación Interniveles** es acción operativa específica entre niveles diferenciados; el **Continuum Asistencial** es concepto sistémico de diseño de red.
- **Relacionados**: Gestión de la Continuidad Asistencial, Coordinación Interniveles, Continuum Asistencial, Documento de Indicaciones para Emergencias.

### Coordinación Interniveles

- **Definición**: acción operativa específica del Establecimiento HODOM de articulación entre niveles diferenciados del sistema sanitario: Atención Primaria (CESFAM, CECOSF, postas), Atención Cerrada hospitalaria, especialidades ambulatorias, dispositivos sociosanitarios (Chile Cuida, SENAMA), durante y al cierre del Episodio HODOM. **Operacionaliza** la Continuidad Asistencial.
- **Fuente**: no normada con esta denominación; complementa DS 1/2022 art. 8 letras l y n; art. 11 letra g.
- **Anclaje técnico**: WHO *Integrated People-Centred Health Services* 2016; MINSAL *Modelo de Atención Integral de Salud Familiar y Comunitaria* 2013; Reid R et al. CHSRF 2002.
- **Relacionados**: Continuidad Asistencial, Continuum Asistencial, Gestión de la Continuidad Asistencial, Plan de Egreso.

### Continuum Asistencial

- **Definición**: concepto sistémico de diseño de red que describe la **trayectoria completa del paciente** a través de múltiples dispositivos asistenciales —urgencia, Atención Cerrada, HD, APS, especialidades, sociosanitario, cuidados paliativos— como una secuencia continua de cuidados sin discontinuidades funcionales. La HD se posiciona como **nodo del continuum**, no como dispositivo aislado.
- **Fuente**: no normada por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: WHO *Integrated People-Centred Health Services Framework* 2016; Coleman EA *The Care Transitions Intervention* Arch Intern Med 2006;166:1822–8; Naylor MD et al. *Transitional Care of Older Adults Hospitalized with Heart Failure* J Am Geriatr Soc 2004;52:675–84.
- **Relacionados**: Continuidad Asistencial, Coordinación Interniveles, Hospitalización Domiciliaria, Transitional Care (sec. 11).

### Interconsulta

- **Definición**: solicitud formal del Equipo de Salud HD a un especialista o servicio externo para evaluación, opinión diagnóstica o tratamiento específico durante el Episodio HODOM. Se registra en la Ficha Clínica del paciente.
- **Fuente**: NT 2024 §Protocolos clínicos (gestión de recetas, interconsultas y evolución en ficha); práctica clínica.

### Pase de Visita Diario

- **Definición**: reunión clínica diaria del Equipo de Salud HD para revisar el estado de cada paciente activo, reevaluar la Categorización y la Estratificación de Riesgo, ajustar el Plan Terapéutico y de Cuidados y planificar las Visitas Domiciliarias del día.
- **Fuente**: NT 2024 §Protocolos clínicos; práctica operativa.
- **Relacionados**: Visita Domiciliaria, Entrega de Turno, Seguimiento Clínico, Categorización del Paciente, Estratificación de Riesgo.

### Entrega de Turno

- **Definición**: traspaso formal de información clínica y operativa entre turnos del Equipo de Salud HD, que asegura la continuidad del Seguimiento Clínico y la cobertura del sistema 24/7.
- **Fuente**: NT 2024 §Protocolos clínicos; DS 1/2022 art. 11 letra c (gestión del personal garantizando continuidad).
- **Relacionados**: Pase de Visita Diario, Seguimiento Clínico, Registro Evolutivo en Ficha Clínica.

### Atención No Programada

- **Definición**: proceso de detección, triage, respuesta y resolución de eventos clínicos no programados durante el Episodio HODOM —agudización, complicación, deterioro súbito, intercurrencia, llamadas urgentes del paciente o cuidador, alertas de monitoreo remoto. Comprende: (i) **canales de detección** (Sistema de Comunicaciones 24/7, telemetría, contacto del cuidador); (ii) **triage** ejecutado por el Médico Regulador o profesional habilitado (Triage Domiciliario); (iii) **respuesta** (consulta telefónica resolutiva, visita urgente presencial, escalamiento a urgencias, Reingreso Hospitalario); (iv) **Tiempo de Respuesta a Evento No Programado** como indicador de proceso. Coexiste con la Ejecución de Atenciones Profesionales Programadas y con el Seguimiento Clínico.
- **Fuente**: DS 1/2022 art. 8 letra l (coordinación de agudización y reingreso); NT 2024 §Protocolos clínicos (actuación ante emergencias y agresiones al equipo de salud).
- **Refinamiento polymath**: la definición previa fundía detección, triage y respuesta sin separarlos. El glosario v1.4.0 los desagrega y vincula con dos lemas autónomos (Triage Domiciliario, Tiempo de Respuesta a Evento No Programado) que permiten medir y mejorar el proceso.
- **Anclaje técnico**: Australia Victoria Health *Hospital in the Home Guidelines* 2017 (after-hours response standard); NHS Virtual Wards (tiempo de respuesta estándar); Hospital at Home Society *Standards*.
- **Relacionados**: Triage Domiciliario, Tiempo de Respuesta a Evento No Programado, Visita Domiciliaria, Agudización, Complicación durante HD, Sistema de Comunicaciones 24/7, Contacto Asincrónico.

### Atención de Acciones Emergentes o No Planificadas

- **Definición**: lema renombrado en v1.3.0. → ver Atención No Programada.

### Egreso de HD

- **Definición**: proceso de cierre del Episodio HODOM por configuración de alguna de las seis Causales del art. 16: Alta Médica por Recuperación; Alta por Cumplimiento del Plan; Reingreso Hospitalario; Fallecimiento en HD; Renuncia Voluntaria; Alta Disciplinaria. Incluye la **Conciliación de Medicamentos al Egreso** y la emisión del Plan de Egreso y la Epicrisis al Alta.
- **Fuente**: DS 1/2022 art. 16 letras a–f; art. 21 (registros del episodio).
- **Relacionados**: Causales de Egreso, Plan de Egreso, Epicrisis al Alta, Conciliación de Medicamentos, Encuesta de Satisfacción Usuaria al Egreso, Constancia de Acciones en caso de Fallecimiento.

### Tramitación de Egreso de HD

- **Definición**: lema renombrado en v1.3.0. → ver Egreso de HD.

### Alta Médica por Recuperación

- **Definición**: causal (a) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por recuperación del cuadro clínico que motivó la hospitalización. Pertenece a la categoría técnica de **egresos clínicamente exitosos** (ver Causales de Egreso).
- **Fuente**: DS 1/2022 art. 16 letra a.
- **Relacionados**: Egreso de HD, Causales de Egreso, Alta Médica.

### Alta por Cumplimiento del Plan

- **Definición**: causal (b) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por término del cumplimiento del Plan Terapéutico y de Cuidados, aun cuando la patología no se haya resuelto completamente. Pertenece a la categoría técnica de **egresos clínicamente exitosos**.
- **Fuente**: DS 1/2022 art. 16 letra b.
- **Relacionados**: Egreso de HD, Causales de Egreso, Plan Terapéutico y de Cuidados, Plan de Egreso.

### Reingreso Hospitalario

- **Definición**: causal (c) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por traslado del paciente a Atención Cerrada. **Tipología técnica**: (i) **Reingreso Programado** (planificado en el Plan Terapéutico, p.ej. para procedimiento que requiere cama hospitalaria); (ii) **Reingreso No Programado** (por Agudización, Complicación o deterioro súbito), subdividible en **Reingreso Evitable** —atribuible a falla en proceso HD: error diagnóstico, monitoreo insuficiente, escalamiento tardío, conciliación de medicamentos defectuosa— y **Reingreso No Evitable**, propio de la trayectoria natural de la enfermedad. La clasificación por evitabilidad es indicador trazador de calidad del Establecimiento HODOM. **Ventanas temporales habituales**: reingreso a 7, 14 y 30 días, equivalentes a las usadas en hospitalización tradicional. La Dirección Técnica coordina el reingreso (DS 1/2022 art. 8 letras m, n, ñ).
- **Fuente**: DS 1/2022 art. 16 letra c; art. 8 letras m, n y ñ.
- **Refinamiento polymath**: la definición previa enunciaba la causal pero no desagregaba programado/no programado ni evitable/no evitable, distinción central en salubrística internacional de calidad. El glosario v1.4.0 introduce la tipología técnica como base para el indicador Reingreso Evitable (sec. 7).
- **Anclaje técnico**: Halfon P, Eggli Y *Validation of the potentially avoidable hospital readmissions rate* J Clin Epidemiol 2006;59:1017–28; AHRQ *Readmission Reduction Toolkit*; CMS *Hospital Readmissions Reduction Program* (HRRP, 2012–vigente); van Walraven C *LACE Index* CMAJ 2010; Cochrane Review *Discharge planning from hospital* (Gonçalves-Bradley DC 2022).
- **Sinónimos**: Reingreso a Atención Cerrada, Reingreso Hospitalario Programado (denominación anterior, ahora subtipo).
- **Relacionados**: Reingreso Evitable (sec. 7), Acuerdo de Traslado a Atención Cerrada, Médico Tratante de Atención Cerrada, Agudización, Complicación durante HD.

### Reingreso Hospitalario Programado

- **Definición**: lema renombrado en v1.3.0. → ver Reingreso Hospitalario.

### Fallecimiento en HD

- **Definición**: causal (d) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por fallecimiento del paciente durante la HD. Detona el registro obligatorio de Constancia de Acciones en caso de Fallecimiento (art. 21 N° 2). Pertenece a la categoría técnica de **egresos por escalamiento o desenlace clínico**.
- **Fuente**: DS 1/2022 art. 16 letra d; art. 21 N° 2.
- **Relacionados**: Egreso de HD, Causales de Egreso, Constancia de Acciones en caso de Fallecimiento.

### Renuncia Voluntaria

- **Definición**: causal (e) del art. 16 del DS 1/2022. Egreso del Episodio HODOM por decisión voluntaria del paciente, su Tutor Legal o un familiar autorizado de no continuar en la modalidad de HD. Pertenece a la categoría técnica de **egresos por interrupción del cuidado**; amerita análisis cualitativo de causas (barreras sociales, fracaso del modelo, Carga del Cuidador insostenible).
- **Fuente**: DS 1/2022 art. 16 letra e; Ley 20.584.
- **Relacionados**: Egreso de HD, Causales de Egreso, Consentimiento Informado, Carga del Cuidador.

### Alta Disciplinaria

- **Definición**: causal (f) del art. 16 del DS 1/2022, resuelta por la Dirección Técnica al verificarse no adherencia al tratamiento o indicaciones por el tutor o cuidador, conductas irrespetuosas hacia el personal o falta de respuesta o rechazo a las visitas domiciliarias. Su configuración en un episodio previo opera como causal autónoma de **exclusión** para futuros ingresos del mismo paciente. Pertenece a la categoría técnica de **egresos por interrupción del cuidado**.
- **Fuente**: DS 1/2022 art. 16 letra f (causal de egreso); art. 17 letra d (causal de exclusión por antecedente previo); art. 8 letra p (atribución resolutiva de la DT).
- **Relacionados**: Egreso de HD, Causales de Egreso, Exclusiones de Ingreso a HD, Dirección Técnica, Adherencia al Plan.

### Plan de Egreso

- **Definición**: conjunto estructurado de indicaciones, derivaciones, recetas, **Conciliación de Medicamentos al Egreso** y orientaciones que el Equipo de Salud HD entrega al paciente, a su Cuidador y a la red asistencial al término del Episodio HODOM, para asegurar la continuidad del cuidado post-egreso.
- **Fuente**: DS 1/2022 art. 16; art. 21 (registros del episodio); práctica clínica.
- **Anclaje técnico**: Coleman EA *Care Transitions Intervention* 2006; Naylor MD *Transitional Care Model* 2011 (Penn); AHRQ *Re-Engineered Discharge (RED) Toolkit*.
- **Relacionados**: Egreso de HD, Conciliación de Medicamentos, Continuidad Asistencial, Coordinación Interniveles.

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

- **Definición**: documento estructurado e **interdisciplinario** que opera como contrato clínico del Episodio HODOM. Incluye, como mínimo: (i) **objetivos terapéuticos individualizados** y medibles; (ii) **criterios de éxito** que indicarán Alta Médica por Recuperación o Alta por Cumplimiento del Plan; (iii) **criterios anticipados de escalamiento o fracaso terapéutico** que indicarían Reingreso Hospitalario; (iv) **plan farmacológico** con Conciliación de Medicamentos al ingreso y revisión periódica; (v) **plan de cuidados de enfermería** (intervenciones, frecuencia, indicadores); (vi) **plan de rehabilitación** (kinésico, ocupacional, fonoaudiológico según cartera); (vii) **plan de educación** al paciente y cuidador; (viii) **plan de egreso anticipado** con derivaciones previsibles. Se propone con la Solicitud, se ajusta tras la Evaluación Domiciliaria Inicial, se modifica durante el Episodio según el Seguimiento Clínico y el Pase de Visita Diario.
- **Fuente**: DS 1/2022 art. 1 inciso primero (componente estructural de la HD); art. 21 N° 8 (plan de cuidados acorde a necesidades de la persona); art. 13 letra c (gestión del plan por enfermería).
- **Refinamiento polymath**: la norma chilena define el plan como "documento que define indicaciones, frecuencias, cuidados y objetivos" sin desagregar componentes operacionales. El glosario v1.4.0 explicita ocho componentes mínimos, coherentes con la práctica HaH internacional y con el estándar NANDA/NIC/NOC para la dimensión de enfermería.
- **Anclaje técnico**: NANDA International *Nursing Diagnoses: Definitions & Classification* (12 ed, 2024); NIC *Nursing Interventions Classification* (8 ed); NOC *Nursing Outcomes Classification* (7 ed); American Nurses Association *Nursing: Scope and Standards of Practice*; Coleman EA *Care Transitions Intervention* 2006; Naylor MD *Transitional Care Model* 2011; AHRQ *Care Planning Toolkit* 2024.
- **Distinción**: el **Plan Terapéutico y de Cuidados** es el documento integrado e interdisciplinario del paciente bajo HD; el **Plan de Cuidados de Enfermería** es la dimensión específica de enfermería, anidada en el plan integrado.
- **Relacionados**: Plan de Cuidados de Enfermería, Conciliación de Medicamentos, Plan de Egreso, Categorización del Paciente.

### Plan de Cuidados de Enfermería

- **Definición**: registro específico de la dimensión enfermería del Plan Terapéutico y de Cuidados, que detalla las intervenciones de cuidado a ejecutar por el Enfermero o Enfermera Clínica durante el Episodio HODOM, preferentemente estructuradas en taxonomía NANDA/NIC/NOC cuando la institución la haya adoptado.
- **Fuente**: DS 1/2022 art. 13 letra c; art. 21 N° 8.
- **Anclaje técnico**: NANDA-I, NIC, NOC (taxonomías de enfermería).
- **Distinción**: ver "Plan Terapéutico y de Cuidados".

### Consentimiento Informado

- **Definición**: documento firmado por el paciente, su Tutor Legal o un familiar autorizado, que acredita la aceptación voluntaria de la modalidad HD y la recepción de la Carta de Derechos y Deberes. Requisito de ingreso y registro formal obligatorio.
- **Fuente**: DS 1/2022 art. 15 letra d; art. 21 N° 4; Ley 20.584; NT 2024 §Registros obligatorios.
- **Anclaje técnico**: Beauchamp TL, Childress JF *Principles of Biomedical Ethics* (8 ed); JCI International Patient Safety Goals; Norma Técnica N° 154/2013 MINSAL §Consentimiento Informado; AMM *Declaración de Helsinki* (revisión 2024).
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

- **Definición**: prescripción farmacológica emitida por el Médico de Atención Directa o el Médico Regulador en el contexto de un Episodio HODOM, conforme a la normativa general de recetas, al Código Sanitario y a los protocolos institucionales del Establecimiento HODOM. Su emisión inicial está precedida por la Conciliación de Medicamentos al ingreso.
- **Fuente**: DS 1/2022 art. 21; NT 2024 §Protocolos clínicos (gestión de recetas); normativa general de prescripción.
- **Relacionados**: Conciliación de Medicamentos, Polifarmacia.

### Registro Evolutivo en Ficha Clínica

- **Definición**: registro longitudinal en la Ficha Clínica donde el Equipo de Salud HD consigna observaciones, resultados, indicaciones, llamadas, videollamadas, Contactos Asincrónicos, eventos relevantes y alertas durante el Episodio HODOM. Reemplaza la denominación previa de "Reporte de Información Clínico-Asistencial Relevante".
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
- **Relacionados**: Egreso de HD, Plan de Egreso, Conciliación de Medicamentos.

### Encuesta de Satisfacción Usuaria al Egreso

- **Definición**: registro obligatorio aplicado al paciente o a su familiar al Egreso del Episodio HODOM para evaluar la experiencia con la modalidad HD.
- **Fuente**: DS 1/2022 art. 21 N° 3.
- **Anclaje técnico**: PREMs (Patient-Reported Experience Measures) — OECD *PaRIS Initiative* 2024; HCAHPS adaptado a HaH (CAHPS Home Health Care); SERVQUAL aplicado a salud; Norma Técnica N° 154/2013 MINSAL.

### Constancia de Acciones en caso de Fallecimiento

- **Definición**: registro obligatorio que documenta las acciones realizadas por el Equipo de Salud HD cuando la causal de Egreso es el Fallecimiento en HD del paciente.
- **Fuente**: DS 1/2022 art. 21 N° 2.

### Ficha Clínica

- **Definición**: registro clínico del paciente en soporte físico o electrónico, que cumple las exigencias del Reglamento sobre Fichas Clínicas y almacena la información clínica producida durante el Episodio HODOM.
- **Fuente**: DS 41/2012; DS 1/2022 art. 21; Ley 19.628 (datos sensibles); NT 2024 §Registros obligatorios (Ficha Clínica).
- **Anclaje técnico**: HL7 FHIR R4/R5 (estándar de interoperabilidad clínica); estándares ISO/HL7 27931 (CDA); SNOMED CT (terminología clínica internacional); CIE-10/11 (codificación diagnóstica); MINSAL Norma Técnica CoreCL-FHIR Chile 2024.

### Sistema de Registro Clínico y Administrativo

- **Definición**: soporte institucional del registro clínico y administrativo del Establecimiento HODOM, materializado como ficha manual, sistema electrónico, archivos o protocolos de trazabilidad. Atraviesa todos los procesos asistenciales.
- **Fuente**: DS 1/2022 art. 21 (registros formales); art. 23 (confidencialidad y reserva).
- **Anclaje técnico**: ver Ficha Clínica.
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
- **Anclaje técnico**: AAMI *Recommended Practices for Medical Equipment Maintenance* (TIR50); ISO 13485 (sistemas de gestión de calidad para dispositivos médicos); JCI Standards FMS (Facility Management and Safety).
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
- **Anclaje técnico**: ATA *Telehealth Practice Guidelines* 2023; NHS Virtual Wards Operational Framework; ISO/IEC 27001 (seguridad de la información en comunicaciones clínicas); Manual de Alta Complejidad HODOM (KB local) — banda ancha y conectividad redundante.

### Respaldo Eléctrico

- **Definición**: respaldo de energía eléctrica del Establecimiento HODOM autorizado por la Superintendencia de Electricidad y Combustibles (SEC). Exigencia reglamentaria que **no se sustituye** por un plan de contingencia operacional, el cual opera como complemento.
- **Fuente**: DS 1/2022 art. 19 letra b; NT 2024 §Infraestructura mínima; Acto Exento N° 31/2024 §Criterio de armonización (no sustitución por plan de contingencia).

### Plan de Contingencia Operacional

- **Definición**: plan exigido para asegurar la continuidad eléctrica y de comunicaciones del Establecimiento HODOM ante eventos disruptivos; complemento del Respaldo Eléctrico autorizado por la SEC, no sustituto de él.
- **Fuente**: NT 2024 §Infraestructura mínima (plan de contingencia operacional para continuidad eléctrica y de comunicaciones); Acto Exento N° 31/2024 §Criterio de armonización.

### Conocimiento Normativo y Técnico

- **Definición**: corpus institucionalizado de manuales, protocolos, planes de capacitación y normativa absorbida localmente por el Establecimiento HODOM; instrumento transversal de los procesos asistenciales, aprobado y mantenido actualizado por la Dirección Técnica.
- **Fuente**: DS 1/2022 art. 8 letra b (aprobación y actualización de manuales y procedimientos); NT 2024 §Protocolos y manuales obligatorios.

---

## 7. Indicadores operativos y de desempeño HODOM

*Sección nueva en v1.4.0. Vocabulario controlado de los indicadores con los que se mide la producción, el uso de capacidad y el desempeño del Establecimiento HODOM. Todos los lemas de esta sección carecen de anclaje normativo chileno explícito y se sustentan en autoridad técnica internacional o en práctica chilena consolidada (FONASA, MINSAL, GRD).*

### Día-Cama HODOM

- **Definición**: unidad operativa de producción del Establecimiento HODOM equivalente al **día-cama hospitalario** del sistema de atención cerrada. Suma de pacientes-día activos en HD en un período dado (mes, año). Es la base de cálculo de Índice Ocupacional HODOM, Estancia Media HODOM y de la codificación GRD HD cuando aplica. En el sistema chileno se codifica como código FONASA 0201408 "Día Cama de Hospitalización Domiciliaria de Baja Complejidad" y derivados.
- **Fuente**: no normada por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: MINSAL Norma de Codificación GRD; FONASA Catálogo de Prestaciones (código 0201408 y derivados); MINSAL Norma Técnica N° 238/2024; OECD *Health Care Quality Indicators framework* 2023.
- **Relacionados**: Episodio HODOM, Índice Ocupacional HODOM, Estancia Media HODOM, Cartera de Prestaciones HODOM.

### Índice Ocupacional HODOM

- **Definición**: indicador de uso de capacidad del Establecimiento HODOM: cociente entre Días-Cama HODOM efectivamente ocupados y Días-Cama HODOM disponibles en el período, expresado como porcentaje. Análogo al índice ocupacional hospitalario. **Interpretación operativa**: a diferencia del hospital tradicional donde >85% es alerta de saturación, en HD el rango operativo seguro depende del modelo organizacional y del sistema de respuesta 24/7; la literatura HaH madura tolera ocupaciones >90% sostenidas si el sistema está bien dimensionado.
- **Fuente**: no normada.
- **Anclaje técnico**: KB local *Indicadores HODOM HSC* (serie 14 meses, promedio 89.8%); MINSAL serie histórica HODOM nacional; OECD HCQ Indicators.
- **Relacionados**: Día-Cama HODOM, Capacidad Operacional HODOM.

### Estancia Media HODOM

- **Definición**: indicador clínico-operativo del Establecimiento HODOM: promedio de Días-Cama HODOM por episodio cerrado en el período. Equivale al ALOS (Average Length of Stay) hospitalario. Se reporta total y desagregada por categoría diagnóstica (CIE-10) y por modalidad (HD Médico, Quirúrgico, Paliativo, etc.). **Su prolongación sostenida con caída del Índice Ocupacional es indicio de barreras al egreso, no de subutilización**.
- **Fuente**: no normada.
- **Anclaje técnico**: KB local *Indicadores HODOM HSC* (PDE 7.4 → 10.8 días, hallazgo de estancamiento por prolongación); OECD HCQ Indicators; AHRQ ALOS measures.
- **Sinónimos**: PDE (Promedio de Días-cama por Egreso), ALOS HODOM.
- **Relacionados**: Día-Cama HODOM, Índice Ocupacional HODOM, Egreso de HD.

### Densidad de Visita

- **Definición**: número promedio de Visitas Domiciliarias por paciente-día en el Episodio HODOM, desagregable por profesión (médica, enfermería, kinésica, otra) y por modalidad (presencial / virtual). Indicador de carga asistencial y de intensidad del cuidado. Determinado por la Categorización del Paciente.
- **Fuente**: no normada.
- **Anclaje técnico**: NHS Virtual Wards Operational Metrics; Australia HITH KPIs; Hospital at Home Society *Operational Metrics*.
- **Relacionados**: Visita Domiciliaria, Categorización del Paciente, Plan Terapéutico y de Cuidados.

### Carga Asistencial Domiciliaria

- **Definición**: volumen agregado de actividad clínica del Equipo de Salud HD en un período: suma ponderada de Visitas Domiciliarias, Contactos Asincrónicos, Atenciones No Programadas y Pase de Visita Diario. Indicador de planificación de dotación y predictor de burnout del equipo.
- **Fuente**: no normada.
- **Anclaje técnico**: NHS Workforce Standards Virtual Wards; Maslach Burnout Inventory en HaH (literatura emergente); Manual de Alta Complejidad HODOM (KB local).
- **Relacionados**: Equipo de Salud HD, Densidad de Visita, Contacto Asincrónico.

### Tiempo de Respuesta a Evento No Programado

- **Definición**: indicador de proceso del Establecimiento HODOM: tiempo transcurrido entre la detección de un evento clínico no programado (llamada, alerta, contacto del cuidador) y la primera respuesta efectiva del Equipo de Salud HD (consulta telefónica resolutiva, llegada de visita urgente, escalamiento). Umbrales operativos internacionales: respuesta telefónica en minutos, visita urgente en horas (típicamente <2h en HaH avanzado; <4h aceptable). Indicador trazador de calidad.
- **Fuente**: no normada.
- **Anclaje técnico**: NHS Virtual Wards Framework; Australia Victoria HITH Guidelines (response standards); Hospital at Home Society *Quality Standards*.
- **Relacionados**: Atención No Programada, Triage Domiciliario, Sistema de Comunicaciones 24/7.

### Reingreso Evitable

- **Definición**: Reingreso Hospitalario durante el Episodio HODOM **atribuible total o parcialmente a falla del proceso HD**: error diagnóstico, monitoreo insuficiente, escalamiento tardío, plan terapéutico subóptimo, Conciliación de Medicamentos defectuosa, educación insuficiente al cuidador. Subtipo de Reingreso No Programado. Su porcentaje sobre el total de reingresos es indicador trazador de calidad y se identifica mediante revisión retrospectiva estructurada (p.ej. algoritmo Halfon-Eggli).
- **Fuente**: no normada.
- **Anclaje técnico**: Halfon P, Eggli Y *Validation of the potentially avoidable hospital readmissions rate* J Clin Epidemiol 2006;59:1017–28; AHRQ *Readmission Reduction Toolkit*; CMS *Hospital Readmissions Reduction Program*; van Walraven C *LACE Index*.
- **Relacionados**: Reingreso Hospitalario, Conciliación de Medicamentos, Estratificación de Riesgo, Evento Adverso en HD.

### Marco Donabedian aplicado a HODOM

- **Definición**: trío clásico de indicadores de calidad aplicado al Establecimiento HODOM conforme el marco Donabedian (1966):
  - **Indicadores de Estructura**: dotación, infraestructura, equipamiento (cumplimiento del art. 19 DS 1/2022, dotación mínima art. 13).
  - **Indicadores de Proceso**: Tiempo de Respuesta a Evento No Programado, Densidad de Visita, Conciliación de Medicamentos completada, adherencia a protocolos, tasa de cumplimiento del Pase de Visita Diario.
  - **Indicadores de Resultado**: tasa de Reingreso Hospitalario (a 7, 14, 30 días), tasa de Reingreso Evitable, tasa de Eventos Adversos en HD, mortalidad en HD, tasa de Renuncia Voluntaria, satisfacción usuaria al egreso, equivalencia funcional al alta (Barthel, FIM).
- **Fuente**: no normada.
- **Anclaje técnico**: Donabedian A *Evaluating the Quality of Medical Care* Milbank Mem Fund Q 1966;44:166–206; Donabedian A *An Introduction to Quality Assurance in Health Care* 2003; OECD *Health Care Quality Indicators*; AHRQ National Quality Forum.
- **Relacionados**: Encuesta de Satisfacción Usuaria al Egreso, Tiempo de Respuesta a Evento No Programado, Reingreso Evitable, Evento Adverso en HD.

---

## 8. Procedimientos y exigencias normativas

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

- **Definición**: seis causales taxativas enumeradas en el art. 16 letras a–f del DS 1/2022, **agrupables en tres categorías técnicas** para análisis de outcomes:
  - **(I) Egresos clínicamente exitosos**: (a) Alta Médica por Recuperación; (b) Alta por Cumplimiento del Plan.
  - **(II) Egresos por escalamiento o desenlace clínico**: (c) Reingreso Hospitalario; (d) Fallecimiento en HD.
  - **(III) Egresos por interrupción del cuidado**: (e) Renuncia Voluntaria; (f) Alta Disciplinaria.

  El indicador *Proporción de egresos exitosos sobre total de egresos* es trazador internacional de desempeño HaH; los egresos de categoría III ameritan análisis cualitativo de causas (barreras sociales, fracaso del modelo, conflicto, Carga del Cuidador insostenible).
- **Fuente**: DS 1/2022 art. 16 letras a–f.
- **Refinamiento polymath**: la enumeración normativa es taxativa pero el agrupamiento es heterogéneo (mezcla egresos positivos, escalamientos clínicos, muerte, decisión del paciente, sanción institucional). El glosario v1.4.0 introduce las tres categorías técnicas para análisis de outcomes, sin alterar la enumeración legal.
- **Anclaje técnico**: Hospital at Home Society *Quality Standards* 2024; Australia Victoria Health *HITH Performance Indicators*; AHRQ *Quality Indicators for Hospital at Home*.

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
- **Anclaje técnico**: OMS *Guidelines on Core Components of Infection Prevention and Control Programmes* 2016; CDC *Healthcare Infection Control Practices Advisory Committee* (HICPAC) Guidelines; JCI International Patient Safety Goals (Goal 5: Reduce Risk of Health Care Associated Infections); APIC *Text of Infection Control and Epidemiology* (5 ed).
- **Notas**: en HD el perfil IAAS es distinto al hospitalario (CLABSI domiciliaria por catéter venoso central, CAUTI domiciliaria por catéter urinario, infección de sitio operatorio en herida quirúrgica seguida en domicilio); la normativa chilena no diferencia perfiles. El glosario v1.4.0 los reconoce para fines de vigilancia interna.

### REAS (Reglamento de Manejo de Residuos de Establecimientos de Atención de Salud)

- **Definición**: reglamento sobre manejo de residuos especiales aplicable al Establecimiento HODOM, que debe contar con protocolo ajustado para retiro y eliminación.
- **Fuente**: DS 6/2009 MINSAL; DS 1/2022 art. 5 letra p; NT 2024 §Protocolos y manuales obligatorios (Manejo de residuos).

### RCP Básica (Reanimación Cardiopulmonar Básica)

- **Definición**: capacitación en soporte vital básico de 3 horas conforme al Decreto Exento N° 52/2022. Constituye exigencia **acumulativa** —no sustitutiva— del curso IAAS de 80 horas y del uso certificado de desfibrilador para el personal clínico que realiza atención directa.
- **Fuente**: Decreto Exento N° 52/2022 MINSAL; DS 1/2022 art. 13 letras c, d, e; NT 2024 §Requisitos resumidos por cargo, §Inducción y certificación y §Criterio armonizado sobre Coordinación.
- **Anclaje técnico**: AHA *Guidelines for CPR and ECC* (actualización vigente); ILCOR *Consensus on Science with Treatment Recommendations* (CoSTR) — actualización 2025; ERC *European Resuscitation Council Guidelines*.

### Soporte Vital Básico

- **Definición**: capacitación obligatoria del personal profesional y técnico que ejecuta atención clínica directa, materializada en el curso de RCP Básica vigente.
- **Fuente**: NT 2024 §Inducción y certificación; DS 1/2022 art. 13 letras c, d, e.
- **Anclaje técnico**: AHA/ILCOR/ERC (ver RCP Básica).
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
- **Relacionados**: Modalidades de HD por Línea Clínica.

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

## 9. Calidad, seguridad y resultados

*Sección nueva en v1.4.0. Recoge el vocabulario de seguridad del paciente aplicado a HD, distinguiendo conceptos que la norma chilena confunde en el genérico "complicación". Las distinciones siguen el Marco Conceptual de la Clasificación Internacional para la Seguridad del Paciente (OMS CISP 2009).*

### Evento Adverso en HD

- **Definición**: daño no intencional al paciente **causado por la atención de salud** durante el Episodio HODOM, no atribuible a la evolución natural de la enfermedad. Incluye caídas con lesión durante o por intervención del equipo, errores de medicamentos con daño efectivo, infecciones asociadas a dispositivos en mantención domiciliaria (CLABSI, CAUTI), lesiones por presión adquiridas durante HD, lesiones por procedimientos. Constituye **evento de notificación al sistema de calidad y seguridad institucional** conforme Norma Técnica N° 154/2013 MINSAL.
- **Fuente**: no normada con esta denominación específica por DS 1/2022 ni NT 2024; obligación implícita por Norma Técnica N° 154/2013 MINSAL.
- **Anclaje técnico**: OMS *Marco Conceptual de la Clasificación Internacional para la Seguridad del Paciente* (CISP) 2009; IOM *To Err is Human* 1999; AHRQ Patient Safety Network 2024; Norma Técnica N° 154/2013 MINSAL.
- **Distinción**: el **Evento Adverso** es daño causado por la atención; la **Complicación durante HD** es desfavorable pero causado por la enfermedad o tratamiento indicado; el **Incidente** es suceso que pudo o no causar daño; el **Casi-Evento** es incidente interceptado antes del daño.
- **Relacionados**: Complicación durante HD, Incidente en HD, Casi-Evento (Near Miss) en HD, IAAS, Conciliación de Medicamentos.

### Incidente en HD

- **Definición**: suceso durante el Episodio HODOM que pudo o no causar daño al paciente, no esperable conforme al estándar de cuidado, que se reporta al sistema institucional de gestión de riesgos aun cuando no haya producido daño efectivo (p.ej. preparación de medicamento equivocado interceptada antes de la administración; caída sin lesión; pérdida transitoria de comunicaciones con paciente crítico).
- **Fuente**: no normada con esta denominación por DS 1/2022 ni NT 2024.
- **Anclaje técnico**: OMS CISP 2009; AHRQ Patient Safety Network; Norma Técnica N° 154/2013 MINSAL.
- **Distinción**: el **Incidente** puede haber producido o no daño; el **Evento Adverso** produjo daño efectivo; el **Casi-Evento** es incidente sin daño porque fue interceptado.
- **Relacionados**: Evento Adverso en HD, Casi-Evento (Near Miss) en HD.

### Casi-Evento (Near Miss) en HD

- **Definición**: incidente durante el Episodio HODOM que estuvo a punto de causar daño al paciente y fue **interceptado** por un mecanismo de barrera (revisión por par, alerta tecnológica, observación del cuidador, doble chequeo de medicamento). Su notificación es fuente primaria de aprendizaje organizacional y mejora del proceso, dado que ocurre en mayor frecuencia que los eventos adversos consumados y revela vulnerabilidades del sistema.
- **Fuente**: no normada.
- **Anclaje técnico**: OMS CISP 2009; Reason J *Human Error* 1990 y *Managing the Risks of Organizational Accidents* 1997 (modelo de queso suizo); Norma Técnica N° 154/2013 MINSAL.
- **Distinción**: subtipo específico de Incidente en HD, caracterizado por la intercepción exitosa.
- **Relacionados**: Incidente en HD, Evento Adverso en HD.

### Notificación de Eventos Centinelas

- **Definición**: obligación institucional del Establecimiento HODOM de reportar al sistema de calidad y seguridad los eventos centinelas (subconjunto de Eventos Adversos de gravedad mayor: muerte inesperada, daño permanente, evento que requiera intervención inmediata para preservar la vida) ocurridos durante el Episodio HODOM, conforme Norma Técnica N° 154/2013 MINSAL.
- **Fuente**: Norma Técnica N° 154/2013 MINSAL.
- **Anclaje técnico**: JCI *Sentinel Event Policy and Procedures*; OMS CISP.
- **Relacionados**: Evento Adverso en HD, Fallecimiento en HD, Reingreso Evitable.

---

## 10. Normativa cruzada citada

*Esta sección lista las fuentes externas citadas a lo largo del glosario, en prosa libre (excepción al esquema). Desde v1.4.0 incorpora también autoridades técnicas internacionales que sustentan los campos `Anclaje técnico:`.*

### 10.1 Normativa chilena

#### DS 1/2022 MINSAL — Reglamento HODOM

Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria. Fuente primaria del corpus. Anclaje: `urn:salud:kb:hodom-reglamento-ds1-2022`.

#### Acto Exento N° 31/2024 MINSAL

Acto administrativo del Ministerio de Salud que aprueba la Norma Técnica HODOM, suscrito el 05-jun-2024 por la Ministra Ximena Aguilera Sanhueza. Anclaje: `urn:salud:kb:hodom-decreto-exento-31-2024`.

#### NT 2024 — Norma Técnica HODOM

Norma Técnica para Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria, texto anexo de 16 páginas al Acto Exento N° 31/2024. Anclaje: `urn:salud:kb:hodom-norma-tecnica-2024`.

#### Norma Técnica N° 243/2025 MINSAL

Norma Técnica para la implementación de la Hospitalización Domiciliaria como proceso transversal en la red asistencial pública (adultos, pediatría, GO, salud mental, paliativos).

#### Norma Técnica N° 238/2024 MINSAL

Norma técnica sectorial relativa a niveles de complejidad de la HD y codificación FONASA asociada (código 0201408 baja complejidad y derivados).

#### Ley 20.584

Ley sobre derechos y deberes de las personas en relación con acciones vinculadas a su atención en salud (2012). Sustento del Consentimiento Informado, la Carta de Derechos y Deberes y la calificación de la información clínica como dato sensible (art. 12).

#### Ley 19.628

Ley sobre protección de la vida privada y de los datos de carácter personal (1999). Aplica al tratamiento de información clínica como dato sensible.

#### Ley 20.575

Ley que establece el principio de finalidad en el tratamiento de datos personales (2012). Refuerza la Ley 19.628.

#### DS 41/2012 MINSAL — Reglamento sobre Fichas Clínicas

Reglamento que regula el manejo de fichas clínicas; aplicable a la Ficha Clínica del Establecimiento HODOM.

#### DS 594/2000 MINSAL

Reglamento sobre condiciones sanitarias y ambientales básicas en lugares de trabajo. Aplicable a las dependencias administrativas del Establecimiento HODOM.

#### DS 6/2009 MINSAL — Reglamento REAS

Reglamento sobre manejo de residuos de establecimientos de atención de salud.

#### Res. Ex. N° 60/2022 MINSAL — Norma Técnica IAAS

Norma Técnica sobre Programa Nacional de Prevención y Control de IAAS.

#### Decreto Exento N° 52/2022 MINSAL — Norma Técnica RCP y Desfibriladores

Norma técnica de contenidos para capacitación en reanimación cardiopulmonar básica y uso de desfibriladores.

#### Res. Exenta N° 875/2013 MINSAL — Norma Técnica N° 154

Norma Técnica N° 154 sobre Programa Nacional de Calidad y Seguridad de la Atención en Salud. Sustento del sistema de notificación de Eventos Adversos, Incidentes y Casi-Eventos.

#### DS 90/2017 MINSAL — Certificación de Auxiliares

Reglamento sobre certificación de auxiliares de la salud por la SEREMI. Aplica a auxiliares paramédicos de enfermería del Equipo de Salud HD.

#### DS 725/1968 — Código Sanitario

Código Sanitario; su Libro X regula las sanciones por contravenciones de los Establecimientos HODOM.

#### DFL N° 1/2005 MINSAL

DFL que fija el texto refundido, coordinado y sistematizado del DL N° 2.763/1979 y de las Leyes N° 18.933 y N° 18.469. Sustento jurídico del Acto Exento N° 31/2024.

#### Ley 19.880

Ley de Bases de los Procedimientos Administrativos. Sustento jurídico del Acto Exento N° 31/2024.

#### Ley 16.744

Ley sobre accidentes del trabajo y enfermedades profesionales. Sus organismos administradores pueden suscribir convenios con prestadores HODOM.

#### Decreto N° 136/2004 MINSAL

Reglamento Orgánico del Ministerio de Salud.

#### Decreto N° 140/2004 MINSAL

Reglamento Orgánico de los Servicios de Salud.

#### DS N° 28/2009 MINSAL

Reglamento que delega en la Ministra de Salud la facultad de suscribir, bajo la fórmula "Por orden del Presidente de la República", los decretos que aprueban normas técnicas.

#### Resolución N° 7/2019 (Contraloría)

Resolución de la Contraloría General de la República invocada como fundamento jurídico del Acto Exento N° 31/2024.

#### Res. Ex. N° 328/2023 (Subsecretaría de Salud Pública)

Resolución que creó el grupo de trabajo encargado de elaborar la propuesta de Norma Técnica HODOM 2024.

#### SEC — Superintendencia de Electricidad y Combustibles

Organismo que autoriza el respaldo eléctrico del Establecimiento HODOM.

#### Superintendencia de Salud

Organismo que mantiene el Registro de Prestador Individual del personal de salud habilitado.

#### ISAPRE — Institución de Salud Previsional

Entidad con la que el Prestador HODOM puede suscribir Convenios con Terceros para asegurar continuidad de la atención en domicilio según el seguro de salud del paciente.

#### FONASA — Fondo Nacional de Salud

Asegurador público chileno; mantiene el catálogo de prestaciones con códigos específicos para HD de baja complejidad (0201408) y derivados.

#### SENAMA — Servicio Nacional del Adulto Mayor

Servicio público chileno con programas de Cuidados Domiciliarios y soporte al cuidador, complementarios al sistema HODOM.

#### Chile Cuida

Programa intersectorial del Sistema de Protección Social (Subsecretaría de Servicios Sociales) que provee cuidadores formales y apoyo a personas en situación de dependencia.

### 10.2 Estándares y guías internacionales (autoridades técnicas)

#### Hospital at Home Society (USA)

Sociedad estadounidense que mantiene los *Standards for Hospital at Home Programs* (2024), referente operativo internacional. Citada en lemas: Hospitalización Domiciliaria, Visita Domiciliaria, Categorización del Paciente, Cribado de Idoneidad, Tiempo de Respuesta a Evento No Programado, Marco Donabedian.

#### NHS England

*Virtual Wards Operational Framework* (2022); modelo de referencia tecnológicamente intensivo de HaH. Citada en lemas: Visita Domiciliaria, Contacto Asincrónico, HD Admisión-Evitada, Triage Domiciliario.

#### Victoria Department of Health (Australia)

*Hospital in the Home Guidelines* (2017); referente operativo internacional consolidado. Citada en lemas: Hospital in the Home (sec. 11), Atención No Programada, Tiempo de Respuesta a Evento No Programado.

#### Cochrane Collaboration

Revisiones sistemáticas sobre HaH: Shepperd S et al. *Admission avoidance hospital at home* (2016, CD007491); Shepperd S et al. *Early discharge hospital at home* (2017, CD000356); Gonçalves-Bradley DC et al. *Discharge planning from hospital* (2022).

#### CMS (Centers for Medicare & Medicaid Services, USA)

*Acute Hospital Care at Home Waiver* (2020–vigente); *Hospital Readmissions Reduction Program* (HRRP, 2012–vigente). Marco de codificación y reembolso de referencia.

#### OMS (Organización Mundial de la Salud)

Múltiples documentos citados: *Marco Conceptual de la Clasificación Internacional para la Seguridad del Paciente* (CISP, 2009); *High 5s Action on Patient Safety — Medication Reconciliation* (2014); *Consolidated telemedicine implementation guide* (2022); *Social Determinants of Health Framework* (2010); *Long-Term Care for Older People* (2017); *Adherence to Long-Term Therapies* (2003); *Medication Without Harm — Polypharmacy* (2019); *Integrated People-Centred Health Services* (2016); *Guidelines on Core Components of Infection Prevention and Control Programmes* (2016).

#### AHRQ (Agency for Healthcare Research and Quality, USA)

Patient Safety Network; *Care Coordination Quality Measures*; *Readmission Reduction Toolkit*; *Re-Engineered Discharge (RED) Toolkit*; *Care Planning Toolkit*.

#### CDC (Centers for Disease Control and Prevention, USA)

*Healthcare Infection Control Practices Advisory Committee* (HICPAC) Guidelines.

#### JCI (Joint Commission International)

*International Patient Safety Goals*; *Sentinel Event Policy and Procedures*; *Standards FMS* (Facility Management and Safety).

#### IHI (Institute for Healthcare Improvement)

*5 Million Lives Campaign*; *How-to Guide: Prevent Adverse Drug Events Medication Reconciliation* (2011).

#### IOM / National Academy of Medicine (USA)

*To Err is Human: Building a Safer Health System* (1999); *Crossing the Quality Chasm* (2001).

#### OECD

*Health Care Quality Indicators framework* (2023); *PaRIS Initiative* (Patient-Reported Indicator Surveys, 2024).

#### ATA (American Telemedicine Association)

*Telehealth Practice Guidelines* (2023).

#### ILCOR / AHA / ERC

ILCOR *Consensus on Science with Treatment Recommendations* (CoSTR); AHA *Guidelines for CPR and ECC*; ERC *European Resuscitation Council Guidelines*. Autoridades técnicas en RCP / Soporte Vital Básico.

#### NANDA-I, NIC, NOC

NANDA International *Nursing Diagnoses* (12 ed, 2024); *Nursing Interventions Classification* (8 ed); *Nursing Outcomes Classification* (7 ed). Taxonomía estándar internacional de cuidados de enfermería.

#### HL7 / SNOMED CT / CIE-10/11

Estándares de interoperabilidad clínica (HL7 FHIR R4/R5; CDA), terminología clínica (SNOMED CT) y codificación diagnóstica (CIE-10/11).

#### Instrumentos clínicos validados citados

Charlson Comorbidity Index (Charlson ME 1987); CIRS-G (Miller MD 1992); NEWS2 (Royal College of Physicians UK 2017); LACE Index (van Walraven C 2010); HOSPITAL Score (Donzé J 2013); Escala de Sobrecarga del Cuidador de Zarit (Zarit SH 1980); Caregiver Strain Index (Robinson BC 1983); Beers Criteria (AGS 2023); STOPP/START (O'Mahony 2015); GOLD Report; ESC HF Guidelines; Halfon-Eggli avoidability algorithm (2006).

---

## 11. Anexo terminológico internacional

*Sección nueva en v1.4.0. Define términos del paraguas internacional Hospital at Home y modalidades adyacentes que el lector salubrista necesita conocer para ubicar HODOM en el mapa global. Las entradas de esta sección son **informativas, no prescriptivas para el modelo chileno**: usan el campo `Estatus:` en lugar de `Fuente:` para distinguir su rol.*

### Hospital at Home (HaH)

- **Definición**: término paraguas internacional para modalidades asistenciales que sustituyen o continúan la hospitalización tradicional trasladando intensidad clínica al domicilio. Comprende variantes como Admission-Avoidance HaH, Early-Supported-Discharge HaH, Inpatient-at-Home, Virtual Wards, Hospital in the Home (HITH). **El modelo chileno HODOM (DS 1/2022) es una variante específica dentro de este paraguas**, no su sinónimo estricto.
- **Estatus**: género internacional del cual HODOM es especie.
- **Anclaje técnico**: Hospital at Home Society (USA); Cochrane Reviews (Shepperd 2016, 2017); Levine DM 2020; Leff B 2005.
- **Relacionados**: Hospitalización Domiciliaria (cuerpo principal), HD Admisión-Evitada, HD Alta-Temprana Asistida.

### Virtual Ward (Sala Virtual)

- **Definición**: modalidad del NHS inglés (Virtual Wards Operational Framework 2022) que extiende la sala hospitalaria al domicilio con monitorización remota digital intensiva, equipos multidisciplinarios y respuesta 24/7. Más densa tecnológicamente que el modelo HODOM chileno; incorpora telemetría, IoT médico y dashboards de seguimiento poblacional.
- **Estatus**: variante anglosajona contemporánea; no equivale estrictamente a HODOM chileno pero es referente para evolución tecnológica.
- **Anclaje técnico**: NHS England *Virtual Wards Operational Framework* 2022.

### Hospital in the Home (HITH)

- **Definición**: modalidad australiana, especialmente desarrollada en el estado de Victoria, donde todos los hospitales metropolitanos y regionales operan programas HITH que gestionan aproximadamente 6% de los días-cama estatales. Modelo de referencia operativa internacional, basado en evidencia robusta de equivalencia de outcomes.
- **Estatus**: referente operativo internacional consolidado.
- **Anclaje técnico**: Victoria Department of Health *HITH Guidelines* (2017); Caplan GA *Hospital in the Home — Then and Now* MJA 2020.

### Inpatient-at-Home

- **Definición**: variante emergente del HaH que evita incluso el paso por urgencias, con triaje directo desde atención primaria o comunidad. Forma más radical del Admission-Avoidance.
- **Estatus**: subtipo emergente, no formalmente desarrollado en Chile.
- **Anclaje técnico**: Manual de Alta Complejidad HODOM (KB local); Levine DM 2020.

### Subacute Care / SNF-ST (Skilled Nursing Facility — Short Term)

- **Definición**: modalidad post-aguda institucional norteamericana **distinta** de HaH: cuidado en facility de enfermería especializada de corta estancia (LOS promedio 27 días) tras hospitalización aguda; no es atención en domicilio sino en una facility intermedia. **No aplica al modelo chileno**: Chile no tiene SNF estructurados; el espacio post-agudo lo cubren parcialmente HODOM, APS y cuidados domiciliarios sociales (Chile Cuida, SENAMA). Se define para evitar confusión semántica.
- **Estatus**: fuera de alcance del modelo chileno; informativo.
- **Anclaje técnico**: CMS SNF coverage; KB local *Transiciones y prevención de readmisiones*; *Post-Acute and Long-Term Care Medicine* (3 ed).

### LTACH (Long-Term Acute Care Hospital)

- **Definición**: modalidad hospitalaria norteamericana para pacientes con necesidades médicas complejas prolongadas (ventilación mecánica prolongada, manejo complejo de heridas, multiorgánicos crónicos). LOS promedio 26 días, costo promedio USD 38.500 por paciente. **No existe equivalente en Chile**; se define para evitar confusión con HD compleja prolongada.
- **Estatus**: fuera de alcance del modelo chileno; informativo.
- **Anclaje técnico**: CMS LTACH classification.

### IRF (Inpatient Rehabilitation Facility)

- **Definición**: modalidad post-aguda norteamericana de rehabilitación intensiva intrahospitalaria, ≥3 horas diarias de terapia ≥5 días/semana, equipo interdisciplinario. **No existe formalmente como categoría en Chile**; el equivalente parcial son unidades de rehabilitación de hospitales y los servicios kinésicos. Distinto de HD rehabilitadora.
- **Estatus**: fuera de alcance del modelo chileno; informativo.
- **Anclaje técnico**: CMS IRF requirements.

### Transitional Care

- **Definición**: concepto desarrollado por Mary Naylor (Penn): modelo de cuidado coordinado por enfermería de práctica avanzada (APN) que acompaña al paciente de alto riesgo a través de la transición hospital → hogar durante 30–90 días post-alta. **No es HaH** pero es complementario y comparte el énfasis en continuidad. Componentes: visita domiciliaria post-alta dentro de 24h, conciliación de medicamentos, plan de acompañamiento, comunicación con APS.
- **Estatus**: marco conceptual aplicable al Plan de Egreso de HD; no es modalidad HaH per se.
- **Anclaje técnico**: Naylor MD et al. *Transitional Care of Older Adults* JAGS 2004; Penn Transitional Care Model Resource Center; Coleman EA *Care Transitions Intervention* 2006.

### Step-Down Unit

- **Definición**: unidad hospitalaria de cuidados intermedios, entre UCI y sala convencional, para pacientes que ya no requieren UCI pero necesitan monitorización más intensiva que sala. **No equivale a HD**; es paso intermedio dentro del hospital físico. El concepto **step-down** sí se aplica análogamente a HD para describir Transferencia desde mayor intensidad (ver Step-Up vs Step-Down en sec. 4).
- **Estatus**: concepto hospitalario; el término 'step-down' tiene uso análogo en HaH para describir flujos de Transferencia.
- **Anclaje técnico**: terminología estándar de cuidados intensivos; Manual de Alta Complejidad HODOM (KB local).

### Rapid Response Team (Equipo de Respuesta Rápida)

- **Definición**: en el contexto hospitalario, equipo multidisciplinario que responde a deterioros clínicos detectados en sala general antes de que requieran UCI. **Análogo conceptual en HaH**: el equipo de respuesta del Sistema 24/7 ante Atención No Programada. El modelo chileno no formaliza este rol como entidad separada; la función la ejerce el Médico Regulador con el resto del Equipo de Salud HD según corresponda.
- **Estatus**: concepto hospitalario con aplicación análoga en HaH; informativo.
- **Anclaje técnico**: IHI *5 Million Lives Campaign — RRT*; DeVita MA *Rapid Response Teams* 2006.

### OPAT (Outpatient Parenteral Antimicrobial Therapy)

- **Definición**: terapia antimicrobiana parenteral administrada en régimen ambulatorio (domicilio, clínica infusional, hospital de día), sin requerir hospitalización. **En Chile, una prestación tipo OPAT puede ejecutarse dentro de HODOM** como parte de la Cesta de Prestaciones Complejas (Alta Complejidad HODOM) o como atención ambulatoria diferenciada. Distinguible de HD: OPAT es modalidad específica de antibioticoterapia; HD es modalidad asistencial completa.
- **Estatus**: concepto operativo del que HD puede incluir variantes.
- **Anclaje técnico**: IDSA *Practice Guidelines for OPAT* 2018; Tice AD *OPAT Outcomes*.
- **Relacionados**: Cesta de Prestaciones Complejas (Alta Complejidad HODOM).

---

