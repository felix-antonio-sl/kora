---
_manifest:
  urn: urn:gn:kb:bpmn-d03-gestion-ipr
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml
version: 2.0.0
status: published
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
    skeleton_count: 15
    meat_count: 152
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d03-gestion-ipr.md.json
---

# BPMN D03: Gestión de Intervenciones Públicas Regionales (IPR)
## Source
### Contexto requerido
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml

## Metadatos Dominio
### Criticidad
🔴 Crítica
### Dueno
Jefatura DIPIR
### Procesos
9
### Subprocesos
~25
### Ref Fuente
#### Contexto requerido
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.1888-3727

## Mapa General Dominio
### Cpt
Mapa general del ciclo de vida de las Intervenciones Públicas Regionales (IPR), incluyendo pre-fase y fases P1–P7.
### Mermaid
flowchart LR
    subgraph PREFASE["🎯 Pre-Fase"]
        P0["P0: Selector<br/>de Vías"]
    end

    subgraph CICLO_VIDA["📋 Ciclo de Vida IPR"]
        P1["P1: Ingreso y<br/>Admisibilidad"]
        P2["P2: Evaluación<br/>Técnico-Económica"]
        P3["P3: Obtención de<br/>Financiamiento"]
        P4["P4: Formalización"]
        P5["P5: Ejecución y<br/>Supervisión"]
        P6["P6: Modificaciones<br/>en Ejecución"]
        P7["P7: Cierre y<br/>Evaluación Ex Post"]
    end

    P0 --> P1 --> P2 --> P3 --> P4 --> P5 --> P7
    P5 <--> P6

    style P0 fill:#FF9800,color:#fff
    style P1 fill:#2196F3,color:#fff
    style P2 fill:#9C27B0,color:#fff
    style P3 fill:#4CAF50,color:#fff
    style P4 fill:#00BCD4,color:#fff
    style P5 fill:#E91E63,color:#fff
    style P6 fill:#FFC107,color:#000
    style P7 fill:#607D8B,color:#fff


## P0 Selector de Vias de Financiamiento IPR
### Tipo
Pre-Fase (Decisión Estratégica)
### Objetivo
Orientar selección de vía antes de formulación
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A[("Iniciativa<br/>Identificada")] --> B{"¿Propósito<br/>Principal?"}

    B -->|"Activo Durable"| C["🏗️ PROYECTO"]
    B -->|"Servicio/Prestación"| D["📊 PROGRAMA"]

    C --> E{"Evaluar<br/>Criterios"}
    E -->|"Municipio + <5.000 UTM"| F["🏘️ FRIL"]
    E -->|"Conservación/ANF/Estudio"| G["📜 Circular 33"]
    E -->|"Foco productivo"| H["🚀 FRPD"]
    E -->|"Default"| I["📐 SNI General"]

    D --> J{"Tipo<br/>Ejecutor"}
    J -->|"Privado sin fines lucro"| K["🎁 8% FNDR"]
    J -->|"GORE"| L["📋 Glosa 06"]
    J -->|"Entidad Pública"| M["🔄 Transferencia"]
    J -->|"Foco productivo"| N["🚀 FRPD"]

    style A fill:#4CAF50,color:#fff
    style F fill:#FF9800,color:#fff
    style G fill:#9C27B0,color:#fff
    style H fill:#E91E63,color:#fff
    style I fill:#607D8B,color:#fff

### Matriz Decision
#### Filas
| Via | Tipo | Ejecutor | Monto | Condicion_Clave |
| --- | --- | --- | --- | --- |
| FRIL | Proyecto | Municipalidad | < 5.000 UTM | Infraestructura menor |
| Circular 33 | Proyecto | Variable | Variable | Conservación, ANF, estudios |
| FRPD | Ambos | Habilitado | Variable | Foco productivo/innovación |
| SNI General | Proyecto | Variable | Variable | Default |
| 8% FNDR | Actividad | Privado s/f lucro | Variable | Concurso |
| Glosa 06 | Programa | GORE | Variable | Ejecución directa |
| Transferencia | Programa | Entidad pública | Variable | ITF interno |

