---
_manifest:
  urn: urn:salud:kb:politica-desarrollo-sistemas
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-002 v04
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
- desarrollo-sistemas
- codigo-fuente
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:politica-desarrollo-sistemas
  salud:
    minsal_id: PS-NC-002
    minsal_version: '04'
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Desarrollo de Sistemas -- PS-NC-002 v04


Sistema de Gestion de Seguridad de la Informacion -- MINSAL Nivel Central. Noviembre 2024.
Clasificacion de seguridad: Publica.

## Proposito y alcance

Establecer lineamientos para garantizar la seguridad en productos de software desarrollados para MINSAL y las instituciones del Sector Salud, en cada etapa del desarrollo y controlando los ambientes de trabajo (desarrollo, testing, produccion).

Aplica a todos los sistemas de informacion desarrollados, actualizados o mantenidos para MINSAL y Sector Salud, independientemente de si el trabajo es interno o externo. Aplica a todos los funcionarios y terceros que participen en cualquier etapa del desarrollo de sistemas.

### Controles ISO 27001:2022 asociados

| Control | Nombre |
|---|---|
| 8.19 | Instalacion del software en sistemas de produccion |
| 8.25 | Seguridad en el ciclo de vida del desarrollo |
| 8.29 | Pruebas de seguridad en desarrollo y aceptacion |
| 8.31 | Separacion de los entornos de desarrollo, prueba y produccion |
| 8.32 | Gestion de cambios |

## Marco normativo

| Instrumento | Referencia |
|---|---|
| ISO 27001:2022 | Seguridad de la informacion, ciberseguridad y proteccion de la privacidad |
| ISO 27002:2022 | Controles de seguridad de la informacion |
| Marco Juridico SSI | Portal CSIRT del Ministerio del Interior |
| Ley 19.628 | Proteccion de vida privada y datos personales |
| Ley 19.799 | Firmas y documentos electronicos |
| Ley 19.880 | Bases de los procedimientos administrativos |
| Ley 19.927 | Delitos de pornografia infantil |
| Ley 20.285 | Transparencia de la funcion publica |
| Ley 21.180 | Transformacion Digital del Estado |
| Ley 21.459 | Delitos informaticos (deroga Ley 19.223, adecua al Convenio de Budapest) |
| Ley 21.663 | Marco de Ciberseguridad |
| Decreto 83, 2004 | Norma tecnica sobre seguridad y confidencialidad de documentos electronicos |
| Decreto 136, 2005 | Reglamento Organico del MINSAL |
| Decreto 533 | Marco regulatorio en ciberseguridad para instituciones publicas |
| Decreto Supremo N° 7 | Norma Tecnica de Seguridad de la Informacion y Ciberseguridad |

Documentos relacionados: Procedimiento de desarrollo seguro. Guia Tecnica Lineamientos de Desarrollo de Software (Gobierno Digital, SEGPRES).

## Roles

| Rol | Responsabilidad |
|---|---|
| Jefe Departamento TIC | Establecer controles de acceso para entornos de desarrollo/pruebas/produccion; supervisar medidas de control con Encargado de Seguridad; supervisar desarrollos en ambientes seguros y diferenciados |
| Encargado de Seguridad / Ciberseguridad | Coordinar revisiones periodicas de seguridad en produccion; proponer practicas de desarrollo seguro; evaluar riesgos con equipos de desarrollo y operaciones |
| Operaciones TIC (Soporte) | Recibir, canalizar y gestionar avisos de problemas o incidentes; documentar y escalar incidentes segun protocolos |
| Operaciones TIC (Desarrollo) / Areas de Negocio con equipos de desarrollo | Cumplir todos los lineamientos en cada fase; documentar exhaustivamente el sistema con trazabilidad |
| Operaciones TIC (Infraestructura) | Implementar y mantener proteccion de entornos de desarrollo/pruebas/produccion; configurar y monitorear infraestructura |

## Materias que aborda

- Separacion de ambientes de desarrollo, prueba y operacionales
- Politica de desarrollo seguro
- Entorno de desarrollo seguro
- Pruebas de seguridad del sistema
- Pruebas de aprobacion del sistema
- Control de acceso al codigo fuente

## Definiciones

