---
_manifest:
  urn: urn:gn:kb:bpmn-d05-inventarios-activo-fijo
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D05_inventarios_activo_fijo_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- bpmn
- inventarios
- activo-fijo
- sigas
- sigfe
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D05_inventarios_activo_fijo_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D05_inventarios_activo_fijo_koda.yml: 866b4cd7ee85542957200f88eb2a6f4dd9e97886a4eeb904c40ca0aa0751050c
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.06
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 3
    meat_count: 11
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d05-inventarios-activo-fijo.md.json
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:bpmn-d05-inventarios-activo-fijo
---

# D05: Gestión de Inventarios y Activo Fijo

## Metadatos del Dominio

| Campo | Valor |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ID** | `DOM-INVENTARIOS-AF` |
| **Criticidad** | 🟡 Media |
| **Dueño** | DAF |
| **Procesos** | 2 |
| **Subprocesos** | ~10 |
| **Ref. Fuente** | [kb_gn_054_bpmn_c4_koda.yml] L.960-1200 |

---

## Mapa General del Dominio

```mermaid
flowchart LR
 subgraph EXISTENCIAS["📦 Existencias (Inventarios)"]
 P1A["Catálogo; materiales"]
 P1B["Recepción; desde OC"]
 P1C["Consumo y; despacho"]
 P1D["Inventario; físico"]
 P1E["Control; vencimientos"]
 end

 subgraph ACTIVO_FIJO["🏢 Activo Fijo"]
 P2A["Alta de; bienes"]
 P2B["Valorización y; depreciación"]
 P2C["Movimientos; internos"]
 P2D["Baja de; bienes"]
 P2E["Inventario; físico AF"]
 end

 P1A --> P1B --> P1C --> P1D
 P1C --> P1E
 P2A --> P2B --> P2C
 P2C --> P2D
 P2C --> P2E

 style P1B fill:#4CAF50,color:#fff
 style P2A fill:#2196F3,color:#fff
```

---

## P1: Gestión de Inventarios y Bodegas

| Campo | Valor |
| ----------- | -------------------------------- |
| **ID** | `BPMN-GN-INVENTARIOS-BODEGAS-01` |
| **Sistema** | SIGAS |

### Catálogo de Materiales

```mermaid
flowchart TD
 A["Identificar necesidad; de nuevo ítem"] --> B["Verificar si; existe código"]
 B --> C{"¿Existe?"}
 C -->|"Sí"| D["Usar código; existente"]
 C -->|"No"| E["Crear nuevo; código en SIGAS"]
 E --> F["Asignar:; • Nombre; • Unidad medida; • Categoría; • Valorización"]

 style F fill:#2196F3,color:#fff
```

### Recepción de Bienes desde OC

```mermaid
flowchart TD
 A["OC aceptada; por proveedor"] --> B["Proveedor entrega; en bodega"]
 B --> C["Bodeguero verifica:; • Cantidad; • Calidad; • Guía despacho"]
 C --> D{"¿Conforme?"}
 D -->|"Sí"| E["Firmar guía; de recepción"]
 D -->|"No"| F["Rechazar/; Devolver"]
 E --> G["Ingresar en; SIGAS"]
 G --> H["Actualizar; stock"]
 H --> I["Notificar a; requirente"]

 style H fill:#4CAF50,color:#fff
```

### Consumo y Despacho

```mermaid
flowchart TD
 A["Unidad solicita; materiales"] --> B["Generar vale; de consumo"]
 B --> C["Jefatura; autoriza"]
 C --> D["Bodeguero; prepara pedido"]
 D --> E["Despachar y; firmar vale"]
 E --> F["Actualizar stock; en SIGAS"]
 F --> G["Imputar a; centro costo"]

 style G fill:#FF9800,color:#fff
```

### Inventario Físico

```mermaid
flowchart TD
 A["Programar inventario; (mensual/trimestral)"] --> B["Bloquear movimientos; en SIGAS"]
 B --> C["Equipo realiza; conteo físico"]
 C --> D["Comparar con; saldo sistema"]
 D --> E{"¿Diferencias?"}
 E -->|"Sí"| F["Investigar; causas"]
 E -->|"No"| G["Cerrar inventario"]
 F --> H{"¿Justificado?"}
 H -->|"Sí"| I["Ajustar sistema"]
 H -->|"No"| J["Responsabilidad; administrativa"]
 I --> G
 J --> G

 style G fill:#4CAF50,color:#fff
```

### Control de Vencimientos (FEFO)

```mermaid
flowchart TD
 A["Ingresar artículo; con fecha vencimiento"] --> B["SIGAS registra; y alerta"]
 B --> C["Despachar primero; próximos a vencer"]
 C --> D{"¿Próximo a; vencer sin uso?"}
 D -->|"Sí"| E["Evaluar:; • Uso urgente; • Donación; • Baja"]
 D -->|"No"| F["Continuar; operación normal"]

 style C fill:#FFC107,color:#000
```

### Valorización de Existencias

