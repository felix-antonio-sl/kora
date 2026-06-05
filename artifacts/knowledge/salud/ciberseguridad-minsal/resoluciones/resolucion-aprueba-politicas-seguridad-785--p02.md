---
_manifest:
  urn: urn:salud:kb:resolucion-aprueba-politicas-seguridad-785-p02
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile. Resolución Exenta N°785 (03-NOV-2021). Aprueba Instructivo
      de Seguridad de la Información y Ciberseguridad para el Sector Salud.
  extensions:
    kora:
      family: note
    salud:
      minsal_id: RES_785
      fecha: '2021-11-03'
      signatario: Ministro de Salud
      documento_aprobado: Instructivo de Seguridad de la Información y Ciberseguridad
        para el Sector Salud, v1.3, Agosto 2021
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- resolucion
- acto-administrativo
lang: es
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
extensions:
  kora:
    shard_index: 2
    shard_count: 3
    shard_root_urn: urn:salud:kb:resolucion-aprueba-politicas-seguridad-785
---

# Resolución Exenta N°785 — Aprueba Instructivo de Seguridad de la Información y Ciberseguridad para el Sector Salud - Parte 02

## 6.6 Lineamientos para la Gestión de Incidentes de Seguridad y Ciberseguridad

Referencia: Guía de Notificación de Incidentes para Organismos de la Administración Pública (CSIRT, `www.csirt.gob.cl`).

#### 6.6.1 Gestión de Incidentes

- Gestionar los incidentes de seguridad de la información o ciberseguridad. Crear bitácora con descripción de cada actividad desarrollada.
- Designar responsables de gestionar, comunicar y dar respuesta a incidentes, liderado por el responsable de seguridad/ciberseguridad.
- Contar con un equipo de respuesta para identificar riesgos de afectación de servicios, verificar cumplimiento de planes de gestión y reportar ciberincidentes.
- Establecer planes de gestión de riesgos de ciberseguridad formulados según estándares y directrices coherentes.
- Los planes de gestión de riesgo deben ser actualizados y sometidos a aprobación de la dirección institucional. Incluir medidas para protección de datos personales y sensibles (Ley N°19.628).

#### 6.6.2 Obligación de Reportar Incidentes

- Reportar al CSIRT de Gobierno (`soc@csirt.interior.gob.cl`) y al Equipo de Seguridad Ministerial (`seguridadtic@minsal.cl`) todos los ciberincidentes que alcancen los niveles de peligrosidad e impacto establecidos.
- Los incidentes que afecten disponibilidad, autenticidad, integridad o confidencialidad deben ser comunicados al Equipo de Seguridad Ministerial para estadística, tipología y gestión del conocimiento.
- El responsable de seguridad debe coordinar la respuesta y realizar planes de mejoramiento según causa raíz.

#### 6.6.3 Niveles de Peligrosidad

El nivel determina la potencial amenaza de materialización de un incidente.

| Nivel | Tipo de Incidente | Ejemplos |
| --- | --- | --- |
| **Crítico** | Amenaza Avanzada Persistente (APT) | Ataques dirigidos con mecanismos sofisticados de ocultación, anonimato y persistencia; ingeniería social |
| **Muy alto** | Código dañino | Distribución de malware, configuración de malware, webinjects |
| **Alto** | Intrusión | Acceso no autorizado, abuso de claves, sabotaje, interrupción de servicio, contenido abusivo |
| **Alto** | Código dañino | Sistema infectado, servidor C&C |
| **Alto** | Intrusión | Compromiso de aplicaciones (SQL injection), compromiso de cuentas con privilegios, intento de intrusión con exploit desconocido |
| **Alto** | Disponibilidad del servicio | DoS, DDoS |
| **Alto** | Compromiso de la información | Acceso no autorizado, modificación no autorizada, sabotaje a datos, ransomware |
| **Medio** | Fraude | Ingeniería social, discurso de odio, ciberacoso, explotación de vulnerabilidades conocidas, intento de acceso con vulneración de credenciales, mala configuración, uso no autorizado de recursos |
| **Medio** | Suplantación | Derechos de autor, suplantación de entidad |
| **Medio** | Vulnerabilidad | Criptografía débil, amplificador DDoS, servicios con acceso potencial no deseado, revelación de información, sistema vulnerable |
| **Bajo** | Contenido abusivo | Spam, escaneo de redes, sniffing |

#### 6.6.4 Niveles de Impacto

Criterios: tipología de información/sistemas afectados, grado de afectación a instalaciones, interrupción en prestación del servicio, tiempo y costos de recuperación, pérdidas económicas, cantidad de unidades afectadas, daños reputacionales.

