---
_manifest:
  urn: urn:gov:kb:intro-tde
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- gobierno
- chile
- estrategia
- normativa
- interoperabilidad
- ciberseguridad
- datos
- knowledge
lang: es
---

# Guía Maestra de Transformación Digital del Estado (TDE)

## Marco Estratégico TDE

### Visión 2030 y Objetivos
- Estado unificado, proactivo y confiable.
- Uso estratégico y ético de datos.
- Ecosistema de identidad digital centrado en las personas.
- Superar promedio OCDE en confianza.


| Objetivo | Definición |
| :--- | :--- |
| Experiencia Digital | Simplicidad, eficiencia e inclusión para personas y empresas. |
| Estrategia de Datos | Fortalecimiento del diseño de políticas públicas mediante datos. |
| Integración | Articulación del Estado como unidad de servicios y procesos. |
| Gobernanza | Consolidación de la rectoría digital nacional. |
| Talento Digital | Desarrollo de competencias en el sector público. |
| Sostenibilidad | Modelo escalable de servicios digitales compartidos. |
| Identidad Digital | Sistema nacional seguro con colaboración público-privada. |

### Desafíos Críticos
| Categoría | Descripción |
| :--- | :--- |
| Gobernanza | Fragmentación institucional; ausencia de rectoría en datos e identidad. |
| Confianza | Baja confianza ciudadana (24% Chile vs 45% OCDE); fraude digital al alza. |
| Operacional | Silos y sistemas obsoletos; solo 1% de municipios integrados. |
| Capacidades | Escasez de talento especializado; resistencia al cambio. |

### Principios Rectores
*   **Digital por diseño:** Integración tecnológica desde el inicio.
*   **Centrado en personas:** Simplicidad, accesibilidad y control de datos.
*   **Gobierno integrado:** Interoperabilidad y principio de "una sola vez".
*   **Eficiencia:** Optimización de recursos para impacto público.
*   **Gobierno abierto:** Transparencia y reutilización de datos.
*   **Innovación abierta:** Ecosistema GovTech activo.
*   **Seguridad y confianza:** Protección de datos y gestión de riesgos.
*   **Resiliencia:** Continuidad operacional y sostenibilidad.

- ---


## Ejes Estratégicos e Iniciativas

| Eje | Iniciativas Clave |
| :--- | :--- |
| **1. Servicios Personas** | Rectoría Gob.cl; estándares UX/UI; App móvil central; ChileAtiende con IA; Medición MESU. |
| **2. Sector Público Eficiente** | Expediente electrónico; Notificador electrónico; ERP municipal; Fortalecimiento EvalTIC. |
| **3. Gestión de Datos** | Consejo Estratégico de Datos; PMG Gobernanza; Nueva Interoperabilidad; Lago de Datos. |
| **4. Gobernanza** | Fortalecimiento SGD; Modernización normativa IA/Datos; Red de Coordinadores TD. |
| **5. Talento Digital** | Campus Digital; Estatuto especial TIC; Alfabetización digital. |
| **6. Identidad e Infra** | Cédula Digital; Estrategia Cloud-first; Carpeta Ciudadana; Wallet de credenciales. |

- ---


## Marco Institucional y Legal

### Institucionalidad
*   **Rectoría:** Secretaría de Gobierno Digital (SGD) - Ministerio de Hacienda.
*   **Soporte:** Ley 21.658.
*   **Mandato Central (Ley 21.180):** Procedimientos administrativos 100% electrónicos (Cero Papel).
*   **Fecha Límite:** 31-12-2027.

### Normas Técnicas (Decretos Supremos)
| Norma | Foco | Requisitos Clave |
| :--- | :--- | :--- |
| **DS 7 (Seguridad)** | Ciberseguridad | Política de Seguridad formal; Marco NIST; Responsable Institucional (RIS). |
| **DS 9 (Autenticación)** | Identidad | Uso obligatorio de ClaveÚnica (Personas) y Clave Tributaria (Empresas). |
| **DS 12 (Interoperabilidad)** | Datos | Uso de Red de Interoperabilidad; Cese de PISEE al 31-12-2026. |
| **DS 10 (Documentos)** | Gestión Doc. | Política de Gestión Documental; Identificador Único (IUIe); Microformas. |
| **DS 8 (Notificaciones)** | Comunicación | Domicilio Digital Único (DDU); Notificación válida tras 3 días hábiles. |
| **DS 11 (Calidad)** | Mejora Continua | Catálogo de plataformas; Designación de Coordinador TD por Jefe de Servicio. |

