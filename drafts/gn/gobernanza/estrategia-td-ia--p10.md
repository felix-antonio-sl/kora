---
_manifest:
  urn: urn:gn:kb:estrategia-td-ia-p10
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
    shard_index: 10
    shard_count: 12
    shard_root_urn: urn:gn:kb:estrategia-td-ia
---

# Estrategia y Plan de Transformación Digital e IA "Ñuble Aumentado" (2025–2028) - Parte 10

## B 1 programa de cumplimiento ley 21 719 politica de datos y catalogo guia de ano
- **Titulo:** B.1. Programa de Cumplimiento Ley 21.719; Política de Datos y Catálogo; Guía de Anonimización
- **Contenido:** 
ID: `PTN-B1-COMPLIANCE-PROGRAM-01`
Purp: Implementado por el CTD y supervisado por el DPO.

## S 1 programa de cumplimiento de la ley n 21 719 de proteccion de datos personale
- **Titulo:** **1. Programa de Cumplimiento de la Ley N° 21.719 de Protección de Datos Personales**
- **Contenido:** 
ID: `PTN-B1-LAW21719-COMPLIANCE-01`

- Act: Designación del Delegado de Protección de Datos (DPO).
- Act: Creación de un Registro de Actividades de Tratamiento.
- Act: Realización de Evaluaciones de Impacto en la Protección de Datos (EIPD) obligatorias para tratamientos de alto riesgo.
- Act: Implementación de un procedimiento para gestionar derechos ARCO-P.
- Act: Establecimiento de un Protocolo de Notificación de Brechas de Seguridad.

## S 2 politica de gobierno de datos del gore nuble y gestion de datos como product
- **Titulo:** **2. Política de Gobierno de Datos del GORE Ñuble y Gestión de Datos como Producto**
- **Contenido:** 
ID: `PTN-B1-DATA-GOVERNANCE-POLICY-01`

- Cpt: Principios Rectores del Tratamiento de Datos: licitud, lealtad, transparencia, finalidad, proporcionalidad, calidad, responsabilidad, seguridad, e información.
- Cpt: Roles y Responsabilidades: Asignación formal de roles de Dueño del Dato y Custodio del Dato.
- Cpt: Catálogo Maestro de Datos y Modelo Semántico: Creación de un catálogo que inventariará, describirá y clasificará todos los datasets.
- Cpt: Contratos de Datos (Data Contracts): Todo producto de datos clave deberá contar con un "contrato" formal (Esquema, Calidad, Seguridad, Linaje).
- Cpt: Ciclo de Vida del Producto de Datos: La creación y evolución seguirá un ciclo de vida gestionado.
- Ctx: El ciclo de vida se detalla en el Anexo D.5.

## S 3 guia de anonimizacion y seudonimizacion de datos
- **Titulo:** **3. Guía de Anonimización y Seudonimización de Datos**
- **Contenido:** 
ID: `PTN-B1-ANONYMIZATION-GUIDE-01`
Fnd: Basada en las definiciones de la Ley N° 21.719.

- Cpt: Anonimización: Se aplicarán técnicas para crear datasets donde sea razonablemente irreversible identificar a una persona.
- Cpt: Seudonimización: Para tratamientos internos, se utilizarán técnicas que permiten re-identificación controlada.
- Req: Aplicación obligatoria en la preparación de datasets para entrenamiento de IA.

## C ia responsable y sda
- **Titulo:** C. IA Responsable y SDA
- **Contenido:** 
ID: `PTN-C-RESPONSIBLE-AI-01`
Purp: Establecer el marco operativo para el ciclo de vida de la IA.

## C 1 guia de asistentes ficha sda marco de riesgos protocolo de incidentes
- **Titulo:** C.1. Guía de Asistentes (Ficha SDA); Marco de Riesgos; Protocolo de Incidentes
- **Contenido:** 
ID: `PTN-C1-AI-GUIDE-01`

