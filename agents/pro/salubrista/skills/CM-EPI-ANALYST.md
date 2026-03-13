---
_manifest:
  urn: urn:pro:skill:salubrista-epi-analyst:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-EPI-ANALYST

## Proposito
Conducir analisis epidemiologico y poblacional aplicado a decisiones sanitarias. Convierte datos, perfiles de riesgo, tendencias e inequidades en inteligencia accionable para gestion, diseno, implementacion o vigilancia, sin trasladar el analisis a diagnostico clinico individual.

## Input/Output
- **Input:** problema: string, escala: string, datos: object
- **Output:** EpiAnalysis { pregunta_analitica, indicadores_priorizados: string[], hallazgos: string[], riesgos: string[], implicancias_sistema: string[], incertidumbre_residual: string, vigilancia_requerida: bool }

## Procedimiento
1. KB_FIRST: resolver `kb_route` para el tema epidemiologico o de razonamiento sanitario integrado y recuperar el contenido pertinente con `knowledge_retrieval` antes de razonar con el modelo.
2. DEFINIR la pregunta analitica: descriptiva / comparativa / estratificacion de riesgo / brote / inequidad / carga de enfermedad / escenario.
3. FIJAR la unidad de analisis: poblacion, cohorte, territorio, establecimiento, red, programa o grupo vulnerable.
4. PRIORIZAR indicadores utiles para la decision:
   - frecuencia, tasas, tendencias, letalidad, uso de servicios, cobertura, brechas, estratificacion, distribucion territorial
5. ANALIZAR el problema:
   - tendencias temporales
   - comparaciones entre grupos o territorios
   - riesgos y vulnerabilidades
   - brechas de acceso, oportunidad o continuidad
   - factores del sistema que amplifican el dano poblacional
6. SI la pregunta es causal o de evaluacion de impacto:
   - identificar exposicion, outcome, posibles confusores y limites inferenciales
   - declarar la fuerza de evidencia y la incertidumbre
7. SI hay evento agudo, brote o senal relevante:
   - marcar `vigilancia_requerida = true`
   - separar claramente lo que corresponde a vigilancia formal
8. TRADUCIR hallazgos en implicancias para el sistema:
   - priorizacion
   - reasignacion de recursos
   - necesidades de diseno o rediseño
   - necesidades de implementacion o seguimiento
9. OUTPUT: pregunta analitica, indicadores priorizados, hallazgos, riesgos, implicancias para el sistema e incertidumbre residual.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| pregunta_analitica | string | Tipo de pregunta epidemiologica dominante |
| indicadores_priorizados | string[] | Indicadores clave para la decision |
| hallazgos | string[] | Hallazgos principales |
| riesgos | string[] | Riesgos o grupos vulnerables identificados |
| implicancias_sistema | string[] | Consecuencias para gestion, diseno o implementacion |
| incertidumbre_residual | string | Limites de dato o inferencia |
| vigilancia_requerida | bool | True si requiere activacion de vigilancia |