| Nivel | Descripción |
| --- | --- |
| **Crítico** | Afecta seguridad ciudadana con potencial peligro para la vida. Afecta a más del 50% de procesos. Interrupción ≥12 horas o >40% de usuarios. Daños reputacionales de difícil reparación con eco mediático. |
| **Muy alto** | Afecta seguridad ciudadana con peligro para bienes materiales. Afecta vida privada y honra. Afecta más del 40% de procesos. Interrupción ≥8 horas o >30% de usuarios. Afecta >40% de instalaciones a nivel nacional. |
| **Alto** | Afecta >30% de procesos. Interrupción ≥6 horas o >20% de usuarios. Daños reputacionales con eco mediático afectando a terceros. |
| **Medio** | Afecta >20% de procesos. Interrupción ≥4 horas y >10% de usuarios. Daños reputacionales con eco mediático sin afectar reputación de terceros. |
| **Bajo** | Afecta ≥10% de sistemas. Interrupción ≥2 horas y >5% de usuarios. Afecta ≥10% de instalaciones. Daños reputacionales sin eco mediático. |
| **Sin impacto** | No hay impacto apreciable. |

#### 6.6.5 Contenido de los Reportes

Campos mínimos: resumen ejecutivo, identificación de la institución, encargado de ciberseguridad, fecha y hora de ocurrencia, fecha y hora de detección, descripción detallada, recursos tecnológicos afectados, origen o causa, taxonomía/clasificación/tipo, nivel de peligrosidad, nivel de impacto, indicadores de compromiso (IP, dominios, subdominios, correos, MD5), plan de acción y medidas de resolución/mitigación, afectados actuales y potenciales, medios necesarios, impacto económico estimado, cantidad de unidades afectadas, daños reputacionales, bitácoras generadas automáticamente, antecedentes adjuntos, clasificación de confidencialidad TLP.

#### 6.6.6 Oportunidad de los Reportes

Tres etapas: reporte inicial (obligatorio), reportes intermedios (actualización) y reporte final.

| Nivel de Peligrosidad | Reporte Inicial | Reporte Intermedio | Reporte Final |
| --- | --- | --- | --- |
| Alto | Inmediato (1 hora) | 24/48/72 horas | Máximo 30 días corridos |

Los plazos se computan desde que se toma conocimiento del incidente o sus efectos.

#### 6.6.7 Canales de Comunicación

- Reportar a CSIRT de Gobierno: `soc@interior.gob.cl`
- Reportar al Equipo de Seguridad Ministerial: `seguridadtic@minsal.cl` o Mesa de Servicios `mesadeservicios@minsal.cl`
- Alternativas: sistema `https://www.csirt.gob.cl` o telefónicamente al número de emergencias cibernéticas `1510`.

#### 6.6.8 Tratamiento de los Reportes

Los reportes serán tratados como documentación confidencial, especialmente en datos que expongan antecedentes técnicos propios que pongan en riesgo la ciberseguridad, así como información de usuarios conforme a legislación de protección de la vida privada.

#### 6.6.9 Resolución de Ciberincidentes

Una vez detectado un ciberincidente, el organismo debe efectuar todas las gestiones necesarias para su resolución y restaurar la normal provisión de servicios, según su plan de gestión de riesgos, dando primera prioridad a medidas que eviten o minimicen el impacto a los usuarios y la continuidad del negocio.

## 6.7 Lineamiento de Seguridad para el Desarrollo de Software Seguro

- Integrar seguridad de la información dentro del ciclo de vida del desarrollo, adquisición o mantención del software, desde las etapas iniciales (diseño y requerimientos) hasta las pruebas de seguridad en producción.
- Configurar y usar algún proyecto OWASP para revisión de vulnerabilidades en aplicaciones antes de entregar.
- Implementar mecanismos de autenticación seguros: contraseñas de al menos `10` caracteres con combinación de letras, números, símbolos, mayúsculas y minúsculas.
- Implementar mecanismos de limitación de intentos de inicio de sesión (ralentización, bloqueo de IP o bloqueo de cuentas después de un número predeterminado de intentos fallidos). No bloquear permanentemente.
- En caso de ataques de fuerza bruta: implementar múltiples factores de autenticación.
- Usar autenticación criptográfica a través de módulos de hardware criptográfico seguro con mecanismo adicional (password, biometría, otros).
- Identificar datos sensibles o críticos para implementar protecciones correctas.
- Las comunicaciones que transporten información de usuarios entre sistemas deben estar protegidas mediante TLS con el cifrado más fuerte disponible.
- Evitar, cuando sea posible, el almacenamiento de datos sensibles por parte de la aplicación. Si no se puede evitar, proteger mediante encriptación.
- Implementar sistemas de acceso seguro a datos, accediendo cada usuario solo a aquello respecto de lo cual tiene permisos.
- Establecer mecanismos de comunicación segura de datos, cualquiera que sea el medio o técnica utilizada.
- Establecer plazos máximos de almacenamiento y métodos para destrucción de datos, manteniendo registro auditable (log) con identificación del usuario, descripción del contenido, motivo del acceso y destinatario.
- Sobre adquisición de sistemas a terceros: establecer acuerdo previo y formal con cláusulas de seguridad que permitan resguardar propiedad intelectual, alojamiento de datos, cloud computing y cumplimiento de las Políticas y Procedimientos de Seguridad de la Información del MINSAL.
- Establecer firma de contratos de confidencialidad independientes de otras obligaciones (duración indefinida).
- Incluir responsabilidades de terceros en la gestión de incidentes de seguridad. Diferenciar entre quien establece/autoriza los acuerdos con terceros y quien audita su cumplimiento.