| Termino | Definicion |
|---|---|
| **Entorno Pre-Productivo** | Entornos de Desarrollo y Testing donde se simula produccion para testear seguridad y funcionalidad |
| **Seguridad en el Desarrollo de Sistemas** | Practicas durante el ciclo de vida para proteger el sistema contra accesos no autorizados, fallos y riesgos |
| **SDLC Seguro** | Metodologia que integra seguridad en cada fase del ciclo de vida (planificacion a mantenimiento) |
| **Evaluacion de Vulnerabilidades** | Proceso para identificar, clasificar y priorizar vulnerabilidades antes de la implementacion |
| **Principio de Privilegios Minimos** | Otorgar solo los derechos necesarios para cumplir la funcion |
| **Autenticacion y Autorizacion** | Verificacion de identidad y control de acceso |
| **Control de Versiones** | Sistema de gestion y rastreo de cambios en el codigo fuente |
| **Codificacion Segura** | Practicas para escribir codigo libre de vulnerabilidades |
| **Gestion de Parcheo** | Actualizacion de software para corregir vulnerabilidades post-despliegue |

## Directrices

Directrices de seguridad aplicables al ciclo de vida del desarrollo de software.

### Lineamientos generales

- Criterios estandarizados de seguridad y calidad en cada fase del SDLC, conforme a estandares internos y normativos
- Todo sistema cumple esta politica, independientemente de si es interno o externo
- Sistemas criticos: aquellos con informacion sensible o esenciales para operaciones institucionales; requieren medidas estrictas y monitoreo constante
- Todo desarrollo por terceros debe adherirse a los lineamientos de seguridad en todas las etapas (controles de calidad y pruebas de seguridad incluidos)

### Fase inicial: Analisis previo del sistema

| Actividad | Detalle |
|---|---|
| Identificacion de problemas de seguridad | Detallar amenazas y vulnerabilidades potenciales que el nuevo sistema debe atender |
| Estudio de factibilidad | Evaluar criticidad del sistema y definir controles de seguridad necesarios |
| Levantamiento de requisitos | Recopilar y autorizar formalmente; participacion del jefe de proyecto y usuario solicitante |

## Fase de diseno

### Elementos del diseno del proyecto

| Componente | Contenido |
|---|---|
| Diseno de Presentacion | Visualizacion e interaccion del usuario final |
| Diseno de Arquitectura | Tipo de proyecto (web, escritorio, servicios web, movil), interaccion con otros sistemas, lenguaje de desarrollo |
| Diseno de Base de Datos | Diseno logico y conceptual del modelo de negocio, optimizado para rendimiento y seguridad |

#### Coordinacion de roles

Jefe de Proyecto, Encargado de BD y Encargado de Plataforma de Soporte de Aplicaciones deben participar en diseno y desarrollo. Culmina con el documento de requerimientos.

#### Registros de auditoria de datos

- Incluir identidad del usuario que crea/modifica, fecha y hora de cada evento
- Proteger los registros contra accesos no autorizados y manipulaciones

## Desarrollo y Testing

### Prohibiciones

| Prohibicion |
|---|
| Escribir o modificar codigo auto-copiante, malicioso o perjudicial (virus, gusanos) |
| Incluir funciones u operaciones no documentadas o no autorizadas |
| Realizar modificaciones sin registro y documentacion del cambio |

#### Gestion del codigo fuente

| Requisito |
|---|
| Almacenar en repositorio correspondiente para trazabilidad de todas las modificaciones |
| Acceso restringido mediante contrasenas, solo a usuarios autorizados |
| Consultores externos acceden solo durante vigencia del proyecto |
| Empresa externa debe firmar acuerdo de confidencialidad para sistemas criticos |

#### Entorno de desarrollo

- Desarrollo en entorno local separado con bases de datos de desarrollo distintas de las de produccion
- Proceso basado en documento de levantamiento de requisitos

#### Pruebas y Testing

| Requisito |
|---|
| Al menos dos tipos de pruebas: internas (equipo de testing) y de aceptacion (usuario solicitante) |
| Pruebas de integracion: validacion de instalacion, almacenamiento, configuracion, seguridad, calidad y recuperacion ante errores |
| Pruebas funcionales y de rendimiento |
| Resultados documentados en el plan de prueba |
| Controles de acceso en testing tan estrictos como en produccion |
| Usuarios solicitantes solo con permisos de lectura en testing |

#### Validacion de sistemas criticos

- Validacion de datos de entrada para procesamiento adecuado
- Controles de validacion en datos de salida que confirmen precision del procesamiento
- Controles de integridad en mensajes intercambiados con otros sistemas

#### Adherencia tecnica

Todos los desarrollos deben cumplir los lineamientos de la guia tecnica aplicable para desarrollo de software en la Administracion del Estado.

### Pruebas de seguridad del sistema

