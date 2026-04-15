---
_manifest:
  urn: urn:fxsl:kb:metodologia-modelamiento-opm-p04
  provenance:
    created_by: kora/curator
    created_at: '2026-03-25'
    source: synthesis:opm-iso-19450,opm-opl-es,opcloud-tutorial-videos,opm-applied-system-modeling,opm-canonical-example
version: 3.5.1
status: published
tags:
- opm
- methodology
- system-modeling
- sd-construction
- refinement
- complexity-management
- modeling-protocol
- patterns
- antipatterns
- control-flow
- error-handling
- quantitative
- simulation
- executable-modeling
- opcloud
lang: es
extensions:
  kora:
    family: specification
    depends_on:
    - urn:fxsl:kb:opm-iso-19450
    - urn:fxsl:kb:opl-es
    shard_index: 4
    shard_count: 4
    shard_root_urn: urn:fxsl:kb:metodologia-modelamiento-opm
---

# Metodologia de Modelamiento OPM — Protocolo de Modelamiento Conceptual de Sistemas - Parte 04

## 13 Requirements Modeling en OPCloud

En este corpus, el modelamiento de requirements se trata como una capacidad de OPCloud, no como una extension normativa independiente de OPM. Por lo tanto, las siguientes reglas aplican solo cuando el modelo se implementa en OPCloud.

### 13.1 Operaciones Disponibles

OPCloud permite agregar, remover y visualizar requirements sobre elementos, links o diagramas completos. Las relaciones recuperables en el tutorial son:

- Exhibition
- Characterization
- Aggregation Participation

### 13.2 Convencion de Trazabilidad

Cuando se use trazabilidad de requirements en OPCloud, el tagged structural link con tag **"satisfies"** DEBERIA usarse como convencion de trazabilidad entre artefacto y requirement.

**Correcto:** `Seat satisfies RQ1 Driver Seat.`

**Incorrecto:** Conectar requirements a artifacts via procedural links (los requirements no transforman ni habilitan procesos; la relacion es estructural).

### 13.3 Ejemplo Minimo

Ejemplo recuperable desde el tutorial:

- Door-Peephole: peephole como parte de door
- Restricciones dimensionales: 56-64 inches
- Componentes: lens + sleeves
- Componente opcional: peephole cover
- Funcion: one-way view for seeing visitors

### 13.4 Analisis de Gaps y Generacion Asistida

OPCloud ofrece capacidades auxiliares que el modelador PUEDE usar para detectar vacios y acelerar derivacion de requirements:

- **Identification of Missing Knowledge:** DEBERIA usarse como heuristica de deteccion de gaps, no como verdad del modelo. `Pistol` sirve para filtrado rapido; `RGCN`, cuando este disponible, ofrece mayor precision. El umbral de confianza DEBERIA ajustarse explicitamente antes de aceptar sugerencias.
- **AI Requirements Generation:** toma OPPL como insumo y genera texto de requirement, verification type, acceptance criteria y model triplets. La salida DEBE revisarse manualmente antes de integrarla al corpus o al modelo.
- **Version comparison:** el modelador DEBERIA comparar resultados del analisis entre versiones sucesivas para distinguir mejoras reales de ruido introducido por cambios de layout o renaming.

## 14 Simulacion y Ejecucion del Modelo

### 14.1 Depth-First OPD Tree Traversal para Ejecucion

La ejecucion animada del modelo OPM sigue un recorrido **depth-first** del OPD tree. Los tokens fluyen a lo largo de los links: al llegar a un proceso in-zoomed, el control se transfiere recursivamente al subproceso mas profundo (topmost del nivel mas bajo). El control retorna al nivel padre tras completar el ultimo subproceso.

Los tokens se visualizan como valores que se pasan entre objetos y procesos: consumed (eliminado del source), instrument (read-only, permanece), resultee (creado en destination). Tokens computacionales llevan valores numericos.

### 14.2 Transition Conceptual → Computational

El modelador DEBE reconocer el punto en el OPD tree donde la transicion de modelamiento conceptual puro a modelamiento computacional es necesaria. Indicadores:

- Los valores numericos especificos se vuelven necesarios para decision de diseno
- Trade-off studies requieren parametros cuantitativos
- El proceso fisico tiene una formula matematica subyacente (ej: V = V0 - (F/m)*t)

En este punto, el modelador DEBE convertir procesos conceptuales a procesos computacionales y usar la realizacion soportada por la herramienta. En OPCloud, la senal visual recuperable es el uso de `{}` en el OPD.

### 14.3 Simulacion Conceptual vs Ejecucion Computacional en OPCloud

El modelador DEBE distinguir entre:

- **Simulacion conceptual:** animacion visual del flujo de tokens para validar orden, precondiciones y cobertura del comportamiento
- **Ejecucion computacional:** corrida efectiva de formulas, atributos computacionales y actualizacion de valores

Reglas operativas:

- La velocidad de animacion DEBERIA ajustarse para hacer visibles procesos rapidos o loops
- Si el orden observado no coincide con el esperado, el modelador DEBE revisar altura relativa de subprocesos, links de control y condiciones
- Los tokens computacionales transportan valores; los conceptuales solo evidencian disponibilidad, consumo, creacion o cambio de estado

## 15 Invariantes

Los invariantes se verifican operativamente en §16, donde se organizan por nivel con severidad asignada.