## 6.8 Lineamiento sobre Tratamiento de Datos Sensibles para Uso en Nube y Contratos Relacionados

**Marco normativo de la nube:**

- Toda información personal recolectada, almacenada, procesada y transmitida debe ser diseñada para dar cumplimiento a obligaciones de reserva o secreto.
- Los sistemas de acceso remoto a datos deben ser diseñados para ser accedidos solo desde dentro de la Red del Ministerio, con canales seguros y protegidos con nombre de usuario y contraseña segura.
- De todo proceso sobre el sistema o los datos debe quedar registros detallados y auditables (identificación del usuario, descripción del contenido, motivo del acceso, operaciones de tratamiento, tiempo de retención, destinatarios).
- Los sistemas deben considerar sistemas de respaldo que permitan recuperación segura de la información en tiempos razonables para procesos críticos.
- Los datos sensibles deben ser seudonimizados antes de ser ingresados en sistemas en nube, manteniendo en servidores locales los datos de reidentificación.

**Medidas organizativas:**

- Prohibición de uso de la información más allá de las necesidades asociadas al cumplimiento del contrato
- Auditabilidad: obligación de que el proveedor mantenga auditorías externas de seguridad y entregue evidencias
- Notificación de incidentes de seguridad: obligación del proveedor de comunicar los incidentes que afecten a su servicio
- Monitoreo y Cumplimiento: contar con monitoreo de los servicios prestados
- Condiciones contractuales: definir claramente alcance de los servicios, márgenes de crecimiento/reducción elástica, SLA y sanciones por incumplimiento
- Resguardos de legalidad: no considerar cláusulas fuera de las competencias del Ministerio (prórroga de competencia a tribunales extranjeros o arbitrales, renuncia a responsabilidades del proveedor, renuncia a garantías, cesiones de datos sensibles no autorizadas por ley)

**Medidas técnicas:**

- Certificaciones de seguridad acordes a la criticidad de la información. Para información crítica y datos sensibles de salud: nivel más alto de certificación según estándar generalmente aceptado.
- Encriptación de datos confidenciales no susceptibles de seudonimización.
- Seudonimización de información sensible de personas naturales, manteniendo en servidor local los códigos de reidentificación.
- Elasticidad: planificación adecuada de la capacidad; reservar capacidad con anticipación o definir valores de crecimiento flexibles en contrato.
- Modificación y destrucción de datos: el proveedor realiza tratamiento por mandato del contratante. Toda modificación, cancelación o destrucción debe realizarse por instrucciones del mandante con acta de las operaciones.
- Definir acceso y eliminación de datos tratados: períodos mínimos y máximos de retención.
- Dispositivos digitales y magnéticos: someter a procedimientos de formateo seguro antes de descartar.
- Prohibición de destruir o descartar originales sin autorización del mandante en procesos de digitalización.

**Aspectos a medir:**

- Cumplimiento de las medidas de seguridad acordadas
- Cumplimiento de los niveles de servicio acordados
- Cumplimiento de las políticas del prestador de servicios
- Cumplimiento de medidas asociadas a la destrucción de datos al final del contrato

#### 6.8.1 Seguridad en Nube

Principios de seguridad que los Prestadores de Servicios deben cumplir:

