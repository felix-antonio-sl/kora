---
_manifest:
  urn: urn:gn:kb:bpmn-d07-rrhh
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D07_rrhh_koda.yml
version: 2.0.0
status: published
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
    cr: 1.04
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
---

# BPMN D07: Gestión de Personas (RRHH)

## Metadatos Dominio

### Criticidad
🟠 Alta

### Dueno
Área de Gestión de Personas

### Procesos
7

### Subprocesos
~20

## Body MD
\# D07: Gestión de Personas (RRHH)
\## Metadatos del Dominio
| Campo           | Valor                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ID**          | `DOM-RRHH`                                                                                                                                             |
| **Criticidad**  | 🟠 Alta                                                                                                                                                 |
| **Dueño**       | Área de Gestión de Personas                                                                                                                            |
| **Procesos**    | 7                                                                                                                                                      |
| **Subprocesos** | ~20                                                                                                                                                    |
| **Ref. Fuente** | [kb_gn_054_bpmn_c4_koda.yml](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml) L.1410-1880 |
---
\## Mapa General del Dominio
```mermaid
flowchart LR
    subgraph CICLO_VIDA["👤 Ciclo de Vida del Funcionario"]
        P1["P1: Ingreso y<br/>Contratación"]
        P2["P2: Inducción"]
        P3["P3: Remuneraciones"]
        P4["P4: Tiempo y<br/>Ausentismo"]
        P5["P5: Desarrollo y<br/>Capacitación"]
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
\## P1: Ingreso y Contratación
| Campo        | Valor                     |
| ------------ | ------------------------- |
| **ID**       | `BPMN-GN-RRHH-INGRESO-01` |
| **Sistemas** | SIGPER, SIAPER            |
\### Diagrama de Flujo
```mermaid
flowchart TD
    subgraph RECLUTAMIENTO["📋 Reclutamiento"]
        A["Identificar vacante"]
        B["Elaborar perfil<br/>de cargo"]
        C["Publicar llamado:<br/>• Empleo Público<br/>• GORE web"]
        D["Recepción de<br/>postulaciones"]
    end
    subgraph SELECCION["🔍 Selección"]
        E["Filtro curricular"]
        F["Evaluación técnica/<br/>psicológica"]
        G["Entrevista Comisión"]
        H["Propuesta de<br/>terna"]
        I["Gobernador/a<br/>decide"]
    end
    subgraph CONTRATACION["✍️ Contratación"]
        J["Oferta formal"]
        K["Aceptación candidato"]
        L["Resolución de<br/>nombramiento"]
        M["Alta en SIGPER<br/>y SIAPER"]
        N["Firma contrato/<br/>decreto"]
    end
    A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M --> N
    style N fill:#4CAF50,color:#fff
```
\### Tipos de Contrato
| Tipo           | Descripción                                |
| -------------- | ------------------------------------------ |
| **Planta**     | Cargo titular, carrera funcionaria         |
| **Contrata**   | Transitorio, renovación anual              |
| **Honorarios** | Servicios específicos, sin vínculo laboral |
---
\## P2: Inducción e Integración
| Campo     | Valor                       |
| --------- | --------------------------- |
| **ID**    | `BPMN-GN-RRHH-INDUCCION-01` |
| **Fases** | 11                          |
\### Diagrama de Flujo
```mermaid
flowchart TD
    A["Alta del<br/>funcionario"] --> B["Bienvenida<br/>institucional"]
    B --> C["Entrega de<br/>credencial y accesos"]
    C --> D["Presentación en<br/>división/área"]
    D --> E["Asignar mentor/<br/>agente inductor"]
    E --> F["Recorrido<br/>instalaciones"]
    F --> G["Capacitación:<br/>• Misión/visión<br/>• Organigrama<br/>• Sistemas<br/>• Normativa"]
    G --> H["Entrega de<br/>documentos clave"]
    H --> I["Configuración<br/>puesto trabajo"]
    I --> J["Seguimiento<br/>30-60-90 días"]
    J --> K["Evaluación<br/>período prueba"]
    style K fill:#4CAF50,color:#fff
