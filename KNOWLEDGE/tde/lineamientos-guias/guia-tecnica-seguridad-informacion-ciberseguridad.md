---
_manifest:
  urn: "urn:tde:kb:guia-tecnica-seguridad-informacion-ciberseguridad"
  provenance: "https://wikiguias.digital.gob.cl/guias/GU-CIBER-001"
version: 1.0.0
status: published
tags: [tde, lineamientos-guias, seguridad-de-la-informacion, ciberseguridad, datos, guia-tecnica]
lang: es
---

# Guía Técnica de Seguridad de la Información y Ciberseguridad

**Base normativa:** Art. 12, Norma Técnica de Seguridad de la Información y Ciberseguridad (Decreto N° 7, 2023, SEGPRES). Aplica a todos los órganos de la Administración del Estado (OAE).
**Marco de referencia:** familia NCH-ISO 27000, NIST CSF, Decreto N° 83/2015. Pueden usarse otros estándares con efectos equivalentes.
**Versión:** 1.0 — 24/03/2025

---

## Definiciones clave

| Término | Definición |
|---------|-----------|
| Apetito al riesgo | Cantidad de riesgo que un OAE asume para alcanzar sus objetivos estratégicos |
| Ataque día cero | Exploit de vulnerabilidad desconocida por el proveedor; sin parches disponibles |
| Custodio | Encargado de otorgar y supervisar accesos a activos de información bajo su custodia |
| Dueño de activo | Encargado de inventariar, clasificar y actualizar los activos según esquema del OAE |
| Evento precursor | Indicio de posible incidente futuro; puede o no materializarse |
| Plan de continuidad operativa | Lineamientos para mantener operación de plataformas ante fallos |
| Plan de recuperación | Acciones para restaurar operación normal tras una disrupción |
| Plan de respuesta | Procedimientos para enfrentar un incidente confirmado |
| Redundancia | Duplicación de componentes software/hardware para asegurar disponibilidad ante fallos |
| Tolerancia al riesgo | Cantidad de volatilidad del entorno que una institución puede tolerar |

---

## Política de Seguridad de la Información y Ciberseguridad

Cada OAE debe elaborar una Política de Seguridad de la Información y Ciberseguridad (Art. 5, Norma Técnica), aprobada por el/la Jefe/a de Servicio, con actualización idealmente anual.

### Contenido obligatorio de la Política

1. **Objetivos generales y específicos** — con indicadores de cumplimiento
2. **Alcance** — identificación y clasificación de todos los activos de información
3. **Legislación y normas aplicables** — incluyendo toda normativa sectorial pertinente
4. **Roles y responsabilidades:**
   - **Responsable Institucional de Seguridad** — vela por seguridad, cumplimiento y actualización de la Política. Denominaciones equivalentes según Instructivo Presidencial N°8/2018, Decreto N°7/2023 y Ley N°21.663. **No puede externalizarse** (Art. 5 inc. 3°, numeral 4 de la Norma Técnica). Preferentemente reporta al Jefe de Servicio, no al área TIC.
   - **Responsable de Activos de Información** — identifica, clasifica, prioriza activos y gestiona el riesgo. Cada OAE decide si este rol se unifica o no con el anterior.
5. **Clasificación de la información y tratamiento** — vinculada a sensibilidad y criticidad
6. **Gestión de riesgos** — objetivos, rendición de cuentas y medición del proceso
7. **Gestión de vulnerabilidades técnicas** — funciones, responsabilidades, monitoreo y tratamiento
8. **Control de acceso** — procedimientos de distribución de identidades, recuperación escalonada de credenciales comprometidas
9. **Respaldos de información** — mecanismos, procesos, requisitos y procedimiento de restauración
10. **Continuidad** — plan de continuidad operativa y planes de recuperación/respuesta. Los operadores de importancia vital deben elaborarlo (Art. 8° lit. c, Ley N°21.663)
11. **Controles criptográficos** — para todo el ciclo de vida: transporte y almacenamiento
12. **Privacidad y protección de datos** — desde el diseño, según normativa vigente
13. **Eliminación segura** — procesos formales, registro de cada eliminación, conforme al Art. 11 del Decreto N°10/2023 (Norma Técnica de Documentos y Expedientes Electrónicos)

