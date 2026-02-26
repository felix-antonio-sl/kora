---
_manifest:
  urn: urn:gov:kb:cloud-publica
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- cloud
- infraestructura
- compras-publicas
- gobierno-digital
- chile
- knowledge
lang: es
---

# Recomendaciones Técnicas para la Adquisición de Servicios de Cloud Pública

Fuente: WikiGuías SGD — `urn:gov:kb:cloud-publica`
Alcance: OAEs (Órganos de la Administración del Estado). Carácter consultivo; permanente revisión.
Elaborado con aportes del Consejo de Política de Suministro TI, ChileTec y ACTI A.G.

## Conceptos Clave

| Término | Definición |
|---|---|
| Cloud Computing | Modelo de acceso bajo demanda, vía red, a recursos compartidos y configurables (redes, servidores, almacenamiento, aplicaciones, servicios), con mínima gestión del proveedor (NIST, 2011) |
| Cloud First | Los OAEs deben evaluar preferentemente uso de servicios en la nube al diseñar arquitecturas tecnológicas, sobre infraestructuras propias, respetando eficiencia, legalidad, neutralidad tecnológica y seguridad |
| Cloud Smart | La adopción de nube debe considerar objetivos estratégicos, modelos de operación, criterios financieros y protección de datos; complementa Cloud First con estrategia gradual e integral |
| Cloud Pública | Servicios de cómputo operados por proveedor externo, accesibles vía internet, compartidos entre múltiples clientes, pago por uso |
| Territorialidad de datos | En Cloud Pública la ubicación física de los datos puede ser extraterritorial; la normativa chilena no exige datos dentro del territorio nacional salvo disposiciones sectoriales específicas |

Características del modelo Cloud:
- Autoservicio bajo demanda
- Amplio acceso a la red
- Agrupación de recursos
- Elasticidad rápida
- Servicio medido

Modelo financiero: OPEX vs CAPEX — facilita asignación de recursos; menor inversión inicial.

## Criterios Generales para Adopción

Mover cargas tecnológicas al Cloud Público requiere más que contratar infraestructura externa. Requisitos mínimos:

1. Evaluación de las reales necesidades
2. Definición de expectativas
3. Disponibilidad de capacidades profesionales (internas y/o externas)
4. Planificación detallada
5. Diseño de nuevo modelo de operación

Oportunidades:
- Actualización tecnológica permanente
- Menor personal dedicado a operación de infraestructura propia
- Respaldo y gestión permanente de seguridad
- Flexibilidad y escalabilidad
- Continuidad operacional

**Propiedad de datos (SaaS):** Los términos de servicio deben indicar explícitamente que los datos son propiedad del OAE y que nunca se transfiere su propiedad ni derechos de uso al proveedor. Al término del contrato, exigir devolución en formatos estándar y borrado seguro.

## Árbol de Decisiones Pre-Adopción

Preguntas de respuesta Sí/No para evaluar preparación institucional. Objetivo: responder Sí a todas.

| ID | Pregunta | Guía si NO |
|---|---|---|
| Q1 | ¿Cuenta con ≥2 profesionales (internos o externos) con experiencia en control y gestión de Cloud (Administradores de Sistemas, DevOps, SREs)? | Diseñar mecanismo para contar con al menos dos profesionales idóneos antes de avanzar |
| Q2 | ¿Tiene sistemas productivos legacy críticos que aún no puede migrar? | Si requiere migración urgente por obsolescencia/riesgos, evaluar "lift and shift" como medida temporal |
| Q3 | ¿Sus sistemas deben escalar de manera repentina o impredecible? | Evaluar Cloud solo para capacidades actuales o crecimiento vegetativo; también considerar housing/hosting |
| Q4 | ¿Tiene documentadas sus aplicaciones, infraestructura y sistemas? (diagrama infraestructura, CMDB, diagramas despliegue, TPS, RTO/RPO, mapa procesos) | Establecer proyecto de migración que incluya estrategia de documentación |
| Q5 | ¿Tiene planificada (Gantt) la migración con actividades, tiempos y recursos? | Definir y documentar plan de migración; apoyarse en proveedores especializados si corresponde |
| Q6 | ¿Posee área de ciberseguridad y un CISO, con recursos propios o externalizados? | El rol de CISO institucional debe ser interno; labores técnicas y operativas pueden ser externas |

## Qué Comprar: Modelos de Servicio

**SaaS** — cuando se requiere software específico que solo necesita configuración (ERP, CRM, KMS, CMS, ofimática). Ejemplos: Google Workspace, Office 365, Zimbra.

**IaaS / PaaS** — cuando la institución gestiona aplicaciones propias o de terceros que requieren escalar. Servicios típicos:
- Cómputo (máquinas y servidores virtuales)
- Plataformas para contenedores
- Redes virtuales
- Bases de datos y big data
- Almacenamiento
- Herramientas de seguridad (firewalls virtuales, detección de amenazas)
- Entornos de desarrollo
- Sistemas de gestión de identidad y acceso