## P1 Ingreso Pertinencia y Admisibilidad
### Subprocesos
- Recepción
- CDR
- Admisibilidad Documental
### Diagrama de Flujo
#### Mermaid
flowchart TD
    subgraph EE["🏢 Entidad Externa"]
        A["📄 Postulación<br/>preparada"]
    end

    subgraph GORE["🏛️ GORE Ñuble"]
        B["📬 Oficina Partes:<br/>Recepcionar y registrar"]
        C["📊 DIPIR:<br/>Registrar en sistema"]
        D["👥 CDR:<br/>Evaluar pertinencia"]
        E{"¿Pre-admisible?"}
        F["✅ PRE-ADMISIBLE"]
        G["❌ NO PRE-ADMISIBLE"]
        H["🔍 Analista:<br/>Revisión documental"]
        I{"Estado<br/>admisibilidad"}
        J["✅ ADMISIBLE"]
        K["⚠️ CON OBSERVACIONES"]
        L["❌ INADMISIBLE"]
    end

    subgraph SUBSANACION["🔄 Subsanación"]
        M["Corregir en plazo"]
        N{"¿OK?"}
    end

    A --> B --> C --> D --> E
    E -->|"Sí"| F --> H --> I
    E -->|"No"| G
    I -->|"OK"| J
    I -->|"Observa"| K --> M --> N
    I -->|"Rechaza"| L
    N -->|"Sí"| J
    N -->|"No"| L

    style J fill:#4CAF50,color:#fff
    style L fill:#f44336,color:#fff

### Roles Involucrados
#### Filas
| Rol | Responsabilidad |
| --- | --- |
| Oficina de Partes | Recepcionar, registrar, derivar |
| Jefatura DIPIR | Registrar, convocar CDR |
| CDR | Evaluar pertinencia estratégica |
| Analista Preinversión | Revisión documental exhaustiva |

## P2 Evaluacion Tecnico Economica
### Tracks
- A (SNI)
- B (Glosa 06)
- C (Simplificadas)
- D (Transferencias)
### Diagrama de Tracks
#### Mermaid
flowchart TD
    A["IPR Admisible"] --> B{"Tipo de<br/>Iniciativa"}

    B -->|"Proyecto IDI"| C["Track A:<br/>SNI/MDSF"]
    B -->|"Programa GORE"| D["Track B:<br/>Glosa 06/DIPRES"]
    B -->|"FRIL/FRPD/C33/8%"| E["Track C:<br/>Vías Simplificadas"]
    B -->|"Transf. a Entidad Pública"| F["Track D:<br/>ITF Interno"]

    subgraph TRACK_A["Track A: SNI"]
        C --> C1["Revisión RIS"]
        C1 --> C2["Envío a MDSF"]
        C2 --> C3["RATE: RS/FI/OT"]
    end

    subgraph TRACK_B["Track B: Glosa 06"]
        D --> D1["Perfil MML"]
        D1 --> D2["Diseño MML"]
        D2 --> D3["DIPRES/SES evalúa"]
        D3 --> D4["RF/FI/OT"]
    end

    subgraph TRACK_C["Track C: Simplificadas"]
        E --> E1["Requisitos específicos"]
        E1 --> E2["Evaluación GORE"]
        E2 --> E3["RS/FI/OT"]
    end

    subgraph TRACK_D["Track D: Transferencias"]
        F --> F1["Postulación GESDOC"]
        F1 --> F2["Admisibilidad DAE"]
        F2 --> F3["Eval. MML"]
        F3 --> F4["ITF Interno"]
    end

    style C3 fill:#4CAF50,color:#fff
    style D4 fill:#4CAF50,color:#fff
    style E3 fill:#4CAF50,color:#fff
    style F4 fill:#4CAF50,color:#fff

