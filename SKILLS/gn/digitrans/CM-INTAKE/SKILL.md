---
_manifest:
  urn: urn:gn:skill:digitrans-intake:2.0.0
  type: lazy_load_endofunctor
---

## Proposito
Clasificar cada consulta entrante de DIGITRANS por dominio TDE, nivel de profundidad y cierre solicitado.

## Input/Output
- **Input:** Consulta entrante sobre Transformacion Digital del Estado
- **Output:** Clasificacion estructurada: [Dominio TDE] + [Nivel de profundidad] + [Cierre solicitado?]

## Procedimiento
1. Identificar si la consulta cae en normativa, plataformas, estrategia o madurez/CPAT.
2. Determinar el nivel de profundidad requerido (basal, medio, profundo).
3. Detectar cuando la consulta exige distinguir norma vigente, dato institucional, interpretacion o incertidumbre.
4. Detectar si el mensaje expresa cierre del trabajo actual o cae fuera del dominio TDE.
5. Devolver una clasificacion semantica neutral, sin routing efectivo a estados del agente.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| dominio | enum(normativo\|plataformas\|estrategias\|cpat\|ambiguo\|fuera_scope) | Dominio TDE detectado |
| nivel_profundidad | enum(basal\|medio\|profundo) | Profundidad requerida por la consulta |
| etiquetas_requeridas | string[] | Labels que la respuesta debe distinguir |
| cierre_solicitado | bool | True si el mensaje indica cierre del trabajo actual |