- **Controles de acceso, identidad y autenticación robustos** tanto en tránsito como en reposo. El acceso a todas las interfaces de servicio debe restringirse a personas autenticadas y autorizadas.
- **Protección de activos de información y datos** tanto en tránsito como en reposo. Centros de datos bajo estándares reconocidos. Criterios claros sobre controles criptográficos. Política clara de retención y eliminación de datos. La propiedad de un dato no debe modificarse al ser tratada en entornos cloud.
- **Seguridad Operacional, del Personal y Proveedores**: procesos y procedimientos para garantizar la seguridad en la operación, incluyendo gestión de personal y proveedores, con posibilidad de vetar personal o proveedores con historiales de incumplimiento.
- **Gestión segura de los clientes**: separación de clientes y promoción del uso seguro del servicio. Transmitir claramente las responsabilidades de cada parte. Garantizar separación lógica o física de clientes.
- **Proveer información de auditorías a los clientes**: proporcionar registros de auditoría para controlar acceso al servicio y datos. Acceso razonable respetando políticas de confidencialidad.
- **Marco de gobernanza**: el Prestador de Servicios debe tener un marco de gobernanza de seguridad con suficiente coordinación y dirección.
- **Reporte de incidentes de seguridad**: transparentar al cliente información detallada y oportuna sobre incidentes de seguridad que afecten el servicio contratado y adoptar medidas para mitigar daños.

## 6.9 Estructura Documental

Se recomienda definir una estructura documental para la definición de controles de seguridad:

| Nivel | Descripción | Responsable |
| --- | --- | --- |
| Política | Establece lo que se debe cumplir | Comité de Seguridad de la Información / Encargado de Seguridad de la Información |
| Procedimientos y planes | Detallan los procesos a seguir para cumplir los objetivos | Comité de Seguridad de la Información / Encargado de Seguridad de la Información |
| Instrucciones de trabajo | Acciones detalladas para aspectos concretos a documentar | Cada área de la Institución |
| Registros | Presentan resultados obtenidos o proporcionan evidencia de las actividades desempeñadas | Cada área de la Institución |

## 6.10 Lineamientos de Gestión para la Mejora Continua

Estructurar y mantener un modelo de Gestión de Mejora Continua para el SGSI de cada Servicio, con revisión anual, permitiendo desarrollar los procesos necesarios para mantener en el tiempo los controles de seguridad y avanzar en la Madurez de los Procesos.

Se recomienda el uso del Modelo Deming (PDCA: Plan, Do, Check, Act) u otro modelo equivalente que propicie mejora continua.

## 6.11 Lineamientos en Medición del Nivel de Cumplimiento y Niveles de Madurez

Al menos una vez al año se debe contrastar la aplicación de cada lineamiento como proceso de control de seguridad, evaluando su nivel de madurez, por auditoría interna o por una parte no involucrada directamente en dicho control.

Se define una base de medición estandarizada para los Niveles de Madurez fundamentada en marcos de referencia internacionales (CMM, COBIT, ISO/IEC 15504). Esto permite contrastar la realidad institucional con el nivel deseable y extraer brechas (GAPs) para planificar controles de mitigación.

Se debe priorizar alcanzar una línea base de nivel de madurez a nivel sectorial, al menos en los procesos de control priorizados. Por ejemplo, alcanzar un nivel de madurez 3 o Formalizado: contar con política, procedimiento y/o instructivo que formalice el quehacer en dicho tema.

**Nota sobre la fuente OCR:** Las páginas 29-30 del documento fuente contienen la tabla de Niveles de Madurez con información gráfica densa que no es recuperable del OCR. El contenido de esas páginas debe consultarse directamente en el documento original aprobado.

## 7. Controles de Seguridad Mínimos a Implementar

Resumen de controles mínimos recomendados por el Ministerio del Interior y el Ministerio de Salud.

## Dominio 5 — Políticas de Seguridad de la Información

| Control NCh-ISO 27001 | Objetivo | Implementación |
| --- | --- | --- |
| A.5.1.1 Políticas para la seguridad de la información | Proporcionar lineamientos compatibles con la misión y objetivos estratégicos, orientados a mitigar riesgos de seguridad | Establecer un conjunto de políticas de seguridad respaldadas por planificación estratégica institucional, aprobadas por la dirección o Comité de Seguridad |
| A.5.1.2 Revisión de las políticas | Disponer de lineamientos para conservar confidencialidad, integridad y disponibilidad | Documentos aprobados por la dirección, comunicados y difundidos al personal y stakeholders. Revisados al menos cada 2 años o cuando se produzcan cambios significativos |

El documento de política debe estar aprobado por Resolución Exenta o similar.

