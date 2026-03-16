---
_manifest:
  urn: "urn:tde:kb:manual-coordinadora-transformacion-digital"
  provenance: "https://wikiguias.digital.gob.cl/Manuales/manual-del-coordinador"
version: 1.0.0
status: published
tags: [tde, plataformas-manuales, casilla-única, clave-única, coordinadores-de-transformación-digital, datos-abiertos, plataforma, docdigital, pisee, firma, simple, habilitacion]
lang: es
---

# Manual del Coordinador/a de Transformación Digital (CTD)

## Rol y responsabilidades del CTD

El CTD es el responsable designado por la Jefatura de Servicio para liderar la implementación de la Ley N° 21.180 sobre Transformación Digital del Estado en su institución.

Responsabilidades:

- **Contraparte oficial ante SGD:** entrega información de avances, cumplimiento de indicadores y materias relevantes, respetando plazos y formatos solicitados.
- **Liderazgo interno:** coordina unidades para el cumplimiento de la Ley de Transformación Digital.
- **Plan de mejora continua:** impulsa su creación y seguimiento.
- **Difusión interna:** comunica hitos, plazos y temas de transformación digital a los equipos institucionales.
- **Red de Coordinadores/as:** participa activamente, comparte experiencias y buenas prácticas.
- **Apoyo a jefatura:** entrega reportes y recomendaciones para decisiones estratégicas.

Idealmente, el rol requiere **dedicación exclusiva**.

## Designación del CTD

1. Tramitar Oficio al Director de la Secretaría de Gobierno Digital (Ministerio de Hacienda) indicando al CTD y su subrogante. Datos requeridos por persona: nombre completo, RUT, email, teléfono y cargo.
2. Enviar el oficio vía **DocDigital**; si no está habilitado, enviar a: **oficinapartes@hacienda.gov.cl**.
3. El CTD y subrogante deben registrarse en la **Red de Coordinadores** adjuntando el oficio de designación: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2643

## Equipo de Transformación Digital

Composición sugerida (se recomienda formalizar mediante acto institucional):

- CTD (líder)
- Subrogante oficial
- Profesional de Desarrollo de Personas (gestión del cambio)
- Profesional Legal
- Profesional de Tecnología
- Representantes de las distintas direcciones/unidades

Funciones del equipo:
- Apoyar al CTD en diseño, ejecución y seguimiento del plan de transformación digital.
- Coordinar la digitalización de procedimientos administrativos (priorizando mayor impacto ciudadano).
- Promover la adopción de plataformas y servicios compartidos de la SGD.
- Levantar información técnica para cumplimiento de indicadores y reportes.
- Participar en capacitaciones y acompañar a funcionarios/as en cambios tecnológicos.
- Articular áreas para implementación transversal y sostenible.

## Habilitación de plataformas y servicios compartidos

### ClaveÚnica

