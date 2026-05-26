---
_manifest:
  urn: urn:tde:kb:terminos-condiciones-claveunica
  provenance:
    source: https://wikiguias.digital.gob.cl/terminos-y-condiciones/terminos-condiciones-claveunica
version: 1.0.0
status: published
tags:
- tde
- plataformas-terminos
- claveunica
- identidad-digital
- términos-y-condiciones
- plataformas-compartidas
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:terminos-condiciones-claveunica
---

# Términos y Condiciones: integración y uso del Sistema de ClaveÚnica

Aprobados por Resolución Exenta N° 733/2025 de la Subsecretaría de Hacienda.

---

## 1. Alcance y obligatoriedad

Regulan el uso del Sistema de ClaveÚnica por las Entidades Usuarias y sus responsabilidades y obligaciones asociadas.

Son **obligatorios para todas las Entidades Usuarias sin necesidad de aprobación o aceptación expresa**, por disposición del artículo segundo transitorio de la Ley N° 21.658.

---

## 2. Glosario

| Término | Definición |
|---------|-----------|
| Autenticación | Proceso electrónico que valida datos de identificación de un/a usuario/a para permitirle acceso a una plataforma |
| ClaveÚnica | Mecanismo oficial de autenticación operado por la SGD; uso exclusivo para personas naturales; basado en OpenID Connect; factor primario: contraseña vinculada al RUN |
| Contraseña | Combinación de caracteres de carácter confidencial utilizada para autenticarse a través del Sistema de ClaveÚnica |
| Entidad Usuaria | Entidad integrada al Sistema de ClaveÚnica que lo utiliza como mecanismo de autenticación |
| Integración | Proceso de conexión y habilitación al Sistema de ClaveÚnica |
| Mecanismo Oficial de Autenticación | ClaveÚnica, cédula de identidad digital y todo mecanismo validado por la SGD conforme la Norma Técnica de Autenticación |
| Ministerio | Ministerio de Hacienda |
| Subsecretaría | Subsecretaría de Hacienda |
| SGD / Secretaría | Secretaría de Gobierno Digital |
| Norma Técnica de Autenticación | DS N° 9, 17-ago-2023, Ministerio SEGPRES |
| Reglamento | DS N° 4, 2020, Ministerio SEGPRES (Ley N° 21.180 Transformación Digital del Estado) |
| RUN | Rol Único Nacional asignado por el Servicio de Registro Civil e Identificación |
| Servicios SaaS | Software de terceros suministrado vía internet; se accede desde navegador sin instalar en infraestructura propia |
| Usuario/a | Persona natural titular de cuenta activa de ClaveÚnica |

---

## 3. Criterios para ser considerada Entidad Usuaria

La SGD considerará al menos:
- a. Que la finalidad de la Administración sea promover el bien común de forma continua y permanente.
- b. Existencia de disposición legal o administrativa que permita u obligue a la entidad a utilizar ClaveÚnica, regule los casos de uso y considere medidas de seguridad adicionales.
- c. Capacidad de la entidad para garantizar seguridad, confiabilidad y responsabilidad, y para cumplir estándares técnicos aplicables.
- d. Existencia de institución pública con competencia para supervisar o fiscalizar el buen uso por parte de la Entidad Usuaria.

---

## 4. Habilitación e integración

