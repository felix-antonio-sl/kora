---
_manifest:
  urn: urn:gn:kb:estrategia-td-ia-p11
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
    shard_index: 11
    shard_count: 12
    shard_root_urn: urn:gn:kb:estrategia-td-ia
---

# Estrategia y Plan de Transformación Digital e IA "Ñuble Aumentado" (2025–2028) - Parte 11

## D 4 1 marco metodologico para el ciclo de vida de asistentes de ia
- **Titulo:** **D.4.1. Marco Metodológico para el Ciclo de Vida de Asistentes de IA**
- **Contenido:** 
ID: `PTN-D41-ALM-FRAMEWORK-01`

- Cpt: Requisito Mandatorio: Arquitectura con Capas de Guardrails por Diseño.
 - Req: Toda solución de IA deberá ser implementada con componentes de software explícitos para la gestión de riesgos en tiempo de ejecución.
 - Cpt: 1. Guardrails de Entrada: Validación y Reescritura de Prompts.
 - Cpt: 2. Guardrails de Salida: Validación de Formato; Comprobación de Fidelidad; Sanitización de Seguridad y PII.
 - Cpt: 3. Guardrails Operacionales: Gestión de Excepciones y Rutas de Escalado; Límites de Recursos.

## D 4 6 ciclo de vida industrial del producto de ia
- **Titulo:** **D.4.6. Ciclo de Vida Industrial del Producto de IA**
- **Contenido:** 
ID: `PTN-D46-AI-PRODUCT-LIFECYCLE-01`

- Cpt: 1. Fase de Pruebas y Validación Avanzada.
 - Req: Metodología de Evaluación Híbrida (Offline y Online).
 - Req: Evaluadores Híbridos (heurísticos, humanos, "LLM-as-a-Judge").
 - Req: Métricas de Calidad Clave (precisión, fidelidad, ausencia de sesgos, latencia).
- Cpt: 2. Fase de Mantenimiento y Evolución (Post-producción).
 - Req: Monitoreo Continuo de Deriva (Drift).
 - Req: Implementación del "Data Flywheel" para captura de feedback y mejora continua.

## E servicios ciudadanos
- **Titulo:** E. Servicios Ciudadanos
- **Contenido:** 
ID: `PTN-E-CITIZEN-SERVICES-01`

## E 1 prd nuble app y nuble seguro guia de estilo y lenguaje claro
- **Titulo:** E.1. PRD Ñuble App y Ñuble Seguro; Guía de Estilo y Lenguaje Claro
- **Contenido:** 
ID: `PTN-E1-APP-PRD-01`

## S 1 documento de requisitos de producto prd nuble app
- **Titulo:** **1. Documento de Requisitos de Producto (PRD): Ñuble App**
- **Contenido:** 
ID: `PTN-E1-APP-PRD-DETAILS-01`

- Cpt: 1.1. Visión General y Propósito del Producto.
 - Def: La Ñuble App será el punto de acceso digital único y oficial del GORE.
- Cpt: 1.2. Objetivos y Métricas de Éxito (KPIs).

 | Objetivo Estratégico | Métrica Clave | Línea Base (Año 1) | Meta (Año 3) |
 | :--- | :--- | :--- | :--- |
 | Mejorar el acceso a servicios | Tasa de Adopción | 5% | >= 30% |
 | Aumentar la eficiencia del GORE | % de reducción de consultas | 0% | >= 40% |
 | Incrementar la satisfacción ciudadana | Calificación promedio (CSAT) | N/A | >= 4.0 / 5.0 |
 | Fortalecer la seguridad regional | Tiempo mediano de derivación | N/A | < 5 minutos |

- Cpt: 1.3. Perfiles de Usuario (User Personas).
 - Cpt: María, Dirigenta Vecinal.
 - Cpt: Carlos, Pequeño Agricultor.
 - Cpt: Javiera, Estudiante Universitaria.
- Cpt: 1.4. Requisitos Funcionales (Features).
 - Cpt: Módulo 1: Mi GORE (Panel Ciudadano).
 - Cpt: Módulo 2: Trámites y Fondos.
 - Cpt: Módulo 3: Observatorio de Inversión.
 - Cpt: Módulo 4: Ñuble Seguro.
 - Cpt: Módulo 5: Participación Ciudadana.
