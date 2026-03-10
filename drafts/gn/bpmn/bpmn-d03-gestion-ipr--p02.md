---
_manifest:
  urn: urn:gn:kb:bpmn-d03-gestion-ipr-p02
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- bpmn
- ipr
- gestion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml: ad228323fcd3053399a1bea70e24f3a0d3ffdc1da1a6f46050562a2bbc463a88
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.53
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 15
    meat_count: 152
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d03-gestion-ipr.md.json
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:gn:kb:bpmn-d03-gestion-ipr
---

# BPMN D03: Gestión de Intervenciones Públicas Regionales (IPR) - Parte 02

## P6 Modificaciones en Ejecucion
- **Subprocesos:** Solicitud, Evaluación, Tramitación
### Diagrama de Flujo
- **Mermaid:** flowchart TD
 A["Detectar necesidad; de modificación"] --> B["UT prepara; informe técnico"]
 B --> C["Oficio formal; al GORE"]
 C --> D["Supervisor GORE; analiza"]
 D --> E{"¿Altera; objetivo?"}
 E -->|"Sí"| F["❌ Rechazar"]
 E -->|"No"| G["Verificar; umbrales"]
 G --> H{"¿Requiere; CORE/SNI?"}
 H -->|"Sí"| I["Tramitar como; nueva aprobación"]
 H -->|"No"| J["Aprobar; internamente"]
 I & J --> K["Convenio; modificatorio"]

 style F fill:#f44336,color:#fff
 style K fill:#4CAF50,color:#fff

## P7 Cierre Tecnico Financiero y Evaluacion Ex Post
- **Subprocesos:** Cierre Técnico, Cierre Financiero, Evaluación Ex Post
### Diagrama de Flujo
- **Mermaid:** flowchart TD
 subgraph CIERRE_TEC["📋 Cierre Técnico"]
 A["Recepción provisoria"]
 B["Período garantía"]
 C["Recepción definitiva"]
 D["Informe final; técnico"]
 end

 subgraph CIERRE_FIN["💰 Cierre Financiero"]
 E["Rendición final; SISREC"]
 F["Revisión DAF"]
 G{"¿Saldos?"}
 H["Reintegro"]
 I["Resolución cierre; convenio"]
 J["Devolución; garantías"]
 end

 subgraph EXPOST["📊 Evaluación Ex Post"]
 K["Selección muestra"]
 L["Estudio evaluativo"]
 M["Lecciones aprendidas"]
 end

 A --> B --> C --> D
 D --> E --> F --> G
 G -->|"Sí"| H --> I
 G -->|"No"| I
 I --> J --> K --> L --> M

 style M fill:#9C27B0,color:#fff

## Sistemas Involucrados
### Filas
| Sistema | Fases_de_Uso |
| --- | --- |
| SYS-BIP-SNI | P1, P2, P5, P7 |
| SYS-GESDOC | P1, P2 |
| SYS-SIGFE | P3, P4, P5, P7 |
| SYS-SISREC | P7 |

## Normativa Aplicable
### Filas
| Norma | Alcance |
| --- | --- |
| LOC 19.175 | Competencias GORE |
| Ley de Presupuestos | Glosa 06, 14, 16 |
| Instructivo SUBDERE FRIL | Track C |
| Circular 33 MDSF | Track C |
| Resolución 30/2015 CGR | Rendiciones |
| Normas SNI/MDSF | Track A |

## Referencias Cruzadas
### Filas
| Dominio_Relacionado | Ctx_Optional | Vinculo |
| --- | --- | --- |
| D02 Ciclo Presupuestario | | CDP, modificaciones, SIGFE |
| D08 Rendiciones | | Cierre financiero, SISREC |
| D01 Actos Administrativos | | Resoluciones, Convenios |

## Ultima Actualizacion
- **Cpt:** Última actualización: 2025-12-16
