---
_manifest:
  urn: urn:tde:kb:decreto-12-interoperabilidad
  provenance:
    source: https://wikiguias.digital.gob.cl/Normas/Decreto12
version: 1.0.0
status: published
tags:
- tde
- lineamientos-normas
- decreto
- norma-tecnica
- interoperabilidad
- nodo
- gestor-de-codigos
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:decreto-12-interoperabilidad
---

# Decreto 12 — Norma Técnica de Interoperabilidad

> Promulgación: 19-MAY-2023 | Publicación: 17-AGO-2023 | Versión: Única

## Encabezado

**Bases legales:**

| Instrumento | Materia |
|-------------|---------|
| DS Nº 100/2005 SEGPRES (CPR arts. 32 Nº6 y 35) | Constitución Política |
| Ley Nº 19.880 | Bases procedimientos administrativos |
| Ley Nº 18.993 | Crea MINSEGPRES |
| Ley Nº 19.628 | Protección de la vida privada |
| Ley Nº 21.180 | Transformación Digital del Estado |
| DFL Nº 1/2020 MINSEGPRES | Gradualidad implementación ley 21.180 |
| DS Nº 4/2020 MINSEGPRES | Reglamento medios electrónicos (en adelante "el Reglamento") |
| Ley Nº 19.799 | Documentos electrónicos y firma electrónica |
| DS Nº 181/2002 Economía | Reglamento ley 19.799 |
| DS Nº 14/2014 Economía | Modifica DS 181/2002 |
| Resolución Nº 7/2019 CGR | Exención toma de razón |

**Considerando (síntesis):** Ley 21.180 requiere que los medios electrónicos del Estado interactúen entre sí. Mesa Técnica de Interoperabilidad con CGR, DIPRES, SRCeI, SUSESO, CPLT, SII, Tesorería, Desarrollo Social, Hacienda, FONASA y Gobierno Digital. Consulta ciudadana dic. 2021. DS anterior (Nº 5/2022) retirado en abr. 2022 para revisión. [→ Artículo 27]

---

## Disposiciones generales

### Artículo 1 — Objeto

Definir los **estándares, protocolos y herramientas** para que los órganos de la Administración del Estado **interoperen datos, documentos y expedientes electrónicos**.

### Artículo 2 — Definiciones

| Término | Definición |
|---------|-----------|
| **Código** | Secuencia de símbolos que identifican unívocamente un objeto, entidad o estado. |
| **Consumidor de Servicios de Interoperabilidad** | Órgano que demanda un servicio de interoperabilidad a otro para intercambiar un dato, documento o expediente electrónico. |
| **Dato** | Representación de un atributo o variable (letras, números o símbolos), capturable por observación o medición. |
| **Dato Abierto** | Dato digital con características técnicas y jurídicas para ser usado, reutilizado y redistribuido libremente. |
| **Dato Digital** | Dato representado en variables discretas (bits), tratable por dispositivos o sistemas (art. 2 lit. o) ley Nº 19.628). |
| **Endpoints** | Dirección URI de un servicio web para recibir o enviar información. |
| **Interoperar** | Operación que permite a dos órganos, conectados por un nodo, intercambiar o transmitir datos, documentos o expedientes electrónicos. |
| **Metadatos** | Datos que describen el contexto, contenido y estructura de un dato. |
| **Plataforma Electrónica** | Software, datos e infraestructura tecnológica que sustenta procesos o procedimientos. |
| **Protocolo de Comunicación** | Conjunto de reglas y estándares que determinan cómo se transmiten los datos en la red de interoperabilidad. |
| **Proveedor de Servicios de Interoperabilidad** | Órgano al que se demanda un servicio de interoperabilidad por parte de otro. |
| **Reglamento** | DS Nº 4/2020 MINSEGPRES. |
| **Servicios de Interoperabilidad** | Servicios informáticos automatizados que permiten la interoperabilidad de datos, documentos o expedientes entre consumidores y proveedores mediante un nodo validado. |
| **Transacción** | Instancia completa de comunicación entre consumidor y proveedor: envío de consulta → recepción → respuesta del proveedor → recepción de la respuesta. |
| **Token** | Secuencia de caracteres vinculada a información que se desea proteger, usada como credencial de autenticación, identificador de sesión y de transacción. |
| **URI** | Medio simple y extensible de identificar un recurso en internet (Uniform Resource Identifier). |

---

## Artículo 3 — Red de interoperabilidad

