---
_manifest:
  urn: urn:gn:kb:bpmn-d07-rrhh
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D07_rrhh_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- rrhh
- bpmn
- gestion-personas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D07_rrhh_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D07_rrhh_koda.yml: 6f057ef1f3c5dc59c43b5d51a1f7eac20fd95fcfdc2f0d043c2ee832ca215872
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
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d07-rrhh.md.json
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:gn:kb:bpmn-d07-rrhh
---

# D07: Gestión de Personas (RRHH)


## Metadatos del Dominio

| Campo | Valor |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ID** | `DOM-RRHH` |
| **Criticidad** | 🟠 Alta |
| **Dueño** | Área de Gestión de Personas |
| **Procesos** | 7 |
| **Subprocesos** | ~20 |
| **Ref. Fuente** | [kb_gn_054_bpmn_c4_koda.yml](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml) L.1410-1880 |

---

## Mapa General del Dominio

```mermaid
flowchart LR
 subgraph CICLO_VIDA["👤 Ciclo de Vida del Funcionario"]
 P1["P1: Ingreso y; Contratación"]
 P2["P2: Inducción"]
 P3["P3: Remuneraciones"]
 P4["P4: Tiempo y; Ausentismo"]
 P5["P5: Desarrollo y; Capacitación"]
 P6["P6: Bienestar"]
 P7["P7: Egreso"]
 end

 P1 --> P2 --> P3
 P3 --> P4
 P3 --> P5
 P3 --> P6
 P4 & P5 & P6 --> P7

 style P1 fill:#4CAF50,color:#fff
 style P3 fill:#2196F3,color:#fff
 style P7 fill:#f44336,color:#fff
```

---

## P1: Ingreso y Contratación

| Campo | Valor |
| ------------ | ------------------------- |
| **ID** | `BPMN-GN-RRHH-INGRESO-01` |
| **Sistemas** | SIGPER, SIAPER |

### Diagrama de Flujo

```mermaid
flowchart TD
 subgraph RECLUTAMIENTO["📋 Reclutamiento"]
 A["Identificar vacante"]
 B["Elaborar perfil; de cargo"]
 C["Publicar llamado:; • Empleo Público; • GORE web"]
 D["Recepción de; postulaciones"]
 end

 subgraph SELECCION["🔍 Selección"]
 E["Filtro curricular"]
 F["Evaluación técnica/; psicológica"]
 G["Entrevista Comisión"]
 H["Propuesta de; terna"]
 I["Gobernador/a; decide"]
 end

 subgraph CONTRATACION["✍️ Contratación"]
 J["Oferta formal"]
 K["Aceptación candidato"]
 L["Resolución de; nombramiento"]
 M["Alta en SIGPER; y SIAPER"]
 N["Firma contrato/; decreto"]
 end

 A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M --> N

 style N fill:#4CAF50,color:#fff
```

### Tipos de Contrato

| Tipo | Descripción |
| -------------- | ------------------------------------------ |
| **Planta** | Cargo titular, carrera funcionaria |
| **Contrata** | Transitorio, renovación anual |
| **Honorarios** | Servicios específicos, sin vínculo laboral |

---

## P2: Inducción e Integración

| Campo | Valor |
| --------- | --------------------------- |
| **ID** | `BPMN-GN-RRHH-INDUCCION-01` |
| **Fases** | 11 |

### Diagrama de Flujo

```mermaid
flowchart TD
 A["Alta del; funcionario"] --> B["Bienvenida; institucional"]
 B --> C["Entrega de; credencial y accesos"]
 C --> D["Presentación en; división/área"]
 D --> E["Asignar mentor/; agente inductor"]
 E --> F["Recorrido; instalaciones"]
 F --> G["Capacitación:; • Misión/visión; • Organigrama; • Sistemas; • Normativa"]
 G --> H["Entrega de; documentos clave"]
 H --> I["Configuración; puesto trabajo"]
 I --> J["Seguimiento; 30-60-90 días"]
 J --> K["Evaluación; período prueba"]

 style K fill:#4CAF50,color:#fff
```

---

## P3: Remuneraciones y Compensaciones

| Campo | Valor |
| ------------ | -------------------------------- |
| **ID** | `BPMN-GN-RRHH-REMUNERACIONES-01` |
| **Sistemas** | SIGPER, PREVIRED, SIGFE |
| **Base** | Escala Única de Sueldos (EUS) |

### Diagrama de Flujo Mensual

```mermaid
flowchart TD
 A["Inicio mes"] --> B["Recopilar novedades:; • Licencias; • Horas extra; • Descuentos"]
 B --> C["Calcular remuneración; bruta"]
 C --> D["Aplicar descuentos:; • Previsión; • Salud; • Impuestos; • Otros"]
 D --> E["Generar liquidación"]
 E --> F["Revisión y; validación"]
 F --> G["Autorización; pago"]
 G --> H["Pagar PREVIRED; (cotizaciones)"]
 H --> I["Transferir a; cuentas funcionarios"]
 I --> J["Contabilizar; en SIGFE"]
 J --> K["Archivar; liquidaciones"]

 style I fill:#4CAF50,color:#fff
```

### Componentes de la Remuneración