- Pruebas rigurosas durante desarrollo y antes de implementacion en produccion segun criterios del Departamento TIC
- Procedimiento definido para analisis de seguridad en aplicaciones (vulnerabilidades y estandares)

### Marcha Blanca y Produccion

| Paso | Requisito |
|---|---|
| Autorizacion | Usuario solicitante autoriza paso a produccion via correo, tras finalizar testing |
| Plazos marcha blanca | Especificos segun caracteristicas del proyecto |
| Auditoria de controles | Obligatorio revisar y auditar controles de seguridad definidos en diseno antes de produccion |
| Auto-revision | Equipo de desarrollo revisa y audita sus propios sistemas antes de pruebas formales |
| Revision de testing | Equipo de pruebas audita controles de seguridad conforme a especificaciones de diseno |
| Modificaciones | Requieren reiniciar ciclo de desarrollo (levantamiento de requisitos) |
| Traspasos a produccion | En periodos de baja carga, coordinados con area responsable |

### Proteccion de datos de produccion

Prohibido el uso de bases de datos operativas (produccion) para pruebas y la exportacion de modelos y datos a terceros externos.

## Separacion de ambientes

| Tipo de separacion | Medida |
|---|---|
| Red | Segmentos de red distintos con direcciones IP diferenciadas |
| Versiones del sistema | Cada ambiente opera con versiones especificas |
| Bases de datos | Bases de datos distintas para cada entorno |
| Roles | Roles especificos y distintos para cada ambiente (principio de minimo privilegio) |

#### Reglas de implementacion

- Definir, documentar e implementar reglas y autorizaciones para la transicion de software de desarrollo a produccion
- Todos los cambios en produccion deben ser probados en entorno de prueba o ensayo antes de implementacion

#### Restricciones en pruebas

No realizar pruebas en sistemas de produccion (salvo circunstancias excepcionales aprobadas por Encargado de Seguridad/Ciberseguridad).

#### Acceso a herramientas de desarrollo

Compiladores, editores y otras herramientas de desarrollo no deben estar accesibles desde sistemas operacionales salvo necesidad absoluta.

#### Perfiles de usuario

Usuarios deben utilizar distintos perfiles para sistemas operacionales y de prueba, con menus y mensajes de identificacion adecuados.

#### Modificaciones de software critico

Cualquier modificacion (parches, modulos adicionales) debe ser analizada y validada en ambientes de desarrollo y prueba antes de produccion.

#### Acceso restringido a produccion

Ningun proveedor, programador o analista encargado del mantenimiento de aplicaciones tendra acceso a ambientes de produccion.

### Control de cambios a datos de produccion

| Elemento | Detalle |
|---|---|
| Copias de seguridad | Completas antes de cualquier cambio |
| Recursos | Identificar y asignar los necesarios |
| Pruebas pre/post | Definir pruebas antes y despues de la implementacion |
| Comunicacion | Planificar y comunicar el cambio con suficiente antelacion |
| Criterios de aceptacion | Establecer criterios claros de aceptacion o rechazo |
| Plan de contingencia | Permitir reversion de cambios ante problemas |
| Documentacion | Tipos de cambios documentados y registrados; conservacion segun periodo que MINSAL determine |

En concordancia con el procedimiento para gestion de cambios en ambientes productivos.

### Controles criptograficos

- Sistemas y tecnicas criptograficas robustas para acceso, almacenamiento de claves, proteccion de BD y transmision de datos sensibles
- Todos los sitios y sistemas web deben usar **HTTPS** con certificados validos de entidades acreditadas
- Cumplir con la politica de uso de criptografia: algoritmos aprobados y seguros

### Adquisicion de sistemas a terceros

| Requisito |
|---|
| Acuerdo formal previo que garantice proteccion de propiedad intelectual, uso de datos, tratamiento de datos sensibles y confidencialidad |
| Incluir responsabilidades de terceros en correccion de errores y gestion de incidentes de seguridad |
| Diferenciar entre quien establece/autoriza acuerdos y quien audita cumplimiento (evitar conflicto de interes) |
| Certificacion y aceptacion del sistema independiente del proveedor y de la contraparte institucional |
| Proceso de adquisicion formal y conforme a todas las disposiciones de esta politica |
| Proveedor externo debe aceptar y aplicar politicas de seguridad MINSAL (confidencialidad, propiedad intelectual, soporte, mantenimiento, clausulas de finalizacion y traspaso) |
| Pruebas de software con datos ficticios o anonimizados; prohibido usar datos reales |

### Adquisicion de sistemas en la nube

