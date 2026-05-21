---
_manifest:
  urn: urn:salud:kb:hodom-glosario-terminologico
  provenance:
    created_by: Claude Code (Opus 4.7, 1M context) con Felix Sanhueza Luna
    created_at: '2026-05-14'
    updated_at: '2026-05-14'
    sources:
      - urn:salud:kb:hodom-reglamento-ds1-2022
      - urn:salud:kb:hodom-decreto-exento-31-2024
      - urn:salud:kb:hodom-norma-tecnica-2024
version: 1.0.1
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
    - urn:salud:kb:salubrista
---

# Glosario Terminológico de Hospitalización Domiciliaria (HODOM)

Vocabulario controlado del dominio HODOM derivado exhaustivamente de las tres fuentes normativas vigentes:

- **DS 1/2022** — Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria (25 artículos).
- **Acto Exento N° 31/2024** del 05-jun-2024 — Aprueba la Norma Técnica HODOM (Ministra Ximena Aguilera Sanhueza).
- **NT 2024** — Norma Técnica para Establecimientos que Otorgan Prestaciones de HD (16 páginas anexas al Acto Exento).

Cada entrada incluye: definición canónica, anclaje normativo exacto, uso en el modelo OPM HODOM v1.1 (cuando aplica), sinónimos y términos relacionados. Las entradas con `[modelo OPM v1.1]` están materializadas como cosa/proceso/estado/instrumento/agente en `~/projects/hd-hsc-os/docs/models/opm-hodom-bundle-v1.1.json`.

Criterio de armonización: si dos fuentes tensionan, prevalece **DS 1/2022 > NT 2024 > Acto Exento 31/2024**. Este criterio es editorial del corpus/glosario; no se atribuye como sección literal del acto administrativo.

Nota de auditoría 2026-05-14: se corrigen anclajes normativos inequívocos del DS 1/2022 detectados en revisión semántica y lógica: roles clínicos en art. 12 numerales 1–6; personal administrativo/auxiliar y otros profesionales en art. 13; dependencias en art. 19; registros en art. 21; documento de indicaciones en art. 22; confidencialidad en art. 23; fiscalización/sanción en art. 24; vigencia/transitorio en art. 25. También se normaliza la denominación “Acto Exento N° 31/2024” y se evita atribuir al acto una sección literal inexistente de “criterio de armonización”.


---

## 1. Sistema y Unidades

### Establecimiento que Otorga Prestaciones de Hospitalización Domiciliaria
- **Definición**: establecimiento de salud de atención cerrada (público o privado), prestador en convenio, o unidad/servicio interno que otorga prestaciones de hospitalización domiciliaria.
- **Anclaje**: DS 1/2022 art. 1.
- **Uso OPM v1.1**: cosa física sistémica `e-establecimiento`. Sistema exhibidor del proceso central. Frontera del modelo.
- **Sinónimos**: Establecimiento HODOM (forma breve).
- **Relacionados**: Unidad o Servicio de HD, Servicio de Atención Cerrada, SEREMI (autorizador).

### Unidad o Servicio de Hospitalización Domiciliaria
- **Definición**: parte operativa del Establecimiento que organiza los habilitadores del proceso de HD (equipo de salud, dirección técnica, conocimiento, registros, capacidad operacional). En la NT 2024 §Ámbito se la nombra como "servicio o unidad de hospitalización domiciliaria".
- **Anclaje**: DS 1/2022 art. 1; NT 2024 §Ámbito de Aplicación.
- **Uso OPM v1.1**: cosa física sistémica `e-unidad-hd`. Parte interna del Establecimiento (RF1).
- **Sinónimos**: Unidad HD, Servicio de HD, UHD.
- **Relacionados**: Equipo de Salud HD, Dirección Técnica HD.

### Servicio o Unidad de Atención Cerrada del Establecimiento
- **Definición**: parte del Establecimiento que provee la hospitalización tradicional (cama hospitalaria) desde la cual se origina la transferencia a HD y hacia la cual se reingresa en caso de inestabilidad.
- **Anclaje**: DS 1/2022 art. 1 + art. 16 letra c (reingreso hospitalario programado).
- **Uso OPM v1.1**: cosa física sistémica `e-atencion-cerrada`. Es origen y destino del Paciente (SE1 etiquetado).
- **Sinónimos**: Atención Cerrada, AC, Servicio Hospitalario.
- **Relacionados**: Equipo del Servicio de Atención Cerrada, Médico Tratante de AC.

### SEREMI
- **Definición**: Secretaría Regional Ministerial de Salud correspondiente al domicilio de las dependencias administrativas del Establecimiento HODOM. Autoridad sanitaria que otorga, fiscaliza y sanciona la autorización sanitaria.
- **Anclaje**: DS 1/2022 arts. 4-6 (autorización), art. 24 (fiscalización), Libro X del Código Sanitario (sanción).
- **Uso OPM v1.1**: no modelado en SD raíz; reservado para OPD paralelo de Cumplimiento Normativo (pendiente).
- **Sinónimos**: Autoridad Sanitaria Regional, Seremi de Salud.
- **Relacionados**: Autorización Sanitaria, Fiscalización, Libro X Código Sanitario.

### Servicios de Salud
- **Definición**: red asistencial pública del país a la cual debe remitirse un ejemplar del acto administrativo de aprobación de la Norma Técnica HODOM.
- **Anclaje**: Acto Exento 31/2024 (distribución operativa).
- **Uso OPM v1.1**: no modelado.
- **Sinónimos**: SS.
- **Relacionados**: Servicio de Salud Ñuble (referencia HSC).

### División de Gestión de la Red Asistencial
- **Definición**: división de la Subsecretaría de Redes Asistenciales del MINSAL encargada de publicar la Norma Técnica HODOM aprobada.
- **Anclaje**: Acto Exento 31/2024 (publicación ordenada).
- **Sinónimos**: DIGERA.

### Equipo de Gestión de Camas
- **Definición**: equipo institucional que coordina el traslado coordinado del paciente desde Atención Cerrada al domicilio. No definido directamente en la normativa nacional; presente en realidad operativa de hospitales como HSC.
- **Anclaje**: realidad operativa Hospital de San Carlos; complementa DS 1/2022 art. 1 (modalidades de traslado).
- **Uso OPM v1.1**: cosa física sistémica `e-equipo-gestion-camas`. Co-agente del subproceso #3 Realización de Transferencia a HD.
- **Sinónimos**: GC, Gestión de Camas.
- **Relacionados**: Realización de Transferencia a HD, Equipo del Servicio de AC.

---

## 2. Roles Profesionales (cargos del Equipo de Salud HD)

### Dirección Técnica
- **Definición**: cargo obligatorio del Establecimiento HODOM. Médico cirujano con jornada mínima 22 horas semanales, con formación de postítulo o postgrado en gestión en salud y curso de IAAS de 80 horas. Responsable de organización, funcionamiento y representación del establecimiento ante autoridades.
- **Anclaje**: DS 1/2022 arts. 7-10; NT 2024 §Habilitación del personal.
- **Uso OPM v1.1**: cosa física sistémica `e-direccion-tecnica`. Parte interna de la Unidad HD.
- **Sinónimos**: DT, Director Técnico, Directora Técnica.
- **Funciones (DS 1/2022 art. 8)**: representar al establecimiento, aprobar manuales, velar por IAAS, mantener stock, coordinar reingreso hospitalario, cautelar registros, alta disciplinaria del art. 16 letra f.
- **Relacionados**: Manual de Organización Interna, Plan de Capacitación Anual (PAC).