## Dominio 6 — Organización de la Seguridad de la Información

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.6.1.1 Roles y responsabilidades | Lograr liderazgo y guía en implementación, operación y mejora del SGSI | Designar formalmente un Encargado de Seguridad que reporte al Jefe de Servicio, con perfil adecuado, liderazgo, conocimiento técnico y capacidad de gestión |
| A.6.1.1 Roles y responsabilidades | Contar con un equipo multidisciplinario de decisión que apoye al encargado de seguridad | Designar integrantes del Comité de Seguridad con representantes de todas las áreas donde se identifiquen riesgos de seguridad de la información, incluyendo al menos un representante de tecnología. El comité debe sesionar al menos de forma anual |
| A.6.1.2 Segregación de funciones | Reducir el riesgo de negligencia, mal uso o compromiso de la información | Establecer una política de segregación de funciones que impida acceder, modificar, utilizar o destruir activos sin autorización, considerando posibilidad de sabotaje o colusión. Puede limitarse a procesos o sistemas específicos |
| A.6.1.3 Contacto con autoridades | Mantener contacto con autoridades y grupos de interés para gestión de incidentes | Establecer procedimiento con autoridades internas y externas para manejo de incidentes: medios de contacto, mecanismos de constancia de comunicaciones, pasos a seguir |
| A.6.1.4 Contacto con grupos especiales de interés | Mantenerse al tanto de tendencias, normas y métodos de seguridad relevantes | Mantener una lista de grupos de interés contactada con regularidad. Mantener contacto con el Área de Seguridad del MINSAL (`seguridadtic@minsal.cl`) y el CSIRT del Ministerio del Interior. Informar inmediatamente cada cambio de contactos |

## Dominio 7 — Seguridad de Recursos Humanos

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.7.1.2 Términos y condiciones de la relación laboral | Formalizar responsabilidades de seguridad de la información | Cada colaborador a honorarios debe firmar contrato que especifique responsabilidades en seguridad. Funcionarios de planta o contrata: la resolución de ingreso debe especificar responsabilidades en seguridad. Firmar acuerdo de confidencialidad cuando amerite |
| A.7.2.1 Responsabilidades de la dirección | Concientizar a los trabajadores sobre sus responsabilidades | La dirección debe impartir instrucciones sobre: 1) Uso seguro de sistemas informáticos, 2) Uso seguro de red interna e internet, 3) Generación, transmisión, recepción, procesamiento y almacenamiento de información, 4) Procedimientos para reporte de incidentes |
| A.7.2.2 Concientización, educación y formación en seguridad de la información | Concretar el compromiso de la dirección con medidas claras | Instrucciones impartidas mediante actividades presenciales, grupales o por medios acordes a las necesidades de la institución |

## Dominio 8 — Administración de Activos

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.8.1.1 Inventario de activos | Identificar los activos de información y sus responsables | Identificar e inventariar activos mediante procedimiento documentado, asignando un responsable por cada activo. Actualización al menos anual |
| A.8.1.2 Propiedad de los activos | Asignar responsable de cada activo identificado | Responsable registrado en el inventario |
| A.8.2.1 Clasificación de la información | Clasificar y etiquetar activos según necesidad de protección | Analizar y valorar cada activo para determinar necesidad, prioridad y grado de protección. Cada activo debe tener una categoría de clasificación en conformidad con la LOCBGAE |
| A.8.2.2 Etiquetado de la información | Procedimiento de etiquetado según clasificación | Definir procedimiento para etiquetado de activos acorde a la clasificación, incluyendo etiquetado en la salida de sistemas |
| A.8.1.3 Uso aceptable de los activos | Garantizar que el personal conozca y aplique los lineamientos de protección de activos | Definir política de uso aceptable que establezca: 1) Responsabilidades del personal en cuidado de activos, 2) Lineamientos de uso de correo, internet y medios de almacenamiento extraíbles, 3) Prohibición de software no autorizado |
| A.8.2.3 Manejo de activos | Garantizar la protección de la información contenida en medios de almacenamiento | Definir procedimientos de manejo seguro de medios (solicitud, entrega, uso, transporte, devolución y eliminación), alineados al uso aceptable de activos |
| A.8.3.1 Gestión de los medios | Gestión de medios removibles | Establecer restricciones de acceso a medios de almacenamiento extraíbles, con controles de conexión |
| A.8.3.2 Eliminación de medios | Eliminación segura | Procedimiento de eliminación de medios en el período |
| A.8.3.3 Transferencia física de medios | Protección en tránsito | Controles aplicados a la transferencia física |