| Invariante | Enforcement |
|-----------|-------------|
| Nombre del proceso principal termina en gerundio (EN) o se encabeza por infinitivo / `-ción` / `-miento` valido (ES) | lint |
| Todos los nombres de things son singulares | lint |
| Grupo beneficiario es objeto fisico | lint |
| Atributo del beneficiario es objeto informatical | lint |
| Exactamente un proceso principal por SD | schema |
| Agent links solo conectan a humanos (exclusividad) | manual |
| Instrument links solo conectan a no humanos | manual |
| Todo enabler persiste sin cambio neto tras el proceso | manual |
| Objetos environmentales tienen contorno dashed | lint |
| Sistema exhibe proceso principal via exhibition-characterization | manual |
| Consumption/result links NO en outer contour de proceso in-zoomed | lint |
| Todo subproceso conectado a al menos un transformee | lint |
| Modelo bimodal: todo OPD tiene paragrafo OPL equivalente | schema |
| Un hecho del modelo aparece en al menos un OPD | schema |
| Structural links son homogeneos (excepcion: exhibition-characterization) | lint |
| Enablers y affectees pertenecen a Pre(P) ∩ Post(P); consumees solo a Pre(P); resultees solo a Post(P) | manual |
| Probabilidades en fan XOR suman exactamente 1 | lint |
| Subprocesos paralelos tienen borde superior de elipse a la misma altura | manual |
| Split links control-modified NO estan permitidos | lint |
| Arquitectura del sistema produce al menos una capacidad emergente | manual |
| Links NO DEBEN cruzar areas ocupadas por things | manual |
| Things NO DEBEN ocultarse mutuamente (excepcion: port folding) | manual |
| Minimizar numero de links y cruces de links en cada OPD | manual |
| Si se usan requirements en OPCloud, la trazabilidad usa links estructurales y la convencion "satisfies" | manual |
| En OPCloud, procesos computacionales se distinguen visualmente con `{}` en el OPD | lint |
| Sinonimos resueltos: un thing = un nombre canonico | manual |

## 16 Checklist de Validacion

Todos los invariantes de §15 DEBEN verificarse en el nivel aplicable. Esta tabla lista checks operativos adicionales organizados por nivel.

| Nivel | Check | Condicion | Severidad |
|-------|-------|-----------|----------|
| SD | Sistema clasificado | Tipo determinado (artificial/natural/social/socio-tecnico) | CRITICA |
| SD | Purpose/outcome definido | Beneficiary + attribute + transicion estados | CRITICA |
| SD | Funcion definida | Main process + main transformee | CRITICA |
| SD | Enablers presentes | ≥1 agente o instrumento | ALTA |
| SD | Environment identificado | ≥1 objeto environmental | MEDIA |
| SD | Problem occurrence (si aplica) | Proceso environmental causa estado negativo | MEDIA |
| SD | Instrument reclassification | Instrumentos con desgaste relevante reclasificados a affectee | MEDIA |
| SD1 | Refinamiento correcto | Sync → in-zooming; async → unfolding | ALTA |
| SD1 | Sin event a no-primero | Event links no a subprocesos intermedios (o justificacion) | ALTA |
| SD1 | Split links resueltos | Ningun effect link underspecified en in-zoom multi-subprocess | ALTA |
| SD1 | Estados expresados | Estados relevantes visibles y conectados | ALTA |
| SD1 | Tipo async correcto | Aggregation para partes; generalization para tipos | ALTA |
| SD1 | Sin redundancia | Sin duplicacion innecesaria de hechos del SD | MEDIA |
| SD2+ | Precedencia links | Out-zooming aplica matriz de precedencia | ALTA |
| SD2+ | OPD tree valido | Etiquetado secuencial correcto | MEDIA |
| SD2+ | Role shift coherente | Instrument en abstract = affectee en detail solo si cambio neto = 0 | ALTA |
| Quant | Operandos explicitos | Operaciones no conmutativas con roles designados | MEDIA |
| Quant | Computational workflow | Atributos computacionales con tipo, alias y formula | MEDIA |
| Quant | Range validation | Rangos definidos para atributos con dominio acotado | MEDIA |
| Error | Exception handlers | Procesos con time bounds tienen overtime/undertime links | MEDIA |
| Error | Indeterminate resolution | Affectees en transicion resueltos por exception handler | MEDIA |
| Global | Claridad | Ningun OPD excede 20-25 entidades | MEDIA |
| Global | Inner/outer scoping | Objetos inner solo existen en scope de su proceso padre | MEDIA |
| Global | Name coherency | Sin nombres duplicados no resueltos | ALTA |
| Global | Ontology enforcement | Nivel configurado para organizacion (Suggest o Enforce) | MEDIA |
| Global | Model informativeness | Grading ejecutado; sin precedence links faltantes criticos | MEDIA |
| Global | System map | Generado para modelos con >10 OPDs | MEDIA |
| Global | Specification constructs | OPD + OPL + OPM spec completos en breadth-first order | MEDIA |
| Global | Port folding | Usado donde layout fisico de componentes es relevante | BAJA |
| Global | Implicit objects | Objetos implicitos en texto fuente identificados y modelados explicitamente | ALTA |
| Req | Trazabilidad estructural | Si se usan requirements en OPCloud, se ocupan links estructurales y convencion "satisfies" | MEDIA |
