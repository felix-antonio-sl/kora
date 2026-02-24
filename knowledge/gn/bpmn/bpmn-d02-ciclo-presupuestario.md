---
_manifest:
  urn: urn:gn:kb:bpmn-d02-ciclo-presupuestario
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE \xD1uble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- presupuesto
- bpmn
- finanzas
- gn
lang: es
---

# Ciclo Presupuestario Regional (BPMN D02)

## Metadatos y Estructura del Dominio
- **ID Dominio:** DOM-PRESUPUESTO
- **Criticidad:** Crítica (Rojo)
- **Responsables:** DAF (Funcionamiento) / DIPIR (Inversión)
- **Volumen:** 5 Procesos principales / ~15 Subprocesos
- **Referencia SSOT:** LOC 19.175 Art. 72-73

## Mapa General del Ciclo Anual
```mermaid
flowchart LR
    subgraph CICLO["📅 Ciclo Anual"]
        P1["P1: Formulación<br/>(May-Jun)"]
        P2["P2: Aprobación<br/>(Sep-Nov)"]
        P3["P3: Distribución<br/>(Dic-Ene)"]
        P4["P4: Ejecución<br/>(Todo el año)"]
        P5["P5: Control y<br/>Cierre (Dic-Ene)"]
    end

    subgraph TRANSVERSAL["🔄 Transversal"]
        PM["Modificaciones<br/>Presupuestarias"]
    end

    P1 --> P2 --> P3 --> P4 --> P5
    P4 <--> PM
    P5 -.->|"Retroalimentación"| P1

    style P1 fill:#2196F3,color:#fff
    style P2 fill:#4CAF50,color:#fff
    style P3 fill:#FF9800,color:#fff
    style P4 fill:#9C27B0,color:#fff
    style P5 fill:#607D8B,color:#fff
    style PM fill:#E91E63,color:#fff
```

## P1: Formulación del Presupuesto (Mayo-Junio)
### Flujo de Formulación
```mermaid
flowchart TD
    A["📜 DIPRES emite<br/>instructivo y clasificador"] --> B["Definir techos<br/>preliminares"]

    subgraph INVERSION["💼 Inversión (DIPIR)"]
        C1["Propuesta marco<br/>de inversión"]
        C2["Cartera proyectos<br/>con RS vigente"]
        C3["Asignaciones por<br/>fuente (FNDR/FRIL/FRPD)"]
    end

    subgraph FUNCIONAMIENTO["🏢 Funcionamiento (DAF)"]
        D1["Personal (Subt. 21)"]
        D2["Bienes/Servicios (Subt. 22)"]
        D3["Transferencias (Subt. 24)"]
    end

    B --> C1 & D1
    C1 --> C2 --> C3
    D1 --> D2 --> D3
    C3 & D3 --> E["Consolidación<br/>propuesta"]
    E --> F["Presentación a<br/>Gobernador/a"]
    F --> G["Ajustes según<br/>prioridades ERD"]
    G --> H["📤 Envío a DIPRES"]

    style A fill:#2196F3,color:#fff
    style H fill:#4CAF50,color:#fff
```

### Estructura de Subtítulos y Responsables
| Subtítulo | Concepto | Responsable |
| :--- | :--- | :--- |
| 21 | Personal | DAF |
| 22 | Bienes y Servicios | DAF |
| 24 | Transferencias Corrientes | DAF/DIPIR |
| 29 | Activos No Financieros | DAF |
| 31 | Inversión (Iniciativas) | DIPIR |
| 33 | Transferencias de Capital | DIPIR |

## P2-P4: Aprobación, Distribución y Ejecución
- **P2 Aprobación (Sep-Nov):** Intervención de Gobernador, CORE, DIPRES y CGR.
- **P3 Distribución (Dic-Ene):** Distribución inicial del presupuesto aprobado y carga masiva en SIGFE.
- **P4 Ejecución (Anual):** Gestión de compromisos, devengos y pagos según calendario mensual.

## P5: Control y Cierre de Ejercicio (Diciembre-Enero)
### Flujo de Cierre y Evaluación
```mermaid
flowchart TD
    subgraph CONTROL["🔍 Control Durante el Año"]
        A["Control interno<br/>(DAF, DIPIR, U. Control)"]
        B["Seguimiento DIPRES<br/>(mensual)"]
        C["Sistema KPIs y<br/>alertas tempranas"]
    end

    subgraph CIERRE["📅 Cierre 31/12"]
        D["Consolidar<br/>información (DAF)"]
        E["Cerrar cuentas<br/>en SIGFE"]
        F["Calcular deuda<br/>flotante"]
        G["Regularizar<br/>deuda flotante"]
        H["Informe cierre<br/>a DIPRES/CGR"]
    end

    subgraph EVALUACION["📊 Evaluación"]
        I["Evaluar resultados<br/>físicos y financieros"]
        J["Informe evaluación<br/>ex post (DIPIR)"]
    end

    A & B & C --> D --> E --> F --> G --> H
    H --> I --> J

    style H fill:#607D8B,color:#fff
    style J fill:#9C27B0,color:#fff
```

### Gestión de Deuda Flotante
```mermaid
flowchart TD
    A["Obligaciones devengadas<br/>al 31/12 pendientes<br/>de pago"] --> B{"¿SIC<br/>suficiente?"}
    B -->|"Sí"| C["Financiar con<br/>SIC"]
    B -->|"No"| D["SIC + Mayor<br/>aporte fiscal"]
    C & D --> E["Incorporar en<br/>presupuesto año siguiente"]
    E --> F["Primera prioridad<br/>de pago"]

    style F fill:#FF9800,color:#fff
```

## Reportería, Sistemas y Normativa
### Reportes Oficiales
| Reporte | Frecuencia | Destinatario |
| :--- | :--- | :--- |
| Informe Ejecución Mensual | Mensual | DIPRES, CORE |
| Informes por Glosas | Trimestral | Transparencia |
| Cartera de Proyectos | Mensual | Web institucional |
| Acuerdos CORE | 5 días hábiles | Web institucional |

### Ecosistema de Sistemas
| Sistema | Función |
| :--- | :--- |
| SYS-SIGFE | Gestión financiera central del Estado |
| SYS-BIP-SNI | Gestión de inversión pública |
| SYS-TRANSPARENCIA | Publicación de información activa |

### Marco Normativo Aplicable
| Norma | Alcance |
| :--- | :--- |
| LOC 19.175 Art. 72-73 | Competencias presupuestarias del GORE |
| Decreto 854/2004 Hacienda | Clasificador presupuestario vigente |
| Ley de Presupuestos (Anual) | Marco legal del ejercicio financiero |
| Glosa 14 Partida 31 | Uso de 3% para emergencias |
| Glosa 16 Partida 31 | Exigencias de transparencia |
| NICSP-CGR | Normas Internacionales de Contabilidad Sector Público |
| Resolución 30/2015 CGR | Procedimientos de rendiciones de cuentas |

## Referencias Cruzadas
| Dominio Relacionado | Vínculo / Dependencia |
| :--- | :--- |
| D03 Gestión IPR | CDP, financiamiento de proyectos de inversión |
| D08 Rendiciones | Contabilización, conciliación en SIGFE |
| D04 Compras | Órdenes de compra, contratos y devengos |
