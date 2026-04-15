---
_manifest:
  urn: urn:gn:kb:bpmn-actos-administrativos
  provenance:
    created_by: FS
    created_at: '2026-03-15'
    source: BPMN D01 Tramitación Actos Administrativos GORE Ñuble, reconciliado con
      ssot-actos-admin v1.1.1
version: 1.0.0
status: published
tags:
- actos-administrativos
- resoluciones
- convenios
- gore-nuble
- tramitacion
lang: es
extensions:
  gn:
    family: guide
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:bpmn-actos-administrativos
---

# Tramitación de Actos Administrativos — GORE Ñuble

## Visión General

| Atributo | Valor |
|---|---|
| Criticidad | Alta |
| Dueño funcional | Unidad Jurídica |
| Procesos | 2 |
| Subprocesos | ~14 fases |

Dos procesos principales:

1. **P1 — Resoluciones**: tramitación de resoluciones (exentas y afectas) y decretos. 8 etapas canónicas de aprobación.
2. **P2 — Convenios y Transferencias**: tramitación de convenios y transferencias de recursos.

Elementos transversales: expediente electrónico, firma electrónica avanzada (FEA) y toma de razón (cuando aplica).

## Tipos de acto administrativo

| Tipo | Sujeto a TdR | Subtipos |
|---|---|---|
| Decreto | Sí | — |
| Resolución | Depende del monto | Exenta (< umbral CGR), Afecta (>= umbral CGR) |
| Oficio | No | — |

Umbral Toma de Razón CGR para GORE Ñuble: **2.500 UTM** (base legal: Res. 7/2019 CGR).

## Mapa de Procesos

```mermaid
flowchart LR
 subgraph PROCESOS["Procesos de Actos Administrativos"]
 P1["P1: Resoluciones; y Decretos"]
 P2["P2: Convenios y; Transferencias"]
 end

 subgraph TRANSVERSAL["Elementos Transversales"]
 T1["Expediente; Electrónico"]
 T2["Firma Electrónica; Avanzada"]
 T3["Toma de Razón; (cuando aplica)"]
 end

 P1 --> T1 & T2
 P2 --> T1 & T2 & T3

 style P1 fill:#2196F3,color:#fff
 style P2 fill:#4CAF50,color:#fff
```

## Etapas de aprobación (8 canónicas)

SLA: 15 días hábiles.

| Seq | Etapa | Actor |
|-----|-------|-------|
| 1 | Elaboración (Borrador) | Unidad competente |
| 2 | V.B. Jurídico | Asesoría Jurídica |
| 3 | V.B. Control | Unidad de Control |
| 4 | V.B. Jefatura División | Jefe/a de División |
| 5 | V.B. Administrador/a Regional | Administrador/a Regional |
| 6 | Firma Gobernador/a (FEA) | Gobernador/a Regional |
| 7 | Toma de Razón CGR | Contraloría General (solo Resoluciones Afectas y Decretos) |
| 8 | Notificación y Archivo | Oficina de Partes |

Resoluciones Exentas (monto < 2.500 UTM): omiten etapa 7 (TdR); pasan directamente de Firma a Notificación.

### Diagrama de Flujo

```mermaid
flowchart TD
 subgraph FASE1["1. Elaboracion"]
 A["Unidad competente:; Elaborar borrador"]
 B["Adjuntar antecedentes"]
 C["Ingresar al SGD"]
 end

 subgraph FASE2["2. VB Juridico"]
 D["Asesoria Juridica; recibe expediente"]
 E["Verificar legalidad; y forma"]
 F{"OK?"}
 G["VB Juridico"]
 H["Observar"]
 end

 subgraph FASE3["3. VB Control"]
 K["Unidad Control:; Verificar procedencia"]
 L{"Conforme?"}
 M["VB Control"]
 N["Reparar"]
 end

 subgraph FASE4["4. VB Jefatura Division"]
 I["Jefe/a Division:; Revisar y visar"]
 end

 subgraph FASE5["5. VB Administrador/a"]
 O["Administrador/a Regional:; Revisar y visar"]
 end

 subgraph FASE6["6. Firma"]
 P["Gobernador/a:; Firma con FEA"]
 end

 subgraph FASE7["7. Toma de Razon"]
 P2{"Tipo acto"}
 TDR["CGR: Toma de Razon"]
 EX["Exenta: omitir TdR"]
 end

 subgraph FASE8["8. Notificacion y Archivo"]
 Q["Oficina Partes:; Numerar y fechar"]
 R["Notificar a; interesados"]
 S["Publicar si; corresponde"]
 T["Archivar expediente"]
 end

 A --> B --> C --> D --> E --> F
 F -->|"Si"| G --> K --> L
 F -->|"No"| H --> A
 L -->|"Si"| M --> I --> O --> P --> P2
 L -->|"No"| N --> A
 P2 -->|"Afecta/Decreto"| TDR --> Q
 P2 -->|"Exenta"| EX --> Q
 Q --> R --> S --> T

 style P fill:#4CAF50,color:#fff
 style T fill:#607D8B,color:#fff
```

