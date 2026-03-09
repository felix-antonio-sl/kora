---
_manifest:
  urn: urn:gn:skill:digitrans-intake:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-INTAKE

## Proposito
Clasificar cada consulta entrante de DIGITRANS por dominio TDE, nivel de profundidad y necesidad de puente evolutivo.

## Input/Output
- **Input:** Consulta entrante sobre Transformacion Digital del Estado
- **Output:** Clasificacion estructurada: [Dominio TDE] + [Nivel de profundidad] + [Necesita ORKO bridge?] + [Cierre solicitado?]

## Procedimiento
1. Identificar si la consulta cae en normativa, plataformas, estrategia/madurez o CPAT.
2. Determinar si la respuesta puede quedarse en marco TDE o requiere puente hacia ORKO y H_org.
3. Detectar cuando la consulta exige distinguir norma vigente, dato institucional, interpretacion o incertidumbre.
4. Detectar si el mensaje expresa cierre del trabajo actual o cae fuera del dominio TDE.
5. Devolver una clasificacion semantica neutral, sin routing efectivo a estados del agente.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| dominio | enum(normativo\|plataformas\|estrategias\|cpat\|ambiguo\|fuera_scope) | Dominio TDE detectado |
| nivel_profundidad | enum(basal\|medio\|profundo) | Profundidad requerida por la consulta |
| necesita_orko_bridge | bool | True si conviene activar el puente evolutivo |
| etiquetas_requeridas | string[] | Labels que la respuesta debe distinguir |
| cierre_solicitado | bool | True si el mensaje indica cierre del trabajo actual |