- Cpt: 1.5. Requisitos No Funcionales.
 - Cpt: Rendimiento: Carga < 3s en 4G, funcional con conectividad intermitente.
 - Cpt: Seguridad: Comunicación cifrada, datos de "Ñuble Seguro" con máximo nivel de seguridad.
 - Cpt: Accesibilidad: Cumplir con nivel AA de WCAG 2.1.
 - Cpt: Escalabilidad: Arquitectura backend modular y basada en microservicios.
 - Cpt: Privacidad: Construida bajo el principio de privacidad por diseño.

## S 2 guia de estilo y lenguaje claro para servicios digitales ciudadanos
- **Titulo:** **2. Guía de Estilo y Lenguaje Claro para Servicios Digitales Ciudadanos**
- **Contenido:** 
ID: `PTN-E1-STYLE-GUIDE-01`

- Cpt: 2.1. Misión Comunicacional: Comunicarse de manera clara, útil, empática y respetuosa.
- Cpt: 2.2. Tono de Voz: Servicial, Respetuoso, Eficiente, Cercano pero Institucional.
- Cpt: 2.3. Principios de Redacción.
 - Cpt: Principio 1: Lenguaje Claro es Ley.
 - Cpt: Principio 2: Escribir para el Usuario, no para la Institución.
 - Cpt: Principio 3: Consistencia es Confianza.
- Cpt: 2.4. Microcopy y UX Writing: Ejemplos Prácticos.

## F gestion del plan y sostenibilidad
- **Titulo:** F. Gestión del Plan y Sostenibilidad
- **Contenido:** 
ID: `PTN-F-PLAN-MANAGEMENT-01`

- Cpt: F.1. Medición y Transparencia: KPIs por Trazo/Pulso; Especificaciones del Tablero Ñuble 250.
- Cpt: F.2. Finanzas y Adquisiciones: Modelo Financiero Trianual; Formatos EVALTIC.
- Cpt: F.3. Implementación: Mapa Estratégico de Implementación (Gantt Simplificado).

## G documentos fundacionales
- **Titulo:** G. Documentos Fundacionales
- **Contenido:** 
ID: `PTN-G-FOUNDATIONAL-DOCS-01`

## G 1 propuesta de resolucion exenta para la creacion de la oficina digital e ia o
- **Titulo:** G.1. Propuesta de Resolución Exenta para la Creación de la Oficina Digital e IA (ODIA)
- **Contenido:** 
ID: `PTN-G1-ODIA-RESOLUTION-01`

- Cpt: 1. Propuesta de Resolución Exenta que Crea la Oficina Digital e IA (ODIA).
 - Fnd: VISTOS y CONSIDERANDO.
 - Act: RESUELVO: CRÉASE la ODIA; ESTABLÉCESE su misión; FIJANSE sus funciones; INSTRÚYESE colaboración.

## G 2 lineamientos estrategicos para la sucesion de gesdoc
- **Titulo:** G.2. Lineamientos Estratégicos para la Sucesión de Gesdoc
- **Contenido:** 
ID: `PTN-G2-GESDOC-SUCCESSION-01`

- Cpt: 1. Diagnóstico Estratégico y Principio de Sucesión Colaborativa.
 - Def: La estrategia es de integración y sucesión planificada, no de reemplazo confrontacional.
- Cpt: 2. Hoja de Ruta de Integración (Corto Plazo: 3-6 meses).
 - Act: Desarrollo de un Conector de Datos (API) para extraer datos de Gesdoc.
 - Act: Ingesta al Repositorio Central (RUC).
- Cpt: 3. Hoja de Ruta de Sucesión (Mediano Plazo: 12-18 meses).
 - Act: Mapeo y Reingeniería de Procesos.
 - Act: Migración de Funcionalidades.
 - Act: Migración de Datos Históricos.
 - Act: Decomisionamiento Controlado.
- Cpt: 4. Propuesta de Valor y Beneficios del Enfoque.