---

## Funciones, Categorías y Subcategorías

Marco basado en estructura de dominios NIST (referencias cruzadas: CIS Controls, COBIT 5, ISO 27001/27002, NCH equivalentes INN).

### Función de Identificación

Diagnóstico inicial mediante auditoría interna, entrevistas u otro medio de valoración. Herramientas recomendadas: MITRE ATT&CK, NIST CSF, CIS Controls v8, ISO/IEC 27001.

#### Contexto de la institución

Analizar, evaluar y comunicar aspectos internos y externos que afecten el desempeño, incluyendo:
- Aspectos legales, regulatorios y obligaciones contractuales
- Definiciones estratégicas (misión, visión, buenas prácticas)
- Interdependencias con otros OAEs (diagrama de entorno + identificación de actores)

#### Gobernanza

Establecer cómo los actores interactúan según sus atribuciones. Permite monitorear requisitos regulatorios e identificar riesgos operativos y del entorno.

#### Gestión de activos de información

**Inventario de activos:** dispositivos físicos, plataformas software, sitios web, bases de datos, aplicaciones. Actualización periódica. Apoyarse en ITIL v4 / CMDB.

**Dueños de activos:** cada activo requiere un dueño que:
- Clasifica según sensibilidad/criticidad
- Revisa periódicamente restricciones de acceso
- Gestiona eliminación conforme a lineamientos

**Custodios:** responsables técnicos de los accesos; garantizan integridad, disponibilidad y confidencialidad.

**Clasificación de activos** (Decreto Supremo N°83/2005):
- Documentos públicos: sin carácter reservado ni secreto
- Documentos reservados: acceso circunscrito a la unidad del órgano por ley o norma administrativa
- Documentos secretos: Art. 22, Ley N°20.285

Los OAE deben mantener índice actualizado de actos y documentos secretos/reservados (Art. 23, Ley de Transparencia; Res. Ex. N°500/2022, CPLT).

**Mapeo de comunicación y flujo de datos:** mecanismos de monitoreo y control del flujo, con registro de todos los emisores/receptores y sus privilegios.

---

### Gestión de riesgos

Proceso secuencial: contexto → identificación → análisis → evaluación → tratamiento → comunicación/monitoreo.

Herramientas de apoyo: Documento Técnico N°70 del CAIGG, OWASP Risk Rating, plantilla AGESIC.

**Contexto del riesgo:** definir objetivos, alcances, prioridades y restricciones del OAE en gestión de riesgos.

**Tolerancia y apetito al riesgo:** definir y comunicar criterios claramente; todas las medidas de mitigación se basan en ellos.

**Identificación del riesgo:** incluye riesgos de fuentes externas al control del OAE y dependencias con servicios de otros OAEs o terceros críticos para la misión.

**Análisis de riesgo:** estimación de impacto = probabilidad × impacto potencial. Permite metodologías cualitativas o cuantitativas.

**Evaluación del riesgo:** contrastar estimaciones con niveles de tolerancia definidos.

**Tratamiento del riesgo** — opciones:
- Tolerar/aceptar
- Mitigar mediante procedimiento o control
- Transferir (a tercero)
- Evitar (eliminar la fuente)

Los activos de alto riesgo permanecen clasificados como tal independientemente del tratamiento. La aceptación del riesgo debe documentarse y ser aprobada por el responsable de activos.

**Comunicación, monitoreo y revisión:** registro actualizado permanente de todos los riesgos. Los riesgos aceptados sin tratamiento deben constar en documento formal aprobado.

#### Relación con proveedores

