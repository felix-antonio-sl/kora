---
_manifest:
  urn: "urn:tde:kb:manual-coordinadora-tde"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Manuales/manual-del-coordinador"
version: 1.0.0
status: published
tags: [tde, coordinador-tde, plataformas, habilitacion, claveunica, pisee, casilla-unica, docdigital, simple, firmagob, datosgob]
lang: es
---

# Manual del Coordinador/a de Transformacion Digital

Guia sobre rol, funciones, responsabilidades del CTD y paso a paso para habilitar plataformas y servicios compartidos de SGD.

## Publico objetivo

- Autoridades y jefaturas de OAE que no han designado CTD
- CTD que deseen conocer su rol y responsabilidades
- Equipos de TDE que deseen habilitar plataformas y servicios compartidos

## Rol del Coordinador/a de Transformacion Digital (CTD)

Responsable de liderar implementacion de Ley N 21.180 de Transformacion Digital del Estado en su institucion. Funcion principal: alinear estrategia nacional de SGD con realidad interna del organismo.

### Responsabilidades

- **Comunicacion con Gobierno Digital**: contraparte oficial ante SGD; reportar avances, indicadores, materias relevantes
- **Liderar TDE en la institucion**: coordinar unidades para cumplimiento de Ley TDE
- **Gestionar mejoras continuas**: impulsar plan de mejora continua de procesos y herramientas
- **Informar y sensibilizar internamente**: compartir hitos, plazos, actividades de TDE
- **Participar en Red de Coordinadores/as**: compartir experiencias y buenas practicas entre OAE
- **Acompañar jefatura de servicio**: reportes y recomendaciones para toma de decisiones estrategicas

Recomendacion: **dedicacion exclusiva**.

### Designacion del CTD

1. Tramitar oficio dirigido al Director de SGD del Ministerio de Hacienda
   - Indicar titular + subrogante: nombre completo, RUT, email, telefono, cargo
   - Enviar via DocDigital o correo: oficinapartes@hacienda.gov.cl
2. Registrarse en Red de Coordinadores: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2643
   - Adjuntar oficio de designacion

## Equipo de Transformacion Digital

Grupo de trabajo transversal para liderar, coordinar y ejecutar procesos de TDE segun Ley N 21.180 y directrices de SGD.

### Foco prioritario

- Digitalizacion de PA y otras tramitaciones
- Incorporacion de tecnologias para optimizar gestion institucional
- Implementacion de plataformas y servicios compartidos de SGD

### Composicion

- Liderado por CTD (designado por Jefatura de Servicio)
- Subrogante oficial
- Profesionales de distintas areas seleccionados por experiencia y rol estrategico

Perfiles sugeridos:
- Desarrollo de personas (gestion del cambio)
- Legal
- Tecnologia
- Representantes de distintas direcciones

Recomendacion: oficializar y formalizar el equipo dentro de la institucion.

### Funciones

- Apoyar CTD en diseno, ejecucion y seguimiento del plan de TDE
- Coordinar digitalizacion de PA (priorizar por impacto en atencion ciudadana)
- Promover adopcion de plataformas y servicios compartidos de SGD
- Levantar informacion tecnica/operativa para indicadores y reportes SGD
- Participar en capacitacion, sensibilizacion y acompanamiento de funcionarios
- Articular areas para implementacion transversal y sostenible

## Habilitacion de plataformas y servicios compartidos

### ClaveUnica

Servicio de autenticacion digital para validar identidad de personas naturales en plataformas de OAE. Gratuito.

**Pasos de habilitacion:**

1. Asistir a capacitacion inicial: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785
2. Solicitar credenciales de integracion en CeroFilas (Sandbox/Desarrollo y QA): https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2372
3. Credenciales de produccion: solo tras cumplir requisitos de certificacion
4. Requisito: OAE debe tener dominio .gob.cl (si no, presentar plan de adopcion)
5. Integrar segun Guia Tecnica para Integradores
6. Solicitar certificacion y activacion en produccion

**Requisitos de certificacion:**
- Uso de boton oficial de CU
- Protocolo HTTPS en aplicacion integradora
- Llamada correcta al formulario de CU
- State dinamico
- Llamadas al servicio desde backend
- Cierre de sesion

Cambios de RedirectUri: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2229

### Red de Interoperabilidad PISEE

Conexiones directas y seguras via internet entre nodos de interoperabilidad alojados en infraestructura de OAE. Permiten intercambio de datos, documentos y expedientes electronicos.

**Pasos de habilitacion:**