La **red de interoperabilidad** consiste en un conjunto de conexiones directas y seguras a través de internet, basadas en **nodos de interoperabilidad** alojados en la infraestructura de los órganos, que actuando como proveedores y/o consumidores permiten el intercambio de datos, documentos y expedientes electrónicos (arts. 16 bis, 17 lit. d), 19 y 24 bis ley Nº 19.880; y Título VII del Reglamento). La trazabilidad, registros y autorizaciones de acceso se almacenan centralizadamente mediante comunicación obligatoria de las plataformas con los **servicios centralizados de interoperabilidad**.

## Artículo 4 — Componentes de la red de interoperabilidad

| Nº | Componente |
|----|-----------|
| 1 | Nodos de interoperabilidad |
| 2 | Servicios centralizados de interoperabilidad |
| 3 | Herramientas complementarias: Gestor de Códigos del Estado y Catálogo de Elementos transmisibles |
| 4 | Elementos transmisibles en la red |

> Los componentes 1, 2 y 3 son dispuestos por la División de Gobierno Digital del MINSEGPRES a todos los órganos.

## Artículo 5 — Forma de integrarse a la red de interoperabilidad

Los órganos deberán integrarse a la red actuando como **proveedores y/o consumidores**, a través de nodos de interoperabilidad conectados a los servicios centralizados de interoperabilidad.

---

## Artículo 6 — Requisitos de un nodo de interoperabilidad

El **nodo de interoperabilidad** es un componente de software alojado en la infraestructura del órgano, que le permite integrarse a la red con los estándares y protocolos de esta norma. La División de Gobierno Digital pondrá a disposición un nodo estándar; cada órgano podrá optar por desarrollar uno propio.

Todo nodo deberá cumplir al menos:

1. Establecer conexión segura entre órganos (→ guía técnica, Artículo 27; y Norma Técnica de Seguridad, art. 57 Reglamento).
2. Enviar y recibir datos, documentos y expedientes electrónicos entre órganos de la red.
3. Permitir la recepción y envío de mensajes entre órganos integrantes de la red.
4. Conectarse directamente a otro nodo y a los servicios centralizados, registrando trazabilidad de entrada/salida de mensajes.
5. Conectarse y comunicarse con el Gestor de Autorizaciones.
6. Ser la **única vía de acceso** a los servicios de interoperabilidad (enlace entre el Catálogo de Servicios y los órganos).
7. Encriptar mensajes y respuestas (métodos según guía técnica → Artículo 27).
8. Validar el certificado de autenticación del nodo consumidor.
9. Auto-monitorear sus propias operaciones (→ guía técnica, Artículo 27).
10. Utilizar protocolos autorizados por la División de Gobierno Digital (→ guía técnica, Artículo 27).

> Un órgano puede tener uno o más nodos según su arquitectura tecnológica. La comunicación del nodo con los sistemas internos es responsabilidad de cada órgano.

---

## Artículo 7 — Servicios centralizados de interoperabilidad

Los **servicios centralizados** son el conjunto de herramientas de software e infraestructura que habilitan: Catálogo de Servicios, Registro de Trazabilidad, Directorio de Datos, Catálogo de Esquemas, Gestor de Acuerdos y Gestor de Autorizaciones; junto con la infraestructura que almacena los metadatos de cada transacción. Validan permisos de acceso entregando tokens y endpoints a los nodos. Son desarrollados por la División de Gobierno Digital del MINSEGPRES. Los órganos designarán funcionarios(as) responsables de mantener actualizada la información de cada servicio.

## Artículo 8 — Catálogo de Servicios de Interoperabilidad

Componente de software que lista los datos, documentos y expedientes electrónicos que los órganos proveen para intercambio en la red. Los órganos deberán **publicar todos los servicios bajo su administración** en el Catálogo. Cada servicio debe tener un código unívoco (del Gestor de Códigos del Estado) y vincularse con el Catálogo de Procedimientos Administrativos y Trámites.

Por cada servicio publicado, los órganos deben:
1. Describir datos de entrada y salida.
2. Indicar si requiere esquema aprobado del Catálogo de Esquemas.
3. Designar un(a) funcionario(a) responsable de su gestión y disponibilidad.
4. Indicar transacciones por segundo (TPS) que podrá entregar.
5. Señalar el porcentaje de acuerdo de nivel de servicio (ANS).

> La primera carga la efectúa la División de Gobierno Digital. La incorporación de nuevos servicios y las actualizaciones son responsabilidad de cada órgano (→ guía técnica, Artículo 27).

