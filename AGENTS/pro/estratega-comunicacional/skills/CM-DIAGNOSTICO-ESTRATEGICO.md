---
_manifest:
  urn: urn:pro:skill:estratega-diagnostico-estrategico:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Analizar la situacion comunicacional en 5 dimensiones para producir un diagnostico estructurado que habilite decisiones de narrativa, mensajes o piezas tacticas.

## Input/Output

- **Input:** Descripcion del proyecto, situacion o problema comunicacional del usuario.
- **Output:** DiagnosticoEstrategico { contexto, objetivos, stakeholders, gaps, riesgos }

## Procedimiento

1. **CONTEXTO** — Que esta pasando: situacion actual, historia relevante, momento del ciclo organizacional o de marca.
2. **OBJETIVOS** — Clasificar el objetivo comunicacional dominante: informar, persuadir, alinear, defender o posicionar.
3. **STAKEHOLDERS** — Mapear audiencias primarias, secundarias, hostiles y aliadas. Identificar intereses y expectativas de cada grupo.
4. **GAPS** — Identificar desconexion entre lo dicho y lo hecho o percibido. Contrastar narrativa oficial con realidad operativa.
5. **RIESGOS** — Evaluar riesgos reputacionales, de coherencia, de timing y de canal. Clasificar por probabilidad e impacto.
6. Presentar diagnostico estructurado con hallazgos por dimension. Preguntar que falta antes de avanzar.

## Signature Output

```
Diagnostico Estrategico:
CONTEXTO: <sintesis situacional>
OBJETIVOS: <clasificacion dominante>
STAKEHOLDERS: <mapa audiencias>
GAPS: <hallazgos coherencia>
RIESGOS: <evaluacion>
Siguiente paso recomendado: <narrativa | arquitectura | pieza tactica>
```
