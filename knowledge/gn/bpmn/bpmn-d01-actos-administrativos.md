---
_manifest:
  urn: urn:gn:kb:bpmn-d01-actos-administrativos
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- bpmn
- actos-administrativos
- ley-19880
- ley-21180
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml: b0cfd30ba3085e4149285f535c9083cf50f7abcc622a77edf76c80b1d324c84e
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.65
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 10
    meat_count: 95
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d01-actos-administrativos.md.json
---

# BPMN D01: Tramitación de Actos Administrativos
## Source
### Contexto requerido
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml

## Metadatos Dominio
### Criticidad
🟠 Alta
### Dueno
Unidad Jurídica
### Procesos
2
### Subprocesos
~14 fases
### Ref Fuente
#### Contexto requerido
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.100-499

## Mapa General Dominio
### Cpt
Mapa general de los procesos de actos administrativos (resoluciones exentas y convenios/transferencias) y elementos transversales.
### Mermaid
flowchart LR
    subgraph PROCESOS["📋 Procesos de Actos Administrativos"]
        P1["P1: Resoluciones<br/>Exentas"]
        P2["P2: Convenios y<br/>Transferencias"]
    end

    subgraph TRANSVERSAL["🔧 Elementos Transversales"]
        T1["Expediente<br/>Electrónico"]
        T2["Firma Electrónica<br/>Avanzada"]
        T3["Toma de Razón<br/>(cuando aplica)"]
    end

    P1 --> T1 & T2
    P2 --> T1 & T2 & T3

    style P1 fill:#2196F3,color:#fff
    style P2 fill:#4CAF50,color:#fff


## P1 Flujo Resoluciones Exentas
### Fases
7
### SLA
15 días hábiles
### Diagrama de Flujo Completo
#### Mermaid
flowchart TD
    subgraph FASE1["1️⃣ Iniciación"]
        A["Área Requirente:<br/>Elaborar borrador"]
        B["Adjuntar<br/>antecedentes"]
        C["Ingresar al SGD"]
    end

    subgraph FASE2["2️⃣ Revisión Jurídica"]
        D["Jurídica recibe<br/>expediente"]
        E["Verificar legalidad<br/>y forma"]
        F{"¿OK?"}
        G["✅ V°B° Jurídico"]
        H["❌ Observar"]
    end

    subgraph FASE3["3️⃣ Gestión"]
        I["Centro Gestión:<br/>Asignar N° resolución"]
        J["Completar<br/>formalidades"]
    end

    subgraph FASE4["4️⃣ Control"]
        K["Unidad Control:<br/>Verificar procedencia"]
        L{"¿Conforme?"}
        M["✅ V°B° Control"]
        N["❌ Reparar"]
    end

    subgraph FASE5["5️⃣ V°B° Administrador/a"]
        O["Administrador/a Regional:<br/>Revisar y visar"]
    end

    subgraph FASE6["6️⃣ Firma"]
        P["Gobernador/a:<br/>Firma con FEA"]
    end

    subgraph FASE7["7️⃣ Notificación y Archivo"]
        Q["Oficina Partes:<br/>Numerar y fechar"]
        R["Notificar a<br/>interesados"]
        S["Publicar si<br/>corresponde"]
        T["Archivar expediente"]
    end

    A --> B --> C --> D --> E --> F
    F -->|"Sí"| G --> I --> J --> K --> L
    F -->|"No"| H --> A
    L -->|"Sí"| M --> O --> P --> Q --> R --> S --> T
    L -->|"No"| N --> A

    style P fill:#4CAF50,color:#fff
    style T fill:#607D8B,color:#fff

### Roles por Fase
#### Filas
| Fase | Responsable |
| --- | --- |
| Iniciación | Área Requirente |
| Revisión Jurídica | Unidad Jurídica |
| Gestión | Centro de Gestión |
| Control | Unidad de Control |
| V°B° Administrador/a | Administrador/a Regional |
| Firma | Gobernador/a Regional |
| Notificación y Archivo | Oficina de Partes |

