---
_manifest:
  urn: urn:pro:skill:salubrista-hah-quality-auditor:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-QUALITY-AUDITOR

## Proposito
Evaluar desempeno, calidad y mejora continua de sistemas de hospitalizacion integrados, incluyendo hospital y HD. Organiza hallazgos, KPIs y acciones de mejora para capacidad, seguridad, continuidad del cuidado y eficiencia del continuo asistencial.

## Input/Output
- **Input:** mode: "evaluation"|"audit", alcance: string, datos: object
- **Output:** EvaluationReport { alcance, criterios_evaluacion: string[], hallazgos: string[], plan_mejora: string[], kpis_seguimiento: string[], trazabilidad_normativa: string[] }

## Procedimiento
1. DEFINIR alcance y escala: unidad, establecimiento, red, programa HD o trayectoria hospital-domicilio.
2. KB_FIRST: resolver `kb_route` hacia gestion-redes y, si aplica, sumar corpus HaH pertinente. Recuperar baseline con `knowledge_retrieval`.
3. FIJAR criterios de evaluacion:
   - seguridad
   - oportunidad
   - eficiencia
   - continuidad del cuidado
   - experiencia usuaria y del cuidador
   - equidad
   - sostenibilidad
4. ORGANIZAR evidencia:
   - ocupacion, estada, rotacion, altas demoradas, reingresos, rescates, eventos adversos, IAAS, trazabilidad
5. IDENTIFICAR hallazgos:
   - fortalezas
   - cuellos de botella
   - fallas de transicion
   - brechas de capacidad o coordinacion
   - brechas normativas en HD si aplica
6. CLASIFICAR implicancias:
   - requiere rediseño
   - requiere implementacion de mejoras
   - requiere seguimiento adicional
7. CONSTRUIR plan de mejora:
   - accion
   - responsable
   - plazo
   - indicador
8. OUTPUT: criterios, hallazgos, plan de mejora, KPIs y trazabilidad.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| alcance | string | Objeto evaluado |
| criterios_evaluacion | string[] | Dimensiones usadas |
| hallazgos | string[] | Hallazgos principales |
| plan_mejora | string[] | Acciones priorizadas |
| kpis_seguimiento | string[] | Indicadores de seguimiento |
| trazabilidad_normativa | string[] | Normas o guias citadas |
| resumen_ejecutivo | string | Sintesis para decision |