Los contratos deben alinearse con la Política de Seguridad. Requieren:
- Inventario de contratos con contrapartes técnicas, plazos y fechas de vencimiento/renovación
- Identificación de riesgos de cadena de suministro cibernética
- Proceso de evaluación, monitoreo, revisión y auditoría de proveedores (con SLAs)

**Contratación de servicios en la nube** — el acuerdo de servicio debe incluir:
- Protección de la información al término del contrato
- Revisiones periódicas de cumplimiento técnico y seguridad
- Auditorías periódicas cuyos resultados se comuniquen al OAE
- Recolección, mantención y protección de evidencia (logs y hallazgos de auditoría)
- Modelo de Responsabilidades Compartidas conforme a Convenio Marco o Bases respectivas

---

### Función de Protección

#### Gestión de servidores

| Aspecto | Requisito |
|---------|-----------|
| Administración | Roles y responsabilidades definidos; protocolo de asignación/revocación de privilegios |
| Registro | Eventos de autenticación y acciones: mínimo **12 meses** o lo que la regulación del OAE obligue |
| Separación de entornos | Producción, pruebas, preproducción y desarrollo deben operar de forma independiente y aislada |
| Acceso a servidores | Solo mediante redes seguras (VPN) con llaves criptográficas (SSH) |
| Configuración | No usar configuración de fábrica; documentar formalmente |
| Sincronización horaria | Hora oficial chilena según DS N°25/1966 (SHOA) |
| Gestión de capacidad | Revisión continua de recursos HW y SW |
| Redundancia | Probada con frecuencia; garantiza disponibilidad ante eventos disruptivos |
| Actualización de aplicaciones | Parches vigentes, licenciamiento vigente, política de actualizaciones definida |
| Mantenimiento | Solo personal autorizado; uso de VPN/llaves para mantenimiento remoto; registro de cada mantención |
| Actualización de software | Solo actualizaciones autorizadas por el responsable de activos, probadas y ejecutadas por usuario con competencias técnicas. Plan de vuelta atrás obligatorio |

#### Gestión de redes

- Separación de entornos en redes
- Monitoreo de eventos y anomalías
- Control de acceso: solo personal autorizado (funcionarios/honorarios/proveedores); sistemas críticos requieren autenticación multifactor (2FA o similar)
- VPN obligatoria para conexiones externas; recomendada autenticación OTP adicional
- Monitoreo continuo de puertos, protocolos y servicios
- Firewall actualizado con configuración adaptada al OAE (nunca de fábrica)

#### Gestión de credenciales, privilegios y contraseñas

- Procedimientos formales para otorgamiento y revocamiento de accesos
- Registro continuo de accesos con privilegios elevados
- Modelo de roles (no asignación directa a usuarios individuales)
- Contraseñas: mínimo 10 caracteres, o prohibir claves de diccionarios/brechas públicas
- Contraseñas siempre cifradas (OneWay Function); nunca en texto legible
- No forzar cambio periódico salvo sospecha de acceso no autorizado
- Autenticación multifactor para sistemas con información personal identificable (PII)
- Comunicación de autenticaciones siempre cifrada; credenciales encriptadas
- Nuevas credenciales: no entregar juntos usuario y contraseña; forzar cambio en primer uso

#### Concienciación y formación

Cada OAE debe mantener un plan anual de capacitación que incluya:
- Campañas, recordatorios, folletos (con registro de actividades)
- Alcance de responsabilidades de cada funcionario/honorario
- Declaración del impacto potencial de fallas de seguridad
- Metodología de manejo y reporte de incidentes
- Buenas prácticas en resguardo de información y contraseñas

El plan se revisa anualmente y se activa ante nuevos ingresos o cambios de función.

---

### Seguridad de los datos

Aplica a todos los datos del OAE, tengan o no carácter personal. Para datos personales, también aplica Ley N°19.628 (o su reemplazo).

#### Encriptación y criptografía

Objetivos: confidencialidad, integridad/autenticidad, autenticación de procesos.

