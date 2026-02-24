---
_manifest:
  urn: "urn:fxsl:skill:planner-backlog-curator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-BACKLOG-CURATOR

## Proposito
Gestiona el backlog como flujo: prioriza, detecta bloqueos, recomienda siguiente historia, y en modo predictivo propone historias nuevas.

## Procedimiento (modo curado)
1. Listar todas las historias pendientes con sus 5 elementos.
2. Calcular prioridad para cada una: Valor / (Coste_Estimado × Multiplicador_Riesgo).
   - Multiplicador_Riesgo: lectura=1.0, escritura=1.5, destructiva=3.0.
   - Coste_Estimado: basado en complejidad (simple=1, estandar=2, complejo=4, critico=8).
3. Ordenar por prioridad descendente.
4. Verificar WIP limits por zona del codebase.
5. Identificar bloqueos: historias con dependencias no resueltas.
6. Recomendar siguiente historia para el coder: la de mayor prioridad sin bloqueos.
7. Presentar backlog como tabla priorizada.

## Procedimiento (modo predictivo)
1. Analizar OKRs activos: que KRs tienen bajo progreso.
2. Analizar historias completadas: que patrones emergen (areas del codebase mas tocadas, tipos de historia mas frecuentes).
3. Analizar metricas de producto si disponibles: que usan los usuarios, donde hay friccion.
4. Proponer 3-5 historias borrador que acerquen los KRs a sus targets.
5. Marcar cada propuesta con confianza (alta|media|baja) y justificacion.
6. Presentar al PO como BORRADORES para curado. NO son decisiones tomadas.

## Output
Modo curado: tabla {posicion, historia, valor, coste, riesgo, prioridad, estado}. Modo predictivo: tabla {propuesta, justificacion, confianza, kr_asociado}.
