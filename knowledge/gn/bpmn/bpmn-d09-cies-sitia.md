---
_manifest:
  urn: "urn:gn:kb:bpmn-d09-cies-sitia"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "GORE Ñuble"
version: "2.0.0"
status: published
tags: [gore-nuble, gobierno-regional, seguridad-publica, cies, sitia, bpmn]
lang: es
---

# D09: Gestión Operativa CIES-SITIA (Seguridad Pública)

## Metadatos del Dominio

| Atributo | Detalle |
| :--- | :--- |
| **Identificador** | `DOM-CIES` |
| **Criticidad** | 🟠 Alta |
| **Responsable** | Supervisor CIES |
| **Alcance** | 3 Procesos principales / ~8 Subprocesos |
| **Referencia** | kb_gn_054_bpmn_c4_koda.yml (L.4142-4306) |

## Mapa General del Dominio

```mermaid
flowchart LR
    subgraph CIES["🎥 Centro CIES-ÑUBLE"]
        P1["P1: Monitoreo y<br/>Detección"]
        P2["P2: Coordinación<br/>Interinstitucional"]
        P3["P3: Gestión de<br/>Evidencias"]
    end

    subgraph SITIA["🤖 Integración SITIA"]
        S1["SITIA-Patentes"]
        S2["SITIA-Armas"]
        S3["SITIA-Evidencia"]
        S4["SITIA-Unificación"]
    end

    P1 --> P2
    P1 --> P3
    P1 <--> S1 & S2 & S4
    P3 <--> S3

    style P1 fill:#2196F3,color:#fff
    style P2 fill:#FF9800,color:#fff
    style P3 fill:#9C27B0,color:#fff
```

## Contexto Operativo

| Dimensión | Especificación |
| :--- | :--- |
| **Horario** | 16 horas (08:00-00:00) / Proyección 24/7 |
| **Localización** | Sala de monitoreo GORE Ñuble |
| **Interoperabilidad** | Policías, emergencias, 21 municipios |
| **Base Legal** | Ley 21.427 (Seguridad), Ley 20.965 (Cámaras), Ley 20.502 (Ministerio Interior) |

## P1: Monitoreo, Detección y Escalamiento

| Control | Valor |
| :--- | :--- |
| **ID Proceso** | `BPMN-GN-CIES-SITIA-MONITOREO-01` |
| **Plataforma Base** | HikCentral VMS |

### Flujo de Monitoreo

```mermaid
flowchart TD
    subgraph MONITOREO["🎥 Monitoreo Continuo"]
        A["Operador CIES<br/>monitorea cámaras"]
        B["Sistemas SITIA<br/>detectan automáticamente:<br/>• Patentes alertadas<br/>• Armas visibles"]
    end

    subgraph DETECCION["⚡ Detección"]
        C["Identificar evento/<br/>incidente"]
        D{"Clasificar<br/>prioridad"}
        D -->|"🔴 Alta"| E["Alarma inmediata"]
        D -->|"🟠 Media"| F["Registro y seguimiento"]
        D -->|"🟢 Baja"| G["Solo registro"]
    end

    subgraph ESCALAMIENTO["📢 Escalamiento"]
        E --> H["Supervisor CIES<br/>evalúa"]
        H --> I["Activar protocolo<br/>según tipo"]
        I --> J["Coordinar con:<br/>• Carabineros<br/>• PDI<br/>• Bomberos<br/>• SAMU"]
    end

    A --> C
    B --> C
    C --> D
    F --> H

    style E fill:#f44336,color:#fff
    style J fill:#4CAF50,color:#fff
```

### Clasificación de Incidentes

| Prioridad | Criterio | Acción Requerida |
| :--- | :--- | :--- |
| 🔴 **Alta** | Delito flagrante / Riesgo vital | Activación y despacho inmediato |
| 🟠 **Media** | Comportamiento anómalo / Sospecha | Monitoreo activo y evaluación |
| 🟢 **Baja** | Evento administrativo / Registro | Documentación en bitácora |

## P2: Coordinación Interinstitucional

| Control | Valor |
| :--- | :--- |
| **ID Proceso** | `BPMN-GN-CIES-SITIA-COORD-01` |
| **Contrapartes** | Carabineros, PDI, Bomberos, SAMU, Municipios |

### Flujo de Despacho

```mermaid
flowchart TD
    A["Incidente<br/>clasificado"] --> B["Enlace CIES<br/>activa canal"]
    B --> C{"Tipo de<br/>emergencia"}
    
    C -->|"Seguridad"| D["📞 Carabineros<br/>133"]
    C -->|"Investigación"| E["📞 PDI<br/>134"]
    C -->|"Incendio"| F["📞 Bomberos<br/>132"]
    C -->|"Salud"| G["📞 SAMU<br/>131"]
    
    D & E & F & G --> H["Confirmar recepción<br/>y unidades"]
    H --> I["Seguimiento<br/>en tiempo real"]
    I --> J["Registro de<br/>respuesta"]
    J --> K["Cierre de<br/>incidente"]

    style K fill:#4CAF50,color:#fff
```

### Canales de Comunicación

| Medio | Aplicación Operativa |
| :--- | :--- |
| **Radio VHF** | Enlace directo con cuadrantes policiales |
| **Líneas CENCO** | Comunicación con centrales de emergencia |
| **WhatsApp Inst.** | Coordinación con seguridad municipal |
| **SITIA** | Notificación e integración nacional |

## P3: Gestión de Evidencias Digitales

| Control | Valor |
| :--- | :--- |
| **ID Proceso** | `BPMN-GN-CIES-SITIA-EVIDENCIA-01` |
| **Repositorio** | SITIA-Evidencia (Genetec Clearance) |

