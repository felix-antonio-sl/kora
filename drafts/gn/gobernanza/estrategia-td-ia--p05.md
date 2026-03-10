---
_manifest:
  urn: urn:gn:kb:estrategia-td-ia-p05
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/04_habilitadores/tde/kb_gn_720_estrategia_td_ia_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- estrategia
- transformacion-digital
- ia
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/tde/kb_gn_720_estrategia_td_ia_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/tde/kb_gn_720_estrategia_td_ia_koda.yml: 5328885f1b3ae852439424dd840565fd06c753ed1f56cc32252f923d0bff8a50
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.88
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 1
    meat_count: 416
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__estrategia-td-ia.md.json
  kora:
    shard_index: 5
    shard_count: 12
    shard_root_urn: urn:gn:kb:estrategia-td-ia
---

# Estrategia y Plan de Transformación Digital e IA "Ñuble Aumentado" (2025–2028) - Parte 05

## S 6 arquitectura de capacidades materializando la vision
- **Titulo:** 6. Arquitectura de Capacidades: Materializando la Visión
- **Contenido:** 
ID: `PTN-2-CAPABILITIES-ARCHITECTURE-01`
Fnd: La estrategia se organiza en cinco pilares de acción desplegados sobre una arquitectura de capacidades institucionales coherente.
Cpt: El "stack" de capacidades se organiza en capas jerárquicas.

- Cpt: Capa 1: Gobernanza y Estrategia (El Timón).
 - Def: La capa de decisión y reglas, no de tecnología.
- Cpt: Capa 2: Plataformas Centrales (Los Motores).
 - Def: La infraestructura tecnológica y de datos compartida, reutilizable y escalable.
- Cpt: Capa 3: Servicios Cognitivos y de Negocio (La Caja de Herramientas).
 - Def: La lógica de negocio y la IA, encapsuladas como servicios "headless".
- Cpt: Capa 4: Experiencia y Canales (Las Vitrinas).
 - Def: La capa de interacción con el usuario.
Req: Cada pilar estratégico contribuye al desarrollo de una o más de estas capas.

## S 6 1 pilar 1 gobernanza y modernizacion responde al trazo 5 de nuble 250
- **Titulo:** 6.1. Pilar 1: Gobernanza y Modernización (Responde al Trazo 5 de Ñuble 250)
- **Contenido:** 
ID: `PTN-2-PILLAR1-GOVERNANCE-01`
Purp: Construye las Capas 1, 2 y 3. Establece las "reglas del juego" y desarrolla las capacidades núcleo.

## S 6 1 1 sub pilar industrializacion de la capacidad de ia mediante la gobernanza
- **Titulo:** 6.1.1. Sub-Pilar: Industrialización de la Capacidad de IA mediante la Gobernanza del Conocimiento y la Ingeniería de Agentes
- **Contenido:** 
ID: `PTN-2-PILLAR1-AI-INDUSTRIALIZATION-01`

- Cpt: 6.1.1.1. Adopción del Marco de Ingeniería Unificado.
 - Act: Se decreta la adopción formal del conjunto de normativas de la "Usina de IA" (Anexo D.4) como el estándar único y obligatorio para todo el ciclo de vida de asistentes y artefactos de conocimiento.
 - Def: Este marco constituye el modelo semántico del GORE, representando el significado de los conceptos, sus relaciones y reglas de negocio para asegurar que la IA opere sobre una base de conocimiento coherente.
 - Res: Transforma la capacidad artesanal en una línea de producción industrial.
- Cpt: 6.1.1.2. Establecimiento del Repositorio Único de Conocimiento (RUC).
 - Act: Se mandata la implementación de la arquitectura de directorios definida en la `Guía para la Gestión del Repositorio Central de Conocimiento` como la fuente única de verdad, gobernada por control de versiones (Git).
- Cpt: 6.1.1.3. Institucionalización del Ciclo de Vida del Conocimiento.
 - Act: Se formaliza el proceso de 6 fases (Sourcing, Staging, Audit, Publishing, Registration, Maintenance) descrito en la `Guía para la Gestión del Repositorio Central de Conocimiento`.
 - Obj: Garantizar la calidad, trazabilidad y vigencia de cada activo de conocimiento que alimenta a los asistentes.

