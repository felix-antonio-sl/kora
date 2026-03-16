---
_manifest:
  urn: "urn:tde:kb:recomendaciones-tecnicas-cloud-publica"
  provenance: "https://wikiguias.digital.gob.cl/guias/guias/recomendaciones_cloud"
version: 1.0.0
status: published
tags: [tde, lineamientos-guias, guia-tecnica, cloud]
lang: es
---

# Recomendaciones Técnicas para la Adquisición de Servicios de Cloud Pública en los OAE

**Elaborado por:** Secretaría de Gobierno Digital (SGD)
**Versión:** Segunda versión (actualización periódica)
**Carácter:** Consultivo — orienta la definición del requerimiento técnico en la etapa de precompra; contribuye a formulación de proyectos en el marco de EVALTIC. No resuelve problemáticas de preservación digital, seguridad de la información o determinación de mecanismos de compra.
**Agradecimientos:** Consejo de Política de Suministro TI, industria tecnológica nacional (ChileTec, ACTI A.G.)

---

## Conceptos clave

| Concepto | Definición |
|---------|-----------|
| Cloud Computing | Acceso bajo demanda y a través de la red a recursos compartidos configurables (redes, servidores, almacenamiento, aplicaciones y servicios), asignados y liberados con mínima gestión del proveedor (NIST, 2011) |
| Nube Primero (Cloud First) | Evaluación preferente de servicios en la nube sobre infraestructuras propias o administradas (on premise, housing o similares), observando principios de eficiencia, legalidad, neutralidad tecnológica y seguridad. Establecido en Instructivo Presidencial N°1/2018 |
| Nube Inteligente (Cloud Smart) | Los OAE deben considerar objetivos estratégicos, modelos de operación, aspectos financieros y protección de datos al adoptar y operar soluciones en la nube. Armonizable con Cloud First para una estrategia gradual, integral y efectiva |
| Territorialidad de los datos | La normativa chilena, por regla general, **no exige** que los datos estén dentro de las fronteras nacionales, salvo que exista normativa sectorial o interna que disponga lo contrario |

---

## Capítulo 1: Árbol de decisiones para la compra

La adopción de Cloud Público requiere diseño estratégico mínimo e implica al menos:
- Evaluación de las reales necesidades
- Definición de expectativas
- Disponibilidad de capacidades profesionales (internas y/o externas)
- Planificación detallada
- Diseño de un nuevo modelo de operación

**5 características esenciales del modelo Cloud Público:**
1. Autoservicio bajo demanda
2. Amplio acceso a la red
3. Agrupación de recursos
4. Elasticidad rápida
5. Servicio medido

**Oportunidades del Cloud Público:**
- Actualización tecnológica permanente
- Disminución de personal dedicado a operación
- Respaldos automáticos
- Gestión permanente de seguridad
- Flexibilidad y escalabilidad
- Continuidad operacional
- Menores montos de inversión inicial
- Modelo OPEX (gastos de operación) vs. CAPEX (inversión), facilitando asignación de recursos

**Propiedad de los datos:** para servicios SaaS, verificar que los términos de servicio indiquen explícitamente que los datos son propiedad del OAE contratante, sin transferencia de propiedad ni derecho de uso al proveedor. Los datos y metadata deben poder ser solicitados en cualquier momento en formatos estándar. Criterio de especial observación al término del contrato.

---

### Árbol de decisiones — 6 preguntas

Cuestionario de respuesta Sí/No. Para asegurar adopción exitosa, deben cumplirse condiciones que aseguren **Sí** a todas las preguntas. Son de carácter higiénico y contempla aspectos que se espera estén resueltos mediante recursos internos o externos.

**Pregunta 1: ¿Cuenta con al menos 2 profesionales (internos o externos) con experiencia en control y gestión de Cloud (Administradores de Sistemas, Devops y/o SREs)?**
- SÍ → ir a pregunta 2
- NO → diseñar mecanismo para contar con al menos 2 profesionales idóneos, luego ir a pregunta 2

**Pregunta 2: ¿Tiene sistemas productivos legacy críticos que no puede migrar aún a tecnologías más modernas?**
- SÍ (con urgencia de migrar por obsolescencia o condiciones de seguridad) → evaluar migración "lift and shift" como medida **temporal y parcial** hasta lograr la actualización, luego ir a pregunta 3
- NO → ir a pregunta 3