Pasos:
1. Asistir a la [capacitación inicial de ClaveÚnica](https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785).
2. Solicitar credenciales de integración (Sandbox/Desarrollo y QA) en: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2372
3. Requisito previo: el OAE debe tener dominio `.gob.cl`. Si no lo tiene, presentar plan de adopción.
4. Integrar según [Guía Técnica para Integradores](https://docs.google.com/document/d/16c0D2jVhuYOYGI9z4kC2aoNH8oWNA9v1cc3tXQ76TO0/edit).
5. Solicitar certificación de integración. Requisitos:
   - Uso del botón oficial de ClaveÚnica.
   - Protocolo HTTPS en la aplicación integradora.
   - Llamada correcta al formulario de ClaveÚnica.
   - State dinámico.
   - Llamada correcta al servicio.
   - Llamadas al servicio desde el backend.
   - Cierre de sesión implementado.
6. Las credenciales de producción se habilitan solo al cumplir todos los requisitos de certificación.

Cambios de RedirectUri: formulario disponible en https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2229

### Red de Interoperabilidad PISEE

Pasos:
1. Asistir a la capacitación ["PISEE: Introducción a la red de interoperabilidad"](https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785).
2. [Solicitar Nodo de Desarrollo](https://gobdigital.cerofilas.gob.cl/tramites/informativo/3041) a través del CTD (para pruebas y validación previa a producción).
3. Asistir al taller técnico según necesidad:
   - [Consumo de Servicios de Información](https://gobdigital.cerofilas.gob.cl/tramites/iniciar/3021)
   - [Proveedor de Servicios de Información](https://gobdigital.cerofilas.gob.cl/tramites/iniciar/3022)
4. Designar (a través del CTD) a los funcionarios o asesores encargados de administrar servicios de interoperabilidad en el [Portal PISEE](https://portal.pisee.cl/). Una vez enrolados, se autentican con ClaveÚnica.
5. [Solicitar Nodo de Producción](https://gobdigital.cerofilas.gob.cl/tramites/informativo/3020).

### Plataforma de Notificaciones Electrónicas (CasillaÚnica)

Pasos:
1. Enviar ticket a Mesa de Servicios manifestando intención de sumarse a la plataforma.
2. Seleccionar procedimientos administrativos registrados en CPAT que se notificarán, conforme criterios de la SGD.
3. Designar equipo de contacto institucional: contacto técnico + contacto de negocio + administrador institucional.
4. Participar en capacitaciones sobre la plataforma.
5. Solicitar Habilitación de institución en CeroFilas.
6. La SGD habilita a la institución en ambiente demo.
7. Realizar configuraciones según modalidad de envío: web, API o SIMPLE.
8. Corregir observaciones de la SGD al ambiente demo (si las hay).
9. La SGD habilita en producción.

### DocDigital

Pasos:
1. Asistir a la capacitación ["Introducción a nuevos usuarios y usuarias"](https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785).
2. El CTD designa el rol de **Administrador Principal** (máximo 3 por institución): https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2678. Esto habilita la institución en **DocDigital versión Demo**.
3. Al crearse el perfil de Administrador Principal en Demo, se recibe correo con enlaces y manuales.
4. En Demo, el Administrador Principal crea usuarios, dependencias, oficinas de partes y administradores; realiza pruebas. Se recomienda asistir a las capacitaciones mensuales: https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785
5. **Habilitación en producción:** la SGD informa mensualmente la fecha de pase a producción de las instituciones en Demo.
6. En producción: el Administrador Principal crea usuarios, asigna permisos e implementa plan de adopción interno.

### SIMPLE

Pasos:
1. Participar en un [SIMPLE DAY](https://gobdigital.cerofilas.gob.cl/tramites/informativo/2785) (sincrónico o asincrónico).
2. Solicitar credenciales para el entorno de capacitación.
3. Completar el manual "Aprendiendo SIMPLE".
4. Digitalizar los manuales Inicial e Intermedio.
5. Solicitar credenciales en el ambiente compartido de desarrollo.
6. Completar y enviar la ficha de solicitud de acompañamiento.

Detalle de etapas disponible en: https://gobdigital.cerofilas.gob.cl/etapas/ver/44256439/0

### FirmaGob

#### Municipios

1. Solicitar el [convenio Subsecretaría de Hacienda–Municipio](https://gobdigital.cerofilas.gob.cl/tramites/informativo/2286).
2. Tramitar el convenio con firma del Alcalde y enviarlo a la SGD.
3. Al recibir convenio firmado por la Subsecretaría, generar:
   - Decreto de aprobación del convenio en el municipio.
   - Decreto para establecer roles de operador y ministro de fe ([modelo disponible](https://docs.google.com/document/d/1AVoCUtsmaKl-WvImZSt5LoCSPhlLqFln/edit)).
4. Solicitar **Habilitación de la Institución**: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627 (adjuntar ambos decretos).
5. Gobierno Digital informa acceso al operador.
6. El operador ingresa con ClaveÚnica y crea usuarios; comenzar con el Ministro de Fe como "Autoridad/Funcionario".
7. Solicitar **Asignación de Ministro de Fe**: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627
8. Gobierno Digital confirma asignación.
9. El Ministro de Fe ingresa con ClaveÚnica, solicita Certificado de Propósito General y se **autocertifica** (requisito para certificar a los demás usuarios).

#### Órganos del Gobierno Central

1. Emitir acto administrativo aceptando condiciones de uso ([modelo](https://cms-firma-prod.s3-us-west-2.amazonaws.com/uploads/filer_public/e4/d2/e4d2c33c-a9e5-4ac1-a8f8-91d7f736a385/20240327-ca-modeloaceptacondicionesuso.pdf)); designar Ministro de Fe y Operador en el mismo acto.
2. Solicitar **Habilitación de la Institución**: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627 (adjuntar acto administrativo; informar RUT institución, nombre/RUT/cargo/correo del Operador).
3. Gobierno Digital informa acceso al operador.
4. El operador ingresa con ClaveÚnica y crea usuarios; comenzar con el Ministro de Fe como "Autoridad/Funcionario".
5. Solicitar **Asignación de Ministro de Fe**: https://gobdigital.cerofilas.gob.cl/tramites/informativo/1627
6. Gobierno Digital confirma asignación.
7. El Ministro de Fe ingresa con ClaveÚnica, solicita Certificado de Propósito General y se **autocertifica**.

### Datos.Gob (Portal de Datos Abiertos)

Pasos:
1. Solicitar habilitación y nombramiento del administrador: https://gobdigital.cerofilas.gob.cl/tramites/iniciar/2536 (debe ser gestionado por el CTD).
2. La SGD verifica que el trámite fue ingresado por el CTD y crea el usuario administrador.
3. Participar en capacitaciones sobre la plataforma.
4. El administrador registra y habilita a otros usuarios de la institución.
5. Publicar conjuntos de datos conforme términos y condiciones: https://datos.gob.cl/terms_and_conditions_institute