### Track A SNI MDSF
#### Mermaid
flowchart LR
    A["Revisión<br/>interna GORE"] --> B["Verificar<br/>RIS aplicable"]
    B --> C["Cargar en<br/>BIP/Carpeta Digital"]
    C --> D["Oficio a MDSF"]
    D --> E["MDSF evalúa<br/>(5+10 días)"]
    E --> F{"RATE"}
    F -->|"RS"| G["✅ Aprobado"]
    F -->|"FI"| H["Subsanar<br/>(60 días)"]
    F -->|"OT"| I["❌ Rechazado"]
    H --> E

    style G fill:#4CAF50,color:#fff
    style I fill:#f44336,color:#fff

### Track C Vias Simplificadas
#### Mermaid
flowchart TD
    subgraph FRIL["FRIL"]
        F1["Postular<br/>GESDOC+BIP"]
        F2["Admisibilidad"]
        F3["Evaluación<br/>técnica"]
        F4["RS (60 días)"]
        F1 --> F2 --> F3 --> F4
    end

    subgraph FRPD["FRPD"]
        R1["Postular<br/>formulario online"]
        R2["Adm.<br/>Administrativa"]
        R3["Adm.<br/>Técnica/Ranking"]
        R4["Evaluación<br/>GORE"]
        R5["RS"]
        R1 --> R2 --> R3 --> R4 --> R5
    end

    subgraph C33["Circular 33"]
        C1["Postular<br/>GESDOC+BIP"]
        C2["Admisibilidad"]
        C3["Revisión<br/>técnica"]
        C4["RS/FI/OT"]
        C1 --> C2 --> C3 --> C4
    end


## P3 Obtencion de Financiamiento
### Rutas
- A (Sin CORE)
- B (Con CORE)
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["IPR con RS/RF"] --> B{"¿Requiere<br/>Acuerdo CORE?"}

    subgraph RUTA_A["Ruta A: Sin CORE"]
        C["Solicitar CDP"]
        D["DAF emite CDP"]
        E["Instrucción a<br/>Depto. Presupuesto"]
    end

    subgraph RUTA_B["Ruta B: Con CORE"]
        F["Preparar carpeta<br/>CORE"]
        G["Envío formal<br/>al CORE"]
        H["Votación CORE"]
        I{"¿Aprobado?"}
        J["Certificado<br/>Acuerdo CORE"]
        K["Solicitar creación<br/>presupuestaria"]
    end

    B -->|"No"| C --> D --> E
    B -->|"Sí"| F --> G --> H --> I
    I -->|"✅"| J --> K
    I -->|"❌"| L["Rechazado"]

    style E fill:#4CAF50,color:#fff
    style K fill:#4CAF50,color:#fff
    style L fill:#f44336,color:#fff

### Criterios para Acuerdo CORE
#### Filas
| Condicion | Requiere_CORE |
| --- | --- |
| Monto > 7.000 UTM | ✅ Sí |
| Nuevo programa/proyecto | ✅ Sí |
| Aumento costo <= 10% (tope 7.000 UTM) | ❌ No |
| Uso 3% emergencia (Glosa 14) | ❌ No |
| Regularización de ingresos | ❌ No |

## P4 Formalizacion
### Subprocesos
- Actos
- Convenio
- Devengo
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["Financiamiento<br/>aprobado"] --> B{"Tipo de<br/>modificación"}

    B -->|"Interna"| C["Resolución GORE"]
    B -->|"Afecta Partida 31"| D["Solicitud a DIPRES"]

    C & D --> E["Visaciones internas<br/>(DAF, DIPIR, Jurídica)"]
    E --> F["Firma Gobernador/a"]
    F --> G["Control externo<br/>(DIPRES/CGR)"]
    G --> H["Elaborar Convenio<br/>de Transferencia"]
    H --> I["Revisión Jurídica"]
    I --> J["Firma GORE +<br/>Entidad Receptora"]
    J --> K["Resolución aprobatoria"]
    K --> L["Programar<br/>transferencias"]

    style L fill:#4CAF50,color:#fff