## S 6 1 2 sub pilar automatizacion inteligente de procesos y orquestacion de la ge
- **Titulo:** 6.1.2. Sub-Pilar: Automatización Inteligente de Procesos y Orquestación de la Gestión Pública
- **Contenido:** 
ID: `PTN-2-PILLAR1-AUTOMATION-01`
Purp: Re-arquitecturar los flujos de trabajo clave del GORE.

- Cpt: El Motor BPMN como Orquestador Central.
 - Act: Se implementará un motor de Procesos de Negocio (BPMN) que actuará como el "sistema nervioso central" de `NEXO GORE`.
- Cpt: `Servicio de Asistencia Jurídica y de Conformidad` como Copiloto Jurídico y de Conformidad.
 - Mech: Será invocado por cualquier flujo para coproducir borradores y pre-auditarlos en tiempo real.
- Cpt: `Servicio de Asistencia Financiera y Presupuestaria` como Copiloto Financiero.
 - Mech: Asistirá al Módulo de Gestión Financiera. Al detectar necesidad de modificación presupuestaria, generará el borrador del acto administrativo.
- Cpt: `Servicio de Asistencia Financiera y Presupuestaria` como Pre-Auditor de Rendiciones.
 - Mech: La inteligencia de "RINDE FÁCIL ÑUBLE" se materializará en un servicio que realizará una pre-revisión automática de las rendiciones.
Cpt: Integración de servicios cognitivos en ciclos de gestión.
- Cpt: Ciclo de Vida de IPR: Generación y tramitación de Convenios, Pre-evaluación de Admisibilidad.
- Cpt: Ciclo Presupuestario: Tramitación de Modificaciones Presupuestarias y automatización de reportes.
- Cpt: Ciclo de Aprobaciones: Orquestación del flujo de Resoluciones y Decretos, con pre-auditoría.
- Cpt: Ciclo de Compras Públicas: Se implementará un asistente que guiará en la correcta aplicación de la Ley N° 19.886.

## S 6 1 3 sub pilar fundamentos de ingenieria de datos
- **Titulo:** 6.1.3. Sub-Pilar: Fundamentos de Ingeniería de Datos
- **Contenido:** 
ID: `PTN-2-PILLAR1-DATA-ENGINEERING-01`
Purp: Establecer la disciplina técnica para la captura, movimiento, almacenamiento, procesamiento y entrega de datos.

- Cpt: Principio de Fiabilidad y Escalabilidad.
 - Req: Toda infraestructura de datos se diseñará para ser robusta, segura y escalable.
- Cpt: Principio de Contratos de Datos.
 - Req: Se definirá formato, calidad y tiempos de entrega esperados para cada flujo de datos.
- Cpt: Principio de Observabilidad por Diseño.
 - Req: Se implementará un monitoreo continuo de la calidad de los datos (frescura, completitud, exactitud) en cada etapa del ciclo de vida.
 - Mech: La observabilidad se implementará mediante un framework de validación declarativa como Great Expectations.
 - Req: Las reglas de calidad serán parte del 'Contrato de Datos' y se ejecutarán automáticamente en los pipelines de ingesta y transformación.
- Cpt: Principio de Versionamiento Integral.
 - Req: Se aplicará control de versiones a datos, esquemas, transformaciones y definiciones de métricas.
Cpt: KPIs asociados.
- Cpt: KPI-3: Eficiencia del Ciclo IPR.
 - Def: Tiempo promedio desde el ingreso de una IPR hasta la total tramitación del acto que aprueba su financiamiento.
 - Mdl: Línea Base: > 6 meses, Meta 3 años: < 60 días.
- Cpt: KPI-4: Tasa de Observaciones CGR.
 - Def: Porcentaje de actos administrativos observados por Contraloría.
 - Mdl: Línea Base: X%, Meta 3 años: Reducción del 50%.

## S 6 2 pilar 2 competitividad y sostenibilidad responde a los trazos de crecimien
- **Titulo:** 6.2. Pilar 2: Competitividad y Sostenibilidad (Responde a los Trazos de Crecimiento y Territorio de Ñuble 250)
- **Contenido:** 
ID: `PTN-2-PILLAR2-COMPETITIVENESS-01`
Purp: Aplicar las capacidades de la Capa 2 y 3 para generar valor público en dominios económicos y medioambientales.

