---
_manifest:
  urn: urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad-p02
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: 'MINSAL Chile, SGSI Nivel Central. PS-NC-005 v5, mayo 2025. Elaborado:
      Pablo Fabres F., Jose Villa C. Revisado: Jose Villa C. Aprobado: Jorge Herrera
      R., Jefe Depto. TIC.'
  extensions:
    kora:
      family: note
    salud:
      minsal_id: PS-NC-005
      minsal_version: '5'
      fecha_aprobacion: mayo 2025
      paginas: 20
      ambito: Nivel Central, Subsecretarias de Salud Publica y Redes Asistenciales
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- ciberseguridad
- minsal
- sgsi
- politica-general
- iso-27001
- gobernanza
- incidentes
- continuidad
- ia-transparencia
lang: es
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
extensions:
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica General de Seguridad de la Informacion y Ciberseguridad del Ministerio de Salud - Parte 02

## Cumplimiento

Todos los usuarios del Ministerio de Salud (funcionarios de planta, contrata, honorarios, asesores, consultores, practicantes y otros trabajadores) deben dar cumplimiento a esta Politica General, las politicas especificas y procedimientos relacionados que se aprueben. Aplica tambien a proveedores tecnologicos y terceros con relaciones contractuales con MINSAL y el sector salud, segun la naturaleza y alcance de cada proyecto.

Cada actor debe seguir rigurosamente las politicas y procedimientos especificos para asegurar proteccion de informacion critica, continuidad operativa y resiliencia de la infraestructura tecnologica del sistema de salud.

## Marco Normativo

### Normas y Estandares de Referencia

| Documento | Descripcion |
|---|---|
| NCh-ISO 27001:2013 | Sistema de gestion de la seguridad de la informacion - Requisitos |
| NCh-ISO 27001:2022 | Actualizacion de la norma ISO 27001 incorporada en v5 |
| Marco Juridico de SSI | Publicado en portal del CSIRT del Ministerio del Interior |
| Documentos del SGSI MINSAL | Disponibles en Intranet http://isalud.minsal.cl y sitio web https://www.minsal.cl/seguridad_de_la_informacion/ |

### Leyes y Decretos Aplicables

| Norma | Materia |
|---|---|
| Ley 19.650 | Perfecciona normas del area de la salud |
| Ley 19.966 | Regimen de Garantias Explicitas en Salud (GES) |
| Ley 19.628 (1999) | Proteccion de la vida privada |
| Ley 19.799 | Documentos y firmas electronicas |
| Ley 20.285 (2008) | Acceso a la informacion publica |
| Ley 20.584 (2012) | Derechos y deberes en atencion de salud |
| Ley 20.120 (2006) | Investigacion cientifica en el ser humano, genoma, prohibicion clonacion humana |
| Ley 20.724 (2014) | Regulacion de farmacias y medicamentos |
| D.F.L. N°29 (2005) | Estatuto Administrativo |
| D.F.L. N°1/19653 | Bases Generales de la Administracion del Estado |
| Ley 21.180 | Transformacion Digital del Estado |
| DS N°7/2023 | Norma tecnica de seguridad de la informacion y ciberseguridad |
| Ley 21.459 (2022) | Delitos informaticos (deroga Ley 19.223, adecua a Convenio de Budapest) |
| Ley 21.663 | Marco de Ciberseguridad |
| Decreto N°273 | Obligacion de reportar incidentes de ciberseguridad |
| Decreto N°164 (2023) | Politica Nacional de Ciberseguridad 2023-2028 |
| Decreto N°295 (2024) | Reglamento de reporte de incidentes de ciberseguridad (Ley 21.633) |
| DS N°7/2023 | Norma Tecnica de Seguridad de la Informacion y Ciberseguridad (estandares minimos para la administracion publica) |
| Decreto N°12 (2025) | Actualizacion Politica Nacional de Inteligencia Artificial |
| Circular N°711/2023 | Lineamientos sobre uso de herramientas de IA en el sector publico |
| Res. Exenta N°372/2025 | Recomendaciones del Consejo para la Transparencia sobre Transparencia Algoritmica |
| Oficio N°7286/2025 | Guia del Consejo para la Transparencia para adopcion de Recomendaciones sobre Transparencia Algoritmica |

## Terminologia

