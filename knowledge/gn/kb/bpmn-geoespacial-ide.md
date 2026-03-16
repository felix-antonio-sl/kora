---
_manifest:
  urn: "urn:gn:kb:bpmn-geoespacial-ide"
  provenance:
    created_by: "FS"
    created_at: "2026-03-15"
    source: "BPMN D10 Gestión Información Geoespacial IDE/Geonodo GORE Ñuble"
version: "1.0.0"
status: published
tags: [geoespacial, ide, geonodo, sig, gore-nuble, interoperabilidad]
lang: es
extensions:
  gn:
    family: guide
---

# Gestión de Información Geoespacial (IDE/Geonodo) — GORE Ñuble

## Visión General

El dominio de Gestión de Información Geoespacial articula la Infraestructura de Datos Espaciales (IDE) y el Geonodo del Gobierno Regional de Ñuble. Tiene criticidad media, es liderado por el Coordinador Regional IDE y se estructura en 3 procesos con aproximadamente 10 subprocesos.

Los tres procesos cubren el ciclo completo de la información geoespacial institucional:

- **P1 — Ciclo de Vida de Datos Geoespaciales**: planificación, captura, calidad, documentación, publicación y evaluación de uso.
- **P2 — Publicación e Interoperabilidad**: servicios OGC (WMS/WFS/WCS), API REST institucional y Geoportal público.
- **P3 — Gobernanza de Datos Geoespaciales**: estructura de roles, trazabilidad, versionamiento y licenciamiento.

## Marco Estratégico

| Aspecto | Alineamiento |
|---|---|
| ERD Ñuble | Gestión territorial informada |
| PROT Ñuble | Plan Regional de Ordenamiento Territorial; vinculante (Art. 17 LOC) |
| IDE Chile | Interoperabilidad nacional |
| ISO/TC 211 | Estándares geoespaciales |
| OGC | Servicios web abiertos |

## Mapa de Procesos

```mermaid
flowchart LR
    subgraph CICLO["Ciclo de Datos Geoespaciales"]
        P1["P1: Ciclo de Vida<br/>de Datos"]
        P2["P2: Publicacion e<br/>Interoperabilidad"]
        P3["P3: Gobernanza<br/>de Datos"]
    end

    subgraph INFRAESTRUCTURA["Infraestructura"]
        I1["Geonodo"]
        I2["Servicios OGC"]
        I3["Geoportal"]
        I4["API"]
    end

    P1 --> P2 --> P3
    P2 <--> I1 & I2 & I3 & I4

    style P1 fill:#2196F3,color:#fff
    style P2 fill:#4CAF50,color:#fff
    style P3 fill:#9C27B0,color:#fff
```

## Ciclo de Vida de Datos Geoespaciales

El proceso P1 estructura el flujo completo de datos geoespaciales en 6 fases secuenciales con retroalimentación de mejora continua.

### Diagrama de Flujo

```mermaid
flowchart TD
    subgraph PLANIFICAR["1. Planificar"]
        A["Definir necesidades<br/>(UN-IGIF)"]
        B["Especificaciones<br/>(ISO 19131)"]
        C["Catalogo objetos<br/>(ISO 19110)"]
    end

    subgraph CAPTURAR["2. Capturar/Integrar"]
        D["Formularios/<br/>recolectores"]
        E["ETL desde fuentes"]
        F["Control de versiones"]
    end

    subgraph CALIDAD["3. Calidad"]
        G["QA/QC<br/>(ISO 19157)"]
        H["Validaciones<br/>automatizadas"]
    end

    subgraph DOCUMENTAR["4. Documentar"]
        I["Metadatos<br/>(ISO 19115-1)"]
        J["URL descarga/<br/>servicios"]
        K["Licencias"]
    end

    subgraph PUBLICAR["5. Publicar"]
        L["WMS/WFS/WCS"]
        M["API endpoints"]
        N["Geoportal"]
        O["Registro CSW"]
    end

    subgraph USAR["6. Usar y Evaluar"]
        P["Tableros/<br/>dashboards"]
        Q["Indicadores<br/>uso/impacto"]
        R["Retroalimentacion"]
    end

    A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M --> N --> O --> P --> Q --> R
    R -.->|"Mejora continua"| A

    style N fill:#4CAF50,color:#fff
```

### Responsables por Etapa

| Etapa | Responsable |
|---|---|
| Planificar | Coord. Regional IDE |
| Capturar/Calidad | UGIT / Equipo SIG |
| Documentar/Publicar | UGIT / Equipo SIG |
| Usar y Evaluar | Divisiones usuarias |

## Publicación e Interoperabilidad

El proceso P2 expone los datos geoespaciales procesados a través de servicios estandarizados OGC, una API REST institucional y un Geoportal público.

### Servicios OGC