## Convenios y Transferencias

Proceso para la tramitación de convenios y transferencias asociadas a actos administrativos.

### Diagrama de Flujo

```mermaid
flowchart TD
 A["Area requirente; propone convenio"] --> B["Elaborar borrador; de convenio"]
 B --> C["Revision Juridica"]
 C --> D{"Ajustes?"}
 D -->|"Si"| B
 D -->|"No"| E["Resolucion que; aprueba convenio"]
 E --> F["Toma de Razon; si corresponde"]
 F --> G["Firma de partes"]
 G --> H["Ejecucion y; seguimiento"]
```

### Contenido Mínimo del Convenio

| Elemento | Descripción |
|---|---|
| Partes | GORE + Entidad receptora |
| Objeto | Descripción del programa/proyecto |
| Monto | Valor total y calendario |
| Plazos | Duración y fechas clave |
| Obligaciones | Deberes de cada parte |
| Rendición | Modalidad, plazos, SISREC |
| Restitución | Condiciones de devolución |
| Probidad | Cláusulas anticorrupción |

### Criterios de Toma de Razón

Resolución aprobatoria del convenio se somete a TdR CGR cuando el monto supera el umbral (2.500 UTM para GORE Ñuble).

```mermaid
flowchart TD
 A["Convenio; firmado"] --> B{"Monto >= 2.500 UTM?"}
 B -->|"Si"| C["Requiere; Toma de Razon"]
 B -->|"No"| D["Exento"]
 C --> E["CGR revisa; legalidad"]
 E --> F{"Resultado"}
 F -->|"Tomado Razon"| G["Acto vigente"]
 F -->|"Observado"| H["Subsanar y; reenviar"]

 style C fill:#f44336,color:#fff
 style D fill:#4CAF50,color:#fff
 style G fill:#4CAF50,color:#fff
```

## Expediente Electrónico

Estructura del expediente electrónico conforme a Ley 21.180 de Transformación Digital del Estado.

```mermaid
flowchart TD
 subgraph EXPEDIENTE["Expediente Electronico"]
 A["Metadatos:; - ID unico; - Fecha creacion; - Tipo acto"]
 B["Documentos:; - Borrador; - Antecedentes; - Visaciones"]
 C["Firmas:; - FEA funcionarios; - FEA autoridad"]
 D["Trazabilidad:; - Log de acciones; - Fechas/horas"]
 end

 A --> B --> C --> D

 style C fill:#2196F3,color:#fff
```

### Principios TDE Aplicables

| Principio | Aplicación |
|---|---|
| Equivalencia funcional | Documento digital = papel |
| Neutralidad tecnológica | Sin dependencia de proveedor |
| Interoperabilidad | Comunicación entre sistemas |
| Seguridad | Integridad, autenticidad, no repudio |

## Normativa Aplicable

| Norma | Alcance |
|---|---|
| Ley 19.880 LBPA | Procedimiento administrativo |
| Ley 21.180 TDE | Expediente electrónico |
| Ley 19.799 | Firma electrónica |
| Res. 7/2019 CGR | Umbrales Toma de Razón |
| Resolución 30/2015 CGR | Rendiciones |
| Ley 19.886 | Contratación pública |

## Sistemas de Información

| Sistema | Función |
|---|---|
| SYS-DOCDIGITAL | Gestión documental, expediente |
| SYS-FIRMAGOB | Firma Electrónica Avanzada |
| SYS-SIGFE | Registro de compromisos |
| SYS-TRANSPARENCIA | Publicación |
