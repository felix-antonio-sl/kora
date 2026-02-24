---
_manifest:
  urn: urn:tde:kb:simple-saas
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- simple
- saas
- bpms
- procesos-digitales
- chile
- tde
lang: es
---

# Plataforma SIMPLE (Modalidad SaaS)

## Definición y Conceptos
- SIMPLE (Sistema de Implementación de Procesos Ligeramente Estandarizados) es un modelador de procesos de negocio (BPMS) en la nube.
- Permite a las instituciones públicas automatizar flujos de baja complejidad mediante una interfaz gráfica y lógica de negocio explícita.

- **BPMS**: plataforma para modelar, automatizar, monitorear y optimizar procesos.
- **BPMN**: lenguaje estándar de diagramas de flujo utilizado para el modelado.

## Ambientes de Trabajo
- **Desarrollo**: entorno compartido para la creación y testeo de nuevos trámites por parte de los OAEs.
- **Capacitación**: espacio para talleres prácticos ("Aprendiendo SIMPLE") y elaboración de manuales.
- **Productivo**: ambiente individual gratuito para disponibilizar procesos a la ciudadanía.
- **SaaS**: modelo donde la infraestructura es gestionada por la SGD y la lógica por cada institución.

## Componentes del Modelador
### Formularios y Campos
- Lienzo interactivo para la captura de datos.

- **Texto**: textbox, textarea, párrafos con soporte HTML.
- **Selección**: checkbox, radio buttons, selectores de lista.
- **Entidades**: integración con datos de regiones, comunas e instituciones oficiales.
- **Archivos**: campos para carga de documentos con límites de tamaño y vigencia.
- **JS**: soporte para scripts personalizados mediante campo Javascript.

### Tareas y Conexiones
- Componentes lógicos que estructuran el flujo.

- **Secuencial**: flujo lineal de pasos.
- **Evaluación**: bifurcación basada en condiciones de negocio.
- **Paralela**: ejecución simultánea de múltiples tareas.
- **Unión**: convergencia obligatoria de ramas paralelas para continuar el proceso.

## Acciones e Integraciones
- **Comunicación**: envío automático de correos con adjuntos.
- **Documental**: generación de PDFs/HTML dinámicos y descarga desde URLs externas.
- **Web Services**: consumo de servicios externos vía REST o SOAP; almacenamiento de respuestas en variables del proceso.
- **Variables**: definición y manipulación de datos en el contexto del trámite.
- **Redirección**: envío del usuario a sitios externos tras completar hitos.

## Ciclo de Vida de la Digitalización
- Proceso integral que abarca:

1. **Modelado**: diseño gráfico del flujo institucional.
2. **Implementación**: configuración de formularios, acciones y reglas.
3. **Ejecución**: operación en ambiente productivo SaaS.
4. **Monitoreo**: seguimiento de KPIs para detectar cuellos de botella.
5. **Optimización**: mejora continua del proceso basada en datos de uso.

## Acompañamiento Técnico
- Liderado por el Equipo de Digitalización de la SGD.

- **Talleres**: "Aprendiendo SIMPLE" para formación de digitalizadores internos.
- **Visado**: presentación obligatoria de procesos antes del paso a producción.
- **Comunidad**: webinars ("Simple Day") y manuales de buenas prácticas para la red de OAEs.