### Regla de Devengo
#### Filas
| Tipo_Receptor | Momento_Devengo |
| --- | --- |
| Privados y Municipios | Convenio tramitado |
| Servicios Públicos | Al aprobar rendición |

## P5 Ejecucion y Supervision
### Subprocesos
- Inicio
- Licitación
- Seguimiento
### Diagrama de Flujo
#### Mermaid
flowchart TD
    subgraph INICIO["🚀 Inicio"]
        A["Chequeo documentación<br/>técnica"]
        B["Reunión coordinación<br/>GORE-UT"]
        C["Carpeta de<br/>seguimiento"]
    end

    subgraph LICITACION["📋 Licitación (si aplica)"]
        D["Bases y publicación<br/>Mercado Público"]
        E["Adjudicación"]
        F["Contrato"]
        G["Entrega terreno/<br/>Orden inicio"]
    end

    subgraph SEGUIMIENTO["📊 Seguimiento"]
        H["Visitas a terreno"]
        I["Revisión informes<br/>avance"]
        J["Estados de Pago"]
        K["Actualizar BIP"]
        L["Monitoreo financiero<br/>SIGFE"]
        M["Comité seguimiento"]
    end

    A --> B --> C --> D --> E --> F --> G
    G --> H --> I --> J --> K
    L --> M

    style K fill:#4CAF50,color:#fff

### Hitos de Control
#### Filas
| Hito | Responsable |
| --- | --- |
| Inicio de obra | UT / ITO |
| Avances periódicos | Supervisor GORE |
| Recepción provisoria | UT |
| Recepción definitiva | UT |

## P6 Modificaciones en Ejecucion
### Subprocesos
- Solicitud
- Evaluación
- Tramitación
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["Detectar necesidad<br/>de modificación"] --> B["UT prepara<br/>informe técnico"]
    B --> C["Oficio formal<br/>al GORE"]
    C --> D["Supervisor GORE<br/>analiza"]
    D --> E{"¿Altera<br/>objetivo?"}
    E -->|"Sí"| F["❌ Rechazar"]
    E -->|"No"| G["Verificar<br/>umbrales"]
    G --> H{"¿Requiere<br/>CORE/SNI?"}
    H -->|"Sí"| I["Tramitar como<br/>nueva aprobación"]
    H -->|"No"| J["Aprobar<br/>internamente"]
    I & J --> K["Convenio<br/>modificatorio"]

    style F fill:#f44336,color:#fff
    style K fill:#4CAF50,color:#fff


## P7 Cierre Tecnico Financiero y Evaluacion Ex Post
### Subprocesos
- Cierre Técnico
- Cierre Financiero
- Evaluación Ex Post
### Diagrama de Flujo
#### Mermaid
flowchart TD
    subgraph CIERRE_TEC["📋 Cierre Técnico"]
        A["Recepción provisoria"]
        B["Período garantía"]
        C["Recepción definitiva"]
        D["Informe final<br/>técnico"]
    end

    subgraph CIERRE_FIN["💰 Cierre Financiero"]
        E["Rendición final<br/>SISREC"]
        F["Revisión DAF"]
        G{"¿Saldos?"}
        H["Reintegro"]
        I["Resolución cierre<br/>convenio"]
        J["Devolución<br/>garantías"]
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
| D02 Ciclo Presupuestario | file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md | CDP, modificaciones, SIGFE |
| D08 Rendiciones | file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md | Cierre financiero, SISREC |
| D01 Actos Administrativos | file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D01_actos_administrativos.md | Resoluciones, Convenios |

## Ultima Actualizacion
### Cpt
Última actualización: 2025-12-16