```
---
\## P3: Remuneraciones y Compensaciones
| Campo        | Valor                            |
| ------------ | -------------------------------- |
| **ID**       | `BPMN-GN-RRHH-REMUNERACIONES-01` |
| **Sistemas** | SIGPER, PREVIRED, SIGFE          |
| **Base**     | Escala Única de Sueldos (EUS)    |
\### Diagrama de Flujo Mensual
```mermaid
flowchart TD
    A["Inicio mes"] --> B["Recopilar novedades:<br/>• Licencias<br/>• Horas extra<br/>• Descuentos"]
    B --> C["Calcular remuneración<br/>bruta"]
    C --> D["Aplicar descuentos:<br/>• Previsión<br/>• Salud<br/>• Impuestos<br/>• Otros"]
    D --> E["Generar liquidación"]
    E --> F["Revisión y<br/>validación"]
    F --> G["Autorización<br/>pago"]
    G --> H["Pagar PREVIRED<br/>(cotizaciones)"]
    H --> I["Transferir a<br/>cuentas funcionarios"]
    I --> J["Contabilizar<br/>en SIGFE"]
    J --> K["Archivar<br/>liquidaciones"]
    style I fill:#4CAF50,color:#fff
```
\### Componentes de la Remuneración
| Componente       | Descripción                   |
| ---------------- | ----------------------------- |
| **Sueldo base**  | Según grado EUS               |
| **Asignaciones** | Zona, antigüedad, profesional |
| **Bonos**        | PMG, productividad, otros     |
| **Horas extra**  | Según normativa               |
---
\## P4: Tiempo, Asistencia y Ausentismo
| Campo  | Valor                               |
| ------ | ----------------------------------- |
| **ID** | `BPMN-GN-RRHH-TIEMPO-AUSENTISMO-01` |
\### Diagrama de Flujo
```mermaid
flowchart TD
    subgraph REGISTRO["📋 Registro"]
        A["Funcionario marca<br/>entrada/salida"]
        B["Sistema registra<br/>en reloj control"]
        C["Generar reporte<br/>diario"]
    end
    subgraph PERMISOS["📝 Permisos"]
        D["Solicitar permiso:<br/>• Administrativo<br/>• Particular"]
        E["Jefatura aprueba/<br/>rechaza"]
        F["Registrar en<br/>sistema"]
    end
    subgraph LICENCIAS["🏥 Licencias"]
        G["Funcionario presenta<br/>licencia médica"]
        H["RRHH recepciona<br/>y valida"]
        I["Enviar a Isapre/<br/>COMPIN"]
        J["Resolución:<br/>• Aprobada<br/>• Rechazada"]
        K["Ajustar<br/>remuneración"]
    end
    subgraph FERIADOS["🌴 Feriados"]
        L["Solicitar feriado<br/>legal/progresivo"]
        M["Verificar saldo<br/>disponible"]
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
\## P5: Desarrollo Organizacional y Capacitación
| Campo  | Valor                            |
| ------ | -------------------------------- |
| **ID** | `BPMN-GN-RRHH-DESARROLLO-ORG-01` |
\### Diagrama de Flujo
```mermaid
flowchart TD
    subgraph DNC["📊 Detección de Necesidades"]
        A["Aplicar encuesta DNC"]
        B["Análisis de brechas"]
        C["Priorizar necesidades"]
    end
    subgraph PAC_CAP["📋 Plan de Capacitación"]
        D["Elaborar PAC anual"]
        E["Comité Bipartito<br/>aprueba"]
        F["Asignar presupuesto"]
    end
    subgraph EJECUCION["🎓 Ejecución"]
        G["Convocar a<br/>funcionarios"]
        H["Ejecutar<br/>capacitaciones"]
        I["Evaluar aprendizaje"]
        J["Certificar"]
    end
    subgraph SEGUIMIENTO["📈 Seguimiento"]
        K["Medir transferencia<br/>al puesto"]
        L["Evaluar impacto"]
        M["Retroalimentar<br/>próximo ciclo"]
    end
    A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M
    style J fill:#4CAF50,color:#fff
```
\### Calificaciones
```mermaid
flowchart TD
    A["Período calificatorio<br/>(sep-ago)"] --> B["Precalificación<br/>por jefatura"]
    B --> C["Notificación a<br/>funcionario"]
    C --> D{"¿Apelación?"}
    D -->|"No"| E["Junta Calificadora<br/>define nota final"]
    D -->|"Sí"| F["Junta resuelve<br/>apelación"]
    F --> E
    E --> G["Listas:<br/>1-2-3-4 o Eliminación"]
    G --> H["Registrar en<br/>hoja de vida"]
    style G fill:#9C27B0,color:#fff
```
---
\## P6: Bienestar y Calidad de Vida
| Campo  | Valor                       |
| ------ | --------------------------- |
| **ID** | `BPMN-GN-RRHH-BIENESTAR-01` |
\### Diagrama de Flujo
```mermaid
flowchart TD
    subgraph AFILIACION["📋 Afiliación"]
        A["Funcionario ingresa"]
        B["Invitar a<br/>Servicio de Bienestar"]
        C["Aceptar y afiliar"]
        D["Descuento mensual<br/>por planilla"]
    end
    subgraph PRESTACIONES["🎁 Prestaciones"]
        E["Solicitar beneficio:<br/>• Médico<br/>• Económico<br/>• Préstamo<br/>• Convenio"]
        F["Unidad Bienestar<br/>evalúa"]
        G["Consejo Administrativo<br/>aprueba si requiere"]
        H["Otorgar beneficio"]
    end
    subgraph ACTIVIDADES["🎉 Actividades"]
        I["Planificar eventos:<br/>• Deportivos<br/>• Recreativos<br/>• Culturales"]
        J["Ejecutar actividad"]
        K["Evaluar satisfacción"]
    end
    A --> B --> C --> D
    E --> F --> G --> H
    I --> J --> K
    style H fill:#4CAF50,color:#fff
```
\### Prevención de Riesgos
```mermaid
flowchart TD
    A["Identificar riesgos<br/>laborales"] --> B["Elaborar matriz<br/>de riesgos"]
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
\## P7: Egreso y Desvinculación
| Campo  | Valor                    |
| ------ | ------------------------ |
| **ID** | `BPMN-GN-RRHH-EGRESO-01` |
\### Causales de Egreso
```mermaid
flowchart TD
    A["Egreso de<br/>funcionario"] --> B{"Causal"}
    B -->|"Voluntario"| C["Renuncia<br/>voluntaria"]
    B -->|"Jubilación"| D["Retiro por<br/>pensión"]
    B -->|"Término contrata"| E["No renovación<br/>31/12"]
    B -->|"Calificación"| F["Eliminación<br/>por nota"]
    B -->|"Disciplinario"| G["Destitución"]
    B -->|"Salud"| H["Incompatibilidad<br/>de salud"]
    C & D & E & F & G & H --> I["Procedimiento<br/>de cierre"]
    style I fill:#607D8B,color:#fff