```mermaid
flowchart LR
    subgraph CAPAS["Datos Procesados"]
        A["Capa tematica"]
    end

    subgraph SERVICIOS["Servicios OGC"]
        B["WMS<br/>(visualizacion)"]
        C["WFS<br/>(entidades)"]
        D["WCS<br/>(coberturas)"]
    end

    subgraph FORMATOS["Formatos"]
        E["GeoJSON"]
        F["GML"]
        G["KML"]
        H["Shapefile"]
    end

    A --> B & C & D
    C --> E & F & G & H

    style B fill:#2196F3,color:#fff
    style C fill:#4CAF50,color:#fff
```

### API Institucional

```mermaid
flowchart TD
    A["Cliente externo"] --> B{"Endpoint"}
    B -->|"/datasets"| C["Listar conjuntos"]
    B -->|"/datasets/{id}"| D["Detalle conjunto"]
    B -->|"/tiles/{z}/{x}/{y}"| E["Teselas"]
    B -->|"/search"| F["Busqueda avanzada"]
    C & D & E & F --> G["Respuesta JSON"]

    style G fill:#4CAF50,color:#fff
```

### Geoportal

| Funcionalidad | Descripción |
|---|---|
| Búsqueda | Por tema, palabra clave, ubicación |
| Previsualización | Visor WMS integrado |
| Descarga | Múltiples formatos |
| Tutoriales | Guías por perfil de usuario |

## Gobernanza de Datos Geoespaciales

El proceso P3 define la estructura de roles, los mecanismos de trazabilidad y el régimen de licenciamiento de las capas geoespaciales institucionales.

### Roles de Gobernanza

```mermaid
flowchart TD
    subgraph COMITE["Comite Geo Institucional"]
        A["Gobernador/a<br/>(Patrocinio)"]
    end

    subgraph OPERATIVO["Nivel Operativo"]
        B["Coord. Regional IDE<br/>(Liderazgo)"]
        C["UGIT / Equipo SIG<br/>(Operacion tecnica)"]
        D["Puntos Focales<br/>Sectoriales"]
    end

    subgraph SOPORTE["Soporte"]
        E["Juridica<br/>(Licencias)"]
        F["TI<br/>(Infraestructura)"]
        G["Comunicaciones<br/>(Difusion)"]
    end

    A --> B --> C & D
    B --> E & F & G

    style B fill:#4CAF50,color:#fff
```

### Trazabilidad y Versionamiento

El flujo de trazabilidad opera en cuatro pasos: un cambio en una capa geoespacial genera un commit en el repositorio GitHub institucional, se actualiza la versión en los metadatos asociados y se notifica a los consumidores afectados.

```mermaid
flowchart LR
    A["Cambio en capa"] --> B["Commit en<br/>GitHub institucional"]
    B --> C["Actualizar version<br/>en metadatos"]
    C --> D["Notificar<br/>consumidores"]

    style D fill:#FF9800,color:#fff
```

### Licenciamiento

| Tipo de Capa | Licencia Recomendada |
|---|---|
| Datos abiertos | CC BY 4.0 |
| Bases de datos | ODbL |
| Datos restringidos | Acuerdo específico |

## Ética de Datos Geoespaciales

| Principio | Aplicación |
|---|---|
| Minimización | Evitar granularidad innecesaria |
| Anonimización | Cuando corresponda |
| Transparencia | Declarar origen y licencias |
| No estigmatización | Evitar visualizaciones dañinas |
| Calidad | Tratarla como deber público |

## Plan de Implementación

Plan de despliegue en 180 días, organizado en 4 fases progresivas desde la constitución del Comité Geo hasta la evaluación de KPIs y capacitación.

```mermaid
gantt
    title Plan IDE GORE Nuble
    dateFormat  YYYY-MM-DD
    section Fase 0 (0-30)
    Comite Geo constituido           :a1, 2025-01-15, 15d
    Inventario y diagnostico         :a2, 2025-01-20, 15d
    section Fase 1 (30-90)
    Politica y guia metadatos        :b1, 2025-02-01, 30d
    Geonodo operativo                :b2, 2025-02-15, 30d
    Piloto 5 conjuntos               :b3, 2025-03-01, 30d
    section Fase 2 (90-150)
    Geoportal y API                  :c1, 2025-04-01, 30d
    Integracion servicios externos   :c2, 2025-04-15, 30d
    section Fase 3 (150-180)
    Evaluacion KPIs                  :d1, 2025-05-15, 15d
    Capacitacion y plan anual        :d2, 2025-05-25, 15d
```

## Normativa Aplicable

| Norma | Alcance |
|---|---|
| ISO 19115-1 | Metadatos |
| ISO 19157 | Calidad de datos |
| ISO 19131 | Especificaciones |
| Política IDE Chile | Interoperabilidad nacional |
| Ley 21.455 | Cambio climático (datos) |

## Sistemas de Información

| Sistema | Función |
|---|---|
| Geonodo | Plataforma geoespacial |
| CSW | Catálogo de metadatos |
| Servicios OGC | WMS/WFS/WCS |
| Geoportal | Portal público |
| API Geoespacial | API REST |
| GitHub Institucional | Versionamiento |