## Artículo 9 — Registro de Trazabilidad

Componente de software que almacena la información de cada transacción para registrar y validar operaciones de procedimientos administrativos. Los nodos enviarán el registro a los servicios centralizados **de manera paralela e inmediata** al envío de la consulta o respuesta. En casos de interrupción, alto volumen o fuerza mayor, se permite envío diferido por paquetes dentro de las **48 horas** siguientes a la primera transacción del paquete.

Cada nodo debe registrar:
1. Plataforma o servicio web a través del cual se solicitan/reciben los datos.
2. Órgano requirente, funcionario(a) responsable, órgano destinatario, procedimiento, gestión encargada y plazo (art. 9 ley Nº 19.880).
3. Marca de tiempo en **UTC+00:00** (sincronizada con el Servicio Hidrográfico y Oceanográfico de la Armada).
4. Para datos sensibles: RUN del(de la) interesado(a), autorización del(de la) interesado(a) y funcionario(a) responsable (art. 24 bis ley Nº 19.880).
5. Tipo de respuesta (error o transacción exitosa).
6. Nombre y código del órgano proveedor.
7. Nombre y código del órgano consumidor.

## Artículo 10 — Directorio de Datos

Servicio centralizado que exhibe los datos disponibles en el Catálogo de Servicios, con descripción, atributos y funcionario(a) responsable. Permite buscar e identificar datos administrados por otros órganos. Todos los datos expuestos en un servicio publicado deben publicarse en el Directorio. Los órganos deberán hacer un **catastro de los datos que administran** según sus competencias y mantenerlos publicados y actualizados. Para solicitar un dato publicado: el órgano consumidor lo solicita al proveedor mediante el Catálogo de Servicios. Para datos sensibles: requiere además la autorización del(de la) interesado(a) mediante el **Gestor de Autorizaciones**.

## Artículo 11 — Catálogo de Esquemas

El **Catálogo de Esquemas** gestiona el listado de esquemas aprobados para interoperar. Un **esquema basal** define un dato atómico o pequeño conjunto de datos relacionados. Un **esquema documental** define un conjunto de datos que componen un documento (compuesto de esquemas basales). La primera carga la efectúa la División de Gobierno Digital; las actualizaciones son responsabilidad de cada órgano que ofrezca servicios (→ procedimiento en guía técnica, Artículo 27). Cambios de funcionario(a) responsable: plazo máximo **3 días** para actualizar. Nuevos esquemas requieren **visación de la División de Gobierno Digital**. Esquemas con errores sintácticos o incompatibles serán rechazados hasta que el órgano subsane el error.

## Artículo 12 — Gestor de Acuerdos

Servicio centralizado que facilita la solicitud de un servicio de interoperabilidad entre consumidor y proveedor, habilitando la conexión y definiendo niveles de servicio mediante **términos y condiciones** o convenios tipo. Aplica a datos y servicios del Directorio de Datos o Catálogo de Servicios. No aplica para datos abiertos. Los acuerdos pueden ser para: (a) uso de un servicio, (b) interoperar un dato una única vez, o (c) acceso permanente a un servicio. **Solo se pueden celebrar acuerdos por medio del Gestor de Acuerdos.** Cada órgano debe autoevaluar la cantidad de TPS que podrá realizar y establecer su ANS.

## Artículo 13 — Tramitación de solicitudes de acuerdo

La solicitud debe ser efectuada por el(la) **Jefe(a) de la Unidad de Tecnologías** del órgano consumidor (o quien cumpla esas funciones), con visto bueno del área jurídica. Cuando corresponda, se debe adjuntar la ley que da origen al procedimiento administrativo. La solicitud se envía al órgano proveedor vía Gestor de Acuerdos, con aviso automático a la División de Gobierno Digital.

Plazos:
- **15 días hábiles** para que el proveedor responda (aceptando o denegando).
- Extensible hasta **5 días hábiles adicionales** si el proveedor lo requiere.
- La **negativa debe ser siempre justificada**.

La División de Gobierno Digital **mediará** en caso de negativa, analizando argumentos técnicos y legales. En caso de **negativa injustificada o fuera de plazo**, la División tomará la decisión por sí. En caso de **falta de capacidad manifiesta** (pocos funcionarios TI, infraestructura limitada, presupuesto insuficiente u otra circunstancia fundada): la División presta apoyo técnico y el proveedor debe incluir la mejora en su Plan de Mejora Continua (→ Norma Técnica de Calidad y Funcionamiento, art. 57 Reglamento). Aprobada la solicitud, los(as) Jefes(as) Superiores de Servicio suscriben el acuerdo en la plataforma **con firma electrónica avanzada**.