**Pregunta 3: ¿Los sistemas que administra deben escalar de manera repentina y/o no predecible?**
- SÍ → ir a pregunta 4
- NO → evaluar Cloud Pública solo para capacidades actuales más crecimiento vegetativo, o bien opciones housing/hosting con crecimiento moderado y predecible; luego ir a pregunta 4

**Pregunta 4: ¿Tiene documentadas sus aplicaciones, infraestructura y sistemas con los siguientes instrumentos?**
1. Diagrama de infraestructura
2. CMDB (base de datos de configuración)
3. Diagramas de despliegue o equivalentes
4. Demanda de transacciones por unidad de tiempo (segundo, minuto)
5. RTO y RPO para sistemas críticos
6. Mapa de procesos y su vinculación con sistemas

- SÍ (los 6 instrumentos) → ir a pregunta 5
- NO (alguno de los puntos) → establecer un Proyecto de Migración con estrategia y plan de actividades que resuelva las preguntas previas (antes del inicio de la adopción de Cloud) y genere esos instrumentos; luego ir a pregunta 5

**Pregunta 5: ¿Tiene conocido y planificado (ej. Gantt) las actividades y el tiempo para migrar sus sistemas al Cloud?**
- SÍ → ir a pregunta 6
- NO → establecer planificación con recursos y tiempos adecuados, incluyendo gestión del cambio; apoyarse en proveedores especializados; resolver primero los puntos de la pregunta 4; luego ir a pregunta 6

**Pregunta 6: ¿Posee área de ciberseguridad y un CISO (con recursos propios o externalizados)?**
- SÍ → continuar con el Capítulo 2
- NO → identificar cómo resolver estas funciones durante el proceso de adopción y en la operación con Cloud Público. El rol de CISO institucional **debe ser interno**, aunque las labores técnicas/operativas de apoyo pueden ser resueltas externamente. Luego continuar con el Capítulo 2

---

## Capítulo 2: ¿Qué comprar?

### Regla principal de selección

| Situación | Recomendación |
|-----------|--------------|
| Capacidades de gestión técnica limitadas + software para necesidad específica que solo requiere configuración (ERP, CRM, KMS, CMS, etc.) | **Preferir SaaS** (Software as a Service). No comprar Cloud Pública para instalar aplicaciones desde cero (requiere capacidades similares a On Premises) |
| Gestión de aplicaciones propias o de terceros que requieren escalar, con recursos profesionales disponibles para gestionar, modificar, desarrollar y administrar | **IaaS** (infraestructura) y/o **PaaS** (plataforma) en Cloud Público |

Modelo de compra habitual: el proveedor ofrece "créditos" equivalentes a una suma de dinero para adquirir servicios Cloud. Puede incluir servicios de soporte del proveedor.

### Servicios adquiribles en Cloud (modalidades IaaS, PaaS, BaaS, CaaS, SaaS)

- Capacidad de cómputo (máquinas y servidores virtuales)
- Gestores y plataformas para contenedores
- Network (redes virtuales)
- Bases de datos y big data
- Almacenamiento (espacio en disco)
- Herramientas de seguridad (firewalls virtuales, sistemas de detección de amenazas)
- Entornos de desarrollo
- Sistemas de gestión de identidad y acceso
- Repositorios de almacenamiento
- Sistema de archivos distribuidos
- Servicio de Kubernetes elástico
- Balanceo de tráfico
- Base de datos relacional como servicio
- Servicio de DNS
- Red de distribución de contenidos estáticos (CDN)
- Servicio de correos
- Monitoreo de infraestructura
- Servicio de WAF
- Base de datos no relacional (ej. Mongo Atlas)
- Servicio de encolamiento
- Servicios de ETL
- Servicio de data streams
- Servicio de Datawarehouse
- Servicio de detección de amenazas
- Servicio automático de evaluación de seguridad (Inspector)
- Inteligencia artificial como servicio
- Plataforma de desarrollo de aplicaciones móviles (MBaaS)
- Servicio de gestión de API
- Servicio de identidad y acceso como servicio

---

## Capítulo 3: Consideraciones para la elección del proveedor