```
\### Procedimiento de Cierre
```mermaid
flowchart TD
    A["Resolución de<br/>cese"] --> B["Entrega de cargo"]
    B --> C["Devolución de:<br/>• Credencial<br/>• Equipos<br/>• Documentos"]
    C --> D["Cierre de accesos:<br/>• TI<br/>• Edificio"]
    D --> E["Certificado de<br/>servicios"]
    E --> F["Liquidación final:<br/>• Feriados pendientes<br/>• Bonos proporcionales"]
    F --> G["Baja en SIGPER<br/>y SIAPER"]
    style G fill:#f44336,color:#fff
```
---
\## Sistemas Involucrados
| Sistema        | Función                             |
| -------------- | ----------------------------------- |
| `SYS-SIGPER`   | Gestión de personas, remuneraciones |
| `SYS-SIAPER`   | Control personal Estado             |
| `SYS-PREVIRED` | Cotizaciones previsionales          |
| `SYS-SIGFE`    | Contabilización                     |
---
\## Normativa Aplicable
| Norma                  | Alcance                     |
| ---------------------- | --------------------------- |
| **Ley 18.834**         | Estatuto Administrativo     |
| **Ley 18.575**         | Bases Administración Estado |
| **Ley 20.880**         | Probidad, declaraciones     |
| **Código del Trabajo** | Honorarios                  |
---
\## Referencias Cruzadas
| Dominio Relacionado                                                                                                                              | Vínculo                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| [D02 Ciclo Presupuestario](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md)   | Subtítulo 21, Remuneraciones |
| [D01 Actos Administrativos](file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D01_actos_administrativos.md) | Resoluciones de nombramiento |
---
*Última actualización: 2025-12-16*