## S 1 guia de asistentes y ficha de transparencia de sistemas de decision automati
- **Titulo:** **1. Guía de Asistentes y Ficha de Transparencia de Sistemas de Decisión Automatizada (SDA)**
- **Contenido:** 
ID: `PTN-C1-SDA-FICHA-01`

- Req: Obligatoriedad de documentar y publicar una Ficha SDA para cada sistema de IA.
- Cpt: Contenido de la Ficha SDA: Nombre, Objetivo, Responsable, Modelo Operativo, Funcionamiento, Datos Utilizados, Lógica de Decisión, Medidas de Mitigación, Canal de Consultas.
- Req: Todas las Fichas SDA aprobadas serán publicadas en el Portal de Transparencia de IA.

## S 2 marco de gobernanza de ia basado en riesgos
- **Titulo:** **2. Marco de Gobernanza de IA Basado en Riesgos**
- **Contenido:** 
ID: `PTN-C1-RISK-FRAMEWORK-01`
Fnd: Adopción de un enfoque basado en riesgo.

- Cpt: Riesgo Inaceptable: Prohibido.
- Cpt: Alto Riesgo: Requerirá supervisión humana estricta, auditorías externas y EIPD obligatoria.
- Cpt: Riesgo Limitado: Requerirán obligaciones de transparencia (Ficha SDA).
- Cpt: Riesgo Bajo o Mínimo: Requisitos de gobernanza mínimos.
- Cpt: Checklist de Evaluación Ética y de Riesgos Pre-despliegue.
 - Cpt: Riesgo de Sesgo y Discriminación.
 - Cpt: Riesgo de Privacidad (EIPD Simplificada).
 - Cpt: Riesgo de Seguridad.
 - Cpt: Riesgo de Calidad y Fiabilidad (Alucinaciones).
 - Cpt: Riesgo de Explicabilidad ("Caja Negra").
 - Cpt: Riesgo de Impacto Laboral (Workforce).
- Mech: El Subcomité de IA asignará un nivel de riesgo al sistema, lo que determinará los controles requeridos.

## S 3 protocolo de registro y gestion de incidentes de ia
- **Titulo:** **3. Protocolo de Registro y Gestión de Incidentes de IA**
- **Contenido:** 
ID: `PTN-C1-INCIDENT-PROTOCOL-01`

- Act: Habilitación de un Canal de Reporte Unificado.
- Act: Mantenimiento de un Registro Centralizado de Incidentes.
- Act: Proceso de Escalamiento y Resolución para incidentes de criticidad Alta o Crítica.

## D capacidades nucleo aip alm ide cies
- **Titulo:** D. Capacidades Núcleo (AIP, ALM, IDE, CIES)
- **Contenido:** 
ID: `PTN-D-CORE-CAPABILITIES-01`

- Cpt: D.1. AIP y ALM: Guía Maestra ALM; Plantilla "Ficha AIP"; Catálogo de Asistentes Existentes.
- Cpt: D.2. IDE Ñuble: Kit Geoespacial con Perfiles ISO/TC 211.
- Cpt: D.3. CIES y SITIA: Dossier de Operación CIES; Dossier de Integración SITIA.
- Cpt: D.4. Marco de Ingeniería de IA y Conocimiento ("Usina de IA").
 - Cpt: D.4.1. `Marco Metodológico para el Ciclo de Vida de Asistentes de IA`
 - Cpt: D.4.2. `Guía para la Gestión del Repositorio Central de Conocimiento`
 - Cpt: D.4.3. `Protocolo de Programación Declarativa de Asistentes de IA`
 - Cpt: D.4.4. `Norma para la Elaboración de Artefactos de Conocimiento Institucional`
 - Cpt: D.4.5. `Estándar para la Digitalización Estructurada de Formularios`
 - Cpt: D.4.6. `Ciclo de Vida Industrial del Producto de IA`
- Cpt: D.5. Ciclo de Vida del Producto de Datos
