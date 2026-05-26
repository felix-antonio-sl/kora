---
_manifest:
  urn: urn:tde:kb:guia-tecnica-metadatos-documentos-expedientes
  provenance:
    source: https://wikiguias.digital.gob.cl/guias/Metadatos_Expediente_Electrónico
version: 1.0.0
status: published
tags:
- tde
- lineamientos-guias
- expediente-electronico
- guia-tecnica
- metadatos
- documentos-electronicos
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:guia-tecnica-metadatos-documentos-expedientes
---

# Guía Técnica de Metadatos para Documentos y Expedientes Electrónicos

**Norma Técnica:** Documentos y Expedientes Electrónicos — **Versión BORRADOR**

---

## Metadatos para la gestión documental en el Estado

Los metadatos son elementos indivisibles de la identidad de expedientes y documentos electrónicos. Describen estructura, contenido y contexto (autor, fecha, lugar, protocolos de representación). Su objetivo: garantizar **disponibilidad, recuperación, accesibilidad, conservación e interoperabilidad** del documento con otros sistemas.

Los metadatos son de registro permanente mientras exista el expediente o documento en resguardo o custodia institucional, y para su preservación a largo plazo en el Archivo Nacional. Deben conservarse sin sobrescribirse en las plataformas de resguardo institucional.

Cada institución puede implementar el registro en repositorios documentales, bases de datos u otras soluciones de gestión institucional. Es **obligatoria** la existencia de estos metadatos y su generación en formato estandarizado para la interoperabilidad.

---

## 3. Metadatos de expedientes y documentos electrónicos

### Estructura del esquema

El esquema considera 4 entidades en modelo entidad-relación:
1. **Documento**
2. **Expediente**
3. **Actor:** institución, persona física o jurídica responsable o involucrada en creación, producción, custodia o gestión.
4. **Relación:** asociación entre dos o más entidades con relevancia en el contexto de gestión.

**Conteo total del esquema:**

| Tipo | Expedientes | Documentos |
|------|-------------|------------|
| Total elementos | 29 | 46 |
| Obligatorios | 18 | 12 |
| Condicionales | 5 | 16 |
| Sugeridos | 6 | 18 |

**Convención de colores:**
- **Verde:** obligatorios (toda creación del conjunto de metadatos).
- **Amarillo:** condicionales (obligatorios cuando se cumple una condición específica).
- **Blanco:** sugeridos (uso a criterio del organismo según necesidades descriptivas).

**Marcas especiales:**
- **AN:** requerido por el Archivo Nacional para transferencia digital.
- **MU:** metadato múltiple; pueden incorporarse múltiples registros del campo.

### 3.1. Metadatos para expedientes electrónicos (Tabla 1)

Los metadatos se agrupan en 8 grupos:

| Código | N° | Sub N° | Rótulo | Definición | Obligación | AN | MU |
|--------|-----|---------|--------|-----------|-----------|----|----|
| MGDEE1_1 | 1 | 1.1 | Identificador de expediente | ID único asignado automáticamente al expediente en el sistema de gestión documental. | **Obligatorio** | SI | — |
| MGDEE1_2 | 1 | 1.2 | Código serie | Código serie del cuadro de clasificación documental del OAE. | Sugerido | NO | — |
| MGDEE1_3 | 1 | 1.3 | Número del expediente | Número de orden interno dentro de una serie documental. | Sugerido | NO | — |
| MGDEE1_4 | 1 | 1.4 | Estado | Estado del proceso del expediente (fase de ciclo de vida). | Sugerido | NO | — |
| MGDEE1_5 | 1 | 1.5 | Título del expediente | Palabra, frase o caracteres para denominar el expediente (formal o atribuido). | **Obligatorio** | SI | — |
| MGDEE2_1 | 2 | 2.1 | Resumen | Relato sintético del contenido global del expediente. | Sugerido | NO | — |
| MGDEE2_2 | 2 | 2.2 | Asunto del expediente | Materia o tema del expediente, reflejo de los fines u objetivos de la tramitación. | **Obligatorio** | SI | — |
| MGDEE3_1 | 3 | 3.1 | Fecha de creación | Fecha en que es generado el expediente (formato ISO 8601: aaaa-mm-dd hh:mm:ss). | **Obligatorio** | SI | — |
| MGDEE3_2 | 3 | 3.2 | Fecha de finalización | Fecha de finalización o cierre del expediente (formato ISO 8601). | **Obligatorio** | SI | — |
| MGDEE4_1 | 4 | 4.1 | Mecanismo de incorporación | Mecanismo de incorporación al sistema de gestión documental (manual, carga masiva, mixto u otro). | **Obligatorio** | NO | — |
| MGDEE4_2 | 4 | 4.2 | URI de expediente | Enlace al expediente en repositorio documental o plataforma estandarizada. | **Obligatorio** | NO | — |
| MGDEE51_1 | 5 | 5.1.1 | Código de OAE productor | Identificación del OAE que genera el expediente (codificación GESCODE). | **Obligatorio** | SI | — |
| MGDEE51_2 | 5 | 5.1.2 | Nombre OAE productor | Nombre institucional si el OAE no está en el codificador. | Condicional | SI | — |
| MGDEE51_3 | 5 | 5.1.3 | Tipo Relación OAE | Relación entre el expediente y el OAE (ver lista N°4). | **Obligatorio** | NO | SI |
| MGDEE51_4 | 5 | 5.1.4 | Código de OAE relacionado | Identificación del OAE que custodia, gestiona o respalda el expediente (GESCODE). | **Obligatorio** | NO | SI |
| MGDEE51_5 | 5 | 5.1.5 | Nombre OAE relacionado | Nombre institucional si el OAE no está en GESCODE. | Condicional | NO | SI |
| MGDEE52_1 | 5 | 5.2.1 | Tipo de relación con otros actores | Tipo de relación entre el actor (persona natural o jurídica) y el expediente. Obligatorio para identificación de interesados. | **Obligatorio** | NO | SI |
| MGDEE52_2 | 5 | 5.2.2 | Tipo de actor relacionado | Tipo de actor relacionado que indica el tipo de identificación requerido. Obligatorio para identificación de interesados. | **Obligatorio** | NO | SI |
| MGDEE52_3 | 5 | 5.2.3 | RUN/RUT relacionado | RUN/RUT/Pasaporte del actor relacionado. Obligatorio para identificación de interesados. | Condicional | NO | SI |
| MGDEE52_4 | 5 | 5.2.4 | Nombre del actor relacionado | Nombre de la persona natural o jurídica si no se cuenta con RUN/RUT. Obligatorio para interesados sin identificación. | Condicional | NO | SI |
| MGDEE53_1 | 5 | 5.3.1 | Identificador de expediente/documento vinculado | ID del expediente o documento que conforma el índice del presente expediente. | **Obligatorio** | SI | SI |
| MGDEE53_2 | 5 | 5.3.2 | Fecha de incorporación del expediente/documento | Fecha y hora de incorporación del documento/expediente vinculado (ISO 8601). | **Obligatorio** | SI | SI |
| MGDEE6_1 | 6 | 6.1 | Nivel de acceso | Indicación relativa al acceso y consulta del expediente (ver lista N°7). Por defecto: 1 - Público. | **Obligatorio** | SI | — |
| MGDEE6_2 | 6 | 6.2 | Fecha fin restricción | Fecha que determina el desbloqueo del expediente. | Sugerido | NO | — |
| MGDEE6_3 | 6 | 6.3 | Texto Advertencia | Texto a presentar cuando un usuario intente acceder a información restringida. | Sugerido | NO | — |
| MGDEE6_4 | 6 | 6.4 | Información de carácter sensible y/o privada | Marca si el expediente contiene información sensible. Lista controlada [1-SI / 2-NO]. Por defecto: 2 (NO). | **Obligatorio** | NO | — |
| MGDEE7_1 | 7 | 7.1 | Código CPAT asociado | Código del procedimiento administrativo en CPAT. | **Obligatorio** | NO | — |
| MGDEE7_2 | 7 | 7.2 | Nombre de procedimiento administrativo | Nombre del PA si no está en CPAT. | Condicional | NO | — |
| MGDEE8_1 | 8 | 8.1 | Versión MDGEE | Versión del esquema de metadatos utilizado. Por defecto: 001. | **Obligatorio** | NO | — |

### 3.2. Metadatos para documentos electrónicos (Tabla 2)

Los metadatos se agrupan en 10 grupos:

| Código | N° | Sub N° | Rótulo | Definición | Obligación | AN | MU |
|--------|-----|---------|--------|-----------|-----------|----|----|
| MGDDE1_1 | 1 | 1.1 | Identificador | Código único asignado automáticamente al documento en el sistema. | **Obligatorio** | SI | — |
| MGDDE1_6 (serie) | 1 | 1.2 | Código serie | Código serie del cuadro de clasificación del OAE. Obligatorio para transferencia al AN. | Condicional | SI | — |
| MGDDE1_3 | 1 | 1.3 | Número del documento | Número de orden interno dentro de una serie documental. | Sugerido | NO | — |
| MGDDE1_4 | 1 | 1.4 | Estado | Estado de generación del documento. | Sugerido | NO | — |
| MGDDE1_5 | 1 | 1.5 | Versión | Número de versión del documento. | Sugerido | NO | — |
| MGDDE1_6 | 1 | 1.6 | Título del documento | Palabra, frase o caracteres para denominar el documento (formal o atribuido). | **Obligatorio** | SI | — |
| MGDDE1_7 | 1 | 1.7 | Resolución de captura | Nivel de resolución de la imagen. Obligatorio para microformas. | Condicional | SI | — |
| MGDDE1_8 | 1 | 1.8 | Nombre archivo asociado | Nombre del archivo digital referenciado. | Sugerido | NO | — |
| MGDDE2_1 | 2 | 2.1 | Tamaño | Volumen del documento en Kb. | Sugerido | NO | — |
| MGDDE2_2 | 2 | 2.2 | Cantidad de páginas o extensión | N° total de páginas. Obligatorio para microformas. | Condicional | SI | — |
| MGDDE2_3 | 2 | 2.3 | Formato | Estructura/extensión del archivo electrónico. | Sugerido | NO | — |
| MGDDE2_4 | 2 | 2.4 | Nombre y versión del software | Programa informático utilizado para generar el documento. | Sugerido | NO | — |
| MGDDE3_1 | 3 | 3.1 | Resumen | Relato sintético del contenido global del documento. | Sugerido | NO | — |
| MGDDE3_2 | 3 | 3.2 | Palabras clave del documento | Materias/temas del documento expresados en palabras representativas. | **Obligatorio** | SI | — |
| MGDDE3_3 | 3 | 3.3 | Idioma | Idioma en que está generado el documento. | Sugerido | NO | — |
| MGDDE3_4 | 3 | 3.4 | Comunas | Identificación geográfica del origen/residencia del OAE que resguarda el documento. | Sugerido | NO | — |
| MGDDE4_1 | 4 | 4.1 | Fecha de creación | Fecha de generación del documento (ISO 8601). | **Obligatorio** | SI | — |
| MGDDE4_2 | 4 | 4.2 | Fecha de modificación | Fecha de última modificación (ISO 8601). | Obligatorio | NO | — |
| MGDDE4_3 | 4 | 4.3 | Fecha de captura | Fecha de incorporación al repositorio (para documentos externos o microformas). Obligatorio para microformas. | Condicional | SI | — |
| MGDDE4_4 | 4 | 4.4 | Cobertura temporal | Tiempo (fechas) al que hace referencia el acto del documento. | Sugerido | NO | — |
| MGDDE5_1 | 5 | 5.1 | Tipo documental | Nombre/código del tipo documental estandarizado (ver lista N°1). Por defecto: 3 (Antecedente). Obligatorio si se cuenta con tipificación. | Condicional | NO | — |
| MGDDE5_2 | 5 | 5.2 | Origen del documento | Origen de incorporación al repositorio institucional. Obligatorio para microformas. | Condicional | SI | — |
| MGDDE5_3 | 5 | 5.3 | Mecanismo de incorporación | Mecanismo de incorporación al repositorio (ver lista N°2). Por defecto: 2 - Digital. | **Obligatorio** | NO | — |
| MGDDE5_4 | 5 | 5.4 | URI documento externo | Enlace a documento en repositorio externo. Obligatorio para documentos externos referenciados. | Condicional | SI | — |
| MGDDE5_5 | 5 | 5.5 | Ubicación física del documento referenciado | Código de almacenamiento físico del documento físico referenciado. Obligatorio para documentos físicos referenciados (expediente híbrido o microforma). | Condicional | NO | — |
| MGDDE5_6 | 5 | 5.6 | Estado de conservación microforma | Estado del documento original a partir del cual se generó la microforma (ver lista N°3). Por defecto: 1 (Muy Bueno). Obligatorio para microformas. | Condicional | SI | — |
| MGDDE5_7 | 5 | 5.7 | Disposición | Destino planificado del documento por normativa o valoración documental. | Sugerido | NO | — |
| MGDDE61_1 | 6 | 6.1.1 | Código OAE | Identificación del OAE que genera, gestiona o custodia el documento. | **Obligatorio** | SI | SI |
| MGDDE61_2 | 6 | 6.1.2 | Nombre OAE | Nombre institucional si no se cuenta con el código OAE. Obligatorio si no se identifica por código. | Condicional | SI | SI |
| MGDDE61_3 | 6 | 6.1.3 | Tipo de relación entre documento y OAE | Relación entre el documento y el OAE (gestionador, autor institucional, custodia). Al menos: autor institucional + custodia. | **Obligatorio** | SI | SI |
| MGDDE62_1 | 6 | 6.2.1 | Tipo de relación con otros actores | Tipo de relación entre el actor y el documento. Al menos: autor(es)/creador(es). Obligatorio si se registra relación. | Condicional | SI | SI |
| MGDDE62_2 | 6 | 6.2.2 | Tipo de actor relacionado | Tipo de actor relacionado (ver lista N°6). Obligatorio si se registra relación. | Condicional | NO | SI |
| MGDDE62_3 | 6 | 6.2.3 | Identificación de actor relacionado | RUN/RUT/Pasaporte del actor. Obligatorio si se registra relación. | Condicional | SI | SI |
| MGDDE62_4 | 6 | 6.2.4 | Nombre del actor relacionado | Nombre si no se cuenta con RUN. Obligatorio si se registra relación. | Condicional | NO | SI |
| MGDDE7_1 | 7 | 7.1 | Nivel de acceso | Acceso y consulta de los documentos (ver lista N°7). Por defecto: 1 (Público). | **Obligatorio** | SI | — |
| MGDDE7_2 | 7 | 7.2 | Fecha fin restricción | Fecha hasta la que se presenta el texto de advertencia. | Sugerido | NO | — |
| MGDDE7_3 | 7 | 7.3 | Texto Advertencia | Texto a presentar cuando usuario intente acceder a información restringida. | Sugerido | NO | — |
| MGDDE7_4 | 7 | 7.4 | Información de carácter sensible | Marca si el documento contiene información sensible. Lista [1-SI / 2-NO]. Por defecto: 2 (NO). | **Obligatorio** | NO | — |
| MGDDE8_1 | 8 | 8.1 | Tipo Firma | Tipo de firma electrónica (avanzada/simple). Por defecto: 1 (AVANZADA). Ver lista controlada. | Sugerido | NO | SI |
| MGDDE8_2 | 8 | 8.2 | Proveedor | Proveedor del servicio de firma electrónica. | Sugerido | NO | SI |
| MGDDE8_3 | 8 | 8.3 | Firma Electrónica Avanzada | Indica si el documento tiene FEA. Lista [1-SI / 2-NO]. Por defecto: 2 (NO). | **Obligatorio** | NO | — |
| MGDDE84_1 | 8 | 8.4.1 | Nombre/Cargo Representación | Nombre y cargo de la persona que firma. | Sugerido | NO | SI |
| MGDDE84_2 | 8 | 8.4.2 | RUN firmante | Identificación de la persona que firma. | Sugerido | NO | SI |
| MGDDE9_1 | 9 | 9.1 | Código procedimiento administrativo asociado | Código CPAT del PA asociado específicamente a la creación del documento. Obligatorio si vinculado a un PA específico. | Condicional | NO | — |
| MGDDE9_2 | 9 | 9.2 | Nombre procedimiento administrativo asociado | Nombre del PA si no está en CPAT. Obligatorio si vinculado a un PA no codificado en CPAT. | Condicional | NO | — |
| MGDDE10 | 10 | 10.1 | Versión MGDDE | Versión de la Guía Técnica de Metadatos utilizada. Por defecto: 1. | **Obligatorio** | NO | — |