## Dominio 9 — Control de Acceso

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.9.1.1 Política de control de acceso | Control de acceso lógico a los sistemas y activos | Contar con controles de acceso lógico basados en identificador único y contraseña. Para requerimientos más estrictos: múltiples factores de autenticación (firma electrónica, OTP, biometría). Definir política de gestión de acceso lógico que establezca: 1) Métodos de autenticación autorizados, 2) Gestión de identificadores y contraseñas (largo, complejidad, vida útil, historial, clasificación de usuarios privilegiados), 3) Revisión periódica de accesos otorgados, 4) Redes y servicios accesibles, 5) Lineamientos sobre quién puede acceder a qué redes/servicios, basada en principios de compartimentalización, necesidad de saber y menor privilegio |
| A.9.1.2 Accesos a las redes y a los servicios de la red | Proteger el acceso a servicios de red | Establecer políticas de acceso lógico para todos los sistemas |
| A.9.2.1 Registro y cancelación de registro de usuario | Gestión del acceso lógico | Procedimientos para: 1) Asignación de información de autenticación (jefe directo como responsable de la solicitud), 2) Alta, baja, modificaciones y cancelación de derechos de acceso (incluyendo acceso privilegiado), 3) Entrega segura de información de autenticación temporal (prohibición de entrega mediante texto no protegido), 4) Obligación de cambiar información de autenticación temporal con el primer uso |
| A.9.2.2 Asignación de acceso de usuario | Asignar acceso a usuarios | Evidencia del proceso de alta, baja y modificación de derechos de acceso |
| A.9.2.3 Gestión de derechos de acceso privilegiados | Control de usuarios privilegiados | Restricciones especiales para cuentas con privilegios elevados |
| A.9.2.4 Gestión de información secreta de autenticación de usuarios | Gestión segura de contraseñas | Uso de contraseñas diferentes en distintos sistemas; información de autenticación de uso personal |
| A.9.4.3 Sistema de gestión de contraseñas | Gestión de contraseñas | Sistema para gestión de contraseñas temporales y entrega segura |

**Instrucciones a usuarios sobre control de acceso lógico:**

1. Mantener en forma confidencial la información de autenticación asignada
2. No registrar la información de autenticación en papel
3. No almacenar la información de autenticación de forma desprotegida
4. No compartir la información de autenticación con otros usuarios
5. Mantener la información de autenticación grupal solo dentro de los miembros del grupo
6. No incluir la información de autenticación en procesos automatizados o de inicio de sesión automáticos (macro o script)
7. Cambiar la información de autenticación cuando haya indicios de posible compromiso de un sistema
8. Evaluar adecuadamente factores de autenticación inmutables (factores biométricos)

**Procesos de inicio de sesión seguros:**

- Terminar sesiones después de un período de inactividad
- No mostrar la contraseña que se ingresa
- Proteger con encriptación los inicios de sesión forzados
- No transmitir información de autenticación sin cifrar

## Dominio 10 — Criptografía

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.10.1.1 Política sobre el uso de controles criptográficos | Proteger la confidencialidad, integridad y autenticidad de la información | Establecer política de uso de controles criptográficos que aborde: 1) Mecanismos de cifrado para proteger información (discos duros, respaldos), 2) Uso y gestión de certificados digitales (firma electrónica, firma electrónica avanzada), 3) Uso de criptografía para canales seguros (correo, VPN, SSL/TLS/HTTPS, IPSec, SSH), incluyendo gestión de llaves y certificados, 4) Listado de algoritmos o protocolos criptográficos inseguros de uso prohibido |
| A.10.1.2 Gestión de claves | Gestión de llaves criptográficas | Política de gestión de llaves criptográficas |

**Algoritmos/protocolos criptográficos de uso prohibido:**

- MD4, MD5, SHA-1
- DES, 3DES
- RC4
- RSA o DSA con largo de llaves ≤1024 bits
- Criptografía basada en curvas elípticas con largo de llaves ≤160 bits
- Cualquier tipo de algoritmo criptográfico "casero" o implementaciones "caseras"