| Componente | Descripción |
| ---------------- | ----------------------------- |
| **Sueldo base** | Según grado EUS |
| **Asignaciones** | Zona, antigüedad, profesional |
| **Bonos** | PMG, productividad, otros |
| **Horas extra** | Según normativa |

---

## P4: Tiempo, Asistencia y Ausentismo

| Campo | Valor |
| ------ | ----------------------------------- |
| **ID** | `BPMN-GN-RRHH-TIEMPO-AUSENTISMO-01` |

### Diagrama de Flujo

```mermaid
flowchart TD
 subgraph REGISTRO["📋 Registro"]
 A["Funcionario marca; entrada/salida"]
 B["Sistema registra; en reloj control"]
 C["Generar reporte; diario"]
 end

 subgraph PERMISOS["📝 Permisos"]
 D["Solicitar permiso:; • Administrativo; • Particular"]
 E["Jefatura aprueba/; rechaza"]
 F["Registrar en; sistema"]
 end

 subgraph LICENCIAS["🏥 Licencias"]
 G["Funcionario presenta; licencia médica"]
 H["RRHH recepciona; y valida"]
 I["Enviar a Isapre/; COMPIN"]
 J["Resolución:; • Aprobada; • Rechazada"]
 K["Ajustar; remuneración"]
 end

 subgraph FERIADOS["🌴 Feriados"]
 L["Solicitar feriado; legal/progresivo"]
 M["Verificar saldo; disponible"]
 N["Jefatura autoriza"]
 O["Descontar días"]
 end

 A --> B --> C
 D --> E --> F
 G --> H --> I --> J --> K
 L --> M --> N --> O

 style K fill:#FF9800,color:#fff
```

---

## P5: Desarrollo Organizacional y Capacitación

| Campo | Valor |
| ------ | -------------------------------- |
| **ID** | `BPMN-GN-RRHH-DESARROLLO-ORG-01` |

### Diagrama de Flujo

```mermaid
flowchart TD
 subgraph DNC["📊 Detección de Necesidades"]
 A["Aplicar encuesta DNC"]
 B["Análisis de brechas"]
 C["Priorizar necesidades"]
 end

 subgraph PAC_CAP["📋 Plan de Capacitación"]
 D["Elaborar PAC anual"]
 E["Comité Bipartito; aprueba"]
 F["Asignar presupuesto"]
 end

 subgraph EJECUCION["🎓 Ejecución"]
 G["Convocar a; funcionarios"]
 H["Ejecutar; capacitaciones"]
 I["Evaluar aprendizaje"]
 J["Certificar"]
 end

 subgraph SEGUIMIENTO["📈 Seguimiento"]
 K["Medir transferencia; al puesto"]
 L["Evaluar impacto"]
 M["Retroalimentar; próximo ciclo"]
 end

 A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M

 style J fill:#4CAF50,color:#fff
```

### Calificaciones

```mermaid
flowchart TD
 A["Período calificatorio; (sep-ago)"] --> B["Precalificación; por jefatura"]
 B --> C["Notificación a; funcionario"]
 C --> D{"¿Apelación?"}
 D -->|"No"| E["Junta Calificadora; define nota final"]
 D -->|"Sí"| F["Junta resuelve; apelación"]
 F --> E
 E --> G["Listas:; 1-2-3-4 o Eliminación"]
 G --> H["Registrar en; hoja de vida"]

 style G fill:#9C27B0,color:#fff
```

---

## P6: Bienestar y Calidad de Vida

| Campo | Valor |
| ------ | --------------------------- |
| **ID** | `BPMN-GN-RRHH-BIENESTAR-01` |

### Diagrama de Flujo

```mermaid
flowchart TD
 subgraph AFILIACION["📋 Afiliación"]
 A["Funcionario ingresa"]
 B["Invitar a; Servicio de Bienestar"]
 C["Aceptar y afiliar"]
 D["Descuento mensual; por planilla"]
 end

 subgraph PRESTACIONES["🎁 Prestaciones"]
 E["Solicitar beneficio:; • Médico; • Económico; • Préstamo; • Convenio"]
 F["Unidad Bienestar; evalúa"]
 G["Consejo Administrativo; aprueba si requiere"]
 H["Otorgar beneficio"]
 end

 subgraph ACTIVIDADES["🎉 Actividades"]
 I["Planificar eventos:; • Deportivos; • Recreativos; • Culturales"]
 J["Ejecutar actividad"]
 K["Evaluar satisfacción"]
 end

 A --> B --> C --> D
 E --> F --> G --> H
 I --> J --> K

 style H fill:#4CAF50,color:#fff
```

### Prevención de Riesgos

```mermaid
flowchart TD
 A["Identificar riesgos; laborales"] --> B["Elaborar matriz; de riesgos"]
 B --> C["Medidas preventivas"]
 C --> D["CPHS monitorea"]
 D --> E{"¿Accidente?"}
 E -->|"Sí"| F["DIAT/DIEP"]
 E -->|"No"| G["Seguir monitoreando"]
 F --> H["Mutual investiga"]
 H --> I["Medidas correctivas"]

 style F fill:#f44336,color:#fff
```

---