---

## 4. Listas controladas de metadatos

Las listas controladas estarán disponibles en el **Gestor de Códigos (GESCODE)** del Estado.

### Lista 1 — Tipo Documental (MGDDE5_1)

42 tipos documentales estandarizados, incluyendo: Acta, Acuerdo, Antecedente, Autorización, Base, Boleta, Carta, Certificado, Circular, Citación, Convenio, Constancia, Contrato, Declaración, Decreto, Denuncia, Dictamen, Estado de situación, Estudio, Expediente administrativo, Ficha, Informe, Instructivo, Mandato, Memorándum, Minuta, Nómina, Nota, Notificación, Oficio, Ordenanza, Prospecto, Querella, Reclamo, Registro, Resolución, Respuesta, Retrocompra, Sentencia, Solicitud, Términos de referencia, Transcripción.

### Lista 2 — Mecanismo de incorporación del documento (MGDDE5_3)

1. Físico
2. Digital
3. Digitalización

### Lista 3 — Estado de conservación microforma (MGDDE5_6)

| Valor | Estado | Descripción |
|-------|--------|-------------|
| 1 | Muy Bueno | Sin deterioros; fácil manipulación. |
| 2 | Bueno | Deterioros menores que no comprometen información; fácil manipulación. |
| 3 | Regular | Hojas/cuadernillos sueltos; manchas por humedad sin comprometer información; rasgados menores (<50% superficie); restauraciones anteriores no especializadas; deterioros de bordes (hasta 50% de fojas). Manipular con cuidado. |
| 4 | Malo | Rasgados y faltantes mayores (≥50%); tintas oxidadas con aureolas y roturas (≥50%); daño biológico (hongos, insectos); aureolas/manchas significativas (≥50%). Manipular con mucho cuidado. |
| 5 | Muy Malo | Deterioros extremos; volumen puede estar incompleto; humedad/microorganismos activos/daños graves por insectos (>50%); oxidación de tintas en todo el soporte. Manipulación con extremo cuidado. |