| Estándar | Tipo | Uso |
|---------|------|-----|
| AES (128/192/256 bits) | Simétrico | Cifrado de datos; no incluye intercambio de llaves seguro |
| RSA | Asimétrico | Llave pública cifra, llave privada descifra |
| SHA-2 / SHA-3 | Hash | Protección de contraseñas (NO usar SHA-1) |

#### Mecanismos de eliminación de datos

Procedimientos formales para eliminación segura. Considerar tiempos reglamentarios de retención (auditorías, legal).

#### Interoperabilidad, intercambio y transferencia de datos

- Cifrado de punto a punto; protocolo no obsoleto
- Autenticación segura de nodos y servicios (conforme Norma Técnica de Interoperabilidad)
- Información personal y sensible: cifrado de nivel alto
- Procedimientos formales para responsabilidades en envíos, recepciones y transmisiones
- Conformidad con Norma Técnica de Interoperabilidad y directrices SGD

---

### Procesos y procedimientos para proteger la información

#### Desarrollo seguro

- Personal capacitado periódicamente en seguridad
- Ambientes separados: desarrollo, testing, producción (equipo de desarrollo sin acceso a producción, o acceso controlado/temporal con registro)
- Repositorios de código con mecanismos de seguridad
- Metodologías de desarrollo seguro (ej. OWASP)
- Requisitos mínimos de seguridad definidos desde el inicio del ciclo de desarrollo
- Hitos de seguridad periódicos: ethical hacking, análisis automatizados, revisión de código — antes del paso a producción
- Herramientas de análisis de código automatizadas para detección de vulnerabilidades previo a producción

#### Control de cambios

Todo cambio sobre plataformas debe incluir:
- Registro de actividades ejecutadas
- Autorización y pruebas previas (pull requests aprobados, tests unitarios)
- Evaluación del riesgo para seguridad de la información
- Plan de vuelta atrás (rollback)
- Proceso de solución rápida (hotfix) para vulnerabilidades urgentes
- Gestores de versionamiento para recuperar estados anteriores

#### Gestión de respaldos

- Frecuencia definida y documentada conforme al plan de continuidad
- Pruebas de integridad de cada respaldo (incluyendo verificación del medio de almacenamiento)
- Procedimiento de restauración documentado; verificar integridad tras restauración exitosa
- Almacenamiento en locación geográfica **distinta** al servidor de operación
- Mismas medidas de protección física/lógica que el servidor
- Respaldos cifrados (conforme sección de controles criptográficos)

#### Gestión de vulnerabilidades técnicas

- Procedimiento con líneas de acción por rol, tiempo de reacción y nivel de criticidad
- Medidas correctivas: desde parches hasta controles, enmarcadas en gestión de cambios o respuesta a incidentes
- Resolución oportuna; las medidas se aplican según urgencia de la vulnerabilidad

#### Plan de continuidad

- Constituir "Equipo de Respuesta a Incidentes de Seguridad Informática" (Art. 24 lit. d, Ley Marco de Ciberseguridad)
- Conocer nivel de riesgo tolerable y tiempo máximo de recuperación por plataforma
- Planes de respuesta y recuperación por plataforma
- Planes de prueba para servicios esenciales

#### Procesos de recursos humanos

Cláusulas de seguridad en nombramientos y convenios que incluyan:
- Compromiso de confidencialidad y no divulgación
- Responsabilidades sobre datos personales y propiedad intelectual
- Responsabilidad sobre clasificación de información
- Sanciones ante omisión de requisitos de seguridad

Cláusulas vigentes mientras dure el contrato/convenio; pueden extenderse según grado de confidencialidad.

---

### Registro de eventos

Los registros de actividad deben contener (cuando aplique):
- Identificación del usuario y origen (IP, nombre usuario)
- Registro horario del acceso
- Número de intentos fallidos y exitosos
- Todas las acciones y transacciones realizadas
- Información a la cual se accedió

---

### Función de Detección

#### Análisis de eventos