| Termino | Definicion |
|---|---|
| Activo | Todo elemento logico o fisico, componente de hardware, equipamiento o sistema relacionado con la informacion, que permita su generacion, almacenamiento, soporte, envio o intercambio |
| Activo de Informacion | Datos o informacion cuyo tratamiento es esencial para el funcionamiento del organo; deben protegerse en confidencialidad, integridad, disponibilidad u otros factores de importancia |
| Ciberseguridad y Seguridad de la Informacion | Conjunto de acciones, politicas, medidas preventivas y reactivas para prevencion, mitigacion, manejo, respuesta y estudio de amenazas y riesgos de incidentes de seguridad, antes, durante y despues de su ocurrencia; proteger, preservar y restablecer confidencialidad, integridad y disponibilidad de activos y plataformas electronicas, aumentando su resiliencia |
| Gestion de Riesgo | Proceso estructurado y proactivo por el cual se identifican, evaluan, controlan y tratan los riesgos derivados de una o mas amenazas determinadas |
| Incidente de Seguridad | Todo evento de seguridad indeseado o inesperado que comprometa disponibilidad, autenticidad, integridad o confidencialidad de sistemas informaticos, activos de informacion, datos o servicios |
| Integridad | Atributo de los activos y activos de informacion relativo a la exactitud, autenticidad y completitud de los mismos |
| Plataforma electronica | Software o conjunto de software, datos e infraestructura tecnologica que sustenta procesos o procedimientos |
| Riesgo | Efecto de la incertidumbre sobre los activos de informacion y los objetivos de una entidad, expresado en relacion con las consecuencias de un evento o incidente de seguridad y su probabilidad de ocurrencia |
| Servidor | Equipo virtual o fisico dedicado a entregar servicios de red, bases de datos, sitios web, sistemas informaticos, carpetas compartidas y recursos para responder peticiones de usuarios |
| Sistema Informatico | Conjunto de componentes logicos y fisicos que, interactuando entre si, permiten realizar la funcion para la cual fueron disenados |
| Usuarios(as) | Personas naturales o sus apoderados, representantes de personas juridicas o entidades sin personalidad juridica que actuan como interesados en un procedimiento administrativo, y funcionarios que acceden a las plataformas electronicas que soportan procedimientos administrativos |

## Difusion

La comunicacion de la presente politica se efectuara por canales que garanticen accesibilidad y comprension para todos los usuarios:

| Canal |
|---|
| Sitio web MINSAL: http://www.minsal.cl/seguridad_de_la_informacion/ |
| Intranet MINSAL: http://isalud.minsal.cl/ |
| Correo informativo |

## Revision Periodica

Revision del contenido a lo menos cada dos anos por el Comite de Seguridad de la Informacion, o cuando necesidades de cambio lo requieran para garantizar idoneidad, adecuacion y efectividad.

## Historial de Versiones

| Version | Ano | Autor | Descripcion |
|---|---|---|---|
| v1 | 2011 | Rodrigo Vidal | Creacion de la politica general. Ambito: sector salud |
| v2 | 2019 | Jose Villa | Reduccion de alcance a Subsecretarias de Salud Publica y Redes Asistenciales |
| v3 | 2023 | Jose Villa | Actualizacion integral: estructura documental, roles, controles ISO 27001, gobernanza |
| v4 | 2024 | Jose Villa | Actualizacion a ISO 27001:2022. Incorpora Ley 21.663 Marco de Ciberseguridad. Agrega Estrategia y Plan Director; Gestion de Incidentes |
| v5 | 2025 | Jose Villa | Incorpora lineamientos de IA, transparencia algoritmica, Ley 21.459 delitos informaticos, Arquitectura de Referencia Ministerial, actualizacion Decreto N°295/2025 reporte incidentes, Circular N°711/2023 IA en sector publico, Res. Exenta N°372/2025 transparencia algoritmica |

## Referencias

| Referencia | Ubicacion |
|---|---|
| Politica de Riesgo | http://isalud.minsal.cl/ministerio/dgstic/SGSI/Paginas/default.aspx |
| Procedimiento de Riesgos de Seguridad de la Informacion | http://isalud.minsal.cl/ministerio/dgstic/SGSI/Paginas/default.aspx |
| Documentacion SGSI | https://www.minsal.cl/seguridad_de_la_informacion/ |
| CSIRT Nacional - Reporte de Incidentes | https://portal.anci.gob.cl |
