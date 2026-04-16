# Session: 2026-04-07 04:18:10 UTC

- **Session Key**: agent:mente-omega:telegram:direct:7192195698
- **Session ID**: e4b87bc4-d198-49d2-89fb-365e0c10b16c
- **Source**: telegram

## Conversation Summary

user: A new session was started via /new or /reset. Run your Session Startup sequence - read the required files before responding to the user. Then greet the user in your configured persona, if one is provided. Be yourself - use your defined voice, mannerisms, and mood. Keep it to 1-3 sentences and ask what they want to do. If the runtime model differs from default_model in the system prompt, mention the default model. Do not mention internal steps, files, tools, or reasoning.
Current time: Monday, April 6th, 2026 - 11:48 PM (America/Santiago) / 2026-04-07 03:48 UTC
assistant: [[reply_to_current]] Buenas noches, Felix. Soy Mente Omega, listo para convertir complejidad en claridad operable, con rigor y sin relleno. ¿Qué quieres abordar hoy?
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "803",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-04-07 05:55 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

Tenemos un desafío en donde enfrentarás una altísima complejidad.

Mira, te voy a pasar un repositorio con muchísima información en bruto del sistema de hospitalización domiciliaria del Hospital de San Carlos, que está en este proceso de la migración de los datos legados a una nueva estructura de datos. Te voy a pasar entonces el acceso al repositorio para que tengas una idea de cuál es la información con la que se ha trabajado hasta la fecha.

Posteriormente te voy a pasar también el modelo de datos actual hacia el cual se está migrando. Posteriormente te daré acceso a la normativa de funcionamiento de la hospitalización domiciliaria y después a varios modelos OPM elaborados para ir tratando de entender cómo se estructura este sistema y también un modelo categorial.

Así que va a haber mucha información con respecto a la hospitalización domiciliaria.

Lo que tú tienes que hacer es evaluar todo eso e identificar los usuarios de un sistema para la hospitalización domiciliaria que cuente con todo lo necesario para poder apoyar en brindar las atenciones, incluyendo atenciones telemáticas que deben ser realizadas y funcionar en base a la normativa vigente chilena, así como también los registros clínicos que deberán ser digitalizados y sistemas para el apoyo logístico y de rutas que deberá también ser dinámico y todo lo que tiene que ver con lo que es una hospitalización misma y la gestión de un grupo de 20 a 30 pacientes que están hospitalizados en sus casas.

Así que te voy a concentrar toda esa información y tu tarea va a ser identificar los usuarios del sistema y elaborar en función de sus necesidades e historias de usuario el diseño del sistema operativo de la hospitalización domiciliaria del Hospital de San Carlos. 

/home/felix/projects/hdos/documentacion-legacy
/home/felix/projects/hdos/docs/models/erd-modelo-integrado-hodom.html
/home/felix/projects/hdos/docs/models/FHIR_R4_Resource_References.md
/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/normativa/raw/01-reglamento-hodom-ds1-2022.md
/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/normativa/raw/02-decreto-exento-31-2024-aprueba-norma-tecnica.md
/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/normativa/raw/03-norma-tecnica-hodom-2024.md
/home/felix/projects/hdos/docs/specs/manual-rem-2026.md
/home/felix/.openclaw/workspace-mente-omega/kv_outbox_mente-omega/opm-hodom-model-v2.5.md
/home/felix/.openclaw/workspace-mente-omega/kv_outbox_mente-omega/modelo-categorial-hodom-san-carlos.md
assistant: [[reply_to_current]] Sí. Síntesis de abordaje: la ruta dominante aquí es diseño de sistema, con capas de normativa, modelado clínico y migración de datos; voy a extraer primero actores, obligaciones operativas y capacidades mínimas del sistema, y desde ahí construir usuarios, necesidades, historias de usuario y el diseño operativo. Empiezo revisando las fuentes base que me pasaste.
assistant: [[reply_to_current]] Sí, ya entré en materia.

Síntesis: la ruta dominante es diseño de sistema, apoyado en análisis y modelado. Ya pude leer los dos artefactos más densos y útiles que sí están accesibles, el modelo OPM y el modelo categorial, y con eso ya aparece una primera estructura sólida del sistema, sus procesos, restricciones y actores.

Primer recorte útil, todavía provisional pero fuerte:
1. usuarios clínico-asistenciales directos:
- médico de atención directa
- enfermero clínico
- TENS
- kinesiólogo
- fonoaudiólogo
- trabajador social

2. usuarios de coordinación y operación:
- profesional coordinador
- gestora encargada
- personal administrativo
- conductor / operador logístico
- director técnico
- eventualmente médico regulador

3. usuarios externos o co-actores del sistema:
- paciente
- cuidador / familiar responsable
- equipo APS / CESFAM
- establecimiento derivador hospitalario
- SEREMI / auditoría / reporte REM

4. sistema debe cubrir, como mínimo:
- elegibilidad e ingreso
- planificación clínica
- visitas y atención domiciliaria
- telesalud y llamadas
- registro clínico digital completo
- programación diaria y ruteo dinámico
- egreso y contrarreferencia
- gobernanza, cupos, REM, trazabilidad normativa

Pero hay una restricción real: varios de los archivos clave que me diste están fuera de mi área accesible, en particular:
- `/home/felix/projects/hdos/...`
- `/Users/felixsanhueza/...`

Eso significa que ahora mismo no puedo abrir:
- el repositorio legacy
- el ERD HTML
- el FHIR references
- la normativa en esos paths
- el manual REM en ese path

Recomendación concreta: súbeme o copia esos archivos/directorios dentro de `/workspace` o dentro de `~/.openclaw/workspace-mente-omega/`, y sigo de inmediato con el análisis completo.

Si quieres, apenas los dejes accesibles, te entrego en este orden:
1. mapa definitivo de usuarios del sistema,
2. necesidades por usuario,
3. historias de usuario priorizadas,
4. diseño operativo del sistema HODOM San Carlos, módulo por módulo,
5. y una propuesta de arquitectura alineada con normativa chilena y migración de datos.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "814",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-04-07 05:59 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

/home/felix/kora/KNOWLEDGE/salud/hodom/normativa
assistant: [[reply_to_current]] Voy a probar ese path ahora, porque si entra, ya puedo incorporar la capa normativa al análisis y cerrar mejor los usuarios y obligaciones del sistema.
assistant: [[reply_to_current]] Síntesis: ese path sigue fuera de mi área accesible, así que todavía no lo puedo abrir desde aquí.

Necesito que lo copies o montes dentro de uno de estos lugares:
- `/home/felix/.openclaw/workspace-mente-omega/`
- o, equivalente en sandbox, `/workspace/`