1. Asistir a capacitacion: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785
2. Solicitar Nodo de Desarrollo via CTD: https://gobdigital.cerofilas.gob.cl/tramites/informativo/3041
3. Asistir a taller tecnico segun necesidad:
   - Consumo: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/3021
   - Proveedor: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/3022
4. Designar funcionarios para administracion en Portal PISEE (https://portal.pisee.cl/); autenticacion via ClaveUnica
5. Solicitar Nodo de Produccion: https://gobdigital.cerofilas.gob.cl/tramites/informativo/3020

### Plataforma de Notificaciones Electronicas (CasillaUnica)

Canal oficial para envio de notificaciones electronicas de OAE a personas via DDU.

**Pasos de habilitacion:**

1. Enviar ticket a Mesa de Servicios manifestando intencion
2. Seleccionar PA registrados en CPAT segun criterios SGD
3. Designar equipo: contacto tecnico + contacto negocio + administrador institucional
4. Participar en capacitaciones
5. Solicitar habilitacion en CeroFilas
6. SGD habilita en ambiente demo
7. Configuraciones segun medio (web, API o SIMPLE)
8. Corregir observaciones SGD (si aplica)
9. SGD habilita en produccion

### DocDigital

Plataforma de comunicaciones oficiales del Estado: tramitar, enviar y recibir oficios, resoluciones, convenios entre OAE.

**Pasos de habilitacion:**

1. Asistir a capacitacion "Introduccion a nuevos usuarios": https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785
2. CTD designa "Administrador Principal" (max 3 por institucion): https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2678
   - Habilita institucion en DocDigital Demo
   - Permite crear usuarios, dependencias, oficinas de partes, administradores
3. Administrador Principal recibe correo con enlaces y manuales
4. Participar en capacitaciones mensuales: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785
5. SGD informa fecha mensual de habilitacion en Produccion
6. Administrador Principal crea usuarios y permisos en produccion; implementa plan de adopcion interno

### SIMPLE

Herramienta para digitalizar PA y tramites. Sistema modelador de procesos (BPMS).

**Pasos de habilitacion:**

1. Participar en SIMPLE DAY (sincronico y asincronico): https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785
2. Solicitar credenciales entorno de capacitacion
3. Completar manual "Aprendiendo SIMPLE"
4. Digitalizar manuales Inicial e Intermedio
5. Solicitar credenciales ambiente compartido de desarrollo
6. Completar y enviar ficha de solicitud de acompanamiento

Detalle: https://gobdigital.cerofilas.gob.cl/etapas/ver/44256439/0

### FirmaGob

#### Habilitacion para municipios

1. Solicitar convenio Subsecretaria de Hacienda-Municipio: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2286
2. Tramitar convenio (firma Alcalde) → enviar a SGD
3. Recibir convenio firmado por Subsecretaria → generar:
   - Decreto aprobacion convenio
   - Decreto roles operador y ministro de fe (modelo: https://docs.google.com/document/d/1AVoCUtsmaKl-WvImZSt5LoCSPhlLqFln/edit)
4. Solicitar habilitacion: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627
5. Operador ingresa con ClaveUnica → crea usuarios (empezando por Ministro de Fe como "Autoridad/Funcionario")
6. Solicitar asignacion Ministro de Fe: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627
7. Ministro de Fe: solicitar certificado de Proposito General + autocertificarse

#### Habilitacion para gobierno central

1. Acto administrativo aceptando condiciones de uso; designar Ministro de Fe y Operador
   - Modelo: https://cms-firma-prod.s3-us-west-2.amazonaws.com/uploads/filer_public/e4/d2/e4d2c33c-a9e5-4ac1-a8f8-91d7f736a385/20240327-ca-modeloaceptacondicionesuso.pdf
2. Solicitar habilitacion: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627
   - Datos: RUT institucion, acto administrativo, nombre/RUT/cargo/correo del Operador
3. Operador ingresa con ClaveUnica → crea usuarios (empezando por Ministro de Fe como "Autoridad/Funcionario")
4. Solicitar asignacion Ministro de Fe: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627
5. Ministro de Fe: solicitar certificado de Proposito General + autocertificarse

### Datos.Gob

Portal de Datos Abiertos para publicar datos de forma transparente, estandarizada y reutilizable.

**Pasos de habilitacion:**

1. Solicitar habilitacion + nombramiento administrador: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2536
2. SGD verifica que tramite fue ingresado por CTD → crea usuario administrador
3. Participar en capacitaciones
4. Administrador puede registrar y habilitar otros usuarios
5. Publicar datasets conforme T&C: https://datos.gob.cl/terms_and_conditions_institute
