---
_manifest:
  urn: "urn:tde:kb:guia-cloud-publica"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/guias/guias/recomendaciones_cloud"
version: 1.0.0
status: published
tags: [cloud, iaas, paas, saas, sla, tde, guia, adquisicion]
lang: es
---

# Recomendaciones técnicas para adquisición de Cloud Pública en OAE

- **Autor**: Secretaría de Gobierno Digital (SGD)
- **Versión**: 2ª (en revisión permanente)

## Objetivo

Recomendaciones técnicas para adquisición de servicios de Cloud Pública por OAE, orientadas a profesionales TI en etapa de precompra. Incluye consideraciones para elección de proveedor y definición de SLAs.

## Alcance

Carácter consultivo. Orienta definición de requerimiento técnico para adquisición de servicios en Nube Pública y formulación de proyectos EVALTIC. No abarca preservación digital, seguridad de la información ni determinación de mecanismos de compra.

## Conceptos clave

| Concepto | Definición |
|----------|-----------|
| Cloud Computing | Acceso bajo demanda vía red a recursos compartidos y configurables (redes, servidores, almacenamiento, aplicaciones) con mínima gestión del proveedor (NIST, 2011) |
| Cloud First | OAE evalúan uso preferente de nube sobre infraestructura propia (on-premise, housing), observando eficiencia, legalidad, neutralidad tecnológica y seguridad. Instructivo Presidencial N° 1, 2018 |
| Cloud Smart | Considerar objetivos estratégicos, modelos de operación, finanzas y protección de datos al adoptar/operar nube. Compatible con Cloud First |
| Territorialidad de datos | Normativa chilena, por regla general, no exige ubicación de datos dentro de fronteras nacionales → permite uso de Cloud Pública, salvo normativa sectorial/interna contraria |

## Criterios generales para uso de Cloud Pública

**Requisitos previos mínimos**:
- Evaluación de necesidades reales
- Definición de expectativas
- Disponibilidad de capacidades profesionales (internas/externas)
- Planificación detallada
- Diseño de nuevo modelo de operación

**5 características esenciales Cloud Público** (NIST):
1. Autoservicio bajo demanda
2. Amplio acceso a red
3. Agrupación de recursos
4. Elasticidad rápida
5. Servicio medido

**Oportunidades**: actualización tecnológica permanente, menor personal operación, respaldos, seguridad gestionada, flexibilidad, escalabilidad, continuidad operacional, menores montos de inversión.

**Modelo financiero**: OPEX (gastos operación) vs. CAPEX (inversión) → facilita asignación de recursos.

**Propiedad de datos**: verificar que términos de servicio expliciten que datos son propiedad del OAE contratante, sin transferencia de propiedad/derecho de uso al proveedor. Datos (y metadata) solicitables en cualquier momento en formatos estándar. Especial observación al término de contrato.

## Árbol de decisiones para la compra

| # | Pregunta | Si SÍ | Si NO |
|---|----------|-------|-------|
| 1 | ¿Cuenta con ≥2 profesionales (internos/externos) con experiencia en Cloud, SysAdmin, DevOps y/o SRE? | → Pregunta 2 | Diseñar mecanismo para contar con ≥2 profesionales idóneos → Pregunta 2 |
| 2 | ¿Tiene sistemas legacy críticos que no puede migrar? | Si urgencia por obsolescencia → evaluar "lift and shift" como medida temporal → Pregunta 3 | → Pregunta 3 |
| 3 | ¿Los sistemas deben escalar de forma repentina/no predecible? | → Pregunta 4 | Evaluar Cloud sólo para capacidad actual + crecimiento vegetativo, o housing/hosting → Pregunta 4 |
| 4 | ¿Tiene documentadas apps, infraestructura y sistemas? (6 instrumentos: diagrama infraestructura, CMDB, diagramas despliegue, demanda transacciones, RTO/RPO, mapa procesos-sistemas) | Los 6 → Pregunta 5 | Proyecto de migración previo para documentar → Pregunta 5 |
| 5 | ¿Tiene planificado (Gantt) actividades y tiempo de migración? | → Pregunta 6 | Establecer planificación y documentar plan de migración → Pregunta 6 |
| 6 | ¿Posee área de ciberseguridad y CISO? | → Capítulo 2 "Qué comprar" | Resolver funciones CISO (rol interno obligatorio, apoyo técnico puede ser externo) → Capítulo 2 |

## Qué comprar

### SaaS (Software as a Service)

**Cuándo**: capacidades técnicas limitadas + necesidad de software específico que sólo requiere configuración (ERP, CRM, KMS, CMS). No se recomienda Cloud Pública para instalar aplicaciones desde cero sin capacidades técnicas.

**Ejemplo**: Google Workspace, Office 365, Zimbra.

### IaaS + PaaS

**Cuándo**: aplicaciones propias/terceros que requieren escalar, se pueden gestionar/modificar/desarrollar/migrar. Requiere recursos profesionales adecuados para administrar espacio, BD, balanceo de carga.

### Servicios Cloud adquiribles