## Dominio 11 — Seguridad Física y Ambiental

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.11.1.1 Perímetro de seguridad física | Proteger las instalaciones de procesamiento contra accesos no autorizados, robos, mal uso o daños por peligros ambientales | Establecer política de seguridad física alineada a políticas de control de acceso lógico y análisis de riesgos. Definir perímetros de seguridad física (áreas seguras) con barreras de resguardo, controles de acceso apropiados y protección física |
| A.11.1.2 Controles de acceso físico | Control de acceso a áreas seguras | Establecer procedimiento de acceso a áreas seguras y designar personal autorizado. Registros de acceso |
| A.11.1.4 Protección contra amenazas externas y del ambiente | Proteger el equipamiento de daño | Establecer política de seguridad del equipamiento: 1) Ubicación que minimice acceso innecesario y percances, 2) Controles de seguridad física contra robos, incendios, humo, agua, vibraciones/terremotos, interferencia del suministro eléctrico, 3) Mecanismos de monitoreo de condiciones ambientales (humedad, temperatura), 4) Mecanismos de detección temprana y extinción de incendios, 5) Mecanismos de mantención periódica del equipamiento |
| A.11.2.1 Ubicación y protección del equipamiento | Protección del equipamiento | Evidencias de controles de seguridad ambiental en áreas seguras |
| A.11.2.4 Mantenimiento del equipamiento | Mantenimiento programado | Evidencias del mantenimiento realizado |
| A.11.2.7 Seguridad en la reutilización o descarte de equipos | Prevenir pérdida de información en reutilización o descarte | Establecer política de reutilización o descarte de activos con requisitos de borrado, sobreescritura o destrucción según clasificación. Procedimiento de borrado seguro: 1) Los datos deben ser eliminados o sobrescritos de manera segura antes de reutilizar o descartar, 2) Prohibición de formateo normal en descarte de equipos — obligatorio borrado seguro, 3) Para datos sensibles: destrucción segura del medio de almacenamiento. Alternativa: encriptación de la información (al destruir la llave, la información no se puede recuperar) |
| A.11.2.8 Equipo de usuario desatendido | Proteger equipos desatendidos | Política de escritorio y pantalla limpios: 1) Prohibición de consumo de alimentos, bebidas y tabaco en cercanías del equipamiento, 2) Cierre o bloqueo de sesión al terminar funciones y antes de levantarse del puesto, forzando uso de autenticación para reanudar, 3) Mantención de escritorio limpio de papeles o medios de almacenamiento con información institucional |
| A.11.2.9 Política de escritorio limpio y pantalla limpia | Protección de documentos y pantallas | Evidencia de difusión de la política |

## Dominio 12 — Seguridad de las Operaciones

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.12.2.1 Controles contra código malicioso | Proteger la información contra código malicioso | Establecer política contra código malicioso: 1) Características de la solución (centralizada o no, lista blanca/gris/negra, actualización de firmas), 2) Capacitaciones al personal sobre conductas de riesgo (abrir archivos adjuntos de correo, uso de medios extraíbles en computadores no seguros), 3) Implementación de mecanismos de detección y limpieza de código malicioso. Capacitaciones alineadas a responsabilidades de la dirección. |
| A.12.3.1 Respaldo de la información | Proteger contra pérdida de datos | Establecer política de respaldos: 1) Sistemas o equipamiento a respaldar, 2) Periodicidad de respaldos de estaciones de trabajo (no menor a un respaldo anual), 3) Periodicidad de respaldos de sistemas de información (no inferior a un respaldo mensual), 4) Retención de respaldos (no inferior a tres ciclos), 5) Infraestructura necesaria para almacenamiento, 6) Ubicación que minimice riesgo de ser afectada por los mismos incidentes que los sistemas de información, 7) Requerimientos de seguridad para la infraestructura de almacenamiento (controles de acceso, condiciones físicas y ambientales), 8) Pruebas de restauración (no inferior a una prueba anual por sistema, documentadas), 9) Software de respaldos disponible junto con los respaldos |
| A.12.4.4 Sincronización de relojes | Facilitar seguimiento de eventos y consistencia de registros | Establecer política de sincronización de relojes: 1) Establecer fuente de tiempo para la hora oficial de Chile, 2) Mecanismos para mantener la sincronización de relojes en los sistemas |
| A.12.5.1 Instalación del software en sistemas operacionales | Asegurar integridad de los sistemas | Establecer prohibición del uso de software no autorizado en alguna política de seguridad. Procedimiento de instalación de software: 1) Instalación en sistemas, 2) Instalación en estaciones de trabajo, 3) Listado de software permitido (incluyendo software base, tipos de software instalables por usuarios, software que requiera autorización especial), 4) Listado de software o categorías prohibidas, 5) Mecanismos de revisión de software instalado |
| A.12.6.2 Restricciones sobre la instalación de software | Control de instalación de software | Evidencias de resultados de revisiones de software instalado |

## Dominio 13 — Seguridad en las Comunicaciones

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.13.1.1 Controles de red | Proteger la información en sistemas y aplicaciones mediante administración y control de las redes | Establecer política de seguridad de red: 1) Mecanismos y responsabilidades para administración de equipos de redes, 2) Mecanismos de autorización del acceso a distintas redes y sistemas, 3) Mecanismos para controlar/restringir conexión a redes y sistemas internos y externos |
| A.13.2.1 Políticas y procedimientos de transferencia de información | Mantener la seguridad de la información transferida | Establecer política de comunicaciones seguras: 1) Medidas de protección para transferencia de información a través de cualquier medio de comunicación (incluyendo transporte físico), 2) Medidas para proteger la información contra intercepción, copia y/o destrucción, 3) Medidas para detección y protección contra código malicioso transmitido por medios electrónicos, 4) Lineamientos para uso aceptable de mensajería electrónica, 5) Uso de criptografía para proteger la información transferida, 6) Controles adicionales para mensajes que no se puedan autenticar |
| A.8.3.3 Transferencia física de medios | Protección de medios en tránsito | Evidencia de procedimientos para transferencia física |
| A.13.2.3 Mensajería electrónica | Uso aceptable de mensajería | Evidencia de configuración de sistemas de correo acorde a la política |