| Método | Descripción | Uso |
| -------- | ------------------------- | ----------- |
| **PPP** | Precio Promedio Ponderado | Default |
| **FIFO** | First In, First Out | Alternativo |
| **FEFO** | First Expired, First Out | Perecibles |

---

## P2: Gestión de Activo Fijo

| Campo | Valor |
| ------------- | ------------------------ |
| **ID** | `BPMN-GN-ACTIVO-FIJO-01` |
| **Umbral** | ≥ 3 UTM para capitalizar |
| **Normativa** | NICSP 17, 21, 31 |

### Alta de Bienes

```mermaid
flowchart TD
 A["Bien adquirido; (compra, donación, etc.)"] --> B{"Valor ≥ 3 UTM; y vida útil > 1 año"}
 B -->|"Sí"| C["Activo Fijo"]
 B -->|"No"| D["Gasto del período"]
 C --> E["Asignar N° inventario"]
 E --> F["Plaquetear bien"]
 F --> G["Registrar en SIGAS:; • Código; • Valor; • Ubicación; • Responsable"]
 G --> H["Contabilizar; en SIGFE"]

 style H fill:#4CAF50,color:#fff
```

### Valorización y Depreciación

```mermaid
flowchart TD
 A["Bien dado de alta"] --> B["Determinar:; • Vida útil; • Valor residual"]
 B --> C["Calcular depreciación; mensual (línea recta)"]
 C --> D["SIGAS ejecuta; depreciación automática"]
 D --> E["Generar asientos; SIGFE mensuales"]
 E --> F["Valor libro =; Costo - Deprec. Acum."]

 style F fill:#9C27B0,color:#fff
```

### Movimientos Internos

```mermaid
flowchart TD
 A["Solicitud de; traslado"] --> B["Jefatura origen; autoriza"]
 B --> C["Actualizar ubicación; y responsable en SIGAS"]
 C --> D["Bien se traslada; físicamente"]
 D --> E["Jefatura destino; confirma recepción"]

 style E fill:#FF9800,color:#fff
```

### Baja de Bienes

```mermaid
flowchart TD
 A["Identificar bien; para baja"] --> B{"Causal"}
 B -->|"Deterioro; irreparable"| C["Informe técnico"]
 B -->|"Obsolescencia"| D["Informe funcional"]
 B -->|"Pérdida/Hurto"| E["Denuncia +; Sumario"]
 B -->|"Donación"| F["Autorización; Gobernador/a"]
 
 C & D & E & F --> G["Resolución; de baja"]
 G --> H["Dar de baja; en SIGAS"]
 H --> I["Contabilizar; en SIGFE"]
 I --> J["Destino físico:; • Destrucción; • Remate; • Donación"]

 style J fill:#607D8B,color:#fff
```

### Inventario Físico Activo Fijo

```mermaid
flowchart TD
 A["Programar inventario; (anual)"] --> B["Corte de sistema; y reportes"]
 B --> C["Equipos verifican; existencia física"]
 C --> D["Escanear plaquetas; o verificar N°"]
 D --> E["Comparar con; registro SIGAS"]
 E --> F{"¿Diferencias?"}
 F -->|"Sí"| G["Investigar; y regularizar"]
 F -->|"No"| H["Cerrar inventario"]
 G --> H

 style H fill:#4CAF50,color:#fff
```

---

## Casos Especiales

### Bienes de Proyectos FNDR

```mermaid
flowchart LR
 A["Proyecto FNDR; entrega bienes"] --> B["Transferencia a; entidad receptora"]
 B --> C["GORE registra; como ANF hasta; traspasar"]
 C --> D["Resolución de; transferencia"]
 D --> E["Receptor da; de alta en su; patrimonio"]

 style D fill:#FF9800,color:#fff
```

### Comodatos y Préstamos

| Tipo | Descripción |
| ---------------------- | -------------------------------- |
| **Comodato recibido** | Bien de tercero en custodia GORE |
| **Comodato entregado** | Bien GORE en custodia de tercero |

> ⚠️ Ambos requieren convenio y registro separado en control paralelo.

---

## Sistemas Involucrados

| Sistema | Función |
| ------------ | --------------------------- |
| `SYS-SIGAS` | Gestión de inventarios y AF |
| `SYS-SIGFE` | Contabilización |
| `SYS-SIGFIN` | Integración financiera |

---

## Normativa Aplicable

| Norma | Alcance |
| -------------- | -------------------------------- |
| **NICSP 17** | Propiedad, planta y equipo |
| **NICSP 21** | Deterioro activos no generadores |
| **NICSP 31** | Activos intangibles |
| **Res. CGR** | Procedimientos de baja |
| **Ley 18.575** | Responsabilidad patrimonial |

---

## Referencias Cruzadas

| Dominio Relacionado | Vínculo |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [D04 Compras] | Recepción desde OC |
| [D02 Ciclo Presupuestario] | Contabilización AF |

---

*Última actualización: 2025-12-16*