| Categoría | Servicios |
|-----------|----------|
| Cómputo | Máquinas/servidores virtuales |
| Contenedores | Gestores y plataformas (Kubernetes elástico) |
| Red | Redes virtuales, DNS, CDN, balanceo de tráfico |
| Datos | BD relacional, BD no relacional (Mongo Atlas), Data streams, Datawarehouse, ETL |
| Almacenamiento | Repositorios, sistemas de archivos distribuidos |
| Seguridad | Firewalls virtuales, detección amenazas, WAF, evaluación seguridad automática |
| Desarrollo | Entornos de desarrollo, gestión de API, MBaaS |
| Identidad | Gestión de identidad y acceso como servicio |
| Monitoreo | Monitoreo de infraestructura |
| Correo | Servicio de correos |
| IA | Inteligencia artificial como servicio |
| Encolamiento | Servicio de encolamiento |

**Modelo de compra**: proveedor ofrece "créditos" equivalentes a suma de dinero. Puede incluir soporte. Compra debe explicitar servicios en que se usarán créditos (IaaS, PaaS, BaaS, CaaS, SaaS).

## Elección del proveedor

### Tipos de proveedores

| Tipo | Alcance |
|------|---------|
| Hyperscalers | Globales, corporaciones tecnológicas |
| Regionales | Continentales, empresas de servicios TI y telecomunicaciones |
| Locales | Nacionales, servicios a demanda más específicos |

Selección depende de: especificidad de servicios, SLA requerido, capacidad institucional de administración, recursos financieros.

### 5 criterios clave de evaluación

| Criterio | Elementos |
|----------|----------|
| **Fiabilidad y disponibilidad** | Uptime adecuado a niveles de servicio, centros de datos redundantes para continuidad |
| **Seguridad** | Cumplimiento normativo, gestión de identidad y acceso robusta, modelo claro de responsabilidades proveedor-institución |
| **Escalabilidad y flexibilidad** | Escalamiento automático arriba/abajo, variedad de servicios (almacenamiento a IA) |
| **Rendimiento** | CDN para entrega de contenido, proximidad geográfica de centros de datos (latencia) |
| **Soporte** | Niveles de soporte ante incidencias, recursos de ayuda, documentación, comunidad activa |

### Rol de partners/resellers

- Provisión frecuentemente indirecta: reseller/partner/socio comercial firma contrato y mantiene relación técnico-comercial
- Hyperscalers y regionales operan en Chile mediante partners
- Consumo en consola puede diferir de monto final (márgenes, impuestos, conversión de moneda)
- Soporte primer nivel → partner; escalamiento → proveedor global
- Art. 35 bis Ley N° 19.886: contrataciones complejas requieren análisis técnico, financiero, ciclo de vida útil, consulta al mercado

**Considerar en requerimientos de compra**:
1. Expectativas técnicas y comerciales del modelo de operación
2. Modelo comercial (tasas adicionales, precios, cobros, impuestos según instrumento de compra)
3. Modelo de servicios: responsabilidades institución + socio comercial + proveedor Nube + control de consola

## Acuerdos de Nivel de Servicio (SLA)

### Definición

Parte de relación contractual que establece calidad, disponibilidad y rendimiento. Define métricas (uptime, tiempos de respuesta, almacenamiento). SLAs deben ser acordes a misión, visión, objetivos institucionales y tipo de servicios.

### Ejemplo de SLAs

- Servicio crítico en horario hábil: 99.5% disponibilidad, 30 min tiempo de respuesta soporte
- Mismo servicio fuera de horario: 97% disponibilidad, 4 horas respuesta

### Elementos de un SLA

| Elemento | Descripción |
|----------|-------------|
| Disponibilidad (uptime) | % de tiempo disponible. Se expresa en "nueves" (ej. 99.9%) |
| Rendimiento | Límites de almacenamiento, procesamiento, transacciones/s, IOPS, red |
| Tiempo de respuesta | Período máximo de respuesta a solicitudes/incidencias |
| Mantenimiento programado | Períodos planificados fuera de línea |
| Compensación por incumplimiento | Créditos de servicio, extensiones de contrato |
| Seguridad y cumplimiento | Medidas de seguridad, estándares y regulaciones |
| Escalación | Procedimientos para informar/resolver problemas, plazos, responsabilidades |
| Backup y recuperación | Políticas de respaldo, frecuencia, procedimientos de recuperación |

### Establecimiento del SLA

1. Definir objetivos y requisitos claros (servicios críticos, rendimiento, seguridad)
2. Establecer expectativas claras y comprensibles para ambas partes
3. Personalizar SLA según necesidades específicas
4. Negociación proactiva con métricas y datos de uso proyectado
5. Definir multas y compensaciones proporcionales
6. Incluir cláusulas de revisión periódica
7. Considerar escalabilidad futura
8. Mantener relación de colaboración con reuniones periódicas de revisión

### Seguimiento y cumplimiento

1. Equipo dedicado de gestión (técnica, legal, gestión)
2. Métricas clave de monitoreo definidas
3. Herramientas de monitoreo en tiempo real
4. Revisiones periódicas programadas con proveedor
5. Informes de cumplimiento automatizados
6. Auditorías periódicas (internas/externas)
7. Gestión proactiva de problemas (desviaciones recurrentes)
8. Sistema de seguimiento de incidentes
9. Revisión y actualización del SLA según necesidades cambiantes
10. Comunicación abierta con canales efectivos
