---
_manifest:
  urn: "urn:kora:kb:tde:lineamientos-normas:decreto-9-norma-autenticacion:1.0.0"
  provenance: "https://wikiguias.digital.gob.cl/Normas/Decreto9"
version: 1.0.0
status: draft
tags: [tde, lineamientos-normas, decreto, norma-tecnica, autenticacion, clave-unica, clave-tributaria]
lang: es
---

# Decreto 9 — Norma Técnica de Autenticación

> Promulgación: 19-MAY-2023 | Publicación: 17-AGO-2023 | Versión: Única

## Encabezado

**Bases legales:**

| Instrumento | Materia |
|-------------|---------|
| DS Nº 100/2005 (CPR arts. 32 Nº6 y 35) | Constitución Política |
| Ley Nº 19.880 | Bases procedimientos administrativos |
| Ley Nº 18.993 | Crea MINSEGPRES |
| Ley Nº 21.180 | Transformación Digital del Estado |
| Ley Nº 19.628 | Protección de la vida privada |
| Ley Nº 19.477 | Ley Orgánica del SRCeI |
| DFL Nº 1/2020 MINSEGPRES | Gradualidad implementación ley 21.180 |
| DS Nº 4/2020 MINSEGPRES | Reglamento medios electrónicos (en adelante "el Reglamento") |
| Resolución Nº 7/2019 CGR | Exención toma de razón |

**Considerando (síntesis):** Ley 21.180 requirió normar mecanismos de autenticación para validar identidad en plataformas electrónicas. Mesa Técnica de Autenticación con SRCeI, SII, Entidad Acreditadora, Hacienda, Educación, FONASA y CPLT. Consulta ciudadana sep.–dic. 2021. DS anterior (Nº 3/2022) retirado en abr. 2022 para revisión. [→ Artículo 19]

---

## Disposiciones generales

### Artículo 1 — Objeto

Establecer la forma en que los órganos de la Administración del Estado deberán **implementar y/o integrar mecanismos oficiales de autenticación** en sus plataformas electrónicas, para validar con un nivel de confianza determinado los datos de identidad de quienes accedan a plataformas que soportan procedimientos administrativos.

### Artículo 2 — Definiciones

| Término | Definición |
|---------|-----------|
| **Autenticación** | Proceso electrónico que valida datos de identificación de un(a) usuario(a) para permitir acceso a una plataforma electrónica. |
| **Factor de Autenticación** | Dato o conjunto de datos de identificación reservados o inherentes a un(a) usuario(a), que establecen su identidad con distintos grados de confianza. |
| **Mecanismo de Autenticación** | Método o conjunto de procesos electrónicos que sustentan la autenticación con un nivel de confianza determinado. |
| **Mecanismo Oficial de Autenticación** | Mecanismo de autenticación que cumple esta norma y cuenta con validación del MINSEGPRES. |
| **Plataforma Electrónica** | Software, datos e infraestructura tecnológica que sustenta procesos o procedimientos. |
| **Reglamento** | DS Nº 4/2020 MINSEGPRES. |
| **Usuarios(as)** | Interesados(as) en un procedimiento administrativo y funcionarios(as) que acceden a plataformas que lo soportan. |

---

## De los mecanismos oficiales de autenticación

### Párrafo 1º — Sobre ClaveÚnica y Clave Tributaria

### Artículo 3 — Mecanismos oficiales de autenticación

Los órganos deberán utilizar **mecanismos oficiales de autenticación** para el acceso de interesados(as), salvo que corresponda excepción de tramitación electrónica (art. 18 inc. 5° ley Nº 19.880). Si no es posible usar un mecanismo oficial, el órgano podrá usar otro, previa **autorización expresa del MINSEGPRES** (según guía técnica → Artículo 19).

### Artículo 4 — ClaveÚnica

- **Administrador:** MINSEGPRES a través de la División de Gobierno Digital.
- **Uso:** exclusivo para **personas naturales**.
- **Estándar:** OpenID Connect.
- **Factor de Autenticación:** contraseña creada y administrada por la persona, vinculada a su RUN.
- **Enrolamiento y atención:** dependiente del SRCeI.
- **Términos y condiciones:** determinados por la División de Gobierno Digital. Deben ser aceptados por el(la) Jefe(a) Superior de Servicio para integración del organismo (→ guía técnica, Artículo 19).

### Artículo 5 — Clave Tributaria

- **Uso:** exclusivo para **personas jurídicas** o entidades/agrupaciones sin personalidad jurídica.
- **Factor de Autenticación:** contraseña entregada por el SII a contribuyentes.
- **Restricción:** Salvo el SII para sus propias plataformas, **ningún otro órgano puede integrar Clave Tributaria para autenticar personas naturales**. Toda autenticación de personas naturales mediante Clave Tributaria ante órganos distintos del SII **no tendrá validez alguna.**
- **Administrador:** SII, que determina los términos y condiciones (deben ser aceptados por el(la) Jefe(a) Superior de Servicio para integración).

---

### Párrafo 2º — Requisitos técnicos de los mecanismos oficiales de autenticación

### Artículo 6 — Estándares de los mecanismos oficiales de autenticación

- Basados en **OpenID Connect y OAuth 2.0**, o superiores.
- Datos de identificación almacenados **cifrados** (algoritmos: Bcrypt, PBKDF2, SHA-3, Argon2, o superiores).
- Transmisión cifrada con **TLSv1.2**, o superior.
- Registros de gestión y actividades deben ser **trazables** y cumplir el Párrafo 4º de este Título.