- Cpt: Sub-Pilar: Fomento Productivo Aumentado.
 - Act: Se implementarán herramientas digitales para potenciar sectores clave. Incluye pilotos de AgroTech y Turismo Inteligente financiados vía FRPD.
- Cpt: Sub-Pilar: Economía Circular Basada en Datos.
 - Act: Se creará una plataforma regional que conecte a productores con gestores de residuos, usando la IDE Ñuble para mapear flujos.

## S 6 3 pilar 3 capital humano aumentado gestion del cambio y desarrollo de compet
- **Titulo:** 6.3. Pilar 3: Capital Humano Aumentado: Gestión del Cambio y Desarrollo de Competencias (Responde a Trazos de Bienestar y Cultura de Ñuble 250)
- **Contenido:** 
ID: `PTN-2-PILLAR3-HUMAN-CAPITAL-01`
Nat: Pilar transversal enfocado en el componente humano de la Capa 1.

## S 6 3 1 estrategia de gestion del cambio y adopcion interna
- **Titulo:** 6.3.1. Estrategia de Gestión del Cambio y Adopción Interna
- **Contenido:** 
ID: `PTN-2-PILLAR3-CHANGE-MANAGEMENT-01`

- Cpt: 6.3.1.1. Plan de Comunicación Interna.
 - Def: Desarrollo de una estrategia por fases (Sensibilización, Comprensión, Adopción) con mensajes segmentados por audiencia.
- Cpt: 6.3.1.2. Red de Campeones del Cambio.
 - Def: Identificación y empoderamiento de líderes de cambio en cada división.
- Cpt: 6.3.1.3. Fomento de Comunidades de Práctica (CoP).
 - Obj: Fomentar activamente la ruta "Connect" para compartir conocimiento tácito.
 - Act: Se lanzarán 2-3 pilotos iniciales.

## S 6 3 2 programa de desarrollo de competencias digitales y de ia
- **Titulo:** 6.3.2. Programa de Desarrollo de Competencias Digitales y de IA
- **Contenido:** 
ID: `PTN-2-PILLAR3-SKILLS-DEVELOPMENT-01`

- Cpt: 6.3.2.1. Mapa de Competencias Críticas.
 - Act: Diagnóstico y definición de las nuevas habilidades requeridas por cada rol.
- Cpt: 6.3.2.2. Itinerarios Formativos por Perfil.
 - Act: Diseño de rutas de aprendizaje (Nivel Fundacional, Usuario Avanzado, Experto).
- Cpt: 6.3.2.3. Plataforma de Aprendizaje y Certificación Interna.
 - Act: Implementación de un sistema para la entrega, seguimiento y validación del aprendizaje.

## S 6 4 pilar 4 resiliencia y seguridad responde al trazo blanco y rojo de nuble 2
- **Titulo:** 6.4. Pilar 4: Resiliencia y Seguridad (Responde al Trazo Blanco y Rojo de Ñuble 250)
- **Contenido:** 
ID: `PTN-2-PILLAR4-RESILIENCE-01`
Purp: Fortalecer la Capa 2, consolidando la infraestructura crítica de seguridad y gestión de desastres.

- Cpt: Sub-Pilar: Consolidación del Ecosistema CIES-SITIA.
 - Act: Se formalizará la integración del Centro Integrado de Emergencia y Seguridad (CIES) con la plataforma nacional SITIA.
 - Mech: Federar la red de 209 cámaras regionales y adoptar los modelos de IA de SITIA para la detección de patentes y analítica de video.
 - Obj: Crear una red de teleprotección unificada y de vanguardia.
- Cpt: Sub-Pilar: Ciberseguridad y Continuidad Operativa.
 - Act: Se implementará un Plan Director de Ciberseguridad basado en la Norma Técnica de Seguridad (DS N°7).
 - Cpt: Componentes del Plan Director.
 - Act: Hardening de la infraestructura (servidores, redes, aplicaciones) para minimizar vulnerabilidades.
 - Act: Monitoreo continuo de la salud, rendimiento y seguridad de la plataforma.
 - Act: Plan de recuperación ante desastres (DRP) para garantizar la continuidad de los servicios críticos.
