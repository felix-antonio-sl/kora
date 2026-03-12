---
_manifest:
  urn: "urn:kora:kb:specs:modeler:1.0.0"
  provenance:
    created_by: "gemini-cli"
    created_at: "2026-03-09"
    source: "OPCloud Reverse Engineering Analysis + FXSL OPM Methodology"
status: draft
project: kora
type: technical-specification
---

# 📄 Especificación Técnica: Kora Modeler (v1.0)

**Estado:** Draft para Sprint 0  
**Referencia:** urn:kora:kb:specs:modeler:1.0.0  
**Filosofía:** "El modelo es el Grafo; el Diagrama y el Lenguaje son proyecciones".

---

## 1. Arquitectura Core: Desacoplamiento Semántico

A diferencia de las herramientas tradicionales, Kora Modeler separa la **capa de persistencia lógica (KODA Graph)** de la **capa de representación visual (Canvas)**.

*   **Lógica No-Geográfica:** El orden de ejecución de los procesos (secuencial/paralelo) NO depende de la posición vertical en el canvas. Se define mediante metadatos de "Precedencia" y "Dependencia" en el grafo.
*   **Motor Bimodal Activo:** El editor de texto OPL no es un visor; es un IDE. Cambios en el texto refactorizan el grafo y actualizan el OPD mediante algoritmos de auto-layout.

---

## 2. Requisitos Funcionales por Capacidad (Backlog Técnico)

### CAP-01: Entes y Ontología FXSL
*   **Identidad Única (URN):** Cada objeto y proceso posee un URN único. Un cambio de nombre en un OPD se propaga mediante referencia, no mediante búsqueda de texto.
*   **Esencia Estricta:** Implementar validación de tipos. Un proceso informático no puede consumir un objeto físico sin un "Transductor" intermedio (Proceso de Digitalización).

### CAP-02: Máquina de Estados Categórica
*   **Invariantes de Estado:** Los estados no son solo etiquetas; son nodos hijos del objeto. 
*   **Validación de Simulación:** Un objeto no puede saltar de un estado A a un estado C si no existe una trayectoria definida en el modelo.

### CAP-03: Smart Linker e Inferencia
*   **Asistente de Enlaces:** Basado en la esencia de los entes (KODA Ontology), el sistema prioriza el enlace más probable:
    *   `Humano` + `Proceso` ➔ Sugerir `Agent Link`.
    *   `Datos` + `Proceso` ➔ Sugerir `Instrument Link` o `Consumption`.
*   **Multiplicidad Paramétrica:** Soportar variables reactivas (ej: `n = count(Inputs)`).

### CAP-04: Requisitos como Ciudadanos de Primera Clase
*   **Objetos de Requisito:** Los requisitos se modelan como **Objetos Informáticos** con estados `{Pending, Met, Violated}`.
*   **Trazabilidad Nativa:** Un proceso "Satisface" un requisito mediante un enlace de *Exhibition*. Si el proceso no se ejecuta en la simulación, el estado del requisito cambia automáticamente a `Violated`.

---

## 3. Innovaciones Kora (Diferenciadores Técnicos)

### 3.1. Arquitectura de Subsistemas (Micro-Kernel)
*   **Contratos de Interfaz:** Los sub-modelos se conectan mediante "Puertos de Interfaz" (Things transparentes).
*   **Sincronización Git-based:** El modelo se guarda en archivos YAML/JSON estructurados, permitiendo `merge` y `diff` semántico entre múltiples modeladores.

### 3.2. IDE Bimodal (OPL-IDE)
*   **IntelliSense OPM:** Autocompletado en el panel OPL para nombres de entes existentes y tipos de enlaces válidos.
*   **Refactorización:** "Rename" en el texto actualiza todos los diagramas (OPDs) instantáneamente.

### 3.3. Simulación Proactiva (Monte Carlo)
*   **Análisis de Sensibilidad:** Ejecutar 1,000 simulaciones asíncronas para identificar cuellos de botella estadísticos en procesos XOR basados en probabilidades de ruta definidas en los enlaces.

---

## 4. Invariantes Técnicas (Definición de "Done")

1.  **Consistencia Bimodal:** Cualquier estado del grafo debe representarse sin pérdida de información tanto en OPL como en OPD.
2.  **Validación ISO 19450:** El sistema debe impedir visualmente enlaces prohibidos (ej: Agregación entre Objeto y Proceso).
3.  **Persistencia YAML:** El formato de guardado debe ser humano-legible y apto para control de versiones.

---

## 5. Roadmap de Implementación (Sprint 0 a 3)

| Fase | Objetivo | Entregable |
| :--- | :--- | :--- |
| **Sprint 0** | Core Engine | Grafo de conocimiento KODA con soporte para Objetos y Procesos. |
| **Sprint 1** | Bimodalidad Base | Render de OPD (Canvas) y Generador de OPL sincrónico. |
| **Sprint 2** | Smart Linking | Motor de inferencia de enlaces y validación de esencia. |
| **Sprint 3** | Simulación | Ejecución de tokens y cambio de estado de objetos. |