### Lista 4 — Tipo Relación OAE (MGDEE51_3 / MGDDE61_3)

1. Autor institucional
2. Destinatario
3. Productor / generador
4. Custodia

### Lista 5 — Tipo de relación con otros actores (MGDEE52_1 / MGDDE62_1)

1. Responsable
2. Interesado
3. Autor/creador
4. Referido
5. Destinatario
6. Ministro de Fe

### Lista 6 — Tipo de actor relacionado (MGDEE52_2 / MGDDE62_2)

1. Ciudadano
2. Extranjero
3. Institución privada
4. Funcionario

### Lista 7 — Nivel de acceso (MGDEE6_1 / MGDDE7_1)

1. Público
2. Restringido
3. Secreto
4. Reservado

### Lista 8 — Origen del documento (MGDDE5_2)

1. Repositorio Externo
2. Interoperabilidad
3. Plataforma ciudadana
4. Repositorio Ciudadano

---

## Especificaciones técnicas de campos

> Complemento a las tablas §3.1 y §3.2. Atributos de implementación por campo: tipo de dato, forma de ingreso, valor por defecto y restricciones técnicas.

### Expedientes electrónicos

| Código | Tipo dato | Ingreso | Por defecto | Comentario técnico | Ejemplo |
|--------|-----------|---------|-------------|-------------------|---------|
| MGDEE1_1 | Alfanumérico | Automático | — | Asegurar unicidad, persistencia y estandarización de la codificación. | EXP-20230925-001 |
| MGDEE1_2 | Alfanumérico | Automático | — | — | — |
| MGDEE1_3 | Alfanumérico | Automático | — | — | — |
| MGDEE1_4 | Alfanumérico | Automático/manual | — | El estado es un registro del proceso; puede referirse al estado de su creación o la fase de vida del expediente. | — |
| MGDEE1_5 | Texto | Manual | — | Destinar el uso de mayúsculas únicamente para el inicio del título y para nombres propios. | Asignación de presupuesto para compra de insumos. |
| MGDEE2_1 | Texto | Manual | — | — | — |
| MGDEE2_2 | Texto | Manual | — | Este dato es un ámbito amplio que representa el contenido del expediente. | Compra de insumos tecnológicos para el año 2023. |
| MGDEE3_1 | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | Automático | — | Debe tener posibilidad de ser modificado, pero dicho cambio debe quedar registrado. | 2023-20-10:11:56:57 |
| MGDEE3_2 | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | Automático | — | Debe tener posibilidad de ser modificado, pero dicho cambio debe quedar registrado. | 2023-20-11:16:56:57 |
| MGDEE4_1 | Texto | Automático/manual | 1 | — | 1 (Incorporación manual) |
| MGDEE4_2 | URI | Automático | — | La institución podrá hacer uso de sus propios servicios de URIs persistentes y/o utilizar la plataforma de URIs persistente que el Estado disponga. | https://dominio-institución/servicio-persistente/20.500.13034/401 |
| MGDEE51_1 | Numérico | Automático | — | La identificación del OAE generador es un valor requerido por AN. | 46 (Gobierno Regional de la Región de La Araucanía) |
| MGDEE51_2 | Texto | Automático/manual | — | — | Gobierno Regional de la Región de La Araucanía |
| MGDEE51_3 | Numérico | Automático/manual | 1 (custodia) | Es obligatorio al menos identificar el OAE responsable de la custodia del expediente. | 1 (Custodia) |
| MGDEE51_4 | Numérico | Automático/manual | — | Es obligatorio al menos identificar el OAE responsable de la custodia del expediente. | 46 (Gobierno Regional de la Región de La Araucanía) |
| MGDEE51_5 | Texto | Automático/manual | — | — | Gobierno Regional de la Región de La Araucanía |
| MGDEE52_1 | Numérico | Automático/manual | 1 - Responsable | Es obligatorio asignar al menos un funcionario responsable de la apertura del expediente. Al ser campo múltiple es esperable incorporar los interesados u otros tipos de relaciones. | 2 (Interesado) |
| MGDEE52_2 | Numérico | Automático/manual | 4 - Funcionario | Al igual que el metadato anterior es obligatorio especificar el funcionario responsable inicial del expediente. | 1 (Ciudadano) |
| MGDEE52_3 | Alfanumérico | Automático/manual | Formato RUN/RUT | — | 60100003-2 |
| MGDEE52_4 | Texto | Automático/manual | — | — | Entel Chile / Julian Santelices Machuca |
| MGDEE53_1 | Alfanumérico | Automático | — | Es requerido en caso que el documento forme parte de un expediente. | — |
| MGDEE53_2 | Alfanumérico | Automático | — | — | 2023-20-11:16:56:57 |
| MGDEE6_1 | Numérico | Manual | 1 - Público | Codificación numérica y rótulo conocido. | 1 (acceso público) |
| MGDEE6_2 | Fecha | Manual | — | — | — |
| MGDEE6_3 | Texto | Manual | — | — | — |
| MGDEE6_4 | Numérico | Manual | 2 (NO) | Una posibilidad que puede abordar cada OAE es identificar categorías controladas para información sensible y/o privada. | 2 |
| MGDEE7_1 | Alfanumérico | Automático | — | Disponibilizado por el Catálogo de Procedimientos Administrativos y Tramitaciones (CPAT). | 5076 (PA-UNI00002-00001- Convalidación de Programa de Perfeccionamiento Académico) |
| MGDEE7_2 | Alfanumérico | Manual | — | — | Convalidación de Programa de Perfeccionamiento Académico |
| MGDEE8_1 | Numérico | Automático | 001 | — | 001 |