- Proveedor debe cumplir estandares de seguridad MINSAL y certificados relevantes para proteccion de datos en nube
- Exigir SLA que defina disponibilidad, seguridad, respuesta ante incidentes, politicas de recuperacion de datos y gestion de incidentes

### Arquitectura referencial

| Aspecto | Requisito |
|---|---|
| Alineacion estrategica | Disenar conforme a vision y objetivos tecnologicos de la arquitectura de referencia |
| Estandares y tecnologias | Seguir plataformas, frameworks y patrones de diseno aprobados |
| Revision y aprobacion | Cambios significativos aprobados por Jefe TIC o equipo de gobernanza de arquitectura |
| Reutilizacion y modularidad | Diseno modular para escalabilidad, reduccion de duplicacion y optimizacion de recursos |
| Documentacion continua | Documentar arquitecturas y modelos de datos, mantener actualizada en cada fase |

### Interoperabilidad

| Aspecto | Requisito |
|---|---|
| Estandares HL7 | Compatibilidad con HL7 v2.x y FHIR (R4 y posteriores) para intercambio de datos clinicos (HCE, RIS, LIS) |
| Protocolos de integracion | REST, GraphQL, JSON, XML con HTTPS, SFTP, TCP/IP |
| APIs documentadas | Consistentes para integracion de funcionalidades y datos entre sistemas internos y de terceros |
| Compatibilidad arquitectonica | Compatible con arquitectura empresarial existente y futura |
| Datos interoperables | Formatos estructurados y normalizados segun directrices organizacionales y normativas |
| Pruebas de interoperabilidad | Verificar conectividad, rendimiento y seguridad al interactuar con otros sistemas |

## Control de acceso al codigo fuente

| Requisito |
|---|
| Almacenamiento en repositorio central controlado de MINSAL, preferiblemente no en sistemas operacionales |
| Acceso restringido con contrasenas, solo a usuarios autorizados; lectura/escritura segun necesidades ministeriales |
| Consultores externos acceden solo durante vigencia del proyecto, solo a funcionalidades necesarias; prohibido acceso a ambientes productivos |
| Acuerdo de confidencialidad obligatorio para empresas externas con codigo de sistemas criticos |
| Gestion de acceso segun procedimientos establecidos; personal de soporte sin acceso irrestricto |
| Desarrolladores sin acceso directo al repositorio; uso de herramientas de desarrollo que controlen actividades y autorizaciones |
| Listas de programas en entorno seguro; registro de auditoria de todos los accesos a bibliotecas de codigo fuente |
| Acceso de lectura a repositorio centralizado para componentes compartidos entre desarrolladores |
| Controles adicionales para codigo publicado (ej. firmas digitales) |

## Clausula de propiedad intelectual

| Aspecto | Detalle |
|---|---|
| Titularidad | Toda creacion intelectual (software, codigo fuente, documentacion, algoritmos, disenos, metodologias) es propiedad exclusiva de MINSAL |
| Codigo fuente | Propiedad exclusiva de MINSAL; documentado, versionado y almacenado en repositorio centralizado |
| Cesion de derechos | Funcionarios, personal a honorarios, estudiantes en practica transfieren derechos mediante documento formal de cesion |
| Contratacion de terceros | Contrato debe incluir clausula de cesion total de propiedad intelectual; entrega de codigo fuente y documentacion tecnica completa |
| Licencias de terceros | Revisar y aprobar condiciones de uso de software o componentes de terceros; solo componentes cuya licencia no comprometa titularidad |
| Confidencialidad | Toda informacion, especificacion y codigo es confidencial y propiedad de MINSAL; NDAs obligatorios para todas las partes |
| Terminacion de contratos | MINSAL mantiene derecho exclusivo de uso y acceso a todos los materiales; proveedor transfiere inmediatamente todos los activos digitales |

## Difusion

| Canal | Destino |
|---|---|
| Intranet MINSAL | `http://isalud.minsal.cl` |
| Correo informativo | Funcionarios |
| Sitio web MINSAL | `http://www.minsal.cl/seguridad_de_la_informacion/` |

## Periodo de revision

Cada **2 anos** o ante cambios significativos, verificando: adecuacion al proposito, reflejo de cambios tecnologicos, alineacion con legislacion vigente, estandares internacionales y mejores practicas.

## Excepciones

El Jefe TIC, el CISO o el Comite de Seguridad evaluan y establecen condiciones especificas de excepcion, siempre que no infrinjan legislacion ni comprometan seguridad. Cada excepcion se documenta e inicia revision de la politica.
