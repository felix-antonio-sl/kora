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

# Lineamientos Técnicos: Recomendaciones para la adquisición de servicios de Cloud Pública

## Contexto y Objetivo

| Atributo | Descripción |
| :--- | :--- |
| **Objetivo** | Entregar recomendaciones técnicas para adquisición de servicios de Cloud Pública en OAEs, enfocadas en precompra, selección de proveedor y SLAs. |
| **Propósito** | Orientar definición de requerimientos técnicos y apoyar formulación de proyectos EvalTI. |
| **Alcance** | Carácter consultivo, aplicable a profesionales TI de la Administración del Estado. |
| **Vigencia** | Revisión permanente según evolución tecnológica y normativa. |

## Conceptos Cloud Pública

| Concepto | Definición |
| :--- | :--- |
| **Cloud Computing** | Acceso bajo demanda a recursos configurables (redes, servidores, almacenamiento) con mínima gestión del proveedor. |
| **Nube Primero** | Evaluación preferente de servicios nube sobre infraestructura propia en diseños arquitectónicos. |
| **Nube Inteligente** | Adopción estratégica basada en objetivos operativos, financieros y de protección de datos. |
| **Territorialidad** | Ubicación física de datos puede ser extraterritorial; normativa chilena no exige residencia nacional por defecto. |

## Criterios Generales de Adopción

### Requisitos Mínimos
- Evaluación de necesidades reales.
- Definición clara de expectativas.
- Capacidades profesionales (internas/externas).
- Planificación detallada y nuevo modelo operativo.

### Beneficios y Oportunidades
- Actualización tecnológica permanente.
- Reducción de personal en operación de infraestructura física.
- Gestión de seguridad y respaldo delegado.
- Escalabilidad y continuidad operacional.
- Cambio de modelo financiero: CAPEX a OPEX.

### Propiedad y Gestión de Datos
- **Propiedad:** El OAE mantiene propiedad absoluta; prohibida transferencia de derechos al proveedor.
- **Acceso:** Exigir disponibilidad de datos/metadatos en formatos estándar y documentados.
- **Término:** Definir condiciones de devolución y borrado seguro de información.

## Evaluación de Madurez (Preguntas Clave)

| Pregunta | Acción si SÍ | Acción si NO |
| :--- | :--- | :--- |
| ¿Equipo de min. 2 profesionales con exp. Cloud? | Avanzar a siguiente pregunta. | Diseñar mecanismo para contar con equipo idóneo. |
| ¿Sistemas legacy críticos no migrables? | Evaluar "lift and shift" temporal. | Avanzar a siguiente pregunta. |
| ¿Requerimiento de escalabilidad repentina? | Considerar capacidades elásticas. | Evaluar Cloud para uso base o housing/hosting. |
| ¿Infraestructura y sistemas documentados? | Avanzar a siguiente pregunta. | Ejecutar proyecto de documentación previa. |
| ¿Plan de migración definido (Gantt)? | Avanzar a siguiente pregunta. | Definir plan con recursos y tiempos. |
| ¿Área de ciberseguridad y CISO? | Avanzar a diseño detallado. | Definir resolución de funciones; CISO debe ser interno. |

## Modelos de Servicio y Selección

### Recomendaciones por Modalidad
- **SaaS (Software as a Service):** Preferir para software estándar (ERP, CRM, Ofimática).
- **IaaS/PaaS:** Usar cuando se requiere gestionar, modificar o desarrollar aplicaciones propias.

### Catálogo de Servicios Comunes
- Cómputo (VMs) y Contenedores (Kubernetes).
- Almacenamiento y Bases de Datos (Relacionales/No Relacionales).
- Redes, DNS, WAF y Balanceo de tráfico.
- Seguridad (Detección de amenazas, inspección automática).
- IA y Analítica (Datawarehouse, ETL, Data streams).

## Selección de Proveedores

| Criterio | Requerimiento Técnico |
| :--- | :--- |
| **Fiabilidad** | Niveles de uptime acordes a criticidad y centros de datos redundantes. |
| **Seguridad** | Cumplimiento normativo, robustez en gestión de identidad y modelo de responsabilidad compartida. |
| **Escalabilidad** | Capacidad automática arriba/abajo y variedad de servicios avanzados. |
| **Rendimiento** | Optimización vía CDN y proximidad geográfica de centros de datos (baja latencia). |
| **Soporte** | Niveles de respuesta claros, documentación exhaustiva y comunidad activa. |

## Rol de Partners y Socios

### Gestión Comercial y Técnica
- **Provisión:** Relación usual a través de resellers o partners locales.
- **Modelo Financiero:** Considerar márgenes, impuestos y conversión de moneda en presupuestos.
- **Soporte:** Partner actúa como primer nivel; escalamiento a proveedor global según necesidad.

### Requisitos de Contratación
- Definir claramente responsabilidades entre OAE, Partner y Proveedor Cloud.
- Establecer modelo de control y administración de la consola de servicios.
- Aplicar mecanismos de análisis de ciclo de vida (Art. 35 bis, Ley 19.886).

## Acuerdos de Nivel de Servicio (SLA)

### Métricas Fundamentales
- **Uptime:** Tiempo de actividad garantizado (ej. 99.9%).
- **Rendimiento:** Límites de procesamiento, I/O y latencia de red.
- **Respuesta:** Tiempos máximos para atención de incidencias.
- **Backup:** Frecuencia de respaldos y tiempos de recuperación (RTO/RPO).

### Gestión del Acuerdo
- **Personalización:** Ajustar SLAs a misión institucional; evitar términos genéricos.
- **Compensaciones:** Definir créditos de servicio o multas ante incumplimientos.
- **Monitoreo:** Designar equipo supervisor y usar herramientas en tiempo real.
- **Revisión:** Programar reuniones periódicas para ajustes y mejora continua.

## Referencias y Normativa

### Marco Legal Chile
- **Ley N° 19.886:** Ley de Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios.
- **Art. 35 bis (Ley 19.886):** Obligación de análisis técnico/financiero previo en contrataciones complejas.
- **Instructivo Presidencial N° 1 (2018):** Directrices sobre adopción preferente de servicios en la nube.

### Referencias Técnicas
- NIST (2011). Definition of Cloud Computing.
- SGD (Chile). Lineamientos Técnicos WikiGuías.
- Nigro (2022). Cloud computing: retos y oportunidades.