### Tipos de proveedores Cloud

| Tipo | Descripción |
|------|-------------|
| **Hyperscalers** | Proveedores globales; escala más amplia; asociados a corporaciones tecnológicas globales |
| **Regionales** | Cubren un continente; asociados a empresas de servicios tecnológicos y telecomunicaciones |
| **Locales** | Empresas nacionales; servicios más específicos o de alcance local |

No existe *a priori* un tipo de proveedor mejor. La selección depende de la especificidad de los servicios, el nivel de SLA requerido, la capacidad de administración de la institución y los recursos financieros disponibles.

### 5 características clave para evaluar proveedores

**1. Fiabilidad y disponibilidad**
- **Uptime:** nivel de disponibilidad adecuado a los niveles de servicio requeridos (especificado en el SLA)
- **Centros de datos redundantes:** garantizan continuidad del servicio ante fallas en un centro de datos; se aprovecha implementando procedimientos de continuidad operacional

**2. Seguridad**
- **Cumplimiento normativo:** adhesión a estándares y regulaciones de seguridad
- **Gestión de identidad y acceso:** mecanismos robustos + procedimientos claros de coordinación con la institución
- **Determinación de responsabilidades:** modelo claro de responsabilidades compartidas entre proveedor e institución

**3. Escalabilidad y flexibilidad**
- **Escalabilidad automática:** escalamiento fácil de recursos (arriba o abajo) según necesidades; capacidad de escalabilidad automática para cargas variables
- **Variedad de servicios:** amplia gama desde almacenamiento básico hasta inteligencia artificial

**4. Rendimiento**
- **CDN (Red de Entrega de Contenidos):** si se requiere, verificar si el proveedor ofrece CDN para acelerar carga de datos y aplicaciones
- **Localización de centros de datos:** la proximidad geográfica influye en latencia; centros de datos cercanos a los usuarios ofrecen menores tiempos de respuesta

**5. Soporte y servicio al cliente**
- **Niveles de soporte:** evaluar los distintos niveles ofrecidos ante situaciones adversas o incidencias de operación
- **Recursos de ayuda y documentación:** disponibilidad de documentación detallada y comunidad activa

### El rol de los Partners o Socios de Negocios

En muchos casos (especialmente Hyperscalers y empresas regionales en Chile), la provisión de servicios Cloud se realiza de forma **indirecta** a través de un reseller, partner, socio comercial o distribuidor. Este modelo tiene implicaciones:

- El "consumo" visible en la consola de uso puede diferir del monto final a pagar (márgenes de comercialización, impuestos, conversión de monedas)
- El soporte técnico de primer nivel generalmente lo provee el partner; se escala al proveedor global si es necesario
- Los requerimientos de compra deben incluir:
  1. Expectativas técnicas y comerciales del modelo de operación
  2. Modelo comercial (tasas adicionales, modalidad de precios, cobros, impuestos, instrumento de compra)
  3. Modelo de servicios, con responsabilidades explícitas de:
     - La institución
     - El socio comercial
     - El proveedor de Nube Pública
     - El modelo de control de la consola y distribución de responsabilidades en su administración

En virtud del artículo 35 bis de la Ley N°19.886 (contratacióncomplejas), se deben utilizar mecanismos de análisis técnico, financiero, de ciclo de vida útil, consulta al mercado y otros procedimientos existentes.

---

## Capítulo 4: Consideraciones de servicio

### Acuerdos de Nivel de Servicio (SLAs)

El SLA en contexto Cloud forma parte de la relación contractual entre proveedor y cliente; establece términos y condiciones sobre calidad, disponibilidad y rendimiento de los servicios. Define métricas específicas, proporciona base objetiva para resolución de problemas y compensaciones por incumplimientos.

**Ejemplo de valores SLA:**
- Servicio crítico en horario hábil: 99.5% de disponibilidad + 30 minutos de tiempo de respuesta de soporte
- Mismo servicio fuera de horario hábil: 97% de disponibilidad + 4 horas de tiempo de respuesta

### Elementos del SLA