### Ciclo de Vida de Evidencia

```mermaid
flowchart TD
    subgraph SOLICITUD["📋 Solicitud"]
        A["Fiscalía/Tribunal<br/>solicita evidencia"]
        B["Recepción oficio<br/>en GORE"]
        C["Verificar:<br/>• Orden judicial<br/>• Requerimiento MP"]
    end

    subgraph EXTRACCION["🎬 Extracción"]
        D["Supervisor CIES<br/>autoriza"]
        E["Localizar grabación<br/>en HikCentral"]
        F["Exportar clip<br/>seguro"]
        G["Subir a<br/>SITIA-Evidencia"]
    end

    subgraph ENTREGA["📤 Entrega"]
        H["Generar cadena<br/>de custodia"]
        I["Entrega por medio<br/>controlado"]
        J["Acta de entrega"]
        K["Registro para<br/>trazabilidad"]
    end

    A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K

    style J fill:#4CAF50,color:#fff
```

### Estándares de Cadena de Custodia

| Componente | Verificación de Integridad |
| :--- | :--- |
| **Algoritmo Hash** | Garantía de no alteración de bits |
| **Metadatos** | Estampado de tiempo y georreferencia (cámara) |
| **Logs de Acceso** | Trazabilidad completa de manipulación |
| **Firma Digital** | Certificación de origen y autenticidad |

## Capacidades SITIA

### SITIA-Patentes: Lectura y Contraste

```mermaid
flowchart LR
    A["Red de pórticos<br/>públicos/privados"] --> B["Lectura automática<br/>de placas"]
    B --> C["Contraste en<br/>tiempo real"]
    C --> D{"¿Encargo de<br/>búsqueda?"}
    D -->|"Sí"| E["🚨 Alerta a CIES<br/>y policías"]
    D -->|"No"| F["Registro histórico"]

    style E fill:#f44336,color:#fff
```

### SITIA-Armas: Detección Mediante IA

```mermaid
flowchart LR
    A["Cámaras CIES"] --> B["Modelo IA<br/>(YOLOv11)"]
    B --> C{"¿Arma<br/>detectada?"}
    C -->|"Sí"| D["🚨 Alerta automática"]
    C -->|"No"| E["Continuar monitoreo"]
    D --> F["Operador verifica"]
    F --> G["Escalar si confirma"]

    style D fill:#f44336,color:#fff
```

## Privacidad y Retención de Datos

### Políticas de Almacenamiento

| Concepto | Regla Aplicable |
| :--- | :--- |
| **Retención Estándar** | 30 días corridos |
| **Disposición Final** | Eliminación segura irreversible |
| **Cautela Ciudadana** | Extensión hasta 6 meses (solicitud víctima/testigo) |

### Flujo de Cumplimiento Normativo

```mermaid
flowchart TD
    A["Grabación<br/>generada"] --> B["Almacenar<br/>30 días"]
    B --> C{"¿Solicitud de<br/>cautela?"}
    C -->|"Sí"| D["Extender retención<br/>hasta 6 meses"]
    C -->|"No"| E["Eliminar<br/>automáticamente"]
    D --> F["Revisar al<br/>vencimiento"]
    F --> E

    style E fill:#607D8B,color:#fff
```

### Restricciones Legales (Ley 19.628)

*   **Licitud:** Solo fines de seguridad pública y persecución penal.
*   **Finalidad:** Uso exclusivo según convenios interinstitucionales.
*   **Proporcionalidad:** Captación limitada al espacio público autorizado.

## Sostenibilidad Operativa

### Estructura de Financiamiento

| Componente | Origen de Fondos |
| :--- | :--- |
| **Personal CIES** | Presupuesto anual GORE (Subtítulo 21) |
| **Mantenimiento HW** | Garantía técnica (22 meses) / Mantención GORE |
| **Soporte SITIA** | Convenio marco Subsecretaría Prevención del Delito (SPD) |

### Ciclo de Mantenimiento

```mermaid
flowchart LR
    A["Mantención<br/>preventiva"] -->|"Trimestral"| B["Revisión equipos"]
    B --> C["Actualizaciones<br/>software"]
    C --> D["Reporte estado"]

    style D fill:#4CAF50,color:#fff
```

## Ecosistema de Sistemas

| Sistema | Funcionalidad Clave |
| :--- | :--- |
| `SYS-HIKCENTRAL` | VMS para gestión de videovigilancia regional |
| `SYS-SITIA` | Plataforma nacional de integración de datos |
| `SYS-SITIA-EVIDENCIA` | Portal de gestión y entrega de clips judiciales |
| `SYS-SITIA-PATENTES` | Motor de lectura y alerta de placas vehiculares |
| `SYS-SITIA-ARMAS` | Módulo de inteligencia artificial para detección de armas |

## Marco Normativo Aplicable

| Norma | Ámbito de Aplicación |
| :--- | :--- |
| **Ley 21.427** | Modernización de la gestión policial y seguridad |
| **Ley 20.965** | Regulación de cámaras de vigilancia en espacios públicos |
| **Ley 20.502** | Funcionamiento de servicios de seguridad y emergencias |
| **Ley 19.628** | Protección de la vida privada y datos sensibles |
| **Ley 21.719** | Nueva ley de protección de datos personales |

## Referencias Cruzadas

| Dominio Relacionado | Vínculo Operativo |
| :--- | :--- |
| D01 Actos Administrativos | Formalización de convenios GORE-Policiales |
| D12 Gestión Territorial | Ubicación estratégica de puntos de monitoreo |