### Coordinación
- **Definición**: cargo institucional ejercido por un profesional de la salud (preferentemente enfermera/o) con 5 años de experiencia clínica, formación en gestión y curso de IAAS de al menos 80 horas (vigencia 5 años).
- **Anclaje**: DS 1/2022 art. 11; NT 2024 §Habilitación.
- **Uso OPM v1.1**: indirectamente representado por `e-enfermera-coordinadora` cuando la coordinación es ejercida por enfermería.
- **Funciones**: supervisar actualización de manuales, supervisar procesos clínicos, gestionar personal, supervisar calidad de cuidados, gestionar insumos.
- **Relacionados**: Enfermera Coordinadora de HD.

### Médico Cirujano de Atención Directa
- **Definición**: médico cirujano del Equipo de Salud HD con experiencia mínima 2 años en patologías médico-quirúrgicas. Supervisa actividades asistenciales en domicilio, participa en evaluación de ingreso/egreso, evalúa e indica tratamiento, puede usar TICs para diagnóstico/tratamiento/prevención/rehabilitación.
- **Anclaje**: DS 1/2022 art. 12 Nº 1; NT 2024 §Requisitos por cargo.
- **Uso OPM v1.1**: cosa física sistémica `e-medico-aten-directa` (agregada en Unfold #1 SD-Eq-Salud-HD).
- **Sinónimos**: M.AD, Médico AD, Médico de HD.

### Médico Cirujano Regulador
- **Definición**: médico cirujano del Equipo de Salud HD con experiencia mínima 2 años en regulación médica. Atención a distancia o atención directa durante HD. Puede ser la misma persona que cumple Atención Directa (DS 1/2022 art. 12 Nº 2).
- **Anclaje**: DS 1/2022 art. 12 Nº 2; NT 2024 §Requisitos por cargo; criterio de armonización normativa de este glosario (los 2 años son en regulación médica, no se sustituyen por experiencia médico-quirúrgica general).
- **Uso OPM v1.1**: cosa física sistémica `e-medico-regulador`. Co-agente de subprocesos #2 Evaluación de Solicitud, #6 Coordinación Clínica HD, y 2.2/2.3 del SD-1.2.
- **Sinónimos**: M.Reg, Médico Regulador.
- **Relacionados**: Médico de Atención Directa.

### Enfermero(a) Clínico
- **Definición**: enfermero/a del Equipo de Salud HD con experiencia mínima 2 años + curso vigente de soporte vital básico. Ejecuta plan de cuidados de enfermería y plan terapéutico según complejidad. Educa a paciente, familia y/o cuidadores. Evalúa pacientes durante visita.
- **Anclaje**: DS 1/2022 art. 12 Nº 3; NT 2024 §Requisitos por cargo.
- **Uso OPM v1.1**: cosa física sistémica `e-enfermero-clinico` (agregada en Unfold #1).
- **Sinónimos**: Enfermera Clínica, Enf.Clínica.
- **Relacionados**: Plan de Cuidados de Enfermería.

### Enfermera Coordinadora de HD
- **Definición**: rol coordinador del establecimiento ejercido por enfermería (DS 1/2022 art. 11). En el modelo HODOM v1.1 es el rol que en SD-1.2 absorbe las dimensiones de evaluación territorial, red de apoyo, voluntariedad inicial y logística (supuesto declarado S-v1.2-1).
- **Anclaje**: DS 1/2022 art. 11; supuesto S-v1.2-1 del modelo.
- **Uso OPM v1.1**: cosa física sistémica `e-enfermera-coordinadora`. Co-agente de #2 Evaluación de Solicitud, #6 Coordinación Clínica HD, y 2.1/2.2/2.3 del SD-1.2.
- **Sinónimos**: Enf.Coord HD, Coordinadora de HD.
- **Relacionados**: Coordinación (rol institucional genérico), Enfermero Clínico (función asistencial distinta).

### Kinesiólogo(a)
- **Definición**: kinesiólogo/a del Equipo de Salud HD con experiencia mínima 2 años + soporte vital básico. Otorga terapias motoras y respiratorias en domicilio.
- **Anclaje**: DS 1/2022 art. 12 Nº 4.
- **Uso OPM v1.1**: cosa física sistémica `e-kinesiologo` (agregada en Unfold #1).
- **Sinónimos**: Kinesiólogo HD, Kine.

### Técnico de Enfermería
- **Definición**: auxiliar paramédico, técnico de nivel medio o técnico de nivel superior de enfermería. Experiencia mínima 1 año + soporte vital básico. Cumple plan de cuidados y plan terapéutico bajo competencia definida por enfermería clínica. Auxiliares requieren certificación SEREMI según DS 90/2017.
- **Anclaje**: DS 1/2022 art. 12 Nº 5; NT 2024 §Habilitación; DS 90/2017 (auxiliares).
- **Uso OPM v1.1**: cosa física sistémica `e-tecnico-enfermeria` (agregada en Unfold #1).
- **Sinónimos**: TENS, Auxiliar Paramédico, Técnico Paramédico.

### Trabajador(a) Social
- **Definición**: profesional del Equipo de Salud HD que elabora informe de diagnóstico social del hogar (vivienda, servicios sanitarios básicos, telefonía, accesos viales), verifica disponibilidad de cuidador o tutor legal, evalúa situación económica del grupo familiar, confecciona informe social y participa en reuniones del equipo clínico.
- **Anclaje**: DS 1/2022 art. 12 Nº 6.
- **Uso OPM v1.1**: NO modelado por decisión declarada del operador (supuesto S-v1.2-1). En el modelo, sus funciones de evaluación social-domiciliaria son absorbidas por la Enfermera Coordinadora de HD. Reintroducible por especialización si la operación lo exige.
- **Sinónimos**: T.Social, Asistente Social.

### Fonoaudiólogo
- **Definición**: profesional adicional del Equipo de Salud HD según la cartera de prestaciones ofrecidas por el establecimiento. DS 1/2022 art. 14 admite "otros profesionales y técnicos según prestaciones brindadas al paciente y su familia".
- **Anclaje**: DS 1/2022 art. 14; decisión del operador 2026-05-14.
- **Uso OPM v1.1**: cosa física sistémica `e-fonoaudiologo` (agregada en Unfold #1 por decisión del operador).
- **Sinónimos**: Fono.

### Profesional de Salud de HD (abstracción)
- **Definición**: rol genérico que abstrae a cualquier profesional del Equipo de Salud HD que ejecuta la Evaluación Domiciliaria Inicial con multiplicidad 1..N (varios profesionales asincrónicos).
- **Anclaje**: derivado de DS 1/2022 art. 12 + arts. 13-14.
- **Uso OPM v1.1**: cosa física sistémica `e-profesional-hd`. Agente del subproceso #4 Evaluación Domiciliaria Inicial con multiplicidad 1..N (cosa-coend de la auditoría categorial).
- **Sinónimos**: Prof.HD.
- **Relacionados**: Médico de Atención Directa, Enfermero Clínico, Kinesiólogo, etc.

### Médico Tratante de Atención Cerrada
- **Definición**: médico del Servicio de Atención Cerrada del Establecimiento que origina la solicitud de transferencia a HD. Comunicación activa con la Dirección Técnica HD para coordinación de agudización y reingreso.
- **Anclaje**: DS 1/2022 art. 8 letra n (función de DT: coordinar con médicos tratantes); realidad operativa HSC.
- **Uso OPM v1.1**: cosa física sistémica `e-medico-tratante`. Agente único de #1 Elaboración de Solicitud de Transferencia a HD. Parte del Equipo del Servicio de Atención Cerrada.
- **Sinónimos**: M.Tratante AC.

### Personal Administrativo y Auxiliar
- **Definición**: personal no clínico del Establecimiento que cumple actividades establecidas por la Dirección Técnica.
- **Anclaje**: DS 1/2022 art. 14.
- **Uso OPM v1.1**: no modelado individualmente (queda en abstracción del Establecimiento).

---

## 3. Pacientes y Estados Clínicos

### Paciente
- **Definición operativa**: persona destinataria del proceso HODOM. Distintos tipos según situación clínica.
- **Anclaje**: DS 1/2022 art. 15 (requisitos de ingreso); NT 2024 §Definiciones.
- **Uso OPM v1.1**: cosa física ambiental `e-paciente` (con nombre largo "Paciente Hospitalizado Clínicamente Estable") como transformee primario.

### Paciente Hospitalizado Clínicamente Estable
- **Definición**: abstracción del modelo OPM HODOM v1.1 que agrupa los dos tipos normativos (paciente agudo y paciente crónico reagudizado) por compartir la transformación nuclear de la hospitalización domiciliaria. Supuesto declarado F6.
- **Anclaje**: derivada de NT 2024 §Definiciones + decisión del modelo v1.1.
- **Uso OPM v1.1**: cosa física ambiental `e-paciente`. 3 estados lineales E1→E2→E3.
- **Especializable**: por subtipos `paciente-agudo` y `paciente-cronico-reagudizado` si la operación lo exige.

### Paciente Agudo
- **Definición**: persona sin patología previa y con cuadro clínico agudo que requiere hospitalización para recuperar salud.
- **Anclaje**: NT 2024 §Definiciones.
- **Uso OPM v1.1**: no modelado por separado; absorbido en F6 (Paciente Hospitalizado Clínicamente Estable).

### Paciente Crónico Reagudizado
- **Definición**: persona con patología previa y cuadro clínico agudo, asociado o no a esa patología de base, que requiere hospitalización para recuperar salud.
- **Anclaje**: NT 2024 §Definiciones.
- **Uso OPM v1.1**: no modelado por separado (F6).

### Condición Clínica Estable
- **Definición**: equilibrio de funciones vitales que permite el traslado del paciente al domicilio pese a patología no resuelta o parcialmente solucionada. Requisito de ingreso a HD.
- **Anclaje**: NT 2024 §Definiciones; DS 1/2022 art. 15 letra a.
- **Uso OPM v1.1**: implícito en la designación del transformee como "Clínicamente Estable".

### Red de Apoyo Familiar, Social o Tutor Responsable
- **Definición**: red personal del paciente a cargo del cuidado en domicilio, requisito de ingreso a HD.
- **Anclaje**: DS 1/2022 art. 15 letra c.
- **Uso OPM v1.1**: cosa física ambiental `e-red-apoyo`. En SD-0 es instrumento (H2); en SD-1 #3 cambia rol procedural a co-agente (Δ-J).
- **Sinónimos**: Red de Apoyo, Cuidador, Tutor.

### Cuidador / Tutor Legal
- **Definición**: persona responsable del cuidado directo del paciente en domicilio. La Trabajadora Social verifica su disponibilidad.
- **Anclaje**: DS 1/2022 art. 12 Nº 6 (verificación por T.Social); art. 15 letra c.
- **Uso OPM v1.1**: implícito en `e-red-apoyo`.

### Domicilio del Paciente
- **Definición**: residencia del paciente que cumple condiciones sanitarias mínimas, servicios básicos y telefonía, dentro del radio de cobertura del Establecimiento. Requisito de ingreso.
- **Anclaje**: DS 1/2022 art. 15 letra b.
- **Uso OPM v1.1**: cosa física ambiental `e-domicilio`. Habilitador ambiental (H2 + D3) en SD-0 (subido en v1, Δ3). En SD-1.2 exhibe Coordenadas del Domicilio (RF2).

### Estado `en atención cerrada transferible a HD` [estado del Paciente]
- **Definición**: estado inicial del Paciente cuando está hospitalizado en Atención Cerrada y cumple los requisitos de ingreso para transferirse a HD.
- **Anclaje**: derivado de DS 1/2022 art. 15.
- **Uso OPM v1.1**: estado `s-paciente-en-cerrada-1` (inicial).

### Estado `hospitalizado en domicilio` [estado del Paciente]
- **Definición**: estado intermedio del Paciente durante la HD (entre transferencia exitosa y egreso).
- **Anclaje**: derivado de DS 1/2022 art. 1.
- **Uso OPM v1.1**: estado `s-paciente-en-domicilio-2`.

### Estado `egresado` [estado del Paciente]
- **Definición**: estado final del Paciente al término de la hospitalización domiciliaria por cualquiera de las 6 causales del art. 16.
- **Anclaje**: DS 1/2022 art. 16.
- **Uso OPM v1.1**: estado `s-paciente-egresado-3` (final).

---

## 4. Procesos Asistenciales

### Hospitalización Domiciliaria
- **Definición**: modalidad asistencial alternativa a la hospitalización tradicional en atención cerrada, para personas con patología aguda o crónica reagudizada; entrega cuidados similares a los de establecimientos hospitalarios, en calidad y cantidad, sin los cuales habría sido necesaria la permanencia en atención cerrada. Requisitos estructurales: indicación médica, control médico, plan terapéutico del equipo de salud, término por egreso.
- **Anclaje**: DS 1/2022 art. 1; NT 2024 §Definiciones.
- **Uso OPM v1.1**: proceso central `p-hd` exhibido por el Establecimiento. Sistema → Sub-procesos del SD-1.
- **Sinónimos**: HD, HDOM, Hospitalización en Domicilio.
- **Relacionados**: Atención Cerrada (alternativa), Atención Domiciliaria (distinta, ambulatoria).

### Atención Domiciliaria
- **Definición**: acciones de salud realizadas en domicilio por prestadores en modalidad ambulatoria y de libre elección. **NO ES** Hospitalización Domiciliaria.
- **Anclaje**: NT 2024 §Definiciones; DS 1/2022 art. 3 (exclusión expresa).
- **Uso OPM v1.1**: fuera de frontera.

### Atención Profesional
- **Definición operativa**: cada acción asistencial individual del Equipo de Salud HD durante una visita al domicilio (atención del Médico AD, kinesiterapia, curación, administración de medicamentos, educación al paciente, etc.).
- **Anclaje**: derivado del proceso #5 Ejecución de Atenciones Profesionales Programadas (DS 1/2022 art. 12).
- **Uso OPM v1.1**: a refinarse en SD-1.3 (pendiente).

### Elaboración de Solicitud de Transferencia a HD
- **Definición operativa**: subproceso #1 del SD-1. Acción del Médico Tratante de AC que genera la Solicitud de Transferencia a HD en estado `creada` usando el Formulario de HD como instrumento.
- **Anclaje**: derivado del modelo OPM HODOM v1.1.
- **Uso OPM v1.1**: proceso `p-elaboracion-solicitud`.

### Evaluación de Solicitud de Transferencia a HD
- **Definición operativa**: subproceso #2 del SD-1. Cambia la Solicitud `creada → respondida`. Refinable en SD-1.2 con 3 sub-procesos (Recepción, Verificación de Criterios, Resolución).
- **Anclaje**: derivado de la práctica HSC + DS 1/2022 art. 12 Nº 6 (participación en evaluación de pacientes hospitalizados).
- **Uso OPM v1.1**: proceso `p-evaluacion-solicitud` con refinamiento descomposición → opd-sd1-2.

### Realización de Transferencia a HD
- **Definición operativa**: subproceso #3 del SD-1. Cambia el Paciente `en cerrada → en domicilio`. Bifurcación operativa entre traslado por medios propios de la Red de Apoyo XOR traslado coordinado por Equipo de Gestión de Camas.
- **Anclaje**: DS 1/2022 art. 1 (término técnico "transferencia").
- **Uso OPM v1.1**: proceso `p-transferencia` (nombre canónico §1.1 OPL-ES: "Realización de Transferencia" termina en -ción).

### Otorgamiento de Consentimiento Informado
- **Definición operativa**: subproceso a refinarse en SD-Transferencia. Acción que cambia el Consentimiento Informado de `pendiente` a `otorgado` y consume/usa la Carta de Derechos y Deberes.
- **Anclaje**: DS 1/2022 art. 15 letra d; F1 v0 ratificado en handoff v1.1.
- **Uso OPM v1.1**: pendiente (compromiso F1).

### Evaluación Domiciliaria Inicial
- **Definición operativa**: subproceso #4 del SD-1. Múltiples evaluaciones profesionales asincrónicas (1..N profesionales) al inicio del episodio HD, cuyas conclusiones se integran para cambiar el Plan Terapéutico y de Cuidados de `pre-HD` a `HD`.
- **Anclaje**: derivado de prácticas de NT 2024 §Protocolos clínicos.
- **Uso OPM v1.1**: proceso `p-evaluacion-domiciliaria`.

### Ejecución de Atenciones Profesionales Programadas
- **Definición operativa**: subproceso #5 del SD-1. Bloque concurrente con #6 y #7. Loop operativo (programar, preparar, realizar, registrar) de las atenciones planificadas en el Plan.
- **Anclaje**: derivado del modelo operativo HODOM.
- **Uso OPM v1.1**: proceso `p-ejecucion-atenciones`. A refinarse en SD-1.3 (pendiente).

### Coordinación Clínica HD
- **Definición operativa**: subproceso #6 del SD-1. Bloque concurrente con #5 y #7. Funciones absorbidas v1: Seguimiento Clínico + Categorización Clínica-Operativa + Gestión de Continuidad Asistencial (Δ-A, Δ-C, Δ-D del v1). Afecta el Plan + genera Reporte.
- **Anclaje**: derivado de NT 2024 §Protocolos clínicos.
- **Uso OPM v1.1**: proceso `p-gestion-clinica` (nombre canónico §1.1: "Coordinación" termina en -ción).

### Atención de Acciones Emergentes o No Planificadas
- **Definición operativa**: subproceso #7 del SD-1. Bloque concurrente con #5 y #6. Detección, clasificación y escalamiento de eventos no programados. Segundo productor del Reporte (B5).
- **Anclaje**: derivado de DS 1/2022 art. 8 letra l (coordinar agudización y reingreso); NT 2024 §Protocolos.
- **Uso OPM v1.1**: proceso `p-gestion-emergentes`.

### Tramitación de Egreso de HD
- **Definición operativa**: subproceso #8 del SD-1. Cambia el Paciente `hospitalizado en domicilio → egresado` por una de las 6 causales del DS 1/2022 art. 16. Absorbe la sub-rama de Reingreso Hospitalario Programado (Δ1 del v1).
- **Anclaje**: DS 1/2022 art. 16; término técnico "Egreso".
- **Uso OPM v1.1**: proceso `p-egreso` (nombre canónico §1.1: "Tramitación" termina en -ción). A refinarse en SD-Egreso con 6 causales.

### Recepción de Solicitud de Transferencia
- **Definición operativa**: sub-proceso 2.1 del SD-1.2. Cambia la Solicitud `creada → recibida`. Acción del Enfermera Coordinadora.
- **Uso OPM v1.1**: proceso `p-recepcion-solicitud`.

### Verificación de Criterios de Ingreso a HD
- **Definición operativa**: sub-proceso 2.2 del SD-1.2. Cambia la Solicitud `recibida → evaluada`. Bloque concurrente interno por dimensión: M.Reg (clínica) + Enf.Coord (territorial, red, voluntariedad, logística). Genera las Coordenadas del Domicilio.
- **Anclaje**: DS 1/2022 art. 15 (criterios) + art. 17 (exclusiones).
- **Uso OPM v1.1**: proceso `p-verificacion-criterios`.

### Resolución de Solicitud de Transferencia
- **Definición operativa**: sub-proceso 2.3 del SD-1.2. Cambia la Solicitud `evaluada → respondida` con state-expression nivel 2 en 4 sub-estados (aceptada, rechazado categórico, rechazo condicional, no concluyente).
- **Uso OPM v1.1**: proceso `p-resolucion-solicitud`.

---

## 5. Documentos y Registros

### Solicitud de Transferencia a HD
- **Definición operativa**: documento generado en #1 Elaboración por el Médico Tratante de AC. Es la **instancia documental** concreta con estados (`creada`, `recibida`, `evaluada`, `respondida`). Distinta del Formulario de HD que es la plantilla. Contiene estructuralmente el Plan Terapéutico y de Cuidados (Δ-E).
- **Anclaje**: derivado de DS 1/2022 art. 21 y práctica HSC.
- **Uso OPM v1.1**: cosa informacional sistémica `e-solicitud` con 4 estados nivel 1 + state-expression nivel 2 de `respondida`.
- **Relacionados**: Formulario de HD (plantilla), Plan Terapéutico (parte).

### Formulario de Hospitalización Domiciliaria
- **Definición operativa**: plantilla/schema estable (sin estados) usado como instrumento de #1 Elaboración para generar la Solicitud. Δ-H separa esto del objeto generado.
- **Anclaje**: derivado del modelo operativo + DS 1/2022 art. 21 Nº 6 (Formulario de Ingreso, distinto).
- **Uso OPM v1.1**: cosa informacional sistémica `e-formulario` (sin estados).

### Plan Terapéutico y de Cuidados
- **Definición operativa**: documento que viaja dentro de la Solicitud (RF1 atemporal, Δ-E). Cambia de `pre-HD` a `HD` por #4 Evaluación Domiciliaria Inicial. Afectado por #6 Coordinación Clínica HD.
- **Anclaje**: derivado de DS 1/2022 art. 1 (plan terapéutico del equipo de salud) + art. 21 Nº 8 (plan de cuidados acorde a necesidades).
- **Uso OPM v1.1**: cosa informacional sistémica `e-plan` con 2 estados.

### Plan de Cuidados de Enfermería
- **Definición**: documento específico de la dimensión enfermería ejecutado por el Enfermero(a) Clínico. Listado como registro obligatorio formal del DS 1/2022 art. 21 Nº 8.
- **Anclaje**: DS 1/2022 art. 21 Nº 8; art. 12 Nº 3 (función del Enfermero Clínico).
- **Uso OPM v1.1**: NO modelado todavía como cosa separada. Decisión pendiente: cosa nueva separada vs absorbido en Plan Terapéutico vs renombrar Plan existente (pregunta abierta del Unfold #3).

### Consentimiento Informado
- **Definición**: documento firmado por el paciente, tutor o familiar que acredita aceptación voluntaria de la modalidad HD + entrega de la Carta de Derechos y Deberes. Requisito de ingreso.
- **Anclaje**: DS 1/2022 art. 15 letra d + art. 21 Nº 4; NT 2024 §Registros (acredita entrega de la Carta).
- **Uso OPM v1.1**: NO modelado todavía. Compromiso F1 v0 a rescatar en SD-Transferencia con estados `pendiente` / `otorgado`.
- **Sinónimos**: CI.
- **Relacionados**: Carta de Derechos y Deberes, Otorgamiento de CI, Ley 20.584.

### Carta de Derechos y Deberes
- **Definición**: documento que el establecimiento entrega al paciente o representante. La firma del Consentimiento Informado acredita su entrega.
- **Anclaje**: Ley 20.584 (Derechos y Deberes de las Personas); DS 1/2022 art. 21 Nº 5; NT 2024 §Registros.
- **Uso OPM v1.1**: NO modelado todavía. F1 v0.
- **Sinónimos**: CDD, Carta D y D.

### Formulario de Ingreso
- **Definición**: documento estructurado al ingreso del paciente a HD, distinto del Consentimiento. Recoge datos administrativos y clínicos iniciales.
- **Anclaje**: DS 1/2022 art. 21 Nº 6.
- **Uso OPM v1.1**: NO modelado todavía. Productor candidato: subproceso de admisión dentro de SD-Transferencia.

### Resumen Clínico en Domicilio
- **Definición**: documento físico o digital que permanece en el domicilio del paciente para consulta en emergencias por equipos externos. Contiene diagnósticos, tratamientos y cuidados.
- **Anclaje**: NT 2024 §Registros obligatorios.
- **Uso OPM v1.1**: NO modelado todavía. Productor candidato: Evaluación Domiciliaria Inicial o Coordinación Clínica HD.

## 5.1 Registros clínico-asistenciales

### Reporte de Información Clínico-Asistencial Relevante
- **Definición operativa**: documento generado por #6 Coordinación Clínica HD (resultados, observaciones, llamadas, videollamadas, eventos, alertas) y por #7 Atención de Acciones Emergentes (eventos no planificados). Productor múltiple (B5).
- **Anclaje**: derivado del modelo operativo + NT 2024 §Registros.
- **Uso OPM v1.1**: cosa informacional sistémica `e-reporte-info`. Generado por #6 y #7 (T2 productor múltiple).

### Reporte de Atención Profesional
- **Definición**: reporte producido por el profesional luego de cada atención individual (cubre el registro obligatorio del DS 1/2022 art. 21 Nº 7: "descripción del proceso asistencial con todas las atenciones").
- **Anclaje**: DS 1/2022 art. 21 Nº 7.
- **Uso OPM v1.1**: NO modelado individualmente; queda dentro del Reporte de Información o de la Ficha Clínica.

### Curso Clínico-Asistencial
- **Definición**: registro/síntesis de la dinámica evolutiva del paciente durante el episodio HD.
- **Anclaje**: derivado de la práctica clínica.
- **Uso OPM v1.1**: NO modelado en v1 (Δ-B eliminó esta cosa del v0).

### Epicrisis al Alta
- **Definición**: registro de cierre del episodio asistencial. Productor: Tramitación de Egreso de HD.
- **Anclaje**: DS 1/2022 art. 21 Nº 9; F4 v0.
- **Uso OPM v1.1**: NO modelado todavía. Compromiso F4 v0 a rescatar en SD-Egreso.

### Encuesta de Satisfacción Usuaria al Egreso
- **Definición**: registro obligatorio aplicado al egreso del paciente.
- **Anclaje**: DS 1/2022 art. 21 Nº 3; F4 v0.
- **Uso OPM v1.1**: NO modelado. F4.

### Constancia de Acciones en caso de Fallecimiento
- **Definición**: registro obligatorio cuando la causal de egreso es fallecimiento del paciente.
- **Anclaje**: DS 1/2022 art. 21 Nº 2; F4 v0.
- **Uso OPM v1.1**: NO modelado. F4.

### Ficha Clínica
- **Definición**: registro clínico (físico o electrónico) que cumple el DS 41/2012 sobre Fichas Clínicas. Almacenamiento de información clínica del paciente.
- **Anclaje**: DS 41/2012; DS 1/2022 art. 21; NT 2024 §Registros.
- **Uso OPM v1.1**: representada por la cosa más general `e-sistema-registro` (Sistema de Registro Clínico y Administrativo).

### Sistema de Registro Clínico y Administrativo
- **Definición operativa**: soporte/instrumento institucional del registro clínico. Puede ser ficha papel, sistema electrónico, archivos y protocolos de trazabilidad.
- **Anclaje**: DS 1/2022 art. 21.
- **Uso OPM v1.1**: cosa informacional sistémica `e-sistema-registro`. Instrumento transversal de todos los procesos.
- **Sinónimos**: SRCA, Sistema de Registro.

### Registro del Episodio de HD
- **Definición**: agregación documental del episodio HD. Contiene todos los registros formales obligatorios.
- **Anclaje**: DS 1/2022 art. 21.
- **Uso OPM v1.1**: cosa pendiente (compromiso F4 v0). A modelarse en Unfold #3 SD-Registro-Episodio-HD.

## 5.2 Manuales, protocolos y capacitación

### Manual de Organización Interna
- **Definición**: documento aprobado por la Dirección Técnica con organigrama, roles, horarios y reglamento de higiene.
- **Anclaje**: NT 2024 §Protocolos y manuales obligatorios.
- **Uso OPM v1.1**: parte de `e-conocimiento` (Conocimiento Normativo y Técnico).

### Protocolos Clínicos
- **Definición**: documentos aprobados por DT con protocolos para evaluación e ingreso, programación de rutas, categorización y egreso, gestión de recetas, actuación ante emergencias.
- **Anclaje**: NT 2024 §Protocolos clínicos obligatorios.
- **Uso OPM v1.1**: parte de `e-conocimiento`.

### Manual de Procedimientos
- **Definición**: documento con procedimientos técnicos específicos (manejo de vías venosas, catéteres urinarios, traqueostomías, toma de muestras, precauciones de aislamiento).
- **Anclaje**: NT 2024 §Protocolos.
- **Uso OPM v1.1**: parte de `e-conocimiento`.

### Plan de Capacitación Anual (PAC)
- **Definición**: plan obligatorio que cubre IAAS, RCP básica, inducción y cursos de humanización del cuidado.
- **Anclaje**: NT 2024 §Plan de Capacitación Anual.
- **Uso OPM v1.1**: parte de `e-conocimiento`.
- **Sinónimos**: PAC.

### Reglamento Interno de Orden, Higiene y Seguridad
- **Definición**: reglamento institucional exigido en la solicitud de autorización sanitaria.
- **Anclaje**: DS 1/2022 art. 5 (antecedentes para autorización).
- **Uso OPM v1.1**: parte de `e-conocimiento`.

---

## 6. Capacidad Operativa

### Capacidad Operacional Disponible
- **Definición operativa**: recursos materiales del Establecimiento (vehículos, equipamiento, insumos, medicamentos, comunicaciones 24/7, respaldo eléctrico) que habilitan el proceso HODOM. Supuesto S3: producto heterogéneo dominado por factor material.
- **Anclaje**: DS 1/2022 art. 19 + NT 2024 §Equipamiento.
- **Uso OPM v1.1**: cosa física sistémica `e-capacidad-operacional` con estados `suficiente`/`insuficiente`. Desplegable en Unfold #2 SD-Cap-Op-HD.
- **Sinónimos**: Cap.Op.

### Infraestructura
- **Definición**: dependencias administrativas y operativas del Establecimiento (área administrativa, bodegas con control de temperatura, recinto de aseo, zona transitoria de residuos, estacionamiento, sector seguro para fichas).
- **Anclaje**: DS 1/2022 art. 19 letras a-k; NT 2024 §Infraestructura mínima.
- **Uso OPM v1.1**: cosa física sistémica `e-infraestructura` (Unfold #2). Incluye respaldo eléctrico SEC autorizado.

### Vehículos de Transporte
- **Definición**: vehículos para traslado del equipo de salud y de pacientes. Servicio propio o tercero en convenio.
- **Anclaje**: NT 2024 §Equipamiento; DS 1/2022 art. 19 letra i (estacionamiento).
- **Uso OPM v1.1**: cosa física sistémica `e-vehiculos-transporte` (Unfold #2).

### Equipamiento Médico
- **Definición**: equipos mínimos obligatorios para monitorización de signos vitales (presión arterial, frecuencia cardíaca/respiratoria, saturación de oxígeno) + instrumentos según cartera.
- **Anclaje**: NT 2024 §Equipamiento.
- **Uso OPM v1.1**: cosa física sistémica `e-equipamiento-medico` (Unfold #2).
- **Sinónimos**: Dispositivos de uso médico.

### Dispositivos de Uso Médico
- **Definición**: instrumento, aparato, implemento, máquina, equipo, artefacto, implante u otro artículo similar que cumple normativa vigente. Sinónimo operativo de Equipamiento Médico.
- **Anclaje**: NT 2024 §Definiciones.

### Insumos Clínicos
- **Definición**: material clínico fungible para procedimientos. Almacenamiento en bodega con control de temperatura.
- **Anclaje**: DS 1/2022 art. 19; NT 2024 §Equipamiento.
- **Uso OPM v1.1**: cosa física sistémica `e-insumos-clinicos` (Unfold #2).

### Medicamentos
- **Definición**: stock farmacológico del Establecimiento. Farmacia o botiquín autorizado, o convenios que aseguren abastecimiento y cadena de frío en domicilio.
- **Anclaje**: NT 2024 §Equipamiento; DS 1/2022 art. 19 (botiquín autorizado).
- **Uso OPM v1.1**: cosa física sistémica `e-medicamentos` (Unfold #2).

### Sistema de Comunicaciones 24/7
- **Definición**: sistema telefónico o radial 24/7 con grabación o registro manual de llamadas. Soporte informático e internet permanente.
- **Anclaje**: DS 1/2022 art. 19; NT 2024 §Infraestructura mínima.
- **Uso OPM v1.1**: cosa física sistémica `e-comunicaciones-24-7` (Unfold #2).

### Respaldo Eléctrico
- **Definición**: respaldo de energía eléctrica autorizado por la Superintendencia de Electricidad y Combustibles (SEC). Exigencia reglamentaria del DS 1/2022; **no se sustituye** por plan de contingencia (el plan es complementario).
- **Anclaje**: DS 1/2022 art. 19 letra c; criterio de armonización normativa de este glosario.
- **Uso OPM v1.1**: absorbido en `e-infraestructura` (Unfold #2).

### Cartera de Prestaciones de HD
- **Definición**: listado de prestaciones brindadas por el Establecimiento. Si una prestación requerida por el paciente no está en la cartera, es exclusión categórica de ingreso (art. 17 Nº 3).
- **Anclaje**: DS 1/2022 art. 5 letra p; art. 17 Nº 3; NT 2024 §Equipamiento ("cartera de prestaciones ofrecida").
- **Uso OPM v1.1**: cosa informacional sistémica `e-cartera`. Instrumento de 2.2 Verificación de Criterios.
- **Sinónimos**: Listado de prestaciones, Oferta de prestaciones.

### Conocimiento Normativo y Técnico
- **Definición operativa**: corpus de manuales, protocolos, planes de capacitación y normativa absorbida localmente por el Establecimiento. Supuesto S1: declarado sistémico aunque la fuente externa MINSAL es ambiental.
- **Anclaje**: DS 1/2022 art. 8 letra b; NT 2024 §Protocolos y manuales.
- **Uso OPM v1.1**: cosa informacional sistémica `e-conocimiento`. Instrumento transversal.
- **Sinónimos**: Manuales DT, Protocolos vigentes.

### Coordenadas del Domicilio
- **Definición operativa**: representación informacional de la ubicación geográfica del Domicilio del Paciente, generada durante la Verificación de Criterios (2.2). Necesaria para verificar radio de cobertura y planificar logística.
- **Anclaje**: NT 2024 §Equipamiento (vehículos + radio de cobertura).
- **Uso OPM v1.1**: cosa informacional sistémica `e-coordenadas-domicilio` (RF2 exhibe a Domicilio del Paciente).

---

## 7. Procedimientos Normativos

### Autorización Sanitaria
- **Definición**: acto administrativo de la SEREMI que autoriza al Establecimiento a otorgar prestaciones de HD. Vigencia 3 años, prorrogable automáticamente.
- **Anclaje**: DS 1/2022 arts. 4-6.
- **Uso OPM v1.1**: NO modelado; reservado para OPD paralelo de Cumplimiento Normativo.
- **Excepción**: si la autorización del establecimiento ya contempla HD, no se requiere autorización adicional.

### Antecedentes de la Solicitud de Autorización Sanitaria
- **Definición**: 15+ antecedentes requeridos en la solicitud (DS 1/2022 art. 5 letras a-o): identificación, dominio del inmueble, planos, listado de equipos, programa de mantención, protocolos, etc.
- **Anclaje**: DS 1/2022 art. 5.

### Fiscalización
- **Definición**: actividad de la SEREMI que controla las actividades del Establecimiento. Las contravenciones se sancionan según Libro X del Código Sanitario.
- **Anclaje**: DS 1/2022 art. 23.
- **Uso OPM v1.1**: NO modelado.

### Requisitos de Ingreso a HD
- **Definición**: 4 condiciones que el paciente debe cumplir para ingresar a HD: (a) situación clínica (patología aguda o crónica reagudizada, clínicamente estable, susceptible de tratamiento en domicilio), (b) residencia con condiciones sanitarias mínimas dentro del radio de cobertura, (c) red de apoyo familiar o tutor responsable, (d) consentimiento informado escrito.
- **Anclaje**: DS 1/2022 art. 15 letras a-d.
- **Uso OPM v1.1**: predicados χ_i internos al proceso 2.2 Verificación de Criterios (no son cosas).

### Causales de Egreso
- **Definición**: 6 causales del DS 1/2022 art. 16 letras a-f:
  - a) alta médica por recuperación del cuadro clínico
  - b) cumplimiento del plan terapéutico y de cuidados
  - c) reingreso hospitalario programado por inestabilidad o complicaciones
  - d) fallecimiento
  - e) renuncia voluntaria del paciente o representante
  - f) alta disciplinaria determinada por DT (no adherencia, conductas irrespetuosas, rechazo a visitas)
- **Anclaje**: DS 1/2022 art. 16.
- **Uso OPM v1.1**: a refinarse en SD-Egreso como state-expression de `egresado` o subprocesos hermanos.

### Exclusiones de Ingreso
- **Definición**: 4 condiciones que impiden ingreso a HD (DS 1/2022 art. 17): (a) inestabilidad clínica o ausencia de diagnóstico establecido, (b) patología de salud mental descompensada, (c) necesidad de prestación no incluida en el listado del Establecimiento, (d) condición de alta disciplinaria previa del art. 16 letra f.
- **Anclaje**: DS 1/2022 art. 17.
- **Uso OPM v1.1**: gatillan el sub-estado `rechazado categórico` de `respondida` en SD-1.2.

### IAAS (Infecciones Asociadas a la Atención de Salud)
- **Definición**: programa de prevención y control de infecciones asociadas a la atención de salud. Curso obligatorio de 80 horas para Dirección Técnica, Coordinación y personal clínico. Vigencia 5 años.
- **Anclaje**: Res. Ex N° 60/2022 MINSAL; DS 1/2022 arts. 7-13; NT 2024 §Habilitación.
- **Uso OPM v1.1**: requisito implícito de los roles profesionales.

### REAS (Reglamento sobre Manejo de Residuos de Establecimientos de Atención de Salud)
- **Definición**: reglamento DS 6/2009 sobre manejo de residuos especiales. El Establecimiento HODOM debe tener protocolo ajustado.
- **Anclaje**: DS 6/2009; DS 1/2022 art. 5 letra o; NT 2024 §Manejo de residuos.

### RCP (Reanimación Cardiopulmonar Básica)
- **Definición**: curso de soporte vital básico (RCP) de 3 horas. Requisito acumulativo (NO sustituye IAAS de 80 horas) para personal clínico directo.
- **Anclaje**: Decreto Exento N° 52/2022; DS 1/2022 art. 12; NT 2024 §Habilitación.

### Soporte Vital Básico
- **Definición**: capacitación obligatoria del personal profesional y técnico que realiza atención clínica. Requisito acumulativo con IAAS y certificación de desfibrilador.
- **Anclaje**: NT 2024 §Inducción y certificación.

### Inducción Obligatoria
- **Definición**: capacitación al ingreso del personal: 44 horas mínimo, carácter teórico-práctico, registro obligatorio en hoja de vida.
- **Anclaje**: NT 2024 §Inducción y certificación.

### Convenio con Terceros
- **Definición**: prestadores públicos y privados pueden celebrar convenios con terceros (incluyendo ISAPRES u organismos de la Ley 16.744) para garantizar continuidad de atenciones en domicilio según seguro de salud.
- **Anclaje**: NT 2024 §Convenios permitidos.

### Prestador de Hospitalización Domiciliaria en Convenio
- **Definición**: prestador público o privado que recibe pacientes desde establecimientos de salud para continuar tratamiento.
- **Anclaje**: NT 2024 §Definiciones.

---

## 8. Normativa Cruzada Citada

### DS 1/2022 (Reglamento HODOM)
- Reglamento de Establecimientos que Otorgan Prestaciones de HD.
- Fuente de la mayoría de exigencias normativas del modelo.
- **Anclaje raíz**: `~/kora/artifacts/knowledge/salud/salubrista/hodom/normativa/01-reglamento-hodom-ds1-2022.md`.

### Acto Exento N° 31/2024
- Acto administrativo del MINSAL que aprueba la Norma Técnica HODOM (05-jun-2024).
- Suscrito por Ministra Ximena Aguilera Sanhueza.
- **Anclaje raíz**: `02-decreto-exento-31-2024-aprueba-norma-tecnica.md`.

### NT 2024 (Norma Técnica HODOM)
- Norma Técnica para Establecimientos que Otorgan Prestaciones de HD.
- 16 páginas anexas al Acto Exento 31/2024.
- **Anclaje raíz**: `03-norma-tecnica-hodom-2024.md`.

### Ley 20.584 (Derechos y Deberes de las Personas)
- Ley sobre derechos y deberes de las personas en relación con su atención en salud (2012). Sustento del Consentimiento Informado y la Carta de Derechos y Deberes.

### Ley 19.628 (Protección de la Vida Privada)
- Ley sobre protección de la vida privada y datos personales (1999). Aplica al tratamiento de información clínica como dato sensible.

### Ley 20.575 (Principio de Finalidad)
- Principio de finalidad en el tratamiento de datos personales (2012). Refuerzo de 19.628.

### DS 41/2012 (Reglamento sobre Fichas Clínicas)
- Reglamento que regula el manejo de fichas clínicas. La Ficha Clínica del Establecimiento HODOM debe cumplir DS 41.

### DS 594/2000 (Condiciones Sanitarias Lugares de Trabajo)
- Condiciones sanitarias y ambientales básicas en lugares de trabajo. Aplica a las dependencias administrativas del Establecimiento.

### DS 6/2009 (Reglamento REAS)
- Reglamento sobre manejo de residuos especiales. Ver REAS arriba.

### Res. Ex N° 60/2022 (Norma Técnica IAAS)
- Norma Técnica sobre Programa de Prevención y Control de IAAS.

### Decreto Exento N° 52/2022 (Norma Técnica RCP)
- Norma técnica de contenidos para capacitación en RCP básica y uso de desfibriladores.

### Res. Exenta N° 875/2013 (Norma Técnica N° 154)
- Norma Técnica N° 154 sobre Programa Nacional de Calidad y Seguridad de la Atención en Salud.

### DS 90/2017 (Certificación de Auxiliares)
- Certificación de auxiliares de la salud por SEREMI. Aplica a Técnicos/Auxiliares de Enfermería.

### DS 725/1968 (Código Sanitario)
- Código Sanitario. El Libro X regula sanciones por contravenciones de los Establecimientos HODOM.

### DFL 1/2005 (Texto Refundido MINSAL)
- DFL del Ministerio de Salud que fija texto refundido del DL 2.763/1979 y de las leyes 18.933 y 18.469. Sustento jurídico del Acto Exento 31/2024.

### Ley 19.880
- Ley de Bases de los Procedimientos Administrativos. Sustento jurídico del Acto Exento.

### Ley 16.744 (Accidentes y Enfermedades del Trabajo)
- Ley sobre accidentes del trabajo y enfermedades profesionales. Organismos administradores pueden celebrar convenios con prestadores HODOM (NT 2024 §Convenios permitidos).

### Decreto N° 136/2004 (Reglamento Orgánico MINSAL)
- Reglamento orgánico del Ministerio de Salud.

### Decreto N° 140/2004 (Reglamento Orgánico SS)
- Reglamento orgánico de los Servicios de Salud.

### DS N° 28/2009
- Reglamento que delega en la Ministra de Salud la facultad de suscribir decretos que aprueban normas técnicas bajo la fórmula "Por orden del Presidente de la República".

### Resolución N° 7/2019 (Contraloría)
- Resolución de la Contraloría General de la República. Fundamento jurídico del Acto Exento.

### Res. Ex. N° 328/2023 (Subsec. Salud Pública)
- Resolución que creó el grupo de trabajo para elaborar la propuesta de Norma Técnica HODOM 2024.

### SEC (Superintendencia de Electricidad y Combustibles)
- Organismo que autoriza el respaldo eléctrico del Establecimiento HODOM.

### Superintendencia de Salud
- Mantiene el Registro de Prestador Individual del personal habilitado.

### ISAPRE (Institución de Salud Previsional)
- Una de las instituciones con las que el prestador HODOM puede celebrar convenios (NT 2024 §Convenios).

---

## 9. Índice alfabético de términos

A: Acto Exento 31/2024, Atención Cerrada, Atención Domiciliaria, Atención de Acciones Emergentes o No Planificadas, Atención Profesional, Autorización Sanitaria.

C: Capacidad Operacional Disponible, Carta de Derechos y Deberes, Cartera de Prestaciones de HD, Causales de Egreso, Condición Clínica Estable, Conocimiento Normativo y Técnico, Consentimiento Informado, Constancia de Acciones en caso de Fallecimiento, Coordinación, Coordinación Clínica HD, Coordenadas del Domicilio, Curso Clínico-Asistencial, Cuidador / Tutor Legal, Convenio con Terceros.

D: Decreto Exento 52/2022, Decreto Supremo 1/2022, Decreto Supremo 6/2009, Decreto Supremo 41/2012, Decreto Supremo 90/2017, Decreto Supremo 594/2000, DFL 1/2005, Dirección Técnica, División de Gestión de la Red Asistencial, Dispositivos de Uso Médico, Domicilio del Paciente.

E: Elaboración de Solicitud de Transferencia a HD, Egresado (estado), Encuesta de Satisfacción Usuaria al Egreso, Enfermera Coordinadora de HD, Enfermero(a) Clínico, Epicrisis al Alta, Equipamiento Médico, Equipo de Gestión de Camas, Equipo de Salud HD (ver Unfold #1), Establecimiento HODOM, Evaluación Domiciliaria Inicial, Evaluación de Solicitud de Transferencia a HD, Exclusiones de Ingreso.

F: Ficha Clínica, Fiscalización, Fonoaudiólogo, Formulario de Hospitalización Domiciliaria, Formulario de Ingreso.

H: Hospitalización Domiciliaria.

I: IAAS, Infraestructura, Inducción Obligatoria, Insumos Clínicos, ISAPRE.

K: Kinesiólogo.

L: Ley 16.744, Ley 19.628, Ley 19.880, Ley 20.575, Ley 20.584.

M: Manual de Organización Interna, Manual de Procedimientos, Medicamentos, Médico Cirujano de Atención Directa, Médico Cirujano Regulador, Médico Tratante de Atención Cerrada.

N: Norma Técnica HODOM 2024.

O: Otorgamiento de Consentimiento Informado.

P: Paciente, Paciente Agudo, Paciente Crónico Reagudizado, Paciente Hospitalizado Clínicamente Estable, Personal Administrativo y Auxiliar, Plan de Capacitación Anual (PAC), Plan de Cuidados de Enfermería, Plan Terapéutico y de Cuidados, Prestador en Convenio, Procedimientos Normativos, Profesional de Salud de HD, Protocolos Clínicos.

R: Realización de Transferencia a HD, RCP, Recepción de Solicitud de Transferencia, Red de Apoyo Familiar, REAS, Reglamento Interno, Registro del Episodio de HD, Reporte de Atención Profesional, Reporte de Información Clínico-Asistencial Relevante, Requisitos de Ingreso a HD, Res. Ex 60/2022, Res. Ex 328/2023, Res. Exenta 875/2013, Resolución N° 7/2019, Respaldo Eléctrico, Resolución de Solicitud de Transferencia, Resumen Clínico en Domicilio.

S: SEC, SEREMI, Servicios de Salud, Servicio o Unidad de Atención Cerrada, Sistema de Comunicaciones 24/7, Sistema de Registro Clínico y Administrativo, Solicitud de Transferencia a HD, Soporte Vital Básico, Superintendencia de Salud.

T: Técnico de Enfermería, Tramitación de Egreso de HD, Trabajador(a) Social.

U: Unidad o Servicio de Hospitalización Domiciliaria.

V: Vehículos de Transporte.

---

## 10. Notas de uso del glosario

- **Trazabilidad normativa estricta**: cada definición está anclada a artículo, sección o letra específica de la fuente normativa. Si no hay anclaje normativo, se declara como "derivado del modelo operativo" o "decisión del operador".
- **Uso OPM v1.1**: indica si el término está materializado como cosa, proceso, estado, instrumento o agente en `~/projects/hd-hsc-os/docs/models/opm-hodom-bundle-v1.1.json`. Si no está modelado, se declara la razón (pendiente / fuera de frontera / decisión declarada).
- **Sinónimos**: se usan formas breves operativas. La forma canónica es la primera enunciada en la entrada.
- **Términos relacionados**: enlaces semánticos a otras entradas del glosario.
- **Versionado**: este glosario es v1.0.0. Cambios futuros en la normativa o decisiones del operador requieren incrementar versión.
- **Criterio de armonización**: DS 1/2022 > NT 2024 > Acto Exento 31/2024. Si dos fuentes tensionan, prevalece la jerarquía superior.
