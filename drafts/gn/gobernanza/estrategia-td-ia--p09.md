---
_manifest:
  urn: urn:gn:kb:estrategia-td-ia-p09
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
    shard_index: 9
    shard_count: 12
    shard_root_urn: urn:gn:kb:estrategia-td-ia
---

# Estrategia y Plan de Transformación Digital e IA "Ñuble Aumentado" (2025–2028) - Parte 09

## A gobernanza y cumplimiento
- **Titulo:** A. Gobernanza y Cumplimiento
- **Contenido:** 
ID: `PTN-A-GOVERNANCE-01`

## A 1 marco normativo operativo tde plantilla raci matriz de gates
- **Titulo:** A.1. Marco Normativo Operativo TDE; Plantilla RACI; Matriz de Gates
- **Contenido:** 
ID: `PTN-A1-FRAMEWORK-01`
Purp: Constituir el manual de operaciones para la gobernanza diaria.

## S 1 marco normativo operativo de la transformacion digital del estado tde
- **Titulo:** **1. Marco Normativo Operativo de la Transformación Digital del Estado (TDE)**
- **Contenido:** 
ID: `PTN-A1-TDE-FRAMEWORK-01`

- Cpt: Checklist de Cumplimiento Ley 21.180 (Cero Papel).
 - Cpt: Expediente Electrónico: ¿Todo nuevo procedimiento se inicia y gestiona en una plataforma digital?
 - Cpt: Firma Electrónica Avanzada (FEA): ¿Todos los actos administrativos terminales son firmados con FEA?
 - Cpt: Comunicaciones Oficiales: ¿El intercambio de oficios se realiza a través de `DocDigital`?
 - Cpt: Notificaciones: ¿Las notificaciones se realizan a través de `Notificador` al Domicilio Digital Único (DDU)?
 - Cpt: Política de Gestión Documental: ¿La división aplica la Política de Gestión Documental del GORE?
- Cpt: Guía Rápida de Normas Técnicas para Jefes de División.
 - Cpt: Seguridad (DS N°7): Su división debe colaborar con el CISO para clasificar activos de información.
 - Cpt: Autenticación (DS N°9): Todo sistema debe integrarse con **ClaveÚnica**.
 - Cpt: Interoperabilidad (DS N°12): Antes de solicitar datos, debe verificar si están disponibles en la Red de Interoperabilidad.
 - Cpt: Calidad (DS N°11): Su división debe colaborar con la ODIA para registrar plataformas en el Catálogo.

## S 2 plantilla de matriz de responsabilidades raci
- **Titulo:** **2. Plantilla de Matriz de Responsabilidades (RACI)**
- **Contenido:** 
ID: `PTN-A1-RACI-TEMPLATE-01`

| Tarea / Entregable Clave | Gobernador / CORE | Administrador/a Regional | Oficina ODIA (Líder TD) | Jefatura de División (Dueño Proceso) | Asesoría Jurídica | CISO / DPO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Aprobación Estratégica del Proyecto** | **A** | **I** | **R** | **C** | **C** | **I** |
| **Definición de Requisitos del Negocio** | **I** | **C** | **C** | **A** / **R** | **I** | **I** |
| **Validación Técnica y de Seguridad** | **I** | **A** | **R** | **C** | **C** | **C** |
| **Gestión de la Ejecución y Avance** | **I** | **I** | **A** / **R** | **C** | **I** | **I** |
| **Adopción y Gestión del Cambio** | **I** | **C** | **R** | **A** | **I** | **I** |
| **Reporte de KPIs y Favorabilidad** | **A** | **I** | **R** | **I** | **I** | **I** |

## S 3 matriz de gates de cumplimiento
- **Titulo:** **3. Matriz de "Gates" de Cumplimiento**
- **Contenido:** 
ID: `PTN-A1-GATES-MATRIX-01`