### Artículo 7 — Medidas de prevención

Los órganos administradores de mecanismos oficiales deberán:
- Implementar pruebas anti-bot (Captcha u otros).
- Limitar el número máximo de intentos fallidos (con bloqueo al alcanzar el límite).
- Establecer un procedimiento de desbloqueo.

### Artículo 8 — Lineamientos gráficos y usabilidad del proceso de autenticación

- Incorporar buenas prácticas de **experiencia de usuario y accesibilidad web**.
- Cumplir las **definiciones de marca y lineamientos gráficos** provistos por el administrador del mecanismo oficial.

### Artículo 9 — Términos y condiciones de los mecanismos oficiales de autenticación

El órgano que administre un mecanismo oficial deberá publicar los **términos y condiciones** en su página web.

---

### Párrafo 3º — Proceso de integración a los mecanismos oficiales de autenticación

### Artículo 10 — Integración a los mecanismos oficiales de autenticación

Los órganos deberán integrar mecanismos oficiales en sus plataformas que requieran autenticación. El proceso de integración (→ guía técnica, Artículo 19) comprende:

1. Solicitud de integración del órgano al administrador del mecanismo.
2. Entrega de credenciales e integración del mecanismo en la plataforma.
3. Certificación de la integración y habilitación del mecanismo.

### Artículo 11 — Revocación de la habilitación

El administrador de cada mecanismo **revocará de inmediato** la habilitación al órgano que no cumpla los estándares o usos establecidos en esta norma y en las guías técnicas.

---

### Párrafo 4º — Del uso de los mecanismos oficiales de autenticación por los órganos de la Administración del Estado

### Artículo 12 — Deber de información

Los órganos deberán informar **inmediatamente** al CSIRT del Ministerio del Interior y al administrador del mecanismo oficial, ante sospecha de riesgos o amenazas de seguridad (en los mecanismos o en las plataformas que los utilizan), sin perjuicio de otras obligaciones según los términos y condiciones del Artículo 9. También deben informar **oportunamente** al administrador ante eventos que impliquen aumentos de demanda no previstos que puedan afectar el buen funcionamiento.

### Artículo 13 — Registro de trazabilidad de accesos

Los órganos deben implementar y mantener un **registro de accesos** para determinar la trazabilidad de autenticaciones. Para cada acceso autenticado se almacenará al menos:

1. **Identificador del(de la) usuario(a)** que accede. (Para representantes de personas jurídicas con Clave Tributaria, la forma de identificación la determina el SII.)
2. **Fecha y hora** del acceso en UTC+00:00, en permanente sincronización con el Servicio Hidrográfico y Oceanográfico de la Armada de Chile.

### Artículo 14 — Protección de datos personales

Los órganos deben respetar en todo momento la ley Nº 19.628 respecto a quienes se autentiquen, implementando mecanismos que garanticen:
- Reserva y protección de datos personales.
- Derechos de los(as) usuarios(as) de acceder, rectificar, cancelar y oponerse al tratamiento de sus datos cuando sea procedente.
- Uso de datos solo para las finalidades previstas en la ley.

### Artículo 15 — Incorporación de factores de autenticación adicionales

Los órganos **podrán** implementar factores de autenticación **complementarios o adicionales**, especialmente en plataformas con acceso a información sensible. La necesidad de elevar niveles de seguridad debe evaluarse por cada órgano, velando por facilitar el acceso de los interesados.

---

## Validación de un nuevo mecanismo oficial de autenticación

### Artículo 16 — Solicitud para incorporar un nuevo mecanismo oficial de autenticación

Los órganos podrán solicitar en cualquier momento al MINSEGPRES (División de Gobierno Digital) la incorporación de un nuevo mecanismo oficial, adicional a los reconocidos en esta norma. La solicitud será analizada y resuelta previa consulta al SRCeI.

### Artículo 17 — Requisitos técnicos

Los mecanismos que requieran calidad de oficiales deben cumplir, a lo menos, los procesos y estándares de esta norma y los que establezcan las guías técnicas (→ Artículo 19).

### Artículo 18 — Procesos de gestión de usuarios(as)

Para tener calidad de mecanismo oficial, se requiere:

1. **Enrolamiento de Usuarios(as):** proceso seguro que minimice riesgo de suplantación, con tipo y cantidad de datos de identificación proporcionales a las necesidades del procedimiento. Debe incluir protocolo de atención, políticas de privacidad, y acciones de educación y promoción sobre el mecanismo.
2. **Gestión de datos de identificación:** procesos para crear, modificar y revocar credenciales o dispositivos asociados a la autenticación.
3. **Soporte a Usuarios(as):** servicio de soporte para consultas generales y específicas sobre el mecanismo e informar de problemas en su uso.

---

## Disposiciones finales

### Artículo 19 — Guía técnica

La División de Gobierno Digital del MINSEGPRES dictará una o más guías técnicas con los aspectos operativos y procesos de implementación.

### Artículo 20 — Gradualidad

La aplicación es acorde a la gradualidad del DFL Nº 1/2020 MINSEGPRES. La División de Gobierno Digital definirá los lineamientos y formato de cumplimiento para los órganos obligados.

### Artículo 21 — Revisión y actualización de la norma

Revisión y actualización **al menos cada dos años**, contados desde la entrada en vigencia. Las actualizaciones considerarán aprendizajes y dificultades reportados por los órganos, impulsando buenas prácticas y minimizando efectos de prácticas incorrectas.