## Artículo 14 — Gestor de Autorizaciones

Permite a las **personas naturales interesadas** en un procedimiento administrativo:
1. Ver el historial de autorizaciones de tratamiento de datos otorgadas (verificable: quién, cuándo, cómo, para qué procedimiento, qué datos sensibles).
2. **Revocar** cualquiera de las autorizaciones otorgadas.
3. **No otorgar** el consentimiento.

La autorización se presta integrada a **Clave Única** (art. 30 lit. f) ley Nº 19.880). El consentimiento aplica a toda gestión del procedimiento hasta su tramitación total y debe incorporarse como documento al expediente electrónico, siendo preservado por el órgano. La revocación **no tiene efecto retroactivo** sobre gestiones ya realizadas.

## Artículo 15 — Requisitos del consentimiento

El consentimiento debe:

1. Prestarse por el(la) mismo(a) interesado(a), su apoderado(a) o representante legal.
2. Otorgarse **por escrito**.
3. Ser un **acto afirmativo claro** (solo mediante el Gestor de Autorizaciones; excepto interesados(as) autorizados para soporte papel).
4. Ser **libre**: el(la) interesado(a) no puede ser obligado(a) a otorgarlo. El procedimiento **nunca termina** por la sola negativa del consentimiento.
5. Ser **específico, informado e inequívoco**: informar en lenguaje simple y claro el propósito, especificando que aplica al procedimiento hasta su total tramitación.
6. Ser **esencialmente revocable**: el(la) interesado(a) puede revocar en cualquier momento sin perder el derecho a ejercer el procedimiento. El procedimiento **nunca termina** por la revocación.

> En caso de negativa o revocación, el(la) interesado(a) deberá aportar por sí todos los documentos e información necesarios. La revocación no aplica retroactivamente a gestiones ya realizadas.

---

## Artículo 16 — Herramientas complementarias

Son herramientas complementarias el **Gestor de Códigos del Estado** y el **Catálogo de Procedimientos Administrativos y Trámites**, gestionadas por la División de Gobierno Digital del MINSEGPRES. Los órganos son responsables de mantener actualizada la información en ellas.

## Artículo 17 — Gestor de Códigos del Estado

Componente de software que gestiona los **códigos estandarizados** asignados a órganos del Estado, procedimientos administrativos, nombres territoriales, entre otras dimensiones. Permite a cada órgano:

1. Visualizar los códigos estandarizados disponibles.
2. Gestionar sus propios códigos internos con metadatos.
3. Acceder a equivalencias de códigos utilizados por otros órganos.
4. Incorporar nuevas categorías de códigos con metadatos y relaciones con categorías existentes.

## Artículo 18 — Catálogo de Procedimientos Administrativos y Trámites

Nómina de procedimientos administrativos y trámites identificados por los órganos, para su codificación, estandarización y caracterización. Cada órgano deberá identificar sus procedimientos especificando al menos:

1. Nombre, ley de origen y código unívoco del procedimiento o trámite.
2. Si requiere o no interoperar datos, documentos o expedientes de otro órgano.
3. En caso de requerir interoperabilidad: el vínculo con el Directorio de Datos y el Catálogo de Servicios necesarios.
4. Si se requiere activar el Gestor de Autorizaciones (datos sensibles).
5. Mecanismo de contacto para el(la) interesado(a) sobre dudas del procedimiento o trámite.

---

## Artículo 19 — Elementos transmisibles

Los proveedores deben transmitir por medio del nodo los **datos y documentos de su competencia** necesarios para el conocimiento o resolución de un procedimiento administrativo del órgano consumidor. Los documentos deben estar descritos conforme a un esquema documental (→ Artículo 11). Deben transmitirse:
- Datos personales de los(as) interesados(as).
- Otros datos relevantes para la tramitación.
- Documentos y expedientes electrónicos necesarios (arts. 17 lit. d) y 24 bis ley Nº 19.880).
- Otros elementos no personales pero relevantes para la tramitación.

> Los **datos abiertos** son consumidos directamente por los órganos sin pasar por la red de interoperabilidad. Los documentos públicos deben publicarse en portales conforme a la ley Nº 20.285.

## Artículo 20 — Clasificación de datos

