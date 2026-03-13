---
_manifest:
  urn: urn:pro:skill:salubrista-quality-auditor:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-QUALITY-AUDITOR

## Proposito
Evaluar desempeno, calidad y mejora continua de unidades, establecimientos, programas o redes sanitarias. Ordena evidencia, hallazgos, KPIs y acciones de mejora para que el medico salubrista humano pueda decidir rediseños o planes de implementacion con base trazable.

## Input/Output
- **Input:** mode: "evaluation"|"audit", alcance: string, datos: object
- **Output:** EvaluationReport { alcance, criterios_evaluacion: string[], hallazgos: string[], plan_mejora: string[], kpis_seguimiento: string[], trazabilidad_normativa: string[] }

## Procedimiento
1. DEFINIR alcance y escala del ejercicio: unidad, establecimiento, red, programa o territorio.
2. RESOLVER `kb_route` hacia gestion-redes general y, si aplica, herramientas o corpus especifico del dominio evaluado. Recuperar baseline con `knowledge_retrieval`.
3. FIJAR criterios de evaluacion:
   - efectividad
   - eficiencia
   - calidad y seguridad
   - equidad
   - oportunidad
   - experiencia usuaria
   - sostenibilidad
4. ORGANIZAR la evidencia:
   - estructura, proceso y resultado
   - indicadores existentes y faltantes
   - brechas de dato o trazabilidad
5. IDENTIFICAR hallazgos:
   - fortalezas
   - brechas
   - riesgos
   - desviaciones respecto al objetivo sanitario u operativo
6. CLASIFICAR implicancias:
   - requiere rediseño
   - requiere implementacion/cambio
   - requiere seguimiento adicional
7. CONSTRUIR plan de mejora:
   - accion
   - responsable
   - plazo
   - indicador de seguimiento
8. OUTPUT: criterios, hallazgos, plan de mejora, KPIs y trazabilidad.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| alcance | string | Objeto evaluado |
| criterios_evaluacion | string[] | Dimensiones de evaluacion usadas |
| hallazgos | string[] | Hallazgos principales |
| plan_mejora | string[] | Acciones priorizadas |
| kpis_seguimiento | string[] | Indicadores de seguimiento |
| trazabilidad_normativa | string[] | Normas o guias citadas |
| resumen_ejecutivo | string | Sintesis para decision |