| Gate de Cumplimiento | Fase del Proyecto | Criterio de Aprobación | Medio de Verificación |
| :--- | :--- | :--- | :--- |
| **G1: Pertinencia Estratégica** | Inicio | Alineamiento con Plan Maestro y ERD Ñuble 250. Superación de validación de viabilidad tripartita. | Acta de Constitución del Proyecto con RACI e Informe de Viabilidad Tripartito. |
| **G2: Cumplimiento Normativo TDE** | Diseño | Adherencia a Normas Técnicas de Ley 21.180. | Checklist de Cumplimiento TDE visado por ODIA. |
| **G3: IA Responsable y Privacidad** | Diseño | Publicación de Ficha SDA. EIPD aprobada por Subcomité de IA y DPO. | Ficha SDA publicada. Acta de aprobación del Subcomité. |
| **G4: Ciberseguridad** | Diseño | Diseño aprobado por el CISO. | Informe de evaluación de seguridad visado por CISO. |
| **G5: Adquisiciones y Financiero** | Planificación | Proceso EVALTIC aprobado (si aplica). Cumplimiento Ley de Compras. Sostenibilidad financiera. | Oficio resultado EVALTIC. Orden de Compra tramitada. |
| **G6: Puesta en Producción** | Ejecución | Plan de paso a producción aprobado. | Acta de aprobación del CTD para despliegue. |

## A 2 vademecum juridico administrativo del gore nuble para la td ia
- **Titulo:** A.2. Vademécum Jurídico-Administrativo del GORE Ñuble para la TD-IA
- **Contenido:** 
ID: `PTN-A2-LEGAL-VADEMECUM-01`
Purp: Consolidar el fundamento legal de las iniciativas del Plan Maestro.

## S 1 mapeo de iniciativas a la ley n 19 175 loc gore
- **Titulo:** **1. Mapeo de Iniciativas a la Ley N° 19.175 (LOC GORE)**
- **Contenido:** 
ID: `PTN-A2-LAW-MAPPING-01`

| Iniciativa del Plan Maestro | Competencia Legal Habilitante (Ley N° 19.175 y mods.) |
| :--- | :--- |
| **Oficina ODIA, CTD, Gobernanza** | **Art. 16 a):** "Diseñar, elaborar, aprobar y aplicar las políticas, planes, programas y proyectos de desarrollo de la región". |
| **IDE Ñuble, Observatorio Ñuble 250** | **Art. 17 c):** "Orientar el desarrollo territorial". **Art. 16 c):** "Fomentar y velar por la buena administración de los recursos". |
| **Asistentes de Automatización Inteligente** | **Art. 24 k):** "Administrar los bienes y recursos propios del GORE". |
| **Ñuble App, Asistentes Ciudadanos** | **Art. 19 b):** "Participar en acciones tendientes a facilitar el acceso de la población a la salud, educación y cultura". **Art. 16 j):** "Asesorar a las municipalidades". |
| **CIES ↔ SITIA, Módulo Ñuble Seguro** | **Art. 16 i):** "Diseñar y ejecutar políticas, planes y programas regionales de prevención del delito y de asistencia a víctimas". **Art. 16 k):** "Adoptar las medidas necesarias para enfrentar situaciones de emergencia o catástrofe". |

## S 2 navegacion del ciclo presupuestario para proyectos td ia
- **Titulo:** **2. Navegación del Ciclo Presupuestario para Proyectos TD-IA**
- **Contenido:** 
ID: `PTN-A2-BUDGET-CYCLE-01`
Fnd: Basado en ``.

- Cpt: Formulación: Las iniciativas se incluirán en el Anteproyecto Regional de Inversiones (ARI) y en el Programa Público de Inversión Regional (PROPIR).
- Cpt: Aprobación: El "Programa Habilitante de Gobernanza TD-IA" será presentado al CORE para aprobación.
- Cpt: Ejecución y Control: La ejecución será monitoreada a través de SIGFE (financiero) y BIP (físico).

## S 3 encuadre en el sistema nacional de inversiones sni y ley de compras publicas
- **Titulo:** **3. Encuadre en el Sistema Nacional de Inversiones (SNI) y Ley de Compras Públicas**
- **Contenido:** 
ID: `PTN-A2-SNI-CHILECOMPRA-01`

- Cpt: Iniciativas de Inversión (SNI): Proyectos de gasto de capital serán formulados como IDI y presentados al MDSF para obtener RS.
- Fnd: La formulación se rige por la `kb_gn_024_guia_idi_sni_sts`.
- Cpt: Programas (Glosa 06): Iniciativas de gasto corriente serán formuladas como PPR y presentadas a DIPRES/SES para obtener RF.
- Fnd: La formulación se rige por la `kb_gn_025_guia_programas_sts`.
- Cpt: Adquisiciones (Ley N° 19.886): Toda adquisición se realizará a través de ChileCompra.

## B datos y privacidad
- **Titulo:** B. Datos y Privacidad
- **Contenido:** 
ID: `PTN-B-DATA-PRIVACY-01`
Purp: Establecer el marco de gobernanza para los datos.