Conforme al Directorio de Datos (→ Artículo 10), cada órgano deberá **clasificar los datos** que gestione en: personales, sensibles, estadísticos, secretos, reservados u otros, según la ley Nº 19.628 y la normativa vigente aplicable.

---

## Artículo 21 — De la coordinación de interoperabilidad

Se establecen reglas de gestión de la interoperabilidad articuladas en **comités por niveles**, en virtud de los principios de eficiencia, eficacia, coordinación (principio de interoperabilidad, art. 16 bis ley Nº 19.880).

## Artículo 22 — Niveles de coordinación

Los niveles son: **primer nivel** (institucional), **segundo nivel** (sectorial) y **tercer nivel** (estratégico).

## Artículo 23 — Primer nivel o nivel institucional

Coordinado por la División de Gobierno Digital del MINSEGPRES con representantes de los órganos. Resuelve los **problemas operativos** que se presenten al interoperar, salvo aquellos que correspondan a comités sectoriales.

## Artículo 24 — Segundo nivel o nivel sectorial

Existirán tantos **comités sectoriales** como sectores económicos y sociales requieran coordinarse, para coordinar estándares, codificaciones y esquemas de cada sector. La División de Gobierno Digital apoyará cada comité.

## Artículo 25 — Tercer nivel o nivel estratégico

**Comité Estratégico**: coordina, valida y aprueba estándares, protocolos, codificaciones, esquemas y cualquier materia que garantice el adecuado funcionamiento de la red. Su composición se determina por acto administrativo del MINSEGPRES. Es presidido por el(la) Jefe(a) de la División de Gobierno Digital. Funciones: asesoría técnica para validar propuestas sectoriales; resolución de discrepancias entre órganos; sugerencia de datos, esquemas y metadatos basales transversales.

## Artículo 26 — Rol de la División de Gobierno Digital

Conforme al art. 9A ley Nº 18.993, la División de Gobierno Digital apoya la coordinación estratégica de interoperabilidad mediante: guías técnicas, propuestas de estándares, esquemas y códigos; asesoría a los órganos para la implementación de la red; y convocatoria de instancias de coordinación transversales o sectoriales.

---

## Disposiciones finales

### Artículo 27 — Guía técnica

La División de Gobierno Digital del MINSEGPRES dictará una o más **Guías Técnicas de Interoperabilidad** con los aspectos operativos y procesos de implementación de esta norma.

### Artículo 28 — Gradualidad

La aplicación es acorde a la gradualidad del DFL Nº 1/2020 MINSEGPRES. La División de Gobierno Digital definirá los lineamientos y formato de cumplimiento para los órganos obligados.

### Artículo 29 — Revisión y actualización de la norma

Revisión y actualización **al menos cada dos años**, contados desde la entrada en vigencia. Las actualizaciones considerarán aprendizajes y dificultades reportados por los órganos, impulsando buenas prácticas y minimizando efectos de prácticas incorrectas.

---

## Disposiciones Transitorias

### Artículo primero transitorio

Los órganos tendrán **1 año** desde la entrada en vigencia para construir el catastro inicial del inciso cuarto del Artículo 10 e incorporarlo al Directorio de Datos.

### Artículo segundo transitorio

**Cese del uso de PISEE.** El **31 de diciembre de 2026** es el último día de funcionamiento de la Plataforma Integrada de Servicios Electrónicos del Estado (PISEE). A partir de esa fecha, la red de interoperabilidad de esta norma será la **única vía de interoperabilidad** para todos los órganos.

### Artículo tercero transitorio

La interoperabilidad corresponde a la **sexta y última fase** de aplicación de la ley de Transformación Digital (DFL Nº 1/2020). Los órganos que usen PISEE en versión anterior deberán migrar a la red de interoperabilidad:
- **Grupos "A" y "B":** durante el año **2025**.
- **Grupo "C":** durante el año **2026**.

Los órganos podrán comenzar la transición antes de la Fase 6.

### Artículo cuarto transitorio

Los esquemas asociados a PISEE deberán ser revisados por los órganos que los utilicen, con **1 año** desde la entrada en vigencia para modificar, ajustar o actualizar los esquemas al Catálogo de Servicios de Interoperabilidad.

### Artículo quinto transitorio

**Reemplazo de convenios.** Quedan sin efecto todos los convenios sobre interoperabilidad vigentes entre órganos en lo que no sean compatibles con esta norma (art. cuarto transitorio del Reglamento).