1. La entidad solicita integración por primera vez a través del trámite "Solicitud de Credenciales de Integración a ClaveÚnica" en: https://gobdigital.cerofilas.gob.cl/
2. La SGD acepta la solicitud solo si la entidad cumple los requisitos exigidos.
3. Si por error se acepta una entidad sin habilitantes legales/administrativos, la SGD puede **revocar la autorización en cualquier etapa**, incluso con credenciales en producción. La SGD no es responsable de los daños que esto ocasione; es responsabilidad de la entidad verificar previamente el cumplimiento de los requisitos.
4. Al aceptar la solicitud, la SGD entrega credenciales de integración; la entidad ejecuta el proceso según la Guía Técnica Manual de Integración a ClaveÚnica (disponible en https://wikiguias.digital.gob.cl/).
5. La entidad es considerada Entidad Usuaria solo cuando se haya **certificado conforme al Manual Técnico y las credenciales hayan entrado en producción**.
6. Toda asistencia técnica durante y después de la integración se solicita a través de la Mesa de Servicios de la SGD: https://gobdigitalcl.freshdesk.com/support/tickets/new
7. Las entidades que integren ClaveÚnica a través de servicios SaaS deben cumplir el mismo proceso de habilitación. La solicitud de integración debe ser realizada por una persona de la dotación del órgano público responsable, usando URL institucional del órgano.

---

## 5. Contrapartes técnicas y comunicaciones

- La Entidad Usuaria debe designar una **contraparte administrativa** y una **contraparte técnica**, e informar a la SGD conforme al Manual de Integración a ClaveÚnica.
- Toda comunicación formal con la SGD se realiza a través de la Mesa de Servicios: https://gobdigitalcl.freshdesk.com/support/tickets/new

---

## 6. Obligaciones de las Entidades Usuarias

### 6.1. Cumplimiento de la normativa vigente

1. Utilizar ClaveÚnica en estricto apego a la normativa aplicable y a los habilitantes legales o administrativos que les permitan ser Entidad Usuaria.
2. Cumplir en todas las plataformas donde se use ClaveÚnica:
 - Ley N° 19.880 (Bases de Procedimientos Administrativos).
 - Ley N° 19.628 (Protección de la Vida Privada).
 - Ley N° 21.663 (Marco de Ciberseguridad).
 - Todas las demás normas administrativas relacionadas.
3. Cumplir con normas técnicas mandatadas por el artículo 57 del Reglamento, en especial la Norma Técnica de Autenticación, y el artículo 47 del DS N° 181/2020 del Ministerio de Economía (Reglamento Ley N° 19.799 sobre documentos electrónicos y firma electrónica). Las entidades no pertenecientes a la Administración del Estado deben cumplir estas normas salvo incompatibilidad con su naturaleza.
4. Cumplir con los lineamientos, estándares, directrices y guías técnicas establecidas por la SGD en el marco de la Ley N° 21.658 y su reglamento.

### 6.2. Difusión y comunicación

1. Comunicar y difundir los presentes Términos y Condiciones y las obligaciones derivadas dentro de la organización.
2. Cuando la integración se realice a través de un proveedor SaaS:
 - Difundir los Términos y Condiciones al proveedor.
 - Incorporar en las bases de licitación y en el contrato con el proveedor SaaS la **obligación de cumplir estos Términos y Condiciones**.
 - Establecer en el contrato la forma en que el proveedor cumplirá el deber de comunicación y difusión internamente.

### 6.3. Garantía de la correcta integración y funcionamiento

Conservar, actualizar, reparar y realizar cualquier actividad necesaria para mantener la infraestructura y sistemas operativos en condiciones óptimas que garanticen la correcta integración y funcionamiento de ClaveÚnica.

### 6.4. Adopción de medidas de seguridad

1. Habilitar o implementar un **segundo factor de autenticación** cuando un trámite o servicio requiera nivel de seguridad superior al factor primario de ClaveÚnica, conforme indique la SGD, la Agencia Nacional de Ciberseguridad u otra autoridad competente. Si la SGD exige un segundo factor por razones de seguridad, SGD y Entidad Usuaria acordarán un plan de trabajo conjunto para su implementación.
2. Los factores adicionales de autenticación y/o seguridad complementarios a ClaveÚnica no pueden basarse en información accesible mediante la propia ClaveÚnica o disponible en fuentes de acceso público.
3. Dar aviso **inmediato** a la SGD ante sospecha o identificación de incidentes de seguridad (accesos no autorizados a contraseñas, credenciales, etc.).
4. Cooperar con la SGD proveyendo información necesaria para auditorías e identificación de brechas de seguridad.
5. Realizar actualizaciones o modificaciones en protocolos o estándares que la SGD solicite por razones de seguridad o continuidad del servicio, conforme al Manual Técnico de Integración de ClaveÚnica.

### 6.5. Prohibiciones

Las Entidades Usuarias tienen **expresamente prohibido**:

1. Solicitar, almacenar o registrar las credenciales o contraseñas de usuarios de ClaveÚnica; recomendar, inducir o permitir que sean compartidas con terceros.
2. Crear, habilitar o recomendar mecanismos de automatización que permitan acceso a ClaveÚnica por parte de uno o más usuarios/as.
3. Utilizar ClaveÚnica para acceder o intentar acceder a cuentas, información o recursos sin autorización expresa de la SGD.
4. Manipular o intentar manipular el Sistema de ClaveÚnica para obtener acceso no autorizado, eludir medidas de seguridad o modificar configuraciones o procesos de manera no permitida.
5. Distribuir, sublicenciar o transferir el Sistema de ClaveÚnica a terceros mediante su integración.
6. Compartir las credenciales de integración con terceros ajenos a la Entidad Usuaria o a sus proveedores SaaS, o permitir su obtención fraudulenta por terceros no autorizados.
7. Utilizar ClaveÚnica para fines maliciosos: extracción o divulgación no autorizada de datos personales, actividades ilegales, o daño a la seguridad del sistema y/o de los usuarios.
8. Realizar ingeniería inversa, descompilar o intentar desensamblar el software o componentes del Sistema de ClaveÚnica con el fin de obtener información confidencial o aprovechar vulnerabilidades.

---

## 7. Disponibilidad y suspensión del servicio

### 7.1. Suspensiones programadas

- La SGD puede interrumpir temporalmente ClaveÚnica por mantención preventiva o mejora de infraestructura.
- Aviso previo de **al menos 48 horas** a través de la página web de ClaveÚnica, indicando horas de inicio y término.

### 7.2. Suspensiones no programadas

Causales:
- **Emergencias:** fallas técnicas, cortes de energía, caso fortuito o fuerza mayor.
- **Acción de terceros:** fallas en infraestructura causadas por un tercero (ej. ataque informático).

Comunicación: a través de la página web de ClaveÚnica y/o a la contraparte técnica.

Las Entidades Usuarias aceptan que la SGD **no puede asegurar un porcentaje determinado de disponibilidad** del servicio y que pueden producirse interrupciones por emergencias o acción de terceros. La SGD realizará todos los esfuerzos razonables dentro de sus capacidades operativas para evitar estas contingencias.

### 7.3. Otros ajustes al Sistema

Cualquier ajuste o cambio que afecte o pueda afectar el funcionamiento normal de las plataformas integradas o la autenticación de personas usuarias será comunicado a la Entidad Usuaria con la misma forma establecida en los párrafos precedentes.

---

## 8. Incumplimiento y suspensión del servicio

- El incumplimiento de cualquier disposición de estos Términos y Condiciones faculta a la SGD a **suspender los servicios de ClaveÚnica sin previo aviso**.
- La misma facultad aplica ante incumplimiento por parte de proveedores SaaS u otras modalidades similares.
- La SGD notifica por correo electrónico a la contraparte técnica las razones de la suspensión y la causal de incumplimiento.
- La suspensión **no exime** a la Entidad Usuaria del cumplimiento de las demás obligaciones de estos Términos y Condiciones.
- La SGD determinará prudencialmente las condiciones de reanudación del servicio.

---

## 9. Costos

- Todos los costos derivados de la integración, implementación o utilización del Sistema de ClaveÚnica son de **exclusivo cargo de la Entidad Usuaria**.
- Incluye: administración, actualización, reparación e infraestructura; hardware y software; personal y recursos internos; seguridad de la información, ciberseguridad y protección de la vida privada.

---

## 10. Uso de la marca ClaveÚnica

- ClaveÚnica es marca registrada a nombre de la Secretaría y Administración General del Ministerio de Hacienda, inscrita bajo el N° 1062117 del Registro de Marcas del INAPI.
- El uso no autorizado infringe la Ley N° 19.039 de Propiedad Industrial (artículo 19 bis, letra d).
- Está **expresamente prohibido**: reproducir, modificar o distribuir sin autorización el software o componentes del Sistema de ClaveÚnica, y usar sin autorización la marca y/o logos del portal https://claveunica.gob.cl.

---

## 11. Responsabilidad por daños y perjuicios

- El Ministerio queda **liberado de toda responsabilidad** por daños directos e indirectos, previstos e imprevistos, que experimente la Entidad Usuaria como consecuencia del mal uso del Sistema de ClaveÚnica o de la contravención de las obligaciones de estos Términos y Condiciones.
- Tampoco es responsable de daños y/o perjuicios producto de la suspensión del servicio por incumplimiento.

---

## 12. Modificación de los Términos y Condiciones

- La Subsecretaría se reserva el derecho de modificar sin expresión de causa y en cualquier momento estos Términos y Condiciones.
- Es **responsabilidad de las Entidades Usuarias revisarlos periódicamente**.
- Modificaciones avisadas previamente en https://claveunica.gob.cl, salvo situaciones urgentes de fuerza mayor.
- Las modificaciones entran en vigencia transcurridos **10 días hábiles** desde su publicación en el Diario Oficial.

---

## 13. Adecuación de estándares

- Las Entidades Usuarias integradas antes de la entrada en vigencia de estos Términos y Condiciones tienen **60 días corridos** para adecuarse.
- El plazo puede ser extendido prudencialmente por la SGD para entidades con dificultades o impedimentos operativos suficientes, previa justificación enviada a **claveunica@digital.gob.cl** dentro del mismo plazo.
- El incumplimiento faculta a la SGD a suspender el servicio de ClaveÚnica.