### Documentos electrónicos

| Código | Tipo dato | Ingreso | Por defecto | Comentario técnico | Ejemplo |
|--------|-----------|---------|-------------|-------------------|---------|
| MGDDE1_1 | Alfanumérico | Automático | — | Asegurar unicidad, persistencia y estandarización de la codificación. | DOCU-20230925-001-XYZ |
| MGDDE1_6 (serie) | Alfanumérico | Manual/automático | — | — | — |
| MGDDE1_3 | Alfanumérico | Manual/automático | — | — | — |
| MGDDE1_4 | Alfanumérico | Manual/automático | — | — | — |
| MGDDE1_5 | Alfanumérico | Manual/automático | — | — | 1.1 |
| MGDDE1_6 | Texto | Manual | — | Destinar el uso de mayúsculas únicamente para el inicio del título y para nombres propios. | Resolución exenta asigna presupuesto para compra de insumos |
| MGDDE1_7 | — | Automático | — | Se refiere a la cantidad de píxeles que la imagen contiene, expresada como píxeles en horizontal por vertical. Obligatorio para Microformas. | 3000x2000 |
| MGDDE1_8 | — | Automático | — | — | — |
| MGDDE2_1 | — | Automático | — | — | — |
| MGDDE2_2 | Numérico | Automático | — | Obligatorio para documentos de tipo Microforma. | 104 |
| MGDDE2_3 | Texto | Automático | — | — | pdf |
| MGDDE2_4 | Texto | Automático | — | — | pdf |
| MGDDE3_1 | Texto | Manual | — | — | — |
| MGDDE3_2 | Texto | Manual | — | Palabras cortas, simples o compuestas en una frase breve, que expresen la información más relevante del contenido del documento. | Resolución de compra tecnológica - Adquisición de licencias de software |
| MGDDE3_3 | Texto | Manual | — | — | — |
| MGDDE3_4 | Numérico | Automático | — | — | — |
| MGDDE4_1 | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | Automático | — | Metadato posible de ser modificado. Debe quedar registrado el historial de modificaciones. | 2023-20-11:16:56:57 |
| MGDDE4_2 | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | Automático | — | Metadato posible de ser modificado. Debe quedar registrado el historial de modificaciones. | 2023-20-11:16:56:57 |
| MGDDE4_3 | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | Automático/manual | — | — | 2023-20-11:16:56:57 |
| MGDDE4_4 | Fecha | Automático/manual | — | — | 2023-20-11:16:56:57 |
| MGDDE5_1 | Numérico | Manual | 3 (Antecedente) | El valor a seleccionar desde lista controlada dependerá de un término genérico. | 30 (Oficio) |
| MGDDE5_2 | Numérico | Automático | 1 | — | 1 (repositorio externo) |
| MGDDE5_3 | Numérico | Automático | 2. Digital | — | 2 (digital) |
| MGDDE5_4 | Alfanumérico | Automático | — | En caso de tratarse de un repositorio externo se debe utilizar una URI persistente del documento. | http://bibliotecadigital.dipres.gob.cl/handle/11626/19183 |
| MGDDE5_5 | Alfanumérico | Automático | — | Cada institución define sus políticas de codificación. | space_40_archivador_20.5.10_oae_33706 |
| MGDDE5_6 | Numérico | Automático | 1 (Muy Bueno) | Es requerido si se trata de un documento microforma. | 1 (Muy Bueno) |
| MGDDE5_7 | Texto | Manual/automático | — | — | Preservación Institucional |
| MGDDE61_1 | Numérico | Automático | — | — | 46 (Gobierno Regional de la Región de La Araucanía) |
| MGDDE61_2 | Alfanumérico | Automático/manual | — | Sólo es obligatorio en caso que no se identifique por el código OAE. | Gobierno Regional de la Región de La Araucanía |
| MGDDE61_3 | Numérico | Automático | 1 (Autor institucional) | Por lo menos debe incorporarse la relación con el autor institucional si corresponde. | 1 (Autor institucional) |
| MGDDE62_1 | Numérico | Automático/manual | 3 (Autor/creador) | Al menos se debe registrar al autor(es)/creador(es) del documento. | 3 |
| MGDDE62_2 | Numérico | Automático | 1 (Ciudadano) | — | 1 |
| MGDDE62_3 | Alfanumérico | Automático/manual | — | — | 677368373-5 |
| MGDDE62_4 | Alfanumérico | Manual | — | — | Entel Chile / Julian Santelices Machuca |
| MGDDE7_1 | Numérico | Manual | 1 (Público) | — | 1 |
| MGDDE7_2 | Fecha | Manual | — | — | — |
| MGDDE7_3 | Texto | Manual | — | — | — |
| MGDDE7_4 | Numérico | Manual | 2 (NO) | — | 1 |
| MGDDE8_1 | Numérico | Automático | 1 (AVANZADA) | — | 2 (SIMPLE) |
| MGDDE8_2 | Texto | Automático | — | — | — |
| MGDDE8_3 | Numérico | Automático | 2 (NO) | — | 1 (SI) |
| MGDDE84_1 | Texto | Automático/manual | — | — | — |
| MGDDE84_2 | Numérico | Manual/automático | — | — | — |
| MGDDE9_1 | Alfanumérico | Automático/manual | — | Disponibilidad por el Catálogo de procedimientos administrativos y trámites. | 5076 (Convalidación de Programa de Perfeccionamiento Académico - PA-UNI00002-00001) |
| MGDDE9_2 | Texto | Manual | — | — | Convalidación de Programa de Perfeccionamiento Académico |
| MGDDE10 | Numérico | Automático | 1 | — | 1 |

---

## Referencias normativas

- ISO 15.489: Information and documentation - Records management - Part 1: General. https://www.iso.org/standard/56639.html
- ISO 23.081: Information and documentation — Records management processes — Metadata for records — Part 1: Principles. Geneva: ISO.
- Archivo Nacional de Chile: Procedimiento para la Transferencia de Documentos en Soporte Papel al Archivo Nacional de Chile, versión 2021.