## P2 Convenios y Transferencias
### Cpt
Proceso para la tramitación de convenios y transferencias asociadas a actos administrativos.
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["Área requirente<br/>propone convenio"] --> B["Elaborar borrador<br/>de convenio"]
    B --> C["Revisión Jurídica"]
    C --> D{"¿Ajustes?"}
    D -->|"Sí"| B
    D -->|"No"| E["Resolución que<br/>aprueba convenio"]
    E --> F["Toma de Razón<br/>si corresponde"]
    F --> G["Firma de partes"]
    G --> H["Ejecución y<br/>seguimiento"]

### Contenido Minimo Convenio
#### Filas
| Elemento | Descripcion |
| --- | --- |
| Partes | GORE + Entidad receptora |
| Objeto | Descripción del programa/proyecto |
| Monto | Valor total y calendario |
| Plazos | Duración y fechas clave |
| Obligaciones | Deberes de cada parte |
| Rendicion | Modalidad, plazos, SISREC |
| Restitucion | Condiciones de devolución |
| Probidad | Cláusulas anticorrupción |
### Criterios Toma de Razon
#### Mermaid
flowchart TD
    A["Convenio<br/>firmado"] --> B{"Monto y<br/>naturaleza"}
    B -->|"Supera umbral<br/>CGR"| C["Requiere<br/>Toma de Razón"]
    B -->|"Bajo umbral"| D["Exento"]
    B -->|"Normativa<br/>específica"| E["Consultar<br/>Res. CGR"]

    style C fill:#f44336,color:#fff
    style D fill:#4CAF50,color:#fff


## Expediente Electronico Ley 21180
### Estructura Expediente
#### Mermaid
flowchart TD
    subgraph EXPEDIENTE["📁 Expediente Electrónico"]
        A["Metadatos:<br/>• ID único<br/>• Fecha creación<br/>• Tipo acto"]
        B["Documentos:<br/>• Borrador<br/>• Antecedentes<br/>• Visaciones"]
        C["Firmas:<br/>• FEA funcionarios<br/>• FEA autoridad"]
        D["Trazabilidad:<br/>• Log de acciones<br/>• Fechas/horas"]
    end

    A --> B --> C --> D

    style C fill:#2196F3,color:#fff

### Principios TDE
#### Filas
| Principio | Aplicacion |
| --- | --- |
| Equivalencia funcional | Documento digital = papel |
| Neutralidad tecnológica | Sin dependencia de proveedor |
| Interoperabilidad | Comunicación entre sistemas |
| Seguridad | Integridad, autenticidad, no repudio |

## Sistemas Involucrados
### Filas
| Sistema | Funcion |
| --- | --- |
| SYS-DOCDIGITAL | Gestión documental, expediente |
| SYS-FIRMAGOB | Firma Electrónica Avanzada |
| SYS-SIGFE | Registro de compromisos |
| SYS-TRANSPARENCIA | Publicación |

## Normativa Aplicable
### Filas
| Norma | Alcance |
| --- | --- |
| Ley 19.880 LBPA | Procedimiento administrativo |
| Ley 21.180 TDE | Expediente electrónico |
| Ley 19.799 | Firma electrónica |
| Resolución 30/2015 CGR | Rendiciones |
| Ley 19.886 | Contratación pública |

## Referencias Cruzadas
### Filas
| Dominio_Relacionado | Ctx_Optional | Vinculo |
| --- | --- | --- |
| D03 Gestión IPR | file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D03_gestion_ipr.md | Fase 4 Formalización |
| D02 Ciclo Presupuestario | file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md | Modificaciones, resoluciones |
| D08 Rendiciones | file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md | Convenios de transferencia |

## Ultima Actualizacion
### Cpt
Última actualización: 2025-12-16