## Dominio 14 — Adquisición, Desarrollo y Mantenimiento de Sistemas

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.14.1.1 Análisis y especificación de requisitos de seguridad de la información | Incorporar la seguridad en el ciclo de vida de los sistemas | Los requisitos de seguridad deben ser definidos e incluidos en procesos y proyectos de adquisición, desarrollo de nuevos sistemas o mejora de sistemas existentes |
| A.14.2.1 Política de Desarrollo Seguro | Las reglas para el desarrollo de software y sistemas deben ser establecidas y aplicadas a los desarrollos dentro de la organización | Establecer política de desarrollo seguro que considere: a) seguridad del entorno de desarrollo, b) orientación sobre seguridad del ciclo de vida del desarrollo, c) pautas de codificación segura para cada lenguaje de programación, d) requisitos de seguridad en la fase de diseño, e) puntos de verificación de seguridad dentro de los hitos del proyecto, f) repositorios seguros, g) seguridad en el control de versión, h) conocimiento de seguridad de aplicación necesario, i) capacidad de los desarrolladores de evitar, encontrar y solucionar vulnerabilidades. Si se externaliza: obtener garantía de que la parte externa cumple estas reglas. |
| A.14.2.2 Procedimientos de control de cambios del sistema | Los cambios a los sistemas deben ser controlados mediante procedimientos formales | La introducción de nuevos sistemas y cambios importantes debe seguir un proceso formal de documentación, especificación, pruebas, control de calidad e implementación administrada. Incluir evaluación de riesgos, análisis de impactos y especificación de controles de seguridad necesarios. |
| A.14.2.7 Desarrollo tercerizado | La organización debe supervisar y monitorear la actividad del desarrollo del sistema tercerizado | Considerar a través de toda la cadena de suministro externo: acuerdos de licencia, propiedad de código y derechos de propiedad intelectual; requisitos contractuales para diseño seguro, codificación y prácticas de prueba; pruebas de aceptación de calidad y precisión de entregables; evidencia de pruebas suficientes contra contenido malicioso y vulnerabilidades conocidas |
| A.14.2.8 Prueba de seguridad de sistemas | Durante el desarrollo se debe realizar la prueba de funcionalidad de seguridad | Los sistemas nuevos y actualizados deben someterse a pruebas y verificaciones exhaustivas durante el desarrollo. Para desarrollos internos: pruebas iniciales por el equipo de desarrollo. Pruebas de aceptación independientes (tanto para desarrollos internos como externalizados) para garantizar que el sistema funciona según se espera y solo como se espera. |
| A.14.2.9 Prueba de aprobación del sistema | Definir los programas de prueba de aceptación y los criterios pertinentes para los nuevos sistemas | Las pruebas de aceptación deben incluir pruebas de requisitos de seguridad y adherencia a prácticas de desarrollo seguro. Realizar pruebas en entorno realista para no introducir vulnerabilidades al entorno de la organización. |

## Dominio 15 — Relaciones con los Proveedores

| Control | Objetivo | Implementación |
| --- | --- | --- |
| A.15.1.1 Política de seguridad para las relaciones con el proveedor | Mantener la seguridad de los activos de la institución accesibles a los proveedores | Establecer política de seguridad para las relaciones con proveedores que establezca los requisitos de seguridad que deben cumplir, alineada a los objetivos estratégicos institucionales y a sus políticas de seguridad |
| A.15.2.2 Gestión de cambios a los servicios del proveedor | Gestionar los cambios cuando se producen en los servicios de los proveedores | Considerar: cambios a los acuerdos del proveedor; cambios realizados por la organización para implementar mejoras a sus servicios, desarrollo de nuevas aplicaciones y sistemas, modificaciones o actualizaciones de políticas y procedimientos, nuevos controles o controles cambiados. Cambios en los servicios del proveedor: cambios y mejoras en redes, uso de nuevas tecnologías, adopción de nuevos productos/versiones, nuevas herramientas y entornos de desarrollo, cambios en ubicación física de instalaciones, cambio de proveedores, subcontratación a otro proveedor. |
