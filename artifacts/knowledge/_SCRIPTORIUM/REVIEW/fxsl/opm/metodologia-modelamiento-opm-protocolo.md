---
_manifest:
  urn: "urn:fxsl:kb:metodologia-modelamiento-opm-protocolo"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "synthesis:metodologia-modelamiento-opm,opm-iso-19450,opm-opl-es,opcloud-tutorial-videos"
version: "0.1.0"
status: draft
tags: [opm, methodology, protocol, modeling-workflow, heuristics, validation]
lang: es
extensions:
  kora:
    family: specification
    depends_on:
      - "urn:fxsl:kb:opm-corpus-architecture"
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:opm-opl-es"
      - "urn:fxsl:kb:opcloud-tutorial-videos"
---

# Metodologia de Modelamiento OPM - Protocolo

## Definicion

Este artefacto define el protocolo de trabajo para modelar con OPM sin duplicar la semantica base del lenguaje. La semantica formal vive en [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450). La realizacion en espanol vive en [OPL-ES](urn:fxsl:kb:opm-opl-es). Los pasos de herramienta viven en [OPCloud Tutorial Videos](urn:fxsl:kb:opcloud-tutorial-videos).

## Boundary

Este protocolo SI cubre:

- Orden de decisiones de modelamiento
- Clasificacion del sistema
- Construccion progresiva de SD y SD1+
- Reglas de seleccion entre in-zooming y unfolding
- Heuristicas y anti-patterns
- Gates de validacion antes de publicar

Este protocolo NO cubre:

- Taxonomias completas de links
- EBNF y gramatica OPL
- UI detallada de OPCloud
- Tutoriales largos o worked examples extensos

## Regla de Precedencia Operativa

| Si la duda es sobre... | Ir a... |
|------------------------|---------|
| Semantica OPM, notacion, dinamica, naming EN | [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450) |
| Surface form, gramatica y roundtrip EN -> ES | [OPL-ES](urn:fxsl:kb:opm-opl-es) |
| Wizard, settings, hierarchy, simulation, requirements en OPCloud | [OPCloud Tutorial Videos](urn:fxsl:kb:opcloud-tutorial-videos) |
| Secuencia de decisiones y quality gates | Este artefacto |

## Workflow

### Fase 1 - Clasificar

1. Determinar tipo de sistema: artificial, natural, social o socio-tecnico.
2. Fijar idioma del modelo: EN o ES.
3. Resolver si el trabajo es conceptual puro o implementacion en OPCloud.

### Fase 2 - Construir SD

1. Definir proceso principal.
2. Definir beneficiario y atributo del beneficiario.
3. Definir input/output states.
4. Definir agente(s), instrumentos, environment y problem occurrence cuando aplique.

Regla de idioma:

- EN: naming conforme a ISO 19450.
- ES: naming conforme a OPL-ES.

### Fase 3 - Refinar

| Situacion | Mecanismo |
|----------|-----------|
| Subprocesos con orden fijo | In-zooming |
| Variantes o tipos independientes | Unfolding |
| Exceso de detalle en un OPD | Crear descendiente |
| Estado irrelevante en nivel alto | State suppression |
| Vista transversal puntual | View creation |

### Fase 4 - Optimizar Modelo

Aplicar estas heuristicas solo cuando reduzcan grasa sin perder FS:

- Proceso state-preserving -> tagged structural link
- Objeto transiente no observado -> invocation link
- Objeto implicito en texto -> explicitar
- Sinonimos/homonimos -> resolver a nombre canonico
- Generalizacion en SD cuando los especificos saturan el top-level

### Fase 5 - Validar

Antes de publicar, verificar:

1. Unicidad de rol del artefacto dentro del corpus
2. Naming coherente con idioma del modelo
3. Sin duplicacion innecesaria de taxonomias ya presentes en ISO u OPL-ES
4. Sin mezcla de semantica base con features de herramienta
5. Gate operacional superado

## Anti-Patterns

| Anti-pattern | Correccion |
|-------------|------------|
| Reescribir la ISO completa en la metodologia | Reemplazar por criterio de decision + referencia |
| Poner wizard/UI dentro de una spec metodologica | Extraer a guia de herramienta |
| Mezclar EN y ES sin politica de idioma | Fijar idioma del modelo y aplicar la autoridad correspondiente |
| Mantener procesos que no transforman nada | Convertir a relacion estructural o revisar el modelo |
| Saturar SD con detalle de bajo nivel | Generalizar o refinar a SD1 |

## Gate Operacional

| Gate | Pregunta |
|------|----------|
| G1 | El SD es comprensible para stakeholders no tecnicos |
| G2 | El mecanismo de refinamiento elegido corresponde al tipo de relacion |
| G3 | Cada simplificacion conserva hechos y no solo cosmetica |
| G4 | La autoridad de cada regla usada es rastreable |
| G5 | El artefacto no invade el rol de otro documento del corpus |

## Contenido a Derivar

Cuando el protocolo detecta contenido tool-specific o pedagogico, DEBE derivarlo:

- OPCloud -> [OPM OPCloud Operational Guide](urn:fxsl:kb:opm-opcloud-operational-guide)
- Ejemplo y companion de OPL-ES -> [OPM OPL-ES Practical Companion](urn:fxsl:kb:opm-opl-es-practical-companion)