| Elemento | Descripción |
|---------|-------------|
| Disponibilidad/Uptime | Porcentaje de tiempo de servicio disponible; expresado en "nueves" (ej. 99.9%); más nueves = mayor confiabilidad |
| Rendimiento | Capacidad comprometida de almacenamiento, procesamiento, transacciones por segundo, operaciones I/O, rendimiento de red |
| Tiempo de respuesta | Período máximo para responder a solicitud o incidencia |
| Mantenimiento programado | Períodos en que el servicio puede estar fuera de línea por mantenimiento planificado |
| Compensación por incumplimiento | Medidas correctivas o compensaciones ante incumplimiento del SLA (créditos de servicio, extensiones de contrato) |
| Seguridad y cumplimiento normativo | Medidas de seguridad del proveedor + estándares y regulaciones que debe cumplir |
| Escalación y resolución de problemas | Procedimientos de reporte, plazos de resolución y responsabilidades de ambas partes |
| Backup y recuperación de datos | Políticas de copia de seguridad, frecuencia de respaldo y procedimientos de recuperación |

### Establecimiento e implementación del SLA

1. **Definir objetivos y requisitos claros** — servicios críticos, necesidades de rendimiento, requisitos de seguridad y cumplimiento
2. **Establecer expectativas claras** — cada métrica y condición bien definida y comprensible para ambas partes
3. **Personalizar el SLA** — adaptarlo a las necesidades específicas de la organización
4. **Negociación proactiva** — proporcionar métricas y datos específicos sobre uso proyectado y expectativas de rendimiento
5. **Definir multas y compensaciones claras** — proporcionales al impacto del incumplimiento en las operaciones
6. **Incluir cláusulas de revisión periódica** — para ajustar el SLA según cambios tecnológicos y de necesidades
7. **Considerar la escalabilidad** — asegurar que el SLA sea flexible para cambios en volumen de uso, expansión geográfica u otras expansiones
8. **Fomentar relación de colaboración** — reuniones periódicas de revisión del servicio, cumplimiento de SLAs y adaptaciones necesarias

### Seguimiento y cumplimiento del SLA

- **Equipo de gestión:** representantes de las áreas técnica, legal y de gestión
- **Métricas de monitoreo:** identificar KPIs para evaluar el rendimiento del proveedor
- **Herramientas de monitoreo:** seguimiento en tiempo real del rendimiento y disponibilidad; alertas sobre posibles problemas
- **Revisiones periódicas:** análisis detallado de métricas de rendimiento, discusión de problemas pasados y planificación de mejoras
- **Informes automáticos de cumplimiento:** claros, detallados y accesibles para todas las partes
- **Auditorías periódicas:** internas o externas para evaluar cumplimiento del SLA en profundidad
- **Gestión proactiva de problemas:** identificar desviaciones recurrentes de las condiciones de servicio
- **Sistema de seguimiento de incidentes:** registra y clasifica interrupciones para análisis posterior e identificación de patrones
- **Actualización periódica del SLA:** ajustar según necesidades cambiantes
- **Comunicación abierta:** canales efectivos con el proveedor para resolución rápida de problemas

---

## Notas

1. **Precompra:** proceso de preparación de la contratación administrativa
2. **SLA:** Acuerdos de niveles de servicios
3. **EvalTI:** proceso para Instituciones Públicas destinado a promover el buen uso de los recursos TIC, fomentar proyectos de valor para la gestión interna y las personas, e impulsar tecnologías emergentes, eficiencia en el gasto y transparencia
4. **Cloud Computing (referencia):** NIST (2011); Nigro, H. (2022). "Cloud Computing: Retos y Oportunidades". *Ingeniería, Matemáticas y Ciencias de la Información*, 9(18):11-16
5. **Cloud First (referencia):** Instructivo Presidencial N°1 de 2018
6. **Art. 35 bis, Ley N°19.886:** en adquisiciones y contrataciones complejas y sobre los montos que determine el reglamento, los organismos del Estado deben previamente obtener y analizar información técnica, de precios, costos y ciclo de vida útil. Las consultas a terceros se realizan mediante consulta pública a través del Sistema de Información de Compras o, excepcionalmente, mediante cotizaciones directas (con registro en el Sistema). Las reuniones presenciales o virtuales con proveedores son posibles solo cuando sean imprescindibles, dejando registro y cumpliendo la Ley N°20.730 (lobby)