Monitoreo continuo incluyendo: entorno físico/lógico, actividades de personal y proveedores, código malicioso, amenazas y vulnerabilidades.

Cada evento analizado debe incluir:
- Identificación de causa de origen
- Posible motivo y correlación con eventos anteriores
- Estimación del impacto potencial y nivel de riesgo
- Herramientas de correlación de logs y alertas tempranas
- Separación entre eventos dentro del nivel de riesgo tolerable y eventos que requieren análisis en profundidad

#### Gestión del código malicioso

- Mecanismos de protección instalados y actualizados automáticamente y con frecuencia
- Revisiones rutinarias en plataformas y redes (archivos o modificaciones sin autorización)
- Plan de continuidad incluye recuperación ante eventos de código malicioso

#### Monitoreo de la red

- Solo acceden redes los actores expresamente autorizados y previamente formalizados
- Sistema de cortafuegos complementario a la administración de red (nunca configuración de fábrica)
- Mecanismos de registro y monitoreo de tráfico (uso normal vs. posibles eventos)
- Todos los puertos cerrados por defecto; apertura solo cuando estrictamente necesario y con cierre posterior
- Segregación de redes según política de control de accesos y clasificación de información

#### Proceso de detección

Actividades que permitan:
- Establecer roles y responsabilidades en detección, comunicación y clasificación de eventos
- Cumplir con requisitos de seguridad de la Política y el análisis de riesgos
- Comunicar eventos detectados a todos los interesados
- Mediciones continuas de efectividad para mejora continua

---

### Función de Respuesta

#### Planes de respuesta ante incidentes

El plan se activa una vez **confirmado** un incidente. Debe abordar:

1. Notificar a la ANCi y al regulador cuando corresponda
2. Identificar activos, controles, roles y responsabilidades involucrados
3. Evaluar impacto del incidente
4. Determinar si la red fue comprometida (incluidos ataques de día cero y APT)
5. Determinar si datos sensibles fueron comprometidos (riesgo para titulares)
6. Evaluar daño a servidores
7. **Acciones de mitigación:** contener afectaciones y aislar el incidente
8. **Acciones de restablecimiento:**
   - Erradicar el riesgo de acceso del atacante
   - Actualizar parches, blindar infraestructura, cerrar accesos, modificar contraseñas comprometidas
   - Erradicar archivos infectados; reconfigurar o reemplazar hardware si necesario
   - Restaurar nivel de servicio al estado anterior al incidente
   - Verificar exfiltración/pérdida de datos una vez recuperada la integridad, disponibilidad y confidencialidad
9. Canales de comunicación definidos durante mitigación y recuperación
10. Preparar y publicar declaraciones internas y públicas (naturaleza, causas, alcance, pasos, actualizaciones)
11. Preservar evidencias para análisis forense posterior (artefactos, logs, detalles de vulneración)
12. Registro y seguimiento completo del incidente (hora, datos, tipo, descubridor, ubicación, alcance)
13. Informe de respuesta a incidentes
14. Mejora continua a partir de lecciones aprendidas y análisis de causa raíz

#### Análisis forense

Posterior al incidente, realizar análisis que:
- Recopile información y evidencia preservando la cadena de custodia
- Resuelva la vulnerabilidad causante
- Actualice procedimientos de respuesta con lecciones aprendidas

---

### Función de Recuperación

Implementar todas las acciones, procesos y procedimientos para restablecer cualquier capacidad, plataforma, sistema, servidor, red o servicio afectado.

#### Gestión de incidentes — proceso obligatorio

Etapas mínimas:
1. Usar escala de la Guía de Notificación de Incidentes de ANCi
2. Determinar activos involucrados e impacto sobre servicios
3. Activar planes de respuesta y, si corresponde, plan de continuidad operativa
4. Notificar al CSIRT de Gobierno según la Guía de Notificación de Incidentes

---

## Revisión y actualización

La guía debe revisarse al menos cada año. Se deja registro de todas las versiones.

| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0 | 24/03/2025 | Versión inicial |