Catálogo de servicios disponibles (no excluyente, disponible en IaaS/PaaS/BaaS/CaaS/SaaS):
Máquina virtual, repositorios de almacenamiento, sistema de archivos distribuidos, Kubernetes elástico, balanceo de tráfico, BD relacional, DNS, CDN estáticos, correo, monitoreo de infraestructura, WAF, BD no relacional (Mongo Atlas), encolamiento, ETL, data streams, Datawarehouse, detección de amenazas, Inspector (evaluación de seguridad automática), BD como servicio, IA como servicio, MBaaS, gestión de API, identidad y acceso como servicio.

Modelo de compra: los proveedores ofrecen créditos de dinero para adquisición de servicios; explicitar en la compra los servicios específicos donde se utilizarán.

## Selección de Proveedores

Tipos de proveedores:
- Hyperscalers: globales, corporaciones tecnológicas globales
- Regionales: cubren un continente; empresas de servicios tecnológicos y telecomunicaciones
- Locales: nacionales, servicios específicos o de alcance local

No existe a priori un tipo de proveedor mejor para todas las instituciones. La selección depende de: especificidad de servicios, SLA requerido, capacidad institucional y recursos financieros.

Características clave a evaluar:

| Dimensión | Criterios |
|---|---|
| Fiabilidad y disponibilidad | Uptime acorde a niveles de servicio; infraestructura redundante; procedimientos de continuidad operacional |
| Seguridad | Cumplimiento normativo; gestión de identidad y acceso robusta; modelo de responsabilidades claro entre proveedor e institución |
| Escalabilidad y flexibilidad | Escalamiento automático arriba/abajo; variedad de servicios (desde almacenamiento básico hasta IA) |
| Rendimiento | CDN; localización de centros de datos cercana para menor latencia |
| Soporte | Niveles de soporte ante incidencias; documentación detallada; comunidad activa |

## Rol de Partners y Socios Comerciales

En muchos casos la provisión es indirecta vía reseller/partner/socio comercial (especialmente hyperscalers y regionales en Chile). Impactos:
- Consumo visible en consola puede diferir del monto final a pagar por márgenes, impuestos, conversión de monedas.
- Soporte de primer nivel lo provee el partner; escala al proveedor global cuando es necesario.

Obligación legal: art. 35 bis, Ley N° 19.886 — en contrataciones complejas, los OAEs deben obtener y analizar previamente información técnica, de precios y costos del ciclo de vida útil. Si se requiere consulta a terceros, realizarla mediante consulta pública en el Sistema de Información de Compras y Contrataciones del Estado. Las reuniones presenciales o virtuales con potenciales proveedores proceden solo cuando sea imprescindible por el tipo de bien/servicio.

Requisitos del modelo de servicios:
- Definir responsabilidades y funciones de: institución / socio comercial / proveedor de Nube
- Definir modelo de control de la consola de servicios y distribución de responsabilidades en su administración

## SLA: Acuerdos de Nivel de Servicio

SLA = marco contractual que define métricas, calidad, disponibilidad y compensaciones por incumplimiento.

Elementos del SLA:

| Elemento | Descripción |
|---|---|
| Disponibilidad (uptime) | Porcentaje de tiempo con servicio disponible (expresado en "nueves", ej. 99,9%) |
| Rendimiento | Límites y capacidades de recursos (almacenamiento, procesamiento, TPS, I/O, red) |
| Tiempo de respuesta | Período máximo para responder a solicitud o incidencia |
| Mantenimiento programado | Períodos de servicio fuera de línea por mantenimiento planificado |
| Compensación por incumplimiento | Créditos de servicio o extensiones de contrato ante incumplimientos |
| Seguridad y cumplimiento normativo | Medidas de seguridad y estándares que el proveedor debe cumplir |
| Escalación y resolución | Procedimientos para informar y resolver problemas (plazos y responsabilidades) |
| Backup y recuperación | Políticas de respaldo, frecuencia y recuperación ante pérdida o corrupción |

Ejemplo de SLA diferenciado por horario:
- Servicio crítico en horario hábil: 99,5% disponibilidad; 30 min. tiempo de respuesta de soporte
- Mismo servicio fuera de horario hábil: 97% disponibilidad; 4 horas de respuesta ante incidentes

Recomendaciones para establecimiento e implementación:
- Definir objetivos institucionales y servicios críticos antes de negociar
- Personalizar SLAs según necesidades específicas del OAE; no aceptar términos genéricos
- Negociar proactivamente métricas y penalidades con datos de uso proyectado y riesgos
- Incluir cláusulas de revisión periódica y escenarios de escalabilidad futura
- Definir multas por incumplimiento y compensaciones proporcionales al impacto
- Designar equipo de gestión para supervisar cumplimiento (áreas técnica, legal y de gestión)
- Programar revisiones periódicas con proveedor; automatizar informes de cumplimiento
- Implementar sistema de seguimiento de incidentes para análisis posterior y mejora continua

## Referencias

- NIST (2011). Definition of Cloud Computing.
- Héctor Nigro (2022). Cloud computing: retos y oportunidades.
- Ley N° 19.886 y artículo 35 bis (Compras públicas y contratación).
- Instructivo Presidencial N° 1 (2018) sobre adopción preferente de servicios en la nube.