- ---


## Gobernanza y Ciclo de Inversión TIC

### Actores del Ecosistema
| Nivel | Actor | Rol |
| :--- | :--- | :--- |
| **Transversal** | Hacienda / SGD | Liderazgo, coordinación TDE y plataformas compartidas. |
| **Presupuestario** | DIPRES | Gestión de proceso EVALTIC y recursos. |
| **Institucional** | Comité de TD | Gobernanza interna, diagnósticos y Plan de TD. |
| **Técnico** | Coordinador TD | Enlace técnico institucional con SGD. |
| **Ejecución** | PMO / Jefatura Proy. | Gestión de proyectos, metodologías y estándares. |

### Fase 1: EVALTIC (Formulación)
*   **Clasificación:** Operación (bajo riesgo), Crecimiento (medio), Transformación (alto).
*   **Restricciones:** Prohibido aumento de dotación permanente vía TIC; prohibido ampliar datacenters propios (salvo excepción).
*   **Prioridad:** Alineamiento Cloud First y estándares TDE.

- ---


## Pilares Habilitadores

### Infraestructura Digital
*   **Cloud First:** Preferencia por servicios SaaS; evaluación de fiabilidad y seguridad.
*   **SIMPLE SaaS:** Plataforma de procesos; eliminación automática de archivos a los 30 días.
*   **ClaveÚnica:** Credencial digital oficial; protocolo OpenID Connect; prohibido uso de iframes.

### Gestión de Datos
*   **Activo Estratégico:** Datos deben ser catalogados y tener responsables (CDO/Data Stewards).
*   **MGDE:** Marco de 12 dimensiones para evaluación de madurez.
*   **Metadatos:** Esquema obligatorio (29 metadatos para expedientes, 46 para documentos).
*   **Anonimización:** Técnicas de enmascaramiento, aleatorización y generalización (K-Anonimidad).

### Ciberseguridad (Ciclo NIST)
1.  **Identificar:** Inventario de activos y gestión de riesgos.
2.  **Proteger:** Mínimo privilegio; MFA; contraseñas 10+ caracteres; desarrollo seguro (OWASP).
3.  **Detectar:** Monitoreo de red y correlación de logs.
4.  **Responder:** Plan de respuesta; notificación obligatoria a ANCI/CSIRT.
5.  **Recuperar:** Planes de continuidad (BCP) y recuperación ante desastres (DRP).

- ---


## Diseño y Valor Público

### Estándares de Diseño
*   **Accesibilidad:** Cumplimiento obligatorio WCAG-AA.
*   **Lenguaje:** Voz activa, trato de "tú", tono positivo; oraciones < 20 palabras.
*   **Metodología:** Investigación con usuarios, prototipado e iteración ágil.
*   **Calidad Web:** Instrumento de evaluación (Imprescindible 60%, Esperable 25%, Deseable 15%).

- ---


## Anexos y Glosario

| Término | Definición |
| :--- | :--- |
| **Interoperabilidad** | Transferencia de datos en línea con mínima intervención humana. |
| **Datos Abiertos** | Datos digitales de uso, reutilización y redistribución libre. |
| **Servicios Compartidos** | Herramientas utilizadas por dos o más órganos del Estado. |
| **Wallet** | App para gestionar credenciales verificables y documentos digitales. |
| **CPAT** | Catálogo de Procedimientos Administrativos y Tramitaciones. |

- ---


## Hitos Relevantes 2024-2025

| Fecha | Hito | Impacto |
| :--- | :--- | :--- |
| **Jun-2024** | Inscripción ANCI | GOREs definidos como "Servicios Esenciales" (obligatorio). |
| **Ago-2024** | UI Kit v1.0 | Estándar visual para plataformas web del Gobierno. |
| **Sep-2024** | Ranking UN | Chile alcanza lugar 31 mundial en E-Government. |
| **Oct-2024** | Portal Datos Abiertos | Nueva versión de datos.gob.cl con visualización geoespacial. |
| **Ene-2025** | DocDigital Municipal | 80% de municipios habilitados para comunicaciones oficiales. |
| **Abr-2025** | WikiGuías | Lanzamiento de plataforma oficial de directrices técnicas SGD. |
| **Jun-2025** | Ley Gestión Datos | Proyecto de ley para intercambio estandarizado de datos públicos. |
