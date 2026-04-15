---
_manifest:
  urn: urn:tde:kb:glosario-plataforma-simple
  provenance: https://wikiguias.digital.gob.cl/Manuales/Glosario_Simple
version: 1.0.0
status: published
tags:
- tde
- plataformas-manuales
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:glosario-plataforma-simple
---

# Glosario — Plataforma SIMPLE

## Resumen

| Término | Definición |
|---------|------------|
| **Acciones** | Conjunto de funcionalidades ejecutables dentro de un proceso: enviar correo, generar variables, consultar servicios web, etc. |
| **Acompañamiento equipo de digitalización** | Servicio de la Secretaría de Gobierno Digital para el desarrollo de procesos institucionales; actividades y requisitos descritos en la guía de servicio de acompañamiento. |
| **Ambiente de desarrollo** | Ambiente compartido para desarrollar nuevos procesos de los OAE que utilizan SIMPLE. |
| **Ambiente de capacitación** | Ambiente compartido para desarrollar manuales de capacitación y ejecutar el taller "Aprendiendo SIMPLE". |
| **Ambiente productivo** | Ambiente entregado gratuitamente a cada OAE por la Secretaría de Gobierno Digital para disponibilizar sus procesos a las personas. |
| **API (Application Programming Interface)** | Conjunto de reglas, protocolos y herramientas que permite que diferentes aplicaciones de software se comuniquen entre sí para enviar o recibir datos. |
| **Aprendiendo SIMPLE** | Taller práctico del equipo de digitalización; parte de la fase de capacitación de cada funcionario que trabajará con SIMPLE. |
| **Auditoría de procesos** | Revisión y análisis de flujos de trabajo para garantizar el cumplimiento de políticas y normativas. |
| **Automatización de procesos** | Uso de tecnología para realizar tareas y procesos con mínima intervención humana. |
| **Back-end** | Parte del software que maneja la lógica, el procesamiento de datos y la interacción con el servidor. En SIMPLE corresponde a la sección donde se encuentra el modelador de procesos. |
| **BPMN (Business Process Model and Notation)** | Lenguaje estándar para modelar procesos de negocio mediante diagramas de flujo. |
| **BPMS (Business Process Management System)** | Plataforma tecnológica para modelar, automatizar, monitorear y optimizar procesos de negocio. |
| **Buenas prácticas de digitalización** | Conjunto de recomendaciones para la digitalización de procesos, descritas en la guía homónima. |
| **Campo botón asíncrono** | Campo que permite ejecutar acciones en un mismo formulario sin presionar el botón "siguiente". |
| **Campo botón siguiente** | Campo que permite reemplazar el botón "siguiente" provisto por defecto. |
| **Campo checkbox** | Campo con varias opciones de selección donde se puede marcar más de una. |
| **Campo comunas** | Campo que despliega regiones y comunas del país para selección en formulario. |
| **Campo date** | Campo para seleccionar una fecha del calendario; puede ser restringida según necesidad del OAE. |
| **Campo documento** | Campo para referenciar un documento creado en la plataforma. |
| **Campo file** | Campo para subir archivos a la plataforma; máximo 15 MB. |
| **Campo file transfer** | Campo para subir archivos sin límite de tamaño; vigencia de 30 días desde la carga. |
| **Campo grilla** | Campo que permite agregar una tabla editable con columnas configurables. |
| **Campo grilla de datos externos** | *(sin definición provista en la fuente)* |
| **Campo instituciones** | Campo que despliega los nombres de los OAE de Chile. |
| **Campo Javascript** | Campo que permite agregar código JavaScript al proceso. |
| **Campo moneda** | Campo que despliega un listado de monedas de diferentes países. |
| **Campo países** | Campo que despliega un listado de países del mundo. |
| **Campo párrafo** | Campo para texto con mayor número de caracteres; configurable con HTML. |
| **Campo password** | Campo que agrega una etiqueta HTML `input` de tipo `password`. |
| **Campo provincias** | Campo que despliega regiones, provincias y comunas de Chile. |
| **Campo radio** | Campo con varias opciones de selección; solo se puede marcar una. |
| **Campo Select** | Campo que agrega varias opciones mediante lista desplegable. |
| **Campo subtítulo** | Campo que agrega texto con etiqueta HTML `H4` por defecto; configurable con `H1`, `H2`, etc. |
| **Campo textarea** | Área de texto multilínea para entradas como comentarios o descripciones. |
| **Campo textbox** | Área de texto básica de una sola línea. |
| **Campo título** | Campo que agrega texto con etiqueta HTML `H3` por defecto; configurable con `H1`, `H2`, etc. |
| **Ciclo de vida de procesos** | Fases de un proceso en un BPMS: modelado, implementación, ejecución, monitoreo y optimización. |
| **Consultar rest (acción)** | Acción para configurar el consumo de un servicio web de tipo REST y almacenar la respuesta en una variable. |
| **Consultar soap (acción)** | Acción para configurar el consumo de un servicio web de tipo SOAP y almacenar la respuesta en una variable. |
| **Crear conexión de unión** | Conexión requerida cuando se usa conexión paralela; permite avanzar a la siguiente tarea al completar todas las tareas paralelas. |
| **Crear conexión paralela** | Conexión que permite ejecutar más de una tarea simultáneamente en un mismo proceso. |
| **Crear conexión paralela por evaluación** | Conexión que ejecuta más de una tarea simultáneamente dependiendo del cumplimiento de una condición. |
| **Crear conexión por evaluación** | Conexión que, mediante una condición, permite avanzar a una u otra tarea siguiente. |
| **Crear conexión secuencial** | Conexión que indica cuál es la siguiente tarea a ejecutar. |
| **Crear tarea** | Componente que contiene los pasos, acciones y configuraciones necesarias para la ejecución del proceso. |
| **Cuenta** | Creación en la nube de la institución usuaria de SIMPLE; requiere un administrador designado como contraparte del Equipo de Digitalización. |
| **Descargar documento (acción)** | Acción para descargar un documento almacenado en una URL pública y transformarlo en base64 dentro de una variable. |
| **Diagrama de proceso** | Representación visual de las etapas, pasos y decisiones de un flujo de trabajo. |
| **Digitalización de procesos** | Transformación de procesos manuales en flujos automatizados mediante tecnología. |
| **Diseñador** | Módulo del back-end de SIMPLE donde el digitalizador crea y configura las tareas de un proceso. |
| **Diseño/rediseño de procesos** | Crear o modificar procesos para hacerlos más eficientes y alineados con los objetivos de la organización. |
| **Documentos** | Archivos de texto generables mediante formato HTML dentro de la plataforma SIMPLE. |
| **Enviar correo (acción)** | Acción para configurar remitente, copia, copia oculta, asunto, contenido y adjuntos de un correo electrónico. |
| **Enviar documento (acción)** | Acción que, mediante llamada REST, envía un documento generado en SIMPLE a un endpoint institucional en formato base64. |
| **Equipo de digitalización** | Equipo de la Secretaría de Gobierno Digital que capacita a los OAE en modelado y optimización de procesos. |
| **Formularios** | Lienzo donde se agregan todos los campos de SIMPLE. |
| **Front-end** | Parte visible e interactiva de una aplicación. En SIMPLE es la interfaz con la que interactúan funcionarios y personas usuarias. |
| **Generar documento (acción)** | Acción para generar un documento dentro del trámite en ejecución; el documento debe estar previamente elaborado en la sección "Documentos". |
| **Generar variable (acción)** | Acción para crear una nueva variable dentro del trámite en ejecución. |
| **Gestión del cambio** | Estrategia para asegurar la adopción efectiva de los procesos digitalizados. |
| **Gestión de procesos** | Disciplina de identificar, diseñar, documentar, implementar, monitorear y optimizar procesos de negocio. |
| **Guía de uso de SIMPLE SaaS** | Guía con los requisitos y compromisos para utilizar SIMPLE. |
| **Integración** | Conexión de sistemas, aplicaciones y servicios externos al BPMS para intercambiar información y ejecutar tareas. |
| **KPI (Key Performance Indicator)** | Métricas clave para evaluar el desempeño y eficiencia de los procesos de negocio. |
| **Manuales de digitalización** | Manuales del Equipo de Digitalización para que los digitalizadores aprendan a usar SIMPLE. |
| **Modelado de procesos** | Representación gráfica de un proceso, comúnmente usando BPMN. |
| **Monitorización de procesos** | Seguimiento en tiempo real del desempeño de un proceso para identificar cuellos de botella o ineficiencias. |
| **Optimización de procesos** | Mejora continua de flujos de trabajo para aumentar eficiencia y reducir costos. |
| **Presentación de procesos** | Reunión en que los digitalizadores de un OAE presentan el proceso desarrollado al equipo de digitalización, posterior al acompañamiento. |
| **Procesos End-to-End** | Procesos completos que abarcan todas las etapas desde el inicio hasta la entrega del resultado final. |
| **Redirección (acción)** | Acción para redireccionar al usuario a una URL externa a SIMPLE al completar una tarea o paso. |
| **Reglas de negocio** | Directrices o condiciones que determinan las acciones y decisiones dentro de un flujo de proceso. |
| **SaaS (Software as a Service)** | Modelo de software donde las aplicaciones se alojan en la nube y se ofrecen a través de Internet. |
| **Simple Day** | Webinar para conocer el modelador de procesos SIMPLE, sus usos, el acompañamiento y cómo acceder. |
| **SIMPLE** | Sistema de Implementación de Procesos Ligeramente Estandarizados. Sistema modelador de procesos (BPMS). |
| **Tareas de SIMPLE** | Actividad configurada para el modelado de procesos. |
| **Task** | Unidad mínima de trabajo dentro de un flujo de proceso en un BPMS. |
| **Variable** | Dato o valor almacenado en la plataforma para un trámite específico. |
| **Workflow** | Secuencia automatizada de tareas, reglas y decisiones que define cómo se ejecuta un proceso. |
