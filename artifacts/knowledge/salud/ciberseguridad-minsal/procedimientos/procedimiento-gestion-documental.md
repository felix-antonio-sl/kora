---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-documental
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: 'MINSAL Chile, SGSI Nivel Central. PROS-NC-010 v01 (Octubre 2024). Clasificación:
      Información Pública.'
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- gestion-documental
- control-documentos
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-gestion-documental
  salud:
    minsal_id: PROS-NC-010
    minsal_version: '01'
    fecha_aprobacion: Octubre 2024
    clasificacion: Información Pública
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento de Gestión Documental

**PROS-NC-010 v01, Octubre 2024. Clasificación: Información Pública. Documento Controlado.**

## 1. Disposiciones Generales

### 1.1 Propósito

Establecer un marco de control para la creación, revisión, aprobación, distribución y eliminación de documentos del Sistema de Gestión de Seguridad de la Información (SGSI) del Ministerio de Salud, asegurando la protección y disponibilidad de todo tipo de documento durante su ciclo de vida dentro del alcance del sistema.

### 1.2 Alcance

Abarca todas las etapas del ciclo de vida de los documentos del SGSI, desde su creación hasta su eliminación, garantizando que cada fase cumpla con los controles de seguridad y protección de la información.

Aplicable a todos los funcionarios (planta, contrata, reemplazos y suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para las Subsecretarías de Salud Pública y Redes Asistenciales, en el Nivel Central.

#### Control ISO 27001:2022 asociado

| ID | Control |
|-------|---------|
| 7.5 | Información Documentada |

### 1.3 Terminología

- **Documento Controlado**: Documento afecto a cambios y/o modificaciones, que se identifica y fiscaliza para asegurar que no se utilicen versiones no actualizadas.
- **CISO** (*Chief Information Security Officer*): Encargado de Ciberseguridad y Seguridad de la Información del MINSAL.

### 1.4 Documentos Aplicables

- Política General de Seguridad de la Información y Ciberseguridad.

## 2. Roles y Responsabilidades

### 2.1 Dueño del Proceso de Gestión Documental del SGSI (CISO)

- Responsable de la creación, revisión y validación de la documentación y sus actualizaciones.
- Mantener vigente el maestro de documentos mediante su actualización periódica.
- Encargado de la validación técnica y alineación con estándares de seguridad de la información.
- Encargado de distribuir la documentación a los usuarios y responsables correspondientes.
- Gestionar el control de versiones del maestro de documentos para asegurar su precisión y trazabilidad.

### 2.2 Dueño de Proceso vinculado al Documento (Jefaturas)

- Responsable de solicitar modificaciones o eliminaciones de documentos.
- Responsable de determinar a quién debe llegar el documento redactado.

### 2.3 Encargado de Revisar el Documento (CISO, Comité SGSI, Jefe TIC, Div. Jurídica)

- Revisar el documento luego de su elaboración para detectar errores o mejoras.
- Proponer ajustes o cambios, previa elaboración de acto administrativo (Div. Jurídica).

### 2.4 Encargado de Aprobar el Documento (Jefe TIC, Dirección)

- Dar aprobación a las solicitudes de creación, modificación, eliminación y similares de documentos.
- Elaboración de acto administrativo (Div. Jurídica).
- Aprobación del acto administrativo (Dirección).

## 3. Matriz de Responsabilidades (RACI)

| Actividad | Dueño Proceso Gestión Documental (CISO) | Dueño Proceso vinculado (Jefatura) | Encargado Revisar (CISO, Comité SGSI, Jefe TIC, Div. Jurídica) | Encargado Aprobar (Jefe TIC, Dirección) |
|-----------|:---:|:---:|:---:|:---:|
| Creación de documento | R/A | R/A | | |
| Codificación de documento | R/A | | | |
| Revisión del documento | | | R/A | |
| Aprobación del documento | | | | R/A |
| Actualización en el maestro de documentos | R/A | | | |
| Distribución del documento | R/A, I | I | | |
| Solicitud de modificación | | R/A | | |
| Aprobación de la modificación | | | | R/A |
| Registro de la modificación | R/A | | | |
| Distribución de documento modificado | R/A, I | | | |
| Solicitud de eliminación | R/A | R/A | | |
| Aprobación y eliminación del documento | R/A | | | R/A |
| Comunicación de la eliminación del documento | R/A, I | | | |

**Leyenda**: R = Responsable de Ejecutar | A = Responsable del Resultado | C = Consultado | I = Informado

## 4. Métricas e Indicadores

### 4.1 Actualización Periódica del Maestro (IO1)

| Concepto | Valor |
|----------|-------|
| Cálculo | Meses transcurridos desde última actualización del Maestro |
| Frecuencia | Cada vez que se revisa la actualización del Maestro |
| Umbral Vigente | ≤ 12 Meses |
| Umbral No Vigente | > 12 Meses |

### 4.2 Vigencia de Registros (IO2)

| Concepto | Valor |
|----------|-------|
| Cálculo | Meses transcurridos desde última versión de un documento tipo PROS y PS |
| Frecuencia | Cada vez que se revise o actualice un documento |
| Umbral Vigente | ≤ 24 Meses |
| Umbral No Vigente | > 24 Meses |

## 5. Registros

- Maestro de documentos.
- Actos administrativos aprobatorios.

## 6. Difusión

El contenido de la documentación debe ser accesible y comprensible para todos los usuarios. Canales mínimos de difusión:

- Publicación en la intranet de MINSAL (`isalud.minsal.cl`).
- Correo informativo.
- Publicación en el sitio web de MINSAL (`minsal.cl/seguridad_de_la_informacion/`).

## 7. Revisión y Medición

El presente procedimiento deberá ser revisado **cada dos años** o cuando ocurran **cambios significativos** para garantizar que:

- Sigue siendo adecuado para su propósito y preciso.
- Refleja los cambios en las tecnologías.
- Está alineado con la legislación vigente, los estándares internacionales y las mejores prácticas.

## 8. Anexos

Material complementario: cuadro de responsabilidades por tipo documental, catalogo de tipos de documentos, y especificaciones de estructura.

## 8.1. Cuadro de Responsabilidades según Tipo de Documento

| Tipo de Documento | Elaborado por | Revisado por | Aprobado por |
|-------------------|--------------|-------------|-------------|
| Política | CISO o Dueño del proceso | CISO o Jefe TIC | Dirección |
| Procedimiento | CISO o Dueño del proceso | CISO o Jefe TIC | Dirección |
| Instructivo | CISO o Dueño del proceso | CISO o Jefe TIC | Dirección |
| Registros | CISO, Jefe TIC | CISO o Jefe TIC | Jefe TIC, Dirección |
| Recursos | Jefe TIC, Dirección | — | — |
| Plantillas | CISO | — | — |
| Flujos | CISO | — | — |
| Actas | CISO | — | — |
| Programas | CISO | — | — |
| Presentaciones | CISO | — | — |

## 8.2. Tipos de Documentos

| Tipo | Código | Descripción |
|------|--------|-------------|
| Política | PS | Documento de alto nivel que muestra las intenciones globales asociadas a una actividad, establecida por la Dirección. Define las reglas de ejecución de los procedimientos. |
| Procedimiento | PROS | Documento que indica la secuencia de actividades necesarias para transformar las entradas de un proceso en las salidas, y los responsables de su realización. |
| Instructivo | ITS | Documento que define paso a paso cómo realizar tareas o actividades específicas de un procedimiento. |
| Registro | REG | Documento que contiene evidencia objetiva de que las actividades planteadas en los procedimientos se están llevando a cabo según lo definido. |
| Recursos | REC | Bienes materiales o intelectuales que aportan en la realización de actividades: bases de datos, sistemas, obras gráficas, obras multimedia. |
| Plantilla | PLA | Documento con formato base para lograr la estandarización de documentos reiterativos de la organización. |
| Flujos | FLJ | Documento con diagramas de flujo que grafican las actividades que suceden durante un proceso. Forma visual de mostrar las actividades descritas en los procedimientos. |
| Actas | ACT | Documentos de registro de puntos tratados y acuerdos adoptados en reuniones de trabajo internas o con terceros externos. También actas de conformidad en recepción de productos/servicios o actas de revisión de entregables por la dirección. |
| Presentaciones | PPT | Material de apoyo multimedia para reuniones de trabajo, capacitaciones y otras actividades insertas en los procesos organizacionales. |

## 8.3. Estructura de los Documentos

#### Formato

- Tamaño: Carta.
- Fuente: Arial o Barlow.
 - Títulos: negrita y mayúsculas, tamaño 11.
 - Primer subtítulo: negrita, tamaño 11.
 - Segundo subtítulo: negrita y subrayado, tamaño 10.
- Interlineado: simple 1.0.
- Márgenes: estándar de Word.
- Alineación: izquierda y justificado según corresponda.

#### Encabezado

- Logo de la Institución.
- Nombre del documento.
- Codificación del documento (ej.: PROS-10).
- Versión vigente del documento.
- Páginas: número de página y total de páginas del documento.
- Color del TLP definido según clasificación de seguridad.

#### Pie de Página

- Frase "Documento Controlado, prohibida su reproducción parcial o total sin autorización", centrada, Arial o Barlow, cursiva, tamaño 11.
- Clasificación de seguridad: centrada, Arial o Barlow, negrita, tamaño 10, con formato "Clasificación de seguridad: [clasificación]".

### 8.4 Clasificación de Seguridad de la Información

Sistema utilizado para categorizar la información según su nivel de sensibilidad y el impacto que podría tener su divulgación no autorizada.

| Nivel | Criterio de Clasificación | Restricción de Acceso |
|-------|--------------------------|----------------------|
| **Secreto** | Documentos que la ley establece como Secretos. No pueden ser divulgados. | Disponible solo para un grupo específico de empleados que ejercen funciones definidas. Información altamente sensible, de uso exclusivamente interno. |
| **Reservado** | Su divulgación no autorizada podría implicar un impacto no deseado para MINSAL o violación de normativa vigente. Declarada como reservada según Ley 20.285. | Disponible solo para un grupo específico de empleados y terceros autorizados. |
| **Uso Interno** | El acceso no autorizado podría ocasionar daños y/o inconvenientes menores a la organización. | Disponible para todos los empleados y terceros seleccionados. Puede ser entregada al público mediante canal OIRS, previa consulta al Propietario del Activo, sujeta a normativa vigente. |
| **Pública** | Hacer pública la información no puede dañar a la organización de ninguna forma. | Puede ser distribuida sin restricciones, sujeta a controles de Copyright, utilizando los procedimientos establecidos para su difusión pública. |

#### Protocolo TLP (Traffic Light Protocol) 2.0

MINSAL adhiere al protocolo TLP 2.0 presentado por FIRST, vigente desde agosto 2022. Permite al autor definir de manera clara y ágil el grado de distribución permitido.

| Código TLP | Color | Equivalencia | Cuándo utilizarlo | Cómo compartirlo |
|-----------|-------|-------------|-------------------|-----------------|
| TLP:RED | `#ff2b2b` | Secreto | Información limitada a personas concretas. Podría tener impacto en privacidad, reputación u operaciones si es mal utilizada. | No compartir con ningún tercero fuera del ámbito donde fue expuesta originalmente. |
| TLP:AMBER | `#ffc000` | Reservado | Información que requiere ser distribuida de forma limitada pero supone un riesgo para la privacidad, reputación u operaciones si es compartida fuera. | Compartir solo con miembros de la propia organización, proveedores o asociados que necesiten conocerla. El emisor puede especificar restricciones adicionales. |
| TLP:GREEN | `#33ff00` | Uso Interno | Información útil para todas las organizaciones que participan. | Compartir con organizaciones afiliadas o miembros del mismo sector, pero nunca a través de canales públicos. |
| TLP:CLEAR | `#ffffff` | Pública | Información que no supone ningún riesgo de mal uso. | Distribuir sin restricciones, sujeta a controles de Copyright. |

### 8.5 Control de Documentos

Debe estar presente en todos los tipos de documentos (punto 8.2) y contener:

| Campo | Descripción |
|-------|-------------|
| Versión | Versión del documento |
| Realizado por | Dueño del proceso |
| Revisado | Colaboradores que revisaron |
| Aprobado | Jefe que aprobó |
| Fecha | Fecha de aprobación del documento |

### 8.6 Control de Versiones

- Debe ir en la segunda hoja del documento.
- Es una comparativa entre las diversas versiones del documento controlado.
- **La última versión es la que se toma en cuenta para difusión.**
- Debe establecer:

| Campo | Descripción |
|-------|-------------|
| Versión | Número de versiones existentes del mismo documento |
| Fecha | Fecha de aprobación de la versión |
| Cambios de la Versión | Descripción del cambio y razón de la modificación |
| Pág. o Sección modificada | Lugar del documento donde se realiza el cambio |

### 8.7 Factores para la Actualización de Documentos

El Dueño del Proceso puede realizar actualizaciones a documentos en estado **Vigente** considerando:

- Cambios en las definiciones originales:
 - Actualización de actividades (incluye eliminar).
 - Nuevos instructivos y/o registros que desee asociar.
 - Modificación en responsabilidad de los roles.
 - Modificación de las entradas/salidas de información.
- Corrección de desviaciones y/o malas interpretaciones del documento.
- Recomendaciones de auditorías internas y/o externas.

### 8.8 Factores para la Eliminación de Documentos

El Dueño del Proceso puede solicitar la eliminación de documentos en estado **Vigente** considerando:

a) El documento soporta una actividad que actualmente no se realiza.
b) El documento soporta una actividad que se fusionó con otra.

### 8.9 Maestro de Documentos

Contiene la información asociada a todos los documentos controlados por el proceso de Gestión Documental del SGSI del MINSAL. Solo incluye **versiones actualizadas** de documentos aprobados. No incluye información eliminada.

| Campo | Descripción |
|-------|-------------|
| Nombre del documento | Título del documento |
| Codificación | Código del documento |
| Versión | Versión vigente |
| N.º Resolución Aprobatoria | Acto administrativo que lo aprueba |
| Fecha de Aprobación | Fecha del acto aprobatorio |
| Estado del Documento | Vigente, Obsoleto, etc. |
| Tipo del Documento | PS, PROS, ITS, REG, REC, PLA, FLJ, ACT, PPT |
| Clasificación según acceso | Secreto, Reservado, Uso Interno, Pública |
| Ubicación del documento | Ruta o repositorio donde se almacena |
