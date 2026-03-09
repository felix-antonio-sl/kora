---
_manifest:
  urn: urn:gn:kb:bpmn-d04-compras-contrataciones
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D04_compras_contrataciones_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- compras-publicas
- bpmn
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D04_compras_contrataciones_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D04_compras_contrataciones_koda.yml: 19700dc6bb9e38a84be1d89d8043f4178da2cc3349e284b132420e3bfb0a8c87
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.05
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
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d04-compras-contrataciones.md.json
---

# BPMN D04: Compras Públicas y Contrataciones

## Metadatos Dominio

### Criticidad
🟠 Alta

### Dueno
Unidad de Abastecimiento

### Procesos
4

### Subprocesos
~12

## Body MD
\# D04: Compras Públicas y Contrataciones
\## Metadatos del Dominio
| Campo           | Valor                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ID**          | `DOM-COMPRAS`                                                                                                                                        |
| **Criticidad**  | 🟠 Alta                                                                                                                                               |
| **Dueño**       | Unidad de Abastecimiento                                                                                                                             |
| **Procesos**    | 4                                                                                                                                                    |
| **Subprocesos** | ~12                                                                                                                                                  |
| **Ref. Fuente** | [kb_gn_054_bpmn_c4_koda.yml](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml) L.700-950 |
---
\## Mapa General del Dominio
```mermaid
flowchart LR
    subgraph CICLO["📋 Ciclo de Compras"]
        P1["P1: Plan Anual<br/>de Compras"]
        P2["P2: Licitación<br/>Pública"]
        P3["P3: Órdenes<br/>de Compra"]
        P4["P4: Gestión de<br/>Contratos"]
    end
    P1 --> P2 --> P3 --> P4
    P1 -->|"Convenio Marco"| P3
    style P1 fill:#2196F3,color:#fff
    style P2 fill:#FF9800,color:#fff
    style P3 fill:#4CAF50,color:#fff
    style P4 fill:#9C27B0,color:#fff
```
---
\## P1: Plan Anual de Compras (PAC)
| Campo       | Valor                    |
| ----------- | ------------------------ |
| **ID**      | `BPMN-GN-COMPRAS-PAC-01` |
| **Período** | Anual (Diciembre-Enero)  |
\### Diagrama de Flujo
```mermaid
flowchart TD
    A["Divisiones identifican<br/>necesidades"] --> B["Unidades envían<br/>requerimientos"]
    B --> C["Abastecimiento consolida"]
    C --> D["Clasificar por:<br/>• Convenio Marco<br/>• Licitación<br/>• Compra Directa"]
    D --> E["Validación<br/>presupuestaria (DAF)"]
    E --> F["Aprobación<br/>Gobernador/a"]
    F --> G["Publicar PAC en<br/>Mercado Público"]
    G --> H["Monitoreo y<br/>ajustes trimestrales"]
    style G fill:#4CAF50,color:#fff
```
\### Contenido del PAC
| Elemento          | Descripción              |
| ----------------- | ------------------------ |
| Producto/Servicio | Descripción detallada    |
| Cantidad estimada | Unidades requeridas      |
| Monto estimado    | Valor en pesos           |
| Período           | Trimestre de adquisición |
| Mecanismo         | CM/LP/CD/TDP             |
---
\## P2: Licitación Pública
| Campo      | Valor                           |
| ---------- | ------------------------------- |
| **ID**     | `BPMN-GN-COMPRAS-MECANISMOS-01` |
| **Umbral** | > 1.000 UTM                     |
\### Diagrama de Flujo
```mermaid
flowchart TD
    subgraph PREPARACION["📋 Preparación"]
        A["Elaborar bases<br/>técnicas y admin."]
        B["Revisión jurídica"]
        C["Resolución que<br/>aprueba bases"]
    end
    subgraph PUBLICACION["📤 Publicación"]
        D["Publicar en<br/>Mercado Público"]
        E["Período de<br/>consultas"]
        F["Respuestas y<br/>aclaraciones"]
        G["Recepción<br/>de ofertas"]
    end
    subgraph EVALUACION["🔍 Evaluación"]
        H["Comisión evaluadora<br/>revisa ofertas"]
        I["Aplicar criterios:<br/>• Precio<br/>• Calidad<br/>• Experiencia"]
        J["Acta de evaluación"]
        K["Propuesta de<br/>adjudicación"]
    end
    subgraph ADJUDICACION["✅ Adjudicación"]
        L["Resolución de<br/>adjudicación"]
        M["Publicar resultado"]
        N["Notificar a<br/>oferentes"]
        O["Período de<br/>impugnación"]
    end
    A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M --> N --> O
    style L fill:#4CAF50,color:#fff
```
\### Mecanismos de Compra
```mermaid
flowchart TD
    A["Necesidad de<br/>adquisición"] --> B{"Monto<br/>estimado"}
    B -->|"> 1.000 UTM"| C["🏛️ Licitación<br/>Pública"]
    B -->|"100-1.000 UTM"| D["📋 Licitación<br/>Privada"]
    B -->|"< 100 UTM"| E["💳 Compra<br/>Directa"]
    A --> F{"¿Existe<br/>Convenio Marco?"}
    F -->|"Sí"| G["🛒 Convenio<br/>Marco"]
    F -->|"No"| B
    style C fill:#f44336,color:#fff
    style G fill:#4CAF50,color:#fff
```
---
\## P3: Ejecución de Órdenes de Compra
| Campo       | Valor                   |
| ----------- | ----------------------- |
| **ID**      | `BPMN-GN-COMPRAS-OC-01` |
| **Sistema** | Mercado Público         |
\### Diagrama de Flujo
```mermaid
flowchart TD
    A["Adjudicación/<br/>Contrato vigente"] --> B["Abastecimiento:<br/>Generar OC"]
    B --> C["Asociar CDP y<br/>partida presupuestaria"]
    C --> D["Firma jefatura<br/>respectiva"]
    D --> E["Enviar OC a<br/>proveedor"]
    E --> F["Proveedor<br/>acepta OC"]
    F --> G["Recepción de<br/>bienes/servicios"]
    G --> H{"¿Conforme?"}
    H -->|"Sí"| I["Acta de<br/>recepción"]
    H -->|"No"| J["Rechazo/<br/>Devolución"]
    I --> K["Facturación"]
    K --> L["Pago"]
    style L fill:#4CAF50,color:#fff
```
\### Estados de la OC
| Estado       | Descripción                 |
| ------------ | --------------------------- |
| Generada     | OC creada en el sistema     |
| Enviada      | Notificada al proveedor     |
| Aceptada     | Proveedor confirma          |
| Recepcionada | Bienes/servicios entregados |
| Pagada       | Proceso completado          |
---
\## P4: Gestión de Contratos
| Campo           | Valor                          |
| --------------- | ------------------------------ |
| **ID**          | `BPMN-GN-COMPRAS-CONTRATOS-01` |
| **Responsable** | Administrador de Contrato      |
\### Diagrama de Flujo
```mermaid
flowchart TD
    subgraph FORMALIZACION["📋 Formalización"]
        A["Elaborar contrato"]
        B["Revisión jurídica"]
        C["Firma de partes"]
        D["Resolución aprobatoria"]
        E["Garantías:<br/>• Fiel cumplimiento<br/>• Anticipo"]
    end
    subgraph EJECUCION["⚙️ Ejecución"]
        F["Designar administrador<br/>de contrato"]
        G["Seguimiento<br/>de hitos"]
        H["Verificar<br/>cumplimiento"]
        I["Estados de pago<br/>parciales"]
    end
    subgraph CIERRE["✅ Cierre"]
        J["Recepción<br/>definitiva"]
        K["Acta de cierre"]
        L["Devolución<br/>garantías"]
        M["Evaluación<br/>proveedor"]
    end
    A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M
    style M fill:#4CAF50,color:#fff
```
\### Funciones del Administrador de Contrato
| Función       | Descripción                    |
| ------------- | ------------------------------ |
| Supervisión   | Verificar cumplimiento técnico |
| Comunicación  | Enlace con proveedor           |
| Documentación | Mantener expediente            |
| Hitos         | Certificar avances             |
| Pagos         | Autorizar estados de pago      |
---
\## Control y Transparencia
\### Obligaciones de Publicación
| Información       | Plataforma           |
| ----------------- | -------------------- |
| PAC               | Mercado Público      |
| Licitaciones      | Mercado Público      |
| Adjudicaciones    | Mercado Público      |
| Contratos         | Transparencia Activa |
| Órdenes de Compra | Mercado Público      |
\### Prohibiciones
> ⚠️ **Fraccionamiento prohibido**: No dividir compras para eludir umbrales.
> ⚠️ **Conflicto de intereses**: Funcionarios deben declarar inhabilidades.
---
\## Sistemas Involucrados
| Sistema           | Función                           |
| ----------------- | --------------------------------- |
| `ORG-CHILECOMPRA` | Mercado Público, OC, licitaciones |
| `SYS-SIGFE`       | CDP, compromisos, pagos           |
| `SYS-DOCDIGITAL`  | Contratos, resoluciones           |
---
\## Normativa Aplicable
| Norma                      | Alcance            |
| -------------------------- | ------------------ |
| **Ley 19.886**             | Compras públicas   |
| **Reglamento D.S. 250**    | Procedimientos     |
| **Directivas ChileCompra** | Operativas         |
| **Ley 20.730**             | Lobby y conflictos |
---
\## Referencias Cruzadas
| Dominio Relacionado                                                                                                                              | Vínculo                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| [D02 Ciclo Presupuestario](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md)   | CDP, compromisos             |
| [D05 Inventarios](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D05_inventarios_activo_fijo.md)         | Recepción de bienes          |
| [D01 Actos Administrativos](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D01_actos_administrativos.md) | Resoluciones de adjudicación |
---
*Última actualización: 2025-12-16*
