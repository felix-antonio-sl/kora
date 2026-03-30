# Checklist de Auditoria OPM — Completo

Fuentes normativas: `urn:fxsl:kb:opm-iso-19450`, `urn:fxsl:kb:metodologia-modelamiento-opm`, `urn:fxsl:kb:opm-sd-wizard`.

Usar este checklist en Modo EVALUAR. Aplicar capa por capa.

---

## Capa 1 — Naming [ALTA]

| # | Check | Condicion de PASS | Fuente |
|---|-------|-------------------|--------|
| N1 | Proceso: gerundio (EN) | Nombre del proceso termina en "-ing" | ISO 19450 §SD Wizard Paso 1 |
| N2 | Proceso: infinitivo (ES) | Nombre del proceso termina en -ar/-er/-ir | OPL-ES §1.1 |
| N3 | Objetos: sustantivo singular | Sin plurales directos; usar Set/Conjunto o Group/Grupo | metodologia §2 |
| N4 | Estados: minusculas | Estado sin capitalizacion en palabras | ISO 19450 §3.68 |
| N5 | Max 4 palabras por thing | Nombre tiene ≤4 palabras lexicas | ISO 19450 §3 |
| N6 | Beneficiario: sufijo correcto | Humanos: Group/Grupo; Inanimados: Set/Conjunto | metodologia §6.2 |

---

## Capa 2 — Links Procedurales [CRITICA/ALTA]

| # | Check | Condicion de PASS | Severidad | Fuente |
|---|-------|-------------------|-----------|--------|
| L1 | Proceso con transforming link | Todo proceso tiene ≥1 (consumption/result/effect) | CRITICA | ISO 19450 §4.3 |
| L2 | Agent link solo en humanos | Ningun robot/software/IA con agent link | ALTA | metodologia §6.5 |
| L3 | Instrument link en no-humanos | Ningun humano con instrument link (salvo colision roles resuelta) | ALTA | metodologia §6.5 |
| L4 | Unicidad de rol | Un objeto tiene exactamente 1 rol por proceso | ALTA | ISO 19450 §procedural link uniqueness |
| L5 | Colision roles resuelta | Si agent+affectee del mismo proceso: transforming link prevalece | ALTA | metodologia §4.4 |
| L6 | Consumption/result en inner scope | Prohibidos en outer contour de proceso in-zoomed | CRITICA | metodologia §7.4 |
| L7 | State-specified correctos | Links a estado especifico arrancan del estado, no del objeto | ALTA | ISO 19450 §state-specified |
| L8 | Invocacion correcta | Invocation link tiene forma de zigzag; auto-invocacion = par de links | MEDIA | ISO 19450 §visual notation |

---

## Capa 3 — SD Completitud [CRITICA]

| # | Check | Condicion de PASS | Fuente |
|---|-------|-------------------|--------|
| S1 | Purpose definido | Beneficiary + beneficiary attribute + 2 estados + transicion | metodologia §6.11 |
| S2 | Funcion definida | Main process + main transformee presente | metodologia §6.3-6.4 |
| S3 | Enablers presentes | ≥1 agente o instrumento conectado al proceso principal | metodologia §6.11 |
| S4 | Beneficiary es objeto fisico | Grupo beneficiario representado como objeto fisico | metodologia §6.2 |
| S5 | Beneficiary attribute es informatical | Atributo del beneficiario es objeto informatical | metodologia §6.3 |
| S6 | Exhibition del sistema | Sistema exhibe proceso principal via exhibition-characterization | metodologia §6.6 |
| S7 | Problem occurrence (artificial/social) | Proceso ambiental causa estado negativo si sistema es artificial/social | metodologia §6.10 |
| S8 | Environment identificado | ≥1 objeto ambiental (contorno dashed) presente | metodologia §6.9 |
| S9 | Natural: sin problem occurrence | Si el sistema es natural, NO hay problem occurrence | metodologia §5 |
| S10 | Natural: sin agentes humanos | Si el sistema es natural, NO hay agent links — solo instruments | metodologia §5 |

---

## Capa 4 — Refinamiento SD1+ [MEDIA/ALTA]

| # | Check | Condicion de PASS | Fuente |
|---|-------|-------------------|--------|
| R1 | Subprocesos conectados a transformees | Cada subproceso tiene ≥1 transforming link | metodologia §4.3 |
| R2 | Timeline principle | Subprocesos ordenados top-to-bottom; paralelos a misma altura | metodologia §7.1 |
| R3 | Migracion de links | Consumption/result migrados de P a subprocesos al hacer in-zooming | metodologia §7.4 |
| R4 | Aggregation vs Generalization | Aggregation cuando todo necesita todas las partes; Generalization para variantes | metodologia §7.2 |
| R5 | Inner vs outer object scope | Objeto creado dentro de proceso in-zoomed = inner (scope del proceso) | metodologia §7.3 |
| R6 | State expression en SD1 | Estados que se suprimieron en SD expresados en SD1 donde se usan | metodologia §7.5 |
| R7 | Split state-specified correcto | Si P se in-zoomea: P1 saca del estado-entrada; P2 pone en estado-salida | metodologia §7.4 |

---

## Capa 5 — Relaciones Estructurales [MEDIA]

| # | Check | Condicion de PASS | Fuente |
|---|-------|-------------------|--------|
| E1 | Aggregation semantica | El todo requiere TODAS sus partes para funcionar | metodologia §7.2 |
| E2 | Generalization semantica | Especializaciones son variantes del mismo patron de transformacion | metodologia §7.2 |
| E3 | Exhibition correcta | Exhibition conecta exhibitor a sus features (atributos u operaciones) | ISO 19450 §3.20-3.21 |
| E4 | Classification correcta | La clase define el patron; instancias son realizaciones concretas | ISO 19450 §3.7-3.28 |
| E5 | Links estructurales entre cosas del mismo tipo | Objeto-objeto o proceso-proceso (excepto exhibition que puede cruzar) | ISO 19450 §structural links |

---

## Capa 6 — OPL [ALTA]

| # | Check | Condicion de PASS | Fuente |
|---|-------|-------------------|--------|
| O1 | OPL generado desde OPD | Sentencias OPL derivables del diagrama | ISO 19450 §bimodal |
| O2 | Equivalencia semantica | OPL y OPD expresan exactamente el mismo modelo | ISO 19450 §bimodal |
| O3 | Convenciones tipograficas | **Objeto** negrita, *Proceso* cursiva, `Estado` monoespaciado | OPL-ES §1.7 |
| O4 | Verbos correctos en ES | Usar tabla de verbos OPL-ES (ver opl-plantillas-es.md §vocabulario) | OPL-ES §2 |
| O5 | Estructura de sentencia | Orden canonico sujeto-verbo-complemento; no reordenar | OPL-ES §1.8 |
| O6 | Estado sigue al objeto en ES | "**Objeto** en `estado`" (no "`estado` **Objeto**" como en EN) | OPL-ES §1.9 |

---

## Resumen de Severidades

| Severidad | Descripcion | Impacto |
|-----------|-------------|---------|
| CRITICA | Viola la semántica fundamental de OPM | Modelo invalido — FAIL automatico |
| ALTA | Viola regla normativa explicita | Modelo incompleto o ambiguo — requiere correccion |
| MEDIA | Violacion de buena practica documentada | Modelo funcional pero mejorable |
| BAJA | Convencion de estilo o claridad | Recomendacion opcional |

**Criterio PASS**: cero hallazgos CRITICOS y cero hallazgos ALTOS sin resolver.