Por ejemplo, si dejas la normativa en algo como:
- `/home/felix/.openclaw/workspace-mente-omega/hodom/normativa/`

yo sigo de inmediato.

Si quieres, el siguiente bloque ideal para destrabar esto sería:
1. normativa,
2. `FHIR_R4_Resource_References.md`,
3. ERD integrado,
4. luego el repositorio legacy.
user: [media attached: 3 files]
[media attached 1/3: media/inbound/03-norma-tecnica-hodom-2024---0ec4ce57-1854-40d4-a07e-4cbff4a99ec7.md (text/markdown) | media/inbound/03-norma-tecnica-hodom-2024---0ec4ce57-1854-40d4-a07e-4cbff4a99ec7.md]
[media attached 2/3: media/inbound/02-decreto-exento-31-2024-aprueba-norma-tecnica---58c2421a-8a34-410b-9418-c22931285377.md (text/markdown) | media/inbound/02-decreto-exento-31-2024-aprueba-norma-tecnica---58c2421a-8a34-410b-9418-c22931285377.md]
[media attached 3/3: media/inbound/01-reglamento-hodom-ds1-2022---4746aae7-b335-4df1-b449-b96fe0154ec9.md (text/markdown) | media/inbound/01-reglamento-hodom-ds1-2022---4746aae7-b335-4df1-b449-b96fe0154ec9.md]
To send an image back, prefer the message tool (media/path/filePath). If you must inline, use MEDIA:https://example.com/image.jpg (spaces ok, quote if needed) or a safe relative path like MEDIA:./image.jpg. Avoid absolute paths (MEDIA:/...) and ~ paths - they are blocked for security. Keep caption in the text body.
Conversation info (untrusted metadata):
```json
{
  "message_id": "820",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-04-07 06:00 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

[Telegram Ominono id:7192195698 +1m Tue 2026-04-07 06:00 GMT+2] <media:document>

<file name="03-norma-tecnica-hodom-2024---0ec4ce57-1854-40d4-a07e-4cbff4a99ec7.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="914edb8e86e8c921">>>
Source: External
---
---
_manifest:
 urn: "urn:salud:kb:hodom-norma-tecnica-2024"
 provenance:
 created_by: "Codex"
 created_at: "2026-03-13"
 source: "source/pro/hodom/normativa-hodom/NORMA-TECNICA-DECRETO-EXENTO-N°-31-SRA-2024.md"
version: "1.0.1"
status: published
tags: [hodom, norma-técnica, minsal, hospitalización-domiciliaria, requisitos]
lang: es
extensions:
 kora:
 family: normative
---

# Norma Técnica para Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria

## Finalidad, ámbito de aplicación y convenios permitidos

- La norma técnica se dicta conforme al art. `18` del `DS N° 1/2022`, Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria.
- Finalidad:
 - fijar directrices y requisitos mínimos para servicios o unidades de prestadores públicos y privados que presten hospitalización domiciliaria a pacientes agudos o crónicos reagudizados
 - asegurar tratamiento, cuidados y seguimiento seguros y de calidad
- Obligación transversal:
 - los servicios o unidades de hospitalización domiciliaria deben garantizar continuidad de la atención cumpliendo normativa vigente y asegurando atención segura y de calidad
- Ámbito de aplicación:
 - regula a unidades o servicios de establecimientos de salud o prestadores en convenio, públicos y privados, que otorguen hospitalización domiciliaria a pacientes agudos o crónicos reagudizados
 - materias reguladas:
 - personal
 - infraestructura
 - equipamiento
 - registros
 - procedimientos técnicos
 - protocolos u otros
 - requisitos y condiciones de traslado del equipamiento médico y del personal desde y hacia el domicilio
 - medidas de seguridad correspondientes
- Convenios permitidos:
 - los prestadores públicos y privados pueden celebrar convenios con terceros, incluidas instituciones de salud previsional u organismos administradores de la `Ley N° 16.744`, para garantizar continuidad de las atenciones en el domicilio según el seguro de salud

## Definiciones y marco legal citado

### Definiciones

- **Hospitalización Domiciliaria (HD)** - modalidad asistencial alternativa a la hospitalización tradicional; el usuario recibe cuidados similares a los otorgados en establecimientos hospitalarios, en calidad y cantidad, sin los cuales habría requerido permanencia en atención cerrada.
- **Paciente agudo** - persona sin patología previa y con cuadro clínico agudo que requiere hospitalización para recuperar salud.
- **Paciente crónico reagudizado** - persona con patología previa y cuadro clínico agudo, asociado o no a esa patología de base, que requiere hospitalización para recuperar salud.
- **Condición Clínica Estable** - equilibrio de funciones vitales que permite traslado al domicilio pese a patología no resuelta o parcialmente solucionada.
- **Atención Domiciliaria** - acciones de salud realizadas en domicilio por prestadores en modalidad ambulatoria y de libre elección.
- **Dispositivos de uso médico** - instrumento, aparato, implemento, máquina, equipo, artefacto, implante u otro artículo similar que cumpla normativa vigente.
- **Prestador de hospitalización domiciliaria en convenio** - prestador público o privado que recibe pacientes desde establecimientos de salud para continuar tratamiento.

### Marco legal citado

| Documento | Año | Descripción |
| --- | --- | --- |
| Decreto `01/MINSAL` | 2022 | Reglamento de establecimientos que otorgan prestaciones de Hospitalización Domiciliaria. |
| Decreto `725/MINSAL` | 1968 | Código Sanitario. |
| Ley `20.584/MINSAL` | 2012 | Derechos y deberes de las personas en relación con acciones vinculadas a su atención en salud. |
| Ley `N° 19.628` | 1999 | Protección de la vida privada. |
| Ley `N° 20.575` | 2012 | Principio de finalidad en el tratamiento de datos personales. |
| Decreto `41/MINSAL` | 2012 | Reglamento sobre Fichas Clínicas. |
| Decreto `594/MINSAL` | 2000 | Condiciones sanitarias y ambientales básicas en lugares de trabajo. |
| Decreto `6/MINSAL` | 2009 | Reglamento `REAS`. |
| Res. Ex `60/MINSAL` | 2022 | Norma Técnica sobre Programa de Prevención y Control de `IAAS`. |
| Decreto exento `52` | 2022 | Norma técnica de contenidos para capacitación en reanimación cardiopulmonar básica y uso de desfibriladores. |
| Res. Exenta `N° 875` | 2013 | Norma Técnica N° 154 sobre Programa Nacional de Calidad y Seguridad de la Atención en Salud. |

## Habilitación del personal y requisitos por cargo

- Regla transversal:
 - todo funcionario o trabajador, profesional, técnico o auxiliar de la salud, debe estar habilitado para el ejercicio profesional en Chile conforme a normativa vigente
 - los auxiliares deben contar con certificación de `SEREMI` según `DS N° 90/2017`
- Especialidades exigidas:
 - si se declaran prestaciones de HD pediátricas o psiquiátricas, debe existir médico cirujano con la especialidad correspondiente o con experiencia demostrable de al menos `2` años en esos servicios
- Dirección Técnica:
 - médico cirujano
 - formación de postítulo o postgrado en gestión en salud
 - curso de prevención de `IAAS`
 - permanencia mínima: `22` horas semanales
- Coordinación:
 - profesional de la salud, preferentemente enfermera/o
 - formación en gestión en salud
 - la fuente presenta conflicto entre exigencia de `IAAS` de `80` horas en el texto general y `RCP` de `3` horas en la tabla resumida

### Requisitos resumidos por cargo

| Cargo | Experiencia | Formación / Capacitación | Vigencia |
| --- | --- | --- | --- |
| Director(a) técnico(a) | `2` años clínica | Postítulo gestión / `IAAS` (`80` hrs) | `5` años máx. |
| Coordinación | `5` años clínica | Formación en gestión; requisito de capacitación inconsistente en la fuente: texto general = `IAAS` (`80` hrs), tabla = `RCP` (`3` hrs) | `5` años máx. |
| Médico(a) atención directa | `2` años médico-quirúrgica | Curso `IAAS` (`80` hrs) / `RCP` (`3` hrs) | `5` años máx. |
| Médico(a) regulador | `2` años médico-quirúrgica | `RCP` (`3` hrs) | `5` años máx. |
| Enfermero(a) clínico | `2` años clínica | `RCP` (`3` hrs) | `5` años máx. |
| Kinesiólogo(a) | `2` años clínica | `RCP` (`3` hrs) | `5` años máx. |
| Técnico o Auxiliar | `1` año clínica | `RCP` (`3` hrs) | `5` años máx. |

### Inconsistencia interna de la fuente sobre Coordinación

- La fuente no es internamente consistente:
 - en el texto general exige que Coordinación cuente con formación en gestión en salud, curso de `IAAS` de al menos `80` horas y perfil profesional preferente de enfermera/o
 - en la tabla resumida por cargo asigna a Coordinación `RCP` de `3` horas
- Estado de la inconsistencia:
 - no resuelta en la fuente
 - debe tratarse como tensión normativa hasta verificar texto oficial o fe de erratas

### Inducción y certificación

- El personal profesional y técnico que realiza atención clínica debe contar con:
 - curso de soporte vital básico
 - curso `IAAS`
 - certificación de uso de desfibrilador
- Al ingreso:
 - inducción obligatoria de al menos `44` horas
 - carácter teórico-práctico
 - registro obligatorio en hoja de vida

## Infraestructura, equipamiento y abastecimiento

### Infraestructura mínima

- Toda unidad o servicio de HD debe contar con:
 - dependencias administrativas con:
 - sistema de comunicación telefónica o radial permanente
 - sistema de grabación o registro manual de llamadas para trazabilidad, con fecha, hora, emisor, receptor y derivación
 - soporte informático e internet
 - respaldo de energía eléctrica autorizado o plan de contingencia
 - sector seguro para resguardo de fichas clínicas y protocolos
 - dependencia para residuos destinada a disposición transitoria, si corresponde
 - dependencia específica para servicios de aseo
 - bodegas para almacenamiento de insumos con control de temperatura según especificaciones del fabricante
 - farmacia o botiquín autorizado, o convenios que aseguren abastecimiento y cadena de frío en domicilio

### Equipamiento y dispositivos de uso médico

- Equipamiento mínimo obligatorio:
 - equipos para monitorizar signos vitales:
 - presión arterial
 - frecuencia cardíaca
 - frecuencia respiratoria
 - saturación de oxígeno
 - instrumentos adicionales según cartera de prestaciones ofrecida
 - vehículos de transporte con acceso a estacionamiento o lugar de detención transitoria

## Registros, protocolos y plan de capacitación anual

### Registros obligatorios

- **Ficha clínica**
 - puede ser física o electrónica
 - debe cumplir `DS N° 41` sobre fichas clínicas
- **Consentimiento informado**
 - documento firmado
 - acredita entrega de la carta de Derechos y Deberes
- **Resumen clínico en domicilio**
 - debe contener diagnósticos, tratamientos y cuidados
 - sirve para consulta en emergencias por equipos externos

### Protocolos y manuales obligatorios

- Documentos que deben mantenerse actualizados y aprobados por Dirección Técnica:
 - **Manual de Organización Interna**
 - organigrama
 - roles
 - horarios
 - reglamento de higiene
 - **Protocolos clínicos**
 - evaluación e ingreso de pacientes
 - programación de rutas y visitas domiciliarias
 - categorización y egreso de pacientes, incluidas altas y fallecidos
 - gestión de recetas, interconsultas y evolución en ficha
 - actuación ante emergencias y agresiones al equipo de salud
 - **Manual de procedimientos**
 - manejo de vías venosas periféricas y centrales
 - catéteres urinarios
 - traqueostomías
 - toma de muestras
 - precauciones de aislamiento
 - **Manejo de residuos**
 - procedimiento ajustado al `DS N° 6/2009` para retiro y eliminación de residuos especiales
 - **Plan de Capacitación Anual (PAC)**
 - `IAAS`
 - `RCP` básica
 - inducción
 - cursos de humanización del cuidado

## Bibliografía citada por la norma

1. Decreto supremo `N° 1/2022`, Ministerio de Salud, Reglamento de HD.
2. Estudio de Evaluación Ex Post Hospitalización en Domicilio, Ministerio de Desarrollo Social (`2013`).
3. Hospitalización domiciliaria como alternativa sustentable para implementar en Chile: scoping review (`2020`).
4. La hospitalización domiciliaria: antecedentes, situación actual y perspectivas (`Cotta et al.`).
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="914edb8e86e8c921">>>
</file>

<file name="02-decreto-exento-31-2024-aprueba-norma-tecnica---58c2421a-8a34-410b-9418-c22931285377.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="af7bc867624d6935">>>
Source: External
---
---
_manifest:
 urn: "urn:salud:kb:hodom-decreto-exento-31-2024"
 provenance:
 created_by: "Codex"
 created_at: "2026-03-13"
 source: "source/pro/hodom/normativa-hodom/DECRETO-EXENTO-N°-31-SRA-2024.md"
version: "1.0.1"
status: published
tags: [hodom, decreto-exento, norma-técnica, minsal, hospitalización-domiciliaria]
lang: es
extensions:
 kora:
 family: normative
---

# Decreto Exento N° 31/2024 que Aprueba la Norma Técnica para Hospitalización Domiciliaria

## Acto aprobatorio, fecha y autoridad suscriptora

- Decreto exento `N° 31`.
- Fecha: `05 Jun 2024`, Santiago.
- Órgano emisor: Ministerio de Salud.
- Autoridad suscriptora:
 - `Ximena Aguilera Sanhueza`
 - Ministra de Salud
- Fórmula de cierre: `ANÓTESE Y COMUNÍQUESE`.

## Fundamentos documentales y jurídicos invocados

- Memorándums citados:
 - `C37/N° 93/2023`, Jefe de División de Gestión de la Red Asistencial
 - `C37/N° 81/2023`, Jefe de División de Gestión de la Red Asistencial
 - `B35/N° 669/2023`, Jefa de División Políticas Públicas Saludables y Promoción
 - `N° 35/2023`, Jefe de Gabinete de la Subsecretaría de Redes Asistenciales
- Base jurídica citada:
 - `DFL N° 1/2005` del Ministerio de Salud, que fija texto refundido, coordinado y sistematizado del `DL N° 2.763/1979` y de las leyes `N° 18.933` y `N° 18.469`
 - `Ley N° 19.880`
 - `DS N° 1/2022` del Ministerio de Salud, Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria
 - `Decreto N° 136/2004` del Ministerio de Salud, Reglamento Orgánico del Ministerio de Salud
 - `Decreto N° 140/2004` del Ministerio de Salud, Reglamento Orgánico de los Servicios de Salud
 - `DS N° 28/2009` del Ministerio de Salud
 - `Resolución N° 7/2019` de la Contraloría General de la República

## Fundamentos materiales del decreto

| N° | Fundamento |
| --- | --- |
| 1 | El art. 1 del `DFL N° 1/2005` atribuye al Estado, por medio del Ministerio de Salud y demás organismos, la garantía de acceso libre e igualitario a acciones de promoción, protección, recuperación y rehabilitación de la salud, además de coordinar, controlar y, cuando proceda, ejecutar esas acciones. |
| 2 | El art. 4 del mismo cuerpo asigna al Ministerio de Salud la formulación, fijación y control de políticas de salud y, en especial, la rectoría del sector salud, incluida la formulación, control y evaluación de planes y programas generales. |
| 3 | En `2022` el Ministerio de Salud dictó el `DS N° 1/2022`, que aprueba el reglamento de establecimientos que otorgan prestaciones de hospitalización domiciliaria. |
| 4 | El art. 18 del `DS N° 1/2022` dispone que una norma técnica del Ministerio de Salud regulará condiciones mínimas de personal, infraestructura, equipamiento, registros, procedimientos, protocolos, traslado y seguridad para hospitalización domiciliaria. |
| 5 | La `Resolución Exenta N° 328/2023` de la Subsecretaría de Salud Pública creó un grupo de trabajo para elaborar la propuesta de norma técnica, con participación de ambas subsecretarías, Servicios de Salud y prestadores privados de hospitalización domiciliaria. |
| 6 | El Memorándum `C37/N° 93/2023` solicitó la aprobación de la Norma Técnica para establecimientos que otorgan prestaciones de hospitalización domiciliaria, adjuntando el texto normativo y sus antecedentes. |
| 7 | El `DS N° 28/2009`, N° 1 numeral 2, delega en la Ministra de Salud la facultad de suscribir, bajo la fórmula "Por orden del Presidente de la República", los decretos que aprueban normas técnicas. |

## Efecto jurídico y mandatos operativos

- Se aprueba la **Norma Técnica para Establecimientos que otorgan prestaciones de Hospitalización Domiciliaria**.
- La norma aprobada consta en un documento adjunto de `16` páginas, que forma parte integrante del decreto.
- Publicación ordenada:
 - la División de Gestión de la Red Asistencial de la Subsecretaría de Redes Asistenciales debe publicar el texto íntegro del decreto y de la norma aprobada en [MINSAL](https://www.minsal.cl)
 - la publicación debe realizarse desde el total trámite del acto exento
- Distribución operativa:
 - debe remitirse un ejemplar del acto administrativo a los Servicios de Salud del país
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="af7bc867624d6935">>>
</file>

<file name="01-reglamento-hodom-ds1-2022---4746aae7-b335-4df1-b449-b96fe0154ec9.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="959ec6963b3630da">>>
Source: External
---
---
_manifest:
 urn: "urn:salud:kb:hodom-reglamento-ds1-2022"
 provenance:
 created_by: "Codex"
 created_at: "2026-03-13"
 source: "source/pro/hodom/normativa-hodom/norma-1181901-reglamento-hodom.md"
version: "1.0.1"
status: published
tags: [hodom, reglamento, normativa, hospitalización-domiciliaria, minsal]
lang: es
extensions:
 kora:
 family: normative
---

# Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria

## Ámbito de aplicación y concepto de hospitalización domiciliaria

Fuente oficial: [LeyChile - Norma 1181901](https://www.leychile.cl/Navegar?idNorma=1181901)

- Arts. 1-3.
- El reglamento rige a:
 - establecimientos de salud de atención cerrada, públicos o privados
 - prestadores públicos o privados en convenio con esos establecimientos
 - unidades o servicios que forman parte de esos establecimientos y otorgan prestaciones de hospitalización domiciliaria
- **Hospitalización domiciliaria** - modalidad asistencial alternativa a la hospitalización en atención cerrada para personas con patología aguda o crónica reagudizada; entrega cuidados similares a los otorgados en establecimientos hospitalarios, en calidad y cantidad, sin los cuales habría sido necesaria la permanencia en atención cerrada.
- Requisitos estructurales de la modalidad:
 - indicación médica
 - control médico
 - plan terapéutico del equipo de salud
 - término determinado por egreso del paciente
- Obligaciones del establecimiento de atención cerrada o del prestador en convenio:
 - ofrecer diversas alternativas de servicios de hospitalización domiciliaria para elección
 - asegurar acceso, oportunidad, continuidad y calidad de las prestaciones
- Exclusión expresa:
 - el reglamento no aplica a atenciones de salud domiciliarias ambulatorias y de libre elección, correspondientes al ejercicio libre de la profesión

## Autorización sanitaria, vigencia y antecedentes exigidos

- Arts. 4-6.

| Materia | Regla |
| --- | --- |
| Autoridad | La autorización sanitaria la otorga la `SEREMI` correspondiente al domicilio de las dependencias administrativas. |
| Excepción | Si la autorización sanitaria del establecimiento ya contempla atenciones en modalidad de hospitalización domiciliaria, esa autorización basta y no se requiere una adicional. |
| Vigencia | `3` años. |
| Prórroga | Automática y sucesiva por períodos iguales, mientras la autoridad no la deje sin efecto expresamente. |

- Antecedentes que debe incluir la solicitud:
 - identificación del establecimiento: nombre, nombre de fantasía si existe, domicilio, teléfono y correo electrónico
 - documentos que acrediten dominio del inmueble o derecho a uso, incluido certificado de dominio vigente, arriendo, comodato u otro
 - certificado municipal acorde a la actividad o certificado de recepción definitiva para edificaciones nuevas
 - escritura pública de constitución e individualización de representantes legales, o individualización del propietario si es persona natural
 - individualización del profesional que asumirá la Dirección Técnica y declaración jurada simple de aceptación del cargo
 - nómina del personal de salud habilitado, según registro de prestador individual de la Superintendencia de Salud o título revalidado o reconocido
 - planos de planta física con distribución funcional, flujos de circulación, recintos generales, bodegas o mobiliario para insumos, equipos y medicamentos
 - copias de planos o certificados de instalaciones de electricidad, agua potable y gas, visados por personal autorizado
 - listado de equipos utilizados en procedimientos generales y específicos, con autorización cuando corresponda
 - programa de mantención preventiva de maquinarias, equipos y vehículos de transporte, propios o arrendados
 - listado de elementos de protección personal según riesgo laboral
 - horario de funcionamiento y distribución de turnos del personal
 - manual de normas y procedimientos técnicos
 - reglamento interno de orden, higiene y seguridad
 - autorización sanitaria de botiquín, cuando corresponda
 - listado de prestaciones brindadas
 - protocolo de manejo de residuos especiales en establecimiento autorizado según reglamento `REAS`

## Dirección Técnica y coordinación del establecimiento

### Dirección Técnica

- Arts. 7-10.
- La Dirección Técnica es obligatoria.
- Requisito profesional:
 - médico cirujano habilitado para ejercer, según registro de prestador individual de la Superintendencia de Salud o título revalidado o reconocido
- Responsabilidad legal:
 - organización y funcionamiento del establecimiento
 - actividades técnicas y administrativas desarrolladas en él
- Funciones:
 - representar al establecimiento frente a autoridades de salud
 - aprobar manuales y procedimientos internos, técnicos y administrativos; velar por cumplimiento y actualización periódica según evidencia científica disponible
 - aprobar funciones, jornada y sistema de turnos del personal
 - velar por vacunación del personal sanitario conforme a programas `MINSAL`
 - mantener stock de insumos y medicamentos acorde a las prestaciones
 - verificar programas preventivos y de reparación de maquinarias, equipos médicos y vehículos
 - dotar al personal de elementos de seguridad personal y velar por condiciones mínimas de seguridad en lugares de trabajo y transporte
 - velar por cumplimiento del programa `IAAS`
 - cautelar cumplimiento de la prestación ofrecida en información, cobertura y tiempo de respuesta según convenio con el paciente
 - mantener registro manual o electrónico de intervenciones clínicas; velar por seguridad, integridad, confidencialidad e inviolabilidad; emitir certificados médicos cuando proceda
 - velar por resguardo de información clínica reservada y secreto profesional
 - velar por coordinación con instituciones derivadoras y médicos tratantes
 - coordinar agudización y requerimiento de reingreso hospitalario, con comunicación activa con el médico tratante
 - asegurar traslado oportuno a establecimiento de atención cerrada mediante servicio propio o tercero en convenio
 - participar en implementación y mantención de sistema de gestión de calidad, incluidas auditorías de reacciones adversas y mortalidad
 - gestionar implementación de programa de capacitación continua para personal profesional, técnico y auxiliar
- Jornada mínima: `22` horas semanales, informadas a la `SEREMI`.
- Todo cambio de Director Técnico debe comunicarse de forma inmediata a la `SEREMI`.

### Coordinación

- Art. 11.
- La coordinación debe estar a cargo de un profesional de salud con:
 - `5` años de experiencia clínica
 - formación en gestión
 - al menos un curso de `80` horas en prevención de `IAAS`
- Funciones:
 - supervisar actualización de manuales de organización interna, normas y procedimientos
 - supervisar procesos clínicos de hospitalización domiciliaria y respaldo de sus registros
 - gestionar personal garantizando continuidad asistencial
 - supervisar calidad de cuidados
 - gestionar insumos operacionales, mantenciones preventivas y reparación de equipos
 - mantener programa de inducción del personal y gestionar capacitaciones que aseguren competencias
 - coordinar continuidad de la atención con establecimientos de salud públicos o privados

## Dotación clínica mínima y otras funciones del personal

- Arts. 12-14.
- Dotación clínica mínima:
 - **Médico cirujano de Atención Directa**
 - experiencia mínima: `2` años en manejo de patologías médico-quirúrgicas
 - funciones:
 - supervisar actividades asistenciales prestadas en domicilio
 - gestionar oferta y demanda del establecimiento
 - apoyar técnicamente al equipo de salud en atención directa
 - coordinar continuidad de atención con establecimientos públicos o privados
 - reforzar indicaciones médicas o del personal de salud a paciente, familia y cuidadores
 - participar en evaluación de pacientes hospitalizados para decidir y gestionar ingreso y egreso a hospitalización domiciliaria
 - evaluar e indicar tratamiento a pacientes hospitalizados en domicilio
 - cumplir otras labores encomendadas por coordinación o Dirección Técnica
 - puede utilizar tecnologías de información y comunicación para diagnóstico, tratamiento, prevención y rehabilitación; otros profesionales designados por Dirección Técnica también pueden utilizarlas
 - **Médico cirujano regulador**
 - experiencia mínima: `2` años en regulación médica
 - cargo: atención a distancia o atención directa durante hospitalización domiciliaria
 - puede utilizar tecnologías de información y comunicación con el mismo alcance clínico del médico de Atención Directa
 - el mismo profesional de Atención Directa puede cumplir esta función
 - **Enfermero(a) clínico**
 - experiencia mínima: `2` años de experiencia clínica
 - requisito adicional: curso vigente de soporte vital básico
 - funciones:
 - participar en evaluación de pacientes hospitalizados para gestionar ingreso y egreso
 - evaluar pacientes durante visita con instrumentos acordes para visualizar evolución y flujos de derivación
 - gestionar cuidados mediante plan de cuidados de enfermería y ejecución del plan terapéutico según complejidad
 - educar a paciente, familia y/o cuidadores sobre plan terapéutico y autocuidado
 - cumplir otras labores encomendadas por coordinación o Dirección Técnica
 - **Kinesiólogo(a)**
 - experiencia mínima: `2` años de experiencia clínica
 - requisito adicional: curso vigente de soporte vital básico
 - función: otorgar terapias motoras y respiratorias
 - **Auxiliar paramédico de enfermería, técnico de nivel medio de enfermería o técnico de nivel superior de enfermería**
 - experiencia mínima: `1` año de experiencia clínica
 - requisito adicional: curso vigente de soporte vital básico
 - funciones definidas por enfermería clínica dentro de su competencia; debe cumplir plan de cuidados y plan terapéutico
 - **Trabajador(a) social**
 - funciones:
 - elaborar informe de diagnóstico social del hogar, vivienda, servicios sanitarios básicos, acceso a telefonía y accesos viales
 - verificar disponibilidad de cuidador o tutor legal
 - evaluar situación económica del grupo familiar
 - confeccionar informe y seguimiento de evaluación e intervención social
 - elaborar informe social
 - colaborar en gestión y coordinación de derivaciones y participar en reuniones del equipo clínico
- Personal administrativo y auxiliar:
 - cumple las actividades que establezca Dirección Técnica
 - el establecimiento puede contar con otros profesionales y técnicos según prestaciones brindadas al paciente y su familia
- Control documental:
 - debe mantenerse actualizado y a disposición de la `SEREMI` el listado de todo el personal y los antecedentes que acrediten su habilitación profesional o técnica

## Requisitos de ingreso, causales de egreso y exclusiones

- Arts. 15-17.

### Requisitos de ingreso

| Condición | Exigencia |
| --- | --- |
| Situación clínica | Patología aguda o crónica reagudizada, clínicamente estable y susceptible de tratamiento en domicilio o adecuación del esfuerzo terapéutico. |
| Residencia | Condiciones sanitarias mínimas, servicios básicos y telefonía, dentro del radio de cobertura. |
| Apoyo | Red de apoyo familiar, social o tutor responsable a cargo del cuidado. |
| Consentimiento | Aceptación escrita e informada del paciente, tutor o familiar. |

### Causales de egreso

- Alta médica por recuperación del cuadro clínico.
- Cumplimiento del plan terapéutico y de cuidados.
- Reingreso hospitalario programado por inestabilidad del cuadro clínico y complicaciones.
- Fallecimiento.
- Renuncia voluntaria del paciente o de quien lo represente.
- Alta disciplinaria determinada por Dirección Técnica si concurre alguna de estas circunstancias:
 - no adherencia al tratamiento o indicaciones por tutor o cuidador
 - conductas irrespetuosas hacia el personal
 - falta de respuesta o rechazo a visitas domiciliarias

### Exclusiones

- No pueden recibir prestaciones de hospitalización domiciliaria pacientes con:
 - inestabilidad clínica o ausencia de diagnóstico establecido
 - patología de salud mental descompensada
 - necesidad de prestación no incluida en el listado del establecimiento
 - alguna condición de alta disciplinaria del art. 16 letra f)

## Infraestructura, registros, confidencialidad, fiscalización y vigencia

- Arts. 18-25.
- La norma técnica del Ministerio de Salud regula condiciones mínimas de:
 - personal
 - infraestructura
 - equipamiento
 - registros
 - procedimientos técnicos
 - protocolos u otros
 - requisitos y condiciones de traslado del equipamiento y del personal
 - medidas de seguridad
- Dependencias administrativas u oficina central:
 - sistema telefónico o radial disponible `24/7`, con grabación continua o registro manual/protocolo de atención de llamados
 - soporte informático e internet
 - respaldo de energía eléctrica autorizado por la `SEC`
 - área administrativa para archivos, fichas clínicas y antecedentes de pacientes en forma segura
 - bodegas para equipamiento, insumos clínicos, productos farmacéuticos o medicamentos con condiciones que mantengan características e integridad; termolábiles en refrigeradores con temperatura controlada y registro
 - acceso a servicios de alimentación, servicios higiénicos con ducha, casilleros y sala de guardarropía/estar para personal de turno
 - área cerrada para disposición transitoria de residuos según normativa vigente y plan de manejo
 - protocolo y flujo de desecho de cortopunzantes
 - estacionamiento para vehículos de traslado del equipo de salud o pacientes
 - norma de señalización y vías de evacuación
 - recinto de depósito de material de aseo
- Equipamiento:
 - el establecimiento debe disponer de equipos, instrumentos, aparatos, dispositivos y otros elementos de uso médico necesarios para diagnóstico y tratamiento adecuados, en especial los vinculados a mantención de funciones vitales y monitoreo permanente
- Registros formales mínimos:
 - criterios de ingreso y egreso
 - acciones en caso de fallecimiento
 - encuesta de satisfacción usuaria al egreso
 - consentimiento informado
 - constancias de entrega de carta de derechos y deberes
 - formulario de ingreso
 - descripción del proceso asistencial con todas las atenciones del paciente
 - plan de cuidados acorde a necesidades de la persona
 - epicrisis al alta
- Entrega de información:
 - debe existir documento para el paciente o su representante con indicaciones de cuidados e indicaciones para emergencias o episodios que afecten continuidad de la atención
- Confidencialidad:
 - si el registro manual o electrónico contiene información de salud considerada dato sensible, debe resguardarse confidencialidad y reserva
 - el tratamiento solo procede cuando la ley lo autorice expresamente y en los casos previstos por el ordenamiento vigente
- Fiscalización y sanción:
 - la `SEREMI` del lugar donde se ubica el establecimiento fiscaliza y controla sus actividades
 - las contravenciones se sancionan según el `Libro X` del Código Sanitario
- Vigencia:
 - el reglamento entra en vigencia con su publicación en el Diario Oficial
 - establecimientos, prestadores, unidades o servicios que ya prestaban hospitalización domiciliaria al entrar en vigencia deben ajustar sus procedimientos en un plazo de `6` meses desde la publicación
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="959ec6963b3630da">>>
</file>
assistant: [[reply_to_current]] Perfecto. Con esto ya puedo incorporar la capa normativa formal y cruzarla con el modelo OPM y el modelo categorial para pasar de intuición a diseño exigible. Voy a cerrar ahora un primer mapa normativo de usuarios y capacidades obligatorias del sistema.
assistant: [[reply_to_current]] Síntesis: con la normativa ya aparece algo decisivo, el sistema no puede diseñarse solo como ficha clínica más agenda, porque en HODOM es a la vez sistema asistencial, sistema regulatorio y sistema logístico. Si eso no se integra desde el inicio, se rompe la operación o se incumple la norma.

Artefacto principal: evaluación inicial de usuarios normativos y capacidades obligatorias del sistema HODOM San Carlos

Tensión dominante
El sistema debe sostener simultáneamente:
1. atención clínica segura en domicilio,
2. continuidad asistencial y telemática,
3. trazabilidad regulatoria ante SEREMI y MINSAL,
4. operación diaria de rutas, insumos, turnos y cupos.

Usuarios del sistema, primera versión ya bastante firme

A. Usuarios clínico-asistenciales obligatorios
1. Director técnico
- no es solo un jefe, es un actor regulado
- necesita aprobar manuales, protocolos, turnos, trazabilidad clínica, calidad, IAAS, stock, mantención, coordinación con derivadores y reingresos
- el sistema debe darle vista de cumplimiento, auditoría, incidentes, mortalidad, capacidad y documentación vigente

2. Coordinación HODOM
- actor central del sistema
- supervisa procesos clínicos, registros, continuidad asistencial, personal, insumos, mantenciones, inducción y capacitación
- necesita tablero operativo completo: pacientes activos, carga por profesional, rutas, alertas, cobertura, documentación faltante, contingencias

3. Médico de atención directa
- evalúa ingreso y egreso, indica tratamiento, supervisa atención, refuerza indicaciones, coordina continuidad
- necesita ficha clínica longitudinal, evolución, plan terapéutico, teleatención, órdenes, egreso, epicrisis, reingreso y contrarreferencia

4. Médico regulador
- la norma lo reconoce explícitamente
- puede hacer atención a distancia o directa
- necesita módulo de regulación/telemedicina, registro de llamados, triage, indicaciones remotas, escalamiento y coordinación de reingreso

5. Enfermero/a clínico
- participa en ingreso/egreso, evalúa evolución, gestiona plan de cuidados, educa al paciente/cuidador
- necesita registro clínico diario estructurado, plan de cuidados, signos vitales, invasivos, educación, adherencia, alertas y handoff

6. Kinesiólogo/a
- terapias motoras y respiratorias
- necesita evaluación funcional, objetivos terapéuticos, sesiones, evolución, escalas, programación y eventualmente teleseguimiento

7. TENS / auxiliar paramédico / técnico
- ejecuta cuidados definidos por enfermería dentro de su competencia
- necesita tareas asignadas, validación de ejecución, administración/registro de procedimientos, checklists y reportes de incidente

8. Trabajador/a social
- actor normativo, no accesorio
- evalúa hogar, servicios básicos, telefonía, accesos viales, cuidador, situación económica
- necesita evaluación social estructurada, verificación de elegibilidad domiciliaria, red de apoyo, seguimiento social y coordinación con red externa

B. Usuarios operativos y administrativos
9. Personal administrativo
- la norma lo reconoce para funciones definidas por Dirección Técnica
- necesita admisión, documentación, consentimientos, archivo, agenda, coordinación, reportabilidad, control documental y soporte a REM

10. Operador logístico / despacho / programación
- aunque no siempre aparezca como cargo clínico formal, la operación normativa exige rutas, visitas, vehículos, traslados y seguridad
- necesita programación diaria, georreferenciación, optimización de rutas, control de móvil, contingencias, tiempos y reasignación dinámica

11. Bodega / farmacia / abastecimiento
- la norma exige stock, condiciones de almacenamiento, cadena de frío y trazabilidad
- necesita inventario, reservas por paciente, control de temperatura, despacho y reposición

12. Encargado de calidad / IAAS / capacitación
- puede coincidir con coordinación o DT, pero funcionalmente es usuario
- necesita evidencias de capacitación, vigencias, IAAS, incidentes, auditoría y protocolos

C. Usuarios externos co-operantes
13. Paciente
- no es un objeto pasivo; necesita ver plan, visitas, indicaciones, señales de alarma, consentimiento, contacto y eventualmente teleatención

14. Cuidador / tutor / familiar responsable
- es un actor crítico de elegibilidad y continuidad
- necesita indicaciones, educación, confirmación de visitas, registro de incidencias, aceptación/rechazo, contacto y apoyo para emergencias

15. Equipo derivador hospitalario
- necesita derivar, adjuntar antecedentes, coordinar ingreso, recibir retroalimentación y reingresos

16. APS / CESFAM
- necesita contrarreferencia, continuidad post egreso, información clínica pertinente y articulación territorial

17. SEREMI / fiscalización / auditoría
- no opera el día a día, pero el sistema debe servirle evidencia
- por eso es usuario indirecto de auditoría y cumplimiento

Capacidades del sistema que ya quedan normativamente obligadas

1. Gestión de elegibilidad e ingreso
- criterios clínicos
- condiciones del domicilio
- red de apoyo / cuidador
- consentimiento informado
- exclusiones
- formulario de ingreso
- carta de derechos y deberes

2. Ficha clínica y registro formal
- ficha clínica física o electrónica conforme a DS 41
- resumen clínico domiciliario disponible para emergencias
- registro integral del proceso asistencial
- plan de cuidados
- epicrisis
- encuesta de satisfacción
- acciones ante fallecimiento

3. Telesalud y regulación remota
- la norma permite uso de TIC por médico de atención directa y regulador, y eventualmente otros profesionales designados
- el sistema debe registrar quién atendió, cuándo, por qué medio, qué evaluación hizo, qué indicó y qué escalamiento definió
- no basta videollamada, debe quedar como acto clínico trazable

4. Operación diaria y logística
- programación de rutas y visitas
- turnos
- gestión de vehículos
- trazabilidad de llamadas 24/7
- contingencias y respaldo eléctrico/operacional
- monitoreo de cobertura y oportunidad

5. Gestión de insumos, equipos y medicamentos
- stock
- bodega
- termolábiles
- cadena de frío
- mantención preventiva
- disponibilidad por cartera de prestaciones

6. Gobernanza documental
- manual de organización interna
- protocolos clínicos
- manual de procedimientos
- manejo de residuos
- PAC
- control de vigencia, aprobación y versión

7. Cumplimiento y auditoría
- habilitación del personal
- cursos vigentes
- inducción 44 horas
- IAAS
- RCP
- certificaciones
- evidencia para fiscalización

Implicancias de diseño que ya son inevitables
1. El cuidador debe modelarse como actor de sistema, no solo como dato del paciente.
2. La teleatención debe ser un tipo formal de encuentro clínico, no una nota libre.
3. El sistema debe unir clínica + logística + compliance en un mismo episodio.
4. La unidad primaria del sistema debe ser el episodio de hospitalización domiciliaria, no solo el paciente.
5. Debe existir un plano de auditoría fuerte: quién hizo qué, cuándo, bajo qué rol y con qué respaldo normativo.

Alertas y tensiones detectadas
1. La norma técnica trae una inconsistencia interna sobre Coordinación:
- texto general: IAAS 80 horas
- tabla: RCP 3 horas
Mi recomendación es diseñar el sistema para soportar ambas evidencias y marcar la exigencia como “requiere validación normativa oficial”, no asumir una sola.

2. El reglamento exige telefonía/radio 24/7 y trazabilidad de llamados.
- eso obliga a un módulo de llamadas/incidentes, aunque hoy la operación real use planillas o WhatsApp.

3. Hay una diferencia importante entre “atención domiciliaria” ambulatoria y “hospitalización domiciliaria”.
- el sistema debe evitar mezclar ambos flujos, porque normativamente no son lo mismo.

Recomendación concreta
El primer entregable grande ya debería estructurarse así:
1. mapa de usuarios del sistema,
2. capacidades por usuario,
3. historias de usuario por macroproceso,
4. módulos del sistema,
5. matriz de trazabilidad normativa por módulo.

Siguiente paso claro
Pásame ahora, idealmente en este orden:
1. el ERD integrado,
2. FHIR_R4_Resource_References,
3. el repositorio legacy o sus artefactos más representativos.

Con eso te devuelvo la versión 1 del diseño del sistema operativo HODOM San Carlos, ya no preliminar sino estructurada por usuarios, módulos e historias de usuario.
user: [media attached: 6 files]
[media attached 1/6: media/inbound/RUTAS---c98c3c4d-f852-43af-a233-8f5830cd34e7.zip (application/zip) | media/inbound/RUTAS---c98c3c4d-f852-43af-a233-8f5830cd34e7.zip]
[media attached 2/6: /home/felix/.openclaw/media/inbound/REGISTRO_DIARIO_PACIENTES_HODOM---7d1c01dc-072e-4cb5-8813-38dc02475838.zip (application/zip) | /home/felix/.openclaw/media/inbound/REGISTRO_DIARIO_PACIENTES_HODOM---7d1c01dc-072e-4cb5-8813-38dc02475838.zip]
[media attached 3/6: media/inbound/PROGRAMACIO_N_2026---93363d95-68b5-497d-82ec-b119ad51c306.xlsx (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet) | media/inbound/PROGRAMACIO_N_2026---93363d95-68b5-497d-82ec-b119ad51c306.xlsx]
[media attached 4/6: media/inbound/HODOM_2025---7644d273-31ad-4bfb-b641-bd165837f4e0.zip (application/zip) | media/inbound/HODOM_2025---7644d273-31ad-4bfb-b641-bd165837f4e0.zip]
[media attached 5/6: media/inbound/ENTREGA_KINE---65ac1bce-1248-4354-9543-20655a92cc43.zip (application/zip) | media/inbound/ENTREGA_KINE---65ac1bce-1248-4354-9543-20655a92cc43.zip]
[media attached 6/6: media/inbound/2025_PROGRAMACIO_N---6d8c98a7-c536-49fa-a799-f0c16ff4db60.xlsx (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet) | media/inbound/2025_PROGRAMACIO_N---6d8c98a7-c536-49fa-a799-f0c16ff4db60.xlsx]
To send an image back, prefer the message tool (media/path/filePath). If you must inline, use MEDIA:https://example.com/image.jpg (spaces ok, quote if needed) or a safe relative path like MEDIA:./image.jpg. Avoid absolute paths (MEDIA:/...) and ~ paths - they are blocked for security. Keep caption in the text body.
Conversation info (untrusted metadata):
```json
{
  "message_id": "859",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-04-07 06:02 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

<media:document>
assistant: [[reply_to_current]] Síntesis: estos archivos ya me sirven para confirmar la capa operativa real del servicio, aunque hay una limitación técnica importante, aquí puedo leer texto e imágenes, pero los `.zip` y `.xlsx` entran como binario y no se pueden inspeccionar bien sin extraerlos.

Aun así, por nombre y contexto, ya queda confirmado que el sistema HODOM no es solo clínico, sino al menos cinco sistemas acoplados:
1. programación diaria,
2. ruteo/logística,
3. registro diario de pacientes,
4. handoff/entrega de turno,
5. histórico operativo anual del programa.

Eso refuerza algo clave: los usuarios del sistema no pueden modelarse solo como “profesionales clínicos”. Hay, como mínimo, estos grupos funcionales:

1. conducción y cumplimiento
- director técnico
- coordinación HODOM
- encargado de calidad / IAAS / capacitación

2. atención clínica directa
- médico atención directa
- médico regulador / telemático
- enfermero clínico
- TENS
- kinesiólogo
- fonoaudiólogo
- trabajador social

3. operación diaria
- programador de visitas
- despachador / coordinador logístico
- conductor / móvil
- bodega / farmacia / abastecimiento
- administrativo documental

4. red externa y continuidad
- equipo derivador hospitalario
- APS / CESFAM
- paciente
- cuidador / tutor

5. fiscalización y reporte
- SEREMI / auditoría
- REM / estadísticas / gestión

Y los módulos del sistema, ya en versión bastante firme, serían:
- admisión y elegibilidad
- episodio HODOM
- ficha clínica digital
- plan terapéutico y plan de cuidados
- teleatención y regulación remota
- programación diaria
- rutas y optimización dinámica
- registro de visitas y procedimientos
- entrega de turno
- insumos, medicamentos y equipamiento
- egreso, epicrisis y contrarreferencia
- cumplimiento normativo y trazabilidad
- analítica operativa y REM

Bloqueo real
Para sacar de estos archivos las historias de usuario correctas, necesito ver contenido estructurado, no solo el nombre del archivo.

Lo mínimo que te pediría ahora, para no hacerte perder tiempo, es esto:
1. del `PROGRAMACIÓN 2026` y `2025 PROGRAMACIÓN`, envíame:
- nombres de hojas
- encabezados de cada hoja
- idealmente exportados a CSV o markdown

2. de los `.zip`, envíame:
- listado de archivos internos
- y 1 a 3 archivos representativos extraídos por paquete, en texto, CSV, XLSX exportado a CSV o markdown

Prioridad sugerida
1. REGISTRO_DIARIO_PACIENTES_HODOM
2. PROGRAMACIÓN 2026
3. RUTAS
4. ENTREGA_KINE
5. HODOM_2025

Si quieres, en paralelo a eso yo ya puedo empezar a redactarte la “versión 1 del mapa de usuarios y historias de usuario” basada en normativa + OPM + modelo categorial + estos subdominios operativos confirmados.
