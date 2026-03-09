---
_manifest:
  urn: "urn:knowledge:kora:core:specs:user-stories:1.0.0"
  provenance:
    created_by: "gemini-cli"
    created_at: "2026-03-09"
    source: "Deduplication and consolidation of 543 reverse-engineered stories from OPCloud"
status: final
project: kora
type: requirements-document
---

# 📋 Historias de Usuario Consolidadas y Deduplicadas — Kora Modeler

Este documento presenta el backlog consolidado de capacidades del sistema, eliminando las duplicaciones por redundancia de interfaz (mismas acciones desde diferentes botones) y enfocándose en la **capacidad semántica y funcional**.

---

## EP-01 — Gestión de Entidades (Things) y Ontología Core

### HU-0101 — Creación y Naming Bimodal
Como modelador, quiero crear entes (objetos y procesos) con sincronización bimodal instantánea, para que el nombre se actualice en el OPD (diagrama), OPL (lenguaje) y árbol jerárquico simultáneamente.
**Criterio de Aceptación:** 
- Soportar auto-formato de capitalización (configurable).
- Validar nombres únicos según el tipo de ente.
- Permitir la edición desde cualquier representación (canvas, texto o árbol).

### HU-0102 — Clasificación de Esencia y Afiliación
Como modelador, quiero definir la esencia (físico/informático) y afiliación (sistémico/ambiental) de un ente, para que su representación visual y gramática OPL cambien según las reglas ISO 19450.
**Criterio de Aceptación:**
- Objetos físicos muestran sombra; informáticos son planos.
- Entes ambientales usan contorno discontinuo (dashed).

---

## EP-02 — Ciclo de Vida y Estados de Objeto

### HU-0201 — Definición de Máquina de Estados
Como modelador, quiero asignar estados a un objeto, para modelar su comportamiento dinámico.
**Criterio de Aceptación:**
- Soportar marcadores: Inicial (bold), Final (doble), Default (flecha) y Actual (resaltado).
- Permitir estados que sean iniciales y finales simultáneamente.

### HU-0202 — Supresión Visual de Estados
Como modelador, quiero ocultar los estados no conectados de un objeto, para reducir el ruido visual sin eliminar la lógica del modelo.
**Criterio de Aceptación:**
- Mostrar indicador de elipsis (...) con el conteo de estados suprimidos.
- Permitir la expresión (mostrar) mediante doble clic.

---

## EP-03 — Enlaces Procedurales y Lógica de Transformación

### HU-0301 — Motor de Enlaces Inteligente (Smart Link Table)
Como modelador, quiero que al conectar dos entes, el sistema proponga solo los enlaces válidos según su esencia y tipo.
**Criterio de Aceptación:**
- Filtrar enlaces de Agente solo para objetos físicos.
- Soportar variantes: Consumo, Resultado, Efecto e Instrumento.
- Incluir modificadores de Condición (c), Evento (e) y Negación (NOT).

### HU-0302 — Lógica de Grupos y Multiplicidad
Como modelador, quiero definir la cardinalidad y lógica booleana de las relaciones.
**Criterio de Aceptación:**
- Crear arcos XOR (exactamente uno) y OR (al menos uno) entre enlaces.
- Definir multiplicidad mediante valores fijos, rangos (n..m) o variables paramétricas.
- Asignar probabilidades de ruta y etiquetas de camino (paths).

---

## EP-04 — Refinamiento y Jerarquía (Zooming)

### HU-0401 — In-zooming y Línea de Tiempo
Como modelador, quiero refinar un proceso creando un OPD descendiente, para detallar sus subprocesos con orden temporal.
**Criterio de Aceptación:**
- Orden vertical implica secuencia; horizontal implica paralelo.
- Heredar automáticamente el contexto del diagrama padre.

### HU-0402 — Abstracción Visual (Semi-fold)
Como modelador, quiero ver los componentes internos de un ente refinado de forma compacta en el diagrama padre.
**Criterio de Aceptación:**
- Permitir extraer/reinsertar componentes del semi-fold mediante interacción directa.
- Sincronizar enlaces desde/hacia componentes internos.

---

## EP-05 — Integraciones y Simulación Computacional

### HU-0501 — Orquestación de Protocolos (ROS/MQTT/Python)
Como modelador, quiero asociar lógica computacional a los procesos mediante funciones de usuario o protocolos industriales.
**Criterio de Aceptación:**
- Configurar nodos ROS (Publish/Subscribe) y brokers MQTT.
- Escribir scripts personalizados en un IDE integrado con acceso a los alias de los objetos.

### HU-0502 — Ejecución y Validación de Rangos
Como modelador, quiero ejecutar el modelo para validar que los valores de los objetos se mantienen dentro de los rangos definidos.
**Criterio de Aceptación:**
- Definir rangos matemáticos [min, max].
- Feedback visual de validación: Verde (dentro), Rojo (fuera), Azul (definido sin valor).

---

## EP-06 — Colaboración y Gestión de Conocimiento

### HU-0601 — Arquitectura de Sub-modelos
Como modelador, quiero conectar modelos independientes como subsistemas, para permitir el trabajo en paralelo de múltiples equipos.
**Criterio de Aceptación:**
- Definir entes compartidos (transparentes) como contrato de interfaz.
- Sincronización asíncrona entre el modelo principal y los sub-modelos.

### HU-0602 — Ontología Organizacional y Estereotipos
Como administrador, quiero definir una terminología obligatoria y plantillas de entes (estereotipos).
**Criterio de Aceptación:**
- Validar nombres contra el diccionario organizacional (Sugerir/Forzar).
- Aplicar estereotipos que inyectan atributos y estados predefinidos.

---

## EP-07 — Herramientas de Análisis y Auditoría

### HU-0701 — Validación Semántica y Linter
Como modelador, quiero que el sistema audite el modelo contra las reglas ISO 19450 y convenciones de nombrado.
**Criterio de Aceptación:**
- Detectar procesos sin efecto, objetos huérfanos o violaciones de herencia.

### HU-0702 — Generación de Requisitos e IA
Como modelador, quiero generar requisitos técnicos automáticamente a partir de la lógica del modelo.
**Criterio de Aceptación:**
- Exportar matriz de trazabilidad y requisitos a Excel/PDF.
- Usar ML/IA para identificar conocimiento faltante (enlaces probables omitidos).

---

## EP-08 — Administración, Versiones y Exportación

### HU-0801 — Control de Versiones y Historial
Como modelador, quiero gestionar el historial de cambios del modelo, para recuperar estados previos o comparar evoluciones.
**Criterio de Aceptación:**
- Auto-guardado inteligente y creación de versiones manuales.
- Comparación semántica de diferencias entre versiones.

### HU-0802 — Exportación Multiformato
Como modelador, quiero generar entregables profesionales del modelo.
**Criterio de Aceptación:**
- Generar PDF con tabla de contenidos, diccionario de elementos y OPL.
- Exportar diagramas en alta resolución (SVG/PNG) y metadatos en JSON/YAML.
