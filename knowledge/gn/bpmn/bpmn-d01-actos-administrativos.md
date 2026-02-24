---
_manifest:
  urn: "urn:gn:kb:bpmn-d01-actos-administrativos"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "GORE Ñuble"
version: "2.0.0"
status: published
tags: [gore-nuble, gobierno-regional, bpmn, actos-administrativos, ley-19880, ley-21180]
lang: es
---

# BPMN D01: Tramitación de Actos Administrativos

## Metadatos y Mapa General del Dominio

### Atributos de Dominio
| Atributo | Valor |
| :--- | :--- |
| ID | DOM-ACTOS-ADMIN |
| Criticidad | 🟠 Alta |
| Dueño | Unidad Jurídica |
| Procesos | 2 |
| Subprocesos | ~14 fases |

### Mapa General de Procesos
```mermaid
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
```

## Proceso P1: Resoluciones Exentas

### Flujo de Tramitación
- **ID**: BPMN-GN-RES-EXENTAS-FLUJO-01
- **Fases**: 7
- **SLA**: 15 días hábiles

```mermaid
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
```

### Roles y Responsabilidades P1
| Fase | Responsable |
| :--- | :--- |
| Iniciación | Área Requirente |
| Revisión Jurídica | Unidad Jurídica |
| Gestión | Centro de Gestión |
| Control | Unidad de Control |
| V°B° Administrador/a | Administrador/a Regional |
| Firma | Gobernador/a Regional |
| Notificación y Archivo | Oficina de Partes |

## Proceso P2: Convenios y Transferencias

### Flujo de Convenios
```mermaid
flowchart TD
    A["Área requirente<br/>propone convenio"] --> B["Elaborar borrador<br/>de convenio"]
    B --> C["Revisión Jurídica"]
    C --> D{"¿Ajustes?"}
    D -->|"Sí"| B
    D -->|"No"| E["Resolución que<br/>aprueba convenio"]
    E --> F["Toma de Razón<br/>si corresponde"]
    F --> G["Firma de partes"]
    G --> H["Ejecución y<br/>seguimiento"]
```

### Contenido Mínimo de Convenios
| Elemento | Descripción |
| :--- | :--- |
| Partes | GORE + Entidad receptora |
| Objeto | Descripción del programa/proyecto |
| Monto | Valor total y calendario |
| Plazos | Duración y fechas clave |
| Obligaciones | Deberes de cada parte |
| Rendición | Modalidad, plazos, SISREC |
| Restitución | Condiciones de devolución |
| Probidad | Cláusulas anticorrupción |

### Criterios de Toma de Razón
```mermaid
flowchart TD
    A["Convenio<br/>firmado"] --> B{"Monto y<br/>naturaleza"}
    B -->|"Supera umbral<br/>CGR"| C["Requiere<br/>Toma de Razón"]
    B -->|"Bajo umbral"| D["Exento"]
    B -->|"Normativa<br/>específica"| E["Consultar<br/>Res. CGR"]

    style C fill:#f44336,color:#fff
    style D fill:#4CAF50,color:#fff
```

## Expediente Electrónico (Ley 21.180)

### Estructura del Expediente
```mermaid
flowchart TD
    subgraph EXPEDIENTE["📁 Expediente Electrónico"]
        A["Metadatos:<br/>• ID único<br/>• Fecha creación<br/>• Tipo acto"]
        B["Documentos:<br/>• Borrador<br/>• Antecedentes<br/>• Visaciones"]
        C["Firmas:<br/>• FEA funcionarios<br/>• FEA autoridad"]
        D["Trazabilidad:<br/>• Log de acciones<br/>• Fechas/horas"]
    end

    A --> B --> C --> D

    style C fill:#2196F3,color:#fff
```

### Principios de Transformación Digital (TDE)
| Principio | Aplicación |
| :--- | :--- |
| Equivalencia funcional | Documento digital = papel |
| Neutralidad tecnológica | Sin dependencia de proveedor |
| Interoperabilidad | Comunicación entre sistemas |
| Seguridad | Integridad, autenticidad, no repudio |

## Sistemas y Normativa

### Ecosistema de Sistemas
| Sistema | Función |
| :--- | :--- |
| SYS-DOCDIGITAL | Gestión documental, expediente |
| SYS-FIRMAGOB | Firma Electrónica Avanzada |
| SYS-SIGFE | Registro de compromisos |
| SYS-TRANSPARENCIA | Publicación |

### Marco Normativo
| Norma | Alcance |
| :--- | :--- |
| Ley 19.880 LBPA | Procedimiento administrativo |
| Ley 21.180 TDE | Expediente electrónico |
| Ley 19.799 | Firma electrónica |
| Resolución 30/2015 CGR | Rendiciones |
| Ley 19.886 | Contratación pública |

## Referencias Cruzadas

| Dominio Relacionado | Vínculo | Referencia |
| :--- | :--- | :--- |
| D03 Gestión IPR | Fase 4 Formalización | `D03_gestion_ipr.md` |
| D02 Ciclo Presupuestario | Modificaciones, resoluciones | `D02_ciclo_presupuestario.md` |
| D08 Rendiciones | Convenios de transferencia | `D08_rendiciones.md` |

---
**Última actualización**: 2025-12-16
